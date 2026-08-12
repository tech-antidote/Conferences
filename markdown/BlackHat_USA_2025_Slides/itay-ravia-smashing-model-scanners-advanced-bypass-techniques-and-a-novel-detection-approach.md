---
title: "Smashing Model Scanners Advanced Bypass Techniques and a Novel Detection Approach"
speakers: ["Itay Ravia"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Itay Ravia_Smashing Model Scanners Advanced Bypass Techniques and a Novel Detection Approach.pdf"
pages: 60
sha256: "775a0c4c8807b7c0c2cad84ff253387964a0b368e2eaa4accddf58fe477961f1"
text_chars: 22443
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:55:13Z"
---
# Smashing Model Scanners Advanced Bypass Techniques and a Novel Detection Approach

**Speakers:** Itay Ravia  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Itay Ravia_Smashing Model Scanners Advanced Bypass Techniques and a Novel Detection Approach.pdf` (60 pages)

## Slide 1

**Smashing Model Scanners** Advanced Bypass Techniques and a Novel Detection Approach

By Itay Ravia Head of Aim Labs

#BHUSA   @BlackHatEvents

## Slide 2

## **About me**

- On a mission to secure the AI revolution, which is currently like a whack-a-mole game

- Over a decade of cybersecurity and AI research

- ● Head of Aim Labs @ Aim Security

- Author of #EchoLeak vulnerability (CVSS score 9.3) in M365 Copilot - First AI agent 0-click

#BHUSA   @BlackHatEvents

## Slide 3

The risks of using 3p AI models

## **Today’s Menu**

How current protections are inherently flawed

A novel detections approach FTW

#BHUSA   @BlackHatEvents

## Slide 4

### **Weights**

## **What are AI Models?**

Usually millions-billions of numerical parameters

Models are made out of 2 parts

**Architecture**

How those parameters interact with one another

#BHUSA   @BlackHatEvents

## Slide 5

**What are AI Models?**

These days you can find architectures for nearly any task you have in mind on platforms such as Hugging Face

#BHUSA   @BlackHatEvents

## Slide 6

## **What are AI Models?**

ML engineers / data scientists use proprietary or public datasets to retrain existing models to their very-specific subtask

#BHUSA   @BlackHatEvents

## Slide 7

## **ML Frameworks & Formats**

|**ML Framework**|**Model file formats**|**Serialization format**|
|---|---|---|
|PyTorch|PyTorch ZIP|Pickle inside Zip|
||PyTorch legacy|Pickle|
|Tensorflow|Keras v3|“Json”|
||Keras legacy|HDF5|
||SavedModel|“Protobuf”|
|Transformers|SafeTensors
…|“Json” + SafeTensors|
|MLflow|-|Pickle
Cloudpickle (still pickle…)|
|Joblib|Joblib|Joblib pickle|
|ONNX|ONNX|Protobuf|

#BHUSA   @BlackHatEvents

## Slide 8

## **ML Frameworks & Formats**

|**ML Framework**|**Model file formats**|**Serialization format**|
|---|---|---|
|PyTorch|PyTorch ZIP|**Pickle**inside Zip|
||PyTorch legacy|**Pickle**|
|Tensorflow|Keras v3|“Json”|
||Keras legacy|HDF5|
||SavedModel|“Protobuf”|
|Transformers|SafeTensors
…|“Json” + SafeTensors|
|MLflow|-|**Pickle**
Cloudpickle (still**pickle…**)|
|Joblib|Joblib|Joblib**pickle**|
|ONNX|ONNX|Protobuf|

#BHUSA   @BlackHatEvents

## Slide 9

## **ML Frameworks & Formats**

|**ML Framework**|**Model file formats**|**Serialization format**|
|---|---|---|
|PyTorch|PyTorch ZIP|**Pickle**inside Zip|
||PyTorch legacy|**Pickle**|
|Tensorflow|Keras v3|**“Json”**|
||Keras legacy|**HDF5**|
||SavedModel|**“Protobuf”**|
|Transformers|SafeTensors
…|“Json” + SafeTensors|
|MLflow|-|**Pickle**
Cloudpickle (still**pickle…**)|
|Joblib|Joblib|Joblib**pickle**|
|ONNX|ONNX|Protobuf|

#BHUSA   @BlackHatEvents

## Slide 10

## **ML Frameworks & Formats**

|**ML Framework**|**Model file formats**|**Serialization format**|
|---|---|---|
|PyTorch|PyTorch ZIP|**Pickle**inside Zip|
||PyTorch legacy|**Pickle**|
|Tensorflow|Keras v3|**“Json”**|
||Keras legacy|**HDF5**|
||SavedModel|**“Protobuf”**|
|Transformers|SafeTensors
…|**“Json”**+ SafeTensors|
|MLflow|-|**Pickle**
Cloudpickle (still**pickle…**)|
|Joblib|Joblib|Joblib**pickle**|
|ONNX|ONNX|Protobuf|

#BHUSA   @BlackHatEvents

## Slide 11

### **Black Hat Asia 2024**

[1] Peng Zhou, https://i.blackhat.com/Asia-24/Presentations/Asia-24-Zhou-HowtoMakeHuggingFace.pdf

#BHUSA   @BlackHatEvents

## Slide 12

## **Using 3p Models Risks**

Code Execution Load Time

Code Execution Inference Time

Backdoored Inputs

#BHUSA   @BlackHatEvents

## Slide 13

## **Current Protection: Static Scanners**

Contain a preset denylist / allowlist of modules and functions, based on known methods attackers can use to inject malicious payloads into the model files

For example, using os.system in a pickle is detected as malicious

In other formats, based on rules denylisting modules, such as Lambda functions in Keras

#BHUSA   @BlackHatEvents

## Slide 14

## **HF Picklescan**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS >
HF Picklescan
class A:
def __reduce__(self):
return os.system, ("echo Pwned.", )
torch.save(A(), "/tmp/pytorch_model.bin")
Detected Pickle imports (1)
"posix.system"
model = torch.nn.Linear(10, 20)
torch.save(model.state_dict(), "/tmp/state_dict.pt")
Detected Pickle imports (3)
“collections.OrderedDict",
“torch.FloatStorage",
“torch._utils. rebuild tensor_v2"
model = torch.nn.Linear(10, 20)
torch.save(model, "/tmp/pytorch_model.bin")
Detected Pickle imports (6)
“_builtin__.set",
"“torch._utils. rebuild parameter”,
“torch.FloatStorage",
“torch.nn.modules.linear.Linear",
"collections.OrderedDict",
“torch._utils._rebuild_tensor_v2"
#BHUSA @BlackHatEvents
```

## Slide 15

## **Bypass Method #1**

Thousands of python libraries, thousands of functions within each

Scanners denylist can never be comprehensive

Wrote an AI agent to find esoteric functions that call python exec / eval / other unsafe functions based on GitHub source code

#BHUSA   @BlackHatEvents

## Slide 16

## **Bypass Method #1**

2 hours of work yielded >50 “easy examples” of unsafe functions missed by current static scanners

#BHUSA   @BlackHatEvents

## Slide 17

## **Bypass Method #1**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Bypass :
Method #1
Detected Pickle imports (1) x File Security Scans '
{ pytorch_model.bin
"mlflow.projects.backend.local._run_entry_
v No issue
v No issue
v No issue
> Send
#BHUSA @BlackHatEvents
```

## Slide 18

## **Static Scanners Shortcomings**

Near impossible

to create a comprehensive denylist

#BHUSA   @BlackHatEvents

## Slide 19

## **Bypass Method #2**

In pickle formats - using dill / cloudpickle imports, but also in others such as Keras Lambda layers

Custom architectures may include python bytecode into the model file

Hence, model scanning is at least as complex a problem as the halting problem

Static code analysis is NP-hard, leaving static scanners at an obvious disadvantage

#BHUSA   @BlackHatEvents

## Slide 20

## **Bypass Method #2**

Even simple examples go undetected

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat '
BRIEFINGS ela
Bypass EEE
Method #2
Even simple examples go
» 4
y
Z
oO
undetected s
uuu uu
H
et
ig?
module = torch.__builtins__[x + y + z](o + s)
module.system("echo \"You've been pwned.\"")
return arg
#BHUSA @BlackHatEvents
```

## Slide 21

## **Bypass Method #2**

Even simple examples go undetected

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Bypass
Method #2
Even simple examples go
undetected
(arg):
xX
y=
Detected Pickle imports (10)
"collections.OrderedDict",
"dill._dill._import_module",
"dill._dill._create_function",
"torch._utils._rebuild_tensor_v2",
"dill._dill._create_code",
"torch.FloatStorage",
"_codecs.encode",
"torch.nn.modules.linear.Linear",
"dill._dill._load_type",
"torch._utils._rebuild_parameter"
File Security Scans
{ pytorch_model.bin
v No issue
Y No issue
#BHUSA @BlackHatEvents
```

## Slide 22

## **Static Scanners Shortcomings**

Near impossible Computationally There is inherent to create a limited because ambiguity in only comprehensive static code analysis looking at modules denylist is NP-hard used

#BHUSA   @BlackHatEvents

## Slide 23

## **Bypass Method #3**

Static scanners are over-simplistic in their simulation of the loading process

Let’s talk Pickles…

#BHUSA   @BlackHatEvents

## Slide 24

## **Bypass Method #3**

Static scanners are over-simplistic in their simulation of the loading process

Python assembly language - retains state over two data structures:

- Stack - LIFO structure

- Random access memory

#### For our purposes:

- PYTHON_IMPORT (GLOBAL, STACK_GLOBAL)

- PUSH_STACK / POP_STACK (STRING, INT, …)

- PUT_MEM / GET_MEM (PUT, BINPUT, MEMOIZE, GET, BINGET)

- INSTANTIATE (INST, OBJ)

- CALL_IMPORTED_FUNC (REDUCE)

#BHUSA   @BlackHatEvents

## Slide 25

## **Bypass Method #3**

Static scanners are over-simplistic in their simulation of the loading process

[2] mmaitre314, https://github.com/mmaitre314/picklescan

#BHUSA   @BlackHatEvents

## Slide 26

## **Bypass Method #3**

An attacker could utilize this to desynchronize scanner and unpickler

[2] mmaitre314, https://github.com/mmaitre314/picklescan

#BHUSA   @BlackHatEvents

## Slide 27

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT

STACK MEMO DETECTED IMPORT 0 1 1 2 2 3

##### UNPICKLER DATA STRUCTURES

STACK MEMO ACTUAL IMPORT 0 1 1 2 2 3

#BHUSA   @BlackHatEvents

## Slide 28

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT PUSH_STACK “os”

STACK MEMO “os” 0 1 2

DETECTED IMPORT 1 2 3

UNPICKLER DATA STRUCTURES

STACK MEMO ACTUAL IMPORT “os” 0 1 1 2 2 3

#BHUSA   @BlackHatEvents

## Slide 29

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT PUSH_STACK “os” INSTANTIATE “builtins str”

DETECTED IMPORT

STACK MEMO DETECTED IMPORT “os” 0 1 builtins.str 1 2 2 3

##### UNPICKLER DATA STRUCTURES

ACTUAL IMPORT

STACK MEMO ACTUAL IMPORT “os” 0 1 builtins.str 1 2 2 3

#BHUSA   @BlackHatEvents

## Slide 30

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT PUSH_STACK “os” INSTANTIATE “builtins str”

DETECTED IMPORT

STACK MEMO DETECTED IMPORT “os” 0 “builtins str” 1 builtins.str 1 2 2 3

PUT_MEM 0

##### UNPICKLER DATA STRUCTURES

ACTUAL IMPORT

STACK MEMO ACTUAL IMPORT “os” 0 “os” 1 builtins.str 1 2 2 3

#BHUSA   @BlackHatEvents

## Slide 31

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT PUSH_STACK “os”

INSTANTIATE “builtins str”

DETECTED IMPORT

STACK MEMO DETECTED IMPORT “os” 0 “builtins str” 1 builtins.str “builtins str” 1 2 2 3

PUT_MEM 0

##### UNPICKLER DATA STRUCTURES

GET_MEM 0

STACK “os” “os”

ACTUAL IMPORT

MEMO 0 “os” 1 1 2 2 3

1 builtins.str

#BHUSA   @BlackHatEvents

## Slide 32

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT PUSH_STACK “os”

INSTANTIATE “builtins str”

DETECTED IMPORT

STACK MEMO DETECTED IMPORT “os” 0 “builtins str” 1 builtins.str “builtins str” 1 2 “system” 2 3

PUT_MEM 0

##### UNPICKLER DATA STRUCTURES

GET_MEM 0 PUSH_STACK “system”

STACK “os” “os” “system”

MEMO ACTUAL IMPORT 0 “os” 1 builtins.str 1 2 2 3

#BHUSA   @BlackHatEvents

## Slide 33

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os”

INSTANTIATE “builtins str”

DETECTED IMPORT

STACK MEMO DETECTED IMPORT “os” 0 “builtins str” 1 builtins.str “builtins str” 1 2 builtins str.system “system” 2 3

PUT_MEM 0

##### UNPICKLER DATA STRUCTURES

GET_MEM 0

PUSH_STACK “system”

PYTHON_IMPORT

STACK MEMO ACTUAL IMPORT “os” 0 “os” 1 builtins.str “os” 1 2 os.system “system” 2 3

#BHUSA   @BlackHatEvents

## Slide 34

**Bypass Method #3** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os”

INSTANTIATE “builtins str”

DETECTED IMPORT

|STACK||MEMO||DETECTED IMPORT|
|---|---|---|---|---|
|“os”|0|“builtins str”|1|builtins.str|
|“builtins str”|1||2|builtins str.system|
|“system”|2||3||

PUT_MEM 0

##### UNPICKLER DATA STRUCTURES

GET_MEM 0

PUSH_STACK “system”

PYTHON_IMPORT

STACK MEMO ACTUAL IMPORT “os” 0 “os” 1 builtins.str “os” 1 2 os.system “system” 2 3

#BHUSA   @BlackHatEvents

## Slide 35

Bypass Method #3 SCANNER DATA STRUCTURES
INPUT STACK MEMO DETECTED IMPORT
“os” 0 “builtins str” 1 builtins.str
PUSH_STACK “os”
“builtins str” 1 2 builtins str.system
INSTANTIATE “builtins str”
“system” 2 3
PUT_MEM 0
UNPICKLER DATA STRUCTURES
GET_MEM 0 STACK MEMO ACTUAL IMPORT
“os” 0 “os” 1 builtins.str
PUSH_STACK “system”
“os” 1 2 os.system
PYTHON_IMPORT
“system” 2 3
#BHUSA   @BlackHatEvents

## Slide 36

## **Static Scanners Shortcomings**

Near impossible Computationally to create a limited because comprehensive static code analysis denylist is NP-hard

There is inherent Always behind the ambiguity in only curve of novel looking at modules attack methods used

#BHUSA   @BlackHatEvents

## Slide 37

## **Bypass Method #4**

Joblib - a pickle that’s optimized for numpy arrays

Some model file formats are just too complicated to statically analyze

A block of pickle opcodes with numpy array “interruptions” in the middle:

- Random numpy array bytes (dtype uint32, float16, …)

- Embedded pickle blobs that use a new stack and new memo (dtype object)

#BHUSA   @BlackHatEvents

## Slide 38

### **Bypass Method #4** SCANNER DATA STRUCTURES

INPUT
PUSH_STACK “os”
PUT_MEM 0
PUSH_STACK “system”
PUT_MEM 1

STACK MEMO DETECTED IMPORT
“os” 0 “os” 1
“system” 1 “system” 2

##### UNPICKLER DATA STRUCTURES

STACK MEMO ACTUAL IMPORT
“os” 0 “os” 1
“system” 1 “system” 2
2 3
3 4

#BHUSA   @BlackHatEvents

## Slide 39

**Bypass Method #4** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os” PUT_MEM 0 PUSH_STACK “system”

STACK MEMO DETECTED IMPORT
“os” 0 “os” 1 joblib.NumpyArrayWrapper
“system” 1 “system” 2

##### UNPICKLER DATA STRUCTURES

PUT_MEM 1

Numeric values from an array with a dynamically determined length

STACK MEMO ACTUAL IMPORT
“os” 0 “os” 1 joblib.NumpyArrayWrapper
“system” 1 “system” 2
2 3
3 4

#BHUSA   @BlackHatEvents

## Slide 40

**Bypass Method #4** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os” PUT_MEM 0

|STACK||MEMO|DETECTED IMPORT|
|---|---|---|---|
|“os”|0|“os”|1
joblib.NumpyArrayWrapper|
|“system”|1|“system”|2|

PUSH_STACK “system”

##### UNPICKLER DATA STRUCTURES

PUT_MEM 1

Numeric values from an array with a dynamically determined length

GET_MEM 0

STACK MEMO ACTUAL IMPORT
“os” 0 “os” 1 joblib.NumpyArrayWrapper
“system” 1 “system” 2
“os” 2 3
3 4

#BHUSA   @BlackHatEvents

## Slide 41

**Bypass Method #4** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os” PUT_MEM 0

|STACK||MEMO|DETECTED IMPORT|
|---|---|---|---|
|“os”|0|“os”|1
joblib.NumpyArrayWrapper|
|“system”|1|“system”|2|

PUSH_STACK “system”

##### UNPICKLER DATA STRUCTURES

PUT_MEM 1

Numeric values from an array with a dynamically determined length

GET_MEM 0

GET_MEM 1

PYTHON_IMPORT

|STACK||MEMO|ACTUAL IMPORT|
|---|---|---|---|
|“os”|0|“os”|1
joblib.NumpyArrayWrapper|
|“system”|1|“system”|2
os.system|
|“os”|2||3|
|“system”|3||4|

#BHUSA   @BlackHatEvents

## Slide 42

**Bypass Method #4** SCANNER DATA STRUCTURES

INPUT

PUSH_STACK “os” PUT_MEM 0

|STACK||MEMO|DETECTED IMPORT|
|---|---|---|---|
|“os”|0|“os”|1
joblib.NumpyArrayWrapper|
|“system”|1|“system”|2|

PUSH_STACK “system”

##### UNPICKLER DATA STRUCTURES

PUT_MEM 1

Numeric values from an array with a dynamically determined length

GET_MEM 0

GET_MEM 1

PYTHON_IMPORT

|STACK||MEMO|ACTUAL IMPORT|
|---|---|---|---|
|“os”|0|“os”|1
joblib.NumpyArrayWrapper|
|“system”|1|“system”|2
os.system|
|“os”|2||3|
|“system”|3||4|

#BHUSA   @BlackHatEvents

## Slide 43

## **Bypass Method #4**

Some model file formats are just too complicated to statically analyze

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Bypass File Security Scans ;
Method HA { model11.joblib
Some model file formats are just v No issue (7
too complicated to statically
©Q d
analyze
v No issue
Detected Pickle imports (4)
‘sklearn.Linear_model._base.LinearRegres
‘joblib.numpy_pickle.NumpyArrayWrapper",
“numpy.ndarray",
“numpy .dtype"
#BHUSA @BlackHatEvents
```

## Slide 44

## **Static Scanners Shortcomings**

Near impossible Computationally to create a limited because comprehensive static code analysis denylist is NP-hard

There is inherent ambiguity in only looking at modules used

Always behind the Some formats too curve of novel convoluted to attack methods properly analyze this way

#BHUSA   @BlackHatEvents

## Slide 45

## **Why not allowlist-based static scanners then?**

Custom architectures often include non-standard libraries

For example, YOLO models achieve State-of-the-Art results for image-based tasks  while relying on non-standard ultralytics library

#BHUSA   @BlackHatEvents

## Slide 46

## **Why not allowlist-based static scanners then?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2) : aN @ultralytics/YOLO121 ‘OG like 92 Follow @ Ultralytics 256
blackhat
BRIEFINGS — ultralytics lilanguages all EvalResults  # License: agpl-3.0
# Model card 15 Filesand versions #& Community 3
Why not P mainy YOLO11
rs | l low li Sst- b aS e d 9) This model has 10 files scanned as suspicious. {Show files
stat i Cc SCa n n e rs  fcakyon Update README.md — 6adfddb
th Q) .gitattributes © safe 1.52 kB
en?
{\ README.md « 29.3 kB
O yololil-seg.pt + File Security Scans x 56.1 MB @LFS
) yolo111-pose.pt
1 yolollm-pose.pt — 42.5 MB @ LFS
( yololim-seg.pt X Suspicious 45.4 MB @ LFS
1) yololin-seg.pt No issue 6.18 MB @LFS
ih}
```

## Slide 47

## **Why not allowlist-based static scanners then?**

Custom architectures often include non-standard libraries

For example, YOLO models achieve State-of-the-Art results for image-based tasks  while relying on non-standard ultralytics library

Formats such as SafeTensors also struggle with custom architectures

#BHUSA   @BlackHatEvents

## Slide 48

## **Let’s talk about DeepSeek and Kimi-K2**

Their architectures were not included in standard SafeTensors libraries such as transformers

To allow loading this SafeTensors repo, transformers allows loading architectures from custom code shipped in the repo.

#BHUSA   @BlackHatEvents

## Slide 49

## **Let’s talk about DeepSeek and Kimi-K2**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Let’s talk about
DeepSeek and
Kimi-K2
"auto_map": {
"AutoConfig": "configuration_deepseek.DeepseekV3Config",
"AutoModel": "modeling_deepseek.DeepseekV3Model",
"AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
3,
{\ modeling deepseek.py © safe
{A tokenizer.json © safe File Security Scans v
{\ modeling_deepseek. py
( tokenizer_config.json ©
not a model
not a pickle
#BHUSA @BlackHatEvents
```

## Slide 50

## **How to Handle Static Scanners’ Shortcomings?**

Pickle has existed for ages, but model scanning is different

Static scanners are like EDRs having malware hashes

Tracing inside a sandbox FTW

#BHUSA   @BlackHatEvents

## Slide 51

## **Why is that the right approach?**

Model loading and inference performs an expected set of system and library calls

By strictly marking “normal” operations, we easily get a comprehensive list of “abnormal” actions for models Targets the “exploit” part of a supply chain attack, and once an attack is recognized, “hashes” can be updated to include it as well

#BHUSA   @BlackHatEvents

## Slide 52

## **Why is that the right approach?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Issues 3
WI i tl t tl RITY DETECTED BY URCE FILE
y 4 Critical aim-glibc-code-execution % Dynamic Scanner © model 1 joblib a
= oP
right approach‘ =
glibc _libc_system called with argO: echo "You've been pwned."
glibc _libc_system called with argO: sleep 0.1
ISSUE DESCRIPTION @ REMEDIATION
This model uses execution functions that are As no ML framework requires CLI commands as
capable of running arbitrary commands on the part of its loading or inference process, avoid
host system during loading. using this model altogether.
al High aim-glibc-process-manipulation % Dynamic Scanner © model 1 joblib v
al High aim-sys-process-creation % Dynamic Scanner OB model 1 joblib v
```

## Slide 53

## **Why is that the right approach?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Issues 1
ERITY WY ISSUE DETECTED BY SOURCE FILE
Why is t h at t h e ul High aim-sys-process-creation % Dynamic Scanner Q pytorch_model.bin
right approach? so
syscall vfork called
ISSUE DESCRIPTION @ REMEDIATION
This model uses process creation syscalls during As no ML framework creates new processes in
loading, which spawn processes that are untraced. loading or inference time, this is highly likely a
malicious model. Avoid using it altogether.
```

## Slide 54

## **Why is that the right approach?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Issues 2
Wh Leal ERITY WY ISSUE DETECTED BY SOURCE FILE
is that the
y 4 Critical aim-python-lib-mlflow-cmd ® Static Scanner © pytorch_model.bin v
=
r | g h t a @) @) ro ac h ? ul High aim-sys-process-creation % Dynamic Scanner O pytorch_model.bin =~
DETAILS
syscall vfork called
ISSUE DESCRIPTION @ REMEDIATION
This model uses process creation syscalls during As no ML framework creates new processes in
loading, which spawn processes that are untraced. loading or inference time, this is highly likely a
malicious model. Avoid using it altogether.
```

## Slide 55

## **Why is that the right approach?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Issues 1
Why is that the ——
right approach? _
syscall connect called with ip_address: 192.168.116.131
syscall socket called
UE DETECTED BY SOURCE FILE
aim-sys-network % Dynamic Scanner © model.pkl a
ISSUE DESCRIPTION @ REMEDIATION
This model uses network-related syscalls Avoid using this model. To further inspect this
during loading, which can enable unauthorized incident, collect more information about the
network access, data exfiltration, or command _ remote address using your network admin or
and control activities. by using public tools such as whois.
```

