---
title: "Anomaly Detection Betrayed Us, so We Gave It a New Job Enhancing Command Line Classification with Benign Anomalous Data"
speakers: ["Ben Gelman", "Sean Bergeron"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Ben Gelman&Sean Bergeron_Anomaly Detection Betrayed Us, so We Gave It a New Job Enhancing Command Line Classification with Benign Anomalous Data.pdf"
pages: 51
sha256: "552374f6d6dc39f7e466ab342913dcdb779e1f01bb93f27fedda46349fd1d190"
text_chars: 11375
ocr_pages: 15
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:51:16Z"
---
# Anomaly Detection Betrayed Us, so We Gave It a New Job Enhancing Command Line Classification with Benign Anomalous Data

**Speakers:** Ben Gelman, Sean Bergeron  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Ben Gelman&Sean Bergeron_Anomaly Detection Betrayed Us, so We Gave It a New Job Enhancing Command Line Classification with Benign Anomalous Data.pdf` (51 pages)

## Slide 1

###### Anomaly Detection Betrayed Us, so We Gave It a New Job: Enhancing Command Line Classification with Benign Anomalous Data

Ben Gelman, Sean Bergeron

#BHUSA @BlackHatEvent s

## Slide 2

## **Introduction**

2

## Slide 3

##### **About Me - Ben**

Data Scientist at Sophos for 4 years

- 5 years in government-funded R&D

- 2 years of post-grad research at academic institutions

3

## Slide 4

###### **About Me - Sean**

- Data Scientist at Sophos for 3 years

- Mechanical engineer

- Deep personality estimation post-grad research

4

## Slide 5

###### **What Are We Talking About?**

5

## Slide 6

###### **How did this happen?**

Command lines

6

## Slide 7

###### **Unsustainable Manual Effort**

7

## Slide 8

**The Perfect, Fully-Automated, Self-Updating System for Command Line Prediction, Featuring LLMs**

8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Perfect, Fully-Automated, Self-Updating System for Command
Line Prediction, Featuring LLMs™
LLM
LARGE LANGUAGE
```

## Slide 9

###### **Not Really: Anomaly Detection Betrayed Us**

# 36% 100%

Malicious Precision

#### Benign Precision

9

## Slide 10

## **Motivation**

10

## Slide 11

#### **Unsupervised: The State of Anomaly Detection Pros Cons**

▪ No labels required

- High false positive rates – extreme alert fatigue

▪ High scalability

▪ Low Cost

▪ Reliance on human expertise

11

## Slide 12

**The State of Anomaly Detection** FPR <2, <2, <3% [1, 2, 3] Feasible?

12

## Slide 13

###### **The State of Anomaly Detection**

13

## Slide 14

###### **The State of Labeled Data: Malicious Data**

Sandbox

VirusTotal

Customer Case Investigations

Expert labeling

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
14
The State of Labeled Data: Mialicious Data
=» Sandbox
= VirusTotal
= Customer Case Investigations
= Expert labeling
: a
CYBERSECURITY i
1
6
0
LABEL
```

## Slide 15

###### **The State of Labeled Data: Benign Data [4, 5]**

15

## Slide 16

###### **The Longtail**

16

## Slide 17

###### **Are We Stuck?**

###### **<u>Anomaly Detection</u>**

###### High FP Rates Scalable

###### **<u>Supervised Learning</u>**

Scalability Issues Low FP Rates

17

## Slide 18

###### **Are We Stuck?**

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
18
Are We Stuck?
Always Has Been
```

## Slide 19

## **Redefining The Role of Anomaly Detection**

19

## Slide 20

###### **The Whole System**

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Whole System
Command Daily Expert
Line Command Features
Database Lines
Subsample
Embedding Model
20
Isolation Forest
Isolation Forest
Q
LLM &
LARGE LANGUAGE
MODEL
Training
Data
Prediction Models
```

## Slide 21

21

## Slide 22

###### **Command Line Datasets**

1.) Regex-based dataset

2.) Aggregated dataset

`o` Regex

`o` Sandbox

`o` Case Investigations `o` Customer telemetry

22

## Slide 23

###### **Expert Features**

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expert Features
= -) p@ilogp(a
| nOWERSHELLe! exE
(BROIL Core eee
```

## Slide 24

###### **Embeddings Model**

24

## Slide 25

###### **Isolation Forest**

1 2 3 4

25

## Slide 26

###### **K-means Anomaly**

26

## Slide 27

###### **Principal Components Analysis (PCA) Anomaly**

27

## Slide 28

###### **Deduplication**

Two nearly duplicate command lines: ls **_-l_** /home/user ls **_-la_** /home/user

**Exact Deduplication**

###### **Near Deduplication**

Command 1 Command 2 Dedupe? Command 1 Command 2 Dedupe? ls -l /home/user ls -l /home/user ls -l /home/user ls -l /home/user ls -l /home/user ls -la /home/user ls -l /home/user ls -la /home/user

28

## Slide 29

###### **LLM Labeling**

29

## Slide 30

###### **LLM Labeling + Demo**

"E:\Applications\AODB\Java\jdk1.8.0_412\bin\aodb-java" -Dprogram.name=standalone.bat -server - XX:MaxMetaspaceSize=1024M -XX:MetaspaceSize=1024M -XX:+UseParallelGC -XX:+UseParallelOldGC - Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000 - Djboss.modules.system.pkgs=org.jboss.byteman -Djava.net.preferIPv4Stack=true - Dorg.tanukisoftware.wrapper.WrapperManager.mbean=false -Djboss.server.default.config=standalone.xml - Dlogging.configuration=file:E:\Applications\AODB\wildfly-26.1.6.Final/standalone/configuration/logging.properties - Dorg.jboss.boot.log.file=E:\Applications\AODB\wildfly-26.1.6.Final/standalone/log/boot.log - Djava.util.logging.manager=org.jboss.logmanager.LogManager -

Dorg.jboss.logging.Logger.pluginClass=org.jboss.logging.logmanager.LoggerPluginImpl -Djboss.remoting.pooledbuffers=false -Dfile.encoding=Cp1252 -Duser.language=en -Xms2048m -Xmx16384m -

Djava.library.path="E:\Applications\AODB\wildfly-26.1.6.Final\lib" -classpath "E:\Applications\AODB\wildfly26.1.6.Final\lib\wrapper.jar;E:\Applications\AODB\wildfly-26.1.6.Final\jboss-modules.jar" - Dwrapper.key="v19OywX5EMaygmtSZdG9t35Naj6wvoH9" -Dwrapper.port=32000 -Dwrapper.jvm.port.min=31000 - Dwrapper.jvm.port.max=31999 -Dwrapper.debug="TRUE" -Dwrapper.pid=2008 -Dwrapper.version="3.5.25-pro" - Dwrapper.native_library="wrapper" -Dwrapper.arch="x86" -Dwrapper.service="TRUE" -Dwrapper.cpu.timeout="10" - Dwrapper.jvmid=2 -Dwrapper.lang.domain=wrapper -Dwrapper.lang.folder=../lang

org.tanukisoftware.wrapper.WrapperJarApp jboss-modules.jar -mp E:\Applications\AODB\wildfly-26.1.6.Final/modules org.jboss.as.standalone -Djboss.home.dir=E:\Applications\AODB\wildfly-26.1.6.Final --server-config=standalone-fullsqlsrv.xml -P=E:\Applications\AODB\wildfly-26.1.6.Final/standalone/configuration/aodb-sqlsrv.properties -b 192.168.7.61

30

## Slide 31

31

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
31
ZG
User
We need to determine whether a command line is benign or malicious.
We have to be very confident in our answer, so let's think about this deeply.
Let's start by explaining what the command line does.
Then explain how, if possible, the command could be used in a benign way.
Then explain how, if possible, the command line could be used maliciously.
Finally, make a verdict on whether the command line is benign or malicious.
Output your response as either VERDICT_BENIGN or VERDICT_MALICIOUS.
Once again, only convict a command as malicious if it is very likely.
Use the term VERDICT_BENIGN or VERDICT_MALICIOUS only ONCE in your
response.
Command line: "E:\Applications\AODB\Java\jdk1.8.0_412\bin\aodb-java" -
Dprogram.name=standalone.bat -server -
XX:MaxMetaspaceSize=1024M -XX:MetaspaceSize=1024M -XX:+UseParallelGC -
XX:+UseParallelOldGC -
Dsun.rmi.dac.client.acInterval-3600000
Collapse ~
oO & Auto-clear +)
>
```

## Slide 32

## **Results**

32

## Slide 33

###### **Evaluation**

**<u>Timesplit</u>** Easier

### **<u>Manual Labels</u>**

Harder

33

## Slide 34

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Training Set
Manual Label AUC
Timesplit Test AUC
Aggregated Baseline (AB)
AB + Full-Scale
AB + Reduced-Scale Combined
AB + Reduced-Scale IF
AB + Reduced-Scale KMeans
AB + Reduced-Scale PCA
0.6138
0.8935
0.8063
0.8028
0.7852
0.7650
0.9979
0.9990
0.9988
0.9985
0.9988
0.9989
Regex-based Baseline (RB)
RB + Full-Scale
RB + Reduced-Scale Combined
RB + Reduced-Scale IF
RB + Reduced-Scale KMeans
RB + Reduced-Scale PCA
0.7072
0.7689
0.7077
0.7337
0.7182
0.7174
0.9988
0.9990
0.9995
0.9998
0.9994
0.9996
```

