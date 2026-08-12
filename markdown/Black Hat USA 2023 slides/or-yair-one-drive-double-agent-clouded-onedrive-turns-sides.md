---
title: "One Drive, Double Agent Clouded OneDrive Turns Sides"
speakers: ["Or Yair"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Or Yair_One Drive, Double Agent Clouded OneDrive Turns Sides.pdf"
pages: 91
sha256: "c2a6a27918abba4a70fb45406fca95b51eb5911e27b3a9262c41e228dc462c52"
text_chars: 20030
ocr_pages: 23
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:23:16Z"
---
# One Drive, Double Agent Clouded OneDrive Turns Sides

**Speakers:** Or Yair  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Or Yair_One Drive, Double Agent Clouded OneDrive Turns Sides.pdf` (91 pages)

## Slide 1

One Drive. Double Agent. Clouded OneDrive Turns Sides

## Slide 2

# Or Yair - OneDrive’s Handler

Security Researcher at SafeBreach 6 years in cyber security starting in the IDF Linux, embedded and some Android research

3 years Windows internals research

Creator of Aikido Wiper (Presented at Black Hat Europe 2022)

## Slide 3

# Agenda

Ransomware Background Research Questions / Goals Research – Turning OneDrive into a ransomware DoubleDrive EDR Bypasses Summary

## Slide 4

# State of Ransomware

Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
State of Ransomware
FORBES > BUSINESS
BREAKING
March 2023 broke ransomware attack records with 459 Ransomware Attacks Upgraded
incidents To 'National Security Threat' In
New White House Cybersecurity
Strategy
By Bill Toulas April 19, 2023 03:00 AM 0
Siladitya Ray Forbes Staff
Forbes
17%
13% 13%
11% 12%
10% 10%
%
5%
Lessthan =z en Between Between il Between Between Between Between Between Ls millio | 2020 | 2021 | 2oze | | 2023 |
$1,000 $1,000and $5,000and = $10,000and + $20,000and $50,000and $100,000 $250,000 $500,000 $1millionand or more
4,999.99 9,999.99 1999999 $49,999.99 $99,999.99 d id id 4,999,999.99
$4; $9. $19; $49, S$ ant ani an S$ 51% 37% 66% 66%
$249,999.99 $499,999.99 $999,999.99
i 2022 (n=965) Wi 2023 (n=216)
Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf
```

## Slide 5

# State of Ransomware

Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
State of Ransomware
Ransom Payments: 2023 vs 2022
17%
14%
13%
11% 12%
9% 10% 10%
8% 7%
4%
2% [|
Less than y Between Between Between Between Between Between Between
$1,000 $1,000 and $5,000and $10,000and $20,000and $50,000 and $100,000 $250,000
$4,999.99 $9,999.99 $19,999.99 $49,999.99 $99,999.99 and and
$249,999.99 $499,999.99
M2022 (n=965) Ml 2023 (n=216)
How much was the ransom payment that was paid to the attackers? Excluding “Don't know" responses.
Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf
6% 6%
Between
$500,000
and
$999,999.99
27%
Th
Between
$1 million and
$4,999,999.99
13%
4%
$5 million
or more
```

## Slide 6

# State of Ransomware

Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
State of Ransomware
01% 37% 66% 66%
In the last year, has your organization been hit by ransomware?
Yes. n=3000 (2023), 5,600 (2022), 5,400 (2021), 5,000 (2020)
Sophos: https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf
```

## Slide 7

State of Ransomware

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
State of Ransomware
FORBES > BUSINESS
Ransomware Attacks Upgraded
To ‘National Security Threat' In
New White House Cybersecurity
Strategy
Siladitya Ray Forbes Staff
Covering breaking news and tech policy stories at F Fotiow |
Forbes.
```

## Slide 8

State of Ransomware

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
State of Ransomware es
March 2023 broke ransomware attack records with 459
incidents
By Bill Toulas April 19, 2023 03:00 AM ft)
```

## Slide 9

Research Goals 🤔

## Slide 10

# Research Goals

A fully undetectable-by-design ransomware

- Fully legitimate flow for encrypting files

- Encrypt all user files and make them impossible to restore

- Bypasses all common ransomware detections

## Slide 11

There is a way to encrypt all of your sensitive data without encrypting a single file on your endpoint?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT IF ITOLD YOU
There is a way to encrypt all of your sensitive data
without encrypting a single file on your endpoint?
```

## Slide 12

Adversaries can encrypt files, while they are not even executing code on endpoints?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
/ WHAT IFITOLD YOU
Adversaries can encrypt files, while they are
not even executing code on endpoints?
```

## Slide 13

What if not a single malicious executable from the adversary needs to be present on endpoints while files are encrypted?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| WHAT IF ITOLD YOU
What if not a single malicious executable from the adversary
needs to be present on endpoints while files are encrypted?
```

## Slide 14

Searching for a double-agent

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Searching for —
a double-agent
```

## Slide 15

Cloud Storage + Local Agents

## Slide 16

I am OneDrive, a trusted tool that is installed by default and shelters you from ransomware

## Slide 17

# OneDrive

In Windows:

## Slide 18

# OneDrive

https://support.microsoft.com/en-us/windows/protect-your-pc-from-ransomware-08ed68a7-939f-726c-7e84-a72ba92c01c3:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OneDrive
HH Microsoft | Support Microsoft365 Office © Windows Surface Xbox —_—Deals
Products Devices What's new Account & billing Templates More support
Protect your PC from ransomware
Security, Windows 7, Windows 8.1, Windows 10
= Store important files on Microsoft OneDrive. OneDrive includes built in ransomware detection
and recovery as well as file versioning so you can restore a previous version of a file. And when
you edit Microsoft Office files stored on OneDrive your work is automatically saved as you go.
https://support.microsoft.com/en-us/windows/protect-your-pc-from-ransomware-O8ed68a7-939f-726c-7e84-a72ba92c01c3:
```

## Slide 19

# OneDrive

- Microsoft’s recommended solution *against ransomware*  Installed by default on every Windows version since 2013.

- Mass file operations by definition

   - Syncs files in OneDrive’s storage with their local duplicates.

## Slide 20

😈

Initial Access

VS

😇

Initial Access

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
wipe
we
ee
RS)
|]
ei
Initial Access
VS
Initial Access
```

## Slide 21

# OneDrive Local File Sync

But can it also sync files outside of the local OneDrive directory? Without me touching them?

And is that a legitimate action?

## Slide 22

# OneDrive

“Use symbolic links to link a local path of the local OneDrive sync folder.”

https://support.microsoft.com/en-us/office/can-t-synchronize-onedrive-files-and-folders-from-a-local-file-location-otherthan-the-default-onedrive-path-b7eef9d4-4203-431d-8345-fe49254f9da0

## Slide 23

# OneDrive

# Symlinks VS Junctions

## Slide 24

OneDrive and OneDrive’s Servers

## Slide 25

Malware/Ransomware and C2 Server

## Slide 26

Recruiting a double-agent asset

## Slide 27

Work for me
Umm… OK, no
and turn sides
problem
please🙏

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Work for me Umm... OK, no
and turn sides problem
please
```

## Slide 28

# Control OneDrive’s C2

Access to the victim’s OneDrive account

## Slide 29

# First Option

### Log out and into a different OneDrive account

Work for me
Umm… OK, no
and turn sides
problem
please🙏

## Slide 30

# Second Option

### Get access to the already logged in account

I have the
creds/token of  Umm… OK, no
the victim’s  problem
account

## Slide 31

ODLs - Thank you for being extra informative

ODLs - OneDrive Logs.

Located in: %localappdata%\Microsoft\OneDrive\logs\Personal Not saved a raw text. Can be parsed using odl.py from: https://github.com/ydkhatri/OneDrive Token is written inside �

## Slide 32

ODLs - Thank you for being extra informative Any process running with the current user’s permissions can control the current user’s OneDrive cloud storage:

## Slide 33

# OneDrive Token

Web Session – JWT Token

OneDrive Windows Agent – Windows Live ID Token

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OneDrive Token
Web Session — JWT Token
GET https://api.onedrive.com/v1.0/drive/ HTTP/1.1
: api.onedrive.com
: bearer
OneDrive Windows Agent — Windows Live ID Token
GET https://api.onedrive.com/v1.@/drive/ HTTP/1.1
>: api.onedrive.com
: WLID1.1 tr
```

## Slide 34

# Attack Flow

Initial
Access

#### **Read Token from Logs**

Junctions

## Slide 35

# Token Exfiltration Without C2

Upload a file containing the token to the victim’s account Share the file with the attacker using OneDrive.

- Microsoft account for the attacker is required, not ideal.

🔑

## Slide 36

# Control OneDrive’s C2

✅ Access to the victim’s OneDrive account

## Slide 37

# Attack Flow

**Initial Access**

**Token Share Upload Token**

Junctions

**Remote Encrypt**

**Read Token from Logs**

## Slide 38

File Recovery Prevention

## Slide 39

OneDrive File Recovery

## Slide 40

# OneDrive’s Recycle Bin & Version History

**https://learn.microsoft.com/en-us/compliance/assurance/assurance-malware-and-ransomware-protection**

## Slide 41

# Wiping Version History

- 500 previous versions

- Previous versions are kept after deletion and restoration from the recycle bin

## Slide 42

# Wiping Version History

Conclusion  - An attacker must:
Empty Create
Encrypt Delete the recycle Encrypted
bin files again

## Slide 43

# Emptying The Recycle Bin

Windows app leads to browser Canary is provided only with a “WLSSC” cookie

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emptying The Recycle Bin
Windows app leads to browser
Canary is provided only with a
“WLSSC” cookie
= | WW Empty recycle bin | S Restore all items
|
POST https://skyap1.onedrive. live.com/API/2/DeleteAll HTTP/1.1
: Skyapi.onedrive. live.com
: Hd73dH@pR/oLzylNrpKMFNa8kBht11qED6HL1lokYcgI=3
> 1141147648
```

## Slide 44

OneDrive Android API

## Slide 45

What Happens in Mobile? – Recycle Bin

OneDrive’s native Android app opening a web view for controlling the recycle bin would be a poor experience

## Slide 46

What Happens in Mobile? � Recycle Bin OneDrive’s Android app opening the browser to view and control the recycle bin would be a very poor experience

## Slide 47

What Happens in Mobile? – Recycle Bin “Delete All” Web Request:

“Delete All” Android Request:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What Happens in Mobile? — Recycle Bin hg
“Delete All” Web Request:
POST https://skyapi.onedrive. live.com/API/2/DeleteAll HTTP/1.1
>: Skyapi.onedrive. live.com
: Hd73dH@pR/oLzylNrpKMFNa8kBht11qED6HLLokYcgI=3
; 1141147648
“Delete All” Android Request:
: Skyapi.live.net
>: WLID1.1 t=EwKFI91IJCSIKd3MFRzZ@a3VWFfSE21ZNFIp7FUR
ET)
```

## Slide 48

What Happens in Mobile? – File Sharing

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What Happens in Mobile? — File Sharing
Share
&& TEMPMAIL
Can Edit v
Your Temporary Email Address Set Expiration
botaj90888@goflipa.com #2 a
=> Oo
Copy link Invite Send files Outlook
"a" has been shared with you.
a.txt
botaj90888@goflipa.com
Allow editing Vv
```

## Slide 49

What Happens in Mobile? – File Sharing

No account for the target email is required. Sharing request:

## Slide 50

# Attack Flow

**Initial Access**

**Read Token from Logs**

Junctions

**Token Share Upload Token**

**Remote Encrypt**

**Delete, Empty and Restore**

## Slide 51

Shadow Copy Recovery

## Slide 52

# Shadow Copy Deletion

Requirement: **Run commands using OneDrive**

## Slide 53

Command Execution Using OneDrive No C2 command line interface but:

- OneDrive’s is installed in the current user directory

- Junction to the installation directory

**Looks like an update**

## Slide 54

Command Execution Using OneDrive Microsoft.Sharepoint.exe

Run by OneDrive.exe every time it starts Terminates quickly if no SharePoint account exists

## Slide 55

Command Execution Using OneDrive Replace Microsoft.Sharepoint.exe Commands over the victim’s storage Even supports updates ✅

😈

## Slide 56

Command Execution Using OneDrive – Shadow Copy Deletion

Applicable only if the victim is an administrator Requires UAC bypass (implemented)

## Slide 57

Shadow Copy Deletion Prevention Most EDRs prevent shadow copy deletion. Surprisingly, Cybereason’s did not prevent shadow copy deletion

## Slide 58

Shadow Copy Deletion Prevention

✅ Shadow copy deletion using OneDrive works without prevention

Can this be done with more EDRs?

## Slide 59

SentinelOne XDR Shadow Copy Deletion Prevention Bypass

1 deletion attempt – The XDR kills the process, raises a detection and all shadow copies except 2 are deleted.

## Slide 60

SentinelOne XDR Shadow Copy Deletion Prevention Bypass

- 4 x (Create 4 shadow copies & Delete all) =

- Kills the processes

- Raises detections

- 4th deletion leads to all shadow copies deletion 👏👏

## Slide 61

SentinelOne XDR Shadow Copy Deletion Prevention Bypass

Bypass + SharePoint replacement = No detection ! SentinelOne XDR has the path of Microsoft.Sharepoint.exe in an “allowlist”

My name is Microsoft.SharePoint.exe 😈

Ohh why didn’t you say before? **I trust you now**

## Slide 62

# Complete Attack Flow

**Shadow Copy Deletion**

## Slide 63

Ransomware Detection? Or Ransomware Implementation?

## Slide 64

Notification Settings

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Notification Settings
OneDrive
D> Notification Settings
Q. Notifications
More Settings Reminders for missed Sharing emails
Email notification when OneDrive detects lots of files are deleted at once
Email notification when others reply to your comments
Email notification when the link in a sharing email you sent was clicked
Notification Settings
@® on
@® om
@® on
@® o
Reminders for missed Sharing emails
Email notification when OneDrive detects lots of files are deleted at once
Email notification when others reply to your comments
Email notification when the link in a sharing email you sent was clicked
```

## Slide 65

Checking OneDrive’s API for the Mass Deletion Notification Setting

**PATCH** https://api.onedrive.com/v1.0/drive/userPreferences/email : Params:

Please don’t let
Of course!
the victim know
No problem.
if I deleted a
lot of files 🙏

## Slide 66

Checking OneDrive’s API for the Mass Deletion Notification Setting

**??** 🤔 **??**

## Slide 67

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
HL Microsoft | Support Microsoft 365 Office Windows Surface More v
Microsoft 365 support Products v Devices v What's new Install Microsoft 365 Account & bil
OneDrive / Files / Manage / Ransomware detection and recovering your files
Ransomware detection and recovering
your Tiles
OneDrive (home or personal), OneDrive for Mac, OneDrive for Windows
Ransomware detection notifies you when your OneDrive files have
been attacked and guides you through the process of restoring
your files. Ransomware is a type of malicious software (malware)
designed to block access to your files until you pay money.
```

## Slide 68

# OneDrive Ransomware Detection

DoubleDrive was run multiple times against multiple accounts and nothing was detected

## Slide 69

# RansomwareDetection Notification Disablement

**PATCH** https://api.onedrive.com/v1.0/drive/userPreferences/email : Params:

Please don’t let
Of course!
the victim know
No problem.
you detected
ransomware🙏

## Slide 70

EDRs

## Slide 71

# Bypassing EDRs

No EDR/XDR that we tested was able to detect the ransomware!

Microsoft Defender For Endpoint

SentinelOne XDR

CrowdStrike Falcon

Palo Alto Cortex XDR

Cybereason

## Slide 72

EDRs - Shadow Copy Deletion

Shadow copy deletion works without prevention:

✅ Cybereason

- ✅ SentinelOne XDR

- ⛔ Palo Alto Cortex XDR

- ⛔ CrowdStrike Falcon

⛔ MDE

## Slide 73

Bypassing EDRs - Decoy Files

2 behaviors Decoy files were encrypted with no detection Decoy files were not visible to OneDrive.exe

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing EDRs - Decoy Files
@ OneDrive - Personal st)
2 behaviors | ———_
4 x
Your privacy settings have been applied from
changes you made in another Office app.
Decoy files were encrypted s « stasindoeu. > dead YG —
with no detection + Nome : essa)
p [) abe.docencrypted \\ def3.txtencrypted
| Renamed in docs8
i ic] LD) abco.docencrypted fecha ag6
Decoy files were not visible arodeeaseyee
[) abc2.docencrypted \\ def2.txtencrypted
to OneDrive.exe
| Renamed in docs8
o abc3.doc.encrypted 1 second ago
[) abc4.docencrypted \\__ def1.txtencrypted
Re id in docs8
o def0.txt.encrypted | ST eee
1 second ago
def1.txt. ited —
ied sneer \\ def0.txtencrypted
f2 txt Renamed in docs8
() def2.tx.encrypted ara
D def3.txt.encrypted
. \\__ abc4.doc.encrypted
{)) def4.txtencrypted | Renamed in docs8
1 second ago
oO ghi0.pdf.encrypted
abc3.doc.encrypted
(1) ghit.pdf.encrypted
Open folder Viewonline — Recyclebin Go premium e
```

## Slide 74

Bypassing EDRs - Known file extensions Encrypted files renamed to end with “.encrypted”, “.wnry”, etc.. did not cause any detection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypassing EDRs - Known file extensions
Encrypted files renamed
to end with “.encrypted”,
“wnry”, etc.. did not
Cause any detection
« afterSentDocu... >» docs0
Name
{)) abedocencrypted
(Ei abc0.doc.encrypted
{)) abc2.docencrypted
o abc3.doc.encrypted
{)) abc4.docencrypted
o def0.txt.encrypted
D def1.txt.encrypted
(") def2.txtencrypted
D def3.txt.encrypted
{)) def4.txtencrypted
oO ghi0.pdf.encrypted
{)) ghit.pdf.encrypted
@ OneDrive - Personal BB
® Processing changes
Our prea SELENGS Ravel Baan applied Worn
charges yOu Hada in anathar Officeispp.
v @
def3.txtencrypted
Renamed in docs8
1 second ago
def2.txtencrypted
Renamed in docs8
1 second ago
def1.txt.encrypted
Renamed in docs8
1 second ago
def0.txt.encrypted
Renamed in docs8
1 second ago
abc4.doc.encrypted
Renamed in docs8
1 second ago
abc3.doc.encrypted
Open folder Viewonline — Recyclebin Go premium
*|
E
a
```

## Slide 75

Bypassing EDRs � Controlled Folder Access

Microsoft trust OneDrive.exe to change files that are located in one of the “Protected Folders”

## Slide 76

Bypassing EDRs – Static Signature

No ransomware executable to detect.

The ransomware executable is OneDrive.exe

## Slide 77

DoubleDrive Demo

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DoubleDrive Demo
Victim's OneDrive BE Windows Powershell Attacker
venv) & Or: onedr: ° ra 9 > python .\options_setup.py
t naths C:\Users\Admin\Documents; pyinstaller --onefile .\endpoint
erin - _takeover.py; pyinstaller 2 :\doubledrive. py;
my mes
OD Name+ v Modified v File size Sh
“Documents Yesterday at 11:05:37 PIV Pri
“Personal Vault Yesterday at 11:05:38 PM Pr
“Pictures
erday at 11:05:37 PN Pri
file Edit View VM Hep II
Windows 11
BB Windows Powershel Downloads
Ps C:\Users\Admin\Downloads> © new Son ~ = View
« b> This PC > Downloads -o Search Downes
ES Name Date medied ye
Wl Documents | The
PRrctwes
O music
EiVideos
O toms =]
=Ca
AOE BM sr2023 0
7°n 9
VM, move the mouse pointer inside or press Ctrl+G.
```

