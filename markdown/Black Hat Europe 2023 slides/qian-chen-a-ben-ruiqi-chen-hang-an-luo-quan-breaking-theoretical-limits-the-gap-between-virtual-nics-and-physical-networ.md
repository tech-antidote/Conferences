---
title: "Breaking Theoretical Limits The Gap Between Virtual NICs and Physical Network Cards"
speakers: ["Qian Chen", "A Ben", "Ruiqi Chen", "Hang An", "Luo Quan"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Qian Chen, A Ben, Ruiqi Chen, Hang An, Luo Quan_Breaking Theoretical Limits The Gap Between Virtual NICs and Physical Network Cards.pdf"
pages: 45
sha256: "121eddb76cfbfb30f2c705ff84aecbd1c48fdaa6e52fcb7971187b32a821df72"
text_chars: 23810
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.0
ocr_unreliable_blocks: 1
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:04:19Z"
---
# Breaking Theoretical Limits The Gap Between Virtual NICs and Physical Network Cards

**Speakers:** Qian Chen, A Ben, Ruiqi Chen, Hang An, Luo Quan  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Qian Chen, A Ben, Ruiqi Chen, Hang An, Luo Quan_Breaking Theoretical Limits The Gap Between Virtual NICs and Physical Network Cards.pdf` (45 pages)


## Slide 1

Breaking Theoretical Limits: The Gap Between Virtual NICs and Physical Network Cards

Quan Luo, Qian Chen  |  December 2023

## Slide 2

## About Us

Quan Luo @TrueUnitySect

Qian Chen @cq674350529

OS Virtualization
Network Protocol

IoT
Network Protocol

A Ben

Ruiqi Chen @kevinoclam2

Hang An @HangAn54637220

OS Browser
Network Protocol

Web

Windows

Linux Kernel

Focus on software source code security analysis and binary vulnerability research

## Slide 3

Introduction

Hyper

V Network

Module Research

Vulnerability

Analysis

Summary

Agenda

## Slide 4

## Agenda

Introduction

Hyper

V Network

Module Research

Vulnerability

Analysis

Summary

## Slide 5

## Virtualization Technology

 Provide the foundational technology for creating and managing virtual resources like virtual servers and virtual networks

Application Application Application
…  provide functionalities like Open
OS OS OS
vNIC vNIC vNIC vNIC vSwitch (SDN) and communication
between adjacent virtual machines
vmswitch vmswitch …
 serve as a fundamental and low-
virtual networking Hypervisor
level infrastructure, which is an
appealing target for virtual machine
Server
NIC …
escape

physical networking

## Slide 6

Windows
These characteristics in physical network cards often need to be simulated and
implemented through software in virtual environments.

Linux

Network Interface Card (NIC) Characteristics

## Slide 7

## Virtual NIC

Application Application Application OS OS OS vNIC vNIC vNIC vNIC

- UDP Segmentation Offload (USO)vSwitch: offload the task of segmenting large UDP packets into vSwitch … small fragments from CPU to NIC virtual networking Hypervisor

- Large Send Offload (LSO): offload the task of segmenting large TCP packets into small Server

- NIC …

- fragments from CPU to NIC

implementation in software

physical networking

 …

## Slide 8

## Virtual NIC

 Category: E1000, E1000e, VMXNET, VMXNET2, VMXNET3, …

 Primary feature: provide functionalities that have been migrated from CPU
to NIC
do segmentation,
checksum and so on
CPU Memory CPU Memory
interrupt interrupt
Bus Bus
receive packets receive packets
do LSO/USO
NIC NIC
past present

## Slide 9

## Past Research Focus

Application Application Application
OS OS OS
vNIC vNIC vNIC vNIC

- vSwitch vSwitch …

- Those functionalities that have been moved from CPU to virtual networking Hypervisor

- NIC, like LSO, USO

fuzzing
code review

Server

- NIC …

- Configuration commands similar to rndis

physical networking

## Slide 10

## Agenda

Introduction

Hyper-V Network Module Research

Vulnerability

Analysis

Summary

## Slide 11

Choose code review when fuzzing yields no promising results

reverse engineering the vmswitch module

## Slide 12

A single ICMPv6 packet whose length is bigger than 65535


> Recovered by OCR — confidence 93/100 on the text kept, 83/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Wireshark packet list]
No.   Time        Source                       Destination                  Protocol   Length   Info
2     69.159055   fe80::db90:748e:fc5f:e62f    fe80::acc6:5128:792d:5005    ICMPv6     69741    Unknown (86)
3     69.159055   fe80::db90:748e:fc5f:e62f    fe80::acc6:5128:792d:5005    ICMPv6     69741    Unknown (86)
4     74.177271   fe80::db90:748e:fc5f:e62f    fe80::acc6:5128:792d:5005    ICMPv6     69741    Unknown (86)
5     74.177271   fe80::db90:748e:fc5f:e62f    fe80::acc6:5128:792d:5005    ICMPv6     69741    Unknown (86)

[Packet details pane]
> Frame 2: 69741 bytes on wire (557928 bits), 69741 bytes captured (557928 bits) on interfac[cut off by hex pane]
> Ethernet II, Src: Microsof_be:bc:00 (00:15:5d:be:bc:00), Dst: VMware_3e:02:d1 (00:0c:29:3e[cut off by hex pane]
v Internet Protocol Version 6, Src: fe80::db90:748e:fc5f:e62f, Dst: fe80::acc6:5128:792d:500[cut off by hex pane]
      0110 .... = Version: 6
    > .... 0000 0000 .... .... .... .... .... = Traffic Class: 0x00 (DSCP: CS0, ECN: Not-ECT)
      .... 0000 0000 0000 0000 0000 = Flow Label: 0x00000
      Payload Length: 0 (Jumbogram)
      Next Header: IPv6 Hop-by-Hop Option (0)
      Hop Limit: 255
      Source Address: fe80::db90:748e:fc5f:e62f
      Destination Address: fe80::acc6:5128:792d:5005
> IPv6 Hop-by-Hop Option
> Routing Header for IPv6 (Source Route)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)
> Routing Header for IPv6 (Unknown type 86)   [dimmed behind caption bar]
> Routing Header for IPv6 (Unknown type 86)   [dimmed behind caption bar, bottom row clipped]

[Hex pane - ASCII column cut off at the right slide edge]
00000000  00 0c 29 3e 02 d1 00 15  5d be bc 00 86 dd 60 00
00000010  00 00 00 00 00 ff fe 80  00 00 00 00 00 00 db 90
00000020  74 8e fc 5f e6 2f fe 80  00 00 00 00 00 00 ac c6
00000030  51 28 79 2d 50 05 2b 00  c2 04 00 01 10 10 2b ff
00000040  00 00 06 d5 00 15 0c ba  73 60 00 00 00 00 56 ff
00000050  02 00 00 00 00 00 10 11  12 13 14 15 16 17 18 19
00000060  1a 1b 1c 1d 1e 1f 20 21  22 23 24 25 26 27 28 29
00000070  2a 2b 2c 2d 2e 2f 30 31  32 33 34 35 36 37 56 56
00000080  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000090  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000a0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000b0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000c0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000d0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000e0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000000f0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000100  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000110  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000120  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000130  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000140  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000150  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000160  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000170  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000180  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
00000190  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000001a0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000001b0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000001c0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000001d0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56
000001e0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56   [dimmed behind caption bar]
000001f0  56 56 56 56 56 56 56 56  56 56 56 56 56 56 56 56   [dimmed behind caption bar]

A single ICMPv6 packet whose length is bigger than 65535
```

## Slide 13

A single ARP packet whose length is only 15 (extra padding added by OS)


> Recovered by OCR — confidence 91/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
No. Time Source
26 @.252788 Microsof_be:bc:00
27 @.252925 Microsof_be:bc:00
Destination
Broadcast
Broadcast
Broadcast
Broadcast
Broadcast
Protocol
ARP
ARP
ARP
ARP
ARP
Length Info
34 Reserved opcode
34 Reserved opcode
34 Reserved opcode
34 Reserved opcode
34 Reserved opcode
Frame 23: 34 bytes on wire (272 bits), 34 bytes captured (272 bits) on interface \Device\NPF
Type: ARP (@x@806)
v Address Resolution Protocol (reserved)
Hardware type: Unknown (24576)
Protocol type: Unknown (0x9e0e)
Hardware size: @
Protocol size: @
Opcode: reserved (@)
```

## Slide 14

## Packet Transmission in Hyper-V

Physical  …
NIC Storage CPU
Memory
Hardware
Address
…
Hypercalls MSRs
Manager
Hypervisor
Packets are mapped to the host through vmbus using DMA (Direct Memory Access)
tunnel traffic over
netVSC
I/O Stack vmswitch vmbus to vmswitch
emulate a NIC
through RNDIS
I/O Stack
procotol
Kernel Mode Kernel Mode
vmswitch is a
demo.exe
VSP, lives in
host kernel User Mode User Mode
Host OS Guest  OS

## Slide 15

## I/O Port vs vmbus

Bus Bus
command
interrupt map
I/O port
command / mem address
CPU inefficient CPU efficien t, with better performance
vmbus_send
mem address
interrupt map
I/O mem

## Slide 16

## How Packets Reaching Network I/O Stack

same code for both
TDI cases, while the latter
may break assumptions
TCPIP
NDIS
from physical link vmbus
NIC vmswitch
no constraints from
adhere to constraints physical and link layer

## Slide 17

## Call Stack for Packets in vmswitch

same code for both cases, while the latter may break assumptions

TDI

TCPIP

NDIS

vmbus

vmswitch

`vmswitch!VmsVmNicPvtRndisDeviceSendPackets vmswitch!RndisDevHostHandlePacketMessages+0x212 vmswitch!VmsVmNicPvtKmclProcessingComplete+0x1e3 vmbkmclr!InpFillAndProcessQueue+0x2d0 vmbkmclr!KmclpVmbusIsr+0x126 vmbusr!ParentRingInterruptDpc+0x62 nt!KiExecuteAllDpcs+0x335 nt!KiRetireDpcList+0x910 nt!KyRetireDpcList+0x5 nt!KiDispatchInterruptContinue` call stack

1. transform from a message to packet 2. enter the protocol processing function (protocol handler) registered in vmswitch for NDIS

## Slide 18

## Call Stack for Packets in vmswitch

TDI

TCPIP NDIS

same code for both cases, while the latter may break assumptions

vmbus

vmswitch

`vmswitch!RndisDevHostDeviceIndicatePackets vmswitch!RndisDevDeviceIndicatePackets+0x4a vmswitch!VmsVmNicPvtPacketForward+0x496 vmswitch!VmsRouterDeliverNetBufferLists+0x81a vmswitch!VmsExtPtReceiveNetBufferLists+0x193 NDIS!ndisMIndicateNetBufferListsToOpen+0x11e NDIS!ndisMTopReceiveNetBufferLists+0x267bc NDIS!ndisCallReceiveHandler+0x47 NDIS!NdisMIndicateReceiveNetBufferLists+0x735 vmswitch!VmsExtMpIndicatePackets+0xa55 vmswitch!VmsExtMpSendNetBufferLists+0x5a8` call stack

1. reach VmsVmNicPvtPacketForward() after a series of filtering, verification, addressing

2. invoke the corresponding handler on the protocol stack to send the packet

## Slide 19

## How to Send Normal Packets

Physical  …
NIC Storage CPU
Memory
Hardware
Address
…
Hypercalls MSRs
Manager
Hypervisor
convert packet into a
message, then call
netVSC
I/O Stack vmswitch vmbus vmbus_sendpacket()
do various
I/O Stack
processing and
Kernel Mode Kernel Mode checks
demo.exe invoke sendxxx()
User Mode User Mode
Host OS Guest  OS

## Slide 20

## How to Send “Anormal” Packets

Physical  …
NIC Storage CPU
Memory
Hardware
Address  hook vmbus_sendpacket() …
Hypercalls MSRs
Manager
Hypervisor
convert packet into a
message, then call
netVSC
I/O Stack vmswitch vmbus vmbus_sendpacket()
do various
I/O Stack
processing and
Kernel Mode Kernel Mode checks
demo.exe invoke sendxxx()
User Mode User Mode
Host OS Guest  OS

## Slide 21

## Packet Process Flow in vmswitch

Forward Physical  Filter …
NIC Storage CPU
Memory
VmsMpNicPvtPacketForward Router filters Hardware
...
VmsPtNicPvtPacketForward forwarders
Address
…
VmsVmNicPvtPacketForwardHypercalls MSRsmonitors
Manager
Hypervisor
netVSC
I/O Stack vmswitch vmbus
I/O Stack
Kernel Mode Kernel Mode
demo.exe
User Mode User Mode
Host OS Guest  OS

## Slide 22

## NDIS Network Interface Architecture

NDIS

protocol handler

protocol handler

vmswitch
TCPIP

vmswitch can be considered as a filtering

driver stacked on top of NDIS

Many of the function pointers in

vmswitch

are treated as dispatch function pointers

for NDIS

NIC

## Slide 23

## vmswitch Stacking Behavior

\```
// ...
\```

\```
RtlInitUnicodeString(&DestinationString, L"VMSP");
ProtocolCharacteristics.Header=8389269;
// ...
\```

\```
ProtocolCharacteristics.OpenAdapterCompleteHandlerEx=VmsPtNicOpenAdapterCompleteEx;
ProtocolCharacteristics.CloseAdapterCompleteHandlerEx=VmsPtNicCloseAdapterCompleteEx;
// ...
\```

\```
ProtocolCharacteristics.UninstallHandler=VmsPtNicUninstall;
\```

\```
v12 =NdisRegisterProtocolDriver(0i64, &ProtocolCharacteristics, &VmsProtocolHandle);
/* ... */
\```

\```
RtlInitUnicodeString(&v35, L"Hyper-V Virtual Switch Extension Filter");
RtlInitUnicodeString(&v36, L"{529B8983-9625-49A5-8284-CE944FD8E242}");
RtlInitUnicodeString(&v37, L"VMSVSF");
\```

\```
FilterDriverCharacteristics.SetOptionsHandler=VmsExtFilterSetFilterModuleOptions;
FilterDriverCharacteristics.SetFilterModuleOptionsHandler=VmsExtFilterSetFilterModuleOptions;
// ...
\```

\```
FilterDriverCharacteristics.SendNetBufferListsHandler=VmsExtFilterSendNetBufferLists;
// ...
\```

\```
v18 =NdisFRegisterFilterDriver(DriverObject, 0i64, &FilterDriverCharacteristics,
&VmsVswitchFilterHandle);
\```

## Slide 24

## Processing Routine

protocol handler
TCPIP TDI
NDIS
protocol handler
vmswitch other guest
…
NIC vmswitch
vmbus

application layer

## Slide 25

## Our Findings

same code for both TDI cases, while the latter

may break assumptions  Data from vmbus is written to the network layer directly, without going TCPIP through the physical and link layer, thus not subject to constraints NDIS  The same implementation is applied to diverse sources of incoming packets, while the hidden preconditions within the implementation may be from physical link vmbus broken NIC vmswitch

NIC

NIC vmswitch _no constraints from adhere to constraints physical and link layer_

## Slide 26

## Agenda

Introduction

Hyper

V Network

Module Research

Vulnerability Analysis

Summary

## Slide 27

Caused by a single ICMPv6 packet whose length is bigger than 65535

CVE-2021-24074 Integer Overflow


> Recovered by OCR — confidence 94/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-24074 Integer Overflow
Windows TCP/IP Remote Code Execution Vulnerability
CVE-2021-24074
Security Vulnerability
Released: Feb 9, 2021
Assigning CNA: Microsoft
CVSS:3.19.8/8.5 ©
Exploitability
The following table provides an exploitability assessment for this vulnerability at the time of original publication.
Publicly disclosed Exploited Exploitability assessment
```

## Slide 28

CVE-2021-24074 Integer Overflow


> Recovered by OCR — confidence 80/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2021-24074 Integer Overflow
Tine Source Destination Protocol Length Info
147 86.629514 fe80: :20c:29fF:fef8:8df3 #f02::1:ffdb:9090 ICMPv6 86 Neighbor Solicitation for fe8@::98c3:5e9d:e2db:909
148 86.629795 Fe8@: :98c3:5e9d:e2db:9090 fes8@: :20c:29F Ff: Fef8:8dF3 ICMPVv6 86 Neighbor Advertisement fe8@: :98c3:5e9d:e2db:9090 (
Frame 148: 86 bytes on wire (688 bits), 86 bytes captured (688 bits) @0 Oc 29 75 3b 86 dd 60
Ethernet II, Src: VMware_86:75:3b (00:0c:29:86:75:3b), Dst: VMware f8:8d:f3 (00:0c:29:f8:8 228 80 2 @2 08 828 00 98
v Internet Protocol Version 6, Src: fe80::98c3:5e9d:e2db:9090, Dst: fesda::20c:29ff:fefs:8df3\| 9220 Se 9d e2 88 88 028 20 G2
0000 0000 .... .... wees seve sees = Traffic Class: @x0@ (DSCP: CSQ, ECN: Not-ECT) 00 00 00 e2 db 98 90 @2
Payload Length: 32
Next Header: ICMPv6 (58)
Hop Limit: 255
Source Address: fe8@::98c3:5e9d:e2db:9090
Destination Address: fe8@::20c:29ff:fefs:8df3
[Destination SLAAC MAC: VMware_f8:8d:f3 (00:0c:29:f8:8d: 3) ]
~ Internet Control Message Protocol v6
Type: Neighbor Advertisement (136)
Code: @
Checksum: @xecc@ [correct]
[Checksum Status: Good]
Flags: @x60000000, Solicited, Override
Target Address: fe8Q::98c3:5e9d:e2db:9090
~ ICMPv6 Option (Target link-layer address : 00:0c:29:86:75:3b)
Type: Target link-layer address (2)
Length: 1 (8 bytes)
Link-layer address: VMware_86:75:3b (@0:0c:29:86:75: 3b)
```

## Slide 29

## CVE-2021-24074

### Integer Overflow

`tcpip!Ipv6pHandleRouterAdvertisement tcpip!Icmpv6ReceiveDatagrams+0x32b tcpip!IppDeliverListToProtocol+0xf0 tcpip!IppProcessDeliverList+0x62 tcpip!IppReceiveHeaderBatch+0x214 tcpip!IppFlcReceivePacketsCore+0x315 tcpip!FlpReceiveNonPreValidatedNetBufferListChain+0x271 tcpip!FlReceiveNetBufferListChainCalloutRoutine+0xc2 nt!KeExpandKernelStackAndCalloutInternal+0x85 tcpip!FlReceiveNetBufferListChain+0xb6` The control flow, originating from the vmswitch module, eventually enters the `NDIS!ndisMIndicateNetBufferListsToOpen+0x11e NDIS!NdisMIndicateReceiveNetBufferLists+0x31c vmswitch!VmsMpNicPvtPacketForward+0x238 vmswitch!VmsRouterDeliverNetBufferLists+0x390 vmswitch!VmsExtPtReceiveNetBufferLists+0x193 NDIS!ndisMIndicateNetBufferListsToOpen+0x11e NDIS!ndisMTopReceiveNetBufferLists+0x267bc NDIS!ndisCallReceiveHandler+0x47 NDIS!NdisMIndicateReceiveNetBufferLists+0x735`

tcpip

module

call stack

## Slide 30

\```
VOID Ipv6pHandleRouterAdvertisement(ICMPV6_MESSAGE *Icmpv6, IP_REQUEST_CONTROL_DATA *Args) {
// ...
\```

\```
USHORT ParsedLength;// (1)
/* ... Validate the Router Advertisement ... */
/* ... Get the Router Advertisement header ... */
\```

\```
Advertisement =NetioGetDataBuffer(NetBuffer, sizeof(ND_ROUTER_ADVERT_HEADER), &AdvertisementBuffer, 1, 0);
ParsedLength=sizeof(ND_ROUTER_ADVERT_HEADER);
\```

\```
/* ... */
\```

\```
while (Ipv6pParseTlvOption(NetBuffer, &Type, &Length)) { // (2)sanity-check the options
switch(Type) {
\```

\```
caseND_OPT_SOURCE_LINKADDR:// ...
caseND_OPT_MTU:// ...
caseND_OPT_PREFIX_INFORMATION:// ...
caseND_OPT_ROUTE_INFO:// ...
}
// Move forward to the next option.
// Keep track of the parsed length, so we can use it below to back up.
NetioAdvanceNetBuffer(NetBuffer, Length); // (3)
ParsedLength+= Length;   // (4)
}
// ...
\```

\```
NetioRetreatNetBuffer(NetBuffer, ParsedLength, 0);   // (5)
// ...
\```

... Option1 Option2 Option5

ICMPv6 Options

## Slide 31

\```
VOID Ipv6pHandleRouterAdvertisement(ICMPV6_MESSAGE *Icmpv6, IP_REQUEST_CONTROL_DATA *Args) {
// ...
\```

\```
USHORT ParsedLength;// (1)
/* ... Validate the Router Advertisement ... */
/* ... Get the Router Advertisement header ... */
\```

\```
Advertisement =NetioGetDataBuffer(NetBuffer, sizeof(ND_ROUTER_ADVERT_HEADER), &AdvertisementBuffer, 1, 0);
ParsedLength=sizeof(ND_ROUTER_ADVERT_HEADER);
\```

\```
/* ... */
while (Ipv6pParseTlvOption(NetBuffer, &Type, &Length)) { // (2)sanity-check the options
switch(Type) {
\```

\```
caseND_OPT_SOURCE_LINKADDR:// ...
caseND_OPT_MTU:// ...
caseND_OPT_PREFIX_INFORMATION:// ...
caseND_OPT_ROUTE_INFO:// ...
}
// Move forward to the next option.
// Keep track of the parsed length, so we can use it below to back up.
NetioAdvanceNetBuffer(NetBuffer, Length); // (3)
ParsedLength+= Length;   // (4)
}
// ...
\```

\```
NetioRetreatNetBuffer(NetBuffer, ParsedLength, 0);   // (5)
// ...
\```

... Option1 Option2 Option5

ICMPv6 Options

## Slide 32

\```
VOID Ipv6pHandleRouterAdvertisement(ICMPV6_MESSAGE *Icmpv6, IP_REQUEST_CONTROL_DATA *Args) {
// ...
\```

\```
USHORT ParsedLength;// (1)
/* ... Validate the Router Advertisement ... */
/* ... Get the Router Advertisement header ... */
\```

\```
Advertisement =NetioGetDataBuffer(NetBuffer, sizeof(ND_ROUTER_ADVERT_HEADER), &AdvertisementBuffer, 1, 0);
ParsedLength=sizeof(ND_ROUTER_ADVERT_HEADER);
\```

\```
/* ... */
\```

\```
while (Ipv6pParseTlvOption(NetBuffer, &Type, &Length)) { // (2)sanity-check the options
switch(Type) {
\```

\```
caseND_OPT_SOURCE_LINKADDR:// ...
caseND_OPT_MTU:// ...
caseND_OPT_PREFIX_INFORMATION:// ...
caseND_OPT_ROUTE_INFO:// ...
}
// Move forward to the next option.
// Keep track of the parsed length, so we can use it below to back up.
NetioAdvanceNetBuffer(NetBuffer, Length); // (3)
ParsedLength+= Length;   // (4)
}
// ...
\```

\```
NetioRetreatNetBuffer(NetBuffer, ParsedLength, 0);   // (5)
// ...
\```

... Option1 Option2 Option5

ICMPv6 Options

## Slide 33

\```
VOID Ipv6pHandleRouterAdvertisement(ICMPV6_MESSAGE *Icmpv6, IP_REQUEST_CONTROL_DATA *Args) {
// ...
\```

\```
USHORT ParsedLength;// (1)
/* ... Validate the Router Advertisement ... */
/* ... Get the Router Advertisement header ... */
\```

\```
Advertisement =NetioGetDataBuffer(NetBuffer, sizeof(ND_ROUTER_ADVERT_HEADER), &AdvertisementBuffer, 1, 0);
ParsedLength=sizeof(ND_ROUTER_ADVERT_HEADER);
\```

\```
/* ... */
\```

\```
while (Ipv6pParseTlvOption(NetBuffer, &Type, &Length)) { // (2)sanity-check the options
switch(Type) {
\```

\```
caseND_OPT_SOURCE_LINKADDR:// ...
caseND_OPT_MTU:// ...
caseND_OPT_PREFIX_INFORMATION:// ...
caseND_OPT_ROUTE_INFO:// ...
\```

\```
}
// Move forward to the next option.
\```

\```
// Keep track of the parsed length, so we can use it below to back up.
NetioAdvanceNetBuffer(NetBuffer, Length); // (3)
ParsedLength+= Length;   // (4)
}
// ...
\```

\```
NetioRetreatNetBuffer(NetBuffer, ParsedLength, 0);   // (5)
\```

\```
// ...
\```

... Option1 Option2 Option5

ICMPv6 Options

## Slide 34

\```
VOID Ipv6pHandleRouterAdvertisement(ICMPV6_MESSAGE *Icmpv6, IP_REQUEST_CONTROL_DATA *Args) {
// ...
\```

\```
USHORT ParsedLength;// (1)
/* ... Validate the Router Advertisement ... */
/* ... Get the Router Advertisement header ... */
\```

\```
Advertisement =NetioGetDataBuffer(NetBuffer, sizeof(ND_ROUTER_ADVERT_HEADER), &AdvertisementBuffer, 1, 0);
ParsedLength=sizeof(ND_ROUTER_ADVERT_HEADER);
\```

\```
/* ... */
\```

\```
while (Ipv6pParseTlvOption(NetBuffer, &Type, &Length)) { // (2)sanity-check the options
switch(Type) {
\```

\```
caseND_OPT_SOURCE_LINKADDR:// ...
caseND_OPT_MTU:// ...
caseND_OPT_PREFIX_INFORMATION:// ...
caseND_OPT_ROUTE_INFO:// ...
\```

\```
}
\```

\```
// Move forward to the next option.
\```

\```
// Keep track of the parsed length, so we can use it below to back up.
NetioAdvanceNetBuffer(NetBuffer, Length); // (3)
\```

\```
ParsedLength+= Length;   // (4) integer overflow
}
\```

\```
// ...
\```

\```
NetioRetreatNetBuffer(NetBuffer, ParsedLength, 0);   // (5)
\```

\```
// ...
\```

... Option1 Option2 Option5

ICMPv6 Options

## Slide 35

Caused by a single ARP packet whose length is only 15

CVE-2022-30223 Out-of-bounds Read


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-30223 Out-of-bounds Read
Windows Hyper-V Information Disclosure Vulnerability
CVE-2022-30223
Security Vulnerability
Released: Jul 12, 2022
Assigning CNA: Microsoft
CVE-2022-30223 7
Impact: Information Disclosure Max Severity: Important
CVSS:3.15.7/5.0 ©
Exploitability
The following table provides an exploitability assessment for this vulnerability at the time of original publication.
Publicly disclosed Exploited Exploitability assessment
```

## Slide 36

CVE-2022-30223 Out-of-bounds Read


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-30223 Out-of-bounds Read
Time Source Destination Length Info
16 7.782714 VMware_86:75:3b Broadcast 42 Who has 192.168.63.2? Tell 192.168
17 7.783109 VMware_f0:42:1f VMware_86:75:3b 60 192.168.63.2 is at 00:50:56:f0:42:
Frame 16: 42 bytes on wire (336 bits), 42 bytes captured (336 bits) on interface \Dé ff ff ff ff ff FF G2 Oc 29 86 75 3b O8 B6 GO 1
» Ethernet II, Src: VMware _86:75:3b (@0@:0c:29:86:75:3b), Dst: Broadcast (ff:ff:ff:fFf: Q8 QO 06 04 2A O1 BB Gc 29 86 75 3b ce a8 3f 81
Source: VMware_86:75:3b (00:0c:29:86:75:3b)
Type: ARP (0x86)
~ Address Resolution Protocol (request)
Hardware type: Ethernet (1)
Protocol type: IPv4 (@x0800)
Hardware size: 6
Protocol size: 4
Opcode: request (1)
Sender MAC address: VMware_86:75:3b (00:0c:29:86:75:3b)
Sender IP address: 192.168.63.129
Target MAC address: 00:00:00 00:00:00 (00:00:00:00:00:00)
Target IP address: 192.168.63.2
```

## Slide 37

## CVE-2022-30223

\```
vmswitch!VmsNblHelperCreateCloneNbl
vmswitch!VmsMpNicPvtPacketForward+0x308
vmswitch!VmsRouterDeliverNetBufferLists+0x81a
vmswitch!VmsExtPtReceiveNetBufferLists+0x193
NDIS!ndisMIndicateNetBufferListsToOpen+0x11e
NDIS!ndisMTopReceiveNetBufferLists+0x267bc
NDIS!ndisCallReceiveHandler+0x47
NDIS!NdisMIndicateReceiveNetBufferLists+0x735
vmswitch!VmsExtMpIndicatePackets+0xa55
vmswitch!VmsExtMpSendNetBufferLists+0x5a8
\```

### Out-of-bounds Read

call stack

## Slide 38

\```
__int64VmsNblHelperCreateCloneNbl(PNET_BUFFER_LISTSrcNetBufferList, NDIS_HANDLENetBufferListPoolHandle, NDIS_HANDLE
NetBufferPoolHandle, chara4, chara5, chara6, inta7, __int64a8) {
// ...
\```

\```
v11 =v10_SrcNetBufferList->NetBufferListInfo[0];
if( v11 &&((unsigned__int8)v11 &0x1C) !=0) {
// ...
if( ((unsigned__int8)v11 &4) !=0) {
// ...
LABEL_14:
v57 =v12;
NdisAdvanceNetBufferListDataStart(v10_SrcNetBufferList, v12, 0, 0i64);
v56 =1;
gotoLABEL_16;
}
if( ((unsigned__int8)v11 &8) ==0) {
v12 = 34;  // (1)
gotoLABEL_14;
}
// ...
}
// ...
LABEL_16:
// ...
v21 = v12;   // (2)
/* ... */
while( 1) {
// ...
\```

\```
v19_dstNetBufferList = NdisCopyFromNetBufferToNetBuffer(v26, 0, v21, v24, 0, &BytesCopied); // (3)
// ...
\```

## Slide 39

-
A 15 byte ARP packet is expanded to 34 bytes, resulting in kernel address leakage

CVE-2022-30223 Out-of-bounds Read


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2022-30223
Tine Source Destination Protocol
1 @.e9e000 Microsof_be:bc:00 Broadcast ARP
2 @.000112 Microsof_be:bc:00 Broadcast ARP
Frame 2: 34 bytes on wire (272 bits), 34 bytes captured (272 bits) on interface \Dev
v Ethernet II, Src: Microsof_be:bc:00 (@0:15:5d:be:bc:00), Dst: Broadcast (ff:ff: ff: ff
Destination: Broadcast (ff:ff: ff: ff: fF: fF)
Type: ARP (@x@806)
v Address Resolution Protocol (opcode @x@10@)
Hardware type: Unknown (24576)
Protocol type: Unknown (@x@@e0)
Hardware size: 6
Protocol size: @
Opcode: Unknown (256)
Out-of-bounds Read
Length Info
34 Reserved opcode @
34 Unknown ARP opcode @x@100
e8 25
```

## Slide 40

## CVE-XXXX-XXXX (not fixed yet)

NULL pointer deference caused by a packet with only 8-byte IP header

## Slide 41


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
How to modify the Fuzzer to find bugs?

Export WASM Struct to JS

...
function createWasmStruct() {
let builder = new WasmModuleBuilder();
let struct_type = builder.addStruct([...]);
builder.addFunction('makeStruct', ...)
.exportFunc()
.addBody([
kExprI32Const, 42,
kGCPrefix, kExprStructNew, struct_type,
kGCPrefix, kExprExternConvertAny
]);
let instance = builder.instantiate();
return instance.exports.makeStruct();
}
let struct = createWasmStruct();

// original-sample.js    Original JS Sample
// A regular JS object
let normalProto = {};
// Change Array's prototype to normalProto
Array.prototype.__proto__ = normalProto;
// Perform a concat operation on an array
print([1].concat());

Mutation

Mutated Attack Code

...
function createWasmStruct() {
let builder = new WasmModuleBuilder();
let struct_type = builder.addStruct([...]);
builder.addFunction('makeStruct', ...)
.exportFunc()
.addBody([
kExprI32Const, 42,
kGCPrefix, kExprStructNew, struct_type,
kGCPrefix, kExprExternConvertAny
]);
let instance = builder.instantiate();
return instance.exports.makeStruct();
}
// Replace normalProto with a WASM struct
let wasmObj = createWasmStruct();
Array.prototype.__proto__ = wasmObj;
print([1].concat());

Key Mutation Points:
- Replace JS object with WASM struct
- Pollute Array prototype chain
- Triggers concat() method

Boom!

$ /tmp/d8-linux-debug-v8-component-93712/d8 /tmp/poc.js

#
# Fatal error in gen/torque-generated/src/objects/js-objects-tq-inl.inc, line 67
# Check failed: !v8::internal::v8_flags.enable_slow_asserts.value() || (IsJSObject_NonInline(*this)).
#
#
#
#FailureMessage Object: 0x7ffd386ecee0
==== C stack trace ===============================

    /tmp/d8-linux-debug-v8-component-93712/libv8_libbase.so(v8::base::debug::StackTrace::StackTrace()+[clipped]
    /tmp/d8-linux-debug-v8-component-93712/libv8_libplatform.so(+0x18e0d) [0x7ff684218e0d]
    /tmp/d8-linux-debug-v8-component-93712/libv8_libbase.so(V8_Fatal(char const*, int, char const*, ..[clipped]
    /tmp/d8-linux-debug-v8-component-93712/libv8.so(+0x25721f2) [0x7ff6813721f2]
    /tmp/d8-linux-debug-v8-component-93712/libv8.so(+0x2660ffc) [0x7ff681460ffc]
    /tmp/d8-linux-debug-v8-component-93712/libv8.so(+0x26589d3) [0x7ff6814589d3]
    /tmp/d8-linux-debug-v8-component-93712/libv8.so(v8::internal::Builtin_ArrayConcat(int, unsigned lo[clipped]
    /tmp/d8-linux-debug-v8-component-93712/libv8.so(+0x1d7bb7d) [0x7ff680b7bb7d]
[1]    1575121 trace trap  /tmp/d8-linux-debug-v8-component-93712/d8 /tmp/poc2.js
```

## Slide 42

Demo

## Slide 43

## Agenda

Introduction

Hyper

V Network

Module Research

Vulnerability

Analysis

Summary

## Slide 44

## What We Have Talked

 Virtual NIC is not total identical to physical network card. And the gap between them may break the protocol stack implementations, resulting in severe vulnerabilities

- An in-depth analysis of multiple vulnerabilities discovered by breaking the theoretical limits outlined by RFC

- A new point to guide the code review or fuzzing routine when targeting virtual NICs

## Slide 45

# Thanks!

TrueUnitySect <u>a4651386@163.com</u>
