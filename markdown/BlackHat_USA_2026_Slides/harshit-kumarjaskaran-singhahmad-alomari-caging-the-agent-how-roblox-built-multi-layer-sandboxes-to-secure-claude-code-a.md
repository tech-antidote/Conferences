---
title: "Caging the Agent How Roblox Built Multi-Layer Sandboxes to Secure Claude Code at Enterprise Scale"
speakers: ["Harshit Kumar", "Jaskaran Singh", "Ahmad Alomari"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Harshit Kumar&Jaskaran Singh&Ahmad Alomari_Caging the Agent How Roblox Built Multi-Layer Sandboxes to Secure Claude Code at Enterprise Scale.pdf"
pages: 44
sha256: "272ad4f387a461e15c31e858fc840888f81ff9d77ae5f55b66f190ed007f97d0"
text_chars: 18417
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:09:54Z"
---
# Caging the Agent How Roblox Built Multi-Layer Sandboxes to Secure Claude Code at Enterprise Scale

**Speakers:** Harshit Kumar, Jaskaran Singh, Ahmad Alomari  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Harshit Kumar&Jaskaran Singh&Ahmad Alomari_Caging the Agent How Roblox Built Multi-Layer Sandboxes to Secure Claude Code at Enterprise Scale.pdf` (44 pages)


## Slide 1

Caging The Agent How Roblox Built Multi-Layer Sandboxes to Secure Claude Code at Enterprise Scale

Ahmad Alomari Sr. Manager, AppSec

Jaskaran Singh Harshit Kumar Principal Security SWE Principal Security SWE

## Slide 2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Harshit Kumar Jaskaran Singh
Principal Security SWE Principal Security SWE
Caging the Agent
How Roblox Built Multi-Layer Sandboxes
to Secure Claude Code at Enterprise Scale
```

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Trigger
DATE: February 2026
ACTOR: Internal Red Team
VECTOR: Prompt Injection
Secret
l=) ~g daa
Malicious GitHub
Prompt Workflow
```

## Slide 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Trigger Blast Radius
DATE: February 2026 a =
ACTOR: Internal Red Team </> —
VECTOR: Prompt Injection
Secret
l=) “gi hata
Malicious GitHub
Prompt Workflow
Game Engine Source Developer Credentials
Code (Core IP) & CI/CD Systems
```

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Trigger
DATE: February 2026
ACTOR: Internal Red Team
VECTOR: Prompt Injection
Secret
5 “J hata
Malicious GitHub
Prompt Workflow
Blast Radius
Game Engine Source
Code (Core IP)
Developer Credentials
& Cl/CD Systems
The Mandate
4©
WEEKS
SA Re-enable agent
access
Ai Maintain developer
productivity
wr Zero compromise
on security
```

## Slide 6

Jaskaran Singh Harshit Kumar
Principal Security SWE Principal Security SWE

## Slide 7

# **The Agent Dilemma**

**NEW RISK**



**Context**

###### **Ingestion**

Malicious input ingested

## Slide 8

# **The Agent Dilemma**

**NEW RISK**   **Context Credential Ingestion Discovery** Malicious input Local environment ingested scanned

## Slide 9

# **The Agent Dilemma**

**NEW RISK**    **Context Credential Sandbox Ingestion Discovery Escape** Malicious input Local environment Deferred execution ingested scanned triggered

## Slide 10

# **The Agent Dilemma**

NEW RISK

  
Context  Credential  Sandbox  Persistence
Ingestion Discovery Escape
Rogue hooks
established
Malicious input  Local environment  Deferred execution
ingested scanned triggered

## Slide 11

The Agent Dilemma
NEW RISK

   
Context  Credential  Sandbox  Persistence Data
Ingestion Discovery Escape Exfiltration
Rogue hooks
established
Malicious input  Local environment  Deferred execution  Secrets leave
ingested scanned triggered network

## Slide 12

# **The Agent Dilemma**

NEW RISK

   
Context  Credential  Sandbox  Persistence Data
Ingestion Discovery Escape Exfiltration
Rogue hooks
established
Malicious input  Local environment  Deferred execution  Secrets leave
ingested scanned triggered network

**Prompt injection** is the only **NEW** risk—but it amplifies and accelerates all subsequent stages by removing friction and human judgment.

## Slide 13

# **So, what do we do?**

 **Agentic Execution** This problem by extension manifests wherever agentic execution happens — including development environments

 **Sandbox Governance** To achieve safe(-ish) execution of automated tasks, we need layers of governance implemented by a Sandbox

 **Consumer Usability** The solution should be easy to use and provide excellent usability for consumers

## Slide 14

Redefining the Trust Boundary
TRUST MODEL COMPARISON EXPANDED ATTACK SURFACE & FLOW
Security Model User Trust Input Trust
 Repositories
Traditional Highly Trusted Mostly Trusted
 Package Registries
Untrusted Inputs   Internal Docs
Agent Model Highly Trusted 
Drive Execution
Autonomous
 MCP Services Agent
PROMPT INJECTION
Critical Takeaway:
Treat all context ingestion as potentially adversarial. Prompt   PR Metadata
injection bypasses traditional filters by execution mapping.

## Slide 15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Chatbot Paradigm
abe
4
IN
= Al Suggestions
tL
Human Intent Validates Action
```

