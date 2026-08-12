---
title: "Out Of Control How KCFG and KCET Redefine Control Flow Integrity in the Windows Kernel"
speakers: ["Connor McGarr"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Connor McGarr_Out Of Control How KCFG and KCET Redefine Control Flow Integrity in the Windows Kernel.pdf"
pages: 36
sha256: "3e962abddc37b370f79a7f7172ed3e731efaeefb53456822adac407dd8ecc26b"
text_chars: 19210
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T22:51:50Z"
---
# Out Of Control How KCFG and KCET Redefine Control Flow Integrity in the Windows Kernel

**Speakers:** Connor McGarr  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Connor McGarr_Out Of Control How KCFG and KCET Redefine Control Flow Integrity in the Windows Kernel.pdf` (36 pages)


## Slide 1

# Out Of Control: How KCFG and KCET Redefine Control Flow Integrity in the Windows Kernel

Connor McGarr [@33y0re] Software Engineer, Prelude Security

#BHUSA @BlackHatEvents

## Slide 2

## About

- Software Engineer at Prelude Security

   - Previously Software Engineer at CrowdStrike on the Windows Sensor Team

- Blog: connormcgarr.github.io

   - Windows OS internals, exploit mitigations, browser and kernel exploitation, malware, reverse engineering articles

- I like C, Assembly, Operating Systems, and Hypervisors!

#BHUSA @BlackHatEvents

## Slide 3

## Introduction To Control Flow Integrity

- Most exploits require two things:

   1. Ability to hijack the legitimate execution (control flow) of an application/operating system

   ~~2. Use the above primitive to execute some malicious code~~

- Control Flow Integrity (CFI) attempts to address the first problem by verifying and mitigating attempts to alter the target of a control-flow transfer

   - Calls/jmps are forwards-edge control-flow transfers

   - Returns are backwards-edge control-flow transfers

#BHUSA @BlackHatEvents

## Slide 4

## Control Flow Guard

- Control Flow Guard is Window’s version of forwards-edge CFI

   - Present in user-mode since Windows 8.1 (as an optional update)

- All indirect call targets which are known at compile-time are stored in a read-only, kernelprotected (and per-process) “CFG bitmap”

   - User-mode address space is 128 TB on 64-bit Windows

   - …there are 128 TB of possible call targets (in theory), but the compiler _should_ generate call targets at 16-byte (0x10) boundaries

      - 128 TB / 16 bytes = 8 TB of potential targets

      - 8 TB * 2 bits (denotes the “state” for every 16 bytes) = **2 TB CFG bitmap size**

      - Memory manager performs some optimizations…

   - Indirect call/jmps are replaced with “thunks” that first check the CFG bitmap for bits related to the call target before transferring execution

#BHUSA @BlackHatEvents

## Slide 5

## Control Flow Guard

- CFG bitmap states

   - 0, 0 -> No valid function present in these 16 bytes

   - 1, 0 -> A valid function (16-byte aligned)

   - 1, 1 -> A valid function (not 16-byte aligned)

   - 0, 1 -> This target is explicitly suppressed (special “export suppression” feature)

- We need 2 bits instead of just 1

   - Compilers should generate functions at 16-byte boundaries there is no guarantee

   - Instead of 1 bit for true/false, 2 bits allows us to encapsulate more information (such as 16byte alignment validity)

#BHUSA @BlackHatEvents

## Slide 6

## Control Flow Guard

1. Corrupt VFTABLE with ROP gadget

1. Corrupt VFTABLE with ROP gadget

jmp rax (rop_gadget)
3. Decision
int 29 (__fastfail)

2. Invoking Func4() executes the gadget

After CFG

**Before CFG**

#BHUSA @BlackHatEvents

## Slide 7

## Backwards-Edge CFI On Windows

- Although CFG did have an impact on exploitation attackers started to just avoid CFG entirely

   - One example of this was reverting to return address corruption (not using a stack overflow primitive) – indicating that a comprehensive CFI solution requires protection of both forwardsedge **_<u>AND</u>_** backwards-edge control-flow

   - Microsoft began by attempting a software-based implementation of backwards-edge CFI called Return Flow Guard (RFG) but deprecated it due to discoveries by their internal red team

- Intel Control-Flow Enforcement Technology (CET) is a hardware solution used by Windows to provide a backwards-edge CFI solution (Windows also supports AMD Shadow Stack)

   - Present in user-mode since Windows 10 19H1 (1903)

   - Windows only uses the Shadow Stack feature of CET

#BHUSA @BlackHatEvents

## Slide 8

## Intel Control-Flow Enforcement Technology

- Intel CET maintains a “shadow stack” containing only return addresses

   - Protected by the kernel, “immutable” to a user-mode attacker

- “call” instructions now also push a return address onto the shadow stack

   - “ret” instructions pops the return address off the shadow stack and compares it with the “traditional” stack’s in-scope return address

   - Mismatch causes a control flow protection fault interrupt (int #21)

call

**ret**

#BHUSA @BlackHatEvents

## Slide 9

## CFG/CET – Kernel-Mode Counterparts

- You may have noticed a few themes so far…

   1. Both CFG and CET are based on a particular “source of truth”

      - CFG bitmap, CET shadow stack

   2. Both sources of truth are protected by the kernel

      - If an attacker wants to modify these sources of truth, they need to ask the kernel to do so (VirtualProtect system call, etc.)

         - There is a user <-> kernel security boundary

- …but what if we wanted to implement CFG and CET in the kernel?

   - If the kernel is the most privileged part of the OS there is no higher “boundary” to ask, an attacker with a kernel-mode read/write primitive can first just corrupt the source of truth and THEN detonate their exploit!

#BHUSA @BlackHatEvents

## Slide 10

1. Make KCFG bitmap page(s) writable
2. Mark the ROP gadget as a valid call target
3. Leak the g_FptrArray, corrupt it with the
ROP gadget, and coherce the kernel to
invoke g_FptrArray[5]() User mode
Kernel Mode

#BHUSA @BlackHatEvents

## Slide 11

## A Higher Security Boundary – Hyper-V

- Luckily for us there IS a higher security boundary on Windows – Microsoft’s hypervisor!

- About a decade ago now (hard to believe!) Microsoft implemented Virtualization-Based Security, or VBS, which is a suite of hypervisor-provided security features

   - “Secured-Core” PCs from Microsoft have many VBS features enabled by default

   - Clean installs of Windows 11 do as well!

- With the implementation of VBS we finally can provide CFG and CET mitigations in the Windows kernel to defend against kernel attackers with a read/write primitive!

#BHUSA @BlackHatEvents

## Slide 12

## Virtualization-Based Security

- VBS leverages Second Level Address Translation (SLAT) to enforce various policies/permissions which cannot be altered even by an attacker with kernel mode exploitation primitives

   - Does this by constructing the concept of “Virtual Trust Levels” which are an isolated region of physical memory (like a VM*)

      - VTL 0 – “Normal world” – What a user interfaces with

      - VTL 1 – “Secure world” – Configures VTL 0 security

- Example – Kernel Data Protection (KDP)

   - Sets a read-only Extended Page Table Entry (EPTE) on a target region(s) of memory

   - An attacker even with a kernel-mode read/write primitive cannot make the page(s) writable because the hypervisor manages the true source of truth for the permission of the target page(s) (EPTEs) (which is _not_ accessible by the NT kernel!)

#BHUSA @BlackHatEvents

## Slide 13

1. Make protected memory writable (PTE level)

2. Write to the protected memory

User mode

### Kernel mode

3. PTE is writable, but EPTE **_<u>STILL</u>_** says readonly! Fatal EPT violation

Hypervisor (Hyper-V)

#BHUSA @BlackHatEvents

## Slide 14

## Virtualization-Based Security

- We can now guarantee the sources of truth for KCFG and KCET are immutable!

   - However, it is not as simple as “just shove CFG and CET in kernel-mode” (which is a primary reason for later adoption than their user-mode counterparts)

- Example – when certain actions occur in the context of a “guest” (VM), a VM Exit may occur to allow the hypervisor to inspect the operation

   - VM Exit is like a context switch but instead of switching into a new thread it involves a switch of execution from “guest” mode to “hypervisor” mode (such as an EPT violation or VMCALL)

      - This is not a free operation – engineers need to consider many such scenarios (this is why the KM implementation of these mitigations is complex in many cases)

- With this in mind, let’s now examine how CFG and CET are implemented in the Windows kernel!

#BHUSA @BlackHatEvents

## Slide 15

## Kernel Control Flow Guard

- Kernel Control Flow Guard (KCFG)

   - Present since Windows 10 1703 (RS2)

   - Fully enabled under Hypervisor-Protected Code Integrity

#BHUSA @BlackHatEvents

## Slide 16

## Kernel Control Flow Guard

- The NT kernel is responsible for asking the Secure Kernel to initialize KCFG as part of system initialization ( **nt!VslInitializeSecureKernelCfg** -> **securekernel!SkmmInitializeNtKernelCfg** ) via secure system call

#BHUSA @BlackHatEvents

## Slide 17

## Kernel Control Flow Guard

- On Kernel CFG initialization the Secure Kernel tracks the region of memory associated with the KCFG bitmap through a structure known as a Normal Address Range (NAR)

   - SK maintains a two kinds of NARs, “normal” NARs (associated with a KM virtual address executable range) and “static” NARs

   - KCFG bitmap, shadow stacks, and a few other regions of memory are static NARs because they are not associated with an image but require management by the Secure Kernel

#BHUSA @BlackHatEvents

## Slide 18

## Kernel Control Flow Guard

- After the Secure Kernel is enlightened with the KCFG bitmap range each kernel image load will result in (generally) these steps:

   1. Allocate and map memory in the KCFG bitmap range

   2. Mark the new mapping as read-only in the EPTEs (Bitmap cannot be corrupted from VTL 0)

   3. Update the KCFG bitmap with the appropriate bit states for all KCFG-protected call targets provided by the image ( **securekernel!RtlSetBits** )

Hypercall to set read-only SLAT entry for VTL 0

HV_MAP_GPA_READABLE

#BHUSA @BlackHatEvents

## Slide 19

## Kernel Control Flow Guard

- In addition to load image operations there are also special circumstances where the KCFG bitmap may need to be updated

   - Example – calling **nt!MmGetSystemRoutine** marks the target function as a valid call target

#BHUSA @BlackHatEvents

## Slide 20

## Kernel eXtended Control Flow Guard (KXFG)

- One of the **_<u>known</u>_** limitations of CFG is that it only validates a target exists anywhere in the bitmap, not that the target is the intended one (coarse-grained CFI)

   - Example – Call targets in Win32k can be corrupted with a valid NT call target

- eXtended Control Flow Guard (XFG) was an attempt to address this (fine-grained CFI)

   - Each indirect call has an additional check (the hash of its prototype). The intent was to limit valid call targets from anything in the bitmap to only developer-intended functions

   - XFG was never fully instrumented (UM/KM) and is now deprecated 

#BHUSA @BlackHatEvents

## Slide 21

## Kernel Control Flow Guard

- KCFG in its current state (no XFG) works just like “traditional” CFG, but recent changes (since 24H2) due to a feature called “hot patching” have slightly altered mechanics

   - **nt!KscpCfgDispatchUserCallTargetEs[No]Smep** is the new dispatch function, and it is now made through a _direct_ call (no longer called indirectly via IAT)

- Other interesting notes

   - KCFG acts as a “software SMEP” – meaning even when HVCI is **<u>DISABLED</u>** (which means KCFG is also not fully enabled) KCFG will _still_ validate that kernel-mode indirect calls never invoke a user-mode address (even with U/S bit set to supervisor in the PTE!)

   - Import Address Table (IAT) indirect calls are explicitly documented as not protected by (K)CFG – and this has been abused by attackers! Since this is the case, not even XFG could help…

#BHUSA @BlackHatEvents

## Slide 22

1. Make IAT writable (HVCI is not applicable here)
2. Arbitrary write primitive to corrupt the IAT
3. Invoke the import (executes the
ROP gadget)
User mode
Kernel mode

#BHUSA @BlackHatEvents

## Slide 23

## Kernel Control Flow Guard

- In the case of IAT abuse KCFG can be “combined” with a mitigation known as Retpoline (developed by Google) which mitigates Specter Type 2 (CVE-2017-5715)

   - KM images can use Retpoline with undocumented **/guard:retpoline** and **/d2guardretpoline** linker and compiler flags

- Retpoline does many things, but importantly for us it replaces indirect IAT calls with _direct_ calls to a special Retpoline dispatch function (which in 99% of cases, via “import optimization”, just calls the target directly)

   - Even though newer CPUs do not use Retpoline (Indirect Branch Restricted Speculation, IBRS), import optimization is still always available and Windows images still use it, even when <u>Retpoline is not enabled!</u>

#BHUSA @BlackHatEvents

## Slide 24

## Kernel Control Flow Guard

- No more reading call targets from the IAT!

- You must be “eligible” for import optimization

   - Both the caller and callee must be from images compiled with **/guard:retpoline** and **/d2guardretpoline**

• Caller and callee must be within 2 GB of each other

#BHUSA @BlackHatEvents

## Slide 25

## Kernel Control Flow Guard

- But what if attackers wanted to use return address corruption to circumvent KCFG?

   - Example: An attacker-controlled thread is suspended, the stack is corrupted, and on thread resume a ROP gadget is invoked

Before stack corruption

After stack corruption (breakpoint ROP gadget reached)

#BHUSA @BlackHatEvents

## Slide 26

## Kernel CET

- That’s where KCET comes in! KM return addresses are now protected!

   - Available since Windows 11 22H2 and, as is the case with KCFG, HVCI is required

#BHUSA @BlackHatEvents

## Slide 27

## Kernel CET

- The “kernel shadow stack” region of memory ( **MiVaKernelShadowStacks** ) is maintained by NT

   - Secure system call is made to SK to mark the shadow stack pages as read-only (plus a special “supervisor shadow stack bit” leveraged by an Intel feature called “Supervisor Shadow-Stack Control”) in the EPTEs

      - We will talk about Shadow-Stack Control later!

#BHUSA @BlackHatEvents

## Slide 28

## Kernel CET

- Each shadow stack (also referred to as SS) receives a static NAR, but there is caching/re-use logic to not incur the cost of SK interaction on every stack creation

   - Two caches: A per-processor (PRCB) and a per-NUMA node cache (both are managed by NT). If “ideal”, on stack deletion, shadow stacks are sent to one of these caches

   - “Slow” path results in calling into SK

#BHUSA @BlackHatEvents

## Slide 29

## Kernel CET

- On both “re-use” from the cache and the slow path the KTHREAD object is updated with the target shadow stack (including other values like shadow stack type)

   - In the “cached” path the backing PFN structure also has its “shadow stack owner data” updated (for debugging/info purposes)

#BHUSA @BlackHatEvents

## Slide 30

## Kernel CET

- …but before we update the thread object the Secure Kernel is responsible for first doing a few things (through the previously-mentioned secure system call), depending on the type of SSS which needs to be created:

   1. Marking the region as read-only (and as supervisor shadow stack, also referred to as SSS) in the EPTEs

   2. Configuring the “shadow stack token”

      - The token is used to validate the shadow stack and denote the state (busy/free)

         - A “restore” token can also be used in conjunction w/ rstorssp/saveprevssp instructions

         - Context switch pattern for SSS: After the Secure Kernel makes the SSS immutable in VTL 0, the restore token from the SSS associated with the new thread’s thread object is used to update the SSP in VTL 0 (note that winnt.h specifies CET_S XSAVE area is not used by NT!)

   3. Initializing the return address

#BHUSA @BlackHatEvents

## Slide 31

## Kernel CET

- One of the main engineering hurdles with KCET is writes to the shadow stack (SS)

   - “Ordinary” data-writes (like mov) are not a problem (without SLAT/hypervisor) – WRSSQ is also only enabled in audit and/or debug mode (undefined instruction otherwise!)

   - PML4 -> PD paging structures are writable, PTE is read-only + dirty bit set

      - “Special” combination of PTE states which denote this is a SS page (thus disallowing data writes)

   - But what about with SLAT? KCET is only enabled when HVCI is!

      - How does the hypervisor know what pages are SSS pages (Hypervisor uses EPTEs!)

      - If the SS is read-only in the VTL 0 EPTEs this would result in an EPT violation (incurring a VM exit)

   - We can use our “special” SSS bit we talked about earlier! Supervisor Shadow-Stack Control to the rescue!

#BHUSA @BlackHatEvents

## Slide 32

## Kernel CET

- The Supervisor Shadow-Stack Control feature uses a special “SSS bit” in the EPTEs to address our problems (and provide more security!)

   - Allows the hypervisor to denote SSS pages

   - As we know VTL 0, via secure system call, tells VTL 1 about pages that need to be marked as SSS

   - • EPT PML4 -> EPT PT (all extended paging structures) have the read bit set, EPT PML4 -> EPT PD have the write bit set, and the EPT PT (EPT PTE) has the SSS bit set

      - Just like in the “without the hypervisor” scenario, this combination of PTE states allows legitimate shadow-stack writes but not ordinary writes (mov, etc. – no EPT violation!)

   - Enforces that shadow-stack accesses cannot occur to a non-shadow stack page (prevents attackers re-mapping SSS pages to arbitrary non-SSS pages via PTEs to construct fake SSs)

- Windows is the only platform leveraging this today!

#BHUSA @BlackHatEvents

## Slide 33

## Kernel CET

- KCET needs to handle other legitimate SSS updates (like returning from an exception)

   - But we don’t want to let VTL 0 handle this. The solution is to let the Secure Kernel do it! • CET MSRs allow the CPU to load SS values when a privilege level switch occurs (IA32_PLX_SSP) _and_ when a hypervisor <-> guest context switch happens (VMX_GUEST_SSP)!

      - VM Entry controls defined by VTL 0’s VMCS allows us to use the VMX_GUEST_SSP MSR value to populate the SSS on context switch (VMENTRY) back into VTL 0 (after the Secure Kernel returns)

   - During “assist”, opportunistic checks are done as well, such as validating that RIP exists in an executable code region within a known kernel image tracked through a NAR in SK

#BHUSA @BlackHatEvents

## Slide 34

## Kernel CET

- Other interesting notes

   - The CPU will fault (obviously) if the return addresses mismatch, but the interrupt handler on Windows will still allow a return into a different return address – so long as that return address is also on the shadow stack! (VTL 1 handles updating the SSP if this occurs)

f

#BHUSA @BlackHatEvents

## Slide 35

## Conclusions

- KCET has only been available for a short time on Windows –execution research w/ both KCFG and KCET enabled is still limited

   - Most public research still revolves around known limitations in KCFG (JOP, COOP, calling other valid call targets) because IBT is not leveraged by Windows

- KCET seems to be the stronger of the two (hardware-enforced)

   - Out-of-context calls (calling into other valid SSP values) is an interesting vector for research!

- Remapping attacks are still possible

   - HLAT mitigates this (and is now available in 24H2!)

- The presence of HVCI, KCFG and KCET raises the bar for attackers, while also outright mitigating some primitives!

- It will be fun to see the “cat-and-mouse” game which follows!

#BHUSA @BlackHatEvents

## Slide 36

## Thank You!

- Greetz & shout-outs!

   - Alan Sguigna, Alex Ionescu, Andrea Allievi (special shout-out!), Satoshi Tanda, Yarden Shafir

- Additional resources

   - Yarden Shafir – OffensiveCon 23: https://www.youtube.com/watch?v=YnxGW8Fvqvk&t=751s

   - https://tandasat.github.io/blog/2025/04/02/sss.html

   - https://cdrdv2-public.intel.com/782161/326019-sdm-vol-3c.pdf

   - https://www.sstic.org/media/SSTIC2025/SSTICactes/windows_kernel_shadow_stack_mitigation/SSTIC2025-Articlewindows_kernel_shadow_stack_mitigation-aulnette_jullian.pdf

#BHUSA @BlackHatEvents
