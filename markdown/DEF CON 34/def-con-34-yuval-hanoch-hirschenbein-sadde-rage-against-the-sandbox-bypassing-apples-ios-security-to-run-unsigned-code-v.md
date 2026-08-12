---
title: "Rage Against the Sandbox Bypassing Apple’s iOS Security to Run Unsigned Code via SSH"
speakers: ["Yuval Hanoch Hirschenbein Sadde"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Yuval Hanoch Hirschenbein Sadde - Rage Against the Sandbox Bypassing Apple’s iOS Security to Run Unsigned Code via SSH.pptx"
pages: 35
sha256: "c8fad55506a154543f82a285c102ded093d9492f105174764497a905c84b3c7b"
text_chars: 21974
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:40:33Z"
---
# Rage Against the Sandbox Bypassing Apple’s iOS Security to Run Unsigned Code via SSH

**Speakers:** Yuval Hanoch Hirschenbein Sadde  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Yuval Hanoch Hirschenbein Sadde - Rage Against the Sandbox Bypassing Apple’s iOS Security to Run Unsigned Code via SSH.pptx` (35 pages)


## Slide 1

Rage Against the Sandbox Bypassing Apple’s iOS Security to Run Unsigned Code via SSH

## Slide 2

## cat /proc/self/stat

- Yuval Hanoch Hirschenbein Sadde, 27, Tel Aviv • mobile security 9 years (7 android + 2 ios)

   - coding since age of 11

   - loving computers since age of 4 (win95 laptop lol)

   - loves hacker jeopardy

## Slide 3

## the goal

- stop using whacky apple developer tools to debug iphones

- • use open-source tools (dropbear SSH, mksh, toybox)

- don’t sign exploits

-

- fork: EPERM

- mmap(PROT_EXEC): SIGKILL

## Slide 4

## iOS security

- Sandbox (or Seatbelt internally) - Apple's SELinux

   - Mandatory Access Framework

   - Sandbox Profiles == SELinux Labels

   - App Store applications run under "container.sb" profile

      - `// bsd/kern/kern_fork.c int fork1(proc_t parent_proc, thread_t`

      - `*child_threadp, ...) {`

```
  // ...
```

```
#if CONFIG_MACF
```

```
  err =mac_proc_check_fork(parent_proc); // calls
Sandbox.kext
```

```
if (err != 0)
```

```
    goto bad;
#endif
```

## Slide 5

## profile examples

```
// container.sb
(version 1)
(deny default)  // implies (deny process-fork)
(allow file-read*
  (subpath "/System/Library")
  (literal
"/private/var/preferences/com.apple.security.plist"))
(allow network-inbound
```

```
// debugserver.sb
(version 1)
(deny default)
(allow process-fork
  (debug-mode))
```

```
  (local ip "*:*"))
(allow process-info-pidinfo
  (target self)
  (entitlement "com.apple.security.exception.process-info")
  (require-all
```

```
    (target others)
    (entitlement
"com.apple.DiagnosticExceptions.extension")))
(allow iokit-open
```

```
  (iokit-user-client-class "IOAppleJPEGDriverUserClient"))
(allow mach-lookup
  (global-name "com.apple.springboard"))
```

## Slide 6

## iOS security

- Sandbox (or Seatbelt internally) - Apple's SELinux

   - Mandatory Access Framework

   - Sandbox Profiles == SELinux Labels

   - App Store applications run under "container.sb" profile

- Code Signing – validate EXEC page

   - on mmap() “vibe checks” the file signature

   - on page fault validates hash of EXEC page content

```
// osfmk/vm/vm_fault.c
```

```
kern_return_t vm_fault_internal(vm_map_t map,...) {
vm_fault_enter(...) {
vm_fault_enter_prepare(...) {
vm_fault_validate_cs(...) {
// ... a few more frames
// bsd/kern/ubc_subr.c
```

```
cs_validate_page(...)  // <- hash checks start
here
```

## Slide 7

## do we really need fork ?

- just implement our fork()less fork()

// mksh.c
  // ...
pid_t child =
fork();
ssh
sh
• oh dear... cat
grep

// tvm.c - our code
pid_t fork() {
  pthread_t p;
pthread_create(&p);
  return (int)p;
}

## Slide 8

## the rabbithole

- isolated resources

   - file descriptors, signal handlers

- gotta wrap a lot of functions!

   - fd stuff - open(), read(), write()

      - translate each "vproc" fd to "real" fd

   - FILE * stuff - printf, fprintf

      - stdout is NOT stdout!!!

   - proc stuff - fork(), waitpid()

```
// tvm.c
```

```
static __thread struct task *current;
```

```
ssize_t write(int fd, const void *buf, size_t
count) {
```

```
if (fd >= MAX_FILES) {
    errno =EBADF;
return-1;
  }
```

```
  int rfd = current->tsk_files[fd];
returndlsym(RTLD_NEXT, "write")(rfd, buf,
count));
}
```

call real write()

## Slide 9

## the rabbithole

- isolated resources

   - file descriptors, signal handlers

- gotta wrap a lot of functions!

   - fd stuff - open(), read(), write()

      - translate each "vproc" fd to "real" fd

   - FILE * stuff - printf, fprintf

      - stdout is NOT stdout!!!

   - proc stuff - fork(), waitpid()

- virtual memory

   - stack, heap, data

   - copy-on-write semantics! `g_val = 1; pid_t child = fork(); if (child == 0) g_val = 5;  // parent sees g_val as 1`

   - pthread accepts a callback!

- `// tvm.c`

```
/* parent returns with non-zero pid
```

- `child returns with 0 */`

```
pid_t fork() {
```

```
  pthread_t p;
```

```
pthread_create(&p, NULL, thread_entry, NULL);
return (pid_t)p;
```

```
}
```

```
void thread_entry() {
// okay now wut
}
```

OLD STACK NEW STACK
0x000
0
fork
ret
<parent>
?
<granny>
:( thread_entr
<ancestor
y
?
> pthread_st
...
art
0xFFF
F

## Slide 10

## the rabbithole

fork()

- isolated resources

   - file descriptors, signal handlers

- gotta wrap a lot of functions!

   - fd stuff - open(), read(), write()

      - translate each "vproc" fd to "real" fd

   - FILE * stuff - printf, fprintf

      - stdout is NOT stdout!!!

   - proc stuff - fork(), waitpid()

- virtual memory

   - stack, heap, data

   - copy-on-write semantics!

```
g_val = 1;
pid_t child =fork();
if (child == 0)
  g_val = 5;  // parent sees g_val as 1
```

- pthread accepts a callback!

VProcess “SSH” VProcess “Shell”
Threa Threa Threa
d d d
Stack, Heap,  Stack, Heap,
Data Data
FDs,  FDs,
Sighandlers Sighandlers

```
// tvm.c
pid_t fork() {
  ptrlist_t pl =new_ptrlist();
  new_task =task_create();
dup_fds_and_sighandlers(new_task,
current);
  // ???
  return new_task->tsk_pid;
}
```

## Slide 11

## Copy-On-Write

• duplicated child memory holds pointers to parent’s memory

```
// tvm.c
pid_t fork() {
  ptrlist_t pl =new_ptrlist();
  new_task =task_create();
dup_fds_and_sighandlers(new_task,
current);
  // collect "duplicated" pointers to &pl
  // ...
fixup(&pl); // "fixup" all
return new_task->tsk_pid;
}
struct ptrent_t {0x00014000
  uint64_t *old;0x0002C000
  uint64_t *new;0x4000
  size_t    size;
}
```

```
struct ptrlist_t {
  ptrent_t *list;
  size_t    count;
}
```

fork()
0x00014000 0x0002C000
0000000 0000000
0 0
0000000 0000000
0 0
0000000 0000000
0 0
7461687 7461687
7 7
3F70757 3F70757
3 3
0000000 0000000
0 0
000145C 00014 2C 5C
C C
0x00030000
0x00018000
0000000 0000000
0 0
00014FF 00014 2C FF
E E
fixup pointers to child memory 0001400 00014 2C 00
8 8
0000000 0000000
0 0
0000000 0000000

not rly :(
gotta optimizeez

## Slide 12

Heap COW

eap

- bugs
- death

```
// heap.h
arena_t *arena_create();
void arena_destroy(arena_t *ar);
```

```
void *arena_alloc(arena_t *ar, size_t
size);
```

// tvm.c
void *malloc(size_t s) {
return arena_alloc(current->tsk_ar,
size);
}

```
void arena_free(arena_t *ar, void *ptr);
```

```
int arena_duplicate(
  arena_t *dst_ar, arena_t *src_ar,
  ptrlist_t *pl);
```

fork()
0x10 SLAB 0x10 SLAB
0x000 slab_t slab_t
0
FREE
CHUNK CHUNK
CHUNK CHUNK
memcpy(
FREE )
CHUNK CHUNK
FREE
FREE
FREE
0xFFF ... ...
F

0x000

```
struct slab_t {
  size_t   obj_size;
  size_t   slab_size;
  size_t   min_off;
  size_t   max_off;
  bitmap_t residents;
  char     data[0];
}
```

## Slide 13

eap

eap
Heap COW - bugs
- death

```
// heap.h
arena_t *arena_create();
void arena_destroy(arena_t *ar);
void *arena_alloc(arena_t *ar, size_t
size);
void arena_free(arena_t *ar, void *ptr);
int arena_duplicate(
  arena_t *dst_ar, arena_t *src_ar,
  ptrlist_t *pl);
```

```
struct ptrent_t {
  uint64_t *old;
  uint64_t *new;
  size_t    size;
}
```

pid_t fork() {
  ptrlist_t pl = new_ptrlist();
  new_task = task_create();
dup_fds_and_sighandlers(new_task,
current);
arena_duplicate(
    new_task->tsk_ar, current->tsk_ar,
&pl);
// ...
fixup(&pl);
return new_task->tsk_pid;
} fork()
0x10 SLAB 0x10 SLAB
0x000 slab_t slab_t
0
FREE
CHUNK CHUNK
CHUNK CHUNK
FREE
CHUNK CHUNK
FREE
FREE
FREE
0xFFF ... ...
F

## Slide 14

## Data COW

```
g_val = 1;
pid_t child =fork();
if (child == 0)
  g_val = 5;  // parent sees g_val
as 1
```

```
#include <stdio.h>
int g_val = 5;
void main() {
printf("%d\n", g_val);
}
```

Address **`0x000`** Space **`0`** __TEXT **`0x800 0`** __DATA

`fork()` __TEXT __DATA

```
4f8 <_main>:
// ...
```

```
     510: 90000048     adrp    x8, 0x8000 <_g_val> // PC-relative load of
     514: b9400108     ldr     w8, [x8]            // g_val value to w8
     518: 910003e9     mov     x9, sp    // load w8 to stack
     51c: f9000128     str     x8, [x9]  // as argument to printf
     520: 90000000     adrp    x0, 0x0// PC-relative load of "%d\n"
     524: 91152000     add     x0, x0, #0x548// ptr to x0 as argument to
printf
```

```
     528: 94000005     bl      0x53c <_printf>  // PC-relative call to GOT'd
printf
```

```
// ...
```

Main optimization:

re-load from disk and memcpy() ONLY writable segs

```
0xFFF
F
```

## Slide 15

## our_Dynamic Linker

```
// linker.h
linker_t *linker_create();
void linker_destroy(linker_t *lnk);
```

```
void *linker_dlopen(
  linker_t *lnk, const char *file, int
flags);
```

```
void linker_dlclose(void *handle);
void *linker_dlsym(
  void *handle, const char *sym);
int linker_duplicate(
  linker_t *dst_linker, linker_t
*src_linker,
  ptrlist_t *pl);
```

- (1) re-loads all libs from disk

(2) memcpy() and fixup writable segs ONLY

```
// tvm.c
```

```
void *emulated_dlsym(const char *file, int flags)
{
```

```
returnlinker_dlsym(current->tsk_lnk, file,
flags);
}
```

```
// but remember...
ssize_t write(int fd, const void *buf, size_t
count) {
  // ...
  returndlsym(RTLD_NEXT, "write")(rfd, buf,
count));
}
pid_t fork() {
  ptrlist_t pl // how programs us our dl=new_ptrlistym and we use real ();
  new_task dlsym ?=task_create();
```

```
// our linker controls elocations!dup_fds_and_sighandlers(new_task,current);*we decide*
arena_duplicate(new_task->tsk_ar, current->tsk_ar,
&pl);
```

```
linker_duplicate(new_task->tsk_lnk, current->tsk_lnk,
&pl);
// ...
fixup(&pl);
```

```
returnnewtask>tskpid;
```

## Slide 16

## our_Dynamic Linker

```
// linker.h
linker_t *linker_create();
void linker_destroy(linker_t *lnk);
```

```
void *linker_dlopen(
  linker_t *lnk, const char *file, int
flags);
```

`void linker_dlclose(void *handle); void *linker_dlsym( void *handle, const char *sym); int linker_duplicate( linker_t *dst_linker, linker_t *src_linker, ptrlist_t       ELF v Mach-O*pl);` Address **`0x000`** Space `PT_LOAD - LC_SEGMENT_64` **`0`** `DT_NEEDED - LC_LOAD_DYLIB` libA.dylib `DT_SONAME - LC_ID_DYLIB DT_SYMTAB - LC_SYMTAB DT_JMPREL - LC_DYSYMTAB` libB.so `DT_REL - LC_DYLD_CHAINED_FIXUPS`

#### `// tvm.c`

```
void *emulated_dlsym(const char *file, int flags)
{
```

```
returnlinker_dlsym(current->tsk_lnk, file,
flags);
```

```
}
```

```
// but remember...
ssize_t write(int fd, const void *buf, size_t
count) {
```

```
  // ...
  returndlsym(RTLD_NEXT, "write")(rfd, buf,
count));
```

```
}
```

```
pid_t fork() {
```

```
  ptrlist_t pl // how programs us our dl=new_ptrlistym and we use real ();
  new_task dlsym ?=task_create();
```

- `// our linker controls elocations!dup_fds_and_sighandle` **`r`** `s(new_task, current);*we decide* arena_duplicate(new_task->tsk_ar, current->tsk_ar,`

- `&pl);`

```
linker_duplicate(new_task->tsk_lnk, current->tsk_lnk,
&pl);
// ...
```

```
fixup(&pl);
```

```
F
```

```
returnnewtask>tskpid;
```

```
0xFFF
```

## Slide 17

## the final piece: callstack!

```
pid_t fork() {
  ptrlist_t pl =new_ptrlist();
  new_task =task_create();
```

```
dup_fds_and_sighandlers(new_task, current);
arena_duplicate(new_task->tsk_ar, current->tsk_ar,
&pl);
```

```
linker_duplicate(new_task->tsk_lnk, current->tsk_lnk,
&pl);
```

```
// ...
fixup(&pl);
return new_task->tsk_pid;
}
```

## Slide 18

## the final piece: callstack!

```
pid_t fork() {
```

```
  ptrlist_t pl =new_ptrlist();
```

```
  new_task =task_create();
```

```
dup_fds_and_sighandlers(new_task, current);
```

```
arena_duplicate(new_task->tsk_ar, current->tsk_ar,
&pl);
```

```
linker_duplicate(new_task->tsk_lnk, current->tsk_lnk,
&pl);
```

```
pthread_create(&p, NULL, thread_entry, new_task);
// ???
```

```
fixup(&pl);
return new_task->tsk_pid;
}
```

```
void thread_entry() {
// ???
}
```

OLD STACK NEW STACK
0x000
0
fork
ret
<parent>
<granny>
?
<ancestor
>
... :(
thread_ent
main
ry
?
pthread_sta
_start
rt
0xFFF
F
add the copied frames to fixups

## Slide 19

## the final piece: callstack!

```
a04 <_func>:
     a04: d10083ff  sub     sp, sp, #0x20
     a08: a9017bfd  stp     x29, x30, [sp, #16]  // push fp
and lr
```

OLD STACK NEW STACK
]  // push fp // push fp  0x000
0
fork fork
ret
<parent> <parent>
<granny> <granny>
<ancestor <ancestor
> >
... ...
main main
pthread_sta
_start
rt
0xFFF
F
gotta "relink" to libc_start manually
_start

```
          // ...
```

fork()
0x00014000 0x0002C000
0000000 0000000
0 fork 0
000145F 0002C 14 5F
0 0
000A5F2 <parent> 000B6 A5 F2
4 4
0000000 0000000
<granny>
0 0
00015A5 0002E 15 A5
0 0
000A454 000B5 A4 54
8 main 8
0000000 0000000
0 0
0x00018000 _start 0x00030000

## Slide 20

## setjmp() with blackjack and hookers

switching
stacks
is easy

## Slide 21

## setjmp() with blackjack and hookers

fork()
OLD STACK NEW STACK
0x000
0
fork fork
<parent> <parent>
<granny> memcpy() <granny>
<ancestor <ancestor
> >
... ...
main main
pthread_sta
_start
rt
0xFFF
F

```
void thread_entry(void *arg) {
  void *fp =
__builtin_frame_address(0);
memcpy(fp-size, arg->parent_sp,
size);
  // ... more setup ...
we can't override our own stack!
}
```

## Slide 22

## setjmp() with blackjack and hookers

fork() longjmp()
OLD STACK NEW STACK TEMP STACK
0x000
0
fork fork
longjmp()
<parent> <parent>
<granny> memcpy() <granny>
<ancestor <ancestor
> >
... ...
main temp framemain temp frame
pthread_sta
_start
rt
0xFFF
F

## Slide 23

## setjmp() with blackjack and hookers

```
#include <stdio.h>
jmp_buf errjmp;
void work_impl() {
while (-1 !=open(“/dev/null”,
O_WRONLY))
    ;
longjmp(errjmp, 1); // error
}
void work() {
  work_impl();
}
void main() {
if (!setjmp(errjmp))
work();
printf(“error\n”);
return1;
}
```

STACK `struct jmp_buf { uint64_t x0; uint64_t x1; // ... uint64_t x28; uint64_t fp;  // x29 longjmp(errjmp) uint64_t lr;  // x30` work_impl `uint64_t sp;  // not rly x31` work `}; sp setjmp(errjmp)` main _start

## Slide 24

## setjmp() with blackjack and hookers

fork() longjmp()
OLD STACK NEW STACK arg->tmpstack
0x000
0
fork
<parent>
<granny>
<ancestor
>
...
thread_entr thread_entr
main
y y
pthread_sta
_start
rt
0xFFF
F
sp
fp
tmp_jmpbuf

```
void thread_entry(void *arg) {
  uint64_t tmpfp, tmpsp, currsp, reg;
  currfp = __builtin_frame_address(0);
if (!setjmp(arg->tmp_jmpbuf)) {
// switch to arg->tmpstack using arg-
>tmp_jmpbuf
    currsp = arg->tmp_jmpbuf[SP];
    arg->tmpstack = mmap(STACKSIZE);
// fp is first 16 bytes pushed to stack
    tmpfp = (long)arg->tmpstack+STACKSIZE–16;
    tmpsp = tmpfp – (currfp – currsp);
// copy current frame to temp stack
memcpy(tmpsp, currsp, currfp-currsp);
// fixup jmp_buf to pointers to temp stack
for (int i = 0; i <JMPBUF_CNT; i++) {
      reg = arg->tmp_jmpbuf[i];
if (reg >= currsp && reg < currfp)
        arg->tmp_jmpbuf[i] -= currsp – tmpsp;
    }
// switch to temp stack via jmpbuf
longjmp(arg->tmp_jmpbuf, 1);
  }
```

```
// code running on temporary stack
thread_entry_cont(arg);
}
```

## Slide 25

## putting it all together

##### Address Space

libtvm.dylib
fork()
mksh
0000000 0000000
mksh 0 0
0000000 0000000
0 0
0000000 0000000
heap
0 0
7461687 7461687
heap 7 7
3F70757 3F70757
3 3
stack 0000000 0000000
0 0
000145C 000 142C 5C
stack
C C
0000000 0000000
tmp stack
0 0
set fixup() also fixes 00014FF 000 142C FF
arg,  final_jmpbuf:E E
new_task - sp, fp to new stack0001400 000 142C 00
- lr to new text seg8 8
0000000 0000000
0 0
0000000 0000000

```
pid_t fork() {
  arg_t *arg =create_arg_with_new_ptrlist();
  arg->new_task =task_create_inherit_sig_fds(current);
  arg->old_task = current;
if (setjmp(arg->final_jmpbuf)) {
```

```
    current = arg->new_task;  // setup child’s thread_local current
pthread_cond_signal(arg->cond);  // signal parent to exit
return0;
```

```
  }
pthread_create(,, tvm_entry, arg);
pthread_cond_wait(arg->cond);  // wait for child to copy from our
stack
```

```
  return arg->new_task->tsk_pid;
}
```

```
void tvm_entry(arg_t *arg) {
if (!setjmp(arg->tmp_jmpbuf)) {
// ... setup temp stack and tmp_jmpbuf
longjmp(arg->jmp_jmpbuf);
  }
```

```
// running on temporary stack!
```

```
arena_duplicate(arg->new_task->tsk_ar, arg->old_task->tsk_ar,
&pl);
linker_duplicate(arg->new_task->tsk_lnk, arg->old_task->tsk_lnk,
&pl);
```

```
stack_duplicate(, &pl);
add_jmpbuf_to_fixups(arg->final_jmpbuf);
// every duplicated memory is loaded to &pl, now fixup!
  fixup(&pl);
lj(filjbf)
```

## Slide 26

### what else ?

- execve()

   - completely re-implement in userspace

      - load dynamically

      - call “main” directly instead of “_start” • we implement crt ourselves

- TTY/PTY & Job Control

   - completely re-implement in userspace

      - setsid(), setpgid(), openpty(), etc etc

      - implement “raw-mode” in userspace

      - userspace “character device”

- Thread Local Storage

   - Our linker needs to implement it

   - We don’t link via system’s linker

## Slide 27

## Code Signing

```
#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
void main() {
  int fd =open(“a.out”, O_RDONLYloadsig);(fd)
mmap(;
NULL, 0, PROT_READ | PROT_EXEC,
MAP_PRIVATE, fd, 0);
  return0;
SIGKILL /
}
EPERM
```

```
void loadsig(int fd) {
  fsignatures_t si = {...};
  int fd =fcntl(fd, F_ADDFILESIGS,
&si);
}
```

```
Can’t map unsigned code
```

## Slide 28

## Code Signing

```
#include <stdio.h>
#include <sys/mman.h>
#include <fcntl.h>
void main() {
  int fd =open(“a.out”, O_RDONLY);
mmap(
NULL, 0, PROT_READ | PROT_EXEC,
MAP_PRIVATE, fd, 0);
  return0;
}
```

## Slide 29

## unicorn

• lets just use an
emulator bro execution of work() is *emulated*:
- work() instructions can be READ-
only
STACK
- both real and emulated CPUs
operate on the same stack (LOL!)
uc_impl_*
uc_emu_sta nullify emulated MMU!
- emulated CPU “sees” host
rt
memory
emulated
stack
work
sp setjmp(jbemu
main )sp
_start

```
#include <unicorn/unicorn.h>
#include <setjmp.h>
int main() {
// save context for emulated work
  jmp_buf jb;
if (setjmp(jb))
returnwork();
```

```
// setup emulator
  uc_engine *uc;
uc_open(UC_ARCH_ARM64, UC_MODE_ARM, &uc);
uc_mem_map_ptr(
```

```
    uc, 0x4000, 0xFFFFFFFFFFFF8000,
UC_PROT_ALL, 0x4000);
```

```
  uc_reg_write(uc, UC_ARM64_REG_SP, jb[SP]);
  uc_reg_write(uc, UC_ARM64_REG_FP, jb[FP]);
uc_reg_write(uc, UC_ARM64_REG_X0, jb[X0]);
// ...
```

```
uc_reg_write(uc, UC_ARM64_REG_X28,
jb[X28]);
```

```
// start emulation
alloca(0x8000);
returnuc_emu_start(uc, jb[LR], 0, 0, 0);
}
```

## Slide 30

my_Dynamic Linker

// a.out
Address  int main() {
0x000 Space - printf(“Hello, World!\n”);
iOS bloat  (Info.plist, app.m)
0 app  -
TVM        (our_heap, our_linker, our_<every  return 0;
__TEXT
syscall>) }
ssh  - unicorn
__TEXT - dropbear   (open-source ssh server)
sh __TEXT - unsigned -> NO PROT_EXEC
- ssh mobile@<iphone> ./a.out
a.out
switch between real CPU and emulated CPU when
__TEXT possible ?
?
DSC  - libSystem  (memcpy, printf, socket, ...)
- EE         (everything else)
__TEXT
0xFFF
F

## Slide 31

## going hybrid

// app
int main() {
execve(“./a.out”);
Address  return 0;
REAL |  Space }
EMU
R-X  app  pc // tvm
| __TEXT
int execve(char *path) {
// map segs as READ
a.out
R--  pc emu_call(pc, argc,
| __TEXT argv);
dylib
R--  }
__TEXT
|
DSC
R-X
| __TEXT

#### `#include <unicorn/unicorn.h>`

```
uint64_t emu_call(uint64_t pc, uint64_t arg1, ...) {
uc_mem_map_ptr(uc, PROT_READ | PROT_WRITE, 0xFF..);
  uint8_t *stack =mmap(PROT_READ | PROT_WRITE,
STACKSIZE);
```

```
uc_reg_write(uc, SP, stack + STACKSIZE);
uc_reg_write(uc, LR, 0xDEADBEEF);
```

```
uc_reg_write(uc, X0, arg1); // ... and all other
```

```
regs
```

```
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF, 0x4000);
while (1) {
```

```
uc_emu_start(uc, pc);
```

```
    pc =uc_reg_read(uc, PC);
if (pc == 0xDEADBEEF)
```

```
returnuc_reg_read(uc, X0);
```

```
if (linker_has_page(pc & ~0x3FFF)) {
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF,
0x4000);
```

```
continue;
    }
```

```
    uint64_t ret = ((func_t)uc_reg_read(uc, PC))(
uc_reg_read(uc, X0), ..., uc_reg_read(X5));
uc_reg_write(uc, X0, ret);
```

```
    pc =uc_reg_read(uc, LR);
```

```
}
```

## Slide 32

## going hybrid

```
#include <unicorn/unicorn.h>
```

detect return with sentinel return
address
Address
REAL |  Space
EMU
R-X R- app  pc
-
| __TEXT
a.out
R-- R- pc
| -X __TEXT
dylib
R-- R-
- __TEXT
|
DSC
R-X R-
| - __TEXT

```
uint64_t emu_call(uint64_t pc, uint64_t arg1, ...) {
uc_mem_map_ptr(uc, PROT_READ | PROT_WRITE, 0xFF..);
  uint8_t *stack =mmap(PROT_READ | PROT_WRITE,
STACKSIZE);
```

```
uc_reg_write(uc, SP, stack + STACKSIZE);
uc_reg_write(uc, LR, 0xDEADBEEF);
```

```
uc_reg_write(uc, X0, arg1); // ... and all other
```

```
regs
```

```
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF, 0x4000);
while (1) {
```

```
uc_emu_start(uc, pc);
```

```
    pc =uc_reg_read(uc, PC);
```

```
if (pc == 0xDEADBEEF)
```

```
returnuc_reg_read(uc, X0);
```

```
if (linker_has_page(pc & ~0x3FFF)) {
```

```
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF,
0x4000);
```

```
continue;
    }
```

```
    uint64_t ret = ((func_t)uc_reg_read(uc, PC))(
uc_reg_read(uc, X0), ..., uc_reg_read(X5));
uc_reg_write(uc, X0, ret);
```

```
    pc =uc_reg_read(uc, LR);
}
```

## Slide 33

## going hybrid

// a.out
int main() {
do_thing();
Address  printf(“goodbye\n”);
REAL |  Space return 0;
EMU
}
R-X R- app  pc
-
| __TEXT
// dylib
void do_thing() {
R-- R- a.out  pc // here be dragons
| X __TEXT return;
dylib
R-- R- }
| -X __TEXT
DSC
R-X R-
| - __TEXT
0xDEADBEE
F

#### `#include <unicorn/unicorn.h>`

```
uint64_t emu_call(uint64_t pc, uint64_t arg1, ...) {
uc_mem_map_ptr(uc, PROT_READ | PROT_WRITE, 0xFF..);
  uint8_t *stack =mmap(PROT_READ | PROT_WRITE,
STACKSIZE);
```

```
uc_reg_write(uc, SP, stack + STACKSIZE);
uc_reg_write(uc, LR, 0xDEADBEEF);
```

```
uc_reg_write(uc, X0, arg1); // ... and all other
```

```
regs
```

```
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF, 0x4000);
while (1) {
```

```
uc_emu_start(uc, pc);
```

```
    pc =uc_reg_read(uc, PC);
```

```
if (pc == 0xDEADBEEF)
```

```
returnuc_reg_read(uc, X0);
```

```
if (linker_has_page(pc & ~0x3FFF)) {
uc_mem_map_ptr(uc, PROT_ALL, pc & ~0x3FFF,
0x4000);
```

```
continue;
    }
```

```
    uint64_t ret = ((func_t)uc_reg_read(uc, PC))(
uc_reg_read(uc, X0), ..., uc_reg_read(X5));
uc_reg_write(uc, X0, ret);
    pc =uc_reg_read(uc, LR);
```

```
}
```

## Slide 34

### what else ?

- dlclose()

   - unmap segs from emulator MMU

- handle func ptrs passed to native

   - sigaction()

   - qsort() / bsearch()

   - CFDictionaryApplyFunction()

- winning race conditions

   - faster emulator

      - skill issue

   - code sign the racy parts

      - beats the purpose

   - dispatch_async_f()

## Slide 35

# DEMO

and then questions!
