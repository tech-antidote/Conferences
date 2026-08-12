---
title: "Unraveling the Mind Behind the APT - Analyzing the Role of Pretexting in CTI and Attribution"
speakers: ["Sanne Maasakkers"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Sanne Maasakkers_Unraveling the Mind Behind the APT - Analyzing the Role of Pretexting in CTI and Attribution.pdf"
pages: 52
sha256: "e4cf62076218f388b183fe1b7951083b23f400ed36a42ae22c717fa91d419375"
text_chars: 16787
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:38:23Z"
---
# Unraveling the Mind Behind the APT - Analyzing the Role of Pretexting in CTI and Attribution

**Speakers:** Sanne Maasakkers  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Sanne Maasakkers_Unraveling the Mind Behind the APT - Analyzing the Role of Pretexting in CTI and Attribution.pdf` (52 pages)


## Slide 1

Unraveling the Mind behind the APT Analyzing the Role of Pretexting in CTI and Attribution

Speaker: Sanne Maasakkers

BlackHat USA 2024 briefings

## Slide 2

## Slide 3

## Contents

## 01 Introduction

02 Research concept 03 Analyzing content 04 Analyzing context 05 Result & demos 06 Conclusion & outlook

3

Introduction

## Slide 4

## Sanne

- Joined Mandiant Intelligence / Google Cloud in 2023 as Senior Analyst

- Previously worked in Red Team / Research & Intel Fusion Team (Fox-IT) and Fusion Centre (NCSC-NL) analyzing threats against The Netherlands

- <3 malware and being creative with (actor/threat) data

- Coach of the European CTF team, creator of Hackchallenges

- EU lead at (DEFCON’s) Adversary Village

4

Introduction

## Slide 5

Exploit Phishing Stolen Credentials % % Brute Force Web Compromise % 17<sup>10</sup> % % Prior Compromise 6 5 Server Third-Party Phishing % Compromise Compromise (Social Media) % 1 % 2 % Other SIM Swap % % 3815 3 2 1

5

## Slide 6

## Threat groups

Introduction

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Threat groups
ae
Introduction
TEMP.
\
Uy
.Y -
e- ‘
——/%
‘UNC.
```

## Slide 7

## Threat groups

Introduction

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Threat groups
ae
Introduction
TEMP.
\
Uy
.Y -
e- ‘
——/%
‘UNC.
FIN
```

## Slide 8

## Threat groups

UNC
UNC UNC
UNC
UNC
UNC
UNC
UNC UNC UNC UNC
UNC
UNC
UNC
UNC
UNC
UNC

8

Introduction

## Slide 9

## Clustering

Emails are associated with a threat group mostly through various technical, tactical and strategical indicators, including: - Technical : reuse of malware or code within malware attachments, reuse of infrastructure, including IP addresses, domains, and hosting providers.

- Tactical : consistent use of specific tactics in the infection chain, patterns in infrastructure.

- Strategical : common geographical and industry targeting.

Behavioral

9

Introduction

## Slide 10

## Spear phishing

10

Introduction

## Slide 11

## Concept

This research focuses on the behavioral characteristics of APT phishing emails, including the pretext and email scenario, and their importance in linking (new) phishing campaigns to their authors. This includes both the content and context of the email.

11

Research concept

## Slide 12

## Example

Subject: [software] update

### Dear,

If you already have [software] installed on your computer, you'll be asked to download and install the update. Once the new update is installed, [software] should function normally. [install instructions including download link] You must have administrative privileges on your computer to install [software].

Subject: Access has been changed

Dear,

This message is to notice you that we have built a new [type] system. The certificate for the current [software] client will soon expire and prevent users from logging on. [install instructions]

Please contact the staff if you have any questions.

### Servicedesk

### ServiceDesk

12

* Emails are slightly altered for security and privacy purposes

Research concept

## Slide 13

VIBEINT refers to information obtained from a gut feeling or intuition, often based on previous experience. It is mostly unverified and unreliable, but it can sometimes provide insights or lead to further investigation.

13

Research concept

## Slide 14

## Scenario

https://blog.sannemaasakkers.com/2021/08/07/adversary-phishing-characteristics/

14

Research concept

## Slide 15

## Content

Subject: [software] update

Dear,

If you already have [software] installed on your computer, you'll be asked to download and install the update. Once the new update is installed, [software] should function normally. [install instructions including download link] You must have administrative privileges on your computer to install [software].

ServiceDesk

EmailSubject

Salutation

Language Textual features

Attachment or URL

Signature

* Email is slightly altered for security and privacy purposes

15

Research concept

## Slide 16

## Context

Sender type

Subject: [software] update EmailTheme

Dear,

If you already have [software] installed on your computer, you'll be asked to download and install the update. Once the new update is installed, [software] should function normally. [install instructions including download link] You must have administrative privileges on your computer to install [software]. ServiceDesk

Persuasion

Goal

Design

* Email is slightly altered for security and privacy purposes

16

Research concept

## Slide 17

## Analysis

Dataset
Textual features Contextual features
Stylometric analysis Language analysis Context analysis
Combined model

17

Research concept

## Slide 18

Stylometry is the statistical analysis of linguistic style in written or spoken language, aiming to identify patterns and features unique to specific authors. This analysis can be applied to attribute authorship.

18

Analyzing content

## Slide 19

## Stylometry

It uses statistics to analyze an author’s lexical and syntactic features .

- Lexical features: word frequencies, word length distribution, Hapax Legomena, vocabulary richness.

- Syntactic features: sentence length, average word length, punctuation usage.

Think of it as identifying someone based on how they talk, not (just) what they say.

It is a common technique and already used to analyze (anonymous) authors , threatening letters or ransom texts .

19

Analyzing content

## Slide 20

## Example

Stylometric 1

Dear Sir, For your information. See the attach.

Stylometric 2

[month] Financial Data Table. Have you got it? Please check it.

Lingua

average_length short_words proportion_digits average_length short_words proportion_digits
4.625 0.50 0.0 4.63 0.36 0.0
proportion_capital text_richness hapax_legomena proportion_capital text_richness hapax_legomena
0.09 1 8 0.09 0.82 9

20

* Emails are slightly altered for security and privacy purposes

Analyzing content

## Slide 21

## Stylometry

However, stylometry has several limitations, including:

- Semantic understanding : it does not understand the meaning of words or the nuances of language.

- Contextual awareness : it struggles to analyze relationships between non-sequential words, sentences, or paragraphs, missing the broader context of the text.

- Domain-specific knowledge : it lacks understanding of specialized fields or jargon, which can be crucial for accurate analysis in certain types of texts.

21

Analyzing content

## Slide 22

## Stylometry

While stylometry has been used for years in authorship attribution, its efficacy on APT emails is limited. A trained model on a relevant dataset results in an overall accuracy of 41% .

01 Text richness

- 02 Average number of words/sentence

03 Distribution of unicode characters

22

Analyzing content

## Slide 23

A language model analyzes text by considering the context of each word, capturing subtle nuances in meaning, and understanding complex word and sentence relationships.

23

Analyzing content

## Slide 24

## Language model

Pre-trained models can be used to perform various natural language processing tasks like text classification. They provide a powerful starting point for fine-tuning on specific tasks, saving time and resources compared to training from scratch.

BERT is a pre-trained language model based on the transformer architecture.

Transformers are deep learning models that use multi-head attention to weigh the importance of different words in a sentence, allowing for better understanding of context and meaning.

24

Analyzing content

## Slide 25

## Language model

This resulted in an accuracy of 60% on all 33 actors. But how? Machine Learning models can be explained by SHAP (SHapley Additive exPlanations). So; what happens if you try to predict a new text on the fine-tuned language model?

25

Analyzing content

https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns

## Slide 26

Important information. Due to the deterioration of the epidemiological situation, as well as due to the increase in the number of sick of the Omicron COVID-19 embassy staff, the Embassy of the Republic of Turkey is being transferred to a state of isolation and closed to the public. Please check the list of sick employees to identify the possibility of contact with them. All detailed information about the sick, as well as about the new mode of operation of the embassy in the attachment. -- Please confirm receipt of the email with a return

response.

## Slide 27

0.047

0.113

Important information. Due to the deterioration of the epidemiological 0.093 0.117 0.03 0.034 1.000 situation, as well as due to the increase in the number of sick of the Omicron 1.000 0.153 COVID-19 embassy staff, the Embassy of the Republic of Turkey is being 0.236 0.047 0.028 0.021 transferred to a state of isolation and closed to the public. Please check the list 0.032 0.014 0.089

of sick employees to identify the possibility of contact with them. All detailed 0.079 0.0127 0.723 information about the sick, as well as about the new mode of operation of the 0.059 0.001 0.033 embassy in the attachment. -- Please confirm receipt of the email with a return 0.005

response.

27

## Slide 28

## Content analysis highlights

01 For replies, the language used was not always consistent with the language of the initial email.

- 02 Similar emails could be written in completely different languages and discuss entirely different topics.

- 03 It's not just about using theme-specific words; it also focuses on the grammar used, such as "had [adverb] [past participle]" or speaking in the first person.

28

Analyzing content

## Slide 29

The context of an email includes elements that shape its meaning and purpose, such as theme, goal and the social engineering techniques employed to influence the recipient.

Analyzing context

29

## Slide 30

## Extracting these features

Large Language Models (LLMs) can effectively extract key contextual elements from emails, including:

- The inclusion of personal touches or signatures

- The overall theme of the email

- The social engineering techniques used to influence the recipient

The local LLM is given extra training documents to better understand and classify these features from emails and do simple categorization tasks.

30

Analyzing context

## Slide 31

## Theme

Analysis of email themes reveals the most common

themes are as follows:

- Invitations or requests (meetings, interviews, events)

- COVID-19 related (absences, changes)

- Account issues (resets, problems, settings)

These are categorized into the following categories:

- A recent event (COVID-19 or global events)

- An important value for the receiver (proposals)

- A timeless and generic theme (please find attached)

```
prompt=f"Iwillgiveyouthe
subjectandcontentofanemail.
Firstofall,givemethemain
themeoftheemail.Additionally,
knowabout
youeverything
Cialdini's6principlesof
influence:Reciprocity,
CommitmentandConsistency,
SocialProof,Authority,Liking,
andScarcity.Basedonthe
suppliedtext,Iwantyoutogive
methemostlikelyprincipleused
inthetext(orNoneifnoneof
theprinciplesmatch)andthe
reasonwhyinmaximumof30
words.\nFormatinstructions:
{format_instructions}\nEmail
subject:{subject}\nEmail
content:{body}\n"
```

Analyzing context

31

## Slide 32

## Social engineering

The principles of influence , defined by Cialdini , are a set of psychological and social phenomena that can be used to influence behavior and decision-making.

By leveraging these principles, phishers can create a sense of urgency, trust, or authority that overrides the recipient's natural caution.

```
prompt=f"Iwillgiveyouthe
subjectandcontentofanemail.
Firstofall,givemethemain
themeoftheemail.Additionally,
knowabout
youeverything
Cialdini's6principlesof
influence:Reciprocity,
CommitmentandConsistency,
SocialProof,Authority,Liking,
andScarcity.Basedonthe
suppliedtext,Iwantyoutogive
methemostlikelyprincipleused
inthetext(orNoneifnoneof
theprinciplesmatch)andthe
reasonwhyinmaximumof30
words.\nFormatinstructions:
{format_instructions}\nEmail
subject:{subject}\nEmail
content:{body}\n"
```

Analyzing context

32

## Slide 33

## Principles of influence

Principle: Authority

Greetings!

On behalf of [important person in policy], I would like to invite you to a briefing with [important person in policy] on [date]. [person] will discuss [topic] and your input will be appreciated.

Kind regards, [name]

Invite.hta

Principle: Commitment and Consistency

Dear [name],

As a follow up on our conversation, I’m sending you the job profile of the developer position at [organization] attached. Looking forward to hearing from you soon.

Kind regards, [name] [recruiter at organization] Job profile.doc

33

* Emails are slightly altered for security and privacy purposes

Analyzing context

## Slide 34

## Principles of influence

Principle: Liking

Hey [name],

Long time no see and best wishes for the New Year! I hope that you will find good health and luck in the upcoming year. Please find my New Year’s wishes attached on this URL:

[URL]

[name]

Principle: Reciprocity

Hi [name],

Sorry for sending this via [platform], but I’ve had a lot of struggles uploading the files. Hope this is OK! Hope it works for you now, it should only be accessible by you. Let me know if there are problems.

[URL to platform]

[name]

34

* Emails are slightly altered for security and privacy purposes

Analyzing context

## Slide 35

## Principles of influence

Principle: Scarcity

Hi [name],

As mentioned, just wanted to pass this document. The password is 123456. This is a confidential document, so please don’t share it with anyone.

Thank you and we keep in touch.

Principle: Social Proof

Hey [name],

My name is [name] and I’ve recently had a talk with [person X, person Y]. We were wondering if you would be interested in joining [project Z], we definitely think you’re the right person with valuable insights. Please find more details here: [URL]

[name]

Files.rar

Kind regards, [name]

35

* Emails are slightly altered for security and privacy purposes

Analyzing context

## Slide 36

Context 36

## Slide 37

## Context

The prediction model built on contextual features achieved a 67% accuracy across all authors, with the following features being the most prevalent:

- 01 Principle of influence

02 Sender category 03 Theme

37

Analyzing context

## Slide 38

The models are combined with a meta model. A meta-model is a higher-level model that learns how to best integrate the predictions or outputs of the three individual models and is used for this analysis.

Result & demos

38

## Slide 39

## Result

The total accuracy of all three models combined (and tuned) results in an overall accuracy to 88 - 96%, after removing the least performing actors from the set. Insufficient data for certain actors impacts the model's ability to learn their patterns effectively, so the model is not fully able to make predictions for those actors.

The remaining groups represent interesting groups that have been active in the last years .

Result & demos

39

## Slide 40

## Analysis

Let’s dive in some visualizations and examples of how it helps clustering.

Get insights in clusters Find similarities and differences 1

Finding outliers Reconsider the links 2 Find author Cluster with more confidence 3

Result & demos

40

## Slide 41

Result 41

## Slide 42

Result 42

## Slide 43

Result 43

## Slide 44

Result

44

## Slide 45

Result

45

## Slide 46

## Subclusters

Multiple actors (labels) have subclusters within their respective clusters. A review of these subclusters revealed the following:

- Change in targeting : actors have adapted their writing styles based on the targets (geographical, industry or person).

- Change over time : subclusters showed emails sent around the same time. Although the content is totally different, these emails might be part of the same campaign.

- Distinct cluster : UNCs are considered part of the actor, but this isn't necessarily the case. They could represent a separate cluster, an affiliate, or simply another individual.

Result & demos

46

## Slide 47

## Find author

comment:”#muddywater” has:email_parents

18 results

Result & demos

47

## Slide 48

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
(tft_m3) sanne@Sannes-MBP APT-emails % python3 predict_emails.py --folder emails/Predict --actor "TEMP.Zagros" —-threshold 80 JJ
```

## Slide 49

## Conclusion

The proposed model for clustering campaigns based on behavioral features has proven effective in analyzing the majority of emails from both APTs and TEMPs.

This underscores the potential of behavioral analysis to contribute to the accurate clustering of groups or linking new attacks to groups , next to clustering techniques already in place. It can aid threat intelligence analysts to understand trends and new phishing TTPs leveraged by specific threat actors and support in threat hunting.

Conclusion & outlook

49

## Slide 50

## Outlook & implications

Further research could involve incorporating technical , tactical and strategical attributes into the model to have a full overview of a campaign. As discussed, those models have limitations, but so does this model:

- LLM usage: The use of LLMs for generating the email text can blur the lines between actors' writing styles.

- Copycats : Actors tend to use the same themes in emails based, like a recent event or even mimic other actors in their emails.

Conclusion & outlook

50

## Slide 51

The streets of persuasion are plated with gold

The Killers - The Rising Tide

51

## Slide 52

# Thank you

X @sannemaasakkers LinkedIn /sannemaasakkers
