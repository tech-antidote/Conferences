---
title: "vCenter Lost How the DCERPC Vulnerabilities Changed the Fate of ESXi"
speakers: ["Hao Zheng", "Zibo Li", "Yue Liu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Hao Zheng & Zibo Li & Yue Liu_vCenter Lost How the DCERPC Vulnerabilities Changed the Fate of ESXi.pdf"
pages: 57
sha256: "3bc887d34cbe39a01f3e401a3e52b4ab07387a29c9a0d46557853226ecfe52f9"
text_chars: 17449
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.5
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:41:33Z"
---
# vCenter Lost How the DCERPC Vulnerabilities Changed the Fate of ESXi

**Speakers:** Hao Zheng, Zibo Li, Yue Liu  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Hao Zheng & Zibo Li & Yue Liu_vCenter Lost How the DCERPC Vulnerabilities Changed the Fate of ESXi.pdf` (57 pages)


## Slide 1

### vCenter Lost

How the DCERPC Vulnerabilities Changed the Fate of ESXi

Hao Zheng                                     Zibo Li                                   Yue Liu

_TianGong Team of QI-ANXIN Group_

#BHAS @BlackHatEvents

## Slide 2

##### Who we are

Hao Zheng @zhz__6951

Zibo Li @zblee_

Yue Liu @Mr_LiuYue

#BHAS @BlackHatEvents

## Slide 3

#### Who we are

TianGong Lab of QI-ANXIN Group

- Focusing on vulnerability discovery and exploitation

- Targeting at Edge Devices/IOT/OS/Virtualization/Browser

- Works published in Black Hat, HITBSecConf, EuroS&P, Usenix, ACM CCS

- Awarded in GeekPwn, Tianfu Cup, Matrix Cup

- Website: <u>https://tiangonglab.github.io/</u>

- X: @TianGongLab

#BHAS @BlackHatEvents

## Slide 4

##### Our previous work on VMware

- Long-term Focus on VMware’s virtualization security

- Discovered and reported multiple vulnerabilities in both ESXi and Workstation

- Presented our research at DEFCON, HITB

#BHAS @BlackHatEvents

## Slide 5

##### Transition to vCenter Server Research

**Noticed** VMware vCenter Server Out-of-Bounds Write Vulnerability (CVE-2023-34048)

- memory corruption

- remote code execution

- exploitation in the wild

Me
Hypervisor
vCenter

https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/23677

#BHAS @BlackHatEvents

## Slide 6

##### Agenda

1. DCERPC Protocol Overview

2. DCERPC Vulnerabilities Discovery

3. Exploitation Challenges & Techniques

4. Beyond vCenter: Privilege Escalation and Control

5. Conclusion

#BHAS @BlackHatEvents

## Slide 7

##### 1. DCERPC Protocol Overview

#BHAS @BlackHatEvents

## Slide 8

##### DCERPC Protocol

- A remote procedure call (RPC) mechanism

- Widely used in Unix and Windows NT systems.

- Uses Interface Definition Language (IDL) to define interfaces.

#BHAS @BlackHatEvents

## Slide 9

##### DCERPC Protocol Structure

- Consists of fixed common header and optional fields

- There are 20 valid packet types

#BHAS @BlackHatEvents

## Slide 10

###### DCERPC in vCenter

- Used in ports 2012, 2014, and 2020

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
DCERPC in vCenter
e Used in ports 2012, 2014, and 2020
LISTEN 2706/vmdird
LISTEN 2706/vmdird
0 0.0.0.0:2014 LISTEN 3274/vmcad
0 0.0.0.0:2020 LISTEN 2511/vmafdd
root@localhost [ ~ ]# ldd /usr/lib/vmware-vmdir/sbin/vmdird | grep “dce"
libdcerpc.so.1 = /opt/likewise/11b64/libdcerpc.so.1 (0x00007f86d206b000 )
root@localhost [ ~ ]# ldd /usr/1lib/vmware-vmca/sbin/vmcad | grep “dcerpc”
libdcerpc.so.1 = /opt/likewise/11b64/lLibdcerpc.so.1 (0x00007fdc52bd0000 )
root@localhost [ ~ ]# ldd /usr/1lib/vmware-vmafd/sbin/vmafdd | grep “dcerpc"
Libdcerpc.so.1 = /opt/lLikewise/11b64/libdcerpc.so.1 (0x00007f6a113c6000 )
root@localhost [ ~ ]# 0
```

## Slide 11

##### 2. DCERPC Vulnerabilities Discovery

#BHAS @BlackHatEvents

## Slide 12

##### CVE-2024-37079/37080

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 94/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-37079/37080
3a. VMware vCenter Server multiple heap-overflow vulnerabilities (CVE-2024-37079, CVE-2024-37080)
Description:
The vCenter Server contains multiple heap-overflow vulnerabilities in the implementation of the DCERPC protocol. VMware has evaluated the severity of these issues to be in the Critical severity range with
a maximum CVSSv3 base score of
Known Attack Vectors:
A malicious actor with network access to vCenter Server may trigger these vulnerabilities by sending a specially crafted network packet potentially leading to remote code execution.
Resolution:
To remediate CVE-2024-37079, and CVE-2024-37080 apply the updates listed in the 'Fixed Version’ column of the ‘Response Matrix’ below to affected deployments.
Workarounds:
In-product workarounds were investigated, but were determined to not be viable.
Additional Documentation:
A supplemental FAQ was created for additional clarification. Please see: https://core.vmware.com/resource/vmsa-2024-0012-questions-ar
```

## Slide 13

##### CVE-2024-37079

Request → Parsing → ✅ (Well-researched)

Response → Generation → ⚠ (Overlooked vulnerability found))

#BHAS @BlackHatEvents

## Slide 14

##### CVE-2024-37079

response of bind authentication packets

Bug!

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-37079 = =
) Bind Request (UUID, version)
response of bind authentication packets Bind Ack Nock 1
Bug!
INTERNAL void rpc__cn_assoc_proc ess_auth_t {Bind Ack
! @RPC Request (Method, Parameters)
rpc pt assoc :
peqinesden @ Process Request (Executes Method) !
rpc_cn_packet_p t Lhe, H
unsigned32 req_header_size : © Response (Result) !
rpc_cn_packet_p t resp_header :
unsigned32 header_size :
unsigned32 auth len Alter Context Request
rpc_cn_sec_ a sec_context :
boolean old_client ‘Alter Context Response;
unsigned32 st
[Optional] Unbind Request
Done Done
```

## Slide 15

##### CVE-2024-37079

header_size = ((pres_cont_list->n_context_elem - 1) * 0x18) + 0x1c + 0x20

The value of n_context_elem comes from bind request packet

#BHAS @BlackHatEvents

## Slide 16

##### CVE-2024-37079

**do_alter_cont_req_action_rtn** function checks the number of Ctx Items

1. 0x1C + 0x18 * (pres_cont_list->n_context_elem - 1)    ≤    0xFE4 2. 0x18 * (pres_cont_list->n_context_elem - 1)    ≤    0xFC8 3. (pres_cont_list->n_context_elem - 1)    ≤    0xA8 4. pres_cont_list->n_context_elem ≤    0xA9

Max(pres_cont_list->n_context_elem) = 0xA9

Max(header_size) = ((0xA9 - 1) * 0x18) + 0x1C + 0x20 = **0xFFC**

#BHAS @BlackHatEvents

## Slide 17

##### CVE-2024-37079

auth_len depends on header_size

*header_size + RPC_CN_PKT_SIZEOF_COM_AUTH_TLR = 0xFFC + 8 = 0x1004

*auth_len =  rpc_g_cn_large_frag_size - *header_size = 0x1000 – 0x1004 = **0xFFFFFFFC**

BOOM!

#BHAS @BlackHatEvents

## Slide 18

##### CVE-2024-37079

**auth_len** indicating how much free space remains

auth_len = 0xFFFFFFFC

Only 4 bytes free space

Always false

**Overflow!!!**

#BHAS @BlackHatEvents

## Slide 19

##### CVE-2024-37080

**Authentication Trailer (Auth TLR)** is an optional structure appended to a PDU

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-37080
Authentication Trailer (Auth TLR) is an optional structure appended to a PDU
auth_tlr = (rpc_cn_auth_tlir_t * unsigned8 *)(pktp) +
fragbuf_p->data_size -
auth_len + RPC_CN_PKT_SIZEOF_COM_AUTH_TLR
Bind Request Packet
COM_AUTH
common_hdr auth_len _TLR
AUTH_DATA
N
auth_tlr
auth_len
```

## Slide 20

Is the check for **auth_tlr** sufficient?

##### CVE-2024-37080

**Auth TLR** validation

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-37080 Is the check for
sufficient?
Auth TLR validation
auth_tlr = (rpc_cn_auth_tlr_t * unsigned8 *)(pktp) +
fragbuf_p->data_size -
auth_len + RPC_CN_PKT_SIZEOF_COM_AUTH_TLR
if unsigned8 *)(auth_tlr) < (unsigned8 *)(pktp ||
unsigned8 *)(auth_tlr) > (unsigned8 *)(pktp) + fragbuf_p->data_size |
unsigned8 *)(auth_tlr) + auth_len < (unsigned8 *)(pktp |
unsigned8 *)(auth_tlr) + auth_len > (unsigned8 *)(pktp) + fragbuf_p->da
st = rpc_s_protocol_error
break
```

## Slide 21

##### CVE-2024-37080

len( **AUTH_DATA** ) == **auth_len** ？

**Validation Pass!**

What If set **auth_len** = 1 without any authentication data?

#BHAS @BlackHatEvents

## Slide 22

##### CVE-2024-37080

**auth_len + header_size > pdu_len**

leading to an **integer underflow** in input_token.len

**Integer Unerflow!!!**

#BHAS @BlackHatEvents

## Slide 23

##### CVE-2024-38812

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 95/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38812
3a. VMware vCenter Server heap-overflow vulnerability (CVE-2024-38812)
Description:
The vCenter Server contains a heap-overflow vulnerability in the implementation of the DCERPC protocol. VMware has evaluated the severity of this issue to be in the Critical severity range with a maximum
CVSSv3 base score of 9.8.
Known Attack Vectors:
A malicious actor with network access to vCenter Server may trigger this vulnerability by sending a specially crafted network packet potentially leading to remote code execution.
Resolution:
To remediate CVE-2024-38812 apply the updates listed in the ‘Fixed Version’ column of the ‘Response Matrix’ below to affected deployments.
Workarounds:
In-product workarounds were investigated, but were determined to not be viable.
Additional Documentation:
A supplemental FAQ was created for additional clarification. Please see: https://bit.ly/vcf-vmsa-2024-0019-qna
```

## Slide 24

##### CVE-2024-38812

DCE/RPC
RPC handle thread
Request
Packet receive pool Process RPC call

#BHAS @BlackHatEvents

## Slide 25

##### CVE-2024-38812

**op_num:** determine the rpc function to invoke

**stub_data:** parameters encoded using **NDR**

Bug!

#BHAS @BlackHatEvents

## Slide 26

##### CVE-2024-38812

###### **NDR Array Representation**

- Maximum counts

- Offset

- Actual counts

- Elements

https://pubs.opengroup.org/onlinepubs/9629399/chap14.htm#tagfcjh_31

#BHAS @BlackHatEvents

## Slide 27

##### CVE-2024-38812

###### Convert to IDL_bound_pair_t

- lower = rang_list + Offset

- upper =  Lower + (Actual Counts) * sizeof(Element)

#BHAS @BlackHatEvents

## Slide 28

##### CVE-2024-38812

Practical implementation

- Z_value = Max Counts * sizeof(Element)

- range_list = malloc(Z_value)

#BHAS @BlackHatEvents

## Slide 29

##### CVE-2024-38812

Practical implementation

Only check whether upper - lower is less than Z_value?

- Z_value = Max Counts * sizeof(Element)

- range_list = malloc(Z_value)

#BHAS @BlackHatEvents

## Slide 30

##### CVE-2024-38812

Practical implementation

Overflow!!!

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38812
Practical implementation
if ( upper - range_list->lower > *Z_values )
LABEL_52:
dcethread_exc_raise(&rpc_x_invalid_bound, ../dcerpc/idl_lib/ndrui.c, @x47Cu);
while ( v7 > (unsigned int)vi11 )
{
12 = range_list[v1ll].upper - range_list[vi1].lower;
goto LABEL_52;
}
| Z_valu |
range_list
} Offset Actual Count: A
lower upper
```

## Slide 31

##### CVE-2024-38813

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 95/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38813
3b. VMware vCenter privilege escalation vulnerability (CVE-2024-38813)
Description:
The vCenter Server contains a privilege escalation vulnerability. VMware has evaluated the severity of this issue to be in the Important severity range with a maximum CVSSv3 base score of 7.5.
Known Attack Vectors:
A malicious actor with network access to vCenter Server may trigger this vulnerability to escalate privileges to root by sending a specially crafted network packet.
Resolution:
To remediate CVE-2024-38813 apply the updates listed in the ‘Fixed Version’ column of the ‘Response Matrix’ below to affected deployments.
Workarounds:
None.
Additional Documentation:
A supplemental FAQ was created for additional clarification. Please see: https://bit.ly/vcf-vmsa-2024-0019-qna
```

## Slide 32

##### CVE-2024-38813

Port Binding in the Initialization Phase

if port occupied, Stop & Return

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38813
Port Binding in the Initialization Phase
VmDirSyncCounterWaitEvent(gVmdirGlobals.pPortListenSyncCounter, &LD
VMDIR_LOG_DEBUG,
[file:
5	1	8	1	4	2	427	581	119	21	89.895874	%s][line:
5	1	8	1	4	3	567	581	37	21	89.266769	%d]
5	1	8	1	4	4	627	581	116	21	90.630157	[%s,%d],
Sool. / / / ; if port occupied,
lotus/vmdir/server/vmdir/init.c,
S@@LL)5 Stop & Return
return status;
if ( LDAP_ports_status )
{
VmDirLog1(VMDIR_LOG_WARNING, @xFFFFFFFF, %s:
5	1	8	1	13	4	932	837	39	14	95.770226	NOT
5	1	8	1	13	5	989	835	38	16	95.770226	all
5	1	8	1	13	6	1046	837	51	14	96.449623	LDAP
5	1	8	1	13	7	1115	836	65	20	96.504158	ports
5	1	8	1	13	8	1199	840	38	11	96.646019	are
5	1	8	1	13	9	1256	835	66	21	96.646019	ready
5	1	8	1	13	10	1338	835	40	16	96.586685	for
5	1	8	1	13	11	1395	835	123	21	92.885994	accepting
5	1	8	1	13	12	1537	835	146	21	88.052467	services.,
goto LABEL_210;
}
LABEL_210:
VmDirLog1(VMDIR_LOG_INFO, @xFFFFFFFF, “Config MaxLdapOpThrs (%d)", gVmdirGlobals.dwMaxFlowCtr1Thr) ;
VmDirLogFeatureStateSwitches();
return Mutex;
}
```

## Slide 33

##### CVE-2024-38813

If port binding succeeds, drop privileges( **setgid, setuid** )

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38813
If port binding succeeds, drop privileges(setgid, setuid)
v32 = setgid(v28->pw_gid);
{
33 = strerror(v32);
vmDirLogi(VMDIR_ LOG_ERROR, OxFFFFFFFF, “setgid failed: %s", v33)3
v29 = 1724LL;
v4@ = 1724LL;
else
{
ppLda = >pw_uid;
v34_ = getuid();
VmDirLog1(VMDIR_ LOG_INFO, OxFFFFFFFF, “Modifying uid from %d to %d", v34, ppLlda);
v35 = setuid(v28->pw_uid);
goto LABEL_210;
36 = strerror(v35);
VmDirLog1(VMDIR_LOG_ERROR, @xFFFFFFFF, setuid
5	1	8	1	3	4	1125	1014	111	19	92.391907	failed:
5	1	8	1	3	5	1262	1014	61	24	91.638733	%s, v36)3
```

## Slide 34

##### CVE-2024-38813

The code looks perfectly fine, so **where is the vulnerability** ？

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
CVE-2024-38813
(32 = setgid(v28->pw_gid);
{
33 = strerror(v32)3
VmDirLog1i(VMDIR_LOG_ERROR, @xFFFFFFFF, “setgid failed: %s", v33)3
29 = 1724LL;
v4@ = 1724LL;
The code looks
perfectly fine, so
where is the
vulnerability?
}
else
{
ppLda = v28->pw_uid;
34 = getuid();
VmDirLog1(VMDIR_LOG_INFO, @xFFFFFFFF, “Modifying uid from %d to %d", v34, pplda)3;
35 = setuid(v28->pw_uid) ;
goto LABEL_210;
36 = strerror(v35);
VmDirLog1(VMDIR_LOG_ERROR, @xFFFFFFFF, “setuid failed: %s", v36);
```

## Slide 35

##### 3. Exploitation Challenges & Techniques

#BHAS @BlackHatEvents

## Slide 36

##### Challenges in Exploiting vmdird

- **Multiple Memory Protection Mechanisms**

vmdird process with multiple memory protection mechanisms enabled, including RELRO, Stack Canary, NX, PIE, and ASLR.

- **Triggered by network requests**

uncontrollable memory allocations and releases make it difficult to precisely control memory layout

#BHAS @BlackHatEvents

## Slide 37

##### Multithread

DCE/RPC
Request1
RPC handle thread Process RPC call
Request1
Request1
Packet receive pool
Request2
Request2
RPC handle thread Process RPC call
Request2

#BHAS @BlackHatEvents

## Slide 38

##### Multithread

thread1

● Multithread arena

thread2

● Memory Isolation

narenas_limit

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
Multithread
e Multithread arena
e Memory Isolation
0x/T/92c000000
0x/T/92c114000
0x1000
0x800000
0x214000
0x114000
Qx3eec000
0x114000
Qx3eec000
0x114000
(gdb ) x/4gx 0x7 f7ec13F9000+0x1D3C98
narenas_limit
0x0000000000000020 0x0000000000000000
0x0000000000000000
0x0000000000000000
```

## Slide 39

##### Multithread

###### Thread Arena 1 Thread Arena 2 Thread Arena 3

###### Thread Arena 18

###### Thread Arena 19

Thread 1 Thread 2 Thread 3 …… Thread 18 Thread 19

#BHAS @BlackHatEvents

## Slide 40

##### Heap grooming

- receive_packet function

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
Heap grooming
fbp = rpc__cn_fragbuf_alloc(1u);
{
frag length = @;
vS = fbp->max_data_size - fbp->data_size;
goto LABEL_11;
}
e receive_packet function
```

## Slide 41

##### Infoleak Object

- a lot of log output functions in dce/rpc

- **syslog object** has function pointer

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025
Infoleak Object
e alot of log output 19 *(_DWORD *)v3 &= ~1u;
functions in dce/rpc 20 *( DWORD *)(v3 + 116) |= @x80u;
21 *(QWORD *)(v3 + 240) = al;
* syslog object has 22} *(_QWORD *)(v3 + 248) = a2;
23 *( QWORD *)(v3 + 224) = malloc;
24 *( QWORD *)(v3 + 232) = free;
```

## Slide 42

##### Out of Bound Read

- response packet output buffer structure

- ● **resonse->buffered_output>iov_elmts->buff_len**

buffered_output

iov_elmts
buffered_output
buff_addr
buff_len

response

iov

#BHAS @BlackHatEvents

## Slide 43

##### Infoleak Memory layout

###### Thread Arena 1

###### Thread Arena 2

###### Thread Arena 3

###### Thread Arena 9

- heap spray on each thread heap

- Overwrite **resp_obj.buffered_out put.iov_elmts.buff_len**

- Leak memory data from response.

…… …… ……
Heap Overflow Heap Overflow Heap Overflow
Resp O bj Resp O bj fragbu f
fragbuf Resp Obj Resp Obj
Resp Obj fragbuf fragbuf
fragbuf fragbuf Resp Obj
fragbuf Resp Obj Resp Obj
Resp Obj Resp Obj Resp Obj
…… …… ……

**……**

Heap Overflow

fragbu f

Resp Obj

Resp Obj
fragbuf
Resp Obj
Resp Obj
……

#BHAS @BlackHatEvents

## Slide 44

##### Arbitrary Address Write

- Leveraging the **fragbuf** structure

- Keep reading until the packet is complete.

- In each loop iteration, **iov_base** is updated from **fragbuf>data_p** .

#BHAS @BlackHatEvents

## Slide 45

##### Arbitrary Address Write

- Heap spray on each thread heap

- Overwrite **frag_obj->data_p** to an arbitrary address.

- Subsequent data sent will be written to the specified address.

#BHAS @BlackHatEvents

## Slide 46

##### Control Flow Hijacking

- vCenter uses the glibc heap manager

- hijack control flow by overwriting **__free_hook**

#BHAS @BlackHatEvents

## Slide 47

4. Beyond vCenter: Privilege Escalation and Control

#BHAS @BlackHatEvents

## Slide 48

##### Privilege Escalation

- Ports with the **FD_CLOEXEC** flag will not be inherited by child processes

- The file descriptor of port 2012 will not be inherited

#BHAS @BlackHatEvents

## Slide 49

##### Privilege Escalation

- 2012、 636 and 389 are all LDAP ports

- However, **FD_CLOEXEC** flag is not set for ports 636 and 389

#BHAS @BlackHatEvents

## Slide 50

##### Privilege Escalation

vmdird process child process
exec
uid = 9899 holding port fd
exploit
spawned by daemon process
new vmdird process root shell
exploit
reverse shell
again uid = 0 uid = 0

#BHAS @BlackHatEvents

## Slide 51

##### Control ESXi

- When ESXi initially connects to vCenter Server, it creates an account named vpxuser.

- vCenter Server uses vpxuser account to manage virtual machines on ESXi.

#BHAS @BlackHatEvents

## Slide 52

##### Control ESXi

- The PostgreSQL database in vCenter stores the connected esxi information

- The password is encrypted using OpenSSL Symmetric EVP

- The key can be easily obtained in vCenter

#BHAS @BlackHatEvents

## Slide 53

##### Demo

#BHAS @BlackHatEvents

> Text below was recovered by OCR (confidence 75/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2025 SSN SS
> vcenter > ~ nc -lvwvp 1337
Listening on 0.0.0.0 1337
```

## Slide 54

##### 5. Conclusion

#BHAS @BlackHatEvents

## Slide 55

##### Conclusion

Bug

###### Bug Research Tips

- Focusing on Boundary Check and Data Content Detection

- Finding the Hidden Gems in Overlooked Areas

Exp

###### Exploitation Tips

- Leveraging Key Context Structures

- Mastering and Exploiting Low-Level Defense Mechanisms

Control

###### Control Tips

- Dual Exploit Privilege Escalation

- Exploiting internal mechanisms

#BHAS @BlackHatEvents

## Slide 56

# Thanks!

#BHAS @BlackHatEvents

## Slide 57

## Q&A

#BHAS @BlackHatEvents
