---
title: "KernJC Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities"
speakers: ["Bonan Ruan", "Jiahao Liu", "Chuqi Zhang", "Zhenkai Liang"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Bonan Ruan & Jiahao Liu & Chuqi Zhang & Zhenkai Liang_KernJC Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities.pdf"
pages: 30
sha256: "e0648f175745d078b78c3caf93b7d2898508a4371ce4a41cc6ac3fd6c7195a5b"
text_chars: 18802
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.6
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:52:14Z"
---
# KernJC Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities

**Speakers:** Bonan Ruan, Jiahao Liu, Chuqi Zhang, Zhenkai Liang  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Bonan Ruan & Jiahao Liu & Chuqi Zhang & Zhenkai Liang_KernJC Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities.pdf` (30 pages)


## Slide 1

# KernJC: Automated Vulnerable Environment Generation for Linux Kernel Vulnerabilities

Speakers: Bonan Ruan, Jiahao Liu Contributors: Chuqi Zhang, Zhenkai Liang

#BHAS @BlackHatEvents

## Slide 2

## **ABOUT US**

**Jiahao Liu** , Ph.D. Student, NUS ➢ GitHub: @ljiahao ➢ Homepage: _<u>ljiahao.github.io</u>_ ➢ E-mail: jiahao99@comp.nus.edu.sg

**Bonan Ruan** , Ph.D. Student, NUS ➢ Ex-NSFOCUS Security Researcher

➢ GitHub: @brant-ruan ➢ Homepage: _<u>profile.wohin.me</u>_ ➢ E-mail: r-bonan@comp.nus.edu.sg

**Zhenkai Liang** , Assoc Prof, NUS ➢ Homepage: _<u>comp.nus.edu.sg/~liangzk</u>_ ➢ E-mail: liangzk@comp.nus.edu.sg

**Chuqi Zhang** , Ph.D. Student, NUS ➢ GitHub: @Icegrave0391 ➢ Homepage: _<u>chuqiz.notion.site</u>_ ➢ E-mail: chuqiz@comp.nus.edu.sg

_<u>nus-curiosity.github.io</u>_

#BHAS @BlackHatEvents

## Slide 3

## **ABOUT KERNJC**

### github.com/NUS-Curiosity/KernJC

#BHAS @BlackHatEvents

## Slide 4

## **ENDLESS KERNEL VULNERABILITIES!**

CVE-2023-52927
CVE-2025-21703
CVE-2025-21700
CVE-2025-21756
CVE-2025-21702
CVE-2025-21836
CVE-2023-52926
CVE-2025-21701

###### Source: Google kernelCTF

(https://docs.google.com/spreadsheets/d/e/2PACX-1vS1REdTA29OJftst8xN5B5x8iIUcxuK6bXdzF8G1UXCmRtoNsoQ9MbebdRdFnj6qZ0Yd7LwQfvYC2oF/pubhtml#)

#BHAS @BlackHatEvents

## Slide 5

## **IMPACT OF KERNEL VULNERABILITIES**

Source: Bonan’s blog post

(https://blog.wohin.me/posts/thoughts-on-vuln-research-2)

#BHAS @BlackHatEvents

## Slide 6

## **REPRODUCTION!**

Vulnerable
Environment
Brain
What Do We
Patient
Need for
Luck
Reproduction?
Proof of Concept
(PoC)

Severity
Assessment
Detection &
Application
Mitigation
Scenarios
Defense
Evaluation

#BHAS @BlackHatEvents

## Slide 7

## **DON’T TAKE SUCCESSFUL ENV FOR GRANTED!**

Hello, when building the test environment, I followed the steps above to compile the kernel... It kept getting stuck... During the test, I didn't find any 'NFQUEUE' rule in the target...

At the time, I selected many configs, and it's possible that some configs were not included. First, check if it's an issue with the compilation options...

#BHAS @BlackHatEvents

## Slide 8

## **EXAMPLE: CVE-2021-22555**

**Description:**

A heap out-of-bounds write affecting Linux since v2.6.19-rc1 was discovered in net/netfilter/x_tables.c. This allows an attacker to gain privileges or cause a DoS (via heap memory corruption) through user name space.

**Report Date:** 2021-04-06 **Affected Product:** Linux Kernel **CVSS:** 7.8 (High) **CWE:** CWE-787 (Out-of-bounds Write) **Impact:** Privilege Escalation **Exploit:** Public **Vulnerable Version Ranges in NVD Database:** [v2.6.19, v4.4.267) [v4.5, v4.9.267) [v4.10, v4.14.231) [v4.15, v4.19.188) [v4.20, v5.4.133) [v5.5, v5.10.31) [v5.11, v5.12)

#BHAS @BlackHatEvents

## Slide 9

## **EXAMPLE: CVE-2021-22555**

###### **`Code Snippet (v5.11.22)`**

\```
void xt_compat_target_from_user(struct xt_entry_target
\```

- `*t, void **dstptr, unsigned int *size) { // ... omitted ...`

\```
target->compat_from_user(t->data, ct->data);
else
\```

\```
memcpy(t->data, ct->data, tsize-sizeof(*ct));
\```

\```
tsize+= off;
t->u.user.target_size= tsize;
\```

###### **`Patch Snippet`**

\```
@@ -1126,9 +1123,6 @@ void xt_compat_target_from_user(struct
xt_entry_target*t, void **dstptr,
\```

###### **`NVD Version Ranges`**

\```
[v2.6.19,v4.4.267)
[v4.5,v4.9.267)
[v4.10,v4.14.231)
[v4.15,v4.19.188)
[v4.20,v5.4.133)
[v5.5,v5.10.31)
[v5.11,v5.12)
\```

\```
target->compat_from_user(t->data, ct->data);
else
\```

- `memcpy(t->data, ct->data, tsize - sizeof(*ct));`

- `- pad = XT_ALIGN(target->targetsize) - target->targetsize;`

- `- if (pad > 0)`

\```
-
memset(t->data + target->targetsize, 0, pad);
tsize+= off;
t->u.user.target_size= tsize;
\```

v5.11.22 seems to be vulnerable

but already patched!

#BHAS @BlackHatEvents

## Slide 10

UM...

You can’t wake a person who is pretending to be asleep.

#### **You can’t trigger a vulnerability which has been patched.**

#BHAS @BlackHatEvents

## Slide 11

## **EXAMPLE: CVE-2021-22555**

###### **Patch Snippet**

\```
diff --git a/net/netfilter/x_tables.c
\```

\```
index 6bd31a7a27fc58..92e9d4ebc5e8d7 100644
\```

- `--- a/net/netfilter/x_tables.c`

\```
+++ b/net/netfilter/x_tables.c
\```

###### **Related Makefiles**

\```
obj-$(CONFIG_NETFILTER)         += netfilter/
obj-$(CONFIG_NETFILTER_XTABLES) += x_tables.o
\```

- `@@ -1126,9 +1123,6 @@ void xt_compat_target_from_user(...`

\```
target->compat_from_user(t->data, ct->data);
\```

\```
else
\```

\```
memcpy(t->data, ct->data, tsize -sizeof(*ct));
\```

- `pad = XT_ALIGN(target->targetsize) - target->targetsize;`

- `if (pad > 0)`

   - `memset(t->data + target->targetsize, 0, pad);`

###### **Temporary Results**

###### **Vulnerable Code Snippet**

###### **`#ifdef CONFIG_COMPAT`**

\```
void xt_compat_target_from_user(...
\```

\```
target->compat_from_user(t->data, ct->data);
else
\```

\```
memcpy(t->data, ct->data, tsize -sizeof(*ct));
pad = XT_ALIGN(target->targetsize) -target->targetsize;
if (pad > 0)
\```

\```
memset(t->data + target->targetsize, 0, pad);
\```

\```
CONFIG_COMPAT
CONFIG_NETFILTER_XTABLES
CONFIG_NETFILTER
\```

#BHAS @BlackHatEvents

## Slide 12

## **EXAMPLE: CVE-2021-22555**

###### **Temporary Results**

\```
CONFIG_COMPAT
CONFIG_NETFILTER_XTABLES
CONFIG_NETFILTER
\```

###### **Related Kconfig Files**

\```
[net/netfilter/Kconfig][net/Kconfig]
menu "Core Netfilter Configuration"if NET
depends on NET&& INET&& NETFILTERconfig INET
... omitted ...... omitted ...
config NETFILTER_XTABLESmenuconfigNETFILTER
\```

###### **Heuristic Analysis Result of Configs**

\```
CONFIG_COMPAT       CONFIG_NETFILTER_XTABLESCONFIG_NETFILTER
CONFIG_NET          CONFIG_NETFILTER_FAMILY_ARPCONFIG_NETFILTER_ADVANCED
CONFIG_INET         CONFIG_IP_NF_IPTABLESCONFIG_NLATTR
CONFIG_IPV6         CONFIG_IP_NF_ARPTABLESCONFIG_GENERIC_NET_UTILS
CONFIG_BPF          CONFIG_IP6_NF_IPTABLES
\```

#BHAS @BlackHatEvents

## Slide 13

## **EXAMPLE: CVE-2021-22555**

###### **Heuristic Analysis Result of Configs**

\```
CONFIG_COMPAT       CONFIG_NETFILTER_XTABLESCONFIG_NETFILTER
CONFIG_NET          CONFIG_NETFILTER_FAMILY_ARPCONFIG_NETFILTER_ADVANCED
CONFIG_INET         CONFIG_IP_NF_IPTABLESCONFIG_NLATTR
CONFIG_IPV6         CONFIG_IP_NF_ARPTABLESCONFIG_GENERIC_NET_UTILS
CONFIG_BPF          CONFIG_IP6_NF_IPTABLES
\```

\```
CONFIG_NETFILTER_XT_TARGET_NFQUEUE
\```

###### **PoC Snippet**

\```
data.match.u.user.match_size = (sizeof(data.match) + sizeof(data.pad));
strcpy(data.match.u.user.name, "icmp6");
data.match.u.user.revision = 0;
data.target.u.user.target_size = sizeof(data.target);
strcpy(data.target.u.user.name, "NFQUEUE");
data.target.u.user.revision = 1;
\```

#BHAS @BlackHatEvents

## Slide 14

UM...

Version

###### **You can’t trigger a vulnerability which has been patched.**

#### **You can’t trigger a vulnerability which doesn’t exist or is inaccessible.**

Config

#BHAS @BlackHatEvents

## Slide 15

## **Bingo!**

Patch **The presence of patch implies the absence of vulnerability.**

##### **Kernel configs can be regarded as a graph. Kconfig and Kbuild mechanisms work in tandem to tailor the kernel.** Graph

#BHAS @BlackHatEvents

## Slide 16

## **OVERVIEW OF KERNJC**

- **Vulnerability Profiling:** Collect vulnerability information for later usage.

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025
=> Used by
Vulnerability
CVE Info —
Release info & Updating
¢ Vulnerability Profiling: Collect vulnerability information for later usage.
```

## Slide 17

## **OVERVIEW OF KERNJC**

- **Vulnerability Profiling:** Collect vulnerability information for later usage.

- • **Version Identification:** Perform patch operation to detect patch presence.

#BHAS @BlackHatEvents

## Slide 18

## **OVERVIEW OF KERNJC**

- **Vulnerability Profiling:** Collect vulnerability information for later usage.

- **Version Identification:** Perform patch operation to detect patch presence.

- • **Config Identification:** Build Kconfig graph and mine reachable configs.

#BHAS @BlackHatEvents

## Slide 19

## **OVERVIEW OF KERNJC**

- **Vulnerability Profiling:** Collect vulnerability information for later usage.

- **Version Identification:** Perform patch operation to detect patch presence.

- **Config Identification:** Build Kconfig graph and mine reachable configs.

- **Environment Provisioning:** Build the kernel and provision the virtual machine.

#BHAS @BlackHatEvents

## Slide 20

## **VULNERABILITY PROFILING**

Distro Vendors
Patch-affected Files
Patch Content
Patch
New CVE ID
Commit(s) Kernel Kernel
Archives Archives
NVD Description
Version Ranges
Kernel Archives
Vul Info CVSS Info
CWE Info New Version
New Version
Release
Reference Links

\```
cve: CVE-2022-0847
patch:
\```

\```
-9d2231c5d74e13b2a0546fee6737ee4446017903
\```

\```
diff --git a/lib/iov_iter.c b/lib/iov_iter.c
index b0e0acdf96c15e..6dd5330f7a9957 100644
---a/lib/iov_iter.c
+++ b/lib/iov_iter.c
@@ -414,6 +414,7 @@ static size_t
copy_page_to_iter_pipe(struct page *page,
size_t offset, size_t by
return 0;
buf->ops = &page_cache_pipe_buf_ops;
+   buf->flags = 0;
...
file: lib/iov_iter.c
\```

\```
Aflawwasfoundinthewaythe"flags"memberofthenewpipebuffer
structurewaslackingproperinitializationincopy_page_to_iter_pipeand
push_pipefunctionsintheLinuxkernelandcouldthuscontainstale
values.Anunprivilegedlocalusercouldusethisflawtowritetopagesin
thepagecachebackedbyreadonlyfilesandassuchescalatetheir
privilegesonthesystem.
\```

\```
v6.9.1
[v5.8,v5.10.102)v6.9.2
[v5.15,v5.15.25)v6.9.3
[v5.16,v5.16.11)+v6.9.4
...+v6.9.5
+v6.9.6
\```

#BHAS @BlackHatEvents

## Slide 21

## **VUL VERSION IDENTIFICATION**

if (len > PAGE_SIZE - 2 - size)
-
if (len > PAGE_SIZE - 2 - size)
1 st patch
+   if (size + len + 2 > PAGE_SIZE)
if (size + len + 2 > PAGE_SIZE)
-
2 nd patch if (len > PAGE_SIZE - 2 - size)
+   if (size + len + 2 > PAGE_SIZE)
Line deletion not found. Re-patching detected!

Vul Version
Patched Version
4 th check ✓
3 rd check ✗
2 nd check ✗
Patch
1 st check ✗
Vulnerability Related Files
Version
Claimed Version Range

###### Re-patching Operation

###### Identification Process

1. Apply the patch on vulnerable file

   1. Locate the latest vulnerable version _v_ claimed by NVD

- >>> The vulnerability is patched successfully

   2. Start from _v_ and move downwards along the kernel version list

2. Apply the patch once again

- >>> Fail to locate the vulnerable site

- Apply the patch on vulnerability related files of each version

- Stop when no re-patching occurs

#BHAS @BlackHatEvents

## Slide 22

## **VUL CONFIG IDENTIFICATION**

Locate direct configs in graph
Kconfig Graph
+
Code Path Desc

Identify hidden configs in graph

DDC (Direct Description-level Configs)
D (Direct Configs) DPC (Direct Path-level Configs)
DCC (Direct Code-level Configs)
Configs
HRC (Hidden Reachable Configs)
H (Hidden Configs) HSC (Hidden Configs with  select  Relation)
HDC (Hidden Configs with  depend  Relation)

###### Identification Process

1. Build the Kconfig graph for target kernel

Config
Direct Config
Hidden Config

2. Gather direct configs ( _D = DDC_ ∪ _DPC_ ∪ _DCC_ )

3. For each config _c_ in _D_

   - Locate _c_ in the Kconfig graph

   - Discover hidden configs for _c_ ( _Hc = HRC_ ∪ _HSC_ ∪ _HDC_ )

4. Collect all hidden configs

#BHAS @BlackHatEvents

## Slide 23

## **VUL CONFIG IDENTIFICATION**

###### **`CVE-2017-18344`**

###### **`CVE-2021-22555`**

\```
Thetimer_createsyscallimplementationin
kernel/time/posix-timers.cintheLinuxkernelbefore
4.14.8doesn'tproperlyvalidatethesigevent-
>sigev_notifyfield,whichleadstoout-of-boundsaccess
intheshow_timerfunction(calledwhen/proc/$PID/timers
isread).Thisallowsuserspaceapplicationstoread
arbitrarykernelmemory(onakernelbuiltwith
CONFIG_POSIX_TIMERSandCONFIG_CHECKPOINT_RESTORE).
\```

\```
#ifdef CONFIG_COMPAT
\```

\```
...
void xt_compat_target_from_user(...
\```

\```
...
target->compat_from_user(t->data, ct->data);
else
\```

\```
memcpy(t->data, ct->data, tsize -sizeof(*ct));
pad = XT_ALIGN(target->targetsize) -target->targetsize;
if (pad > 0)
\```

\```
memset(t->data + target->targetsize, 0, pad);
\```

###### **`CVE-2021-22555`**

\```
diff --git a/net/netfilter/x_tables.c b/net/netfilter/x_tables.c
index 6bd31a7a27fc58..92e9d4ebc5e8d7 100644
---a/net/netfilter/x_tables.c
+++ b/net/netfilter/x_tables.c
\```

\```
net/Makefile:           obj-$(CONFIG_NETFILTER)         += netfilter/
net/netfilter/Makefile: obj-$(CONFIG_NETFILTER_XTABLES) += x_tables.o
\```

###### Direct Config Examples

1. Description-level configs from CVE description of CVE-2017-18344

2. Path-level configs from patches for CVE-2021-22555

3. Code-level configs from vulnerable source code of CVE-2021-22555

#BHAS @BlackHatEvents

## Slide 24

## **VUL CONFIG IDENTIFICATION**

###### Manual Identification

###### KernJC’s Identification

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DDC (Direct Description-level Confi
— (Direct Description-level Configs)
Ny D (Direct Configs) DPC (Direct Path-level Configs)
Configs HRC (Hidden Reachable Configs)
H (Hidden Configs) HSC (Hidden Configs with select Relation)
val HDC (Hidden Configs with depend Relation)
Core Netfilter Configuration
```

## Slide 25

## **DOCKER-LIKE INTERACTION!**

#BHAS @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
DOCKER-LIKE INTERACTION!

[Terminal 1 - help]
$ ./kjc -h
usage: kjc [...

KernJC - A L...

optional argu...
  -h, --help...
  -v, --vers...

subcommands:
  {update,bu...
    update
    build
    start
    stop
    attach
    exec
    cp
    logs
    rm
    ps
    enter
    info            show info o...
    query           query a vul...

[Terminal 2 - build]
$ ./kjc build CVE-2016-10150
[*] Removing potential...
[+] Auto-selected kern...
[*] Initializ...
[*] Downloadi...
    100%|[progress bar]
[*] Decompres...
[*] Building...
[*] Applying...
[*] Loading...
[*] Generatin...
[*] Finding k...
[*] Building...
[+] Built kc...
[+] Found 37...
[*] Loading...
[!] Vuln conf...
[*] Merging...
[+] Applied custom con...
... kernel compilation ... output omitted ...
[+] Built kernel source code
[*] Preparing rootfs (...
[+] Env a30ebfa6f5747f...

[Terminal 3 - ps]
$ ./kjc [ps]
+--------------------+----------------
| ID
+-------
| a30ebf...
+-------

[Terminal 4 - info/query]
$ ./kjc ...
{'create...
  'cve': 'CVE-2016-10150',
  'ip': N...
  'kernel...
  'pid':
  'port':
  'status...

[Terminal 5 - start]
$ ./kjc start --enable-kvm a3
[*] Starting env a3
[+] Started env a30ebfa6f...

[Terminal 6 - exec]
$ ./kjc exec a3 /home/user/poc
Warning: Permanently added '[localhost]:10000' (ECDSA) to the list of known hosts.

[Terminal 7 - cp]
$ cd db/pocs/cve-2016-10150/; gcc -o poc poc.c -static; cd -
~/pjts/KernJC
$ ./kjc cp db/pocs/cve-2016-10150/poc a3:/home/user/
Warning: Permanently added '[localhost]:10000' (ECDSA) to the list of known hosts.
poc

[Terminal 8 - logs]
$ ./kjc logs -f a3
[  OK  ] Reached target (...
         Starting Update...
[  OK  ] Finished Update...

Debian GNU/Linux 11 kern...
... output omitted ...

[Terminal 9 - logs -f]
$ ./kjc logs -f a3
... output omitted ...
[  408.497181] ==================================================================
[  408.498170] BUG: KASAN: use-after-free in kvm_vm_ioctl+0x1150/0x1340 at addr ffff88006[clipped]
[  408.498170] Read of size 8 by task poc/2983
[  408.498170] CPU: 1 PID: 2983 Comm: poc Tainted: G    B          4.8.12 #1
[  408.498170] Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS 1.10.2-1ubuntu[clipped]
[  408.498170]  0000000000000097 ffff88006118faf0 ffffffff81bfe5a2 ffff88006cc018c0
[  408.498170]  ffff88006b8c9a20 ffff88006b8c9a60 ffffffff83a46400 ffff88006118fb18
[  408.498170]  ffffffff815c8cbc ffff88006118fba8 ffff88006b8c9a20 ffff88006cc018c0
[  408.498170] Call Trace:
... output omitted ...

[Terminal 10 - attach]
$ ./kjc attach a3
... output omitted ...
user@kernjc:~$ su # password: neo
Password:
root@kernjc:/home/user#
Adding user `user' to gr...
Adding user user to grou...
Done.

[Terminal 11 - rm]
$ ./kjc rm --force a3
[+] Env a30ebfa6f5747fa9 removed
```

## Slide 26

## **DEMO**

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 72/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025 we”
@ iterm2 Shell Edit View Session Scripts Profiles Toolbelt Window Help o09<« 8 8 G14 QF @ &B 647
Cvenv) > KernJC git:(Cmain) x ./kjc build CVE-2021-22555
[*] Building environment for CVE-2021-22555
```

## Slide 27

## **EXPERIMENTAL RESULTS**

###### Reproduction Performance

RwKC: Reproducibility with KernJC-identified Configs RwDC: Reproducibility with Default Configs FPV: False Positive Version claims in NVD

|**CVE**|**RwKC?**|**RwDC?**|**FPV?**|**CVE**|**RwKC?**|**RwDC?**|**FPV?**|**CVE**|**RwKC?**|**RwDC?**|**FPV?**|**CVE**|**RwKC?**|**RwDC?**|**FPV?**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|2016-10150||✗|✗|2018-12233||✗|✗|2020-27194||✗|✗|2021-3490|||✗|
|2016-4557||✗|✗|2018-5333||✗|✗|2020-27830||✗|✗|2021-3573||✗||
|2016-6187||✗|✗|2018-6555||✗|✗|2020-28941||✗|✗|2021-42008||✗|✗|
|2017-16995||✗|✗|2019-6974||✗|✗|2020-8835||✗|✗|2021-43267||✗|✗|
|2017-18344||✗|✗|2020-14381||||2021-22555||✗||2022-0995||✗|✗|
|2017-2636||✗|✗|2020-16119||✗|✗|2021-26708||✗|✗|2022-1015||✗|✗|
|2017-6704||✗|✗|2020-25656||||2021-27365||✗|✗|2022-25636||✗|✗|
|2017-8824||✗|✗|2020-25669||✗|✗|2021-34866||✗|✗|2022-32250||✗|✗|
|||||2022-34918||✗|✗|2023-32233||✗|✗|||||

- ➢ KernJC successfully builds reproduction environments for all 66 vulnerabilities.

- ➢ 4 of 66 are detected to have incorrect (FP) version claims in NVD.

- ➢ 32 of 66 need non-default configs identified by KernJC to be activated.

#BHAS @BlackHatEvents

## Slide 28

## **EXPERIMENTAL RESULTS**

###### Vulnerability Config Identification Statistics

|**CVE**|**Subsystem**|**DDC**|**DPC**|**DCC**|**HRC**|**HSC**|**HDC**|**CVE**|**Subsystem**|**DDC**|**DPC**|**DCC**|**HRC**|**HSC**|**HDC**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|CVE-2016-10150|KVM|0|1|0|39|0|4|CVE-2020-28941|Accessibility|0|2|0|19|0|0|
|CVE-2016-4557|eBPF|0|1|0|0|2|0|CVE-2020-8835|eBPF|0|1|0|0|2|1|
|CVE-2016-6187|AppArmor|0|1|0|14|0|2|CVE-2021-22555|Netfilter|0|7|1|10|3|406|
|CVE-2017-16995|eBPF|0|1|0|0|2|0|CVE-2021-26708|VSOCK|0|1|0|4|0|6|
|CVE-2017-18344|Time|2|0|0|3|0|3|CVE-2021-27365|SCSI|0|2|0|22|8|0|
|CVE-2017-2636|TTY|0|1|0|17|0|0|CVE-2021-34866|eBPF|0|1|0|0|2|3|
|CVE-2017-6074|DCCP|0|1|0|9|0|0|CVE-2021-3490|eBPF|0|1|0|0|2|2|
|CVE-2017-8824|DCCP|0|1|0|9|0|0|CVE-2021-3573|Bluetooth|0|1|0|32|0|45|
|CVE-2018-12233|JFS|0|1|0|4|0|4|CVE-2021-42008|NET|0|2|0|18|0|14|
|CVE-2018-5333|RDS|0|1|0|9|0|3|CVE-2021-43267|TIPC|0|1|0|5|0|4|
|CVE-2018-6555|IRDA|0|2|1|7|0|37|CVE-2022-0995|WQ|0|1|1|0|0|1|
|CVE-2019-6974|KVM|0|1|0|42|0|4|CVE-2022-1015|Netfilter|0|1|0|4|0|241|
|CVE-2020-16119|DCCP|0|1|0|5|0|0|CVE-2022-25636|Netfilter|0|4|0|19|2|241|
|CVE-2020-25669|Input|0|3|0|3|37|3|CVE-2022-32250|Netfilter|0|1|0|4|0|238|
|CVE-2020-27194|eBPF|0|1|0|0|2|1|CVE-2022-34918|Netfilter|0|1|0|4|0|238|
|CVE-2020-27830|Accessibility|0|2|0|19|0|0|CVE-2023-32233|Netfilter|0|2|0|5|0|317|

#BHAS @BlackHatEvents

## Slide 29

## **EXPERIMENTAL RESULTS**

###### Vulnerabilities with FP Version Range Claims in NVD (TOP 10)

###### We identify 128 vulnerabilities with incorrect version claims in NVD.

The aggregate count of incorrect (FP) versions is 3,042.

Averaging 24 incorrect versions per identified vulnerability.

|**CVE**|**CVSS**|**FP Version Range**|**Vulnerable Version**|**FP Count**|
|---|---|---|---|---|
|CVE-2017-1000407|7.4|v4.14.6 – v4.14.325|v4.14.5|320|
|CVE-2017-18216|5.5|v4.14.57 – v4.14.325|v4.14.56|269|
|CVE-2017-18224|4.7|v4.14.57 – v4.14.325|v4.14.56|269|
|CVE-2020-35508|4.5|v5.9.7 – v5.11.22|v5.9.6|229|
|CVE-2021-4002|4.4|v5.15.5 – v5.15.132|v5.15.4|128|
|CVE-2021-4090|7.1|v5.15.5 – v5.15.132|v5.15.4|128|
|CVE-2022-0264|5.5|v5.15.11 – v5.15.132|v5.15.10|122|
|CVE-2021-4155|5.5|v5.15.14 – v5.15.132|v5.15.13|119|
|CVE-2016-10906|7.0|v4.4.191 – v4.4.302|v4.4.190|112|
|CVE-2015-4170|4.7|v3.12.7 – v3.13.3|v3.12.6|72|

#BHAS @BlackHatEvents

## Slide 30

KERNJC

Source: ChatGPT

KernJC = Kernel _<u>JiaoChang JiaoChang</u>_ , in ancient China, referred to a site dedicated to military training and competition.

Jiao Chang /dʒaʊ tʃɑ:ŋ/

_<u>https://github.com/NUS-CURIOSITY/KernJC</u>_

#BHAS @BlackHatEvents
