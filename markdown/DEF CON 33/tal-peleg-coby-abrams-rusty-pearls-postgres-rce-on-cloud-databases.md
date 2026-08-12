---
title: "Rusty pearls Postgres RCE on cloud databases"
speakers: ["Tal Peleg Coby Abrams"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Tal Peleg Coby Abrams - Rusty pearls Postgres RCE on cloud databases.pdf"
pages: 25
sha256: "0b5e01d575fe70a7a5d6e7ee2927cbc06f0e266ce070fef0e1972b4e1116fd6d"
text_chars: 5749
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:14:47Z"
---
# Rusty pearls Postgres RCE on cloud databases

**Speakers:** Tal Peleg Coby Abrams  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Tal Peleg Coby Abrams - Rusty pearls Postgres RCE on cloud databases.pdf` (25 pages)


## Slide 1

## Slide 2

#### **TAL PELEG**

#### **COBY ABRAMS**

- Cloud security research team lead at Varonis

   - Cloud security researcher at Varonis

- Full stack security hacker

   - Experience in various cybersecurity fields

- Currently specialize in IaaS research

   - Currently specialize in IaaS research

- Excited about breaking things and fixing them again, music, and astrophysics

- Passion for teaching cybersecurity

Tal Peleg + Coby Abrams

## Slide 3

## **What’s About to Happen**

1. We are going to talk about hacking PostgreSQL (CVE-2024-10979) and a cloud hosted PostgreSQL!

2. How we went about the research and why it is interesting

3. Hacking Takeaways for the cybersecurity community

Tal Peleg + Coby Abrams

## Slide 4

## **Background**

**PostgreSQL**

A popular robust and opensource relational database used in a variety of applications including cloud environments.

Tal Peleg + Coby Abrams

## Slide 5

Step 1
THE INITIAL PRIMITIVE USING PERL

## Slide 6

## **Postgres Language Extensions**

Postgres allows writing functions in various languages

- •

- C (built-in) Python

- Perl (built in) • Rust

Can be used in two modes

- Trusted

- Untrusted

Tal Peleg + Coby Abrams

## Slide 7

## **Trusted vs. Untrusted Functions**

Trusted Language Function Untrusted Language Function
Access System Access Open Create
Environment Files Socket Process

Tal Peleg + Coby Abrams

## Slide 8

## **Trusted vs. Untrusted Functions**

Trusted                         plperl Untrusted                      plperlu
Access System Access Open Create
Environment Files Socket Process

Tal Peleg + Coby Abrams

## Slide 9

## **PL/Perl Primitive**

- Perl implements “magic” variables tied to special functionality

- %ENV – used to access and set environment variables

   - _$ENV{PATH} = ‘/bin’;_

- The implementation for these is deep within the Perl language

- PL/Perl did not override this behavior in trusted mode

Tal Peleg + Coby Abrams

## Slide 10

## **Modifying Environment Variables in PL/Perl**

Tal Peleg + Coby Abrams


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Modifying Environment Variables in PL/Perl
postgres=# CREATE FUNCTION set_env(text, text)
RETURNS void AS
$tag$
SENV{$_[O]} = $_[1];
$tag$ language plperl;
CREATE FUNCTION
ljpostgres=# select set_env('PATH', '/tmp/mypath');
set_env
Tal Peleg + Coby Abrams aah” Ni varonis
```

## Slide 11

**Step 2**

**HOW WE LEVERAGE THIS INTO CODE EXECUTION**

## Slide 12

### **Another Language Extension: PL/Rust**

- Now we need something to read our edited environment variables and execute them

- PL/Rust, a compiled language, and also a trusted language, gave us an answer

Tal Peleg + Coby Abrams

## Slide 13

- RUSTC_WRAPPER is removed before invocation

- CARGO_BUILD_RUSTC_WRAPPER, however, is not removed

- rust_gdb script executes the RUST_GDB parameter

Tal Peleg + Coby Abrams

## Slide 14

## **Flow**

**Cargo runs rustc or CARGO_BUILD_RUSTC_WRAPPER** Cannot change parameters passed

**rust_gdb script executes RUST_GDB contents** Can change parameters passed

Tal Peleg + Coby Abrams

## Slide 15

Demo
LET’S SEE THIS IN ACTION!

## Slide 16

## **So What’s Going On?**

- We know you probably have some questions…

- How did we find this vulnerability?

- Why did we choose to exploit PL/Perl and PL/Rust?

- You promised us a cloud RCE!

Tal Peleg + Coby Abrams

## Slide 17

## **Choosing the Objective**

- AWS RDS came up during a different research project

- I was looking for a PE

- What better PE than… RCE?

- And so, the end-goal was set – RCE on an RDS instance

Tal Peleg + Coby Abrams

## Slide 18

## **Acquiring a Target**

- PL/Perl is in the official Postgres repo and is enabled on RDS

- • Perl is from the 80’s

- Perl is a little weird (no offence, we like weird, weird is good)

- • Perl and PL/Perl are opensource

Tal Peleg + Coby Abrams

## Slide 19

## **Getting It Over the Line**

- Postgres provides some challenges – Background Workers

- After finding the primitive, we looked at opensource extensions, specifically those allowed in AWS RDS

- GitHub’s search/Copilot to the rescue

   - _Getenv_

   - _System_

   - _Execv_

- _And in rust, Command_

Tal Peleg + Coby Abrams

## Slide 20

## **Yes, We Briefly Ran Code On RDS**

- Why attack our own cloud database?

- What did we find?

   - _A very limited environment_

   - _The effectiveness of AWS incident response_

- Bug disclosed to PostgreSQL and AWS on October 10<sup>th</sup> 2024 and was patched November 11<sup>th</sup> 2024

Tal Peleg + Coby Abrams

## Slide 21

## **End Users**

- Update your databases

- Least privileges

- Limit extensions

Tal Peleg + Coby Abrams


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
End Users
Don’t make me
tap the sign.
e Update your databases
° Least privileges
° Limit extensions
Incorrect control of environment variables in PostgreSQL PL/Per! allows an unprivileged
database user to change sensitive process environment variables (e.g. PATH). That often suffices
to enable arbitrary code execution, even if the attacker lacks a database server operating system |
user. Versions before PostgreSQL 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21 are affected.
The PostgreSQL project thanks Coby Abrams for reporting this problem.
9Q
Tal Peleg + Coby Abrams ei Nvvaronis
```

## Slide 22

## **Cloud Providers**

- Managed database backends are prone to these vulnerabilities

   - _The Speckle Umbrella story - Imre Rad_

   - _Azure Cosmos for postgres_

- Responsible community research

   - _Container escapes_

   - _Credentials_

   - _Network_

   - _Cross-account_

Tal Peleg + Coby Abrams

## Slide 23

## **Researchers**

- Environment variables are fun

- Prepare before running sensitive payloads

- Deny lists are usually a (good?) bad sign

- Looking for obscure built-in features generally pays off

- Set your goals before researching!

Tal Peleg + Coby Abrams

## Slide 24

# **TL;DR**

- We found a cool RCE on Postgres that works in the cloud

- Look for vulnerabilities everywhere, not only workloads

- • Don’t exploit on a major cloud service just before the weekend

## Slide 25

Thank You!

**Scan to visit the Varonis Threat Labs blog**
