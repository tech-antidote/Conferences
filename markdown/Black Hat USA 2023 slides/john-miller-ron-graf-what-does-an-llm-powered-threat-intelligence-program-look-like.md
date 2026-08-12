---
title: "What Does an LLM-Powered Threat Intelligence Program Look Like"
speakers: ["John Miller", "Ron Graf"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/John Miller & Ron Graf_What Does an LLM-Powered Threat Intelligence Program Look Like.pdf"
pages: 27
sha256: "c318a10f0c60e41338fb92c112d0df92cc505088900c892ba909161abf807409"
text_chars: 12569
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.4
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:11:09Z"
---
# What Does an LLM-Powered Threat Intelligence Program Look Like

**Speakers:** John Miller, Ron Graf  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/John Miller & Ron Graf_What Does an LLM-Powered Threat Intelligence Program Look Like.pdf` (27 pages)


## Slide 1

# What Does an LLM-Powered Threat Intelligence Program Look Like?

Speakers: Ron Graf & John Miller

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
LUISA &
AUGUST 9-10, 20253
BRIEFINGS
What Does an LLM-Powered Threat
Intelligence Program Look Like?
Speakers: Ron Graf & John Miller
#BHUSA @BlackHatEvents
```

## Slide 2

### Speakers

Ron Graf Data Scientist

John Miller Head of Mandiant Intelligence Analysis

#BHUSA  @BlackHatEvents

## Slide 3

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
A.l. is a $1 trillion investment
opportunity but will be ‘biggest How Restaurants Can Use Al Technology
bubble of all time,’ CEO predicts to Reduce Labor Costs, Improve Efficiency,
How Unilever Is Transforming Ice Cream With
Al
Da Corrine How Al and Geospatial Technologies Gan Make a
Difference
July 18,2023 | «€ Share
by Directions Staff
FEATURES
What does the rise of artificial intelligence mean
for the industry?
```

## Slide 4

How do I navigate this environment when planning for a threat intelligence function?

**“How will AI affect next year’s human resources needs?”**

**“What will we be able to deliver that we couldn’t before?”**

**“How much faster will we respond to incidents?” …and more**

#BHUSA  @BlackHatEvents

## Slide 5

#### Session Roadmap

- Background on AI and CTI

- Framework for components of a CTI program

- Historical CTI reporting through lens of framework

- LLM impacts to components of a CTI program

- LLM implementation considerations

- Takeaways for CTI program planning

#BHUSA  @BlackHatEvents

## Slide 6

#### What does a threat intelligence program deliver?

**Improve security decisions** by providing answers to difficult & uncertain questions

- _What are the top threats facing our business?_

- _Which security events are the most malicious?_

- _How can we hunt for undiscovered threats?_

- _Which vulnerabilities should we prioritize?_

- _How can we test our security controls?_

#BHUSA  @BlackHatEvents

## Slide 7

#### What does a threat intelligence program need to succeed?

**Threat Visibility Processing Capability Interpretation Capability** Direct visibility into Convert data to standardized, Apply processed data to address relevant security data useful observations key questions for stakeholders _Example: emails detected Example: Identify email Example: Answer “Is Malware as malicious attachment is Malware X X the top threat to us?”_

#BHUSA  @BlackHatEvents

## Slide 8

#### How could a TI function benefit from LLM capabilities?

**Threat Visibility Processing Capability** Direct visibility into Convert data to standardized, relevant security data useful observations

**Interpretation Capability** Apply processed data to address key questions for stakeholders

_What are possible capacity challenges, in these terms?_

_How can LLMs be applied to help?_

#BHUSA  @BlackHatEvents

## Slide 9

#### **Intelligence Example #1: SpyZeus**

|**Summary**|Two prominent malware types reportedly
merged into single “product” by underground
vendors|
|---|---|
|**Intelligence**
**Type**|Qualified assessments on prominent security
issue|
|**Sources**|Primarily direct/manual “dark web” research|
|**Data Scope**|Weeks of activity in specific forums|
|**Length**|~3 pages|
|**IOCs**|Not in focus|

**What are my barriers to scaling this deliverable?**

- Access to dark web

**Threat Visibility Processing Capability**

   - Not a primary requirement

- Capacity to summarize,

- **Interpretation Capability** explain & assess dark web activity

#BHUSA  @BlackHatEvents

## Slide 10

#### **Intelligence Example #2: APT1**

|**Summary**|Sophisticated nation-state intrusion
operation exposed|
|---|---|
|**Intelligence**
**Type**|Detailing of intrusion operations
& assessed sponsor|
|**Sources**|DFIR data & open-source information
on assessed sponsor|
|**Data Scope**|“Nearly 150 victims over 7 years”
30+ cited open sources on sponsor|
|**Length**|74 pages|
|**IOCs**|3,000+|

###### **What are my barriers to scaling this deliverable?**

   - Regular DFIR data over extended period

- **Threat Visibility** period • Access to open sources

- • Capacity to develop data points

- **Processing Capability** from threat artifacts (e.g. malware) • Chinese-language translation

- • Capacity to plan & direct research on sponsorship questions

- **Interpretation Capability** • Capacity to synthesize gathered data on sponsorship questions

   - Capacity to develop data points from threat artifacts (e.g. malware)

   - • Chinese-language translation

   - Capacity to plan & direct research on sponsorship questions

#BHUSA  @BlackHatEvents

## Slide 11

#### **Intelligence Example #3: Carbanak**

|**Summary**|Exposition of criminal intrusion operation
into financial institutions yielding $1B in
losses|
|---|---|
|**Intelligence**
**Type**|Technical detailing of intrusions &
connected malware operations|
|**Sources**|DFIR data, malware repository information
& malicious infrastructure|
|**Data Scope**|“100 banking entities impacted,” 2-year
scope, multiple control servers|
|**Length**|39 pages|
|**IOCs**|300+|

###### **What are my barriers to scaling this deliverable?**

   - Extended-period DFIR data

   - • Commercial technical sources

- **Threat Visibility** • Commercial technical sources

- • Capacity to develop data points from

- **Processing Capability** threat artifacts (e.g. malware)

- • Capacity to describe intrusion

- **Interpretation Capability** observations

   - Capacity to develop data points from threat artifacts (e.g. malware)

#BHUSA  @BlackHatEvents

## Slide 12

#### **Intelligence Example #4: CCleaner Backdoor**

|**Summary**|Analysis of supply-chain compromise
of popular software|
|---|---|
|**Intelligence**
**Type**|Walkthrough of malicious alterations
to software|
|**Sources**|Primarily malware samples & sample
reverse engineering|
|**Data Scope**|3 identified code samples from specific
incident|
|**Length**|~10 pages|
|**IOCs**|20+|

###### **What are my barriers to scaling this deliverable?**

   - Access to malicious code telemetry

- **Threat Visibility**

- **Processing Capability**

- **Interpretation Capability**

- Rapid-turn malware reverse engineering capability

- Capacity to rapidly characterize risks from emerging events

#BHUSA  @BlackHatEvents

## Slide 13

#### How LLM’s Impact Processing and Interpretation

- Exploit data which is often overlooked due to volume

- Toil reduction for analysts

- Better, faster responses to RFI’s

#BHUSA  @BlackHatEvents

## Slide 14

#### Processing Tasks

High Volume of Text Data

- Exploit data overlooked due to volume

- Prevent waste of scarce experts on trivial tasks

- • Many high-impact, low risk LLM-applications here

**Use LLM’s**

###### **Case-by-Case**

###### **<u>LLM Examples</u>**

Less Critical Thinking More Critical Thinking Needed Needed

- Malware RE reports for less complex samples

- • Translate log into standardized, meaningful format

- • Weekly summary of open source/third-party intel

**Case-by-Case**

###### **Use Human Experts**

###### **<u>Human Expert Examples</u>**

- Malware RE report for novel, complex samples

- • Translate foreign language docs critical for attribution

Low Volume of Text Data

#BHUSA  @BlackHatEvents

## Slide 15

#### Interpretation Tasks

More Time Available to Answer Question

- Most workflows should remain human-in-the-loop

- Fewer low risk applications vs. processing

**Case-by-Case**

**Case-by-Case**

###### **<u>LLM Examples</u>**

- SOC triage of a high-priority, time-sensitive alert

- • Patch prioritization for low CVSS score vulns

- Prioritizing dark web forum monitoring alerts

Trivial Consequences of Hallucinations

**Use LLM’s**

Serious Consequences of Hallucinations

**Use Human Experts**

###### **<u>Human Expert Examples</u>**

- Incident response report writing

- • Patch prioritization for high CVSS score vulns

- Assess likelihood of intruders lateral movements

Less Time Available to Answer Question

#BHUSA  @BlackHatEvents

## Slide 16

#### Impact of Hallucinations - Consequential Example

Actor sends invoice SOC analyst alerted, lure with malicious conducts standard PDF to Accounting response

Automated triage on email & attachment

Results into LLM-powered tool to digestible format for SOC analyst

LLM hallucinates about risks, determines email benign

#BHUSA  @BlackHatEvents

## Slide 17

#### Impact of Hallucinations - Nuisance Example

**Analyst Prompt to LLM:**

**What malware families are associated with APT32?**

###### **LLM Response:**

**APT32, also known as OceanLotus or APT-C-00, has been associated with several malware families throughout its cyber espionage campaigns. Some of the notable malware families linked to APT32 include:**

**1. Cobalt Kitty: A custom remote access trojan (RAT) used by APT32 for initial compromise and establishing a foothold in the target network.**

**2. KOMPROGO: A backdoor RAT employed by APT32 to maintain persistence and execute commands on compromised systems.**

**3. Kasperagent: A modular malware framework utilized by APT32 for reconnaissance, data exfiltration, and lateral movement within the victim network.**

**4. BEACON: A backdoor malware used by APT32 to gain unauthorized access to systems, collect information, and execute commands remotely.**

**5. RemyRat: A remote access trojan used by APT32 to maintain persistence and conduct surveillance on compromised systems.**

#BHUSA  @BlackHatEvents

## Slide 18

#### Beyond Interpretation

- Certain automated actions could be enabled by LLM interpretation capabilities

- Will require thorough vetting to mitigate the impacts of hallucinations

- Examples:

   - Change firewall rules/network configurations

   - Patch vulnerabilities

   - Take system offline until a human clears it to bring it back online

   - Force user password change

#BHUSA  @BlackHatEvents

## Slide 19

#### Impacts of Hallucinations

- Contemplate: which functions can & can’t tolerate fabricated information?

**Unacceptable** -  Hallucinate vulnerability details that change patch prioritization

Acceptable - Misinterpret benign log entries not being reviewed by human anyways

- Prioritize grounding model outputs in factuality should be prioritized

   - ○Knowledge graphs & other sources of truth provide options for grounding

#BHUSA  @BlackHatEvents

## Slide 20

### “Black Hat Sound Bytes”

What are takeaways for threat intelligence functions: AI integration & capability planning?

#BHUSA  @BlackHatEvents

## Slide 21

#### Takeaway: Intentionally codify human expertise

**Engineer systems so experts provide feedback to models with no added burden**

- Meet the experts where they are

- Reinforcement learning with human feedback (RLHF) should be prioritized as a component of any attempt to power a CTI workflow with an LLM

###### **Invest in generalist, well-rounded experts**

- Skill sets tied to specifically to tooling will become less valuable over time

- Breadth of expertise and strong critical thinking skills will become more valuable over time

#BHUSA  @BlackHatEvents

## Slide 22

Takeaways:

Use private models for sensitive use-cases

LLM integration with 3rd-party services (plug-ins/tools) critical

Differentiator: Pre-train / fine-tune on high-quality domain-specific datasets

- _Internally harvested data_

Think beyond text - lots of expertise encoded in slide decks as images/diagrams

- _Third-party data sources_

_● Acquisition considerations_

#BHUSA  @BlackHatEvents

## Slide 23

#### Takeaway:

**Plan for:** **_continuing baseline_ of CTI expertise + expertise** **_in LLM behavior_**

#BHUSA  @BlackHatEvents

## Slide 24

#### Takeaway:

#### **Plan for higher ROI from** **_processing & interpretation_** **investments**

###### More **_intelligence outcomes delivered_** per **_resource invested_**

- Threats assessed

- • Vulnerabilities prioritized

- • Events actioned

-

- Incremental hires

- • Tools

- • Data sources

- • …

#BHUSA  @BlackHatEvents

## Slide 25

Takeaway:

**Plan for higher ROI from** **_processing & interpretation_** **investments** More intelligence outcomes delivered per resource invested

**Resource reduction** vs. **greater ROI**

_“The workforce gap is not going unnoticed by cybersecurity workers – nearly 70% feel their organization does not have enough cybersecurity staff to be effective.” - ISC_<sup>_2_</sup> _, 2022_

#BHUSA  @BlackHatEvents

## Slide 26

##### **Thank you!**

#BHUSA   @BlackHatEvents

## Slide 27

## Resources

_Intelligence content examples_

SpyZeus: <u>https://krebsonsecurity.com/2010/10/spyeye-v-zeus-rivalry-ends-in-quiet-merger/</u> APT1: <u>https://www.mandiant.com/sites/default/files/2021-09/mandiant-apt1-report.pdf</u> Carbanak: <u>https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/08064518/Carbanak_APT_eng.pdf</u> CCleaner: <u>https://www.crowdstrike.com/blog/protecting-software-supply-chain-deep-insights-ccleaner-backdoor/</u>

#BHUSA  @BlackHatEvents
