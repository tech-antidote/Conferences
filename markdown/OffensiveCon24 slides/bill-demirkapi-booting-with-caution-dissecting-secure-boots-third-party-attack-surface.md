---
title: "Booting with Caution Dissecting Secure Boot's Third-Party Attack Surface"
speakers: ["Bill Demirkapi"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2024"
edition: ""
year: 2024
source_pdf: "OffensiveCon24 slides/Bill Demirkapi_Booting with Caution Dissecting Secure Boot's Third-Party Attack Surface.pdf"
pages: 68
sha256: "325140f92e153bd2f8e728360b558337ed58f8c169af9c6fa5baa17992064561"
text_chars: 22306
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:55:55Z"
---
# Booting with Caution Dissecting Secure Boot's Third-Party Attack Surface

**Speakers:** Bill Demirkapi  
**Conference:** OffensiveCon 2024  
**Source:** `OffensiveCon24 slides/Bill Demirkapi_Booting with Caution Dissecting Secure Boot's Third-Party Attack Surface.pdf` (68 pages)


## Slide 1

**Booting with Caution** Dissecting Secure Boot’s Third-Party Attack Surface

Bill Demirkapi

## Slide 2

# **Who Am I?**

 Security Engineer at the Microsoft Security Response Center.  Background in low-level OS internals and cloud security.

 Worked with Secure Boot for over a year.

 Born in Berlin!

## Slide 3

**Intro to Secure Boot**

## Slide 4

# **What is Secure Boot?**

- UEFI **Secure Boot** is a security feature designed to prevent malicious software from loading when your PC starts.

- **TLDR** : Make sure code executed during boot is signed and trusted.

**Source** : EDK2 Repository

## Slide 5

# **What is Secure Boot?**

- UEFI firmware exposes dozens of crucial API functions that are intended to provide basic, **universal** functionality.

- **Example** : LoadImage allows you to load a UEFI driver.

   - With Secure Boot **on** , images must have a valid signature.

   - But how does the firmware know who to trust?

**Source** : Eclypsium

## Slide 6

# **What is Secure Boot?**

- The DB and DBX variables control **what can** and **cannot** load.

- Most common format for entries is SHA256 (Authenticode) hashes and X509 certificates.

- Updates can specify allowed/denied.

**Source** : UEFI Specification

## Slide 7

# **What is Secure Boot?**

- The signature databases are stored as **_authenticated_** variables.

- They can always be read, but only written if the variable data is…

   - Signed with the private half of a key exchange key (KEK variable)

   - Or a platform key (PK variable).

- Every signed update payload also needs to specify an operation.

   - This is typically an “append write” (merge with existing variable).

- **Protects against rollback and empowers our patching capability.**

## Slide 8

# **What is Secure Boot?**

- On machines that ship Windows, two common DB entries include…

   - _Microsoft Windows Production PCA 2011_ = First-Party Images like bootmgr

   - _Microsoft Corporation UEFI CA 2011_ = Third-Party Images like the Linux "shim"

- The **UEFI CA** is why Linux works out of the box, even with Secure Boot enabled.

**Source** : Ubuntu Wiki, Secure Boot Testing

## Slide 9

# **Secure Boot Threat Model**

- **When on** , Secure Boot is responsible for the code integrity **of your boot environment** .

- **When off** , you can already execute untrusted code “by design”.

- This is why MSRC calls them Security Feature Bypasses.

- There is no vulnerability without the security feature!

## Slide 10

# **Secure Boot Threat Model**

 There is often a high bar for abusing Secure Boot vulnerabilities.

- Secure Boot is still a critical feature for enabling a chain of trust.

|**Vector**|**Attack Surfaces**|
|---|---|
|Local|EFI Partition, UEFI Runtime Services*|
|Physical|Hardware, EFI Partition, etc.|
|Adjacent|HTTP or PXE Boot|
|Remote (Man-in-the-Middle)|HTTP Boot|

A “ **local** ” attacker with Admin+ code execution wants to persist in the boot environment.

A **physical** attacker wants to install a bootkit or steal encrypted data.

An **adjacent** attacker wants to gain code execution on machines that use HTTP/PXE boot.

A **remote** man-in-the-middle wants to gain code execution on machines that use HTTP boot.

## Slide 11

# **Example: Secure Boot in Practice**

- Control over signature databases is generally exposed in the BIOS.

- Requires physical access.

- OS can only use signed payloads* to update these variables.

   - Unless Secure Boot is off.

## Slide 12

**Dissecting Secure Boot’s Attack Surfaces**

## Slide 13

# **Common Attack Surfaces**

|**Attack Surface**|**Description**|
|---|---|
|OEM Firmware|Firmware shipped with your device.|
|**Custom OEM Certificates**|Images signed by a custom OEM certificate included in DB.|
|**Third-Party Images**|Images signed by the third-party UEFI CA.|
|**Third-Party Images, Linux Shim**|First-stage bootloader for most Linux distributions.|
|**Third-Party Images, Linux Shim**
**“Second-Stage Images”**|“Second-stage images” signed by custom Linux distribution
certificates.|
|Microsoft Images|Images signed by the first-party Windows CA.|

## Slide 14

# **OEMs: Forking Hell**

- The Embedded Development Kit 2 ( **EDK 2** ) is an open-source and cross-platform firmware development environment.

- Many OEMs use a forked version for their devices.

**Source** : TianoCore Website

## Slide 15

# **OEMs: Forking Hell**

Dump &  Enumerate
Identify Version Known Bugs
Firmware Repository Attacker

**Read more** : _The Firmware Supply-Chain Security is broken: Can we fix it?_ by Binarly

## Slide 16

# **OEMs: Custom Certificates**

- **OEMs** will often ship custom certificates in DB to allow for their code (outside of firmware) to run.

- Unfortunately, these certificates have been found to sign dozens of vulnerable images.

## Slide 17

# **OEMs: Custom Certificates, Case Study**

- In October, I built a PC with an ASUSTeK motherboard.

- Let's dive into the attack surface introduced by my OEM

## Slide 18

# **OEMs: Custom Certificates, Case Study**

- Dump DB & focus on outliers.

**DB Entries**

- How do we find the images allowed by these entries?

   - Microsoft has logs for what is signed via the UEFI and Windows CA, but not custom CAs or hashes.

**ASUSTeK MotherBoard SW Key Certificate**

**ASUSTeK Notebook SW Key Certificate**

Microsoft Corporation UEFI CA 2011 Microsoft Windows Production PCA 2011

**Canonical Ltd. Master Certificate Authority**

**4 Unknown SHA256 Hashes**

## Slide 19

# **OEMs: Custom Certificates, Case Study**

 **VirusTotal** is a malware scanning platform that allows you to search for submissions using filters.

## Slide 20

# **OEMs: Custom Certificates, Case Study**

- Unfortunately, the Canonical certificate was used to sign several vulnerable shim boot loaders.

- **Fun Fact** : Canonical does not want their old certificate included.

## Slide 21

# **OEMs: Custom Certificates, Case Study**

- What about the **4 unknown SHA256 hashes** ?

- Turns out they hardcoded decade old Windows boot managers with known vulnerabilities!

## Slide 22

# **OEMs: Custom Certificates**

- This is not just an ASUSTeK problem. This is an industry problem.

- Most OEMs ship custom certificates.

- Firmware has the same problem: lack of oversight from OEMs.

- With custom DB entries, **it’s up to your OEM** to decide what they include, and what to revoke.

## Slide 23

# **Third-Party UEFI Images**

- Third-Party UEFI images are where the most security vulnerabilities in UEFI drivers have been discovered.

   - >90% of on-by-default revocations in DBX are for third-party drivers.

- Data Sources for Images include…

   - VirusTotal search using signature filter with third-party CA thumbprint.

   - Eventually, internal access to signed images.

## Slide 24

# **Third-Party UEFI Images, Example**

**Read more** : _One Bootloader To Rule Them All_ by Eclyspium


> Recovered by OCR — confidence 93/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Third-Party UEFI Images, Example
° 2 unique shells
: CryptoPro Secure Disk for BitLocker
Read more: One Bootloader To Rule Them All by Eclyspium
```

## Slide 25

# **Third-Party UEFI Images, Example**

- **Problem:** We do not hunt for variants when revoking images.

- Variants can be found trivially by searching for unique strings.

   - In this case, most variants are not on VirusTotal, but that’s not true for other revoked images.

   - **Want to find more bugs? Look for unrevoked variants of revoked EFI images.**

## Slide 26

# **Intro to the Linux Shim**

- **shim** is a software package that works as a first-stage Linux bootloader.

- Microsoft signs shim builds from Linux distros.

- The shim includes the Linux distro’s self-signed certificate and manually loads UEFI drivers signed with it.

## Slide 27

# **Intro to the Linux Shim**

- The shim has an interesting revocation mechanism known as “UEFI Secure Boot Advanced Targeting” ( **SBAT** ).  Images are built with an “.sbat” PE section that specifies version info and other metadata.

   - SBAT revocations are stored in the “SBAT” UEFI variable.

- **Example:** GRUB2 has a vulnerability.

   - Instead of adding every GRUB2 image hash to DBX, a single SBAT revocation can revoke all GRUB2 images below a certain version.

\```
sbat,1,SBAT Version,sbat,1,https://github.com/rhboot/shim/blob/main/SBAT.md
grub,2,Free Software Foundation,grub,2.04,https://www.gnu.org/software/grub/
\```

**Example SBAT Entry**

## Slide 28

# **Intro to the Linux Shim**

- The Linux community has a repository known as **shim-review.**

- Practically any distribution of Linux can ask for their shim to be signed.

- Distros fill out a questionnaire, like the UEFI CA signing process.  Requires approval from trusted developers.

## Slide 29

# **The Linux Shim: Governance Issues**

- In 2020, there were major issues found in GRUB2 by Eclypsium. Dubbed “BootHole”.

- GRUB2 is loaded by shim, so to revoke the secondary GRUB images, you need to revoke the shim.

- **Problem:** Not all “pre-SBAT” shims were revoked in 2020.

- **Problem:** Linux vendors reused their certificates from past shim builds that have signed vulnerable GRUB2 code.

## Slide 30

# **The Linux Shim: Governance Issues, Example**

 Found a few dozen forgotten pre-SBAT shim images that were not revoked with nothing but VirusTotal.

Download files signed with UEFI CA

.data.ident contains version & commit of build

Exclude revoked
images

Filter for “UEFI
SHIM”

Filter version and
SBAT support

Leftover images are exploitable

## Slide 31

# **The Linux Shim: Governance Issues, Example**

**Example of a Shim-Review Response That Violates Policy**

- This is an example shim-review submission following SBAT’s introduction in 2020 in response to “BootHole”.

- **Question:** Did the vendor revoke old vulnerable GRUB2 images or are they using a new key?

- **Vendor:** We use the same key, but since old GRUB2s don’t have SBAT, their shim won’t load them.

## Slide 32

# **The Linux Shim: Governance Issues, Example**

**Example of a Shim-Review Response That Violates Policy**

- Why does revoking old GRUB2s or using a new key matter?

- **Shim does not require SBAT for “chain loaded” images.**

New shim

No SBAT

Image

New shim

New GRUB2

No SBAT Image

## Slide 33

## **The Linux Shim: Second-Stage Images**

- GRUB2 uses the “shim protocol” to verify images.

- Executables that come after GRUB2 are “second-stage” images.

- No Microsoft involvement.

## Slide 34

# **The Linux Shim: Second-Stage Images, Example**

 **Problem:** We have no _direct_ visibility into “secondary images”.  Every Linux image is more attack surface for Windows customers (and vice-versa).  **Solution:** Do our best with VirusTotal!

Download UEFI CA Images

Download Secondary Images

.vendor_cert section uses DER format

Enumerate Vendor Certificates

Filter for “UEFI SHIM”

Filter version and SBAT support

Leftover images are exploitable

## Slide 35

# **The Linux Shim: Second-Stage Images, Example**

- Until late 2023, Fedora used the same certificate created in 2012.

- Why is this a problem?

   - **You don’t need SBAT when chain-loading.**

   - **An attacker can use a pre-SBAT GRUB2 image with the latest shim.**

## Slide 36

# **The Linux Shim: Recap**

- There are still vulnerable shims built before SBAT that never got revoked in DBX.

- Vendors reuse the same self-signed certificates across shim builds, even when there is a security fix.

- Look for commits with security impact that weren’t handled as a security issue.

- Sometimes revocations are done with SBAT only, leaving Windows users exposed.

## Slide 37

# **The Linux Shim: Recap**

- Microsoft has a close relationship with several Linux distributions that help developed the shim.

- **How do we balance customer choice with customer security?**

- **To what extent should we put most customers at risk to support minority use cases?**

## Slide 38

# **Microsoft Images**

- While the third-party attack surface is large, we’re far from perfect.

- **Problem:** We often don’t revoke vulnerable Windows boot managers because of compatibility.

- These are ecosystem challenges, not vendor-specific.

## Slide 39

**Secure Boot Architectural Challenges**

## Slide 40

# **Problem #1: Limited Response Capability**

- Significant increase in vulnerabilities impacting Secure Boot in the past five years.

   - It’s not that we’re writing more vulnerable code.

   - More people are looking at what we’ve distributed for years.

- There are already hundreds of revoked images, and our space is running out…

## Slide 41

# **Problem #1: Limited Response Capability**

- DBX was only designed to revoke roughly ~600 to ~800 unique hashes.

   - Before Windows 10 1709 hardware requirements, OEMs were only required to support **32 KB of space** for individual UEFI variables.

   - DBX allows us to revoke by hash or certificate.

   - **One vulnerability can exist in thousands of builds of the same driver.**

- **Defenders have their hands tied behind their back.**

#### **Size of DBX in Kilobytes**

16
14
12
10
8
6
4
2
0
10-Apr-18 10-Apr-19 10-Apr-20 10-Apr-21 10-Apr-22 10-Apr-23

## Slide 42

# **Problem #1: Limited Response Capability**

- Outside of limited space, DBX doesn’t work for everything.

- Great example is **Option ROMs** (OROMs).

   - Firmware included with hardware designed to help the machine interact with the device.

   - What happens when there is a vulnerability in an OROM?

   - If we revoke, hardware with impacted OROM will likely not function.

   - No one thought it would be a good idea to sign Option ROMs with a separate CA (until now).

- Tough balance between customer experience and security.

## Slide 43

# **Problem #1: Limited Response Capability**

 UEFI “Security Response Team” is designed to coordinate issues.

- **Decentralized nature of OEMs substantially increases time-to-respond.**

**Source** : Decoding UEFI Firmware

## Slide 44

# **Problem #2: Substantial Attack Surface**

The attack surface our customers are exposed to **by default** at the boot stage is massive.

- We sign too much code.

- We lack proper governance over Secure Boot.

- We are often at the mercy of our partners.

## Slide 45

# **Problem #3: Complexity**

- Secure Boot has only been around for a little over a decade.

   - Understanding how it works is challenging and has a steep learning curve.

- Impact is generally limited to privileged attackers.

- But… many of the issues we’ve discussed aren’t crazy vulnerabilitiesthey come from fundamental process gaps.

## Slide 46

**Case Study of a Critical Linux Shim Vulnerability**

## Slide 47

# **Background**

- While investigating the Linux shim for low hanging fruit, I began assessing their threat model.

- **What attack vectors were relevant to the shim?**

- To start, let’s build a mental map about how the shim works.

## Slide 48

# **Attack Surfaces**

- GNU EFI Library Initialization

- **Secure Boot Advanced Targeting**

- Mok Initialization

- Load Options

- **PE parsing for Authenticode signatures**

- **Flexible file systems**

   - Shim supports local, PXE, and HTTP boot.

   - PXE/HTTP use a “virtual file system” (UDP and HTTP respectively).

Initialize GNU EFI  Update SBAT and
Library Check If Revoked
Parse Options &
Initialize Mok State
Install Protocol

Verify GRUB2
Authenticode
Signature
Good Signature Bad Signature

“Manual Map”  Run “Fallback”
GRUB2 Module

## Slide 49

# **Tangent: Fuzzing the Shim**

- How do you fuzz an EFI boot loader?

   - **Start with unit tests. They’re typically designed to run independently.**

   - Copy out the component into your project and reimplement imports.

- **SBAT** : Copied out code.

- **Authenticode Parsing** : Replaced unit test compiler with AFL++.

- Unfortunately, only found out-ofbounds reads

## Slide 50

# **Network Boot**

- Shim has a small footprint. Manually reviewed Network Boot code.

- UEFI specification includes HTTP support.

   - Shim uses the device it was started with.

   - **Example:** If you start shim with HTTP boot, it will load GRUB2 from the same HTTP server.

Initialize HTTP  Configure  Send a  Receive a
Protocol HTTP Protocol Request Response

Store Headers  Allocate Buffer
Copy Sent Data
in Temporary  using
to Buffer
Stack Buffer Content-Length

Can you spot the vulnerability?

## Slide 51

# **CVE-2023-40547**

- Content-Length is set by the untrusted server.

- Server has control over the buffer that the response is copied into…

Attacker
Controlled
OOB-W

## Slide 52

# **Triggering the Bug**

- How do we abuse control over the receive buffer using the Content-Length header?

- Wrote a Python HTTP server:

   - Return a Content-Length of 1.

   - Return well more than 1 byte of data.

## Slide 53


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attacker Victim
Start HTTP Boot over [Pu4.
ral root @test-Virtual-Machine: /home/test/HTTPBOOT Q — - a x
root@test-Virtual-Machine: /home/test/HTTPBOOT# python3 mycoolbadserver .py
Networ
Capturing from virbro
Eile Edit View Go Capture Analyze Statistics Telephony Wireless Tools Help
dhcp or http
No. Time Source Destination Protocol Length Info
2 ©.000238475 192.168 .106 255.255.255.2 DHCP 346 DHCP Offer Transaction ID ®x8d1i
```

## Slide 54

# **Fixing the Bug**

A “patch” was released in January 2024. **Are customers protected?**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fixing the Bug
CVE-2023-40547 - avoid incorrectly trusting HTTP headers
When retrieving files via HTTP or related protocols, shim attempts to
allocate a buffer to store the received data. Unfortunately, this means
getting the size from an HTTP header, which can be manipulated to
specify a size that's smaller than the received data. In this case, the
code accidentally uses the header for the allocation but the protocol
metadata to copy it from the rx buffer, resulting in an out-of-bounds
write.
This patch adds an additional check to test that the rx buffer is not
larger than the allocation.
Resolves: CVE-2023-49547
Reported-by: Bill Demirkapi, Microsoft Security Response Center
Signed-off-by: Peter Jones <pjones@redhat. com>
A “patch” was released in January 2024.
Are customers protected?
```

## Slide 55

# **Fixing the Bug**

- Fortunately, code comes after shim’s SBAT revocation checks.

- Unfortunately, we must revoke every shim built in almost a decade.

- This will break all Linux recovery media on updated machines.

- **Windows:** Targeting this summer with special compatibility checks.

- **Linux:** Unclear timeline.

## Slide 56

# **Unique Attack Surface**

 **Remember:** shim uses the device it was started with to load images.  Can we trick shim into using HTTP boot?

**Source** : GRUB Manual

## Slide 57

# **Unique Attack Surface**

 You can use HTTP boot from the local, adjacent, and remote vectors!  **This means that the vulnerability can be abused from almost every vector Secure Boot is exposed to!**

Shim ( Local )

GRUB2 ( Local )

HTTP Device
Syntax

Shim (HTTP)

Content Length
Exploit

Attacker Server

Shim ( PXE )

GRUB2 ( PXE )

HTTP Device
Syntax
Shim (HTTP)

Content Length
Exploit
Attacker Server

## Slide 58

# **Review**

- This code is not new. It was committed 8 years ago.

- Trivial vulnerability. Significant impact.

- Challenging to fix. Rollback vector strikes again.

Thanks to the Shim maintainers who patiently answered questions!!

## Slide 59

**Where Do We Go From Here?**

## Slide 60

# **Shifting Security Left**

- Before MSRC invested in Secure Boot, Engineering implemented a “Secure Version Number” (SVN) revocation mechanism.

   - Early self-revocation check in first-party images that used a custom UEFI variable.

   - Like SBAT, no reliance on DBX.

- **Problem:** It was not enforced across all first-party images.

- **Problem:** There was substantial attack surface before the SVN check.

- **Problem:** Like SBAT, it can be bypassed “by design”, because the SVN variable is unauthenticated.

## Slide 61

# **Shifting Security Left**

- Revocation via Embedded Secure Version Information ( **REVISE** )

- **REVISE** was a proposal by MSRC to combine SVN with DBX.

   - How? We can revoke any hash we want via DBX.

   - SHA-256 hashes have 32 bytes of space.

- What if we “smuggled” version data through a “fake hash” that only our code recognized?

- We still run into DBX space limitations, but with one hash entry, we can revoke thousands of images by version.

Use special GUID to mark entries containing version data. Fake hash with version data.

## Slide 62

# **Shifting Security Left**

- **REVISE was released in April 2024!**

 We are exploring opportunities to bring REVISE to Shim’s SBAT.

- Combine security and subject-matter experts early in development.

**Source** : Decompiled Bootmgr from April 2024

## Slide 63

# **Mitigating Secure Boot**

### **Recommendations to Address Third-Party Risk 2 - 4 Year Timeframe**

Leverage Intentional Fragmentation of DB(X)

Be Firm, But Listen

Deliver Firmware Updates via OS

Be Transparent About All Changes

Provide SB Visibility & Control to End-Users

Deprecate Most UEFI CA Use Cases

Revisit Minority Use Cases & Customer Impact

Improve UEFI CA Review Pipeline

Invest In Secure & Measured Boot

Revisit “By Design” Bypasses (e.g., Mok)

## Slide 64

# **Mitigating Secure Boot**

- There may be more third-party UEFI CA modules with vulnerable code than there is space in DBX.

- How do we address this?

   - Medium- to long-term: revoke the UEFI CA. It is already being rolled in the next two years.

   - But this breaks old Option ROMs.

- **Our best bet in the short-term is measured boot.**

## Slide 65

# **What Can You Do To Protect Your Organization?**

- **Windows Users:** Enable BitLocker to kill every UEFI CA vulnerability discussed.

   - Still vulnerable to other issues from firmware bugs or first-party images.

   - Working on improving BitLocker to address first-party downgrade attacks.

      - Using Group Policy, you can enable a stricter level of measurements to kill even first-party downgrade attacks.

- **Linux Users:** It depends.

   - **Canonical Users:** Enable TPM-based Full Disk Encryption (when released)

   - No easy mechanism like BitLocker exists from the OS itself

   - A gap Linux can improve on in the long-term.

## Slide 66

# **Areas for Further Research**

- If you want to target third-party code…

   - Review old signed binaries. Hundreds of unrevoked modules with obvious vulnerabilities.

      - **Example:** Try to find variants of binaries revoked in DBX.

      - **Example:** Look at second-stage images signed with Linux vendor certificates.

   - Fuzz GRUB2. Guaranteed low hanging fruit.

   - Look at interesting ways of abusing signed modules to enter an unexpected state.

      - **Example:** Did you know you can chain shim -> GRUB2 -> shim?

- If you want to target first-party code…

   - Maybe I’ll have time in another talk

- If you have a specific target in mind…

   - Look at everything that is on the OEM to manage, including firmware and custom certificates.

## Slide 67

# **The Elephant in the Room**

- We keep focusing on short-term fixes.

- Secure Boot needs an overhaul to remain defensible.

- We must work together.

pov you work for microsoft

## Slide 68

# **Questions?**

**Massive thank you to the Engineering teams across Microsoft and Linux for their support.**
