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
text_chars: 15935
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.9
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:02:41Z"
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


> Recovered by OCR — confidence 75/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSekhat What is NLB?
' Client |
! nee NLB virtual IP NLB Host
| Client |
I Request
| ! NetWork we Dedicated IP
Dedicated IP
Information Classification: General 1
```

## Slide 5

## NLB Modules

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cluster host
Server application nlbmgr.exe
Ov5erating system kernel
Network loading Balancing driver Grlb.sys)
" a Network Load Balancing Manager _
hte es Network adapter driver Network adapter driver
ce Network adapterver a Network adapter
@ nibmgr.exe t o
nlbmprov.dil t t a
```

## Slide 6

## Heartbeat Mechanism

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSekhat Heartbeat Mechanism
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


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Heartbeat Mechanism
NLB heartbeat packet processing flow
NLBCoreReceivePacket
NLBCoreReceiveHeartbeat
ID : @xC@DEO1BF ID : @xC@DE@1DE
NLBCoreReceiveMembershipHeartbeat NLBCoreReceiveIdentityHeartbeat NLBCoreReceiveNRProtocolData
Convergence | | NLBIPList IdentityCache
```

## Slide 8

# Case Studies

#BHEU @BlackHatEvents

## Slide 9

#### Case Study 1: OOB R&W by Evil HostID

\```
/* Identity cache */
MAIN_IDENTITY identity_cache[32];
\```

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

#### Case Study 1: OOB R&W by Evil HostID

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pikekhat Case Study 1: OOB R&W by Evil HostID
identity_cacheLOI
main_context / | ( \
| IDENTITY
\ eco
HostIDG2) }
f ttl
( DIPEntrylist } -
```

## Slide 11

#### Case Study 1: OOB R&W by Evil HostID

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSekhat Case Study 1: OOB R&W by Evil HostiD
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


