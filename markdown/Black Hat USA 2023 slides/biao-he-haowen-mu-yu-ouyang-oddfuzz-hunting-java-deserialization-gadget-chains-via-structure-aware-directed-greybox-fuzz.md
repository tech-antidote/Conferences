---
title: "ODDFuzz Hunting Java Deserialization Gadget Chains via Structure-Aware Directed Greybox Fuzzing"
speakers: ["Biao He", "Haowen Mu", "Yu Ouyang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Biao He & Haowen Mu & Yu Ouyang_ODDFuzz Hunting Java Deserialization Gadget Chains via Structure-Aware Directed Greybox Fuzzing.pdf"
pages: 50
sha256: "9032ca5fa4f8a2aa2841ac915f191f891369b7a2c4755e6565f8369309dacdbc"
text_chars: 21349
ocr_pages: 12
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:13:58Z"
---
# ODDFuzz Hunting Java Deserialization Gadget Chains via Structure-Aware Directed Greybox Fuzzing

**Speakers:** Biao He, Haowen Mu, Yu Ouyang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Biao He & Haowen Mu & Yu Ouyang_ODDFuzz Hunting Java Deserialization Gadget Chains via Structure-Aware Directed Greybox Fuzzing.pdf` (50 pages)


## Slide 1

ODDFuzz: Hunting Java Deserialization Gadget Chains via Structure-Aware Directed Greybox Fuzzing

Speakers: Biao He, Haowen Mu

Contributors: Sicong Cao, Xiaobing Sun, Yu Ouyang, Chao Zhang, Xiaoxue Wu, Ting Su, Lili Bo, Bin Li, Chuanlei Ma, Jiajia Li, Tao Wei

**EAST CHINA NORMAL UNIVERSITY** #BHUSA @BlackHatEvents

## Slide 2

## **About Speakers**

### Biao He

- Security researcher @ Ant Security FG Lab

- Black Hat Europe 2022 Speaker

- @codeplutos

### Haowen Mu

- Founder @ Cyberutopian

- CTF player at Nu1L Team

- @meizjm3i

## Slide 3

## **Agenda**

- Introduction

- Previous work & Remaining challenges

- ODDFuzz: A novel approach to hunting gadget chains

- Evaluation

- Conclusion & Takeaways

## Slide 4

## **Java Deserialization**

Database
Serialization Deserialization
• Communication
• Caching
File • Deep Copy
Stream  Stream  • Cross JVM
Object Object
of Bytes of Bytes
Synchronization
Memory • Persistence

4

## Slide 5

## **Java Deserialization Vulnerability**

## Magic methods will be executed automatically when deserialization

- readObject

- • readResolve

-

- ……

5

## Slide 6

## **Java Deserialization Gadget Chain**

Exploit

A call chain starts with a magic method ( _source method_ ) and ends with a securitysensitive method ( _sink method_ )

6

## Slide 7

## **Why gadget chains are so significant**

### For defenders

### For attackers

- Deserialization is unavoidable

   - Make Java deserialization vulnerability exploitable

- Blacklist

- Bypass blacklist

7

## Slide 8

## **Agenda**

- Introduction

- Previous work & Remaining challenges

- ODDFuzz: A novel approach to hunting gadget chains

- Evaluation

- Conclusion & Takeaways

## Slide 9

## **Existing Solutions** **_Gadget Inspector [BlackHat 2018]_**

Classes Source
Methods Gad g et Gad g et
1 4
Dataflows Gad g et Gad g et
Applicatio Static  Method  2 3
Calls
n Analysis Sink
Meta data Call Graph
E Suffer precision issues
Gad g et Gad g et
Gadget Chain  Source Sink
E Hard to confirm 1 3
1: Gad g et
Gadget Chain  Source Sink
4
2:

1I. Haken, “Automated discovery of deserialization gadget chains,” BlackHat USA, 2018.

9

## Slide 10

## **Existing Solutions** **_SerHybrid [ASE 2020]_**

E Difficult to satisfy
certain hard
constraints
Applicatio Points-to  Fuzzing
n Analysis
Heap Graph
E Heavy-weight

2S. Rasheed and J. Dietrich, “A hybrid analysis to detect java serialization vulnerabilities,” IEEE/ACM International Conference on Software Engineering, 2020.

10

## Slide 11

## **Existing Solutions** **_CodeQL_**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Existing Solutions
CodeQL
Analysis overview
The database schema is (source) language specific, as
|
are queries and libraries. | Query
|
I
l
I
Multi-language code bases are analyzed one Compilation
|
|
|
|
language at a time. _Compled ier
\ Me
N
| \f
!| Code | Query
!| base Evaluation
I
```

## Slide 12

## **Remaining Challenges**

1. Runtime polymorphism and other dynamic language features make it difficult to make trade-offs between precision and recall.

2. Java deserialization gadget chains can be quite long, which causes huge computation space and amplifies the inaccuracy.

3. Existing tools are unable to validate candidate gadget chains, which require manual inspection and are time-consuming and error-prone.

12

## Slide 13

## **Agenda**

- Introduction

- Previous work & Remaining challenges

- ODDFuzz: A novel approach to hunting gadget chains

- Evaluation

- Conclusion & Takeaways

## Slide 14

## **Our approach: ODDFUZZ**

### **_Lightweight Taint_ Analysis and** **_Directed_ Greybox Fuzzing**

E Lightweight static analysis

E Directed Greybox Fuzzing

14

## Slide 15

## **Lightweight static analysis**

### Class A

**Controlling Data Types => Controlling Code!**

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
Class A
public void readObject(ObjectInputStream ois) {
/ public class ValueComparator implements Comparator{
//get comparator
verride
this.comparator = (Comparator) ois. readObjectO; public int compare(Value v1, Value v2) {
Comparator comparator = threadLocal. get ( return vi.getValue() - v2.getValue();
if (comparator == null) { }
comparator = this.comparator; 3
}
//read values
valuel1 = ois.readObject();
value2 = ois. readObject(); r public class InvokeComparator implements Comparator {
//compare an ordered arraylist String methodName; ne
if (comparator }comparetvatuel, value2) > 0) { String className; EXP?
orderedList.add(value1) ;
orderedList.add(value2) ; @0verride
} else { , public int compare(Object 01, Object o2) {
orderedList.add(value2); Method method = Class. forName(className)
orderedList.add(value1) ; -getMethod (methodName) ;
} . method. setAccessible(true) ;
} Controlling Data Types return (int) method. invoke(01,02);
=> Controlling Code! }
```

## Slide 16

## **Lightweight static analysis**

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
public void readObject(ObjectInputStream ois) {
//get comparator
this.comparator = (Comparator) ois.readObject(); New xX = new T()
Comparator comparator = threadLocal.get();
if (comparator == null) { .
comparator = this.comparator; Assign xX = y
+
//read values
valuel = ois. readObject(); Store X.f = y
value2 = ois.readObject();
//compare and add to ordered arraylist _
if (comparator.compare(valuel, value2) > @) { Load y ~ x. F
orderedList.add(value1);
orderedList.add(value2) ; Call r= xX. k(a, )
} else {
orderedList.add(value2) ;
orderedList.add(valuel);
16
```

## Slide 17

## **Lightweight static analysis**

**SPAG (Simplified Pointer Assignment Graph) + Worklist algorithm** 17

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
public void readObject(ObjectInputStream ois) {
//get comparator
this.comparator = (Comparator) ois.readObject(); New xX = new T()
Comparator comparator = threadLocal.get();
if (comparator == null) { .
comparator = this.comparator; Assign xX = y
}
//read values
valuel = ois. readObject(); Store X. f = y
value2 = ois.readObject();
//compare and add to ordered arraylist -
if (comparator.compare(valuel, value2) > @) { Load y x.f
orderedList.add(value1);
orderedList.add(value2) ; Call r= x.k(a, )
} else {
orderedList.add(value2) ;
orderedList.add(value1) ; SPAG (Simplified Pointer
; y Assignment Graph) + Worklist
algorithm
```

## Slide 18

## **Lightweight static analysis**

**Construct SPAG (Simplified Pointer Assignment Graph)**

18

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
/ New xX = new T()) y
Assign X= y alloct
Store X.f = y
Load = xX.f
~ ” a, X x.f
Call r = x.k(a, ...)
Construct SPAG (Simplified
Pointer Assignment Graph)
```

## Slide 19

## **Lightweight static analysis**

Fig. 1: SPAG

**Construct SPAG (Simplified Pointer Assignment Graph)**

19

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
public void readObject(ObjectInputStream ois) { .
VIER COMTBTAtaN this.comparator
this.comparator = (Comparator) ois.readObject();
Comparator comparator = threadLocal.get();
if (comparator == null) {
comparator = this.comparator;
}
//read values
valuel = ois.readObject();
value2 = ois.readObject();
//compare and add to ordered arraylist
if (comparator.compare(value1, value2) > 0) { comparator
orderedList.add(value1);
orderedList.add(value2) ; Fig. 1: SPAG
} else {
orderedList.add(value2) ;
orderedList.add(valuel);
} Construct SPAG (Simplified
} Pointer Assignment Graph)
```

## Slide 20

## **Lightweight static analysis**

Worklist algorithm

20

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
alloct
/ New xX = new T())
Assign xX =y
Store X.f = y
Load = x.f
XS y,
Call r = x.k(a, ...)
Worklist algorithm
20
```

## Slide 21

## **Lightweight static analysis**

- Static Call X.k(a, …)

- • Special Call x.<init>(a, …) / super.k(a, …) **Worklist algorithm**

- • Virtual Call x.k(a, …)

21

## Slide 22

## **Lightweight static analysis**

### Call statement

   - Ø Construct call graph on-the-fly

   - Ø Perform Class Hierarchy Analysis (CHA) on the call statement _only_ when the receive object is tainted

   - Ø Prior knowledge

      - Native method

      - • Specific method (readObject)

- Static Call X.k(a, …)

- • Special Call x.<init>(a, …) / super.k(a, …)

- • Virtual Call x.k(a, …)

22

## Slide 23

## **Lightweight static analysis**

- r

- • Static Call X.k(a, …)

- • Special Call x.<init>(a, …) / super.k(a, …) **Worklist algorithm**

- • Virtual Call x.k(a, …)

23

## Slide 24

## **Lightweight static analysis**

**SPAG (Simplified Pointer Assignment Graph) + Worklist algorithm** 24

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
public void readObject(ObjectInputStream ois) { .
VIER COMTBTAtaN this.comparator
this.comparator =((Comparator) ois.readObject(); |
Comparator comparator = threadLocal.get();
if (comparator == null) {
comparator = this.comparator;
+
//read values
valuel = ois. readObject();
value2 = ois.readObject();
//compare and add to ordered arraylist
if ((comparator.compare(value1, value2) > 0)){ comparator
orderedList.add(value1);
orderedList.add(value2) ;
} else {
orderedList.add(value2) ;
orderedList.add(value1) ; SPAG (Simplified Pointer
; y Assignment Graph) + Worklist
algorithm
```

## Slide 25

## **Lightweight static analysis**

### Class A

**Simplified PAG (Pointer Assignment Graph) + Worklist algorithm**

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Lightweight static analysis
Class A
public void readObject(ObjectInputStream ois) {
//get comparator
this.comparator = (Comparator) ois. readObject
Comparator comparator = threadLocal. get (
if (comparator == null) {
comparator = this.comparator;
public class ValueComparator implements Comparator{
dOverride
public int compare(Value v1, Value v2) {
return v1.getValue() - v2.getValue();
}
}
//read values
valuel1 = ois.readObject();
value2 = ; r public class InvokeComparator implements Comparator {
//compa d ring methodName; .
if ( : a 1 String className; Exn\o""
orderedList.add(value1) ;
orderedList.add(value2) ; @0verride
} else { , public int compare(Object 01, Object o2) {
pee RO AR ee eNO Method method = Class. forName(className)
Simplified PAG (Pointer . getMethod (methodName) ;
} 7 . method. setAccessible(true) ;
} Assignment Graph) + Worklist return (int) method. invoke(o1, 02) ;
algorithm
25
```

## Slide 26

## **Lightweight static analysis - Highlight**

1. Goal: Locate all candidate gadget chains within limited computation time and resources

2. Solution: Andersen-style analysis.

3. Techniques: SPAG and On-demand CHA.

26

## Slide 27

## **Directed greybox fuzzing**

### **_Lightweight Taint_ Analysis and** **_Directed_ Greybox Fuzzing**

E Lightweight static analysis

E Directed Greybox Fuzzing

27

## Slide 28

## **Directed greybox fuzzing – seed generation**

How to generate seeds which satisfied serialization stream format?

- Ø Construct object that will be serialized, rather than generate serialization stream.

Fig. 1: The serialization stream sample<sup>[1]</sup>

28

[1] https://docs.oracle.com/javase/8/docs/platform/serialization/spec/protocol.html

## Slide 29

## **Directed greybox fuzzing – seed generation**

Class A

Okay, but how to construct object that will be serialized?

- Ø Use sun.misc.Unsafe to obtain an instance.

- Ø Use reflection feature to set fields.

29

## Slide 30

## **Directed greybox fuzzing – seed generation**

Fine, How to represent the multi-level struct of seeds?

- Ø We adopt a hierarchical data structure called _property tree_ to handle the complex forms of seeds _._

Fig. 1: property tree

30

## Slide 31

## **Directed greybox fuzzing – seed mutation**

Fine, what values will be assigned to the leaf nodes?

Fig. 1: candidate gadget chain

- Ø Pre-generated values and Random generated values

- Ø Pre-generated values are constructed according to the candidate gadget chain (Fig. 1)

- Ø Pre-generated values have a higher priority when mutation

31

Fig. 2: property tree

## Slide 32

## **Directed greybox fuzzing – seed mutation**

Fine, what values will be assigned to the leaf nodes? **Type Candidate values** Comparator InvokeComparator String class names, method names, ‘f5a5a608’, random Class class involved in gadget chains, random Boolean true, false Integer -15~15, random Object above values

Fig. 1: candidate gadget chain

32

Fig. 2: property tree

## Slide 33

## **Directed greybox fuzzing – seed prioritization**

Entry
Class A
stmt1
stmt2
stmt3
stmt4
stmt5
Exit
33

Fig. 1: candidate gadget chain

Entry
stmt
Exit
Fig. 2: CFG

Fig. 3: CFG

## Slide 34

## **Directed greybox fuzzing – seed prioritization**

Entry
How to efficiently select and schedule
stmt1
the seeds to trigger sensitive sinks?
stmt2 Ø Distance + Coverage
Ø Distance: more likely to reach the sink method
Entry Ø Coverage: exploring more paths
stmt3 Closer to
sink
stmt & sink
𝑝 𝑠, 𝑇! = 𝜑 𝑠' (1 − 𝑑(𝑠, 𝑇 + !))
stmt4
stmt5
Exit
Trigger more branches in the
gadget (exploring diverse
Exit Fig. 1: CFG execution paths)

34

## Slide 35

## **Directed greybox fuzzing – Highlight**

1. Goal: verify whether the candidate gadget chain is reachable and exploitable.

2. Solution: Directed greybox fuzzing.

3. Techniques:

   - Seed generation: Property tree

   - Seed mutation: Pre-generated values

   - Seed prioritization: Hybrid feedback

35

## Slide 36

## **Agenda**

- Introduction

- Previous work & Remaining challenges

- ODDFuzz: A novel approach to hunting gadget chains

- Evaluation

- Conclusion & Takeaways

## Slide 37

## **Evaluation**

### **_Experimental setup_**

- **Target Applications**

   - Known gadget chains reproduction: 22 Java libraries (covering 34 chains) from ysoserial

   - • Unknown gadget chains discovery: Well-known applications (including Oracle WebLogic Server, Sonatype Nexus, Apache Dubbo, protostuff)

- **Implementations**

   - Repeat each experiment 10 times and report the average statistical performance.

   - Set the threshold for each gadget chain to 15 gadgets.

   - Limit the fuzzing campaign to 120 seconds

37

## Slide 38

## **Evaluation - baseline**

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Evaluation - baseline
Sage . Covered Covered Known Identified Confirmed Analysis Fuzzing
Application Version Lo Classes Methods Sources Sinks Chains Chains Chains Time Time
JDK 1.7 4.4M 38.5K 324.6K 7 4 4 9 (1) 1 ImS1s 16m32s
AspectJ Weaver 1.9.2 692.4K 7K 19.8K 4 2 1 9 (1) 0 1m56s 18m
BeanShell 2.0b5 44.8K 1.1K 17K 3 1 1 8 (0) 0 1m53s 16m
C3P0 0.9.5.2 30.3K 644 10.1K 6 3 1 13 (1) 1 1m50s 25m53s
Click 2.3.0 10.8K 73 8.5K 4 1 1 8 (1) 1 1m48s 15m26s
Clojure 1.8.0 58.4K 3.8K 25.7K 5 4 1 184 (1) 1 3m30s 6h7m34s
CommonsBeanutils 1.9.2 714K 504 7.8K 3 1 | 8 (1) 1 1m52s 14m25s
CommonsCollections 3.1 101K 798 9.7K 7 4 5 97 (5) 3 1m58s 3h10m53s
CommonsCollections4 4.0 101K 630 7.4K 5 2 2 112 (2) 2 1m55s 3h41m9s
FileUpload 1.3.1 10.5K 56 3.1K 3 1 1 8 (0) 0 1mS55s 16m
Groovy 2.3.9 252.4K 4.2K 45.6K 4 1 1 13 (0) 0 2m8s 26m
Hibernate 43.11 855.7K TAK 42.7K 3 1 2 8 (2) 2 2m8s 14m7s
JBossInterceptors 2.0.0 24.2K 166 2.3K 2 1 1 8 (0) 0 1mS51s 16m
JSON 2.4 28K 172 5.9K 3 2 1 9 (0) 0 1m52s 18m
JavassistWeld 3.12.1 60.4K 813 11.3K 2 1 1 8 (0) 0 1m58s 16m
Jython 2.5.2 271.9K 6.7K 66.4K 4 1 1 32 (1) 0 2m54s 1h4m
MozillaRhino 1.7R2 118.7K 329 8.2K 4 2 2 7 (2) 2 1m56s 12m10s
Myfaces 2.2.9 330.1K 1.8K 22.8K 2 1 2 7 (0) 0 2mIs 14m
ROME 1.0 94.5K 423 6.9K 2 i} 1 5 (1) 1 Im48s 8m53s
Spring 4.1.4 904.3K 1.3K 14.5K 3 2 2 10 (0) 0 1mS9s 20m.
Vaadin 7.714 572.1K 4.5K 17.5K 4 1 1 13 (1) 1 1m54s 24m37s
Wicket 6.23.0 420.7K 3.2K 11L.1K 2 1 1 7 (0) 0 1m50s 14m
Total - - - - - 34 - -
38
```

## Slide 39

## **Evaluation - baseline**

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Evaluation - baseline
Known GadgetInspector SerHybrid ODDFvUzz
Application Chains Identified Confirmed — Analysis Identified Confirmed Analysis Identified Confirmed —_ Analysis Fuzzing
- Chains Chains Time Chains Chains Time Chains Chains Time Time
JDK 4 5 0 53s N/A N/A N/A 9 (1) 1 1mS1s 16m32s
AspectJ Weaver 1 6 0 Als N/A N/A N/A 9 (1) 0 1m56s 18m
BeanShell 1 2 0 49s 1 0 10m55s 8 (0) 0 1m53s 16m
C3P0 1 2 0 48s N/A N/A N/A 13 (1) 1 1mS0s 25m53s
Click 1 4 0 39s N/A N/A N/A 8 (1) 1 1m48s 15m26s
Clojure 1 12 1 40s N/A N/A Timeout 184 (1) 1 3m30s 6h7m34s
CommonsBeanutils 1 2 0 37s 0 0 13m6s 8 (1) 1 1m52s 14m25s
CommonsCollections 5 4 1 39s 1 1 26mS1s 97 (5) 3 1m58s 3h10m53s
CommonsCollections4 2 4 0 38s 1 1 I1lm21s 112 (2) 2 1m55s 3h41m9s
FileUpload 1 3 0 38s N/A N/A N/A 8 (0) 0 1m55s 16m
Groovy 1 4 0 47s 3 0 1h26m 13 (0) 0 2m8s 26m
Hibernate 2 3 0 Als 3 0 56m37s 8 (2) 2 2m8s 14m7s
JBossInterceptors 1 2 0 38s N/A N/A N/A 8 (0) 0 1lm51s 16m
JSON 1 2 0 39s N/A N/A N/A 9 (0) 0 1m52s 18m
JavassistWeld 1 2 0 39s N/A N/A N/A 8 (0) 0 1m58s 16m
Jython 1 42 1 50s N/A N/A Timeout 32 (1) 0 2m54s 1h4m
MozillaRhino 2 3 0 40s N/A N/A N/A 7 (2) 2 1m56s 12m10s
Myfaces 2 2 0 37s N/A N/A N/A 7 (0) 0 2ml1s 14m
ROME 1 2 0 36s 0 0 6m30s 5) 1 1m48s 8m53s
Spring 2 2 0 38s N/A N/A N/A 10 (0) 0 1m59s 20m
Vaadin 1 5 0 37s N/A N/A N/A 13 (1) 1 1m54s 24m37s
Wicket 1 3 0 36s N/A N/A N/A 7 (0) 0 1m50s 14m
Total 34 116 3 - {9 2 - | 583 (20) 16 - -
39
```

## Slide 40

## **Evaluation - baseline**

#### **Effectiveness**

- ü Detect **_13_** unique gadget chains that cannot be found by baselines.

- ü Report **_6_** exploitable Java ODD vulnerabilities, **_5_** of them have been assigned CVE-IDs.

40

## Slide 41

## **Evaluation – case study**

### WebLogic coherence RCE

Transform java com.tangosol.net.security.PermissionInfo#readExternal(java.io.ObjectInput) deserialization to com.tangosol.util.ExternalizableHelper#readCollection coherence custom com.tangosol.util.ExternalizableHelper#readObject(java.io.DataInput, java.lang.ClassLoader) deserialization com.tangosol.util.ExternalizableHelper#readObjectInternal com.tangosol.util.ExternalizableHelper#readExternalizableLite(java.io.DataInput, java.lang.ClassLoader) com.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal(java.io.DataInput) com.tangosol.util.aggregator.TopNAggregator.PartialResult#add source method com.tangosol.util.comparator.ExtractorComparator#compare com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract com.tangosol.coherence.mvel2.MVEL#executeExpression(java.lang.Object, java.lang.Object) sink method Fig. 1: candidate gadget chain reported by the lightweight static analyzer

41

## Slide 42

## **Evaluation – case study**

c om.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal( java.io.DataInput) com.tangosol.util.aggregator.TopNAggregator.PartialResult#add com.tangosol.util.comparator.ExtractorComparator#compare com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract c om.tangosol.coherence.mvel2.MVEL#executeExpression(java.lang.Object, java.lang.Object)

42

## Slide 43

## **Evaluation – case study**

WebLogic coherence RCE
com.tangosol.net.security.PermissionInfo#readExternal(java.io.ObjectInput)
com.tangosol.util.ExternalizableHelper#readCollection
com.tangosol.util.ExternalizableHelper#readObject(java.io.DataInput, java.lang.ClassLoader)
com.tangosol.util.ExternalizableHelper#readObjectInternal
com.tangosol.util.ExternalizableHelper#readExternalizableLite(java.io.DataInput, java.lang.ClassLoader)
com.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal(java.io.DataInput)
com.tangosol.util.aggregator.TopNAggregator.PartialResult#add
com.tangosol.util.comparator.ExtractorComparator#compare
com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract
com.tangosol.coherence.mvel2.MVEL#executeExpression(java.lang.Object, java.lang.Object)
Pre-generated Randomly generated Hardcoded

43

## Slide 44

## **Evaluation – case study**

c om.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal( java.io.DataInput) com.tangosol.util.aggregator.TopNAggregator.PartialResult#add com.tangosol.util.comparator.ExtractorComparator#compare com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract c om.tangosol.coherence.mvel2.MVEL#executeExpression(java.lang.Object, java.lang.Object) Fig. 1: expected stack trace

com.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal(java.io.DataInput) com.tangosol.util.aggregator.TopNAggregator.PartialResult#add com.tangosol.util.SortedBag#add java.util.TreeMap#put java.util.TreeMap#compare com.tangosol.util.SortedBag.WrapperComparator#compare com.tangosol.util.comparator.ExtractorComparator#compare com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract com.tangosol.coherence.mvel2.MVEL#executeExpression( java.lang.Object, java.lang.Object) Fig. 2: actual stack trace

44

## Slide 45

## **Evaluation – case study**

Trigger the sink method earlier than expected, but sink method has been executed.

com.tangosol.util.aggregator.TopNAggregator.PartialResult#readExternal(java.io.DataInput) com.tangosol.util.aggregator.TopNAggregator.PartialResult#add com.tangosol.util.SortedBag#add java.util.TreeMap#put java.util.TreeMap#compare com.tangosol.util.SortedBag.WrapperComparator#compare com.tangosol.util.comparator.ExtractorComparator#compare com.tangosol.coherence.rest.util.extractor.MvelExtractor#extract com.tangosol.coherence.mvel2.MVEL#executeExpression( java.lang.Object, java.lang.Object)

45

## Slide 46

## **Evaluation – discussion**

1. Runtime polymorphism and other dynamic language features make it difficult to make trade-offs between precision and recall.

2. Java deserialization gadget chains can be quite long, which causes huge computation space and amplifies the inaccuracy.

3. Existing tools are unable to validate candidate gadget chains, which require manual inspection and are time-consuming and error-prone.

46

## Slide 47

## **Evaluation – future work**

1. Better static analysis.

2. More dynamic features support.

3. Automatic exploit construction.

47

## Slide 48

## **Agenda**

- Introduction

- Previous work & Remaining challenges

- ODDFuzz: A novel approach to hunting gadget chains

- Evaluation

- Conclusion & Takeaways

## Slide 49

## **Conclusion & Takeaways**

1. Attendees will know the current state and remaining challenges of state-of-the-art gadget chain discovery tools.

2. Attendees will understand how ODDFuzz works and why it hunts gadget chains efficiently and precisely.

3. Attendees will learn how to optimize fuzzing when adapting it to an object-oriented language.

49

## Slide 50

# Thanks

@codeplutos

@meizjm3i

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piftkhat
LUISA PO2z3 ae iG
Thanks
W @codepLutos W omeizjm3i
```