## Slide 78

Summary

## Slide 79

# Takeaways

No process should be trusted by default even if its executable was created by Microsoft.

If there is no other option, security vendors should understand whether or not attackers can somehow gain control over such a process and stop it before it happens.

## Slide 80

# Takeaways

## Prepare for next-gen ransomware

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Takeaways vw
Prepare for next-gen ransomware
SV Lt
```

## Slide 81

# Takeaways

Invest more in separating access between standard features and security features. �Don’t write tokens into logs or allow disablement of a “RansomwareDetection” setting without extra validation. � )

## Slide 82

Vendor Responses

## Slide 83

# Microsoft

**MSRC:**

No CVE

"Security Researcher Acknowledgments for Microsoft Online Services“

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft
MSRC:
Your case 78044 was assessed as follows:
No CVE
a "Security Researcher
° SENSIS: iniportant ' sek Acknowledgments for
¢ Security Impact: Elevation of Privilege Microsoft Online Services”
Your case 78782 was assessed as follows:
e Severity: Important
¢ Security Impact: Elevation of Privilege
```

## Slide 84

“We have released a fix addressing the issue outlined in this report and customers are automatically protected. We appreciate the opportunity to investigate the findings reported by Or Yair with SafeBreach, which allowed us to implement changes to harden security by default for the affected service, and thank the finder for practicing safe security research under the terms of the Microsoft Bug Bounty Program.”

