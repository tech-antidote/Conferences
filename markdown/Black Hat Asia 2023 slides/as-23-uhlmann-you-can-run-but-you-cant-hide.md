---
title: "You Can Run But You Cant Hide"
speakers: ["Uhlmann"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Uhlmann-You-Can-Run-But-You-Cant-Hide.pdf"
pages: 20
sha256: "7f1e4ccecf41d99c5e4f21aa3409e872eeafa3f581303317c5d823a5d4c13d26"
text_chars: 9214
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:55:34Z"
---
# You Can Run But You Cant Hide

**Speakers:** Uhlmann  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Uhlmann-You-Can-Run-But-You-Cant-Hide.pdf` (20 pages)

## Slide 1

You can Run, but you can’t Hide Finding the Footprints of Hidden Shellcode

John Uhlmann @jdu2600

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat —
ASIA @O0e3
MAY 11-12
BRIEFINGS
You can Run, but you can’t Hide
Finding the Footprints of Hidden Shelicode
John Uhimann
@jdu2600
```

## Slide 2

# whoami

Security Research Engineer at Elastic • Elastic Defend (“EDR”) developer

• Elastic Security Labs Blogger

• <u>https://www.elastic.co/blog/author/john-uhlmann</u>

#BHASIA @BlackHatEvents

## Slide 3

# Agenda

1. Why do security products scan memory?

2. Memory scanning & evasion recap

3. Detection opportunities for hidden shellcode

- Detection via immutable code page principle violations

- Detection via CFG bitmap anomalies

4. Hunting via process behaviour summaries

#BHASIA @BlackHatEvents

## Slide 4

Why do security products scan memory?

- On Windows x64, Microsoft has –

- hardened the kernel,

- claimed the hypervisor, and

- made private executable memory an indefensible boundary for kernel-mode security products.

- This just leaves memory scanning.

- It’s not perfect, but it’s still a valuable defensive layer.

#BHASIA @BlackHatEvents

## Slide 5

# Overview of memory scanners

Generic Scanners

- YARA - memory content signatures

- PE-sieve - image metadata anomalies and content heuristics

- Moneta - memory metadata anomalies

#BHASIA @BlackHatEvents

## Slide 6

# Evasion recap

- Gargoyle - memory protection fluctuation via APC timer and ROP chain

- obfuscate-and-sleep - encrypted state fluctuation via post-sleep stub

- FOLIAGE - encrypted state fluctuation via APC timers and context manipulation

- Shellcode Fluctuation - memory protection fluctuation via post-sleep indirect stub

- DeepSleep - memory protection fluctuation via post-sleep ROP chain

- Ekko - encrypted state fluctuation via timer queues and context manipulation

- Scheduled Tasks ;-)

#BHASIA @BlackHatEvents

## Slide 7

# Evasion recap

Kyle Avery - Avoiding Memory Scanners: Customizing Malware to Evade YARA, PE-sieve, and More <u>https://forum.defcon.org/node/241824</u>

#BHASIA @BlackHatEvents

## Slide 8

# Evasion – key concept

“a common technique for reducing computational burden is to limit analysis on executable code pages only“ - Josh Lospinoso

<u>https://lospi.net/security/assembly/c/cpp/developing/software/2017/03/04/gargoyle-memory-analysis-evasion.html</u>

```
VirtualProtect(pShellcode, sizeof(shellcode), PAGE_READWRITE, &OldProtect);
```

#BHASIA @BlackHatEvents

## Slide 9

# Niche memory scanners

- Patriot - anomalous thread CONTEXT structures

- Hunt-Sleeping-Beacons - anomalous Wait call stacks

- TickTock - anomalous timer-queue timers

#BHASIA @BlackHatEvents

## Slide 10

## Immutable code page principle violations

- Once code pages are written they should never change.

- The memory protection progression for code pages should only be RW to RX.

- Microsoft-Windows-Threat-Intelligence PROTECTVM_LOCAL ETW events

- IsExecutable(LastProtectionMask) && !IsExecutable(ProtectionMask)

