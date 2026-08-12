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
text_chars: 7471
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.8
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:10:31Z"
---
# Reflections on Trust in the Software Supply Chain

**Speakers:** Jeremy Long  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Jeremy Long_Reflections on Trust in the Software Supply Chain.pdf` (32 pages)


## Slide 1

# Reflections on Trust in the Software Supply Chain

Speaker: Jeremy Long

#BHUSA  @BlackHatEvents

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


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 72/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackha
Reproducible Builds
$ shasum -a 256 build. jar
JAR
$ shasum -a 256 build. jar
```

## Slide 21

## Reproducibly Compromised Build

#BHUSA @BlackHatEvents

## Slide 22

## Vulnerable vs Malicious

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vulnerable vs Malicious
?php echo
Hello World!
```

## Slide 23

## binary-source validation

compile

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 72/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
GoCD

Create Configuration Repository

Configuration File Path: /go-working-dir/config/cruise-config.xml

Last modified: less than a minute ago by test                    SAVE   CANCEL

<?xml version="1.0" encoding="utf-8"?>
<cruise xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="cruise-config.xsd" schemaVersion="139">
  <server agentAutoRegisterKey="09cd2027-d420-4667-b96b-6b6c83134396" webhookSecret="55f9add4-5ead-40f2-b677-12b472ed6392" serverId="080ddfb2-f0b2-474b-9392-b29b8266d1f7" tokenGenerationKey="ae79cdde-2652-4bc0-b7f1-71f994175714">
    <security>
      <authConfigs>
        <authConfig id="auth" pluginId="cd.go.authentication.passwordfile">
          <property>
            <key>PasswordFilePath</key>
            <value>/godata/config/passwd.properties</value>
          </property>
        </authConfig>
      </authConfigs>
      <roles>
        <role name="simple-user">
          <users>
            <user>test</user>
          </users>
          <policy>
            <allow action="administer" type="environment">test*</allow>
            <allow action="administer" type="config_repo">test*</allow>
          </policy>
        </role>
      </roles>
      <admins>
        <user>user</user>
        <user>test</user>
      </admins>
    </security>
    <artifacts>
      <artifactsDir>artifacts</artifactsDir>
    </artifacts>
  </server>
  <config-repos>
    <config-repo id="test-xxe-repo" pluginId="gocd-xml">
      <git url="https://gitlab.com/demo621918/my-xml-repo" branch="main" />
    </config-repo>
  </config-repos>
  <pipelines group="defaultGroup">
    <authorization>
      <view>
        <user>user1</user>

GoCD stores server configuration in a xml file
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
