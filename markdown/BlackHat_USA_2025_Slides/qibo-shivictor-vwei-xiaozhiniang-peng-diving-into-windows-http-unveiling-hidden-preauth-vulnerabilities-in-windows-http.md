---
title: "Diving into Windows HTTP Unveiling Hidden Preauth Vulnerabilities in Windows HTTP Services"
speakers: ["Qibo Shi", "Victor V", "Wei Xiao", "Zhiniang Peng"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Qibo Shi&Victor V&Wei Xiao&Zhiniang Peng_Diving into Windows HTTP Unveiling Hidden Preauth Vulnerabilities in Windows HTTP Services.pdf"
pages: 75
sha256: "034dda586bca33cfd0adab332266792781e6fb34ec45fafb8e8e1f5695a66a5a"
text_chars: 38885
ocr_pages: 24
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:59:50Z"
---
# Diving into Windows HTTP Unveiling Hidden Preauth Vulnerabilities in Windows HTTP Services

**Speakers:** Qibo Shi, Victor V, Wei Xiao, Zhiniang Peng  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Qibo Shi&Victor V&Wei Xiao&Zhiniang Peng_Diving into Windows HTTP Unveiling Hidden Preauth Vulnerabilities in Windows HTTP Services.pdf` (75 pages)

## Slide 1

## Diving into Windows HTTP: Unveiling Hidden Preauth Vulnerabilities in Windows HTTP Services

Qibo Shi(k0shl), VictorV, Wei Xiao, Zhiniang Peng

#BHUSA @BlackHatEvents

## Slide 2

### About us

Qibo Shi(k0shl) | Senior Security Researcher of Cyber Kunlun Lab VictorV | Senior Security Researcher of Cyber Kunlun Lab Wei Xiao | Senior Security Researcher of Cyber Kunlun Lab Zhiniang Peng | Associate Professor of Huazhong University of Science and Technology

#BHUSA @BlackHatEvents

## Slide 3

### Agenda

I. Background

II. Overview of the Windows HTTP Service Framework III. Exploring Logic Flaws Leading to Pre-auth DoS IV. Parsing and Handling Stages Leading to Pre-auth RCE V. Conclusion

#BHUSA @BlackHatEvents

## Slide 4

## Background

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Background
```

## Slide 5

### Why HTTP Services?

✓ Most of them are unauthenticated.

- ✓ No user interaction required.

- ✓ No additional configuration needed.

- ✓ Few researchers have focused on it before.

- ✓ Many Windows Services rely on the Windows HTTP APIs (httpapi.dll).

#BHUSA @BlackHatEvents

## Slide 6

### Overview of HTTP Services in Windows

- HttpCreateServerSession https://learn.microsoft.com/en-us/windows/win32/api/http/nf-http-httpcreateserversession

Initializes a new HTTP Server API session.

This is the starting point for configuring a server-side HTTP stack.

- HttpAddUrl/HttpAddUrlToUrlGroup https://learn.microsoft.com/en-us/windows/win32/api/http/nf-http-httpaddurl Registers a URL to listen on.

Binds a specific URL to the server session for handling incoming requests (e.g., http://+:80/example/).

#BHUSA @BlackHatEvents

## Slide 7

### How to find them

● HttpQueryServiceConfiguration

- A Windows API used to query configuration details managed by HTTP.sys.

- Can retrieve:

   - Registered URLs

   - SSL certificate bindings

   - IP listeners

   - Request queue names

   - Service SID bindings

- Allows inspection of system-wide HTTP configuration from user-mode.

#BHUSA @BlackHatEvents

## Slide 8

### How to find them

###### > netsh http show servicestate

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
BRIEFINGS
How to find them
> netsh http show servicestate
Request queues:
Request queue name: Request queue is unnamed.
Version: 1.86
State: Active
Request queue 503 verbosity Level: Basic
Max requests: 1600
Active requests: 6
Queued requests: @
Max queued request age: Os
Requests arrived: 8
Requests rejected: 6
Cache hits: @
Number of active processes attached: 1
Processes:
ID: 3569, image: C:\Windows\System32\svchost.exe
Services: WinRM
Tagged Service: WinRM
Registered URLs:
HTTP: //+:5985/WSMAN/
HTTP: //+:47001/WSMAN/
```

## Slide 9

## Overview of the Windows HTTP Service Framework

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Overview of the Windows HTTP
Service Framework
```

## Slide 10

##### User Mode

Kernel Mode

Web Application (IIS,non-IIS, etc.)

httpapi.dll HTTP.SYS
DeviceIoControl
[\Device\HTTP]
IoControlCode

Network I/O
(TCP/IP Stack)

#BHUSA @BlackHatEvents

## Slide 11

KDC
BITS Printer
.asp
ADFS
etc. IIS framework
IIS Framework
WinRM
etc.
HTTP Services

#BHUSA @BlackHatEvents

## Slide 12

Client
Server
POST
Receive  Parsing
Stage Stage Stage

Server
POST
Receive  Parsing  Response
Stage Stage Stage

HTTP/1.1 200 OK

#BHUSA @BlackHatEvents

## Slide 13

Client
Server
NTLM
POST Kerbros
Receive  Parsing  Response
Stage Stage Stage

HTTP/1.1 200 OK

#BHUSA @BlackHatEvents

## Slide 14

### HTTP Related APIs HttpReceiveHttpRequest

ULONG HttpReceiveHttpRequest( [in] HANDLE RequestQueueHandle, **[in] HTTP_REQUEST_ID RequestId, [in] ULONG Flags,** [out] PHTTP_REQUEST RequestBuffer, **[in] ULONG RequestBufferLength, [out, optional] PULONG BytesReturned,** [in, optional] LPOVERLAPPED Overlapped );

https://learn.microsoft.com/en-us/windows/win32/api/http/nf-http-httpreceivehttprequest

#BHUSA @BlackHatEvents

## Slide 15

### HTTP Related APIs HttpReceiveRequestEntityBody

ULONG HttpReceiveRequestEntityBody( [in] HANDLE RequestQueueHandle, **[in] HTTP_REQUEST_ID RequestId,** [in] ULONG Flags, [out] PVOID EntityBuffer, **[in] ULONG EntityBufferLength,** [out, optional] PULONG BytesReturned, [in, optional] LPOVERLAPPED Overlapped

);

https://learn.microsoft.com/en-us/windows/win32/api/http/nf-http-httpreceiverequestentitybody

#BHUSA @BlackHatEvents

## Slide 16

### HTTP Related APIs

Client

POST /example HTTP/1.1 HttpReceiveHttpRequest
\xDE\xAD\xBE\xEF HttpReceiveRequestEntityBody
handle data
HTTP/1.1 200 OK HttpSendHttpResponse
Connection reset by peer HttpCancelHttpRequest

Server

#BHUSA @BlackHatEvents

## Slide 17

## Exploring Logic Flaws Leading to Pre-auth DoS

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Exploring Logic Flaws Leading to
Pre-auth DoS
```

## Slide 18

### Tips:

**When hunting for pre-auth DoS bugs,** it's not only about memory corruption (e.g., null pointer dereference or out-of-bounds read without info leak) — that's just one class of DoS.

**What if the server can no longer process any normal requests at all?** That’s DoS too — and sometimes even more impactful.

Considering the framework of Windows HTTP services, I focused on the **receive stage** and the **response stage** , where such logic flaws are most likely to exist.

#BHUSA @BlackHatEvents

## Slide 19

### Receiving Stage

**Three Mechanisms:**

⚫ Synchronous

- ⚫ Asynchronous — WaitForMultipleObjects

⚫ Asynchronous — Callback

#BHUSA @BlackHatEvents

## Slide 20

### Synchronous

###### ⚫ Single-threaded

⚫ Service doesn’t invoke HttpReceiveHttpRequest until the current request handling finishes

void SyncHandleFunction() { […] while ( 1 ) { v7 = HttpReceiveHttpRequest(…); // receive http header […] // process http header/ POST data / … } […] return; }

#BHUSA @BlackHatEvents

## Slide 21

### Case Study – CVE-2024-43512

###### Windows Standards-based Storage Management Service

bool __fastcall concrete::HTTPListener::Run(HANDLE *this) // concrete.dll { [...] **LABEL_3:** while ( 1 ) { while ( 1 ) Never { memset_0(v3, 0, 0x1360ui64); update

memset_0(v3, 0, 0x1360ui64); BytesReturned = 0;

v6 = HttpReceiveHttpRequest(this[1], RequestId, 0, v5, **0x1360u** , &BytesReturned, 0i64); // ============> **[a]** if ( v6 == 0xEA ) // ===============> **[b]** {

RequestId = v5->RequestId;

v2 = (struct _HTTP_REQUEST_V2 *)realloc(v3, BytesReturned); // ===============> **[c]** v3 = v2; if ( !v2 ) return 0; goto LABEL_3; // =============> **[d]** } [...]

}

#BHUSA @BlackHatEvents

## Slide 22

### Case Study – CVE-2024-43512

##### **Before**

##### **After**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat : me
BRIEFINGS - \
Case Study — CVE-2024-43512
D:\>python request.py 192.168.217.2Uu
<?xml version="1.0" encoding="utf-8" ?>
<CIM CIMVERSION="2.0" DTDVERSION .O">
<MESSAGE ID="" PROTOCOLVERSION="1.0">
Befo re <SIMPLEEXPRSP>
<EXPMETHODRESPONSE NAME="ExportIndication">
<IRETURNVALUE>
</IRETURNVALUE>
</EXPMETHODRESPONSE>
</SIMPLEEXPRSP>
</MESSAGE>
</CIM>
D:\>python request.py 192.168.217.244
Traceback (most recent call last):
File "C:\Users\k@shl\AppData\Roaming\Python\Python310\site-packages\urlLib3\connectionpool.py", Line 791, in urlopen
response = self._make_request(
File "C:\Users\kO@shl\AppData\Roaming\Python\Python310\site-packages\urlLib3\connectionpool.py", Line 537, in _make_request
response = conn.getresponse()
File "C:\Users\k@shL\AppData\Roaming\Python\Python310\site-packages\urllib3\connection.py", line 461, in getresponse
f httplib_response = super().getresponse()
A ter File "C:\Program Files\Python310\lib\http\client.py", line 1374, in getresponse
response. begin()
File "C:\Program Files\Python310\Lib\http\client.py", Line 318, in begin
version, status, reason = self._read_status()
File "C:\Program Files\Python310\Llib\http\client.py", line 287, in _read_status
raise RemoteDisconnected("Remote end closed connection without"
http.client.RemoteDisconnected: Remote end closed connection without response
```

## Slide 23

#### Asynchronous — WaitForMultipleObjects

⚫ Single thread

⚫ Does not block inside HTTP API functions, but waits for a completion signal ⚫ Creates a separate thread to handle the request

void AsyncHandleObjectFunction() { […] while ( 1 ) {

- v7 = HttpReceiveHttpRequest(…);  // return 0x3E5, will not block […]

if ( WaitForMultipleObjectsEx(…) != 1 ) // wait for receive http header, set signal […]

if ( GetOverlappedResult() ) //  get return value and overlapped buffer

[…] // process http header/ POST data / … in separate thread

} […] return; }

#BHUSA @BlackHatEvents

## Slide 24

### Case Study -- CVE-2025-27471

__int64 __fastcall BaseHttpListener::DoReceiveRequestHeaders(BaseHttpListener *this) // upnphost.dll { NumberOfBytesTransferred = 0; // =====================> **[a]** [...]

**LastError** = (*(__int64 (__fastcall)())this+11) // HttpReceiveHttpRequest , ==========> **[b]** (

*((_QWORD *)this + 14), RequestId, 0i64, v2, v4, 0i64, // =================> [c] &Overlapped);

[...] **case 0xEAu** : // ==============> **[d]**

v4 = NumberOfBytesTransferred; // =============> **[e]** v4 will always remain at 0 if NumberOfBytesTransferred was not updated *((_DWORD *)this + 72) = 0; RequestId = v2->RequestId; free(v3);

v2 = (struct _HTTP_REQUEST_V2 *)malloc(v4);

[...]

if ( GetOverlappedResult(*((HANDLE *)this + 14), &Overlapped, & **NumberOfBytesTransferred** , 0) ) // ===============> **[f]** [...]

}

#BHUSA @BlackHatEvents

## Slide 25

### Case Study -- CVE-2025-27471

###### upnphost!BaseHttpListener::DoReceiveRequestHeaders+0x166 "r eax;g;"

return  0x3e5 or 0x0 as normal

Causes DoS by entering an infinite loop.

#BHUSA @BlackHatEvents

## Slide 26

### Case Study -- CVE-2025-27471

##### **Before**

##### **After**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat : me
BRIEFINGS - \
ig.
Case Study -- CVE-2025-27471
D:\>python upnp_normal.py 192.168.217.150
Content-Length: 31
Before Content-Type: text/html
Server: Microsoft—Windows/10.8 UPnP/1.0 UPnP-Device-Host/1.8 Microsoft—HTTPAPI/2.6
Date: Tue, 01 Jul 2025 05:29:40 GMT
D:\>python upnp_normal.py 192.168.217.150
Exception in thread Thread-1 (thr):
Traceback (most recent call last):
File "C:\Users\k@sh1\AppData\Roaming\Python\Python310\site—packages\urllib3\connectionpool.py", line 791, in urlopen
response = self._make_request(
File "C:\Users\kOsh1\AppData\Roaming\Python\Python310\site-packages\urllib3\connectionpool.py", line 537, in _make_request
response = conn.getresponse()
After File "C:\Users\kOshl\AppData\Roaming\Python\Python310\site-packages\urllib3\connection.py", Line 461, in getresponse
httplib_response = super().getresponse()
File "C:\Program Files\Python310\Lib\http\client.py", line 1374, in getresponse
response. begin()
File "C:\Program Files\Python310\Lib\http\client.py", line 318, in begin
version, status, reason = self._read_status()
File "C:\Program Files\Python310\Lib\http\client.py", line 279, in _read_status
line = str(self.fp.readline(_MAXLINE + 1), "“iso-8859-1")
File "C:\Program Files\Python310\Llib\socket.py", Line 705, in readinto
return self._sock.recv_into(b)
```

## Slide 27

### Asynchronous — Callback

⚫ The most popular mechanism in HTTP services. Examples: Kerberos Proxy, RDP, RDG, WinRM, ADFS, and even IIS

⚫ Uses a thread pool to create handler threads; each thread handles one request. Examples: CreateThreadpoolIo/StartThreadpoolIo/CancelThreadpoolIo

⚫ Registers callbacks to manage every interaction and event.

#BHUSA @BlackHatEvents

## Slide 28

### Asynchronous — Callback

void AsyncHandleIoCompletionRoutine()

###### **Common Callback Functions**

- HandleReceiveRequestIoCompletionCallback

- HandleReceiveEntityIoCompletionCallback

- HandleSendResponseIoCompletionCallback

- HandleCancelResponseIoCompletionCallback

{

[…]

switch ( *((_DWORD *)Overlapped + 8) ) // Depends on the set with each service {

case 1:

HttpReceiveRequestIoCompletion(IoResult, NumberOfBytesTransferred, Overlapped); break;

case 2:

HttpSendResponseIoCompletion(IoResult, NumberOfBytesTransferred, Overlapped); break;

###### **Optional Callbacks (Registered When Needed)**

- HandleWaitForDisconnectionIoCompletionCallback

- HttpReceiveClientCertIoCompletionCallback

case 3:

HttpSendPostResponseIoCompletion(IoResult, NumberOfBytesTransferred, Overlapped); break;

case 4:

HttpReceiveRequestEntityIoCompletion(IoResult, NumberOfBytesTransferred, Overlapped); break;

case 5:

HttpCancelRequestIoCompletion(IoResult, NumberOfBytesTransferred, Overlapped); break;[…]

return;

}

#BHUSA @BlackHatEvents

## Slide 29

### Tips:

- In **single-threaded scenarios** (both sync and async), after processing a request, the service calls HttpReceiveHttpRequest again to wait for the next one.

- In the **callback-based model** , the callback function must call StartThreadpoolIo and then invoke HttpReceiveHttpRequest to start a new thread from the IO thread pool for handling the next request.

###### **Think about this situation:**

If the callback returns **without** calling HttpReceiveHttpRequest, the current thread will exit. Eventually, if **all threads** in the IO thread pool exit this way, there will be **no handler threads left** , and the service will **never process normal requests again** .

#BHUSA @BlackHatEvents

## Slide 30

### Case Study — WSDApi.dll

__int64 __fastcall CWSDHttpListener::HandleRequest( // wsdapi.dll CWSDHttpListener *this, struct _HttpAsyncRequest *a2, __int64 a3, int a4) {

[...] ioresult = *((_DWORD *)a2 + 15); // =============> [a] if ( ioresult ) {

CWSDHttpListener::IoCompletionRoutine

CWSDHttpListener::HandleRequest

Transport = *((_DWORD *)a2 + 15); if ( ioresult > 0 )

Transport = (unsigned __int16)ioresult | 0x80070000; // ================> [b] // forget to call HttpReceiveHttpRequest, no http handler anymore

} else {

[...] Transport = CWSDHttpListener::IssueReceiveRequest(this, v20, v21, v22); // =============> [c] [...]

}

**return Transport; // =============> [d]** }

#BHUSA @BlackHatEvents

## Slide 31

### Case Study

##### **Before**

##### **After**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Case Study
Before After
D:\>python fdres.py 192.168.217.150
Traceback (most recent call last):
D : \>p ython fdres . PY 192 « 168 « 217 . 156 File "C:\Users\kOshL\AppData\Roaming\Python\Python310\site-packages\urllib3\connectionpool.py", Line 791, in urlopen
. a. response = self._make_request(
Content-Type = appLication/soap+xmL File "C:\Users\kOsh1l\AppData\Roaming\Python\Python310\site-packages\urllib3\connectionpool.py", line 537, in _make_request
. response = conn.getresponse()
Server: Microsoft—HTIPAPI/2 “ 3) File "C:\Users\k@sh1L\AppData\Roaming\Python\Python310\site—packages\urllib3\connection.py", Line 461, in getresponse
httplib_response = super().getresponse()
Date : Tue ' 61 Jul 2025 85 736 739 GMT File "c:\Program Files \python310\Lib\http\client. py", line 1374, in getresponse
response. begin()
Content-Length : 3) File "C:\Program Files\Python310\Lib\http\client.py", line 318, in begin
version, status, reason = self._read_status()
File "C:\Program Files\Python310\Lib\http\client.py", line 279, in _read_status
line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
File "C:\Program Files\Python310\lib\socket.py", Line 705, in readinto
return self._sock.recv_into(b)
```

## Slide 32

### Case Study – Low severity

MSRC acknowledged it as a pre-auth DoS, but rated it as low severity because the service is only exposed in trusted networks.

#BHUSA @BlackHatEvents

## Slide 33

### Receiving Stage

###### **Impact:**

- ⚫ Unauthenticated: No authentication or extra configuration required

- ⚫ Easy attack: Triggered by just one or a few malicious packets

- ⚫ Persistent DoS: Service permanently stops handling requests from legitimate clients, and it doesn’t require keep connections from attack client

###### **Secure Development Considerations:**

- ✓ Never exit the handler process early; always invoke HttpReceiveHttpRequest with RequestID = 0 to start listening for new requests

- ✓ Pay special attention to error returns, especially 0xEA and 0x4CD

- ✓ Carefully handle variables and states after error returns to avoid inconsistent behavior

#BHUSA @BlackHatEvents

## Slide 34

### Response stage HttpSendHttpResponse

- HTTPAPI_LINKAGE ULONG HttpSendHttpResponse( [in] HANDLE RequestQueueHandle,

   - **[in] HTTP_REQUEST_ID RequestId,**

   - [in] ULONG Flags,

   - [in] PHTTP_RESPONSE HttpResponse,

   - [in, optional] PHTTP_CACHE_POLICY CachePolicy,

   - [out] PULONG BytesSent,

   - [in] PVOID Reserved1,

   - [in] ULONG Reserved2,

   - [in] LPOVERLAPPED Overlapped,

[in, optional] PHTTP_LOG_DATA LogData

);

#BHUSA @BlackHatEvents

## Slide 35

### Response stage HttpCancelHttpRequest

HTTPAPI_LINKAGE ULONG HttpCancelHttpRequest( [in] HANDLE RequestQueueHandle, **[in] HTTP_REQUEST_ID RequestId,** [in, optional] LPOVERLAPPED Overlapped );

#BHUSA @BlackHatEvents

## Slide 36

### Response Stage Http.sys – Establishes HTTP Connections on the Server Side UxTlAllocateConnectionForLookaside

###### **Default Maximum Connections**

- •Default value: 0xFFFFFFFF (unlimited)

- •Can be configured via the registry:

- HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\HTTP\Parameters Registry value: MaxConnections

#BHUSA @BlackHatEvents

## Slide 37

### Response Stage

Http.sys – After Disconnection •Triggered by actions like HttpSendHttpResponse or HttpCancelHttpRequest UxTlFreeConnectionFromLookaside

#BHUSA @BlackHatEvents

## Slide 38

Response Stage So what happens if the server ends the handler without calling HttpSendHttpResponse or HttpCancelHttpRequest?

#BHUSA @BlackHatEvents

## Slide 39

### Response Stage

So what happens if the server ends the handler without calling HttpSendHttpResponse or HttpCancelHttpRequest?

###### **Connection Resource Leak**

- ✓ Connection reference count **never decreases**

- ✓ Connection-related structures **are never freed** from nonpaged pool

- ✓ Causes **nonpaged pool memory exhaustion** over time

#BHUSA @BlackHatEvents

## Slide 40

### Response Stage

###### BranchCache

◆ Refer to [MS-PCCRR](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-pccrr/6409c168-8a3a-473c-b333-6438f067ef56) ◆ Specific POST Data format

###### **MSG_GETBLKLIST**

#BHUSA @BlackHatEvents

## Slide 41

### Case Study -- CVE-2024-38149

BranchCach -- CTnoDownloadMgr::OnMessage

__int64 __fastcall CTnoDownloadMgr::OnMessage( char a1, unsigned int a2, unsigned int a3, void *a4, _QWORD *a5, __int64 a6, int a7, __int64 a8) { [...] switch ( a3 ) // ==============> **[a]** { case 1u: // ==============> **[b]** v19 = 1; if ( v20 != (TraceLoggingHProvider)&WPP_GLOBAL_Control && (*((_BYTE *)v20 + 108) & 8) != 0 && *((_BYTE *)v20 + 105) >= 4u ) {

**[a]** Variable a3 can be controlled via POST data **[b]** When a3 == 1, it represents MSG_NEGO_REQ **[c]** This can trigger exceptions in the service

•All POST message types have exception handlers, but malformed data can cause exceptions

- •After exception, service **does NOT** call HttpSendHttpResponse or HttpCancelHttpRequest to disconnect

- •If attacker **does NOT** disconnect either → nonpaged pool memory leaks

- •Leads to **kernel nonpaged pool exhaustion → denial of service**

WPP_SF_qqq(*((_QWORD *)v20 + 12), 49i64, &WPP_152a8e42b8b337334125d2feda130716_Traceguids, a4, *v14, v14[1]); goto LABEL_50; } break;

[...] CTnoDownloadMgr::LogInvalidMessage(a6 + 8, v19, 1002i64); SystemError::ThrowHelper(L"CTnoDownloadMgr::OnMessage", -2147024122); // ============> **[c]** [...] }

#BHUSA @BlackHatEvents

## Slide 42

### Case Study -- CVE-2024-38149

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifeschat
BRIEFINGS
SHH) GE) BRI) UM) RET) DH)
testtest
FE Administrator: Commend Pro.»
16.8.26190.17
= Performance &@ un new task
P
CPU
, Memory 4068
1e
z Memory
= Disk 0(¢: | —
= Ethernet
1.8GB(OMB) 2.2GB
1.7/5.4GB 15GB
124MB 77.3 MB
```

## Slide 43

### Response stage

**Impact:**

⚫ Unauthenticated: No authentication or additional configuration needed ⚫ Kernel Crash: Can cause system hang or Blue Screen of Death (BSoD) due to nonpaged pool memory exhaustion

###### **Secure Development Considerations:**

- ✓ Ensure every request handler always ends by sending a response back or canceling the request(or disconnection callback)

#BHUSA @BlackHatEvents

## Slide 44

### IIS

OCSP MCEP Printers BITS DHA
.asp etc. w3wp.exe
IIS svchost.exe
httpapi.dll

#BHUSA @BlackHatEvents

## Slide 45

### IIS

###### HttpExtensionProc

###### **DWORD WINAPI HttpExtensionProc( LPEXTENSION_CONTROL_BLOCK lpECB );**

###### **ISAPI Extensions in IIS**

- ✓ Every IIS web server uses ISAPI extensions to process requests

- ✓ Even .asp and C# applications rely on their respective ISAPI extensions

- ✓ For example, servers handling .aspx files use ISAPI extensions like aspnet_isapi.dll or webengine64.dll

- ✓ Although it looks like the web server is processing .aspx directly, the underlying processing is done through ISAPI extensions

#BHUSA @BlackHatEvents

## Slide 46

### IIS

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
lis
oy ISAPI and CGI Restrictions
Use this feature to specify the ISAPI and CGl extensions that can run on the Web server,
Group by: No Grouping ad
Description
Active Server Pages
ASP.NET v4.0,30319
ASP.NET v4.0,30319
BITS Server Extensions
Internet Printing
Online Certificate Status Protocol (OCSP) Add-On
Restriction
Allowed
Allowed
Allowed
Allowed
Allowed
Allowed
Path
CAWINDOWS\system32\inetsrv\asp.dll
CAWINDOWS\Microsoft.NET\Framework\v4.0,30319\aspnet_isapi.dll
CAWINDOWS\ Microsoft. NET\Framework64\4.0,30319\aspnet_isapidll
CAWINDOWS\system32\ bitssrv.dll
CAWINDOWS\system32\msw3 prt.dll
CAWINDOWS\system32\ocspisapi.dll
```

## Slide 47

### IIS

Client

http://+:80/OCSP

Server

IIS Framework
svchost.exe

appcmd set config "Default Web Site/" /section:system.webServer/handlers /+[name='handlerwa',path='*',verb='*',modules='IsapiModule',scriptProcessor='"C:\Windows\System32\ocspisapi.dll"',resourceType=' Unspecified',requireAccess='None',preCondition='classicMode']

w3wp.exe

#BHUSA @BlackHatEvents

## Slide 48

### IIS

###### **ISAPI_CONTEXT Lifecycle in IIS**

⚫ For each IIS service, IIS initializes an ISAPI_CONTEXT structure ⚫ For every incoming request:

→ IIS **increments** the reference count of ISAPI_CONTEXT → After request handling completes, IIS **decrements** the ref count

⚫ When the reference count reaches zero, the structure is released

isapi.dll!ProcessIsapiRequest → ISAPI_CONTEXT:: ISAPI_CONTEXT iiscore.dll!W3_CONTEXT::SetupStateMachine → Check ref count of ISAPI_CONTEXT

#BHUSA @BlackHatEvents

## Slide 49

### IIS

###### `iiscore.dll! W3_CONTEXT::SetupStateMachine`

if failed

Max ref count is 0x1366

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
lis
iiscore.d1ll! W3 CONTEXT: :SetupStateMachine
LABEL_41:
if ( (*(_intés (_fastcall **)(W3_CONTEXT *))(*(_QWORD *) + 232i64)) (this)
I] ¢ = _InterlockedExchangeAdd((volatile signed __int32 *)(*((_QWORD *)t + 1011) + 212164), lu),
42 = *((_QWORD *)this + @x3F3),
= +1,
*((_BYTE *)t + 8097) = 1,
"if ( 1(*(_intea (_fasteall **)(w3_co ))(*(_QWORD *)this + 232164))(this) )
= (void (_fastcal )(_inte4, _int64, __int64))(*((_QWORD *)this + 1009) + 656164);
45 = *(_DWORD *)(*(_QWORD *)(*((_QWORD *)this + 6) + 40164) + 36164);
:
Max ref count is 0x1366
if failed
++*(_DWORD
8;
23
goto LABEL_92;
e Unavailable";
)this + 8);
es
```

## Slide 50

### IIS

###### **Balancing ISAPI_CONTEXT Reference Count**

- ➢ After an ISAPI extension DLL handles data, IIS helps manage ISAPI_CONTEXT reference counts It provides a support function: ServerSupportFunction

- ➢ Certain operations in ServerSupportFunction invoke ISAPI_CONTEXT::DereferenceIsapiContext to decrement the reference count Example: SSFDoneWithSession triggers dereference

HttpExtensionProc

SupportServerFunction

SSFDoneWithSession

ISAPI_CONTEXT::DereferenceIsapiContext

#BHUSA @BlackHatEvents

## Slide 51

### IIS

###### **Responsibility of Handling ServerSupportFunction**

- ServerSupportFunction is **invoked by the ISAPI extension** via HttpExtensionProc

- • It is **not called by IIS**

- This means **each IIS-based service** (e.g., aspnet_isapi.dll, webengine.dll, or any custom extension)

   - → must handle it **explicitly and correctly**

#BHUSA @BlackHatEvents

## Slide 52

### IIS

###### **Responsibility of Handling ServerSupportFunction**

- ServerSupportFunction is **invoked by the ISAPI extension** via HttpExtensionProc

- • It is **not called by IIS**

- This means **each IIS-based service** (e.g., aspnet_isapi.dll, webengine.dll, or any custom extension)

   - → must handle it **explicitly and correctly**

**Incorrect handling of ServerSupportFunction can silently break the request lifecycle and lead to service-wide impact.**

#BHUSA @BlackHatEvents

## Slide 53

### Case Study -- CVE-2024-38067

ocspisapi.dll – httpextensionproc → OcspSvc::COcspIsapiExtension::DispatchStencilCall

__int64 __fastcall OcspSvc::COcspIsapiExtension::DispatchStencilCall(

OcspSvc::COcspIsapiExtension *this,

struct ATL::AtlServerRequest *a2)

{

[...]

v34 = OcspSvc::OCSPRequestContext::Decode((OcspSvc::OCSPRequestContext *)&v73, *((_DWORD *)v3 + 366), &v85); // =============> **[a]** v13 = v34; **[a]**

**[a]** OCSP server receives an unauthenticated HTTP POST request and decodes the POST data using

[...]

v38 = OcspSvc::OCSPRequestContext::Validate( // ==============> **[b]**

CryptDecodeObjectEx

(OcspSvc::OCSPRequestContext *)&v73,

**[b]** The decoded data is then processed by the OCSP service logic

*((_DWORD *)v3 + 0x16D),

*((_DWORD *)v3 + 0x16F));

**[c]** Regardless of success or failure, the server sends an OCSP response back to the client by calling

[...]

else if ( !v5

OcspSvc::COcspIsapiExtension::SendOCSPStatus

|| (v62 = OcspSvc::COcspIsapiExtension::SendOCSPStatus(v59, v5), (v63 = v62) != 0) // ============> **[c]**

&& (CSPrintErrorLineFile(0x8AB09C6u, v62), v63 < 0) )

}

#BHUSA @BlackHatEvents

## Slide 54

### Case Study -- CVE-2024-38067

ocspisapi.dll – OcspSvc::COcspIsapiExtension::DispatchStencilCall → OcspSvc::COcspIsapiExtension::SendResponseToClient → ServerSupportFunction

__int64 __fastcall OcspSvc::COcspIsapiExtension::SendResponseToClient( struct ATL::AtlServerRequest *a1, struct OcspSvc::COcspResponseCacheEntry *a2, char *a3,

struct _CRYPTOAPI_BLOB *a4, int a5)

{ [...]

if ( (*(unsigned int (__fastcall **))(*((_QWORD *)a1 + 12) + 0xB8i64))( // ===========> **[d]**

*(_QWORD *)(*((_QWORD *)a1 + 12) + 8i64),

**[d]** Internally, SendOCSPStatus calls SendResponseToClient, which invokes ServerSupportFunction (IIS dispatch API), eventually reaching W3_RESPONSE::WriteEntityChunks through SSFVectorSend

1037i64,

v26, 0i64,

0i64) )

[...]

}

#BHUSA @BlackHatEvents

## Slide 55

### Case Study -- CVE-2024-38067

ocspisapi.dll – ServerSupportFunction → W3_RESPONSE::WriteEntityChunks

signed int __fastcall W3_RESPONSE::WriteEntityChunks( W3_RESPONSE *this,

struct _HTTP_DATA_CHUNK *a2, unsigned int a3, unsigned int a4, int a5, struct W3_CONTEXT_BASE *a6, unsigned int *a7, int *a8)

{ [...] if ( v13 ) {

result = W3_RESPONSE::Flush(this, a4, a5, a6, a7, a8); // ===============> **[e] if(result ==  error){**

**return;**

**} }** […]

W3_CONTEXT_BASE::PostCompletion(*((W3_CONTEXT_BASE **)this + 6), 0, 2); // ==============> **[f]** [...]

**[e]** After sending the OCSP status back to the client, the server calls PostCompletion

**[f]** PostCompletion sets the I/O completion callback using PostQueuedCompletionStatus

→ As a result, the session is closed and the ISAPI_CONTEXT structure is dereferenced and eventually released

However, if the unauthenticated client disconnects the TCP connection with the OCSP server before the status is sent back, the **W3_RESPONSE::Flush** function fails and returns a negative error value. As a result, it returns without posting the completion status, and the session will no longer be closed. **The reference count of the ISAPI_CONTEXT will never decrease.** When the reference count reaches 0x1366, the OCSP service will stop receiving requests and return a “503 Service Unavailable" error to any normal client.

}

#BHUSA @BlackHatEvents

## Slide 56

### Case Study -- CVE-2024-38067

##### **Before**

After

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Case Study -- CVE-2024-38067
Before After
D:\>python ocsp_demo.py 192.168.217.2uu
200
Cache-Control: no-cache
Content-Type: appLlication/ocsp-response
D:\>python ocsp_demo.py 192.168.217.244
503 Service Unavailable
Server: Microsoft—IIS/10.0
Date: Tue, 81 Jul 2025 63:11:27 GMT
Content-Length: 5
```