- (Optionally) Anomalous call stack detection

#BHASIA @BlackHatEvents

## Slide 11

# An interesting discovery

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
An interesting discovery
ree Gabriel Landau
i) | think | just made an interesting discovery. If you VirtualAlloc(RWX), it modifies the
CFG bitmap accordingly. If you then VirtualAlloc(RW), the CFG bitmap stays as-is.
Gabriel Landau
ae We may be able to use this to find DLL hollowing and gargoyle-style?
```

## Slide 12

# Control Flow Guard bitmap recap

- Time efficient lookup of valid indirect call targets

- One bitmap per process

- Each 2 bits corresponds to 16 virtual addresses

- x64 bitmap is 2TB – mostly shared or reserved

- PE files bring their own bitmap

- Copied to the correct offset in process bitmap during image load

- Permissive backwards compatibility for JIT

- Memory manager simply marks all executable private addresses as valid targets

#BHASIA @BlackHatEvents

## Slide 13

# CFG bitmap anomalies

- The VAD tree only stores original protection and current protection.

- The CFG bitmap (inadvertently) records the location of all private memory addresses that are, **or have previously been** , executable during the lifetime of the process.

- This can be used to flag memory regions that have been changed from executable to non-executable.

#BHASIA @BlackHatEvents

## Slide 14

# Evasion opportunities

- Protection fluctuation approaches are actually quite noisy.

- Hide your code pages in plain sight.

- Obfuscate them against current signatures ahead of time.

- Encrypt your data pages when not in use.

- Or launch in a new process every time.

- Scheduled Tasks etc.

#BHASIA @BlackHatEvents

## Slide 15

## Hunting via process behaviour summaries

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Hunting via process behaviour summaries
BLEW syscall Monitor - oF x
ProtectVirtual
4 dumpy.exe::24e1dc53939b62d8e6d7a53535 lebf2a7 1f9d617
ProcessCreationTraits
4 Syscalls
dbgcore->kernelbase!OpenThread->ZwOpenThread(all, ALL_ACCESS)
dbgcore->kernelbase!ReadProcessMemory[hooked]->ZwReadVirtualMemory(Isass)
dbgcore->ntdll!NtOpenThread->ZwOpenThread(all, ALL_ACCESS)
exe->kernelbase!LoadLibraryA[hooked]->ZwMapViewOfSection(dbgcore.dll)
exe-> kemnelbase!LoadLibraryA->ZwMapViewOfSection (ktmw32.dll)
exe->ntdlllNtOpenProcess->ZwOpenProcess(System, DUP_HANDLE)
exe->ntdll!NtProtectVirtualMemory->ZwProtectVirtualMemory(self, ntdlllexe, EXECUTE_READ->EXECUTE_READWRITE)
exe-> ntalllexe!NtProtectVirtualMemory[hooked]->ZwProtectVirtualMemory(self, ntdlllexe, EXECUTE_READWRITE-> EXECUTE_READ)
ucrtbase->kernelbase!LoadLibraryExW{hooked]->ZwMapViewOSection(kernel.appcore.dll)
4 TTPHash
ecd0fdd31504dc1e4eae3d852370a87¢3902fd68
4 ekko.exe::19385aad 1e6e3bf97eaeb9833d900bed9568a59a
ProcessCreationTraits
4 Syscalls
exe->kernelbase!LoadLibraryA->ZwMapViewOfSection(advapi32.dll)
exe->kernelbase!LoadLibraryA->ZwMapViewOfSection(msvcrt.dil)
(
(
exe-> kernelbase!LoadLibraryA->ZwMapViewOfSection(rpert4.dll)
exe-> kernelbase!LoadLibraryA->ZwMapViewOfSection(sechost.dll)
ntdlll tp TpTimerCallback-> kernelbase! VirtualProtect->ZwProtectVirtualMemory(self, exe|ntdll!RtIpTpTimerCallback, EXECUTE_READWRITE->READWRITE)
ntdll! tp TpTimerCallback-> kernelbase!VirtualProtect->ZwProtectVirtualMemory(self, exe|ntdll!RtIpTpTimerCallback, READWRITE-> EXECUTE_READWRITE)
ntdll!RtIpTpTimerCallback-> kernelbase!VirtualProtect->ZwProtectVirtualMemory(self, UNKNOWN\ntdll!RtlpTpTimerCallback, EXECUTE_READWRITE->READWRITE)
ntdll! tip TpTimerCallback-> kernelbase!VirtualProtect->ZwProtectVirtualMemory(self, UNKNOWN\ntdll/RtlpTpTimerCallback, READWRITE-> EXECUTE_READWRITE)
4 TTPHash
081cfc3{09e29f9daa1286337246eb1 156fa7d13
4 shellcodefluctuation.exe:1b4ec792d9a72659f1b66e17fc14d6e90b7588a2
ProcessCreationTraits
4 Syscalls
exe-> kernelbase!VirtualProtect->ZwProtectVirtualMemory(self, kernel32|exe, EXECUTE_READ->EXECUTE_READWRITE)
exe-> kernelbaselVirtualProtect->ZwProtectVirtualMemory(self, kernel32|exe, EXECUTE_READWRITE-> EXECUTE_READ)
4 TTPHash
ad4bd0722391edbb4eedba904410ee2bifS6edc
alling vulnerable driver...
bling PPL via DKOM...
starting UserTrace(Syscal1summariser-User-Trace)...
sabling PPL via DKOM. «
] flushing state to file - size = 125174 bytes
```