## Slide 16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Chatbot Paradigm
Al Suggestions
— Ta ie)
Human Intent Validates Action
The Agent Paradigm
Al Context
le Ingestion
Autonomous
Execution
— Direct System
crm §=Access
Machine Autonomy Bypasses Intent
```

## Slide 17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Chatbot Paradigm
2
Caer
a
N
= Al Suggestions
1
<_\ Human Review
4
Execution
Human Intent Validates Action
The Agent Paradigm
Al Context
pal Ingestion
Autonomous
Execution
= Direct System
Cm Access
Machine Autonomy Bypasses Intent
Existing security controls cannot distinguish benign vs. malicious agent actions.
They are designed for human intent.
```

## Slide 18

**One Consistent Security Model**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Multi-Environment Sandbox Architecture
Cloud VM (Devspaces)
<r Strongest isolation.
SS The foundational
RA starting point for the
NY deployment strategy,
macOS Native Sandbox
Maintains local
hardware performance
while enforcing strict
process control.
WSL2 (Windows)
LEE A practical isolation
tj layer bridging Windows
hosts and Linux tooling.
Docker (Linux)
<a Provides maximum
ne environment portability
Wie! across developer setups.
```

## Slide 19

## Slide 20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Core Sandbox
Design Principles &
=
&
L
-
8
Gade
Strict separation from the
host OS; no privilege
escalation pathways.
```

## Slide 21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Core Sandbox
Design Principles
-— Strong Host
Isolation
Strict separation from the
host OS; no privilege
escalation pathways.
-— Immutable
Configuration
aa Settings baked into images or
root-owned. Zero runtime
tampering allowed.
```

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Core Sandbox
Design Principles
&
it
§
Deny-by-Default
Permissions
Implicit denial of all system
resources unless explicitly
granted.
Immutable
Configuration
Settings baked into images or
root-owned. Zero runtime
tampering allowed.
Strong Host
Isolation
Strict separation from the
host OS; no privilege
escalation pathways.
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Core Sandbox
Design Principles
Network Egress ——
Allowlisting
Fail-closed network
architecture restricting
outbound communication.
Deny-by-Default
Permissions
Implicit denial of all system
resources unless explicitly
granted.
Immutable
Configuration
Settings baked into images or
root-owned. Zero runtime
tampering allowed.
Strong Host
Isolation
Strict separation from the
host OS; no privilege
escalation pathways.
```

## Slide 24

###### **DEFENSE IN DEPTH**

### **Multi-Layered Agent Sandboxing**

Ring 1: Behavioral Guardrails
Ring 2: Host Isolation
1 2 3 4 5
Agent Ring 3: Network Segmentation
Ring 4: Centralized Control
Ring 5: Global Visibility

**Zero-Trust Assumption:** Each layer assumes that the others can fail. Sandboxing in only one dimension is insufficient.

## Slide 25

Agent 1 2 3 4 5

###### **Secure Agent Architecture**

### **Ring 1: Behavioral Guardrails**

- **Devspaces & microVMs**

- **Access & Settings**

**Base images with controls & dev tooling baked in:**

###### **Managed Environment**

   - Managed settings & CLAUDE.md files

- Language SDKs

   - Agent user configuration

- Roblox Skills

- Common internal dev tooling

