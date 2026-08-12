---
title: "Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future"
speakers: ["Sid Rao", "Gabriela Sonkeri", "Amel Bourdoucen", "Janne Lindqvist"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Sid Rao&Gabriela Sonkeri&Amel Bourdoucen&Janne Lindqvist_Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future.pdf"
pages: 55
sha256: "63679c31c8a9ffd1e11243c2b4734fe3b8f2cad9aa58f9d0ba04bde8bb35fda3"
text_chars: 27544
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: ["Sid Rao&Gabriela Sonkeri&Amel Bourdoucen&Janne Lindqvist_Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future_TOOLS.txt"]
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T23:01:15Z"
---
# Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future

**Speakers:** Sid Rao, Gabriela Sonkeri, Amel Bourdoucen, Janne Lindqvist  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Sid Rao&Gabriela Sonkeri&Amel Bourdoucen&Janne Lindqvist_Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future.pdf` (55 pages)


## Slide 1

## Lost & Found

The Hidden Risks of Account Recovery in a Passwordless Future <u>Speakers:</u> Sid Rao, Gabriela Sonkeri

**Blackhat USA 2025** August 7, Thursday

Note: This handout version of the slide deck has slightly different (and more) content than the presentation version

## Slide 2

#### ~~Who are we?~~

Dr. Sid Rao

Gabriela Sonkeri *

Senior Security Security Engineer Researcher

Amel Bourdoucen *

Prof. Janne Lindqvist

User and Impact Associate Professor Researcher

**Nokia Bell Labs** Finland

**Wolt** Finland

**F-Secure, Aalto University Aalto University** Finland Finland

* Contributions while working at Nokia Bell Labs

_Special thanks_ : Prof. Tuomas Aura, Dr. Thanh Bui, and Dr. Markku Antikainen

2

## Slide 3

#### ~~Background~~

###### **User’s authentication credentials become unavailable**

- **_<u># 1</u>_** <u>: Authentication credentials are</u> **forgotten** or **mislaid** by the user

- **<u># 2</u>** _<u>:</u>_ Authentication credentials are **inaccessible** to the user

   - Personal device is lost

   - Logging in from a new device or location

###### **Genuine-looking scenarios can be malicious**

**Genuineness cannot be verified**

Genuine scenarios in which a benign user wants to **reclaim control** over or **recover** their account

**Flaws in the recovery flow**

The service provider needs to **provision** reclaiming control in such genuine scenarios

3

## Slide 4

#### ~~Account Recovery Overview~~

An automated process provisioned by the service provider for benign users to reclaim access
Step 0 : Establish Out-of-band trust
Step 4 : Retrieve the token
Recovery Method Step 3 : Send the token
(independent communication channel)
Step 1 : Recover my account Recovery Token
(OTP or URL)
Step 5 : Submit the retrieved token
Step 2 : Generates
Step 6 : Allow recovery if token is valid recovery token
User Service Provider
Recovery Session
(unauthenticated user session)
4

4

## Slide 5

#### ~~Account Recovery Lifecycle~~

Optional steps 1 2 3 4 5 6 7 **Trigger Verification Password Security Terminate Re-authentication Account recovery** Website sends **Change Review existing Usage sessions** User User clicks, a recovery Set up a new User is presented re-authenticates User token to the e.g., “Forgot password with their Website itself to the continues password” recovery method. security settings. terminates website using the to use the Or “Unable account in any existing new password set to login” They are nudged sessions in step 3. a logged-in User proves the to review and session where the possession of better secure user was recovery their account. method by logged in to. submitting the token.

Recovery session

Log-in session

5

## Slide 6

#### ~~Motivation~~

- **Account recovery is a very common user action**

   - 4 out of 5 users have forgotten at least one credential within the last 90 days

   - 25% experiencing the need for account recovery on a daily basis

- **Account recovery is insecure by design**

   - Recovery channels are not under direct control

   - Not possible to know whether the channels are compromised

   - **○** Difficulties of distinguishing between benign users and adversaries **■** Cannot verify the authenticity of the recovery requests

- **Account recovery has not changed or won’t change much**

   - Authentication methods have evolved

   - Passwords → Passphrases → Fingerprints → Face ID → Passkeys

   - ○ Recovery relies on legacy methods of SMS and email-based channels ■ Adversaries can bypass strong authentication by exploiting weak recovery

6

## Slide 7

Account states
Recovery added  AUR MFA added AUR, MFA
without verification Account with an unverified  Account with an unverified
recovery method recovery method and MFA
Recovery added
without verification
No recovery ABM
Recovery verified Recovery verified
Account with
Account
Creation Username, password
Recovery added
after verification
AVR AVR, MFA
Recovery added
after verification Account with a verified  MFA added Account with a verified
recovery method recovery method and MFA
7

## Slide 8

#### ~~Out of Scope~~

###### **Account Hijacking**

###### **Account Remediation**

- Adversary compromises user accounts, e.g., via

   - Leaked credential dumps

   - Password brute force attacks

   - Phishing, Spear Phishing, Whaling

   - A special case of account recovery

   - ● Service provider assists a benign user recover its hijacked account

   - Involves human intervention

- Recovery channels remain intact during the compromise

   - Requires verification of the affected user’s real-life identity

- But, the adversary may want to change them soon to kick out the user completely

**We do not attempt account hijacking**

**We do not exploit account remediation**

We perform **“Account takeover“,** a lateral compromise where the adversary performs a successful account recovery

8

## Slide 9

~~Adversary Model~~ Alice Eve Mallory Chad Benign user **Controls: Controls: Knows:** recovery recovery method recovery method method, no access **Goal:** persistent **Goal:** account **Goal:** spam or lock access takeover Alice out

9

## Slide 10

#### ~~Our contributions~~

1. Auditing Framework

How to conduct a systematic analysis of account recovery of any given web service?

2. Findings

Insights on what could go or has gone wrong in the wild?

#### 3. Best Practice Recommendations

What needs to be taken into considerations for secure account recovery?

10

## Slide 11

#### ~~Terminologies~~

- **Account Recovery:** an automated process provisioned by the online service provider to their benign users for reclaiming access

- **Recovery method** :  an independent communication channel agreed between the service provider and the user

- **Recovery token** : authentication material (e.g., one-time password or link) sent by the service provider to the user through the pre-agreed recovery method

   - The recovery token is submitted back to the service provider in the recovery session

   - The recovery token is used as an alternative to the unavailable credential and grant access

- **Recovery session** : A dedicated, unauthenticated session where an account recovery process takes place

   - **_Note:_** Transmission of recovery token from the service provider to the recovery method happens outside of the recovery session

- **Recovery window** : the duration for which the recovery token stays valid

- ● **Account Takeover** :  Adversary gains control of the victim’s recovery method and uses it to perform a _lateral compromise_ of the target account associated with that method

11

## Slide 12

## Auditing Framework

12

## Slide 13

#### ~~Auditing framework~~

- **Test Setup**

   - **Test Environment:** to simulate real-life account recovery scenarios

   - **Test Process:** to guide the manual execution of the test cases

- **Test Cases**

   - Triggering recovery from different account states

   - Tinkering with recovery and MFA methods

   - ○ Observing the recovery life cycle

###### **<u>https://tinyurl.com/artha-framework</u>**

13

## Slide 14

#### ~~Test Setup~~

**Test Environment Test Process**

- Implementation ● VMs ● Browsers ● Proxies

**Benign Semi-malicious** “Trusted", previously logged in New device/location device/location

Covers Smooth Agnostic to applicable test transitions recovery flow cases and between variations account states account states

**Avoids automatic lockouts and risk-based security controls**

14

## Slide 15

#### ~~Test Case Summary~~

|Test case #|Description|
|---|---|
|Test Case 1|Account creation tests|
|Test Case 2, 3, and 4|Account state specific tests|
|Test Case 5|Recovery when there are multiple recovery methods|
|Test Case 6|Session termination tests|
|Test Case 7|Use of MFA during recovery|
|Test Case 8|Interchangeability of the recovery and MFA
factors/channels|
|Test Case 9|Settings review|

15

## Slide 16

#### ~~Account creation tests (Test case 1)~~

- Follow normal account creation and reach landing account state

- ● Check what information is collected during account creation:

   - Recovery methods

   - Whether MFA is enforced or not

   - Potential account functionality restricted after creation

- Only the mandatory fields of the forms are filled out

- The results of this test case indicate whether some attacks are invalid or not

16

## Slide 17

#### ~~Account state-specific tests (Test case 2, 3, and 4)~~

The goal of these test cases is to check how the recovery process works in these scenarios:

- Recovery when there is no recovery method

   - Is recovery even possible?

- Recovery from unverified recovery methods

   - Does the service provider inform that the method is unverified?

   - Are unverified methods use for recovery?

   - Are those methods marked as verified after a successful recovery?

- Recovery from verified recovery methods

   - Evaluate what happens during each of the stages of the account recovery lifecycle

   - Check the behavior when multiple recovery sessions are triggered simultaneously

Optional steps
1 2 3 4 5 6
Trigger   Verification Password  Security  Re-authentication Account
recovery Change Review Usage

17

## Slide 18

#### ~~Interplay between recovery and MFA methods~~

- Is it possible to have multiple recovery methods?

- ● Recovery when multiple methods available

- ● Recovery from a trusted vs untrusted device

- ● Behavior when there are changes to the recovery methods

- Leveraging MFA during recovery

- ● Is it possible to have multiple MFA factors?

- ● Recovery from a trusted vs untrusted device

- Behavior when there are changes to the MFA factors

If there’s a pool of recovery and MFA methods:

- Can recovery and MFA methods be used interchangeably during login and recovery?

Test case 5

Test case 7

Test case 8

18

## Slide 19

#### ~~Session termination (Test case 6)~~

User + pass Trigger  Trigger  Trigger
Hey, Alice! recovery recovery recovery
MFA?
Intermediate recovery
Logged in
Intermediate login session
session
session

Intermediate recovery
session

- Impact of recovery on parallel sessions

- ● Termination of parallel sessions

- Differences between a benign or semi-malicious recovery

19

## Slide 20

#### ~~Settings Review (Test case 9)~~

Analyze account settings presented by the service providers:

- How are recovery methods and MFA factors presented to the user?

- Is there an activity log for the account?

- Is there additional authentication required for changing the security settings of the account?

   - Adding/removing recovery methods

   - Adding/removing MFA factors

   - Revoking existing sessions

   - Does recovery impact this?

20

## Slide 21

## Findings

21

## Slide 22

#### ~~Dataset for Empirical Analysis~~

- **Source: Tranco list** <u>(https://tranco-list.eu/)</u>

   - Research-oriented ranking  of 1 Million websites

   - Standard for web security and Internet measurement empirical analysis

- **Shortlisted dataset** : Tranco 1M → 200 top websites →25 websites

   - Combination of top and random (excluding the top 13)

   - Matches the following selection criteria

      - ❏ Available in English

      - ❏ Non-explicit (safe at work content)

      - ❏ Fully accessible from desktop browsers

      - ❏ Allows free of charge account creation

      - ❏ Does not require real-life identities

      - ❏ Supports multi-factor authentication

      - ❏ Allows logging in with a website-based credential (not just SSO)

- Results presented in this talk are from the **22 websites**

22

## Slide 23

1. Design Flaws

2. Security Policy Weaknesses

3. Missing Best Practices

23

## Slide 24

1. Design Flaws

   - Mistakes in system’s architecture or logic

   - ● UI design related or hampers UX

   - Mismatches and inconsistencies

2. Security Policy Weaknesses

3. Missing Best Practices

24

## Slide 25

#### ~~Design Flaws~~

###### <u>#1</u> <u>Use of unverified recovery methods</u>

###### <u>#2</u> <u>Inconsistent verification</u>

john.doe@example.com **Mispelled to a non-existent Mispelled to an email of recovery method another user** john.dow@example.com john.dove@example.com

- User cannot recover their account

- May require human intervention similar to account remediation

- ● Leads to dummy or stale accounts

- John Dove may takeover John Doe’s account

- ● Account remediation is required

<u>#3 Restricting security functionalities until verification</u>

25

## Slide 26

#### ~~Design Flaws~~

###### <u>#4 Recovery flow doesn’t match account states</u>

- Email used as usernames becomes a default recovery method. But, what if

   - Account creation with email providers?

   - Only username and password required for account creation?

- What happens if there is no recovery method but the recovery is triggered?

**Recovery Requires human Recovery based on not possible intervention less secure heuristics** ● Not scalable Unpleasant user experience ● Susceptible to evil maid ● Expensive Leads to dummy or stale attacks

- Unpleasant user experience

- Leads to dummy or stale accounts

- Unnecessary exposure of ● Falls back to case 1 or 2

- real-life identities

26

## Slide 27

#### ~~Design Flaws~~

###### <u>#5 Parallel sessions are allowed to continue after recovery</u>

5.  Retrieve
4.  Send
token
Recovery
recovery
Method
token
1.  Log in to account
(username + password)
3.  Trigger recovery
2.  Start logged in session
6.  Submit token
and use the site normally
7.  Allow recovery and grant
access to account Eve
8.  Alice doesn’t
Access:  recovery
Alice notice the account  Service Provider method
takeover, since she is  Goal:  gain access
not kicked out of her  and  maintain
Parallel session  persistence
existing session
attack

27

## Slide 28

#### ~~Design Flaws~~

<u>#6 Inflexible rules</u>

**Restrictions on recovery methods** Lack of fallback options make recovery harder or unpleasant

**Restrictions on MFA methods** Limits MFA usability or hampers usability

<u>#7 Missing or unprompted activity logs</u>

**Activity log does not exist** User forfeits the option to make informed security decisions

**Exists, but user not nudged** Underutilized feature that could have helped to improve security

28

## Slide 29

#### 1. Design Flaws

- Flaws in definition, scope, or enforcement of policies

#### 2. Security Policy Weaknesses

   - Too strict or too lenient rules

   - Missing and insufficient policies

3. Missing Best Practices

29

## Slide 30

Security Policy Weaknesses
1 2 3 4
#1 MFA is not used during recovery
Trigger  Password  Account
 Verification
recovery change Usage
Recovery
Method
1.  Trigger recovery Send   arms-race begins
recovery
3.  Submit token token 7.  Trigger recovery
9.  Submit token
4. Allow recovery
5.  Change password 10. Allow recovery
6.  Grant access to account 11.  Change password
Mallory
12.  Grant access to account Alice
Controls: …
recovery method
N.  Change recovery settings …
Service Provider
Goal:  account  and kick Alice out Arms-race
takeover
attack
 arms-race ends  30
2.  Retrieve token 8.  Retrieve token

## Slide 31

Security Policy Weaknesses
1 2 3 4
#2 Password change is not enforced
after recovery Trigger   Verification Skip  Account
recovery password  Usage
change
Recovery
Method
Send
1.  Trigger recovery
recovery  7.  Log in to account
3.  Submit token token (username + password)
4.  Allow recovery
5. Skip password change 8.  Grant access to account
6.  Grant access to account
Eve
9. Alice doesn’t notice the  Alice
Controls:
account takeover, since
recovery method
her password has not
Goal:  persistent  Service Provider
access
Skip password  changed
attack
2.  Retrieve token

31

## Slide 32

### Isn’t MFA always used?

Isn’t MFA the golden standard?

What if we add MFA to the mix?

32

## Slide 33

Security Policy Weaknesses
1 2 3 4 5 6
#3 MFA is only used after recovery Trigger   Verification Password  Re-auth  MFA Account
recovery change (user +  Usage
pass)
Recovery
Method
Send
recovery  9.  Login denied
1.  Trigger recovery  token
10.  Trigger recovery
3.  Submit token 12.  Submit token
4.  Allow recovery 13.  Allow recovery
14.  Change password
5.  Change password
Mallory 6.  Enforce re-authentication 15.  Enforce re-authentication
Alice
Controls: 7.  username + password + MFA 16.  Username + password +
MFA
recovery method
8. No MFA, access denied Service Provider
Goal:  lock Alice
18.  Grant access to account
out  temporarily
Temporary
lockout attack 33
2.  Retrieve token 11.  Retrieve token

## Slide 34

34

## Slide 35

Security Policy Weaknesses
1 2 3 4 5
#4 MFA is not used from a trusted device recoveryTrigger   Verification Password change Re-auth(user +  Account Usage
pass)
11. Alice cannot retrieve
the token because she
Recovery  no longer has access to
Method 2Method the recovery method
1.  Trigger recovery from  Send  Send
Alice’s trusted machine
recovery  recovery
token token 8.  Try to log in
3.  Submit token
9.  Access denied, invalid
4.  Allow recovery credentials
5.  Change password
Mallory 6.  Grant access to account 10.  Trigger recovery
Alice
Controls:
7.  Change security settings
recovery method
+ physical  and kick Alice out Service Provider
access 12. No longer possible for
Alice to recover
Goal:  account  Permanent
takeover lockout attack 35
2.  Retrieve token

## Slide 36

Security Policy Weaknesses
#5 Password policies are not applied to Password
reuse attack
recovery lifecycle
Recovery
Method
1.  Trigger recovery from  Send
Alice’s trusted machine
recovery
token 7.  Log in to account
3.  Submit token (username + password)
4.  Allow recovery
7.  MFA checks ok
6.  Reuse current password
7.  Enforce re-authentication
8.  Grant access to account
Alice
8.  username + password
recovery method,
7.  No MFA checks (trusted) Service Provider
7.  Grant access to account 9.  Alice doesn’t notice the
gain access
account takeover, since her
36
password has not changed
2.  Retrieve token 11.  Retrieve token

Eve

**Access:** recovery method, physical access, knows password

**Goal:** gain access and  maintain persistence

## Slide 37

#### ~~Security policy weakness~~

###### <u>#6 Long recovery windows or flawed recovery token expiration policies</u>

How long should be the recovery window?

###### **Insecure or bad examples of token termination policies**

- Expires after 1 week

   - **Increased exposure of attack window**

- Expires upon use **but no auto expiration**

- ● **Does not expire on use** , but auto expires after XX duration

- **Token reuse**

37

## Slide 38

#### 1. Design Flaws

2. Security Policy Weaknesses

   - Best practice not followed

3. Missing Best Practices

- Generic best practice is not applicable or insufficient

- Best practice not available

38

## Slide 39

#### ~~Missing Best Practices~~

###### <u>#1 Inconsistency in</u> <u>communicating a lerts</u>

Alerts are not sent for all changes to Emails are prioritized as communication security settings channels for alerts **Account takeover attempts may go unnoticed to Alice arms-race attack** Change recovery No alerts sent to settings Alice about the and kick Alice out changes Mallory Service Alice **Goal:** account Provider takeover

Alice

39

## Slide 40

#### ~~Missing Best Practices~~

###### <u>#2 Account creation allows unsafe states</u>

**vs** Unverified recovery methods

MFA not required

**Weaker recovery process**

###### <u>#3 Inconsistent treatment between recovery and MFA methods</u>

Guidance on Changes to MFA Does not apply how to secure required to recovery MFA and its re-authentication methods purpose

**Lost opportunity to leverage user’s secure habits**

40

## Slide 41

#### ~~Missing Best Practices~~

#4 No rate limiting or anti-bot for unauthenticated sessions
Recovery
spam attack
Recovery
Method
Send recovery
token X T times
1. Trigger recovery
2. Trigger recovery
T. Trigger recovery
Chad T+1 . Trigger recovery Block the user account Alice
Access:
knows recovery method,  Recovery lock
but no access
out attack
Goal: spam or lock out
Alert notification X T times

<u>Note:</u> **<u>T is the threshold</u>** , beyond which the service provider considers recovery attempts as suspicious and automatically blocks the user account

41

## Slide 42

## Best Practice Recommendations

42

## Slide 43

#### ~~For Account Creation~~

**Assume user may need recovery right after signup**

Start account creation

Add and verify 2 methods

     Safe account state

Must have

❏
Two or more  verified ❏ Of  different types
authentication methods

For short flow

- ❏ Use implicit recovery ❏ Nudge users with alert methods to avoid ABM ribbons and restricted use

43

## Slide 44

#### ~~For Recovery Triggering~~

**Recovery triggering is an unauthenticated action for which imposing access control is unfeasible**

##### **Defend**

##### **Decelerate**

❏ Anti-bot protection ❏ Human verification

❏ Manual typing in the UI fields

❏ Avoid copy-pasting or auto-filling

##### **Avoid data leaks**

##### **Free user choice**

❏ Don’t leak unnecessary PII

- ❏ Partially mask recovery hints

❏ No restrictions in recovery options ❏ Default can be most or recently used

44

## Slide 45

#### ~~For Recovery Processing (1)~~

**Recovery flows should not assume by default that the recovery method is intact**

**Secure and indivisible process**

**Interchangeability of factors**

**Noticeably intrusive to ignore**

- ❏ Always do a two-factor recovery

- ❏ Batch process the two factors (i.e., tokens) to avoid TOCTOU

- ❏ Recovery and MFA methods should be interchangeable

- ❏ Available from the same pool → free user choice

- ❏ Logged-in session terminates with an alert

- ❏ New credentials must be set such that old one is obsolete

- ❏ If “skip password” is inevitable, alert the security risks

45

## Slide 46

#### ~~For Recovery Processing (2)~~

###### **Parallel recovery flows make it hard to assess the benign intent**

##### **Session Policy**

- ❏ Recovery triggering should not terminate any ongoing sessions

- ❏ Successful recovery should terminate all types of parallel sessions

Sessions and tokens **Token Policy** should be bound ❏ Recovery token validity should be short and not to be extended ❏ Communicate the validity Service providers and to the users and nudge to users should be able to complete in time review and revoke individually

46

## Slide 47

#### ~~For Alert Notifications~~

**Notifying at the right moment with the right content can save account takeover and remediation**

##### **Venues**

##### **Occasions**

##### **Contents**

- ❏ Website or app UI

- ❏ Push notifications

   - Browser notifications

- ❏

- ❏ Pop-ups and alert ribbons

- ❏ Via authentication methods

- ❏ Account state changes

   - ❏ Alterations to authentication methods

   - ❏ Verification of unverified methods

- ❏ During recovery

   - ❏ _Trigger_ → recovery method + active session

   - ❏ _Successful recovery_ → all channels

   - ❏ Incident details

      - ❏ Incident type ❏ Metadata

   - ❏ Next steps

      - ❏ Contents of the alert

      - ❏ Additional info needed

   - ❏ Security concerns ❏ Anomalies

      - ❏ Associated risks

      - ❏ Reporting

- ❏ During suspicious activities

47

## Slide 48

#### ~~For Reviewing Recovery Events~~

**Reviews should help users analyze, revoke and report suspicious activities that the service provider alone cannot verify**

Account Settings
Security and
Privacy

Activity log

**Activity log properties**

- ❏ Tamper-proof

- ❏ Detailed

- ❏ Highlights anomalies

- ❏ Mention security risks

- ❏ Option to report

- **User nudging**

- ❏ What?

   - ❏ To remove or update obsolete methods

   - ❏ To Identify and report suspicious entries

- ❏ When?

   - ❏ After account creation

   - ❏ After recovery

   - ❏ After remediation ❏ Upon reporting suspicious activities

48

## Slide 49

#### ~~Ideal recovery flow~~

Nudge users to
review security
Two-factor verification
settings
Bind recovery
sessions and tokens
1 2 3 4 5 6 7
Terminate
Trigger   Verification MFA Password  existing  Security  Account
recovery (1st factor) (2nd factor) change sessions  Review Usage
and forget
trusted
Make recovery  devices
hard to miss!
Use auth methods
interchangeably
49

## Slide 50

## Closing Remarks

50

## Slide 51

#### ~~Recap~~

3 8 15
Adversaries Attacks Weaknesses

- Tested **22** most popular websites

   - all of them had **at least 1 security issue**

- **There could be more vulnerable websites and more security issues!!** ■ Contribute and use our auditing framework – <u>ARTHA</u>

51

## Slide 52

#### ~~Attacks Summary~~

|**Adversary**|**Potential Attacks**|**Description**|
|---|---|---|
|**Eve**|Skip password persistence|Exploits the“skip password” optionandno MFA in the recovery
lifecycleto gain stealth access|
|_Controls_: recovery method
|Password reuse persistence|Exploits thepassword reuse during recoveryandno MFA needed
on trusted deviceto gain stealth access|
|_Goal_: persistent access|Parallel session attack|Exploitsactive parallel sessions not terminating upon successful
recoveryto gain stealth access|
|**Mll**|Arms race attack|Exploitsno MFA in the recovery lifecycleto take part in an arms
race and potential win to lockout the victim|
|**aory**
_Controls_: recovery method
|Temporary lockout|ExploitsMFA needed only for login after recoveryto lockout
temporarily until victim can do recovery + login|
|_Goal_: account takeover|Permanent lockout|Exploitsno MFA needed on trusted deviceto permanently
lockout the victim|
|**Chad**|Recovery spam|Exploitslack of anti-spamming and control on recovery
triggeringto spam the victim|
|_Knows_: recovery method
_Goal_: spam or lockout|Recovery lockout|Exploitslack of anti-spamming and control on recovery
triggering to activate automatic lockout feature|

~~5~~ 2

## Slide 53

#### ~~Key Takeaways~~

- **Security vs usability trade-offs could lead to risky gaps**

   - Ease of account recovery over security

      - Low-friction but high-risk recovery mechanism

   - When OoB channels are not under control or cannot be monitored

      - Make no trust assumption

      - Utilize every heuristics and channels available

      - Prioritize security over usability

- **Non-typical security weaknesses could be harmful**

   - Equally harmful as any traditional software or hardware vulnerabilities

   - Low-tech adversaries can exploit

      - No scripting, coding

      - No tools required

      - No sophisticated bugs

      - No internal access or knowledge

- **Bridge the research-practice gaps**

   - Security audits and certification focuses on **internal evaluation** of policies and processes ■ However, the weaknesses discussed in this work mostly are out of scope of conventional vulnerability scanning or pen testing

   - Security research focuses on **external validation** of overlooked or missing best practices

   - ○ Our work bridges this gap as an auditing carried out by an adversary outside of the system, effectively performing **_Attack surface mapping of account recovery_**

53

## Slide 54

#### ~~Points to Remember Moving Forward~~

- **Users are NOT the weakest link in authentication, but account recovery is!**

   - Security weaknesses are not stemmed from user actions or knowledge, but mostly due to the oversight of service providers where users do not have a say

- **Weaknesses in account recovery goes beyond security and hacking**

   - Exploitable in cases of intimate partner violence and stalking where recovery weaknesses become _tools of controls and power_ !

   - Real-world adversaries are mostly insiders who exploit the weaknesses to reset access, monitor every activity or lock out victims

- **Authentication will evolve, but account recovery may remain stagnant**

   - Insights and lessons from this work will stay relevant to future systems

   - Our work lays the foundation for standards, red team tooling, and compliance checks, influencing how to design, test, and monitor recovery processes

54

## Slide 55

# Thank You!

**<u>Contact</u>**

**Sid Rao Email:** <u>sid.rao@nokia-bell-labs.com</u> **Linkedin:** <u>https://www.linkedin.com/in/siddharthprao/</u> **Gabriela Sonkeri Email:** <u>gabriela.sonkeri@wolt.com</u> **Linkedin:** <u>https://www.linkedin.com/in/gabrielasonkeri</u>

55

## Companion resources

### `Sid Rao&Gabriela Sonkeri&Amel Bourdoucen&Janne Lindqvist_Lost & Found The Hidden Risks of Account Recovery in a Passwordless Future_TOOLS.txt`

```text
https://github.com/Nokia-Bell-Labs/Account-Recovery-Threat-Heuristic-Auditing-Framework
```
