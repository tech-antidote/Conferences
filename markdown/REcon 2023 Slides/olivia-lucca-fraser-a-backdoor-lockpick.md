---
title: "A Backdoor Lockpick"
speakers: ["Olivia Lucca Fraser"]
conference: "REcon"
conference_full: "REcon 2023"
edition: ""
year: 2023
source_pdf: "REcon 2023 Slides/Olivia Lucca Fraser_A Backdoor Lockpick.pdf"
pages: 144
sha256: "9ddd5b227a005329ae5173bae33c3b8a1d6fc0816cbf143e52b93a7f00f01322"
text_chars: 63131
ocr_pages: 83
has_ocr: true
redacted_secrets: 0
companion_files: ["Olivia Lucca Fraser_A Backdoor Lockpick.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:27:50Z"
---
# A Backdoor Lockpick

**Speakers:** Olivia Lucca Fraser  
**Conference:** REcon 2023  
**Source:** `REcon 2023 Slides/Olivia Lucca Fraser_A Backdoor Lockpick.pdf` (144 pages)


## Slide 1

## **A Backdoor Lockpick Reversing & Subverting Phicomm’s Backdoor Protocol**

**Olivia Lucca Fraser** Staff Research Engineer, Zero Day Research Team June 9th, 2023

## Slide 2

**Introducing the Wavlink AC1200**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing the Wavlink AC1200
©tenable
```

## Slide 3

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
es
6.8in 7
k
bf a w
i 6.6in >\
x — —_
ce =
1.2in Se eS a
: > 06
de ~~ > Ye
6.6in
——>| Otenable
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eae
PHICOMM
6.6in
Hard to setup, suspicious
wifi
By MC on March 22, 2021
| purchased this router based on the look,
price and the reviews to update my older
router. | got it delivered on time and in great
condition. My problem was the set up. |
plugged all the wires correctly. When | tried
to connect to the internet, the WiFi pops up
with a different name than what the
instructions said. PHICOMM instead of
WAVLINK®. Quite suspicious! Then a
window comes up on my computer with an
insecure website with the PHICOMM name
and a totally different language. | tried
different ways like typing Wifi.wavlink.com as
suggested in the instructions and it leads me
back to the phony website. Hopefully my
information was not hacked by this website.
So | am returning this router and hopefully
this review will help anyone before they
purchase.
Otenable
```

## Slide 6

###### **A Baidu search for “Phicomm K2G A1” brought up listings for a familiar-looking device:**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A Baidu search for “Phicomm K2G AT" brought up
listings for a familiar-looking device:
~ DTW
Bs HSSOi 9ey sean’ seme tame Few 2m
(PS SASH BABK2G-A1 1200OMNMARBAS WiFiF BRE F
JEWAND (K274RHR)
Me nvawer
eth AX3
C)
179 2 “379 Smee wes B79 28
©tenable
```

## Slide 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
-
Corporate needs you to find the differences
between this router and this router
Otenable
```

## Slide 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
; They're the same fouter.
Otenable
```

## Slide 9

**~~Introducing the Wavlink AC1200~~ Introducing the Phicomm K2G A1!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introducing the Waviink AC1200
Introducing the Phicomm K2G Al!
- — ——— Se
“ ©tenable
```

## Slide 10

The _System Status_ ( 系统状态 ) page identifies the device model as K2G, hardware version A1, running firmware version **22.6.3.20** .

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
http://192.168.2.1/cgi-bin/|
The System Status
O & 192,168.21 ( RERA ) page
identifies the device
model as K2G,
hardware version Al,
running firmware
version 22.6.3.20.
Otenable
```

## Slide 11

**Using a Known Post-Auth Command Injection Vuln to Gain Shell Access**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Using a Known Post-Auth
Command Injection Vuln to Gain
Shell Access
©tenable
```

## Slide 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FS
} oo
WWW UPA
eer In]
MT:
OOL .cOoM
```

## Slide 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
r—( root@ kali)-[~]
—# telnet 192.168.2.1
Trying 192.168.2.1...
Connected to 192.168.2.1.
Escape character is **]'.
BusyBox v1.22.1 (2018-05-07 16:22:00 CST) built-in shell (ash)
Enter ‘help’ for a List of built-in commands.
ON Oe Dn) an Vv Ms 7 1 ee eee es
Vie pene VAR! fd 4 FAST NS LASTS Fee
5 Ae a te td fm oy BE Ey AN TAB 9 Ow Jest
Barrier Breaker, unknown
PID=K2GA1
BUILD_TYPE=release
BUILD_NUMBER=20
BUILD_TIME=20180507-161609
MTK OpenWrt SDK V3.4
revision : 57c6a60d
benchmark : APSoC SDK 5.0.1.0
kernel : 144992
root@K2G:/ww/cgi-bin# fj
= ~
- . .
©Otenable
```

## Slide 14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
root@K2G:/ww/cgi-bin# netstat -tunlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name
tcp t') ® 0.0.0.0:80 0.0.0.0:* LISTEN 4319/Lighttpd
tcp t') @ 0.0.0.0:8082 0.0.0.0:* LISTEN 2284/adpush
tcp t) ®@ 0.0.0.0:53 0.0.0.0:* LISTEN 5850/dnsmasq
tcp () @ :::5000 {3% LISTEN 6020/miniupnpd
tcp () @ 32:53 Sonat LISTEN 5850/dnsmasq
tcp ® @, ssz2a :* LISTEN 26584/telnetd
udp () @ 0.0.0.0:53 @.0.0.0:* 5850/dnsmasq
udp () @ 0.0.0.0:67 @.0.0.0:* 5850/dnsmasq
udp () ® 0.0.0.0:1900 @.0.0.0:* 6020/miniupnpd
udp t') @ 192.168.2.1:52610 0.0.0.0:* 6020/miniupnpd
udp 1’) @ 0.0.0.0:21210 0.0.0.0:* 1847/telnetd_startu
udp (1) @ 192.168.2.1:5351 @.0.0.0:* 6020/miniupnpd
udp (1) @ :::53 be 5850/dnsmasq
udp ts) @ st: 5a52 Se 6020/miniupnpd
root@K2G:/ww/cgi-bin# fj
—— —N_
i — ae We
a a a 4 TS Oss ——
ae 2 é . DSSS : — = —
2 = —— s >_- e OL ST —— <= SE eo
—< OO SS — tenable
```

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
roota@K2G: /ww/cgi-bin# netstat -tunlp
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address Foreign Address State PID/Program name
tcp t') ® 0.0.0.0:80 0.0.0.0:* LISTEN 4319/Lighttpd
tcp t') @ 0.0.0.0:8082 0.0.0.0:* LISTEN 2284/adpush
tcp t) ®@ 0.0.0.0:53 0.0.0.0:* LISTEN 5850/dnsmasq
tcp () @ :::5000 {3% LISTEN 6020/miniupnpd
tcp () @ 32:53 Sonat LISTEN 5850/dnsmasq
tcp 1) @. ssoae i* LISTEN 26584/telnetd
udp ts) @ 0.0.0.0:53 @.0.0.0:% 5850/dnsmasq
udp () @ 0.0.0.0:67 @.0.0.0:* 5850/dnsmasq
udp () ® 0.0.0.0:1900 @.0.0.0:* 6020/miniupnpd
udp t') @ 192.168.2.1:52610 0.0.0.0:* 6020/miniupnpd
udp (') ®@ 0.0.0.0:21210 0.0.0.0:* > 1847/telnetd_startu
udp t) @ 192.168.2.1:5351 0.0.0.0:* 6020/miniupnpd
udp () O 22°53 sas 5850/dnsmasq
udp (1) @ st: Sa54 ace 6020/miniupnpd
root@K2G:/ww/cgi-bin# fj
———
SS
= SS >.
> =.
SS
```

## Slide 16

#### **telnetd_startup: first impressions**

● 32-bit MIPS (Little Endian) ELF binary

● Runs as a daemon with root permissions ● Listens (quietly) on UDP port  21210

## Slide 17

**A few interesting strings…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
——
134
981
98F
9f5
a30
a56
aoa
b7d
4288
4204
42b8
42e8
4314
4330
5482
F688
445c
4480
4500
4518
4538
—~ 4554
4580
45a
45b4
LUL 7 LIPS TILETSLT LITYS. LAL
/1ib/1ld-uClibc.so.®
__uCLlibc_main . . .
libssl.so.1.0. A few interesting strings...
Libcrypto.so.1.0.0
BN_set_word
RSA_public_encrypt
RSA_public_decrypt
Libgcc_s.so.1
ABCDEF1234
checkState error
Usage: %s clear - clear telnetd startup flag
%s show - show telnetd startup flag
%s - start daemon
E541A631680C453DF31591A6E29382BCSEAC969DCFDBBCEAG64CB49CBE36578845C507BF5E 7AGBCD724AFA7063CA7
6E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D38F3C6650CDB4590C1208B91
DQ393241898C1FQ@5A6D500C7066298CEBAZEF31QFEDBZE7AF52829E9F 858691
Error: Unable to create the timer.
Warning: Read on timer pipe failed.
K2_COSTDOWN__VER_3.@
iwpriv raQ e2p 26=7010
telnetd -1 /bin/login.sh
READ TELNETD flag: Out of scope
iwpriv raQ e2p 26=FFFF
telnetd default on —
telnetd default off
=e = > Ni —- ———- 7 HLS! iavle
```

## Slide 18

**A few interesting strings…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
——s
FO RUL 7 UNIPsTILETSLD LITYS. LAL
134 /1lib/1ld-uClibc.so.@
981 __uCLibc_main . . .
98f libssl.so.1.0.0 A few interesting strings...
9f5 libcrypto.so.1.0.0
a30 BN_set_word
a56 RSA_public_encrypt
a69 RSA_public_decrypt
b7d libgcc_s.so.1
4288 ABCDEF1234
4204 checkState error
42b8 Usage: %s clear - clear telnetd startup flag
42e8 %s show - show telnetd startup flag
4314 %s - start daemon
4330 E541A631680C453DF31591A6E29382BCS5SEAC969DCFDBBCEA64CB49CBE36578845C507BF5E 7AGBCD724AFA7063CA7
54826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D38F 3C6650CDB4590C1208B91
F688D0393241898C1FQ@5A6D500C7066298CEBAZEF31QFEDBZE7AF52829E9F 858691
445c Error: Unable to create the timer.
4480 Warning: Read on timer pipe failed.
4500 K2_COSTDOWN__VER_3.@
4518 iwpriv raQ@ e2p 26=7010
4538 telnetd -1 /bin/login.sh
“©4554 READ TELNETD flag: Out of scope
4580 iwpriv raQ@ e2p 26=FFFF
45a@ telnetd default on —
45b4 telnetd default off
——e = >» <u > 7 WLS iavle
```