## Slide 16

# Black Hat Sound Bytes

- Threat-Intelligence ETW can be used to detect violations of the immutable code page principle.

- The CFG bitmap can be used to detect shellcode hidden at a point-in-time via changed memory protections such as Gargoyle.

- Kernel telemetry can be used to construct process behaviour summaries – which can be used to identify behavioural outliers for more detailed investigation.

- But, without intervention from Microsoft, private executable memory will likely remain an indefensible boundary for kernel-mode security products.

#BHASIA @BlackHatEvents

## Slide 17

# Questions

Tools

- <u>https://github.com/jdu2600/EtwTi-FluctuationMonitor</u>

- <u>https://github.com/jdu2600/CFG-FindHiddenShellcode</u>

- <u>https://github.com/jdu2600/Etw-SyscallMonitor</u>

#BHASIA @BlackHatEvents

## Slide 18

# Detection References

- <u>https://github.com/VirusTotal/yara</u>

- <u>https://github.com/hasherezade/pe-sieve</u>

- <u>https://github.com/forrest-orr/moneta</u>

- <u>https://www.elastic.co/security-labs/hunting-memory</u>

- <u>https://www.elastic.co/blog/detecting-cobalt-strike-with-memory-signatures</u>

- <u>https://github.com/joe-desimone/patriot</u>

- <u>https://github.com/thefLink/Hunt-Sleeping-Beacons</u>

- <u>https://github.com/WithSecureLabs/TickTock</u>

#BHASIA @BlackHatEvents

## Slide 19

# Evasion References

- <u>https://github.com/JLospinoso/gargoyle</u>

- <u>https://www.cobaltstrike.com/blog/cobalt-strike-3-12-blink-and-youll-miss-it/</u>

- <u>https://github.com/realoriginal/foliage</u>

- <u>https://github.com/mgeeky/ShellcodeFluctuation</u>

- <u>https://github.com/thefLink/DeepSleep</u>

- <u>https://github.com/Cracked5pider/Ekko</u>

- <u>https://www.blackhillsinfosec.com/avoiding-memory-scanners/</u>

#BHASIA @BlackHatEvents

## Slide 20

# OS References

- <u>https://en.wikipedia.org/wiki/W%5EX</u>

- <u>https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nfmemoryapi-virtualprotect</u>

- <u>https://github.com/jdu2600/Windows10EtwEvents/blame/master/manifest/M icrosoft-Windows-Threat-Intelligence.tsv</u>

- <u>https://www.elastic.co/security-labs/finding-truth-in-the-shadows</u>

#BHASIA @BlackHatEvents
