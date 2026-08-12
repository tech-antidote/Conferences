---
title: "Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks"
speakers: ["Raphael Silva"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Raphael Silva - Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks - v1.pdf"
pages: 27
sha256: "a464407d79a335be78cd6e3f436743f753f09276a938a347223dbc544175b5cf"
text_chars: 12615
ocr_pages: 20
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.6
ocr_unreliable_blocks: 0
content_note: "All 27 pages were rendered and read against the source PDF by a vision model; 25 were rewritten and 2 confirmed correct. The ocr_* fields describe the superseded first-pass extraction."
vision_verified_pages_changed: 25
vision_verified_pages: 27
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:40:51Z"
---
# Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks

**Speakers:** Raphael Silva  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Raphael Silva - Install Me Maybe Turning Claimable VS Code Extension IDs into Supply-Chain Attacks - v1.pdf` (27 pages)


## Slide 1

# INSTALL ME MAYBE

Turning claimable VS Code extension IDs into supply-chain attacks

Raphael Silva
Security Researcher @ Aikido Security

## Slide 2

# INTRODUCTION

$ whoami

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

**PACKAGE.JSON**

```json
{
  "publisher": "ms-python",
  "name": "python",
  "activationEvents": [
    "onStartupFinished"
  ],
  "extensionDependencies": [ "…" ]
}
```

## Slide 5

# SILENT TRIGGERS: ACTIVATIONEVENTS & SCRIPTS

- onStartupFinished

- onLanguage

- * – fires at every IDE launch

- …

```json
],
"activationEvents": [
    "*"
],
```

```text
[info] ExtensionService#_doActivateExtension Expressjs.expressjs-session, startup: false, activationEvent: '*'
```

## Slide 6

# DEPENDENCIES

- NPM

- GitHub

- URL

- Local

- …

```json
},
"dependencies": {
  "express": "^4.18.2",
  "expressjs-session": "^4.4.0"
},
"devDependencies": {
  "@types/vscode": "^1.100.0",
  "@types/mocha": "^10.0.10",
  "@types/node": "20.x",
  "eslint": "^9.25.1",
  "@vscode/test-cli": "^0.0.10",
  "@vscode/test-electron": "^2.5.2"
}
```

```json
{
  "name": "foo",
  "version": "0.0.0",
  "dependencies": {
    "express": "expressjs/express",
    "mocha": "mochajs/mocha#4727d357ea",
    "module": "user/repo#feature\/branch"
  }
}
```

```json
},
"dependencies": {
  "express": "https://expressjs.com/",
```

## Slide 7

# THE MAGIC STRING

```json
// .vscode/extensions.json
{
  "recommendations": [
    "ms-python.python"
  ]
}
```

## Slide 8

# WHAT IS PUBLISHER.EXTENSION REALLY?

**PUBLISHER**

`ms-python`

A namespace on a marketplace.
Owned by an account. Marketplace-specific.

**EXTENSION NAME**

`python`

The actual package, declared in `package.json`.
A different person can publish the same name elsewhere.

**THE CATCH**

Looks portable but the **identity is marketplace-specific.**

## Slide 9

# AN EXTENSION IS A LONG-LIVED PROCESS INSIDE YOUR EDITOR.

**SEES**

Workspace files. Open buffers. Project tree.

**TOUCHES**

Terminals. Tasks. Debug sessions. Git.

**READS**

Env vars. `~/.aws`. `~/.ssh`. Local files.

**RUNS IN**

Local. WSL. SSH remote. Devcontainer.

Secrets, source code, etc...

## Slide 10

# SAME STRING. DIFFERENT REGISTRY.

**REGISTRY A**

**VS Code Marketplace**

Microsoft-operated.
Used by stock VS Code.
~70k extensions.

`publisher.extension` — OWNED

≠

**REGISTRY B**

**Open VSX**

Eclipse Foundation.
Used by VS Code-derived editors.
Different namespace ledger.

`publisher` — UNCLAIMED

## Slide 11

# A FAMILIAR FACE?

**2021 · ALEX BIRSAN**

**Dependency confusion in package managers.**

Internal package name → resolved through public registry → attacker had published a higher version. Code execution at Apple, Microsoft, PayPal, dozens more.

**2026 · THIS TALK**

**Dependency confusion for editor extensions.**

Trusted extension ID → resolved through a registry that doesn’t have it → attacker claims the namespace. Code execution in developer environments.

Same primitive, aimed somewhere new. This time what gets confused is a publisher namespace.

## Slide 12

# NAME-TAKEOVER, MEET DEPENDENCY CONFUSION.

**FAMILY A**

**Name takeover**

Trusted reference → unowned namespace. Examples: dangling GitHub Apps, npx confusion, GitHub RepoJacking.

**FAMILY B**

**Dependency confusion**

Same name in multiple registries. The tool picks the wrong one. Birsan 2021.

**INTERSECTION**

**Extension Confusion**

The trusted name *and* the claimable namespace meet in editor tooling.

## Slide 13

# THE ATTACK MODEL

**[ 01 ] Trusted reference**

A workflow names `publisher.extension`.

**[ 02 ] Wrong registry resolves it**

Editor / sync tool checks a registry that doesn't have it.

**[ 03 ] Namespace is unclaimed**

Publisher exists nowhere on the target registry.

**[ 04 ] Attacker registers it**

No proof of ownership against the other registry required.

**[ 05 ] Attacker publishes the ID**

Same name. Same shape. Different author.

**[ 06 ] Install path triggers**

Recommendation · devcontainer · sync · manual · auto-update.

**[ 07 ] Code executes**

On a real developer environment with real privileges.

## Slide 14

# WHERE IDS TRAVEL 1/5

### .vscode/extensions.json

**.VSCODE/EXTENSIONS.JSON**

```json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "internal-team.lint-helper"
  ]
}
```

**Lowest (but still some) friction install path in the editor.**

- Opening the repo prompts to install.

- Lives in the repo — forks, merges, gets copy-pasted.

- Rarely audited like a dependency file.

- Lives in `.code-workspace` and team templates too.

## Slide 15

### WHERE IDS TRAVEL 2/5

**.devcontainer/devcontainer.json**

**DEVCONTAINER.JSON**

```json
{
  "image": "mcr.microsoft.com/devcontainers/python:3",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "acme-corp.deploy-tools"
      ]
    }
  }
}
```

**Open repo. Start container. You’re done.**

- Extension install becomes part of **trusted bootstrap**.
- Container resolution may differ from local.
- Often runs unattended — codespaces, remote dev hosts.

## Slide 16

### WHERE IDS TRAVEL 3/5

**Setup scripts & onboarding docs.**

**SCRIPTS/BOOTSTRAP.SH**

```bash
#!/usr/bin/env bash
# Set up dev env for new joiners