## Slide 19

**A few interesting strings…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FO RUL 7 UNIPsTILETSLD LITYS. LAL
134 /lib/1d-uClibc.so.@
981 __uCLibc_main . . .
98f libssl.so.1.0.0 A few interesting strings...
9f5 libcrypto.so.1.0.0
a30 BN_set_word
a56 RSA_public_encrypt
a69 RSA_public_decrypt
b7d libgcc_s.so.1
4288 ABCDEF1234
4204 checkState error
42b8 Usage: %s clear - clear telnetd startup flag
42e8 %s show - show telnetd startup flag
4314 %s - start daemon
4330 E541A631680C453DF31591A6E29382BCS5SEAC969DCFDBBCEA64CB49CBE36578845C507BF5E 7AGBCD724AFA7063CA7
54826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D38F 3C6650CDB4590C1208B91
F688D0393241898C1FQ@5A6D500C7066298CEBAZEF31QFEDBZE7AF52829E9F 858691
445c Error: Unable to create the timer.
4480 Warning: Read on timer pipe failed.
4500 K2_COSTDOWN__VER_3.@
__ _4518 iwpriv ra@ e2p 26=7010
SS 4538 telnetd -1 /bin/login.sh
= 4554 READ TELNETD flag: Out of scope
~ 4580 iwpriv raQ e2p 26=FFFF
45aQ@ telnetd default on —
~~ 45b4 telnetd default off
es — ™ Ne So a> HLS! iavle
```

## Slide 20

**A few interesting strings…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4538 telnetd -1 /bin/login.sh
== 4554 READ TELNETD flag: Out of scope
FO RUL 7 UNIPsTILETSLD LITYS. LAL
134 /lib/1d-uClibc.so.@
981 __uClibc_main
98f libssl.so.1.0.0 A few interesting strings...
9f5 libcrypto.so.1.0.0
a30 BN_set_word
a56 RSA_public_encrypt \
a69 RSA_public_decrypt
b7d libgcc_s.so.1
4288 ABCDEF1234
4204 checkState error
42b8 Usage: %s clear - clear telnetd startup flag
42e8 %s show - show telnetd startup flag
4314 %s - start daemon
4330 E541A631680C453DF31591A6E29382BCS5EACI69DCFDBBCEA64CB49CBE36578845C507
54826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D
F688D0393241898C1FQ@5A6D500C7066298CEBAZEF310F6DBZE 7AF52829E9F 858691
445c Error: Unable to create the timer.
4480 Warning: Read on timer pipe failed.
450@ K2_COSTDOWN__VER_3.0
4518 iwpriv raQ@ e2p 26=7010
4580 iwpriv raQ@ e2p 26=FFFF
45a@ telnetd default on
45b4 telnetd default off
3F5E7AOBCD/724AFA7063CA7
F3C6650CDB4590C1208B91
==
— — » xe > a> WLS iavle
```

## Slide 21

**A few interesting strings…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
=
4538 telnetd -1 /bin/login.sh
== 4554 READ TELNETD flag: Out of scope
FO RUL 7 UNIPsTILETSLD LITYS. LAL
134 /lib/1d-uClibc.so.@
981 __uCLibc_main
98f libssl.so.1.0.0 A few interesting strings...
9f5 libcrypto.so.1.0.0
a30 BN_set_word
a56 RSA_public_encrypt \
a69 RSA_public_decrypt
b7d libgcc_s.so.1
4288 ABCDEF1234
4204 checkState error
42b8 Usage: %s clear - clear telnetd startup flag
42e8 %s show - show telnetd startup flag
4314 %s - start daemon
4330 E541A631680C453DF31591A6E29382BCS5EACI69DCFDBBCEA64CB49CBE36578845C507
54826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D
F688D0393241898C1FQ@5A6D500C7066298CEBAZEF310F6DBZE 7AF52829E9F 858691
445c Error: Unable to create the timer.
4480 Warning: Read on timer pipe failed.
450@ K2_COSTDOWN__VER_3.0
4518 iwpriv raQ e2p 26=7010
4580 iwpriv raQ@ e2p 26=FFFF
45a@ telnetd default on
45b4 telnetd default off
~ - — - - - -
3F5E7AOBCD/724AFA7063CA7
F3C6650CDB4590C1208B91
—
eS ~ - ™ \_ —S—— a wy tel iavle
```

## Slide 22

**The Main State Machine of the telnetd_startup Service**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Main State Machine of the teInetd_startup Service eine mews
if (
41 = 1) {
= FUN_00401518( 3
if ( != 2) goto code_r0x00401e3c;
}
if (DAT_od O== 2) {
= FUN_0401518(
if ( 24
memset (&
memcpy (& 4 TDOWN.
memset (
FUN_00401f30(
FUN_00402b28(
FUN_00402c28(
memcpy ( &
sendto(DAT_¢
+
break;
$
if (DAT_0¢ @ != 0) goto LAB_00401af0;
= FUN_0401518( 1205
if ( t= 2) {
memset (SDAT_0¢
memcpy (& 1041 ,
= FUN_0040175c();
®) break;
FUN_@04015b0()
FUN_004016b0() ;
sendto(DAT_004147e4, &D)
FUN_00401624();
FUN_0040182c();
> goto LAB_00401e1c;
+
-. }
= } while( true );
, +
. goto LAB_00401eb8;
```

## Slide 23

###### **The Main State Machine of the telnetd_startup Service**

