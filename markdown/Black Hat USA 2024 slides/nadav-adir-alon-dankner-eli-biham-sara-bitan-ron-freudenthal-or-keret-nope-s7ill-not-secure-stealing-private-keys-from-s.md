---
title: "Nope, S7ill Not Secure Stealing Private Keys From S7 PLCs"
speakers: ["Nadav Adir", "Alon Dankner", "Eli Biham", "Sara Bitan", "Ron Freudenthal", "Or Keret"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Nadav Adir & Alon Dankner & Eli Biham & Sara Bitan & Ron Freudenthal & Or Keret_Nope, S7ill Not Secure Stealing Private Keys From S7 PLCs.pdf"
pages: 54
sha256: "e6e24c8d5742588b5b14e858aac1addc7c45a72bc8653e36662efbe5a43ecf2f"
text_chars: 17718
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:35:17Z"
---
# Nope, S7ill Not Secure Stealing Private Keys From S7 PLCs

**Speakers:** Nadav Adir, Alon Dankner, Eli Biham, Sara Bitan, Ron Freudenthal, Or Keret  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Nadav Adir & Alon Dankner & Eli Biham & Sara Bitan & Ron Freudenthal & Or Keret_Nope, S7ill Not Secure Stealing Private Keys From S7 PLCs.pdf` (54 pages)


## Slide 1

# **Nope, S7ill Not Secure: Stealing Private Keys From S7 PLCs**

<u>Nadav Adir, Eli Biham, Sara Bitan, Alon Dankner, Ron Freudenthal, Or Keret</u> Technion

#BHUSA @BlackHatEvents

## Slide 2

–
TLS 1.3 Iron clad armor

Stuxnet

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
USA 2024
blsekhat
&
‘e)
£
&
ae)
CS
a
oO |
e |
fe)
—
‘i.
oY
S|
W)
=)
=
```

## Slide 3

### **Cyber-Physical Systems**

- PLCs are the core of cyber-physical systems

- Ensure seamless operation of essential services, including

   - Electricity grids

   - Transportation control systems and more…

- Industry 4.0 transforms CPS

   - Transition from isolated air-gapped systems to cloud-connected environment

#BHUSA @BlackHatEvents

## Slide 4

### **Who are we?**

##### Alon Dankner

Nadav Adir

**Security Researcher** Technion **Security Researcher** Nokod Security

**B.Sc. Graduate** Technion

**Technion Cyber Lab has a plentiful history of exposing vulnerabilities in Siemens’ PLCs**

#BHUSA @BlackHatEvents

## Slide 5

**The PLC’s Structure and Interfaces**

Edition

TIA Portal HMI – SCADA

PLC S7-1500

S7 Protocol

WinCC

The Operator

Control Program Execution S7 Protocol

Engineering Station
Step7

The Engineer

The Attacker

#BHUSAThe Asset Owner@BlackHatEvents

## Slide 6

### **S7CommPlus Protocol**

- S7 is a proprietary protocol

- Designed to control and monitor the PLCs

- Examples: program download, PLC configuration, and read/write to PLC variables

- • Uses TLS 1.3 for secure communication

Client

PLC

#BHUSA @BlackHatEvents

## Slide 7

### **The Evolution of the S7 Protocol**

Unencrypted Protocol

Stuxnet (Anonymous) 2010

Self-Developed Cryptographic Protocol

Rogue7: Rogue The Race to Native Engineering-Station Code Execution in attacks on S7 PLCs Simatic PLCs (Keren) (Biham et al.) 2021 2019

Standard Protocol but Improperly Implemented

We are here

#BHUSA @BlackHatEvents

## Slide 8

### **Research Objective**

- Compare the version of S7 protected by TLS to the version protected by the self-

- developed protocol

   - Is it resilient to attack that the previous version was susceptible to?

   - Is it susceptible to attacks that the previous version was immune to?

- Threat model:

   - The attacker already has network access

- Any vulnerable device in the network can serve as an attack machine

#BHUSA @BlackHatEvents

## Slide 9

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 10

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 11

#### **S7 PLC Authentication Option 1: Use Initial Self-Signed Certificate**

PLC3
PLC2
Private Key
TIA
Public Key
Certificate Manager
Certificate
PLC1
PLC1 Cert1
PLC2 Cert2
PLC3 Cert3
#BHUSA
PLC2

#BHUSA @BlackHatEvents

## Slide 12

#### **S7 PLC Authentication Option 2: Use Key and Certificate Provisioned by TIA**

PLC3
PLC2
TIA
Certificate Manager
PLC1
PLC1 Cert1
PLC2 Cert2
PLC3 Cert3
PLC2

#BHUSA @BlackHatEvents

## Slide 13

### **PLC Hardware Configuration Download**

- The keys and certificates are part of the PLC hardware configuration

- The PLC configuration includes additionally

   - IP address

   - I/O modules

   - Other settings

Configuration Download Request

Response

Certificate Manager

#BHUSA @BlackHatEvents

## Slide 14

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 15

### **Traffic Interception and Decryption**

- A proxy on S7 communication

• Intercepts and manipulates messages between the client and the PLC

Certificate Manager

Request
Attacker’s Response

Attacker’s Request

Response

Technion’s Cyber Lab

#BHUSA @BlackHatEvents

## Slide 16

### **S7 Packet Sniffer**

- We implemented a packet sniffer

   - Standard TLS proxy tools do not support the S7 protocol stack

###### • Open-source

#BHUSA @BlackHatEvents

## Slide 17

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 18

### **PLC’s Key Provisioning**

- Certificate and private key are issued to the PLC by the TIA

   - Occurs if the customer chooses to create its own key

Configuration
Download Request
Response

Certificate Manager

#BHUSA @BlackHatEvents

## Slide 19

### **PLC’s Key Provisioning**

- Certificate and private key are issued to the PLC by the TIA

   - Occurs if the customer chooses to create its own key

Configuration
Download Request
Response
Certificate
Manager

#BHUSA @BlackHatEvents

## Slide 20

### **The S7 Configuration Download Protocol**

pk0
Client PLC
sk0
TLS 1.3 Handshake ClientHello cert0
pki
ServerHello,  cert0 , CertVerify, Finished
ski
Finished
certi
EncryptedSecretKeyi
Hardware Configuration Download Request
hash = SHA1(2, pki, certi.fingerprint)
EncryptedSecretKeyi , certi, hash, salt SHA1(2, pki, certi.fingerprint)  ≟ hash
ski = Dec_func(EncryptedSecretKeyi)
ClientHello pki
ski
New S7 Session ServerHello,  certi , CertVerify, Finished
certi
⋮
#BHUSA @BlackHatEvents

## Slide 21

### **The PLC Private Key Protection**

- We reverse-engineered the private key encryption process

   - It uses standard encryption algorithms

   - The private key is encrypted by a sequence of ephemeral keys

#BHUSA @BlackHatEvents

## Slide 22

### **Private Key Encryption**

“Hey Jarvis, encrypt the private key and make it as complex as possible”

“Right away sir, I’ll just use the TIA Portal”

#BHUSA @BlackHatEvents

## Slide 23

### **Private Key Encryption**

#BHUSA @BlackHatEvents

## Slide 24

### **Private Key Encryption**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat }
USA 2024 eA
a4
MIHSMFcGCSqGSIb3DQEFDTBKMCkKGCSqGSIb3DQEFDDACBAiOlv
DAYIKoZIhvcNAgkFADAdBglghkgBZQMEASoEEPsSUmHevSU4sfy
Rm&LRSUAYEgZDsIf T4bpX&zIBODeISFLFL?BKVH?3pVKyF JEuy #
CINNAQUHnaltmtUqyWDSshAU3TBavkOlojJEMRcirlqZSrGumy
xbr&yI+vtx@Bao+Z5+JeoTcdUpkmmSd4¥athByS8iFLKsyL+m/1Q
sO4r0o2X3vtUkULZH1cF SpY¥zyzyS5mCbb&2TRU+MeFeerFieLA3
TVbi0095DgvOv5i 3wrMBmsqMLk&wdU=cKbKbvdPh/Bla4gl11+
oSxp5VJd9Inb?fehxSGT?d?TFz2hCEzviEkMOrTWFeul DMSDKPUJBO
wh+KexwSiteey/wgmahg@IDA@ABAoIBACKSsAwuwbYuBIMdV==
o-=== END ENCRYPTED PRIVATE KEY-----
```

## Slide 25

### **Private Key Encryption**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
ephemera)
7 i gis Seg 000 aaehs de
ubl
Ephemeral pp; — RSA encry & Da Be
Private key pt A ny ,
encrypted passphrase — ©
4 *
Y a i fi
Pa
ar
cert I Bibie ate
encrypted private key
```

## Slide 26

### **Private Key Encryption**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat }
USA 2024
3
) Pe Ae
encrypted passphrase # ?
} =
encrypted private key
```

## Slide 27

### **Private Key Encryption**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat }
USA 2024 1
s. a 1 "
configuration to PLC ”
ten S
S?CommPlus Packet | '
ephemeral public ke - a EE hrasc cert fy
— encrypted &
salt
encrypted ephemeral private key
```

