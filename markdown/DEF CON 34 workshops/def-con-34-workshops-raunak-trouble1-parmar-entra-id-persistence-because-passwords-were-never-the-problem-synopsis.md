---
title: "Entra ID Persistence - Because Passwords Were Never the Problem - Synopsis"
speakers: ["Raunak 'Trouble1' Parmar"]
conference: "DEF CON"
conference_full: "DEF CON 34"
year: 2026
source_type: "workshop-materials"
source_dir: "DEF CON 34 - Workshops - Raunak - Trouble1 - Parmar-Entra ID Persistence - Because Passwords Were Never the Problem - Synopsis"
files_included: 1
files_skipped: 0
text_chars: 16626
redacted_secrets: 0
sha256: "f0d4373c822881559690f5db04475e1051c7e92e3e69e278349fd21b3d5c6945"
converted_at: "2026-08-12T07:17:47Z"
---

# Entra ID Persistence - Because Passwords Were Never the Problem - Synopsis

**Speakers:** Raunak 'Trouble1' Parmar  
**Conference:** DEF CON 34 (workshop materials)  
**Contents:** 1 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Materials

### `DEF CON 34 - Workshops - Raunak - Trouble1 - Parmar-Entra ID Persistence - Because Passwords Were Never the Problem - Synopsis.md`

