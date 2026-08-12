---
title: "Breakin 'Em All Overcoming Pokemon Go's Anti-Cheat Mechanism"
speakers: ["Tal Skverer"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Tal Skverer - Breakin 'Em All Overcoming Pokemon Go's Anti-Cheat Mechanism.pdf"
pages: 61
sha256: "be047b65e1928eaedc899c30620acf6f03abe896dd15fa02c73f4bfd0f0d9c66"
text_chars: 23435
ocr_pages: 57
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.1
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:16:46Z"
---
# Breakin 'Em All Overcoming Pokemon Go's Anti-Cheat Mechanism

**Speakers:** Tal Skverer  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Tal Skverer - Breakin 'Em All Overcoming Pokemon Go's Anti-Cheat Mechanism.pdf` (61 pages)


## Slide 1

## Slide 2


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 The Release of Pokémon Go
```

## Slide 3


> Recovered by OCR — confidence 82/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
An Unexpected Journey
MELIVING -
```

## Slide 4


> Recovered by OCR — confidence 93/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
An Unexpected Journey
NEARBY
©)
```

## Slide 5

-

-

-

-

-


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
; What Did You Say Your Name Was?
¢ Tal Skverer
¢ Decade+ of Security Research
¢ Head of Security @ Astrix
« @taltechtreks.com
a @TalSkverer
fin} /in/reverser
@® iattechtrerscom 6 On stage at DEFCON 31, presented Google OAuth 9-day
¢ Automotive Hacking, Reversing Malware, Protocol Analysis,
Web Research, Identity Security
```

## Slide 6

## Slide 7

•

•


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Disclaimers
I'm speaking as an independent security researcher. My
views do not represent my employer.
Based on research from 9 years ago. Security has advanced
greatly, so the techniques shown no longer work today.
All materials presented are based on publicly-available
sources (reference in final slide)
```

## Slide 8


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Humble Beginnings
Request For
Pokémon Data
Nearby Pokémon
Pokémon Go
Server
```

## Slide 9


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sniffing Traffic
Detect automatically
Proxy
Manual
The HTTP proxy is used by the
browser but may not be used by the
other apps.
Use randomised MAC (--
CANCEL
```

## Slide 10


> Recovered by OCR — confidence 75/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sniffing Traffic
pgorelease.niantidabs.com /plfe/rpc Headers | TextView | SyntaxView | WebForms | HexView | Auth | Cookies TRaw
pgorelease.niantidabs.com /plfe/552/rpc h s: //paorelease. nianticlabs.com
pgorelease.niantidabs.com /plfe/552/rpc User-Agent: D : > U; Android 6.0.1; A0001 Build/MHC19Q)
pgorelease.niantidabs.com /plfe/552/rpc Content-Length: 1712
pgorelease.niantidabs.com /plfe/552/rpc s" "oo = ~ >
pgorelease.nianticdlabs.com /plfe/552/rpc
pgorelease.niantidabs.com /plfe/552/rpc
+w8g mr OOBbO ?%U
```

## Slide 11

## Slide 12


> Recovered by OCR — confidence 95/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Protobuf
Protocol Buffers
Protocol Buffers are language-neutral, platform-neutral extensible mechanisms for serializing structured data.
What Are Protocol Buffers?
Protocol buffers are Google's language-neutral, platform-neutral, extensible mechanism for serializing structured data - think XML, but smaller, faster, and simpler. You
define how you want your data to be structured once, then you can use special generated source code to easily write and read your structured data to and from a variety of
data streams and using a variety of languages.
```