## Slide 28

### **Private Key Encryption**

#BHUSA @BlackHatEvents

## Slide 29

### **Private Key Encryption**

#BHUSA @BlackHatEvents

## Slide 30

### **The PLC Configuration Password**

- When the user creates a new TIA project, he can setup

- the PLC configuration password

- Complexity policy:

   - >8 characters, lowercase letter, uppercase letter, and a number

- If the user does not setup the password, a null string is

- used

#BHUSA @BlackHatEvents

## Slide 31

### **Provisioning the Configuration Password**

- The password is sent to the PLC on the first configuration download of the project

- In plaintext! (over TLS)

- Attacker can steal the password

#BHUSA @BlackHatEvents

## Slide 32

**Attack #1: Extracting the PLC’s Secrets During the Initial Key Provisioning**

- **Impact: The attacker can decrypt and modify all the PLC-TIA communication**

- The MITM intercepts the configuration password

   - and the encrypted TLS private key

- Since this is the first connection, TIA didn’t pin the certificate yet…

   - The user must trust the certificate which might be authentic or forged…

Configuration
Download Request
Certificate
Response
Manager

Configuration
Download Request
Response

#BHUSA @BlackHatEvents

## Slide 33

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 34

### **Attack #2: Rogue Client**

- **Impact: The attacker manipulates the PLC operation**