###### **Path Restrictions**

- Denied access to critical paths

- **Prompt Guardrails**

###### **Secrets Detection**

   - Baked-in secrets detection as pre-prompt hook

   - Automatic SIEM notification if secrets are leaked

- Limited sudo access for specific commands (e.g., apt-get)

## Slide 26

**Behavioral Guardrails**

#### **Managed CLAUDE.md**

An immutable policy file defining strict sandbox boundaries while preserving full developer capabilities.

- Strict Policy Rules

Bypasses, credential access, and modifying critical security settings are absolutely forbidden.

- Allowed Actions

Full development freedom to edit project files, execute build commands, and install packages via sudo.

## Slide 27

**Behavioral Guardrails**

#### **Managed Settings**

Enforces default model versions, telemetry requirements, and OpenTelemetry instrumentation parameters globally.

######  **Model Governance**

Pins allowed models to approved Claude versions (Opus, Sonnet, Haiku) and disables non-essential traffic

######  **Unified Observability**

Configures system-wide OTEL endpoints for secure metrics, traces, and logs collection via protobuf

## Slide 28

**Behavioral Guardrails**

#### **Policy & Tool Configurations**

**managed-settings.json**

###### **managed-settings.json**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Behavioral Guardrails
Policy & Tool Configurations
@@@ managed-settings.json
"Read (+*/.env.*)",
"Read (+k/credentials.json)",
"Read (+k/service-account.json)",
"Write (+*/service-account. json)"
"Read (+*/.aws/**)",
“Write (+*k/.aws/**)",
"Read («/.ssh/**)",
"Read (+*k/.password-store/xx)",
"Read (+x/.gnupg/*x)",
"Read (+**/.npmrc)",
"Read (**/.netrc)",
"Write(*x/.netrc)",
"Read (**/*.pem)",
"Write (*x/x.pem)",
"Write (#k/*.crt)",
"Read (+/+. key)",
"Write (+k/*. key)",
“Write (+**/*.tfvars)",
@@@ managed-settings.json
“strictKnownMarketplaces": [
{ “source'
“https: //github. com/anthropics/claude-code.git", “ref"
{ “source ‘tps: //github. com/anthropics/claude-plugins-official.git", h
{ “source https: //github. rbx.com/Roblox/claude-code-plugins.git", "ref
1,
1
Dp
{
"matcher": “Bash|Shell|WebFetch |WebSearch|Agent",
“hooks": [
{ "type": "command", "command": "/etc/claude-code/hooks/infosec/infosec-hooks block-subagent", "timeout": 5 }
1
Bp
{
"matcher": “WebFetch",
"hooks": [
{ "type": "command" “/etc/claude-code/hooks/infosec/infosec-hooks block-uploads", "timeout": 5 }
1
Dp
"matcher": “Read|Bash|Shell",
“hooks' C
{ "type": "command", "command": "/etc/claude-code/hooks/infosec/infosec-hooks block-secret-access", "timeout": 5 }
1
Dy
{
"matcher": “Bash|Shell",
“hooks' C
```

## Slide 29

**Core sandbox isolation capabilities and platform-specific implementations**

**Agent 1 2 3 4 5**

#### **Ring 2: Host Isolation**

###### **Required Capabilities**

###### **Sandbox Implementations**

**Kernel / Process Isolation** 

Prevents unauthorized or arbitrary command execution directly on the host machine.

**Devspace** 

An isolated EC2 machine running a Squid Proxy

to control and log egress traffic.

 **Network Isolation**

Strips default network privileges to restrict ingress and egress communications.

 **Docker Sandbox & WSL**

Deploys highly efficient microVMs utilizing a

local proxy for secure containment.

**Filesystem Isolation** 

Restricts directory traversal, confining activities strictly to the active workspace.

**Declawd** 

Process based mac-OS sandbox built on Seatbelt

paired with Silencer, a custom network proxy kernel

extension.

## Slide 30

Agent 1 2 3 4 5

**Core sandbox isolation capabilities and platform-specific implementations**

#### **Ring 2: Host Isolation**

###### **Required Capabilities**

###### **Sandbox Implementations**

**Kernel / Process Isolation** 

Prevents unauthorized or arbitrary command execution directly on the host machine.

**Devspace** 

An isolated EC2 machine running a Squid Proxy to control and log egress traffic.

 **Network Isolation**

Strips default network privileges to restrict ingress and egress communications.

 **Docker Sandbox & WSL**

Deploys highly efficient microVMs utilizing a local proxy for secure containment.

**Filesystem Isolation** 

Restricts directory traversal, confining activities strictly to the active workspace.



###### **Declawd**

Process based mac-OS sandbox built on Seatbelt paired with Silencer, a custom network proxy kernel extension.

## Slide 31

**Network Segmentation is the main control for limiting Blast Radius**

**Agent 1 2 3 4 5**

#### **Ring 3: Network Segmentation**

###### **Risks of Flat Networks**

###### **Multi-Layer Segmentation Plan**

**Production Services**  Highly vulnerable to lateral movement across flat internal environments.

**Dedicated VPN Profiles**  Isolates and operates sandboxes securely in custom environments.

**Critical Infrastructure**  Exposes core infrastructure and directory services unnecessarily.

**Squid Proxy Filtering** 

Centralized egress filtering using strict host and

path-based rules.

**Datalakes & Resources**  Permits unauthorized data extraction paths and forgotten storage risks.

**Silencer & Kollide** 

Intercepts traffic on endpoints and prevents malicious local misconfigurations.

## Slide 32

**Network Segmentation is the main control for limiting Blast Radius**

**Agent 1 2 3 4 5**

#### **Ring 3: Network Segmentation**

###### **Risks of Flat Networks**

###### **Multi-Layer Segmentation Plan**

**Production Services**  Highly vulnerable to lateral movement across flat internal environments.

##### 

###### **Dedicated VPN Profiles**

Isolates and operates sandboxes securely in custom environments.

**Critical Infrastructure**  Exposes core infrastructure and directory services unnecessarily.

###### **Squid Proxy Filtering**

 Centralized egress filtering using strict host and path-based rules.

**Datalakes & Resources**  Permits unauthorized data extraction paths and forgotten storage risks.

**Silencer & Kollide**  Intercepts traffic on endpoints and prevents malicious local misconfigurations.

## Slide 33

**Centralized gateway, token exchange, and credentials broker**

**Agent 1 2 3 4 5**

#### **Ring 4: Centralized Control**

###### **Gateway & Traf fi** **c Controls**

###### **Identity & Credentials**

**LLM Gateway**  Centralized gateway for all internal agent traffic routing and control.



###### **MCP Gateway**

No static per-user API keys. The gateway exchanges short-lived tokens dynamically.

**Classifiers & PII Detection**  Lightweight prompt injection classifiers (proprietary/internal) and PII filters.

###### **Credentials Broker**

 Safely access service credentials without persisting them inside the sandbox.

**Metrics & Spending Guardrails**  Wallet tracking (denial of wallet), user spend policy, logging, and auditing.

###### **Agent Identity**

 Short-lived identity tokens to uniquely identify and authenticate each agent acting on behalf of a user.

## Slide 34

###### **Authentication Challenge & Strategy**

#### **The Next Frontier: Third-Party Agent Services**

 **The Problem**

 **The Threat**

- **The Goal**

###### **PAT Access Necessity**

###### **Memory Exposure**

###### **Zero-Trust Auth**

Agents need to reach wikis, issue trackers, and code hosts without being handed long-lived Personal Access Tokens (PATs) that expose permanent keys to unverified environments

PATs held in agent memory are vulnerable to prompt injection attacks. Lacking a central inventory, rogue agent actions become entirely indistinguishable from authentic human actions in upstream audit logs

Authenticate to any upstream service dynamically, ensuring the agent never directly holds or manages a long-lived credential at any stage of the lifecycle

## Slide 35

###### **Extending Agents**

#### **Injection vs. Brokering Architecture**

Credential Brokering
1. Send LCA JWT (User Identity)
Agent Sandbox Credential Broker
Isolated Environment
Vault / Auth Service
2. Short lived scoped oauth tokens (Exposed to agent memory)
Vulnerable to Prompt Injection

## Slide 36

###### **Extending Agents**

#### **Injection vs. Brokering Architecture**

Credential Brokering
1. Send LCA JWT (User Identity)
Agent Sandbox Credential Broker
Isolated Environment
Vault / Auth Service
2. Short lived scoped oauth tokens (Exposed to agent memory)
Vulnerable to Prompt Injection
Credential Injection
2. Fetch Token via Auth Flow
Credential Broker
MCP Gateway
Agent Sandbox 1. Tool Call + LCA JWT
Mediating Proxy
Isolated Environment
3. Outbound request with  Vendor API
INJECTED Token GitHub, Jira, etc.
✔  Agent never sees the token
✔  Memory remains isolated

## Slide 37

**THIRD-PARTY AUTHENTICATION AT SCALE**

#### **Secure Identity & Credential Delivery Lifecycle**

**Agent Identity (JWT)** 

- **Credential Broker**

- **MCP Gateway**

-

###### **User-Attributed Tokens**

###### **Vault Integration**

###### **Mediates Tool Traffic**

Issues short-lived, human-attributed identity tokens ( **JWT’s** ) that map directly to authenticated sessions.

Binds the agent workload to the specific human developer, ensuring strict auditability and user context persistence.

A central microservice backed by HashiCorp Vault designed to securely store and handle access mechanics.

Runs background OAuth flows and manages long-lived vendor tokens dynamically.

**Never exposes** long-lived tokens to the agent's untrusted execution environment.

Acts as a proxy that intercepts outbound API calls made by the agent to external platforms.

Automatically injects the required vendor credentials on the agent's behalf mid-flight.

The credential is **mathematically removed** from the memory of the agent process entirely.

## Slide 38

**Continuous monitoring, lifecycle tracking, and telemetry forwarding**

**Agent 1 2 3 4 5**

#### **Ring 5: Global Visibility**

###### **Visibility & Lifecycle Controls**

###### **Agent Identity**

##### 

Crucial for attribution when dealing with thousands of concurrent sandboxes across the user base.

###### **FleetDM Integration**

 Agent inserted into every sandbox during startup to monitor lifecycle and compliance continuously.

###### **Telemetry Forwarding**



All prompts and tool calls are logged by the observability platform via OTEL and pushed directly to the central SIEM.

## Slide 39

## Slide 40

## Slide 41

#### **Security & Experience Incentivization & Secure Defaults**

**Maximum Security** Secure defaults must adhere to baseline security requirements silently

Turnkey Delivery
Marry Best Practices with Turnkey
Delivery
MCP Gateway
Automated Token Exchange
Company-specific skills
Seamless access to third party services
Built-in Agent Identity

**Zero Friction** Productivity is the ultimate goal. Seamless integrations ensure developer speed remains uncompromised

Feedback from your actual users drives secure adoption

## Slide 42

###### **Post-Deployment Analysis**

#### **Post-Deployment Reality**

######  **Outcomes**

**<4 Weeks Secure agent re-enable achieved.** Developer productivity restored safely

**100% Remediation Critical and high risk blockers.** Marrying industry best practices with turnkey delivery

 **Residual Systemic Exposure**

**Local vs. Systemic Risk**

Sandboxes reduce local execution risk but do not eliminate systemic network and data exposure

###### **The Allowlist Paradox**

Trusted domains (like GitHub) can be weaponized for data exfiltration under standard endpoint permissions

###### **Pipeline-Scale Security**

Agent security must scale to protect the entire pipeline (CI/CD, identity, network), not just the host endpoint

## Slide 43

###### **Acknowledgements**

## **Thank You to Our Contributors**

 **Leadership & Direction**

**Nicole Grinstead** Chief Executive **Ahmad Alomari Shawna Murphy Butterworth Lindsey Pilver Tom MacGregor**

 **Core Contributors Iurii zakipnyi John Judge Shounak Datta Charles Zaffery Gan Fang Sakina Mithani Aakash Yadav**

 **Strategic Support David Levitsky William Dawson Rocky Yuan Rex Belli Rahul Toppur Tylor Silva**

Your dedication and collaborative effort drive our shared success

## Slide 44

### **CONTACT & CONTRIBUTION Project Leads**

- **Harshit Kumar Turning paranoia into architecture**  91.harshit@gmail.com

- linkedin.com/in/harshit-kumar-sec/

**Jaskaran Singh Anti-AppSec AppSec Guy**

- jaskaran.singh.dr6j@gmail.com

-  linkedin.com/in/jaskaran-singh-sec

Feel free to reach out for collaboration, questions, or feedback
