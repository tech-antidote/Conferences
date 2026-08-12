---
title: "Burning Tears of PHP's Memory Hardening"
speakers: ["Frank Wu", "xia0o0o0o", "Zhiyun Qian"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Frank Wu&xia0o0o0o&Zhiyun Qian_Burning Tears of PHP's Memory Hardening.pdf"
pages: 46
sha256: "aa1b28c241ef7f0206da8569b4f5f5e8ed7e4bd054f66f0b1f22bda6e8deb71d"
text_chars: 19276
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T23:09:42Z"
---
# Burning Tears of PHP's Memory Hardening

**Speakers:** Frank Wu, xia0o0o0o, Zhiyun Qian  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Frank Wu&xia0o0o0o&Zhiyun Qian_Burning Tears of PHP's Memory Hardening.pdf` (46 pages)

## Slide 1

### **B L A C K H A T U S A 2 0 2 6 · B R I E F I N G S Burning Tears of Burning Tears of PHP's Memory PHP's Memory Hardening Hardening**

A fully remote, generic exploit path that survives PHP's newest heap defenses, from one constrained byte.

**Yifan Wu** · Xiaochuan Yu · Zhiyun Qian  ·  UC Riverside · UC San Diego

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 1

## Slide 2

###### **This research is 100% LLM-free.**

(except for making these slides)

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 2

## Slide 3

###### **Two researchers, one lab.**

```
nebula@blackhat: ~/talks/burning-tears
```

```
nebula@blackhat:~$whoami
```

```
Frank Wu · Nebula Security
Hacking Linux and Android
```

```
Xiaochuan Yu · Nebula Security
Hacking XNU and Browsers
```

```
nebula@blackhat:~$cat recent_work.md
```

- `first public nginx RCE · remote, ASLR bypass, generic config`

- `world’s first Android 17 root (GhostLock) · one URL, full device control`

- `first public Android browser → kernel full-chain (IonStack) in 7 years`

```
nebula@blackhat:~$./burning_tears.sh--target=php --remote
```

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 3

## Slide 4

###### **It started with a CTF.**

###### **1 The CTF** An ordinary PHP challenge.

**2**

**3**

**The 0‑day** A real flaw. PHP patched it. **AN UNPLANNED SIDE‑FIND**

**The real question** One defense cracks, all four?

**Thank you Securinets CTF** 🥰🥰

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 4

## Slide 5

###### **One request. That's all you get.**

**Browser pwn Kernel pwn** `for(let i=0;i<0x4000;i++){ foo(true); for(int i=0;i<N;i++) } msgsnd(qid[i],&msg,size,0); new ArrayBuffer(0x7f00000);`

PHP remote

```
POST /upload.php HTTP/1.1
Host: victim.tld
Content-Length: 8192
data=%00%02%be%ef...
```

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 5

## Slide 6

###### **How you used to pwn PHP.**

```
ZendMM: singly-linked list
```

overflow

next next
in-use buffer free slot free slot …
0x… 30 0x…20
victim victim
chunk returned
object object
by allocator

**read / write victim fields › leak & overwrite a function pointer › RCE**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 6

## Slide 7

###### **Then PHP fought back.**

Shadow Pointer Unlink Prevention RO Metadata
checked on every alloc
chunk A
next zend_mm_heap
encrypted write
fd/bk
_malloc
chunk P
free slot = _free
fd/bk
_realloc
chunk B
shadow
encrypted P->fd->bk == P
read-only at runtime
P->bk->fd == P
✕ freelist poisoning ✕ list-forgery writes ✕ metadata hook hijack
CVE-2024-2961 CVE-2022-31626 public CTF chain

Heap Isolation
request zone
$_GET $_POST
application heap
objects, strings
✕ raw-request spray

Aimed at the exact techniques every public PHP exploit relied on.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 7

## Slide 8

###### **The old exploits died.**

`freelist next` **blocked by Shadow Pointer**

metadata hooks
blocked by Read-only

`$_POST spray` **blocked by Heap Isolation**

Each new defense closes exactly one classic technique freelist, metadata, and raw spray all gone.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 8

## Slide 9

#### **PART I The playing field**

How PHP allocates, and why that lets us shape the heap at all, remotely.

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 9

#BHUSA

## Slide 10

###### **Same request, same heap.**

```
request #1
```

request #1 freed pages freelist
0x…30 0x…80 0x…d0
request #2 freed pages freelist
0x…30 0x…80 0x…d0

Fresh chunk each request, best-fit + LIFO, no cross-request state, so identical requests build identical heaps.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 10

## Slide 11

###### **What fengshui buys us.**

**Anything** (raw bytes) Spray attacker-defined raw memory the interpreter will later trust.

**Anywhere** (placement) Put a chosen object at any offset next to the victim, in one request.

Both are hard under the new defenses. Earning them back is the rest of the talk.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 11

## Slide 12

###### **So we stopped touching the allocator.**

00 01 CONTRIBUTION 02 03
1 byte past the edge
fake zval ++ / −−
index array
leak
BIG fake value type *p
probe
buffer neighbour
hijack
1-byte OOB Index Forgery Arbitrary ++/−− ZOP
the weakest possible bug corrupt a table index, not a pointer read = *p++, write = *p−− the interpreter is the gadget set

###### Every step lives in built-in PHP objects, never the allocator, never app classes.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 12

## Slide 13

**II**

###### **Index Forgery**

Turning the weakest possible bug, one constrained byte, into a strong primitive.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 13

## Slide 14

One byte in.
strong primitive
arbitrary ++/--
write anywhere
fake zval
a controlled object
index forgery
one integer
1-byte OOB
the input
weakest bug

1-byte overflow value constrained no OOB read

The nightmare bug, yet enough. Works here means it works for almost anything stronger.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 14

## Slide 15

###### **Meet the zval.**

+0x00
value (8 bytes)
+0x08
u1.type_info

IS_LONG = 4
IS_DOUBLE = 5
IS_STRING = 6
IS_ARRAY = 7
IS_OBJECT = 8

flip the low type byte -> same 8 bytes reinterpreted

```
flags byte: IS_TYPE_REFCOUNTED = 1<<0
```

Every PHP value is 8 bytes plus a type tag. Control a zval, and you control what PHP believes memory is.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 15

## Slide 16

###### **The real target: arData.**

**Z E N D_ A R R AY ( H AS H TA B L E )** `+0x00` **gc** · refcount `+0x0c` **nTableMask** `+0x10` **arData** → butterfly

**A R DATA I S A B U T T E R F LY** A separate allocation the overflow reaches. arData points to the split: index array on the left half, buckets on the right.

**idx idx idx Bucket[0]Bucket[1]**

`+0x18` **nNumUsed** · size

← index grows  |  arData →   buckets grow →

`+0x38` **pDestructor** · hijack target

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 16

## Slide 17

A normal lookup.
$t[$key]
ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS
victim buf
0x00 0x01 0x02 0x03
overflow source
SPRAYED REGION
arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval
Bucket[0].value
raw string bytes

A zend_array reads from a separatearDatabuffer, index array in front of the buckets.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 17

## Slide 18

A normal lookup.
$t[$key]
ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS
victim buf
0x00 0x01 0x02 0x03
overflow source
SPRAYED REGION
arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval
Bucket[0].value
raw string bytes

hash(key) | mask → a slot → the integer there picks the Bucket. PHP never doubts that integer.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 18

## Slide 19

One byte, one redirect.
$t[$key]
ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS
victim buf
0x4D 0x01 0x02 0x03
overflow source
1-byte OOB SPRAYED REGION
arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval
Bucket[0].value
raw string bytes

The overflow lands onindex[0], not a pointer, just a small integer. One byte moves it far.

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 19

#BHUSA

## Slide 20

One byte, one redirect.
$t[$key]
ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS
victim buf sprayed, known offset
0x4D 0x01 0x02 0x03
overflow source
1-byte OOB fake Bucket
fake zval
arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval
Bucket[0].value
raw string bytes

A large index reaches memorywe sprayed, a fake Bucket holding a fake zval we control.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 20

## Slide 21

###### **Make the fake pass.**

HOW THE CHECK PASSES
forged Bucket (sprayed)
hash: DJBX33A is reversible
+0x00 zval.value you set
craft a string whose hash == the key we look up (Alg.1)
+0x08 zval.u1.type_info you set
key: reoccupy the residual key pointer
+0x10 h (hash) MUST match spray the same key bytes so the compare succeeds
+0x18 key MUST match
lookup passes ✓
$t[key] returns our fake zval

PHP re-checks the bucket key and hash. We forge a match with the reversible DJBX33A hash, and the lookup passes.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 21

## Slide 22

###### **Now you own a zval.**

read $t[$key] *target ++
fake zval
any address
value -> *target
write $t[$key]=$v *target --

Mark the fake zval refcounted, and a plain read/write does ++ / -- through your pointer, at any address.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 22

## Slide 23

###### **But the pointer is constrained.**

###### **W H Y L I M I T E D**

The value pointer is sprayed as a string, encoding-restricted. We control only its low bytes. So ++/-- lands near a chosen spot, not anywhere.

**value = 0x…?? low-byte overlap → nearby sprayed memory**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 23

## Slide 24

###### **Lift to arbitrary.**

###### **O N E E XT R A I N D I R E C T I O N**

Steer the constrained value at the type_flags of another zval in a sprayed array.

++/-- on a type tag → make any zval refcounted → decrement anywhere.

**fake zval.value ─┐ low-byte steer**

**└→ zval.type_flags limited ++/-- → arbitrary ++/--**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 24

## Slide 25

One corrupted index. Four primitives.
the one operation
$t[key] LARGE 2 0 5 Bucket[large] OOB the large index reaches out of bounds
a corrupted index, the 1-byte overflow set index[0] to LARGE
fake Bucket what Bucket[large] lands on
ANY address
+0x00 value low high IF low bytes steer the pointer whole Zend heap
arbitrary −− / free → anywhere
Use of Uninitialized
+0x08 type_info uninit UBI
type · h · key · value(high), residual bytes
+0x10 h uninit
freed zend_string
+0x18 key ptr → UAF
key is dereferenced here
written by a sprayed string uninitialized (UBI)

The **out-of-bounds** access lands on a fake Bucket that is mostly **uninitialized (UBI)** , only the low bytes of `value` are string-written; its `key` is dereferenced into a freed string ( **UAF** ), and steering that value pointer gives **IF** , an arbitrary decrement anywhere.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 25

## Slide 26

###### **OOB and UAF meet here.**

OOB write
leak
via Index Forgery
control a zval
ZOP
the shared waypoint probe
UAF write
reclaim a freed zval
PC control
Different bugs, one waypoint. OOB via Index Forgery and UAF both reach a controlled zval, then run the same ZOP.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 26

## Slide 27

# **III ZOP**

Zend-Oriented Programming, the interpreter's own structures become the gadget set.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 27

## Slide 28

##### **The interpreter is the gadget set. F R O M O N E P R I M I T I V E , E V E RY T H I N G arbitrary ++/--** → **leak** · **probe** · **hijack**

**L E A K P R O B E H I JAC K** flip a type tag, PHP ++/-- as an oracle a destructor prints the pointer to defeat ASLR pointer you control

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 28

## Slide 29

###### **Let PHP print the pointer.**

value = 0x7ffff46123f0 6.9533461755114104e-310
tag 6 -> 5
type = IS_STRING (6) arb -- type = IS_DOUBLE (5)
a heap pointer same bytes, a number
returned in JSON/XML -> Zend heap address leaked

No OOB read. Flip a string zval to a double and the same bytes come back as a number in the response.

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 29

#BHUSA

## Slide 30

###### **ASLR → just probing.**

**PHP SIDE (NEED PHP-FPM / ZIF_SYSTEM)**

**LIBC SIDE (NEED SYSTEM)**

```
0x000059adca4000000x00007ffff780d000
php-fpm .textlibc.so.6
r-xr-x
near each othernear each other
0x000059adf74100000x00007ffff4600000
FPM_heapzend_heap
rw-rw-
```

###### **PROBE PAGE-BY-PAGE FROM A KNOWN HEAP ANCHOR**

```
0x7ffff4600000 ->
```

```
page okpage okpage okpage okpage okunmappedunmappedunmapped
```

**crash -> 502 = boundary found**

The heaps sit near known code, zend_heap by libc, FPM_heap by php-fpm, so we probe from an anchor until a page faults (502).

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 30

## Slide 31

###### **Hijack via a destructor.**

###### **1 · A NESTED-ARRAY POINTER**

###### **2 · REDIRECTED INTO A PACKED INTEGER ARRAY (SPRAY)**

```
zval.value ->
nested zend_array
```

```
arb -- on low
3 LSBytesintintint
```

```
int
```

```
intintint
```

###### **3 · THOSE BYTES OVERLAP A FORGED ZEND_ARRAY**

```
gc . refcount = 1replacement -> 1->0
arData -> arg0argument controlled
pDestructor -> pccall target controlled
```

pc(arg0)
4 · destructor fires -> hijack

A forged array\'s refcount hits zero, PHP calls its destructor, and we control both the function and its argument.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 31

## Slide 32

# **IV Doing it remotely**

Everything so far needs a heap layout, built in one shot, with no raw bytes allowed.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 32

## Slide 33

###### **Isolation has a gap.**

**USER-INPUT HEAP · ISOLATED**

```
$_GET$_POST$_COOKIE
✕ cannot shape the app heap
decode
```

**APPLICATION HEAP · WHERE THE BUG LIVES** `zend_string zend_array zend_object JSON / XML decode lands here ✓`

Raw request fields are walled off, but the objects the app decodes from them land on the app heap, right where the bug is.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 33

## Slide 34

Duplicate keys = a heap script.
{
  "k": "A"*0x3000,
  "k": "B"*0x4000,
  "k": target,
  "k": null
}

Each value is allocated, all-but-one freed, an alloc/free script inside one request.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 34

## Slide 35

###### **Integer arrays are a raw memory editor.**

**A packed, integer-keyed array stores a flat run of zvals. Set each value → spray any 8-byte pattern.**

```
0xdeadbeefdeadbeef0x41414141414141410x0700000000000001
```

```
…
```

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 35

## Slide 36

# **V**

###### **End to end**

One real CVE, one constrained byte, fully remote, from HTTP request to shell.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 36

## Slide 37

###### **One real bug, fully remote.**

###### **C V E -2 0 24 -2 9 6 1**

glibc iconv OOB via a normal PHP app. In practice: one byte, `0x48–0x4D` . value pinned to All four defenses on. No recon request.

**W H E R E T H E WO R K L I V E S** The victim app is a few lines. The exploit is a heap program encoded entirely in one JSON body.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 37

## Slide 38

Build, place, trigger. Once.
build
place forge trigger
spray fake
page-level 1-byte IF → destructor
bucket +
fengshui fake zval → pc(arg0)
zvals
ONE HTTP REQUEST · SHARE-NOTHING RESET AFTER APPLICATION HEAP
spray zvals / strings
free (duplicate keys)
{ }
one JSON body arData victim buffer
dup keys = a heap script
fake bucket + fake zval
packed ints = raw bytes
fake zend_array
forged array refcount → 0  · destructor runs pc(arg0)

###### Leak, layout, and hijack all fold into a single HTTP body, there is no second request.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 38

## Slide 39

###### **Quick demo.**

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 39

#BHUSA

## Slide 40

# **VI**

###### **Does it hold up?**

Real CVEs, all defenses on, measured for reliability, not a one-off crash.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 40

## Slide 41

###### **We revived the dead CVEs.**

TARGET GOAL OLD OURS REQS SUCCESS

|**TARGET**|**GOAL**|**OLD**|**OURS**|**REQS**|**SUCCESS**|
|---|---|---|---|---|---|
|CVE-2024-2961|RCE|**✗**|**✓**|246|**100%**|
|CVE-2022-31626|RCE|**✗**|**✓**|285|**100%**|
|CVE-2019-6977|SBE|**✗**|**✓**|2|**100%**|
|CTF Case A|RCE|**✗**|**✓**|3|**100%**|
|("I hate php" from SecurinetsCTF)||||||
|CTF Case B("php master" from N1CTF)|RCE|**✗**|**✓**|371|**100%**|

Old public exploits: dead under hardening. Rebuilt with IF + ZOP: revived, under 300 requests, 100% over 100 runs.

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 41

## Slide 42

###### **The roadmap, graded.**

**Already merged & effective: Shadow Pointer · Unlink Abuse Prevention , they forced attackers off freelist poisoning**

PROTOT YPE

IN DEVELOPMENT

PROPOSAL

**Further Heap Guard Pages Isolation** Fixed-size gaps do Per-type dedicated little here. A heaps disrupt remote randomized variant page-level shaping, injects real page-level the assumption our entropy. whole path rests on. **verdict: strong only if randomized**

**Read-only Further Heap Metadata Isolation** Metadata falls, but by Per-type dedicated then the write is heaps disrupt remote already strong, and page-level shaping, the ASLR probe the assumption our exposes writable whole path rests on. structs anyway.

**verdict: limited**

PROPOSAL

**Freelist Randomization** Reorders slots in a freelist, but pagelevel spraying still walks past it.

**verdict: partial**

**Isolation + randomization move the needle. Metadata protection helps least.**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 42

## Slide 43

###### **The smallest fix.**

**PATC H - H AS H TA B L E** Check the index stays within `num_used` . Kills Index Forgery at the source. **0.17%** overhead

**PATC H - R E F C N T** Validate the target is an `zend_refcounted` on aligned the PHP heap. Kills arbitrary ++/--. **8.86%** overhead

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 43

## Slide 44

###### **Good hardening works.**

**WH AT PH P G OT RIG H T** Good freelist hardening. Attackers are forced off the allocator.

**WH AT 'S L E FT** Built-in objects and decoderdriven layout.

**If you want a common defense, harden all common paths.**

**Generic object hardening Object Randomization isolation**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 44

## Slide 45

###### **Good hardening works.**

**If you want a common defense, harden all common paths.**

**Generic object hardening**

**Object isolation Randomization github.com/GhostFrankWu/ PHP-security-research**

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 45

## Slide 46

## **THANK YOU**

PHP's hardening moved the bar. We showed where it still needs to go, and shipped two fixes toward it.

**Burning Tears of PHP's Memory Hardening** Yifan Wu · Xiaochuan Yu · Zhiyun Qian Artifact + Docker: one-click reproduction Black Hat USA 2026 Briefings

#BHUSA

BLACK HAT USA 2026 BRIEFINGS · MANDALAY BAY · LAS VEGAS · AUG 5-6 · #BHUSA · 46