## Slide 13


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Protobuf - Intro
message SearchRequest {
string query = 1;
int32 page_number = 2;
optional int32 results_per_page = 3;
optional repeated SearchOption search_options = 4;
search_request.proto search_request_pb2. py
```

## Slide 14


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Protobuf - Intro
import requests
import search_request_pb2
request = search_request_pb2.SearchRequest() protoc 2 Man Page
request.query = "Lord of the Rings Books"
request.page_number = 1 Protobuf compiler
request.results_per_page = 10
option1 = request.search_options.add() .
option1.key = "language" Examples (TL;DR)
Generate Python code from a . proto file:
option1.value = "english"
| protoc --python_out=path/to/output_directory input_file.proto
option2 = request.search_options.add()
option2.key = "sort_order" Decode a protocol message into raw tag/value pairs:
option2.value = “ascending protoc --decode_raw < message.bin
serialized_data = request.SerializeToString()
response = requests.post(
"https: //api.example.com/search",
data=serialized_data
```

## Slide 15


> Recovered by OCR — confidence 89/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Protobuf - Intro
: "Lord of the Rings Books",
4: {
1: "Language"
2: "English"
```

## Slide 16


> Recovered by OCR — confidence 80/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Analyzing Pokemon Go Protocol
3: 1764153216922026362
4{
1: 106
2: "\eee"
3: @x403f323200000000
}
: 126
2¢
1: 1467995033798
1: "4a2e9bc454dae60e7b74fc93b98868ab4700802e"
6 { 7: 0x403f323200000000
9: 0x403b083120000000
1: "\363\230\314..."
8: ©xc0546a8520000000 1: "provider
9: 0x403be83120000000 2: {
1S 1: “eyJhbGcioi..."
2: 2: 1751461009
1: "eyJhbGcioi..."
2: 1751461069 }
}
```

## Slide 17


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
status_code: 2
request_id: 1764153216922026362
requests: {
request_type: 106
request_bytes:
requests: {
request_type: 126
}
requests: {
request_type: 4
request_bytes:
}
unknown6: {
u6_unknown1: 6
u6_unknown2: {
u6_u2_unknown1_bytes:
}
}
latitude: 31.19607543945312
longitude: -81.66437530517578
accuracy: 27.031999588012695
auth_info: {
provider: "google"
token: {
content: "eyJhbGcidi..."
expiration: 1751461009
}
3
unknown12: 4590
Analyzing Pokemon Go Protocol
status_code: OK
request_id: 1764153216922026362
responses: {
response_bytes: —
}
responses: {
response_bytes:
}
responses: {
response_bytes: —-
```

## Slide 18


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Request Type: GET_MAP_OBJECTS
map_cell {
iA s2_cell_id: -8520171482234486784
Pidgey as_of_time_ms: 1467995224510
fort {
fort_id: "9feef60670b74df9871391b4b9e3ca24.16"
last_modified_ms: 1467338329663
Pidgeotto latitude: 35.72228384017944
longitude: 139.7710394859314
enabled: true
(ORMA fort_type: CHECKPOINT
spawn_point {
latitude: 35.72228384017531
longitude: 139.7710394859677
Rattata RMA }
—EE wild_pokemon {
encounter_id: 3736514205889371933
last_modified_ms: 1467995224510
Raticate JORN latitude: 35.72228384017914
—— longitude: 139.7710394859256
sSpawn_point_id: "167fb95d5c"
OR pokemon {
Spearow > 4 pokemon_id: 16
time_till_hidden_ms: 232574
RN }
Fearow ———— catchable_pokemon {
spawnpoint_id: "1502bffd46b"
encounter_id: 11920471590087242045
pokedex_type_id: 23
expiration_time_ms: 1467995429388
latitude: 35.72228384013804
longitude: 139.7710394524156
```

## Slide 19


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Pokemon Go's Protocol —
GET_MAP_OBJECTS
```

## Slide 20

•

•

•


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
) Creating a Pokescanner
Uses protobuf, the message is RequestContainer
Request type 106 fetches map details
Request needs a cell ID, responds with exact location
```

## Slide 21

•

•

•


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Creating a Pokescanner
Constructing aRequestContainer?
Dealing with unknown Fields?
Finding the Cell ID?
```

## Slide 22


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Creating a Pokescanner
Calculator
The S2 library defines a framework for decomposing the unit sphere into a hierarchy of cells. Each cell is
a quadrilateral bounded by four geodesics. The top level of the hierarchy is obtained by projecting the Latitude
six faces of a cube onto the unit sphere, and lower levels are obtained by subdividing each cell into four
children recursively. For example, the following image shows two of the six face cells, one of which has ao esti! e
been subdivided several times: oratories
-73.9932872
©
Kazakhstan
Level
S2 Cell ID
Indonesia Papua New
Guines
Copy S2 Cell ID
Open Google Maps
```

## Slide 23


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Creating a Pokescanner
def _get_auth_ticket(self, jwt_token): class GetMapObjects (object)
def _handle_response(self, response):
req_env = RequestEnvelop_pb2.RequestEnvelop()
req_env.status_code = 2
req_env.rpc_id = Utils.randomize_rpc_id() def get(self, Latitude, longitude, cell_ids)
get_map_objects_request = GetMapObjectsRequest_pb2.GetMapObjectsRequest ()
for cell_id in cell_ids:
get_map_objects_request.cell_id.append(cell_id.id())
get_map_objects_request.since_time_ms.append(0)
get_map_objects_request.latitude = latitude
get_map_objects_request.longitude = Longitude
request = req_env.requests.add()
request.request_type = Constants.GET_MAP_OBJECTS_REQUEST
req_env.auth_info.provider = "google"
req_env.auth_info.token.contents = jwt_token
req_env.unknown12 = 1036 self.request.requests[0].message = get_map_objects_request .SerializeToString()
data = self.request.SerializeToString()
raw_data = req_env.SerializeToString()
return NetUtil.request("POST", Constants.BASE_NIANTIC_URL, raw_data) return self._handle_response(NetUtil.request("POST", self.url, data))
def get_map_objects(self, Location):
neighboring_cell_ids = Utils.get_neighbors(location. latitude, Location. longitude)
new_request Yaw_request.requests.add()
new_request.request_type = RequestEnums_pb2.GET_MAP_OBJECTS
gmo = GetMapObjects.GetMapObjects(raw_request, self.url, self.logger)
```

## Slide 24


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Creating a Pokescanner
‘id': 46,
‘name': ‘Paras'},
9463615543@292253L: {'catchable': False,
47625@5547286647693L: {'catchable': False,
‘id': 19,
‘name': ‘Rattata'},
11732049240346098@13L: {'catchable': False,
‘id': 46,
‘name': ‘Paras'},
12680959522628632829L: {'catchable': True,
‘disappear': ‘Fri Jul 22 22:13:13
‘distance': 200.0,
‘time_till_hidden': 624.074},
16@58988752143383789L: {'catchable': False,
```

## Slide 25


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A Challenger Appears
PogoDev
Unofficial PokemonGO Development
A410 followers © Pallet Town @ https://pogodev.org
```

## Slide 26


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - lam
The First Hurdle
keyphact MOD PogoDev Administrator
PokemonGO Current API Status
Discussion
Hi all,
As many of you have noticed, many scanners and APIs have stopped working and IOS app clients are being forced to
update. The direct cause is unknown at this moment in time, but there are many people working to find a fix. It is not
just you. Everything except the unmodified updated app appears to be having issues.
I've stickied this thread for discussion so as to stop the “My API is not working” and influx of re-posted links and
discussions.
Chat is open again for all to read.
Please use: https://discord.gg/dKTSHZC
Updates
04/08/2016 - 00:49 GMT+1 : Logic and proto behind seem to have changed MapRequest, we're investigating.
```

## Slide 27


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - lam
The First Hurdle
public class NianticTrustManager extends ContextService implements X5@9TrustManager fi
private native void nativeCheckClientTrusted(x5e9Certificate[] x5e9CertificateArr, String str) throws CertificateException;
private native void nativeCheckServerTrusted(x509Certificate[] x5@9CertificateArr, String str) throws CertificateException;
private native x5@9Certificate[] nativeGetAcceptedIssuers();
public NianticTrustManager(Context context, long nativeClassPointer) {
super(context, nativeClassPointer) ;
}
@Override // javax.net.ssl.x509TrustManager
public void checkClientTrusted(x5e9Certificate[] chain, String authType) throws CertificateException {
synchronized (this.callbackLock) {
nativeCheckServerTrusted(chain, authType);
}
}
@Override // javax.net.ssl.x5@9TrustManager
public void checkServerTrusted(Xx5e9Certificate[] chain, String authType) throws CertificateException {
synchronized (this.callbackLock) {
nativeCheckServerTrusted(chain, authType);
}
```

## Slide 28


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HTTPs Proxy
Certificate a Certificate
General Details Certification Path General Details Certification Path
8 Normal HTTPS Flow show: [all>
Field Value
This certificate is intended for the following purpose(s):
ENCRYPTED = . RSA (2048 Bits) * Ensures the identity of a remote computer
a
* All issuance policies
s 0500
@)|Enhanced Key Usage Server Authentication (1.3.6.1.
Subject Key Identifier 436 15¢2533cb9892b le6dc54e8c6.
Server lel Basic Constraints Subject Type=CA, Path Length Co...
F |Key Usage Certificate Signing, Off4ine CRL Si
Issued to: DO_NOT_TRUST_FiddlerRoot
# Insert Proxy in the Middle
Issued by: DO_NOT_TRUST_FiddlerRoot
Valid from 16/
Copy to File... Install Certificate.
```

## Slide 29


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technique: Dynamic RE
Tal learned
Dynamic Reverse Engineering !
```

## Slide 30


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - lam
Bypassing Certificate Pinning
final Class NianticTrustManagerClass = lLpparam.classLoader.loadClass("com.nianticlabs.nia.network.NianticTrustManager") ;
x509Certificate[] cert = new X509Certificate[0];
findAndHookMethod(NianticTrustManagerClass, "“checkServerTrusted", cert.getClass(), String.class,
new CheckServerTrustedHook()
);
final String ORIGINAL_CHAIN = "...";
protected void beforeHookedMethod(MethodHookParam param) throws Throwable {
XposedBridge.log("Injecting Pokemon Go certificate trust chain");
byte[] buffer = Base64.decode(ORIGINAL_CHAIN, Base64.DEFAULT) ;
param.args[0 (x509Certificate[]) SerializationUtils.deserialize(buffer) ;
```

## Slide 31


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technique: Active Probing
Tal learned
Active Probirg!
```

## Slide 32


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 6am
Setting the Stage
message Unknowné {
int32 unknown1 = 1;
Unknown2 unknown2 = 2;
message Unknown2 {
bytes unknown1 = 1;
}
}
```

## Slide 33


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technique: Passive Analysis
Tal learned
Passive Analysis!
```

## Slide 34


> Recovered by OCR — confidence 78/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 19am
Initial Discoveries
{
\376b\ 250: \233\201=d\014\272\035\220\ 365] \265\277k\363\ \K\023\307Z\327qHB{ \013\251\223\300F\324\314:\332
\255\030\327|\3032 Q\301\250\016\225\221\022\213\277q\035\306\341\371\353N\304\325\3449\234\007S\310~\031
NBA
```

## Slide 35


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Android Apps - Intro
Android NDK
The Android NDK is a toolset that lets you implement parts of your class MyActivity : Activity() {
app in native code, using languages such as C and C++. For certain /**
types of apps, this can help you reuse code libraries written in those * Native method implemented in C/C++
languages. */
external fun computeFoo()
Get started
```

## Slide 36


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technique: Static RE
Tal learned
STATIC REVERSE ENGINEERING !
```

## Slide 37

## Slide 38


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technique: Static RE
R6, RO
SP, SP, m
R4, RI
tine
RS, SP, m +arrayl
RO, SP, +arrayl_end
R7,
LR, #
void *__tastcall sub _87444(char *input, int size)
if
time_t time; // r@
char *arrayl ptr_1; // r7
char *array2_ptr; // ri2
char *v8; // r1
char *array1_ptr; // r2
unsigned int current_array1_byte; // t1
char *input_after_header_ptr_or_current_input_block_ptr; // r1@
int v12; // ri
int v13; // r2
int v14; // r3
int final_size_without_header; // Ir
unsigned int final_size; // r7
void *result; // r@
int v19; // ri
int v20; // r2
int v21; // r3
char *v22; // r3
char *v23; // Ir
unsigned int current_block_start_index; // r11
char *current_input_block_ptr; // ri
char *array2_ptr_1; // r2
char current_array2_byte; // t1
char *v28; // r@
char array1[32]; // [sp+®h] [bp-249h] BYREF
char arrayl_end; // [sp+20h] [bp-229h] BYREF
char array3[256]; // [sp+21h] [bp-228h] BYREF
char array2[256]; // [sp+12ih] [bp-128h] BYREF
time = ::time(@);
srand48(time) ;
arrayl_ptr_1 = arrayl;
do
*+t+arrayl_ptr_1 = lrand48();
while ( array1_ptr_1 != &arrayl1_end );
array2_ptr = &array3[255];
```

## Slide 39


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 3pm
Pinpointing the Function
00200BC4
00200BC8
pthread_mutex_trylock
tan
-dynsym
3 time_t time(time_t *timer)
time
ADRL
LOR
Directio Type Address
R12,
PC, [R12,#(time_ptr -
```

## Slide 40


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
var sigEncryptFunctionPointer = nativeLibBaseAddress.add(0x87444) ;
console. log("Hooking sigEncryptFunction at offset: " + sigEncryptFunctionPointer) ;
Interceptor.attach(sigEncryptFunctionPointer, {
onEnter: function (args) {
console.log("Function 0x87444 entered! Parameters: " + args[0] + ", " + args[1]);
this.inputProtobuf = args[0];
this.inputProtobufSize = args[1].toInt32();
onLeave: function(retval) {
console.log("Function 0x87444 returned!");
2m on return and look at their values
(this.inputProtobufSize % 256)));
As an example, we saved some values into “this~* which allows us to retrieve them
cnange tn the stze Wtlt De Clearer
})
```

## Slide 41


> Recovered by OCR — confidence 80/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
1st day - 8pm
The sigEncryptFunction
2: 9588
4{
1: "network"
2: 8078
13: Ox41fe7a3e
14: @x420b2364
21: 0x42700000
26: 3
28: 1
54
2: "\@10\n\e17..."
4: "\@90\e00aa..."
5: "\@@@\000\000..."
6f{
8: "\@00\000\001..."
{
1: 6287
19: 3
{
1: “b79aba9100a15631"
2: “MSM8974"
3: "unknown"
4: “oneplus"
10: 285166495
478491093072
"\257\262\242..."
14:
"b79aba9100a15631"
"MSM8974"
"unknown"
```

## Slide 42


> Recovered by OCR — confidence 90/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
void sigEncryptFunction_87444(char xinput, unsigned int size) {
srand48(time(NULL) );
for (int i = 0; i < 32; i++)
iv_seed[i] = lLrand48() & Oxff;
memmove(input + 32, input, size);
memcpy(input, iv_seed, 32);
```

## Slide 43


> Recovered by OCR — confidence 89/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
void sigEncryptFunction_87444(char xinput, unsigned int size) {
srand48(time(NULL) );
for (int i = 0; i < 32; i++)
iv_seed[i] = lLrand48() & Oxff;
memmove(input + 32, input, size);
memcpy(input, iv_seed, 32);
```

## Slide 44


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
iv_seed[0:32] input[90:256 ] input[256:512] | input[512:790] | 90 | ten
size_remainder = 256 - size % 256;
final_size_without_header = size + size_remainder;
final_size = final_size_without_header + 32;
if (final_size_without_header > size)
{
memset(input + 32 + size, ©, final_size_without_header - size - 1);
}
input[totalsize - 1] = size_remainder;
```

## Slide 45


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
iv_seed[0:32] input[90:256 ] input[256:512] | input[512:790] | 90 | ten
for (int j = 0; j < 32; i++)
current_iv[32*i + j] = ((iv_seed[i] >> ((-i) & 7)) | (iv_seed[i] << i))
for (int current_block = 32; current_block < final_size; current_block += 256)
{
for (int i = 0; i < 256; i++)
input[current_block + i] “ current_iv[il;
encryption_9e9d8(input + current_block, block_encryption_output) ;
memcpy(current_iv, block_encryption_output, 256);
memcpy(input + offset, block_encryption_output, 256);
```

## Slide 46


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
iv_seed[0:32] input[90:256 ] input[256:512] | input[512:790] | 90 | ten
for (int j = 0; j < 32; i++)
current_iv[32*i + j] = ((iv_seed[i] >> ((-i) & 7)) | (iv_seed[i] << i))
for (int current_block = 32; current_block < final_size; current_block += 256)
{
for (int i = 0; i < 256; i++)
input[current_block + i] “ current_iv[il;
encryption_9e9d8(input + current_block, block_encryption_output) ;
memcpy(current_iv, block_encryption_output, 256);
memcpy(input + offset, block_encryption_output, 256);
```

## Slide 47


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
iv_seed[9:32] | encypted_block1 input[256:512] | input[512: 7990] | 90 | len
for (int j = 0; j < 32; i++)
current_iv[32*i + j] = ((iv_seed[i] >> ((-i) & 7)) | (iv_seed[i] << i))
for (int current_block = 32; current_block < final_size; current_block += 256)
{
for (int i = 0; i < 256; i++)
input[current_block + i] “ current_iv[il;
encryption_9e9d8(input + current_block, block_encryption_output) ;
memcpy(current_iv, block_encryption_output, 256);
memcpy(input + offset, block_encryption_output, 256);
```

## Slide 48


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
iv_seed[9:32] | encypted_block1 encypted_block2 | input[512:700] | 90 | len
for (int j = 0; j < 32; i++)
current_iv[32*i + j] = ((iv_seed[i] >> ((-i) & 7)) | (iv_seed[i] << i))
for (int current_block = 32; current_block < final_size; current_block += 256)
{
for (int i = 0; i < 256; i++)
input[current_block + i] “ current_iv[il;
encryption_9e9d8(input + current_block, block_encryption_output) ;
memcpy(current_iv, block_encryption_output, 256);
memcpy(input + offset, block_encryption_output, 256);
```

## Slide 49


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1st day - 8pm
The sigEncryptFunction
for (int j = 0; j < 32; i++)
current_iv[32*i + j] = ((iv_seed[i] >> ((-i) & 7)) | (iv_seed[i] << i))
for (int current_block = 32; current_block < final_size; current_block += 256)
{
for (int i = 0; i < 256; i++)
input[current_block + i] “ current_iv[il;
encryption_9e9d8(input + current_block, block_encryption_output) ;
memcpy(current_iv, block_encryption_output, 256);
memcpy(input + offset, block_encryption_output, 256);
```

## Slide 50


> Recovered by OCR — confidence 92/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
24 day - lam
Making Encryption Work
14171} int encrypt(const unsigned char *input, size_t input_size,
14172 const unsigned char* iv, size_t iv_size,
14173 unsigned char* output, size_t * output_size) {
```

## Slide 51


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
24 day - 9am
Decoding the Signature
message LocationFix {
string proider = 1;
uint64 timestamp_snapshot = 2;
float altitude = 4;
float Latitude = 13;
float Longitude = 14;
float speed = 18;
float course = 20;
float horizontal_accuracy = 21;
float vertical_accuracy = 22;
message DevicelInfo { uint64 provider_status = 26; 1 Ba 2 guirting/inc urate 3 fix acquired
string android_board_name 25
string android_bootloader Bs t
string device_brand = 4;
string device_model = 5;
string device_model_identifier = 6;
string device_model_boot = 7;
string hardware_manufacturer = 8;
string hardware_model = 9;
string firmware_brand = 10;
string firmware_tags = 12;
string firmware_type = 13;
string firmware_fingerprint = 14;
```

## Slide 52


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
24 day - 2pm
Decoding the Signature
message SensoriInfo {
uint64 timestamp_snapshot = 1;
double Linear_acceleration_x
double lLinear_acceleration_y = 4;
double Linear_acceleration_z = 5;
double magnetic_field_x = 6;
double magnetic_field_y = 7;
double magnetic_field_z = 8;
int32 magnetic_field_accuracy = 9;
double attitude_pitch = 10;
double attitude_yaw = 11;
double attitude_roll = 12;
double rotation_rate_x = 13;
double rotation_rate_y = 14;
double rotation_rate_z = 15;
double gravity_x = 16;
double gravity_y = 17;
double gravity_z 18;
int32 status = 19;
```

## Slide 53


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
24 day - 6pm
Decoding the Signature
message Signature {
repeated UnknownMessage field1 = 1; Ni re
uint64 timestamp_since_app_start = 2;
string field3 = 3; required
repeated LocationFix Location_fix = 4;
repeated UnknownMessage fieldS = 5;
repeated UnknownMessage field6 = 6;
repeated SensorInfo sensor_info = 7;
DeviceInfo device_info = 8;
UnknownMessage field9 = 9;
int32 field10 = 10;
bool field12 2
int32 field13 = 13;
int32 field14 14;
string field15= 15;
int32 field16 = 16;
string field17 = 17;
string field18 = 18; ( ]
bool field19 = 19; N requil
int32 field20 = 20;
bool field21 = 21;
bytes field22 = 22;
uint64 timestamp = 23;
repeated uint64 field24 = 24;
int6é4 field25 257 Not ]
int32 field27 ee
```

## Slide 54


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Identifying Missing Fields
(51 @® Reverse Engineering ~
PogoDev
@536 Online @ 19,846 Members
Latitude
| Longitude
| accuracy
Hash {field20}
```

## Slide 55


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
29 day - 11pm
Identifying Missing Fields
Latitude
[ auth_info | | Longitude
| accuracy
Hash Hash {field10}
```

## Slide 56


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
3° day - 4am
Who's This Hash?
status_code: 2
request_id: 1764153216922026362 [ request_bytes ]
requests: {
request_type: 106
request_bytes: —- ...
}
requests: {
request_type: 126
©x1B845328 xxHash64
field24[ ]
}
requests: {
request_type: 4
request_bytes: -——- ...
}
```

## Slide 57


> Recovered by OCR — confidence 86/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 3'¢ day - 7pm
The Final Field
| Hiantic
```

## Slide 58


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finale & Considerations
def _create_encrypted_signature(self, Latitude, Longitude, accuracy, data):
signature = Signature_pb2.Signature()
def
def
def
auth_ticket_hash = xxhash.xxh32(self.request.auth_ticket.SerializeToString(), seed=0x1B845238) .intdigest()
if not accuracy:
accuracy = "\x@e" * 8
self .hash_Location(auth_ticket_hash, d2h(latitude) + d2h(longitude) + d2h(accuracy))
signature.field20 = self.hash_location(0x1B845238, d2h(latitude) + d2h(longitude) + d2h(accuracy))
signature.timestamp_snapshot = 60000
signature.timestamp = int(time.time() * 1000)
return self._encrypt_with_lib(signature.SeriaLlizeToString())
_hash_location(self, seed, data):
return xxhash.xxh32(data, seed=seed) .intdigest()
_hash_auth(self, auth_ticket, data):
auth_ticket_hash = xxhash.xxh64(auth_ticket, seed=0x1B845238) .intdigest()
return xxhash.xxh64(data, seed=auth_ticket_hash) .intdigest()
_encrypt_with_lib(self, data):
encrypt_dLll = ctypes.
encrypt_dLL.argtypes
output_size = ctypes.
[ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_size_t)]
ctypes.c_int
output_size.value = len(data) + 32 + (256 - len(data) % 256)
output = (ctypes.c_ubyte * output_size.vaLlue) ()
ret = encrypt_dll.encrypt(data, len(data), "\x24" * 32, 32, ctypes.byref(output), ctypes.byref(output_size) )
return "".join([chr(x) for x in output])
```

## Slide 59


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Finale & Considerations
From 4th August 2016 - 00:49 GMT +1 until 7th August 2016 - 01:05 GMT +1, amazing things happened. A
community of Pokémon GO players from all around the world came together with the intention of restoring service
to the third-party PoGO API.
We were collectively known as Team Unknown6, due to the first unknown we tried to decrypt. The events which
followed during those three and a half days was nothing short of special, and unforgettable.
It was a lengthy battle of teamwork and effort to decrypt the U6 generation algorithm. The collaboration begun via
the PokémonGoDev sub-reddit and eventually spilled onto the Discord chat servers. Seamless collaboration begun
between highly experienced engineers, which lead to multiple wiki pages and Github repositories created to track and
pool together progress.
2067 Sig = Signature()
208
209 sig.session_hash = self.session_hash
210 sig.timestamp = get_time(ms=True)
211 sig.timestamp_since_start = get_time(ms=True) - RpcApi.START_TIME
212 if sig.timestamp_since_start < 5000:
213 sig.timestamp_since_start = random.randint(5000, 8000)
214
215|*** self._hash_engine.hash(sig.timestamp, request.latitude, request.longitude, request.accuracy, ticket_serialized, sig.session_hash, request.requests)
216 sig. location_hashl1 = self._hash_engine.get_location_auth_hash()
217 sig. location_hash2 = self._hash_engine.get_location_hash()
```

## Slide 60


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7 Finale & Considerations
```

## Slide 61

-

-

-

-

-

-

-

-


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
References
Team Unknown6 repository
Review of the hackathon
Arstechnia article on the hackathon
Reconstructed encryption repository
Hackathon updates Reddit Thread
PokemonGoXposed repository
Pgoapi repository
PogoProtos repository
```
