---
title: "Does Public Disclosure of Vulnerabilities Affect Hacker Participation in Bug Bounty Programs"
speakers: ["Ali Ahmed", "Brian Lee", "Amit Deokar"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Ali Ahmed & Brian Lee & Amit Deokar_Does Public Disclosure of Vulnerabilities Affect Hacker Participation in Bug Bounty Programs.pdf"
pages: 22
sha256: "ca2ca7f630b48044f36d256983784ab3b4dee641c40c728080c7a5ec05fcd2d3"
text_chars: 9270
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T04:05:06Z"
---
# Does Public Disclosure of Vulnerabilities Affect Hacker Participation in Bug Bounty Programs

**Speakers:** Ali Ahmed, Brian Lee, Amit Deokar  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Ali Ahmed & Brian Lee & Amit Deokar_Does Public Disclosure of Vulnerabilities Affect Hacker Participation in Bug Bounty Programs.pdf` (22 pages)


## Slide 1

Does Public Disclosure of Vulnerabilities Affect Hacker Participation in Bug Bounty Programs?

Speaker: Ali Ahmed, Ph.D. – University of Wisconsin Eau Claire

Contributors: Brian Lee – Penn State University, Amit Deokar – University of Massachusetts Lowell

#BHUSA  @BlackHatEvents

## Slide 2

# Two Questions:

➢ As an organization, would you publicly disclose patched vulnerability reports?

➢ As a hacker, would the disclosed reports help you

find more bugs?

#BHUSA @BlackHatEvents

## Slide 3

#### **Many Organizations on HackerOne and BugCrowd Publicly Disclose Reports**

###### BugCrowd’s CrowdStream

HackerOne’s Hactivity

#BHUSA @BlackHatEvents

## Slide 4

### Research Questions

1. How does the public disclosure of patched vulnerabilities affect the discovery of new vulnerabilities in bug bounty programs?

2. Does the disclosed information help hackers in discovering new vulnerabilities?

3. Does the disclosure increase or decrease hackers’ success?

4. If disclosure has an effect, what type of disclosures or hackers are most affected?

#BHUSA @BlackHatEvents

## Slide 5

###### There could be two possibilities:

1. Disclosure can provide valuable information to hackers, which they can use to increase their success in finding new vulnerabilities in a system.

2. Disclosure can also obstruct hackers thinking and could negatively affect their cognitive capabilities. Disclosure can decrease their success in finding new vulnerabilities.

#BHUSA @BlackHatEvents

## Slide 6

## Theoretical Framework

#BHUSA @BlackHatEvents

## Slide 7

#### Theoretical Framework

- Hacking is a highly creative process.

- Disclosure can cause cognitive fixation in hackers and can negatively impact their creativity.

- Fixation is the human tendency to approach a given problem in a set way that limits one’s ability to shift to a new approach to that problem (Duncker 1945).

_Fixation: “The mind’s obstacle to seeing what is right in front of us.”_

- **Prior examples** can reduce creativity, and people tend to fixate on the principles and features of prior examples.

- Disclosure of past discoveries can cause fixation in hackers’ cognitive processes and obstruct their ability to find new ways to discover vulnerabilities.

#BHUSA @BlackHatEvents

## Slide 8

##### **There are types of fixation:**

- Mental set

- The counterintuitive finding that prior experience or domain-specific knowledge can, under some circumstances, interfere with problem-solving performance.

- It is a cognitive trap arising from a desire to find familiar features in problems and reuse shortcuts to solve them.

- Prior experience can prime the mind and block creative problem-solving.

- Functional Fixedness

- It is a cognitive bias that limits a person to use an object only in the way it is traditionally used.

- The iceberg which drowned the Titanic could be used as a float.

Titanic Iceberg

#BHUSA @BlackHatEvents

## Slide 9

##### **We hypothesize:**

- In bug bounty programs disclosing previous examples of discovered vulnerabilities may lead to cognitive fixation in hackers.

- • Hackers are unable to generate new creative ideas to discover unknown vulnerabilities.

- Their search process may conform to the features related to the disclosed vulnerabilities, which is counterproductive in finding new vulnerabilities.

- Thus, disclosure leads to fewer discoveries and lower success for hackers.

#BHUSA @BlackHatEvents

## Slide 10

Study Context, Dataset, and Methods

#BHUSA @BlackHatEvents

## Slide 11

### Dataset

- We collected publicly available data from a leading bug bounty platform.

- Our platform is similar to renowned bug bounty platforms like HackerOne and BugCrowd.

- Once the organization fixes the reported vulnerability, they mark it as resolved (patched) on the platform.

- After resolving, firms can publicly disclose the contents of the report.

#BHUSA @BlackHatEvents

## Slide 12

### **Dataset**

- Our dataset comprises of 368 firms that have launched public bug bounty programs.

- The total number of resolved reports from these firms is 83,473 vulnerability reports.

- Among them, 8,712 vulnerability reports were publicly disclosed by the firms (10.4% of the total).

- Using this report-level data, we created a firm and month-level (unbalanced) panel dataset consisting of 368 firms and 80 months.

- For each firm in each month, we calculated the number of reports resolved, the number of disclosed (and hidden) reports, the bounties awarded, and the number of hackers involved.

#BHUSA @BlackHatEvents

## Slide 13

### **Dependent Variable: Resolutions**

- Our dependent variable is the number of resolved reports for each month by a firm.

- We counted the number of reports resolved for each month by a firm and named it 𝑅𝑒𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛𝑠𝑖𝑡 , i.e., the number of resolved reports by firm _i_ in month _t._

- We also counted the number of unique successful hackers in each month and named it 𝑆𝑢𝑐𝑐𝑒𝑠𝑠𝑓𝑢𝑙𝐻𝑎𝑐𝑘𝑒𝑟𝑠𝑖𝑡

#BHUSA @BlackHatEvents

## Slide 14

### **Independent Variable: Past Disclosures**

- The main independent variables in our firm-month panel data are the cumulative resolutions and cumulative disclosures of reports by each firm in each month.

- We counted the number of resolved reports for each firm in a given month.

- We aggregated the count of resolved reports to capture the overall resolution level of a program.

- This variable is denoted as 𝐶𝑢𝑚𝑙𝑎𝑡𝑖𝑣𝑒𝑅𝑒𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛𝑖𝑡 , representing the sum of resolved reports, σ𝑛𝑡=1 𝑅𝑒𝑠𝑜𝑙𝑣𝑒𝑑𝑅𝑒𝑝𝑜𝑟𝑡𝑠𝑖𝑡 , where _i_ represents a firm and _t_ represents a month.

#BHUSA @BlackHatEvents

## Slide 15

### **Independent Variable: Past Disclosures (cont.)**

𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝑖𝑡 𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝐹𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑖𝑡 = 𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝑅𝑒𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛𝑖𝑡

- Since previously disclosed reports remain visible to hackers, we aggregated the counts of disclosed reports over time and call it 𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝑖𝑡 .

- The 𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝐹𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑖𝑡 serves as our main explanatory variable, capturing the effect of a firm’s disclosure on the discovery and resolution of new vulnerabilities.

- It ranges between 0 and 1, and changes as new reports are disclosed or resolved. Additionally, disclosed reports are categorized as either “valid” or “invalid” by the firm.

- We computed the aggregated level of valid disclosures and divided it by the cumulative resolutions of the firm _i_ until period _t_ to obtain the proportion of disclosed reports that are valid.

#BHUSA @BlackHatEvents

## Slide 16

### **Empirical Specifications**

We used econometric specifications of multiple fixed-effects linear regression models to find the relationship between past disclosures and future resolutions.

𝐿𝑜𝑔𝑅𝑒𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛𝑠𝑖𝑡

- = 𝛽1𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝐹𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑖𝑡−1 + 𝛽2𝐿𝑜𝑔𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐶𝑙𝑜𝑠𝑢𝑟𝑒𝑖𝑡−1

+ 𝛽3𝐿𝑜𝑔𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝐴𝑣𝑒𝑟𝑎𝑔𝑒𝐵𝑜𝑢𝑛𝑡𝑦𝑖𝑡−1

- + 𝛽4𝐿𝑜𝑔𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝑃𝑙𝑎𝑡𝑓𝑜𝑟𝑚𝑅𝑒𝑠𝑜𝑙𝑢𝑡𝑖𝑜𝑛𝑖𝑡−1

+ 𝛽5𝐿𝑜𝑔𝐶𝑢𝑚𝑢𝑙𝑎𝑡𝑖𝑣𝑒𝑃𝑙𝑎𝑡𝑓𝑜𝑟𝑚𝐷𝑖𝑠𝑐𝑙𝑜𝑠𝑢𝑟𝑒𝐹𝑟𝑎𝑐𝑡𝑖𝑜𝑛𝑖𝑡−1 + 𝐹𝑖𝑟𝑚𝑖 + 𝑀𝑜𝑛𝑡ℎ𝑡

+ 𝜀𝑖𝑡 1

where, _Firmi and Montht_ are fixed effects, capturing time-invariant firm and platform characteristics.

#BHUSA @BlackHatEvents

## Slide 17

## Results

#BHUSA @BlackHatEvents

## Slide 18

#### Main Findings

- Using multiple econometrics specifications, we found that past disclosures have a negative effect on the number of future resolutions.

- We also found that fewer hackers are likely to be successful if a firm increases its disclosure level.

Increases
Decreases
Disclosure Cognitive Fixation Creativity Resolutions
Decreases

#BHUSA @BlackHatEvents

## Slide 19

#### Different Types of Disclosure

- In our analysis, we have two types of Disclosures; Valid and Invalid Disclosures.

- The negative effects of disclosures mainly stem from valid disclosures, invalid disclosures have no effect.

- This suggests that hackers use valid disclosed information, which affects their ability.

Decreases
Increases
Valid Cognitive Fixation Creativity Resolutions
Decreases
Disclosure
Invalid
No Effect

#BHUSA @BlackHatEvents

## Slide 20

##### Effect of Disclosure on Different Types of Hackers

- Fixation doesn’t affect novice hackers.

- Disclosure has no effect on novice hackers

- Cognitive theories tell us that fixation affects experienced people more.

- Therefore, we found that experienced hackers are less likely to be successful due to disclosure.

###### No Effect

Novice Hackers
Success
Disclosure
Experienced
Hackers Success
Decreases

#BHUSA @BlackHatEvents

## Slide 21

### Black Hat Sound Bytes

###### Key takeaways:

1. If organizations want hackers to find new vulnerabilities, they must limit their disclosures. If they want to disclose, invalid disclosures could be one possible way.

2. Hackers must use caution in accessing disclosed reports and must overcome cognitive fixation to discover new vulnerabilities.

3. One possible way to reduce fixation is by program switching. Continuously working on the same program could lead to more fixation.

#BHUSA @BlackHatEvents

## Slide 22

• Ali Ahmed is an assistant professor in the Department of Information Systems of the College of Business at the University of Wisconsin – Eau Claire.

- He received his Ph.D. in Business Administration with a concentration in

   - Management Information Systems from the University of Massachusetts Lowell.

- His research focuses on policy and the economics of information security.

- He has extensively studied bug bounty, vulnerability disclosure, and hackers’

   - behavior on bug bounty platforms.

Feel free to connect on LinkedIn

- Email: <u>ahmeda@uwec.edu or ali_ahmed@student.uml.edu</u>

#BHUSA  @BlackHatEvents
