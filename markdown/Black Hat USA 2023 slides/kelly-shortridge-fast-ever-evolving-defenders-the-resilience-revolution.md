---
title: "Fast, Ever-Evolving Defenders The Resilience Revolution"
speakers: ["Kelly Shortridge"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Kelly Shortridge_Fast, Ever-Evolving Defenders The Resilience Revolution.pdf"
pages: 160
sha256: "6ff7c1f71ff8b2eba3378eb8a0644ddd56632e1c898e3be3a15796f03675b318"
text_chars: 21552
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:15:54Z"
---
# Fast, Ever-Evolving Defenders The Resilience Revolution

**Speakers:** Kelly Shortridge  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Kelly Shortridge_Fast, Ever-Evolving Defenders The Resilience Revolution.pdf` (160 pages)


## Slide 1

- FAST VER EVOLVING , E DEFENDERS: THE RESILIENCE REVOLUTION

Kelly Shortridge @swagitda_  |  @shortridge

Black Hat USA 2023

## Slide 2

There’s a pervasive sense that attackers continually outmaneuver us as defenders.

2

shortridge@hachyderm.io | @swagitda_

## Slide 3

- Attackers are fast. They are ever evolving. How could we possibly outmaneuver them?

3

shortridge@hachyderm.io | @swagitda_

## Slide 4

The answer is we become more like attackers: nimble, empirical, and curious.

4

shortridge@hachyderm.io | @swagitda_

## Slide 5

## – This talk is about revolution a new paradigm for systems defense, grounded in resilience.

5

shortridge@hachyderm.io | @swagitda_

## Slide 6

# Attacker Asymmetries

## Slide 7

How many of you have heard attackers only need to get right once and then they win?

7

shortridge@hachyderm.io | @swagitda_

## Slide 8

That’s a myth. They need to get right once for after. initial access then get it right _every time_

8

shortridge@hachyderm.io | @swagitda_

## Slide 9

## So, what are attackers’ _real_ advantages?

9 shortridge@hachyderm.io | @swagitda_

## Slide 10

## 1) Attackers have a **faster** operational tempo

10

shortridge@hachyderm.io | @swagitda_

## Slide 11

## 2) Attackers **design** , develop, and operate mechanisms to outmaneuver us

11

shortridge@hachyderm.io | @swagitda_

## Slide 12

## 3) Attackers research interconnections and interactions in **systems**

12

shortridge@hachyderm.io | @swagitda_

## Slide 13

## 4) Attackers have more tangible and actionable **success metrics**

13

shortridge@hachyderm.io | @swagitda_

## Slide 14

There is no reason why we can’t steal these advantages for ourselves as defenders.

14

shortridge@hachyderm.io | @swagitda_

## Slide 15

All of these reflect a foundation of **resilience** : the ability to prepare for, recover from, and adapt to adverse events.

15

shortridge@hachyderm.io | @swagitda_

## Slide 16

We can seize opportunities that grant us these same advantages via the resilience revolution.

16

shortridge@hachyderm.io | @swagitda_

## Slide 17

I. Faster Tempo

## Slide 18

## Attackers pivot quickly in the face of adversity.

18

shortridge@hachyderm.io | @swagitda_

## Slide 19

Attackers also rapidly evolve their methods.

19 shortridge@hachyderm.io | @swagitda_

## Slide 20

We can achieve a faster tempo by adopting approaches from modern software engineering.

20

shortridge@hachyderm.io | @swagitda_

## Slide 21

Configuration as Code

## Slide 22

CaC : the practice of declaring configurations through markup rather than manual processes

22

shortridge@hachyderm.io | @swagitda_

## Slide 23

## - - Infrastructure as Code (IaC): the ability to create and manage infra via declarative specifications

23

shortridge@hachyderm.io | @swagitda_

## Slide 24

We generate the same environment every time, creating more reliable and predictable services.

24

shortridge@hachyderm.io | @swagitda_

## Slide 25

Organizations already use IaC for the audit trail it generates and making practices repeatable.

25

shortridge@hachyderm.io | @swagitda_

## Slide 26

Let’s take a whirlwind tour of IaC’s bountiful benefits for security programs:

26

shortridge@hachyderm.io | @swagitda_

## Slide 27

## Faster Incident Response

27

shortridge@hachyderm.io | @swagitda_

## Slide 28

## Automatically redeploy infrastructure when incidents happen… or even leading indicators

28

shortridge@hachyderm.io | @swagitda_

## Slide 29

Compromised workloads can be killed and redeployed as soon as an attack is detected

29

shortridge@hachyderm.io | @swagitda_

## Slide 30

## Minimized misconfigurations

30 shortridge@hachyderm.io | @swagitda_

## Slide 31

NSA: misconfigurations are the most common cloud vuln; easy to exploit + highly prevalent

31

shortridge@hachyderm.io | @swagitda_

## Slide 32

IaC helps correct misconfigurations by users and automated systems (machines) alike

32

shortridge@hachyderm.io | @swagitda_

## Slide 33

## Faster patching and security changes

33

shortridge@hachyderm.io | @swagitda_

## Slide 34

The _real_ lesson of Equifax: patching processes must be usable, else procrastination is rational

34

shortridge@hachyderm.io | @swagitda_

## Slide 35

IaC reduces friction for releasing patches, updates, or fixes & decentralizes the process

35

shortridge@hachyderm.io | @swagitda_

## Slide 36

: if an Protip organizational process is unusable or cumbersome, it will be circumvented.

36

shortridge@hachyderm.io | @swagitda_

## Slide 37

Minimized
Environmental
Drift
37 shortridge@hachyderm.io | @swagitda_

## Slide 38

Environmental drift: configs or other attributes “drifting” into an inconsistent state

38

shortridge@hachyderm.io | @swagitda_

## Slide 39

## Automatic infra versioning minimizes this drift; reversion and repeatability becomes easier

39

shortridge@hachyderm.io | @swagitda_

## Slide 40

## Catching vulnerable configurations

40

shortridge@hachyderm.io | @swagitda_

## Slide 41

Status quo is authenticated scanning in production, which introduces new attack paths

41

shortridge@hachyderm.io | @swagitda_

## Slide 42

IaC removes that hazard, instead scanning the code files to find vulnerable assets or configs

42

shortridge@hachyderm.io | @swagitda_

## Slide 43

## Stronger change control

43

shortridge@hachyderm.io | @swagitda_

## Slide 44

IaC introduces change control via SCM, enabling peer reviews on configs + changelog

44

shortridge@hachyderm.io | @swagitda_

## Slide 45

tl;dr IaC grants us a faster operational tempo in a variety of dimensions

45

shortridge@hachyderm.io | @swagitda_

## Slide 46

Automating Security Checks

## Slide 47

CI/CD accelerates dev and delivery of software features without hurting reliability or quality

47

shortridge@hachyderm.io | @swagitda_

## Slide 48

CI/CD pipeline: sets of (ideally automated) tasks that deliver a new software release

48 shortridge@hachyderm.io | @swagitda_

## Slide 49

Compiling the app (building) + testing code + deploying to test/staging + delivering to prod

49

shortridge@hachyderm.io | @swagitda_

## Slide 50

CI/CD is a tool to make software delivery more repeatable, predictable, and consistent.

50

shortridge@hachyderm.io | @swagitda_

## Slide 51

We can enforce **invariants:** achieve properties we want every time we build + deploy + deliver

51

shortridge@hachyderm.io | @swagitda_

## Slide 52

“Database servers should only make outgoing network connections to their replication peers and a short list of core services.”

52

shortridge@hachyderm.io | @swagitda_

## Slide 53

## “Services must communicate over TLS and validate remote certificates.”

53

shortridge@hachyderm.io | @swagitda_

## Slide 54

“Only images built by our CI/CD system may run on the production Kubernetes cluster.”

54

shortridge@hachyderm.io | @swagitda_

## Slide 55

“Secrets should be retrieved on demand from our secrets store instead of being baked into source code or deployment images.”

55

shortridge@hachyderm.io | @swagitda_

## Slide 56

If you can ship software when you want, you can ship security fixes whenever you need to.

56

shortridge@hachyderm.io | @swagitda_

## Slide 57

Everything is recorded; you can set granular policy on who can deploy where and for what

57

shortridge@hachyderm.io | @swagitda_

## Slide 58

58 shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C3) (=) shortridge-sensemaking/fir. X Overview | firewall-demo | | X g Signal Sciences x Ge Nf a x
<> Code {2 Pullrequests 1 © Actions © Security [¥ Insights & Settings
bf = main ~ firewall-demo / banlist.txt Q é t see
ert "Update IP Banlist"’ “ 38ead24 : 1 Ter 1) History
&: swagitda |
| Code Blame (©) 1281 line
l #
#
#
# Binary Defense Systems Artillery Threat Intelligence Feed and Banlist Feed
#
# Note that this is for public use only.
# The ATIF feed may not be used for commercial resale or in products that are charging fees for such services.
# Use of these feeds for commerical (having others pay for a service) use is strictly prohibited.
#
#
#
1.10.241.225
1.85.49.110
1.183.12.102
1.206.27.29
1.215.138.43
1.235.198.19
pte) SHORTRIDGE@HACHYDERM.IO | ASWAGITDA_
```

## Slide 59

CI/CD can help us with patching and keeping dependencies up to date

59

shortridge@hachyderm.io | @swagitda_

## Slide 60

60

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Security / Dependabot Alerts / #120
Improper Input Validation in Octocat #120 tues
Opened on Aug 6 on octocat (pip) - requirements.txt
Severity score
4 Bump Octocat from 8.0.8 to 8.0.9 ~
Updating octocat in requirements.txt would resolve 4 Dependabot ale
Chigh ) 9.5
Weakness types
Vulnerable calls CWE-20
Showing the first of 4 calls to known vulnerable functions in octocat 8
GHSA ID
(filepath)
octocat = octocat.build(octocat_location, Loader=octocat.load)
able function called See all your affected repositories
mona_data[“monalisa”] = octocat
SHORTRIDGE ACHYDERM.IO | ASWAGITDA_
```

## Slide 61

Automated CI/CD pipelines means patches can be tested and pushed to prod in hours vs. days

61

shortridge@hachyderm.io | @swagitda_

## Slide 62

- - Update and patch cycles become an automatic, daily affair, freeing time for other priorities

62

shortridge@hachyderm.io | @swagitda_

## Slide 63

## tl;dr CI/CD lets us move faster and track the – things we do or revert (attackers can’t do so)

63

shortridge@hachyderm.io | @swagitda_

## Slide 64

- II. Design based defense

## Slide 65

How should we prioritize the types of solutions we design? Are some better than others?

65

shortridge@hachyderm.io | @swagitda_

## Slide 66

We want to design solutions that encourage the nimbleness that we envy in attackers.

66

shortridge@hachyderm.io | @swagitda_

## Slide 67

67 shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 95/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ing dependence on human behavior
Increasi
Figure 7-3. The Ice Cream Cone Hierarchy of Security Solutions
@HAC
HYI
HY
```