## Slide 56

## **Why is that the right approach?**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Why is that the
right approach?
Issues 4
SEVERITY SSUE
A Critical
aim-glibc-code-execution
DETECTED BY
SOURCE FILE
% Dynamic Scanner © model.keras
glibc _libc_system called with argO: echo "You've been pwned."
ISSUE D TION
This model uses execution functions that are
capable of running arbitrary commands on the
host system during loading.
al High aim-glibc-process-manipulation
aim-sys-process-creation
aim-keras-unsafe-layer
DETAILS
Use of unsafe Keras layer Lambda
ISSUE DESCRIPTION
This model uses Lambda layers that execute
arbitrary code at both runtime and build time
during model loading. Proper sanitization of this
code requires Dynamic Scanning.
@ REMEDIATION
As no ML framework requires CLI commands as
part of its loading or inference process, avoid
using this model altogether.
% Dynamic Scanner OG model.keras
% Dynamic Scanner © model.keras
® Static Scanner © model.keras
@ REMEDIATION
If this is a homegrown model, consider
converting the Lambda layer to a standard,
already-defined Keras layer if possible. If this is
an untrusted model, use this model only if the
Dynamic Scanner concluded there are no
malicious actions embedded into the model.
```

## Slide 57

## **Static Scanners Shortcomings**

Near impossible Computationally to create a limited because comprehensive static code analysis denylist is NP-hard

There is inherent Always behind the Some formats too ambiguity in only curve of novel attack convoluted to properly looking at modules methods analyze this way used

#BHUSA   @BlackHatEvents

## Slide 58

## **Dynamic Scanners Strengths**

Computationally limited because static code analysis is NP-hard

Near impossible to create a comprehensive denylist

Easy to build an No static analysis exhaustive list of needed as all abnormal system and formats are easy to library calls load / infer

There is inherent ambiguity in only looking at modules used

Unveils novel backdooring methods without prior knowledge

Always behind the curve of novel attack methods Running python (byte)code is not NP-hard ;)

Some formats too convoluted to properly analyze this way No ambiguity when tracing the actual operations

#BHUSA   @BlackHatEvents

## Slide 59

## **Black Hat Sound Bytes**

As data scientists experiment with custom architectures, supply chain risk from model files is here to stay

Static scanners have inherent shortcomings and are always “behind the attackers curve”

Dynamically tracing model operation in a sandbox detects both existing and novel attack methods

#BHUSA   @BlackHatEvents

## Slide 60

# **Thank You!**

Itay Ravia Head of Aim Labs

#BHUSA   @BlackHatEvents
