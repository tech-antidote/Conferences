---
title: "Digital Dominoes Scanning the Internet to Expose Systemic Cyber Risk"
speakers: ["Morgan Hervé-Mignucci"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Morgan Hervé-Mignucci_Digital Dominoes Scanning the Internet to Expose Systemic Cyber Risk.pdf"
pages: 33
sha256: "48472e190870cf063fb38f923a1344b046249b2d58757561e4662a61fbff982b"
text_chars: 9140
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:57:55Z"
---
# Digital Dominoes Scanning the Internet to Expose Systemic Cyber Risk

**Speakers:** Morgan Hervé-Mignucci  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Morgan Hervé-Mignucci_Digital Dominoes Scanning the Internet to Expose Systemic Cyber Risk.pdf` (33 pages)


## Slide 1

# Digital Dominoes: Scanning the Internet to Expose Systemic Cyber Risk

Morgan Hervé-Mignucci

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSek hat
EFFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Digital Dominoes: Scanning the
Internet to Expose Systemic
Cyber Risk
Morgan Herve-Mignucci
```

## Slide 2

###### Morgan Hervé-Mignucci PhD, CFA, CISSP

- Lead **Cyber Catastrophe Modeling** at Coalition, Inc.

- Pioneered cyber risk models adopted by global insurers & reinsurers

- • Previously featured in Financial Times / New York Times for research on systemic infrastructure & climate risk

#BHUSA @BlackHatEvents

## Slide 3

#### 3 Large-scale Cyber Events in 2024

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
BRIEFINGS
S.. = z Ye ore “ 4 y , j y
black hat N Wigrey » ’
UM
3 Large-scale Cyber Events in 2024
CDK GLOBAL
#BHUSA
```

## Slide 4

##### Cyber Catastrophe Risk (CAT)

##### Systemic Cyber Risk (SCR)

- Insurance-specific

   - Broader than insurance

- Portfolio losses quantification

   - Economy- / industry-wide impact

- Commercial CAT models

- • **Risk Management** : underwriting, coverage, capitalization, reinsurance

- Ad hoc impact assessment

- **Interventions** : public policy, regulation, public-private sector collaboration

#BHUSA @BlackHatEvents

## Slide 5

### <u>Same Root Cause</u> Accelerated Interconnectedness in our Increasingly Digital Economies

#BHUSA @BlackHatEvents

## Slide 6

# Dissecting Past Cyber Events

#BHUSA @BlackHatEvents

## Slide 7

#### Categorizing Landmark Cyber Events

Ukraine NotPetya Colonial Pipeline Change Power Grid Healthcare Target Equifax MS Exchange Kaseya CDK Global MOVEit WannaCry SolarWinds Log4J Sony CrowdStrike Orion 3CX 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025

Supply Chain  Direct Targeted  Shared Technology  Trusted Security
Compromise Attacks Vulnerabilities Tool Failures
Nation-State Operations Protocol Vulnerabilities
3 rd party access vector
Destructive Attacks Security Tool
OSS Dependencies
Software update vector
Ransomware Operations Platform Vulnerabilities

#BHUSA @BlackHatEvents

## Slide 8

###### (More or Less) Common Cyber Insurance Levers

From “Silent Coverage Sub-Limits Premium Cyber” to Expansion & Affirmative Introduction Adjustment Exclusion Cyber Underwriting More Robust Scrutiny + Reinsurance Data Formal / Risk Capital Collection Controls

#BHUSA @BlackHatEvents

## Slide 9

#### Major Public Policy / Regulator Response

Public
Reporting

Best Practice / Guidance / Advisory

Attribution / Charges / Coordinate Fines / / “Fix” Sanctions

Supply
Chain
Visibility

Critical Infrastructure

Finance & Insurance

#BHUSA @BlackHatEvents

## Slide 10

#### Loss Estimates from Past Cyber Events

$12B
$8-10B $5-10B
$10B
$8B
$6B
$3-4B
$4B $2-3B
$0.3-1.5B
$2B
<$0.3B
$B
WannaCry  NotPetya  CrowdStrike
(2017) (2017) (2024)
Economic Insured

#BHUSA @BlackHatEvents

## Slide 11

# Modeling What Matters in Systemic Cyber Risk

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BRIEFINGS SE Ne 7
Modeling
What
Matters in
Systemic
Cyber Risk
#BHUSA @BlackHatEvents
```

## Slide 12

###### What is Cyber Catastrophe Risk Modeling?

How many times did we I looked forward in get an AWS US-East-1 time. I saw outage that lasted more 14,000,605 futures. than a week?

One

#BHUSA @BlackHatEvents

## Slide 13

#### Insurance Catastrophe Modeling 101

1 2 3 4 5
Event  Hazard  Exposure  Vulnerability  Insurance
Set Footprint (assets, orgs) / Severity Coverage

Great fit for insurance / reinsurance risk quantification & management use cases

#BHUSA @BlackHatEvents

## Slide 14

#### … But CAT Models suboptimal for SCR

Misaligned Modeling Paradigm

- Static “Nat Cat” approach is a poor fit for dynamic SCR

- Data Issues

- Models unvalidated by a true catastrophe precedent

- Non-insured organizations are out of scope

- Vendor Inertia & Flawed Anchoring

- Vendor models initially overstated risk

- Business inertia prevents necessary model updates

#BHUSA @BlackHatEvents

## Slide 15

###### Data-Driven SCR Modeling

SCR is best represented as a <u>Massive Graph</u>

- Leverage Coalition’s data to curate Aggregation Technologies & Vendors (ATV) datasets

Focus on what is Known (i.e., publicfacing internet)

#BHUSA @BlackHatEvents

## Slide 16

None Basic Detailed Uses AWS AWS USUses US-East-1 East-1 AWS US(Athena) (Athena) East-1 for Market Dynamic (Athena) Share Pricing CAT Typical Uses AWS Level of Uses AWS for Market AWS Dynamic Detail Share Pricing • Overestimate Concentration Uses a CSP & Losses Uses a CSP for Market • CSP Dynamic Limited / Share Pricing Flawed Insights Organization Details

Organization Details

######

###### SCR Target Level of Detail

• More Credible Losses • Nuanced understanding of SCR

#BHUSA @BlackHatEvents

## Slide 17

Identifying Aggregation Technologies & Vendors swag.* shops.myshopify.com Cloudflare ~~CNAME~~ A NS (WAF / LB) ENUM … MX SPF … Outlook, example.com Mailgun ENUM A Banner Nginx, AWS (us-east-1), ENUM MariaDB + version, etc. Simplified dev.* ATV Data AWS CNAME A Gathering (CloudFront) blog.* xyz.cloudfront.net Example

#BHUSA @BlackHatEvents

## Slide 18

# Industry / Segment Deep Dives

#BHUSA @BlackHatEvents

## Slide 19

Inc. 5000 Firms 5K 200%+ US Orgs. Growth 1.4M ~5K Headcount Unique Domains $317B Revenue

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BRIEFINGS | es ae
Inc. 5000 Firms
oK 200%+
US Orgs. Growth
1.4M 5K
Headcount Unique
$317B Domains
Revenue
#BHUSA @BlackHatEvents
```

## Slide 20

Systemic Cyber Risk is Cross-Sectoral DEMO #1 – Most leading ATVs can be found in multiple, sometimes unrelated, industries

#BHUSA @BlackHatEvents

## Slide 21

Registered Investment Advisory Firms 22K $145T Firms AUM 1M+ 18K+ Headcount Unique 60M+ Domains Clients

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SI GIsrNeS | S —w7"\ XX 7 LZ bi
Registered Investment Advisory Firms
22K $145T
Firms AUM
1M+
Headcount 7 SK+
Unique
60M+ Domains
Clients
#BHUSA @BlackHatEvents
```

## Slide 22

Cloud Outage Risk More Nuanced Than Claimed DEMO #2 - A more nuanced datadriven understanding of cloud architecture generates more credible cloud outage loss estimates

#BHUSA @BlackHatEvents

## Slide 23

Multiple Levels of Cloud Outage Risk
Sample CAT Cloud Outage Scenarios
3-6+ days
Global
Services 1-3+ days
Region
Zone
Outage
Length
0 Day(s) 4 Day(s) 8 Day(s) 12 Day(s) 16 Day(s)
Scope : longest AWS, GCP, and Azure outages over 2020-2025

#BHUSA @BlackHatEvents

## Slide 24

#### US Real Estate Agencies (CT)

## 20+K ~2K Agents Unique Domains 2.5+K Agencies

#BHUSA @BlackHatEvents

## Slide 25

Aggregation via SaaS & Franchisor IT DEMO #3 – Most industries have industry-specific ATVs around which organizations tend to be clustered

#BHUSA @BlackHatEvents

## Slide 26

###### Identifying High-SCR Technologies & Vendors

All ATVs from 2024 SCR events were named in an antitrust proceeding

_NSS Labs, Inc. v._ **_CrowdStrike, Inc._** _et al, (N.D. Cal. 2020)_

_U.S.A. v. UnitedHealth Group &_ **_Change Healthcare_** _(D.D.C. 2022)_

_In re Dealer Management Systems Antitrust Litigation (N.D. Ill. 2024) – including_ **_CDK Global, LLC_**

A Glimpse of More to Find in FTC Data

Mortgage / Real Estate

- Origination

- • Marketplaces

- • Bulk data

###### Finance

- Software / API

###### Healthcare

- Bulk Data

- • EHR / CRM

#BHUSA @BlackHatEvents

## Slide 27

# Implications & Recommendations

#BHUSA @BlackHatEvents

## Slide 28

#### For Policymakers

###### Shift to a Proactive, Data-driven Approach to SCR Policymaking

- Expand Definition of

- “Critical Infrastructure” • Focus on Systematically Important Technologies (i.e., ATVs), not just sectors

   - Mandate & Incentivize Measurable Resilience

- Mandate Supply Chain Visibility for organizations utilizing designated critical ATVs

- • Incentivize resilience through market mechanisms like cyber insurance

Leverage Dependency Data to Guide Antitrust and Regulation

#BHUSA @BlackHatEvents

## Slide 29

#### For Risk Owners / CISOs

###### Cannot Prevent SCR -> Build Resilient Organization

###### Resilience & Vulnerability & Containment & Governance & Supply Chain Exposure Operational Crisis Security Management Recovery Management

- Nth-party ATVs

- Architecture

- TPRM / SBOM

- Real-Time Inventory

- Continuous ASM

- Emergency Patching

   - (Real) Tabletop

   - • CRQ

- Zero-Trust

- • Immutable Backups

- Backups • Cyber Insurance

- • IR Playbooks • Out-of-Band

#BHUSA @BlackHatEvents

## Slide 30

#### For Risk Modelers

Prioritize Data-Driven Modeling of Economic Losses

About Catastrophic Scenarios

- Embrace Granular ATV Usage & Detection Data

   - Stress Testing ≠ Systematic FUD

- Gold Standard -> Modeled Loss Traceability

- Else GIGO for Insured Losses

- Anchor Event Catalogs & Assumptions in Updated Data

#BHUSA @BlackHatEvents

## Slide 31

# Next Steps

#BHUSA @BlackHatEvents

## Slide 32

#### Addressing Limitations

Known Unknowns:

- WAFs / VPCs / Internal Networks / Clients

- • Non-Digital Vendor Relationships

- Unknown Unknowns:

- Unnoticed OSS / Components

- Even Better Data Quality:

- Discovery / Enumeration / Attribution

- Richer Context & Asset Classification

#BHUSA @BlackHatEvents

## Slide 33

#### Black Hat Sound Bytes

Ø Systemic Cyber Risk is a “Too Connected to Fail” reality, driven by the deep interconnectedness of our digital economies Ø We must shift from static, theoretical catastrophe models to a dynamic, data-driven approach that maps the Internet's true dependencies

Ø For Risk Owners, the goal is not prevention but resilience; you must understand your risk through the lens of shared technology and your n<sup>th</sup> -party supply chain

#BHUSA @BlackHatEvents
