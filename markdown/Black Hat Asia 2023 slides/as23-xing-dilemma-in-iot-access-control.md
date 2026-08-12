---
title: "Dilemma In IoT Access Control"
speakers: ["Xing"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS23-Xing-Dilemma-In-IoT-Access-Control.pdf"
pages: 19
sha256: "ad8481bbbb18ae937d03ac8024e0c970140018cedec9e5c9ae5771922fcc7363"
text_chars: 4709
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:47:21Z"
---
# Dilemma In IoT Access Control

**Speakers:** Xing  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS23-Xing-Dilemma-In-IoT-Access-Control.pdf` (19 pages)


## Slide 1

Dilemma in IoT Access Control: Revealing Novel Attacks and Design Challenges in Mobile-as-a-Gateway IoT

Luyi Xing*, Xin’an Zhou‡, Jiale Guan*, Zhiyun Qian‡ ‡UC Riverside and *Indiana University Bloomington

#BHASIA @BlackHatEvents

## Slide 2

## What is Mobile-as-a-Gateway (MaaG) IoT?

1. MaaG IoT devices leverage users’ mobile phones to act as “Internet gateways” to communicate with the modern IoT cloud infrastructure.

2. MaaG IoT devices lack persistent Internet connectivity.

#BHASIA @BlackHatEvents

## Slide 3

# Different Architectures of IoT

1. Always connected to the cloud. (“always-connected”)

2. No connection to the cloud. (“no-cloud”)

3. Mobile-as-a-Gateway IoT.

Access
Control
Access Access
Access Control Control
Control
“always‐connected” “no‐cloud” Mobile‐as‐a‐Gateway IoT

#BHASIA @BlackHatEvents

## Slide 4

# Different Architectures of IoT

1. Always connected to the cloud. (“always-connected”)

2. No connection to the cloud. (“no-cloud”)

3. Mobile-as-a-Gateway IoT.

Mobile‐as‐a‐Gateway IoT

#BHASIA @BlackHatEvents

## Slide 5

Dilemma: Remote access control management vs. offline availability

1. Remotely share/revoke access to/from an invitee. (Good for Airbnb business)

2. Offline availability: Access the IoT device even without Internet connections.

3. Contradicting with each other?

#BHASIA @BlackHatEvents

## Slide 6

# Research targets and results

1. We pick 10 popular real-world MaaG IoT devices (smart locks and item trackers).

2. We can identify critical flaws in their access control management.

#BHASIA @BlackHatEvents

## Slide 7

# Threat Model

1. The attacker (temporary user) has full access to their own mobile device. E.g., through jailbreaking/rooting.

2. The cloud service, the owner’s mobile phone, and the IoT device are benign.

#BHASIA @BlackHatEvents

## Slide 8

# Threat Model

1. The attacker (temporary user) has full access to their own mobile device.

   - E.g., through jailbreaking/rooting.

2. The cloud service, the owner’s mobile phone, and the IoT device are benign.

Share/Revoke

#BHASIA @BlackHatEvents

## Slide 9

# Threat Model

1. The attacker (temporary user) has full access to their own mobile device. E.g., through jailbreaking/rooting.

2. The cloud service, the owner’s mobile phone, and the IoT device are benign.

Share/Revoke

#BHASIA @BlackHatEvents

## Slide 10

# Attack scenario

1. After the access is shared to the attacker, can the attacker:

   - I. retain access permanently,

   - II. distribute such access further,

   - III. escalate their privilege?

Share/Revoke

#BHASIA @BlackHatEvents

## Slide 11

# Security Flaws

1. Flaws in MaaG Access Model Translation

2. Flaws in MaaG Policy Synchronization

#BHASIA @BlackHatEvents

## Slide 12

## Flaws in MaaG Access Model Translation

1. Access models are different for the cloud and for the IoT device.

   - I. Why? Because IoT devices lack I/O interfaces, need to reduce cost… II. Thus, it needs Access Model Translation.

AMT

ID Auth Role Privilege Delegation

Credential Attributes

#BHASIA @BlackHatEvents

## Slide 13

## Flaws in MaaG Access Model Translation

2. Is the AMT process semantically sufficient?

E.g., Does the translated attributes maintain user IDs/privileges?

3. Unfortunately, NO.

More generally, loss of semantics in the AMT process.

I’m unable to tell a
guest from an admin!
userID/
privilege ??
credential credential

#BHASIA @BlackHatEvents

## Slide 14

# Flaws in MaaG Policy Synchronization

1.  Policy sync messages must route through the untrusted mobile phone using two kinds of protocols.

   - I. No direct connection between the cloud and the IoT device.

   - II. Subject to reorder/drop/replay.

Untrusted IoT Device
Cloud
HTTPS Bluetooth

#BHASIA @BlackHatEvents

## Slide 15

m1 Grant access m1 Grant access (Applied)
m2 Reset m2 Reset (Applied)
vs.
m1 Grant access m2 Reset (Ignored)
m2 Reset m1 Grant access (Applied)
Result: User is still on the lock!

#BHASIA @BlackHatEvents

## Slide 16

### Mitigating Vulnerabilities in MaaG Access Control

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
ASIA 2023
Mitigating Vulnerabilities in MaaG Access Control
Benign Untrusted Benign
Cloud Service Mobile Device 4 pre-guthentication token loT Device
3. —- @
{nonce, On_Device_Policy} 2. {nonce, On_Device_Policy} —"
<a
we; =
4 5,
{nonce, Policy_Delta}
[{nonce, Policy Delta},
session_key, encrypted_session_key]
Legend: DCKey
Figure 5: Secure Access Policy Synchronization (SAPS) Protocol
```

## Slide 17

# Key Takeaway

1. We find design level problems in the Mobile-as-a-Gateway IoT architecture.

2. Access Model Translation and Access Policy Synchronization are vulnerable for existing Mobile-as-a-Gateway IoT devices.

3. We design a novel protocol to mitigate these flaws.

#BHASIA @BlackHatEvents

## Slide 18

## Demo Time: August/Yale Smart Lock Attack

Video Link: https://youtu.be/LjpVVLhUrtk

#BHASIA @BlackHatEvents

## Slide 19

# Q&A Time

#BHASIA @BlackHatEvents