```markdown
# Persistence in Microsoft Entra ID
## Workshop Synopsis

---

## The one-line pitch

A three-hour, live-tenant workshop where every participant plays the adversary  planting real identity-layer backdoors inside an isolated Microsoft Entra ID tenant, then watching the standard incident response playbook fail against them.

---

## Enhanced Abstract

Enterprise security has moved off the network and onto identity. In 2026, if you own a tenant's identity plane, you own the tenant  and the techniques for owning it durably look nothing like the persistence tradecraft security teams were trained to hunt. Password resets, MFA enforcement, and full session revocation  the actions every IR runbook lists  leave the most valuable classes of Entra ID persistence completely untouched.

This workshop is the operator's field manual for that gap. Across eight hands-on labs and one full-length capstone exercise, participants execute the current, in-the-wild techniques adversaries use to embed themselves inside Microsoft Entra ID after initial compromise  from the classic (service principal credential injection) to the modern (workload identity federation on managed identities, secondary token-signing certificate injection, hidden-membership administrative units).

Every technique is:
- **Performed live** by the participant against their own isolated lab tenant  not demonstrated by the instructor.
- **Tested against remediation**  after planting the anchor, participants simulate the IR actions a defender would take and observe which anchors survive and which do not. This "Break-It / Validate-It" cycle is where the workshop's core lesson lands.
- **Mapped to detection**  for every attack, we cover the exact audit-log event, sign-in-log signal, or configuration-state check that a defender would need to catch it. This is a workshop for red teams, blue teams, and cloud architects in the same room.
- **Grounded in publicly documented tradecraft**  the labs are direct implementations of research published by Datadog Security Labs, Tenable, Semperis, SlashID, Dirk-jan Mollema, and other well-known cloud identity researchers. Nothing is invented for effect; everything is representative of what defenders actually face.

Participants leave with a **layered persistence portfolio**  a set of anchors chosen so no single defender action ends their access  and the mental model to reason about which combinations are truly resilient versus theatrical. Defenders in the room walk out with an audit-log priority list, a configuration-state audit checklist, and a working understanding of why "we rotated all the secrets" is not remediation.

---

## What makes this workshop different

**Identity as the attack surface  not endpoints, not networks.**
Most cloud security workshops still lead with the shared-responsibility model, network segmentation, and CSPM findings. This one starts and ends with identity because that is where the durable compromise happens.

**Hands-on validation of every assumption.**
We do not tell you a technique survives password reset. You plant the anchor, we reset the password, and you watch it keep working. Every module ends with the participant proving  or disproving  the persistence claim themselves.

**Direct relevance to production tenants.**
The techniques covered map to real configurations used in production Entra tenants  federated identity credentials, administrative units, cross-tenant access settings, certificate-based authentication trust stores. These are not edge cases or research toys. They are shipping features whose abuse patterns are documented in current public research.

**Bridges the offense-defense gap.**
Every lab has a defender view  the audit event, the hunt query, and the configuration-state check. Defenders leave with something to deploy on Monday. Operators leave knowing exactly which of their anchors will be caught by which detection.

**Progressive challenge model.**
Early modules are guided step-by-step. Later modules require the participant to decide the technique themselves. The capstone (Lab 8) is entirely operator-driven  the instructor plays the defender, and the participant must maintain access through a full remediation gauntlet.

---

## Workshop structure  3 hours

| Time | Segment | Deliverable |
|------|---------|-------------|
| 0:00 – 0:15 | Opening, objectives, lab environment tour | Participants connected to their pod tenant |
| 0:15 – 0:35 | Part I – Identity as the persistence layer | Mental model + Access→Persistence→Control framework |
| 0:35 – 0:50 | Part II – Recon: **Lab 0** enumeration | Shortlist of targets in each participant's tenant |
| 0:50 – 1:25 | Part III – Applications & Service Principals: **Labs 3a–3c** | 3 SP-based anchors planted |
| 1:25 – 1:55 | Part IV – Federated identity abuse: **Labs 4a–4b** | 2 federation-based anchors planted |
| 1:55 – 2:15 | Part V – Passwordless persistence: **Labs 5a–5b** | TAP + CBA anchors planted |
| 2:15 – 2:30 | Part VI – Device trust: **Lab 6** | Rogue device + PRT |
| 2:30 – 2:45 | Part VII – Administrative Units: **Lab 7** | Hidden AU backdoor account |
| 2:45 – 3:10 | Part VIII – Chaining capstone: **Lab 8**  the Remediation Gauntlet | Per-participant survival matrix |
| 3:10 – 3:25 | Part IX – Defender's Playbook | Audit-log priority list + config audit checklist |
| 3:25 – 3:30 | Q&A + resources |  |

---

## Detailed module descriptions

### Part I  Identity Is the Real Perimeter

The framing lecture. Why traditional persistence tradecraft  registry autoruns, scheduled tasks, service DLL hijacks  is irrelevant in a cloud-first tenant. The Access → Persistence → Control mental model. The four pillars of Entra persistence: **applications, federation, authentication methods, devices**. We add a fifth axis mid-workshop  **administrative units**  because it does not fit the traditional pillar model but is too impactful to skip.

### Part II  Recon: Lab 0

Before you can persist inside something, you have to see it. We enumerate directory role assignments (including PIM-eligible ones), application ownership, service principal role holdings, federation trust and domain configuration, authentication methods on privileged users, Conditional Access policies and their exclusions, cross-tenant partners, and  importantly  administrative units accessible only via the Graph beta endpoint. Tooling: Microsoft.Graph PowerShell, ROADrecon, AzureHound, and Vajra.

### Part III  Applications as Persistence (Module 1)

Service Principal tradecraft is the primary anchor for durable Entra compromise. Three labs cover the spectrum:

**Lab 3a  Owner-based credential injection.** Standard-user ownership of a high-privilege app is silent privilege. We enumerate ownable apps, plant a client secret and X.509 certificate credential, and prove access outlives every password reset because SP client-credentials flow never touches user auth. Reference: *The Tolkien Blackguy  App Registration Ownership as Persistence.*

**Lab 3b  Tenant-wide consent injection (AllPrincipals).** One `oauth2PermissionGrants` write with `consentType=AllPrincipals` grants delegated access across the entire tenant in a single call. No per-user prompts, no consent flow. Reference: *SlashID  Entra App Backdooring.*

**Lab 3c  The SP hijack chain to Global Admin.** The definitive end-to-end path published by Datadog: Application Administrator → hijack Office 365 Exchange Online SP → its `Domain.ReadWrite.All` → federated domain takeover → forged SAML tokens for any hybrid user, including Global Administrators. This lab is the fullest expression of "identity persistence"  every step legitimate, every step logged, but the composition catastrophic. Reference: *Datadog Security Labs  I Spy.*

Adjacent context slides cover the **year-2299 long-lived credential trick** (SlashID's observation of credentials with expiries beyond any rotation policy) and **UnOAuthorized** (Semperis's disclosure of first-party Microsoft applications  Device Registration Service, Viva Engage, Rights Management Service  that allowed authorization bypass to modify Global Administrator membership; patched July 2024).

### Part IV  Federated Identity Abuse (Module 2)

Where secrets stop mattering.

**Lab 4a  Secondary token-signing certificate injection.** Entra's federation configuration accepts a `nextSigningCertificate` alongside the primary. Replacing the primary breaks legitimate auth (loud); adding a secondary does not (silent). Attacker signs forged SAML tokens for any hybrid user. Under-appreciated: **External Identity Provider Administrator** and **Domain Name Administrator**  roles not classified as privileged by Microsoft  both enable this attack. Reference: *Tenable  Stealthy Persistence via Secondary Signing Cert* + *Roles Allowing to Abuse Entra ID Federation.*

**Lab 4b  Federated Identity Credential deployment.** Modern OIDC federation. Attacker hosts a public `.well-known/openid-configuration` and JWKS, registers a `federatedIdentityCredential` on a target SP or User Managed Identity, and authenticates via `client_assertion_type=jwt-bearer`. **Zero secrets are stored in the tenant.** Standard credential-rotation runbooks find nothing to rotate. Especially devastating on User Managed Identities, whose authentication is normally Microsoft-controlled. Reference: *Dirk-jan Mollema  Persisting with Federated Credentials, Entra Apps and Managed Identities.*

### Part V  Passwordless Persistence (Module 3)

The objective is not to steal another password. It is to register another way to trust.

**Lab 5a  Temporary Access Pass to attacker-controlled MFA.** TAP is documented as a bootstrap credential. In practice, `isUsableOnce=false` and a 30-day lifetime turn it into a persistence primitive. Sign in with the TAP, register your own FIDO2 key or Authenticator app, and hold a factor that outlives every password reset.

**Lab 5b  Certificate-Based Authentication binding.** Upload attacker root CA to the tenant trust store, enable CBA in the authentication methods policy, and set `certificateUserIds` on the target user to a subject you control. Password reset  no effect. MFA enforcement  no effect (CBA satisfies MFA). Only removing the CA or clearing the binding breaks it.

### Part VI  Device Trust Manipulation (Module 4)

**Lab 6  Rogue device registration and PRT harvest.** Conditional Access asks: is this device compliant or Entra joined? The answer becomes yes when you become the device. Register attacker VM as Entra-joined, sign in as the target to acquire a Primary Refresh Token bound to your device, then enjoy seamless SSO across every Entra-integrated application. PRTs are device-bound  password reset does not invalidate them, session revocation does not invalidate them. Only device deletion does.

### Part VII  Administrative Units (Module 5)

The hidden blast radius most defenders do not know exists.

**Lab 7  Hidden-membership + restricted-management AU backdoor.** Place a backdoor account inside an AU with `isMemberManagementRestricted=true`  tenant-wide admins can no longer modify it, only admins scoped to the AU can. Combine with `visibility=HiddenMembership` (creatable only via the Graph beta endpoint, invisible in the Entra portal) and the account is off the investigation radar entirely. Scope User Administrator over the AU to your controlled SP. Reference: *Datadog Security Labs  Abusing Entra ID Administrative Units.*

### Part VIII  Chaining Capstone

**Lab 8  The Remediation Gauntlet.** Every anchor planted so far, tested against every IR action a defender would run. The instructor plays the defender, running each row of the survival matrix in sequence: force password reset, revoke sessions, enforce MFA, rotate all app secrets, delete the primary SP, remove one guest account, force auth-method re-registration, remove the attacker CA. Between actions, the participant re-verifies each of their anchors.

The deliverable is per-participant: a personal survival matrix that shows exactly which of their anchors are true persistence, which are single-purpose bait, and where their single point of failure sits. This is the moment the workshop's central claim  layered persistence versus a pile of TTPs  becomes concrete.

### Part IX  The Defender's Playbook

Every anchor planted in the workshop maps to a defender view. We conclude with:

1. **Audit-log priorities**  the top nine event names to alert on, ordered by severity, with the specific attack each catches.
2. **Configuration-state audits**  the ten config checks that beat log-based detection when logs were not collected, retention has aged out, or the persistence predates SIEM ingestion. Referenced approach: *Stream Security  Detecting Entra ID Persistence.*
3. **Hunt query library**  Sentinel / Log Analytics queries for each event.

The core defender takeaway: **password reset is not remediation.** Full remediation requires audit of SP credentials, federated identity credentials, authentication methods, CBA trust store bindings, device objects, administrative units, and cross-tenant access policies. If any of those is missing from the incident response runbook, the workshop has succeeded when the defender in the room adds it.

---

## Learning outcomes

By the end of the workshop, every participant will be able to:

1. Identify high-value application identities and enumerate ownable service principals in an unfamiliar tenant.
2. Plant SP credentials (secrets + X.509 certificates) that outlive every user's password lifecycle.
3. Register federated identity credentials  persistence with zero secrets stored in the tenant.
4. Inject a secondary token-signing certificate to forge SAML tokens without disrupting legitimate authentication.
5. Register attacker-controlled MFA methods, long-lived TAPs, and CBA bindings that survive password resets.
6. Register rogue devices and harvest Primary Refresh Tokens for seamless SSO.
7. Use hidden-membership and restricted-management Administrative Units to hide backdoor accounts from tenant-wide administrators.
8. Chain multiple anchors so no single remediation action ends their access.
9. Map every technique to its MITRE ATT&CK for Cloud technique and its detection anchor.
10. (Defenders) Deploy an audit-log alerting baseline and configuration-state audit checklist that catches the techniques above.

---

## Who this is for

- **Red teamers** operating in cloud engagements who need current post-compromise tradecraft in Entra ID.
- **Blue teamers and SOC analysts** whose IR runbooks predate cloud identity being a first-class target.
- **Cloud security architects** designing detection or hardening for Entra ID environments.
- **Purple teamers** who want to walk out with a matched attack-defense playbook for identity persistence.

**Prerequisites:** basic familiarity with Microsoft Entra ID concepts (users, groups, roles, applications), PowerShell or CLI comfort, and either an Azure subscription or the willingness to use the workshop-provided pod tenant.

---

## What participants take home

- The complete slide deck.
- The step-by-step lab guide (`Lab-Guide.md`) with every command, prerequisite, break-it/validate-it trigger, and detection tip.
- The survival matrix template from Lab 8.
- The defender's audit-log priority list and configuration audit checklist.
- Their pod tenant remains active for 24 hours post-workshop for continued experimentation.

---

## References informing this material

- Datadog Security Labs  *I Spy: Escalating to Entra ID Global Admin*
- Datadog Security Labs  *Abusing Entra ID Administrative Units*
- Tenable Tech Blog  *Stealthy Persistence & PrivEsc via Secondary Token-Signing Cert*
- Tenable Tech Blog  *Roles Allowing to Abuse Entra ID Federation for Persistence and Privilege Escalation*
- Semperis  *UnOAuthorized: Privilege Elevation through Microsoft Applications*
- Dirk-jan Mollema  *Persisting with Federated Credentials, Entra Apps and Managed Identities*
- The Tolkien Blackguy  *App Registration Ownership as Persistence in Entra ID*
- SlashID  *Entra App Backdooring*
- Guardz  *Abusing Entra ID App Registrations for Long-Term Persistence*
- Stream Security  *Have I Been Pwned: Detecting Entra ID Persistence*

---

## Presenter

**Raunak Parmar**  Senior Cloud Security Engineer at White Knight Labs. OSWE. AppSec & Cloud Security research on Azure, Entra ID, and AWS. Creator of Vajra, an open-source post-exploitation toolkit for Entra ID and Azure. Prior speaker at Black Hat, DEF CON, NullCon, RootCon, and HITB. Ex-DJ and music producer. Twitter/X: `@trouble1_raunak`.
```