- We implemented a python script that impersonates a legitimate client

   - Exploits the lack of client authentication

   - Uses open-source libraries (in previous research we had to RE and implement the protocol)

- The attacker sends arbitrary control commands to the PLC

   - such as stop CPU, modify PLC configuration, or write to PLC variables

Attacker’s Request
Response

#BHUSA @BlackHatEvents

## Slide 35

### **Attack #3: PLC Private Key Retrieval**

- **Impact: Decrypts and modifies all the network traffic, at any time**

- Use the rogue client to send upload configuration request

- **The returned configuration contains the private key**

- The decryption process is identical to the one used in initial key provisioning attack

- • 𝐾𝑛𝑜𝑤𝑖𝑛𝑔𝑡ℎ𝑒𝑝𝑎𝑠𝑠𝑤𝑜𝑟𝑑→𝐾𝑛𝑜𝑤𝑖𝑛𝑔𝑡ℎ𝑒𝑝𝑟𝑖𝑣𝑎𝑡𝑒𝑘𝑒𝑦

Configuration
Upload Request
PLC Configuration
Encrypted Private Key

#BHUSA @BlackHatEvents

## Slide 36

### **Attack #1                      Attack #3**

**Initial Key Provisioning PLC Key Retrieval**

Must be performed during initial Can be performed any time <u>provisioning</u>

Attacker needs network access to both Attacker only needs access to the PLC PLC and TIA Can be performed if user hasn't setup a Can be performed if user hasn't setup a password password Can be performed if user has setup a If user has setup a password, the password attacker must know it

#BHUSA @BlackHatEvents

## Slide 37

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 38

### **Control Program Protection**

