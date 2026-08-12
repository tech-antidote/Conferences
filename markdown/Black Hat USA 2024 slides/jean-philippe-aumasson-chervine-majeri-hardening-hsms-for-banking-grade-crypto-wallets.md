---
title: "Hardening HSMs for Banking-Grade Crypto Wallets"
speakers: ["Jean-Philippe Aumasson", "Chervine Majeri"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Jean-Philippe Aumasson & Chervine Majeri_Hardening HSMs for Banking-Grade Crypto Wallets.pdf"
pages: 45
sha256: "db3c4a385f15e26660dcb4a1e11b79f3084b2c0d82a5c47344e8283fccadae42"
text_chars: 13560
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:33:10Z"
---
# Hardening HSMs for Banking-Grade Crypto Wallets

**Speakers:** Jean-Philippe Aumasson, Chervine Majeri  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Jean-Philippe Aumasson & Chervine Majeri_Hardening HSMs for Banking-Grade Crypto Wallets.pdf` (45 pages)


## Slide 1

**Hardening HSMs for** **~~-~~ Banking Grade Crypto Wallets Black Hat 2024**

**JP Aumasson, Chervine Majeri**

## Slide 2

Whois

## **JP**

- Taurus co-founder & CSO

- First BHUS talk was in 2013

**Chervine**

- Taurus lead research engineer

- First BHUS talk is now

Crypto asset custody & issuance for banks (taurushq.com) regulated and running a marketplace for tokenized assets (t-dx.com) In Geneva, Zurich, London, Paris, Vancouver, Dubai

## Slide 3

Outline

**1. What is really an HSM? 2. Security and crypto internals 3. Attack surface and hardening 4. Best practices & a note on cloud HSMs**

<u>Disclaimer: This talk is based on our experience over 7 years with 3 HSM</u> models, deployed in production in multiple environments. YMMV.

## Slide 4

Hardware security module (HSM)

“A dedicated crypto processor that is specifically designed for the protection of the crypto key lifecycle” (HSM vendor) Enterprise/cloud HSMs usually 1RU or PCIE card form factor The actual HSM is the module in the appliance/card

## Slide 5

HSM purpose

Store **secret keys** for crypto operations: ▪ Signature, decryption, symmetric encryption, MAC

High-assurance domain thanks to isolation & anti-tampering Protect keys in case of servers/workstations compromise

## Slide 6

HSM use case examples

- **Blockchain** transaction signing and TEE

- Code signing (HSM mandatory for MS Win apps)

- Database encryption/decryption (usually via KEKs)

- PKI root of trust (for CAs, enterprise PKIs, etc.)

https://www.flickr.com/photos/okolkman/22789012910/in/album-72157661146853781/

## Slide 7

HSM interfaces

Crypto interface over **PCIe or USB** , **TCP/IP if** network-attached Admin interface over serial port, **SSH** , **HTTP/REST** + **TLS** , **GUI**

## Slide 8

Security mechanisms (1/4)

• Local isolation (slots aka partitions)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Security mechanisms (1/4)
¢ Local isolation (slots aka partitions)
HSM Partitions
HSM Partitions are independent logical HSMs that reside within the SafeNet
HSM inside, or attached to, your host computer or appliance. |S=TeastsiV/
Partition has its own data, access controls, security policies, and separate
dministration access for at least some roles, independent from other HSM
eelatitceyats (if your HSM supports more than one). Depending on the product,
the HSM can contain multiple HSM partitions, and each partition can be
associated with one or more Clients. Each HSM Partition has a special
administrative account or role, who manages it.
Partition Roles
Logging In to the
Application Partition
Initializing Crypto Officer
and Crypto User Roles
for an Application
Partition
Changing a Partition Role
Credential
Resetting the Crypto
Officer, Limited Crypto
Officer, or Crypto User
Credential
Activation on Multifactor
Quorum-Authenticated
Partitions
```

## Slide 9

Security mechanisms (2/4)

• Local isolation (slots aka partitions) • RBAC, ABAC-ish model (with per-slot roles)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User Roles
Administration Security
Officer (ASO)
Security mechanisms (2/4)
Administrator
Security Officer (SO)
Token Owner (User)
¢ Local isolation (slots aka partitions)
¢ RBAC, ABAC-ish model (with per-slot roles)
Unauthenticated Users
Administration Security Officer (ASO) Administrator
This user knows and can present the Admin Token SO PIN. The ASO’s main role is to introduce the This user knows and can present the Admin Token User PIN. The following ices are available to the Administrator
Administrator to the module. The following services are available to the ASO: Set or change Real Time Clock (RTC) value
Set the initial Administrator PIN value (ASO cannot change it later)
Set the CKA_TRUSTED attribute on a Public object
Set the CKA_EXPORT attribute on a Public object
Exercise cryptographic services with Public objects
Create, destroy, import, export, generate and derive Public objects
Can change his/her own PIN
Read the System Event Log
Purge a full System Event Log
Configure the Transport Mode feature
Specify the security policy of the HSM
Create new SafeNet ProtectToolkit-C slots/tokens and specify their labels, SO PINs, and minimum PIN Length
Initialize smart cards and specify their labels and SO PINs
Destroy individual SafeNet ProtectToolkit-C slots/tokens
Erase all HSM secure memory, including all PINs and User Keys
Perform firmware upgrade operations
Manage Host Interface Master
Exercise cryptographic Wi blic objects on the Admin Token
```

## Slide 10

Security mechanisms (3/4)

• Local isolation (slots aka partitions)

• RBAC model (with per-slot roles)

• PKCS#11 Cryptoki API

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Security mechanisms (3/4)
¢ RBAC model (with per-slot roles)
¢ PKCS#11 Cryptoki API
Bit Flag Mask [Meaning
0x00000001 True if the mechanism is performed by the
device; false if the mechanism is
performed in software
CKF_ENCRYPT 0x00000100 True if the mechanism can be used with
C_Encryptinit
CKF_DECRYPT 0x00000200 True if the mechanism can be used with
C_Decryptinit
CKF_DIGEST 0x00000400 True if the mechanism can be used with
C_Digestinit
CKF_SIGN 0x00000800 True if the mechanism can be used with
C_Signinit
¢ Local isolation (slots aka partitions)
5.9 Decryption functions
Cryptoki provides the following functions for decrypting data:
¢ C_Decryptlnit
CK_DEFINE_ FUNCTION (CK_RV, C_DecryptInit) (
CK_SESSION_ HANDLE hSession,
CK_MECHANISM PTR pMechanism,
CK_OBJECT HANDLE hKey
i
C_Decryptlnit initializes a decryption operation. hSession is
the session’s handle; pMechanism points to the decryption
mechanism; hKey is the handle of the decryption key.
The CKA_DECRYPT attribute of the decryption key, which
indicates whether the key supports decryption, MUST be
CK_TRUE.
```

## Slide 11

Security mechanisms (4/4)

• Local isolation (slots aka partitions)

• RBAC model (with per-slot roles)

• PKCS#11 Cryptoki API

- FIPS 140-2/3 certified crypto and anti-tampering controls

## Slide 12

Security mechanisms (5/4)

• Local isolation (slots aka partitions)

• RBAC model (with per-slot roles)

• PKCS#11 Cryptoki API

• FIPS 140-2/3 certified crypto and anti-tampering controls

May NOT include:

• Software exploit mitigations like ASLR and DEP

• Remote attestation mechanism

## Slide 13

Internals overview (1/2)

- System-on-chip with a PPC core and crypto accelerators

- Some minimal Linux distrib, some bootloader

- Crypto software libraries

- Signed firmware updates

## Slide 14

Internals overview (2/2)

• Crypto support: mainly FIPS incl. legacy algorithms

• “True RNG” seeding a NIST 800-90A DRBG

## Slide 15

Custom modules

- Firmware extension software component loaded by users

- Replace the original firmware’s init()

- Must be developed C, using the vendor’s SDK

• Size limitation (ex: 8MB)

## Slide 16

What could go wrong (1/3)

• Compromised caller creds = free HSM requests (no filtering) • PKCS#11 intrinsic flaws and limitations (see Ledger’s paper) • Bugs in the PKCS#11 implementation and HSM runtime

### SSTIC 2019

https://blog.inhq.net/posts/yubico-yubihsm-pkcs-vuln/

## Slide 17

What could go wrong (2/3)

- Knowns bugs in outdated OSS components (regreSSHion?)

- Cross-slot attacks (DoS, info leak, code exec?)

- Malicious custom module / supply-chain issues

- RNG issues (remember ROCA?)

## Slide 18

What could go wrong (3/3)

Various HSM bugs:

- Remove a directory from the FS crashes if the name ands with “/”

- Logging "too much" (1 log per message) freezes the HSM freeze, needing a power-cycle

- Client-side segfaults with certain ECC crypto interfaces

- Inconsistent crypto interface between firmware versions

## Slide 19

HSM hardening

A quick tour of measures proposed to harden HSMs

• Deployed in production

- Known tricks for “power users”

- Most won’t work with cloud HSMs

## Slide 20

1/6: Attack surface reduction

• PKCS#11 API override, to only allow “authorized” usage/args • Use directly the filesystem (rather than PKCS#11 objects)

## Slide 21

2/6: Enforce secure configuration

Custom code can enforce that attributes of PKCS#11 objects  are the most restrictive, and stop its operations otherwise

**Ex** : Ensure that secret key are marked as CKA_SENSITIVE and not CKA_EXTRACTABLE.

## Slide 22

-
3/6: In HSM business logic

Move business logic from servers/VMs to the HSM **Ex** : Create blockchain transactions (signature, payload) after enforcing a multi-sig  quorum and governance rules

**Benefits** :

• Computation integrity and confidentiality protected

• Can interact with in-HSM crypto objects

**Risks** : Bugs leading to secrets leak or code execution

## Slide 23

-
4/6: Application level *AC

- Roles = **users** (request approvers), **admins** (rules  approvers)

- Admins sign rules defining authorized quorums

- Users and admins sign with **hardware tokens**

Only admin pubkeys in the HSM Tricks needed to prevent replay and downgrade

## Slide 24

-
5/6 Application level secure channel

HSMs may support secure channels, but only at the network level, or offer  insufficient security (anon DH in old HSMs) If the consumer of the HSM response is not the host talking to the HSM, application-level security  is needed (aka e2ee)

## Slide 25

-
6/6: Minimize black boxing

The proprietary HSM code is generally not open-source, therefore harder to review for bugs, let alone fix them **Alternative** : integrate code from auditable/OSS libraries via the custom modules (may need tweaks/optimization/stripping) Exception: **randomness** : HSM’s PRNG and entropy sources Can post-process with a custom DRBG

## Slide 26

Why a state?

**Stateless** HSMs are convenient and simple to manage

• Multiple instances behind a load balancer

• Immutable state configured once in a key ceremony

However, **statefulness** often needed for

• Anti-replay, anti-downgrade (ex: monotonous counter)

• Enforcement of security policies (ex: via timestamps)

## Slide 27

Challenges of HSM states

- HSMs’ storage is limited, and I/O is slow

- High-availability needs at least 2 redundant HSMs

- State bounded in size (must fit in a ~2MB message)

- State transitions must be verifiable

Solution: **trees** !

## Slide 28

Merkle trees & Merkle proofs

Principle: only reveal state components needed by a request • Encode the state as a Merkle tree

• Admins sign the root, verified in the HSM

• Merkle proofs

What if the state (thus root) changes? How to **verify state changes given a partial state** ?

## Slide 29

Merkle trees limitations

A root represents a list of data nodes Logarithmic membership proof size

Read-only trees are easy…

How to insert/delete?

- Where to insert the data?

- How to efficiently “rebalance” the tree?

## Slide 30

-
Red black trees

• Allow updates on **partial** trees

- Keep Merkle-tree property

- Bounded height of at most 2log( _N_ +1) with _N_ nodes

- **Self-balancing** via simple “coloring rules”

`o` RB1: Root is black

`o` RB2: Any path from a node to a leaf has the same number of black nodes `o` RB3: There can’t be an edge between two red nodes

## Slide 31

Tree examples

- Rebalancing performed through **rotations**

- Rotated subtrees preserve **RB** and **Merkle** properties

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Tree examples
¢ Rebalancing performed through rotations
¢ Rotated subtrees preserve RB and Merkle properties
——Right Rotation——>>
@— Left Rotation
```

## Slide 32

Tree insertion

- Rebalancing is **recursive** over the height of the tree

- • Carries on so long as the parent P is **red**

## Slide 33

Tree insertion

• Case 1:

`o` Parent **P** and uncle **U** are both red

## Slide 34

Tree insertion

• Case 1:

`o` Parent **P** and uncle **U** are both red

- Solution:

`o` Recolor both **P** and **U** to black `o` Recolor **GP** to red `o` No impact on subtrees

## Slide 35

Tree insertion

• Case 2:

`o` Uncle **U** is black `o` **X** is the left child of **P**

## Slide 36

Tree insertion

• Case 2:

`o` Uncle **U** is black `o` **X** is the left child of **P**

• Solution `o` Recolor **P** and **GP** ▪ Breaks RB2

## Slide 37

Tree insertion

• Case 2:

`o` Uncle **U** is black `o` **X** is the left child of **P**

• Solution `o` Recolor **P** and **GP** `o` Rotate **GP** to the right `o` Subtrees not impacted

## Slide 38

Tree insertion

• Case 3:

`o` Uncle **U** is black `o` **X** is the right child of **P**

## Slide 39

Tree insertion

• Case 3: `o` Uncle **U** is black `o` **X** is the right child of **P**

- Solution

`o` Rotate **P** to the left `o` Brings us back to case 2 with **P** and **X** swapped

## Slide 40

Tree conclusion

- **Red-black** and **Merkle** properties can be combined in a single structure

- • Lets us perform **state transitions** on large datasets **within** a low-memory **HSM**

- Inserting a user to a set of 1M requires revealing 20-40 users

## Slide 41

Best practices (1/2)

# **Software defense**

- Keep the HSM firmware updated

• Tighten PKCS#11 attributes (to the minimum needed)

• Enable security features (secure channel)

- Custom code: minimize dependencies

• Custom code: have solid build/deploy integrity (see SLSA.dev)

## Slide 42

Best practices (2/2)

# **Access control**

- Segregate accesses and credentials (admin/SO, slot user/SO)

- • Minimize network exposure (no internet facing, whitelisting)

# **Key management**

- Generate critical keys in key ceremonies (in- or off-HSM?)

- Have reliable & tested back-ups and DR procedures

Use **HSM back-up/cloning** ?

## Slide 43

On cloud HSM aka HSMaaS

Convenient cloud-based systems, notably as KMS back-end

Limitations:

- Access may be indirect via some cloud middleware

- May be multi-tenant, sharing hardware with other users

- Limited capability to configure the HSM and PKCS#11 settings

- Impossible to run custom code

- How to be sure it’s really an HSM and not an emulator?

## Slide 44

Conclusion

**HSMs + in-HSM** custom logic is a powerful setup suitable for various high-assurance security systems, but requires significant investment in

- Bespoke hardening to reduce the attack surface

- Management of compute and storage limitations

- SDLC integrity and QA

- HSM model/vendor-specific shenanigans

## Slide 45

**Thank you**

**A joint work with the Taurus team Acknowledgements: André S., Antony V., Mattia T., Ryan H., Stefano Z., Tal B.** **<u>https://taurushq.com</u>**
