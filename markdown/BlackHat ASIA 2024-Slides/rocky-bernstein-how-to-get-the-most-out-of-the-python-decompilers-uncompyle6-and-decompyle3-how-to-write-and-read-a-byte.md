---
title: "How to Get the Most Out of the Python Decompilers Uncompyle6 and Decompyle3 - How to Write and Read a Bytecode Decompiler"
speakers: ["Rocky Bernstein"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Rocky Bernstein-How to Get the Most Out of the Python Decompilers Uncompyle6 and Decompyle3 - How to Write and Read a Bytecode Decompiler.pdf"
pages: 110
sha256: "b088658647a2af49818185317f354793efd69a3eefbbf22ecc5ff9b040010bdf"
text_chars: 51086
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:50:58Z"
---
# How to Get the Most Out of the Python Decompilers Uncompyle6 and Decompyle3 - How to Write and Read a Bytecode Decompiler

**Speakers:** Rocky Bernstein  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Rocky Bernstein-How to Get the Most Out of the Python Decompilers Uncompyle6 and Decompyle3 - How to Write and Read a Bytecode Decompiler.pdf` (110 pages)


## Slide 1

# **BlackHat Asia 2024 / rocky@gnu.org**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 2

# **`uncompyle6` and** **`decompyle3` : How to Read and Write a High-Level Bytecode Decompiler**

**BlackHat Asia, 2024 Rocky Bernstein rocky@gnu.org Slide text: https://rocky.github.io/blackhat-asia-2024additional/all-notes-print**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 3

# **Survey**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 4

# **Survey**

# ? How many people have used , , or

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 5

# **Survey**

? How many people have used , , or How many people have used the above to decompile _Python_ bytecode?

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 6

# **Survey**

? How many people have used , , or How many people have used the above to decompile _Python_ bytecode? How many people have used `uncompyle6` , or `decompyle3` ?

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 7

# **Github commit statistics for** **`uncompyle6`**

I am the current maintainer and developer of `uncompyle6` , and `decompyle3` .

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 8

# **So, who** **_am_ I?**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 9

# **So, who** **_am_ I?**

https://xkcd.com/2347/

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 10

# **Some Open Source So�ware that Includes My Code:**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 11

# **Background**

Malware is on the rise

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 12

# **Background**

Malware is on the rise Decompilers are not new, but ....

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 13

# **Background**

Malware is on the rise Decompilers are not new, but .... Ideas presented here are new.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 14

# **Background**

Malware is on the rise Decompilers are not new, but .... Ideas presented here are new. "General-purpose" Decompilers

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 15

# **Background**

Malware is on the rise Decompilers are not new, but .... Ideas presented here are new. "General-purpose" Decompilers Bytecode Decompilers (Special Purpose)

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 16

### Theory and books on _making_ compilers:

... _(40 others)_

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 17

**Books on making** **_de_ compilers:**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 18

# **Books on making** **_de_ compilers:**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 19

# **Can AI Save the Day?**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 20

# **Can AI Save the Day?**

Not yet.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 21

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 22

# **Decompilation in the World of High-Level Bytecode**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 23

**Decompilation in the World of High-Level Bytecode** Raise awareness of the differences between "General Purpose" decompiling and High-level Bytecode Decompiling

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 24

**Decompilation in the World of High-Level Bytecode** Raise awareness of the differences between "General Purpose" decompiling and High-level Bytecode Decompiling Introduce Decompilation as a Language-Translation problem.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 25

**Decompilation in the World of High-Level Bytecode** Raise awareness of the differences between "General Purpose" decompiling and High-level Bytecode Decompiling Introduce Decompilation as a Language-Translation problem. Introduce Decompilation as a Compilation Process.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 26

# **Key Takeaways**

Understand more about what is wrong when something goes wrong with decompilation. Understand the difference between _disassembly_ and _decompilation_ . Begin to see the difference between _machine code_ and _high-level bytecode._ Understand the some limits of Python decompilation and decompilation in general.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 27

**Simple Python Program** In file `five.py` :

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 28

# **Simple Python Program**

In file `five.py` :

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

Now run the code:

```
$ python five.py
  5
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 29

# **Simple Python Program**

In file `five.py` :

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

Now run the code:

```
$ python five.py
  5
```

Instruction bytecode of main program:

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 30

# **Byte-Compiling Python**

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 31

# **Byte-Compiling Python**

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

##### Byte compile this program:

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 32

# **Byte-Compiling Python**

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

##### Byte compile this program:

```
1$ python -m compileall five.py
2Compiling 'five.py'...
3$ ls -l __pycache__/five.cpython-38.pyc
4-rw-rw-r-- 1 rocky rocky 301 Feb 17 10:16 __pycache__/five.cpython-38.pyc
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 33

# **Byte-Compiling Python**

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

##### Byte compile this program:

```
1$ python -m compileall five.py
2Compiling 'five.py'...
3$ ls -l __pycache__/five.cpython-38.pyc
4-rw-rw-r-- 1 rocky rocky 301 Feb 17 10:16 __pycache__/five.cpython-38.pyc
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 34

# **Byte-Compiling Python**

```
"""
BlackHat Asia Example
"""
deffive():
"""Returns the string five"""
return"5"
# Call the function we just defined.
print(five())
```

##### Byte compile this program:

```
1$ python -m compileall five.py
```

```
2Compiling 'five.py'...
```

```
3$ ls -l __pycache__/five.cpython-38.pyc
```

```
4-rw-rw-r-- 1 rocky rocky 301 Feb 17 10:16 __pycache__/five.cpython-38.pyc
```

##### I run the bytecode:

```
$ python /tmp/five-moved.pyc
5
```

##### and again I get 5.

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 35

# **Python Bytecode Decompilation Example**

1 $ uncompyle6 /tmp/five-moved.pyc
2 # uncompyle6 version 3.9.1
3 # Python bytecode version base 3.8.0 (3413)
4 # Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0]
5 # Embedded file name: five.py
6 # Compiled at: 2024-02-17 10:16:08
7 # Size of source mod 2**32: 153 bytes
8 """
9 BlackHat Asia Example
10 """
11
12 def five ():
13 """Returns the string five"""
14 return "5"
15
16
17 print(five())
18 # okay decompiling /tmp/five-moved.pyc

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 36

# **Python Bytecode Decompilation Example**

|**`$ uncompyle6 /tmp/five-moved.pyc`**
**`1`**|
|---|
|**`# uncompyle6 version 3.9.1`**
**`2`**|
|**`# Python bytecode version base 3.8.0 (3413)`**
**`3`**|
|**`# Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0]`**
**`4`**|
|**`# Embedded file name: five.py`**
**`5`**|
|**`# Compiled at: 2024-02-17 10:16:08`**
**`6`**|
|**`# Size of source mod 2**32: 153 bytes`**
**`7`**
**`"""`**
**`8`**
**`BlackHat Asia Example`**
**`9`**
**`"""`**
**`10`**
**`11`**
**`def five():`**
**`12`**|
|**`"""Returns the string five"""`**
**`13`**|
|**`return "5"`**
**`14`**|
|**`15`**
**`16`**
**`print(five())`**
**`17`**
**`# okay decompiling /tmp/five-moved.pyc`**
**`18`**|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 37

# **Python Bytecode Decompilation Example**

- **`1 $ uncompyle6 /tmp/five-moved.pyc 2 # uncompyle6 version 3.9.1 3 # Python bytecode version base 3.8.0 (3413) 4 # Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0] 5 # Embedded file name: five.py 6 # Compiled at: 2024-02-17 10:16:08 7 # Size of source mod 2**32: 153 bytes 8 """ 9 BlackHat Asia Example`**

- **`10 """ 11 12 def five (): 13 """Returns the string five""" 14 return "5" 15 16 17 print(five()) 18 # okay decompiling /tmp/five-moved.pyc`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 38

# **Python Bytecode Decompilation Example**

- **`1 $ uncompyle6 /tmp/five-moved.pyc 2 # uncompyle6 version 3.9.1 3 # Python bytecode version base 3.8.0 (3413) 4 # Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0] 5 # Embedded file name: five.py 6 # Compiled at: 2024-02-17 10:16:08 7 # Size of source mod 2**32: 153 bytes 8 """ 9 BlackHat Asia Example`**

- **`10 """ 11 12 def five (): 13 """Returns the string five""" 14 return "5" 15 16 17 print(five()) 18 # okay decompiling /tmp/five-moved.pyc`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 39

# **Python Bytecode Decompilation Example**

- **`1 $ uncompyle6 /tmp/five-moved.pyc 2 # uncompyle6 version 3.9.1 3 # Python bytecode version base 3.8.0 (3413) 4 # Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0] 5 # Embedded file name: five.py 6 # Compiled at: 2024-02-17 10:16:08 7 # Size of source mod 2**32: 153 bytes 8 """ 9 BlackHat Asia Example`**

- **`10 """ 11 12 def five (): 13 """Returns the string five""" 14 return "5" 15 16 17 print(five()) 18 # okay decompiling /tmp/five-moved.pyc`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 40

# **Python Bytecode Decompilation Example**

- **`1 $ uncompyle6 /tmp/five-moved.pyc 2 # uncompyle6 version 3.9.1 3 # Python bytecode version base 3.8.0 (3413) 4 # Decompiled from: Python 3.12.2 (main, Feb 14 2024, 04:48:40) [GCC 13.2.0] 5 # Embedded file name: five.py 6 # Compiled at: 2024-02-17 10:16:08 7 # Size of source mod 2**32: 153 bytes 8 """ 9 BlackHat Asia Example`**

- **`10 """ 11 12 def five (): 13 """Returns the string five""" 14 return "5" 15 16 17 print(five()) 18 # okay decompiling /tmp/five-moved.pyc`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 41

# **Source Code Differences**

**Source code:**

- `1`

   - `"""`

- `2 BlackHat Asia Example 3 """`

- `4`

- `5`

- `6` **`def five`** `(): 7 """Returns the string five"""`

- `8` **`return`** `"5"`

- `9`

- `10`

- `11 # Call the function we just defined.`

- `12 print(five())`

### **Decompiled code:**

- `1 # uncompyle6 version 3.9.1`

- `2 # Python bytecode version base 3.8.0 (3413)`

- `3 # Decompiled from: Python 3.12.2 (main, Feb 14 2024,`

- `4 # Embedded file name: five.py`

- `5 # Compiled at: 2024-02-17 10:16:08`

   - `# Size of source mod 2**32: 153 bytes`

- `6`

- `7 """`

- `8 BlackHat Asia Example 9 """`

- `10`

- `11` **`def five`** `(): 12 """Returns the string five""" 13` **`return`** `"5" 14 15 16 print(five()) 17`

- `18 # okay decompiling /tmp/five-moved.pyc`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 42

# **Source Code Differences**

**Source code:**

- **`1`**

   - **`"""`**

- **`2 BlackHat Asia Example 3 """`**

- **`4`**

- **`5`**

- **`6 def five (): 7 """Returns the string five""" 8 return "5"`**

- **`9`**

- **`10`**

- **`11 # Call the function we just defined.`**

- **`12 print(five())`**

### **Decompiled code:**

- `1 # uncompyle6 version 3.9.1`

- `2 # Python bytecode version base 3.8.0 (3413)`

- `3 # Decompiled from: Python 3.12.2 (main, Feb 14 2024,`

   - `# Embedded file name: five.py`

- `4`

- `5 # Compiled at: 2024-02-17 10:16:08`

- `6 # Size of source mod 2**32: 153 bytes 7 """`

- `8 BlackHat Asia Example 9 """`

- `10 11` **`def five`** `(): 12 """Returns the string five""" 13` **`return`** `"5" 14 15 16 print(five()) 17`

- `18 # okay decompiling /tmp/five-moved.pyc`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 43

# **Source Code Differences**

### **Decompiled code:**

**Source code:**

   - **`1 # uncompyle6 version 3.9.1`**

   - **`2 # Python bytecode version base 3.8.0 (3413)`**

   - **`3 # Decompiled from: Python 3.12.2 (main, Feb 14`** `2024,` **`4 # Embedded file name: five.py`**

   - **`5 # Compiled at: 2024-02-17 10:16:08`**

   - **`6 # Size of source mod 2**32: 153 bytes 7 """`**

- **`1`**

   - **`"""`**

- **`2 BlackHat Asia Example 8 BlackHat Asia Example 3 """ 9 """ 4 10 5 11 def five (): 6 def five (): 12 """Returns the string five""" 7 """Returns the string five""" 13 return "5" 8 return "5" 14 9 15 16 print(five())`**

- **`10 11 # Call the function we just defined. 12 print(five())`**

- **`17`**

- **`18 # okay decompiling /tmp/five-moved.pyc`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 44

# **How These Decompilers Work**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 45

**How These Decompilers Work** Decompilation processed in a pipeline of these phases:

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 46

**How These Decompilers Work** Decompilation processed in a pipeline of these phases: 1. Get bytecode disassembly via xdis

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 47

**How These Decompilers Work** Decompilation processed in a pipeline of these phases: 1. Get bytecode disassembly via xdis 2. Tokenize or "li�" the disassembly

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 48

**How These Decompilers Work** Decompilation processed in a pipeline of these phases: 1. Get bytecode disassembly via xdis 2. Tokenize or "li�" the disassembly 3. Parse tokens into a Parse Tree

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 49

**How These Decompilers Work** Decompilation processed in a pipeline of these phases: 1. Get bytecode disassembly via xdis 2. Tokenize or "li�" the disassembly

3. Parse tokens into a Parse Tree

4. Abstract the Parse Tree into an Abstract Syntax Tree

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 50

**How These Decompilers Work** Decompilation processed in a pipeline of these phases: 1. Get bytecode disassembly via xdis 2. Tokenize or "li�" the disassembly

3. Parse tokens into a Parse Tree

4. Abstract the Parse Tree into an Abstract Syntax Tree 5. Produce Source from the Abstract Syntax Tree

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 51

# **xdis Disassembly using** **`pydisasm` from**

```
$pydisasm/tmp/five_moved.pyc
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 52

# **xdis Disassembly using** **`pydisasm` from**

#### `$` **`pydisasm`** `/tmp/five_moved.pyc`

|`#`
`1`|`pydisasm version`|`6.1.0`|
|---|---|---|
|`#`
`2`|`Python bytecode 3`|`.8.0 (3413)`|
|`#`
`3`|`Disassembled from`|`Python 3.8.18 (default, Sep  4 2023, 13:19:52)`|
|`#`
`4`|`[GCC 12.3.0]`||
|`#`
`5`|`Timestamp in code`|`: 1708217267 (2024-02-17 19:47:47)`|
|`#`
`6`|`Source code size`|`mod 2**32: 148 bytes`|
|`#`
`7`|`Method Name:`|`<module>`|
|`#`
`8`|`Filename:`|`five.py`|
|`#`
`9`|`Argument count:`|`0`|
|`#`
`10`|`Position-only arg`|`ument count: 0`|
|`#`
`11`|`Keyword-only argu`|`ments: 0`|
|`#`
`12`|`Number of locals:`|`0`|
|`#`
`13`|`Stack size:`|`2`|
|`#`
`# `
`14`
`15`|`Flags:`
 `First Line:`|`0x00000040 (NOFREE)`
`1`|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 53

# **xdis Disassembly using** **`pydisasm` from**

#### `$` **`pydisasm`** `/tmp/five_moved.pyc`

|**`#`**
**`#`**
**`1`**
**`2`**|**`pydisas`**
**`Python`**|**`m version 6.1.0`**
**`bytecode 3.8.0 (3413)`**|
|---|---|---|
|**`#`**
**`3`**|**`Disasse`**|**`mbled from Python 3.8.18 (default, Sep  4 2023, 13:19:52)`**|
|**`#`**
**`4`**|**`[GCC 12`**|**`.3.0]`**|
|**`#`**
**`5`**|**`Timesta`**|**`mp in code: 1708217267 (2024-02-17 19:47:47)`**|
|**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`#`**
**`6`**
**`7`**
**`8`**
**`9`**
**`10`**
**`11`**
**`12`**
**`13`**
**`14`**
**`15`**|**`Source`**
**`Method`**
**`Filenam`**
**`Argumen`**
**`Positio`**
**`Keyword`**
**`Number`**
**`Stack s`**
**`Flags:`**
 **`First`** **`L`**|**`code size mod 2**32: 148 bytes`**
**`Name:       <module>`**
**`e:          five.py`**
**`t count:    0`**
**`n-only argument count: 0`**
**`-only arguments: 0`**
**`of locals:  0`**
**`ize:        2`**
**`0x00000040 (NOFREE)`**
**`ine:`**
**`1`**|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 54

# **xdis Disassembly using** **`pydisasm` from**

#### `$` **`pydisasm`** `/tmp/five_moved.pyc`

|**`# pydisas`**
**`# Python`**
**`# Disasse`**
**`# [GCC 12`**
**`1`**
**`2`**
**`3`**
**`4`**
`#    2: '`
`19`
`#    3: N`
`20`
`# Names:`
`21`
`#    0: _`
`22`|**`m version 6.1.0`**
**`bytecode 3.8.0 (3413)`**
**`mbled from Python 3.8.18 (default, Sep  4 2023, 13:19:52)`**
**`.3.0]`**
`five'`
`one`
`_doc__`|
|---|---|
|**`# Timesta`**
**`# Source`**
**`# Method`**
**`5`**
**`6`**
**`7`**
`1:`
`#    1: f`
`23`
`#    2: p`
`24`
`25`|**`mp in code: 1708217267 (2024-02-17 19:47:47)`**
**`code size mod 2**32: 148 bytes`**
**`Name:       <module>`**
 `0`**`LOAD_CONST`** `("\nBlackHat Asia Example\n")`
`ive`
`rint`|
|**`# Filenam`**
**`# Argumen`**
**`# Positio`**
**`# Keyword`**
**`# Number`**
**`# Stack s`**
**`# Flags:`**
**`#`** **`First`** **`L`**
**`8`**
**`9`**
**`10`**
**`11`**
**`12`**
**`13`**
**`14`**
**`15`**

`26`
`27`
`6:`
`28`

`29`

`30`

`31`
`32`
`12:`
`33`|**`e:          five.py`**
**`t count:    0`**
**`n-only argument count: 0`**
**`-only arguments: 0`**
**`of locals:  0`**
**`ize:        2`**
**`0x00000040 (NOFREE)`**
**`ine:`**
**`1`**
 `2`**`STORE_NAME`** `(__doc__)`
 `4`**`LOAD_CONST`** `(<code object five at 0x7f3f4c3d17c0, file "five.py",`
 `6`**`LOAD_CONST`** `("five")`
 `8`**`MAKE_FUNCTION`** `(Neither defaults, keyword-only args, annotations, nor`
 `10`**`STORE_NAME`** `(five)`
 `12`**`LOAD_NAME`** `(print)`|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 55

# **Phases 1 and 2: Bytecode to Tokens**

Bytecode Disassembly:

## Parser Input Tokens:

- `1 1: 0` **`LOAD_CONST`** `('\nBlackHat Asia Example\n') 1 1: 0` **`LOAD_STR`** `('\nBlackHat Asia Example\n') 2 2` **`STORE_NAME`** `(__doc__) 2 2` **`STORE_NAME`** `(__doc__) 3 3 4 6: 4` **`LOAD_CONST`** `<code object five> 4 6: 4` **`LOAD_CODE`** `<code_object five> 5 6` **`LOAD_CONST`** `('five') 5 6` **`LOAD_STR`** `('five') 6 8` **`MAKE_FUNCTION`** `(No parameters) 6 8` **`MAKE_FUNCTION_0`** `(No parameters) 7 10` **`STORE_NAME`** `(five) 7 10` **`STORE_NAME`** `(five)`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 56

# **Phases 1 and 2: Bytecode to Tokens**

## Bytecode Disassembly:

## Parser Input Tokens:

- **`1 1: 0 LOAD_CONST ('\nBlackHat Asia Example\n')`** `1 1: 0` **`LOAD_STR`** `('\nBlackHat Asia Example\n')` **`2 2 STORE_NAME (__doc__)`** `2 2` **`STORE_NAME`** `(__doc__)` **`3`** `3` **`4 6: 4 LOAD_CONST <code object five>`** `4 6: 4` **`LOAD_CODE`** `<code_object five>` **`5 6 LOAD_CONST ('five')`** `5 6` **`LOAD_STR`** `('five')` **`6 8 MAKE_FUNCTION (No parameters)`** `6 8` **`MAKE_FUNCTION_0`** `(No parameters)` **`7 10 STORE_NAME (five)`** `7 10` **`STORE_NAME`** `(five)`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 57

# **Phases 1 and 2: Bytecode to Tokens**

## Bytecode Disassembly:

## Parser Input Tokens:

- **`1 1: 0 LOAD_CONST ('\nBlackHat Asia Example\n') 1 1: 0 LOAD_STR ('\nBlackHat Asia Example\n') 2 2 STORE_NAME (__doc__) 2 2 STORE_NAME (__doc__) 3 3 4 6: 4 LOAD_CONST <code object five> 4 6: 4 LOAD_CODE <code_object five> 5 6 LOAD_CONST ('five') 5 6 LOAD_STR ('five') 6 8 MAKE_FUNCTION (No parameters) 6 8 MAKE_FUNCTION_0 (No parameters) 7 10 STORE_NAME (five) 7 10 STORE_NAME (five)`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 58

# **Phase 3: Parsing Tokens into a Parse Tree**

```
"""
BlackHat Asia Example
"""
```

Constructing Parse Tree from Tokens:

```
LOAD_STR'\nBlackHat Asia Example\n'
STORE_NAME __doc__
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 59

# **Phase 3: Parsing Tokens into a Parse Tree**

```
"""
BlackHat Asia Example
"""
```

Constructing Parse Tree from Tokens:

```
LOAD_STR'\nBlackHat Asia Example\n'
STORE_NAME __doc__
```

Is parsed:

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 60

# **Phase 3: Parsing Tokens into a Parse Tree**

```
"""
BlackHat Asia Example
"""
```

Constructing Parse Tree from Tokens:

```
LOAD_STR'\nBlackHat Asia Example\n'
STORE_NAME __doc__
LOAD_STR
```

Is parsed:

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 61

# **Phase 3: Parsing Tokens into a Parse Tree**

```
"""
BlackHat Asia Example
"""
```

Constructing Parse Tree from Tokens:

**`LOAD_STR`** `'\nBlackHat Asia Example\n'` **`STORE_NAME`** `__doc__` Is parsed: **`LOAD_STR expr`** `::=` **`LOAD_STR`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 62

# **Phase 3: Parsing Tokens into a Parse Tree**

```
"""
BlackHat Asia Example
"""
```

Constructing Parse Tree from Tokens:

**`LOAD_STR`** `'\nBlackHat Asia Example\n'` **`STORE_NAME`** `__doc__` Is parsed:

```
LOAD_STR
 expr  ::= LOAD_STR
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 63

# **Parsing Tokens into a Parse Tree (Part 2)**

Constructing Parse Tree from Tokens:

```
LOAD_STR
 expr  ::= LOAD_STR
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 64

# **Parsing Tokens into a Parse Tree (Part 2)**

Constructing Parse Tree from Tokens:

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 65

# **Parsing Tokens into a Parse Tree (Part 2)**

Constructing Parse Tree from Tokens:

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 66

# **Parsing Tokens into a Parse Tree (Part 2)**

Constructing Parse Tree from Tokens:

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 67

# **Parsing Tokens into a Parse Tree (Part 3)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 68

# **Parsing Tokens into a Parse Tree (Part 3)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
 assign  ::= exprstore
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 69

# **Parsing Tokens into a Parse Tree (Part 3)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
 assign  ::= exprstore
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 70

# **Parsing Tokens into a Parse Tree (Part 4)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
 assign  ::= exprstore
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 71

# **Parsing Tokens into a Parse Tree (Part 4)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
 assign  ::= exprstore
 stmts   ::= assign
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 72

# **Parsing Tokens into a Parse Tree (Part 4)**

```
LOAD_STR
 expr  ::= LOAD_STR
STORE_NAME
 store   ::= STORE_NAME
 assign  ::= exprstore
 stmts   ::= assign
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 73

# **Phases 3 - 5: Final Parse Tree to Source Text** Phase 3. Parse Tree in ASCII Format (First Line):

```
stmts
   0. assign
       0. expr
           L.  1   0  LOAD_STR'\nBlackHat Asia Example\n'
       1. store
                   2  STORE_NAME__doc__
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 74

**Phases 3 - 5: Final Parse Tree to Source Text** Phase 3. Parse Tree in ASCII Format (First Line):

```
stmts
   0. assign
       0. expr
           L.  1   0  LOAD_STR'\nBlackHat Asia Example\n'
       1. store
                   2  STORE_NAME__doc__
```

### Phase 4. Abstract Syntax Tree (First Line)

```
stmts
  0. docstring
        0  LOAD_STR'\nBlackHat Asia Example\n'
        2  STORE_NAME__doc__
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 75

**Phases 3 - 5: Final Parse Tree to Source Text** Phase 3. Parse Tree in ASCII Format (First Line):

```
stmts
   0. assign
       0. expr
           L.  1   0  LOAD_STR'\nBlackHat Asia Example\n'
       1. store
                   2  STORE_NAME__doc__
```

Phase 4. Abstract Syntax Tree (First Line)

```
stmts
  0. docstring
        0  LOAD_STR'\nBlackHat Asia Example\n'
        2  STORE_NAME__doc__
```

Phase 5. Printing the Abstract Syntax Tree (First line)

```
"""
BlackHat Asia Example
"""
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 76

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
: awn. ,
—
< INTERMISSION?
. = .- a
ww Yr whe
Se
BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler
```

## Slide 77

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 78

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
```

Disassembly using `pydisasm` from **`xdis`** :

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 79

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
```

Disassembly using `pydisasm` from **`xdis`** :

```
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 80

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11       # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15       # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 81

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11# """\nBlackHat Asia Example\n"""
121:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
132 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15# def five():
166:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
176 |64 02| LOAD_CONST("five")
188 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
1910 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 82

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11 # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15 # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 83

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
1# ...
2# Constants:
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
5#    2: 'five'
6#    3: None
6#    3: None
7# Names:
7# Names:
8#    0: __doc__
8#    0: __doc__
9#    1: five
9#    1: five
10#    2: print
10#    2: print
11       # """\nBlackHat Asia Example\n"""
11 # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
14
15       # def five():
15 # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
20
21#print(five())
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 84

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11   # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15   # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 85

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11    # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15    # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 86

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
1# ...
2# Constants:
3#    0: '\nBlackHat Asia Example\n'
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
5#    2: 'five'
6#    3: None
7# Names:
8#    0: __doc__
9#    1: five
10#    2: print
11     # """\nBlackHat Asia Example\n"""
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
14
15     # def five():
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
17 6 |64 02| LOAD_CONST("five")
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
20
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 87

# **Bytecode Disassembly**

```
0 |64 00 5a 00 64 01 64 02 |
8 |84 00 5a 01 65 02 65 00 |
12 |65 02 65 01 83 01 01 00 |
16 |83 00 83 01 01 00 64 03 |
24 |53 00                   |
$pydisasm-F extended-bytes -S__pycache__/five.cpython-38.pyc
```

```
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
1# ...
14
2# Constants:
15       # def five():
3#    0: '\nBlackHat Asia Example\n'
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
4#    1: <code object five at 0x7f64cb56c030, file "five.py", line 6>
17 6 |64 02| LOAD_CONST("five")
5#    2: 'five'
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
6#    3: None
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
7# Names:
20
8#    0: __doc__
21       # print(five())
9#    1: five
2212:     12 |65 02| LOAD_NAME(print)
10#    2: print
23 14 |65 01| LOAD_NAME(five)
11     # """\nBlackHat Asia Example\n"""
24 16 |83 00| CALL_FUNCTION(0 positional arguments) ; TOS = five()
12 1:      0 |64 00| LOAD_CONST("\nBlackHat Asia Example\n")
25 18 |83 01| CALL_FUNCTION(1 positional argument) ; TOS = print(five())
13 2 |5a 00| STORE_NAME(__doc__) ; __doc__ = '\nBlackHat Asia Example\n'
26 20 |01 00| POP_TOP
14
27 22 |64 03| LOAD_CONST(None)
15     # def five():
28 24 |53 00| RETURN_VALUE      return None
16 6:      4 |64 01| LOAD_CONST(<code object five at 0x7f64cb56c030, file "five.py>)
29
17 6 |64 02| LOAD_CONST("five")
30
18 8 |84 00| MAKE_FUNCTION(No arguments) ; TOS = deffive(...): ...
31# Method Name:       five
19 10 |5a 01| STORE_NAME(five) ; five = deffive(...): ...
32# Filename:          five.py
20
33#Argumentcount:0
21i(fi())
```

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 88

# **Chained Compare Bytecode**

Python Expression: `"a"` **`<= __file__ <=`** `"b"`

|`1: 0`
`1`|`|64 00|`|**`LOAD_CONST`** `("a")`|
|---|---|---|
|`2`
`2`|`|65 00|`|**`LOAD_NAME`** `(__file__)`|
|`4`
`3`|`|04 00|`|**`DUP_TOP`**|
|`6`
`4`|`|03 00|`|**`ROT_THREE`**|
|`8`
`5`|`|6b 01|`|**`COMPARE_OP`** `(<=)`|
|`10`
`6`|`|6f 12|`|**`JUMP_IF_FALSE_OR_POP`** `(to 18)`|
|`12`
`7`|`|64 01|`|**`LOAD_CONST`** `("b")`|
|`14`
`8`|`|6b 01|`|**`COMPARE_OP`** `(<=) ; TOS = (to 18) <="b"`|
|`16`
`9`|`|6e 04|`|**`JUMP_FORWARD`** `(to 22)`|
|`>> 18`
`10`|`|02 00|`|**`ROT_TWO`**|
|`20`
`11`|`|01 00|`|**`POP_TOP`**|
|`>> 22`
`12`|`|01 00|`|**`POP_TOP`**|
|`24`
`13`|`|64 02|`|**`LOAD_CONST`** `(None)`|
|`26`
`14`|`|53 00|`|**`RETURN_VALUE`**`return None`|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 89

# **Chained Compare Bytecode**

Python Expression: `"a"` **`<= __file__ <=`** `"b"`

|**`1: 0`**
  **`2`**
  **`4`**
  **`6`**
  **`8`**
  **`10`**
  **`12`**
  **`14`**
**`1`**
**`2`**
**`3`**
**`4`**
**`5`**
**`6`**
**`7`**
**`8`**|**`|64`**
 **`|65`**
 **`|04`**
 **`|03`**
 **`|6b`**
 **`|6f`**
 **`|64`**
 **`|6b`**|**`00|LOAD_`**
**`00|LOAD_`**
**`00|DUP_T`**
**`00|ROT_T`**
**`01|COMPA`**
**`12|JUMP_`**
**`01|LOAD_`**
**`01|COMPA`**|**`CONST("a")`**
**`NAME(__file__)`**
**`OP`**
**`HREE`**
**`RE_OP(<=)`**
**`IF_FALSE_OR_POP (to 18)`**
**`CONST("b")`**
**`RE_OP(<=) ; TOS = (to 18) <="b"`**|
|---|---|---|---|
|**`16`**
 **`>> 18`**
  **`20`**
 **`>> 22`**
  **`24`**
  **`26`**
**`9`**
**`10`**
**`11`**
**`12`**
**`13`**
**`14`**|**`|6e`**
 **`|02`**
 **`|01`**
 **`|01`**
 **`|64`**
 **`|53`**|**`04|JUMP_`**
**`00|ROT_T`**
**`00|POP_T`**
**`00|POP_T`**
**`02|LOAD_`**
**`00|RETUR`**|**`FORWARD(to 22)`**
**`WO`**
**`OP`**
**`OP`**
**`CONST(None)`**
**`N_VALUE         return None`**|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 90

# **Chained Compare Parse Tree (new code)**

Python Expression: `"a"` **`<= __file__ <=`** `"b"`

|`1`|`BB_START`|`1'Basic`|`Block 1'`||
|---|---|---|---|---|
|`2`|**`compare`**`_`**`c`**|**`hained`**|||
|`3`
`4`
`5`
`6`
`7`|`0.`**`expr`**
`...`
`1.`**`comp`**
`...`
`4.`|
**`are`**`_`**`chain`**

 **`jifop`**|**`ed`**`_`**`middle`**||
|`8`||`0. 10`|**`JUMP_IF_FALSE_`**|**`OR_POP`** `18 'to 18'`|
|`9`|**`nnn`**|`1.  `|`10 BB_END`|`1'Basic Block 1'`|
|`10`|`5.`|`12`|`BB_START`|`2'Basic Block 2'`|
|`11`
`12`|`6.`
|**`compare`**`_`**`c`**
`...`|**`hained`**`_`**`right`**||
|`13`||`2. 16`|**`JUMP_FORWARD`**|`22 'to 22'`|
|`14`||`3. 16`|`BB_END`|`2'Basic Block 2'`|
|`15`|`2.`|`18`|`BB_START`|`3'Basic Block 3'`|
|`16`|`3.`|`18`|`SIBLING_BLOCK`||
|`17`|`4.`|`18`|**`ROT_TWO`**||
|`18`|`5.`|`20`|**`POP_TOP`**||
|`19`|`6.`|`20`|`BB_END`|`3'Basic Block 3'`|
|`20`|`7.`|`20`|`BLOCK_END_JOIN`|`3'Basic Block DominatorSet<{3}>'`|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 91

# **Chained Compare Parse Tree (new code)**

Python Expression: `"a"` **`<= __file__ <=`** `"b"`

|**`1`**
**`2`**
**`3`**
**`4`**
**`5`**
**`6`**
**`7`**
**`8`**
**`9`**|**`BB_ST`**
**`compa`**
 **`0.`**

 **`1.`**

**`nnn`**|**`ART`**
**`re_c`**
 **`expr`**
 **`...`**
 **`comp`**
 **`...`**
 **`4.`**

|**`1'Basic`**
**`hained`**

**`are_chain`**

 **`jifop`**
 **`0. 10`**
**`1.  `**|**`Block 1'`**
**`ed_middle`**
  **`JUMP_IF_FALSE_O`**
**`10 BB_END`**|**`R_POP 18 'to 18'`**
**`1'Basic Block 1'`**|
|---|---|---|---|---|---|
|**`10`**
**`11`**
**`12`**|

|**`5.`**
 **`6.`**
|**`12`**
 **`compare_c`**
 **`...`**|**`BB_START`**
**`hained_right`**|**`2'Basic Block 2'`**|
|**`13`**
**`14`**|
|
|**`2. 16`**
 **`3. 16`**|**`JUMP_FORWARD  2`**
 **`BB_END`**|**`2 'to 22'`**
**`2'Basic Block 2'`**|
|**`15`**|**`2.`**||**`18`**|**`BB_START`**|**`3'Basic Block 3'`**|
|**`16`**
**`17`**|**`3.`**
 **`4.`**|
|**`18`**
 **`18`**|**`SIBLING_BLOCK`**
  **`ROT_TWO`**||
|**`18`**
**`19`**|**`5.`**
 **`6.`**|
|**`20`**
 **`20`**|**`POP_TOP`**
 **`BB_END`**|**`3'Basic Block 3'`**|
|**`20`**|**`7.`**||**`20`**|**`BLOCK_END_JOIN`**|**`3'Basic Block DominatorSet<{3}>'`**|

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 92

# **Classifying Scopes and Important Control-Flow Points**

- `1 i: int=6 2 zero_bits = 0 3 one_bits = 0 4 # loop dominator 5` **`while`** `i > 0:`

- `6 # if dominator 7` **`if`** `i % 0: 8 # first sibling 9 one_bits += 1`

- `10` **`else`** `: 11 # second sibling 12 zero_bits += 1 13 # join point 14 i << 1 15 # loop-end join point 16 print(one_bits, zero_bits)`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 93

# **Classifying Scopes and Important Control-Flow Points**

- **`1 i: int=6 2 zero_bits = 0 3 one_bits = 0`**

- **`4 # loop dominator`**

- **`5 while i > 0:`**

- **`6 # if dominator 7 if i % 0:`**

- **`8 # first sibling 9 one_bits += 1`**

- **`10 else :`**

- **`11 # second sibling 12 zero_bits += 1`**

- **`13 # join point 14 i << 1 15 # loop-end join point`**

- **`16 print(one_bits, zero_bits)`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 94

# **Classifying Scopes and Important Control-Flow Points**

- **`1 i: int=6`**

- **`2 zero_bits = 0 3 one_bits = 0`**

- **`4 # loop dominator 5 while i > 0:`**

- **`6 # if dominator 7 if i % 0:`**

- **`8 # first sibling 9 one_bits += 1`**

- **`10 else :`**

- **`11 # second sibling`**

- **`12 zero_bits += 1`**

- **`13 # join point`**

- **`14 i << 1`**

- **`15 # loop-end join point`**

- **`16 print(one_bits, zero_bits)`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 95

# **Classifying Scopes and Important Control-Flow Points**

- **`1 i: int=6 2 zero_bits = 0 3 one_bits = 0`**

- **`4 # loop dominator 5 while i > 0:`**

- **`6 # if dominator 7 if i % 0:`**

- **`8 # first sibling 9 one_bits += 1`**

- **`10 else :`**

- **`11 # second sibling 12 zero_bits += 1`**

- **`13 # join point`**

- **`14 i << 1`**

- **`15 # loop-end join point`**

- **`16 print(one_bits, zero_bits)`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 96

# **Classifying Scopes and Important Control-Flow Points**

- `1 i: int=6 2 zero_bits = 0 3 one_bits = 0 4 # loop dominator 5` **`while`** `i > 0: 6 # if dominator 7` **`if`** `i % 0: 8 # first sibling 9 one_bits += 1`

- `10` **`else`** `: 11 # second sibling 12 zero_bits += 1 13 # join 14 i << 1 15 # loop-end join 16 print(one_bits, zero_bits)`

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 97

# **Control Flow Produced from** **`control_flow`**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 98

# **Dominator Regions and Dominators**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 99

# **General Remarks**

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 100

# **General Remarks** Other Python decompilers

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 101

**General Remarks** Other Python decompilers General-Purpose Decompilers

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 102

# **General Remarks**

Other Python decompilers General-Purpose Decompilers How Control Flow Differs

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 103

# **General Remarks**

Other Python decompilers General-Purpose Decompilers How Control Flow Differs Choice of Intermediate Language

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 104

# **Wrapping Up**

1. Understand, pinpoint, report, and even _fix_ problems. 2. Understand how Python text code is related to its bytecode.

3. Extend this code for newer Python Bytecode.

4. Use these techniques in other High-level Bytecode Languages:

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 105

# **Thanks**

# John Aycott and Hartmut Goebel

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 106

# **Thanks**

John Aycott and Hartmut Goebel BlackHat 2024 Asia Reviewers and Organizers

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 107

# **Thanks**

John Aycott and Hartmut Goebel BlackHat 2024 Asia Reviewers and Organizers Phil Young and Speaker-Coaching Program

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 108

# **Thanks**

John Aycott and Hartmut Goebel BlackHat 2024 Asia Reviewers and Organizers Phil Young and Speaker-Coaching Program Stuart Frankel

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 109

# **Thanks**

John Aycott and Hartmut Goebel BlackHat 2024 Asia Reviewers and Organizers Phil Young and Speaker-Coaching Program Stuart Frankel You

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler

## Slide 110

# **Additional Information**

Python Decompilers: https://pypi.org/project/uncompyle6, and https://pypi.org/project/decompyle3/ Cross-Version Python Disassembler: https://pypi.org/project/xdis Python Control Flow: https://github.com/rocky/python-control-flow Older Decompiler Paper: https://rocky.github.io/Deparsing-Paper.pdf PyCon Columbia 2018 talk slides: https://rocky.github.io/pycon2018light.co

PyCon Columbia 2018 talk video: https://www.youtube.com/watch? v=bRQr1OroXUM&feature=youtu.be Additional Slides: https://rocky.github.io/blackhat-asia/2024-additional Slide Text: https://rocky.github.io/blackhat-asia-2024-additional/allnotes-print

BlackHat Asia 2024 / rocky@gnu.org - uncompyle6 and decompyle3: How to Read and Write a High-Level Bytecode Decompiler