## Slide 35

35

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Aggregated Baseline Dataset: Binary Classifier Evaluated on Manual Labels Test Set
— FSIF
0.90
RS Combined
RS IF
RS KMeans
RS PCA
Baseline
7)
°
Q
va]
U
2
zx
```

## Slide 36

36

## Slide 37

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Regex-based Baseline Dataset: Binary Classifier Evaluated on Manual Labels Test Set
— FSIF
RS Combined
RS IF
RS KMeans
RS PCA
Baseline
7)
°
Q
va]
U
2
zx
```

## Slide 38

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Regex-based Baseline Dataset: Binary Classifier Evaluated on Timesplit Test Set
— FSIF
RS Combined
RS IF
- RS KMeans
RS PCA
--- Baseline
7)
°
Q
va]
U
2
zx
```

## Slide 39

## **Conclusion**

39

## Slide 40

**Do You Qualify for Benign Anomaly Detection** Big data? New data coming in? Cybersecurity machine learning model?

40

## Slide 41

###### **Do You Qualify for Benign Anomaly Detection**

41

## Slide 42

###### **Monday Morning**

Pick a cybersecurity model that needs updating Dig up some recent data Run isolation forest

Send anomalies to a small reasoning LLM (Confirm benign labels) Retrain target model

42

## Slide 43

###### **Black Hat Sound Bytes**

Anomaly detection excels at locating benign data in the long tail Modern LLMs have enabled automated pipelines for benign data labeling that were not possible before

Training set augmentation with benign anomalies is a generalizable method for improving cybersecurity models

43

## Slide 44

## **Appendix**

44

## Slide 45

###### **Expert Features**

- Character length

- Proportion of operators:

   - `{'%', '*', '^', '`', '/', '+', '-', '=', '>'}`

- Proportion of upper-case characters

- Proportion of lower-case characters

- ASCII per-character counts

- Shannon entropy

45

## Slide 46

###### **Expert Features cont.**

- Count of `"echo"` markers

- Count of `"replace"` markers

- Count of `"#"` markers

- Count of markers:

```
o{" -e ", " -ec ", " -enc ", " -encodedcommand ", "frombase64string("}
```

- Count of markers:

```
o{"^", '""', "set", "&&", "&&for", "for %", ";;"}
```

- Count of markers:

```
o{"http", "www.", ".com", "html", "tcp", "udp"}
```

- Count of markers:

`o {"lsass", "samsrv", "hklm\\sam", "winlogon", "netlogon", "kerberos.dll", "dump", ".bin", "ntds"}` • Test for deliberate encoding and encryption

- Check for multiple valid file paths

- Check for remote executable

- Check for exactly one hostname and local file path

46

## Slide 47

###### **Spark ML Features**

- Normalized tokens

   - WordPunct tokenize: `"\\w+|[^\\w\\s]+"`

   - Replace numeric digits with *

- Normalized tokens -> TF-IDF

- Normalized tokens -> Compute most common 1024 tokens in vocab -> One-hot encoding

47

## Slide 48

###### **LLM Labeler Prompt**

We need to determine whether a command line is benign or malicious. We have to be very confident in our answer, so let's think about this deeply. Let's start by explaining what the command line does. Then explain how, if possible, the command could be used in a benign way. Then explain how, if possible, the command line could be used maliciously. Finally, make a verdict on whether the command line is benign or malicious. Output your response as either VERDICT_BENIGN or VERDICT_MALICIOUS. Once again, only convict a command as malicious if it is very likely. Use the term VERDICT_BENIGN or VERDICT_MALICIOUS only ONCE in your response. Command line:

48

## Slide 49

###### **Full-scale Command-line Distribution**

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
49
Full-scale Command-line Distribution
Full Scale: Unique & Near-Duplicate Command Lines
Cumulative Total Commands
Cumulative Unique Deduped
Cumulative Near-Duplicate (>0.8)
Cumulative Count
```

