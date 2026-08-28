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
text_chars: 19318
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 46
vision_verified_pages: 46
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T05:34:35Z"
---
# Burning Tears of PHP's Memory Hardening

**Speakers:** Frank Wu, xia0o0o0o, Zhiyun Qian  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Frank Wu&xia0o0o0o&Zhiyun Qian_Burning Tears of PHP's Memory Hardening.pdf` (46 pages)


## Slide 1

### **Burning Tears of PHP's Memory Hardening**

A fully remote, generic exploit path that survives PHP's newest heap defenses, from one constrained byte.

**Yifan Wu** · Xiaochuan Yu · Zhiyun Qian  ·  UC Riverside · UC San Diego

## Slide 2

###### **This research is 100% LLM-free.**

(except for making these slides)

## Slide 3

###### **Two researchers, one lab.**

\```
nebula@blackhat: ~/talks/burning-tears
\```

\```
nebula@blackhat:~$ whoami
\```

\```
Frank Wu · Nebula Security
Hacking Linux and Android
\```

\```
Xiaochuan Yu · Nebula Security
Hacking XNU and Browsers
\```

\```
nebula@blackhat:~$ cat recent_work.md
\```

- `first public nginx RCE · remote, ASLR bypass, generic config`

- `world's first Android 17 root (GhostLock) · one URL, full device control`

- `first public Android browser → kernel full-chain (IonStack) in 7 years`

