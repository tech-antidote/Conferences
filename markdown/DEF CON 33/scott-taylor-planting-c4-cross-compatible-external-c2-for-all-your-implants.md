---
title: "Planting C4 Cross-Compatible External C2 for All Your Implants"
speakers: ["Scott Taylor"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Scott Taylor - Planting C4 Cross-Compatible External C2 for All Your Implants.pdf"
pages: 22
sha256: "56c3e403ff0c7eed766516465d94844928daa59437e84d5b4525f6feb8022828"
text_chars: 5494
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:13:15Z"
---
# Planting C4 Cross-Compatible External C2 for All Your Implants

**Speakers:** Scott Taylor  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Scott Taylor - Planting C4 Cross-Compatible External C2 for All Your Implants.pdf` (22 pages)


## Slide 1

**Planting C4** Cross-Compatible External C2 for All Your Implants

Scott Taylor

C4: Cross-Compatible Command & Control

1

## Slide 2

## Disclaimer

My remarks are in a personal capacity representing my own views, opinions, and experiences. My statements do not reflect the views, positions, or activities of any Sony Group company.

C4: Cross-Compatible Command & Control

2

## Slide 3

## whoami

- Red Team Operator for numerous organizations

   - Sony (current)

   - T. Rowe Price

   - MITRE

- Started as a Linux Sysadmin

- OSCP, Red Hat, Cisco, CompTIA

- B.S. Information Technology

- M.S. Cybersecurity Technology

C4: Cross-Compatible Command & Control

3

## Slide 4

## External C2

C4: Cross-Compatible Command & Control

4

## Slide 5

## LOLC2 (@mthcht)

C4: Cross-Compatible Command & Control

5


> Recovered by OCR — confidence 94/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LOLC2 (@mthcht)
Telegram
©
Mastodon
Gmail
&
Microsoft Outlook
CounterStrike 1.6
Whatsapp
Onedrive
Slack
Microsoft Power
Automate
Cloudflare
=
Microsoft Printer
Microsoft Tasks
Cisco Webex
Microsoft Azure
Functions
Strava
Microsoft Azure
Application Proxy
¥ Jira
Jira
Soundcloud
Google Translate
ee
asana
Asana
Twitter
Microsoft Graph
Spotify
Microsoft Teams
Google Sheet
©)
Github
Instagram
Matrix
Discord
Microsoft Sharepoint
Youtube
zoom
Zoom
Openai
Splunk
Google Drive
(010110)
101000
(000:
Pastebin
Virustotal
Claude
Lichess
Google Calendar
reddit
Reddit
Zulip
Microsoft Azure Blob
Storage
Mattermost
Google Slides
Dropbox
Notion
```

## Slide 6

## In the Wild

- T1102: Web Service

   - Technique added May 31st, 2017

- Used in the wild by threat actors

- Leverage trusted, legitimate sites

C4: Cross-Compatible Command & Control

6

## Slide 7

_Why are these external C2 options not available in every C2 framework?_

C4: Cross-Compatible Command & Control

7

## Slide 8

## GitHub C2

- Mythic GitHub C2 Profile

- Client written for Athena agent in .NET

- Used official GitHub .NET SDK, _octokit.net_

C4: Cross-Compatible Command & Control

8

## Slide 9

## Mythic C2 Agents

|Agent|Author|Language|
|---|---|---|
|Poseidon|its-a-feature|GoLang|
|Athena|checkymander|.NET Core|
|Apollo|djhohnstein|.NET Framework|
|Medusa|ajpc500|Python|
|Thanatos|MEhrn00|Rust|
|Venus|mattreduce|JavaScript (VS Code Extension)|
||_https://github.com/MythicAgents_||

C4: Cross-Compatible Command & Control

9

## Slide 10

## WebAssembly

C4: Cross-Compatible Command & Control

10

## Slide 11

## WebAssembly

- Compiled low-level binary format

- Near-native speed

- Cross-platform & architectureindependent

- Memory-safe sandboxed execution

- Supported by all major browsers

> • Supported by numerous WASM runtimes? C4: Cross-Compatible Command & Control

11

## Slide 12

## WebAssembly System Interface (WASI)

- Bridge to the real system!

- Run apps anywhere with a wasm runtime

   - Cloud

   - Server-side apps

   - Command-line tools

   - Embedded Systems

   - Plugin Systems

C4: Cross-Compatible Command & Control Allows access to operating

12

## Slide 13

## Extism (by Dylibso)

- Universal WASM plugin system

- Numerous language support

- Host (SDK) and Plugin (PDK) Support

- Rich WASM runtime enhancements

   - Persistent memory

   - Host-controlled HTTP

> • Execution limits, timeouts, and C4: Cross-Compatible Command & resource control Control

13

## Slide 14

## Extism

C4: Cross-Compatible Command & Control

14


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Plug-in Development Compile to Host Software
Kit (PDK) -wasm file Development Kit (SDK)
```

## Slide 15

# C4: Cross-Compatible Command and Control

C4: Cross-Compatible Command & Control

15

## Slide 16

## Hello World

Hello,
World!

Hello,
World!

Hello, Hello, Hello, World! World! World!

C4: Cross-Compatible Command & Control

16


> Recovered by OCR — confidence 89/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hello World
plugins > hello-world > src > lib.rs >...
use extism pdk::*;
#[plugin_ fn]
pub fn c4() -> FnResult<String> {
Hello,
World!
```

## Slide 17

## HTTP Test

Status:
200
Status:
200
Status:
200
Status:
200
Status:
200

C4: Cross-Compatible Command & Control

17


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HTTP Test
plugins > http-test > src > lib.rs > ...
use extism_pdk::*;
use serde::{Deserialize, Serialize};
#[plugin_ fn]
pub fn c4(url: String) -> FnResult<String> {
Create HTTP request
let req = HttpRequest: :new(&url1) ;
match http: :request::<()>(&req, None) {
Ok(response) => {
Return just the status code as a string
}
J
Err(e) => {
Return error information
let error ErrorResponse {
error: format! ("HTTP request failed: {}", e),
Ok(serde_json::to_string(&error) ?)
```

## Slide 18

## AWS S3

- Two actions: “send” and “receive”

   - Send – upload file with message

   - Receive – check for messages and delete after retrieval

- Messages/Files uploaded by folder of “agent id”

- File name is timestamp to avoid duplicate name

C4: Cross-Compatible Command & • Allows for large messagesControl

18

## Slide 19

## AWS S3: API Reference

> • Send

- Receive

{ "action": "send", "param s": { "agent_id": "string", "m essage": "string", "access_key": "string", "secret_key": "string", "region": "string", "bucket": "string", } }

{ "action": “receive", "param s": { "agent_id": "string", "access_key": "string", "secret_key": "string", "region": "string", "bucket": "string", } }

C4: Cross-Compatible Command & Control

19

## Slide 20

## Python Host: Load Plugin

- Import _extism_ package

- Create _manifest_ that allows

   - outbound HTTP requests

- Enable _WASI_

- Return loaded plugin

C4: Cross-Compatible Command & Control

20

## Slide 21

## Python Host: Run plugin

- Load plugin

- Setup message

- Call _c4_ function and pass input

- Rinse & Repeat

C4: Cross-Compatible Command & Control

21

## Slide 22

## Conclusion

- External C2 doesn’t have to be challenging

- WASM is continuously developing

- Start using C4 plugins today!

- Reach out @scottctaylor12

C4: Cross-Compatible Command & Control

22
