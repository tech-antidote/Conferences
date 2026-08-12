---
title: "Stealthy Sensitive Information Collection from Android Apps"
speakers: ["Bai"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Bai-Stealthy-Sensitive-Information-Collection-from-Android-Apps.pdf"
pages: 36
sha256: "0d82a79c3499d4221279266e0bcae8d46194773a7d1bbd28c31deacaed092549"
text_chars: 11770
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.2
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T02:08:52Z"
---
# Stealthy Sensitive Information Collection from Android Apps

**Speakers:** Bai  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Bai-Stealthy-Sensitive-Information-Collection-from-Android-Apps.pdf` (36 pages)


## Slide 1

### Stealthy Sensitive Information Collection from Android Apps

Bai Guangdong@UQ, Zhang Qing@ByteDance, Xia Guangshuai@ ByteDance

#BHASIA @BlackHatEvents

## Slide 2

CONTENTS

01 About us
02 Background
03 Our work
04
Summary
05 Q&A

#BHASIA @BlackHatEvents

## Slide 3

# **01 About Us**

#BHASIA @BlackHatEvents

## Slide 4

**Bai Guangdong** Associate professor from UQ

**Zhang Qing**

Senior security and privacy expert (CIPT/CIPP/FIP) from ByteDance

**Xia Guangshuai**

Security researcher from ByteDance

#BHASIA @BlackHatEvents

## Slide 5

## PRIVACY

MUCH HAS BEEN TALKED, BUT NOT MUCH DONE

#BHASIA @BlackHatEvents

## Slide 6

# **02 Background**

#BHASIA @BlackHatEvents

## Slide 7

##### Data regulation is increasingly important

User data protection has gained **a great deal of attention** around the world. Many countries have put in place **legislation** to regulate the collection and use of personal data, such as the well-known European Union (EU) General Data Protection Regulation (GDPR).

Infringements of user privacy could result in **large penalties** , e.g., “a fine of up to €20 million, or 4% of the firm’s worldwide annual revenue” set by GDPR.

#BHASIA @BlackHatEvents

## Slide 8

#### Post-GDPR Era

#BHASIA @BlackHatEvents

Source: https://unctad.org/page/data-protection-and-privacy-legislation-worldwide

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
71% 5%
COUNTRIES WITH COUNTRIES WITH COUNTRIES WITH COUNTRIES WITH
LEGISLATION DRAFT LEGISLATION NO LEGISLATION NO DATA
Source: https://unctad.org/page/data-protection-and-privacy-legislation-worldwide
```

## Slide 9

##### Evolution of Android privacy data protection

|Android 6|Android 9|Android 10|Android 11|Android 12|Android 13|
|---|---|---|---|---|---|
|Runtime Permissions|Restricted access to
logs|MAC address randomization|Package visibility|Microphone and camera
indicators|Runtime permission
for notifications|
|Access Hardware
Identifier (e.g., Wi-
Fi/bluetooth MAC)
needs LOCATION
permission|Restricted access to
phone numbers|Restriction on non-resettable
device identifiers|Restrictions on
/sdcard/Android/data|Permission package
visibility|New runtime
permission for
nearby Wi-Fi devices|
||Restricted access to
Wi-Fi location and
connection
information|Restrictions on direct access to
configured Wi-Fi networks|Add
READ_PHONE_NUMB
ERS permission|Clipboard access
notifications|Use of body sensors
in the background
requires new
permission|
|||Some telephony, Bluetooth, Wi-
Fi APIs require FINE location
permission|Auto-reset
permissions from
unused apps|Add
BLUETOOTH_SCAN, BL
UETOOTH_ADVERTISE,
and BLUETOOTH_CONN
ECT permissions|Permission required
for advertising
ID(GAID)|
|||Add
ACCESS_BACKGROUND_LOCATI
ON permission||Support restricting apps
from obtaining
advertising ID (GAID)||
|||Protection of USB device serial
number||||

#BHASIA @BlackHatEvents

## Slide 10

##### Android 6: Runtime permissions

Runtime permissions have been added since Android 6, and runtime permissions are required to obtain sensitive information such as device unique identifiers and location information, and use services such as Camera.

#BHASIA @BlackHatEvents

## Slide 11

##### Android 10: Device unique identifier restriction

Starting from Android 10, Google restricts the acquisition of **device unique identifiers** , and apps can no longer obtain device unique identifiers such as **IMEI/SN/IMSI/ICCID** .

#BHASIA @BlackHatEvents

## Slide 12

#### Android 12: GAID restriction

Starting from Android 12, for **GAID** ( **Google advertising ID** ), users can prohibit the App from obtaining GAID through the limit tracking settings.

#BHASIA @BlackHatEvents

## Slide 13

#### iOS Identifier for Advertisers (IDFA)

BTW, for iOS, starting from iOS 14.5, if the app wants to obtain **IDFA** (equivalent to Android GAID), it must be **manually authorized by the user** .

#BHASIA @BlackHatEvents

## Slide 14

#### Research questions

Are these measures adequate to protect user privacy? **Manually authorizing** to obtain IDFA since iOS 14 has caused disputes, but, **is it a storm in a teacup** ?

#BHASIA @BlackHatEvents

## Slide 15

#### Research questions

Are these measures adequate to protect user privacy? **Manually authorizing** to obtain IDFA since iOS 14 has caused disputes, but, **is it a storm in a teacup** ?

#BHASIA @BlackHatEvents

## Slide 16

# **03 Our work**

#BHASIA @BlackHatEvents

## Slide 17

###### **The Dangers of Unrestricted Access to Privacy Information Using Webview**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
The Dangers of Unrestricted Access to Privacy Information Using Webview
Hi, do you want to be rich?
miss Just open this website: www.
exampletest.com
Thanks! 9")
```

## Slide 18

###### **The Dangers of Unrestricted Access to Privacy Information Using Webview**

**webView** .setWebChromeClient( **chromeClient** );

#BHASIA @BlackHatEvents

## Slide 19

###### **The Dangers of Unrestricted Access to Privacy Information Using Webview**

webSettings.setDatabaseEnabled(true); String dir = this.getApplicationContext().getDir("database", Context.MODE_PRIVATE).getPath(); webSettings.setGeolocationEnabled(true);

webSettings.setGeolocationDatabasePath(dir);

@Override

public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) { callback.invoke(origin, true, false);

super.onGeolocationPermissionsShowPrompt(origin, callback); }

#BHASIA @BlackHatEvents

## Slide 20

**The Dangers of Unrestricted Access to Privacy Information Using Webview**

Searching for _onGeolocationPermissionsShowPrompt_ and _onPermissionRequest_ function in github limit on .java or .kt file.

We got 1127 result back (Limited to Github search ability), and among them, 639 are positive cases.

#BHASIA @BlackHatEvents

## Slide 21

###### **The Dangers of Unrestricted Access to Privacy Information Using Webview**

https://github.com/react-native-webview/react-native-webview/issues/2903

#BHASIA @BlackHatEvents

## Slide 22

###### **Complex and confusing AD id**

- Most users and even developers don't know the existence of AD ids.

- Hard to set even for domain experts, due to the complex UIs

- GAID is designed to be resettable, but resetting it is not much meaningful, as it is still there and can be used to track users during a particular period of time, for example, **cross-tracking the user in two apps is still possible**

- OAID is an AD id on Android OEM devices in China. Apps can get two AD ids in serval models of Android devices, i.e., GAID and OAID.

- Since OAID is not a feature in AOSP, there are more ways to bypass auditing on many Android phones to get OAID.

#BHASIA @BlackHatEvents

## Slide 23

###### **Our findings on these two advertising IDs**

OAID GAID
restriction tracing is  user authorization  restriction tracing is  user authorization
brand OAID settings GAID exists GAID settings
allowed required  allowed required
- - -
A  Yes-8 Yes  No No
- - -
B Yes-3 Yes No No
C  Yes-5 Yes No Yes Yes-3 Yes No
D Yes-4 Yes（but not work） No Yes Yes-5 Yes No
E  Yes-4 Yes（but not work） No Yes Yes-5 Yes No
F  Yes-4 Yes（but not work） No Yes Yes No UI No
G Yes-4 Yes Yes Yes Yes-5 Yes（but not work） No
H  Yes-5 Yes  No Yes No No UI No

###### Advertising IDs have actually become permanent or long-lasting!

#BHASIA @BlackHatEvents

## Slide 24

###### **Ways to Get Sensitive Data**

Official channels provided by 01 AOSP

02 Java reflection

03 Call in native code

04 Call directly through Binder

05 Call via vulnerabilities

06 Hidden channels

#BHASIA @BlackHatEvents

## Slide 25

###### **Ways to Get Sensitive Data**

- Official channels provided by AOSP:

Most are implemented through various Manager APIs

Eg:  TelephonyManager.getImei/getDeviceId…

- Java reflection：

In this way static scanning can be bypassed

eg: **telephonyMgr.getClass().getMethod("getImei", int.class).invoke(telephonyMgr, slotId);**

#BHASIA @BlackHatEvents

## Slide 26

###### **Ways to Get Sensitive Data**

- Call in native code:

difficult to analyze

eg : **jmethodID getDeviceId = ((*env)->GetMethodID(env, TelephoneManager_Cls, "getDeviceId", "()Ljava/lang/String;"));**

**jobject imei= (*env)->CallObjectMethod(env, telephonymanager, getDeviceId);**

- Call directly through Binder：

difficult to analyze

eg: **IBinder mRemote = (IBinder) Class.forName("android.os.ServiceManager").getMethod("getService", String.class).invoke(null, "phone");**

**mRemote.transact(144, _data, _reply, 0)**

**String imei = _reply.readString();**

#BHASIA @BlackHatEvents

## Slide 27

###### **Ways to Get Sensitive Data**

- Call via vulnerabilities:

Many OEM manufacturers add their own APIs. This may be error-prone.

Those APIs may be vulnerable, leading to exploitable vulnerabilities.

Such vulnerabilities are challenging to detect, as they are specific to the particular OEM.

Eg: CVE-2021-25344

#BHASIA @BlackHatEvents

## Slide 28

###### **Ways to Get Sensitive Data**

- Hiden channels:

- ①  Get CPU SN:

/sys/devices/soc0/serial_number

- ② Get IMSI/ICCID/Phone Number (A-201311522, won’t fix): **target sdk <30** & without any permission getContentResolver().query(”content://telephony/siminfo/”, null, null, null, null);

Google believes that all apps have an sdk version higher than 30, but this is not the case in third-party app stores!

#BHASIA @BlackHatEvents

## Slide 29

###### **Hook String constructor**

Hook native String constructor to

detect sensitive data

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
Hook String constructor
st envAddr = ptr(Java.vm.tryGetEnv().handle) ;
artSymbol = envPointAddr = envAddr.readPointer
rea an onst envPointAddr167 = envPointAddr.add((167) * Process.pointerSize);
Hook native String constructor to ‘ a» : om ynst newStringUtfAddr = envPointAddri167.readPointer (
_ onEnter(args) {
detect sensitive data Int} 3
onLeave(retval) {
if (retval == @x@) {
return;
et ret = Java.vm.getEnv().getStringUtfChars(retval, \null).readCString();
isSensitiveInfoInString(ret,"jni::newStringUtf")
st envPointAddr163 = envPointAddr.add((163) * Proceés.pointerSize) ;
f ((elconst newStringAddr = envPointAddr163.readPointer (
Int Interceptor.attach(newStringAddr, {
onEnter(args) {
onLeave(retval) {
if (retval == 0x0) {
return;
let ret = Java.vm.getEnv().getStringUtfChars(retval, null).readCString(
```

## Slide 30

###### **Hook String constructor**

Advantage：

- No need to pay attention to the way the app calls sensitive data.

- Even if 0-day or n-day is used, it can be detected

Disadvantages：

- A large number of Strings are hooked, and the app runs stuck

#BHASIA @BlackHatEvents

## Slide 31

###### **Hook String**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
Hook String
Welcome to your new Pixel
© Tap for tips
```

## Slide 32

###### **Hook String constructor - results**

Starting from Android 10, third-party apps are no longer allowed to obtain the **unique identifier of the device** .

#BHASIA @BlackHatEvents

## Slide 33

###### **Hook String constructor - results**

brand Android version CVE UUID with perms
Google Android 10 CVE-2021-0428 ICCID READ_PHONE_STATE
Samsung Android 11 CVE-2021-25344 SN without any perms
Samsung Android 11 CVE-2021-25358  IMSI without any perms
Samsung Android 11 CVE-2021-25515 BSSID without any perms
Samsung Android 12 CVE-2022-22272 IMSI READ_PHONE_STATE
Xiaomi Android 11 CVE-2020-14105  SNO without any perms

#BHASIA @BlackHatEvents

## Slide 34

# **04 Summary**

#BHASIA @BlackHatEvents

## Slide 35

###### **Summary & Key take-ways**

- **System-level protection** : Starting from Android 10, third-party apps cannot obtain the unique identifier of the device. If this happens in an app, the app must have exploited some vulnerabilities (0-day or n-day).

- **App-level protection** : If the app's webview does not handle permissions properly, it will also be used by any URL to obtain user data.

- **The disaster of fragmentation** : Some OEMs do not strictly follow the AOSP permission policy, and many custom APIs can be used to obtain the unique identifier of the device.

- **New challenges** : The AD id becomes a persistent id to some extent. Users can be tracked continuously from the first power on until the phone is restored to factory Settings.

#BHASIA @BlackHatEvents

## Slide 36

# **05 Q&A**

twitter@cnwatcher

#BHASIA @BlackHatEvents