- TIA uses AES to encrypt the control program

   - The AES key is derived the from a random seed

   - The seed is encrypted under the hardcoded common PLC key

- The encrypted program and the encrypted seed are sent to the PLC over TLS

H AES Key Encrypts the Program
Seed
E E(Seed) Sent to the PLC

#BHUSA @BlackHatEvents

## Slide 39

### **Attack #4: Malicious Control Program Injection**

- **Impact: The PLC runs a malicious control program**

- The program transmission is susceptible to replay attacks

- The attacker creates a malicious control program in his own lab

   - and uses rogue client to download it to any PLC

#BHUSA @BlackHatEvents

## Slide 40

### **Attack #4: Malicious Control Program Injection**

- **Impact: The PLC runs a malicious control program**

- The program transmission is susceptible to replay attacks

- The attacker creates a malicious control program in his own lab

   - and uses rogue client to download it to any PLC

0xea1dadab = a bad 1dea

#BHUSA @BlackHatEvents

## Slide 41

### **Attack #5: Rogue PLC**

- **Impact: Impersonates a legitimate PLC and send forged status messages**

   - using the retrieved private key and certificate

- TIA does not show a warning message

   - Since the pinned certificate, issued to the extracted key, is used

Request
Attacker’s Response
Certificate
Manager

#BHUSA @BlackHatEvents

## Slide 42

### **Attack #6: A Stealth MITM Attack**

- **Impact: Stuxnet effect:**

- When the operator queries the PLC state

   - as the malicious program is running

- The MITM substitutes the real state with a forged healthy-looking state

   - displayed to the operators

- No warning message is presented to the user (as in Rogue PLC)

Certificate

Manager

State Request
Attacker’s Response ☺

State Request
Real Response 

#BHUSA @BlackHatEvents

## Slide 43

### **S7 Version Comparison**

**# Attack S7 w/o TLS S7 over TLS** Extracting PLC secrets during 1 X √ initial download 2 Rogue client √ √ 3 PLC private key retrieval X √ Malicious control program 4 X √ injection 5 Rogue PLC √ √ 6 A stealth MITM attack X √

#BHUSA @BlackHatEvents

## Slide 44

