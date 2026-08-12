---
title: "DaBootZone Breaking the DA1469x BootROM"
speakers: ["Chris Bellows"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Chris Bellows_DaBootZone Breaking the DA1469x BootROM.pdf"
pages: 44
sha256: "d18637a0a968e88a7b87ee2cae190d4482c751e0275e830dac9d55329585265f"
text_chars: 28074
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.4
ocr_unreliable_blocks: 7
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:12:33Z"
---
# DaBootZone Breaking the DA1469x BootROM

**Speakers:** Chris Bellows  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Chris Bellows_DaBootZone Breaking the DA1469x BootROM.pdf` (44 pages)


## Slide 1

### **DABOOTZONE**

###### **BREAKING THE DA1469X BOOTROM**

## Slide 2

## **WHOAMI**

##### **Chris Bellows Research Science Director @ Atredis Partners Owl Illustrator**

https://www.atredis.com

2


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHOAMI
Chris Bellows
Research Science Director @ Atredis Partners
Owl Illustrator
How to draw an owl
S TREDIS PARTNERS ones
1. Draw some circles 2. Draw the rest of the owl https: //www.atredis.com
```

## Slide 3

## **WHAT THIS IS ABOUT**

Bizdev Research Consulting


> Recovered by OCR — confidence 94/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT THIS IS ABOUT
Car Salesman: “slaps roof of car" let's see if this bad boy will
fit all the stuff you need
```

## Slide 4

## **DA1469X**

##### **Renesas Da1469x microcontrollers**

- <sup>**DA14691**</sup>

- <sup>**DA14695**</sup>

- <sup>**DA14697**</sup>

- <sup>**DA14699**</sup>

**Arm Cortex-M33, Bluetooth LE,PMU,Clocks,Crypto,blah,blah Security features**

   - <sup>**Secure Access - debug interface controls**</sup>

   - <sup>**Secureboot - firmware validation**</sup>

- <sup>**Encrypted Firmware - on-the-fly decryption of firmware**</sup>

- **Development Board available, fairly inexpensive ~100$**

## Slide 5

**THE IMPORTANT STUFF. SECURITY FEATURES**

**One-Time-Programmable (OTP) Segment Configuration Script controls settings**

   - **•Dev/Prod Modes**

   - **•Secure Boot**

- **Encryption Keys Provisioned here:**

   - **•QSPI FW Keys - on-the-fly fw decryption**

   - **•User Data Keys - application keys**

**•Public Keys - secure boot authentication**

## Slide 6

## **ENCRYPTION AT REST**

**Defensible external storage of user applications? Encryption! •Keys loaded into OTP (QSPI Area)**

**•Application encrypted with provisioned key**

**•HW Engine decrypts application as its executed**

**•AES-CTR Mode**

**•Allows decryption of arbitrary blocks**

**• Performance / Execute-In-Place (XIP)**

## Slide 7

## **SECURE BOOT**

**Validates the application against public key stored in OTP Once activated the following is enforced:**

**•Cannot be disabled**

**•Applications must be signed**

**•Applications must be encrypted**

**•OTP Key section read disabled**

**•Keys can be revoked**

## Slide 8

## **BOOTROM**

##### **Small code block executed first**

**• Initializes the system**

**• Handles transition to application/customer code**

**• Immutable (some exceptions)**

**• Manufacturer only “patch” section**

**• Focused-ion-beam (FIB)**

##### **Security Implemented Here**

**• Secureboot**

- **OTP**

**• Debug/Readback protections Notable bug examples**

**• iPhone bugs (limera1n/checkm8)**

## Slide 9

## **EXTRACTION**

**Datasheet provides the memory mappings Debugger/JLink to read to a file Load into IDA Draw the rest of the owl**


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
EXTRACTION
Datasheet provides the memory mappings
Debugger/JLink to read to a file
Load into IDA
Draw the rest of the owl
8 Library function J Regular function
Instruction Oo Data Unexplored {J External symbol
Functions
Function name
Booter_Flow
CLK_Enable_RC32M
CLK_Set_source_xtal32m
CLK_Switch_to_RC32M
CLK_Switch_to_XTAL32M
CRC_get_crc16_ccitt
CRYPTO_is_processing_data
CRYPTO_setup_data_and_st...
CRYPTO_setup_data_locatio...
CRYPTO_waiting_for_input
CRYPT_process_last_block
Cache_setup_qspi_cache
ConfigurationScript_Read
ConfigurationScript_Read_O...
ConfigurationScript_Read_Q...
Crypto_Validate_EdDSA
Crypto_hash_sha512_setup
Crypto_setup_sha512_start...
DeviceAdministration_KeyTy...
ImageHeader_version_check
NVIC_ICERO_clear_b16
a | Start
000015E8
0000155C
0000159C
00000344
00000384
0000146C
000014FC
00005D98
000014B8
00001520
00005E34
00001ADC
00000228
000001E0
00002026
00000C94
0000250C
IDA View-A
CLK_Enable_RC32M();
CRG_TOP_CLK_AMBA_REG[@] = 0;
SYS_WDOG_WATCHDOG_CTRL_REG = 6;
v@ = CRG_TOP_PMU_CTRL_REG;
CRG_TOP_PMU_CTRL_REG = v@ & OxFFFFFFF7;
do
ptr_sys_stat_reg = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg & 0x80) == @ );
GPIO_P@_@8_MODE_REG = 0x200;
GPIO_P@_@8_MODE_REG = 0x100;
GPIO_P@_@8_MODE_REG = 0x200;
WDOG_feed_ff();
ptr_pmu_ctrl_reg = CRG_TOP_PMU_CTRL_REG;
CRG_TOP_PMU_CTRL_REG = ptr_pmu_ctrl_reg & @xFFFFFFFB;
do
ptr_sys_stat_reg_ = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg_ & 0x200) == @ );
ptr_power_ctrl_reg = CRG_TOP_POWER_CTRL_REG;
CRG_TOP_POWER_CTRL_REG = ptr_power_ctrl_reg & OxFF8FFFFF
CRG_TOP_POWER_CTRL_REG = ptr_power_ctrl_reg & OxFF8FFF7F
ptr_pmu_ctrl_reg_ = CRG_TOP_PMU_CTRL_REG;
CRG_TOP_PMU_CTRL_REG = ptr_pmu_ctrl_reg_ & OxFFFFFFFE;
do
ptr_sys_stat_reg__ = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg_ & 8) == @ );
OTPC_set_read_mode() ;
QSPIC_Software_Reset_peripheral();
Remapped at 0x0.
DA14691 end address:
SYSRAM (code) 800000 880000 0x860000
Reserved
Opening binary file for writing... [c:\users\chris\bootrom. bin]
Reading 131072 bytes from addr @x@@90@008 into file...0.K.
8 Library function J) Regular function Instruction J Data Unexplored [J External symbol [J Lumina fun
Functions Pseudocode-A
v@ = sub_155C();
= 6:
while ( ( 2 & 0x800)
sub_ 15E8 000015E8
sub_18AC 000018AC
sub_195C 0000195C
sub_1ADC 00001ADC
sub_1C00 00001C00
sub_1C6C 00001C6C
sub_1CAC 00001CAC
sub_1DAC 00001DAC
sub_1DE8 00001DE8
sub_1E20 00001E20
sub_1EC4 00001EC4
sub_1EEO 00001EEO
sub_1EF4 00001EF4
sub_1F08 00001F08
sub_1F46 00001F46
00001FA2
EMOR ~4u;
while ( ( & 0x200) @)
( & OxFF8FFFFF | 0x400000;
sub_1CAC(1);
sub_1DAC() ;
sub_2052();
sub_ 20B6(v1);
|
v2 = sub -264C(0x110 6
```

## Slide 10

## **ANALYSIS CHALLENGES**

##### **Dense code**

- **•No strings**

- **•No symbols**

- **•No debug statements/printf-like functions**

**•No external libraries**

🫠

## Slide 11

## **LET THE HW GUIDE YOU**

###### **Datasheet Provides Addresses**

**IDA Segments**

- <sup>**Create manually/IDAPython**</sup>

- <sup>**SVD Loader (Edit>Plugins>SVD File Management)**</sup> **•**<sup>**SDK_10.0.12.146.1/config/embsys/Dialog_Semiconductor/DA1469x-00.xml**</sup>

## Slide 12

## **BACKWARDS IS FORWARD**

##### **Register access defines functionality**

Function Folders


> Recovered by OCR — confidence 80/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BACKWARDS IS FORWARD
Register access defines functionality
UART: 5802000C UART_UART_LCR_REG 5 4
; RW: Line Control Register
int _fastcall sub_264C(int result) int __fastcall UART_reset_and_configure_uart(int result)
{ {
int vir f/ ra int v1; // r3
UART_UART_SRR_REG = 7; UART_UART_SRR_REG = 7;
= v1 = UART_UART_LCR_REG;
vi = UART_UART_LCR_REG: - ;
UART_UART_DLF_REG = (unsigned _ int8)result; ART UART DLE REG = Fesulle:
UART_UART_ITER_DLH_REG = BYTE2(result); UART_UART_IER_DLH_REG = BYTE2(result) ;
_UART_IIR_FCR_ ; UART_UART_IIR_FCR_REG = 7;
UART_UART IER DLH_REG = BYTE2(result) & OxFE; UART_UART_IER_DLH_REG = BYTE2(result) & OxFE;
return result; return result;
Wa Functions Functions
Function name {Segment | Start | Length
Fu n ct io n Fo | d e rs FA sub_BE2 Code 00000BE2 0000005C
sub_2A9E Reset natiral ortier i fi NM\_handler 000024D0 00000002
sub_D78 Rename h Fi SVCall_handler 000024D2 00000002
Function name |Segment | Start | Length « | Locals
```

## Slide 13

## **UNICORNS**

**https://www.unicorn-engine.org/**


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
UNICORNS
% python booter.py secure_img.bin
invalid register name CYCLECNT, skipping def load_jlink_reg_str(mu, raw_str):
invalid reg config value: XPSR - 69000000:APSR mon
peyote meg contig vane Ti eee RoEXeee to) loads a raw string from a jlink session of the register state. example:
invalid register name CFBP, skipping
invalid register name MSPLIM, skipping PC = 000015E8, CycleCnt = 000011CE
invalid register name PSPLIM, skipping R®@ = 00000000, R1 = 00000000, R2 = 00000002, R3 = 00000000
[-] Tracing basic block at Entry - Booter_Flow (@x15e8) - LR Qx1b6 - block size = Qx R4 = 00000000, R5 = 00000000, R6 = 00000000, R7 = 20000000
[-] Tracing basic block at Entry - CLK_Enable_RC32M (Qx155c) - LR @xi5ee - block siz R8 = 22F03812, R9 = 54020200, R10= 20030000, R11= 00000000
[+] Read: CRG_TOP + 0x@044 (4 bytes) R12= 18846521
[+] Read: CRG_TOP + @x0@014 (4 bytes) - = =
[+] Read: CRG_TOP + 0x0014 (4 bytes) SP(R13)= 20040000, MSP= 20040000, PSP= 00000000, R14(LR
[+] Read: CRG_TOP + @x@020 (4 bytes)
[+] Read: CRG_TOP + @x0028 (4 bytes) CFBP = 00000000, CONTROL = 00, FAULTMASK = 00, BASEPRI = @@, PRIMASK = 00
[-] Tracing basic block at Entry - WDOG_feed_ff (@x1544) - LR @x1638 - block size = MSPLIM = 00000000
+ = 000001BB
+
4
+
[+] Read: CRG_TOP + @x0020 (4 bytes) PSPLIM = 00000000
+
+
+
+
+
)
XPSR = 69000000: APSR = nZCvQ, EPSR = 01000000, IPSR = @0@ (NoException)
[+] Read: CRG_TOP + @x@028 (4 bytes) tna
[+] Read: CRG_TOP + @x00f@ (4 bytes)
[+] Read: CRG_TOP + @x@0f®@ (4 bytes)
[+] Read: CRG_TOP + @x@020 (4 bytes)
[+] Read: CRG_TOP + @x@028 (4 bytes)
[-] Tracing basic block at Entry - OTPC_enable_clock_and_reset (@x1cac) mu.mmio_map 0x50000000, crg_top_read, None, crg_top_write, None)
[+] Read: CRG_TOP + @x@0@0 (4 bytes) . . 5 .
[-] Tracing basic block at Entry - OTPC_set_read_mode (@xidac) - LR Qx1 mu.mm1o_map ®x50010000, periph2_read, None, periph2_write, None)
[-] Tracing basic block at Entry - QSPIC_set_manual_mode (@x2052) - LR mu.mmio_map(0x50020000, periph_read, None, periph_write, None)
Read: CRG_TOP + @x0000 (4 byt 5 ‘ ; .
Read: CRG_TOP + @x0020 (4 bytes) mu.mmio_map(@x30070000, Otp.mmio_read, otp, Otp.mmio_write, otp)
Tracing basic block at Entry - QSPIC_Software_Reset_peripheral (Q@x2| mu.mmio_map 0x38000000, Qspi.mmio_read, qspl, Qspi.mmio_write, qspi)
Tracing basic block at Entry - QSPIC_Enable_CS_active_low (@x1leeQ@) mu.mmio map ®x10080000, Otp.mem read, otp, Otp.mem write, otp)
Tracing basic block at Entry - QSPIC_Disable_CS_active_low (@xlef4) = _ =
Tracing basic block at Entry - QSPIC_Enable_CS_active_low (@xlee@) - LR Qx2192 - block size = Qx14
Tracing basic block at Entry - QSPIC_WriteData_manual_mode (Qx2460) - LR @x2198 - block size = 0x20
I: Release Power-down / Device ID
Tracing basic block at Entry - QSPIC_Disable_CS_active_low (Qxlef4) - LR @x219c - block size = 0x14
Tracing basic block at Entry - QSPIC_Enable_CS_active_low (@xlee@) - LR Qx21ba - block size = 0x14
Tracing basic block at Entry - QSPIC_WriteData_manual_mode (Qx2460) - LR @x21c@ - block size = Qx20
regs = raw_str.strip().replace('\n',',').replace(' ','').split(',')
```

## Slide 14

## **AIDAPAL PLUG**

##### **Manual Analysis**

##### **Aidapal Analysis**

**https://github.com/atredispartners/aidapal**


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AIDAPAL PLUG
Manual Analysis
int
__fastcall UART_reset_and_configure_uart(int result)
int v1; // r3
UART_UART_SRR_REG = 7;
v1 = UART_UART_LCR_REG;
UART_UART_LCR_REG = v1 | 0x80;
UART_UART_DLF_REG = result;
UART_UART_RBR_THR_DLL_REG = BYTE1(result) ;
UART_UART_IER_DLH_| A = BYTE2(result);
UART_UART_LCR_REG =
UART_UART_IER_DLH_REG
return result;
7;
BYTE2(result) & OxFE;
Aidapal Analysis
int _ fastcall configureUartRegisters_264c(int inputValue)
int previousLerValue; // r3
UART_UART_SRR_REG = 7;
previousLerValue = UART_UART_LCR_REG;
UART_UART_LCR_REG previousLerValue | 8x80;
UART_UART_DLF_REG = inputValue;
UART_UART_RBR_THR_DLL_ REG = BYTE1(inputValue) ;
UART_UART_IER_DLH_REG = = BYTE2(inputValue) ;
UART_UART_LCR_REG = 3;
UART_UART_IER_DLH_REG
return inputValue;
BYTE2(inputValue) & OxFE;
int _ fastcall sub _264C(int result) OT
{ AIDAPAL
int v1; // 73
UART_UART_SRR_REG = 7;
V1 = UART_UART_LCR_REG;
UART_UART_LCR_REG = vi | @x8@;
UART_UART_DLF_REG = (unsigned __int8)result;
UART_UART_RBR_THR_DLL_REG = BYTE1(result);
UART_UART_IER_DLH_REG = BYTE2(result);
UART_UART_LCR_REG = 3;
UART_UART_IER_DLH_REG
return result;
BYTE2(result) & @xFE;
@80026A6 sub_264C:14 (26A6) (Synchronized with IDA View-A, IDA View-B)
&& aiDAPal Results
aiDAPal Function Name
aiDAPal Comment
This function configures various UART registers with the provided input value. It
sets specific bits in the Software Reset Register, Line Control Register, Divisor
~ Latch Fraction Register, Receive Buffer Register Threshold, Interrupt Enable
Register, and Interrupt Identification Register/FIFO Control Register based on the
input value.
aiDAPal Variables
~¥ result inputValue “vi previousLerValue
Accept
Cancel
https://github.com/atredispartners/aidapal
```

## Slide 15

## **NAVIGATION SYSTEM**

REN_da1469x_3v3_DST_20220421.pdf


> Recovered by OCR — confidence 77/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NAVIGATION SYSTEM
bootrom
Start LDO_Radio &
power domains
~ Init OTP & Flash and Reset Set UART Baudrate@
8 Flash —> Dev.ModeFlag=True —> XTAL_ok Flag = False 115k2 & Pxx/Pyy
2
£
2
a
i Locate and Run CS Enable XTAL XTAL settled in ves—y! xTAL_ok Flag = True
£
=
Oo ‘NO:
c
v
NOK =
Dev. mode Flag? >—TRUE Enable Debugger ——> XTAL_ok Flag —No—> Get FW From UART
True?
FALSE i Switch to RC32M |
| - { —_ Switch to XTAL32M -——~
3 Locate FLASH_Prod Header << NO: FW loaded?
8
2
sub_1544(v@);
v3 = CRG_TOP_PMU_CTRL_REG;
CRG_TOP_PMU_CTRL_REG = v3 & @xFFFFFFFB;
do
v4 = CRG_TOP_SYS_STAT_REG;
while ( (v4 & @x200) = @ J;
v5. = CRG_TOP_POWER_CTRL_REG;
CRG TOP. POWER_CTRL_REG = v5 & @xFFSFFFFF | @x490000;
CRG_TOP_POWER_CTRL_REG = v5 & @xFFEFFFI7F | @x4ee0e8a;
CRG_TOP_PMU_CTRL_REG = v6 & OxFFFFFFFE;
do
v7 = CRG_TOP_SYS_STAT_REG;
v8 = sub_1CACc(1);
w9 = sub_1DAC(va);
v1@ = sub_2052(v9);
byte_2883C954 = i;
vil = CRG_COM_CLK_COM_REG;
CRG_COM_CLK COM REG = v11_/ 1:
GPIO_P@_89 MODE REG PA
GPIO_P@_@8 MODE REG = 1
sub_1544(v12);
v13 = CRG_TOP_CLK_CTRL_REG:
vl4 = CRG_XTAL_XTAL32M_CTRL1_REG;
CAG_XTAL_XTAL32M_CTAL1_REG = vid | &
```

## Slide 16


> Recovered by OCR — confidence 76/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Start LDO_Radio &
3
8
&
8
FALSE
|
| Locate_FLASH_Prod_Header
oK
power domains
§
= Init OTP & Flash and Reset Set UART Baudrate@
2
& y
5
2
8 NO
5
2
Y
Dev. mode Flag? >—TRUED Enable Debugger —P>-< ™TAL-OKFI9B= nop! | Get FW From UART
ves
Switch to RC32M
Switch to XTAL32M.
FW loaded?
Device administration
Upgrade
Pending
YES
FW Validation
Update image
|
FW Validation
Current Executable Image
NOK
Reject Upgrade +> Trigger HW_Reset(); > END
Device Administration
‘Check Administration Data and
Perform Key revocation
—
Accept Image
OK-
Load Image
Setup QSPI /
Decrypt on the Fly
T
NOK
v
Configure Cache Remap QSPI
| ‘Address RAM)
Trigger HW_Reset();
> END
SYS_WDOG_WATCHDOG_CTRL_REG = 6
ptr_sys_stat_reg = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg & @x8i a)
ptr_pmu_ctrl_reg = CRG_TOP_PMU_CTRL_REG;
ptr_sys_stat_reg_ = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg_ & 0x200) =
ptr_power_ctrl_reg = CRG_TOP_POWER_CTRL_REG;
ptr_pmu_ctrl_reg_ = CRG_TOP_PMU_CTRL_REG;
CRG_TOP_PMU_CTRL_REG = ptr_pmu_ctrl_reg_ & OxFFFFFFFE
ptr_sys_stat_reg_ = CRG_TOP_SYS_STAT_REG;
while ( (ptr_sys_stat_reg_ & 8) =e )
OTPC_enable_clock_and_reset(1);
OTPC_set_read_mode();
LoBYTE(configuration_script) = 1;
dword_2003C958 = 0;
CRG_COM_CLK_COM_REG = ptr_clk_com_reg |
GPIO_P0_09_MODE_REG
ConfigurationScript_Read ( (struct_configuration_script_ptr +)éconfiguration_script) ;
cUk_ctrl_reg = CRG_TOP_CLK_CTRL_REG:
T (elketri_reg & 0x4000)
ptr_xtal32_ctrll_reg = CRG_XTAL_XTAL32M_CTRL1_REG
BYTEL(xtal32m_ready_flag) = 0;
while ( (unsigned _int#)xtal32m_ready_flag
ptr_xtal32_stat_reg = CRG_XTAL_XTAL32H_STAT1_REG;
breaks
>
while ( (unsigned __int8)xtal32m_ready_flag
if ( (unsigned __int8)xtal32m_ready flag !=
BYTEL (xtal32m_ready_flag) = 1;
while ( (unsigned _int8)xtal32m_ready_flag
ptr_xtal32_ctrl0_reg = CRG_XTAL_XTAL32M_CTRLO_REG;
f ( (BYTE) configuration_script )
ptr_Sys_ctrl_reg = CRG_TOP_SYS_CTRL_REG;
CRG_TOP_SYS_CTRL_REG = ptr_sys_ctrl_reg | @x80;
get_fw_ack = UART_Get_FW( (int)Sconfiguration_script);
white ( BYTEL(configurationscript) != 1);
(check_current_fw_addr_and_update_addr(product_img_offsets) )
(int) product_ing_offsets,
(struct_configuration_script_ptr *)&configuration_script) )
(int) product_ing_of fsets,
(struct_configuration_script_ptr *)&configuration_script
>
Sub_AGE( (struct_configuration_script_ptr *)Sconfiguration_script, product_ing_offsets);
(struct_configuration_script_ptr *)Sconfiguration_script,
product_ing offsets) )
Wo06_Pet_1c341) ;
Cache_setup_qspi_cache(dword_2003C950, product_ing_ offsets);
return RESET_to_REMAP_ADR_val(2u)
```

## Slide 17

**Firmware Image**

## **BUGS**

##### **Secureboot pain point - writable areas Flash format defines these**

##### **SIGNED**

**ENCRYPTED**

## Slide 18

## **PRODUCT HEADER VALIDATION**

Check Primary Product  Extract Primary Product
Valid
Header CRC Firmware Image Address
Check Backup Product  Return to Firmware Image
Header CRC Address to Boot Flow
Write Backup Product
Valid Return to Boot Flow and fail
Header to Primary Location
Seems ok.

## Slide 19

## **PRODUCT HEADER** **~~VALIDATION~~**

**Nope.**

**backup_product_header_buff[258] - fixed length value product_header_length - user controlled 2-byte value in the Product Header (Length of Flash Config Section)**

**This one was trying its very best to be useful**

## Slide 20

✅ **PRODUCT HEADER VALIDATION**


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
is_valid = QSPI_read_header_check_crc(configuration_script_ptr—>flash_header_ptr, product_header_length) ;// _$
if ( is_valid !=1) // if the first Flash Product Header CRC check fails, check the next at offset 0x1000 in QSPI
QSPI_Cycle_CS(); // begin process to check backup Flash Product Header
// read the flash config length from the next header in QSPI (@x100@ + 0x14)
QSPI_Send_Read_Request(3, configuration_script_ptr-—>flash_header_ptr + @x1014);
QSPI_Get_Read_Result((char *)&flash_cfg_len, 2u);
QSPI_reset();
product_header_length = flash_cfg_len + @x16;// calculate the entire length for the CRC check
// check the second Flash Product Header (@x1000) CRC against the stored CRC value
is_valid = QSPI_read_header_check_crc(configuration_script_ptr->flash_header_ptr + 0x1000,flash_cfg_Len + @x16);// <-—f LARGE VALID HEADER
// if the second Flash Product Header CRC fails, indicate as such and return to calle!
// at this point the first header has failed CRC and the second has passed
// check the first Flash Product Header (@x@) calculated CRC against the value stored in the Flash Product Header
// read the backup buffer and write it to the primary location
QSPI_Cycle_CS();
// initiate a QSPI read at the start of the backup Flash Product Header (@x1000)
QSPI_Send_Read_Request(3, configuration_script_ptr->flash_header_ptr + 0x1000);
// read the entire backup header, including the stored CRC at the end . wr
QSPI_Get_Read_Result(backup_product_header_buff, product_header_length + 2); // I AM THE APP NOWgamk
QSPI_reset();
QSPI_Cycle_CS();
QSPI_sector_erase(configuration_script_ptr-—>flash_header_ptr);// erase the primary product header at @x@
```

## Slide 21

**Example Infinite Loop Payload**

##### **Invalid Primary Header**

##### **Infinite Loop Payload**

**Stack Pivot Address Backup CRC Pre-Computed CRC**

## Slide 22

##### **Before Overflow**

##### **After Overflow**

**O riginal Return**

**Payload Return**


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
J-Link>setbp @xi@82 <--- vulnerable call CPU is halted (PC = 0x00000082) .
J-Link>regs
Breakpoint set @ addr 0x@@001082 (Handle = 2)9M oc ~ oooo1082, cyclecnt = O0EAAFBE
J-Link>go RO = 2003FEDC, R1 = (@OO03049, R2 = 00003149, R3 = 2003FEDC
R4 = 00000000, R5 = 00000000, R6 = 00000000, R7 = 2003FEDO
R8 = 9220C050, RO = D@8C1@6E, R10= 20030000, R11= 00000000
R12= ABAQ8801
SP(R13)= 2003FED@, MSP= 2003FED0, PSP= 00000000, R14(LR) = 00001F3F
Before Overflow After Overflow
2003FED@ = 2003C944 2003C954 4EE54BA6 33333131
2003FEE® = 33333131 33333131 33333131 33333131
20@3FEF®@ = 33333131 33333131 33333131 33333131
2003FFQ0 = 33333131 33333131 33333131 33333131
2003FF10 = 33333131 33333131 33333131 33333131
2003FF20 = 33333131 33333131 33333131 33333131
2003FF30 = 33333131 33333131 33333131 33333131
2003FF40 = 33333131 33333131 33333131 33333131
2003FF5@ = 33333131 33333131 33333131 33333131
2003FF60 = 33333131 33333131 33333131 33333131
2003FF70 = 33333131 33333131 33333131 10333131
2003FF8@ = 33333131 2003FF88 2003FFBO0 FFFFFFB8
2003FF9@ = 00000001 EQ00E100 00010000 00000001
2003FFA@ = ABAQ8801 000025DB @00026BE 29000000
2003FFB@ = 00010000 2003C954 ABAQ8801 006025DB
2003FFC@ = 2003FFC8 00002863 2003FFFQ 2003C954
2003FFD@ = 00000001 00000000 00010000 31310001
2003FFE@ = ABAQ8801 01003147 2003FFFO @@0017D9
2003FFF@ = 00000000 00000000 00000000 000001BB
20040000 = BFOOBFOO BFOOBFOO E7FEBFQ0 AQF10400
20040010 = 33338047 33333131 33333131 33333131
J-Link>mem32 20@3FEDO,0x100
2003FED@ = 2003C944 2003C954 4EE54BA6 33333131
2003FEE@ = 33333131 33333131 33333131 33333131
2003FEF®@ = 33333131 33333131 33333131 33333131
2003FF00 = 33333131 33333131 33333131 33333131
2003FF1@ = 33333131 33333131 33333131 33333131
2003FF2@ = 33333131 33333131 33333131 33333131
2003FF30 = 33333131 33333131 33333131 33333131
2003FF40 = 33333131 33333131 33333131 33333131
2003FF50 = 33333131 33333131 33333131 33333131
2003FF60 = 33333131 33333131 33333131 33333131
2003FF70 = 33333131 33333131 33333131 33333131
2003FF80 = 33333131 33333131 33333131 33333131
2003FF90 = 33333131 33333131 33333131 33333131
20@3FFA@ = 33333131 33333131 33333131 33333131
2003FFB@ = 33333131 33333131 33333131 33333131
2003FFC@ = 33333131 33333131 33333131 33333131
20@3FFD@ = 33333131 33333131 33333131 84C00000
2003FFEO = AAQ@2000 A8A5CCBB 00000066 |2004000E Payload Return
2003FFF@ = 24070001 24242424 BFQOBFQ0 BFQ@BFOO
20040000 = BFO@BFOQ BFOQ@BFOO E7FEBFQ0 AQF10400
Original Return
20040010 = 33338047 33333131 33333131 33333131
```

## Slide 23


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
J-Link>setbp @x114@ <--—-— function exit
Breakpoint set @ addr 0x@0001140 (Handle =
PC
R@
00001140, CycleCnt = @2ACD568
00000031, R1 = 00000002, R2 = 00000010, R3 = 38000000
R4 = 00000000, R5 = 00000000, R6 = 20000000, R7 = 2003FFE8 J-Link>regs
R8 9220C050, RIO D@8C106E, R10@= 20030000, R11= 00000000 PC = 2004000A, CycleCnt = @2ACD570
R12= ABAQ8801
SP(R13)= 20@3FFE8, MSP= 2Q03FFE8, PSP= 00000000, R14(LR) = 0000113B RO = 00000031, R1 = 00000002, R2 = 00000010, R3 38000000
j-Link>mem32 2003FFE8, 0x20 R4 = 00000000, R5 = 00000000, R6 = 80000000, R7 00000066
200SFFES 6 MRE 24070001 24242424 R8 = 9220C050, RO = DQ8C106E, R10@= 20030000, R11= 00000000
20040008 = E7FEBFOQ AQF10400 33338047 33333131 i
20040018 = 33333131 33333131 33333131 33333131 SP(R13)= 2003FFF@, MSP= 2Q03FFFQ, PSP= 00000000, SE
20040028 = 33333131 33333131 33333131 33333131 J-Link>s ;
20040038 = 33333131 33333131 33333131 33333131
20040048 = 33333131 33333131 33333131 33333131 2004000A:
20040058 = 33333131 33333131 33333131 33333131 J-Link>s
00001140: 8@ BD POP {R7 , a}
```

## Slide 24

❌

❌

❌ ❌


> Recovered by OCR — confidence 76/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> }
while ( BYTE1(configuration_script) '= 1 );
et CVE-2024-25076
if ( check_current_fw_addr_and_update_addr(product_img_offse
if { !SRCWREBOOT_check_and_validate!
product_img_offsets[1],
(FW_ImageHeader *)&dword_2003C956,
(struct_configuration_script_ptr +)&configuration_script) }
else if { !SECWREBOOT_ check_and_validate(
(FW_ImageHeader *)&dword_2@03C950,
(struct_configuration_script_ptr *)&configuration_script) )
WOOG_Pet_1¢34();
sub_A6E((struct_configuration_script_ptr *)&configuration_script, product_img_offsets);
(struct_configuration_script_ptr *)&configuration_script,
product_img_offsets) )
OTPC_standby();
Cache_setup_qspi_cache(dword_2003C950, product_img_offsets) ;
return RESET_to_REMAP_ADR_ val(2u);
```

## Slide 25

## **ENCRYPTION**

- **Key Indexes •Index into OTP for encryption engine**

- **Nonce**

   - **•User defined Nonce**

   - **•Avoid IV reuse**

**AES-CTR mode enables fast/arbitrary block decryption AES-CTR provides no auth (malleable)**

💸

##### **SIGNED**

**ENCRYPTED**

## Slide 26

# **_“A CORRUPTED NONCE COULD NOT BE USED TO EXECUTE ARBITRARY CODE, RIGHT? “_ ME, PROBABLY**

## Slide 27

## **THIS WILL NEVER WORK**

**First blocks of the encrypted image: [    Stack Pointer     ]   [   Reset Vector    ] Key: FAA30A7DCC58C862576C486BC858DBDCDE88B6DDE0612E8C3D292A30D6447B02 IV: 59CD394A2E99EE4B000000000000000**

**AES-CTR**

**Where could the Reset Vector point to?**

**QSPI Flash mappings are quite large…**

## Slide 28

## **BACK OF THE NAPKIN HACKING**

##### **Quick test script**

- **Decrypt a known initial block using a known Nonce/Key**

- **Iterate over Nonce changes**

## Slide 29

## **BACK OF THE NAPKIN HACKING**

**IV** **= Nonce +** **Block Counter**


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
BACK OF THE NAPKIN HACKING
—[$]> python nonce_hunt\ copy.py FAA3@A7DCC58C862576C486BC858DBDCDE88B6DDE0
Searching by byte
potential iv 01920304050607080000000000000000 - SP dd7ea2fd Reset 362cf679
potential iv 01020304050c07080000000000000000 - SP dbdbbef4 Reset 36706836
searching 4byte blocks
potential iv 01920304050607080000000000000000 - SP dd7ea2fd Reset 362cf679
potential iv 02820304050607080000000000000000 - SP 69b@b6c7 Reset 3634e178
potential iv 050a0304050607080000000000000000 - SP c20a37db Reset 161b2fee
potential iv 05720304050607080000000000000000 - SP fe4dc684 Reset 160d9b52
potential iv 06480304050607080000000000000000 -— SP @1eb79c4 Reset 367e69ee
potential iv 96620304050607080000000000000000 - SP 8d43ae5b Reset 1602dfid
potential iv 06ea0304050607080000000000000000 - SP 3fdf567f Reset 164b236f
potential iv 08150304050607080000000000000000 - SP 9093bi1id Reset 16545aaf
potential iv 08440304050607080000000000000000 - SP if25dbbf Reset 160aaea2
potential iv @98a0304050607080000000000000000 -— SP 8657becd Reset 3627840e
IV = Nonce + Block Counter
```

## Slide 30

## **BACK OF THE NAPKIN HACKING**

##### **Modified Nonce Break Payload Reset/Halt**

##### **Break**

🫠

**T-bit of XPSR is 0 but should be 1. Changed to 1**

## Slide 31

## **STILL NOT CONVINCED**

Sig Check is here

**We are here**


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
STILL NOT CONVINCED
We are here
Load Image
Upgrade NO FW Validation
Pending Current Executable Image
YES NOK
FW Validation J {
— +—}> Trigger HW_Reset(); >! D
Update Image mOR | Reject Upgrade rigger HW_Reset(); i EN
OK
‘OK:
6
2 v
a Device Administration
£ Check Administration Data and j Accept Image
£ Perform Key revocation
>
a
| Configure Cache f Remap QSPI
Dec: 4 hea es —OK-> Ctrl with IVT Start. ——> Copy IVT @0x0 (IVT in SW Reset
| ryP Address RAM)
pest T
NOK
Trigger HW_Reset(); > END
```

## Slide 32

## **STILL NOT CONVINCED**

##### **Too complex to apply to a locked down target with zero knowledge? How to detect code exec?**

#### **Image Headers**

**- easy!**

- <sup>**fill entire unused flash space with NOPs**</sup>

- **•**<sup>**monitor SPI address access**</sup>

#### **Original Signed Image**

**NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP Unused Flash Area**

**NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP NOP**

## Slide 33

## **THIS WILL BE EASY**

##### **Nothing is easy.**

- <sup>**USON/WLCSP**</sup>

- <sup>**QSPI Decoder**</sup>

- <sup>**Antenna wires**</sup>

## Slide 34

## **KEEP IT SIMPLE**

**Original Nonce SPI Serial-In**

**Modified Nonce SPI Serial-In**

## Slide 35

## **FAST FWD**

Write FW  Write
Update FW
Start Timed
Power On  Power Off
Image with  to Target  Capture to
Capture
Target Target
Mutated Nonce SPI File

## Slide 36

👀

**One of many captures was a standout Reconfirmed it wasn’t an anomaly**

**Boot Boot**

## Slide 37

**Iterate over where its being stored in flash to determine where it actually is (0xa7f0-0x200000)**

**•**<sup>**Make window smaller and smaller until it stopped**</sup> **•**<sup>**Backup until it works again**</sup>

🎉 **0x1d4744 - 0x1d4747**

## Slide 38

## **NOW WHAT**

**How to get the encrypted firmware? Header Config specifies BURSTCMDA/B Registers**

**- these control how  the SoC talks to the SPI flash**

**- reconfigure to use single mode (0x03)**

**Modified FW**

## Slide 39

## **PROGRESS**

##### **Slowing down the target to Single SPI allows capture, showing the SoC accessing the payload at 0x1d4744**

## Slide 40

## **ALMOST THERE**

**SPI only does decryption in ‘Auto’ mode, which only allows reading. ‘Manual’ mode allows writing to SPI, but cannot read decrypted and payload fails to continue.**

## Slide 41

## **THE OWL**

Write Second
Write Original Nonce
Stage to RAM to
QSPIC_CTR_NONCE Registers
Set QSPI Interface to  Read next 2 bytes from
Auto Mode Encrypted Section
(Auto Decryption)
Write Command 0x11  Set QSPI Interface to
with Decrypted Bytes Manual Mode

## Slide 42

**THE OWL**


> Recovered by OCR — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
THE OWL
@x99 (reset)
0x03 @x00002074 (read)
@x@3 @ @x@000000e (read)
0x03 @ 0x00000012 (read)
@x®@3 @ @x00000016 (read)
@x@6 (write enable)
@x@1 (write status register)
@x@5 (read status register)
@x®@3 @ @x00002400 (read)
Q@x@3 @ 0x00002404 (read)
@x@3 @ @x@00025fc (read)
0x03 @x00fd4744 (read) <----— TRANSITION TO STAGE 1
0x03 Q@x00fd4780 (read)
| Ox00Fd4f6@ (read)
Ox00fd4f8@ (read)
0x00004/N (EM100 specific) <---- STAGE 2 DUMPING DECRYPTED APP
Q@x@0006 (EM10@ specific)
0x00000 (EM100 specific)
@x00008} (EM1@0 specific)
```

## Slide 43

##### **SIGNED**

ENCRYPTED
❌


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Type Device Administration Section (2
| Length of Device Administration Section
(2 Bytes)
Type Key revocation record (2 bytes)
OxAAS5
Length of Key revocation record
Key Index (1 Byte)
| KeyType (OwAl = Sign key, OxA2= Decr. |
Key, OxA3 = User Data Key
Key Index (1 Byte)
```

## Slide 44

## **DONE.**

###### **COMPUTERS ARE THE WORST.**
