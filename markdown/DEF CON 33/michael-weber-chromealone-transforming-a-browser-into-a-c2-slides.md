---
title: "ChromeAlone - Transforming a Browser into a C2 Slides"
speakers: ["Michael Weber"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Michael Weber - ChromeAlone - Transforming a Browser into a C2 Slides.pdf"
pages: 72
sha256: "70f731756c637718756fa68ed39433a3b9f32ef67b8c69b7d3f74c4ae2cd43a8"
text_chars: 22442
ocr_pages: 17
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.4
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:07:44Z"
---
# ChromeAlone - Transforming a Browser into a C2 Slides

**Speakers:** Michael Weber  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Michael Weber - ChromeAlone - Transforming a Browser into a C2 Slides.pdf` (72 pages)


## Slide 1

# ChromeAlone

Transforming a Browser into a C2 Platform

## Slide 2

## whoami

- Mike Weber

   - Building offensive Chrome extensions since 2018

- Principal Security Engineer at Praetorian Security

   - Praetorian Labs Researcher

   - Offensive Tool Developer

   - Occasional 0-day hunter

- Who I am not

   - Director of Attack & Penetration at Protiviti

   - Senior Cyber Security Consultant at EY

   - Senior Advisor at Steelhead Advisors LLC

   - Principal Scientist at BAE Systems

   - Software Engineer at Lockheed Martin

## Slide 3

## Code + Slides Online

github.com/praetorian-inc/ChromeAlone


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Code + Slides Online
github.com/praetorian-inc/ChromeAlone
1. Draw some circles 2. Draw the rest of the owl
```

## Slide 4

## Why target the browser?

- It’s whitelisted by EDR

- It’s how the user accesses most internal resources

- It’s everywhere

- Chromium has so many built-in features, it’s practically an OS

## Slide 5

## Browser Extensions

- What you used to use to install adblockers

- ● Convenience features for power users


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Browser Extensions
What you used to use to install adblockers
@ Convenience features for power users
grammarly
```

## Slide 6

## Known Extension Abuse

- Malware authors have bought or published apps in the Chrome Store to make a quick buck

   - Adware / Click Fraud

   - ○ Crypto Mining

   - Credential + Cookie Theft

- LummaC2 sideloaded extensions as a postexploitation attack

- ● Supply Chain Attacks

   - Cyberhaven was used to attack other extensions and infect them

## Slide 7

## Malicious Extensions for Pentesting

- CursedChrome

- Cookiejacking + HTTP Traffic Proxying

- ● RedExt

- Information Extraction (History, Cookies, Page DOM, Screenshots, etc.)

- ● Sliver

- Hijacks / modifies any existing extensions on disk

- ● SquareX

   - Syncjacking / hijacking existing extensions in store with OAuth phishing

## Slide 8

## Extension Abuse Prevention

- Manifest v3 (RIP adblockers)

- Reduced capabilities of extensions regarding request interception

- ● Chrome Store Review Process

   - Every permission needs explicit justification / manual review if you ask for wide permissions

- Chrome Apps Deprecated

   - Lots of powerful capabilities like raw socket access removed from the browser…or not

## Slide 9

Isolated Web Apps (IWAs) Why do Isolated Web Apps Exist? (In Google’s words):


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Isolated Web Apps (IWAs)
Why do Isolated Web Apps Exist? (In Google’s words):
So you want to make a new Web API
Follow the TAG design principles! (https /.W3.0rg/TR/design-principles/)
1.2. “It should be safe to visit a web page”
If it’s not:
Change your API so it’s safe
Change the Web Platform to make it safe (see Cross-Origin Isolation)
1.4. “Ask users for meaningful consent”
If you can’t:
Figure out how to
Maybe enterprise only
```

## Slide 10

## Isolated Web Apps (IWAs)

For when you want something in Chrome that does something DANGEROUS

- Direct Sockets (raw TCP/UDP send/recv)

- ● Unrestricted WebUSB ● GetAllScreensMedia

## Slide 11

Isolated Web App Protections


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How do they work?
Bundling & Signing
All app resources are
bundled in a Signed Web
Bundle.
The bundle is signed by a
developer-owned key.
Isolated Web App Protections
Strict CSP
Guarantees* that all
executable content comes
from the bundle.
* apps could ship a JS interpreter
to bypass CSP eval restrictions
Isolation
Mandatory Cross-Origin
Isolation.
Storage Isolation
(StoragePartitions instead
of double-keying).
```

## Slide 12

## Isolated Web App Protections

\```
Content-Security-Policy: base-uri 'none';
                         default-src 'self';
                         object-src 'none';
                         frame-src 'self' https: blob: data:;
                         connect-src 'self' https: wss: blob: data:;
                         script-src 'self' 'wasm-unsafe-eval';
                         img-src 'self' https: blob: data:;
                         media-src 'self' https: blob: data:;
                         font-src 'self' blob: data:;
                         style-src 'self' 'unsafe-inline';
                         require-trusted-types-for 'script';
\```

## Slide 13

## Isolated Web Apps - Quotes from the Devs

"...[This] lands us in a place where the API is very abusable, it creates this sort of attractive nuisance of capability..."

"You can design a broken application...it does require that the overall application architecture...trying to be a secure application" "This is only as secure as chrome apps ever were" **"Who's going to use this besides malware authors?"**

## Slide 14

## Case Study

Let’s talk about a “Nightmare” Red Teaming scenario


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study
Let's talk about a “Nightmare” Red Teaming scenario
HashiCorp
Vault
webauthn
Endpoint
Detection
and Response
(EDR)
Lo tf
```

## Slide 15

## Case Study (Assumptions)

- The user actively logs into SSO once a day using Chrome

- ● The user NEVER logs directly into Vault ● Our goal is a machine that exposes RDP to specific credentials ONLY in Vault

- ● Vault is accessible internally via SSO with MFA on a physical Security Key

## Slide 16

## Case Study (Assumptions, Cont.)

- We trick the user to run one Powershell script on a Windows host

- This is a Post-Exploitation tool, Initial Access is out of scope

- ● Minus the Powershell script, EDR is fine-tuned and the SOC is good

- ● Chrome is whitelisted by EDR for network traffic

## Slide 17

Architecture

## Slide 18

## Slide 19

## The Plan

- **Sideload our Extension + Isolated Web App**

- ● Capture Okta SSO Credentials at Login + Session-ride ● Tunnel Traffic through User via SOCKS

- ● Trick User into Authenticating to Vault ● RDP into Target via SOCKS ● WIN!

## Slide 20

## Sideloading Chrome Extensions

- Stored in JSON file on disk

- Could be Preferences or Secure Preferences

- ● Individual Extensions request permissions ● Very common to ask for dangerous permissions

   - This one is Adobe Acrobat

## Slide 21

## Sideloading Chrome Extensions

- Stored in JSON in Preferences/Secure Preferences file on disk

- ● Secured against modification by hash calculations

- Hash calculations replicated by Trotus/Elex adware in 2016

   - Discussed by tigzy from Adlice

- Public PoCs from Nicholas Murray + Gordon Long for Windows + MacOS

## Slide 22

Sideloading Chrome Extensions


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sideloading Chrome Extensions
Permissions
Read and change your browsing history on all your signed-in devices
Block content on any page
Read data you copy and paste
Communicate with cooperating native applications
Site access
Allow this extension to read and change all your data on websites you visit: @ On all sites
Site settings
Pin to toolbar
Allow in Incognito
Warning: Google Chrome cannot prevent extensions from recording your browsing history. To
disable this extension in Incognito mode, unselect this option.
Allow access to file URLs
Collect errors
```

## Slide 23

Installing Isolated Web Apps

● Unlike extensions, IWAs don’t touch any JSON files


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Installing Isolated Web Apps
@ Unlike extensions, |WAs don’t touch any JSON files
Download || Copy to Clipboard
Isolated Web Apps
Discover updates of policy-installed IWAs now
Developer Mode
Install IWA via Dev Mode Proxy: |http://localhost:8000.
Install IWA from Signed Web Bundle: | Select fie...
Install IWA from Update Manifest: [htip:/localhost:8000/update_manifest json || Fetch
Installed Dev Mode IWAs
* Google Keep (1.0) —> (/Users/weber/Library/Application Support/Google/Chrome/Profile 2/iwa/73k5vauxtch7euhx/main.swbn)
Perform update now
"IsolatedWebAppPolicyManager", "WebAppDirectoryDiskState"
```

## Slide 24

## Isolated Web Apps on Disk

● That’s not JSON at all…

## Slide 25

## LevelDB

- An open source Google DB Format ○ With mediocre open source tooling…


> Recovered by OCR — confidence 70/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LevelDB
@ An open source Google DB Format
© With mediocre open source tooling...
&” LevelDB Viewer
File
Key
bytearray(b'web_apps-dt-. bytearray(b'\nV\n https://drive.google.com/7ifhs=2\x12\x0cGoogle Drive\x18\x01"\x19https://drive.google.com/
bytearray(b'web_apps-dt-... bytearray(b'\n[\n%https://www.youtube.com/?feature=ytca\x12\x07YouTube\x 18\x01"\x 18https://www.youtube.com/
bytearray(b'web_apps-dt-... bytearray(b'\nx\n2https://mail.google.com/mail/?usp=installed_webapp\x12\x05Gmail\x18\x01*\x1dhttps://
bytearray(b'web_apps-dt-... bytearray(b"\n\x91\x01\n:https://docs.google.com/presentation/?usp=installed_webapp\x 12\x06Slides\x 18\x01*%https:
bytearray(b'web_apps-dt-... / ‘\nT\n\ mail.google.com/chat/\x12\x0bGoogle Chat\x18\x01*\x1dhttps://mail.google.com/ch
10 bytearray(b'web_apps-dt bytearray(b'\n\x87\x06\nHisolated-app://d6sii27z6gonfdc7kcuddjtxhfpdvgcqdy2toutlissffdi7cfzqaaic/\x 12\x0bGoog!
```

## Slide 26

## LevelDB

● Actually fairly straightforward layout

- But that bit about CRC-32 isn’t QUITE right…


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LevelDB
e Actually fairly straightforward layout
° But that bit about CRC-32 isn’t QUITE right...
CRC-32 of block data
Int16 data length for this
block
Block type (see below):
1: Full
2: First
3: Middle
4: Last
```

## Slide 27

## CRC-32C

- It’s this: https://github.com/google/leveldb/blob/main/util/crc32c.h

- ● Save yourself the time and just use their implementation.

   - Don’t forget to mask

## Slide 28

## Protobuf

### The value of each key is a serialized Protobuf object

Found at https://chromium.googlesource.com/chromium/src/+/main/chrome/browser/web_applications/proto/web_app.proto#198

## Slide 29

## Sideloading Isolated Web Apps

- Serialize your app into a Protobuf object

- ● Calculate the CRC-32C for  the object

- ● Add it into the SyncData LevelDB structure ● Make sure these flags are turned on

   - Thankfully these ARE in JSON in ./Local State

## Slide 30

## Sideloading Isolated Web Apps

- Other Details like:

   - How to calculate the Isolated Web App ID

   - How to run the app from the command line

   - How to run the app without showing it to the user

## Slide 31


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How to draw an owl
1. Draw some circles 2. Draw the rest of the owl
```

## Slide 32

## DOORKNOB

- Powershell scripts to sideload Chrome Extensions + IWAs ○ Provide an extension folder or a signed web app bundle and it generates the installer for you.

- Loads with minimal user interaction

   - Chrome needs to restart to load the extension, but we can maintain window/tab state

## Slide 33

## The Plan

- ~~Sideload our Extension + Isolated Web App~~

- **Capture Okta SSO Credentials at Login + Session-ride**

- ● Tunnel Traffic through User via SOCKS

- ● Trick User into Authenticating to Vault ● RDP into Target via SOCKS ● WIN!

## Slide 34

## Malicious Chrome Extensions

- Since we’re sideloading, we ask for ALL the scary permissions

   - background keeps Chrome running even if the user closes it

   - ○ clipboardRead is for capturing copied credentials

   - cookies is for stealing user sessions

   - ○ declarativeNetRequest is for disabling CSP + X-FrameOptions

   - history gives context for what the user visits regularly and when

- <all_urls> gives us these permissions for EVERYTHING

- ● Not how we capture most credentials though ○ Thanks Manifest v3

## Slide 35

## Malicious Chrome Extensions

- Content scripts do the heavy lifting

   - Can inject into every page

- Intercept EVERY form submission

- ● We need to run in both “Worlds”

   - MAIN

   - ISOLATED

- Won’t the user notice? ○ Remember that bit about wasm-unsafe-eval…

## Slide 36

## WASM

- If you thought javascript sucked to analyze…

- ● Oh yeah, it’s also the entire Golang runtime compiled into WASM


> Recovered by OCR — confidence 81/100 on the text kept, 48/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
WASM
e If you thought javascript sucked to analyze...
@ Oh yeah, it’s also the entire Golang runtime compiled into WASM
«const 125216)
«const 125232)
«const 125856)
«const 125873)
«const 126528
«const 127232
«const 127936)
«const 127992) "
«const 128056
«const 128672)
«const 128792)
«const 128816)
«const 130272)
«const 130304
«const 130392
«const 130416)
«const 131456
«const 131488
«const 131576)
«const 132672)
«const 132704)
«const 132792
«const 134080
«const 135744)
«const 135864)
«const 137504
«const 137536)
«const 137624)
$label29
lock $label28
k $label27
ock $label26
$label25
block $label24
b $label23
k $label21
b Slabel19
ock $label18
block $label17
block $label16
k $label13
block $label12
b k $label11
$label10
k $label9
block $label8
block $label
```

## Slide 37

## WASM

- There’s no good tooling for it - Ghidra chokes on Hello World.

- ● wasm-unsafe-eval is an all or nothing permission

- Cannot load WASM without this CSP permission

- ● You can call back out into javascript from your WASM to essentially have unsafe-eval ○ Or you can use it to load more WASM you dynamically decrypt and/or receive over the wire

## Slide 38

WASM vs. Javascript


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WASM vs. Javascript
package main
import (
“syscall/js"
var wasmModule []byte
func main() {
go. run(wasmModule. instance) ;
wasmArray := js.Global().Get("Uint8Array") .New( len(wasmModule
js.CopyBytesToJS(wasmArray, wasmModule)
go0bj := js.Global().Get("Go") .New
promise := js.Global().Get("WebAssembly").Call("instantiate", wasmArray, go0bj.Get("importObject"
promise.Call("then", js.FuncOf(func(this js.Value, args []js.Value) interface{} {
instance := args[@].Get("instance")
go0bj.Call("run", instance
return nil
```

## Slide 39

## WASM

- The Chrome Store review process has no way to deal with this


> Recovered by OCR — confidence 84/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WASM
e@ The Chrome Store review process has no way to deal with this
| MALWARE
| ANALYST
```

## Slide 40

## Capturing Credentials

- Javascript is super flexible

- ● We can just add extra listeners to anything

- targetForm.addEventListener(“submit”, credStealerFunction);

- ● If you want to fully replace functions, you can do that too

   - navigator.credentials.get = ourWebAuthnInterceptorFunction

## Slide 41

## Capturing Credentials

● Every form submission gets relayed back to our command & control ○ No red highlighting or alerts in the actual deployed extension

## Slide 42

## Shelling Out

- This talk is about only using Chrome ○ But sometimes we need help

- ● NativeMessaging to the Rescue! ● A mechanism to run other programs

## Slide 43

## Native Messaging

- Requires writing registry keys and files to disk

   - Since we’ve already sideloaded we get this for free

   - DOORKNOB has this built in if you want to use it

## Slide 44

## Native Messaging

- The configuration JSON is fairly static

- Allowed_origins, name, and path are all that matter

- ● All binaries are required to process stdio for passing messages

## Slide 45

## Native Messaging

### ● Not exactly subtle


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Native Messaging
@ Not exactly subtle
v © chrome.exe 63.18MB GOADF9725...\localuser Google Chrome
@ chrome.exe 6 6.43 MB - 725...\localuser Google Chrome
@ chrome.exe 19.05 MB ADF97 ocaluser Google Chrome
@ chrome.exe 6 18.36 MB ADF97 ocaluser Google Chrome
€ chrome.exe 512 8.9 MB - 725...\ Google Chrome
€ chrome.exe 25.46 MB c Google Chrome
€ chrome.exe 2 69.08 MB - 7 jocaluser Google Chrome
€ chrome.exe 6060 60.5 MB 9 ocaluser Google Chrome
€ chrome.exe 93 MB jocaluser Google Chrome
@ chrome.exe 2 26.13 MB ~GOADF97 ocaluser Google Chrome
@ chrome.exe 86.73 MB GOADF97 ocaluser Google Chrome
@ chrome.exe 7.14MB GOADF9725...\localuser Google Chrome
@ chrome.exe 3 15.35 MB GOADF97 ocaluser Google Chrome
@ chrome.exe 76 12.74MB GOADF97 ocaluser Google Chrome
cmd.exe 1.86MB GOADF9725...\localuser Windows Command Processor
conhost.exe } 5.67 MB - 7 jocaluser Console Window Host
NativeAppHost.exe 713, 4.53 MB 7 7 ocaluser NativeAppHost
```

## Slide 46

## Native Messaging

- Not exactly subtle

   - `C:\Windows\system32\cmd.exe /d /s /c "c:\path\to\native_host.exe"`

\```
chrome-extension://ihdbjhcjkmijbmdbfnebmoikoahfogge/ --parent-window=0" < \\.
\```

      - `\pipe\chrome.nativeMessaging.in.b4b2575ecc3200cd > \\.`

      - `\pipe\chrome.nativeMessaging.out.b4b2575ecc3200cd`

   - ALL NativeMessaging looks like this, so EDR can’t ban chrome.exe spawning cmd.exe

- Binary needs to be written to process Chrome specific messages…

   - It DOES load the binary though, so you CAN get code execution through DLL sideloading

## Slide 47

## HOTWHEELS

- A weaponized WASM Browser Extension

   - Credential Jacking

   - NativeMessaging Shelling Out

   - Session Theft

   - File Read Operations

   - History Read Access

## Slide 48

## The Plan

- ~~Sideload our Extension + Isolated Web App~~

- ~~Capture Okta SSO Credentials at Login + Session-ride~~

- ● **Tunnel Traffic through User via SOCKS**

- ● Trick User into Authenticating to Vault ● RDP into Target via SOCKS ● WIN!

## Slide 49

## Tunneling Traffic

- We could just use CursedChrome…

- ● But we have all these DANGEROUS IWA powers

## Slide 50

## Direct Sockets

● The primary IWA feature that we will abuse


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Direct Sockets
@ The primary IWA feature that we will abuse
Use cases
The initial motivating use case is to support creating a web app that talks to servers and devices that have their own protocols incompatible
with what's available on the web. The web app should be able to talk to a legacy system, without requiring users to change or replace that
system.
¢ Secure Shell
e Remote Desktop Protocol
e printer protocols
¢ Mail
* IRC
¢ |OT smart devices
¢ Distributed Hash Tables for P2P systems
¢ Resilient collaboration using IPFS
e Virtual Desktop Infrastructure (VDI)
```

## Slide 51

## Direct Sockets

● Slightly weird usage restrictions hidden in the specification ○ Not sure how this number got picked…isn’t ½ of 65536 32768?

## Slide 52

Direct Sockets

## Slide 53

## Direct Sockets

- Isolated Web Apps are supposed to remain isolated from the browser

- But you can host a TCPSocketServer which the browser can connect to

- ● Implement a Websocket Server using Direct Sockets for internal comms

- Now we have the power of chrome extensions + IWAs working together

- ● Then implement a SOCKS server using Direct Sockets

## Slide 54


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
How to draw an owl
1. Draw some circles 2. Draw the rest of the owl
```

## Slide 55

## BLOWTORCH

- Provides a full SOCKS5 proxy to the attacker from the victim’s machine

   - All comms originate from chrome.exe which is typically whitelisted

   - Combine with cookie stealing from HOTWHEELS to session ride with network position

- Yes, RDP works

## Slide 56

## The Plan

- ~~Sideload our Extension + Isolated Web App~~

- ~~Capture Okta SSO Credentials at Login + Session-ride~~

- ● ~~Tunnel Trafc through User via SOCKS~~ fi

- **Trick User into Authenticating to Vault**

- ● RDP into Target via SOCKS ● WIN!

## Slide 57

## WebAuthn

● Passwordless authentication using keys stored on external devices ○ Often used as an additional authentication factor ○ Phishing Resistant

## Slide 58

## Unrestricted WebUSB Permissions

● Isolated Web Applications can access restricted devices

○ Brings back an old attack vector from 2018


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Unrestricted WebUSB Permissions
@ lsolated Web Applications can access restricted devices
° Brings back an old attack vector from 2018
Chrome Lets Hackers Phish Even ‘Unphishable Yubikey Users
While still the best prote hishing attacks, some Yubikey models are vulnerable
after a recent update to
```

## Slide 59

## Unrestricted WebUSB Permissions

- Couldn’t get WebUSB to interact with YubiKeys, Keyboard, or Mouse ○ Could be partial / buggy implementation

   - Could be a skill issue

- Isolated Web Apps can’t do this…maybe extensions can?

## Slide 60

## WebAuthn

- Can we break this with Chrome Extensions?

   - First open an iFrame for the target site on page

   - Then have our injected content script trigger the desired WebAuthn request

## Slide 61

## WebAuthn

- What happens if you trigger a WebAuthn request in one tab then change tabs and do it again?

   - When you press your Yubikey, which tab’s challenge is resolved first?

## Slide 62

## WebAuthn

● What happens if you trigger a WebAuthn request in one tab then change tabs and do it again?

- The first request takes precedence over the active window/tab

## Slide 63

## WebAuthn

● What happens if you trigger a WebAuthn request in one tab then change tabs and do it again?

- But it will resolve if we press the Yubikey again

## Slide 64

## WebAuthn

- Now hook navigator.credentials.get()

   - Every time you try to auth on a tab, we secretly open an iFrame in a background tab

   - ○ Looks like the first Yubikey touch didn’t register

   - ○ If you have enough tabs this is invisible entirely

## Slide 65

## WebAuthn

- Automate capture of a WebAuthn challenge for our target every N minutes ○ Push it to the client, when they eventually use WebAuthn they’ll get hit

- ● Turn WebAuthn targets into Push Notification Spam

   - If you’re feeling aggressive, just constantly pop up WebAuthn requests until they press it

## Slide 66

## PAINTBUCKET

- Secretly coerce your target into answering WebAuthn challenges ○ Just provide a captured challenge to the target and wait

## Slide 67

## The Plan

- ~~Sideload our Extension + Isolated Web App~~

- ~~Capture Okta SSO Credentials at Login + Session-ride~~

- ● ~~Tunnel Trafc through User via SOCKS~~ fi

- ~~Trick User into Authenticating to Vault~~

- **RDP into Target via SOCKS**

- ● **WIN!**

## Slide 68

DEMO

## Slide 69

## Limitations

- Edge and Chrome have different implementation details

   - No Unrestricted WebUSB in Edge, for example

   - But it DOES load IWAs…it got stuck in an infinite loop until recently

- Isolated Web Applications are constantly changing

   - They might restrict installations to apps signed by Google by default instead of anyone

- Some of the permissions don’t have working demos

- ● DOORKNOB is Windows + Chrome only…for now

## Slide 70

## Defensive Recommendations

- Enterprise Browser Policy stops (some of) this

   - ExtensionInstallBlocklist = *

      - _<u>https://chromeenterprise.google/policies/#ExtensionInstallBlocklist</u>_

   - ExtensionInstallAllowList = <what your org needs> ■ _<u>https://chromeenterprise.google/policies/#ExtensionInstallAllowlist</u>_

- There is nothing to explicitly disable Isolated Web Apps right now

- ● Watch for any file modifications of Chrome data not by Chrome

   - Secure Preferences, Preferences, Local State, or LevelDB files

- Watch for NativeMessaging registry entry modifications

   - `HKCU\HKLM\SOFTWARE\Google\Chrome\NativeMessagingHosts\com.my_company.my_application`

## Slide 71

## Thank You!

Code is online at github.com/praetorian-inc/ChromeAlone

● If you have questions or success stories let me know via @bouncyhat

## Slide 72

## References

- Offensive Browser Extension Development - https://www.irongeek.com/i.php?page=videos/derbycon8/track-4-02-ofensivef -browser-ex <u>tension-development-michael-weber</u>

- ● Browser Extension Supply Chain Attacks - https://www.darktrace.com/blog/cyberhaven-supply-chain-attack-exploiting-browser-extensi <u>ons</u>

- ● LummaC2 Sideloading - https://www.esentire.com/blog/lummac2-malware-and-malicious-chrome-extension-delivered-via-dll-side-loa <u>ding</u>

- ● BlinkOn 19 - https://www.youtube.com/watch?v=Q3b5NB-7HQQ ● CursedChrome - https://github.com/mandatoryprogrammer/CursedChrome ● RedExt - https://github.com/Darkrain2009/RedExt ● Browser Syncjacking - https://labs.sqrx.com/browser-syncjacking-cc602ea0cbd0 ● Isolated Web Apps Explainer - https://github.com/WICG/isolated-web-apps ● LevelDB Writeup - https://www.cclsolutionsgroup.com/post/hang-on-thats-not-sqlite-chrome-electron-and-leveldb ● DirectSockets Explainer - https://wicg.github.io/direct-sockets/ ● WebUSB Yubikey Phishing - https://www.wired.com/story/chrome-yubikey-phishing-webusb/