## Slide 57

### IIS

###### **Impact:**

- ⚫ Unauthenticated: No authentication or extra configuration required

- ⚫ Persistent DoS: Service permanently stops handling requests from legitimate clients; does not require maintaining connections from the attacker

- ⚫ More Severe: Mishandling ISAPI_CONTEXT reference counting can not only cause persistent DoS but also lead to use-after-free remote code execution — a common issue when pointer reference counts are mishandled

###### **Secure Development Considerations:**

- ✓ Use ServerSupportFunction carefully within HttpExtensionProc of your ISAPI extension DLL, especially for dispatch routines that manage referencing and dereferencing of ISAPI_CONTEXT.

#BHUSA @BlackHatEvents

## Slide 58

## Parsing and Handling Stages Leading to Pre-auth RCE

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
; bisekhat
EFFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Parsing and Handling Stages
Leading to Pre-auth RCE
```

## Slide 59

### KDC Proxy HTTP Server

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
KDC Proxy HTTP Server
a
Cl
a | DNS Server
{|
443(HTTPS)
KDC Proxy
Server
=S
| Domain query
=
443(HTTPS) —=
Oo
S> KDC Server
LDAP,
Kerberos auth —
443(HTTPS) SS
Gal)
```

## Slide 60

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Register callback KpsHttploCompletion Network
HttpReceiveClie KpsHttpReceiveClientCertloCompletion
new Client
Connect
Client Send
Client
Disconnect
ntCertificate
HttpReceiveHttp KpsHttpReceiveRequestloCompletion
Request
HttpReceiveReq KpsHttpReceiveRequestEntityloCompletion
uestEntityBody
HttpWaitForDisc
onnect
No KpsHttpCancelRequestloCompletion
HttpCancelHttp
Request
( KpsHttpSendPostResponseloCompletion
HttpSendHttpRe
sponse
Server Sent
Complete
KpsHttpSendResponseloCompletion
```

## Slide 61

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
DNS server
query domain -
KpsHttpReceiveR
‘Entityloc DsGetDcName \w@evereroet Xxx.testyours.ZZ
sGetDcName S/T
eques vot ylovo ae SRV _kerberos._tcp.dc._msdcs.testyours.zz
mpletion ae SRV _kerberos._tcp.default-first-site-name._sites.dc._msdcs.testyours.zz
se abc.testyours.zz
7
MSAFD socket
socket ae FAKE LDAP server
s.
se, response kerberos server:
. abcd.testyours.zz
KpsSocketloCompletion
abc.testyours.zz
KpsSocketConnectAndSendloCompletion
FAKE Kerberos server
/
WSARecv KpsSocketRecvDataLengthloCompletion
abcd.testyours.zz
KpsSocketRecvDataloCompletion
```

## Slide 62

### Case Study -- CVE-2024-43639

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat by 2
BRIEFINGS a
Case Study - CVE-2024-43639
. _int64 __fastcall ASN1EncCheck(Encoder » unsigned int
KpsSocketRecvDataloCompletion {
t dword18 = a1->cur_size_18h;
if ( (__int64)pvoid1® + dword18 - al->cur_buf_28h - (a1->dword24 != @) >= a2 )
KpsDerPack return 1;
{
v9 = al->cur_size_18h;
( ASNiEnc_KDC_PROXY MESSAGE ) if ( a2 > dwordis
v1@ = dword18 + v9;
. 1-> i 18h = v1e;
ASN1DEREncOctetString chelates sea
14 v11 = LocalReAlloc(pvoidie, Wie), 42u);
( ASN1EncCheck )
```

## Slide 63

### Case Study -- CVE-2024-43639

###### 0:007> r

rax=000001af7606b005 rbx=000001af76066fb0 rcx=0000000000000084 rdx=000001af73ac01c0 rsi=00000000fffffbfb rdi=0000000000000005 rip=00007ffd5217740d rsp=0000004a8837f230 rbp=0000000000000000 r8=7ffffffffffffffc  r9=0000004a87f53000 r10=00000fffa9f5a744

r11=4000001000000410 r12=0000000000000000 r13=00007ffd41d50048 r14=0000004a8837f3e8 r15=0000004a8837f3f0 iopl=0         nv up ei pl nz na pe nc

cs=0033  ss=002b  ds=002b  es=002b  fs=0053  gs=002b             efl=00010202 MSASN1!ASN1BEREncLength+0x4d: 00007ffd`5217740d 8808            mov     byte ptr [rax],cl ds:000001af`7606b005=?? ```

###### 0:007> k

# Child-SP          RetAddr Call Site

00 0000004a`8837f230 00007ffd`52176a4b     MSASN1!ASN1BEREncLength+0x4d 01 0000004a`8837f260 00007ffd`41d2ea03     MSASN1!ASN1BEREncCharString+0x2b 02 0000004a`8837f290 00007ffd`52177802 kpssvc!ASN1Enc_KDC_PROXY_MESSAGE+0x73 03 0000004a`8837f2d0 00007ffd`41d40900     MSASN1!ASN1_Encode+0xa2 04 0000004a`8837f300 00007ffd`41d42325     kpssvc!KpsDerPack+0xdc 05 0000004a`8837f360 00007ffd`41d3e9e5     kpssvc!KpsPackProxyResponse+0xcd 06 0000004a`8837f3e0 00007ffd`41d3e7a2 kpssvc!KpsSocketRecvDataIoCompletion+0x20d 07 0000004a`8837f460 00007ffd`52f01f31     kpssvc!KpsSocketIoCompletion+0xb2 ```

#BHUSA @BlackHatEvents

## Slide 64

### Remote Desktop Service

3389:

3387:

HTTP Websocket Wrapper

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Remote Desktop Service
3389:
3387(HTTP websocket)
Client Server
: 3389
X.224 Connection Request PDU-—————————_>: (eo)
? >» Connection Initiation
<$—_———————-.224 Connection Confirm PLU it
MCS Connect Initial PDU with GCC Conference Create Request
H i Basic Settings Exchange
<@—MCS Connect Response PDU with GCC Conference Create Response———¢ RD Server
MCS Erect Domain Request PDU——$—$—______——p>:
MCS Attach User Request POU —_————____—_»»:
<———_—_—_—————-MCS Attach User Confirm POU } Channel Connection a |
; eeeese : cs
3387(HTTP websocket)
3387 ; ™”
. Li
Client Server
X.224 Connection Request PDU: %
? >» Connection Initiation
X.224 Connection Confirm PRU,
-——MCS Connect Initial PDU with GCC Conference Create Request:
i i 4 Basic Settings Exchange n ez
<@—MCS Connect Response PDU with GCC Conference Create Response———t 3387(HTTP websocket)
MCS Erect Domain Request PDU——$—$—______——p>: . 3389
MCS Attach User Request POU —_————____—_»»: (e)
<———_—_—_—————-MCS Attach User Confirm POU } Channel Connection
; eeeese :
```

## Slide 65

### Remote Desktop Gateway Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
Remote Desktop Gateway Service
RD Server
ca
| 3]
443 HTTPS
A 3391 DTLS
{3 |
443 HTTPS RD
5 3391DTLS_ I Gateway
co
= 443 HTTPS
. 3391 DTLS
{o)
```

## Slide 66

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Websocket
non-Websocket
a
Register callback loCompletionCallback Network
( HendersicetecrieRavOataconseton
+ HandleReceiveRequestCompletion \—
( HandleReceiveRequestEntityCompletion )
{ HandleDisconnected
new Client
Connect
Client Send
Client
HttpReceiveHttp
Request
HttpReceiveReq
uestEntityBody
Disconnect
HttpWaitForDisc
onnect
HttpCancelHttp
Request
( HandleWebSocketSendRawDataCompletion )
HandleSendResponseCompletion ) ra SUE
( HandleSendResponseEntityCompletion )
HttpSendHttpRe
sponse
HttpSendRespo
nseEntityBody
```

## Slide 67

Clean Client1, Client2 with
then Client2
ConID1?
with ConID1?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
HandleReceiveRequestCompletion
ProcessOutChannelOrWebS HandleSendResponseCompl CAAHttpServerTransport::Re WebSocketReceiveRaw
ocketRequest etion ceiveData Data
websocket Connection! arg3
= ~
request, ConID1 CAAHttpServer Siliceppe all , f..., .
Client1 > --—P Connection Clean Client,
HttpSendHtt ;
a P Connection1-> then Client2
recv_ov->buff=arg3 with ConID1?
HandleWebSocketReceiveRawDataCompletion
Send Data
Get Connection1
from hash_table
by ConlD1
WebSocketReceiveLoop
memcpy(
Connection1->
recv_ov->buff,
src, size)
Futher Authentication
```

## Slide 68

### Case Study -- CVE-2025-21309

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
BRIEFINGS . ;
Case Study -- CVE-2025-21309
ProcessOutChannelOrWebS HandleSendResponseCompl CAAHttpServerTransport::Re
ocketRequest etion ceiveData
websocket arg3
request, ConID1 _ CAAHttpServerC = CAAHttpServerConn
Client1 yl onnection1 , ection+1430h
HttpSendHttp
Response AddRef timegap
HandleDisconnected
disconnect
CAAHttpServerConne
ction::OnDisconnected
Deref CAAHttpServer
Connection
```

## Slide 69

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
BRIEFINGS
ProcessOutChannelOrWebS
HandleSendResponseCompl CAAHttpServerTransport::Re
ocketRequest
etion ceiveData
Connection1
websocket
request, ConID1 CAAHttpServerC
Client1 --> onnection1 >
arg3
= CAAHttpServerConn
ection+1430h
HttpSendHttp
Response
AddRef
timegap
HandleDisconnected
disconnect
CAAHttpServerConne
ction::OnDisconnected
Deref CAAHttpServer
Connection
ProcessOutChannelOrWebS
ocketRequest
websocket New
request, ConID1 Connection2,
Client2 > Store in
hash_table with
ConlD1
```

## Slide 70

HttpReceiveRequest
EntityBody
Deref
CAAHttpServerConnect
ion1
Get
when finish
Connection2
from
hash_table
by ConID1
arg3
dangling
pointer
HandleWebSocketReceiveRawDataCompletion
Get
Connection2
from
hash_table
memcpy(
by ConID1
Connection2->
recv_ov->buff,
src, size)
Send Data

EntityBody
HandleWebSocketReceiveRawDataCompletion
memcpy(
Connection2->
recv_ov->buff,
src, size)

#BHUSA @BlackHatEvents

## Slide 71

### Case Study -- CVE-2025-21309

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
BRIEFINGS
Case Study -- CVE-2025-21309
O:117> 4r
rax=O00002chas9aabt 0
rdx=0002000000010000
rip=O0007f£fd84747d1?
r8=0000000000000006e
r11=0000000e00000001
rl4=000002c6ee9edd60
cs=0033 ss-002b ds=002b es=002b fs=0053
neveort !mencpy+0x1?7 :
QO007£fd* 8474701? 408919 mov
O:117> k
# Child—-SpP Ret Addr
O00 OO0000d4* 7O37£338 OOOO? ffd* 847390660
01 OO0000d4* 7O37£340 OOO07ffd 64f42c64
O02 OO0000d4* 7O37£380 OOO07ffd 64f£43ba2
O03 GO000dd4* FO37£580 OOOO? ffd* 64£455eb
O4 OO0000d4* FO37£610 OOO0Fffd’ s4927 70s
OS OO0000d4* 7037?£6a0 OOOO7£Ed* 85347493
06 OOO000d4* 7O37£6£0 OOOO7 FEM 85394bee8
0? QOO000d4* 7O37£770 OOO07£fd* 84824cb0
O08 OO0000d4* 7O37?fa60 OOO07ffd* 8539bedch
09 OOO0000d4* 7037f£a90 O0000000* coo00000
rbx=000000000000000e
rei=000002chadlact 66
rep=O000000d47037£338
r9=O00000000000000e
r12=d000000000000000
r1lS=000002c6fc23b¢E 40
rox=000002¢cbhai3 Jaabe 0
rdi=cooddddddd006000
rbp=000000d47037£480
rl0=000002chalIaabtO
ri3=0000d0000000000e
g==002b
Call Gite
nevert |! mencpy+0x1?
nsvert !memopy_s+0x60
saedge! CAAHttpServerTransport : :WebSocketReceiveLooptOxafc
ef 1=-00010283
aaedge!CAAHttpServerTransport : :HandleWebSocketReceiveRavDataCompletion+0s2de
saedge!CAAHttpServerTransport: :IoCompletionCallback+0z22b
KERNEL3 2! BasepTploCallback+0z5a
ntd1l!/TpplopExecuteCallbsck+02193
ntd1ll!/TppWorkerThread+0e448
KERNEL 2 ! BaseThreadInitThunk+0x10
ntdll!RtlUserThreadStart+Oxz2h
```

## Slide 72

## Conclusion

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pie hat
EFINGS
AUGUST be 2025
MANDALAY BAY / LAS VEGAS
Conclusion
```

## Slide 73

### Looking Ahead

⚫ MSRC updated their SDL servicing bar for DoS-related vulnerabilities.(https://learn.microsoft.com/en-us/security/engineering/security-bug-barsample) No bounty for Resource Exhaustion

- ⚫ Logic-based DoS vulnerabilities still in scope for High value assets. Includes: DHCP Server, DNS Server, epmapper (MS-RPC), Hyper-V Remote Access, IIS Web Server HTTP/HTTPs, Kerberos Authentication Service, LDAP, NFS, RDP Server, SMB, and Windows Server Update Service (WSUS).

- ⚫ RCE vulnerabilities are also common in HTTP services, especially during the parsing of POST data. Try to fuzz it!

#BHUSA @BlackHatEvents

## Slide 74

### Take Aways

⚫ Apply useful technique across the entire attack surface to uncover similar issues.

- ⚫ DoS doesn't require crashes — logic flaws in request handling alone can also permanently block services

- ⚫ Further reflection: the potential for DoS and even RCE may lie in the deeper, more fundamental logic of the target

#BHUSA @BlackHatEvents

## Slide 75

# Thanks!

k0shl(@KeyZ3r0) https://x.com/KeyZ3r0 VictorV(@vv474172261) https://x.com/vv474172261 Wei(@XiaoWei___) https://x.com/XiaoWei___ Zhiniang Peng(@edwardzpeng) https://x.com/edwardzpeng

#BHUSA @BlackHatEvents