## Slide 50

###### **Reduced-scale Command-line Distribution**

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reduced-scale Command-line Distribution
Reduced Scale: Unique & Near-Duplicate Command Lines
Cumulative Total Commands
Cumulative Unique Deduped
Cumulative Near-Duplicate (>0.8)
ay
<
Ss
fo
s)
ov
>
5S
s&s
Ss
fa
s
o)
```

## Slide 51

###### **References**

[1] Vinay, V., & Mangal, A. (2024). SCADE: Scalable Command-line Anomaly Detection Engine. _arXiv preprint arXiv:2412.04259_ .

- [2] Nisslmueller, U. (2022). _LOLBin detection through unsupervised learning: An approach based on explicit featurization of the command line and parent-child relationships_ (Master's thesis, University of Twente).

- [3] Filar, B., & French, D. (2020). Problemchild: Discovering anomalous patterns based on parent-child process relationships. _arXiv preprint arXiv:2008.04676_ .

- [4] Hendler, D., Kels, S., & Rubin, A. (2020, October). Amsi-based detection of malicious powershell code using contextual embeddings. In _Proceedings of the 15th ACM Asia Conference on Computer and Communications Security_ (pp. 679-693).

- [5] Hendler, D., Kels, S., & Rubin, A. (2018, May). Detecting malicious powershell commands using deep neural networks. In _Proceedings of the 2018 on Asia conference on computer and communications security_ (pp. 187-197).

51
