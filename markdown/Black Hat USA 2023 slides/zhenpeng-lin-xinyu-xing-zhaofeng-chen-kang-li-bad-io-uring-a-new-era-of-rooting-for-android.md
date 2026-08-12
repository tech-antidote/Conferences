---
title: "Bad io uring A New Era of Rooting for Android"
speakers: ["Zhenpeng Lin", "Xinyu Xing", "Zhaofeng Chen", "Kang Li"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zhenpeng Lin & Xinyu Xing & Zhaofeng Chen & Kang Li_Bad io_uring A New Era of Rooting for Android.pdf"
pages: 63
sha256: "c57c69205b0a80c00d53d778a3a3d85c1f22830792c0da489aba7d1b5f7e0a0c"
text_chars: 19212
ocr_pages: 21
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:27:48Z"
---
# Bad io uring A New Era of Rooting for Android

**Speakers:** Zhenpeng Lin, Xinyu Xing, Zhaofeng Chen, Kang Li  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zhenpeng Lin & Xinyu Xing & Zhaofeng Chen & Kang Li_Bad io_uring A New Era of Rooting for Android.pdf` (63 pages)


## Slide 1

# **Bad io_uring: A New Era of Rooting for Android**

**_Zhenpeng Lin_** , Xinyu Xing, Zhaofeng Chen, Kang Li

#badiouring #BHUSA  @BlackHatEvents

## Slide 2

## Who We Are

- **Zhenpeng Lin**

   - Ph.D. from _Northwestern University_

   - Specialized in **_kernel security_**

- **Xinyu Xing**

   - Associate Professor at _Northwestern University_

- **Zhaofeng Chen**

   - Principle Researcher at _Cer0k_

- **Kang Li**

   - Chief Security Officer at _Cer0k_

#badiouring #BHUSA @BlackHatEvents

## Slide 3

## The io_uring

- Efficient I/O opera0ons

- Less Syscalls

- Under **_ACTIVE_** development

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
The to_uring
¢ Efficient |/O operations
e Less Syscalls
¢ Under ACTIVE development
UserSpace
pee ‘Seoaguine
ce
(< ce
KY ?
ors
0
(4
submission oy)
Ci
K ernel
T/O execution
rs Lod completion queue
re
‘
```

## Slide 4

## The BAD io_uring

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
The BAD ito _uring
» Eduardo Vela... X
 @sirdarckcat
"Why io_uring so bad?"
```

## Slide 5

## The BAD io_uring

• Very buggy

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
The BAD ito _uring
¢ Very buggy
» Eduardo Vela... X
 @sirdarckcat
"Why io_uring so bad?"
```

## Slide 6

## The BAD io_uring

- Very buggy

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
The BAD ito _uring
¢ Very buggy
Eduardo Vela... X
 @sirdarckcat
"Why io_uring so bad?"
€ C QQ © @ syzkaller.appspot.com/upstream/fixed anx*
io_uring 17/161 A v x
syzbot Linux v
& Open [982] Subsystems| | & Fixed [4669]] | && Invalid [10858]] | ~/ Kernel Health| | / Bug Lifetin
```

## Slide 7

## The BAD io_uring

- Very buggy

- Ac0ve development, and **_ACTIVE exploita0on_**

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
The BAD ito _uring
¢ Very buggy
¢ Active development, and ACTIVE exploitation
€ Cc a
Eduardo Vela... X
@sirdarckcat
"Why io_uring so bad?"
&@ syzkaller.appspot.com/upstream/fixed
syzbot Linux v
io_uring
17/161
“a
v x
& Open [982]
Subsystems
7K Fixed [4669]
& Invalid [10858]
// Kernel Health
~~ Bug Lifetin
```

## Slide 8