> Recovered by OCR — confidence 79/100 on the text kept, 51/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Case Study 1: OOB R&W by Evil HostiD
iopl=0
cs=0010
Resetting default
PROCESS_NAME:
STACK_TEXT:
ffed
scope
jmp
r14=ffffb38b6ef38090 ri5=ffffb38b6e457750
$$=0018 ds=002b es=002b fs=0053 gs=002b
rax {41414141 41414141}
: Ffffb38b"
: 80000000"
: 98000000"
: 00000275
6e457750
d70847e0
6b9f2380
80000000
90000001
80000000"
00000000"
00050213
00001062
09000000
6fbad190
6d586b80
90000001
99000000 00000001
90000800"
89000880 :
6d699800 :
6d699840 :
88000000 :
6fbad190
d7084a49 :
FLTMGR! FltpPerformPreCal lbacksWorker+0x32a6
FLTMGR! FltpPassThrough+0x172
: nt! IofCallDriver+0x65
nt! TopDeleteFile+0x13¢
: ntlobfDereferenceObjectWithTag+Oxc7
00000000 :
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


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Case Study 3: Race condition to UAF in NLBIPList management =
NLBIPListCheckItem
d resource address
if (pNLBIPList->Items && pNLBIPList->HashTable
Items array
Some code to retrieve the BitVector No Lock!
for ( i = HashTable[v14 % @x1F7]; ; ++i access the array
BitVector array
f (Items[ xxx type_ip )
HashTable array
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


> Recovered by OCR — confidence 78/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
blackhat Case Study 4: Race condition to DoS by NRProtocol :
Raw args Funcinfo Source Addrs Headings Nonvolatile regs Frame nums Sa
nt |! KeBugCheckEx
nt! KeAcquireSpinLockAtDpcLevel+0xd - \ }
NLB! NLBCoreNRProtocolStartSending+0x73
NLB! NLBCoreLoadProcessHeartbeat+0xf 89
NLB! NLBCoreReceiveMembershipHeartbeat+0x1lfb
NLB! NLBCoreReceivePacket+0x14b
NDIS!ndisCallReceiveHandler+0xb9 ; inté4 — fastcall NLBCoreNRProtocolStartSendi int64 al, _ int64 a2, int
NDIS!ndisCallNextDatapathHandler<2,void * _ptr64 & __ptr64.v F
NDIS!ndisIterativeDPInvokeHandlerOnTracker<2,void __cdecl(voi
NDIS! ndisInvokeNext ReceiveHandler+0xa6
NDIS! NdisMIndicateReceiveNetBuf ferLists+0x116
21168x64!RECEIVE: :RxProcessInterrupts+0x1f3
CUSTOMER_CRASH_COUNT 1
PROCESS_NAME: System
TRAP_FRAME f£££££8007d9937d0 —— ( trap Oxfffff£8007d9937d6
NOTE: The trap frame does not contain all registers
Some register values may be zeroed or incorrect
rax=0000000000000000 rbx=0000000000000000 rex=0000000000000068
rdx=fff£f££9007d993b58 rsi=0000000000000000 rdi=0000000000000000
ril=fff£££8007d9939b0 r12=0000000000000000 r13=0000000000000000
r14=0000000000000000 r1S=0000000000000000
nt ! KeAcquireSpinLockAtDpcLevel+0xd:
fffff800° 7dfa8d2d £0480fba2900 lock bts qword ptr [rex].0 ds: 00000000° 00000068=?777727727272272727222?
Resetting default scope
STACK_TEXT
```

## Slide 26

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
+ 0x28) - d/ >= )// Expansion check: calculate
Jhether the currently available space is sufficient
if ( {3+ > ad) Expansion expansion
= NLBVectorReserve(al, + awalys_1);
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
```

## Slide 27

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
UINT NewSize; // e
unsigned int v3; //
53 //
size_t v6; //
NLB Host NLB Host __int64 v7; //
——— int v10; // 3
int vil; // [rsp+3
char *v13; //
int64 v14; // +
PVOID VirtualAddress; // [ ll 10h] BYR
= *(_DWORD *)(vector + @x1@) * t;// Vector->ElementSize * NewCount
1 if ( *(_DWORD *)( + 0x28) - *(_DWORD *)( + 0x18) < )
{
wee tua ess = @164;
i] (&Vi > » ' BLN');// Memory will not be released
NLBVectorSwap( » V9)5
}
}
```

## Slide 28

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisek hat Case Study 5: Moderate Severity but Unauth DoS .
& Attacker
NRPPacket
#pragma pack(push, 1)
typedef struct _NRP_PACKET
t
unsigned long Magic;
unsigned char Funcld; \
unsigned long unk1;
unsigned char Type; f
unsigned char Index; J
unsigned char TestBit; ,
unsigned short unk2; |
unsigned long ExtendLen;
#pragma pack(pop)
J
```

## Slide 29

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisek hat Case Study 5: Moderate Severity but Unauth DoS
& Attacker
#pragma pack(push, 1) ©
typedef struct _NRP_PACKET
unsigned long Magic;
unsigned long unk1i;
unsigned char lestbit;
unsigned short unk2; NLBCoreRec
unsigned long ExtendLen;
#pragma pack(pop)
NLBCoreReceiveMembe
Magi
NLBCoreNRProtocolReceiveAck(al, 18,
NLBCoreNRProtocolReceiveIPv4Remove(al,
T)&WPP_GLOBAL_Control HIDWORD(WPP_GLOBAL_Control
```

## Slide 30

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
- ~
ak NRPPacket
i#pragma pack(push,1)
itypedef struct _NRP_PACKET
unsigned long ExtendLen; //+@xe The length of the following part has different meanings depending on the FunclId
NRP_PACKET , *PNRP_PACKET ;
}
'
'
unsigned char Type; //+®x9 Fixed to 2, otherwise calling NLBCoreExceptionListGetBucketOwnership will fail
unsigned long Magic; //+@x® Fixed to @xBEEF
1 unsigned char FuncId; //+@x4 1 -- Ack 2 -- IPv4Add 3 -- IPv4Remove 4 -- IPv6Add 5 -- IPv6Remove
| unsigned long unk1; //+x5
; unsigned char Index; //+@xa HostID,less than 32,The size of each element in the array corresponding to this subscript value is Qx5E@,
;see NLBCoreExceptionListGetBucketOwnership
' unsigned char TestBit; //+Oxb
unsigned short unk2; //+Oxc
```

## Slide 31

##### Case Study 5: Moderate Severity but Unauth DoS

Information Classification: General

#BHEU @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Case Study 5: Moderate Severity but Unauth DoS
kd> p
kd> p
If fFFF803° 9a56343F 48217510
kd> p
LBINLBVectorReserve+0x37:
If fFFF803° 9a563443 488d4d10
kd> p
kd> p
LBINLBVectorReserve+0x43:
kd> p
kd> r rax
kd> g
reakpoint @ hit
LB!NLBVectorReserve+0x4a:
a: kd> r rax
[SC-CLIENT] !! Service timeout: Service StorSvc, PID 0x00000410, OpCode 0x0e000010, pel
jae
and
lea
mov
mov
call
nop
nop
qword ptr [rbp+10h],rsi
rex, [rbp+10h]
r8d,20424C4Eh
edx,ebx
qword ptr [NLB!_imp NdisAllocateMemoryWithTag]
dword ptr [rax+rax]
dword ptr [rax+rax]
[SC-CLIENT] !! Service timeout: Service wemsvc, PID 0x00000718, OpCode @x00000010, Time
[eusy* Debuggee not_connected
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
PROCESS_NAME: System
STACK_TEXT
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
