---
title: "Virtualization Based (In)Security"
speakers: ["Ori David"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Ori David - Virtualization Based (In)Security.pdf"
pages: 62
sha256: "9bb587275d6e43bc757d09338b1ca7c758afb9428fd8bc5d9b66554b759bf89d"
text_chars: 8568
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:09:04Z"
---
# Virtualization Based (In)Security

**Speakers:** Ori David  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Ori David - Virtualization Based (In)Security.pdf` (62 pages)


## Slide 1

##### **Virtualization-Based (In)security Weaponizing VBS Enclaves**

**Ori David**

## Slide 2


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Edit Format |View Help
<html> “
<head>
<title>My First VBScript Code!!!</title>
</head>
<body>
<script types text/vbscript >
document.write("Yes!!! I have started learning VBScript.")
</script>
</body>
```

## Slide 3

## Slide 4

###### **Whoami**

Ori David

Security researcher at Akamai

Background in red teaming and threat hunting

## Slide 5

###### **Agenda**

Virtualization  VBS  Abusing VBS
Based Security Enclaves Enclaves

## Slide 6

###### **Virtualization-Based Security**

## Slide 7

###### **Pushing the boundaries**

- Windows traditionally relied on the ring3/0 boundary

- This proved to be insufficient

   - Kernel exploits

   - Bring Your Own Vulnerable Driver

## Slide 8

###### **Virtualization Based Security**

VM1 VM2
Hyper-V

## Slide 9

###### **Virtualization Based Security**

Operating  Isolated
System
Memory
Hyper-V

## Slide 10

###### **Virtual Trust Level (VTL)**

User Mode
Ring3
Ring0
Kernel Mode

## Slide 11

###### **Virtual Trust Level (VTL)**

VTL0 VTL1
Isolated
User
User
Mode
Mode
Ring3
Ring0
Secure
Kernel
Kernel
Mode
Mode

## Slide 12

**VBS Enclaves**

## Slide 13

###### **What is an Enclave?**

Process Enclave
Access Enclave
Data

## Slide 14

###### **What is an Enclave?**

Process Enclave
Invoke Enclave
Method

## Slide 15

###### **VBS Enclaves**

- Execute part of a process in IUM

- Nothing in VTL0 can access the enclave

VTL0 VTL1
Process Enclave

## Slide 16

###### **VBS Enclave Lifecycle**

VTL0 VTL1
Process.exe VBS Enclave
EnclaveModule.dll
*Enclave modules
 must be signed
CallEnclave

## Slide 17

### **Abusing VBS** **<u>Enclaves</u>**

## Slide 18

###### **Enclave Abuse Potential**

Inaccessible Memory

Untraceable API calls

## Slide 19

###### **VBS Enclave API Calling**

VTL0 VTL1
Process.exe VBS Enclave
EnclaveModule.dll
NTDLL.DLL VERTDLL.DLL
EDR
Normal Kernel Secure Kernel

## Slide 20

#### **Loading a Malicious Enclave**

## Slide 21

###### **Obtain a Legitimate Signature**

- Enclave signing is exposed to 3rd parties

   - Compromise authorized signer

   - Obtain signing privileges legitimately

## Slide 22

###### **Exploit a Loader Vulnerability**

- Exploit a vulnerability in the enclave loading process

   - CVE-2024-49076 by Alex Ionescu


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit a Loader Vulnerability
¢ Exploit a vulnerability in the enclave loading process
¢ CVE-2024-49076 by Alex lonescu
What privileges would an attacker gain by successfully exploiting this vulnerability?
An attacker who successfully exploited this vulnerability couldjload a non-Microsoft DLL into an enclave,
potentially leading to code execution within the context of the target enclave.
```

## Slide 23

#### **Abusing Debuggable Enclave Modules**

## Slide 24

###### **Debuggable Enclave Modules**

• As enclaves reside in VTL1, debugging them isn’t straightforward

## Slide 25

###### **Debuggable Enclave Modules**

- To solve this, we can create debuggable enclave modules


> Recovered by OCR — confidence 87/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Debuggable Enclave Modules
¢ To solve this, we can create debuggable enclave modules
Memory 1
vbsenclave.def enclave.c
Enclave Host “| (Global Scope)
© Routine |= 0x000002c06a3e5040 {ImageAtBase0x2c06a3e4000!CallEnclaveTest(void *)}
"CallEnclaveTest"));
```

## Slide 26

###### **Debuggable Enclave Modules**

- Interestingly, debuggable enclaves reside in IUM

- To enable debugging, the secure kernel implements exceptions

   - SkmmDebugReadWriteMemory

   - SkmmDebugProtectVirtualMemory

\```
VTL0VTL1
\```

Process.exe VBS Enclave
Debuggable.dll

## Slide 27

###### **Abusing Debuggable Enclaves**

• Obviously, using a debuggable enclave in production is not a good idea

- But that’s not the only problem!

## Slide 28

###### **Abusing Debuggable Enclaves**

Obtain any debuggable enclave

Load enclave into
attacker process

“Debug” the enclave to execute code

## Slide 29

###### **Abusing Debuggable Enclaves to Execute Code in IUM**

VTL0 VTL1
VBS Enclave
Process.exe
Debuggable.dll
EnclaveRoutine

GetProcAddress ->  “EnclaveRoutine”

## Slide 30

###### **Abusing Debuggable Enclaves to Execute Code in IUM**

VTL0 VTL1
VBS Enclave
Process.exe
Debuggable.dll
EnclaveRoutine

VirtualProtect  →  pEnclaveRoutine =  PAGE_EXECUTE_READWRITE

## Slide 31

###### **Abusing Debuggable Enclaves to Execute Code in IUM**

VTL0 VTL1
VBS Enclave
Process.exe
Debuggable.dll
EnclaveRoutine
WriteProcessMemory  →  pEnclaveRoutine = Shellcode

## Slide 32

###### **Abusing Debuggable Enclaves to Execute Code in IUM**

VTL0 VTL1
VBS Enclave
Process.exe
Debuggable.dll
EnclaveRoutine
CallEnclave  →  pEnclaveRoutine

## Slide 33

###### **Abusing Debuggable Enclaves – The Catch**

- The unrestricted enclave memory access goes both ways

- Despite that – there are still advantages:

   - An EDR/analyst might not consider this scenario

   - Enclave code still evades VTL0 API monitoring

## Slide 34

###### **Abusing Debuggable Enclaves – HELP ME**

- I haven’t managed to find one yet, but some will likely leak eventually

?

## Slide 35

##### **Exploiting Vulnerable Enclave Modules**

## Slide 36

**BYOVE**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bring
your own
vulnerable driver
Bring your
own
vulnerable enclave
```

## Slide 37

###### **CVE-2023-36880**

- Information disclosure vulnerability in a Microsoft Edge enclave module

- • Could allow limited code execution(?)

## Slide 38

###### **CVE-2023-36880**

- Discovered by Alex Gough, who also shared a PoC

- The vulnerability provides an arbitrary read/write primitive within the

enclave

## Slide 39

###### **Exploiting CVE-2023-36880**

- Enclaves are protected with Arbitrary Code Guard (ACG) by default

   - No new executable pages during runtime

   - Cannot turn executable pages writable

## Slide 40

## Slide 41

###### **Bring Your Own Vulnerable Enclave - Round 2 -**

## Slide 42

###### **CVE-2023-36880 – What can we do?**

Write data into VTL1

Write data into VTL0 from VTL1

Store data out of the reach of EDRs

Modify data within the process while bypassing hooks

## Slide 43

###### **Mirage – VTL1 Based Memory Evasion**

- Sleep obfuscation technique

- Hide shellcode in IUM during sleep

## Slide 44

###### **Mirage – VTL1 Based Memory Evasion**

VTL0 VTL1
Mirage.exe VBS Enclave
Shellcode
Write shellcode
into the enclave

## Slide 45

###### **Mirage – VTL1 Based Memory Evasion**

VTL0 VTL1
Mirage.exe VBS Enclave
Shellcode Shellcode
Periodically write
Shellcode into the process

## Slide 46

###### **Mirage – VTL1 Based Memory Evasion**

VTL0 VTL1
Mirage.exe VBS Enclave
Shellcode Shellcode
Overwrite shellcode
 with benign data

## Slide 47

**Mirage - Demo**

## Slide 48

###### **BYOVE - Round 1.5**

- Cedric Van Bockhaven and Matteo Malvica of Outflank demonstrated a full ROP exploit to achieve VTL1 RCE

Secure Enclaves for Offensive Operations (Part II) - Outflank

## Slide 49

## **Enclave Malware TTPs**

## Slide 50

###### **Protecting Secrets**

- Use the enclave as it was intended to – hide secrets

   - Additional payloads

   - Encryption keys

   - Configuration

## Slide 51

###### **Things We Can’t Do:**

File
Operations

Networking

Process  Registry
Interaction Access

###### **Things We Can Do:**

**???**

## Slide 52

###### **Access VTL0 Memory**

• Enclaves have read/write access to the VTL0 usermode memory of the

process

## Slide 53

###### **Access VTL0 Memory**

- Access adheres to memory protection permissions

\```
memcpy(readonly_vtl0_address, local_buffer, size);
\```

\```
memcpy(writable_vtl0_address, local_buffer, size);
\```

- Cannot change VTL0 memory protection permissions

\```
VirtualProtect(readonly_vtl0_address, size, PAGE_READWRITE, &old);
\```

## Slide 54

###### **Monitor VTL0 Memory**

\```
char* bad_string = "VBS is lame";
char* good_string = "VBS is COOL";
\```

\```
while (1)
{
\```

\```
if (strcmp(vtl0_buffer, bad_string) == 0)
{
memcpy(vtl0_buffer, good_string, strlen(good_string));
}
}
\```

## Slide 55

###### **Execute VTL0 code**

- Enclaves cannot execute VTL0 code within VTL1

\```
int (=func)() = (int (*)())executable_vtl0_address;
int result = func();
\```

- But - they can invoke VTL0 code remotely via CallEnclave

\```
CallEnclave(executable_vtl0_address, 0, TRUE, &out);
\```

*This execution occurs in VTL0, making the evasion advantage limited

## Slide 56

###### **Execute VTL0 code**

\```
char* shellcode = “…”; /= Spawn calc.exe
memcpy(vtl0_buffer, shellcode, sizeof(shellcode));
CallEnclave((PENCLAVE_ROUTINE)vtl0_buffer, 0, TRUE, &out);
\```

## Slide 57

###### **Anti-debugging**

Enclave
Debugger
User
Kernel
 mode
mode
Isolated
User
Secure
Mode
Kernel
Mode

## Slide 58

###### **Anti-debugging**

• Most classic techniques are not available

IsDebuggerPresent

GetTickCount

## Slide 59

###### **Anti-debugging**

- Manual PEB inspection: an enclave can access VTL0 memory, including the PEB

\```
If (PEB->BeingDebugged)
{
TerminateProcess(GetCurrentProcess(),0);
}
\```

• rdtsc: While timing-related functions are not accessible, we can run the rdtsc assembly instruction

\```
rdtscWrapper PROC
rdtsc;
ret;
rdtscWrapper ENDP
\```

## Slide 60

**Advanced Anti-analysis (AKA: Making Researchers Cry)** Move critical logic into the enclave 1 Detect debuggers from within the enclave 2 Profit 3

## Slide 61

###### **Conclusion**

- VBS is cool

- VBS enclaves have a lot of potential

- Keep an eye on them from an offensive perspective

## Slide 62

# Thank You!

@oridavid123
