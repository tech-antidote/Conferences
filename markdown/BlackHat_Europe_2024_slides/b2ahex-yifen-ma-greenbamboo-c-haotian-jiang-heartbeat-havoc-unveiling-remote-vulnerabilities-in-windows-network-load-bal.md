---
title: "Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing"
speakers: ["b2ahex", "Yifen Ma", "Greenbamboo C", "Haotian Jiang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/b2ahex & Yifen Ma & Greenbamboo C & Haotian Jiang_Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing_wp.pdf"
pages: 22
sha256: "4558d442ee37e44fbcdf98a9b3e81db19e1e71eb187b8bf6c99ce384f630f824"
text_chars: 23815
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:48:04Z"
---
# Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing

**Speakers:** b2ahex, Yifen Ma, Greenbamboo C, Haotian Jiang  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/b2ahex & Yifen Ma & Greenbamboo C & Haotian Jiang_Heartbeat Havoc Unveiling Remote Vulnerabilities in Windows Network Load Balancing_wp.pdf` (22 pages)


## Slide 1

# Heartbeat Havoc: Unveiling Remote Vulnerabilities in

# Windows Network Load Balancing

By RyeLv(@b2ahex), Greenbamboom

# Abstract

This paper unveils various zero-click vulnerabilities in Windows Network Load Balancing (NLB), which could significantly impact system availability and security. These vulnerabilities potentially enable attackers to conduct dangerous activities such as remote code execution (RCE), denial-of-service (DoS), information disclosure, and memory leaks. We conducted an in-depth reverse engineering of the NLB heartbeat protocol, successfully identifying these vulnerabilities and reporting them to MSRC. They were subsequently merged into CVE-202328240 and CVE-2023-33163. Additionally, we will show other cases, while not officially recognized, still have the potential to disrupt the stability of NLB services. We look forward to providing a detailed presentation of our findings at this conference.

# 1. Background

## 1.1 NLB Overview

Windows Network Load Balancing (NLB) is a service provided by Microsoft Windows operating systems, designed to enhance the availability and scalability of network services. NLB operates by distributing incoming traffic across multiple servers within a cluster, this allows for the efficient handling of increased traffic loads. Individual servers in an NLB cluster are called hosts, with the capability to accommodate up to 32 hosts in a single cluster.

NLB utilizes predefined rules and load distribution algorithms to determine the appropriate server to handle incoming requests. Additionally, it continuously monitors the health of servers in real-time. In the event of a server failure, NLB automatically redirects incoming requests to other available servers, ensuring uninterrupted service delivery.

NLB is versatile and can be applied to various network services and application scenarios, including web servers, FTP servers, mail servers, and more. Each NLB Host has its own Dedicated IP, which is used for management, and they all share the same Virtual IP for handling client requests. Its straightforward configuration and operation require no additional hardware devices, making it a cost-effective and easy-to-manage solution for load balancing.

## Slide 2

## 1.2 NLB Modules

When we install the NLB feature in Windows, It will add some new files. The main executable you interact with is nlbmgr, which is the NLB Manager. It allows us to configure and manage NLB clusters:

At the kernel level, we have the nlb.sys driver, which is the core component handling the network load balancing process. This driver works closely with the TCP/IP stack to intercept and distribute incoming traffic to the network adapters. Above this layer, we have the server application, which receives traffic routed by NLB. The nlb.sys driver communicates directly with the network adapter drivers, making sure that requests distributed across different hosts based on the NLB configuration.

## 1.3 NLB Heartbeat Mechanism

In Windows Network Load Balancing ,the heartbeat feature and convergence process ensure

## Slide 3

the reliability and high availability of the cluster. Each host sends and receives heartbeat packets to check the online status of other hosts in the cluster. If a host fails to respond within the specified timeframe, NLB treats it as inactive, triggering the convergence process. During convergence, the active hosts redistribute the network load, keeping service continuity and load balancing.

These core functions are mainly handled by the nlb.sys file.

We’ll dive into the nlb code and walk through the process of handling heartbeat packets in NLB.

NLBCoreReceivePacket is the entry point when a heartbeat packet arrives. It receives the packet and passes to NLBCoreReceiveHeartbeat, which is responsible for validating that it's a normal heartbeat message and call different processing functions according to the type of heartbeat packet.

If the heartbeat relates to membership, the NLBCoreReceiveMembershipHeartbeat checks and updates the status of the nodes, ensuring consistency across the cluster. For identity-related heartbeat packets, NLBCoreReceiveIdentityHeartbeat will update IdentityCache and NLBIPList.

if there is any additional protocol data in the heartbeat packet,

NLBCoreReceiveNRProtocolData function parses it to update the cluster's status accordingly.

## Slide 4

# **Case Studies**

## 2.1 Case Study 1: OOB R&W by Evil HostID

In NLB configuration, the Host ID serves as a unique identifier for each host within the cluster. It's typically assigned a value between 0 and 31, as NLB clusters support up to 32 hosts.

When a new host is added to the NLB cluster，the system will send an IdentityHeartbeat packet. The IdentityHeartbeat packets are processed by NLBCoreReceiveIdentityHeartbeat

## Slide 5

The functions NLBCoreReceiveIdentityFQDNPayload and NLBCoreReceiveIdentityDIPPayload will reference the HostID set here to index the IdentityCache

As shown in this diagram, the IdentityCache is an array of 32 entries, each corresponding to a specific HostID. Each HostID has a corresponding DIPEntryList, which contains all the DIP entries associated with that HostID. The DIPEntryList is a linked list, allowing for operations such as add, get DIP entries. NLB uses the DIPEntryList to manage the specific IP addresses of each host in the cluster and utilizes them during load balancing and failover processes:

Let’s imagine a scenario where we make a special heartbeat packet and set its HostID to a

## Slide 6

value greater than 32. So what happens if the HostID Goes beyond this range?

let's check the two core processing functions of the Identity heartbeat packet: NLBCoreReceiveIdentityFQDNPayload and NLBCoreReceiveIdentityDIPPayload

### Trigger by NLBCoreReceiveIdentityFQDNPayload

NLBCoreReceiveIdentityFQDNPayload is to receive FQDNPayload and update it to the global IdentityCache. At this case, we make an NLB heartbeat packet with a HostID of 0x22222222:

As shown in the code, it used directly without validation, this index can fall outside the array's intended bounds, resulting in an out-of-bounds (OOB) write and allows the attacker to overwrite adjacent memory locations with controllable data, as shown in the memmove operation:

```
__int64 NLBCoreReceiveIdentityFQDNPayload(…)
{
pFRAME_HDR = PocData
    HostID =pFRAME_HDR->HostID;     //Parse the HostID, we can control this
    V10 = HostID -1;
    pwszFQDN =pFRAME_HDR->idhb_msg->fqdn     //we can control the pwszFQDN too
    ...
    p_Lock = &pContext->Lock;
if( DispatchLevel )
KeAcquireSpinLockAtDpcLevel(&p_Lock->SpinLock);
else
pContext->Lock.OldIrql=KeAcquireSpinLockRaiseToDpc(&p_Lock->SpinLock);
```

## Slide 7

```
pContext->IdentityCache[v10].HostID= HostID -1;      //OOB
pContext->IdentityCache[v10].ttl=3 * pContext->params.identity_period; //OOB
/*An out-of-bounds write with controllable content */
memmove(&pContext->IdentityCache[v10].fqdn, pwszFQDN, qdn_char*sizeof(WCHAR));
    ...
}
```

So we can achieve the crash in NLBCoreReceiveIdentityFQDNPayload:

### Trigger by NLBCoreIdentityCacheAddDIPEntry

Go back to the beginning of NLBCoreReceiveIdentityHeartbeat, when DataType is equal to 2, NLBCoreReceiveIdentityDIPPayload is called.

This function has the same and references the HostID that has not been safely verified, but the difference is that its reference logic is in a sub-function. Let's check what this function does: it will be parsing the nlb heartbeat packet we send , update the two global tables DIPEntryList and NLBIPList:

```
__int64 __fastcall NLBCoreReceiveIdentityDIPPayload(...)
{
  HostID =*(_DWORD *)(a3 +8);
  v10 =8*(unsignedint)*(unsigned __int8 *)(a4 +1)-10;
  type =*(_WORD *)(a4 +8);
if( type !=23||(unsignedint)v10 >=0x10)// Check the type and length of DIPPayload
{
*(_DWORD *)&dip_addr[16]=0;
*(_OWORD *)dip_addr =0i64;
    v13 =2;
if( type ==2)                            // IPv4
{
*(_DWORD *)&dip_addr[4]=*(_DWORD *)(a4 +10);
*(_QWORD *)&dip_addr[8]=0i64;
*(_DWORD *)&dip_addr[16]=0;
*(_DWORD *)dip_addr =2;
}
else
{
if( type ==23)                         // IPv6
```

## Slide 8

```
{
        v14 =*(_OWORD *)(a4 +10);
*(_DWORD *)dip_addr =3;
*(_OWORD *)&dip_addr[4]= v14;
goto LABEL_12;
}
      v13 =*(_DWORD *)dip_addr;
}
if(!v13 )
{
      v12 =0xC0000001;
goto LABEL_30;
}
```

```
    v15 =NLBCoreIdentityCacheAddDIPEntry(pContext, HostID,&dip_addr, a5);// Initialize the
dip_addr and Update DIPEntryList
```

```
...
// there is another uaf vulnerability, we will explain it in case study 3
NLBIPListAddItemEx(&pContext->DIPList,5,*(int*)v19,&v19[4],0,0i64); // Update NLBIPList
...
```

```
}
```

NLBCoreIdentityCacheAddDIPEntry constructs a DIPEntry based on dip_addr and inserts it into the **IdentityCache[HostID].DIPEntryList** . However, as each HostID has a corresponding DIPEntryList, indexing based on HostID can lead to an Out-of-Bounds (OOB) Read. We modify the POC to enter the NLBCoreIdentityCacheAddDIPEntry and set the HostID to 0x11111111:

### Trigger by NLBCoreIdentityCacheGetDIPEntry

NLBCoreIdentityCacheGetDIPEntry is designed to get a DIPEntry from the IdentityCache based on a given HostID.

So, as expected, the reference to HostID in NLBCoreIdentityCacheGetDIPEntry also suffers from the same vulnerability:

```
__int64 NLBCoreIdentityCacheGetDIPEntry(…int HostID)
```

```
{
```

## Slide 9

```
  ...
if( WPP_GLOBAL_Control !=(PDEVICE_OBJECT)&WPP_GLOBAL_Control &&
(HIDWORD(WPP_GLOBAL_Control->Timer)&8)!=0)
WPP_SF_(WPP_GLOBAL_Control->AttachedDevice,73i64,
&WPP_cbc99019d247383a94b51dd988f41ab3_Traceguids);
  v9 =(KSPIN_LOCK *)(a1 +104);
*(_OWORD *)a4 =0i64;
*(_DWORD *)(a4 +16)=0;
if( a5 )
KeAcquireSpinLockAtDpcLevel(v9);
else
*(_BYTE *)(a1 +112)=KeAcquireSpinLockRaiseToDpc(v9);
  v10 =(_QWORD *)(a1 +536i64*(unsignedint)(HostID -1)+0x2618);  //Controllable HostID
  v11 =(_QWORD *)*v10;    // OOB Read
  ...
}
```

We can also trigger a crash in NLBCoreIdentityCacheGetDIPEntry, causing an out-of-bounds read:

However, in the above some vulnerability triggering paths, We found that there are possible ways to rce here.

For example, in the NLBCoreReceiveIdentityFQDNPayload function, we can control each parameter of the memmove function, maybe we can find a module outside of KCFG and modify the function pointer to control the RIP register like this.

## Slide 10

### Security Checks Removed:  From WLBS to NLB

We found something interesting when study the old WLBS code with the refactored NLB version.

In WLBS, there was a safety check to make sure the HostID not go over 32, but in the new NLB module, that check is missing.

This shows how refactor code can sometimes accidentally leave out important checks, which could create vulnerabilities.

## 2.2 Case Study 2: Integer overflow in TLV_HEADER

This vulnerability occurs within the NLBCoreReceiveIdentityDIPPayload function as previously introduced.

When calculating the length from the TLV_HEADER, the computation is expressed as 8 * (unsigned int)*(unsigned __int8 *)(a4 + 1) – 10, that is: **v10 = 8 * (pTLV->length8) - 10** .

Due to the unsigned calculation here, when pTLV->length8 is less than **2** , it triggers an integer overflow, bypassing the subsequent safety check of **if((unsigned int)v10 >= 0x10)** . Subsequent references to a4 will further trigger an OOB Read: **v14 = *(_OWORD *)(a4 + 10).** `__int64 __fastcall` **`NLBCoreReceiveIdentityDIPPayload`** `(...) { HostID = *(_DWORD *)(a3 + 8); v10 = 8 * (unsigned int)*(unsigned __int8 *)(a4 + 1) - 10;` _`//`_ `integer overflow type = *(_WORD *)(a4 + 8); if ( type != 23 || (unsigned int)v10 >= 0x10 )` _`// bypass 0x10 check`_ `{`

## Slide 11

|`……`
 `if ( type== 23 )`_`// IPv6`_
 `{`
`v14= *(_OWORD*)(a4+ 10);`_`//`_`OOB Read`|
|---|
|`*(_DWORD*)dip_addr= 3;`|

Bugs of this kind are not easy to trigger crashes. Let's observe it from Windbg. NLB!NLBFilterReceiveNetBufferLists is used to receive nlb related packets, with its second parameter(_NET_BUFFER_LIST) being the buffer list of the received packet, The _NET_BUFFER_LIST can be viewed as a linked list where each node represents a buffer for a network packet. Each node contains a pointer to the buffer of the data packet as well as other information related to the packet:

Observe that FirstNetBuffer points to 0xffffc204`9787cf50, and the buffer of the packet is described by mdl. MDL stands for Memory Descriptor List, which is a data structure used in the Windows operating system to describe memory regions.

We observe CurrentMdl, the structure information is as follows, where ByteCount is 0x54, MappedSystemVa is 0xffff99010fd4560a, and the effective range of the buffer is **0xffff99010fd4560a+0x54 = 0xffff9901`0fd4565e** :

## Slide 12

Then triggered the integer overflow and successfully bypassed the length check. The vulnerable code accesses 0x10 bytes out of bounds from the buffer end address ( **0xffff9901`0fd4565e** ):

- 2.3 Case Study 3: Race condition to UAF in NLBIPList management

In Case Study 1, we mentioned that in NLBCoreReceiveIdentityDIPPayload, It will update DIPEntryList and NLBIPList. Now, we will continue to discuss a race condition vulnerability occurring in the NLBIPList management process and how to trigger this race condition to achieve a Use-After-Free (UAF).

When we were examining and evaluating all accesses to the shared resources within the NLB module, we came across this:

## Slide 13

NLBIPListCheckItem will be called in the NLBCoreIOControlQueryFilter function, but there is no lock operation. It will cause problems when items are added or removed elsewhere. Now we just need to find a suitable release point, like **NLBIPListIncreaseSize:**

```
CallStack:
NLBFilterReceiveNetBufferLists
```

- `->NLBCoreReceivePacket`

- `->NLBCoreReceiveHeartbeat`

- `->NLBCoreReceiveIdentityHeartbeat`

- `->NLBCoreReceiveIdentityDIPPayload`

- `->NLBIPListAddItemEx`

- `->NLBIPListIncreaseSize`

Whenever a new IdentityDIPPayload is received, the IP address information will be added to the NLBIPList, and the NLBIPList will dynamically expand the pNLBIPList->Items[] and pNLBIPList->HashTable[] array sizes as the IP address increases. This operation will Causes the original Items and HashTable to be released:

## Slide 14

NLBCoreIOControlQueryFilter inside Use-After-Free crash due to race condition:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
v5 = NdisAllocateMemoryWithTag(&VirtualAddress, 44 * v2, @x2@424C4Eu);
16 = v55
if (Ivo )
{
memset (VirtualAddress, @, 44 * v2);
9 = NdisAllocateMemoryWithTag(&NewBuffer, 2 * (v2 + 503), @x20424C4Eu);
if (v9)
NdisFreeMemory(VirtualAddress, 44 * v2, @);
v7 = WPP_GLOBAL_Control;
if ( WPP_GLOBAL_Control
return v4;
if ( (HIDWORD(WPP_GLOBAL_Control->Timer) & 1) == @ )
goto LABEL_19;
v8 = 21464;
V6 = 95
goto LABEL_10;
(PDEVICE_OBJECT)&WPP_GLOBAL_Control )
memset(NewSuffer, @, 2464 * (unsigned int)(v2 + 5@3))5
for ( i = @; i < *(_DWORD *)(al + 24); *(_DWORD *)&vi1[v13 + 40] = *(_DWORD *)(v13 + vid + 40) )
{
vil = (char *)VirtualAddress;
vi2 = i+;
v13 = 44 * v12;
via = *(_QWORD *)(a1 + 16);
*(_OWORD *)((char *)VirtualAddress + v13) = *(_OWORD *)(v13 + v14);
*(_QWORD *)&v11[v13 + 16] = *(_OWORD *)(v13 + vi4 + 16);
*(_QWORD *)&v11[v13 + 32] = *(_QWORD *)(v13 + vid + 32);
}
NdisFreeMemory(*(PVOID *)(2l + 16), 44 * *(_{
RD *)(al + 28), @);
NdisFreeMemory(*(PVOID *)(al + 1072), 2 * *(_DWORD *)(al + 28) + 1006, 0);
*(_QWORD *)(a1 + 16) = VirtualAddre:
*(_QWORD *)(a1 + 1072) = NewBufffer
*(_DWORD *)(al + 28) = v.
NLBIPListRecomputeHashes(a1) ; : Y reya
Lapel tee Release)old|memory/blocks
v= 4;
goto LABEL_19;
v7 = WPP_GLOBAL_Control;
if ( WPP_GLOBAL_Control == (PDEVICE_OBJECT)&NPP_GLOBAL_Control )
return v45
if ( (HIDWORD(WPP_GLOBAL_Control->Timer) & 1) I= @ )
8 = 20164;
LABEL_10:
WPP_SF_D(v7->AttachedDevice, v8, &hPP_287f06a88e7d39b20c13ced8dd187b41_Traceguids, v6);
+
LABEL_19:
if ( WPP_GLOBAL_Control != (PDEVICE_OBJECT)&WPP_GLOBAL_Control && (HIDNORD(WPP_GLOBAL_Control->Timer) & 8) !
00042358 NLBIPListIncreaseSize:é1 (100042358) (Synchronized with IDA View-A, Hex View-1)
af (22)
{
v9 = *(_QWORD *)(a1 + 16);
Af ( v9 && (v10 = *(_QWORD *)(a1 + 1072)) I= @ )// Get the memory address of the item array
‘ if (a2 == 2)
: {
v1 = *(_DWORD *)a3;
t
' else if ( a2 == 3)
11 = *a3 * a3[4] * 03[8] * 03[42] | ((a3[4] * a3[5] * a3[9] * 03[13] | ((a3[2] * 23[6] * 23[40] * a3[44] | ((a3[3] * a3[7]
' vi2 = vil % @x407;
*(_DWORD *)(21 + 4 * ((unsigned __int64)vi2 >> 5) + 36);
ittest(&v13, v12 & @xiF) )
if/NUBIPListincreaseSize)is\calledjat}this)time;,
: via = *( WORD *)235 the)above)ltemArray/will)be)release}andjthe)following)
; } access)to)ltemArray/will|cause)uaf}
else if ( a2 == 3)
' ; vid = 23 * a3[4] * 03[8] * a3[42] | ((a3[4] * a3[5] * a3[9] * a3[13] | ((a3[2] * a3[6] * 0340] * 3[14] | ((a3[3] * a3
'
else
{
v4 = 0;
if (2-1)
1,
for (i = (unsigned __int16 *)(v10 + 2464 * (v14 % @xIF7)); 3 ++i )// Use the obtained item array
00041D40 NLBIPListCheckItemIndex:19 (1C0041D40)
NLBCorelOControlQueryFilter inside Use-After-Free crash due to race condition:
```

## Slide 15

## 2.4 Case Study 4: Race condition to DoS by NRProtocol

Now that we've seen how race conditions can lead to Use-After-Free (UAF) vulnerabilities in shared esources, let's explore another bug about race conditions but this time, the outcome is a Denial of Service (DoS).

### Trigger by NLBCoreLoadProcessHeartbeat

NRProtocol is an internal protocol within the NLB module, used for communication between nodes in a cluster. ensuring that all nodes maintain a consistent view of the cluster's membership and load information.

While executing the above function, it will read the pLoad->NRProtocol(rcx+0xc9b8) and pass it to NLBCoreNRProtocolStartSending as the first parameter. The value saved by rcx+0xc9b8 is a global shared resource. There is a multi-thread security problem. The NLBCoreLoadProcessHeartbeat function does not acquire the lock when accessing this, which will cause problems in some cases.

The attacker sends Heartbeat packets, making the code execution path:

```
NLBFilterReceiveNetBufferLists
```

- `->NLBCoreReceivePacket`

- `->NLBCoreReceiveHeartbeat`

## Slide 16

- `->NLBCoreReceiveMembershipHeartbeat`

- `->NLBCoreLoadProcessHeartbeat`

As shown by the arrow above, the value read by this instruction is unsafe because there is no lock protection. If thread 1 is executing this instruction, thread 2 is executing NLBApeDeInitializeCoreLoad operation or NLBCoreIOControlReload operation at the same time, this kind of operation will release the value of [rdi+0xc9b8] and make [rdi+0xc9b8]=0:

this will cause thread 1 to read the value of rdi+0xc9b8 unreliable and trigger DoS:

## Slide 17

### Trigger by NLBCoreLoadReceiveNRProtocolData

We can construct different NLB packages to trigger lock-free access to pLoad->NRProtocol in another code flow, they end up triggering the same conditional race vulnerability.

The attacker sends data packets, making the code execution path:

```
NLBFilterReceiveNetBufferLists
```

- `->NLBCoreReceivePacket`

- `->NLBCoreReceiveHeartbeat`

- `->NLBCoreReceiveNRProtocolData`

- `->NLBCoreLoadReceiveNRProtocolData`

## Slide 18

### The NRP Packet we constructed:

```
#pragma pack(push,1)
typedefstruct _NRP_PACKET
{
unsignedlong Magic;
unsignedchar FuncId;
unsignedlong unk1;
unsignedchar Type;
unsignedchar Index;
unsignedchar TestBit;
unsignedshort unk2;
unsignedlong ExtendLen;
}NRP_PACKET,*PNRP_PACKET;
#pragma pack(pop)
charbuf[9000+14]{};
memcpy(buf,"\xff\xff\xff\xff\xff\xff\x00\x50\x56\xc0\x00\x08\x88\x6f",14);
int index =0x19;
int SendLen =1500;
char* nlb = buf +14;
*(unsignedlong*)(nlb)=0xC0DE01DE;
*(unsignedlong*)(nlb +4)=0x205;
*(unsignedlong*)(nlb +8)=0x20;
*(unsignedlong*)(nlb +12)=inet_addr("192.168.40.100");
*(unsignedlong*)(nlb +21)= SendLen -0x19;
  auto pNrp =(PNRP_PACKET)(nlb + index);
pNrp->Magic=0xBEEF;
pNrp->FuncId=2;
pNrp->Type=3;
pNrp->Index=0;
pNrp->TestBit=0;
pNrp->ExtendLen=4;
*(unsignedlong*)(pNrp +1)=0x12345678;
```

And after running the poc, the system crashes in the NLBCoreNRProtocolReceiveData:

## Slide 19

## 2.5 Case Study 5: Moderate Severity but Unauth DoS

This is a bug defined as "Moderate severity DoS". Still, we thought it was worth mentioning. An attacker can continuously send special packets to trigger a memory leak bug in the target nlb server, thereby exhausting the target's non-paged memory pool, and this memory is never released. Eventually this will cause a BSoD of the current Nlb host.

This bug is located in the NLBCoreNRProtocolReceiveData process, and its trigger path is as follows:

```
NLBCoreNRProtocolReceiveData
```

- `->NLBCoreNRProtocolReceiveIPv4Add/NLBCoreNRProtocolReceiveIPv6Add`

- `->NLBVectorPushBack`

- `->NLBVectorReserve`

This call stack showcases how NLB handles received data by dynamically expanding the Vector container to store IP addresses from the packet. During its execution,It checks if the Vector has enough space for the new element. If not, it calls NLBVectorReserve to add more space.

The core logic of NLBVectorReserve using NdisAllocateMemoryWithTag to allocate nonpaged memory.

## Slide 20

However, through my analysis, I found a big problem: the non-paged memory isn't release in the code. Specifically, every time NLBVectorReserve is called, it increases the allocated memory size dynamically, with each expansion increasing by at least One-third of the current size.

Because non-paged memory is limited in kernel space, this rapid growth quickly uses it up. So we can make special NRPackets and send them to the NLB host. This makes the host enter the NLBVectorReserve process, which keeps allocating non-paged memory. By analysis the NLB driver, we get the structure of the NRPacket and make the payload to trigger this.

To remotely trigger the allocation of non-paged memory, our NRPacket must bypass the checks within the NLBVectorReserve call stack. The NRPacket structure includes like Magic, FuncId, Type, and Index. Each one is crucial for deciding how the packet is handle. 1.The Magic field must match specific values, such as 0xC0DE01C0 or 0xC0DE01F0, to send the packet to the right handling function, like NLBCoreReceiveMembershipHeartbeat or NLBCoreReceiveNRProtocolData.

2.Inside NLBCoreNRProtocolReceiveData, the FuncId field undergoes a switch-case check. if

## Slide 21

FuncId is 2, it directs the code flow to the NLBVectorReserv.

3.At the same time, we need to bypass check of NLBCoreExceptionListIPv4Add, which means that we need to set the type field to 2.

4.Additionally, The Index field is checked to ensure it is must be less than or equal to 0x20 to bypass the safeguard conditions.

When we trigger NLBVectorPushBack repeatedly, all non-paged memory will eventually be exhausted:

once the non-paged memory is exhausted,the system and applications will cause many exceptions, and causing crash:

## Slide 22

# 2. Conclusion

This paper has detailed the discovery of several vulnerabilities within the Network Load Balancing (NLB) heartbeat feature, encompassing integer overflows, race conditions, Out-ofbounds Read&Write, memory leaks, use-after-free (UAF) , null pointer dereferences. And We recommend that relevant customers upgrade the patch and block NLB heartbeats sent by unknown IP addresses. By understanding and addressing these vulnerabilities, network administrators can better safeguard their systems against potential threats, ensuring the reliability and security of their network infrastructure.

Additionally, it's worth noting that there were security checks for some of the above mentioned vulnerabilities in its predecessor version of NLB, known as WLBS. This observation underscores the importance of maintaining critical security checks, as software updates may inadvertently remove some security checks that originally existed, resulting in potential vulnerabilities being exposed.

Finally, The refactored module may be a good choice for novice Bug Bounty hunters. It may be reproduce old bugs or may have new attack surfaces, and there are often many technical articles and related codes available for security research.
