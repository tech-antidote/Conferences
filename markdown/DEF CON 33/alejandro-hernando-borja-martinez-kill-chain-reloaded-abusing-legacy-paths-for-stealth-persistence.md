---
title: "Kill Chain Reloaded Abusing legacy paths for stealth persistence"
speakers: ["Alejandro Hernando Borja Martinez"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Alejandro Hernando Borja Martinez - Kill Chain Reloaded Abusing legacy paths for stealth persistence.pdf"
pages: 49
sha256: "33b088c4224e1f61697d65359603f47f583ab6fcb5b0b08e348ba0ee87ab81ed"
text_chars: 20528
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:51:04Z"
---
# Kill Chain Reloaded Abusing legacy paths for stealth persistence

**Speakers:** Alejandro Hernando Borja Martinez  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Alejandro Hernando Borja Martinez - Kill Chain Reloaded Abusing legacy paths for stealth persistence.pdf` (49 pages)


## Slide 1

Kill Chain Reloaded: Abusing legacy paths for stealth persistence

Alejandro Hernando @0xedh & Borja Martínez @borjmz

## Slide 2

### 0xedh@defcon33:~$ whoami

#### Alejandro Hernando / @0xedh

Red team and researcher in the Hacking Accenture Spain team.

I like to break things in my free time and spend money on gadgets.

Github: @0xedh Telegram: @edhx0 Twitter: @0xedh

## Slide 3

### borjmz@defcon33:~$ whoami

Borja Martínez / @borjmz / vorga

Red team and researcher in the Hacking Accenture Spain team.

From time to time I play the occasional CTF and was part of the ID-10-T (Retired) team.

Telegram: @borjmz Twitter: @Qm9yamFN Github: @borjmz

## Slide 4

### Table of Contents

01

02

Research of vulnerable Artifacts

UEFI Exploitation

03

Vulnerable driver usage and exploitation

## Slide 5

01

## Research of vulnerable Artifacts

## Slide 6

### Contextualization: Why does it matter to talk about this now?

- UEFI bootkits are no longer theoretical: they are real, active and used by APTs.

- BlackLotus (2023): the first known malware to bypass Secure Boot in Windows 11.

- Pre-SO persistence = total control + EDR evasion.

- Digital signatures and Secure Boot are not enough if vulnerable binaries are not revoked.

## Slide 7

### Secure Boot ≠ secure by default

- Secure Boot depends on an updated chain of trust.

- Revoked binaries are stored in the DBX (UEFI) database.

- It is easy to load legitimate but vulnerable bootloaders if the DBX is out of date.

## Slide 8

### The CrowdStrike case (2024)

- Failed update caused massive BSODs on thousands of endpoints.

- Real impact: banks, airports, hospitals, critical services offline.

- A single piece of software in the boot environment = whole system down.

- What if this was done by a malicious bootkit?

## Slide 9

### Real bootkits in the real world

Here is a quick table with some of the most known bootkits that have been used in real operations, many of them linked to APTs

Most of them are loaded before the operating system, which means that no EDR, antivirus or traditional solution can see them. They control the system from the moment you turn it on.

## Slide 10

### The objective

- To find signed software/firmware with useful functions for post-exploitation.

- We are looking for:

   - Drivers with MmMapIoSpace, ZwMapViewOfSection, MmCopyMemory, memcpy, etc.

   - Vulnerable (signed) UEFI drivers -> to load bootkits.

   - Vulnerable native signed windows apps (wpbbin.exe)

- Tools:

   - VirusTotal + RetroHunt -> YARA rules + retrohunting of old drivers.

   - Microsoft Catalog -> downloaded .CAB of legitimate signed drivers.

   - Own scripts -> string extraction, fast static analysis, hash matching, etc.

## Slide 11

## Slide 12

02

# UEFI Exploitation

## Slide 13

### UEFI and Bootloader – The Real Entry Point

- UEFI is the first software that runs after powering on the system.

- Acts like a mini OS: has its own heap, services, and .efi modules.

- Loads components from the EFI System Partition (ESP) – bootloaders and drivers.

- The bootloader (bootmgfw.efi, shim.efi, etc.) launches the OS.

- Everything before ExitBootServices() runs outside OS/EDR visibility.

- If we load our signed .efi at this stage, we get pre-OS full control.

- We can redirect the boot flow, persist, or disable protections.

- This is the foundation for the loading chain shown in the next demos.

## Slide 14

### Vulnerable bootloaders

- There are a lot of vulnerable applications in the wild, as an example, **CVE-2022-34302**


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vulnerable bootloaders
There are a lot of vulnerable applications in the wild, as an example, CVE-2022-34302
MODIFIED
This CVE record has been updated after NVD enrichment efforts were completed. Enrichment data supplied by the NVD may require
amendment due to these chang
'1JAn attacker may use this bootloader to bypass or tamper with
e Boot protection: c rbitrary code in the pre-boot stage, an attacker simply ds to replace the existing
signed bootloader currently in u: ith this bootloader. Access to the EFI System Partition is required for booting using external media.
Metrics [ cyssversion4.0 [RXEENGREMERIN CVSS Version 2.0
NVD enrichment effo rence publicly ai
CVSS 3.x Severity and Vector String:
\ NIST: NVD Base Score: 6.7 MEDIUM Vector: CVSS:3.1/AV:
```

## Slide 15

### Microsoft DBX revocation list

● https://github.com/microsoft/secureboot_objects

## Slide 16

### Microsoft DBX revocation list

- **C3D65E174D47D3772CB431EA599BBA76B8670BFAA51081895796432E2EF6461F** = Good old **CVE-2022-34302**

- And the other ones?

## Slide 17

### Reboot Restore Analysis

- Firmware looks for the **ESP** ’s \EFI\Boot\ **bootx64.efi** .

- **Shdloader.efi** is renamed or copied over **bootx64.efi** .

- When the firmware invokes “bootx64”, it actually runs **Shdloader.efi** first.

- **Shdloader.efi** then implements its own logic (decompression, signature checks, etc.) before finally loading the real **bootmgfw.efi** .

## Slide 18

### #PHASE 1 - What does “shieldloader” do?

- Opens the ESP’s FAT volume

- Locates the file \EFI\Boot\ **shdmgr.ef_** ( **notice the underscore, proprietary NAUY format** )

- ● Allocates the file’s size, and reads all bytes into a buffer

## Slide 19

### #PHASE 2 - Decompress the “NAUY” format

- Inspects the **0x200-byte header** at the start

- Reads the **ASCII magic “NAUY”** , and extracts the compressed and uncompressed lengths from the header

- Walks through the chunks, decompress or memcpy

## Slide 20

The “NAUY” format


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The “NAUY” format
uint16
uint16
char[4]
uint32
uint32
header_size = 0x0200
reserved/version (unused)
total_uncompressed_length
total_compressed_length
(padding/reserved to 0x20)
800-byte TRAILER
Repeat until you've consumed total_compressed_length bytes:
CHUNK RECORDS
uint32 hash_len // # of leading bytes signed
uint32 fmt_ver // format/version (0x00010000)
uint32 sig_len // always 256
uint8[12] padding
uint8[516] public-key DER blob (ignored at runtime)
uint8[256] RSA-PKCS#1-v1.5 signature
uint16
uint8
uint8
record_len
flags // bit2 (®x®4) = compressed
payload[record_len-4]
else -> memcpy (payload)
// includes this 4-byte hdr
```

## Slide 21

### #PHASE 3 - Crypto signature verification

- It jumps to the **last 800 bytes** , “RSAS” followed by 256-byte RSA signature.

- ● If the magic is wrong, the padding check fails, or the digest doesn’t match, **check_signature()** returns false, and the loader aborts with **EFI_SECURITY_VIOLATION** .

## Slide 22

### #PHASE 4 - Starting the bootmanager

- Finally, the loader hands off to the standard UEFI Boot Services. It calls **LoadImage()** and returns a new EFI handle. It then invokes **StartImage()** , which transfers control into the loaded PE.

## Slide 23

### The “shell.ef_” container

● Just a few commands… But better than nothing.


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The “shell.ef_” container
e Just a few commands... But better than nothing.
cd -Displays or changes the current directory.
cp -Copies one or more source files or directories to a destination.
nap Defines a mapping between a user-defined name and a device handle.
nkdir -Creates one or more new directories.
hu -Moves one or more files to a destination within a file system.
reset -Resets the system.
set -Displays, changes or deletes a UEFI Shell environment variables.
Is -Lists a directory’s contents or file information.
rm -Deletes one or more files or directories.
vol -Displays the volume information for the file system that is specified
by fs.
date -Displays and sets the current date for the system.
time -Displays or sets the current time for the system.
timezone -Displays or sets time zone information.
stall -Stalls the operation for a specified number of microseconds.
for -Starts a loop based on for syntax.
goto -moves around the point of execution in a script.
if -Controls which script commands will be executed based on provided con
ditional expressions.
shift -moves all in-script parameters down 1 number (allows access over 10) .
exit -Exits the UEFI Shell or the current script.
else -Else identifies the portion of the code executed if the if was FALSEP
ress ENTER to continue or ’Q’ break:q
Shell> _
```

## Slide 24

### What does “shdmgr.ef_” do?

- After decompressing the EFI in shdmgr.ef_, the loader skips the custom format and directly loads another EFI image.

- No signature verification: **load_unsigned_efi()** <u>never calls</u> **check_signature()** .

- No container parsing: it expects a straight PE image, so you can drop any *.efi there.

- It actually contains its own minimal PE loader and relocator.

## Slide 25

## Slide 26

### Bitlocker protection

- When you enable BitLocker on an OS volume, the VMK is sealed in the TPM against the current values of several Platform Configuration Registers (PCRs).

- With Secure Boot enabled, PCR 7 records a hash of every EFI executable that runs before the kernel: bootmgfw.efi, BCD, early drivers,etc.

- If any one PCR is different the unseal fails and Windows falls back to BitLocker recovery mode.

## Slide 27

### Bitlocker protection

- Use WMI to run DisableKeyProtectors with **DisableCount = 0**

- Deploy and overtwrite boot files, replace **shdmgr.ef_** with **shell.ef_**

- “ **stage0.efi** ”, a <u>signed tool capable of enrolling unsigned binaries</u> into MOK (knoppix).

## Slide 28

## Slide 29

### Enough ASCII art! Let's do something

- What about **WPBT** (Windows Platform Binary Table)?

- WPBT lets the firmware place one native app (signed) at C:\Windows\System32 and executes it in the session manager context.

- <u>In updated Windows 11 24H2, you can’t just use a leaked code signing certificate.</u>

- ● Simply dropping an unsigned “malicious.exe” via WPBT is “useless”, the file lands on disk but nothing launches it.

## Slide 30

### Lenovo wpbbin.exe

- This binary was used by “ **Lenovo Service Engine** ” (LSE) to smuggle a big blob of PE files, registry keys and config data from firmware into Windows.

- It uses **Lenovo LUFT table** , that isn’t part of ACPI spec, only Lenovo’s binary parses it.

- ● This lets an attacker install an arbitrary driver or service completely from ACPI, no disk write needed until Windows does it for you.

## Slide 31

### Lenovo LUFT table

##### We construct a new LUFT table that:

- **Drops hell.sys** (read from vulndriver.sys in the repo, this is a signed vulnerable driver).

- ● **Creates a service key** under HKLM\SYSTEM\CurrentControlSet\Services\2srvdriver.

- ● Sets <u>DisplayName, ImagePath, Type, Start, ErrorControl</u> values.

- **Re-use slot #6 in the XSDT** (originally the OEM’s WSMT entry) to point at the LUFT buffer instead, and fix the XSDT checksum.

## Slide 32

### What does the lenovo native app do?

- **Looks for** custom ACPI table named **LUFT** .

- **Writes** the embedded **binary to disk** calling the function labeled as “save_binary” to C:\Windows\System32\Drivers\XXXX.sys

- Then **invokes create_reg_key()** on every sub-descriptor, which in turn writes or patches the registry so the binary will launch automatically.

## Slide 33

### WPBT

##### To construct our WPBT:

- Find a **writable runtime-memory** space (1 MiB at BIN_ADDR, we allocated it before with our .EFI) and **copy our real payload** (the Lenovo-signed native app) there

- ● **Overwrite** the **first 16 bytes of the in-RAM SRAT** with that WPBT header

## Slide 34

### To summarize…

- Firmware finishes POST, enters **ExitBootServices()** ; **RT-memory** still **contains our injected blobs** .

- ● Windows loader scans the XSDT, **find our LUFT** . ● Probes the RAM page that used to be **SRAT** but **now begins with “WPBT”** ; sees a valid length & checksum, accepts it as the WPBT.

- **smss.exe** (session manager) copies the Lenovo-signed EXE from the WPBT to disk and **executes it as NtProcessStartup** .

- Lenovo **native signed app** (started later by RunServicesOnce) **parses the LUFT** ; **drops hell.sys** , <u>writes the registry values,</u> and starts the service (or schedules it for next boot, depending on the flags).

- ● On the next boot, <u>Windows sees a legitimate driver entry under Services\2srvdriver,</u> **loads hell.sys** at kernel time, and the **system is compromised** .

## Slide 35

## Slide 36

03

Vulnerable driver usage and exploitation

## Slide 37

### BYOVD – From EFI to Kernel without detection

- We use legitimate but vulnerable drivers to gain kernel-level access.

- These drivers expose powerful memory access primitives like:

- ● **ZwMapViewOfSection** , **MmMapIoSpace** , **MmCopyMemory** , **ZwTerminateProcess** , etc.

- Poorly implemented IOCTLs allow user-mode control over kernel functions.

Once loaded, we use them to:

- Bypass security mechanisms.

- Elevate privileges by modifying **EPROCESS** tokens (SYSTEM token steal).

- ● Hook and modify kernel structures.

- Disable callbacks: process/thread/image notifications via **PspCreateProcessNotifyRoutine** .

- These drivers are often found on Microsoft Update Catalog or via VirusTotal RetroHunt.

- Our custom EFI loaders plant the drivers silently during early boot.

## Slide 38

### What Does the Driver Do?

A signed Huawei kernel-mode driver that enforces process protection, blocks access to targeted processes, and relaunches them automatically.

- **HwAiGalleryGuardDriver.sys** is a signed driver from Huawei, typically installed as part of the HwAIServiceSetup package. It runs with kernel privileges and remains active even after the associated software is uninstalled.

- The driver registers a process creation and termination callback via **PsSetCreateProcessNotifyRoutine** , allowing it to monitor and react to specific processes defined by user-mode input.

- It also registers an object access filter using **ObRegisterCallbacks** to intercept PsProcessType object operations (like **OpenProcess** ) and strip access rights such as **PROCESS_TERMINATE** from other processes trying to interfere.

- When a monitored process terminates, the driver automatically recreates it, using **APC injection** into a thread of a trusted process (services.exe), launching a hidden command like “sc.exe start myservice.exe”.

- This design provides a stealthy, persistent protection mechanism: the process is shielded from external control, and silently restored if killed all under kernel-level control and without any user-mode component being responsible.

## Slide 39


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NTSTATUS result; //
NTSTATUS ntStatus;
Protected Process
)3
(e-g-, notepad.exe)
{
LOBYTE(
}
else
| Process Callback Registered | {
| (PsSetCreateProcessNotifyEx) |
[Process Exit Detected] NTSTATUS status; //
void *threadHandle; //
Ox1FFFFFu, @i64, @i64, ies, ( )StartRoutine, ei6
else
| Object Callback Registered
(ObRegisterCallbacks)
| return 1;
}
else
{
- Block TERMINATE access sub_140001900("RegisterForbidingKill Fail, status=@x%@8x.", (un
- Modify process rights return 0;
[Access Attempt Detected]
```

## Slide 40

### How does it interact with User-Mode?

The driver is fully controllable from user-mode without authentication or privilege checks.

- It exposes a device object ( **\\.\HwAiGalleryGuardDriverControl** ) that accepts IOCTL requests from any user-mode process.

- The included tool iGalCheck.exe communicates with the driver using commands like /protect and /unprotect.

- These commands trigger the **IOCTL 0x222004** , which does not validate input or require administrative privileges.

- The buffer passed contains a Unicode string with the path to the executable to protect, typically like "C:\Windows\System32\notepad.exe".

- No input sanitization, signature checking, or access control is performed any process can be protected arbitrarily.

## Slide 41


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if (!
| iGalCheck.exe
| (User-Mode Tool)
H @x2220e4u, ex194u, » @x194u, & R » 0164) )
ei64;
", guiea) )
» 8ui64) )
}
else
{
sub_1490@01010(" e le e | in 11 | ?install | load | unload | ?load | pri
| Sets internal compare string |
```

## Slide 42

### What internal validation logic does it use?

The driver's validation is minimal and based solely on an exact path string comparison.

- Upon receiving a request, the driver retrieves the target process's PEB using **PsGetProcessPeb** and KeStackAttachProcess.

- It extracts the process's CommandLine and compares it with an internal compare_string (set earlier **via IOCTL** ).

- The comparison uses **RtlCompareUnicodeString** , which is case-sensitive and does not normalize path syntax.

- No signature, hash, or executable metadata is verified only a raw string match on the command line.

## Slide 43

### How does it maintain persistence?

It uses driver-level callbacks and APC injection to ensure process resurrection.

- Even after uninstalling the software, the driver remains loaded, as the uninstall routine does not remove it.

- Manual removal is required using tools like sc delete, devcon remove, and sc stop for associated services.

- When a protected process exits, the driver launches a new process using APC injection into a thread of services.exe.

## Slide 44

- The routine CreateProcessByApc constructs a command line like sc.exe start hell and injects it via KeInsertQueueApc.

- This kernel-level process creation bypasses standard security hooks, allowing silent and persistent restarts.

## Slide 45

### What Security Mechanisms Does It Ignore?

It bypasses typical user-mode protections and disables process control.

- Removes the ability to terminate protected processes by clearing **PROCESS_TERMINATE** rights ( **ClearTerminateRight** ).

- Evades user-mode monitoring tools (like Task Manager or Sysmon) by performing operations entirely in kernel space.

- Uses legitimate system processes (e.g., services.exe) as injection targets to hide malicious activity.

- No signature validation means even untrusted or tampered binaries can be protected.

- These characteristics make the driver <u>a powerful primitive for</u> “rootkits”, EDR evasion, and stealth persistence.

## Slide 46

## Slide 47

### Conclusions

- Secure Boot isn't a silver bullet

- Signed binaries exploitable if DBX not updated.

- ● UEFI: overlooked & powerful attack surface

   - Early execution bypasses traditional EDR.

- EFI loaders chain silently into custom payloads

   - Legitimate ESP entries provide persistent footholds.

- BYOVD (Bring Your Own Vulnerable Driver)

   - Abuses legitimate drivers for kernel implants.

- Exploits poor IOCTLs for kernel R/W & privilege escalation.

   - Disable critical protections

- All components are signed, trusted & load silently

- Publicly sourced drivers (Microsoft Catalog, VT RetroHunt).

- ● Full persistence across reboots

   - Effective even with BitLocker/VBS enabled, with tweaks ;)

## Slide 48

### References

- ESET. (s. f.). Machine Learning and UEFI. https://web-assets.esetstatic.com/wls/en/papers/white-papers/ESET_Machine_Learning_UEFI.pdf

- HackingThings. (s. f.). SignedUEFIShell [GitHub repository]. GitHub. https://github.com/HackingThings/SignedUEFIShell/tree/main

- SOC Investigation. (2023). UEFI persistence via wpbbin: Detection & response. https://www.socinvestigation.com/uefi-persistence-via-wpbbin-detection-response/

- Sophos. (2023, junio 2). Researchers claim Windows backdoor affects hundreds of Gigabyte motherboards. https://news.sophos.com/en-us/2023/06/02/researchers-claim-windows-backdoor-affects-hundreds-of-gigabyte-motherboards/

- tandasat. (s. f.). WPBT-Builder [GitHub repository]. GitHub. https://github.com/tandasat/WPBT-Builder?tab=readme-ov-file

- Persistence Info. (s. f.). WPBBin. https://persistence-info.github.io/Data/wpbbin.html

- Unified Extensible Firmware Interface Forum. (s. f.). UEFI Revocation List File. https://uefi.org/revocationlistfile

- Microsoft. (s. f.). secureboot_objects [GitHub repository]. GitHub. https://github.com/microsoft/secureboot_objects

- HackingThings. (s. f.). OneBootloaderToLoadThemAll [GitHub repository]. GitHub. https://github.com/HackingThings/OneBootloaderToLoadThemAll/

- Knopper, K. (s. f.). Knoppix and UEFI. https://www.knopper.net/knoppix/knoppix-uefi-en.html

- br-sn. (n.d.). Removing Kernel Callbacks Using Signed Drivers. Retrieved from https://br-sn.github.io/Removing-Kernel-Callbacks-Using-Signed-Drivers/

- br-sn. (n.d.). CheekyBlinder [GitHub repository]. GitHub. Retrieved from https://github.com/br-sn/CheekyBlinder

- VL. (2021). Removing Process Creation Kernel Callbacks. Medium. Retrieved from https://medium.com/@VL1729_JustAT3ch/removing-process-creation-kernel-callbacks-c5636f5c849f

- lawiet47. (n.d.). STFUEDR [GitHub repository]. GitHub. Retrieved from https://github.com/lawiet47/STFUEDR

- hfiref0x. (n.d.). KDU (Kernel Driver Utility) [GitHub repository]. GitHub. Retrieved from https://github.com/hfiref0x/KDU

- TheCruZ. (n.d.). kdmapper [GitHub repository]. GitHub. Retrieved from https://github.com/TheCruZ/kdmapper

- Sophos. (2022, October 4). BlackByte ransomware returns, abuses RTCore64.sys driver to disable kernel callbacks. Sophos News. Retrieved from https://news.sophos.com/en-us/2022/10/04/blackbyte-ransomware-returns/

## Slide 49

**https://github.com/0xedh/DEFCON33-KillChainReloaded**

Special mention to @sanguinawer for helping us out!!!!

Thanks to @s4dbrd and JC