## Slide 85

“We appreciate you sharing your research with us to ultimately help protect our customers. Starting with Falcon version 6.58, released August 1, CrowdStrike has visibility into junctions deemed suspicious by our team. This includes junction creation within OneDrive directories. Over the next several weeks we will be using this new sensor visibility to build high fidelity detections around malicious use of junctions, including the OneDrive ransomware technique.”

## Slide 86

“We would like to thank Mr. Yair and SafeBreach team for their cooperation in this coordinated disclosure process and emphasize that Cybereason enthusiastically supports the work of researchers who participate in the responsible disclosure and mitigation of vulnerabilities in software. Cybereason EDR with PRP �Predictive Ransomware Protection) will Detect and Prevent this attack and similar activity after single encryption of a file, and further improvements based on our communications with this team are being planned.”

## Slide 87

“This feature evasion in Cortex XDR agent reported to Palo Alto Networks is fixed in Cortex XDR agents with CU-1040 and later content update versions for all customers.”

## Slide 88

No response from SentinelOne, only from HackerOne:

“Thanks for your report. Based on your initial description, there do not appear to be any security implications as a direct result of this behavior.”

## Slide 89

# Update To Be Safe

|OneDrive Client|23.061.0319.0003
23.101.0514.0001|
|---|---|
|CrowdStrike Falcon|7.02|
|Palo Alto XDR|CU-1040 and later content update versions|
|Cybereason|23.1.100 and above with PRP enabled
22.1.300 and above with PRP enabled|
|MDE|No Response|
|SentinelOne XDR|No Response|
|Controlled Folder Access
Bypass|Not Fixed|

## Slide 90

# Alternative Token Extraction Method

Dump the OneDrive.exe process Search for “WLID1.1 t=”

Credit:

- Ariel Gamrian — Threat Security Researcher @ SafeBreach

- Finding the WLID token in a OneDrive process dump

## Slide 91

# DoubleDrive GitHub + Q&A

**@oryair1999 https://www.linkedin.com/in/or-yair/ or.yair@safebreach.com**

https://github.com/SafeBreach-Labs/DoubleDrive
