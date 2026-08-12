---
title: "Cryptography is hard Breaking the DoNex ransomware"
speakers: ["Gijs Rijnders"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Gijs Rijnders_Cryptography is hard Breaking the DoNex ransomware.pdf"
pages: 24
sha256: "7b8229efdfaea230d98196a9fa57accda868abbd21e770762cf1d5e4e3450d83"
text_chars: 13368
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:29:28Z"
---
# Cryptography is hard Breaking the DoNex ransomware

**Speakers:** Gijs Rijnders  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Gijs Rijnders_Cryptography is hard Breaking the DoNex ransomware.pdf` (24 pages)


## Slide 1

# **Cryptography is hard: Breaking the DoNex ransomware**

Gijs Rijnders 30-06-2024

## Slide 2

## **whoami**

- Malware reverse engineer

- CTI analyst

- Specialized in ransomware

- Finding & exploiting weaknesses to build decryptors/disrupt botnets

in/gijs-rijnders/ crysearch.nl

evolution536

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vx-underground
Your chances of being a victim of
ransomware increases over 250% if your
organization owns a computer.
Do not use computers.
[Reposted, apparently people didn't get
the joke]
Oss B77 4 dp;
@3: @2 2 1
```

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Month
04-2024
03-2024
02-2024
01-2024
12-2023
11-2023
10-2023
09-2023
08-2023
07-2023
06-2023
05-2023
#Victims claimed by Ransomware groups (total = 6839)
0
300 400 500
#Victims
T T T
200 600 700
T
100
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Donex ransomeware leakage
Home About Archives
mirel
Nous sommes votre partenaire en matiére de recrutement et de sélection. Nous nous déplacons sans en
gagement en entreprise afin de {... }
2024.02.27 Donex ransomeware leakage
Home About Archives
CHOCOTOPIA
Chocotopia is a center of entertainment in the heart of Prague. You can visit here Museum of Chocola
CHOCOTOPIA
and experience Chocolate {... }
Chocotopia is a center of entertainment in the heart of Prague.
You can visit here Museum of Chocolate and experience Chocolate
workshops, Wax museum of legends by Grévin, Candy shop, and
our Snack @ dessert bar.
elsa pspa Currently, our new Chocotopia Experience center is open and
looking forward for visitors, who are looking for unique adventure.
Da oltre 50 anni, Elsap é un’impresa dedita alla rappresentanza e alla distribuzione di componenti ele
onici ed elettromeccanici {... }
Website: www.chocotopia.cz
24.02.24
Total leaked:33GB
```

## Slide 6

## **How the cyber criminal plans it**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How the cyber criminal plans it
(1) Encrypts victim's
systems
(3) Victim negotiates with
cyber criminal
(4) Provides decryption
tool far victim
(2) Victim notified
Via ransom note
(3) Victim negotiates with
eyber criminal
(5) Victim restores files and
interaction with the cyber
criminal ends
nO
```

## Slide 7

**How we plan it**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
How we plan it
(1) Encrypts victim's
systems
(2) Victim notified
via ransom note
(3) Victim goes to
NoMoreRansom and
identifies ransomware strain
/> NOMORE RANSOM
; (5) Victim recovers files using
(4) NoMoreRansom provides free decryptor and does not
free decryption tool negotiate with cyber criminal
i «
```

## Slide 8

## **Building a decryptor**

- Implements inverse logic of ransomware

- Based on

- Cryptographic weakness

- Leaked decryption keys

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Building a decryptor a 4 x
File About
Decrypt files
- Implements inverse logic of ransomware Add directory
- Based on
. Remove directo
- Cryptographic weakness ry
- Leaked decryption keys Parameters
Threads 5 v
Start decryption
Encrypted file extension f58A66B51
Back Finish
```

## Slide 9

## **Distributing decryptors**

https://www.nomoreransom.org/en/index.html

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Distributing decryptors
Upload encrypted files here (size cannot Type below any email, website URL, onion or/and
be larger than 1 MB) bitcoin address you see in the RANSOM DEMAND.
Note: Be especially accurate with the spelling.
c_3 Choose first file from PC
4__ Choose second file from
—J pc
Or upload the file (txt or html) with the ransom note
left by criminals
Go! Find out
The general advice is not to pay the ransom. By sending your mon-
ey to cybercriminals you'll only confirm that ransomware works,
and there’s no guarantee you'll get the decryption key you need in
return.
EUR POL PY LITIE
Powered by:
powered by aWS iM Barracuda
https://www.nomoreransom.org/en/index.html
```

## Slide 10

**And now… DoNeX**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
And now... DoNeX
if ( CreateMutexA(®, 1, "CheckMutex") && GetLastError() == ERROR_ALREADY_EXISTS )
{
_loadd11(@);
(0x403338);
}
for ( i = 0; i < 0x21CQ; i += 64 )
{
*(__m128i *)&xml_config[i] = _mm_xor_si128((__m128i)xor_key_vector, *(__m128i *)&xml_config[il]);
*(__m128i *)&xml_config[i + 16] _mm_xor_si128((__m128i)xor_key_vector, *(__m128i *)&xml_config[i + 16]);
*(__m128i *)&xml_config[i + 32] _mm_xor_sil28(x*(__m128i *)&xml_config[i + 32], (__m128i)xor_key_vector) ;
*(__m128i *)&xml_config[i + 48] _mm_xor_si128((__m128i)xor_key_vector, *(__m128i *)&xml_config[i + 48]);
}
for ( ; i < @x21E7; ++i )
xml_config[i] “= @xA9u; -
config_ptr = maybe_parse_xm1l(@, (char)xml_config, (int) returns_2); Execute script
Snippet list Please enter script body
Name key =
. ea =
@ Decrypt config size =
patch =
decrypted = bytearray()
i range(size):
dec = get_wide_byte(ea + i) ~ key
decrypted. append(dec)
patch:
patch_byte(ea + i, dec)
(decrypted)
Line 1 of 1
& Line:1 Column:1
```

## Slide 11

## **The configuration**

- Ransom note

- Whitelisted files / directories

- Victim-specific options

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The configuration
- Ransom note
- Whitelisted files / directories
- Victim-specific options
?xuml version="1.6" encoding="UTF-8"7>
root>
<ewhite_extens>386; adv;ani;bat;bin;cab;cmd;com;cpl;cur
ewhite_files>bootmgr; autorun.inf;boot.ini;bootfont.bi
ewhite_folders>$recycle.bin;config.msi; $windows.~bt;$
¢kill_keep>sql;:oracle:mysq; chrome; veeam: firefox;excel
¢services>vss;sql:svc$:memtas:mepocs:msexchange; sopho
¢black_db>ldf;mdf</black_db>
<encryption_thread>30</eancryption_thread>
ewalk_thread>15</walk_thread>
élocal_disks>true</local_disks>
¢network_shares>true</network_shares>
¢kill_processes>true</kill_processes>
¢kill_services>true</kill_services=>
<shutdown_system>true</shutdown_system=>
¢delete_eventlogs>=true</delete_eventlogs>
écmd>wmic shadowcopy delete /nointeractive</cmd>
écmd>vssadmin Delete Shadows /All /Quiet</cmd>
¢content> 11! DoNex ransomware warning
Rot;hot;hot;&qt; Your data are stolen and encrypted
```

## Slide 12

**The Cryptography: key generation**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Cryptography: key generation
pointe
ryption_key = generates_secure_random_key( (HCRYPIPRUV]asavee
rsa_encrypts_buffer(random_encryption_key, 16
footer
params [1]
params[2] = retaddr;
if ( CryptAcquireContextA(params, @, @, lu, 0)
|| GetLastError() != -2146893802
(result
{
poBuffer =
hCryptProv;
= (char *)CryptAcquireContextA(params, ®, ®, lu, 8u)) !=@ )
(PBYTE)malloc(random_len) ;
memset (pbBuffer, ®, random_len);
if ( CryptGenRandom(params[@], random_len, pbBuffer) )
S
v4 =
if ( random_len > @ )
{
if (
{
v5
v6
do
{
(unsigned int) random_len >= 8 && unk_439E74 >= 2 )
v7
v8
_mm_cvtsi32_si128(6u) ;
_mm_cvtsi32_si128(0x1Fu);
_mm_cvtepu8_epi32(_mm_cvtsi32_si128(*(_DWORD x) &pbBuffer[v4]));
_mm_sra_epi32(
_mm_add_epi32(
(__m128i)_mm_shuffle_ps(
(__m128)_mm_mul_epi32(_mm_unpacklo_epi32(v7, v7), (__m128i)xmmword_4293F®0) ,
(__m128)_mm_mul_epi32(_mm_unpackhi_epi32(v7, v7), (__m128i)xmmword_4293F@) ,
221),
```

## Slide 13

**Following the trail**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Following the trail
6 xrefs to random_encryption_key
Direction | Tyr| Address | Text
encrypts_file_mode_1+203 push random_encryption_key
clears_event_logs_and_s... mov eax, random_encryption_key
clears_event_logs_and_s... mov random_encryption_key, 0
extract_config_and_prep... mov random_encryption_key, eax
encrypts_local_file+37C push random_encryption_key
FileW = CreateFileW(1lpNewFileName, @xC0000000, @, @, OPEN_EXISTING, @x8@u, 0);
Line 1 of 5 if ( FileW != (HANDLE)-1 )
{
Size = 0;
v16 = (unsigned __int64)(file_size.QuadPart / (unsigned int)number_of_blocks) >> 3
v16;
file_size.QuadPart / (unsigned int)number_of_blocks;
LpNewF i Lehaces CEC iii, PAIRG4S_(V16, V22)) >> 3
peer = 1 * v22;
SetFilePointer(FileW, i * v22, (PLONG)&lpNeWGileName, @);
ReadFile(FileW, \pBuffer, read_block_size, S&NijnberOfBytesRead, 2);
salsa20_encrypt({intrandom_encryption_key, 1// &v20, 0, (int) lpBuffer, read_block_size);
SetFilePointer(FileW, v18, (PLONG)&lpNewFildName, 0);
fem, pBuf fer;
Writer 1 (6}MEtehpapietierperead_olock_size, S&NumberOfBytesRead, @);
v16 = v21;
i = Size + 1;
Size = i;
» ( i < number_of_blocks );
ointerEx(FileW, file_size, ®, ®);
ile(FileW, pointer_to_footer, ®x200u,/&NumberOfBytesRead, 0);
Handle(Filew) ;
ransom_note( lpFileName) >
( v19 )
j___free_base(v19);
```

## Slide 14

**The encryption function**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
unsigned int __cdecl salsa2@_schedule_32(int a1, int a2, int a3)
{
int v3; // esi
int v4; // edi
e e
The encryption function iam te io
int v6; // ecx
int v8; // edx
__int64 *nonce_ptr, int v9; // edi
unsigned int a4, char v10; // al
PBYTE buffer, int v11; // esi
int buffer_length) int v12; // edx
int v13; // ecx
void *key_schedule_proc; // edx int v14; // eax
PBYTE v7; // eax int v15; // edx
unsigned int v8; // ebx int v16; // edx
int v9; // edi unsigned int v17; // ecx
BNE sp UI) GES unsigned int result; // eax
nis WS OS int v19[16]; // [esp+Ch] [ebp-90h]
BYTE *v12; // ecx : c
char keystream[64]; // [esp+@h] [ebp-50h] BYREF int v20[16]; // [esp+4Ch] [ebp-50h] BYREF
__int64 nonce_int64; // [esp+4@h] [ebp-10h] BYREF int state[4]; // Lesnsechl fehn-10h] BYREF
__int64 v16; // [esp+48h] [ebp-8h] ;
void *use_128_bita; // [esp+5Ch] [ebp+Ch] qmemcpy(state, “expand 32-byte k", sizedf(state));
PBYTE buffera; // [esp+68h] [ebp+18h] v3 = a3 Pel;
onsen SENEELO_SaneetNe se unsigned int __cdecl salsa2@_schedule_16(char *a1, int a2, int a3)
key_schedule_proc = 0; { . .
v16 = Q@LL; int v3; // esi
if ( use_128_bit == 1 ) int v4; // edi
key_schedule_proc = salsa20@_schedule_16; unsigned int v5; // kr00_4
use_128_bita = key_schedule_proc; _BYTE «v6; // edx
if ( !key_schedule_proc ) char *v7; // ecx
return 1; int v8; // esi
if ( !encryption_key ) char v9; // al
return 1; 7 ‘ .
. int v10; // esi
if ( !nonce_ptr ) int v11; // edi
return 1; a ’
of) so SOGEe int v12; // edx
if ( ‘buffer ) int v13; // ecx
return 1; int v14; // eax
v8 = a4; int v15; // edx
nonce_int64 = *nonce_ptr; int v16; // edx
if ( (a4 & 0x3F) !=@ ) unsigned int v17; // ecx
{ unsigned int result; // eax
LOBYTE(v16) = a4 >> 6; int v19[16]; // [esp+Ch] [ebp-90h]
ae ae) at >> ui int v20[16]; // [esp+4Ch] [ebp-50h] BYREF
u Ge > ey i | eileen re Samene1 0)
BYTES 016) nanedioeaaa: int v21[4 =F ‘ h] BYREF
((void (__cdecl *)(PBYTE, _€nt64 *, char *))key_schedule_proc) (encryption_key, &nonce_int64,
v7 = buffer;
qmem€py(v21, “expand 16-byte k", sizJof(v21));
```

## Slide 15

**Salsa20 or ChaCha20?**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Salsa20 or ChaCha20?
#include <stdint.h>
#define ROTL(a,b) ( << (b)) | ((a) >> (32 - (b)))) int __cdecl salsa2@_key_expansion(_DWORD +a1)
#define QR(a, b, \ {
b *= ROTL(a \ int result; // eax
‘ a sorte \ al[4] *= _ROL4 (al + a1[#2], 7);
= s a1[8] *= __ROL4__(al1[4] + *41, 9);
1
a *= ROTL(d
#define ROUNDS 20
a1[12] *= _ROL4__(a1[8] + 91[4], 13);
*al “= _ ROR4__(a1[12] + a1][8], 14);
ai[9] *= _ ROL4_(a1[5] + a1\1], 7);
a1[13] *= _ ROL4__(a1[9] + a1], 9)3
ai[i] *= _ ROL4__(a1[13] + a1l[9="%3);
a1[5] *= __ROR4__(a1[1] + a1[13], 14);
ail
The constant is the same as Salsa20 ("expand 32-byte k"). ChaCha replaces the Salsa20 quarter-round 14] “= _ ROL4._(al[i0] + a1l6], 7);
QR(a, b, c, d) with: a1[2] *= _ROL4__(a1[14] + a1[10], 9);
a1[6] *= _ ROL4__(a1[2] + a1[14], 13);
a1[10] “= __ROR4__(a1[6] + a1[2], 14);
a1[3] *= _ ROL4__(a1[15] + a1[11], 7);
Dole CS op a1[7] *= _ROL4_(a1[3] + a1[15], 9);
c t= d; b “= c; b < a1[11] *= _ ROL4_(a1[7] + a1[3], 13);
a += b; d *= a; d result = _ ROR4__(a1[11] + a1[7], 14);
c t= d; b *=c; b a1[15] “= result;
return result;
```

## Slide 16

**Key in global variable, nonce is zero…**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Key in global variable, nonce is zero...
xxd -l 178 oh@tkz. xD
Babeeeee:
Baeeee18:
BaBG80208:
BaBBBOSB:
Baeaeae4B:
Baeeee58:
B8GG8068:
Baeeee78:
ed97
Bd43
aohe,
8339
2765
35c8
ec?3
3674
e2de
7726
84bb
a23at
d38c
578f
af Ba
78ce
5249 WAb6
2542 g2at
bied chaz
B7Bc 1576
bBf? 7259
Bfba 78e9
bS57 9e46
4567 B821T
F5BA66B51
2236
dva2
fa4b
bb?t
Bde5
7F38
1d65
ebeb
--.-RI.V"S[..
ae
xxd -1l 12B8eefheck.xlsx7RGQBA66B51
BBBBRBRBE
BeBBBE18
BeBBBE2e:
BBBBBE38:
BABBBE48:
BeB88G5e:
BeBB8R6E:
BeeBBa7e:
ed97
Bd43
5 Doe
8339
2T65
35c8
ec93
3674
e2de
7726
OS hbk
a23f
d38c
578f
afB4
78c8
5249
2542
208
87Be
bat?
&fba
bB5?7
4567
fA56
d2at
eBa2
1578
7259
28e9
9046
B21f
2236
d7va2
fa4b
bbof
Bde5
7F308
1d65
efea
eee AL VS 22.7.
```

## Slide 17

## **Stream ciphers & re-using key material**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Stream ciphers & re-using key material
Key + Nonce
Plaintext File
|
Keystream Encrypted File
J__y
Generator
Keystream
```

## Slide 18

## **The XOR operation**

A B A xor B
0 0 0
1 0 1
0 1 1
1 1 0

## Slide 19

## **Recovering the keystream**

https://en.wikipedia.org/wiki/Known-plaintext_attack

## Slide 20

## **In practice, it’s not that easy**

**File Size Encrypted** < 1MiB Entire file <10MiB First 1MiB <100MiB 5 blocks of 1MiB >100MiB 100 blocks of 1MiB

## Slide 21

**Input file constraints**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Input file constraints
Filew = teF ileW( LpNewFileName, 0000000, 8, @, OPEN_| STING, Qu, @);
if ( FileW != (HANDLE)-1 )
{
Size = 0;
v16 nsigned __int64)(file_size.QuadPart / (unsigned int)number_of_blocks)
v21 v16;
v22 = file_size.QuadPart / (unsigned int)number_of_blocks;
(LPCWSTR)((i * __PAIR64__(v16, v22)) >> 32);
i (FileW, i * v22, (PLONG)&lpNewFileName, @);
(FileW, LpBuffer, read_block_size, SNumberOfBytesRead, @);
Saleaee encrypt ((int))random_ encryption_key, 1, &v20, ®, (int) lpBuffer, read_block/size);
(FileW, v18, (PLONG) &pNewFileName, a);
v19 = = ipputfer;
ileW, lpBuffer, read_block_size, S&Number0fBytesRead, 9);
i = Size + 1;
number_of_blocks );
: (FileW, file_size, @, @);
FileW, pointer_to_footer, 0x20@u, &NumberOfBytesRead, 0);
(Filew);
writes_ransom_note( 1pFileName) ;
if ( v19 )
j__free_base(v19);
```

## Slide 22

**Putting it all together**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Putting it all together
>» DoNexDecrypt - 0 x
File Options Help
Decrypt files
C:\Users \user\ Downloads test \Set 1\Encrypted ;
C:\Users\user\Downloads\test \Set2\Encrypted Add directory
Remove directory
Parameters
Encrypted file extension f58A66B51
Start decryption
Back Finish
```

## Slide 23

Meme from Dynexo GmbH

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The server has infected by ransomware
Where is backup?
On the server
>.
Meme from Dynexo GmbH
```

## Slide 24
