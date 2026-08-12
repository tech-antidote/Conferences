---
title: "XUnprotect Reverse Engineering macOS XProtect Remediator"
speakers: ["Koh Nakagawa"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Koh Nakagawa_XUnprotect Reverse Engineering macOS XProtect Remediator.pdf"
pages: 97
sha256: "800f01db2125f8e25a0d61b4c3ac292562310e55d0f7a7aea6c99f4030705975"
text_chars: 36929
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: ["Koh Nakagawa_XUnprotect Reverse Engineering macOS XProtect Remediator_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:57:21Z"
---
# XUnprotect Reverse Engineering macOS XProtect Remediator

**Speakers:** Koh Nakagawa  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Koh Nakagawa_XUnprotect Reverse Engineering macOS XProtect Remediator.pdf` (97 pages)


## Slide 1

# **XUnprotect: Reverse Engineering macOS XProtect Remediator**

Koh M. Nakagawa (@tsunek0h) FFRI Security, Inc.

## Slide 2

## **NSUserFullName()**

• Koh M. Nakagawa (@tsunek0h)

- Security researcher at FFRI Security, Inc.

- Mainly focusing on Apple product security

- Gave talks at Black Hat and CODE BLUE

## Slide 3

## **About This Presentation**

- **This presentation covers:**

`o` Technical deep dive into XProtect Remediator (XPR)

- How XPR’s detection logic works

▪ Malware removed (or ‘remediated’) by each scanner

   - Provenance Sandbox (which XPR utilizes for identifying the source of files being remediated)

- **This presentation does not cover:**

`o` Evaluation of XPR

▪ Such as effectiveness as a macOS security product

`o` Traditional XProtect

▪ For this topic, see Stuart Ashenbrenner's excellent talk at MDOYVR23 ▪ <u>https://youtu.be/43BIK-e7FBE</u>

## Slide 4

## **What You’ll Gain from This Talk?**

###### **Deep understanding of XPR**

Defensive

**Offensive**

**For Blue Teamers:** Learn XPR’s detection/remediation capabilities & Apple-exclusive threat intel

**For Red Teamers:** Learn TCC & Provenance Sandbox bypass

## Slide 5

## **Outline**

###### **1. Introduction**

2. Tooling

3. RE results

4. Vulnerability Research

5. Conclusion

## Slide 6

## **What Is XPR?**

###### **_Three layers of defense_**

_Malware defenses are structured in three layers:_

_1. Prevent launch or execution of malware: App Store, or Gatekeeper combined with Notarization_

_2. Block malware from running on customer systems: Gatekeeper, Notarization, and XProtect_

**_3. Remediate malware that has executed: XProtect[Remediator]_**

_…_

**_XProtect[Remediator] acts to remediate malware that has managed to successfully execute_** _._

- _“_ Apple Platform Security _”_ by Apple

<u>https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf</u>

## Slide 7

## **What Is XPR?**

• Introduced in macOS Monterey as a replacement for the MRT

- Built-in mechanisms and updated once or twice per month

- Contains 20+ scanners, each targeting a specific malware family

<u>https://arstechnica.com/gadgets/2022/08/apple-quietly-revamps-malware-scanning-features-in-newer-macos-versions/</u>

<u>https://eclecticlight.co/2022/08/30/macos-now-scans-for-malware-whenever-it-gets-a-chance/</u>

Each scanner targets a specific malware family (e.g., XProtectRemediatorAdload is a scanner for well-known Adload adware)

## Slide 8

## **Why Is Remediation Needed?**

- Some malware samples bypass the first and second layers of defense: `o` Through supply chain attacks (such as the 3CX supply chain attack) `o` By tricking users into disabling Gatekeeper through social engineering

- Apple needs a way to remove malware that slips through these defenses

<u>https://www.kandji.io/blog/amos-macos-stealer-analysis</u>

<u>https://speakerdeck.com/patrickwardle/mac-ing-sense-of-the-3cx-supplychain-attack-analysis-of-the-macos-payloads?slide=28</u>

## Slide 9

## **Research Motivation**

• From offensive security perspective

`o` XPR scanners are attractive exploitation targets due to their powerful entitlements `o` TCC bypass:

   - Some scanners have FDA entitlement (kTCCServiceSystemPolicyAllFiles)

   - Gergely Kalman’s CVE-2024-40842 (TCC info leak)

- User-to-root privilege escalation:

   - XPR scanners run with both root and user privileges

## Slide 10

## **Research Motivation**

- From defensive security perspective

   - Several malware families targeted by XPR remain unknown

      - Howard Oakley, Alden Schmidt, and Phil Stokes have identified several targets

      - ▪ However, several remain unknown due to limited reverse engineering efforts

   - XPR's remediation logic is unclear

      - Is XPR's remediation simply scanning files with YARA and deleting any that match?

- **_CardboardCutout_** _remains unidentified. …_ **_FloppyFlipper_** _remains unidentified. …_ **_RoachFlight_** _remains unidentified._

- “Why XProtect Remediator scans now take longer” by Howard Oakley <u>https://eclecticlight.co/2025/01/03/why-xprotect-remediator-scans-now-take-longer/</u>

## Slide 11

## **Research Target**

- /Library/Apple/System/Library/CoreServices/XProtect.app `o` Contents/MacOS/XProtectRemediator* `o` Contents/MacOS/XProtect

   - Contents/XPCServices/XProtectPluginService.xpc

- These XPR related binaries are written in Swift

Swift-specific sections

## Slide 12

## **Related Work**

<u>https://alden.io/posts/secrets-of-xprotect/</u>

<u>https://github.com/SentineLabs/XProtect-Malware-Families</u>

<u>https://eclecticlight.co</u>

## Slide 13

## **Outline**

###### 1. Introduction

###### **2. Tooling**

3. RE results

4. Vulnerability Research

5. Conclusion

## Slide 14

## **Static Analysis**

- Binary Ninja

- Stripped Swift Mach-O binaries

- Symbols are stripped, but some symbols can be recovered `o` BinDiff reveals many shared functions between XPR scanners and libXProtectPayloads.dylib `o` We can import symbols exported by libXProtectPayloads.dylib into XPR scanners

## Slide 15

## **Challenges in RE of Stripped Swift Binaries**

- Some key missing information of stripped Swift binaries

   - Type metadata accessor

   - Type metadata

   - Protocol Witness Table (PWT)

- Reversing Swift binaries without this information is quite difficult…

Symbols of type metadata are missing…

## Slide 16

## **Swift Metadata**

- Swift binaries contain extensive internal metadata for reflection

- This metadata includes type metadata accessor, type metadata, PWT `o` __TEXT.__swift5_protos, __TEXT.__swift5_types, __TEXT.__swift5_fieldmd, and more `o` “DisARMing Code” by Jonathan Levin (https://newdebuggingbook.com)

- With ipsw swift-dump, this metadata can be extracted as Swift code `o` <u>https://github.com/blacktop/ipsw</u>

   - But no tools to import this metadata into a disassembler…

## Slide 17

## **binja-swift-analyzer**

• Custom Swift analysis plugin for Binary Ninja

- Based on ipsw swift-dump

`o` Available on GitHub (https://github.com/FFRI/binja-swift-analyzer)

- Key features

   - Type metadata accessor and type metadata parsing

   - `o` PWT analysis for structs and classes

   - Class method identification

   - Swift string analysis (immortal and large strings)

   - Visual representation of protocol conformance and class inheritance

## Slide 18

**Type Metadata Accessor Identification**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Type Metadata Accessor Identification
100077ea0 sub_100877ea@() __pure
100077ea9 return &data_1000f69a0
100077ea0 type metadata accessor for YaraRuleVariable.VariableType() __pure
100077ea9 return &type metadata for YaraRuleVariable.VariableType
Symbols | © type metadata for XPPluginAPIL
Name
type metadata accessor for XPPluginAPl.YaraMatcher
type metadata accessor for XPPluginAPl.YaraMeta
type metadata accessor for XPPluginAPl.YaraError
type metadata accessor for XPPluginAPIl.YaraScanResult
type metadata accessor for XPPluginAPIl.YaraMetaType
type metadata accessor for XPPluginAPI.YaraRule
type metadata accessor for XPPluginAPl.YaraRuleVariable
type metadata for XPPluginAPL.YaraError
type metadata for XPPluginAPL.YaraMetaType
```

## Slide 19

**Type Metadata Identification**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
void* rax_3 =
*(rax_3
*(rax_3
rax_3
rax_3
rax_3
rax_3
rax_3
rax_3
rax_3
rax_3
rax_3
(
*(
*(
*(
*(
*(
*(
*(
*(
*(
+
++eeererterrtett
void* rax_3
*(rax_3 +
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
*(rax_3
t++eeteeeetetet
Type Metadata Identification
swift_initStackObject (sub_100@9b3b@(&data_100106998), &var_118)
data_100@c65e0
&data_10@0f1be0
&data_1000f13F8
rax & 1
rdx
&data_10@0f1b78
&data_1000F14068
rax_1 & 1
rdx_1
&data_1000f1920
&data_10@0F13b8
(&data_100106998), &var_118)
data_10@@c65e@
&type metadata for RemediationBuilder .FileMacho
&pwt of RemediationBuilde. ..ationBuilder .FileConditionConvertible
rax & 1
rdx
&type metadata for RemediationBuilder .FileNotarised
&pwt of RemediationBuilde. ..ationBuilder .FileConditionConvertible
rax_1 & 1
rdx_1
&type metadata for RemediationBuilder.FileYara
&pwt of RemediationBuilde...ationBuilder .FileConditionConvertible
```

## Slide 20

## **Dynamic Analysis – LLDB Scripting Bridge**

- LLDB Python Scripting Bridge

- Branch tracing script (https://github.com/kohnakagawa/LLDB)

   - Swift binaries contain many indirect branches, such as function calls via VTable and PWT

   - Manually identifying branch targets in LLDB is time-consuming

   - This script automatically captures target addresses

   - Trace data is exported as JSON for import via my binja-missinglink plugin

   - ▪ <u>http://github.com/FFRI/binja-missing-link</u>

## Slide 21

## **Branch Tracing & Imported into Binja**

PWT information is also added for function calls via PWT

Resolved symbol information is also added

## Slide 22

**Dynamic Analysis – Custom LLDB Commands**

- Custom commands for dumping Swift Objects

   - Standard expr -O -l Swift -- <address> command does not work for complex Swift objects like existential containers and Swift arrays…

`o` Created enhanced commands for dumping Swift objects utilizing Swift reflection

## Slide 23

## **Outline**

###### 1. Introduction

2. Tooling

###### **3. RE results**

   **1. Overview**

   2. Initialization

   3. RemediationBuilder

   4. Remediation Logic

   5. Provenance Sandbox

4. Vulnerability Research

5. Conclusion

## Slide 24

## **Flow of “Remediation”**

daemon.scan.startup.plist DAS-CTS
daemon.scan.plist
XPC
Contents/MacOS/XProtect XProtectPluginService.xpc
agent.scan.startup.plist
agent.scan.plist DAS-CTS GCD & NSTask
Swift Mach-O XPR scanners
Initialization
… Adload BlueTop WaterNet
mod_init_func Vnode Rapid Aging
Remediation/Detection
…
BadGacha Trovi
RemediationBuilder XPPluginAPI
Collect remediated
Remediates threats
threat info
Provenance Sandbox
Send remediated
threat info
These files have the same
plist 3 rd stage payload 2 nd stage payload evil.app
provenance attribute
…

## Slide 25

## **Outline**

1. Introduction

2. Tooling

**3. RE results**

   1. Overview

   **2. Initialization**

   3. RemediationBuilder

   4. Remediation Logic 5. Provenance Sandbox

4. Vulnerability Research

5. Conclusion

## Slide 26

## **mod_init_func_0**

- mod_init_func_0 (function with constructor attr, executed before _start) `o` Sensitive strings (YARA, file paths, etc.) for remediation are encrypted with XOR cipher `o` These strings are decrypted before _start

`o` Pointers to decrypted strings are stored in __DATA.__common

Simple XOR cipher

## Slide 27

## **Decrypting XPR Sensitive Strings**

• Alden’s nice Binja script can decrypt these encrypted strings `o` However, some strings cannot be decrypted

_The output isn’t perfect, there is some occasional junk._

   - “The Secrets of XProtectRemediator” by Alden Schmidt

- My custom LLDB SB script decrypt all these strings `o` <u>https://github.com/FFRI/binja-xpr-analyzer/tree/main/dump_secret_config</u>

## Slide 28

**Decryption Results**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
04e23817983f1c0e9290ce7 f90e6c9e75bF45190
99c31f166d1f1654a1b7dd1la6bec3b935022a020
MACOS.0260dfd
MACOS. f07788a
MACOS.ad27ff5
MACOS. 8ccf842
/Library/Preferences/com.common.plist
/Library/Preferences/com.settings.plist
/etc/change_net_settings.sh
/etc/pf_proxy.conf
.preferences.plist
-net.preferences.plist
/Library/Preferences/
/Library/LaunchDaemons/
/Library/
/etc/st-up.sh
/etc/run_upd.sh
.service.plist
/etc/
. background
. background.
right-click
right click
option click
choose open
click open
press open
unidentified developer
are you sure you want
will always allow it
run on this mac
rule macos_rankstank
strings:
$injected_func
$xor_decrypt =
$stringA "S55 /
rule macos_redpine_implant {
strings:
$classA = "CRConfig"
$classD = "CRPwriInfo"
$classE = "CRGetFile"
$classF "CRXDump"
condition:
all of them
= "_run_avcodec"
{ 80 b4 04 ?? ?? 00 00 7a }
.main_storage"
$stringB "session-Llock"
$string? = "%s/
condition:
2 of them
UpdateAgent"
```

## Slide 29

## **Program Entry Point**

- A plugin class is instantiated

`o` Each XPR scanner typically defines one plugin class (such as AdloadPlugin)

- XPAPIHelpers is instantiated and passed to the plugin main function `o` The plugin entry point is XProtectPluginProtocol.main(api: XPPluginAPI.XPAPIHelpersProtocol)

Plugin class is instantiated

XPAPIHelpers is instantiated and passed to the plugin main

## Slide 30

**XPAPIHelpers**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
class XPAPIHelpers {
let
var
let
let
var
logger: XPLogger
pluginService: XProtectPluginDispatchProtocol
codeSignature: XProtectPluginCodeSignatureAPIProtocol
file: XProtectPluginAPIPath
Launchd: XProtectPLuginLaunchdAPIProtocol
var
var
let
var
let
lLaunchServices: XPLaunchServicesProtocol
yara: XProtectPLluginAPIYaraProtocol
process: XProtectPLluginProcessAPIProtocol
event: XProtectPluginAPIEventsProtocol
networkSettings: XProtectPluginAPINetworkSettingsProtocol
var
keychain: XProtectPluginKeychainAPIProtocol
var
var
Var
Var
Var
Var
plugin: XProtectPlugtnProtocol ?
pipeline: _OBJC_CLASS_$ CPProfile ?
connection: VerifiablexPCConnectionProtocol
configProfiles: XProtectConfigProfilesAPIProtocol
lazy alertGUI: XPAlertGUIProtocol ?
memory: XPProcessMemoryAPI
Var
lazy behavioralEvents: XPEventDatabaseAPIProtocol ??
```

## Slide 31

## **XPAPIHelpers: Interesting Property**

- var lazy alertGUI: XPAlertGUIProtocol

`o` Contains methods that display an alert dialog to users using NSAlert `o` Current XPR silently remediates threats without notifying users `o` I have not seen any XPR scanners using this property during my research `o` XPR may introduce user notifications for remediation events in the future?

## Slide 32

## **XPR Plugin Main**

- XProtectPluginProtocol.main(api: XPPluginAPI.XPAPIHelpersProtocol) -> XProtecPluginCompletionStatus

   - Instantiating XPLogger class

`o` Recording performance data using os_signpost

`o` Unsetting the MAGIC environment variable (fix for CVE-2024-40842) `o` Verifying XProtectPluginService by checking its

com.apple.private.xprotect.trustedpluginservice entitlement

`o` Enabling Vnode Rapid Aging

- After enabling Vnode Rapid Aging, the remediation begins

## Slide 33

## **Vnode Rapid Aging**

- Vnode Rapid Aging is a feature that suppresses atime updates `o` Updates are suppressed on a per-process basis `o` Can be enabled via sysctl (no entitlement required)

   - Appears to be intended for performance improvement and preservation for forensic investigation

   - Disabled after remediation

_According to the Kernel sources, there’s something called “rapid aging” that might be relevant. Documentation is sparse so I don’t know its intended use, but it looks like something you can set per-process that will prevent access times from being set._

- “WrMeta” by darwin-dev@googlegroups.com

<u>https://groups.google.com/g/darwin-dev/c/7F6uth1rhKw/m/SJQ3zWxeIgEJ</u>

## Slide 34

## **Outline**

1. Introduction

2. Tooling

**3. RE results**

   1. Overview

   2. Initialization

   **3. RemediationBuilder**

   4. Remediation Logic 5. Provenance Sandbox

4. Vulnerability Research

5. Conclusion

## Slide 35

## **How to Describe Remediation Logic**

- Consider remediation under the following conditions:

   - Files under ~/Library/Application Support (search depth up to 5)

   - The file size is 2 MiB or less

   - The file format is Mach-O

   - Not notarized

   - Matches the YARA rule

   - When running as root, add /Library/Application Support to the search targets and match with a different YARA

## Slide 36

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less File format is Mach-O Not notarized Matches YARA rule

## Slide 37

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less

File format is Mach-O

Not notarized

Matches YARA rule

## Slide 38

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less File format is Mach-O Not notarized Matches YARA rule

## Slide 39

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less File format is Mach-O Not notarized Matches YARA rule

## Slide 40

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less File format is Mach-O Not notarized

Matches YARA rule

## Slide 41

## **Naive Implementation**

For each file under ~/Library/Application Support

File size is 2 MiB or less File format is Mach-O Not notarized Matches YARA rule

Implementation for root

## Slide 42

### **Issues When Implementing Remediation Logic**

• Remediation logic is understandable, but…

- Readability and maintainability decrease as conditions increase ▪ If you want to add additional conditions, you need to append more if clauses…

- `o` How can we improve readability and maintainability?

Apple has achieved readability and maintainability by using Swift result builders

## Slide 43

## **What Are Result Builders?**

- Swift result builders are a feature introduced in Swift 5.4

   - Allows us to create Domain Specific Languages (DSLs) within Swift code

   - `o` Used in SwiftUI to describe user interfaces declaratively

- Useful for code that collects multiple elements to produce a single result `o` E.g., generating structural data (e.g., HTML, JSON)

   - In XPR, combining remediation conditions to produce the final remediation decision

_A result builder type is a type that can be used as a result builder, which is to say, as an embedded DSL for collecting partial results from the expression-statements of a function and combining them into a return value._

- “Swift Evolution: Result builders”

<u>https://github.com/swiftlang/swift-evolution/blob/main/proposals/0289-result-builders.md https://developer.apple.com/videos/play/wwdc2021/10253/</u>

## Slide 44

## **Example: Generating HTML**

###### Without Swift result builders

Redundant variables

This element is added when useChapterTitles is set to True

[spellOutChapter: True, useChapterTitles: True]

It’s not clear what the final HTML structure will look like

## Slide 45

## **Example: Generating HTML**

[spellOutChapter: True, useChapterTitles: True]

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
return body {
let chapter = spellOutChapter ? "Chapter "
division {
if useChapterTitles {
headerl(chapter + "1. Loomings.") eee
}
paragraph {
"Call me Ishmael. Some years ago"
<body>
<div>
} <hl>Chapter 1. Loomings.</h1>
<p>Call me Ishmael. Some years ago</p>
h ; : .
pe thee 3 now your insular city” <p>There is now your insular city</p>
</div>
} <div>
} <hl>Chapter 2. The Carpet-Bag.</h1>
diviston ¢ . <p>I stuffed a shirt or two</p>
if useChapterTitles { </div>
headerl(chapter + "2. The Carpet-Bag.") </body>
}
paragraph {
"IT stuffed a shirt or two"
}
}
```

## Slide 46

**Power of Result Builders**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
let yaraMatcher = createYaraMatcher("<some rule>")
for file in enumerateFiles("~/Library/Application Support", 5) {
if file.size <= x x {
if file.isMacho() {
if !file.isNotarized() {
if yaraMatcher.match(file) {
remediate( file)
}
let yaraMatcherRoot = createYaraMatcher("<some rule for root>")
if getuid() == {
for file in enumerateFiles("/Library/Application Support", 5) {
if file.size <= * * {
if file.isMacho() {
if !file.isNotarized() {
if yaraMatcherRoot.match(file) {
remediate( file)
}
```

## Slide 47

**Power of Result Builders**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
let isRoot = getuid()
TestRemediator {
File(searchDir: "~/Library/Application Support", regexp: ".*", searchDepth: 5) {
MaxFileSize(2 * * )
FileMacho( )
FileNotarized( )
FileYara(YaraMatcher("<some rule>") )
}
if isRoot {
File(searchDir: "/Library/Application Support", regexp: ".*", searchDepth: 5) {
MaxFileSize(2 * x )
FileMacho( )
FileNotarized( )
FileYara(YaraMatcher("<some rule>") )
```

## Slide 48

## **Power of Result Builders**

For each file under ~/Library/Application Support File size is 2 MiB or less File format is Mach-O Not notarized Matches YARA rule

## Slide 49

## **Power of Result Builders**

Enabled when running as root

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
let isRoot = getuid()
TestRemediator {
File(searchDir: "~/Library/Application Support", regexp: ".*", searchDepth: 5) {
MaxFileSize(2 * x )
FileMacho( )
FileNotarized( )
FileYara(YaraMatcher("<some rule>") )
}
if isRoot {
File(searchDir: "/Library/Application Support", regexp: ".*", searchDepth: 5) {
MaxFileSize(2 * x )
FileMacho( )
FileNotarized( )
FileYara(YaraMatcher("<some rule>") )
```

## Slide 50

**RemediationBuilder DSL**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Describes remediation conditions for launchd services
enum RemediationBuilder.ServiceRemediationBuilder {}
For files
enum RemediationBuilder.FileRemediationBuilder {}
For processes
enum RemediationBuilder.ProcessRemediationBuilder {}
For Safari App Extensions
enum RemediationBuilder.SafariAppExtensionRemediationBuilder {}
Combining 5 types of remediations (Service, File, Process, SafariAppExtension, Proxy)
enum RemediationBuilder.RemediationArrayBuilder {}
```

## Slide 51

## **Which Scanner Uses RemediationBuilder?**

- RemediationBuilder is used in the following XPR scanners:

   - Adload, BadGacha, CardboardCutout, ColdSnap, Eicar, KeySteal, Pirrit, RankStank, RedPine, RoachFlight, SheepSwap, SnowDrift, WaterNet, Dolittle, Bundlore

- The remaining scanners rely on XPPluginAPI for their implementation

   - Some XPR scanners describe remediation logic both declaratively and imperatively

## Slide 52

**Specification of RemediationBuilder DSL** <u>https://github.com/FFRI/RemediationBuilderDSLSpec https://ffri.github.io/RemediationBuilderDSLSpec/documentation/remediationbuilder</u>

## Slide 53

## **FileRemediationBuilder Example**

File path is /tmp/eicar

File is 68 bytes or more

Match EICAR YARA rule

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EicarRemediator {
File(path: "/tmp/eicar") { FileRemediationBuilder DSL block
MinFtileSize( 68 )
FileYara( YaraMatcher(etcaryYara) )
```

## Slide 54

## **ProcessRemediationBuilder Example**

Process is NOT notarized

Backing file path is /tmp/, .mitmproxy, …

Backing file matches Adload YARA rule

## Slide 55

## **OpenRemediationBuilder**

- Open-source reimplementation of RemediationBuilder

- A minimal implementation that reproduces XPR Eicar's functionality

• https://github.com/FFRI/OpenRemediationBuilder

## Slide 56

## **Outline**

1. Introduction

2. Tooling

**3. RE results**

   1. Overview

   2. Initialization

   3. RemediationBuilder

   **4. Remediation Logic** 5. Provenance Sandbox

4. Vulnerability Research

5. Conclusion

## Slide 57

## **XPR RoachFlight**

- Added in XPR version 96 on 27 April 2023

   - Added at the same time as XPR RankStank

   - XPR RankStank removes payloads used in the 3CX supply chain attack

- The decrypted strings are the two hash values

## Slide 58

## **Remediation Logic of XPR RoachFlight**

Decrypted CDHashes

Processes that have specific CDHashes are remediated

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
let targetCDHashes = ["04e23817983f1c0e9290ce7f90e6c9e75bF45190",
"99c31f166d1f1654a1lb/ddla6bec3b935022a020" |
RoachFlightRemediator {
for cdHash in targetCDHashes {
Process {
}
```

## Slide 59

## **What Are These Two CDHashes?**

- 04e23817983f1c0e9290ce7f90e6c9e75bf45190 is known

`o` The CDHash of the 2<sup>nd</sup> stage payload used in the 3CX supply chain attack `o` This sample is commonly referred to as UpdateAgent

`o` The sample was analyzed by Patrick Wardle and presented at BHUSA 2023

<u>https://x.com/patrickwardle/status/1641690082854989827</u>

## Slide 60

## **What Are These Two CDHashes?**

- 99c31f166d1f1654a1b7dd1a6bec3b935022a020 is unknown `o` Could it potentially be UpdateAgent variant?

`o` Patrick Wardle suggested the possibility of other UpdateAgent samples Sample analyzed by Patrick Wardle

Transmits data to C2, and then, does nothing (known CDHash)

UpdateAgent variant performs more actions? (unknown CDHash)

<u>https://speakerdeck.com/patrickwardle/mac-ing-sense-of-the-3cx-supply-chain-attack-analysis-of-the-macos-payloads?slide=46</u>

## Slide 61

## **XPR BadGacha**

- Added in XPR version 91 on 2 March 2023

- The decrypted strings appear unrelated to any remediation functionalities

- What are these texts used for?

## Slide 62

## **XPR BadGacha: Decrypted Strings**

###### • Hint: background image of AMOS DMG contains similar strings

<u>https://www.kandji.io/blog/amos-macos-stealer-analysis</u>

## Slide 63

## **OCR-based Gatekeeper Bypass Detection**

- XPR BadGacha contains detection logic for Gatekeeper bypass `o` Enumerates mounted DMG files using FileManager.mountedVolumeURLs `o` Retrieves text strings in background images of mounted volumes using OCR `o` Searches for Gatekeeper bypass-related strings

- If it find strings, it reports the threat including the DMG file information `o` Only reporting is performed, without deleting or unmounting the DMG

## Slide 64

#### **Which Malware Family Does XPR BadGacha Detect?**

• Appears to be a generic detection module?

`o` In fact, the detection logic has triggered on several different malware families ▪ E.g., Empire Transfer and ChromeLoader

`o` Apple may have designed XPR BadGacha as a threat hunting scanner

<u>https://9to5mac.com/2024/02/29/security-bite-self-destructingmacos-malware-strain-disguised-as-legitimate-mac-app/</u>

<u>https://www.crowdstrike.com/en-us/blog/how-crowdstrikeuncovered-a-new-macos-browser-hijacking-campaign/</u>

## Slide 65

## **Other BadGacha Detection**

- A mechanism to detect processes without their backing files was previously implemented (removed in XPR version 135)

`o` The detection was likely removed due to frequent false positive detections `o` This logic also appears not be designed to target a specific malware family

_After installing the latest stable version of Chromium, I have been getting the following warnings when running an XProtect Remediator scan. I'm not sure if this is a bad issue, but I think it is something Apple should look at. Thanks._

- “Apple Developer Forums”

<u>https://developer.apple.com/forums/thread/742828</u> False positive alert reported by a user

## Slide 66

## **XPR RedPine**

- Added in version 114 on October 12, 2023, and retired in 2024

- Decrypted strings are a YARA rule and four file paths

   - The YARA rule detects the TriangleDB iOS implant

- Kaspersky researchers noted the possibility of TriangleDB macOS implant `o` RedPine appears to be TriangleDB macOS implant

   - No details about TriangleDB macOS implant have been made public

_While analyzing TriangleDB, we found that the class CRConfig (used to store the implant’s configuration) has a method named populateWithFieldsMacOSOnly. … its existence means that macOS devices can also be targeted with a similar implant;_

- _“_ Dissecting TriangleDB, a Triangulation spyware implant _” by_ Georgy Kucherin, Leonid Bezvershenko, and Igor Kuznetsov

<u>https://securelist.com/triangledb-triangulation-implant/110050/</u>

## Slide 67

## **XPR RedPine: Two Scans**

- XPR RedPine has the com.apple.system-task-ports.read entitlement `o` Allows to obtain task ports and read memory of other processes

- When XPR RedPine is executed as root, it performs two scans

   - Scans the main executable file in memory

`o` Scans loaded libraries (called LoadedLibrary Scanner)

## Slide 68

### **Scanning the Main Executable in Memory**

- XPProcessMemoryAPI is used for in-memory scanning

   - Only __TEXT segment is scanned and matches it against the YARA rule

   - `o` Excludes platform processes from scan targets

## Slide 69

##### **Why Does XPR RedPine Perform In-Memory Scanning?**

- Perhaps macOS implant was also deployed only in memory without leaving any payload on disk?

_The implant, which we dubbed TriangleDB, is deployed after the attackers obtain root privileges on the target iOS device by exploiting a kernel vulnerability. It is deployed in memory, meaning that all traces of the implant are lost when the device gets rebooted._

- “Dissecting TriangleDB, a Triangulation spyware implant” by Georgy Kucherin, Leonid Bezvershenko, and Igor Kuznetsov <u>https://securelist.com/triangledb-triangulation-implant/110050/</u>

Note: YARA scan described with ProcessRemediationBuilder is performed on the backing file (not on process memory)

## Slide 70

## **LoadedLibrary Scanner**

• A scanner that examines loaded libraries

Are these really dylib paths?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
« Ascanner that examines loaded libraries
RedPineScanner {
Process {
ProcessIsAppLleSigned
HasLoadedLibrary{"/System/Library/PrivateFrameworks/FMCore. framework" )
HasLoadedLibrary|"/System/Library/Frameworks/CoreLocation.framework/CoreLocation" )
HasLoadedLibrary{"/System/Library/Frameworks/AVFoundattion. framework/AVFoundation" )
HasLoadedLibrary("/usr/lib/ltibsgqlite3.dylib" )
}.reportOnly( )
```

## Slide 71

## **Peculiar Logic**

• Except for /usr/lib/libsqlite3.dylib, no actual file paths are specified! `o` CoreLocation and AVFoundation are symlinks

▪ When these are loaded as libraries, their symlinks are resolved

`o` FMCore.framework is a directory

▪ Of course, it’s impossible to load a directory as a dylib…

## Slide 72

## **Mystery of the LoadedLibrary Scanner**

- Hypothesis 1: XPR’s Bug

   - Did Apple incorrectly specify the LoadedLibrary paths?

- Hypothesis 2: SIP & SSV bypass

   - Did the attacker replace the directory and the symlinks with attacker’s dylibs?

   - `o` It is unlikely because macOS becomes unstable…

## Slide 73

## **Hypothesis 3: Stealthier Reflective Loader**

- TriangleDB iOS implant uses reflective loading for its modules `o` macOS implant maybe implemented it, too

- Patrick’s research showed reflectively loaded dylibs has empty backing files `o` Serves as one of the key indicators of reflective loading

Can we specify a backing file to hide indicators of reflective loader?

No backing file!

<u>https://speakerdeck.com/patrickwardle/mirror-mirror-restoring-reflective-code-loading-on-macos?slide=40</u>

## Slide 74

## **Stealthier Reflective Loader**

- I developed a new reflective loader that can specify a backing file `o` Achieved by modifying dyld’s all_imges_info

- macOS implant might load dylibs reflectively while specifying backing files? `o` To hide indicators of reflective loader

###### Output of vmmap

Directory path is specified as the backing file

## Slide 75

## **Remaining Mysteries**

- It’s more natural to specify an unused system library path as a backing file `o` Why specify a directory or symlink?

- Why doesn’t XPR RedPine remediate threat?

   - Because reportOnly property is set to True

   - If remediation wasn't the goal, what was the purpose of deploying it?

Does not remediate threat

## Slide 76

## **XPRTestSuite**

- Contains RE results of 15 XPR scanners

- Contains scripts to reproduce XPR remediation

- Useful for XPR research and testing purposes

- https://github.com/FFRI/XPRTestSuite

## Slide 77

## **Outline**

1. Introduction

2. Tooling

**3. RE results**

   1. Overview

   2. Initialization

   3. RemediationBuilder

   4. Remediation Logic

   **5. Provenance Sandbox**

4. Vulnerability Research

5. Conclusion

## Slide 78

### **Which App Created Remediated Files?**

Persisted thru LaunchAgents Cracked infected app
2 nd stage payload
3 rd stage payload
Which app created these files?
Cannot get it from the
remediated files only
XPR

## Slide 79

## **Solution: Provenance Sandbox**

Provenance Sandbox
XPR can retrieve which app dropped these
remediated files based on the provenance attribute
Persisted thru LaunchAgents Cracked infected app
com.apple.provenance:
0102000A0B0C0D0E0F1011
2 nd stage payload com.apple.provenance:
0102000A0B0C0D0E0F1011
com.apple.provenance:
0102000A0B0C0D0E0F1011 Registers app
3 rd stage payload information &
provenance data
com.apple.provenance: Which app has this
0102000A0B0C0D0E0F1011 provenance attr?
0A0B0C0D0E0F1011,
Also fetches  /Volume/Installer/ChromeInst
aller.app
provenance attribute
ChromeInstaller.app
XPR ExecPolicy

## Slide 80

## **Provenance Sandbox**

- Enables identification of processes that create and modify files `o` For App Sandbox, files that are dropped have a quarantine attribute attached `o` You can think of Provenance Sandbox as being replaced by the provenance attribute `o` Like App Sandbox, it also applies to child processes

- When a process is running in Provenance Sandbox, a provenance attribute is attached to files during the following operations:

   - create, rename, setacl, setattrlist, setextattr, setflags, setmode, setowner, setutimes, truncate, deleteextattr, swap, open (called with O_RDWR or O_TRUNC flags), link

## Slide 81

## **com.apple.provenance**

• An 11-byte integer value

`o` 01 02 00 E9 AC 02 3A 98 15 DF 25

▪ The use of the first 3 bytes is unknown

▪ The following 8 bytes are random numbers (generated by arc4random)

## Slide 82

## **Why XPR Collects Provenance Attribute?**

• Provenance attribute helps to discover malware variants

`o` In case that there are other samples that drop the same 2<sup>nd</sup> stage payload

Cracked
infected app
Persisted thru
Other previously unknown
LaunchAgents
cracked apps drop the same
2 nd stage payload
Updates YARA
2 nd stage  rules, CRL,
payload Notarization
3 rd stage  status, …
payload
Sends analytics to Apple
XPR

## Slide 83

## **How to Utilize Provenance Attribute**

###### • Identifying applications that achieved persistence

... Running other processes… $HOME/Library/LaunchAgents Google Chrome.app com.apple.provenance: com.apple.provenance: 0102009A947F71827A32E5 0102009A947F71827A32E5 Same provenance attribute Contains registered application information (signing info, …) ExecPolicy

## Slide 84

## **Tools to Utilize Provenance Attribute**

- ShowProvenanceInfo

   - This app retrieves provenance attribute, then enumerates which apps created and modified files

   - <u>https://github.com/FFRI/ShowProvenanceInfo</u>

- Aftermath plugin collecting provenance attribute is also implemented `o` Planning to submit a Pull Request after this talk

<u>https://github.com/jamf/aftermath</u>

## Slide 85

## **Outline**

1. Introduction

2. Tooling

3. RE results

   1. Overview

   2. Initialization

   3. RemediationBuilder

   4. Remediation Logic

   5. Provenance Sandbox

**4. Vulnerability Research**

5. Conclusion

## Slide 86

## **Arbitrary File Deletion (TCC Bypass)**

- Arbitrary file deletion vulnerability

`o` Inspired by “Aikido Wiper” by Or Yair

- Vulnerabilities allow to delete arbitrary files by exploiting TOCTOU in EDR and AV

- `o` His research is focused on Windows platform

`o` On macOS, achieving arbitrary file deletion requires TCC bypass

<u>https://www.safebreach.com/blog/safebreach-labs-researcher-discovers-multiple-zero-day-vulnerabilities/</u>

## Slide 87

## **Classic TOCTOU: CVE-2024-40843**

• YARA rule matching → Remediating file

- Replace the target file using a symlink

`o` After matching YARA rule before remediating file

`o` The timing of YARA rule match can be monitored through log command

## Slide 88

## **Provenance Sandbox Bypass**

- I reported several bypass methods

- Example 1: Process execution via LaunchServices `o` Drop a .terminal script and execute .terminal using open

   - While executed by Terminal.app, Terminal does not run within the Provenance Sandbox

- Example 2: Bypass through XPC

`o` Execute workflow files via automator (fixed in Sequoia 15)

- **Previous App Sandbox bypass techniques are likely applicable**

## Slide 89

## **Outline**

1. Introduction

2. Tooling

3. RE results

   1. Overview

   2. Initialization

   3. RemediationBuilder

   4. Remediation Logic 5. Provenance Sandbox

4. Vulnerability Research

**5. Conclusion**

## Slide 90

## **Conclusion**

- **Covered:**

`o` Tooling and how to analyze XPR

`o` XPR internals (initialization, XPAPIHelpers, RemediationBuilder, remediation logic) `o` Provenance Sandbox (brief overview, how to utilize provenance attribute) `o` A bit of vulnerability research

- **Not covered:**

   - Provenance Sandbox internals and other use cases of provenance attribute

   - `o` Other XPR scanners internals (such as XPR CardboardCutout) `o` Several bugs of XPR scanners

## Slide 91

## **Future Work**

- XProtect Behavior Service (XBS)

`o` XBS internals and how can XBS detection be bypassed? `o` Stay tuned!

- Tracking Gatekeeper

`o` I found this while analyzing syspolicyd

`o` It also appears to use a provenance attribute

## Slide 92

## **Black Hat Sound Bytes**

- **XPR is a treasure trove of Apple's threat intelligence**

   - Security researchers should actively engage in analyzing scanners in future updates

   - `o` My custom tools for XPR analysis will be published on GitHub, so please use them

- **Provenance attribute serves as a valuable forensic artifact**

   - Blue teams make the most of it

   - Red teams may need to bypass Provenance Sandbox to achieve stealth operations

- **Vulnerabilities in XPR and Provenance Sandbox are quite basic** `o` Similar bugs found in AVs on other platforms may still exist in XPR

   - Previous App Sandbox escape bugs may apply to Provenance Sandbox bypass

## Slide 93

## **Acknowledgements**

- @howardnoakley

- @Morpheus______

- @birchb0y

- @philofishal

- @patrickwardle

- @gergely_kalman

- @blacktop__

- @oryair1999

## Slide 94

## **Published Tools**

• All published tools are available from the following link

• <u>https://github.com/FFRI/PoC-public/tree/main/bhusa2025/xunprotect</u>

## Slide 95

## **Disclaimer**

This document is a work of authorship performed by FFRI Security, Inc. (hereafter referred to as "the Company"). As such, all copyrights of this document are owned by the Company and are protected under Japanese copyright law and international treaties. Unauthorized reproduction, adaptation, distribution, or public transmission of this document, in whole or in part, without the prior permission of the Company is prohibited.

While the Company has taken great care to ensure the accuracy, completeness, and utility of the information contained in this document, it does not guarantee these qualities. The Company will not be liable for any damages arising from or related to this document.

©FFRI Security, Inc. Author: FFRI Security, Inc.

## Slide 96

## **Thank You!**

**Feedback? Ideas?** @tsunek0h (X) @tsunekoh@infosec.exchange (Mastodon) research-feedback@ffri.jp **White paper (in progress)**

## Slide 97

## **Icon**

• https://www.flaticon.com

• https://macosicons.com/#/

## Companion resources

### `Koh Nakagawa_XUnprotect Reverse Engineering macOS XProtect Remediator_TOOLS.txt`

```text
https://github.com/FFRI/PoC-public/tree/main/bhusa2025/xunprotect
```
