---
title: "Architecture Analysis of VMProtect 3.8 Demystifying the Complexity"
speakers: ["Holger Unterbrink"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Holger Unterbrink_Architecture Analysis of VMProtect 3.8 Demystifying the Complexity.pdf"
pages: 58
sha256: "d4d815530ea835badaf960397701daea15ad405a47765ad73136ae08757799d6"
text_chars: 26375
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.9
ocr_unreliable_blocks: 12
ocr_timeouts: 0
pages_recovered_from_text_layer: 2
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:17:25Z"
---
# Architecture Analysis of VMProtect 3.8 Demystifying the Complexity

**Speakers:** Holger Unterbrink  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Holger Unterbrink_Architecture Analysis of VMProtect 3.8 Demystifying the Complexity.pdf` (58 pages)


## Slide 1

Architecture Analysis of VMProtect 3.8

Holger Unterbrink

## Slide 2

## Who am I ?

Holger Unterbrink @hunterbr72

Technical leader -  Security Researcher at Cisco Talos

Malware Analysis, Threat hunting, Tool development and lately Big Data/Machine Learning Won the IDA plugin contest 2020 with the Dynamic Data Resolver Instrumentation Plugin

Germany

## Slide 3

## Disclaimer

**Question:** What is the goal of the talk ?

**?**

Answer: Demystify the Virtual Machine of VMP. Get a starting point for own research.

**Question:** Can I crack VMProtect protected real world samples after the talk ?

Answer: Most likely, NO. Depends on the time you have and the VMP settings used.

**Question:** Will I be able to understand how the Virtual Machine work after the talk ? Answer: Yes, I hope so.

**Question:** Why should I spend time on VMProtect ? Answer: VMProtect 3.5 Source code leaked and VMProtect 3.8 binary, too.  Latest version on 27<sup>th</sup> June is 3.8.8

## Slide 4

# Other research on VMProtect

**Inside VMProtect (** Samuel Chevet) <u>https://webtv.univ-lille.fr/video/7566/inside-vmprotect (</u> **2015)**

**VMProtect 2 - Detailed Analysis of the Virtual Machine Architecture** <u>https://blog.back.engineering/17/05/2021/ (2021) https://blog.back.engineering/21/06/2021/</u>

**VMProtect 3.5: Virtualization-Based Software Obfuscation** <u>https://www.mitchellzakocs.com/blog/vmprotect3 (2021)</u>

**VMProtect 3.x Devirtualization** <u>https://github.com/JonathanSalwan/VMProtect-devirtualization (~2022)</u>

## Slide 5

# Other research on VMProtect

How To Unpack VMProtect Malware (Paid - VMProtect 3 – Targets only misconfigured VMP protected malware) <u>https://www.patreon.com/posts/how-to-unpack-1-61634765</u>

**AllThingsIDA’s Poor man's guide to de-obfuscating VMProtect’s 32bit import obfuscation  (2023)** <u>https://www.youtube.com/watch?v=ZhQUbjFbsTw https://www.youtube.com/watch?v=uxOVbG-azIA https://www.youtube.com/watch?v=GvWSa6HTlNY</u>

**Analyzing Mutation-Coded - VM Protect and Alcatraz (2024)** <u>https://keowu.re/posts/Analyzing-Mutation-Coded-VM-Protect-and-Alcatraz-English/</u>

## Slide 6

Intro

## Slide 7

## VMProtect

#### VPN to Singapore


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMProtect
VPN to Singapore
VMProtect Overview Purchase
Complete solution
to software protection
Secure your code against reverse engineering, analyzing, and
cracking. Use the advantage of|code virtualization) which
executes virtualized fragments of code on several virtual
machines embedded into the protected application.
```

## Slide 8

## VMProtect

Looks like they are also effected by the recent geo political issues – No Love for the West anymore

<u>https://vmpsoft.com/</u>

## Slide 9

Pricelist


> Recovered by OCR — confidence 93/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pricelist
For Individuals
Lite Professional
+1 year of free +1 year of free
updates updates
All the features in Lite,
and more:
Obfuscation features:
For Companies
© Ultimate
+1 year of free
updates
Allthe features in
Professional, and more:
1 additional year
of updates
Renewal of updates for
```

## Slide 10

How does it work ?

## Slide 11

## VMProtect 3.8 GUI – Compilation Type

#### Translation of CISC code to a RISC Virtual Machine

Original Intel code Complex Instruction Set Computing (CISC) instruction will be translated to multiple virtualized instructions VMProtect VM uses Reduced Instruction Set Computing (RISC) e.g. inc eax v_add(v_reg, 1) e.g. dec eax v_add(v_reg, -1) e.g. lea ecx, [esp + ebx * 8 + 23] … multiple RISC instructions

Order

## Slide 12

## Very very simplified architecture More or less a chain of VMHandlers

Main Switch
1. 4.
2. 3.
5. 6.
VMHandler 1 VMHandler 2 VMHandler 3
VMHandler 4

## Slide 13

# Very simplified VM Architecture – Stack Machine

#### But a bit more technical…

VMHandlerTable

Fetch VMHandler e.g. v_add() Decode

Execute

## Slide 14

Virtual Machine Protection


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Virtual Machine Protection
* Instances - this options allows to specify the] number of the virtual machine|copies (the default value is 10). Each
virtual machine will have unique set of properties (different registers positions, different bytecode direction,
different handlers of commands, etc.) that makes harder the analysis and hacking of virtualized code.
¢ Complexity - this options allows to specify [the probability of creating complex handlers (consisting of several
simple handlers) {inside the virtual machine. This option also greatly complicates the analysis and hacking of
virtualized code. As the complexity increases, the size of the protected file also increases.
```

## Slide 15

## VMProtect 3.8 GUI – Complexity and Instances

Default = 10 None, 1% , 10%, 20%, 100%


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VMProtect 3.8 GUI — Compl
¥ Virtual Machine
¥ Functions for Protection
Version Default
New markers and strings Instances 1 Default = 10
Complexity 100% None, 1% , 10%, 20%, 100%
Licenses ¥ File
Files Memory Protection No
Import Protection No
Resource Protection No
Pack the Output File No
Output File Z:\VMprotect\vs\t2\Asm2\x64\Release\complexity_check\Asm2-10diff-instr.vmp-c100-i1.exe
¥ Detection
Debugger
Virtualization Tools
¥ Additional
Segments
Strip Debug Information
A debugger has been found running in your system.
Debugger Found Please, unload it from memory and restart your program.
Virtualization Tools Found Sorry, this application cannot run under a Virtual Machine.
File corrupted! This program has been manipulated and maybe
it's infected by a Virus or cracked. This file won't work anymore.
This code requires valid serial number to run.
Program will be terminated.
File Corrupted
Serial Number Required
HWID Mismatched This application cannot be executed on this computer.
ty ¥ Licensing Parameters
Output file size is 290304 bytes (2465%)
```

## Slide 16

VMP 3.5

# Licensed vs. Unlicensed Versions

Demo or unregistered version

Licensed version with random register assignment


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Licensed vs.
Unlicensed
Versions
if
#tifdef DEMO VMP 3.5
(true)
#else
(ctx.options.flags & cpUnregisteredVersion)
#endif
crypt_registr_ = (ctx.options.flags & cpEncryptBytecode) ? regEBX : 0;
pcode_registr_ = regESI;
stack_registr_ = regEBP;
if (type_ == vtAdvanced) Demo or
jmp_registr_ = regEDI; j
else if (cpu_address_size == osQWord) unregistered
jmp_registr_ = regR11; version
else
jmp_registr_ = 0;
else {
work_registr_List .push_back(regEBX) ;
work_registr_List . push_back(regEBP) ;
work_registr_lList .push_back(regEST) ;
if (cpu_address_size == osQWord) {
}
crypt_registr_ = 0;
if (ctx.options.flags & cpEncryptBytecode) {
if (cpu_address_size == osDWord) {
crypt_registr_ = regEBX;
}
Licensed version
with random register
assignment
else
crypt_registr_ = work_registr_list .GetRandom();
}
pcode_registr_ = work_registr_list .GetRandom();
stack_registr_ = work_registr_List .GetRandom();
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
jmp_registr_ = (type_ == vtAdvanced || cpu_address_size == osQWord) ? work_registr_list.GetRandom() :
```

## Slide 17

Main-Function after protection


> Recovered by OCR — confidence 72/100 on the text kept, 57/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Main-Function after protection
:0000000140001000 main proc near 3 CODE XREF: __scrt_common_main
:@8@0080140001000 arg_8 = qword ptr 10h
:0800000140001006 mov rbp, rsp
:@@20000140001009 sub rsp, 20h
:000000014900100D push rax
. . : :000000014000100E push rex
:@@20000140001017 [rax-4Fh], ch
:@@0000014000101A i al, dx
int main() :@@@0000140001020
VMProtectBegin("Test marker"); pounapeeeooospenanenes
. : :0000000140001035 qword ptr [rsp+@]
VMProtectEnd() ; . :0@00000140001039
dq @A5@D8D485859B7C1ih
:0000000140001062 call $+5
```

## Slide 18

# Main-Function after protection

##### Anti-Disasm not fixed

##### Anti-Disasm fixed

call/jmp to VMP Section

Code trace


> Recovered by OCR — confidence 72/100 on the text kept, 54/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Main-Function after protection
Anti-Disasm not fixed Anti-Disasm fixed
:@@00000140001000 proc near ; _scrt_common_main_seh+107 - text :0800000140001088 main proc near 3 CODE XRE
:0000000140001000 arg = qword ptr 1@h 10000000140001000 arg 8 = qword ptr 10h
:@00000014000100D push rax : :000000014000100E push rex .
:@08000014000100E push rex . :00000014000100F call/jmp to VMP Section
:0000000140001014 xchg ah, [rbx+0]
:0000000140001017 add [rax-4Fh], ch
:000000014000101A in al, dx
:000000014000101B sub eax, @F7489C7Fh
:000000014000101E test | qword ptr [rsp+8], OFFFFFFFFF834D52Fh
setb byte ptr [rsp+3]
:@000000140001039 0 :0000000140001044 loc_140@@1044: 3 CODE XREF: main+Ftp
10@0000014600103A rsp, [rsp+1eh] : :0000000140001044 push rbx
:@0@0000140001044 loc_140001044: ; CODE » : main+Ftp ee on
:@0@0000140001044 rbx
```

## Slide 19

".vmp0"

Detect it easy !

… but things can be different, depending on the VMP settings!


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Asm2_single_instr-c1-i1.wmp.e
Name Virtual Size Virtual Address | Raw Size Raw Address Reloc Address | Linenumbers | Relocations N...| Linenumbers ... | Characteristics
Byte[8] | Dword Dword | Dword | Dword | Dword Dword Word Word | Dword
text 00000F20 00001000 00001000 00000400 00000000 00000000 0000 0000 60000020
data 00001056 00002000 00001200 00001400 00000000 00000000 0000 0000 40000040
data 00000140 00004000 00000200 00002600 00000000 00000000 0000 0000 0000040
pdata 000001D4 00005000 00000200 00002800 00000000 00000000 0000 0000 40000040
AO! 00037CEC 00006000 0003700 00002A00 00000000 00000000 0000 0000 68000020
sreloc 00000048 0003E000 00000200 00034800 00000000 00000000 0000 0000 40000040
sre 000001D5 0003F000 00000200 0003AA00 00000000 00000000 0000 0000 40000040
vy PE64
Operation system: Windows(Vista)[AMD64, 64-bit, Console]
Linker: Microsoft Linker(14.36.33134)
Compiler: Microsoft Visual C/C++(19.36.33030)[C+ +] Dete -
Language: C/C++
Tool: Visual Studio(2022 version 17.6)
Packer: Packer detected(Heuristic)[Section 3 (".pdata") compressed]
@ oS can be ditfere depending o e p
```

## Slide 20

Fully protected sample

Output file over 100 000% larger than input


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Name Value
¥ Virtual Machine
Functions for Protection
Version Default
Ne k d strit
lew markers and strings Instances Default
VMProtectMarker1 Complexity 20%
Licenses ¥ File
Files Memory Protection Yes
Import Protection Yes
Resource Protection Yes
Pack the Output File Yes
Output File Z:\VMprotect\vs\t2\Asm2\x64\Release\complexity_check\Asm2_5incs_3mov.vmp1-full_protected.exe
¥ Detection
Debugger User-mode + Kernel-mode
Virtualization Tools Yes
¥ Additional
Segments
Strip Debug Information
Strip Relocations (for EXE files only)
Shadow Stack Compatible
Watermark
Lock To HWID
¥ Messages
A debugger has been found running in your system.
Debugger Found Please, unload it from memory and restart your program.
Virtualization Tools Found Sorry, this application cannot run under a Virtual Machine.
File corrupted! This program has been manipulated and maybe
it's infected by a Virus or cracked. This file won't work anymore.
This code requires valid serial number to run.
Program will be terminated.
File Corrupted
Serial Number Required
HWID Mismatched This application cannot be executed on this computer.
Licensing Parameters
Compilation Log Output file over 100 000% larger than input
[7 output fle size is 13488640 bytes (11asaa%]4—
```

## Slide 21

Multiple random sections


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Multiple random sections
Name Virtual Size Virtual Address | Raw Size Raw Address Reloc Address | Linenumbers | Relocations N...| Linenumbers ... | Characteristics
Byte[8] | Dword | Dword | Dword | Dword | Dword | Dword | Word | Word | Dword
text O0000F60 00001000 “00000000 “00000000 “(00000000 “00000000 “0000 “0000 “60000020
data 00001056 00002000 00000000 00000000 00000000 00000000 0000 0000 40000040
data 00000140 00004000 00000000 00000000 00000000 00000000 0000 0000 0000040
.pdata 000001D4 00005000 00000000 00000000 00000000 00000000 0000 0000 40000040
0S" 0079EB12 00006000 00000000 00000000 00000000 00000000 0000 0000 60000020
1) 00000870 007A5000 00000A00 00000400 00000000 00000000 0000 0000 C0000040
IPG O0OCDCODC 007A6000 00CDC200 O0000E00 00000000 00000000 0000 0000 68000060
Src 000001D5 01483000 00000200 0OCDDO000 00000000 00000000 0000 0000 40000040
```

## Slide 22

# Fully protected and packed sample

Latest DIE version


> Recovered by OCR — confidence 90/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fully protected and packed sample
: p
vy PE64 Latest
Operation system: Windows(Vista)[AMD64, 64-bit, Console] DIE version
Protector: VMProtect(new 36 jmp 12)[DS]
Protection: Generic(Heuristic) [Strange sections]
Packer: Packer detected(Heuristic)[High entropy + Section 6 (".!|PG") compressed]
```

## Slide 23

Fully protected But not packed sample

Not packed No Anti-Dbg


> Recovered by OCR — confidence 86/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
:000000014077474D
PE64
2
Fully protected
But not packed
byte ptr [rsp+8], 32h sample
3CBF67B9h
word ptr [rsp+@], 1F80h
qword ptr [rsp+1@h], 7Eh
qword ptr [rsp+10h], @FFFFFFFFF4@D5Fe2h
qword ptr [rsp+8]
rsp, [rsp+1eh]
near ptr unk_140B77781
Operation system: Windows(Vista)[AMD64, 64-bit, Console]
Protector: VMProtect(new 25 jmp 9)[DS]
Protection: Generic(Heuristic)[Strange sections]
Packer: Packer detected(Heuristic)[High entropy + Section 3 (".pdata") compressed]
PE64
Operation system: Windows(Vista)[AMD64, 64-bit, Console]
Not packed
Packer: Packer detected(Heuristic)[High entropy + Section 3 (".pdata") compressed] [R\ew-AVahars Dleyss
```

## Slide 24

How can we simplify the complexity ?

## Slide 25

Sample code for testing


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
main proc
call _CRT_INIT
push rbp
mov rbp, rsp
sub rsp, 32
push rax
call VMProtectBegin
mov rax, Odeadcafeh
pop rax
lea rex, fmtStr
call printf
Main proc
call _CRT_INIT
push rbp
mov rbp, rsp
sub rsp, 32
push rax
push rcx
|call VMProtectBegin |
mov rax, Odeadbeefh
mov rax, 9dead1337h
add rax, Qaaaaaaaah
add eax, Obbbbh
add ax, Occh
rol rax, 1
ror rax, 2
nop
nop
nop
not rax
neg rax
xor rax, Offffh
inc rax
dec rex
}call VMProtectEnd |
main proc
call _CRT_INIT
push rbp
mov rbp, rsp
sub rsp, 32
push rax
|call VMProtectBegin |
mov rax, Odeadcafeh
inc rax
inc rax
inc rax
inc rax
inc rax
mov rax
inc rax
inc rax
inc rax
inc rax
inc rax
mov rax, 9dead1337h
inc rax
inc rax
inc rax
inc rax
inc rax
|call VMProtectEnd |
Odeadbeefh
xor ecx, ecx pop rcx
* pop rax
call exit pop rx
7 lea rex, fmtStr ea rex, fmtStr
main endp wl pes: call printf
xor ecx, ecx xor ecx, ecx
end call exit call exit
main endp main endp
Sample code for testing
```

## Slide 26

# Control Flow Graphs to the rescue ….

Code trace

Python Script builds CFG as PDF


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Control Flow Graphs to the rescue ....
$ head asm2_single_instr.vmp3-c0-11-20240609-135638. log
0x0000000140001006 mov rbp, rsp
0x0000000140001009 sub rsp, 0x20
0x000000014000100D push rax
0x000000014000100E call 0x0000000140006580
0x0000000140006580 pushfq
0x0000000140006581 add qword ptr ss: [rsp+0x08], OxFFFFFFFFBFFFEFED
0x000000014000658A push rbp
0x000000014000658B mov rbp, 0xD78290B4F6B57699
0x0000000140006595 push r9
0x0000000140006597 mov qword ptr ss: [rsp+0x18], Ox60228E5B
import sys
import graphviz
import argparse
from pathlib import Path
parser=argparse.ArgumentParser(description="This script takes an X64dbg instructions trace log file and generates a corrosponding graph.")
parser.add_argument(“tracelog filename")
args=parser.parse_args()
trace_fname = args.tracelog filename
graph_fname = f"{Path(trace_fname) .stem}-graph”
print(f"[INFO] Loading trace from {trace_fname}")
with open(trace_fname) as file:
lines = file.readlines()
Code trace
Python Script
builds CFG as
PDF
```

## Slide 27

Code trace split into basic blocks and than use Graphviz to build a Code Flow Graph (CFG)

CFG in PDF Format


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
--- 0x0000000140001006 ---
0x0000000140001006 mov rbp, rsp
0x0000000140001009 sub rsp, 0x20
0x000000014000100D push rax
bb_start = 0x0000000140001006
bb_end = 0x000000014000100E
jmp_addr = ['0x0000000140010E1A"]
0x0000000140010E1A call 0x00000001400064D2
bb_start = 0x0000000140010E1A
bb_end = 0x0000000140010E1A
jmp_addr = ['0x00000001400064D2"]
bb_idx = [1]
--- 0x00000001400064D2 ---
0x00000001400064D2 push ri2
0x00000001400064D4 mov qword ptr ss: [rsp+0Ox1(
bb_start = 0x00000001400064D2
bb_end = 0x00000001400064E2
jmp_addr = ['0x000000014001BF44"]
bb_idx = [2]
0x000000014001BF44 |jmp 0x000000014001B 544
Code trace split into basic blocks
and than use Graphviz to build a Code
Flow Graph (CFG)
B asm2_multiple_instr.vmp1-c0-i1-20240609-143630-graph.pdf
B asm2_multiple_instr.vmp1-c10-i1-20240609-150850-graph.pdf
B asm2_multiple_instr.vmp1-c20-i1-20240609-151402-graph.pdf
B asm2_multiple_instr.vmp2-c0-i1-20240609-144425-graph.pdf
B asm2_multiple_instr.vmp2-c10-i1-20240609-152026-graph.pdf
B asm2_multiple_instr.vmp3-c0-i1-20240609-145114-graph.pdf
B asm2_multiple_instr.vmp3-c10-i1-20240609-153206-graph.pdf
B asm2_multiple_instr.vmp3-c20-i1-20240609-153725-graph.pdf
B asm2_single_instr.vmp1-c0-i1-20240609-132343-graph.pdf
B asm2_single_instr.vmp1-c10-i1-20240609-154406-graph.pdf
B asm2_single_instr.vmp1-c20-i1-20240609-154824-graph.pdf
B asm2_single_instr.vmp2-c0-i1-20240609-133133-graph.pdf
B asm2_single_instr.vmp2-c10-i1-20240609-155402-graph.pdf
B asm2_single_instr.vmp2-c20-i1-20240609-155947-graph.pdf
B asm2_single_instr.vmp3-c0-i1-20240609-135638-graph.pdf
B asm2_single_instr.vmp3-c10-i1-20240609-172813-graph.pdf
B asm2_two_instr.vmp1-c0-i1-20240609-141257-graph.pdf
B asm2_two_instr.vmp1-c10-i1-20240609-173623-graph.pdf
B asm2_two instr.vmp2-c0-i1-20240609-141933-graph.pdf
B asm2_two_instr.vmp2-c20-i1-20240609-174806-graph.pdf
CFG in PDF Format
```

## Slide 28

asm2 _multiple_instr .vmp -c100 -i1-20240610-143435.log

Execution order

Central switch

Initialization and central VM logic (next slide)

Unprotected Code

## Slide 29

asm2_multiple_instr.vmp -c100 -i1-20240610-143435.log

Basic Block execution
order index
Central VM logic
This is harder to identify in
graphs of complex samples

## Slide 30

No surprise. More instructions lead to more basic blocks below the central switch

asm2_ single _instr-c1-i1.vmp-20240610-143947.log

asm2 _multiple _instr.vmp-c1-i1-20240610-142851.log

## Slide 31

VMProtecEnd
Trace BB index: 186
VMProtectBegin
Trace BB index: 80
Main switch
Higher complexity setting makes the graph simpler !
Most simple CFG !
asm2 _single_instr-c100 -i1.vmp-20240610-144215.log

## Slide 32

15 JMPs
Main switch

asm2 _multiple_instr .vmp -c100 -i1-20240610-143435.log

## Slide 33

Left site

51 JMPs
asm2 _multiple_instr .vmp-c1-i1-20240610-142851.log

## Slide 34

###### Right site

51 JMPs

asm2 _multiple_instr .vmp-c1-i1-20240610-142851.log

## Slide 35

VMProtect Internals

## Slide 36

asm2_ 5incs_3mov .vmp1-c0-i1.exe Main switch

## Slide 37

Next virtual Instruction Block e.g. VMHandler “inc <register>” In this case it is R8, but this is random, could also be another register

## Slide 38

How are VMHandlers executed and connected ?

We are starting here on the next slide at block 717

Main Switch
1. 4.
2. 3.
5. VMHandler 1 VMHandler 2 VMHandler 3 6. Simplified Logic
VMHandler 4

## Slide 39

Calculation of the next vInstr Block – Block 14002ABC3 (717)

The code below is distributed over multiple lines of code, plus a lot of dead code and

other instruction in-between

ByteCodePtr can be different e.g. _sub rbx,1_ Encrypted offset to next vInstr (E966F * 8 = 74B78 -> EDX ptr to offset) -> VMHandlerTableEntry XOR EDX (VMHandlerTableEntry ) with Rolling key in EBP

Do some math to calculate final value for EDX (offset to next vInstr handler)

New rolling Key in EBP

Next vInstr handler This vInstr handler start

… next slide

## Slide 40

### Calculation of the next vInstr Handler – Block 14002906A (720)

Add hardcoded value in RCX with RDX Hardcoded value loaded earlier in ECX

New rolling key

Next vInstr Handler

This vInstr Handler start

## Slide 41

# Remember the VMHandler table offset ( _sub rbx,1 ) ?_

The VMHandler table is not linear.


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Remember the VMHandler table offset (sub rbx,1 ) ?
dd 2E£202302h ; 4. VMHandler . offset (sub 1) at 14003B6BC
; 3. VMHandler enc. offset (rbx=rbx rbx, [rox] ; [rbx]=[14001076A]) at 14003420E
d
dd @AA925452h ; 2. VMHandler . offset (sub 4) at 14001C425
. VMHandler . offset (sub 4) at 1400304A1
. VMHandler . offset (sub 4) at 1400311D3
The VMHandler table is not linear.
sub rbx, 4
edx, [rbx+r9*8-74878h] ;
cisco
```

## Slide 42

Remember the rolling key ? What about R10 ?

New rolling Key in EBP

##### … it’s all just obfuscation:


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Remember the rolling key ? What about R10 ?
push rbp 3 PSp=14FBD@ rsp->14FBC8
xor [rspip10}2-1sh+var_1FEC6], edx ; rsp=14FBC8, rl@=FF6F*2=1FEDE, [rsp+ri@*2-1FEDE]=[14FBC8]=00015834 — XOR [RBP] with EDX
rsp = 14FBC8 -> FFFF956A New rolling
rsp = 14FBC8 -> 1615@DC97 Key in EBP
rsp = 14FBC8 -> 1615@E54E
[ move RSP to new RBP ] new rolling key ?
; rbp -> FFFF956A
; rbp -> 1615@DC97
. it’s all just obfuscation:
mov eax, 88807D21h ; --- new block 14@@2ABC3
lea rex, ds:QFFFFFFFFDC26EF2Dh[rax*2] ; [rax*2-23D91@D3]=[ED27 E96F]
neg cx > rex -> @8000808ED271691
movzx ri@d, cl
neg r16w 5 r1e -> FF6F
; rsp=14FBC8, r10=FF6F*2=1FEDE, [rsp+r10*2-1FEDE ]=[14FBC8]=9EAF3830
```

## Slide 43

Let’s proof the assumption and get all connections of all VMHandlers…

The python script extracts all ‘ **add <reg1>, <reg2** >’ statements and sets **breakpoints** on them to get their values at runtime. regex1 = re.compile(r'(0x[01234567890ABCDEF]{16}) (ad[cd]) (r.{1,2}), (r.{1,2})’)

Next vInstr Handler This vInstr Handler start

## Slide 44

### … after feeding it into X64dbg:

Execution Order

False Positive of the regex Proofs our assumption it is always R8 (in this case)


> Recovered by OCR — confidence 79/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Execution
Order
... after feeding it into X64dbg:
addr=000000014003D568 , rbx=4001077C, rdx=@, res=4001077C
addr=000000014003D56F , rbx=4001077C, rsi=100000000, res=14001077C
addr=000000014001AF15 , r8=1400311D3, rcx=FFFFFFFFFFFFF2CE, res=1400304A1
False Positive
of the regex
laddr=000000014001C510, r10=70, rsp=14FBD@,re
addr=0000000140031BFC,r8 e
addr=0000000140037041,r8
addr=0000000140017672,r8
addr=000000014002F9C3, r8=14003A96D, rsi=FFFFFFFFFFFD7@C4, res=140011A31
addr=000000014003C4AF ,r8=140011A31, r11=CF42,res=14001E973
addr=0000000140026F6A, r8=14001E973,r11=11B2E, res=1400304A1
140014C57
Proofs our
assumption
it is always R8&
(in this case)
```

## Slide 45

### … and cleaned up (including an anomaly check).

Initialization

VMProtectStart

Breakpoint address

Start of Next VMHandler VMHandler

VMProtectEnd

asm2_5incs_3mov.vmp1-c0-i1-20240620-105921

## Slide 46

Does it make a difference if we change the complexity rate ? No.

asm2_5incs_3mov.vmp1 -c100 -i1-20240625-110446


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Does it make a difference if we change the complexity rate ? No.
$ python parse_bp_out.py
0000000140033957:
000000014003C78C:
000000014003ED68:
0000000140019D90:
000000014002AECD:
0000000140016EF9:
00000001400146F3:
00000001400146F3:
00000001400146F3:
00000001400146F3:
00000001400146F3:
00000001400146F3:
00000001400146F3:
00000001400323FD:
0000000140033957:
00000001400146F3:
00000001400146F3:
0000000140033957:
000000014003C78C:
000000014003C78C:
000000014003C78C:
140031F48 --140013CA7
140013CA7 o 140013CA7
140013CA7 “-. 140013CA7
140013CA7 “<. 140036452
140036452 ms 140034A5B
140024FD7 “<- 140024FD7
140024FD7 g 140024FD7
140024FD7 “-. 140024FD7
140024FD7 “<. 140024FD7
140024FD7 “©. 140024FD7
140024FD7 “ 140024FD7
140024FD7 ae 140032378
140032378 < 140041975
140031F48 - 140013CA7
140013CA7 — 140013CA7
140024FD7 — 1400298B1
140031F48 7 140013CA7
140013CA7 “—, 140013CA7
140013CA7 +, 140013CA7
140013CA7 -— 140036452
<-- 140033957 Init Block (Anomaly: 1)
<-- 140033957 VMProtectStart Block (Anomaly: 2)
<-- 140033957 VMProtectEnd Block (Anomaly: 3)
asm2_5incs_3mov.vmp1-€100-i1-20240625-110446
```

## Slide 47

asm2_5incs_3mov.vmp1 -c100-i10 -20240625-110446


> Recovered by OCR — confidence 75/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
addr=0000000140088459 , rbp=14014AE6A J itcx=BC8CF $=|149207739
addr=00000001400A8EFD, rbp=14023@D7B, r10=FFFFFFFFFFE9AB@3, res=1400CB87E
addr=000000014013596B , rbp=1400CB87E , rbx=FFFFFFFFFFFA869A, res=140073F18
addr=000000014018757D, rbp=140073F18, rsi=16824A, res=1401DC16
2
addr=000000014900D7@D7 , rbp=1401DC162, r10=FFFFFFFFFFFA@DAA, res=14017CF@C
<-- Init
addr=@0000001402207FE, rbp=14017CF@C, rcx=FFFFFFFFFFFBC@60, res=140138F6C
<-- reg change VMProtectStart |
addr=00000001400945@D, r11=140165D8A, rbp=FFFFFFFFFFF73D91, res=14@@D9B1B
addr=00000001401FD1B5 , r11=140@D9B1B, rbx=986A, res=1400E3385
addr=00000001400E9DED, r11=1400E3385, rsi=10100F, res=1401E4394
3
addr=000000014019BC54, r11=140204756, rcx=E427, res=140212B7D
1
<-- reg change VMProtectEnd |
addr=00000001401D29C6,rsi DX=17B829, res=1401E953
addr=00000001402266E0, rsi=1401E9530, r8=45777, res=14022ECA7
1400A3401
addr=00000001400DD7D6 , rsi=14022ECA7, rbx=FFFFFFFFFFF7C5BC, res=1401AB263
addr=00000001400B3C9B , rsi=14008D45E , rdx=2ACB8, res=1400B8116
```

## Slide 48

VMHandler

## Slide 49

### Translation of “INC EAX”

1<sup>st</sup> : There is not just one “INC <Register>” VMHandler and they all look different!


> Recovered by OCR — confidence 80/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Translation of “INC EAX”
1st : There is not just one “INC <Register>” VMHandler and they all look different!
mov rax, Odeadcafeh
inc rax Oxdeadcafe —> Oxdeadcaff
inc rax |Oxdeadcaff —> Oxdeadcbd0
inc rax ; (Oxdeadcb0@ -> Oxdeadcb01
inc rax ; Oxdeadcb01 -—> Oxdeadcb02
```

## Slide 50

##### “INC <Register>” handler (likely add <p1,p2>) – VMHandler Nr. 4 in Graph

Get Parameter 1 and 2
“inc eax”
(add p1,p2)
Store result
? Next slide…
Next “INC” – VMHandler – Nr. 8 in Graph

Other “INC” - VMHandler

Different “INC” VMHandler can have different instructions, other registers, other dead code, etc

## Slide 51

### Stack is changed between VMHandlers

##### First mov of DEADCB00 from 14FE98 to 14FC00

##### Second mov of DEADCB00 from 14FC00 to 14FE90

## Slide 52

Translation of MOV rax, 0xDEADCAFE Operation

Get and “Decode String” VMHandler (From Block 140019C53 – Block 140022639)

Decode DEADCAFE value

Stack organization VMHandler (From Block 140027A67 – Block 140025CD4)

Actual “MOV” VMHandler (From Block 14001E330 – Block 14002BA0C)

Move DEADCAFE from 14FEB0 to 14FC88

Write DEADCAFE to EAX

## Slide 53

Helpful Tool – Execution Trace Viewer

X64dbg


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Helpful Tool — Execution Trace Viewer
Filtered ti ¥ 4 441 > > | Page: 1/1 regex=Oxdeadcaff ~ | Filter Find: Registers ¥ « v
= address opcodes disasm registers
2872 0x140idalied 4813da3 adc rdx, rbx rdx: eflags
2876 0Ox140idaif9 4c8bd2 mov r10, rdx r10:
2938 0x140224d15 498bac0270ffdd mov rbp, qword ptr [r10 + rax - ] rbp:
2939 0x140224did 488bdd mov rbx, rbp rbx:
reg hex dec
- rax Oxlla8le7c 296230524
id About x rex Oxffffffff7e8.. 18446744071537485979
rdax Oxdeadcafe 3735931646
rbx Oxi 1
Execution Trace Viewer 1.0.0 rsp Oxi4tb£0 1375216
. rbp 0x1f£20361d2 8355275218
(C) 2019 Teemu Laurila rsi Ox3£ff 16383
rid Oxffffffffe23... 18446744073210304153
ri2 0x0 0
®> Trace into. 7 ri4 0x0 0
30
0x0
0x0
0x0
0x0
0x0
‘Command Text
‘Command Condition:
Record trace é.. || OK || Cancel pa
c:0 P:0
```

## Slide 54

## What’s next ?

- Blog post

- Tool release

- Collaboration ?

- VMP 4.0 … I am a bit scared ☺

## Slide 55

blog.talosintelligence.com
@talossecurity
blog.talosintelligence.com
@talossecurity

## Slide 56

blog.talosintelligence.com
@talossecurity
blog.talosintelligence.com
@talossecurity

## Slide 57

Stay Connected and Up To Date Spreading security news, updates, and other information to the public.

ThreatSource Newsletter cs.co/TalosUpdate Social Media Posts X: @talossecurity

_Talos publicly shares security information through numerous channels to help make the internet safer for everyone._

White papers, articles & other information talosintelligence.com Talos Blog blog.talosintelligence.com Videos cs.co/talostube Beers with Talos & Talos Takes talosintelligence.com/podcasts

## Slide 58