EXTS=(
  ms-vscode.cpptools
  redhat.vscode-yaml
  internal.platform-helper     # written 2021, no one remembers why
)

for e in "${EXTS[@]}"; do
  code --install-extension "$e" --force
done
```

**The kind of file nobody reviews.**

- Bootstrap scripts. `README.md` install lists.
- Devbox / Nix / Docker base images.
- Wiki onboarding pages. Slack pins.
- Internal “recommended extensions” sheets that nobody updates.

`Stale references age into install paths.`

## Slide 17

### WHERE IDS TRAVEL 4/5

**IDE migration. Settings sync. Forks.**

**EDITOR MIGRATION / IMPORT**

“Bring my extensions from VS Code.” The source list assumes Microsoft’s registry. The destination differs.

**SETTINGS SYNC**

Cloud sync carries extension lists across machines, accounts, and sometimes editor variants.

**THIRD-PARTY SYNC TOOLS**

Community scripts and dotfiles. Stale identifiers from years ago, on every laptop.

**SPECIFIC NOTE**

**Cursor** looked more defensive in the missing-extension import flow I tested. The broader marketplace fragmentation issue still applies across other editors, sync tools, and devcontainer paths.

`Convenience flows are trust boundaries with the safety off.`

## Slide 18

### WHERE IDS TRAVEL 5/5

**And then auto-updates make it worse.**

- A claimable ID gets imported / synced / installed once.
- Attacker registers the namespace later.
- Attacker publishes `v1.0.0` → `v1.0.1`.
- The editor pulls the higher version. **Silently.**
- Remove from marketplace later? Already installed copies stay.

```json
// What the editor sees
"acme-corp.deploy-tools": "^1.0.0"
// What gets installed today
attacker → "1.0.1"   ✓ auto-update
```

`Removal ≠ remediation. The installed copy keeps executing.`

## Slide 19

### WHERE IDS TRAVEL 5/5

**Scan, check, score. Twice.**

**PHASE 01 · DISCOVERY**

- Public repo & setup-file sweeps for `publisher.extension` references.
- Existence check against the registry the target actually resolves through.
- Namespace claimability check (publisher present? owner active? ownership cross-verified?).
- Prioritize by prevalence, install counts, workflow context, org relevance.

**PHASE 02 · COMPARISON**

- Top-N VS Marketplace extensions × Open VSX availability.
- Top 5k → narrow but high-signal slice.
- Top 20k → the part that got uncomfortable.
- No exploitable lists, no scanner logic published.

## Slide 20

### RESULTS FROM SCANNING

**Not just the long tail.**

| TOP 5,000 | TOP 20,000 |
| --- | --- |
| **2,560** — CLAIMABLE COMBOS | **14,628** — CLAIMABLE COMBOS |
| **2,325** — UNIQUE NAMESPACES | **12,353** — UNIQUE NAMESPACES |
| **~330M** — VS MARKETPLACE INSTALLS TIED TO VULN ENTRIES | **~420M** — VS MARKETPLACE INSTALLS TIED TO VULN ENTRIES |

## Slide 21

### ENM - ETHICAL NON-MALWARE

**Strict ethics. Minimum metadata.**

**COLLECTED — ATTRIBUTION ONLY**

- [✓] Timestamp, IP, forwarded-for
- [✓] User agent, editor name + version
- [✓] Extension install path
- [✓] Remote context flag (`local` / `WSL` / `SSH` / `devcontainer`)
- [✓] Git email domain, git remote (when present)
- [✓] Host / user clues when available

**NEVER COLLECTED**

- [ ] Source files, code, or repo content
- [ ] Tokens, credentials, secrets
- [ ] Shell command output
- [ ] Environment variable values
- [ ] Persistence, post-exploitation, lateral movement
- [ ] Anything beyond proving execution

## Slide 22

### WHAT DID THE CALLBACKS LOOK LIKE?

**This is what disclosure was built on.**

**CALLBACK.JSON (REDACTED)**

```json
{
  "ts":        "2026-03-1█T0█:42:1█Z",
  "ip":        "███.███.█.███",
  "editor":    "any-vscode-fork/1.█.█",
  "ext_path":  "/home/█████/.any-vscode-fork/extensions/publisher.extension-1.0.0",
  "remote":    "local",
  "git_email": "█████@evil-corp.com",
  "git_remote": "github.com/evil-corp/██████████",
  "user":      "██████",
  "host":      "EC-laptop-██████"
}
```

**SIGNALS THAT MATTERED**

- Corporate git email domain
- Corporate git remote
- Repeated host / user pairs
- Editor metadata (variant + version)
- Remote-context flag (WSL / SSH / devcontainer)

`IP alone was noisy. Stack the signals.`

## Slide 23

### END RESULTS

**ACROSS THE RESEARCH**

**1,100,000+**

callbacks from real developer environments.

## Slide 24

### END RESULTS

**By the numbers.**

| TOTAL CALLBACKS | DISTINCT IPS | COUNTRIES |
| --- | --- | --- |
| **1,100,000+** | **110,000+** | **160+** |
| From the PoC extensions under claimable IDs. | 17,255 distinct hosts. | Pretty much everywhere |

| REPORTS / DISCLOSURES | BOUNTIES SO FAR | TOP-20K CLAIMABLE COMBOS |
| --- | --- | --- |
| **200+** | **$200k+** | **14,628** |
| BBPs, VDPs & direct contacts. | Multiple programs. Still climbing. | ~420M VS Marketplace installs tied to them. |

## Slide 25

# TO BE FINISHED

- Mitigations

- Bug Bounty Programs responses (lots of positive ones and some negatives)

- MAJOR ETHICAL DISCLAIMER. This research ended up getting a bit out of hand and some ethical boundaries are muddied. If I were to redo it I’d be much more careful about unintended fallout. All in all the responses from the programs were positive in general but it could have gone a different way as well.

- How the marketplaces are dealing with this now (Microsoft ignoring and Open VSX putting a band aid on it).

## Slide 26

### BUT HOW PREVALENT IS IT?

*Collage of four news-article screenshots.*

**SECURING THE CLOUD** · MAY 16, 2023

VSCode Security: Malicious Extensions Detected- More Than 45,000 Downloads- PII Exposed, and Backdoors Enabled

By Ori Abramovsky, Head Of Data Science, Cloud Security

Malicious VSCode extensions with millions of installs discovered

By **Bill Toulas**

June 9, 2024 · 10:22 AM · 7

VSCode extensions found downloading early-stage ransomware

By **Bill Toulas**

March 20, 2025 · 03:54 PM · 0

**RL Blog**

Threat Research | April 3, 2024

Malicious helpers: VS Code Extensions observed stealing sensitive information

## Slide 27

### INSTALL ME MAYBE

Turning claimable VS Code extension IDs into supply-chain attacks

@0x_rcss

raphaelcssilva

Raphael Silva

Security Researcher @ Aikido Security

*X and LinkedIn icons sit above the two handles; a circuit-board “34” skull logo fills the right side.*