**We begin in state 2…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
; . . = recvfrom( 0X100, 0x100, &
The Main State Machine of the telnetd_startup Service af
at = FUN. Sinieieta ;
if ( != 2) goto code_r0x00401e3c;
Lizse
We begin in state 2... sea ee es
= FUN_00401518(
if ( 24
memset (&
memcpy (& 4 TDOWN,
memset (
FUN_@0401f30(
FUN_00402b28(
FUN_00402c28(
memcpy (&
sendto(DAT_¢
+
break;
$
if (DAT_0¢ @ != 0) goto LAB_00401af0;
= FUN_0401518( 1205
if ( t= 2) {
memset (SDAT_0¢
memcpy (& 1041 ,
= FUN_0040175c();
®) break;
FUN_004015b0()
FUN_004016b0();
sendto(DAT_004147e4, 8D,
FUN_00401624();
FUN_0040182c();
: goto LAB_00401e1c;
+
= +
: } while( true );
+
goto LAB_00401eb8;
```

## Slide 24

###### **The Main State Machine of the telnetd_startup Service**

**We begin in state 2…**

**Then go to state 0…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a - . = recvfrom(_fd,
The Main State Machine of the telnetd_startup Service df (on I= BeantneneD
at = Saeraisia( 12)3
!= 2) goto code_r0x00401e3c;
in state 2... 0 =2)4
FUN_00401518(
if ( 24
memset (& e
memcpy (SDAT_00414
memset (
FUN_@0401f30(
FUN_00402b28(
FUN_00402c28(
memcpy (&DAT_(
sendto(DAT_004
Then go to state 0...
a 0 != 0) goto LAB_00401afO;
= FUN_00401518( 12)3
if (
memset (SDAT_‘
memcpy(SDAT_00414af0,
= FUN_0040175c();
FUN_004015b0()
FUN_004016b0( )
sendto(DAT_0
FUN_00401624()
FUN_0040182c();
goto LAB_00401e1c;
+
}
} while( tru
+
goto LAB_00401eb8;
```

## Slide 25

###### **The Main State Machine of the telnetd_startup Service**

We begin in state 2…
Then go to state 0…
Then proceed to state 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a - . = recvfrom(
The Main State Machine of the telnetd_startup Service #
a FUN. 00401528( 2
!= 2) goto code_r0x00401e3c;
in state 2... 0041470 == 2) {
FUN_00401518(
if (
memset (&
memcpy (&DAT_00414b ‘OSTDOWN__| 0", 0x
memset (
FUN_@0401f30(
FUN_00402b28( L E 5
FUN_00402c28( D: D
memcpy (&DAT_( 49a, 0x10);
sendto(DAT_¢ T_0¢ 10X10, 0, &
Then go to state 0...
i 2) goto LAB_00401af0;
= FUN_00401518( 12)5
if (
memset (&DAT_|
memcpy (& 10414af0,
= FUN_0040175c();
Then proceed to state 1
FUN_@04015b0()
FUN_@04016b0()
sendto(DAT_0
FUN_@0401624()
FUN_0040182c();
goto LAB_00401e1c;
+
}
} while( truc
+
goto LAB_00401eb8;
```

## Slide 26

###### **The Main State Machine of the telnetd_startup Service**

We begin in state 2…

**Then go to state 0… Then proceed to state 1**

**Which takes us to this final check before either (a) 0x7010 is written to EEPROM at offset 0x26, or (b) a telnetd service is launched**

## Slide 27

###### **The Main State Machine of the telnetd_startup Service**

**We begin in state 2…** And when the service starts, it checks the EEPROM for the 0x7010 flag, and launch telnetd if it finds it. **Then go to state 0… Then proceed to state 1 Which takes us to this final check before either (a) 0x7010 is written to EEPROM at offset 0x26, or (b) a telnetd service is launched**

## Slide 28

**STATE 2 (the initial state)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
STATE 2
(the initial state)
——
“ Otenable
```

## Slide 29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
}
= FUN_00401518( tact ya
if (i == 2) {
}
memset (&DAT_00414ba0,0, 2x80);
memcpy (&DAT_00414baQ,"K2_COSTDOWN__VER_3.0", 0x14);
memset ( tacl ,0,9x58);
FUN_00401f30( tac! iF
FUN_00402b28(auStack_e@,&DAT_00414ba0, 0x80);
FUN_00402c28( tacl ,&DAT_004149a0) ;
DAT_@0414b70 H
DAT_00414b74
DAT_@0414b78 .
DAT_00414b7c = Q;
memcpy (&DAT_00414b70, &DAT_004149a0, 0x10);
sendto(DAT_004147e4, &DAT_00414b70, 0x10,0,&
DAT_004147e0 = Q;
break;
```

## Slide 30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_004147e0 == 2) f{
= FUN_00401518( tacl 2); <
if (i == 2) {
memset (&DAT_00414ba0,0, 2x80);
memcpy (&DAT_00414baQ,"K2_COSTDOWN__VER_3.0", 0x14);
memset ( tacl ,0,9x58);
FUN_00401f30( tac! iF
FUN_00402b28(auStack_e@,&DAT_00414ba0, 0x80);
FUN_00402c28( tacl ,&DAT_004149a0) ;
DAT_@0414b70 H
DAT_00414b74
DAT_@0414b78 .
DAT_00414b7c = Q;
memcpy (&DAT_00414b70, &DAT_004149a0, 0x10);
sendto(DAT_004147e4, &DAT_00414b70, 0x10,0,&
DAT_004147e0 = Q;
}
break;
}
```

## Slide 31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int FUN_00401518(void xparam_1,int param_2)
{
int
int
char *
size t H
if (param_2 == 1) {
else {
if (param_2 != 2) {
if (param_2 == 0) {
= memcmp(param_1, &
return —( != 0);
}
puts("checkState error");
return —2;
}
“ABCDEF1234";
10;
memcmp(param_1,
return
©tenable
```

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int FUN_00401518(void *param_1,int param_2) a checkState(void *payload, int next_state)
47{
: 48 int
int ; 49 int
int 1 ; 5@ char expec ;
char *_s2; 51 size_t é ;
size_t H 52
53) if (next_state == 1) {
if (param_2 == 1) { 54\/* dead code */
= "STTH": 55 x = "STTH";
=4; 56 =4;
{
} 57 }
else {
if (param_2 != 2) {
if (param_2 == 0) {
58 else {
59 if (next_state != 2) {
6@/* dead code */
. 61 if (next_state == 0) {
= memcmp(param_1,&DAT_00404294,4); 62 = memcmp (payload, "STSE", 4) ;
return —( != 0); 63 return —( = Q);
} 64 }
puts("checkState error"); 65 puts("checkState error");
return -2; 66 return -2;
} 67 }
= "ABCDEF1234"; 68/* Note that the checkState variable is ALWAYS 2. */
= 10; 69 x = "ABCDEF1234";
70 = 10;
memcmp(param_1, 71
-1; 72 memcmp (payload,
== 0) { 73 -1;
. 74 i 1 == 0) {
= param_2; 75) = next_state;
76 +}
return ; 77, return
78}
```

## Slide 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
}
= FUN_00401518( tact ya
if (i == 2) {
}
memset (&DAT_00414ba0,0, 2x80);
memcpy (&DAT_00414baQ,"K2_COSTDOWN__VER_3.0", 0x14);
memset ( tacl ,0,9x58);
FUN_00401f30( tac! iF
FUN_00402b28(auStack_e@,&DAT_00414ba0, 0x80);
FUN_00402c28( tacl ,&DAT_004149a0) ;
DAT_@0414b70 H
DAT_00414b74
DAT_@0414b78 .
DAT_00414b7c = Q;
memcpy (&DAT_00414b70, &DAT_004149a0, 0x10);
sendto(DAT_004147e4, &DAT_00414b70, 0x10,0,&
DAT_004147e0 = Q;
break;
```

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
}
= FUN_00401518( tact ya
if (i == 2) {
}
memset (&DAT_00414ba0,0, 2x80);
memcpy (&DAT_00414baQ,"K2_COSTDOWN__VER_3.0", 0x14);
memset ( tacl ,0,9x58);
FUN_@0401f30(auStack_e@); <
FUN_00402b28(auStack_e@,&DAT_00414ba0, 0x80);
FUN_00402c28( tacl ,&DAT_004149a0) ;
DAT_@0414b70 H
DAT_00414b74
DAT_@0414b78 .
DAT_00414b7c = Q;
memcpy (&DAT_00414b70, &DAT_004149a0, 0x10);
sendto(DAT_004147e4, &DAT_00414b70, 0x10,0,&
DAT_004147e0 = Q;
break;
```

## Slide 35

**the tell-tale constants of an MD5 hash context:**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the tell-tale constants of an MD5 hash context:
void FUN_00401f30(undefined4 *param_1)
|
*param_1 = Q;
param_1[2]
param_1[1]
param_1[3]
param_1[4]
param_1[5]
return;
Qx67452301;
Q;
@xefcdab89;
@x98badcfe;
Qx10325476;
©tenable
```

## Slide 36

**the tell-tale constants of an MD5 hash context:**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
the tell-tale constants of an MD5 hash context:
void FUN_00401f30(undefined4 *param_1) void md5_init(uint *md5_context)
{ 1
*param_1 = Q; *md5_context = Q;
param_1[2] Qx67452301; md5_context [2] 0x67452301;
param_1[1] = Q; md5_context [1] Q;
param_1[3] Oxefcdab89; md5_context [3] Oxefcdab89;
param_1[4] @x98badcfe; md5_context [4] @x98badcfe;
param_1[5] @x10325476; md5_context [5] @x10325476;
return; return;
```

## Slide 37

**So, the service waits for the client to send the token “ABCDEF1234” and then responds with an MD5 hash of the string “K2_COSTDOWN__VER_3.0” padded with zeros to a 128-byte buffer.**

**It then enters STATE 0.**

## Slide 38

#### **STATE 0**

**(the second state)**

## Slide 39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c();
if ( '= Q) break;
DAT_004147e0 = 1;
FUN_004015bQ();
FUN_@04016b@();
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624();
FUN_@040182c();
goto LAB_00401e1c;
```

## Slide 40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c(); <
if ( '= @) break;
DAT_004147e0 = 1;
FUN_004015bQ();
FUN_@04016b@();
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624();
FUN_@040182c();
goto LAB_00401e1c;
```

## Slide 41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int rsa_public_decrypt_nonce(void)
{
RSA *
BIGNUM
int n;
uint
size_t
BIGNUM * (3];
= RSA_new();
[0] = BN_new();
= BN_new();
BN_set_word(a,0x10001)
BN_hex2bn( ,
"E541A631680C453DF31591A6E29382BC5EAC969DCFDBBCEA64CB49CBE36578845C507BF5E7A6BCD724AFA70
63CA754826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B38845 1D38F 3C6650C
DB4590C1208B91F688D0393241898C1F05A6D500C7066298C6BA2EF310F6DB2E7AF52829E9F858691"
i;
H
= [0];
memset (&DECRYPTED_NONCE, @, x20);
= RSA_size(rsa);
= RSA_public_decrypt(n,&ENCRYPTED_NONCE, &DECRYPTED_NONCE, rsa,3)}
if ( < 0x101) {
= strlen(&DECRYPTED_NONCE) ;
< 0x101 * 1);
```

## Slide 42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c();
if ( '= Q) break;
DAT_004147e0 = 1;
FUN_004015bQ();
FUN_@04016b@();
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624();
FUN_@040182c();
goto LAB_00401e1c;
```

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c();
if ( '= @) break;
DAT_004147e0 = 1;
FUN_004015b@(); <
FUN_@04016b@(); <
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624();
FUN_@040182c();
goto LAB_00401e1c;
```

## Slide 44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 Void generate_random_plaintext (void)
5
6 {
long
char x*
int
= random();
if (false) {
trap(7);
}
= G&RANDOMLY_GENERATED_PLAINTEXT_at_4149b@ +
iL +=
* = % @x5d + Qx21;
} while (i != 0x1f);
END_OF_PLAINTEXT = @Q;
return;
```

## Slide 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 int rsa_encrypt_with_public_key(void)
5
6 {
RSA * ;
BIGNUM xa;
int H
BIGNUM x [3];
= RSA_new();
[2] = BN_new();
= BN_new();
BN_set_word(a, ®x10001);
BN_hex2bn ( ,
"E541A631680C453DF31591A6E29382BC5EAC969DCFDBBCEA64CB49CBE36578845C507BF5E7A6BCD724AFA70
63CA754826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D38F3C6650C
DB4590C1208B91F688D0393241898C1F05A6D500C7066298C6BA2EF310F6DB2E7AF52829E9F858691"
3
- ’
= [0];
memset (G&ENCRYPTED_SECRET, 0, @x80);
= RSA_size(rsa);
= RSA_public_encrypt( , SRANDOMLY_GENERATED_PLAINTEXT_at_4149b@,&ENCRYPTED_SECRET, rsa,3);
return >> Ox1f;
```

## Slide 46

**This encrypted secret is sent to the client, as an authentication challenge.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
This encrypted secret is sent to the client, as an
authentication challenge.
©tenable
```

## Slide 47

**This encrypted secret is sent to the client, as an authentication challenge.**

**Meanwhile…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
This encrypted secret is sent to the client, as an
authentication challenge.
Meanwhile...
©tenable
```

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c();
if ( '= Q) break;
DAT_004147e0 = 1;
FUN_004015bQ();
FUN_@04016b@();
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624();
FUN_@040182c();
goto LAB_00401e1c;
```

## Slide 49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (DAT_@04147e@ != @) goto LAB_00401afQ;
= FUN_00401518( »2)3
if ( '= 2) {
memset (&DAT_00414af@,0,0x80);
memcpy (&DAT_00414af@,
= FUN_0040175c();
if ( '= @) break;
DAT_004147e0 = 1;
FUN_004015bQ();
FUN_@04016b@();
sendto(DAT_004147e4, &DAT_004149f0, 0x80,0,&
FUN_00401624(); <
FUN_0@040182c(); <
goto LAB_00401e1c;
```

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 Void xor_decrypted_nonce_with_plaintext (void)
5
6 {
byte
byte
int
byte
&DECRYPTED NONCE + i;
&RANDOMLY_GENERATED_PLAINTEXT_at_4149b@ + i;
= &XORED_ MSG 00414b80 + i;
+= 1;
* = * “ x
} while (i != 0x20);
return;
```

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6 |int set_ephemeral_keys (void)
7
8 i{
9 size t ;
10! char [512];
11) char [512];
12) uint [22];
13
14, memset( ,0,0x58);
15) sprintf ( »''%S+PERM" , &XORED_MSG_ 00414b80);
16) sprintf ( ,''%S+TEMP" , &XORED_MSG_@0414b80);
17} md5_init(md5);
18 = strlen( 3
19} md5_add(md5, ,
20 md5_digest(md5,&PERM_KEY);
21) + md5_init( );
22 = strlen(
23} md5_add(md5, 1
24 md5_digest( ,SlEMP_KEY);
25, return Q;
26\}
3
```

## Slide 52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (STATE != @) goto INCREMENT_FD_INDEX_at_4@1afQ;
= checkState( »2)3
if (S != 2) {
memset (&ENCRYPTED_NONCE,0,0x8Q);
memcpy (&ENCRYPTED_NONCE,
= rsa_public_decrypt_nonce();
if (S != 0) break;
STATE = 1;
generate_random_plaintext();
rsa_encrypt_with_public_key();
sendto(SKT, &ENCRYPTED_SECRET, ®x80,0,&
xor_decrypted_nonce_with_plaintext();
set_ephemeral_keys();
goto LAB 004@lelc;
Otenable
```

## Slide 53

#### **STATE 1**

**(the third and final state)**

## Slide 54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
if (STATE == 1) {
= checkState( 2);
if (S != 2) goto code_rQ@x00401e3c;
}
167\code_r@x@0401e3c:
168)/* Check ephemeral password */
169 if ( == Qx10) {
170 = memcmp( ,&PERM_KEY, @x10);
171 Lf (S == 0) {
172 = "iwpriv raQ@ e2p 26=7010";
173 }
174 else {
175 = memcmp( ,»&TEMP_KEY,@x10);
176 if ((S != @) || (S = is_process_running("phddns"),
177 = "telnetd -l /bin/login.sh";
178 }
179 system ( ys
180
!= @)) goto RESET_STATE_MACHINE;
©tenable
```

## Slide 55

**The message “ABCDEF1234” will send us back to the beginning.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The message “ABCDEF1234” will send
if (STATE == 1) { us back to the beginning.
= checkState( r2)3 <
if (S != 2) goto code_rQ@x00401e3c;
}
167\code_r@x@0401e3c:
168)/* Check ephemeral password */
169 if ( == Qx10) {
170 = memcmp( ,&PERM_KEY, @x10);
171 Lf (S == 0) {
172 = "iwpriv raQ@ e2p 26=7010";
173 }
174 else {
175 = memcmp( ,»&TEMP_KEY,@x10);
176 if ((S != @) || (S = is_process_running("phddns"),
177 = "telnetd -l /bin/login.sh";
178 }
179 system ( ys
180
!= @)) goto RESET_STATE_MACHINE;
©tenable
```

## Slide 56

**The message “ABCDEF1234” will send us back to the beginning.**

**But a message that matches one of these ephemeral keys will launch telnetd, either when the device reboots, or immediately.**

## Slide 57

**How is the client supposed to determine TEMP_KEY and PERM_KEY?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How is the client supposed to determine TEMP_KEY and PERM_KEY?
©tenable
```

## Slide 58

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

###### **Public-key-decrypted nonce**

## Slide 59

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

###### **Public-key-decrypted nonce**

**Random string of 31 printable characters**

## Slide 60

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

###### **Public-key-decrypted nonce**

**Random string of 31 printable characters**

## Slide 61

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

**Public-key-decrypted nonce** **`+TEMP`** **_or_** **`+PERM` Random string of 31 printable characters**

## Slide 62

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

MD 5

**Public-key-decrypted nonce** **`+TEMP`** **_or_** **`+PERM`**

**Random string of 31 printable characters**

## Slide 63

###### **How is the client supposed to determine TEMP_KEY and PERM_KEY?**

MD 5

Public-key-decrypted nonce
Random string of 31 printable characters

**`+TEMP`** **_or_** **`+PERM`**

- **We are expected to use the same private key we used to** **_encrypt_ the nonce to** **_decrypt_ the random secret that the server sends us in response.**

- **We can then compose the ephemeral key using the same formula that the server does.**

## Slide 64

###### **How is the client supposed to determine TEMP_KEY or PERM_KEY?**

MD 5

**Public-key-decrypted nonce** **`+TEMP`** **_or_** **`+PERM`**

Random string of 31 printable characters

**But we don’t** **_have_ the private RSA key!**

## Slide 65

###### **How is the client supposed to determine TEMP_KEY or PERM_KEY?**

MD 5

**Public-key-decrypted nonce** **`+TEMP`** **_or_** **`+PERM`**

**Random string of 31 printable characters**

**Maybe there’s another way…**

## Slide 66

###### **How is the client supposed to determine TEMP_KEY or PERM_KEY?**

MD 5

Public-key-decrypted nonce
Random string of 31 printable characters

**Public-key-decrypted nonce** **`+TEMP`**

**_or_** **`+PERM`**

**Let’s look a bit more closely at this part here**

## Slide 67

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6 |int set_ephemeral_keys (void)
7
8 i{
9 size t ;
10! char [512];
11) char [512];
12) uint [22];
13
14, memset( ,0,0x58);
15) sprintf ( »''%S+PERM" , &XORED_MSG_ 00414b80);
16) sprintf ( ,''%S+TEMP" , &XORED_MSG_@0414b80);
17} md5_init(md5);
18 = strlen( 3
19} md5_add(md5, ,
20 md5_digest(md5,&PERM_KEY);
21) + md5_init( );
22 = strlen(
23} md5_add(md5, 1
24 md5_digest( ,SlEMP_KEY);
25, return Q;
26\}
3
```

## Slide 68

_Concatenating things like this would make sense if_ XORED_MSG_00414b80 _was NECESSARILY a null-terminated string!_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6 |int set_ephemeral_keys (void)
7
8 i{
)
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26}
size_t
char
char
uint
[512];
[512];
[22];
memset ( ,9,0x58);
sprintf (
sprintf (
md5_init(md5);
= strlen(
md5_add(md5,
md5_digest (
md5_init( );
= strlen(
'
,&PERM_KEY);
md5_add(md5,
md5_digest (
return 0;
!
,&TEMP_KEY);
Concatenating things like this would
make sense if
XORED_MSG_00414b8@ was
NECESSARILY a null-terminated
string!
-
4
,''%S+PERM" , &ORED_MSG_@0414b80);
,'%S+TEMP", &XORED_ MSG 00414b8Q);
);
3
```

## Slide 69

_Concatenating things like this would make sense if_ XORED_MSG_00414b80 _was NECESSARILY a null-terminated string!_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gt set_ephemeral_keys (void)
. yy Concatenating things like this would
make sense if
H XORED_MSG_00414b88@ was
[512]; NECESSARILY a null-terminated
[512]; string!
-
,, 0x58); v
,'"%S+PERM" , &XORED_MSG_00414b80);
,"%S+TEMP" , &XORED_MSG_00414b80);
strlen( );
;
'
,&PERM_KEY);
```

## Slide 70

_If we had a way to make the first byte of_ XORED_MSG_00414b80 _zero, then we could easily predict the ephemeral passwords._

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
6 |int set_ephemeral_keys (void)
7
8 i{
)
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26}
size_t
char
char
uint
[512];
[512];
[22];
memset ( ,9,0x58);
sprintf (
sprintf (
md5_init(md5);
= strlen(
md5_add(md5,
md5_digest (
md5_init( );
= strlen(
'
,&PERM_KEY);
md5_add(md5,
md5_digest (
return 0;
!
,&TEMP_KEY);
If we had a way to make the first
byte of XORED_MSG_80414b80
zero, then we could easily predict the
ephemeral passwords.
,''%S+PERM" , &ORED_MSG_@0414b80);
,'%S+TEMP", &XORED_ MSG 00414b8Q);
);
3
```

## Slide 71

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int rsa_public_decrypt_nonce(void)
{
RSA *
BIGNUM
int n;
uint
size_t
BIGNUM * (3];
= RSA_new();
[0] = BN_new();
= BN_new();
BN_set_word(a,0x10001)
BN_hex2bn( ,
"E541A631680C453DF31591A6E29382BC5EAC969DCFDBBCEA64CB49CBE36578845C507BF5E7A6BCD724AFA70
63CA754826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B38845 1D38F 3C6650C
DB4590C1208B91F688D0393241898C1F05A6D500C7066298C6BA2EF310F6DB2E7AF52829E9F858691"
i;
H
= [0];
memset (&DECRYPTED_NONCE, @, x20);
= RSA_size(rsa);
= RSA_public_decrypt(n,&ENCRYPTED_NONCE, &DECRYPTED_NONCE, rsa,3)}
if ( < 0x101) {
= strlen(&DECRYPTED_NONCE) ;
< 0x101 * 1);
```

## Slide 72

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
int rsa_public_decrypt_nonce(void)
{
RSA *rsa;
BIGNUM +a;
int n;
uint
size_t
BIGNUM * [3];
= RSA_new();
[0] = BN_new();
= BN_new();
BN_set_word(a,0x10001);
BN_hex2bn( ,
"E541A631680C453DF31591A6E29382BC5EAC969DCFDBBCEA64CB49CBE36578845C507BF5E7A6BCD724AFA70
63CA754826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B38845 1D38F 3C6650C
DB4590C1208B91F688D0393241898C1F05A6D500C7066298C6BA2EF310F6DB2E7AF52829E9F858691"
i;
—>e = a;
n= [0];
memset (&DECRYPTED_NONCE, 0, x20);
= RSA_size(rsa);
= RSA_public_decrypt(n,&ENCRYPTED_NONCE, &DECRYPTED_NONCE,
if ( < 0x101) {
= strlen(&DECRYPTED_NONCE) ;
< @x101 * 1);
> openssl-1.0.2 master) grep -r "# *define *RSA_NO_PADDING"
./crypto/rsa/rsa.h:# define RSA_NO_PADDING 3
> openssl1-1.0.2 master |
tenapie
```

## Slide 73

_We don’t actually need the corresponding private RSA key to have SOME control over what an UNPADDED application of_ RSA_public_decrypt() _does to our input!_

## Slide 74

_We don’t actually need the corresponding private RSA key to have SOME control over what an UNPADDED application of_ RSA_public_decrypt() _does to our input!_

_If we just want to control the first byte of the plaintext, trial and error is good enough._

## Slide 75

**So long as we don’t need to worry about the padding scheme, there’s nothing to stop us from applying this function to entirely phony “ciphertexts” and seeing what it produces.**

## Slide 76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Optimal Asymmetric Encryption
Mihir Bellare! and Phillip Rogaway?
1 Advanced Networking Laboratory, IBM T.J. Watson Research Center,
PO Box 704, Yorktown Heights, NY 10598, USA. e-mail: mihir@watson. ibm.com
2 Department of Computer Science, University of California at Davis,
Davis, CA 95616, USA. e-mail: rogaway@cs.ucdavis.edu
Abstract. Given an arbitrary k-bit to k-bit trapdoor permutation f
and a hash function, we-exhibit an encryption scheme for which (i) any
string z of length slightly less than k bits can be encrypted as f(rz),
where rz is a simple probabilistic encoding of z depending on the hash
function; and (ii) the scheme can be proven semantically secure assuming
the hash function is “ideal.” Moreover, a slightly enhanced scheme is
shown to have the property that the adversary can create ciphertexts
only of strings for which she “knows” the corresponding plaintexts—
such a scheme is not only semantically secure but also non-malleable
and secure against chosen-ciphertext attack.
```

## Slide 77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Optimal Asymmetric Encryption
Mihir Bellare! and Phillip Rogaway?
1 Advanced Networking Laboratory, IBM T.J. Watson Research Center,
PO Box 704, Yorktown Heights, NY 10598, USA. e-mail: mihir@watson. ibm.com
2 Nenartment of Comnuter Science. Tniversity of Califarnia at Davis
1.2 The plaintext aware scheme
A variety of goals for encryption have come to be known which are actually
stronger than the notion of [11]. These include non-malleability [7] and chosen
ciphertext security. We introduce a new notion of an encryption scheme being
plaintext-aware—roughly said, it should be impossible for a party to produce a
valid ciphertext without “knowing” the corresponding plaintext (see Section 3
for a precise definition). In the ideal-hash model that we assume, this notion can
be shown to imply non-malleability and chosen-ciphertext security.
and secure against chosen-ciphertext attack.
```

## Slide 78

**The main takeaway for us here is that** **_unpadded_ RSA encryption is** **_not_ “plaintext aware.”**

**It** **_is_ possible for us to produce a valid ciphertext without “knowing” the corresponding plaintext.**

## Slide 79

- **So, if we can produce phony but “valid” ciphertext, knowing only the public key, what exactly do we want to do with that?**

- **It seems that the telnetd_startup service places very few constraints on what the corresponding plaintext should be.**

- **Little more than a string length check, which I think is redundant anyway. (It can’t be more than 256 characters long – but the key itself is only 1024 bits,**

## Slide 80

_Remember that the random secret only contains printable characters._

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 Void generate_random_plaintext (void)
5
6 {
long
char *
int i;
Remember that the random secret only
contains printable characters.
= random();
if (false) {
trap(7);
= G&RANDOMLY_GENERATED_PLAINTEXT_at_4149b@ +
i += 1;
* = @x5d + Qx21;
} while (i != 0x1f);
END_OF_PLAINTEXT = @Q;
return;
```

## Slide 81

_Remember that the random secret is then XORed with the “decrypted” nonce, which we control._

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 oid xor_decrypted_nonce_with_plaintext (void)
5
6
byte ; Remember that the random secret is
byte ; then XORed with the “decrypted”
int nonce, which we control.
byte
+= 1;
*
} while (
return;
©tenable
```

## Slide 82

_Remember that the random secret is then XORed with the “decrypted” nonce, which we control._

_So, if we randomly generate a nonce that “decrypts” to an array of bytes that BEGINS with a printable character, then we have a 1-in-94 chance of causing an XOR collision that makes_ XORED_MSG_00414b80 _begin with a null byte!_

## Slide 83

_Remember that the random secret is then XORed with the “decrypted” nonce, which we control._

_So, if we randomly generate a nonce that “decrypts” to an array of bytes that BEGINS with a printable character, then we have a 1-in-94 chance of causing an XOR collision that makes_ XORED_MSG_00414b80 _begin with a null byte!_

_As far as the_ %s _format string is concerned, that would make_ XORED_MSG_00414b80 _an EMPTY STRING!_

## Slide 84

_DEMO TIME_

## Slide 85

#### **Are other models and firmware versions affected?**

## Slide 86

#### **Are other models and firmware versions affected?**

**To find out, I ordered Phicomm’s newest consumer router from Amazon, the K3C, and while I waited for it to arrive, I painstakingly scoured Chinese language router hacking forums for as many leaked firmware blobs as I could find.**

**I identified three different variations of the backdoor protocol.**

## Slide 87

### **Reconstructing the History of Phicomm’s Backdoor Protocol**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARCH
mipsel
arm
mips
mips.
mipsel
mips
mips
mipsel
mips
mips
mipsel
Reconstructing the History of
Phicomm’s Backdoor Protocol
FIRMWARE BUILD DATE MARKET
22.5.9.163
21.5.37.246
32.1.15.93
32.1.22,113
20.4.1.7
32.1.76.175
33.1,.25.177
2?.6.506.28
32.1.45.267
32.1.46.268
22.6.3.20
2017-02-15
2017-05-24
2017-06-17
2017-07-24
2017-08-09
2017-09-19
2017-09-21
2017-12-04
2018-01-26
2018-01-31
2018-05-07
Chinese
Chinese
Chinese
Chinese
Chinese
Chinese
International
Chinese
Chinese
Chinese
Chinese
telnetd_startup shalsum DEVICE IDENTIFIER
Oc3abid9al33b5acd4eabl1. none
040703661103 ac36bfad7f none
aes446fcare443acga7184 none
be189e091aisbiz49bed9c<e none
2d76lafSa2cObO7328793c none
bel89e091aisbiz49bed9c<e none
bel89e091lafebiz49bed9ce none
5/d9ae0ec01/ibd21374f72 none
2000b7as0aatb6b442tdett KIC _INTELALL VER_3.0
2000b7as80aasb6b442tdsit KSC _INTELALL VER_3.0
6ff3c24241pScSsa5eclegc K2 | COSTDOWN | VER_3.0
©tenable
```

## Slide 88

**Reconstructing the History of Phicomm’s Backdoor Protocol**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reconstructing the History of
Phicomm’s Backdoor Protocol
PUBLIC KEY PRIVATE KEY LEAKED PLAINTEXT CONTROL XOR SECRET SALTS TESTED
CC232B9BB0 SFC8FFBF53A yes yes no PERP, TEMP virtual
CC232B9BB0 9FC8FFBF53A no yes yes PERM, TEMP virtual
CC232B9BB0 SFCB8FFBF53A yes yes no PERP, TEMP virtual
CC232B9BB0 9FCB8FFBF53A no yes yes PERM, TEMP virtual
CC232B9BB0 SFC8FFBFS3A no yes yes PERM, TEMP virtual
CC232B9BB0 9FC8FFBF53A no yes yes PERM, TEMP virtual
CC232B9BB0 SFC8FFBFS3A, no yes yes PERM, TEMP hardware
CC232B9BB0 9FCBFFBF53A no yes yes PERM, TEMP virtual
E/FFDIA1BB unknown no yes yes PERM, TEMP virtual
E7FFD1IA1BE unknown no yes yes PERM, TEMP virtual
E541463168C unknown no yes yes PERM, TEMP hardware
Otenable
```

## Slide 89

# **Backdoor Protocol: Version 1**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Backdoor Protocol:
Version 1
©tenable
```

## Slide 90

**As found on the Phicomm K2 router with firmware version 22.5.9.163 (built in February, 2017).**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
As found on the Phicomm K2 router with firmware version 22.5.9.163 (built in February, 2017).
PHICOMM High Performance K2 100M WIFI 5 Wireless Router 1FE Wan 4FE LAN 5GA
C WIFI Router Dual Band 2.4G &5.8G English Firmware
C$25.71
Store Discount: Get C$1.37 off orders over C$27.35 v
Quantity:
1 SP
Ships to © Canada
Shipping: C$32.22
From China to Canada via AliExpress Standard Shipping
Estimated delivery on Jul 04 More options v
75-Day Buyer Protection
Money back guarantee
```

## Slide 91

**Here, the ephemeral keys are just the MD5 hashes of the decrypted nonce provided by the client, concatenated (in the same insecure way) with the special salts.**

**(With one variation: “PERM” is spelled “PERP” in this build.) No random plaintext is used, no XOR operation is performed. This is easy to exploit with a null byte injection even if you** **_don’t_ have the private key…**

## Slide 92

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—_——
Produce a random 32-byte message called NONCE, and encrypt it with
the (leaked) PRIVATE KEY used for all Phicomm routers prior to 2018.
Store the result as ENCRYPTED_NONCE.
Send ENCRYPTED_NONCE to Server
The Client is now expected to append one of two
suffixes to NONCE:
Decrypt ENCRYPTED_NONCE with RSA_public_decrypt()
and store result as DECRYPTED_NONCE
Create two ephemeral passwords by calling
sprintf(RAW_TEMP_KEY, "%s+TEMP", DECRYPTED_NONCE), and
sprintf(RAW_PERM_KEY, "%s+PERP", DECRYPTED_NONCE), [sic]
respectively.
(Note the format string.)
Compute the MD5 hashes of RAW_TEMP_KEY and RAW_PERM_KEY
and store the 16-byte results as TEMP_KEY and PERM_KEY,
respectively .
+ __|
```

## Slide 93

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Client is now expected to append one of two
suffixes to NONCE:
-"+TEMP", to launch a telnetd session that will
last until the router is rebooted, or
- "+PERP" [sic], to write a flag to a physical volume,
which the telnetd_startup daemon will check for
when the system is rebooted, and launch telnetd
if it finds it.
Store the result in RAW_KEY.
Compute the MD5 hash of RAW_KEY, and store
the result in BACKDOOR_KEY.
Send BACKDOOR_KEY to Server
If BACKDOOR_KEY matches TEMP_KEY then
call system("telnetd -! /bin/login.sh"),
launching an unencrypted telnetd shell
as root. No credentials are required to
log into this shell.
If BACKDOOR_KEY matches PERM_KEY then
call system("iwpriv ra0 e2p 26=7010"),
writing the bytes [HEX: 7010] to EEPROM,
at offset 0x26 (virtual address 0x40026). This
code will instruct the telnetd_startup daemon
to launch telnetd -I /bin/login.sh on boot.
```

## Slide 94

**The most obvious flaw in the oldest version of the backdoor that I was able to find is that** **_Phicomm baked the private RSA key into the_** **`telnetd_startup`** **_binary!_**

**This was a completely unforced error. The binary doesn’t even** **_use_ the private key.**

**Here’s the Ghidra decompilation for rsa_public_decrypt_nonce() in the telnetd_startup that shipped with the Phicomm K2, fw version 22.5.9.163.**

## Slide 95

**The most obvious flaw in the oldest version of the backdoor that I was able to find is that** **_Phicomm baked the private RSA key into the_** **`telnetd_startup`** **_binary!_**

**This was a completely unforced error. The binary doesn’t even** **_use_ the private key.**

**Here’s the Ghidra decompilation for rsa_public_decrypt_nonce() in the telnetd_startup that shipped with the Phicomm K2, fw version 22.5.9.163.**

## Slide 96

**The most obvious flaw in the oldest version of the backdoor that I was able to find is that** **_Phicomm baked the private RSA key into the_** **`telnetd_startup`** **_binary!_ This was a completely unforced error. The binary doesn’t even** **_use_ the private key.**

**Here’s the Ghidra decompilation for rsa_public_decrypt_nonce() in the telnetd_startup that shipped with the Phicomm K2, fw version 22.5.9.163.**

## Slide 97

###### **Tools for Exploiting this Version of the Backdoor Exist in the Wild**

**Hackers were quick to notice this mistake, and a tool for gaining an unauthenticated root shell appears widely on Chinese language router forums.**

## Slide 98

**I spun up a Windows VM, launched RoutAckPro, and sniffed.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| spun up a Windows VM, launched RoutAckPro, and sniffed.
Source: 192.168.2.147
Destination: 192.168.2.1
~ User Datagram Protocol, Sre Port: 21211, Dst Port
Source Port: 21211
Destination Port: 21210
Length: 136
Checksum: 0x51a7 [unverified]
[Checksum Status: Unverified]
[Stream index: 1231]
~ [Timestamps]
[Time since first frame: 4941.497322000 seconds]
[Time since previous frame: 2.052111000 seconds]
~ Data (128 bytes)
Data: 049d62f7d1505c068a264d098f3f4dde0017aed785c8Fa79...
[Length: 128]
& Chinesey — Englishy *
“ove to give bit
from the rsh to the boating
Pi to Yingbin *
the answer
bb 57
a7
db
ES] (|) e
Instant Scan Import
©tenable
```

## Slide 99

# **Backdoor Protocol: Version 2**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Backdoor Protocol:
Version 2
©tenable
```

## Slide 100

**I bought an international release of the Phicomm K3C router off Amazon, to see if it had a similarly vulnerable backdoor.**

**This one is running firmware version 33.1.25.177**

## Slide 101

**Honestly, this brand new K3C International edition, running 33.1.25.77, was my first clue that there are indeed variations in the backdoor protocol from one Phicomm device to another. The tool that worked so well on the (half-assedly rebranded) K2G, seen earlier, would not work on this device without modifications.**

## Slide 102

**The Phicomm K3C did indeed have a service listening on UDP port 21210, but instead of responding to “ABCDEF1234” with a device-identifying MD5 hash, it would respond to** **_any_ message with 128 bytes of highentropy data.**

**I needed to get inside the device to take a closer look.**

## Slide 103

###### **I wanted to access the filesystem, and ideally get a shell.**

**The web interface didn’t share the K3G A1’s command injection vulnerability… but I did find a UART port.**

## Slide 104

###### **I wanted to access the filesystem, and ideally get a shell.**

**The web interface didn’t share the K3G A1’s command injection vulnerability… but I did find a UART port.**

## Slide 105

**Don’t worry, I opened a window.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Don’t worry, | opened a window.
—— —
m@ ©tenable
```

## Slide 106

**I set up my UART-to-USB bridge and got to work.**

## Slide 107

**Interrupting the boot process gave me unauthenticated access to a UBOOT shell, from which I could dump the NAND storage.**

## Slide 108

**I found and modified a TCL expect script by someone named Valerio, and used it to hexdump the NAND while I got some rest. Most of the NAND dump appeared to contain very high-entropy data, likely encrypted or compressed. But there were a few valuable bits of information in the clear…**

## Slide 109

###### **A /etc/passwd file, for example!**

**…from which hashcat could easily recover the root password for the device.**

**I rebooted the device and logged in as root, over UART.**

## Slide 110

**Imagine my delight (mild disappointment) when I loaded this device’s telnetd_startup into Ghidra, and saw that it hadn’t even been stripped!**

**The state machine looks almost exactly like what we saw in the K2G A1, but without the ABCDEF → DEVICE_ID exchange.**

## Slide 111

**Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service.**

## Slide 112

**Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service.**

**Let’s be lazy here, and call on the reverser’s favourite tool:** strings **.**

## Slide 113

**Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service.**

**Let’s be lazy here, and call on the reverser’s favourite tool:** strings **.**

## Slide 114

**Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service.**

**Let’s be lazy here, and call on the reverser’s favourite tool:** strings **.**

_Does this look familiar?_

## Slide 115

**Here’s rsa_public_decrypt_nonce() from the k2.22.5.9.163Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service. Let’s be lazy here, and call on the reverser’s favourite tool:** strings **.** _Does this look familiar?_

## Slide 116

**Here’s rsa_public_decrypt_nonce() from the k2.22.5.9.163Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service.**

**Let’s be lazy here, and call on the reverser’s favourite tool:** strings **.** _Does this look familiar?_

## Slide 117

**Here’s rsa_public_decrypt_nonce() from the k2.22.5.9.163Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service. Let’s be lazy here, and call on the reverser’s favourite tool:** strings **. It’s the same public key that they used for the K2.22.9.163!** _Does this look familiar?_ **They redacted the private key, but left the public key unchanged.**

## Slide 118

**Here’s rsa_public_decrypt_nonce() from the k2.22.5.9.163Ghidra will not automatically load the region of this big-endian MIPS binary where certain important data is stored, such as the hardcoded public RSA key used by the service. Let’s be lazy here, and call on the reverser’s favourite tool:** strings **. It’s the same public key that they used for the K2.22.9.163!** _Does this look familiar?_ **They redacted the private key, but left the public key unchanged.**

## Slide 119

**But it’s cool, we don’t actually** **_need_ the private key to pop this version of the Phicomm backdoor.**

**We can use the same trick we used for the K2G A1, and just skip the → ABCDEF DEVICE_ID exchange.** (Note to self: now is a good time to plug in the K3C.)

## Slide 120

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phicomm's Backdoor Protocol: Version 2 (2017 - 2018)
Client
Produce a random 32-byte message called NONCE, and encrypt it with
the (leaked) PRIVATE KEY used for all Phicomm routers prior to 2018.
Store the result as ENCRYPTED_NONCE.
Send ENCRYPTED_NONCE to Server
Server
Send 128-byte CHALLENGE_CIPHERTEXT to Client
Decrypt ENCRYPTED_NONCE with RSA_public_decrypt()
and store result as DECRYPTED_NONCE
Generate a string of 31 random, printable
characters (between ASCII codes 0x21 and Ox7e)
and store the result as SECRET_PLAINTEXT
Encrypt SECRET_PLAINTEXT with RSA_public_encrypt()
using the hardcoded, 1024-bit public RSA key, with the
RSA_NO_PADDING option set ("Textbook RSA").
Store the 128-byte result as CHALLENGE_CIPHERTEXT
XOR SECRET_PLAINTEXT with the first 31 bytes
of DECRYPTED_NONCE, and store the result in
MASKED_SECRET.
```

## Slide 121

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Decrypt the CHALLENGE_CIPHERTEXT with the correct
PRIVATE KEY and XOR the result with the unencrypted NONCE.
The Client now possesses the MASKED_SECRET.
Create two ephemeral passwords by calling
sprintf(RAW_TEMP_KEY, "%s+TEMP", MASKED_SECRET), and
sprintf(RAW_PERM_KEY, "%S+PERM", MASKED_SECRET),
respectively.
(Note the format string.)
Compute the MDS5 hashes of RAW_TEMP_KEY and RAW_PERM_KEY
and store the 16-byte results as TEMP_KEY and PERM_KEY,
respectively.
The Client is now expected to append one of two
suffixes to MASKED_SECRET:
-"+TEMP", to launch a telnetd session that will
last until the router is rebooted, or
- "+PERM", to write a flag to a physical volume,
which the telnetd_startup daemon will check for
when the system is rebooted, and launch telnetd
if it finds it.
Store the result in RAW_KEY.
Compute the MD5 hash of RAW_KEY, and store
the result in BACKDOOR_KEY.
```

## Slide 122

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
respectively.
The Client is now expected to append one of two
suffixes to MASKED_SECRET:
-"+TEMP", to launch a telnetd session that will
last until the router is rebooted, or
- "+PERM", to write a flag to a physical volume,
which the telnetd_startup daemon will check for
when me system is rebooted, and launch telnetd
if it finds it.
Store the result in RAW_KEY.
Compute the MDS5 hash of RAW_KEY, and store
the result in BACKDOOR_KEY.
Send BACKDOOR_KEY to Server
If BACKDOOR_KEY matches TEMP_KEY then
call system("telnetd -! /bin/login.sh"),
launching an unencrypted telnetd shell
as root. No credentials are required to
log into this shell.
If BACKDOOR_KEY matches PERM_KEY then
call system("iwpriv ra0 e2p 26=7010"),
writing the bytes [HEX: 7010] to EEPROM,
at offset 0x26 (virtual address 0x40026). This
code will instruct the telnetd_startup daemon
to launch telnetd -I /bin/login.sh on boot.
```

## Slide 123

_DEMO TIME Part Deux_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEMO TIME
Part Deux
= Otenable
```

## Slide 124

# **Backdoor Protocol: Version 3**

**(Back where we started.)**

## Slide 125

**This seems to be when it dawned on Phicomm that the internet is slow to forget a leaked private key, and that it was time to switch things up.**

**The third version of the protocol includes the ABCDEF1234 → DEVICE_ID exchange, and each device ID seems to have its** **_own_ pair of RSA keys. The public key is baked into the telnetd_startup binary, and the private key seems, in each case, to have been successfully kept as a secret, but is presumably used by officials (?) to gain a root shell on the router.**

## Slide 126

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
user1@shrine-of-the-demo-gods : ~/projects/backdoor-Lockpick/demo$ find . -path "*bin/telnetd_startup" -exec strings -f -t x -n 256 {} \;
-/fw/K3C.32.1.22.113/usr/bin/telnetd_startup: 4ab8 CC232B9BBQ6C49EA1BDDQDE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB9ZEB363990FAE43
569778B58FA170FB1EBF3D1E88B7F6BA3DC47E59CF5F3C3064F62E504A12C5240F B85BE 727316C10EFF23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F9
F445ED4ED@344AC2B1F6CC124D9ED309A519
-/fw/K2GA1.22.6.3.20/usr/bin/telnetd_startup: 4330 E541A631680C453DF31591AGE29382BCSEACI69DCFDBBCEA64CB49CBE36578845C507BF5E7A6BCD724A
FA7063CA754826E8D13DBA18A2359EB54B5BE3368158824EA316A495DDC3059C478B41ABF6B388451D38F3C6650CDB4590C1208B91F 688D0393241898C1FQ5A6D500C7066
298COBAZEF310F6DBZE 7AF52829E9F 858691
./fw/K2.22.5.9.163/usr/bin/telnetd_startup: 3ef@ CC232B9BBQ6C49EA1BDDODE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB9ZEB363990FAE4356
9778B58FA170FB1EBF3D1E88B7FOBA3DC47E59CF5F3C3064F62E504A12C5240F B85BE727316C10EFF23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F9F4
45ED4ED0344AC2B1F6CC124D9ED309A519
./fw/K2.22.5.9.163/usr/bin/telnetd_startup: 3ff4 OFC8FFBFS3AECF8461DEFB98D81486A5D2DEE341F377BA16FB1218FBAE23BB1F3766732F 8D382E15543FC
2980208D968E 7AE1AC4B48F53719F6D9964E583AQB791150B9C0C354143AE285567D8C042240CA8D7A6446E49CCAF575ACC63C5SBAC8CF5B6A7 7DEEQS80E50CZ2BFEB62C06
ACA49EQFD0831D1BBQCB72BC9B565313C9
./fw/K3C.33.1.25.177--international/usr/bin/telnetd_startup: 4ab8 CC232B9BBO6C49EA1BDD@DE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB
92EB363990FAE43569778B58FA170FB1EBF3D1E88B7F6BA3DC47ES9CF5F3C3064F62E504A12C5240F B85BE727316C10EF F23CB2DCE973376D0CB6158C72F6529A90127860
Q0D820443CA44F9F445ED4EDQ@344AC2B1F6CC124D9ED309A519
./fw/K2A7 .22.6.506.28/usr/bin/telnetd_startup: 4160 CC232B9BBO6C49EA1BDD@DE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB92EB363990FAE4
3569778B58FA170FB1EBF3D1E88B7F6BA3DC47ES59CF5F3C3064F62E504A12C5240FB85BE 727316C10EF F23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F
9F445ED4ED0344AC2B1F6CC124D9ED309A519
./fw/K3.21.5.27.246/usr/sbin/telnetd_startup: 3cf@ CC232B9BBQ6C49EA1BDDODE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB92EB363990FAE43
569778B58FA170FB1EBF3D1E88B7F6BA3DC47E59CF5F3C3064F62E504A12C5240FB85BE727316C10EFF23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F9
F445ED4ED0344AC2B1F6CC124D9ED309A519
./fw/K3C.32.1.45.267/usr/bin/telnetd_startup: 4d58 E7FFD1A1BB9834966763D1175CFBF1BA2DF53A004B6297 7ESB985DFFD6D43785ESBCAQ88A6417BAFO70
BCE199B043C24B03BCEB970D7E47EEBA7F59D2BE4764DD8F Q6DB8EQE2945C912F52CB31C56C8349B689198C4A@D88FDOZ29CCECDDFF9C1491FFB7893C11FAD69987DBA15FF
11C7F1D570963FA3825B6AE92815388B3E03
./fw/K3C.32.1.15.93/usr/bin/telnetd_startup: 44e8 CC232B9BBO6C49EA1BDDODE1EF9926872B3B16694AC67 7C8C581E1B4F59128912CBB92EB363990FAE435
_ 69778B58FA170FB1EBF3D1E88B7F6BA3DC47ES9CF5F3C3064F62E504A12C5240F B85BE727316C10EF F23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F9F
oo, 445ED4ED0344AC2B1F6CC124D9ED309A519
SSS 1 rurese.32.1.15.93/usr/bin/tetneta_ startup: 45ec 9FC8FFBFS3AECF8461DEFB98D81486A5D2DEE341F377BA16FB1218FBAE23BB1F3766732F8D382E15543F
se C2980208D968E 7AE1AC4B48F53719F6D9964E583AQB791150B9C0C354143AE285567D8C042240CA8D7A6446E49CCAF5 75ACCO3CS5SBAC8CFS5B6A7 7DEEQS8QE50C2BFEB62CO
2 6ACA49EQFD0831D1BBOCB72BC9B56531309
-/w/K3P..20.4.1.7/usr/bin/telnetd_startup: 4150 CC232B9BBQ6C49EA1BDDODE1EF9926872B3B16694AC677C8C581E1B4F59128912CBB9ZEB363990FAE43569
778B58FA170FB1EBF3D1E88B7FOBA3DC47ES9CF5F3C3064F 62E504A12C5240F B85BE727316C10EFF23CB2DCE973376D0CB6158C72F6529A9012786000D820443CA44F9F44
= 5ED4ED0344AC2B1F6CC124D9ED309A519
user1@shrine-of-the-demo-gods : ~/projects/backdoor-Lockpick/demo$ , ble
```

## Slide 127

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phicomm's Backdoor Protocol: Version 3 (2018 onward)
Client Server
Send the token "ABCDEF1234"
compute and return DEVICE_IDENTIFYING_HASH
Reply with DEVICE_IDENTIFYING_HASH
Produce a random 32-byte message called NONCE, and encrypt it with
the PRIVATE KEY for the device the DEVICE_IDENTIFYING_HASH
identifies. Store the result as ENCRYPTED_NONCE.
Send ENCRYPTED_NONCE to Server
Decrypt ENCRYPTED_NONCE with RSA_public_decrypt()
and store result as DECRYPTED_NONCE
Generate a string of 31 random, printable
characters (between ASCII codes 0x21 and Ox7e)
and store the result as SECRET_PLAINTEXT
Encrypt SECRET_PLAINTEXT with RSA_public_encrypt()
using the hardcoded, 1024-bit public RSA key, with the
RSA_NO_PADDING option set ("Textbook RSA").
```

## Slide 128

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Send 128-byte CHALLENGE_CIPHERTEXT to Client
Decrypt the CHALLENGE_CIPHERTEXT with the correct
PRIVATE KEY and XOR the result with the unencrypted NONCE.
The Client now possesses the MASKED_SECRET.
Generate a string of 31 random, printable
characters (between ASCII codes 0x21 and Ox7e)
and store the result as SECRET_PLAINTEXT
Encrypt SECRET_PLAINTEXT with RSA_public_encrypt()
using the hardcoded, 1024-bit public RSA key, with the
RSA_NO_PADDING option set ("Textbook RSA").
Store the 128-byte result as CHALLENGE_CIPHERTEXT
XOR SECRET_PLAINTEXT with the first 31 bytes
of DECRYPTED_NONCE, and store the result in
MASKED_SECRET.
+]
Create two ephemeral passwords by calling
sprintf(RAW_TEMP_KEY, "%s+TEMP", MASKED _SECRET), and
sprintf(RAW_PERM_KEY, "%s+PERM", MASKED_SECRET),
respectively.
(Note the format string.)
Compute the MD5 hashes of RAW_TEMP_KEY and RAW_PERM_KEY
and store the 16-byte results as TEMP_KEY and PERM_KEY,
```

## Slide 129

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
and store the 16-byte results as TEMP_KEY and PERM_KEY,
respectively.
+]
The Client is now expected to append one of two
suffixes to MASKED_SECRET:
-"+TEMP", to launch a telnetd session that will
last until the router is rebooted, or
- "+PERM", to write a flag to a physical volume,
which the telnetd_startup daemon will check for
when the system is rebooted, and launch telnetd
if it finds it.
Store the result in RAW_KEY.
Compute the MD5 hash of RAW_KEY, and store
the result in BACKDOOR_KEY.
Send BACKDOOR_KEY to Server
If BACKDOOR_KEY matches TEMP_KEY then
call system("telnetd -! /bin/login.sh"),
launching an unencrypted telnetd shell
as root. No credentials are required to
log into this shell.
If BACKDOOR_KEY matches PERM_KEY then
call system("iwpriv ra0 e2p 26=7010"),
writing the bytes [HEX: 7010] to EEPROM,
at offset 0x26 (virtual address 0x40026). This
code will instruct the telnetd_startup daemon
to launch telnetd -I /bin/login.sh on boot.
```

## Slide 130

**The Responsible Disclosure Process**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Responsible Disclosure Process
Peg
PHICOMM
(OUR PCRTAL TO THE SMART
SSS Grane
```

## Slide 131

**I set out to find someone at Phicomm with whom I could discuss these vulnerabilities, and inform them of Tenable’s 90-day coordinated disclosure protocol.**

**Generally speaking, we notify the vendor that we’ve found a 0-day, and tell them that** **_if they respond_ , we will disclose in 90 days time, or as soon as we learn that the vulnerability has been patched.**

**We also tell them that we will disclose in 45 days time if we receive no reply.**

## Slide 132

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Olivia Fraser <bughunters@tenable.com> Tue, Oct 5, 2021, 2:10 PM * a
to service, support.usa, bcc: Vulnerability
Hello,
A researcher at Tenable has discovered several critical vulnerabilities on the Phicomm K2G router, and we are seeking a security contact at Phicomm with whom we
may further discuss the matter.
We've internally assigned this issue the tracking number of TRA-384.
Thank you for your time.
postmaster@freecomm-networks.com © Tue, Oct 5, 2021, 6:32PM
tome v
*** CAUTION: This email was sent from an EXTERNAL source. Think before clicking links or opening attachments. ***
FLA PBA B28 fe AS BE SER:
Ei: seeking security contact to discuss vulnerabilities in Phicomm K2G (tracking number: TRA-384)
ARSC ABE. HMR (SE.
ARS BSI PRK 1K 19 AY 53 DHAKA S MSL AE. ANIA, RAMRIABA,
```

## Slide 133

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Olivia Fraser <bughunter:
to service, support.usa, bec:
Hello,
Aresearcher at Tenable ha
may further discuss the mz
We've internally assigned t
Thank you for your time.
postmaster@freecomn
tome v
*** CAUTION: This ema
a
TeaLA Fue A Bee P88
SEM: seeking security cont
PARSER. EMRE
ARS BS7EIZ PH 1 K 19 Jy
Chinese (Simplified) x
English
Delivery of message to the following recipient or
group has been delayed:
support.usa@phicomm.com Subject: seeking
security contact to discuss vulnerabilities in
Phicomm K2G (tracking number: TRA-384) This
message has not been delivered. Will keep trying
to deliver. The server will continue to attempt to
deliver this message for the next 1 day, 19 hours,
and 53 minutes. If delivery is still not possible by
then, a notification will be sent to you
Translate Full Page
Google Translate
at Phicomm with whom we
```

## Slide 134

**I tried to reach out over other channels, but the situation did not look promising.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| tried to reach out over other channels, but the situation did not look promising.
©tenable
```

## Slide 135

**I tried to reach out over other channels, but the situation did not look promising.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| tried to reach out over other channels, but the situation did not look promising.
| am falling | am fading
@phicomm
| have lost it all
©tenable
```

## Slide 136

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Otenable
seeking security contact to discuss vulnerabilities in Phicomm K2G (tracking number: TRA-384)
Service <service@phicomm.eu>
Reply-To: bughunters@tenable.com
To: Olivia Fraser <bughunters@tenable.com>, "support.usa@phicomm.com" <support.usa@phicomm.com>
*** CAUTION: This email was sent from an EXTERNAL source. Think before clicking links or opening attachments. ***
Dear Sir,
Thank you for contacting Phicomm Support in Germany. Phicomm has closed all Business worldwide since 01.01.2019.
Yours sincerely
Service Team Phicomm
S444: Olivia Fraser
AGAMA: Dienstag, 5. Oktober 2021 20:10
IKEA: service@phicomm.eu; support.usa@phicomm.com
Ei: seeking security contact to discuss vulnerabilities in Phicomm K2G(tracking number: TRA-384)
[Quoted text hidden]
Otenable
```

## Slide 137

##### **So, what happened?**

- **2008: Gu Guoping founds Shanghai Feixun, which will later be known as “Shanghai Phicomm”**

- **2012: Lianbi Financial founded by ????**

- ● **2014: Phicomm declares operating income of 10 billion yuan (about $1.5 billion USD), dubbed “Little Huawei” in the Chinese press.**

- ● **2014: Phicomm initiates merger with Huiqiu Technology (formerly Beisheng Pharmaceutical)**

- ● **2015: Guoping gains control of Lianbi Financial** ● **2015: Phicomm launches “0-yuan purchase plan”**

- **2016: Huiqiu discloses that Guoping had gained control of the company. Guoping’s affiliate Xianyan receives largest fine in history from China Securities Regulatory Commision (about $500 million USD)**

● **2016: Guoping claims to have lost financial control of Phicomm**

## Slide 138

##### **The “0-yuan Purchase Plan”**

Essentially, the deal was that you could apply for a full rebate on the purchase of Phicomm routers and IoT devices if you register for the Lianbi Financial and Huaxia Wanija Financial Peer-to-Peer lending Apps.

## Slide 139

**Further Reading…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Further Reading...
Crime, Law and Social Change (2023) 79:369-393
https://doi.org/10.1007/s10611-022-10053-y
Crime and crisis in China's P2P online lending market:
a comparative analysis of fraud
Li Huang'® - Henry N. Pontell?
Accepted: 17 August 2022 / Published online: 15 September 2022
©The Author(s) 2022
The Lianbi e-commerce trick
Lianbi Finance (Lianbi) was among the “Big Four” P2P lending platforms in the
second wave of the crash, all of which ended with closings and criminal investiga-
tions. The Lianbi fraud involved collected funds of $12.7 billion, costing 1.1 million
investors about $2 billion (Zhu, 2021b). Aside from its size, this case gained major
attention due to its association with China’s e-commerce giant JD.com, a publicly
traded company on Nasdaq. Lianbi took advantage of consumer finance and online
shopping in order to advance a tech start-up venture. After the fraud was uncovered,
investors gathered at JD.com’s headquarter demanding a return of their money.
The central figure in the scheme was Guoping Gu (Gu), the controller of
Phicomm, a leading tech company dealing in telecommunications equipment. Its
flagship product, routers, became the key item in Lianbi’s financial conspiracy. In
2016, Phicomm and Lianbi launched a “O RMB Purchase” promotion on different
e-commerce platforms (Beijing News, 2018). Customers who participated paid $61
for the most basic Phicomm router. When they received the product it included a “K
code”, along with instructions directing them to the Lianbi app and website where
they could enter the code in order to obtain a $61 credit in their accounts.
By accepting the promotion consumers became entrapped in a conspiracy
designed to lure them into investing more money for supposed high returns, purchas-
ing additional financial products sold by Lianbi, or purportedly saving more by buy-
ing other refund-eligible products. Lianbi was able to attract large numbers of victims
within a relatively short period of time due to Phicomm’s collaboration with JD.com
in the promotion. During JD.com’s 2018 online shopping festival, Phicomm had
record-high sales of 722,000 electronic products (Beijing News, 2018). The day after
the festival, however, investors found that they were unable to access their accounts
on Lianbi. In response to investor complaints, the Shanghai Songjiang Public Secu-
rity Bureau immediately began an investigation. Gu and Lianbi’s legal representative
both fled the country, but were apprehended and returned to China shortly thereafter.
```

## Slide 140

● **2018-06: Lianbi Financial filed on suspicion of “illegally absorbing public deposits” (i.e. running a Ponzi scheme) – Gu Guoping is arrested.**

● **2021-02-04: Shanghai No. 1 Intermediate People’s Court holds public hearing for fraud case against Guoping** ● **2021-06-23: Songjian Police arrest Lianbi personnel**

## Slide 141

```
“On the morning of December 8, the Shanghai No. 1
Intermediate People’s Court publicly sentenced the
defendants Gu Guoping, Nong Jin, Chen Yu, Zhu Jun,
Wang Jingjing, and Zhang Jimin on the case of
fundraising fraud. Gu Guoping was sentenced to life
imprisonment for the crime of fundraising fraud,
deprived of political rights for life, and
confiscated of all personal property.”
```

## Slide 142

**To make a long story short, we should not expect patches.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
To make along story short, we
should not expect patches.
©tenable
```

## Slide 143

##### **Security Advisories**

● **CVE-2022-25213: Improper access control for UART shell**

- **CVE-2022-25214: Improper access control on LocalClientList.asp**

- **CVE-2022-25215: Improper access control on LocalMACConfig.asp**

- **CVE-2022-25218: Unpadded RSA lets attacker control plaintext**

● **CVE-2022-25219: Null byte interaction error in password generator**

**See Tenable research advisory TRA-2022-01 for details.**

## Slide 144

# **Thank You!**

###### **Olivia Lucca Fraser**

**Staff Research Engineer on Tenable’s Zero Day Research Team github.com/oblivia-simplex**

## Companion resources

### `Olivia Lucca Fraser_A Backdoor Lockpick.txt`

```text
https://github.com/oblivia-simplex/backdoor-locksmith
```