\```
nebula@blackhat:~$ ./burning_tears.sh --target=php --remote
\```

## Slide 4

###### **It started with a CTF.**

r3kapig
# securinets-ctf-quals-2024 › Pwn-I HATE PHP!

Frank Wu ⚡NEBU 🪓PWN · 2024/10/13 03:10
maybe we are close to aaw..

\```
RDI  0x76838d200040 ← 0
RSI  0x76838d201060 → 0x76838d201090 → 0x76838d2010f0 → 0x76838d1f3e90 → 0x…f0ef5fa25 (_efree) ← ...
R8   0
\```

👍 1

Frank Wu ⚡NEBU 🪓PWN · 2024/10/13 03:41
WT█

\```
4 months ago · Detect heap freelist corruption (...
1278  #if ZEND_MM_HEAP_PROTECTION
1279  /* We keep track of free slots by organizing them in a linked list, with the
1280   * first word of every free slot being a pointer to the next one.
1281   *
1282   * In order to frustrate corruptions, we check the consistency of these pointers
1283   * before dereference by comparing them with a shadow.
1284   *
1285   * The shadow is a copy of the pointer, stored at the end of the slot. It is
1286   * XOR'ed with a random key, and converted to big-endian so that smaller
1287   * corruptions affect the most significant bytes, which has a high chance of
1288   * resulting in an invalid address instead of pointing to an adjacent slot.
1289   */
1290
1291  #define ZEND_MM_FREE_SLOT_PTR_SHADOW(free_slot, bin_num) \
1292      *((zend_mm_free_slot**)((char*)(free_slot) + bin_data_size[(bin_num)] - sizeof(zend_mm_free_slot*)))
\```

PROTECTION added right before 4 month

**1**

**The CTF**
An ordinary PHP challenge.

**2**

**The 0-day**
A real flaw. PHP patched it.

AN UNPLANNED SIDE-FIND

**3**

**The real question**
One defense cracks, all four?

**Thank you Securinets CTF** 🥰🥰

## Slide 5

###### **One request. That's all you get.**

**Browser pwn**
\```
for(let i=0;i<0x4000;i++){
    foo(true);
}
new ArrayBuffer(0x7f00000);
\```

**Kernel pwn**
\```
for(int i=0;i<N;i++)
  msgsnd(qid[i],&msg,size,0);
\```

**PHP remote**
\```
POST /upload.php HTTP/1.1
Host: victim.tld
Content-Length: 8192

data=%00%02%be%ef...
\```

## Slide 6

###### **How you used to pwn PHP.**

\```
ZendMM: singly-linked list
\```

overflow →

in-use buffer
next 0x…30 · free slot
next 0x…20 · free slot
…

victim object · chunk returned by allocator · victim object

**read / write victim fields › leak & overwrite a function pointer › RCE**

## Slide 7

###### **Then PHP fought back.**

**Shadow Pointer**
checked on every alloc
next
encrypted
free slot
shadow
encrypted
=
✕ freelist poisoning

**Unlink Prevention**
chunk A
fd/bk
chunk P
fd/bk
chunk B
P->fd->bk == P
P->bk->fd == P
✕ list-forgery writes

**RO Metadata**
write → ✕
zend_mm_heap
_malloc
_free
_realloc
read-only at runtime
✕ metadata hook hijack

**Heap Isolation**
request zone
$_GET $_POST
✕
application heap
objects, strings
✕ raw-request spray

~~CVE-2024-2961~~  ~~CVE-2022-31626~~  ~~public CTF chain~~

Aimed at the exact techniques every public PHP exploit relied on.

## Slide 8

###### **The old exploits died.**

`freelist next`
✕
**blocked by Shadow Pointer**

`metadata hooks`
✕
**blocked by Read-only**

`$_POST spray`
✕
**blocked by Heap Isolation**

Each new defense closes exactly one classic technique
freelist, metadata, and raw spray all gone.

## Slide 9

#### **PART I The playing field**

How PHP allocates, and why that lets us shape the heap at all, remotely.

## Slide 10

###### **Same request, same heap.**

request #1
freed pages
freelist
0x…30 → 0x…80 → 0x…d0

request #2
freed pages
freelist
0x…30 → 0x…80 → 0x…d0

Fresh chunk each request, best-fit + LIFO, no cross-request state, so identical requests build identical heaps.

## Slide 11

###### **What fengshui buys us.**

**Anything** (raw bytes) Spray attacker-defined raw memory the interpreter will later trust.

**Anywhere** (placement) Put a chosen object at any offset next to the victim, in one request.

Both are hard under the new defenses. Earning them back is the rest of the talk.

## Slide 12

###### **So we stopped touching the allocator.**

**00 · 1-byte OOB**
1 byte past the edge
buffer · neighbour
the weakest possible bug

**01 · Index Forgery** (CONTRIBUTION)
index array
BIG → fake
corrupt a table index, not a pointer

**02 · Arbitrary ++/−−**
fake zval
++ / −−
value | type → *p
read = *p++, write = *p−−

**03 · ZOP**
leak
probe
hijack
the interpreter is the gadget set

Every step lives in built-in PHP objects, never the allocator, never app classes.

## Slide 13

**II**

###### **Index Forgery**

Turning the weakest possible bug, one constrained byte, into a strong primitive.

## Slide 14

###### **One byte in.**

**1-byte OOB**
the input
weakest bug

**index forgery**
one integer

**fake zval**
a controlled object

**arbitrary ++/--**
write anywhere
strong primitive

1-byte overflow · value constrained · no OOB read

The nightmare bug, yet enough. Works here means it works for almost anything stronger.

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

\```
flags byte: IS_TYPE_REFCOUNTED = 1<<0
\```

Every PHP value is 8 bytes plus a type tag. Control a zval, and you control what PHP believes memory is.

## Slide 16

###### **The real target: arData.**

**ZEND_ARRAY (HASHTABLE)**
+0x00  **gc** · refcount
+0x0c  **nTableMask**
+0x10  **arData** → butterfly
+0x18  **nNumUsed** · size
+0x38  **pDestructor** · hijack target

**ARDATA IS A BUTTERFLY**
A *separate* allocation the overflow reaches. arData points to the split: index array on the left half, buckets on the right.

idx idx idx Bucket[0] Bucket[1]
← index grows  |  arData →   buckets grow →

## Slide 17

###### **A normal lookup.**

$t[$key]

ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS

victim buf
overflow source

0x00 0x01 0x02 0x03

SPRAYED REGION

arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval

Bucket[0].value
raw string bytes

A zend_array reads from a separatearDatabuffer, index array in front of the buckets.

## Slide 18

###### **A normal lookup.**

$t[$key]

ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS

victim buf
overflow source

0x00 0x01 0x02 0x03
0x00 → Bucket[0]

SPRAYED REGION

arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval

Bucket[0].value
raw string bytes

hash(key) | mask → a slot → the integer there picks the Bucket. PHP never doubts that integer.

## Slide 19

###### **One byte, one redirect.**

$t[$key]

ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS

victim buf
overflow source

1-byte OOB → 0x4D  0x01  0x02  0x03

SPRAYED REGION

arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval

Bucket[0].value
raw string bytes

The overflow lands onindex[0], not a pointer, just a small integer. One byte moves it far.

## Slide 20

###### **One byte, one redirect.**

$t[$key]

ARDATA BUFFER (BUTTERFLY) · INDEX | BUCKETS

victim buf
overflow source

1-byte OOB → 0x4D  0x01  0x02  0x03

sprayed, known offset
fake Bucket
fake zval

arData
Bucket[0] Bucket[1] Bucket[2] BUCKETS
zval zval zval

Bucket[0].value
raw string bytes

A large index reaches memorywe sprayed, a fake Bucket holding a fake zval we control.

## Slide 21

###### **Make the fake pass.**

**forged Bucket (sprayed)**
+0x00  zval.value  you set
+0x08  zval.u1.type_info  you set
+0x10  h (hash)  MUST match
+0x18  key  MUST match

**HOW THE CHECK PASSES**

hash: DJBX33A is reversible
craft a string whose hash == the key we look up (Alg.1)

key: reoccupy the residual key pointer
spray the same key bytes so the compare succeeds

**lookup passes ✔**
$t[key] returns our fake zval

PHP re-checks the bucket key and hash. We forge a match with the reversible DJBX33A hash, and the lookup passes.

## Slide 22

###### **Now you own a zval.**

fake zval
value -> *target

read $t[$key]      *target ++
write $t[$key]=$v *target--

any address

Mark the fake zval refcounted, and a plain read/write does ++ / -- through your pointer, at any address.

## Slide 23

###### **But the pointer is constrained.**

###### **WHY LIMITED**

The value pointer is sprayed as a string, encoding-restricted. We control only its low bytes.

So ++/-- lands *near* a chosen spot, not anywhere.

**value = 0x…??**
low-byte overlap
→ nearby sprayed memory

## Slide 24

###### **Lift to arbitrary.**

###### **ONE EXTRA INDIRECTION**

Steer the constrained value at the type_flags of another zval in a sprayed array.

++/-- on a type tag → make any zval refcounted → decrement anywhere.

fake zval.value
low-byte steer
└→ zval.type_flags
limited ++/-- → arbitrary ++/--

## Slide 25

###### **One corrupted index. Four primitives.**

the one operation

$t[key] → LARGE 2 0 5 → Bucket[large]
OOB — the large index reaches out of bounds
a corrupted index, the 1-byte overflow set index[0] to LARGE

**fake Bucket** — what Bucket[large] lands on
+0x00  value    low | high
+0x08  type_info  uninit
+0x10  h  uninit
+0x18  key  ptr →

🟩 written by a sprayed string   🟧 uninitialized (UBI)

IF — low bytes steer the pointer
arbitrary −− / free → anywhere
→ ANY address / whole Zend heap

UBI — Use of Uninitialized
type · h · key · value(high), residual bytes

UAF → freed zend_string
key is dereferenced here

The **out-of-bounds** access lands on a fake Bucket that is mostly **uninitialized (UBI)** , only the low bytes of `value` are string-written; its `key` is dereferenced into a freed string ( **UAF** ), and steering that value pointer gives **IF** , an arbitrary decrement anywhere.

## Slide 26

###### **OOB and UAF meet here.**

**OOB write**
via Index Forgery

**UAF write**
reclaim a freed zval

**control a zval**
the shared waypoint

**ZOP**

leak
probe
PC control

Different bugs, one waypoint. OOB via Index Forgery and UAF both reach a controlled zval, then run the same ZOP.

## Slide 27

# **III ZOP**

Zend-Oriented Programming, the interpreter's own structures become the gadget set.

## Slide 28

###### **The interpreter is the gadget set.**

**FROM ONE PRIMITIVE, EVERYTHING**
arbitrary ++/-- → leak · probe · hijack

**LEAK**
flip a type tag, PHP prints the pointer

**PROBE**
++/-- as an oracle to defeat ASLR

**HIJACK**
a destructor pointer you control

## Slide 29

###### **Let PHP print the pointer.**

value = 0x7ffff46123f0
type = IS_STRING (6)
a heap pointer

tag 6 -> 5
arb --

6.9533461755114104e-310
type = IS_DOUBLE (5)
same bytes, a number

returned in JSON/XML -> Zend heap address leaked

No OOB read. Flip a string zval to a double and the same bytes come back as a number in the response.

## Slide 30

###### **ASLR → just probing.**

**PHP SIDE (NEED PHP-FPM / ZIF_SYSTEM)**
php-fpm .text — 0x000059adca400000 — r-x
near each other
FPM_heap — 0x000059adf7410000 — rw-

**LIBC SIDE (NEED SYSTEM)**
libc.so.6 — 0x00007ffff780d000 — r-x
near each other
zend_heap — 0x00007ffff4600000 — rw-

###### **PROBE PAGE-BY-PAGE FROM A KNOWN HEAP ANCHOR**

0x7ffff4600000 ->
page ok  page ok  page ok  page ok  page ok  unmapped  unmapped  unmapped

crash -> 502 = boundary found

The heaps sit near known code, zend_heap by libc, FPM_heap by php-fpm, so we probe from an anchor until a page faults (502).

## Slide 31

###### **Hijack via a destructor.**

###### **1 · A NESTED-ARRAY POINTER**

zval.value ->
nested zend_array

arb -- on low
3 LSBytes

###### **2 · REDIRECTED INTO A PACKED INTEGER ARRAY (SPRAY)**

int int int int int int int

###### **3 · THOSE BYTES OVERLAP A FORGED ZEND_ARRAY**

gc . refcount = 1
replacement -> 1->0

arData -> arg0
argument controlled

pDestructor -> pc
call target controlled

pc(arg0)
4 · destructor fires -> hijack

A forged array's refcount hits zero, PHP calls its destructor, and we control both the function and its argument.

## Slide 32

# **IV Doing it remotely**

Everything so far needs a heap layout, built in one shot, with no raw bytes allowed.

## Slide 33

###### **Isolation has a gap.**

**USER-INPUT HEAP · ISOLATED**

\```
$_GET  $_POST  $_COOKIE
✕ cannot shape the app heap
decode
\```

**APPLICATION HEAP · WHERE THE BUG LIVES** `zend_string  zend_array  zend_object`
JSON / XML decode lands here ✓

Raw request fields are walled off, but the objects the app decodes from them land on the app heap, right where the bug is.

## Slide 34

###### **Duplicate keys = a heap script.**

\```
{
  "k": "A"*0x3000,
  "k": "B"*0x4000,
  "k": target,
  "k": null
}
\```

Each value is allocated, all-but-one freed, an alloc/free script inside one request.

## Slide 35

###### **Integer arrays are a raw memory editor.**

**A packed, integer-keyed array stores a flat run of zvals. Set each value → spray any 8-byte pattern.**

\```
0xdeadbeefdeadbeef  0x4141414141414141  0x0700000000000001  …
\```

## Slide 36

# **V**

###### **End to end**

One real CVE, one constrained byte, fully remote, from HTTP request to shell.

## Slide 37

###### **One real bug, fully remote.**

###### **CVE-2024-2961**

glibc iconv OOB via a normal PHP app. In practice: one byte, value pinned to `0x48-0x4D`.

All four defenses on. No recon request.

**WHERE THE WORK LIVES**
The victim app is a few lines. The exploit is a heap program encoded entirely in one JSON body.

## Slide 38

###### **Build, place, trigger. Once.**

**build**
spray fake bucket + zvals

**place**
page-level fengshui

**forge**
1-byte IF → fake zval

**trigger**
destructor → pc(arg0)

ONE HTTP REQUEST · SHARE-NOTHING RESET AFTER
APPLICATION HEAP

{ }
one JSON body
dup keys = a heap script
packed ints = raw bytes

spray zvals / strings
free (duplicate keys)
arData victim buffer
fake bucket + fake zval
fake zend_array

forged array refcount → 0 · destructor runs
pc(arg0)

Leak, layout, and hijack all fold into a single HTTP body, there is no second request.

## Slide 39

###### **Quick demo.**

## Slide 40

# **VI**

###### **Does it hold up?**

Real CVEs, all defenses on, measured for reliability, not a one-off crash.

## Slide 41

###### **We revived the dead CVEs.**

|**TARGET**|**GOAL**|**OLD**|**OURS**|**REQS**|**SUCCESS**|
|---|---|---|---|---|---|
|CVE-2024-2961|RCE|**✗**|**✓**|246|**100%**|
|CVE-2022-31626|RCE|**✗**|**✓**|285|**100%**|
|CVE-2019-6977|SBE|**✗**|**✓**|2|**100%**|
|CTF Case A ("I hate php" from SecurinetsCTF)|RCE|**✗**|**✓**|3|**100%**|
|CTF Case B ("php master" from N1CTF)|RCE|**✗**|**✓**|371|**100%**|

Old public exploits: dead under hardening. Rebuilt with IF + ZOP: revived, under 300 requests, 100% over 100 runs.

## Slide 42

###### **The roadmap, graded.**

Already merged & effective: **Shadow Pointer** · **Unlink Abuse Prevention**, they forced attackers off freelist poisoning

**PROTOTYPE**
**Read-only Metadata**
Metadata falls, but by then the write is already strong, and the ASLR probe exposes writable structs anyway.
verdict: limited

**IN DEVELOPMENT**
**Further Heap Isolation**
Per-type dedicated heaps disrupt remote page-level shaping, the assumption our whole path rests on.
verdict: strong

**PROPOSAL**
**Guard Pages**
Fixed-size gaps do little here. A randomized variant injects real page-level entropy.
only if randomized

**PROPOSAL**
**Freelist Randomization**
Reorders slots in a freelist, but pagelevel spraying still walks past it.
verdict: partial

Isolation + randomization move the needle. Metadata protection helps least.

## Slide 43

###### **The smallest fix.**

**PATCH-HASHTABLE**
Check the index stays within `num_used`. Kills Index Forgery at the source.

**0.17%** overhead

**PATCH-REFCNT**
Validate the target is an aligned `zend_refcounted` on the PHP heap. Kills arbitrary ++/--.

**8.86%** overhead

## Slide 44

###### **Good hardening works.**

**WHAT PHP GOT RIGHT**
Good freelist hardening. Attackers are forced off the allocator.

**WHAT'S LEFT**
Built-in objects and decoder-driven layout.

**If you want a common defense, harden all common paths.**

**Generic object hardening**
**Object isolation**
**Randomization**

## Slide 45

###### **Good hardening works.**

**If you want a common defense, harden all common paths.**

**Generic object hardening**
**Object isolation**
**Randomization**

github.com/GhostFrankWu/PHP-security-research

## Slide 46

## **THANK YOU**

PHP's hardening moved the bar. We showed where it still needs to go, and shipped two fixes toward it.

**Burning Tears of PHP's Memory Hardening**
Yifan Wu · Xiaochuan Yu · Zhiyun Qian
Artifact + Docker: one-click reproduction
Black Hat USA 2026 Briefings