## Exploitation Against io_uring

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidekhat ae ae
USA 20es
Exploitation Against io_uring
CVE-2022-29582
An io_uring vulnerability
Posted by Awarau and pgl.on August 05, 2022 - 93 ‘ijiidietatadald
CVE 2021-20226 reference =
unting bug which leads to local I I (A)
Privilege escalation in io uring
FP omirees tt, Follow ceitoitetion aba ied on ai
[CVE- 7 womens EX loitation applied on an
2022-1786] A Journey To The Dawn io_uring UAF
ALESSANDRO GROPPO
DECEMBER 21, 2022
```

## Slide 9

## Exploitation Against io_uring

- <u>60% submissions to KCTF VRP</u> exploited io_uring as of June 2023

- Around 1 million USD paid out for those bugs

- All public exploits targeted desktop Linux kernel

#badiouring #BHUSA @BlackHatEvents

## Slide 10

## Exploitation Against io_uring

- <u>60% submissions to KCTF VRP</u> exploited io_uring as of June 2023

- Around 1 million USD paid out for those bugs

- All public exploits targeted desktop Linux kernel

- Measures taken by Google

   - ChromeOS: io_uring disabled

   - Google servers: io_uring disabled

   - GKE AutoPilot: invesEgaEng disabling io_uring by default

   - Android: io_uring **_restricted_**

#badiouring #BHUSA @BlackHatEvents

## Slide 11

## Exploitation Against io_uring

- <u>60% submissions to KCTF VRP</u> exploited io_uring as of June 2023

- Around 1 million USD paid out for those bugs

- All public exploits targeted desktop Linux kernel

- Measures taken by Google

   - ChromeOS: io_uring disabled

   - Google servers: io_uring disabled

   - GKE AutoPilot: invesEgaEng disabling io_uring by default

   - Android: io_uring **_restricted_**

      - s"ll accessible from **_privileged_** context (e.g., adb)

#badiouring #BHUSA @BlackHatEvents

## Slide 12

## Exploiting io_uring on Android

• A lot of bugs, a lot of poten0al!

#badiouring #BHUSA @BlackHatEvents

## Slide 13

## Exploiting io_uring on Android

• A lot of bugs, a lot of poten0al!

• 🤓 Fun and profit!

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Exploiting io_uring on Android
¢ A lot of bugs, a lot of potential!
e ©? Fun and profit!
Code execution reward amounts
Description Maximum Reward
Pixel Titan M with Persistence, Zero click Up to $1,000,000
Pixel Titan M without Persistence, Zero click Up to $500,000
Local App to Pixel Titan M without Persistence | Up to $300,000
Secure Element Up to $250,000
Trusted Execution Environment Up to $250,000
Kernel | Up to $250,000
Privileged Process | Up to $100,000
```

## Slide 14

## Exploiting io_uring on Android

• A lot of bugs, a lot of poten0al!

- 🤓 Fun and profit!

- ☹ No public writeup for exploi0ng it on Android

#badiouring #BHUSA @BlackHatEvents

## Slide 15

## CVE-2022-20409

- No difference than other io_uring bugs

- A stable **invalid-free** bug

- The bug I used to _pwn_ **_Google Pixel 6_** and **_Samsung S22_** _in 2022_

- <u>Fixed on 7/29/2022</u>

#badiouring #BHUSA @BlackHatEvents

## Slide 16

## io_uring’s AsyncIO

- Each I/O operation is a _req_ in the submission queue

- Each req can be processed _asynchronously_

- Each req has its _identity_

#badiouring #BHUSA @BlackHatEvents

## Slide 17

## Initializing identity

