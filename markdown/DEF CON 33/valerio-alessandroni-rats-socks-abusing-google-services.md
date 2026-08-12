---
title: "RATs & Socks abusing Google Services"
speakers: ["Valerio Alessandroni"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Valerio Alessandroni - RATs & Socks abusing Google Services.pdf"
pages: 26
sha256: "c0c176a4b1b5d0f7d0f5b45b966dc2d7e9e5184505c8c5080020c1f77d9d0610"
text_chars: 9072
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:15:59Z"
---
# RATs & Socks abusing Google Services

**Speakers:** Valerio Alessandroni  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Valerio Alessandroni - RATs & Socks abusing Google Services.pdf` (26 pages)


## Slide 1

## **RATs & Socks abusing Google Services** Google Calendar RAT: Infrastructure-less Command&Control and GSSocks

DEF CON 33

https://blog.keephack.ing

## Slide 2

### Whoami

**Valerio “MrSaighnal” Alessandroni**

- Offensive Security Lead at EY Italy

- 10 years of experience as Pentester & Offensive Security Specialist

- Former Military

- Holder of multiple certifications: OSCP, OSEP, OSWE, OSWP, eWPTX, eCPTX, eCPPT, CEH, CRTO etc.

- Advanced Persistent Tortellini Crew Member

- Brazilian Jiu Jitsu Practitioner

- Passionate about space exploration

<u>https://www.linkedin.com/in/valerio-alessandroni/</u>

- <u>https://github.com/mrsaighnal https://blog.keephack.ing</u>

<u>https://x.com/mrsaighnal</u>

DEF CON 33

2

https://blog.keephack.ing

## Slide 3

### Index

1. Google Calendar RAT (GCR)

2. GCR - Technical Discussion

3. Security Considerations

4. DEF CON Bonus - Socks5 Over Google Services

DEF CON 33

3

https://blog.keephack.ing

## Slide 4

# **1. Google Calendar RAT (GCR)**

_"Hacking is like art. It’s about taking something that already exists and making it do something that it was never intended to do"_ Dan Kaminsky

DEF CON 33

4

https://blog.keephack.ing

## Slide 5

### 1. Google Calendar RAT

##### **Initial Idea**

- Perform C2 Without the Hassle of Building Infrastructure

- Save Time and Budget by Leveraging Existing Services

- Turn Trusted Services into C2 Channels (Living Off the Land)

- Developing a Tool which stays under the radar

- Researching New, Creative C2 Techniques

- Exploring Innovative Ideas While Keeping It Fun

DEF CON 33

5

https://blog.keephack.ing

## Slide 6

### 1. Google Calendar RAT

**GCR Diagram Flow**

CALENDAR

Command&Control

ATTACKER

Get command request from Google
Calendar
Send command response to
Google Calendar
Command
Execution
TARGET

DEF CON 33

6

https://blog.keephack.ing

## Slide 7

### 1. Google Calendar RAT

Timeline Multiple sources mentioned the research:
• Google
• Security Affairs APT41 deployed
• Wired malware
• BitDefender leveraging the
Concept publiclyGCR Proof of released on Action Team mentioned theGoogle Cybersecurity project on the Threat ••• The Hacker NewsLinkedinMedium demonstrated in technique GCR.
GitHub Horizon report Q3  • etc.
Jun  Oct Nov Jan
2023 2023 2023 2025
Threat
GCR has
Actors
been added
shared the  GCR has been
to C2Matrix
PoC on the  added to LOLC2
Project
Dark Web Project
(https://lolc2.github.io/)

Timeline

DEF CON 33

7

https://blog.keephack.ing

## Slide 8

# **2. GCR - Technical Details**

_"Simplicity is the ultimate sophistication"_ Steve Jobs

DEF CON 33

8

https://blog.keephack.ing

## Slide 9

### 2. GCR - Technical Details

##### **Google Calendar**

TITLE
Field
DESCRIPTION
Field

DEF CON 33

9

https://blog.keephack.ing


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2. GCR - Technical Details
Google Calendar
& calendar Today < > April3,2025
TITLE
Field
DESCRIPTION
Field
https://blog.keephack.ing DEF CON 33
```

## Slide 10

### 2. GCR - Technical Details

##### **Google Calendar as a Shared Database**

TITLE
Field
max length
1024 characters
DESCRIPTION
Field
max length
8191 characters

DEF CON 33

10

https://blog.keephack.ing

## Slide 11

### 2. GCR - Technical Details

##### **Google Calendar Setup**

Service Account Creation

###### **Enable Google API**

DEF CON 33

11

https://blog.keephack.ing

## Slide 12

### 2. GCR - Technical Details

##### **Google Calendar RAT Setup**

DEF CON 33

12

https://blog.keephack.ing


> Recovered by OCR — confidence 81/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2. GCR - Technical Details
Google Calendar RAT Setup
pollingTime = 0
VY def print_banner():
15 banner = “
20 : | ; | hi” Command&Control via Google Calendar Events
https: //github.com/MrSaighnal/GCR-Google-Calendar-RAT
29 print(banner)
30 time.sleep(1.5)
https://blog.keephack.ing DEF CON 33
12
```

## Slide 13

### 2. GCR - Technical Details

##### **Google Calendar RAT Demo**

TARGET MACHINE ATTACKER MACHINE

###### <u>VIDEO LINK: https://github.com/MrSaighnal/DEFCON33/blob/main/slide_13_GCR_demo.mp4</u>

DEF CON 33

13

https://blog.keephack.ing

## Slide 14

# **3. Security Considerations**

_"Simplicity is the ultimate sophistication"_ Steve Jobs

DEF CON 33

14

https://blog.keephack.ing

## Slide 15

### 3. Security Considerations

##### **Analysis**

##### **Pros**

##### **Cons**

- Infrastructure-less mechanism

   - No need to buy domain name

   - No need to buy Server and/or VPS

   - ○ No need to make a history for domain or IP (trust making)

   - Exploit Google Trust

- Hard to be detected via traffic inspection

- ● High availability (Thanks to Google Infrastructure)

   - Google domains are a single point of failure

      - Not all enterprises allow interaction with Google domains (due to policy or DLP restrictions)

   - Limited to HTTPS Protocol

   - Limited to 443 Port

   - Google APIs quota limit

   - Polling based communication

- Traffic is encrypted by default (HTTPS)

- High anonymity by using Google as “proxy”

DEF CON 33

15

https://blog.keephack.ing

## Slide 16

### 3. Security Considerations

**From PoC to APT: GCR-like C2 Observed in the Wild**

In 2025, **APT41** used **Google Calendar** as a **C2 channel** , with a method strikingly **similar** to what was demonstrated in the **GCR Poc** and later attributed to their malware **TOUGHPROGRESS *** .

- Similar technique leveraging the event description field

- ▪ Same date (May 30, 2023)

DEF CON 33

*https://cloud.google.com/blog/topics/threat-intelligence/apt41-innovative-tactics

16

https://blog.keephack.ing

## Slide 17

### 3. GCR - Technical Discussion

##### **Other C2s Abusing Legitimate Services**

##### **Limitations**

**Google Slides RAT**

- Limited to an asynchronous request-response communication model for command execution

- Does not support TCP socket redirection

###### **Known Abused Google Services**

Gmail Drive Sheets

Slides Calendar Translate

- Cannot tunnel other network protocols

- Unable to handle multiple simultaneous connections

DEF CON 33

17

https://blog.keephack.ing

## Slide 18

# **4. DEF CON Bonus - Socks5 Over Google Services**

_“Hackers produce new concepts, perceptions, and sensations out of the raw data of existence”_ McKenzie War A Hacker Manifesto (2004)

DEF CON 33

18

https://blog.keephack.ing

## Slide 19

### 4. Socks5 Over Google Services

**Presenting Google Sheets Socks (GSSocks)**

- Post-Initial Access Tool which aims to stay under the radar

- Multiplatform Client and Server written in Go

- Provide SOCKS5 over Google Sheets. Usable via proxychains or other tools

- Multiplexing mechanism. Multiple bidirectional connections.

**GSSocks**

DEF CON 33

19

https://blog.keephack.ing

## Slide 20

### 4. Socks5 Over Google Services

##### **Data Flow Analysis**

SHEETS

ATTACKER MACHINE TARGET MACHINE TARGET ORGANIZATION
localhost:9191 localhost:1080
PROXYCHAINSCLIENT +  HTTPS, RDP, TCP, HTTP,  HTTPS, RDP, TCP, HTTP,
SMB ETC. SMB ETC.
GSS CLIENT GSS SERVER SOCKS5 SERVER

DEF CON 33

20

https://blog.keephack.ing

## Slide 21

### 4. Socks5 Over Google Services

**Google Sheets as a Shared Database**

**_Sender label: client/server_**

**_Socket ID_**

**_Chunk Timestamp_**

**_Base64 encoded data chunk_**

DEF CON 33

21

https://blog.keephack.ing

## Slide 22

### 4. Socks5 Over Google Services

##### **Limitations & Solutions/Optimizations**

###### SHEETS

**GSSOCKS CLIENT**

**GSSOCKS SERVER**

- ~33% overhead introduced by base64 encoding.

- Maximum of 5000 characters per cell.

- Google quota limit per account (60 requests per minute) <u>which resulted in very slow data transmission.</u>

- Splitting data to fill up to 5000 characters per cell.

- Batching read, write, and delete operations to reduce the number of requests.

- Implemented a rotational account system to increase the bitrate.

###### BEFORE

By using **1** account for the Client and **1** account for the Server:

- About 20 minutes to execute PSexec via Proxychains

- ● About 15 minutes to execute SecretsDump via proxychains

###### AFTER OPTIMIZATION

By using **4** account for the Client and **3** account for the Server:

- About 2 minutes to execute PSexec via Proxychains

- About 1 minute to execute SecretsDump via proxychains

DEF CON 33

https://blog.keephack.ing

## Slide 23

### 4. Socks Over Google Services

##### **Demo Proxychains + Impacket-SecretsDump**

<u>VIDEO LINK: https://github.com/MrSaighnal/google-sheets-socks/blob/main/video/slide_23_SecretsDump.mp4</u>

DEF CON 33

23

https://blog.keephack.ing

## Slide 24

### 4. Socks Over Google Services

##### **Detection**

###### **Process Explorer**

**142.251.209.10 mil04s50-in-f10.1e100.net 216.58.204.138 par21s05-in-f10.1e100.net**

DEF CON 33

24

https://blog.keephack.ing

## Slide 25

### 4. Socks Over Google Services

##### **Google Mitigations**

DEF CON 33

25

https://blog.keephack.ing


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
4. Socks Over Google Services
Google Mitigations
Your accounthas been [iE
disabled
(Q) @gmail.com ~
This account became unavailable on Apr 12, 2025. Starting on Mar
8, 2026, this account will be considered for deletion.
If you think your account was disabled by mistake, submit an appeal as
soon as possible.
You can also download your data from some Google services. This gives
you a way to keep your data even if your account is not restored.
Download your data Start appeal
https://blog.keephack.ing DEF CON 33
```

## Slide 26

#### **GSSOCKS Github Project**

**Thank You!**

DEF CON 33

26

https://blog.keephack.ing
