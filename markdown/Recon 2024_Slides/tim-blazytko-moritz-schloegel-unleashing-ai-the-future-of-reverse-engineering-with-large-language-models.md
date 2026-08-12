---
title: "Unleashing AI The Future of Reverse Engineering with Large Language Models"
speakers: ["Tim Blazytko", "Moritz Schloegel"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Tim Blazytko & Moritz Schloegel_Unleashing AI The Future of Reverse Engineering with Large Language Models.pdf"
pages: 114
sha256: "ec4e875d38d91c5060614606fe98c6994a2ba83375c7125eac030b2a4b6cbbf1"
text_chars: 20902
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.4
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: ["Tim Blazytko & Moritz Schloegel_Unleashing AI The Future of Reverse Engineering with Large Language Models_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:18:30Z"
---
# Unleashing AI The Future of Reverse Engineering with Large Language Models

**Speakers:** Tim Blazytko, Moritz Schloegel  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Tim Blazytko & Moritz Schloegel_Unleashing AI The Future of Reverse Engineering with Large Language Models.pdf` (114 pages)


## Slide 1

#### The Future of Reverse Engineering with Large Language Models

Tim Blazytko Moritz Schloegel Twitter `@mr_phrazer` Twitter `@m_u00d8` HOME `synthesis.to` HOME `mschloegel.me` Envelope tim@blazytko.to Envelope moritz.schloegel@cispa.de

## Slide 2

#### About Us

- Tim Blazytko

   - Chief Scientist & Head of Engineering, co-founder of emproof

   - designs software protections for embedded devices

   - trainer for (de)obfuscation and reverse engineering techniques

- Moritz Schloegel

   - fresh postdoc at CISPA Helmholtz Center

   - working with bugs by day (mostly fuzzing)

   - code deobfuscation by night

1

## Slide 3

Setting the Scene

Question-Circle Using LLMs for RE Magic Local LLMs Trophy Enhancements through Static Analysis

2

## Slide 4

LLMs in Reverse Engineering

## Slide 5

Disclaimer

- hyped and fast-developing field

- teasing powers and limitations for RE

- not specific to tools or LLMs

4

## Slide 6

#### Disclaimer

- hyped and fast-developing field

- teasing powers and limitations for RE

- current snapshot, maybe soon outdated

- • not specific to tools or LLMs

4

## Slide 7

Applications to Reverse Engineering

• renaming variables
• commenting code
• explaining code
• answering questions
• scripting support

### • renaming functions

5

## Slide 8

Applications to Reverse Engineering

• commenting code
• explaining code
• answering questions
• scripting support

- renaming functions

- renaming variables

5

## Slide 9

Applications to Reverse Engineering

• explaining code
• answering questions
• scripting support

- renaming functions

- renaming variables

- commenting code

5

## Slide 10

Applications to Reverse Engineering

• answering questions
• scripting support

- renaming functions

- renaming variables

- commenting code

- explaining code

5

## Slide 11

Applications to Reverse Engineering

• scripting support

- renaming functions

- renaming variables

- commenting code

- explaining code

- answering questions

5

## Slide 12

Applications to Reverse Engineering

- renaming functions

- renaming variables

- commenting code

- explaining code

- answering questions

- scripting support

5

## Slide 13

#### Applications to Reverse Engineering

- renaming functions

- renaming variables

- commenting code

- today: focus on use cases

- • explaining code

- answering questions

- scripting support

5

## Slide 14

Use Case Function Preselection

## Slide 15

“For the given decompiler output, analyze the code and suggest a meaningful function name.”

## Slide 16

\```
Renamedfunctionat0x10002b50toCallWithArguments
Renamedfunctionat0x10004b50toDecodeComplexAlgorithm
Renamedfunctionat0x10008b60toSetValueToMemoryLocation
Renamedfunctionat0x10002b70toCallFunctionPointerWithArguments
\```

## Slide 17

`Renamed function at 0x10002b50 to CallWithArguments Renamed function at 0x10004b50 to DecodeComplexAlgorithm Renamed function at 0x10008b60` often too generic `to SetValueToMemoryLocation Renamed function at 0x10002b70 to CallFunctionPointerWithArguments`

## Slide 18

\```
Renamedfunctionat0x40cbb5toDecompileCodeAnalyze
Renamedfunctionat0x4033c2toDecompileCodeAnalyze
Renamedfunctionat0x4024c2toDecompileCodeAnalyze
Renamedfunctionat0x402d58toDecompileCodeAnalyze
Renamedfunctionat0x40ed62toDecompileAndProtectMemoryPage
Renamedfunctionat0x409e53toDecompileAndFindMatchingStringInMemory
Renamedfunctionat0x40e4ddtoDecompileAndAnalyzeFunction
\```

## Slide 19

`Renamed function at 0x40cbb5 to DecompileCodeAnalyze Renamed function at 0x4033c2 to DecompileCodeAnalyze Renamed function at 0x4024c2 to DecompileCodeAnalyze Renamed function at 0x402d58 to DecompileCodeAnalyze Renamed function` sometimes entirely useless `at 0x40ed62 to DecompileAndProtectMemoryPage Renamed function at 0x409e53 to DecompileAndFindMatchingStringInMemory Renamed function at 0x40e4dd to DecompileAndAnalyzeFunction`

## Slide 20

\```
Renamedfunctionat0x1000cf10toInitializeKeyLoggerAndHandleErrors
Renamedfunctionat0x10014ae0toCreateNamedPipesAndRunShellCommands
Renamedfunctionat0x100186d0toSearchForAProcessByName
Renamedfunctionat0x1001d880toSendHTTPPOSTRequestAndHandleResponse
\```

## Slide 21

`Renamed function at 0x1000cf10 to InitializeKeyLoggerAndHandleErrors Renamed function at 0x10014ae0 to CreateNamedPipesAndRunShellCommands Renamed function at 0x100186d0` can be very helpful `to SearchForAProcessByName Renamed function at 0x1001d880 to SendHTTPPOSTRequestAndHandleResponse`

## Slide 22

Use Case Identification of Library Functions

## Slide 23


> Recovered by OCR — confidence 78/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
@80007ac void* copy_backward_string(void* arg1, void* arg2, int32_t arg3)
@00007ac int32_t i = arg3
@00007be void* r4 = arg2 - 1
@00007b4 void* r3 argi - 1
900007c8 do {
@00007b8 char *(r4 +1)
@06087b8 1
@00007c8 } while (i != 6)
@00007c4 return r3
q
Log Q Search log
[Default] Renaming sub_7ac to copy_backward_string
[Default] Renaming sub_82@ to return_address_of_data_838
[Default] Renaming sub_3e4 to process_input_and_copy_string
[Default] Renaming sub_77c to save_and_clear_fpu_registers
```

## Slide 24

good approximation, but incorrect


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
@80007ac void* copy_backward_string(void* arg1, void* arg2, int32_t arg3)
@60007ac int32_t i arg3
@00007be void* r4 = arg2 - 1
@00007b4 void* r3 = argl - 1
980007c8 do {
@88887b8 char r5 = *(r4 + 1)
good approximation, but incorrect
000007c4 return r3
q
Log Search log
[Default] Renaming sub_7ac to copy_backward_string
[Default] Renaming sub_82@ to return_address_of_data_838
[Default] Renaming sub_3e4 to process_input_and_copy_string
[Default] Renaming sub_77c to save_and_clear_fpu_registers
```

## Slide 25

Enhancing Decompiler Output

## Slide 26

“Enhance the following decompiler output by suggesting more meaningful variable names. Also, add comments.”

## Slide 27

memcpy

15


> Recovered by OCR — confidence 87/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
memcpy
int32_t remaining_bytes = count;
x source_ptr = source - 1;
x dest_ptr = destination —
r byte_to_copy = *(source_ptr + 1);
source_ptr = source_ptr + 1;
x(dest_ptr + 1) = byte_to_copy;
dest_ptr = dest_ptr + 1;
remaining_bytes = remaining_bytes - 1;
(remaining_bytes != @);
dest_ptr;
```

## Slide 28

memcpy

works well for common code

15


> Recovered by OCR — confidence 77/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
memcpy
000007ac int32_t remaining_bytes = count;
@00007be sid’ source_ptr = source - 1;
~~ Jworks well for common code
000007b8 source_ptr = source_ptr + 1;
000007bc *(dest_ptr + 1) = byte_to_copy;
@00007bce dest_ptr = dest_ptr + 1;
@00007c0 remaining_bytes = remaining_bytes - 1;
@00007c0 (remaining_bytes != @);
000007¢4 dest_ptr;
```

## Slide 29

RC4 KSA

16


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RC4 KSA
transform_string(char* input_string, 2 32_tx lookup_table)
* source = input_string;
* index_ptr = nullptr;
_t intermediate_values[1024] = {0};
x buffer;
_-builtin_memset(&buffer, @, @x3fc);
int32_t accumulator = 0;
2_t* intermediate_ptr = intermediate_values;
int32_t temp_val = lookup_func(@:index_ptr, lookup_table);
*(index_ptr + source) = index_ptr->byte_val;
index_ptr = &index_ptr[1];
xintermediate_ptr = zero_extend(*(temp_val + param));
intermediate_ptr = &intermediate_ptr[1];
ile (index_ptr < 0x100);
```

## Slide 30

RC4 KSA

not always helpful

16


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
RC4 KSA
transform_string(char* input_string, 2 32_tx lookup_table) {
* source = input_string;
* index_ptr = nullptr;
_t intermediate_values[1024] = {0};
x buffer;
int32_t accumulator = 0;
2_t* intermediate_ptr not a lways h e lpfu l
int32_t temp_val = lookup_func(@:index_ptr, lookup_table);
x(index_ptr + source) = index_ptr->byte_val;
index_ptr = &index_ptr[1];
xintermediate_ptr = zero_extend(*(temp_val + param));
intermediate_ptr = &intermediate_ptr[1];
ile (index_ptr < 0x100);
```

## Slide 31

Use Case Analysis Guidance for Unfamiliar Instruction Sets

## Slide 32

“Explain me the following assembly snippet.”

## Slide 33

- `; Load Immediate Shifted:`

- `; Load the immediate value 0xc00 into the upper 16 bits of register r3 0000076c 3c600c00 lis r3, 0xc00 {0xc000000}`

- `; Move to Special Purpose Register:`

- `; Move the contents of register r3 to special-purpose register 0x230 00000770 7c708ba6 mtspr 0x230, r3`

- `; Instruction Synchronize:`

- `; Synchronize the instruction stream, ensuring all previous instructions are completed before continuing`

- `00000774 4c00012c isync`

## Slide 34

- `; Load Immediate Shifted:`

- `; Load the immediate value 0xc00 into the upper 16 bits of register r3 0000076c 3c600c00 lis r3, 0xc00 {0xc000000}`

- `; Move to Special Purpose Register:`

- `; Move the contents of register r3 to special-purpose register 0x230 00000770` works well for assembly snippets `7c708ba6 mtspr 0x230, r3 ; Instruction Synchronize: ; Synchronize the instruction stream, ensuring all previous instructions are completed before continuing`

- `00000774 4c00012c isync`

## Slide 35

Use Case Identification of Algorithms

## Slide 36

“Analyze the following code and explain what it does.”

## Slide 37

RC4 KSA

This function performs some kind of data transformation or encryption/decryption by manipulating bytes and using loops to iterate through memory.

22

## Slide 38

RC4 KSA

This function performs some kind of data transformation or encryption/decryptionoften generic or wrong by manipulating bytes and using loops to iterate through memory.

22

## Slide 39

Use Case

Code Logic Explanation

## Slide 40

“The following code implements a crypto algorithm. Which one and why?”

## Slide 41

RC4 KSA

The code snippet likely implements the RC4 cryptographic algorithm due to its characteristic key scheduling and pseudo-random generation processes.

25

## Slide 42

RC4 KSA

The code snippet likely implements the RC4 cryptographic algorithm due to its characteristic key schedulingcontext oft and ps **e** udo-random generation processes.n helps

25

## Slide 43

Use Case Verification Oracle

## Slide 44

“Does the following code implement XXX? Answer YES or NO.”

## Slide 45

“Does the following code implement XXX? Answer YES or NO.” good to filter false positives from heuristics

## Slide 46

Use Case

Script Development

## Slide 47

“The following code implements a string decryption routine. Rebuilt it in Python.”

## Slide 48

\```
defdecrypt(input_string):
xor_key=0x22
decrypted_chars=[chr(ord(char)^xor_key)forcharininput_string]
return''.join(decrypted_chars)
\```

30

## Slide 49

`def decrypt(input_string): xor_key = 0x22 decrypted_chars = [chr(ord(char) ^ xor_key) for char in input_string] return ''.join(decrypted_chars)` works fine for small tasks

30

## Slide 50

#### Interim Conclusion

- good for approximations and high-level understanding

- answers sometimes generic or wrong

- adding context often helps

- no real (code) understanding

31

## Slide 51

Tools

## Slide 52

Tools & Integrations (Selection)

- various tools and wrappers for commercial LLMs

- IDA Pro: Gepetto, Copilot for IDA Pro

- Ghidra: GhidraChatGPT, GptHidra

- Binary Ninja: Sidekick, BinaryNinja-OpenAI

33

## Slide 53

Gepetto

\```
https://github.com/JusticeRage/Gepetto
\```

34


> Recovered by OCR — confidence 71/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Gepetto
a
int result; //
char Str(1021]; //
char Destination[257]; //
1, sizeof( Synchronize with >
Edit var comment. 1
streat( » PathName) ; Collapse declarations Numpad+-
streat(! » aUpgradeExe) ; Mark as decompiled
ees + 5 Copy to assembly
an Hide casts \
https://github.com/JusticeRage/Gepetto
34
```

## Slide 54

#### Binary Ninja Sidekick

\```
https://sidekick.binary.ninja/
\```

35

## Slide 55

Downsides

## Slide 56

GLOBE Internet connection required

## Slide 57

Money-Bill-Alt Every query costs $$$

## Slide 58

EYE Privacy risks

## Slide 59

# LIGHTBULB Local LLMs

38

## Slide 60

Local LLMs

Pros:

- offline

- privacy-sensitive

39

## Slide 61

Local LLMs

Cons:

Pros:

- offline

   - slower

- privacy-sensitive

39

## Slide 62

Local LLMs

## Cons:

Pros:

- offline

- privacy-sensitive

- slower

- less powerful

39

## Slide 63

#### Local LLMs

## Cons:

Pros:

- offline

- privacy-sensitive

- slower

- less powerful

- computation resources

39

## Slide 64

Local LLMs are .. slower

Anecdotally, for some function renaming queries: • GPT query: <2s

• Mistral 7B on M1 Macbook Pro: 5-8s

• Mistral 7B on M3 Macbook Air: 10s

40

## Slide 65

Local LLMs are .. less powerful

1500
1500
1250
1000
750
500
250 175
20 7 47
0
41
GPT3 GPT3.5 Turbo GPT4 Mistral 7B Mixtral 8x7B
#parameters (in billions)

## Slide 66

Local LLMs require computation resources

Good GPU:

- NVIDIA GTX 3090

- NVIDIA GTX 4090

ARM-based Mac:

- M1/M2/M3 Macbook

- or workstation

42

## Slide 67

Good news: We can already use local LLMs for RE

43

## Slide 68

(Unfair) Comparison to GPT4

Use Case Mistral 7B Mixtral 8x7B function renaming identify library functions enhance decompiler output annotate assembly explain code logic helper script development verification oracle

44

## Slide 69

# Can we do better?

45

## Slide 70

Context-sensitive Annotations

Context helps..

46

## Slide 71

Context-sensitive Annotations

..so let’s use available information!

46

## Slide 72

Context-sensitive Annotations

_⇒_ incorporate insights from static analysis

46

## Slide 73

Context-sensitive Annotations

example: function renaming

46

## Slide 74

Context-sensitive Annotations

LIGHTBULB rename only “relevant” functions

46

## Slide 75

Context-sensitive Annotations

improves accuracy and speed LIGHTBULB rename only “relevant” functions

46

## Slide 76

Context-sensitive Annotations

46


> Recovered by OCR — confidence 76/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Context-sensitive Annotations
1@@@ead@ enum WIN32_ERROR __fastcall configure_proxy_settings( * argl)
1608eadd * fsbase
10@8eadd var_c = *fsbase
10@8eade *fsbase = &var_c
10@8eaee var_114 = @
10@8eb3a if (var_11@ != @)
1008eb65 if (eax_3 != @)
10@8eb6d esi_2 = &eax_3[5]
sub_1002e3d@(&var_118, “http=")
```

## Slide 77

Context-sensitive Annotations

strings and API functions

46


> Recovered by OCR — confidence 75/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Context-sensitive Annotations
1@@@ead@ enum WIN32_ERROR __fastcall configure_proxy_settings( * argl)
16@8eadd * fsbase
10@8eadd var_c = *fsbase
10@8eade *fsbas|
"eae strings and API functions
10@8eb3a if (var_11@ != @)
16@8eb59 * eax_3 = sub_1002e3d0(&var_118, "http=")
1008eb65 if (eax_3 != @)
10@Geb6d esi_2 = &eax_3[5]
```

## Slide 78

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 79

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990 memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 80

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990 memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 81

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540 strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 82

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540 strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 83

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150 strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 84

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150 strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 85

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190 CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 86

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190 CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 87

#### Context-sensitive Annotations

sub_400540
sub_409760 sub_4090d0 sub_40c150strcmp sub_40c570 sub_40c990memcpy
sub_40cd70
sub_40d190CallsFunc sub_4004f0
?
sub_400510 sub_400540strlen call graphmissing context
sub_400600 sub_400740

47

## Slide 88

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 89

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600 writeFile sub_400740execute

48

## Slide 90

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600 writeFile sub_400740execute

48

## Slide 91

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740 execute

48

## Slide 92

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740 execute

48

## Slide 93

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExec sub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 94

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExec sub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 95

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190 launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 96

Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190 launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 97

#### Context-sensitive Annotations: Bottom-up Propagation

sub_400540
sub_409760 sub_4090d0 sub_40c150 sub_40c570 sub_40c990
sub_40cd70
sub_40d190launchFile sub_4004f0
writeAndExecsub_400510 sub_400540 simple but effective
sub_400600writeFile sub_400740execute

48

## Slide 98

# Tools

49

## Slide 99

Tools

\```
https://github.com/mrphrazer/reverser_ai
\```

50


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tools
ReverserAl (v1.1)
Author: Tim Blazytko
Provides automated reverse engineering assistance through the use of local large language models (LLMs) on
consumer hardware.
Description:
ReverserAl is a research project designed to automate and enhance reverse engineering tasks through the use of
locally-hosted large language models (LLMs). Operating entirely offline, this initial release features the automatic
suggestion of high-level, semantically meaningful function names derived from decompiler output. ReverserAl is
provided as a Binary Ninja plugin; however, its architecture is designed to be extended to other reverse
engineering platforms such as IDA and Ghidra.
https://github.com/mrphrazer/reverser_ai
50
```

## Slide 100

ReverserAI

- Binja plugin to include local LLMs

- more playground than finished product

- supports two models (Mistral 7B and Mixtral 8x7B)

51

## Slide 101

# Can we do better?

52

## Slide 102

#### Things to improve

- better queries (prompt engineering)

- better models: `https://github.com/eugeneyan/open-llms`

- fine-tuned models

53

## Slide 103

#### Things to improve

- better queries (prompt engineering)

- better models: `https://github.com/eugeneyan/open-llms`

- fine-tuned models

53

## Slide 104

aIDAPal

\```
https://github.com/atredispartners/aidapal
\```

54


> Recovered by OCR — confidence 80/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
alDAPal
About
aiDAPal is an IDA Pro plugin that uses a
locally running LLM that has been fine-
tuned for Hex-Rays pseudocode to
1 README.md Update README.md
eks ag0 assist with code analysis.
1 idapal.py initial plugin upload 3weeks ago Readme
© Custom properties
YY 94 stars
Y 9 forks
aiDAPal Report repository
https://github.com/atredispartners/aidapal
54
```

## Slide 105

#### aIDAPal

- plugin for IDA with focus on enhancing decompiler output

- fine-tuned Mistral 7B _⇒_ can keep up with GPT4

- also uses available context information

55

## Slide 106

aIDAPal

- plugin for IDA with focus on enhancing decompiler output

- • fine-tuned Mistral 7Bfine-tuning works well _⇒_ can keep up with GPT4

- also uses available context information

55

## Slide 107

Currently Impossible

- _real_ code analysis

- bug finding (beyond easy patterns)

- cross-function analysis

56

## Slide 108

Currently Impossible

- _real_ code analysis

- bug finding (beyond easy patterns)

- LLMs as helper, not automated analysts

- cross-function analysis

56

## Slide 109

Future Trends

## Slide 110

Expectations

- enhanced scalability for broader inputs

- advancements in on-device LLMs

58

## Slide 111

Potential Emerging RE Applications

- semantic code search

- identification of noteworthy code segments

- patch recommendation systems

- binary similarity and clustering

59

## Slide 112

Conclusion

## Slide 113

Takeaways

1. LLMs are good for approximations and high-level understanding

2. But: They can be wrong and have no real (code) understanding

3. Adding context often helps increase accuracy

4. Local LLMs are somewhat worse but ensure privacy

61

## Slide 114

#### Summary

- (local) LLMs help, check them out

- but they are no panacea, be wary of the hype

Tim Blazytko Twitter `@mr_phrazer` HOME `synthesis.to`

Moritz Schloegel

Twitter `@m_u00d8` HOME `mschloegel.me`

62

## Companion resources

### `Tim Blazytko & Moritz Schloegel_Unleashing AI The Future of Reverse Engineering with Large Language Models_tools.txt`

```text
https://github.com/mrphrazer/reverser_ai
```