## Slide 68

“Human fallibility is like gravity, weather, and terrain, just another foreseeable hazard.”

68

shortridge@hachyderm.io | @swagitda_

## Slide 69

Finite cognitive resources; competing pressures; exhaustion, stress, distraction…

69

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Finite cognitive resources; competing
pressures; exhaustion, stress, distraction...
69 SHORTRIDGE@HACHYDERM.IO | A@SWAGITDA_
```

## Slide 70

Kelly Lum pushed for HTTPS as the default for - Tumblr blogs in 2016 (a design based solution)

70

shortridge@hachyderm.io | @swagitda_

## Slide 71

Isolation, standardization, message buses, declarative dependencies, queues, failover…

71

shortridge@hachyderm.io | @swagitda_

## Slide 72

Modularity

## Slide 73

**Modularity** : allows structurally or functionally distinct parts to retain autonomy during periods of stress & allows for easier recovery from loss

73

shortridge@hachyderm.io | @swagitda_

## Slide 74

Unless components can fail independently, you don’t have modularity in the resilience sense.

74

shortridge@hachyderm.io | @swagitda_

## Slide 75

Queues and message brokers support modularity, each in different ways…

75

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Queues and message brokers support
modularity, each in different ways...
75 SHORTRIDGE@HACHYDERM.IO | A@SWAGITDA_
```