### **Stealth Man-in-the-Middle Attack Demo**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024 }
dirWINDOWS\RedirectDocuments\Automationvronmans_single_led_projectlronmans_single_led_project
Bel | IA Online Options Tools Window Help Totally Integrated Automation
x 2 cms 2G BA Ss coonline # PORTAL
Devices = Topology v th Network view |[¥ Device view
a 1 : i ¢ 4
a
Gojeyer asempaey [F
@@ PLC_1 [CPU 1512C-1 PN]
BY Device confgurati
&! Online & diag
Gal Wetch and force tables
Online backups
BH Trece:
HB OPC UA communication
GD Web applica 5
ik Device pre
28} Program info
SIEMENS
> [i Local module:
Iq Ungrouped devices
settings
ss-device functions
Gf Common data
E) Documentation settings
® Languages & resources . ——
a erson Zone toe a Properties __[Cii:infomal (d:Disonostics SIMATIC
Ww Online access General 10 tags System constants Texts S7-1500
3 Card ReaderlUS8 memory Hkarmeadaaaea
. Operating mode
[Detalis. view, » Advanced Interface networked with
Ethemet addresses
Subnet:
ana EU) Add new subnet
Di 16/DQ 16 [x12
Add new watch table ro 4 =
igh speed counters
Il Force table <akonte ten Internet protocol version 4 (IPv4)
Pulse generators (PT
133] Wetch table_1 it
aeup @ Set iP address in the project
cle
\size HY
Communication load U b " 7" ry *
fem and clark a Subnet mask ——— Sle
2 nemary 3 t 42 165.0178
IP address:
4. Portal viow ia ae cori lel caries on
```

## Slide 45

### **Password Stealing Demo**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lack hat
USA 2024
Li Ti A /.adinWINDOWS\RedirectiDocuments\Automation\ironmans_password_projectironmans_password_project Oracle VM VirtualBox
Totally Integrated Automatios
V17., a
>
Add new device
Devices & @ Show all devices
networks
Protection of confidential PLC data
Select your: ial PLC. data is tobe
@ Protection of
confidential PLC data Protection of confidential PLC configuration data activated:
= Cor PLC config date (e.g. OPCUA ) are pi in the TIA Portal
project and during runtime.
= If the PLC must be replaced with 8 replacement PLC, the password for the protection of
< PLC confi n data must also be assigned for the new PLC
Protection of confidential PLC configuration data deactivated:
- Confidential PLC configuration data (e.g. OPC UA certificates) are not protected in the TIA
Portal project and during runtime.
- No special password treatment when replacing the substitute PLC
faa Protects the PLC configuration data from the TA
Portal project and the PLC.
sword: | Pres: "Setup" to set the password
Setup
word TAproject
a
not show this dialog again Cancel
> Project view. Onened nrniect-\ectidinaday adi WINDOWS\Redirert\Docimente\Automatinnliranmans nas. \iranmans nasewnrd nroiect
```

## Slide 46

#BHUSA @BlackHatEvents

## Slide 47

### **Talk Roadmap**

Retrieving Extracting the Private the Traffic Key of a Private Key Interception Production A Stealth During Initial and Background PLC MITM Attack Provisioning Decryption on the S7 PKI

Summary and Mitigations

#BHUSA @BlackHatEvents

## Slide 48

### **Mitigations – ICS Customers**

- Set all three kinds of passwords supported by S7

1. PLC configuration password Password #1

Password #1

2. CPU access protection password Password #1Password #2

• that restricts access to privileged operations Password #2 Password #1 Password #3

Password #2

Password #1

• To use CA certificates Password #3 Password #2 Password #4

Password #3

3. TIA user password Password #2 Password #4 Password #3 Password #4

• To protect the control programPassword #3 Password #4

Password #4

4. Know-how protection password

- Passwords must be strong and unique per PLC

#BHUSA @BlackHatEvents

## Slide 49

### **Mitigations – Challenges**

- A huge number of strong and unique passwords is required

   - For all users and PLCs

- Clearly – unmanageable

- Therefore, users do not use them

- • Or set the same passwords on all PLCs • Thus, eliminating the security effect of these passwords

- • Protecting all those passwords is almost impossible

- Trusted CA does not help if the private key is exposed 

PLC1 Aa123456 PLC2 SoManyPassw0rds! PLC3 DontForgetPLC3 PLC4 NotSecure4Sure

#BHUSA @BlackHatEvents

## Slide 50

### **Siemens’ Response**

- We discloded our findings to Siemens about a year ago

- In order to mitigate the attacks, Siemens recommends customers to:

   - Perform initial provisioning in a secure environment

   - Use passwords!

#BHUSA @BlackHatEvents

## Slide 51

### **Mitigations – PLC Vendors**

###### **Implement full The private key mutual must not leave authentication the PLC**

**Avoid self-signed certificates for initialization**

###### **Use key exchange protocols**

Each party It should be authenticates the impossible to other party retrieve the private key from the PLC

Use vendor Don’t send the certificates instead key/passwords over the network

#BHUSA @BlackHatEvents

## Slide 52

### **The K7 Protocol**

- Countermeasure: a new security architecture

- Provides authentication and authorization

- Based on capability tickets

Biham, Eli, Bitan, Sara, and Dankner, Alon. **"K7: A Protected Protocol for Industrial Control Systems that Fits Large Organizations."** Sixth Annual Industrial Control System Security (ICSS) Workshop. 2020. <u>https://dl.acm.org/doi/abs/10.1145/3442144.3442149.</u>

Patent US 2022/0182229 A1

#BHUSA @BlackHatEvents

## Slide 53

### **A Message to the Customers**

###### **Demand Secure Products!!**

#BHUSA @BlackHatEvents

## Slide 54

## Thank you

Nadav Adir, Eli Biham, Sara Bitan, Alon Dankner, Ron Freudenthal, Or Keret

Technion

{nadav.adir,biham,sarab,dankner,ronf,or.keret}@cs.technion.ac.il

#BHUSA @BlackHatEvents
