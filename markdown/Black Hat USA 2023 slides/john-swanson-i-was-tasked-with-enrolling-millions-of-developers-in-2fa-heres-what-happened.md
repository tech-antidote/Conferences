---
title: "I Was Tasked With Enrolling Millions of Developers in 2FA - Here's What Happened"
speakers: ["John Swanson"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/John Swanson_I Was Tasked With Enrolling Millions of Developers in 2FA - Here's What Happened.pdf"
pages: 48
sha256: "3fa5b6e85f42550ac1edd71a8c59b39bfa095d803bda54b94ae50495b92861ff"
text_chars: 14964
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:12:01Z"
---
# I Was Tasked With Enrolling Millions of Developers in 2FA - Here's What Happened

**Speakers:** John Swanson  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/John Swanson_I Was Tasked With Enrolling Millions of Developers in 2FA - Here's What Happened.pdf` (48 pages)


## Slide 1

**I Was Tasked with Enrolling Millions of Developers in 2FA — Here’s What Happened**

**John Swanson** https://infosec.exchange/@swannysec https://twitter.com/swannysec

## Slide 2

# **Story Time**

Created with Midjourney

## Slide 3

### **Who am I?**

- You can call me **Swanny**

- • Director, Security Strategy **@GitHub**

- • Planning, leadership, program management.

- **Dad, nerd**

## Slide 4

### **Agenda**

**Problem statement and associated challenges Strategy**

**Tactics**

**Current state and what comes next Key lessons**

## Slide 5

**What’s the problem?**

## Slide 6

**Protecting Developers** The software supply chain starts with the developer. How do we keep developers safe?

Supply Chain ("ingredients")
User Accounts Dependencies Your Code Build Process Distribution
End-to-End Supply Chain
("ingredients + integrity")

## Slide 7

#### **What’s missing? 2FA**

GitHub.com 2FA Adoption


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What's missing? 2FA
0%
W 2FA
(GitHub.com 2FA Adoption +)
```

## Slide 8

Our Objective


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C Our Objective +)
GitHub will require all users who
contribute to code on GitHub.com
to enable one or more forms of
two-factor authentication (2FA)
by the end of 2023.
```

## Slide 9

#### **Two Core Issues**

**2FA is still hard 2FA adoption to use and easy often conflicts to lose with business** 😞 **goals**

## Slide 10

#### **The Classic Security Problem**

- We need to introduce a new security measure which introduces cost or appears to slow users down.

- How do we get where we need to go in the face of competing priorities?

- How can you do so while limiting the downsides and maximizing the upsides?

- How do we preserve trust/buy-in and crush the “culture of no?”

## Slide 11

#### **Strategy and Tactics In a Business Setting**

- **Strategy pursues** the higher level **business objectives and outcomes.**

- • **Tactics define how** individual workstreams contribute to those objectives and outcomes at the ground level.

**• Both are essential.**

- “ <u>Portrait of Carl von Clausewitz,</u> ” Karl Wilhelm Wach, Public Domain.

## Slide 12

**Strategy**

## Slide 13

#### **On Strategy**

**Opening moves matter!** Set your initiative up for success by aligning with the business.

## Slide 14

Understand the
Problem Deeply
• Research and discovery
is critical  before planning
or executing!
• Involve a wide set of
stakeholders  early.
Created with Midjourney

## Slide 15

**Research Head Start**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Research Head Start
OpenSource Security
Enrolling all npm publishers in
enhanced login verification
and next steps for two-factor
authentication enforcement
Today we're introducing enhanced login verification to the npm registry, and we will begin a
staged rollout to maintainers beginning Dec 7.
```

## Slide 16

#### **Establish Principles to Align Tactics with Strategy**

- Figure out **how you want to work** .

- What cultural values do you want to capture? Is there a specific approach you want to apply?

- • **Document these** and use them to make sure you’re on the right course later.

## Slide 17

#### **Our 2FA Operating Principles**

- **Internal metrics on user activity must not be viewed as obstacles to account security improvements** since those metrics are meaningless if we lose the overall trust of our customers through ATO and supply chain compromise.

- Conversely, **security improvements must not come at the expense of user experience (UX) or make the product inaccessible** . Security that isn’t usable isn’t security.

- **Good account security** is a core feature and trust preservation measure that **should not rely on additional licensing** . Security is a right, not a privilege.

## Slide 18

#### **Write it Down**

   - **Capture** at minimum: - The problem and why it needs to be solved

   - - Operating principles

      - The objective and relevant success criteria

   - Then **socialize it widely!**

- " <u>The Rosetta Stone,</u> " libookperson, licensed under <u>CC BY 2.0.</u>

## Slide 19

##### **Want a template to make this easy?**

**<u>https://github.com/swannysec/strategic-planning-template</u>**


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q swannysec / strategic-planning-template
Code Issues Pull requests Actions Projects Wiki Security Insights
Wanta tem plate re renames |
make this easy? — ~
Preview | Code Blame rw O 4 0 ~
The purpose of this document is to define a high-level strategic proposal (along with any potential alternatives) to
share with leadership for their approval and/or feedback and build better alignment among project teams. This
document is also designed to provide a clear “north star” for subsequent tactical planning and execution. This
document will help accountable leaders bring clarity to the problem they're trying to solve, the principles by which
they will solve the problem, the success criteria, and a sense of the lift and critical dependencies associated with the
work. Using this template helps build and maintain a sense of alignment among leaders, individual contributors, and
leadership by making clear where you're going, why, and how.
Problem Statement
What is the specific problem that needs to be solved? How does it impact your organization's effectiveness or values,
customer outcomes, or revenue outcomes? What risk does it present? What happens if you fail to address it? This
section tells the story of why you should undertake this work. Keep this section as plain and straightforward as you
can so the problem is readily understood. Save the complexity for later.
Objectives
What are the primary objectives for this program? Keep these short and sweet, without complexity. Use bullets, try to
have no more than five total objectives, and where possible make sure the outcomes are measurable (binary
objectives are ok where you simply need to establish something new!). Make sure the objectives consider all
necessary business needs including customer and internal requirements, risk, sustainability, and scalability. If you
intend to ship something that isn’t safe or that you can’t maintain, you probably need to reassess your objectives.
Operating Principles
lat Are there already a set of existing operating principles that this program will operate under? If not, what should they
emplate be? These statements should reflect company values, business or customer requirements, and anti-goals if necessary.
https ithub.com/swannysec/strategic-plannin
These help guide decision making in a consistent manner through the life of a program. Again, use simple, bulleted
statements.
```

## Slide 20

Is preparation
just blocking
iterative process?
Strategy isn’t optional.
Would you build your house
without a foundation?
Created with Midjourney

## Slide 21

**Tactics**

## Slide 22

#### **On Tactics**

- We built a **healthy, collaborative environment**

- • We applied **no-BS pragmatism**

- **Data** drove our decisions

- • We **focused on user experience (UX)**

- We invested in **communications**

## Slide 23

Psychological
Safety =
Encourage the best work from
everyone by  building  an
environment which encourages
psychological safety  and open,
trust-based collaboration .
Photo by me!

## Slide 24

#### **Collaboration is a Catalyst**

- **Cast a wide net** to assemble the right contributors and build support for your efforts.

- • **Look beyond security** , engineering, and product.

Created with Midjourney

## Slide 25

#### **Who should be at the table?**

• Engineering, Product, Security • Support, Customer Success, Sales, Sales Engineering

• Internal Comms, PR, Marketing, Legal

## Slide 26

#### **Pragmatism Beats Optimism**

- **Make** hard, but **decisive choices** that lean toward ground truth over hope.

- Ensure objectives are **sustainable** .

   - noun

1. A practical approach to problems and affairs | tried to **strike a balance between principles and pragmatism**

“Pragmatism”, Merriam-Webster.com Dictionary.

## Slide 27

" Created with Midjourney
Rhodes Park School Pupils in the School Computer Lab, " by IICD,
licensed under  CC BY 2.0.

#### **Pragmatism in Practice**

- We want **strong security outcomes** .

- We also **need to reach a diverse global audience** with different accessibility challenges.

- Decision: We chose **balanced objectives that don’t exclude** developers.

## Slide 28

#### **Let the Data Be Your Guide**

- **Explore data** to figure out what the business can already tell you.

- **Measure** the effectiveness of what you build via **KPIs** and adjust as needed!

## Slide 29

#### **User Experience is Everything**

- If 2FA isn’t **usable and durable** , can you really enroll millions of people and not make them miserable?

- Challenges: - Accessibility/availability of factors

Created with Midjourney

" <u>LEGO 'Grumpy Cat' meme,</u> " Ochre Jelly, marked with Public Domain Mark 1.0.

- Durability/resilience to loss

- - Ease of configuration/use

## Slide 30

**More Factor Options**


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
More Factor Options
©) wrycittube Team Enterprise Explore Marketplace Pricing
a
4:03
Thursday, January 20
development platform,
in your pocket
Google Play [f @ App Store
```

## Slide 31

#### **New 2FA Configuration Flow**

**reduction in SMS 2FA registration**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
New 2FA Configuration Flow
Enable two-factor authentication (2FA)
Setup authenticator app
fe-scan the QR code
reduction in SMS
2FA registration §&
Verify the code from the app
2FA option:
© SMS authentication
```

## Slide 32

#### **Scheduled 2FA Verification**

**of users safely re-configure 2FA without lockout**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Scheduled 2FA Verification
Verify your two-factor authentication (2FA) settings
Monalisa Octocat
monalisa
of users safely
re -config u re 2 FA This is a one-time verification of your recent configured 2FA credentials.
without lockout @
Make sure that 2FA is correctly configured, and avoid a potential account lockout
disaster. If you're having trouble verifying, you'll be able to reconfigure 2FA for your
account.
You can choose to skip 2FA verification at this moment, we'll remind you again
later.
```

## Slide 33

#### **Preferred Factors**


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Preferred Factors
Two-factor authentication
Two-factor authentication adds an additional layer of security to your account by requiring more than just a password
to sign in. Learn more about two-factor authentication.
Two-factor methods
EF] Authenticator app Enabled ) ( Preferred
Use an application on your p ctor authentication codes w
a) SMS/Text message bled
You will ri 'e authentication code to this phone number: +1 206550123
Security keys are hardware that can be used as your second factor of authentication
€) itHub Mobile 2 devices
GitHub Mobile can be used for two-factor authentication by installing the GitHub Mobile app and signing in to your
ount
```

## Slide 34

#### **Slow and Steady Wins the Race**

Regular in-product reminders, occasional email reminders

Prompt to enable 2FA once a day when accessing GitHub

Blocked from accessing GitHub features until you enable 2FA Validate that your 2FA setup is working correctly

Speed kills. It’s tempting to be bold and ship fast. It’s also a good way to end your 2FA project before it gets off the ground!

## Slide 35

Customer-facing
Roles are Amplifiers
• Support, Customer Success,
and Sales preparation isn’t a
“nice to have.” It’s  essential .
• Consider:
- Business process
- Policy
- Awareness " Mega-megaphone, ” Gruenemann, licensed under CC BY 2.0.

## Slide 36

#### **Communicate Early and Often**

- Engage your PR, marketing, and internal communications teams.

- Be **clear, consistent, and transparent** in your comms. Explain why.

- Include a **straightforward call to action** .

- **Use multiple forms** of communication!

## Slide 37

## **Results and Next Steps**

## Slide 38

#### **Initial**

#### **Feedback =** 💖


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
l n i t i a | (> Andres Pineda
. Folks at @github care so much about your security that they get very
—
happy when we turn on 2FA on our accounts.
a) Paul Razvan Berg @ EthCc fi @
If you haven't done it yet, go and bring them some happiness ©? ©
#Security #MFA
Major props to @github for making 2FA mandatory for all code .
contributors.
This is an important step towards enhancing the security of the Internet.
[GitHub 2FA] Your GitHub account, PaulRBerg, will & 3) Stephen Shankland
require 2FA ~
Microsoft's @github now requires 2-factor authentication. Get used to it .
— it's the wave of the future.
wane teria artan mm With all the open-source projects at Github 2FA makes it harder for bad
ee actors get access and insert malware that'd distributed to other projects.
You don't need to do anything in re
github.blog/2022-05-04-sof...
```

## Slide 39

#### **2FA Adoption vs. Ticket Volume**

**reduction** in 2FA-related support tickets per 100k users


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2FA Adoption vs. Ticket Volume
2FA Adoption
2FA-related Tickets
reduction in 2FA-related
support tickets per 100k
```