## Slide 76

A queue adds a buffer; a message broker can - replay and make return code non blocking.

76

shortridge@hachyderm.io | @swagitda_

## Slide 77

Both tools standardize how services pass data around and provide a centralized view.

77

shortridge@hachyderm.io | @swagitda_

## Slide 78

If your systems are modular, you can create temporary “airgaps” (the “airlock approach”)

78

shortridge@hachyderm.io | @swagitda_

## Slide 79

Queue

Processing service
Service A
(vulnerable)

79

shortridge@hachyderm.io | @swagitda_

## Slide 80

Queue
(growing)
Processing service thrown
“out the airlock”
Processing service
Service A
(vulnerable)

80

shortridge@hachyderm.io | @swagitda_

## Slide 81

Queue
(draining)
Processing service
Service A (healed +
redeployed)

81

shortridge@hachyderm.io | @swagitda_

## Slide 82

## – Modularity minimizes incident impact think ransomware in serverless (it doesn’t happen)

82

shortridge@hachyderm.io | @swagitda_

## Slide 83

Modularity allows for basic encapsulation and separation of concerns… and supports isolation

83

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Modularity allows for basic encapsulation and
separation of concerns... and supports isolation
83 SHORTRIDGE@HACHYDERM.IO | A@SWAGITDA_
```

## Slide 84

Here’s what it’s like to live in 2023 with a strong engineering culture:

84

shortridge@hachyderm.io | @swagitda_

## Slide 85

RLBox : trap C code in a WebAssembly (Wasm) sandbox to isolate hazardous subcomponents

85

shortridge@hachyderm.io | @swagitda_

## Slide 86

86 shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sandbox
memory
Sandbox
memory
> Firefox
Sandbox
memory
Browser
memory
libogg
SHORTRIDGE@MHACHYDERM.IO | @SWAGITDA
```