• _iden5ty_ stores in _io_uring_

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
=
Initializing identity
¢ identity stores in io_uring
ee°e@ identity
int io_uring_alloc_task_context(struct task_struct *task)
{
struct io_uring_task *tctx;
tctx = kmalloc(sizeof(*tctx), GFP_KERNEL);
io_init_identity(&tctx->__identity) |
tctx->identity = &tctx->__identity;
task->io_uring = tctx;
1O_Uring
```

## Slide 18

## Initializing identity

- _iden5ty_ stores in _io_uring_

- _iden5ty_ references to the nested ___iden5ty_

#badiouring #BHUSA @BlackHatEvents

## Slide 19

## Initializing identity

- _iden5ty_ stores in _io_uring_

- _iden5ty_ references to the nested ___iden5ty_

- _io_uring_ is referenced by _task_

#badiouring #BHUSA @BlackHatEvents

## Slide 20

## identity COW

• If _iden5ty_ changes (e.g., cred changes), new _iden5ty_ is created

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
identity COW
¢ If identity changes (e.g., cred changes), new identity is created
WY
static bool io_identity_cow(struct to_kiocb *req) identity
{ +
struct to_uring_task *tctx = current->io_uring; io_uring *
struct io_identity *id; WUT
_ y ; identity *
LLL LL aD
id = kmemdup(req->work.identity, sizeof(*id),
GRP_KERNEL) ;
io_init_identity(id); \ a iG J
req->work.identity = id; 1O_uring task
tctx->identity = id;
```

## Slide 21

## identity COW

- If _iden5ty_ changes (e.g., cred changes), new _iden5ty_ is created

- _iden5ty *_ will reference to the new _iden5ty_ on heap

#badiouring #BHUSA @BlackHatEvents

## Slide 22

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
stat
{
ic bool io_identity_cow(struct io_kiocb *req)
struct to_uring_task *tctx = current->io_uring;
/* drop tctx and req identity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
if (req->work.identity != &tctx->__identity &&
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 23

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
stat
{
ic bool io_identity_cow(struct io_kiocb *req)
struct to_uring_task *tctx = current->io_uring;
/* drop tctx and req identity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity );
if (req->work.identity != &tctx->__identity &&
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 24

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
stat
{
ic bool io_identity_cow(struct io_kiocb *req)
struct to_uring_task *tctx = current->io_uring;
/* drop tctx and req identity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
if (req->work.identity != &tctx->__identity &&
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 25

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
thread A
static bool io_identity_cow(struct io_kiocb *req)
{
koows thread B
struct to_uring_task *tctx = currént->io_uring;
/* drop tctx and req identity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
if (req->work.identity != &tctx->__identity &&
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 26

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
thread A
static bool io_identity_cow(struct io_kiocb *req)
{ aan thread B
struct to_uring_task *tctx = currént->io_uring;
This is False
/* drop tctx and Tepjdent ity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
if (req->work.identity != &tctx->__identity &&
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 27

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
thread A
static bool io_identity_cow(struct io_kiocb *req)
{ aan thread B
struct to_uring_task *tctx = currént->io_uring;
This is Palse
/* drop tctx and Tepjdent ity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
thread A->io_uring-ridentity
if sven svork. ac, I= &tctx->__identity &
refcount_dec_and_test(&req->work. identity->count ) )
kfree(req->work. identity );
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 28

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
thread A
static bool io_identity_cow(struct io_kiocb *req)
{ aan thread B
struct to_uring_task *tctx = currént->io_uring;
This is Palse
/* drop tctx and Tepjdent ity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
thread A->io_uring-ridentity
if sven svork. ac, I= &tctx->__identity &
refcount_dec_and_test(&r work. identity->count ) )
kfree(req->work. identity );
This is true
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 29

## The BUG

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
The BUG
thread A
static bool io_identity_cow(struct io_kiocb *req)
{ aan thread B
struct to_uring_task *tctx = currént->io_uring;
This is False
/* drop tctx and Tepjdent ity references, if needed */
if (tctx->identity != &tctx->__identity &&
refcount_dec_and_test(&tctx->identity->count ) )
kfree(tctx->identity);
thread A->io_uring-ridentity
if sven svork. ac, I= &tctx->__identity &
refcount_dec_and_test(&r work. identity->count ) )
kfree(req->work. identity);
invatlicl Free This is true
req->work.identity = id;
tctx->identity = id;
return true;
```

## Slide 30

### The Memory Corruption Capability

• Invalid-free a _kmalloc-256_ object in the middle

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RT NN eee
black hat oe SOS B's g
USA 2023 —y ‘ we
The Memory Corruption Capability
¢ Invalid-free a kmalloc-256 object in the middle
identity — | ee
Uy
GF allocated object
GY Freel object
kmalloe-256
```

## Slide 31

## Exploitation on Android

- Restricted Access

   - No user_ns

   - No FUSE, userfaulJd

   - No msg_msg, user_key_payload, etc.

   - Very limited choice of syscalls

#badiouring #BHUSA @BlackHatEvents

## Slide 32

## Exploitation on Android

- Restricted Access

   - No user_ns

   - No FUSE, userfaulJd

   - No msg_msg, user_key_payload, etc.

   - Very limited choice of syscalls

- 🧐

- • But we have **_pipe_**

- _pipe_buffer_ is an **_<u>elas/c object</u>_** --- good for spraying

- _pipe_buffer_ contains a global pointer --- good for leaking

#badiouring #BHUSA @BlackHatEvents

## Slide 33

### UAF from identity to pipe_buffer

- Trigger the invalid-free of _identity_ , which frees _io_uring_task_ in the middle

#badiouring #BHUSA @BlackHatEvents

## Slide 34

### UAF from identity to pipe_buffer

- Trigger the invalid-free of _identity_ , which frees _io_uring_task_ in the middle

- Spray _pipe_buffer_ in **kmalloc-256**

#badiouring #BHUSA @BlackHatEvents

## Slide 35

### UAF from identity to pipe_buffer

- Trigger the invalid-free of _iden5ty_ , which frees _io_uring_task_ in the middle

- Spray _pipe_buffer_ in **kmalloc-256**

- Free _io_uring_task_ , which frees _pipe_buffer_

#badiouring #BHUSA @BlackHatEvents

## Slide 36

### UAF from identity to pipe_buffer

- Trigger the invalid-free of _iden5ty_ , which frees _io_uring_task_ in the middle

- Spray _pipe_buffer_ in **kmalloc-256**

- Free _io_uring_task_ , which frees _pipe_buffer_

- How to **leak** _pipe_buffer_ out?

#badiouring #BHUSA @BlackHatEvents

## Slide 37

## Recap of The io_uring Design

• The **_ring buffer_** is accessible to both userspace and kernel

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifeK hat
USA 20253
Recap of The ito_uring Design
¢ The ring buffer is accessible to both userspace and kernel
UserSpace
pie Serco
Ce LOL, /,
w <n f ‘i
o~
g
O- e *
submission queud A CJ PS CE completion queue.
S¢ %e
‘
K ernel
T/O execution
```

## Slide 38

## The Shared Ring

- **User** pages **_shared_** between kernel and userspace

- The memory is allocated by **_buddy allocator_** and mapped to userspace

- No copy_to/from_user is needed

- Date can be transported directly without copying

   - Read/write kernel memory from userspace

   - Read/write userspace memory from kernel

#badiouring #BHUSA @BlackHatEvents

## Slide 39

## The “DirtyPage” Technique

- Some user pages are recycled with slab pages

   - **Spraying pages to reclaim freed slab pages**

   - Spray objects? No! We spray pages now!

   - Candidates: _io_uring, pipe_

- What is the advantage?

   - Powerful 🤓 : Read/write slab objects from userspace

   - • Stable 🤓 : Spray once to have persist read/write on vicEm object

   - 🤓 : Just allocate more

   - • Simple

#badiouring #BHUSA @BlackHatEvents

## Slide 40

#### Achieving Read/Write on pipe_buffer

• Preparing the memory layout

#badiouring #BHUSA @BlackHatEvents

## Slide 41

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

#badiouring #BHUSA @BlackHatEvents

## Slide 42

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

- Freeing the slab page

#badiouring #BHUSA @BlackHatEvents

## Slide 43

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

- Freeing the slab page

- Reclaiming the freed slab page

#badiouring #BHUSA @BlackHatEvents

## Slide 44

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

- Freeing the slab page

- Reclaiming the freed slab page

- Reading _pipe_buffer_

   - _ops_ --- **bypass kaslr**

#badiouring #BHUSA @BlackHatEvents

## Slide 45

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

- Freeing the slab page

- Reclaiming the freed slab page

- Reading _pipe_buffer_

   - _ops_ --- **bypass kaslr**

- Wri0ng _pipe_buffer_

   - _flags_ --- **<u>Dirty Pipe Retro!</u>**

#badiouring #BHUSA @BlackHatEvents

## Slide 46

#### Achieving Read/Write on pipe_buffer

- Preparing the memory layout

- Triggering the invalid-free

- Freeing the slab page

- Reclaiming the freed slab page

- Reading _pipe_buffer_

   - _ops_ --- **bypass kaslr**

- Wri0ng _pipe_buffer_

   - _flags_ --- **<u>Dirty Pipe Retro!</u>**

   - _page_ --- **arbitrary r/w** on kernel memory?

#badiouring #BHUSA @BlackHatEvents

## Slide 47

## How Pipe Uses Pages

- **_kmap_atomic_** the page

- copy **_in/out_** the page

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es
How Pipe Uses Pages
¢ kmap_atomic the page
static ssize_t
e copy infout the page prpe_readtesruct kiocb *xiocb, struct iov_iter *to) {
// in copy_page_to_iter_iovec
kaddr = kmap_atomic( page);
from = kaddr + offset;
left = copyout(buf, from, copy);
}
static ssize_t
pipe_write(struct kiocb *iocb, struct tov_iter *to)
{
// in copy_page_from_iter_iovec
kaddr = kmap_atomic( page);
to = kaddr + offset;
left = copyin(to, buf, copy);
```

## Slide 48

## How Pipe Uses Pages

- **_kmap_atomic_** the page

- copy **_in/out_** the page

- **_kmap_atomic_** is **_page_address_**

#badiouring #BHUSA @BlackHatEvents

## Slide 49

## How Pipe Uses Pages

- **_kmap_atomic_** the page

- copy **_in/out_** the page

- **_kmap_atomic_** is **_page_address_**

- **_page_address_**

   - equals (page<< **SHIFT** )+ **OFFSET**

   - **SHIFT** is fixed

   - **OFFSET** is also **fixed** on ARM64

#badiouring #BHUSA @BlackHatEvents

## Slide 50

## Achieving Kernel Arbitrary R/W

- Given a kernel address

   - Calculate the its page

   - Calculate the offset

   - Overwrite the _pipe_buffer_ with calculated data

- _Read/Write_ by reading/wri0ng the pipe

#badiouring #BHUSA @BlackHatEvents

## Slide 51

## Escalating Privilege On Pixel 6

#badiouring #BHUSA @BlackHatEvents

## Slide 52

## Samsung’s KNOX

- Samsung has customized protec0on for their kernel --- KNOX

- KNOX protects cred integrity

#badiouring #BHUSA @BlackHatEvents

## Slide 53

## Samsung’s KNOX

- Samsung has customized protec0on for their kernel --- KNOX

- KNOX protects cred integrity

#badiouring #BHUSA @BlackHatEvents

## Slide 54

## Samsung’s KNOX

• Samsung has customized protection for their kernel --- KNOX

- KNOX protects cred integrity

#badiouring #BHUSA @BlackHatEvents

## Slide 55

## Samsung’s KNOX

• Samsung has customized protection for their kernel --- KNOX

- KNOX protects cred integrity

#badiouring #BHUSA @BlackHatEvents

## Slide 56

## Samsung’s KNOX

- Samsung has customized protec0on for their kernel --- KNOX

- KNOX protects cred integrity

- **_cred_** object is read-only, **_uid_** field is read-only

#badiouring #BHUSA @BlackHatEvents

## Slide 57

## Validating cred Integrity

- Cross-checking between **_task_** and **_cred_**

- Integrity is validated at syscall entry

#badiouring #BHUSA @BlackHatEvents

## Slide 58

## Validating cred Integrity

- Cross-checking between **_task_** and **_cred_**

- Integrity is validated at syscall entry

- How to prevent the cred is forged?

#badiouring #BHUSA @BlackHatEvents

## Slide 59

## Validating cred Integrity

- How to prevent the cred is forged?

   - Checking if the **_cred_** is from **_cred_jar_ro/tsec_jar_** slab

#badiouring #BHUSA @BlackHatEvents

## Slide 60

## Validating cred Integrity

- How to prevent the cred is forged?

   - Checking if the **_cred_** is from **_cred_jar_ro/tsec_jar_** slab

   - This check is weak which could by bypassed

#badiouring #BHUSA @BlackHatEvents

## Slide 61

## Bypassing KNOX

- Forging a **_root cred_** with correct references

- Tampering the **_slab_cache_** of the forged cred’s page

#badiouring #BHUSA @BlackHatEvents

## Slide 62

## Escalating Privilege On S22

#badiouring #BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidekhat
USA 20es
e* O06
Galaxy Store Galllery Play Store Google
6Osc
il (0)
<
```

## Slide 63

## Takeaways

- io_uring is a huge ahack surface not only to desktop but also to AOSP

- **_Restric0ng_** io_uring on Android doesn’t seem enough

- Object spray is not the only exploit op0on, try **_DirtyPage_ (** page spray **)** !

- Android kernel exploita0on with **_DirtyPage_** is simple!

<u>hhps://github.com/Markakd/bad_io_uring @Markak_ hhps://zplin.me</u>

#badiouring #BHUSA @BlackHatEvents