## Slide 40

#### **Account Lockouts**

**reduction** in account lockout recovery attempts per 100k users


> Recovered by OCR — confidence 96/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Account Lockouts
Daily Account Recovery Attempts
reduction in account lockout
recovery attempts per 100k
```

## Slide 41

#### **Recovery Code Interaction**

**increase** in recovery code downloads or prints per 100k users


> Recovered by OCR — confidence 96/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Recovery Code Interaction
Daily Recovery Code Retrievals
increase in recovery code
downloads or prints per 100k
```

## Slide 42

#### **Positive Ecosystem Impact**

“ <u>Securing PyPI accounts via Two-Factor Authentication.”</u> Donald Stufft.

“ <u>Requiring MFA on popular gem maintainers.”</u> Jenny Shen.

## Slide 43

#### **What’s Next?**

- Lots of users left to enroll!

- Passkey support

• 2024+


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Lots of users
left to enroll!
Passkey
support
2024+
Security
Introducing passwordless
authentication on GitHub.com
Passkeys are now available in public beta. Opting in lets you upgrade security keys to
passkeys, and use those in place of both your password and your 2FA method.
```

## Slide 44

**Key Lessons**

## Slide 45

#### **Lessons for 2FA**

- **Trust by design: optimize user experience** and internal preparation **before raising requirements!**

- **Think hard about whether 2FA is feasible for everyone.** Consider alternatives or **adjust your objectives to add flexibility.**

- **Invest** effort **in solid communication** (internal and external). Lean into comms specialists.

- **Moderate the pace of enrollment** to allow improvements!

## Slide 46

#### **Lessons Useful Beyond 2FA**

- **Prepare thoroughly and write these down, then share broadly:**

   - Problem statement and relevant **data from research**

   - Operating **principles**

   - Clear and **sustainable objectives**

- **Leadership and culture matter.**

   - Maintain a **psychologically safe** , positive team **environment**

   - **Collaborate** with teams **across the whole organization**

## Slide 47

#### **Acknowledgments**


> Recovered by OCR — confidence 88/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
cknowledgments
@
@abbashaiderali @anna-talley @brotherben @buckelij @chriskirkland @cli1150 @flamingolegs @forced-request @galaxyallie
@gennyburleson @hagould @hemantkumar @hpsin @iburtally @jamespetercross @jessephus @jessicacano @johnpreed
@josepalafox @juliettewyman @juststephanie @kith @lauraleap @lgarron @liliana3186 @lowply @mattsalem
@maya-ross @mayamessinger @mumileski @mph4 @mylesborins @nebiyou- @oreoshake @ptoomey3 @rajlaud
gebretatios
@reversaw @richard-saunders @robcrystalornelas @rzomayah @samanthachau @samkovacs @samueldev @sseacrest @stehley
8
@steiza @sumojava @taz @tiedyefridays @vesjones @whitneystewart @yukaav @zacharysierakowski @zack-evans
```

## Slide 48

#### **Questions?**

**Need more info on GitHub’s 2FA efforts?** <u>https://github.blog/tag/2fa/</u>

**Want to follow-up?** swannysec@github.com or swanson.john.d@gmail.com <u>https://swannysec.net https://twitter.com/swannysec https://infosec.exchange/@swannysec</u> Planning Template