## Slide 87

## Imagine not worrying about 0day anymore*.

87

shortridge@hachyderm.io | @swagitda_

## Slide 88

You’ve been so focused on AI you’ve missed groundbreaking things like this. It’s sad. :(

88

shortridge@hachyderm.io | @swagitda_

## Slide 89

In software, we’re lucky that we can isolate failure to handle unexpected interactions

89

shortridge@hachyderm.io | @swagitda_

## Slide 90

– or Start “boring”: set AWS security groups use serverless functions, containers, or VMs

90

shortridge@hachyderm.io | @swagitda_

## Slide 91

If a vulnerable component is in a sandbox, the attacker faces a challenge to reach their goal

91

shortridge@hachyderm.io | @swagitda_

## Slide 92

Paved Roads

## Slide 93

## - **Paved roads** : well integrated, supported solutions to common problems that allow humans to focus on their unique value creation

93

shortridge@hachyderm.io | @swagitda_

## Slide 94

Attackers have paved roads, like Cobalt Strike – it makes the easy way the pwnful way.

94

shortridge@hachyderm.io | @swagitda_

## Slide 95

Hyperscale nation states love building platforms and toolchains for their attack ops, too

95

shortridge@hachyderm.io | @swagitda_

## Slide 96

We can adopt a similar approach for protecting our software and systems from attack.

96

shortridge@hachyderm.io | @swagitda_

## Slide 97

- Netflix: Wall E framework turns security requirements into filters to replace checklists

97

shortridge@hachyderm.io | @swagitda_

## Slide 98

Question for when you return to work: What toil are you currently offloading onto your peers?

98

shortridge@hachyderm.io | @swagitda_

## Slide 99

- “The bulk of the ‘going internet facing’ checklist - boiled down to one item: Will you use Wall E?”

99

shortridge@hachyderm.io | @swagitda_

## Slide 100

Block: enabling backend services to securely connect across business unit boundaries

100

shortridge@hachyderm.io | @swagitda_

## Slide 101

III. Systems Thinking

## Slide 102

Attackers think in systems while defenders think in components. It doesn’t have to be this way.

102

shortridge@hachyderm.io | @swagitda_

## Slide 103

Attackers search for your hidden “this will always be true” assumptions…

103 shortridge@hachyderm.io | @swagitda_

## Slide 104

Then they ask, “you say this will always be true; is that the case?” to break those assumptions

104

shortridge@hachyderm.io | @swagitda_

## Slide 105

Attackers target our “this will always be true” assumptions that exist all over our stack.

105

shortridge@hachyderm.io | @swagitda_

## Slide 106

Parsing this string will always be fast

106

shortridge@hachyderm.io | @swagitda_

## Slide 107

Messages on this port will always - be post auth

shortridge@hachyderm.io | @swagitda_

107

## Slide 108

An alert will always fire if a malicious executable appears

108

shortridge@hachyderm.io | @swagitda_

## Slide 109

The attacker thinks, “They say X here, but I can show that it isn’t quite true… interesting. Let’s keep looking to see if they’re just a little wrong or _really_ wrong.”

109

shortridge@hachyderm.io | @swagitda_

## Slide 110

We can adopt a similar process through decision trees and resilience stress testing

110

shortridge@hachyderm.io | @swagitda_

## Slide 111

111 shortridge@hachyderm.io | @swagitda_

## Slide 112

We can refine our mental models continuously rather than waiting for attackers to exploit them

112

shortridge@hachyderm.io | @swagitda_

## Slide 113

113

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(Example) Attack Tree for Cryptominer in a Container
#yolosec
Scan public repos
for keys
Publicly exposed Docker socket
Run Shodan or scanning tool
Schedule their own container Scan public Docker images for keys
Scan for vulnerable web apps Access hosted container service
Exploit a known vuln Schedule a privileged container
. Escape container by
Download cryptominer War writing on host
\GITDA_
```

## Slide 114

Resilience stress tests help us identify the confluence of conditions where failure happens

114 shortridge@hachyderm.io | @swagitda_

## Slide 115

How do disruptions impact the entire system’s ability to recover and adapt?

115

shortridge@hachyderm.io | @swagitda_

## Slide 116

## We can move fast and observe how failure unfolds in our systems through experiments

116

shortridge@hachyderm.io | @swagitda_

## Slide 117

117 shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Firewall?
a)
Misconfigured
port injection
Conf Lo Alert
onjig og e Incident Wait...
Firewall did not detect or block the change on all instances.
Standard Port AAA security policy out of sync on the Portal
Team instances. Port change did not trigger an alert and log
data indicated successful change audit. However, we
unexpectedly learned the configuration management tool
Result: Hypothesis disproved.
caught the change and alerted the SOC.
Figure 2-6. An example security chaos experiment simulating a misconfigured port
injection scenario
```

## Slide 118

118 shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 91/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Endpoint | > Execute relevant malicious actions
Deploy to production Make proposed changes
Figure 9-5. Engineering workflow change evaluation
118 SHORTRIDGE@HACHYDERM.IO | A@SWAGITDA_
```

## Slide 119

Verizon: deploy a pod containing known vulns on a target cluster to test security controls

119

shortridge@hachyderm.io | @swagitda_

## Slide 120

If we adopt this across the industry, vendors now must prove their products work… >:)

120

shortridge@hachyderm.io | @swagitda_

## Slide 121

IV. Tangible Success

## Slide 122

Attackers can measure tangible success and receive immediate feedback on their metrics

122

shortridge@hachyderm.io | @swagitda_

## Slide 123

Do they have access, how much access do they have, and have they accomplished their goals?

123

shortridge@hachyderm.io | @swagitda_

## Slide 124

Defenders struggle to create lucid, actionable metrics that offer immediate feedback

124

shortridge@hachyderm.io | @swagitda_

## Slide 125

CISOs, your “risk coverage” and “time to detect” mean nothing, it’s embarrassing

125

shortridge@hachyderm.io | @swagitda_

## Slide 126

System signals

## Slide 127

## Reliability signals also benefit systems security

127

shortridge@hachyderm.io | @swagitda_

## Slide 128

Who deployed what and when? (like orchestrator and deployment logs)

128

shortridge@hachyderm.io | @swagitda_

## Slide 129

Who accessed what and when? (like cloud audit data)

129

shortridge@hachyderm.io | @swagitda_

## Slide 130

netflow
Database logs, billing records,  ,
production crash dumps, error messages…

130

shortridge@hachyderm.io | @swagitda_

## Slide 131

Traditional infosec doesn’t measure load, latency, performance, or throughput (a mistake)

131

shortridge@hachyderm.io | @swagitda_

## Slide 132

## e.g. high CPU usage and memory shortages are signals about systems security

132

shortridge@hachyderm.io | @swagitda_

## Slide 133

- Well resourced attackers will monitor the system they’re attacking to avoid hitting limits or alarms

133

shortridge@hachyderm.io | @swagitda_

## Slide 134

## Experiments can reveal what signals you _should_ – be collecting don’t take visibility for granted

134

shortridge@hachyderm.io | @swagitda_

## Slide 135

So, what system signals can indicate attacks? bffs… Turns out SREs and DevOps are our

135

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
So, what system signals can indicate attacks?
Turns out SREs and DevOps are our bffts...
135 SHORTRIDGE@MHACHYDERM.IO | @SWAGITDA__
```

## Slide 136

Accept queue depth: attacker hijacking system execution (T1574) or process hollowing (T1055)

136

shortridge@hachyderm.io | @swagitda_

## Slide 137

## Autoscale replica count: lateral movement (T1072); cryptomining; brute forcing (T1110)

137

shortridge@hachyderm.io | @swagitda_

## Slide 138

## Billing alerts: cloud priv escalation (T1078); - crypto mining (T610); querying data for recon

138

shortridge@hachyderm.io | @swagitda_

## Slide 139

Cache hit rate (CHR): DoS; data exfiltration (T1567); brute forcing

139

shortridge@hachyderm.io | @swagitda_

## Slide 140

Disk usage, throughput, & IOPS: ransomware (T1486); staging data for exfiltration (T1074)

140

shortridge@hachyderm.io | @swagitda_

## Slide 141

DNS lookup errors: lateral movement, C&C, data exfil (T1071.004); DoS for ransom (T1498)

141

shortridge@hachyderm.io | @swagitda_

## Slide 142

Error rate: credential stuffing (T1110) or DoS
142 shortridge@hachyderm.io | @swagitda_

## Slide 143

Heartbeat response: endpoint DoS (T1499); restricting connections for evasion (T1562)

143

shortridge@hachyderm.io | @swagitda_

## Slide 144

## Rate limit availability: SSRF (T1190); brute force logins (T1110)

144

shortridge@hachyderm.io | @swagitda_

## Slide 145

Replication lag: unauthorized access or modification (T1565); exploiting inconsistencies

145

shortridge@hachyderm.io | @swagitda_

## Slide 146

Resource consumption creeping towards max levels (CPU, memory): cryptominers; hijacking - resources (T1496); in memory attacks (T1055)

146

shortridge@hachyderm.io | @swagitda_

## Slide 147

## Response time: DoS; unreliable exploit (T1190)

147

shortridge@hachyderm.io | @swagitda_

## Slide 148

Swap usage: data exfiltration (T1074.001)

148

shortridge@hachyderm.io | @swagitda_

## Slide 149

System log lag: stopping or deleting logs to conceal attack operations (T1070)

149

shortridge@hachyderm.io | @swagitda_

## Slide 150

We need our feedback loops to give us immediate sensory input like attackers get

150

shortridge@hachyderm.io | @swagitda_

## Slide 151

# Viva ~~Las Vegas~~ la Révolution

## Slide 152

We can outmaneuver attackers by becoming nimble, curious, and empirical as well

152

shortridge@hachyderm.io | @swagitda_

## Slide 153

We can adopt a faster tempo via Configuration as Code (CaC) and automation like CI/CD

153

shortridge@hachyderm.io | @swagitda_

## Slide 154

- We can pursue design based solutions with our Ice Cream Cone Hierarchy and Paved Roads

154

shortridge@hachyderm.io | @swagitda_

## Slide 155

We can adopt systems thinking, challenging our “this will always be true” assumptions

155

shortridge@hachyderm.io | @swagitda_

## Slide 156

We can cultivate tangible success outcomes that leverage system signals for immediate feedback

156

shortridge@hachyderm.io | @swagitda_

## Slide 157

We can fuel a feedback loop to gracefully respond to attacks and adapt as attackers evolve

157

shortridge@hachyderm.io | @swagitda_

## Slide 158

And that, comrades, is the resilience revolution.

158 shortridge@hachyderm.io | @swagitda_

## Slide 159

## Order the book today: <u>Amazon Bookshop</u>

& other major retailers

159

shortridge@hachyderm.io | @swagitda_


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Security Chaos
Order the book today: Engineering
Sustaining Resilience in Software and Systems
Amazon
Bookshop
& other major retailers
Kelly Shortridge
with Aaron Rinehart
159 SHORTRIDGE@HACHYDERM.IO | A@SWAGITDA_
```

## Slide 160

/in/kellyshortridge @swagitda_ shortridge@hachyderm.io @shortridge.bsky.social chat@shortridge.io

160

shortridge@hachyderm.io | @swagitda_
