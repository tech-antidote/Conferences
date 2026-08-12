---
title: "Double Tap at the Blackbox Hacking a Car Remotely Twice with MiTM"
speakers: ["Yingjie Cao", "Xinfeng Chen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Yingjie Cao & Xinfeng Chen_Double Tap at the Blackbox Hacking a Car Remotely Twice with MiTM.pdf"
pages: 50
sha256: "2d11aba85331d5d5f7846919657487117c8208d04428379b1de72583a92c850b"
text_chars: 17129
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:08:57Z"
---
# Double Tap at the Blackbox Hacking a Car Remotely Twice with MiTM

**Speakers:** Yingjie Cao, Xinfeng Chen  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Yingjie Cao & Xinfeng Chen_Double Tap at the Blackbox Hacking a Car Remotely Twice with MiTM.pdf` (50 pages)

## Slide 1

### Double Tap at the Blackbox Hacking a Car Remotely Twice with MiTM

Yingjie Cao

Xinfeng Chen

360 Vulnerability Research Institute

SIG Void Technology

#BHAS @BlackHatEvents

## Slide 2

###### # Yingjie Cao (@YinJai_c)

- Security researcher @ 360 Vulnerability Research Institute

- Specialized in connected vehicle security

- A full-chain exploiter of Blackberry QNX system, the most popular automotive OS

- His work has been accepted by both industry and academia, including IEEE S&P and Blackhat Asia

###### # Xinfeng Chen

- Security researcher @ SIG Void Technology

- Specialized in mobile security

- Skilled at customizing AOSP to bypass application protections

#BHAS  @BlackHatEvents

## Slide 3

PART

01

# **The Prologue**

#BHAS  @BlackHatEvents

## Slide 4

##### Three years ago…

There were two security events in Chengdu,

Tianfu Cup, the biggest vulnerability competition in China

An automotive cybersecurity standard conference about GB44495

#BHAS  @BlackHatEvents

## Slide 5

##### 15 days before Tianfu Cup 2021 registration

- We were told there is an automotive track

- We need to pick a top 10 brand in China

- Finally, we chose a brand with over 90,000 units sold in 2021

- 15 days left, with zero knowledge to the target

- - NO hardware, NO car

- We need to find extremely easy approaches to exploit it

#BHAS  @BlackHatEvents

## Slide 6

PART

02

# **The Car Hacking Landscape**

#BHAS  @BlackHatEvents

## Slide 7

##### Challenges of Hacking a Car

Synaktiv triple-killed Tesla @Pwn2Own Till today, few researchers can follow their work due to the extremely high technical bar.

#BHAS  @BlackHatEvents

## Slide 8

##### Saving researchers' wallet

Guangzhou, China

The biggest second-hand car components market in China, maybe globally largest. You can find almost every category of car parts here

Pros:

- Much affordable than purchasing a car

- - You can disassemble the chips, dumping firmware

Cons:

- It still costs you $100-$2000 to buy an IVI

- -  No guarantee to boot up it

- The sources of component vary, development version, production version, 4S sales version.

#BHAS  @BlackHatEvents

## Slide 9

##### Saving researchers' wallet

Pros:

- Much affordable than directly purchasing a

- car

   - Flexible pick-up and return

- Cons:

- Do NOT disassemble it if you do not have

- confidence to put it back. - Hardware / software version cannot be

- assured

#BHAS  @BlackHatEvents

## Slide 10

PART

03

# **First Blood**

#BHAS  @BlackHatEvents

## Slide 11

##### MiTM leads to get shell

Updating with
HTTP

- Hijacking the update traffic

- - Changing the APK to a remote shell APP

- Then we have access to all applications

- But only with a low privilege app (10001)

#BHAS  @BlackHatEvents

## Slide 12

##### Reverse Engineering the Applications

**“Factory” ?? Which program invokes it? BtPhone**

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekchat AN >
ASIA 2025 ig
private boolean c str
int length = str. length i
Log.d("BtPhoneMainActivity", "input =" + str +", len
if (length > 4 & str. startsWith("4i") && str.endsWith("#*"
Bundle bundle = new " Bundle ;
bundle. putString(’ ng_msg", str);
ntry.class).get(IIpcService.class) ).sendData(1001, bundle, indowUtil.CAR_DEVTOOLS) ;
“+ str);
return false;
Which program invokes it?
BtPhone
#BHAS @BlackHatEvents
```

## Slide 13

##### Factory Mode

- The '#' and '*' in the strings hints us to trigger these functions with  pressing on the phone call numbers

- The input should

   - length > 4

   - starts with *#

   - ends with #*

#BHAS  @BlackHatEvents

## Slide 14

##### Factory Mode

- *#9925*111#*

Factory mode Factory user version test

- Check  OS version & Hardware version & Unique ID

   - We can trigger this directly on the screen

Testing 4G, USB storage, camera, becon, etc

OS, MCU, hardware, version number, unique ID Version number of  each app Device Unique ID MCU version number

OLED testing mode Exihibition Mode

Aftersale mode

Some Ester Eggs

#BHAS  @BlackHatEvents

## Slide 15

##### Factory Mode

- *#9387*141#*

Factory mode Factory user version test

- System settings

- Directly input it, nothing happened

??

Testing 4G, USB storage, camera, beacon, etc

- Authentication required ??

OS, MCU, hardware, version number, unique ID Version number of  each app Device Unique ID MCU version number

OLED testing mode Exihibition Mode

Aftersales mode

Some Ester Eggs

#BHAS  @BlackHatEvents

## Slide 16

##### Factory Mode

Factory mode Factory user version test

Turning on Factory mode with a **key What is the key?**

Version number of  each app Device Unique ID MCU version number OLED testing mode Exihibition Mode Aftersale mode

Some Ester Eggs

#BHAS  @BlackHatEvents

## Slide 17

##### Factory Mode

The code invokes factory mode authentication

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Factory Mode
public void onReceiveData(IIpcService.IpcMessageEvent ipcMessageEvent) {
switch (c)
case 0:
if (msgID == 1001) {
String string = payloadData.getString(IpcConfig.IPCKey.STRING MSG) ;
if (!TextUtils.isEmpty(string)) {
c.b("SecurityCheckService", "onReceive----- > code = " + string);
if (this.f1165a.g(string)) {
c.b("SecurityCheckService", string + " isSecretKey.");
this.f1165a.a(string, getApplicationContext());
return;
} else if (com.car.devtools.a.c.c.a(string)) {
c.b("SecurityCheckService", string + " isFactoryCode.");
this.f1165a.b(string, getApplicationContext());
return;
} else {
return;
public boolean a(String str, String str2) {
this.b = b.b(str);
c.b("SecurityCheckPresenter", " verifySecretKey() mCateId:" + this.b);
int e = e(this.b);
c.b("SecurityCheckPresenter", String. format (MyApplication.a().getString(R.string.text_
return false;
}
return b.c(str2, str);
The code invokes factory mode authentication
public
static boolean c(String str, String str2) {
if (TextUtils.isEmpty(str2)) {
return false;
}
tring a2 = a(str, str2)}
com.
xiaopeng] lib.b.c.a("FactoryCodeModel", "Current Code " + str2 + "'s mSecretKey is: " + a2);
return str2.equals(a2); check input
}
public static Stying a(String str, String str2) {
{return b(str, b(str2)); ]
}
public static String b(String str, String str2p {
It (TextUtils.isemptp(str2)) 1
return "";
}
try {
1 = Integer.valueOf(str2).intValue();
}
cat¢h (Exception e) {
com.xiaopeng.lib.b.c.e("FactoryCodeModel", e.getMessage());
}yv
return a(str, i);
}
brivate static String a(String str, int i) k
char[] charArray = str.toCharArray();
int
for
}
String format = new DecimalFormat("00000000") . format (Math. abs(i2));
if (format.length() > 8) {
}
format = format.substring(0, 9);
return "*#0000*" + i + "*" + format + "#*";
}
#BHAS @BlackHatEvents
```

## Slide 18

##### Factory Mode

unique device ID

   - Simply doing addition and multiplication based on unique device ID

   - It is not a crypto implementation at all

   - In our case, the code is *#0000*10000*01344103#*

- *#9995*111#*

#BHAS  @BlackHatEvents

## Slide 19

##### The debugging interface

+ With ADB open + But a low privilege shell(2000) Console service (ADB) LPE HOW ?? Capturing log Capturing modem log Navigation log switch Clearing the log Reboot Copy ACC LCC to USB Copy Android and Modem Log to USB Copy Android Log to USB

#BHAS  @BlackHatEvents

## Slide 20

##### Android LPE for Remote Exploit Chain

**We don’t want to use any complicated exploit** CVE-2015-1805, pipe read and pipe write overrun

#BHAS  @BlackHatEvents

## Slide 21

##### CVE-2015-1805

#### pipe_read() -> pipe_iov_copy_to_user

```
staticintpipe_iov_copy_to_user(structiovec*iov, constvoid*from, unsignedlonglen, intatomic)
{
unsignedlong copy;
while (len >0) {      /* copy from pipe buffer */
while (!iov->iov_len)   /* the data will be copied to each iov[idx].iov_base */
      iov++;
    copy =min_t(unsignedlong, len, iov->iov_len); /* length to copy */
if (atomic) {    /* fast copy */
if (__copy_to_user_inatomic(iov->iov_base, from, copy))
return-EFAULT;
    } else {
if (copy_to_user(iov->iov_base, from, copy))
return-EFAULT;
    }
    from += copy;
    len -= copy;
iov->iov_base+= copy;
iov->iov_len-= copy;
  }
return0;
}
```

#BHAS  @BlackHatEvents

## Slide 22

##### CVE-2015-1805

#### pipe_read()

```
static ssize_t pipe_read(structkiocb *iocb, conststructiovec *_iov,
unsignedlongnr_segs, loff_tpos)
{
```

`/* ... */ for (;;) { if (bufs) {` **Check if all iov.base are writeable** `/* ... */ atomic = !iov_fault_in_pages_write(iov, chars); redo:`

```
        addr = ops->map(pipe, buf, atomic);
        error = pipe_iov_copy_to_user(iov, addr + buf->offset, chars, atomic);
        ops->unmap(pipe, buf, addr);
if (unlikely(error)) {    /* copy error*/
if (atomic) {    /* atomic copy error*/
atomic =0;
            goto redo;    /* try again without atomic*/
}
```

```
/* ... */
}
/* ... */
}
  }
```

```
}
```

```
if (atomic) {    /* fast copy */
```

```
if (__copy_to_user_inatomic(iov->iov_base, from, copy))
return-EFAULT;
    } else {
if (copy_to_user(iov->iov_base, from, copy))
return-EFAULT;
    }
```

```
staticintiov_fault_in_pages_write(structiovec*iov,
unsignedlonglen)
{
```

```
while (!iov->iov_len)
iov++;
while (len>0) {
unsignedlongthis_len;
this_len=min_t(unsignedlong, len, iov->iov_len);
if (fault_in_pages_writeable(iov->iov_base,
```

```
this_len))
```

```
break;
len-=this_len;
iov++;
  }
returnlen;
}
```

- If error, redo copy to iov

- iov[ **index** ] is changed, but chars are not

- An overflow

- Bypass the writeable check with **TOCTOU**

#BHAS  @BlackHatEvents

## Slide 23

##### The very ancient kernel

- Linux v3.15, affected by many vulnerabilities

- The bad news is, we do not have kernel offset to exploit these vulns.

- CVE-2015-1805

   - Pipe read and pipe write overrun

   - kernel offset needed (we cannot launch it because we do not have kernel access)

- Dirty Cow works!   -> Arbitrary file write

   - From Arbitrary Write to ROOT?

   - Filesystem is read-only, apps, binaries, and configurations can be modified just temporarily and will get back into what it was after reboot

#BHAS  @BlackHatEvents

## Slide 24

##### The LPE pivoting

We have a kernel arbitrary write

We don’t have a kernel offset to locate the write target

So we cannot ROOT it

We have a file arbitrary write

We cannot execute arbitrary file as we can only execute those put on the IVI screen

So we cannot ROOT it

#BHAS  @BlackHatEvents

## Slide 25

##### The LPE pivoting

We have a file arbitrary write

We cannot execute arbitrary file as we can only execute those on the IVI screen

So we cannot ROOT it

- A low-priv shell cannot execute/create/RW any high-priv file

- • We can only touch to execute programs

- • APPs running on low-priv

- • Default binary programs are executed at bootup, but RO filesystem

#BHAS  @BlackHatEvents

## Slide 26

##### The LPE pivoting

We **cannot** execute arbitrary file as we can only execute those on the IVI screen **?**

**HIDDEN FUNCTIONS in Factory Mode!!**

#BHAS  @BlackHatEvents

## Slide 27

##### The LPE pivoting

**Log is running with system privilege !!**

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat ~
ASIA 2025
The LPE pivoting
-—> Log is running with system privilege !!
#BHAS @BlackHatEvents
```

## Slide 28

##### The LPE pivoting

**Log is running with system privilege !!**

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat ~
ASIA 2025
The LPE pivoting
-—> Log is running with system privilege !!
#BHAS @BlackHatEvents
```

## Slide 29

##### The LPE pivoting

We have a kernel arbitrary write

So we cannot ROOT it

We have a file arbitrary write

We cannot execute arbitrary file as we can only execute those put on the IVI screen

So we cannot ROOT it

#BHAS  @BlackHatEvents

## Slide 30

##### The LPE pivoting

We have a kernel arbitrary write

We have a file arbitrary write

We cannot execute arbitrary file as we can only execute those put on the IVI screen

So we cannot ROOT it

#BHAS  @BlackHatEvents

## Slide 31

##### Remote Exploit Chain

#BHAS  @BlackHatEvents

## Slide 32

##### Car control

The program logic in BCM Manager

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat ;
ASIA 2025 aN
Car control
The program logic in BCM Manager
int _lockOff()
{
sp<IBinder> binder = defaultServiceManager()->checkService(String16("carbcmservice") );
Parcel data, reply;
int replyInt = 0;
status_t ret = Q;
data.writeInterfaceToken(String16("android.car.hardware.bcm.ICarBcm") );
ret = data.write((void *)lockOff, SIZE_24*sizeof(unsigned char));
if(ret != NO_ERROR)
perror("trans failed!!");
binder->transact(1, data, Greply, Q);
do {
replyInt = reply.readInt32();
} while (replyInt);
return 0;
lockOff [SIZE_24] = {0x01, 0x00, 0x0, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0, 0x00, 0x08, 0x99, 0x84, 0x80, 0x80,
#BHAS @BlackHatEvents
```

## Slide 33

##### Demo

#BHAS  @BlackHatEvents

## Slide 34

PART

04

# **Second Blood**

#BHAS  @BlackHatEvents

## Slide 35

Almost every connected mobile application uses HTTPS for communication. HTTPS connections are considered secure because they have the following three characteristics:

- **Confidentiality:** The TLS protocol encrypts data, meaning a man-in-the-middle cannot directly read the

- content.

- **Integrity:** Data cannot be tampered with during transmission without being detected.

- **Authentication:** Clients can verify the server’s identity to ensure they are connecting to a legitimate server.

However, is it truly immune to man-in-the-middle attacks?

#BHAS  @BlackHatEvents

## Slide 36

###### **SSL Certificate Validation**

- •Verify up to the root certificate.

- •Use public key to verify signatures.

- •Root certificate ensures trust.

#BHAS  @BlackHatEvents

## Slide 37

###### **Risks of Trust Stores**

- **CA Addition** :

   - User manual addition

   - MDM (Mobile Device Management) addition

   - Malicious software addition

- **Key Questions** :

   - Can you trust all these CAs?

   - Should your app rely on the default trust store?

- **Real-World Concerns** :

   - Known cases of CA breaches or issuing certificates to impostors.

- **Further Reading** :

   - Detailed timeline of CA failures: sslmate.com

#BHAS  @BlackHatEvents

## Slide 38

**Potential for man-in-the-middle attacks in Android applications.**

- •Use of Self-Signed Certificates

- •Trusting User-Installed Certificates

###### **Common Security Issues**

- **1.Custom X509TrustManager**

   - Fails to verify certificate trust in checkServerTrusted.

- **2.WebViewClient Override**

   - onReceivedSslError calls proceed, ignoring certificate errors.

- **3.Custom HostnameVerifier**

   - Lacks strict certificate validation in verify.

- **4.setHostnameVerifier Method**

   - Uses ALLOW_ALL_HOSTNAME_VERIFIER, trusting all hostnames.

#BHAS  @BlackHatEvents

## Slide 39

Now let's demonstrate an interesting case:

**_I just connected to WiFi—how did my car get stolen?_**

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lackhat “pe
mers LA ~
Now let's demonstrate an interesting case:
I just connected to WiFi—how did my car get stolen?
x509Certificates
1: Request mitmproxy
Client
Explicit
#BHAS @BlackHatEvents
```

## Slide 40

###### **_Then, we can use ARP spoofing on the same network as the victim and perform a manin-the-middle attack using mitmproxy._**

Note: 8883 is the MQTTS port, which is often overlooked.

#BHAS  @BlackHatEvents

## Slide 41

**You can see a lot of traffic from ports 443 and 8883. Save the traffic and import your certificate key into Wireshark to easily view the user credentials (User Name & Password) when connecting to MQTTS.**

#BHAS  @BlackHatEvents

## Slide 42

Through packet analysis, we found that car control commands are simple. The msg_id is a random message ID, and the target_id is the car's VIN.

###### **Key findings:**

- •service_type 12, msg_type 2, cmd_type 1, cmd_value 2 opens windows.

- •service_type 12, msg_type 2, cmd_type 2, cmd_value 1 opens the trunk.

By intercepting user credentials and connecting to the MQTT broker, we can control the vehicle.

#BHAS  @BlackHatEvents

## Slide 43

PART

05

# **Security Response**

#BHAS  @BlackHatEvents

## Slide 44

##### Factory Mode – AES Enhancement

- Using unique device ID and fixed bytes to generate hmac

```
hmac =
```

```
hmac.new(b'\x03U\x0f\xf7\xf7\x02`\x01Q\xd5hn\xb8\x
e4y6', HardwareID, hashlib.sha512)
```

- AES CTR encryption with hmac as key and iv, time to be encrypted

unique device ID

```
aes_iv= hmac[32:48]
aes_key= hmac[0:32]
a0 = ((current_time >> 12) & 0xFF)
    a1 = ((current_time >> 4) & 0xFF)
    a2 = ((current_time & 0xF) << 4) | (0x03 & 0xF)
aes_out = bytes([a0, a1, a2]
```

*#9995*111#*

*#0000*10000*01344103#*

#BHAS  @BlackHatEvents

## Slide 45

##### Timeline

#BHAS  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Timeline
2018 Sept, 2021 Early, 2022
2019 Vuln A Does Not Affect Oct, 2024
2021 Oct, 2024
#BHAS @BlackHatEvents
```

## Slide 46

PART

06

# **Future Work**

#BHAS  @BlackHatEvents

## Slide 47

###### Limitations

- We don’t have enough cars to evaluate the landscape of MiTM vulnerabilities, so we call for community to contribute

- Current procedures are still too complicated for those who only have very basic programming knowledge

#BHAS  @BlackHatEvents

## Slide 48

Open tool source for security community Find **MiTM** vulnerabilities on your own!! Feature list:

- Check APP certificate trust settings

- • Decrypt the traffic and generate PoC by replay

- Ethnical issue: • For self-check only, no attack purpose will be provided

Stay tuned:  sigvoid.com/news

#BHAS  @BlackHatEvents

## Slide 49

###### Special Acknowledgement

###### # Gorgias Li

- A dedicated, hardcore security researcher

- He contributed a lot to our project

#BHAS  @BlackHatEvents

## Slide 50

## Thank you ! Any Question?

Yingjiecao[at]protonmail.com Twitter: @YinJai_c

#BHAS  @BlackHatEvents
