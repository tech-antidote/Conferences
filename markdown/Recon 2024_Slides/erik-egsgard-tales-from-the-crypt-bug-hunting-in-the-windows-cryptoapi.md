---
title: "Tales From The Crypt Bug Hunting in the Windows CryptoAPI"
speakers: ["Erik Egsgard"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Erik Egsgard_Tales From The Crypt Bug Hunting in the Windows CryptoAPI.pdf"
pages: 41
sha256: "3792fe04ec4896dfb0daa66674c715906a06db0cbcd01c0164ccc8476b27aea0"
text_chars: 23284
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:29:02Z"
---
# Tales From The Crypt Bug Hunting in the Windows CryptoAPI

**Speakers:** Erik Egsgard  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Erik Egsgard_Tales From The Crypt Bug Hunting in the Windows CryptoAPI.pdf` (41 pages)


## Slide 1

# **Tales From The Crypt**

**Bug Hunting in the Windows CryptoAPI** RECon 2024

## Slide 2

## **Background**

### **Field Effect**

- Founded in 2016​, ~200 employees.

- Headquartered in Ottawa, Canada with employees also in AU, NZ, UK and US.

- A holistic, comprehensive approach to cyber security.

- A focus on solving security challenges for small and midsize organizations.

### **Erik Egsgard**

- ~20 years in cyber security

- EDR Security Developer

- Vulnerability researcher

fieldeffect.com 2

## Slide 3

## **Story Time**

fieldeffect.com 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Story Time
- Crypt Decode fuzzing:
- Got an AFL crash somewhere, think is is in the decoding of
szOID_PKIX_POLICY_QUALIFIER_USERNOTICE
- Another one in decoding of CRYPT_TIMESTAMP_RESPONSE
4,31 °
fieldeffect.com 3
```

## Slide 4

## **Crypt Decoding**

fieldeffect.com 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Crypt Decoding
Cb
BOOL CryptDecodeObjectEx(
[in] DWORD dwCertEncodingType,
[in] LPCSTR lpszStructType,
[in] BYTE *pbEncoded, decodeParam.cbSize = ( decodeParam );
decodeParam.pfnALloc = allocWrapper;
decodeParam.pfnFree = freeWrapper;
[in] DWORD cbEncoded,
[in] DWORD dwFlags,
[in] PCRYPT_DECODE_PARA pDecodePara,
[out] *pvStructinfo,
[in, out] DWORD *pcbStructInfo
if( CryptDecodeObjectEx(
X509_ASN_ENCODING | PKCS_7_ASN_ENCODING,
targetObjectType,
decodePtr,
dataLength,
CRYPT_DECODE_ALLOC_FLAG,
&decodeParam,
&object,
S&objectLength ) )
vlog( "Decoded object into 0x%08x bytes\n", objectLength )
freeWrapper( object );
t
5
else
{
vlog( "CryptDecodeObjectEx failed \n", GetLastError() );
fieldeffect.com 4
```

## Slide 5

## **AFL False Start**

fieldeffect.com 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
AFL False Start
inding to #0.
trumented module crypt
umented module
a crash
\winafl\afl-f
fieldeffect.com 5
```

## Slide 6

## **AFL False Start**

fieldeffect.com 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
AFL False Start
WinAFL 1.17 based on AFL 2.43b (FuzzX509.exe)
T= ESS Te | +- overall results ----+
| run time : @ days, ® hrs, ® min, 31 sec | cycles done : 0
| last new path : © days, © hrs, © min, 1 sec | total paths : 201
| last uniq crash : none seen yet | uniq crashes : 0
| last uniq hang : none seen yet | uniq hangs : 0
+— cycle progress ------------------—- +— map coverage —+—-------------------—— +
| now processing : 2 (1.00%) | map density : 0.16% / 3.65%
| paths timed out : © (0.00%) | count coverage : 1.33 bits/tuple
+- stage progress + findings in depth
| now trying : havoc | favored paths : 135 (67.16%)
| stage execs : 9570/32.8k (29.21%) | new edges on : 179 (89.05%)
| total execs : 52.0k | total crashes : ® (@ unique)
| exec speed : 1637/sec | total tmouts : © (@ unique)
+- fuzzing strategy yields ----------- Sa +- path geometry
| bit flips : 8/344, 4/342, 4/338 | levels : 3
| byte flips : 0/43, 0/41, 0/37 | pending : 200
| arithmetics : 33/2406, 0/1509, 0/21 | pend fav : 135
| known ints : 2/179, 1/1219, 2/1472 | own finds : 200
| dictionary : 0/0, 0/0, 0/0 | imported : n/a
| | stability
|
havoc : 137/32.8k, 0/0
: 44.87%/18, 0.00%
fieldeffect.com 6
```

## Slide 7

## **Timestamp Decoding**

```
0:000> wt -i kernelbase -i kernel32 -i verifier -i ucrtbase -i vcruntime140 -i ntdll
   27     0 [  0] CRYPT32!CryptDecodeObjectEx
    5     0 [  1]   CRYPT32!LoadRegFunc
   76 24702 [  0] CRYPT32!CryptDecodeObjectEx
   16     0 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx
   23   886 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   54     0 [  3]       MSASN1!ASN1_Decode
   14     0 [  4]         CRYPT32!ASN1Dec_TimeStampResp
   77     0 [  5]           MSASN1!ASN1BERDecExplicitTag
   13     0 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
   14     0 [  6]             CRYPT32!ASN1Dec_PKIFreeText
   10     0 [  7]               CRYPT32!ASN1DecRealloc_Elements
   81  2474 [  6]             CRYPT32!ASN1Dec_PKIFreeText
   60  2909 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
   44  3213 [  4]         CRYPT32!ASN1Dec_TimeStampResp
   95  3301 [  3]       MSASN1!ASN1_Decode
   35  4282 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   32     0 [  4]         CRYPT32!Asn1TimeStampResponseExCallback
   29     0 [  5]           CRYPT32!Asn1X509GetPKIFreeText
   45   457 [  4]         CRYPT32!Asn1TimeStampResponseExCallback
   80  4367 [  3]       CRYPT32!PkiAsn1AllocStructInfoEx
   42  8729 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   30   116 [  3]       MSASN1!ASN1_FreeDecoded
   51  8875 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   18  8926 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx
   94 33648 [  0] CRYPT32!CryptDecodeObjectEx
```

fieldeffect.com

7

## Slide 8

## **Strings are Hard**

fieldeffect.com 8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Strings are Hard
©, Decompile: Asn1X509GetPKIFreeText - (crypt32.dll)
PWSTR) *
ng = output
fieldeffect.com 8
```

## Slide 9

## **Strings are Hard**

fieldeffect.com 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Strings are Hard
©, Decompile: Asn1X509GetPKIFreeText - (crypt32.dll)
*
Size
utputString, st
ring [str
fieldeffect.com 9
```

## Slide 10

## **Where Is This Used**

fieldeffect.com 10

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Where Is This Used
The CryptRetrieveTimeStamp function encodes a time stamp request and retrieves the time
stamp token from a location specified by a URL to a Time Stamping Authority (TSA).
Syntax
C++
BOOL CryptRetrieveTimeStamp(
[in] LPCWSTR wszUrl,
DWORD dwRetrievalFlags,
DWORD dwTimeout,
[in] LPCSTR pszHashId,
[in, optional] + CRYPT_TIMESTAMP_PARA *pPara,
[in] t *pbData,
cbData,
[out] PCRYPT_TIMESTAMP_CONTEXT *ppTsContext,
[out, optional] PCCERT_CONTEXT *ppTsSigner,
[out, optional] HCERTSTORE *phStore
Parameters
[in] wszurl
A pointer to a null-terminated wide character string that contains the URL of the TSA to
which to send the request.
fieldeffect.com
10
```

## Slide 11

## **Signtool PoC**

fieldeffect.com 11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Signtool Po
SignTool
Article » 03/28/2022 + 6 contributors
In this article
Partial list of operations, options, and arguments
Remarks
Examples
SignTool (Signtool.exe) is a command-line CryptoAP! tool that digitally-signs files, verifies
signatures in files, and time stamps files.
command f Copy
SignTool [Operation] [Options] [FileName ...
The following command signs and time stamps the file:
SignTool sign /f MyCert.pfx /t http://timestamp.digicert.com MyControl.exe
© Note
For information about time stamping a file after it has already been signed, see Adding
fieldeffect.com
11
```

## Slide 12

## **CVE-2024-30020**

fieldeffect.com 12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
CVE-2024-30020
C:\WINDOWS\system32\cmd. X ar
Microsoft Windows [Version 10.0.22621.3737]
(c) Microsoft Corporation. All rights reserved.
c:\dev\poc>signtool.exe timestamp /td SHA256 /tr http://127.0.0.1:8080/ /v dummy.exe
SignTool Error: An error occurred while attempting to timestamp: dummy.exe
SignTool Error: An unexpected internal error has occurred.
Error information: "SignerTimeStampEx3() failed." (-1073741819/0xc0000005)
C:\dev\poc>
fieldeffect.com 12
```

## Slide 13

## **UserNotice Fuzzing**

fieldeffect.com 13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
UserNotice Fuzzing
[cpu00ee1: 6%]
WinAFL 1.17 based on AFL 2.43b (FuzzX509.exe)
+- process timing ------------------------------------— +- overall results -—---+
| run time : ® days, © hrs, 31 min, 3 sec | cycles done : 0 |
| last new path : © days, © hrs, © min, © sec | total paths : 947 |
| last uniq crash : none seen yet | uniq crashes : 0 |
| last uniq hang : none seen yet | uniq hangs : 0 |
+— cycle progress -—-------------—--—— +—- map coverage —+—-------—--—--—--—--—-—— +
| now processing : 795 (83.95%) | map density : 0.36% / 7.71% |
| paths timed out : © (0.00%) | count coverage : 1.48 bits/tuple |
+- stage progress + findings in depth +
| now trying : havoc | favored paths : 592 (62.51%) |
| stage execs : 12.2k/24.6k (49.48%) | mew edges on : 690 (72.86%) |
| total execs : 2.38M | total crashes : ° (O unique) |
| exec speed : 1298/sec | tal tmouts : © (@ unique) |
+- fuzzing strategy yields —-----+- - -+- path CLS) --- +
| bit flips : 115/46.9k, 45/46.5k, 31/45.5k | levels : 6
byte flips : 1/5863, 3/5409, 2/4526 | pending : 494 |
arithmetics : 183/327k, 4/167k, 4/42.0k | pend fav : 107 |
known ints : 33/24.6k, 21/148k, 17/163k | own finds : 946 |
| imported : n/a |
| stability |
+
havoc : 478/1.31M, 0/0
trim : 44.21%/2090, 0.00%
|
|
|
| dictionary : 0/0, 0/0, 6/16.8k
|
|
+ - _ - _ [cpu0000e1: 4%]
fieldeffect.com
13
```

## Slide 14

## **Timestamp Decoding II**

```
0:000> wt -i kernelbase -i kernel32 -i verifier -i ucrtbase -i vcruntime140 -i ntdll
   27     0 [  0] CRYPT32!CryptDecodeObjectEx
    5     0 [  1]   CRYPT32!LoadRegFunc
   76 24702 [  0] CRYPT32!CryptDecodeObjectEx
   16     0 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx
   23   886 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   54     0 [  3]       MSASN1!ASN1_Decode
   14     0 [  4]         CRYPT32!ASN1Dec_TimeStampResp
   77     0 [  5]           MSASN1!ASN1BERDecExplicitTag
   13     0 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
   14     0 [  6]             CRYPT32!ASN1Dec_PKIFreeText
   10     0 [  7]               CRYPT32!ASN1DecRealloc_Elements
   81  2474 [  6]             CRYPT32!ASN1Dec_PKIFreeText
   60  2909 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
   44  3213 [  4]         CRYPT32!ASN1Dec_TimeStampResp
   95  3301 [  3]       MSASN1!ASN1_Decode
   35  4282 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   32     0 [  4]         CRYPT32!Asn1TimeStampResponseExCallback
   29     0 [  5]           CRYPT32!Asn1X509GetPKIFreeText
   45   457 [  4]         CRYPT32!Asn1TimeStampResponseExCallback
   80  4367 [  3]       CRYPT32!PkiAsn1AllocStructInfoEx
   42  8729 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   30   116 [  3]       MSASN1!ASN1_FreeDecoded
   51  8875 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
   18  8926 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx
   94 33648 [  0] CRYPT32!CryptDecodeObjectEx
```

fieldeffect.com

14

## Slide 15

## **CryptDecodeObjectEx Internals**

10110110
DER
01111101
Data
10100101

_ASN1Dec_* functions_

_ASN1…DecodeEx functions_

fieldeffect.com 15

## Slide 16

## **ASN1Dec_PKIFreeText**

fieldeffect.com 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
ASN1Dec_PKI/FreeText
C, Decompile: ASN1Dec PKiFreeText - (crypt32.dll)
1
2ibo
PKIFreeText ::= SEQUENCE SIZE (1..MAX) OF UTF8String
-- text encoded as UTF-8 String [RFC3629] (note: each
-- UTF8String MAY include an [RFC3066] language tag
-- to indicate the language of the contained text
-- see [RFC2482] for details)
fieldeffect.com 16
```

## Slide 17

## **ASN1Dec_PKIFreeText**

fieldeffect.com 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT ne, a
ASN1Dec_PKIiFreeText ssi
‘G, Decompile: ASN1Dec PKiFreeText - (crypt32.dll)
1
PKIFreeText ::= SEQUENCE SIZE (1..MAX) OF UTF8String
-- text encoded as UTF-8 String [RFC3629] (note: each
-- UTF8String MAY include an [RFC3066] language tag
-- to indicate the language of the contained text
-- see [RFC2482] for details)
bool ASN1Dec_PKIFreeText(ASN1decoding_s *
if (bufferSsi ->StringCount) {
if (bufferSize == 0) {
bufferSize = 0x10;
}
else {
bufferSize = bufferSize * 2;
}
localBuffer = (ANSI STRING *)ASN1DecRealloc(_localDecoder, —>StringArray, bufferSize << 4);
if (localBuffer == (ANSI STRING *)0x0) {
return false;
}
—>StringArray = localBuffer;
}
stringCount = —>StringCount;
—>StringCount = stringCount + 1;
success = ASNIBERDecUTF8String(_localDecoder, 0xc, ->StringArray + stringCount) ;
50 : fieldeffect.com
```

## Slide 18

## **ASN1Dec_PKIFreeText**

fieldeffect.com 18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
ASN1Dec_PKI/FreeText
‘G, Decompile: ASN1Dec PKiFreeText - (crypt32.dll)
1
bool ASN1Dec_PKIFreeText(ASN1decoding_s *
if (bufferSize <= —>StringCount) {
if (bufferSize == 0) {
bufferSize = 0x10;
else { a ~~ “> Tw
localBuffer = (ANSI STRING *)ASN1DecRealloc(_localDecoder, —>StringArray, bufferSize << 4);
if (localBuffer == (ANSI STRING *)0x0) {
return false;
o
—>StringArray = localBuffer;
}
stringCount = —>StringCount;
—>StringCount = stringCount + 1;
success = ASNIBERDecUTF8String(_localDecoder, 0xc, ->StringArray + stringCount) ;
50
fieldeffect.com
```

## Slide 19

## **PoC Attempt**

```
Count = 0xc000000
Count * sizeof( UTF8_STRING ) = 0xc000000 * 0x10
      = 0xc0000000
...
alloc = 0x1000000 * 0x10
alloc = 0x2000000 * 0x10
alloc = 0x4000000 * 0x10
alloc = 0x8000000 * 0x10
alloc = 0x10000000 * 0x10 ***
```

fieldeffect.com 19

## Slide 20

## **Size Checks**

```
0:000> wt -i kernelbase -i kernel32 -i verifier -i ucrtbase -i vcruntime140 -i ntdll
```

- `00007ff7`1f3a13d0`

```
   27     0 [  0] CRYPT32!CryptDecodeObjectEx
```

```
    5     0 [  1]   CRYPT32!LoadRegFunc
```

```
   76 24702 [  0] CRYPT32!CryptDecodeObjectEx
```

- `16     0 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx`

```
   23   886 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx
```

```
   54     0 [  3]       MSASN1!ASN1_Decode
```

```
   14     0 [  4]         CRYPT32!ASN1Dec_TimeStampResp
```

```
g_dwMaxDecodeBufferSize = 0x61a8000
```

```
   77     0 [  5]           MSASN1!ASN1BERDecExplicitTag
```

```
   13     0 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
   14     0 [  6]             CRYPT32!ASN1Dec_PKIFreeText
```

```
= 100MB
```

- `10     0 [  7]               CRYPT32!ASN1DecRealloc_Elements`

- `81  2474 [  6]             CRYPT32!ASN1Dec_PKIFreeText`

```
   60  2909 [  5]           CRYPT32!ASN1Dec_PKIStatusInfo
```

- `44  3213 [  4]         CRYPT32!ASN1Dec_TimeStampResp`

```
   95  3301 [  3]       MSASN1!ASN1_Decode
```

- `35  4282 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx`

- `32     0 [  4]         CRYPT32!Asn1TimeStampResponseExCallback`

- `29     0 [  5]           CRYPT32!Asn1X509GetPKIFreeText`

- `45   457 [  4]         CRYPT32!Asn1TimeStampResponseExCallback`

- `80  4367 [  3]       CRYPT32!PkiAsn1AllocStructInfoEx`

- `42  8729 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx`

- `30   116 [  3]       MSASN1!ASN1_FreeDecoded`

- `51  8875 [  2]     CRYPT32!Asn1InfoDecodeAndAllocEx`

- `18  8926 [  1]   CRYPT32!Asn1TimeStampResponseDecodeEx`

```
   94 33648 [  0] CRYPT32!CryptDecodeObjectEx
```

fieldeffect.com

20

## Slide 21

## **UserNotice Fuzzing**

fieldeffect.com 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
UserNotice Fuzzing
[cpu0e0ee1: 4%]
a cherethiet
WinAFL 1.17 based on AFL 2.43b (FuzzX509.exe) ee eas
(at thatet wet
= eS LE) EES +- overall results -—---+ theese
| run time : 0 days, 1 hrs, 14 min, 2 sec | cycles done : 4 sietets
| last new path : © days, © hrs, © min, 7 sec | total paths : 1337
| last uniq crash : none seen yet | uniq crashes : 0
| last uniq hang : none seen yet | uniq hangs : 0
+—) cycle progress —————————_— +- map coverage -+---------------------— +
| now processing : 1326* (99. | map density : 0.25% / 9.17%
| paths timed out : 0 (0.00%) count coverage : 1.57 bits/tuple
+- stage progress findings in depth
| now trying : havoc favored paths : 701 (52.43%)
| a
| stage execs : 3240/8192 (39. | mew edges on : 904 (67.61%) . WY
| total execs : 5.58M | total crashes : 0 (0 unique) : WS ;
| ‘
+
| exec speed : 1207/sec total tmouts : 0 (0 unique) ; SY
+- fuzzing strategy yields -----------+--------------— +- path geometry ’
| bit flips : 199/118k, 78/117k, 52/115k levels : 14 SS
|
byte flips : 1/14.8k, 4/13.9k, 3/12.1k | pending : 414 ;
arithmetics : 285/828k, 7/439k, 5/83.1k | pend fav : 2 ~
known ints : 54/62.8k, 42/394k, 29/449k | own finds : 1336  "
| imported : n/a
| stability
|
|
|
| dictionary : 0/0, 0/0, 22/145k
| havoc : 555/2.77M, 0/0
| : 34.71%/4739, 0.00%
fieldeffect.com 21
```

## Slide 22

## **Vulnerability Constraints**

- Input Buffer Size <= 100MB

- Object Count * Object Size > 0x80000000 (2GB)

- ASN1 Decoding Expansion = 2GB / 100MB

- Need ~20x Expansion

- Encoding Must Be Valid

fieldeffect.com 22

## Slide 23

## **ASN1DecRealloc Xref**

fieldeffect.com 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
ASN1DecRealloc Xref
References to ASN1DecRealloc - 87 locations
Locati... Labe' Code Unit Context Function Name
18007d7bf qword ptr [->MSASN1. ASN1Dec_OcspBasicResponseList
[->Mi
18007ed74
18007ee83
1806
18007fa63
80
80080120
18008
180087
180088
1800882
180088570
fieldeffect.com
```

## Slide 24

## **Validate Exploitability**

fieldeffect.com 24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Validate Exploitability
if (uVaré
uVa
}
uVarl
7
(lo ars, z a 8 + *(longlong *) (
while ( (int) CONCAT71 (
fieldeffect.com
```

## Slide 25

## **ASN1Dec_CRLDistributionPoints()**

```
Object Size = (1 << 6) = 0x40
Input Size = 2 Bytes
Ratio = 0x20!!
```

fieldeffect.com 25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
ASN1Dec_CRLDistribution
{
—>distPointCount)
52 68, —>distPointArray, initialObj
53
54 return false;
55 }
56 —>distPointArray = distPointeArray;
Count = initialObjectCount;
id-ce-cRLDistributionPoints OBJECT IDENTIFIER ::= { id-ce 31 }
CRLDistributionPoints :
t= SEQUENCE SIZE (1..MAX) OF DistributionPoint
° a) 8 Object Size = (1 << 6) = 0x40
DistributionPoint ::= SEQUENCE {
distributionPoint [e] DistributionPointName OPTIONAL,
reasons [1] ReasonFlags OPTIONAL, Input Size = 2 Bytes
cRLIssuer [2] GeneralNames OPTIONAL }
DistributionPointName ::= CHOICE {
fullName [9] GeneralNames,
nameRelativeToCRLIssuer [1] RelativeDistinguishedName }
Ratio = 0x20!!
fieldeffect.com
```

## Slide 26

## **Vulnerability Options**

- **`szOID_CRL_DIST_POINTS = “2.5.29.31”`**

-

-

-

fieldeffect.com 26

## Slide 27

## **Vulnerability Options**

- **`szOID_CRL_DIST_POINTS = “2.5.29.31”`**

- **`Certificate file`**

-

-

fieldeffect.com 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
Vulnerability Options
° szOID CRL DIST POINTS = “2.5.29.31” ee.
2_click.pfx
¢ Certificate file | dare you_
fieldeffect.com
27
```

## Slide 28

## **Vulnerability Options**

- **`szOID_CRL_DIST_POINTS = “2.5.29.31”`**

- **`Certificate file`**

- **`COM Interface`**

-

fieldeffect.com 28

## Slide 29

## **Vulnerability Options**

- **`szOID_CRL_DIST_POINTS = “2.5.29.31”`**

- **`Certificate file`**

- **`COM Interface`**

- **`SSL/TLS Network Connections`**

fieldeffect.com 29

## Slide 30

## **Reaching Via SSL**

- Certificate in SSL Handshake (client or server*)

- SSL Protocol message limit

   - 16MB

- Certificate Chain of Trust

- Retrieval of Missing Certificates

- Extensions: AIA, OCSP, CRL

fieldeffect.com 30

## Slide 31

## **SSL Object Retrieval**

fieldeffect.com

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
SL Object Retrieval
C++
C++
BOOL CryptRetrieveObjectByUr1w(
[in] LPCWSTR pszurl,
[in] LPCSTR pszObjectOid,
[in] DWORD dwRetrievalFlags,
[in] DWORD dwTimeout,
[out] LPVOID *ppvObject,
[in] HCRYPTASYNC hAsyncRetrieve,
[in, optional] PCRYPT_CREDENTIALS pCredentials,
[in, optional] LPVOID pwerify,
[in] PCRYPT_RETRIEVE_AUX_INFO pAuxInfo LPWSTR pwszCacheFileNamePrefix;
LPFILETIME pftCacheResync;
BOOL #ProxyCacheRetrieval;
DWORD dwHttpStatusCode;
LPWSTR *ppwszErrorResponseHeaders ;
PCRYPT_DATA_BLOB *ppErrorContentBlob;
Pa ra m ete rs } CRYPT_RETRIEVE_AUX_INFO, *PCRYPT_RETRIEVE_AUX_INFO;
typedef struct _CRYPT_RETRIEVE_AUX_INFO {
DWORD cbSize;
FILETIME *pLastSyncTime;
DWORD dwMaxUr1RetrievalByteCount;
PCRYPTNET_URL_CACHE_PRE_FETCH_INFO pPreFetchInfo;
PCRYPTNET_URL_CACHE_FLUSH_INFO pFlushInfo;
PCRYPTNET_URL_CACHE_RESPONSE_INFO *ppResponseInfo;
[in] pszUrl
The address of a PKI object to be retrieved. The following schemes are supported: M em bers
e Idap (Lightweight Directory Access Protocol) dwMaxUr1RetrievalByteCount
¢ http
© https (certificate revocation list (CRL) or online certificate status protocol (OCSP) A value that specifies a limit to the number of bytes retrieved. A value of zero or less specifies
retrievals only) no limit.
e file
fieldeffect.com
```

## Slide 32

## **CA Issuers**

```
CCertChainEngine::GetIssuerUrlStore()
{
    pAuxInfo->dwMaxUrlRetrievalByteCount = 100000;
}
```

fieldeffect.com 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
CA Issuers
X509v3 extensions:
X509v3 Authority Key Identifier:
9D:6E:82:D9:A6:69:4D:B2:CA:D1:8D:21:89:41:82:92:02:C2:C9:D4
X509v3 Basic Constraints:
CA:FALSE
X509v3 Key Usage:
Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment
X509v3 Subject Alternative Name:
DNS :DirectChild
Authority Information Access:
CA Issuers — URI:http://192.168.37.1:8080/intermediate.cer
CCertChainEngine: :GetIssuerUr1Store ()
{
pAuxInfo->dwMaxUrlRetrievalByteCount = 100000;
fieldeffect.com
```

## Slide 33

## **UserNotice Fuzzing**

fieldeffect.com 33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
UserNotice Fuzzing
aciehirteet
WinAFL 1.17 based on AFL 2.43b (FuzzX509.exe) © ts teat
+ eh ittettett
T= [PROCASS Tesla le) SSS +- overall results ----+ <thrttet
| run time : 1 days, 4 hrs, 12 min, 24 sec | cycles done : 40 sietets
| last new path : © days, 3 hrs, 37 min, 39 sec | total paths : 1833
| last uniq crash : none seen yet | uniq crashes : 0
| last uniq hang : none seen yet | uniq hangs : 90
+— cycle progress ———--————_-—-___-_--_— +- map coverage —+---------------------— +
| mow processing : 1370* (74.74%) | map density : 0.30% / 9.78%
| paths timed out : © (0.00%) | count coverage : 1.99 bits/tuple
+- stage progress + findings in depth
| now trying : arith 8\8 favored paths : 725 (39.55%)
_
| stage execs : 73.3k/611k (11.99%) new edges on : 997 (54.39%) . WY
total crashes : 0 (@ unique) ' WS ;
| total execs : 99.7M
|
|
| SS
| exec speed : 410.3/sec | total tmouts : 0 (0 unique) ; .
+- fuzzing strategy yields ----------- SSS +- path geometry : SY
| bit flips : 269/8.78M, 100/8.78M, 58/8.78M levels : 22 SS
|
byte flips : 3/1.10M, 5/248k, 4/279k | pending : 123 :
arithmetics : 331/12.5M, 7/3.09M, 5/488k | pend fav : 0 ~
known ints : 71/1.05M, 63/7.77M, 42/10.7M | own finds : 1832 .
| imported :
| stability
dictionary : 0/0, 0/0, 34/18.1M
havoc : 840/17.9M, 0/0
26 .07%/82.3k, 78.59%
fieldeffect.com 33
```

## Slide 34

## **OCSP Retrieval**

```
  pAuxInfo->dwMaxUrlRetrievalByteCount = 100MB;
```

fieldeffect.com 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FIELD EFFECT
OCSP Retrieval
X509v3 extensions:
X509v3 Authority Key Identifier:
39:31:A6:FC:DC:78:2B:B6:59:59:93:F1:BE:50:AB:EC:F5:1E:08:9F
X509v3 Basic Constraints:
CA: FALSE
X509v3 Key Usage:
Digital Signature, Non Repudiation, Key Encipherment, Data Encipherment
rity Information Access:
OCSP - URI:http://192.168.37.1:8080/ocsp
3.2 Signed Response Acceptance Requirements
Prior to accepting a signed response as valid, OCSP clients SHALL
confirm that:
1. The certificate identified in a received response corresponds to
that which was identified in the corresponding request;
2. The signature on the response is valid;
pAuxInfo->dwMaxUrlRetrievalByteCount = 100MB; 3. The identity of the signer matches the intended recipient of the
request.
4. The signer is currently authorized to sign the response.
5. The time at which the status being indicated is known to be
correct (thisUpdate) is sufficiently recent.
6. When available, the time at or before which newer information will
be available about the status of the certificate (nextUpdate) is
greater than the current time.
fieldeffect.com 34
```

## Slide 35

## **Dead End?**

- **`Compromised Intermediate CA (e.g. Comodo)`**

- **`Firewalls/Security Appliance Inspecting SSL`**

- **`Independently Manage CAs`**

fieldeffect.com 35

## Slide 36

## **Demo Setup**

CRL
DIST
Demo Setup
POINTS
X509
Certificate
100MB Max
OCSP
OCSP
16MB Max

fieldeffect.com 36

## Slide 37

## **CVE-2024-29050**

fieldeffect.com 37

## Slide 38

## **Exploitable?**

- Primitive is write of controlled data 2GB from allocation

Heap
NonPagedPool
Leaked Address Corruption Target

2GB

fieldeffect.com 38

## Slide 39

## **Exploitable?**

- Primitive is write of controlled data 2GB from allocation

- Misses will likely be swallowed by exception handler

- Opportunity for info leaks

- Sensitive data in LSASS, don’t need RCE to win

Heap

NonPagedPool

Leaked Address Corruption Target

2GB

fieldeffect.com 39

## Slide 40

## **Disclosure Timelines**

- **`CVE-2024-30020 – Time Stamp Response`**

- **`2023-12 – Found and reported to MSRC`**

- **`2024-02 – Vulnerability confirmed by MSRC`**

- **`2024-05 – Patch released`**

```
CVE-2024-29050 – CRL Distribution Points
```

- **`2023-09 - Reported to MSRC by VictorV with Kunlun Lab`**

- **`2023-12 – Found and reported by me to MSRC`**

- **`2024-02 – Vulnerability confirmed by MSRC`**

- **`2024-04 – Patch released`**

fieldeffect.com

40

## Slide 41

## **Thank you!**

- **eegsgard@fieldeffect.com**

- **@hexnomad@infosec.exchange**
