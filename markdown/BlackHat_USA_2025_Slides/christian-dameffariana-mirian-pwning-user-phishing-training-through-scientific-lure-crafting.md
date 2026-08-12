---
title: "Pwning User Phishing Training Through Scientific Lure Crafting"
speakers: ["Christian Dameff", "Ariana Mirian"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Christian Dameff&Ariana Mirian_Pwning User Phishing Training Through Scientific Lure Crafting.pdf"
pages: 49
sha256: "f4e98dc249409ca11881b6d3e1e2ec65a1b48be9a7591460945fb5cdd2286892"
text_chars: 12577
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:51:22Z"
---
# Pwning User Phishing Training Through Scientific Lure Crafting

**Speakers:** Christian Dameff, Ariana Mirian  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Christian Dameff&Ariana Mirian_Pwning User Phishing Training Through Scientific Lure Crafting.pdf` (49 pages)

## Slide 1

# Pwning Phishing Training Through Scientific Lure Crafting

Dr. Christian Dameff, MD & Dr. Ariana Mirian, PhD

Black Hat 2025, Human Factors Track

## Slide 2

## Who are we?

● Associate professor @ UCSD

- Co-director @ UCSD Center for Healthcare Cybersecurity

- Security researcher focused on Internet measurement/security

- ● Currently @ Censys, Previously PhD @ UCSD

## Slide 3

## Agenda

● Background & Motivation ● Study Setup, Design, & Methods

● Lessons Learned (and what that means for users) ● Summary

## Slide 4

Audience poll: Does user phishing training work?

## Slide 5

Background + Motivation

## Slide 6

## Phishing Training works…right?

● Many organizations (including ours) perform trainings ○ Annual cybersecurity awareness trainings ○ Simulated phishing tests (embedded trainings)

● Teach a person to spot a phish, and they are trained for life ○ “Human firewalls”

## Slide 7

## Background

● Much prior research is in favor of anti-phishing training ○ i.e : [Jampen et al. 2020] ○ Often lab studies

● Some recent studies that show opposite results ○ I.e : [Lain et al. 2022]

○ Increasingly real world studies with actual users

● Problem: How do we reconcile these conf l icting studies?

## Slide 8

Underlying research question: What is the best modality for anti-phishing training?

## Slide 9

Many different modalities – which to focus on?

Static

Interactive

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
any different modalities — which to focus on?
Click on each of the red flags below to learn more.
Don't Worry!
This is a simulation sent from UC San Diego Health.
Subject: Re: COVID-19 &
Had this been real you wouldve been phished. @ From: HR <hr@yourorganization.com> ©
Reply-To: HR <hr@fakeaddress.com>
To: you@yourorganization.com €
CC: maxine@adifferentorg.net, sergio@college.edu
Date: Monday, June 9, 4:30AM ©
Image of the sender and phishing message,
with warning signs highlighted. { i COVID-19 Policy ©
#2 2MB
The following organization policy has been updated:
COVID-19 - Return to Work Guidelines
Here are five warning signs to watch out for:
Please read and understand the updated guidelines regarding a COVID-free return to the office. It is URGENT that you read this as soon as
possible!!!
Click HERE or di ad the attachment to read the ©
Advice Text
Summary of which of the five warning signs were present in the phishing em:
Please do not share your experience with colleagues, so they can learn too.
Click to acknowledge and close
You are require to enter your username and password before viewing in orfer to register your acknowledgement of the policy update.
Static Interactive
```

## Slide 10

## Let’s Treat Security Research like Medical Research

Medical Outcomes

Security Outcomes

## Slide 11

## Let’s Treat Security Research like Medical Research

Medical Outcomes

Security Outcomes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s Treat Security Research like Medical Research
The Drug Development Process
Stop 1
Discovery and
Development
Step 2
Precinicl Research
Stop 3
Cinical Research
Stop 4
FDA Review
Step 5
FDA Post-Market
Safety Monitoring
Discovery and Development
Research for a new drug begins in the laboratory.
‘More Information
Preclinical Research
Drugs undergo laboratory and animal testing to answer
basic questions about safely.
“More Information
Clinical Research
Drugs are tested on people to make sure they are safe
and effective.
‘More Information
FDA Review
FDA review teams thoroughly examine all of the
submitted data related to the drug or device and make a
decision to approve or not to approve it.
‘More Information
Medical Outcomes
Security Outcomes
```

## Slide 12

Let’s Treat Security Research like Medical Research

- Evidence based cybersecurity should be the norm.

   - Bloodletting & mercury = bad

- Instead of spending millions of dollars AND hours on ineffective solutions, let’s find the EFFECTIVE ones with science.

## Slide 13

Methodology

## Slide 14

Not all evidence is equal

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Not all evidence is equal
Meta-Analysis
Systematic Review
Randomized
Controlled Trial
Prospective, tests treatment
Cohort Studies
Prospective - exposed cohort is
observed for outcome
Case Control Studies
Retrospective: subjects already of interest
looking for risk factors
Case Report or Case S'
Narrative Reviews, Expert Opinion
```

## Slide 15

Randomized 19,000+ Employees into 5 Groups

● Control (no training) ● Generic static

● Generic interactive

● Contextual static

● Contextual interactive

## Slide 16

## The 8 month experiment

- Deployed monthly simulated phishing tests ○ If user clicked, they got one of four trainings

- ○ Control group failure led to 404 page

- Users got 1/10 lures

- Collected:

   - User failure rates

   - Training engagement (ie. time on page)

   - ○ Time since last annual cybersecurity training

   - ○ And additional data

## Slide 17

Lure example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lure example
Hello,
The IT department has found that your logon password has been stolen by a hacker! We need you to update your password with our
database or it will be disabled, preventing you from accessing the system. Please go to the URL below and enter your current username
and password before your access is revoked:
Click here to reset your password
Thank you in advance for your cooperation.
IT Support
```

## Slide 18

Lessons Learned (and what it means for users)

## Slide 19

# Lesson #1: We Can Pwn Users with Scientific Lure Crafting

## Slide 20

Lesson #1: we can pwn users with scientific lure crafting

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lesson #1: we can pwn users with scientific lure crafting
Phishing Lure # of Users Avg Failure Rate
Outlook Pwd 4,931 1.82%
Login Account 12,720 1.85%
Open Enroll 14,691 7.62%
Shared Doc (Microsoft) 15,683 8.99%
OneDrive Medical 18,438 9.20%
Docusign 23,526 9.63%
Building Evac 17,359 10.33%
Traffic Ticket 17,676 18.60%
Dress Code 4,954 27.65%
Vacation Policy 17,923 30.80%
```

## Slide 21

Top Tier Lure Example

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Top Tier Lure Example
Dear %FIRSTNAME%,
Please be advised that as part of our ongoing review process, we plan to institute several fundamental changes to our dress code.
Please view these changes by visiting the Human Resources website.
This policy will go into effect 30 days from the receipt of this notice. It is up to you to know and comply with this change in dress
code.
Any staff member who does not meet the attire or grooming standards set by his or her department will be subject to disciplinery
action and may be asked to leave the premises to change clothing. Hourly paid staff members will not be compensated for any
work time missed because of failure to comply with designated workplace attire and grooming standards.
Regards,
Human Resources
UC San Diego Health
```

## Slide 22

## Lesson #1: we can pwn users with scientific lure crafting

● Whoever controls the lures, controls the failure rate!

## Slide 23

## Lesson #1: we can pwn users with scientific lure crafting

● Whoever controls the lures, controls the failure rate!

● On a long enough time frame, most people are pwned.

## Slide 24

## Lesson #1: we can pwn users with scientific lure crafting

- Whoever controls the lures, controls the failure rate!

- On a long enough time frame, most people are pwned.

● We need to stop punishing employees for failing phish.

## Slide 25

Lesson #2: Training not efficacious (for these modalities/deployment)

## Slide 26

### Lesson #2: training not largely efficacious (in these modalities/deployment)

Annual cybersecurity training has no observable benefit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lesson #2: training not largely efficacious (in these modalities/deployment)
*— Month 1
Month 2
Month 3
— Month 4
*- Month 5
*— Month 6
Month 7
*~—s— Month 8
—™ Average
To
v
oO
ee
fe)
x=
=
wn
es
(0)
wn
=
e
fo)
xs
Annual cybersecurity training has no observable benefit
```

## Slide 27

Lesson #2: training not largely efficacious (in these modalities/deployment)

Overall average improvement over control for monthly embedded training was….1.7%

## Slide 28

Lesson #2: training not largely efficacious (in these modalities/deployment) Overall average improvement over control for monthly embedded training was….1.7%

## Slide 29

Lesson #2: training not largely efficacious (in these modalities/deployment) Overall average improvement over control for monthly embedded training was….1.7%

## Slide 30

# Lesson #3: People Don’t Spend Time on Anti-Phishing Trainings

## Slide 31

## Lesson #3: people don’t spend time on training

● Coded way to measure how much time folks are spending on anti-phishing training

● We measured how much time folks are spending on training

## Slide 32

Lesson #3: people don’t spend time on training ● For the people who did spend time on training, there were different outcomes

● Static trainers did worse , interactive trainers did better

● Overall numbers were really low, so hard to generalize

## Slide 33

Lesson #3: people don’t spend time on training

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lesson #3: people don’t spend time on training
{Fike
```

## Slide 34

Is all of this focus on training worth the outcomes?

## Slide 35

We know:

## Slide 36

We know:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We know:
Phishing Lure #of Users Avg Failure Rate
Outlook Pwd 4,931 1.82%
Login Account 12,720 1.85%
Open Enroll 14,691 7.62%
Shared Doc (Microsoft) 15,683 8.99%
OneDrive Medical 18,438 9.20%
wu
i]
b
o
Docusign 23,526 9.63%
Building Evac 17,359 10.33%
Traffic Ticket 17,676 18.60%
Dress Code 4,954 27.65%
Vacation Policy 17,923 30.80%
N
o
Cumul % of users with 1+ failure
ol Ww
oO Oo
Oo
```

## Slide 37

We know:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
We know:
Phishing Lure #of Users Avg Failure Rate
Outlook Pwd 4,931 1.82%
Login Account 12,720 1.85%
Open Enroll 14,691 7.62%
Shared Doc (Microsoft) 15,683 8.99%
OneDrive Medical 18,438 9.20%
Docusign 23,526 9.63%
Building Evac 17,359 10.33%
Traffic Ticket 17,676 18.60%
Dress Code 4,954 27.65%
Vacation Policy 17,923 30.80%
wu
i]
b
°
N
o
fan
o
2
2
io)
£&
+
a
<
_
=
230
vo
a
3
.
to}
&
SB
is
5
1S)
Oo
```

## Slide 38

is all of this focus on training worth the outcome?

● We CAN find the “right” training

● How much time/effort/money will it take us?

● How much would be erased with a slightly different lure?

## Slide 39

is all of this focus on training worth the outcome?

● We CAN find the “right” training

● How much time/effort/money will it take us?

● How much would be erased with a slightly different lure?

## Slide 40

What if we put energy and resources elsewhere?

## Slide 41

We need to empirically measure these outcomes, and share the data, to better security.

## Slide 42

## Let’s Treat Security Research like Medical Research

Medical Outcomes

Security Outcomes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Let’s Treat Security Research like Medical Research
The Drug Development Process
Stop 1
Discovery and
Development
Step 2
Precinicl Research
Stop 3
Cinical Research
Stop 4
FDA Review
Step 5
FDA Post-Market
Safety Monitoring
Discovery and Development
Research for a new drug begins in the laboratory.
‘More Information
Preclinical Research
Drugs undergo laboratory and animal testing to answer
basic questions about safely.
“More Information
Clinical Research
Drugs are tested on people to make sure they are safe
and effective.
‘More Information
FDA Review
FDA review teams thoroughly examine all of the
submitted data related to the drug or device and make a
decision to approve or not to approve it.
‘More Information
Medical Outcomes
Security Outcomes
```

