---
title: "From HAL to HALT Thwarting Skynet's Siblings in the GenAI Coding Era"
speakers: ["Chris Wysopal"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Chris Wysopal_From HAL to HALT Thwarting Skynet's Siblings in the GenAI Coding Era.pdf"
pages: 24
sha256: "1331a2df0ef00b6df6de26e66aaff7dd851f756404e28dd5addcc02554028fe0"
text_chars: 5992
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.1
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:28:46Z"
---
# From HAL to HALT Thwarting Skynet's Siblings in the GenAI Coding Era

**Speakers:** Chris Wysopal  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Chris Wysopal_From HAL to HALT Thwarting Skynet's Siblings in the GenAI Coding Era.pdf` (24 pages)


## Slide 1

From HAL to HALT: Thwarting Skynet's Siblings in the GenAI Coding Era

Chris Wysopal

Co-founder & CTO, Veracode

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
From HAL to HALT: Thwarting
Skynet's Siblings in the GenAl
Coding Era
Chris Wysopal
Co-founder & CTO, Veracode VE RACODE
#BHUSA @BlackHatEvents
```

## Slide 2

**One of the 1**<sup>**st**</sup> **vulnerability researchers, member of hacker think tank, L0pht in 1990s**

Unites States Senate testimony - 19 May 1998

## Slide 3


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Using Good Hackers to
Battle Bad Hackers
F YOU HAVEA MURKY PASTAND DOUBT
i could becomea dot-com millionaire,
think again. Last week a scraggly band of
hackers known as “LOpht Heavy Industries”
joined with some straitlaced tech execs to
form @Stake, an Internet-security consult-
ing firm.
Into the light: Once shadowy computer code
warriors like Kingpin are going legit
Newsweek, January 17, 2000
```

## Slide 4

**Improve the Security of Your** **_Product_ by Breaking Into It**


> Recovered by OCR — confidence 65/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
trategies [a computers
Improve the PAPER.
Security of gceayal =
by Breaking io :
```

## Slide 5

**Founded @stake security research team and then Veracode to build security into SDLC**

## Slide 6

State of Software Security 2024

Addressing the Threat of Security Debt

## Slide 7

### **new flaws introduced by application age**

50% the "honeymoon phase" of applications where fewer
flaws are introduced
40%
30%
20%
10%
0%
1 2 3 4 5
age of application in (years)

## Slide 8

8


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
organizations are
drowning in security debt
70.8% 45%
of organizations of organizations
have security have critical
debt security debt
“Critical debt: High-severity flaws that remain unremediated for over one year.
```

## Slide 9

9


> Recovered by OCR — confidence 96/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
applications show an
average monthly fix rate
that exceeds
ten percent of all security
flaws.
tean
```

## Slide 10

10


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
why software
security is hard
= security knowledge gaps
= increased application complexity
# incomplete view of risk
# evolving threat landscape
```

## Slide 11

**Let’s add the exciting potential of large language models that can write code!**

## Slide 12

# **Developer GenAI use right now**

Generating code

Understanding code/Code review Remediating defects

Translating programming languages Creating and maintaining unit tests Writing documentation

12

## Slide 13

# **Emerging dev uses for GenAI**

Learning about the code base Searching for answers to avoid reinventing the wheel Reading log files to find a root cause

Creating and running functional & non-functional tests Remediating security vulnerabilities

13

## Slide 14

### **Large Language Models**

Training
Data Set
…
41%
Public GitHub
Code  Repositories 41% of Copilot produced
code contain known
Generator
security vulnerabilities.
Open-Source
›
Projects Large
User Prompt ChatGPT
Language  User Result
Documentation  Model
and
Comments
Bard
Thirds Party Code
(License Risk)
…
Large corpus of data
that includes open
web content.

## Slide 15

**Security Implications of LLMs New York University Study Stanford University Study** on GitHub Copilot on AI Code Generators

**Wuhan University Study** on AI Code Generators **36%**

**Wuhan University Study New York University Study Stanford University Study Purdue University** on AI Code Generators on GitHub Copilot on AI Code Generators on ChatGPT accuracy **36% 41%** Developers using LLMs were **52%** more likely to write insecure Out of the **435 Copilot** generated Of 1689 generated programs 41% of code. 52% of ChatGPTs answers were code snippets found in repos Copilot produced programs incorrect. **36%** contain security contained vulnerabilities They were more confident their Developers preferred them 35% weaknesses, across **6** code was secure. of the time yet 77% of those programming languages. answers were wrong

## Slide 16

## **SALLM Framework For measuring LLM vulnerability generation - Notre Dame**

**Vulnerable@k metric best to worst:**

StarCoder

GPT-4:

GPT-3.5:.

CodeGen-2.5-7B: CodeGen-2B:

https://arxiv.org/abs/2311.00889

## Slide 17

# **Implications of LLM code generation**

Code reuse goes down Code velocity goes up Vulnerability density similar

=

Increased Vulnerability Velocity

17 © Veracode, Inc. 2023 Confidential

## Slide 18

**How can we apply AI to the problem of insecure code, but in a more accurate and trustworthy manner?**

## Slide 19

# **We need a faster test and fix workflow**

Ticket
Train Triage
Find
Manual Fix Months
Build Test Deploy
Review Minutes Find
Recommend Fix

19

## Slide 20

20


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Training data set: Java XSS
public void doGet(HttpServletRequest req, HttpServletResponse resp) {
String name = /req.getParameter("name");
String[] array = new String[10];
array[0] = name;
PrintWriter writer = resp.getWriter();
writer.print1n(“Hello “ + array[0]);
Cross-site scripting (CWE 80)
public void doGet(HttpServletRequest req, HttpServletResponse resp) {
String name = req.getParameter("name");
String[] array = new String[10];
array[0] = name;
PrintWriter writer = resp.getWriter();
writer.println(“Hello “ + StringEscapeUtils.escapeHtml4(array[0]));
20
```

## Slide 21

### **Fix Approach**

Curated Dataset

Code Provenance  Coverage all that
Assurance matter

Training Data Set
Proprietary
Data
Fix LLM Fix
User Prompt
User Result
Suggestions
Supervised
Learning

## Slide 22

# **Recommendations for AI and code security**

Consider the implementation details before leveraging AI for developing and/or securing code

- What does the ML model use for training data?

- Is that training data trustworthy/vetted?

- Are there licensing issues with generated code?

- Is any of my intellectual property being leaked?

- How accurate are the generated fixes?

Be aware of human biases that trick us into feeling overly confident about the correctness of AI-generated content

22

## Slide 23

Data Poisoning IP Infringement **Other Risks to** Bias & Fairness **GenAI Code**

Recursive Learning

Propagation of Deprecated Practices

Hallucinated & Squatted Packages

## Slide 24

GenAI in dev is a powerful tool that requires the same level of security scrutiny and best practices as any other aspect of software development

Include security considerations in GenAI prompts

Automate as much of security process as possible, including automated fixing

**Chris Wysopal Co-founder & CTO Veracode @weldpond**

24 © Veracode, Inc. 2023 Confidential
