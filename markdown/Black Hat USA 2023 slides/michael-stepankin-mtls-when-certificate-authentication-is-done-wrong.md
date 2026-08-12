---
title: "mTLS When Certificate Authentication is Done Wrong"
speakers: ["Michael Stepankin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Michael Stepankin_mTLS When Certificate Authentication is Done Wrong.pdf"
pages: 33
sha256: "35da1f9138d39219dca710f81d6450d4955d97bd7c7cc8130d6164f9a9855219"
text_chars: 13654
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:19:29Z"
---
# mTLS When Certificate Authentication is Done Wrong

**Speakers:** Michael Stepankin  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Michael Stepankin_mTLS When Certificate Authentication is Done Wrong.pdf` (33 pages)


## Slide 1

### **mTLS: when certificate authentication is done wrong**

Michael Stepankin at Github Security Lab

@artsploit

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat
LUISA 2023 te
AUGUST 9-10, 20253
BRIEFINGS
mTLS: when certificate
authentication is done wrong
Michael Stepankin at Github Security Lab
we) @artsploit
```

## Slide 2

Intro: What is mTLS?

Attacks:

Agenda

Improper certificate extraction Follow the chain, where it leads you?

Revocation, what’s the hell?

Takeaways

#BHUSA  @BlackHatEvents

## Slide 3

- Client authentication during TLS handshake

##### What is mutual TLS?

- Based on providing X509 certificate, signed by trusted authority

- Server check public/private key possession of the client

#BHUSA  @BlackHatEvents

## Slide 4

##### TLS 1.2 mutual authentication

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
A 20e
TLS 1.2 mutual authentication
RFC 5246 TLS August 2008
Client Server
ClientHello ween nn >
ServerHello
Certificate*
ServerKeyExchange*
CertificateRequest*
<-------- ServerHelloDone
Certificate*
ClientkKeyExchange
CertificateVerify*
[ChangeCipherSpec ]
Finished 2 2 2 2 ween = >
[ChangeCipherSpec ]
<-------- Finished
Application Data <------- > Application Data
Figure 1. Message flow for a full handshake
```

## Slide 5

##### What is x509 certificate

$ openssl x509 -text -in client.crt Certificate: Data: Used to locate issuer’s certificate Version: 1 (0x0) Serial Number: d6:2a:25:e3:89:22:4d:1b Signature Algorithm: sha256WithRSAEncryption Issuer: CN=localhost Validity Not Before: Jun 13 14:34:28 2023 GMT Not After : Jul 13 14:34:28 2023 GMT Subject: CN=client Subject Public Key Info: The subject, aka "user name" Public Key Algorithm: rsaEncryption RSA Public-Key: (2048 bit) Modulus: 00:9c:7c:b4:e5:e9:3d:c1:70:9c:9d:18:2f:e8:a0:

#BHUSA  @BlackHatEvents

## Slide 6

**Client certificate** Subject: CN=Client **A path from end certificate to root CA** Issuer: CN=IntCA **formes a chain** PubKey: PubKeyClient Signature: <encrypted with PrivKeyInt> **Intermediate CA** Subject: CN=IntCA Issuer: CN=RootCA PubKey: PubKeyInt Signature: <encrypted with PrivKeyCA> **Root Certificate Authority** Subject: CN=RootCA Issuer: CN=RootCA PubKey: PubKeyCA Signature: <encrypted with PrivKeyCA>

#BHUSA  @BlackHatEvents

## Slide 7

##### mTLS setup: pros and cons

###### Pros:

- [Speed] Authorization happens only during TLS handshake, all “keep-alive” HTTP request are considered authenticated.

- [Storage] Similar to JWT, server does not store all clients certificates, only the root certificate.

###### Challenges:

- No granular control. If mTLS enabled, all requests have to be authenticated, even to "/static/style.css"

- Any certificate signed by trusted CA can be used to access this HTTP service. Even if the cert is issued for another purpose.

- No host verification by default, client cert is accepted from any IP.

- Certificate issuance should be implemented separately

- Certificates expire, so should be rotated frequently

#BHUSA  @BlackHatEvents

## Slide 8

##### Previous attacks on x509 validation

Weak signing algorithm

Parsing issues

Lack of Basic Constraints checks

MD5, SHA1

Memory corruptions while parsing X509 structures

End certificates should not be used to sign other certificates

#BHUSA  @BlackHatEvents

## Slide 9

## Chapter 1 Improper certificate extraction from the chain

#BHUSA  @BlackHatEvents

## Slide 10

##### How to use mTLS in Java Spring app

$ cat application.properties contains all trusted ROOT certificates … server.ssl.client-auth=need server.ssl.trust-store=/etc/spring/server-truststore.p12 server.ssl.trust-store-password=changeit … $ curl -k -v –cert client.pem http://localhost/hello contains client and intermediate certs

#BHUSA  @BlackHatEvents

## Slide 11

##### How to extract certificates from TLS session

// java X509Certificate[] certificates = sslSession.getPeerCertificates(); // java (another way) X509Certificate[] certificates = request.getAttribute("javax.servlet.request.X509Certificate");

// node.js let cert = req.connection.getPeerCertificate();

// python cert = self.connection.getpeercert(True)

// PHP $cert = $_SERVER['SSL_CLIENT_CERT']

Why java returns an array? Because the client send not a single certificate, but an array of certificates.

#BHUSA  @BlackHatEvents

## Slide 12

##### How to extract certificates in Java

X509Certificate[] certificates = sslSession.getPeerCertificates();

//way 1 is good String user = certificates[0].getSubjectX500Principal().getName();

//way 2 is dangerous for (X509Certificate cert : certificates) { if (isClientCertificate(cert)) { user = cert.getSubjectX500Principal().getName(); } }

RFC 5248 says that the sender's certificate MUST come first in the list.

The java TLS library only build a single verified chain from the array presented by the client, other certificates in the array can be self-signed.

#BHUSA  @BlackHatEvents

## Slide 13

##### Example: CVE-2023-2422 Improper certificate validation in KeyCloak

X509Certificate[] certs = null; ClientModel client = null; try { certs = provider.getCertificateChain(context.getHttpRequest()); String client_id = null; ... if (formData != null) { client_id = formData.getFirst(OAuth2Constants.CLIENT_ID); }

… matchedCertificate = Arrays.stream(certs) .map(certificate -> certificate.getSubjectDN().getName()) .filter(subjectdn -> subjectDNPattern.matcher(subjectdn).matches()) .findFirst();

Keycloak iterates over all certificates in the array, searching the one that matches client_id form parameter.

This creates a vulnerability, as only the first certificate's signature is checked by JDK.

#BHUSA  @BlackHatEvents

## Slide 14

CVE-2023-2422: Exploit chain **Client certificate** Issuer: CN=IntCA Subject: CN=Client1 PubKey: PubKeyClient Signature: <encrypted with PrivKeyInt> **Intermediate CA** Issuer: CN=RootCA Subject: CN=IntCA PubKey: PubKeyInt Signature: <encrypted with PrivKeyCA> **Self signed Client2 certificate** <u>Issuer:</u> <u>CN=Client2 Subject: CN=Client2</u> PubKey: PubKeyClient2 Signature: <self signed>

#BHUSA  @BlackHatEvents

## Slide 15

##### CVE-2023-2422: Keycloak exploit

Normal client authentication:

$ cat client1.crt client1.key > chain1.pem $ curl --tlsv1.2 --tls-max 1.2 --cert chain1.pem -v -i -s -k "https://127.0.0.1:8443/realms/master/clients-managements/register -node?client_id=client1" -d "client_cluster_host=http://127.0.0.1:1213/"

Now the exploit part, we generate a new self signed certificate and add it to the chain $ openssl req -newkey rsa:2048 -nodes -x509 -subj /CN=client2 -out client2-fake.crt $ cat client1.crt client1.key client2-fake.crt client1.key > chain2.pem $ curl --tlsv1.2 --tls-max 1.2 --cert chain2.pem -v -i -s -k "https://127.0.0.1:8443/realms/master/clients-managements/register-node?client_id=client2" -d "client_cluster_host=http://127.0.0.1:1213/"

#BHUSA  @BlackHatEvents

## Slide 16

##### CVE-2023-2422: How its fixed

Lesson: just extract the username from certs[0] and you’ll be fine

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA 20253
CVE-2023-2422: How its fixed
// Testing only 1st certificate in the chain to match with configured subject
x509Certificate certificate = certs[0];
boolean matchedCertificate = false;
if (clientCfg.getAllowRegexPatternComparison()) {
Pattern subjectDNPattern = Pattern.compile(subjectDNRegexp) ;
matchedCertificate = Arrays.stream(certs)
-map(certificate -> certificate.getSubjectDN().getName())
.filter(subjectdn -> subjectDNPattern.matcher(subjectdn) .matches())
.findFirst();
String subjectdn = certificate.getSubjectDN().getName();
matchedCertificate = subjectDNPattern.matcher(subjectdn) .matches();
Lesson: just extract the username from certs[0] and you'll be fine
```

## Slide 17

##### Another way to pass certificate: as a header

$ cat nginx.conf

http { server { server_name example.com; listen 443 ssl;

… ssl_client_certificate /etc/nginx/ca.pem; ssl_verify_client on;

The common scenario is to check the certificate on reverse proxy and forward it as an additional header without further validation.

Is not an ideal, as any other host from the same network can send a request with this header.

location / { proxy_pass http://host.internal:80; proxy_set_header ssl-client-cert $ssl_client_cert; } }

Also, it’s a neat target for HTML smuggling vulnerabilities on reverse proxies. E.g. CVE-2023-30589 or CVE-2021-33193.

#BHUSA  @BlackHatEvents

## Slide 18

Chapter 2 Follow the chain: where it leads you?

#BHUSA  @BlackHatEvents

## Slide 19

#### Meet Cert Stores

In large systems, servers may not store all Intermediate certificates locally.

They can fetched form a Certificate Store, defined in RFC 4387: Sample locations:

- HTTP URLs

- LDAP directory

- FTP URLS

- Databases

#BHUSA  @BlackHatEvents

## Slide 20

###### **Certificate “Insertion points”**

###### Properties that likely to be used during cert path building

**Client certificate**

Subject: CN=Client Issuer: CN=IntCA

Serial: 1337 Extensions:

- Subject Alternative Name

   - DNS: example.com

- Issuer Alternative Name

- Authority Information Access

Subject and Serial are good places to try SQL and LDAP injections. AIA and SIA extensions are perfect for SSRF attacks, albeit rarely supported.

   - caIssuers: <u>http://example.com/</u>

- Subject Information Access - caRepository: <u>http://example.com/</u>

- Subject Key Identifier: - key_id: 1337

These values are used to query Cert Store **before** the signature check

#BHUSA  @BlackHatEvents

## Slide 21

##### CVE-2023-33201: LDAP injection in Bouncy Castle

PKIXBuilderParameters pkixParams = new PKIXBuilderParameters(k eystore, selector); _//setup additional LDAP store_

X509LDAPCertStoreParameters CertStoreParameters = new

X509LDAPCertStoreParameters. Builder( "ldap://127.0.0.1:1389", "CN=certificates") .build(); CertStore certStore = CertStore. _getInstance_ ("LDAP", CertStoreParameters, "BC"); pkixParam s.addCertStore(c ertStore);

_// Build and verify the certification chain_ try {

CertPathBuilder builder = CertPathBuilder. _getInstance_ ("PKIX", "BC") ; = PKIXCertPathBuilderResult result

- ( PKIXCertPathBuilderResult) builder. build( pkixParams) ;

#BHUSA  @BlackHatEvents

## Slide 22

CVE-2023-33201: LDAP injection in Bouncy Castle

When LDAP CertStore is used, the server needs to find a certificate chain during validation.

**Client certificate** Subject: CN=Client Issuer: CN=IntCA PubKey: PubKeyClient Signature: <encrypted with PrivKeyInt>

So it makes a call to ldap://127.0.0.1:1389/CN=certificates With filter "&(cn=*Client*)(userCertificate=*))" The certificate’s subject is inserted to the query

#BHUSA  @BlackHatEvents

## Slide 23

CVE-2023-33201: LDAP injection in Bouncy Castle

**Client certificate** Subject: CN=Client*)(userPassword=123 Issuer: CN=IntCA PubKey: PubKeyClient Signature: <encrypted with PrivKeyInt>

Translates to the LDAP filter without escape: "&(cn=*Client*)(userPassword=123*)(userCertificate=*))" Which can be exploited as an LDAP injection vulnerability

#BHUSA  @BlackHatEvents

## Slide 24

###### CVE-2023-33201: How its fixed

Lesson: even when signed, some certificate fields are subject to injection attacks.

#BHUSA  @BlackHatEvents

## Slide 25

Chapter 3 Revocation, what's the hell?

#BHUSA  @BlackHatEvents

## Slide 26

###### Revocation

**Client certificate**

Subject: CN=Client Issuer: CN=IntCA Extensions:

- Authority Information Access - oscp: http://example.com/

- CRL Distribution Points - [ <u>http://example.com/</u> ]

- Certificate is checked for revocation by making a request to the URL specified **INSIDE** the certificate.

- Apart from HTTP, LDAP protocol is also supported

- This normally happens after signature check, but not always.

#BHUSA  @BlackHatEvents

## Slide 27

##### So, we can make a Java app to connect to a LDAP URL?

- Right, and java uses JNDI to access LDAP urls.

- URLS are taken CRDLP and OSCP extensions

- For JDK validator, "com.sun.security.enableCRLDP" should be set to "true"

- RCE via JNDI resolution fixed in CVE-2018-2633*

- Blind SSRF via HTTP still possible, but hardly exploitable

*https://mbechler.github.io/2018/01/20/Java-CVE-2018-2633/

#BHUSA  @BlackHatEvents

## Slide 28

##### Revocation support in Bouncy Castle

- Bouncy castle API also requires "org.bouncycastle.x509.enabl eCRLDP" set to "true"

- ● RCE in BC is sadly not possible, as it only fetches specific attributes with empty BaseDN

- HTTP SSRF still possible

#BHUSA  @BlackHatEvents

## Slide 29

##### CVE-2023-28857: Credentials leak in Apereo CAS

- Apereo CAS only verifies the date validity before checking revocation, the signature is not checked.

- Revocation checking on LDAP server can be enabled in the application.properties.

- A custom library is used for LDAP connection, so RCE is not possible.

- CRLDP extensions are supported

#BHUSA  @BlackHatEvents

## Slide 30

##### CVE-2023-28857: Credentials leak in Apereo CAS

- When processing a certificate, Apereo CAS uses LDAP address taken from the certificate, instead of one configured in properties.

- When connecting to LDAP server, it uses the same password that configured in properties.

- An attacker can leak this password by including its own LDAP address in the certificate and sending it in the header.

#BHUSA  @BlackHatEvents

## Slide 31

##### CVE-2023-28857: Fix

Lesson: it's generally dangerous to make requests to URLs taken from certificate fields.

#BHUSA  @BlackHatEvents

## Slide 32

#### Takeaways

- Pay attention when extracting usernames from client mTLS certificates, as the servers only verify the first certificate in the chain.

- Use Certificate Stores with caution, it can lead to LDAP and SQL injections.

- Certificate revocation can lead to SSRF, JNDI or even RCE in the worst case. Revocation should never be performed before signature validation.

#BHUSA  @BlackHatEvents

## Slide 33

# **Thank you**

@artsploit

The full writeup is available at https://gh.io/mtls-research

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blac
khat
LUISA 2023 —S
Thank you
it The full writeup is available at https://gh.io/mtls-research
#BHUSA @BlackHatEvents
```
