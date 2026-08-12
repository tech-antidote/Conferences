---
title: "Three New Attacks Against JSON Web Tokens"
speakers: ["Tom Tervoort"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Tom Tervoort_Three New Attacks Against JSON Web Tokens.pdf"
pages: 38
sha256: "e96ce24e0ec5c99fe6c8e1a9becdd0d648586308c02c1d0345f183bc2317f244"
text_chars: 16199
ocr_pages: 15
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:24:54Z"
---
# Three New Attacks Against JSON Web Tokens

**Speakers:** Tom Tervoort  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Tom Tervoort_Three New Attacks Against JSON Web Tokens.pdf` (38 pages)


## Slide 1

# Three New Attacks Against JSON Web Tokens

Tom Tervoort

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
AUGUST 9-10, ©0253
BRIEFINGS
Three New Attacks Against
JSON Web Tokens
Tom Tervoort
#BHUSA @BlackHatEvents
```

## Slide 2

### Speaker intro

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
WINNER BUREAU
Best Cryptographic Attack VERITAS
```

## Slide 3

### Outline

1. Background

   - Transferring identity claims

   - JSON Web Tokens

   - Prior attacks

   - Criticisms

2. New attacks

   - Sign/encrypt confusion

   - Polyglot token

   - Billion hash attack

3. Takeaways

#BHUSA @BlackHatEvents

## Slide 4

## Background

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
Background
#BHUSA @BlackHatEvents
```

## Slide 5

Transferring identity claims Classic (stateful) approach

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Transferring identity claims
Classic (stateful) approach
Whose token is this?
4EC72A4BFF14A8CB -
My token: >
4EC72A4BFF14A8CB
>
* N
Alice Name: Alice
Server E-mail: alice@example.com Claim store
Birthdate: ... (e.g. session DB
Registered devices: .... or IdP)
Member of groups: ...
```

## Slide 6

### Transferring identity claims Cryptographic approach

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Be Soe
Transferring identity claims
Cryptographic approach
My cryptographically
protected token:
K 1. Bo
Alice
Name: Alice Server
E-maitalice@example.ecom
Expiration date:
```

## Slide 7

### Comparison

**Stateful tokens Signed/encrypted claims** Many central DB lookups needed Fast to verify and easy to scale Mutable claims Claims fixed until expiration Trivially revocable No revocation before expire date Secrets are ephemeral Requires key management Token leak: compromise 1 user Key leak: compromise all users Easy to build, <u>given secure RNG</u> Involves complex cryptography

Common hybrid approach: cryptographic access token and stateful “refresh token”

#BHUSA @BlackHatEvents

## Slide 8

### Cryptography is hard

#BHUSA @BlackHatEvents

_Image sources: HackTricks, SEC Consult blog_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es3
Cryptography is
Sa i
Signedinfo
Ciphertext submitted by attacker
Decryption result (internal to server)
HTTP response send to attacker
9870d401a7d4b9£4c7c5728c980bb6d5
c546ad79e8a198440929c3cf£6£9ab793
'7465878dllde5a8bee5555554efcdb07
lexpire :1645826339090$u: user\ : arealm/bob%
1645826339090
%$m2ZQz+j4D0LL+z2W8EIEgtAxrcd6m0ZZi[...]
200 OK
9870d401a7d4b9£4c7c5728c980bb6d5
00000000000000000000000000000000
c546ad79e8a198440929c3cf6f£9ab793
'7465878d11de5a8bee5555554efcdb07
lexpire : 1645826339090$u: user\ :arealm/bob%
>! 91589 OOnOO [AvOOO10sO8Onnod
XBa@YOrBO1 Oi GO OO1w7 j POuOO2xqOd
$m2ZQz+j4D0LL+zW8EIEgtAxrcd6m0ZZi[...]
200 OK
9870d401a7d4b9f4c7c5728c980bb6d5
00000000000000000000000000000001
c546ad79e8a198440929c3cf£6£9ab793
'7465878d11lde5a8bee5555554efcdb07
lexpire : 1645826339090$u: user\ : arealm/bob%
EE Pd { OtxOHhO1 (P] SOnntOpOs' «! yaag
vntiges jeDonzvawenregeancedenor2i(,
$m22Qz+3j 4D0LL+zZW8EIEgtAxrcd6m0ZZi[.. - Lan
403 Access denied
Set-Cookie: LtpaToken2=""
Image sources: HackTricks, SEC Consult blog
Co-incidental percent sign
Attacker-controlled bitflip
```

## Slide 9

### JSON Web Tokens

- Massive improvement over legacy standards

- Proper integrity protection

- Easy to read and debug

- Simple and concise claims

- > 100 implementations

- Used by OpenID Connect

- **They’re everywhere**

#BHUSA @BlackHatEvents

_Image source: jwt.io_

## Slide 10

### Some JSON Web Acronyms

**JWT** (JSON Web Token): JSON-based claims format using JOSE for protection **JOSE** (Javascript Object Signing and Encryption): set of open standards, including: **JWS** (JSON Web Signature): JOSE standard for cryptographic authentication **JWE** (JSON Web Encryption): JOSE standard for encryption

**JWA** (JSON Web Algorithms): cryptographic algorithms for use in JWS/JWE **JWK** (JSON Web Keys): JSON-based format to represent JOSE keys

#BHUSA @BlackHatEvents

## Slide 11

### Prior JWT attacks

- Bypass signature validation by providing a token signed with the “ **none** ” algorithm

- Bypass blocklist filter with “ **nOne** ”…

- **Algorithm confusion** : using an RSA public key as an HMAC secret key

- **Key injection** /self-signed JWT: putting your own key in the “jwk” header

- Classic crypto attacks against primitives: RSA padding oracle; CurveSwap

- Probably most common: **simple dictionary words** being used as cryptographic keys

#BHUSA @BlackHatEvents

## Slide 12

Important design flaws (personal opinion)

1. Deciding the decryption/validation algorithm based on untrusted ciphertext

2. Letting end users choose between cryptographic algorithms

3. … including one broken since 1998 (RSA PKCS#1 v1.5 encryption) and “none”

4. Some algorithms are interchangeable, some dramatically change security properties

5. Over-engineered: trying to support many (obscure) use cases at once

#BHUSA @BlackHatEvents

## Slide 13

## New attack: sign/encrypt confusion

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
New attack:
sign/encrypt confusion
#BHUSA @BlackHatEvents
```

## Slide 14

### JWT flavors

||**Symmetric JWS**|**Asymmetric JWS**|**Symmetric JWE**|**Asymmetric JWE**|
|---|---|---|---|---|
|**Authenticity**|✔|✔|✔|❌|
|**Confidentiality**|❌|❌|✔|✔|

#BHUSA @BlackHatEvents

_Image source: Takahiro Kawasaki_

## Slide 15

### JWT flavors

||**Symmetric JWS**|**Asymmetric JWS**|**Symmetric JWE**|**Asymmetric JWE**|
|---|---|---|---|---|
|**Authenticity**|✔|✔|✔|❌|
|**Confidentiality**|❌|❌|✔|✔|

#BHUSA @BlackHatEvents

_Image source: Takahiro Kawasaki_

## Slide 16

### Should we expect developers to be crypto experts?

Not suitable for JWTs!
Fine for JWTs
Not suitable for JWTs!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
crypto experts?
fone ne ee 2-2-2 ------- fence e eee eee eee eee teneeeeee te---------------- +
| "alg" Param Value | Key Management | More | Implementation |
| | Algorithm | Header | Requirements |
| | | Params | |
fe ee eee e eee eee e eee fone e eee e eee e eee e ee teneeeeee tenene n-ne e eee +
| RSA1_5 | RSAES-PKCS1-v1_5 | (none) | Recommended- |
RSA-OAEP RSAES OAEP ( ) Re ded . .
| | default peraneters | | | | NOt Suitable for JWTs! is rsa oaep secure? xX & a
| RSA-OAEP-256 | RSAES OAEP using | (none) | Optional |
| | SHA-256 and MGF1 | | |
| | with SHA-256 | | | . .
| A128KW | AES Key Wrap with | (none) | Recommended | News Images Videos Books Maps Flights Finance
| | default initial | | |
| | value using | | |
| | 128-bit key | | |
| A192KW | AES Key Wrap with | (none) | Optional | About 140 re (0,39 secon
| | default initial | | |
| | value using | | | . 7 r r
| | 192-bit key | | | The RSA encryption algorithm is the most secure and widely used
| A2S6KW | AES Key Wrap with | (none) | Recommended | . : . : .
| | default initial | | | public key cryptographic algorithm. In this paper, we review RSA
value usin A . °
256-bit key | | algorithm and one most used padding scheme OAEP with RSA. RSAES-
| dir | Direct use of a | (none) | Recommended | . * . .
| | shared symmetric | | | OAEP protects RSA against semantical insecurity.
| | key as the CEK | | |
| ECDH-ES | Elliptic Curve | "epk", | Recommended+ | droress.or
| | Diffie-Hellman | "apu", | | press.org
| | Ephemeral Static | "apy" | | https://drpress.org » ojs » HSET > article > view PDF :
| | key agreement | | | . .
r | using Concat KDF | | | . ' An Overview of RSA and OAEP Padding - DRP
| ECDH-ES+A128KW | ECDH-ES using | "epk", | Recommended |
| | ECOH-ES using eg | eek: | || Not suitable for JWTs! @ sumuntenuresupeee «jh ee
| | wrapped with | "apy" | | ° : :
| | "A128KW" | | |
| ECDH-ES+A192KW | ECDH-ES using | “epk", | Optional |
| | Concat KDF and CEK | "apu", | |
| | wrapped with | "apy" | |
| | | | |
"A192KW"
```

## Slide 17

### What if we just avoid encrypted JWTs?

Key file:

JWT signer:

JWT validator:

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
"kty": "RSA",
"n": "sEFRQzskiSOruUYiaWAPUMF66Y0xWymrbf6PQqnCdnULa8PwI4kKDVI2XgNGg9X0dc - jRICmp
"e": "AQAB",
"d": "dsIr_P7WqUjNYEyIopFB4a2SKOhTWmQRrbk1GgJZUM1iZOmKub_kn303SLiKMBT8QuIDQHF
"p": "2ubPBIRKrNgC8TOMaim0fJpGa4ZTUcOwntIX4Rzb2IZLThHUFFeTq80GFRgcMTn1W54cqj zM
"q": "ZiBDoJVUNK7s -WDXlkr_69rxwL10r61183j C2BxV3g2xYOoybPj 7yvnXeMUDH8kfNTgPbZZ
"dp": "NzgJ-MW2YKuM8nNidFVPUDdKLEOgL3RnU2kEBRFWk- g8XdoOIWPBsEnzaJrWi-YqSfVa0w
"dq": "XOFm98YyImcsOxbrLj rvZPZMcLMcUIP8YZBp4-20t51d8EqvvDDZbNX1x0Kpj LoYyOhxVs
"qi": "1QH5d-TiaZL Q -NalMj3rFL8VILo031Tr0Qz6c1lp6pONoKOL7BCyosYSoORvainM3i7nv
authlib.jose jwt, JsonWebKey
time time
json
JWT Sj ner: open('rsa-key.jwk', 'r') keyfile:
Q . key JsonWebKey. import _key(json.load(keyfile) )
header = {'alg': 'RS256'}
payload {'iss': 'secure-issuer', ‘sub': username, ‘exp
token jwt.encode(header, payload, key) .decode()
round(time() )
authlib.jose jwt, JsonWebKey
sys, json
JWT validator: key 'rsa-key.jwk', 'r') as keyfile:
JsonWebKey.import_key(json.load(keyfile) )
claims jwt.decode(token, key)
username claims.validate()['sub']
```

## Slide 18

### What if we just avoid encrypted JWTs?

Key file:

**RSA JWK file usable for:**

   - **Signing**

- **Validation**

- **Encryption**

- **Decryption**

#### JWT signer:

JWT validator:

**Decides algorithm based on JWT header. Accepts RSA-encrypted JWE!**

#BHUSA @BlackHatEvents

## Slide 19

### Sign/encrypt confusion attack

##### **Preconditions:**

1. Library supports asymmetric JWTs

2. App uses JWS tokens with RSA or ECDSA (RS*/PS*/ES*)

3. Private key accessible by validation function

4. No specific algorithm or JWT wrapper type is enforced

5. Attacker can determine public key. E.g. by:

   - Reading it from OIDC endpoint **/jwks.json**

- If alg is RS*, can **compute it from two tokens** <u>(https://github.com/SecuraBV/jws2pubkey)</u>

#BHUSA @BlackHatEvents

## Slide 20

## New attack: polyglot JWT

#BHUSA @BlackHatEvents

## Slide 21

### A dangerous pattern

**What if library A and library B parse JWTs differently?**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
A dangerous pattern
1: JWT string 3: JWT string
Library A Library B
(JWT validator) Application (claims
processor)
ee ee
2: Validation result: ok/not okay 4: Authorization decisions
What if library A and library B parse JWTs differently?
```

## Slide 22

### Maybe exploit JSON ambiguity?

See also: <u>https://bishopfox.com/blog/json-interoperability-vulnerabilities</u>

#BHUSA @BlackHatEvents

## Slide 23

### Or an alternative serialization format?

#### **JWS Compact Serialization**

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsImlhdCI6M TUxNjIzOTAyMn0.rv61W60MY3WdNuyFrbDb31rcbBpfuYWoS4fOI6Mmjeg

#### **JWS Flattened JSON Serialization**

{ "protected":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9", "payload":"eyJzdWIiOiJhbGljZSIsImlhdCI6MTUxNjIzOTAyMn0", "signature":"rv61W60MY3WdNuyFrbDb31rcbBpfuYWoS4fOI6Mmjeg"

}

JWT spec requires compact, but some libraries pass the JWT to a general JWS parser that accepts either type

#BHUSA @BlackHatEvents

## Slide 24

### Library mismatch

**python-jwt** JWT validator (assumes compact)

**jwcrypto** JWS validator (first tries JSON; then compact)

#BHUSA @BlackHatEvents

## Slide 25

### A polyglot token

{ " **AAAA** ":". **XXXX** .", "protected": " **AAAA** ", "payload": " **BBBB** ", "signature": " **CCCC** " }

#BHUSA @BlackHatEvents

## Slide 26

### A polyglot token

**jwcrypto** ignored unknown JSON fields:

{ ~~"~~ **~~AAAA~~** ~~":".~~ **~~XXXX~~** ~~.",~~ "protected": " **AAAA** ", "payload": " **BBBB** ", "signature": " **CCCC** " }

#BHUSA @BlackHatEvents

## Slide 27

### A polyglot token

**python-jwt** split on periods, and ignored non-base64 characters:

{ header payload
" AAAA ":". XXXX .",
"protected": " AAAA ",
"payload": " BBBB ",
"signature": " CCCC "
}

Given a token with a legitimate payload, the attacker can replace it with any spoofed claims

#BHUSA @BlackHatEvents

## Slide 28

## New attack: billion hashes attack

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
New attack:
billion hashes attack
#BHUSA @BlackHatEvents
```

## Slide 29

### Some interesting JWE “alg” values

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
"A256KW" wrapping
| PBES2-HS256+A128KW | PBES2 with HMAC | "p2s", | Optional |
| | SHA-256 and | "p2c" | |
| | "A1l28KW" wrapping | | |
| PBES2-HS384+A192KW | PBES2 with HMAC | "p2s", | Optional |
| | SHA-384 and | "pac" | |
| | "A192KW" wrapping | | |
| PBES2-HS512+A256KW | PBES2 with HMAC | "p2s", | Optional |
| | SHA-512 and | "p2c" | |
| | | | |
+ + -
4.8. Key Encryption with PBES2
This section defines the specifics of performing password-based
encryption of a JWE CEK, by first deriving a key encryption key from
a user-supplied password using PBES?2 schemes as specified in
Section 6.2 of [RFC2898], then by encrypting the JWE CEK using the
derived key.
```

## Slide 30

### What can go wrong?

- Standard designer wants versatility: includes useful PBES algorithms

- Library implementer wants feature-completeness: implements all JWE algorithms

- • Library implementer wants simple and clean interface: same API for all algorithms

- • User decodes token with default settings, assuming these must be secure

- Result: application will try to decrypt JWTs claiming to be encrypted with a password, even though that doesn’t really make sense

- But if there’s no token spoofing cross-protocol attack between PBES and other algorithms this should not be a problem, right?

#BHUSA @BlackHatEvents

## Slide 31

### A PBES header parameter

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
A PBES header parameter
4.8.1.2. "“p2c" (PBES2 Count) Header Parameter
The "p2c" (PBES2 count) Header Parameter contains the PBKDF2
iteration count, represented as a positive JSON integer. This Header
Parameter MUST be present and MUST be understood and processed by
implementations when these algorithms are used.
The iteration count adds computational expense, ideally compounded by
the possible range of keys introduced by the salt. A minimum
iteration count of 10@@ is RECOMMENDED.
```

## Slide 32

### DoS with a token header

{ "alg": "PBES2-HS512+A256KW", "p2s": "AAAAAAAAAAAAAAAAAAAAAA", "p2c": 2147483647, "enc": "A128CBC-HS256" }

- Rest of the JWE can consist of bogus strings.

- • The server needs to perform more than **4 billion SHA512 hashes** to derive the token encryption key in before it can determine that this JWT is invalid.

- • **Unauthenticated** : attacker does not need to know what a valid token looks like.

- It has to do this for **every request** with a JWT!

#BHUSA @BlackHatEvents

## Slide 33

## Takeaways

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
Takeaways
#BHUSA @BlackHatEvents
```

## Slide 34

### JWT library research

- Focus on popular open source libraries. Could not cover all 100+ JWT libraries!

- • Vulnerabilities mainly found in highly featured libraries.

- Responsible disclosure very pleasant: fast and excellent response in each case

- • Vulnerabilities found and mitigations implemented in the following libraries:

|**Library**|**Language**|**Affected versions**|**Vulnerability**|**CVE**|
|---|---|---|---|---|
|Authlib|Python|< v1.1.0|Sign/encrypt confusion|CVE-2022-39174|
|JWCrypto|Python|< v1.4|Sign/encrypt confusion|CVE-2022-3102|
|JWX|PHP|< 0.12.0|Sign/encrypt confusion||
|Python-jwt|Python|< v3.3.4|Polyglot token|CVE-2022-39227|
|Jose|JavaScript|< v1.28.1, v2.0.5,
v3.20.3, v4.9.1|Billion hashes|CVE-2022-36083|
|Jose-jwt|.NET|< v4.1|Billion hashes||

#BHUSA @BlackHatEvents

## Slide 35

### Recommendations for JWT library developers

- Less is more: don’t implement features with rare use cases, or turn them off by default.

- Don’t use the “alg” parameter in the token to decide the algorithm. Instead force users to make this explicit in their code or key file.

- Don’t support JWTs using asymmetric or password-based encryption.

- Avoid validate-then-parse-again patterns.

#BHUSA @BlackHatEvents

## Slide 36

### Recommendations for the JOSE working group

- Specify security recommendations to avoid the issues discussed here.

- Explicitly list which JWS and JWE algorithms are allowed for JWTs. Exclude the likes of “none”, PBES and public key encryption.

- Encourage existing methods to enforce that a key is only used with a single algorithm.

- Ideally, remove “alg” from token headers altogether.

#BHUSA @BlackHatEvents

## Slide 37

### Recommendations for application developers using JWTs

- Reconsider if you really need encrypted claims. Boring old random tokens have

   - many advantages!

- Consider JWT alternatives like PASETO, Macaroons or Biscuits.

- When using JWT, always explicitly configure the validation algorithm.

- A JWT validation library is a critical dependency. Don’t forget to patch them!

#BHUSA @BlackHatEvents

## Slide 38

## Thank you!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
Thank you!
#BHUSA @BlackHatEvents
```
