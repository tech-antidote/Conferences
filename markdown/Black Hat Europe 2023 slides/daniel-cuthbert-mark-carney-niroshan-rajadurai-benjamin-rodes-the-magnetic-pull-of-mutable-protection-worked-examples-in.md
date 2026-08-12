---
title: "The Magnetic Pull of Mutable Protection Worked Examples in Cryptographic Agility"
speakers: ["Daniel Cuthbert", "Mark Carney", "Niroshan Rajadurai", "Benjamin Rodes"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Daniel Cuthbert, Mark Carney, Niroshan Rajadurai, Benjamin Rodes_The Magnetic Pull of Mutable Protection Worked Examples in Cryptographic Agility.pdf"
pages: 47
sha256: "e657c9c35de322bc06d033bd9af09ee18fff94feb6c6a88104a2cae6decb9bcf"
text_chars: 10424
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:01:56Z"
---
# The Magnetic Pull of Mutable Protection Worked Examples in Cryptographic Agility

**Speakers:** Daniel Cuthbert, Mark Carney, Niroshan Rajadurai, Benjamin Rodes  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Daniel Cuthbert, Mark Carney, Niroshan Rajadurai, Benjamin Rodes_The Magnetic Pull of Mutable Protection Worked Examples in Cryptographic Agility.pdf` (47 pages)


## Slide 1

\```
Daniel Cuthbert | Mark Carney | Benjamin Rodes | Niroshan Rajadurai
December 2023
\```

Information Classification: General

## Slide 2

## Hello

Daniel “Marty” Cuthbert Global Head of Security Research

Benjamin “Whistler” Rodes

Mark “Mother” Carney

Senior Researcher, CTO @ Quantum Village

Niroshan “Donald” Rajadurai

Principal Security Engineer, Microsoft

Sr. Director, GitHub Advanced Security & AI

Information Classification: General

## Slide 3

Crypto != Cryptography

Information Classification: General

## Slide 4

Information Classification: General

## Slide 5

Information Classification: General

## Slide 6

## So why does this matter?

Information Classification: General

## Slide 7

## **RFC** 132 **0** 615

Information Classification: General

## Slide 8

grep -r -E '\b([Hh][Mm][Aa][Cc]-)?[Mm][Dd]5\b' /supersecurecode/*

Information Classification: General

## Slide 9

## Why do we have this?

From: LogJam-CVSS-of-4.0-honestplease-fix-me-draft-draft-FINAL.docx

To: Quantum computing

Information Classification: General

## Slide 10

Q-Day is coming...

Information Classification: General

## Slide 11

## APRIL 14, 2030

Information Classification: General Source: cloudsecurityalliance.org

## Slide 12

What does that mean for cryptography?

Information Classification: General

## Slide 13

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Quantum vs. Classical Hardness
= Classical Bruteforce Quantum Bruteforce Quantum Factoring == Classical Factoring
1000000
100000
= 10000
a
a
6
= 1000
100
10
1
0 50 100 150 200
Number of Bits to be Computed Over
```

## Slide 14

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
China Telecom's Internet Traffic Misdirection
Routing leak sent US domestic traffic through China
Los Angeles, CA
Eastern Asia
INTERNET | ORACLE
NTELLIGENCE | Cloud Infrastructure
```

## Slide 15

“It’s all about the information”

Information Classification: General

## Slide 16

Yr ‘23 ‘24 ‘25 ‘26 ‘27 ‘28 ‘29 ‘30 ‘31 ‘32 ‘33 ‘34 …
~8yrs to Q-Day; 14th April 2030**
UK Police
Commercial Data
Tax Records
~4yrs to implement
PQC/other solutions Financial Records
Government Records
Mortgages/Gov’t Bonds     (digital signatures) - 30-50yrs

Information Classification: General

## Slide 17

So we have to prepare for tomorrow today

Information Classification: General

## Slide 18

**LOCATE**

Creating an environment for cryptographic agility

**COMPARE**

**DETERMINE**

**REPLACE**

**MONITOR**

Information Classification: General

## Slide 19

## Where do we start?

Information Classification: General

## Slide 20

**LOCATE**

Focus on cryptographic agility, the rest will follow

**COMPARE**

**DETERMINE**

**REPLACE**

**MONITOR**

Information Classification: General

## Slide 21

“describes steps for agencies to undertake as they begin their transition to PQC [post quantum cryptography] by conducting a prioritized inventory of cryptographic systems.” White House Memorandum M-23-02

Information Classification: General

## Slide 22

# CBOM

(Cryptographic Bill Of Materials)

A record containing the details of various cryptographic software components used in a software system

Information Classification: General

## Slide 23

### Why is CBOM Generation Complex?

\```
01
\```

API Variability What’s the “space” of possibilities?

`02` Data Flow Complexity

How do we analyze this space?

> `03` Cryptography Abstractions & Modeling APIs

How do we codify ( _model_ ) the analysis for each API use?

Information Classification: General

## Slide 24

### Data Flow Example: Finding Key Gen Config

May be from multiple sources or “unknown” Trace data to this to variable to find key size

Information Classification: General

## Slide 25

### Data Flow Example: Finding Default Configuration

The set rsa_keygen_bits_ operation is not required! Does an rsa_keygen_bits result flow here? If not, what algorithm does CTX represent? This algorithm would have a default/unknown key size.

Information Classification: General

## Slide 26

#### CodeQL

GitHub’s static analysis engine powered by curated custom queries to hunt for vulnerabilities in your code

Supports a wide range of languages C/C++, C#, Go, Java, Kotlin, JavaScript, Python, Ruby, Swift, TypeScript

###### Robust static analyses

Including interprocedural data flow

Works at scale

Open source

Information Classification: General

## Slide 27

### How CodeQL works

CodeQL Analysis Pipeline
Database
code base turns code  extractor into data exprs... ... stmts what to look for query model key concepts libraries
...
...
...
stores code as data...
...        ...
Results
(SARIF, CSV, ..)

Information Classification: General

## Slide 28

Simple, informative queries leveraging cryptography abstractions

Leveraging CodeQL for CBOM Generation

Abstract Class

Information Classification: General

## Slide 29

##### Unlocking additional information becomes trivial

Same abstractions used for CBOM

Added threshold of an _‘acceptable’_ size threshold (alerts if the size is <2048)

Information Classification: General

## Slide 30

### Cryptography Modeling Architecture

Query
Repository
- CBOM queries
- Vuln alert queries
- …
Instantiations of
abstractions
Think abstract classes
and interfaces
Crypto API Model Instantiations Crypto Model Framework
Instantiates
- Algorithm & operation abstractions
- Code patterns mapped to abstractions
- Normalized algorithm names
Defined Per Crypto API Predefined
Language & API Specific Language & API Agnostic

Information Classification: General

## Slide 31

### Connecting the pieces

Start with our why

Source the information

Transform it to provide meaningful context

Information Classification: General

## Slide 32

Information Classification: General

## Slide 33

Information Classification: General

## Slide 34

Understanding Variant Analysis
Advanced
CodeQL
Security
Monitor
Security bug Diagnose Codify
continuously
Improve
query
Discover  Prevent
Pen testing variants future bugs
Bug bounty program
Audit logs
Fix  Fix Fix in code
original bug variants review
Traditional Security Research Variant analysis w/ GitHub Advanced Security

Information Classification: General

## Slide 35

Threat hunt at scale

GitHub’s CodeQL Multi Repository Variant Analysis (MRVA)

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> codeq! (Workspace)
CommandinjectionSinks.ql
> DATABASES
LANGUAGE
> AST VIEWER @name Command Injection
@description Command Injection sinks
@kind problem
QUERY HISTORY
VARIANT ANALYSIS REPOSITORIES { 5 d java/audit/command-line-injection-sink
@tags secur
import java
import sem
from Commar
select sinks,
GitHub’s CodeQL Multi Repository Variant
Analysis (MRVA)
EVALUATOR LOG VIEWER
CODEQL METHOD MODELING
© Sarif 4\ Go Update Available A\ Analysis Tools Missing
```

## Slide 36

CBOM Reporter https://github.com/santandersecurityresearch/cryp tobom-forge

Generates a CBOM in CycloneDX standard to identify and enumerate cryptographic assets and vulnerabilities in a repository from the CodeQL PQC query output.

Information Classification: General

## Slide 37

Applying multi repository variant analysis to CBOMs

Trigger CBOM
Scan
Build
Dependency
Graph
Application
Analyse
CBOM CBOM
Repository
Pull Cached
Dependency
Data
Scan other  Multi Repo
Dependencies Variant
Analysis

Information Classification: General

## Slide 38

Information Classification: General

## Slide 39

##### Information to drive action

GitHub’s Copilot leverages Retrieval Augmented Generation (RAG) techniques to allow tailored coaching within the business on specific internal Cyber Strategies.

Information Classification: General

## Slide 40

TLP Colours 'red//amber//green' for 'weak//potentially/quantum-weak//reasonable’

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Cryptographic Asset Counts by Category
w/ TLP Indicators by Weakness
TLP Colours 'red//amber//green' for
‘weak//potentially/quantum-weak//reasonable’
T T
hashing asymmetric signatures unknown symmetric
```

## Slide 41

TLP Colours 'red//amber//green' for 'weak//potentially/quantum-weak//reasonable’

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Most Common Algorithms by Count
w/ TLP Indicators by Weakness
Use of algorithm RSA 74
Use of algorithm SHA1
Use of algorithm SHA256
Use of algorithm MD5
Use of algorithm UNKNOWN +
Use of algorithm DH +
Use of algorithm DSA +
Use of algorithm SHA512 — Ts
Use of algorithm ECDSA 4
Use of algorithm AES 7
Use of algorithm SHA 4
Use of algorithm DES —
Use of algorithm CBC 4
Use of algorithm SHA384 4
Use of algorithm X25519 +
Use of algorithm MD4 -—il
Use of algorithm SHA224 4
Use of algorithm AES128 +
Use of algorithm POLY1305 —l
Use of algorithm AES256 4
Use of algorithm CURVE448 4
Use of algorithm ECB
Use of algorithm CFB
Use of algorithm WHIRLPOOL
Use of algorithm ECDH
Use of algorithm MGF1
Use of algorithm SM2 1 '
Use of algorithm RC4 TLP Colours 'red//amber//green' for
Use of algorithm ED25519 ‘weak//potentially/quantum-weak//reasonable’
Use of algorithm GOST
500 750 1000 1250 1500 1750 2000
```

## Slide 42

Information Classification: General


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PB main~ 3branches 2 tags Go to file Add file ~ | code ~ | About
Santander Group Cryptography
Merge pull request #119 from santander-group-. : eacébd8 Sdaysago 252 commits Standard - This document contains
mandatory security requirements for the
github/workflows trying ghcr.io pandoc image in gh action jast month effective use of cryptography for
security within Santander Group.
Cryptography Merge pull request #108 from santander-group-cyber-cto/n473021- last week
Implementations Merge pull request #119 from santander-group-cyber-cto/sshd-split ays ago
*~- Activity
KeyManagement fixing issues 93, 92, 91, 90 months ago
resources nitial git push from CSR repo into main group EM months ago 0 watching
Annex.md Create Annex.md 5n $ ago 4 forks
CryptographyStandard.docx nitial git push from CSR repo into main group EM months ago
Releases 2
Governance.md added exception management months ago
Intro.md exception manageme months ago © v20230703 (Late
README.md added trivy scan flare months ago
changelog.md issue #10 months ago
gen-changelog.sh nitial git push from CSR repo into main group EM months ago
Packages
index.txt move changelog to end of doc months ago , bis
Publish your first package
Contributors 7
© Docker Code Scanning
Santander Global Cryptography Standard
Languages
Please see the Intro page for details about the standard
Shell 100.¢
```

## Slide 43

## Securing our digital landscape takes all of us

Information Classification: General

## Slide 44

**Understand the risks**

Recap: How we prepare for the Post Quantum Crypto world

**Locate and assess CBOM**

**Scale your efforts Instill Crypto Agility**

Information Classification: General

## Slide 45

Try it out & Help the community

Information Classification: General

## Slide 46

Rasmus Larsen

Alvaro Muñoz

Chris Campbell

Walker Chabbott

Paul Hodgkinson

Rutger Schenk

## Thank You

Bas van Schaik

Raul Garcia

James Fletcher

Pierre Tempel

Josh Brown White

Christina Delahanty

Emile El-Qawas

Information Classification: General

## Slide 47

Try it out & Help the community

Information Classification: General