## Slide 43

## broaden data sharing

- Back-up claims with data

- Should vendors be the collector, disseminator, and analyzer of data?

- We don’t need to be an expert, but let’s get data in the hands of the RIGHT people

## Slide 44

Summary

## Slide 45

## In summary

● Lesson #1: we can pwn users with scientific lure crafting

● Lesson #2: trainings (as deployed) are not efficacious

● Lesson #3: people don’t spend time on training

## Slide 46

## In summary

- Recommendation #1: Let’s find the more efficacious places to put time and energy

● Recommendation #2: Empirically analyze security outcomes. Always.

## Slide 47

Audience poll: Does user phishing training work?

## Slide 48

https://arianamirian.com/docs/ieee-25.pdf

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Understanding the Efficacy of Phishing Training in Practice
Grant Ho®t Ariana Mirian‘t Elisa Luot Khang Tong*t Euyhyun Lee*?
Lin Liu*t Christopher A. Longhurst* Christian Dameff* Stefan Savaget Geoffrey M. Voelkert
TUC San Diego °University of Chicago *UC San Diego Health
Abstract—This paper empirically evaluates the efficacy of two
ubiquitous forms of enterprise security training: annual cy-
bersecurity awareness training and embedded anti-phishing
training exercises. Specifically, our work analyzes the results
of an 8-month randomized controlled experiment involving ten
simulated phishing campaigns sent to over 19,500 employees
at a large healthcare organization. Our results suggest that
covering over 133M health records, and 460 associated
ransomware incidents (more than one per day) [2], [11].
Absent an effective technical defense, organizations have
turned to security training as a means to staunch the bleed-
ing. Our own institution admonishes each of us to “Be a
Human Firewall” — to identify and resist enticements to
click on suspicious email-borne links. Indeed, in many sec-
https://arianamirian.com/docs/ieee-25.pdf
```

## Slide 49

## Thank you!

@quaddi@gmail.com @cyberhealth.ucsd.edu @cdameff.bsky.social @cdameff

@arianamirian28@gmail.com @arianamirian.com @arianamirian.bsky.social @arianamirian
