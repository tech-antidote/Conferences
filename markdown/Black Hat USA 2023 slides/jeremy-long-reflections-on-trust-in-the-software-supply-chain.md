---
title: "Reflections on Trust in the Software Supply Chain"
speakers: ["Jeremy Long"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Jeremy Long_Reflections on Trust in the Software Supply Chain.pdf"
pages: 32
sha256: "d32069cd81e532b083ee45c7ed6a3bc63a39b6deee57045b456bd7519158bd1f"
text_chars: 8222
ocr_pages: 8
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:17:07Z"
---
# Reflections on Trust in the Software Supply Chain

**Speakers:** Jeremy Long  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Jeremy Long_Reflections on Trust in the Software Supply Chain.pdf` (32 pages)

## Slide 1

# Reflections on Trust in the Software Supply Chain

Speaker: Jeremy Long

#BHUSA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
USA @Oes
AUGUST 9-10, 2023
Reflections on Trust in the
Software Supply Chain
Speaker:
Jeremy Long
```

## Slide 2

Jeremy Long @ctxt/@ctxt.bsky.social 20+ years in security Founder of OWASP Dependency-Check Currently Principal Security Engineer @ ServiceNow

#BHUSA  @BlackHatEvents

## Slide 3

## The Software Supply Chain is Massive

- “It has been estimated that Free and Open Source Software (FOSS) constitutes 70-90% of any given piece of modern software solutions.”<sup>1</sup>

- **CI/CD Infrastructure and build management tools** are also modern software and are part of the supply chain

- **Third Party Services** used in the CI/CD are also modern software and are part of the supply chain

#BHUSA @BlackHatEvents

## Slide 4

## Targeting the Supply Chain

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2025
Targeting the Supply Chain
Trend No. 3: Digital supply chain risk
Gartner predicts that by 2025, 45% of organizations worldwide will have experienced attacks on
their software supply chains, a three-fold increase from 2021.
```

## Slide 5

## Reflections on Trusting Trust

Compiler Source

OS

Source

“The moral is obvious. You can't trust code that you did not totally create yourself.” -- Ken Thompson

#BHUSA @BlackHatEvents

## Slide 6

Executive Order on Improving the Nation's Cybersecurity: Section 4 Enhancing Software Supply Chain Security

- Provenance of software code and components

- Software Bill of Materials (SBOM)

- Software Composition Analysis (SCA)

#BHUSA @BlackHatEvents

## Slide 7

## What is a dependency?

#BHUSA @BlackHatEvents

## Slide 8

## Industry Frameworks

- Supply-chain Levels for Software Artifacts, or SLSA ("salsa")

- Software Component Verification Standard (SCVS)

#BHUSA @BlackHatEvents

## Slide 9

## Provenance

- SLSA Definition:

Attestation (metadata) describing how the outputs were produced, including identification of the platform and external parameters.

- SCVS Definition:

The chain of custody and origin of a software component. Provenance incorporates the point of origin through distribution as well as derivatives in the case of software that has been modified.

#BHUSA @BlackHatEvents

## Slide 10

## Provenance

#BHUSA @BlackHatEvents

## Slide 11

## SLSA v1.0 - Threats

##### **Use a compromised runtime dependency**

- **Threat** : The adversary injects malicious code into software required to run the artifact.

- **Mitigation** : N/A - This threat is out of scope of SLSA v1.0.

##### **Use a compromised build dependency**

- **Threat** : The adversary injects malicious code into software required to build the artifact.

- **Mitigation** : N/A - This threat is out of scope of SLSA v1.0, though the build provenance may list build dependencies on a best-effort basis for forensic analysis.

#BHUSA @BlackHatEvents

## Slide 12

## Software Composition Analysis (SCA)

- Analyze dependencies for known vulnerabilities

- Runtime dependencies are analyzed

- Build plugins and test dependencies?

- SCA tools that work at the repository level

- OWASP Dependency-Check

   - ü Maven Plugins

   - ü Gradle Plugins

#BHUSA @BlackHatEvents

## Slide 13

## Software Bill of Materials (SBOM)

- CycloneDX and SPDX

- Describes the runtime dependencies

- CycloneDX v1.5 introduced Manufacturing Bill Of Materials (MBOM)

#BHUSA @BlackHatEvents

## Slide 14

###### **Modern Supply Chain Attacks**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bien hat
USA 2&0e53
Modern Supply Chain Attacks
g Crash Override
@crashappsec
Worse than a bad logging library would be a backdoored
library in a popular ide that then backdoored everything
built with it. Vulnerable open source with a supply chain
attack vector. Now there is a nightmare.
3:12 PM - Dec 11, 2021
```

## Slide 15

#### Malicious Dependencies

<u>https://github.com/jeremylong/malicious-dependencies</u>

#BHUSA @BlackHatEvents

## Slide 16

## Demo Explanation

Spring
Demo
Build
Build
Application
Helper
Analyzer

#BHUSA @BlackHatEvents

## Slide 17

## Injecting Malicious Code @ Build Time

- Not limited to Java

- Build Plugins: Maven, Gradle, Poetry, etc.

- Testing Frameworks: JUnit, NUnit, Mocking Frameworks

- Gradle/Maven Wrapper

#BHUSA @BlackHatEvents

## Slide 18

## SLSA v1.0 - Threats

##### **Use a compromised runtime dependency**

- **Threat** : The adversary injects malicious code into software required to run the artifact.

- **Mitigation** : N/A - This threat is out of scope of SLSA v1.0. You may be able to mitigate this threat by pinning your build dependencies, preferably by digest rather than version number. Alternatively, you can apply SLSA recursively, but we have not yet standardized how to do so.

#BHUSA @BlackHatEvents

## Slide 19

## Apply SLSA Recursively

#BHUSA @BlackHatEvents

## Slide 20

## Reproducible Builds

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackha
USA 2025
Reproducible Builds
nd
$ shasum -a 256 build. jar
61fbe3f17c2638ed21da283b06 f1dec342355c1937 f@lbef8231aeb294f f8417
JAR
$ shasum -a 256 build. jar
61fbe3f17c2638ed21da283b06 f1dec342355c1937 f@lbef8231aeb294f f8417
```

## Slide 21

## Reproducibly Compromised Build

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pif hat
USA e2bes
Cc
$ shasum -a 256 build. jar
61fbe3f17c2638ed21da283b06 f1dec342355c1937 f@lbef8231aeb294f f8417
$ shasum -a 256 build. jar
61fbe3f17c2638ed21da283b06 f1dec342355c1937 f@lbef8231aeb294f f8417
```

## Slide 22

## Vulnerable vs Malicious

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Vulnerable vs Malicious
?php echo
Hello World!
> |e
SP
¥
```

## Slide 23

## binary-source validation

compile

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2025
binary-source validation
public class HtmlUtil { =)
public String bold(String c) { =¢
return String. format("<b>%s</b>", Cc);
```

## Slide 24

## binary-source validation: source model

- Class: HtmlUtil + Method: bold

- args: String

- constants: "<b>%s</b>”

- called:

- java.lang.String.format

#BHUSA @BlackHatEvents

## Slide 25

## Java Class Files

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2025
Java Class Files
® CAFEBABE @@@@0@37 @@17@A@@ @3@0@E@8 @O@F@7@@||.... 7
2@  1@@A@@11 00120700 13010006 3C696E69 743£0100 <init>
4@ @3282956 @1000443 6F6465@1 @@@F4C69 6E654E75 QV Code LineNu
6@ 6D626572 5461626C 65010004 626F6C64 01002628 | | mberTable bold &(
8@ 4C6A6176 612F6C61 6E672F53 7472696E 673B294C | | Ljava/Lang/String;)L
10@ 6A617661 2F6C616E 672F5374 72696E67 3B@1@0@0A | | java/Lang/String;
12@ 536F7572 63654669 6(C65@10@ @D48746D 6(557469 | | SourceFile HtmLUti
14@ | 6CZE6A61 76610C@@ @6000701 0093062 3E25733C||1.java <b>%s<
16@ 2F623E@1 @@1@6A61 76612F6C 616E672F 4F626A65 | | /b> java/lang/O0bje
18@ 6374070@ 140C@@15 001600100 @848746D 6(557469 | | ct HtmLUti
200 6C@10@1@ 6A617661 2F6C616E 672F5374 72696E67 | | 1 java/Lang/String
220 @100@666 6F726D61 74010039 284(C6A61 76612F6C format 9(Ljava/1
```

## Slide 26

## binary-source validation: class model

Class: HtmlUtil + Method: bold

- args: String

- constants: "<b>%s</b>”

- called:

- java.lang.String.format

#BHUSA @BlackHatEvents

## Slide 27

## binary-source validation: Comparison

- Class: HtmlUtil + Method: bold

- args: String

- constants: "<b>%s</b>”

- called:

- java.lang.String.format

- Class: HtmlUtil + Method: bold

- args: String

- constants: "<b>%s</b>”

- called:

- java.lang.String.format

#BHUSA @BlackHatEvents

## Slide 28

## binary-source validation: Comparison

- Class: HtmlUtil + Method: bold

- args: String

- constants: "<b>%s</b>”

- called:

- java.lang.String.format

Class: HtmlUtil + Method: bold - args: String

- constants: "<b>%s</b>", "echo 'Never gonna give you up'" - called:

- java.lang.String.format

- java.lang.Runtime.getRuntime()

- java.lang.Runtime.exec()

#BHUSA @BlackHatEvents

## Slide 29

## Binary Source Validation Challenges

- Compiler changes/optimization

- Code generators

- Model generation from a build artifact is technology specific • May limit the types of comparison that can be done

#BHUSA @BlackHatEvents

## Slide 30

## What can we do today?

- Reduce the number of dependencies

- Do not use code generators during the build

   - Generate code and check it into your source repo

   - Treat generated code as you do any other code

- Talk to your SAST and Supply Chain Vendors about build verification

#BHUSA @BlackHatEvents

## Slide 31

## Summary

- The trusting trust problem is real very real

- Any code running during the build can affect the build output - **reproducibly**

- Use OWASP Dependency-Check to scan plugins for maven and gradle builds

- Support open-source developers

#BHUSA @BlackHatEvents

## Slide 32

### Questions?

#BHUSA @BlackHatEvents
