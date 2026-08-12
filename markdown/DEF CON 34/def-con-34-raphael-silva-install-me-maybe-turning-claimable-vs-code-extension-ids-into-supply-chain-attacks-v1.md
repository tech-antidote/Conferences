---
title: "Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks"
speakers: ["Raphael Silva"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Raphael Silva - Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks - v1.pdf"
pages: 27
sha256: "a464407d79a335be78cd6e3f436743f753f09276a938a347223dbc544175b5cf"
text_chars: 10288
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:26:33Z"
---
# Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks

**Speakers:** Raphael Silva  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Raphael Silva - Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks - v1.pdf` (27 pages)

## Slide 1

Turning claimable VS Code extension IDs into supply-chain attacks

Raphael Silva Security Researcher @ Aikido Security

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
TNSTALL Me MARE
Turning claimable VS Code extension IDs into
supply-chain attacks
Raphael Silva
Security Researcher @ Aikido Security
```

## Slide 2

# INTRODUCTION

- $ whoami

- Security Researcher @ Aikido Security

- Focus on malware and SCS vulnerability research

- Like to hack sh!t on my free time

@0x_rcss

aikido.dev

raphaelcssilva

## Slide 3

# WHY VS CODE IS AN ATTACKER’S DREAM

- Massive reach (in ~75 % of developer desktops)

- Anyone can publish

- Auto-updates

- Trust signals are flimsy

- Full IDE privileges

- Forks like **Cursor** , **Windsurf** , **Antigravity** , etc. already make up **18–22%** of market share.

## Slide 4

# VS CODE EXTENSION ANATOMY

- Javascript Project

- Packaged as .vsix. A glorified ZIP that VS Code unpacks into the user profile

- Manifest-driven – package.json (name, publisher, version, scripts, dependencies, etc)

- activationEvents (when does the extension run?)

   - onStartupFinished

   - onLanguage

   - *

- Dependencies

- extensionPack, extensionDependencies

## Slide 5

## SILENT TRIGGERS: ACTIVATIONEVENTS & SCRIPTS

### • onStartupFinished

- onLanguage

- * – fires at every IDE launch

## Slide 6

# DEPENDENCIES

- NPM

- GitHub

- URL

- Local

- …

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
J,
DEPENDENCIES ocpress: 74.4
"express ]s-session”:
yr
“devDependencies”:
"@types/vscode":
* NPM "@types/mocha”:
. “@types/node":
* GitHub "eslint”: 9 1",
“@vscode/test-cli":
* URL “@vscode/test-electron”:
* Local
e
"name":
“version”:
“dependencies”: {
"express":
J,
“dependencies”:
“mocha” :
“module”:
"express": “htt
```

## Slide 7

THE MAGIC STRING

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE MAGIC STRING
{
"recommendations": [
"ms-python.python"
]
}
```

## Slide 8

WHAT IS PUBLISHER.EXTENSION REALLY?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT IS PUBLISHER.EXTENSION REALLY?
PUBLISHER EXTENSION NAME
A namespace on a marketplace. The actual package, declared in package. json.
Owned by an account. Marketplace-specific. A different person can publish the same name elsewhere.
THE CATCH
Looks portable but the identity is marketplace-specific. eS eS
```

## Slide 9

AN EXTENSION IS A LONG-LIVED PROCESS INSIDE YOUR EDITOR **.**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AN EXTENSION IS A LONG-LIVED PROCESS INSIDE
YOUR EDITOR.
Workspace files. Open Terminals. Tasks. Debug Env vars. ~/.aws.~/.ssh. Local. WSL. SSH remote.
buffers. Project tree. sessions. Git. Local files. Devcontainer.
Secrets, source code, etc...
```

## Slide 10

SAME STRING. DIFFERENT REGISTRY.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SAME STRING. DIFFERENT REGISTRY.
VS Code Marketplace
Microsoft-operated.
Used by stock VS Code.
pubLlisher.extension
Open VSX
Eclipse Foundation.
Used by VS Code-derived editors.
publisher
```

## Slide 11

# A FAMILIAR FACE?

Same primitive, aimed somewhere new. This time what gets confused is a publisher namespace.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A FAMILIAR FACE?
2021 - ALEX BIRSAN 2026 + THIS TALK
Dependency confusion in package Dependency confusion for editor
managers. extensions.
Internal package name ~ resolved through public registry > Trusted extension ID — resolved through a registry that doesn’t
attacker had published a higher version. Code execution at Apple, have it > attacker claims the namespace. Code execution in
Microsoft, PayPal, dozens more. developer environments.
Same primitive, aimed somewhere new. This time what gets confused is a publisher namespace.
```

## Slide 12

NAME-TAKEOVER, MEET DEPENDENCY CONFUSION.

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
NAME-TAKEOVER, MEET DEPENDENCY CONFUSION.
FAMILY
Name takeover
Trusted reference ~ unowned namespace.
Examples: dangling GitHub Apps, npx
confusion, GitHub RepoJacking.
FAMILY B
Dependency confusion
Same name in multiple registries. The too
picks the wrong one. Birsan 2021.
INTERSECTION
Extension Confusion
The trusted name and the claimable
namespace meet in editor tooling.
```

## Slide 13

THE ATTACK MODEL

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
THE ATTACK MODEL
Trusted
reference
A workflow names
publisher.extension.
Wrong registry
resolves it
Editor / sync tool
checks a registry
that doesn't have
it.
03 J
Namespace is
unclaimed
Publisher exists
nowhere on the
target registry.
Attacker
registers it
No proof of
ownership against
the other registry
required.
]
Attacker
publishes the
ID
Same name. Same
shape. Different
author.
Install path
triggers
Recommendation -
devcontainer - sync
* Manual - auto-
update.
Code executes
On a real developer
environment with
real privileges.
```

## Slide 14

WHERE IDS TRAVEL 1/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 1/5
. vscode/extensions. json
Lowest (but still some) friction
install path in the editor.
{ ~ Opening the repo prompts to install.
Hip mmendations": . .
ecommendatio . [ ~ Lives in the repo — forks, merges, gets copy-pasted.
"esbenp.prettier-vscode",
"dbaeumer.vscode-eslint", ~ Rarely audited like a dependency file.
“internal-team.lint-helper " ~ Livesin .code-workspace and team templates too.
]
}
```

## Slide 15

WHERE IDS TRAVEL 2/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 2/5
.devcontainer/devcontainer. json
Open repo. Start container. You’re done.
~ Extension install becomes part of trusted bootstrap.
{
"image": "mcr.microsoft.com/devcontainers/python:3",
"customizations": { ~ Often runs unattended — codespaces, remote dev hosts.
"vscode": {
"extensions": [
~ Container resolution may differ from local.
"ms-python.python",
"acme-corp.depLloy-tools "
]
}
}
```

## Slide 16

WHERE IDS TRAVEL 3/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 3/5
Setup scripts & onboarding docs.
The kind of file nobody reviews.
~ Bootstrap scripts. README .md install lists.
~ Devbox / Nix / Docker base images.
~ Wiki onboarding pages. Slack pins.
EXTS=(
~ Internal “recommended extensions” sheets that
ms-vscode.cpptools
redhat. vscode-yaml nobody updates.
internal.platform-helper # written 2021, no one remembers why .
) Stale references age into install paths.
for e in "${EXTS[@]}"; do
code --install-extension "$e" --force
done
```

## Slide 17

WHERE IDS TRAVEL 4/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 4/5
IDE migration. Settings sync. Forks.
EDITOR MIGRATION / IMPORT
“Bring my extensions from VS Code.” The source list
assumes Microsoft’s registry. The destination differs.
SPECIFIC NOTE
Cursor looked more defensive in the missing-
SETTINGS SYNC extension import flow | tested. The broader
Cloud sync carries extension lists across machines, marketplace fragmentation issue still applies across
accounts, and sometimes editor variants. other editors, sync tools, and devcontainer paths.
Convenience flows are trust boundaries with the safety off.
THIRD-PARTY SYNC TOOLS
Community scripts and dotfiles. Stale identifiers from years
ago, on every laptop.
```

## Slide 18

WHERE IDS TRAVEL 5/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 5/5
And then auto-updates make it worse.
~ Aclaimable ID gets imported / synced / installed
once.
// What the editor sees
"acme-corp.deploy-tools": "41.0.0"
~ Attacker publishes v1.0.0 > v1.0.1. // What gets installed today
attacker > "1.0.1" v auto-update
~ Attacker registers the namespace later.
~ The editor pulls the higher version. Silently.
~ Remove from marketplace later? Already installed
. Removal # remediation. The installed co keeps executing.
copies stay. py weep 8
```

## Slide 19

WHERE IDS TRAVEL 5/5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHERE IDS TRAVEL 5/5
Scan, check, score. Twice.
Public repo & setup-file sweeps for
publisher.extension references.
Existence check against the registry the target actually
resolves through.
Namespace claimability check (publisher present? owner
active? ownership cross-verified?).
Prioritize by prevalence, install counts, workflow context,
org relevance.
\RISON
Top-N VS Marketplace extensions x Open VSX availability.
Top 5k > narrow but high-signal slice.
Top 20k —> the part that got uncomfortable.
No exploitable lists, no scanner logic published.
```

## Slide 20

RESULTS FROM SCANNING

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RESULTS FROM SCANNING
Not just the long tail.
2,560 2,325 14,628 12,353
~330M ~A20M
```

## Slide 21

ENM - ETHICAL NON-MALWARE

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ENM - ETHICAL NON-MALWARE
Strict ethics. Minimum metadata.
COLLECTED — ATTRIBUTION ONLY
[v] Timestamp, IP, forwarded-for
[v] User agent, editor name + version
[v] Extension install path
[v] Remote context flag (Local / WSL / SSH /
devcontainer)
[v] Git email domain, git remote (when present)
[v] Host / user clues when available
NEVER COLLECTED
[ ] Source files, code, or repo content
[ ] Tokens, credentials, secrets
[ ] Shell command output
[ ] Environment variable values
[ ] Persistence, post-exploitation, lateral movement
[ ] Anything beyond proving execution
```

## Slide 22

WHAT DID THE CALLBACKS LOOK LIKE?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WHAT DID THE CALLBACKS LOOK LIKE?
This is what disclosure was built on.
"ts":
"ip":
"editor":
"ext_path":
"remote":
"git_email":
"git_remote":
"user":
"host":
(REDACTED)
SIGNALS THAT MATTERED
~ Corporate git email domain
"2026-03-1§§T OM: 42:1gj2", ~ Corporate git remote
y 8 8B ~ Repeated host / user pairs
"any-vscode-fork/1.9.—", ~ Editor metadata (variant + version)
"/home// . any-vscode-fork/extensions/ publisher.extension -1.0.0",
- Remote-context flag (WSL / SSH /
"Local", i
: devcontainer)
“IBMMMG evil-corp.com",
"github.com/evil-corp/xx iii! ",
‘Zz, IP alone was noisy. Stack the
"EC-Laptop - ag" signals.
```

## Slide 23

END RESULTS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
END RESULTS
ACROSS THE RESEARCH
4, 100,000+
callbacks from real developer environments.
```

## Slide 24

END RESULTS

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
END RESULTS
By the numbers.
TOTAL CALLBACKS DISTINCT IPS COUNTRIES
1,100,000+ 11.0,000+ 160+
From the PoC extensions under claimable
IDs. 17,255 distinct hosts.
Pretty much everywhere
REPORTS / DISCLOSURES BOUNTIES SO FAR TOP-20K CLAIMABLE COMBOS
200+ $200k+ 14,628
BBPs, VDPs & direct contacts. Multiple programs. Still climbing. =420MNS)Marketplace)installs\tied|to|them:
```

## Slide 25

# TO BE FINISHED

- Mitigations

- Bug Bounty Programs responses (lots of positive ones and some negatives)

- MAJOR ETHICAL DISCLAIMER. This research ended up getting a bit out of hand and some ethical boundaries are muddied. If I were to redo it I’d be much more careful about unintended fallout. All in all the responses from the programs were positive in general but it could have gone a different way as well.

- How the marketplaces are dealing with this now (Microsoft ignoring and Open VSX putting a band aid on it).

## Slide 26

# BUT HOW PREVALENT IS IT?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
B U T H OW VSCode Security:
Malicious Extensions
PREVALE NT IS Detected- More Than
45,000 Downloads-
|T? Pil Exposed, and
Backdoors Enabled
@ va
Malicious VSCode extensions with
millions of installs discovered
By Bill Toulas
[A June9,2024 GJ 10:22AM M7
VSCode extensions found
downloading early-stage
RL Blog ransomware
Malicious helpers: VS Code Extensions
observed stealing sensitive information
By Bill Toulas
March 20,2025 %} 03:54PM Mo
```

## Slide 27

Turning claimable VS Code extension IDs into supply-chain attacks

@0x_rcss

raphaelcssilva

Raphael Silva Security Researcher @ Aikido Security
