---
title: "Dive into Apple UserFS (Userspace Filesystem)"
speakers: ["Zuozhi Fan"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zuozhi Fan_Dive into Apple UserFS (Userspace Filesystem).pdf"
pages: 43
sha256: "0fdf93ad6a2fe517dcdbd2ead0961d025bce8cfb70b7ac1d01f63587ecbe8a70"
text_chars: 16558
ocr_pages: 11
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:28:25Z"
---
# Dive into Apple UserFS (Userspace Filesystem)

**Speakers:** Zuozhi Fan  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zuozhi Fan_Dive into Apple UserFS (Userspace Filesystem).pdf` (43 pages)

## Slide 1

# Dive into Apple UserFS (Userspace Filesystem)

pattern-f (@pattern_F_) Ant Security Light-Year Lab

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pISek hat
AUGUST 9-10, 2025
BRIEFINGS
Dive into Apple UserFS
(Userspace Filesystem)
pattern-f (@pattern_F_)
Ant Security Light-Year Lab
#BHUSA @BlackHatEvents
```

## Slide 2

### About me

- pattern-f (@pattern_F_) on Twitter

- • Security researcher of Ant Security Light-Year Lab • Focus on iOS & macOS security

- speaker of Black Hat ASIA & USA 2021

#BHUSA  @BlackHatEvents

## Slide 3

### Background

- my previous talk at Black Hat ASIA 2021

- Shared a vulnerability named xattr-oob-swap (CVE-2020-27904) <u>[link]</u>

- • It’s a filesystem bug, can get tfp0 on macOS 10.15.x and below. • iOS & macOS share code base, it should work on iOS too, but…

#BHUSA  @BlackHatEvents

## Slide 4

### Background

- It doesn’t crash iOS. Maybe UserFS stops it.

- • I don’t know the mechanism of UserFS, so I’m not sure.

#BHUSA  @BlackHatEvents

## Slide 5

### Background

• This vulnerability doesn’t affect iOS, really? • Add it to TODO list

#BHUSA  @BlackHatEvents

## Slide 6

### Background

• This vulnerability doe ~~sn’t~~ affect iOS, ~~really?~~ • ~~Add it to TODO list~~

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bike hat Background
USA 2&0e3
¢ This vulnerability doesA+ affect iOS, reath-
File System
Available for: iPhone 6s (all models), iPhone 7 (all models), iPhone SE (1st generation), iPad Pro (all
models), iPad Air 2 and later, iPad 5th generation and later, iPad mini 4 and later, and iPod touch (7th
generation)
Impact: An app may be able to break out of its sandbox
Description: This issue was addressed with improved checks.
CVE-2022-42861: pattern-f (@pattern_F_) of Ant Security Light-Year Lab
```

## Slide 7

### What is UserFS

#### • We know that

- iPhone User Guide said: An external storage device must have only a single data partition, and it must be formatted as APFS, APFS (encrypted), macOS Extended (HFS+), exFAT (FAT64), FAT32, or FAT.

#BHUSA  @BlackHatEvents

## Slide 8

### What is UserFS

- iOS supports various file system

- But when analyzing the iOS kernel cache, I found only apfs & hfs support were present.

- No msdos.kext (fat32, exfat) at all

#BHUSA  @BlackHatEvents

## Slide 9

### What is UserFS

- Instead, apple implement them in user space, called UserFS plugins.

- • But the plugins are not all about UserFS.

#BHUSA  @BlackHatEvents

## Slide 10

### What is UserFS

#### • UserFS is filesystem implemented in user space, with these components.

• `kext, daemon, XPC service, PlugIn, and framework`

userspace daemons XPC service UserFS PlugIns
apfs.dylib
livefileproviderd
  UVFSService exfat.dylib
userfsd
app
msdos.dylib
LiveFS.framework
hfs.dylib
kernel
lifs.kext

#BHUSA  @BlackHatEvents

## Slide 11

### What is UserFS

• UserFS only functions with external storage devices, so let’s started with connecting an external hard drive to iPhone.

#BHUSA  @BlackHatEvents

## Slide 12

### When connecting a USB drive to iPhone

#### • launchd registers a LaunchEvent “usb.device.attached” for userfsd

#BHUSA  @BlackHatEvents

## Slide 13

### When connecting a USB drive to iPhone

#### • userfsd daemon starts and handles this IOKit notification • Make a xpc call to UVFSService

/dev/disk3

#BHUSA  @BlackHatEvents

## Slide 14

### When connecting a USB drive to iPhone

#### • Enumerate UserFS plugins and determine filesystem type of the disk.

- xpc call again, to livefileproviderd.

#BHUSA  @BlackHatEvents

## Slide 15

### When connecting a USB drive to iPhone

#### • familiar command “/sbin/mount”, mount_lifs this time.

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pigeuchat When connecting a USB drive to iPhone <4
USA 2&0e3
¢ familiar command “/sbin/mount’, mount_lifs this time.
-[lifeFilesFPNFSDMounter LiveMounterMountVolume:displayName: provider: domainError:on:how:reply: ]
{
-[lifeFilesFPNFSDMounter LiveMounterReallyMountVolume:displayName: provider: domainError:on:how:reply:]
-[mountEntry mount:] {
posix_spawn(&pid, "/sbin/mount_lifs", actions, attr, { "/sbin/mount_lifs", ... }, environ)
}
}
}
/sbin/|mount_lifs
{
mount("lifs", dir, flags, data) {
lifs.kext lifs_mount(...)
}
```

## Slide 16

### When connecting a USB drive to iPhone

- Finally, we can access files on this exFAT formatted USB hard drive.

- • /var/mobile/Library/LiveFiles/ is a dedicated directory.

#BHUSA  @BlackHatEvents

## Slide 17

### When connecting a USB drive to iPhone

#### • Summary: process of mounting a UserFS volume

userspace daemons XPC service UserFS PlugIns
apfs.dylib
livefileproviderd
  UVFSService exfat.dylib
userfsd
app
msdos.dylib
LiveFS.framework
hfs.dylib
kernel
usb.device.attached lifs.kext

#BHUSA  @BlackHatEvents

## Slide 18

### When accessing files via UserFS

- To read a file: `int fd = open(path, O_RDONLY); read(fd, …);`

- • We know that SYS_open will be dispatched to vnop_open

#BHUSA  @BlackHatEvents

## Slide 19

### When accessing files via UserFS

• Accessing files via UserFS is same, except that SYS_open will be dispatched to lifs.kext`lifs_vnop_open

#BHUSA  @BlackHatEvents

## Slide 20

### When accessing files via UserFS

#### • vnop_open will build a mach message and send it to a server.

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
USA 20253
S$
¢ vnop_open will build a mach message and send it to a server.
int lifs_open_request(lifsmount *li_mount, void *fsnode, void *a3)
{
get_lifs_port(&svr_port);
req.request_id = OSAddAtomic64(1LL, &lifs_request_id);
// ... Copy params to request
lifs_add_req(&req);
ret = lifs_open_send(svr_port, req.request_id, fsnode, a3); {
struct { mach_msg_header_t msgHdr; } openRequest;
openRequest.msgHdr.msgh_id = @x2A5;
mach_msg_send_from_kernel_proper(&openRequest.msgHdr, sizeof(openRequest) );
}
if ( ret ==-@) {
lifs_wait_req_completion(&req) ;
ret = req.retcode_2C;
lifs_remove_req(&req);
return ret;
```

## Slide 21

### When accessing files via UserFS

• Find handler for the open request. • livefileproviderd registers a notification port. That’s the server port.

#BHUSA  @BlackHatEvents

## Slide 22

### When accessing files via UserFS

- livefileproviderd starts a mig server.

IOConnectCallStructMethod

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ij
2)
blackhat When accessing files via UserFS: e ‘Ss
USA 20253
¢ livefileproviderd starts a mig server.
livefileproviderd main()
{
source = dispatch_source_create(DISPATCH_SOURCE_TYPE_MACH_RECV, svr_port, ...);
dispatch_source_set_event_handler(source, *{
dispatch_mig_server(source, 2168, mig_message_dispatcher) ;
4);
} openRequest.msgHdr.msgh_id = @x2A5;
void *mig_lifs_open“send(void *InHeadP, void *xOutHeadP)
{
lifs_open_send(request_id, fsnode, mode, token) {
fileHandle = m_resolve_fsnode(fsnode, &a2, &mountEntry, &a4, @);
id fsObj = [mountEntry fsObjwWithErrorHandler:];
objc_msgSend(fsObj, "LIOpen:withMode:forPID:reply:", fileHandle, mode, pid, ‘(int ret){
int selector = 2;
lifs_send_reply(request_id, ret, selector, (__int64)&v2, 16LL) {
objc_msgSend(1li_UserClient, "callStructMethod:inStruct:inSize:outStruct:outStructSize:");
}
});
( lOConnectCallStructMethod )
```

## Slide 23

### When accessing files via UserFS

- `-[LiveFSUserClient callStructMethod:inStruct:inSize:outStruct:outStructSize:]`

#BHUSA  @BlackHatEvents

## Slide 24

### When accessing files via UserFS

lifs_request_done(…)

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ij
pigeichat When accessing files via UserFS: e ‘Ss
USA 20253
int lifs_open_request(lifsmount *li_mount, void *fsnode, void x*a3)
{
get_lifs_port(&svr_port);
OSAddAtomic64(1LL, &lifs_request_id);
req.request_id
//
lifs_add_req(&req);
ret = lifs_open_send(svr_port, req.request_id, fsnode, a3); {
struct { mach_msg_header_t msgHdr; } openRequest;
openRequest.msgHdr.msgh_id = @x2A5;
mach_msg_send_from_kernel_proper(&openRequest.msgHdr, sizeof(openRequest) );
}
lifs_wait_req_completion(&req) ; int fd = open(path, O_RDONLY);
ret = req.retcode_2C;
}
lifs_remove_req(&req);
return ret;
```

## Slide 25

### When accessing files via UserFS

#### • summarize control flow of “open” syscall

userspace daemons XPC service UserFS PlugIns
apfs.dylib
livefileproviderd
  UVFSService exfat.dylib
userfsd
app
msdos.dylib
LiveFS.framework
hfs.dylib
kernel
lifs.kext
Userfs Volume
/…/LiveFiles/…/abc.txt
#BHUSA  @BlackHatEvents

#BHUSA  @BlackHatEvents

## Slide 26

### When accessing files via UserFS

• livefileproviderd

• LiveFS.framework

#### • UVFSService

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
USA 2&0e3
e livefileproviderd obj c_msgSend( , “LIOpen:withMode: forPID:reply:", , , , & );
void __cdecl —[LiveFSServiceConnection LIOpkn:withMode: forPID: reply: ] (
LiveFSServiceConnection xself,
SEL a2,
id a3,
int a4,
¢ LiveFS.framework int a5,
id a6)
—>mount,
eimai aD a he EI
off=8; NSFileProviderLiveItemImplementation x
«(_ QWORD x) &aay
¢ UVFSService
void __cdecl -[liveFSVolume LIOpen:withMode: forPID:reply:](liveFSVolume *self, SEL a2, id
£
```

## Slide 27

### When accessing files via UserFS

#### • UVFSService

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e3
¢ UVFSService
void -[liveFSVolume LILookup:name:forClient:reply: ] (
liveFSVolume *self, SEL a2, id fileHandle, id nameStr, unsigned client, id reply_b)
{
fileNode -[liveFSVolume getNodeForFH:fileHandle withError:error];
[fileNode lookup:nameStr withResultingNode:&resultNode]; {
self- £FsOps- ->fsops_ lookup} self- >_UVFSNode, [nameStr UTF8String], &uvfsNode);
fileNode = [[liveFSNode alloc] initWithVolume:self—>volume
andParent: self
andName:nameStr
andUVFSNode:uvfsNode];
*resultNode = fileNode;
}
resultFileHandle = [resultNode getFH];
attrData [resultNode getAttrData];
reply_b(retcode, resultFileHandle, attrData);
v@id _ cdecl -[liveFSVolume LIOpen:withMode: forPID:reply:] (liveFSVolume «self, SEL a2, id
£
```

## Slide 28

### When accessing files via UserFS

- UserFS.framework/PlugIns/livefiles_exfat.dylib will do the real job.

- • Parse /dev/disk3s1 as a normal file (or disk image), execute exfat file read/write request.

- Functions exported by exfat.dylib:

#BHUSA  @BlackHatEvents

## Slide 29

### When accessing files via UserFS

#### • summarize full control flow of “open” syscall

userspace daemons XPC service UserFS PlugIns
finally
apfs.dylib
livefileproviderd
  UVFSService exfat.dylib
userfsd
app
msdos.dylib
LiveFS.framework
hfs.dylib
kernel
lifs.kext
Userfs Volume
/…/LiveFiles/…/abc.txt
#BHUSA  @BlackHatEvents

#BHUSA  @BlackHatEvents

## Slide 30

### Real world vulnerabilities - 1

- Vulnerable code (CVE-2020-27904), kernel FS

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
¢ Vulnerable code (CVE-2020-27904), kernel FS
; , T 1 AppleDouble Header File layout:
check_and_swap_attrhdr(attr_header_t *ah, attr_info_t *ainfop) lin ste eee a
{ * .-- AD ENTRY[@] Finder Info Entry (must be fir
/x * .--+-- AD ENTRY[1] Fork Entry (must be 1
; . foe . * | ‘=> FINDER INFO
* Make sure each of the attr_entry_t's fits within total_size. * | IIITITITIIIIL. Fixed Size Data (32 bytes)
*/ * | EXT ATTR HDR
buf_end = ainfop->rawdata + ah->total_size; * | tae et
* ae.
count = ah->num_attrs; i | ATTR ENTRY[1] —-+--
ae = (attr_entry_t x*)(&ah[1]); * | ATTR ENTRY[2] --+--+--.
or (i = 6: i < count: i++) { * | __ATTR ENTRY[N] --+--+--+--.
/* Make sure the fixed-size part of this attr_entry_t fits. */ * | JIT 1; |
1 EINVAL; “™) ATTR DATA 2 <------- rif
} * | IIIT |
/*x Make sure the attribute content fits. x*/ : 7 sel PHT P TIN ——__ .
end = ae->offset + ae->length; * | Attribute Free Space
if((end < ae->offset || end > ah->total_size) ){
return EINVAL;
}
ae = ATTR_NEXT(ae);
}
}
MUST: ah->data_start <= attr entry offset <= ah->total_size #BHASIA OBLACKHATEVENTS
```

## Slide 31

### Real world vulnerabilities - 1

- The vulnerability is about xattr (Extended File Attributes).

- • exfat filesystem doesn’t support xattr. • XNU provides a compatible layer, the vulnerable code exists in compatible code. • The logic is similar in UserFS, but the code is completely rewritten.

#BHUSA  @BlackHatEvents

## Slide 32

### Real world vulnerabilities - 1

• UserFS version of CVE-2020-27904, i.e., CVE-2022-42861 • The rewritten code is LiveFS`-[LiveFSAppleDouble loadAttrHeader]

#BHUSA  @BlackHatEvents

## Slide 33

### Real world vulnerabilities - 1

- This kernel bug impacts iOS too, but only the UserFS code is affected.

- • The UserFS one still exists on iOS < 16.2 & 15.7.2 • It didn't get fixed until I reported it again. • root cause of CVE-2022-42861: the bug-fix of UserFS lost synchronization kernel FS

with

#BHUSA  @BlackHatEvents

## Slide 34

### Real world vulnerabilities - 2

#### • While studying UserFS, I found another xattr bug in kernel FS.

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— ¥
XS
q
pifekhat Real world vulnerabilities
USA 2&0e3
¢ While studying UserFS, | found another xattr bug in kernel FS.
+++ b/bsd/vfs/vfs_xattr.c
get_xattrinfoCvnode_t xvp, int setting, attr_info_t *ainfop, vfs_context_t conte
delta, context);
writesize = sizeofCattr_header_t);
} else {
- /* Create a new, empty resource fork. */
rsrcfork_header_t *rsrcforkhdr;
offset
vnode_setsize(xvp, filehdr->entries[1].offset + delta, 0, context);
```

## Slide 35

### Real world vulnerabilities - 2

• I think it is CVE-2022-42842. • The ability of this bug is limited.

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifekhat Real world vulnerabilitie
USA 2&0e3
¢ | think it is CVE-2022-42842.
¢ The ability of this bug is limited.
Then init_empty_resource_fork will initialize the memory block to some fix values. A partially controlable oob-write
occurs. We can write these bytes beyond the 64KB buffer.
*
For example, we can control that
*(uint8 t *)(buffer + 0x10000) = Oxff;
*(uint16 _t *)(buffer + 0x10000) = Oxffff;
*(uint32_t *)(buffer + 0x10000) = Oxffff1e00;
*(uint64 t *)(buffer + 0x10000) = Oxffff1e001c000000;
```

## Slide 36

### Real world vulnerabilities - 2

• Tales from the iOS/macOS Kernel Trenches - @jaakerblom • With the exploit primitive (kmsg type confusion), I can exploit the kernel FS xattr bug.

#BHUSA  @BlackHatEvents

## Slide 37

### Real world vulnerabilities - 2

• But that primitive was fixed on iOS 15.2, so I can’t exploit this bug easily on macOS >=12.1,>=13.

#BHUSA  @BlackHatEvents

## Slide 38

### Real world vulnerabilities - 2

• Of cause, there is a corresponding UserFS version (no idea of its CVE no.) • LiveFS`-[LiveFSAppleDouble loadADHeader]

#BHUSA  @BlackHatEvents

## Slide 39

### Possible to pwn kernel via UserFS?

- User space oob bugs: The kernel version of them have been proved to be exploitable. So, they are exploitable, in theory. I didn’t try.

- Kernel space race condition bug: It can be converted to kernel UAF. Though it is very hard to write a workable exploit for it, it is exploitable in theory. I didn’t try.

- • Sandbox: App cannot access lifs.kext directly.

- Chain the user space UserFS oob bug with the kernel space lifs UAF? • I think there is a chance to attack kernel via UserFS, at least, in theory (again…).

#BHUSA  @BlackHatEvents

## Slide 40

### The changes in filesystem security model

#### • call stack

   - `kernel FS: SYS_open -> msdos.kext`

- `UserFS: SYS_open -> lifs.kext -> userspace daemons -> exfat.dylib`

- • lifs.kext is simple, just forwards syscall to userspace daemons. • main exploit target

   - `kernel FS: kernel extension`

   - `UserFS: userspace daemons`

- If successfully exploited

   - `kernel FS: kernel read/write`

   - `UserFS: takeover a sandboxed userspace process`

- UserFS will reduce the impact of FS vulnerabilities.

#BHUSA  @BlackHatEvents

## Slide 41

### disadvantages of UserFS

- UserFS is an extra feature. It doesn’t replace (all the) kernel FS.

- Attack surface = kernel FS + UserFS

   - `iOS: only apfs & hfs are kept in kernel`

   - `macOS: all filesystem extensions are reserved in kernel`

- Maintaining two code bases with identical functionality, but it’s hard to keep bug fixes in sync between them.

- • XPC everywhere in UserFS, so, performance?

   - `Compared to CPU, USB disk is too slow. The performance is acceptable.`

#BHUSA  @BlackHatEvents

## Slide 42

### Conclusion

#### • More modules, more bugs.

   - UserFS is an additional feature, kernel FS is still here, thus increasing the attack surface of the filesystem.

- There is a chance to break iOS through UserFS.

- But when accessing files stored on USB disks, only UserFS takes effect. In this case, UserFS can significantly reduce the impact of filesystem vulnerabilities.

- • Overall speaking, I think UserFS is a successful effort by Apple.

#BHUSA  @BlackHatEvents

## Slide 43

## Thanks!

pattern-f (@pattern_F_)

#BHUSA  @BlackHatEvents
