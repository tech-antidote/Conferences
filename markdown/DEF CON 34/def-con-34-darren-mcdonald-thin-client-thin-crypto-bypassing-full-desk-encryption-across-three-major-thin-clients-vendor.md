---
title: "Thin Client Thin Crypto - Bypassing Full-Desk Encryption Across Three Major Thin Clients Vendors without Breaking a Ci"
speakers: ["Darren McDonald"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Darren McDonald - Thin Client Thin Crypto - Bypassing Full-Desk Encryption Across Three Major Thin Clients Vendors without Breaking a Ci.pdf"
pages: 45
sha256: "c06e621732b3398fe74676615b2814752d98095d1af61259bb224164aefd0255"
text_chars: 20535
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:15:41Z"
---
# Thin Client Thin Crypto - Bypassing Full-Desk Encryption Across Three Major Thin Clients Vendors without Breaking a Ci

**Speakers:** Darren McDonald  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Darren McDonald - Thin Client Thin Crypto - Bypassing Full-Desk Encryption Across Three Major Thin Clients Vendors without Breaking a Ci.pdf` (45 pages)

## Slide 1

```
/ / t h i n c l i e n t ? t h i n c r y p t o
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

# **`THIN CLIENT? / THIN CRYPTO`**

```
B y p a s s i n g F u l l - D i s k E n c r y p t i o n A c r o s s E v e r y M a j o r
T h i n C l i e n t W i t h o u t B r e a k i n g a C i p h e r
```

```
Darren McDonald
```

```
D E F C O N 3 4   ·   L a s V e g a s   ·   2 0 2 6
```

```
title
```

```
next →
```

## Slide 2

```
/ / w h o a m i
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Darren McDonald`**

```
AmberWolf  ·  offensive security, red team, hardware
```

```
← prevwhoami
```

```
next →
```

## Slide 3

```
/ / d i s c l o s u r e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

###### **`This project used AI assistance.`**

```
← prevdisclosure
```

```
next →
```

## Slide 4

```
/ / n o t a d u m b t e r m i n a l
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`What thin clients are not`**

```
Dumb, immutable terminals.
```

```
They’re running full Linux, Windows, and BSD
operating systems.
```

```
With secure boot chains and full disk encryption
to protect what’s on them.
```

```
And they hold data worth protecting.
```

```
VT100 · Jason Scott · CC BY 2.0
```

```
← prevthe device
```

```
next →
```

## Slide 5

```
/ / w h a t ’ s o n t h e m
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`So what’s on them worth stealing?`**

```
Enterprise WiFi, 802.1X and VPN credentials
```

- `Client-side certificates`

- `Administrative password hashes for fleet management`

- `Authentication tokens for fleet-management systems`

- `Cached logins and saved passwords`

- `Broker configs: Citrix · Horizon · RDP`

- `Logs and crash dumps, leaking all sorts of`

   - `sensitive data`

- `Full Disk Encryption attempts to protect this`

```
data…
```

```
← prevwhat’s on them
```

```
next →
```

## Slide 6

```
/ / t h e g a p
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Boot chain attacks`**

```
The window between power-on and the OS
```

```
power on→firmware→bootloader→kernel + initramfs→TPM unseal→OS unlocked
```

```
"Full" Disk Encryption
```

```
← prevthe gapnext →
```

## Slide 7

```
/ / t h e l i n e - u p
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

##### **`Targeting and comparing enterprise thin clients`**

```
T H E G O O D
```

```
IGEL OS 11 & 12
```

```
Did it right. Fell anyway.
```

```
T H E B A D
```

```
HP ThinPro 8 & 9
```

```
Incomplete secure boot chain.
```

```
T H E U G L Y
```

```
Dell ThinOS 9 & 10
```

```
Security theatre.
```

```
← prevthe line-up
```

```
next →
```

## Slide 8

```
/ / t h e g o o d
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
T H E G O O D ( r e l a t i v e l y )
IGEL OS 11 & 12
```

```
Right architecture. Modern crypto. Secure Boot
on. And still two ways in.
```

```
primitiveinjection + fail-open
```

```
← prevthe good
```

```
next →
```

## Slide 9

```
/ / t h e g o o d · i g e l
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`What IGEL got right`**

```
TPM + PCR sealing, Secure Boot on
modern crypto (AES-XTS, Argon2id)
signed boot chain, locked-down GRUB
```

```
← previgelnext →
```

## Slide 10

```
/ / t h e g o o d · i g e l · b o o t r e g i s t r y
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

###### `bug 1: where IGEL keeps its boot configuration`

#### **`An unsigned file a signed bootloader trusts`**

```
igelx64.efi reads & runs (Secure Boot signed)
```

```
boot registry (partition 4, first 256 KB)
```

```
000000  69 67 65 6c 62 72 65 67  igelbreg
boot_cmd000008  01 00 6f 73 5f 6d 6f 64  ..os_mod
000010  65 3d 73 74 64 0a 2e 2e  e=std...
```

###### `menuentry "Custom boot command" {`

```
linux $kernel igel_syslog=quiet quiet %s
```

```
←
%s %s   ...
0000a0  62 6f 6f 74 5f 63 6d 64  boot_cmd
0000a8  3d 69 6e 69 74 3d 2f 62  =init=/b
0000b0  69 6e 2f 73 68 0a 00 00  in/sh···
```

```
}
```

- **`✓`** `Secure Boot enforced`

   - **`✗`** `no encryption`

- **`✓`** `binary signed`

   - **`✗`** `no signature`

- **`✓`** `measured into the TPM`

   - **`✗`** `no integrity check`

- **`✓`** `GRUB locked down`

```
← previgel · boot registry
```

```
next →
```

## Slide 11

```
/ / t h e g o o d · i g e l · b o o t r e g i s t r y
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

0:00 / 0:51

- `inject on partition 4 · reboot · “Custom boot command” · Ctrl+Alt+F9 · root shell, every encrypted partition mounted. Under five minutes, no credentials.`

```
← previgel · boot registry · demo
```

```
next →
```

## Slide 12

```
/ / t h e g o o d · i g e l · b o o t r e g i s t r y
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
← previgel · boot registry · disclosure
```

#### **`Disclosed and Patched?`**

|`2026-02-24`
`reported`|`to IGEL PSIRT`|
|---|---|

|`2026-03-11`|`IGEL acknowledged,`|`state they know about`|
|---|---|---|
||`the issue`||

|`2026-04-08`|`IGEL OS 12.`|`7.6 released, boot registry`|
|---|---|---|
||`fixed`||

|`2026-04-12`
`independently`|`retested and confirmed fixed`|
|---|---|

|`2026-06-16`
`ISN`|`-2026-19 published`|
|---|---|

```
CVE | none
```

```
ISN | ISN-2026-19
```

```
resolved? | yes, fixed and re-
```

```
tested.
```

```
resolved in43 days
```

```
fixed in | OS 12: 12.7.6+ · OS
11: 11.11.150
```

```
ISN-2026-19 Code Execution via Boot Registry: kb.igel.com/en/security-safety/current/isn-2026-19-code-execution-via-boot-registry
```

```
next →
```

## Slide 13

```
/ / t h e g o o d · i g e l · c r a s h - t o - g r u b
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
bug 2 · IGEL's signed GRUB config
```

```
GRUB can require every file it loads to
be signed
```

```
set check_signatures=enforce          # every file GRUB loads must carry a valid GPG signature
```

```
for i in gpt1 gpt2 gpt3 gpt4 ; do
    if [ -e ${i}/igel.conf ] ; then   # IGEL search-loops each partition for its config
```

```
IGEL ships a signed GRUB and looks for igel.conf on each partition.
With check_signatures=enforce, an igel.conf we drop on the unencrypted
EFI partition is unsigned, so it should never load.
```

```
But that's exactly what we want.
```

```
← previgel · crash-to-grubnext →
```

## Slide 14

```
/ / t h e g o o d · i g e l · c r a s h - t o - g r u b
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

0:00 / 1:00

```
IGEL OS 12.7.6 · Secure Boot ON
```

```
← previgel · crash-to-grub · demo
```

```
next →
```

## Slide 15

```
/ / t h e g o o d · i g e l · d i s c l o s u r e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Disclosed and Patched?`**

|`2026-04-12`|`GRUB crash reported`|
|---|---|
|`2026-04-14`|`PSIRT: “seems valid”`|
|`2026-06-08`|`remediation shipped: 12.8.2 & 12.9.0`|
|`2026-06-16`|`retested 12.9.0: shell still opens`|
|`2026-06-17`|`ISN-2026-20 published`|

```
fix shipped in57 days
```

|`CVE |none`|
|---|
|`ISN |ISN-2026-20`|
|`resolved? |mostly`|
|`fixed in |12.9.0+ · 11.11.150+`|

```
← previgel · disclosurenext →
```

## Slide 16

```
/ / t h e g o o d · i g e l
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

###### `Architecture right. Bypassed` ~~`twice.`~~ `thrice.`

```
CVE-2025-47827, Zack Didcott
```

```
so what happens when the architecture isn’t right?
```

```
← previgel
```

```
next →
```

## Slide 17

```
/ / t h e b a d
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
T H E B A D
```

### **`HP ThinPro 8 & 9`**

```
A bad TPM seal, bolted to a boot chain it did
not measure.
```

```
primitiveunmeasured payload
```

```
← prevthe badnext →
```

## Slide 18

```
/ / t h e b a d · h p
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`HP sealed the loader. Not the payload.`**

```
firmwareoption ROMsGRUB binary|grub.cfgkernel + initramfs
```

```
green = sealed to PCR 0/2/4  ·  red = unencrypted partition, measured by
nothing
```

```
The TPM checks the loader is untouched, then hands the key to arbitrary code.
```

```
← prevhpnext →
```

## Slide 19

```
/ / t h e b a d · h p · t h e p a t c h
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`One line, and the key leaks.`**

```
# unseal_key — plain shell, in the initramfs on the UNENCRYPTED partition
hptc-tpm-tool -l "sha256:0,2,4" unseal -T /dev/tpm0     # TPM releases the LUKS key
log_success_msg "TPM unseal of LUKS key successfully"
cp  "$key"  <BOOT>/.luks_key            # one line to leak the key
```

```
The key lands on the unencrypted boot partition we can pull.
```

```
The unsealing script is not measured and PCR 0/2/4 are unchanged.
```

```
← prevhp · the patch
```

```
next →
```

## Slide 20

```
/ / t h e b a d · h p · d e m o
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

0:00 / 1:37

```
HP t540 · ThinPro 9.0 · boot our own OS · patch the initramfs · reboot ·
key on the unencrypted partition · LUKS open with the detached header.
Same attack, unchanged, on 8.1.
```

```
← prevhp
```

```
next →
```

## Slide 21

```
/ / t h e b a d · h p · d i s c l o s u r e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Disclosed, Fix Pending`**

|`2026-02-22`|`bypass confirmed · disclosed to HP PSIRT`
`(#6155)`|
|---|---|
|`2026-02-23`|`acknowledged(next day)`|
|`2026-04-14`|`fix confirmed in progress · coordinated`|
||`disclosure agreed`|

```
CVE | reserved (TBA)
resolved? | fix committed,
awaiting release
```

```
2026-05-2390-day window elapsed
```

```
resolved inTBC, fix due mid-July
```

```
← prevhp · disclosurenext →
```

## Slide 22

```
/ / t h e u g l y
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
T H E U G L Y
```

### **`Dell ThinOS 9 & 10`**

```
9.x and 10.x. Not a bug. Not bad architecture.
```

```
primitivepure security theatre
```

```
← prevthe uglynext →
```

## Slide 23

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`A key from the sticker`**

```
the machine magic string
```

###### `the derivation`

###### `sprintf(machine_magic, key = sha512(machine_magic)`

- `"ThinOS Machine Magic (1dead2beaf3cafe4): %s, %s, %x-%x-%x, %6D", // null-byte strip, not crypto planar_serial,   // baseboard serial a = 0xFB; b = 0xFC system_serial,   // system serial for i in 0..63: cpuid_ext,       // CPUID 0x80000000 r = b ^ i ^ key[i] cpuid_basic,     // CPUID 0x00000000 if r == 0: r = a ^ i cpuid_version,   // CPUID 0x00000001 key[i] = r mac);            // NIC MAC a -= 4; b -= 1`

```
pw = sha512(key).hex()[:30]
```

```
every input is printed on the chassis or visible on the wire.
```

```
The real key is in the TPM, but the password protecting it is written on the
side of the box.
```

```
← prevdell 9.x
```

```
next →
```

## Slide 24

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
IGEL and HP bound the key to the boot. Dell 9.x?
No PCRs. Nothing measured.
```

```
no PCR policy · no boot-integrity gate · the TPM password is just the KDF
output
```

```
So there was no seal to bypass. Only a binary to reverse engineer.
```

```
← prevdell 9.x
```

```
next →
```

## Slide 25

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
We had the key. The partitions were plainly GELI.
But the key wouldn’t mount them.
```

```
It needed more reverse engineering.
```

```
← prevdell 9.x
```

```
next →
```

## Slide 26

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
what the reverse engineering found
Five undocumented GELI mods
```

- `1  keyfile HMAC     HMAC(key,"")   →  HMAC("",key)`

- `2  enc_key const    0x00           →  0x01`

- `3  hmac_key const   0x01           →  0x00`

- `4  key halves       mkey | ivkey   →  ivkey | mkey 5  key rotation     1MB  (>>20)    →  4GB  (>>32)`

```
Not one bit of entropy added.
```

```
← prevdell 9.xnext →
```

## Slide 27

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
reimplementing Dell’s TPM unseal was painful.
So we let the device do it.
```

```
patch Dell’s own ramdisk (tpm.subr) · boot · it writes the key to the EFI
partition · a custom decryptor opens the disk
```

```
You can patch the ramdisk to dump the key.
```

```
← prevdell 9.x
```

```
next →
```

## Slide 28

```
/ / t h e u g l y · d e l l 9 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
the same USB didn’t work across 9.x versions.
```

#### **`So we built a Frankenboot.`**

```
early-9.x USB (9.1 bootloader, no hash check) + the target version’s
thinos.ko · swap the module, absorb each version’s subtle changes
```

```
No PCR seal means nothing checks what you boot.
```

```
← prevdell 9.xnext →
```

## Slide 29

```
/ / t h e u g l y · d e l l 9 . x · d e m o
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

0:00 / 1:09

```
Dell Wyse 5070 · ThinOS 9.x · FreeBSD / GELI: live USB → recompute the
key from on-device attributes → geli attach → ZFS pool mounts → config
DB and credentials in the clear. The key never left the device.
```

```
← prevdell 9.x
```

```
next →
```

## Slide 30

```
/ / t h e u g l y · d e l l 9 . x · d i s c l o s u r e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Disclosed and Unpatched (EoL)`**

```
2026-02-20ThinOS 9.x FDE bugs reported
2026-04-21Dell validates the findings
2026-05-15ThinOS 9.x end-of-life · EoSS dropped
```

```
CVEnone issued
```

```
resolved?no. 9.x was not patched;
Dell declared it end-of-life.
```

```
We can show you what Dell did. Not
why.
```

```
whatever the reason, the fielded
9.x devices were never fixed.
```

```
← prevdell 9.x · disclosurenext →
```

## Slide 31

```
/ / t h e u g l y · d e l l · t h e l i f e c y c l e p a g e , o v e r t i m e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
← prevthe public record
```

```
next →
```

#### **`Dell’s Wyse ThinOS 9.x lifecycle page`**

|`Device`|`End of Software Support`|
|---|---|
|`Wyse 3040`|~~`2026-12-31`~~
 `→`**`2026-05-15`**|
|`Wyse 5070`|~~`2027-08-15`~~
 `→`**`ThinOS 10`**|
|`Wyse 5470 Mobile`|~~`2028-06-30`~~
 `→`**`ThinOS 10`**|
|`Wyse 5470 AiO`|~~`2028-04-30`~~
 `→`**`ThinOS 10`**|

```
[1] as of July 2025  →  [2] as of July 2026
```

```
Special note, same page: the 16GB SKUs are not eligible for ThinOS 10.[2]
```

```
"ThinOS 9 has reached EoSS across all supported device platforms as of May
15, 2026".[2]
```

```
[1]web.archive.org/web/20250725061200/https://www.delltechnologies.com/asset/en-us/products/thin-clients/technical-support/wyse-thin-clients-os-lifecycle-matrix.pdf
[2]web.archive.org/web/20260713102743/https://www.delltechnologies.com/asset/en-us/products/thin-clients/technical-support/wyse-thin-clients-os-lifecycle-matrix.pdf
```

## Slide 32

```
/ / t h e u g l y · d e l l 1 0 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`ThinOS 10.x rebuilt from scratch`**

```
FreeBSD→Ubuntu Linux · GELI→LUKS
```

- `A ground-up rewrite. An excellent chance to get it right this time.`

```
← prevdell 10.x
```

```
next →
```

## Slide 33

```
/ / t h e u g l y · d e l l 1 0 . x · l i v e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

## **`LIVE`**

- `/ / L I V E C A P T U R E · d e m o d e v i c e`

```
← prevlivenext →
```

## Slide 34

```
/ / t h e u g l y · d e l l 1 0 . x · d e m o
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

0:00 / 1:21

```
Dell ThinOS 10.x · original build
```

```
← prevdell 10.x · demo
```

```
next →
```

## Slide 35

```
/ / t h e u g l y · d e l l 1 0 . x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`A TPM that protects nothing`**

```
Dell stored the LUKS key in the TPM with no lock.
```

```
The TPM added a checkbox, not security.
```

```
← prevdell 10.xnext →
```

## Slide 36

```
/ / t h e u g l y · d e l l 1 0 . x · t h e f i x
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Dell’s fix: bind to PCR 7`**

```
PCR 7 measures who signed the code.
```

```
So it only runs Dell-signed code. Right?
```

```
← prevdell 10.xnext →
```

## Slide 37

```
/ / t h e u g l y · d e l l 1 0 . x · b y p a s s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Dell uses Canonical’s bootloader.`**

- `$ sbverify --list grubx64.efi   # pulled from Dell’s update package Signer: Canonical Ltd. Secure Boot Signing Issuer: Canonical Ltd. Master Certificate Authority`

```
stock Ubuntu USB→same PCR 7→TPM unseals
```

```
Cracked the day after the patch shipped.
```

```
← prevdell 10.xnext →
```

## Slide 38

```
/ / t h e u g l y · d e l l 1 0 . x · d i s c l o s u r e
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
← prevdell · disclosure
```

```
next →
```

#### **`Disclosed, Bypassed, Then Patched`**

|`2026-02-20`
`ThinOS`|`10.x LUKS bug reported`|
|---|---|

|`2026-04-21`
`Dell val`|`idates the findings`|
|---|---|

|`2026-05-15`
`Dell re`|`leases a patch`|
|---|---|

|`2026-05-20`
`DSA-2026-214 / CVE`|`-2026-40713(PCR 7 fix)`|
|---|---|

|`CVE |CVE-`|`2026-40713 (co-credit`|
|---|---|
|`Christophe`|`Schleypen, NATO CSC) ·`|
|`CVE-2026-`|`56087`|

|`2026-05-21`
`patch`|`bypassednext morning`|
|---|---|

|`2026-06-11`
`Dell promises`|`a revised fix inJune`|
|---|---|

|`2026-06-19`|`revised fix shared`
`candidate)`|`privately(early release`|
|---|---|---|

```
resolved? | yes, 3 Jul 2026 · GA
2605.10.2100 (PCR 1+7+9)
```

|`2026-06-21`|`I retest: fixed`|`with Secure Boot on,not`|
|---|---|---|
||`with Secure Boo`|`t off`|

|`2026-06-25`
`Dell confirms`|`Secure Boot enforced at`|
|---|---|

|`install(closes the SB-off gap)`|
|---|

|`2026-07-03`|`revised`|`fix released · GA 2605.10.2100(PCR`|
|---|---|---|
||`1+7+9)`||

|`2026-07-15`|`DSA-2026-300 /`
`bypass)`|`CVE-2026-56087(the PCR 7`|
|---|---|---|

```
DSA-2026-214 www.dell.com/support/kbdoc/en-us/000463678/dsa-2026-214
DSA-2026-300 www.dell.com/support/kbdoc/en-us/000489640/dsa-2026-300
```

## Slide 39

```
/ / t h e l e s s o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`6/6 Thin Client Operating Systems`**

```
This isn’t a run of bad luck, something is wrong here.
```

|`OS`
`BOOT CH`|`AIN BUG`|`WEAK TPM SEALING`|`CLEARTEXT DATA STORAGE`|
|---|---|---|---|
|`IGEL OS 11`||||
|`IGEL OS 12`||||
|`HP ThinPro 8`||||
|`HP ThinPro 9`||||
|`Dell ThinOS 9`||||
|`Dell ThinOS 10`||||
|`Dell ThinOS 8`||||

```
← prevlesson 1
```

```
next →
```

## Slide 40

```
/ / t h e l e s s o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Auto-sealing FDE is hard`**

```
the boot partition might be too much attack surface to get right
Years of Microsoft BitLocker bypasses prove it
```

```
← prevlesson 2next →
```

## Slide 41

```
/ / t h e l e s s o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`How did they get this so wrong?`**

```
HP and Dell lost to a USB stick.
```

```
Insufficient public scrutiny.
```

```
The tech’s only adversary was a feature checkbox.
```

```
next →
```

```
← prevno excuse
```

## Slide 42

```
/ / t h e l e s s o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`And it only gets easier`**

|`Attack`|`Exploitable by`|
|---|---|
|`TPM + PIN`|`Serious equipment and hardware expertise`|
|`TPM SPI bus sniffing / DMA attacks`|`Basic electronics skills and equipment`|

|`Boot chain attacks`|
|---|

|`A USB stick`|
|---|

```
← previt gets easiernext →
```

## Slide 43

```
/ / t h e l e s s o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

## **`No lasers required.`**

```
Boot chain and TPM attacks are in reach of anyone in this room.
```

```
← previn reach
```

```
next →
```

## Slide 44

```
/ / t h e s c o r e c a r d
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

#### **`Disclosure scorecard`**

```
how they handled it: rating the process, not the bug.
```

```
IGELHP
★★★★★5 / 5★★☆☆☆2 / 5
Responsive and engaged. FixesCoordinated in the end, but no
shipped inside the 90-dayfix date until after the 90-day
window.window, and only once told
they’d feature in this talk.
```

```
Dell
```

```
★★★★★5 / 5
```

```
Engaged across three rounds of
fixes. Caught the incomplete RC
fix before it shipped.
```

```
← prevdisclosure · scorecard
```

```
next →
```

## Slide 45

```
/ / q u e s t i o n s
```

```
T H I N C L I E N T ? T H I N C R Y P T O
```

```
end
```

## **`Questions?`**

- `6 operating systems · 3 vendors ·`

- `6 bugs · zero broken ciphers`

|`IGEL`
`boot`|`OS 11 & 12`
`registry`|`ISN-2026-19`
`CVE-2026-`
`[TBC]`|`Patched?`|
|---|---|---|---|
|`IGEL`
`GRUB`|`OS 11 & 12`
`escape`|`ISN-2026-20`
`CVE-2026-`
`[TBC]`|`Patched?`|
|`HP T`
`Bypa`|`hinPro 8 & 9 FDE`
`ss`|`HPTKTKTKTKTK`
`CVE-2026-`
`[TBC]`|`Fix Pending`|
|`Dell`|`ThinOS 9 FDE Bypass`|`CVE-2026-`
`[TBC]`|`Unpatched`
`(EoL)`|
|`Dell`|`ThinOS 10 FDE Bypass`|`DSA-2026-214`
`DSA-2026-300`
`CVE-2026-`
`40713`
`CVE-2026-`
`56087`|`Patched`|

```
blog.amberwolf.com
write-ups · tools · CVEs
```

###### **`Darren McDonald AmberWolf`**

```
dmcdonald.netblog.amberwolf.com
```

```
github.com/R3n5k1
```

```
end
```

```
← prev
```
