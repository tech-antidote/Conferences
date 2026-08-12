---
title: "JDD In-depth Mining of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction"
speakers: ["Bofei Chen", "Yinzhi Cao", "Lei Zhang", "Xinyou Huang", "Yuan Zhang", "Min Yang"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Bofei Chen & Yinzhi Cao & Lei Zhang & Xinyou Huang & Yuan Zhang & Min Yang_JDD In-depth Mining of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction.pdf"
pages: 63
sha256: "751c74609dfb52d44ea1823bb0aae277968f9d298cd85e1360b053d1b2521450"
text_chars: 47844
ocr_pages: 0
has_ocr: false
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T21:03:35Z"
---
# JDD In-depth Mining of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction

**Speakers:** Bofei Chen, Yinzhi Cao, Lei Zhang, Xinyou Huang, Yuan Zhang, Min Yang  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Bofei Chen & Yinzhi Cao & Lei Zhang & Xinyou Huang & Yuan Zhang & Min Yang_JDD In-depth Mining of Java Deserialization Gadget Chains via Bottom-up Gadget Search and Dataflow-aided Payload Construction.pdf` (63 pages)


## Slide 1

JDD: In-depth Mining of Java Deserialization Gadget Chain via Bottom-up Gadget Search and Dataflow aided Payload Construction

**Speaker: Bofei Chen, Yinzhi Cao Other Contributors: Lei Zhang, Xinyou Huang, Yuan Zhang, Min Yang**

#BHAS @BlackHatEvents

## Slide 2

### Who Are We

###### **Bofei Chen (Speaker)**

- PhD student at Fudan University @ Secsys Lab

- Focus on program analysis, vulnerability detection and exploitation.

###### **Yinzhi Cao (Speaker)**

- Associate Professor at Johns Hopkins University

- Technical Director at the JHU Information Security Institute

- Focus on security and privacy of the Web, smartphones, and machine learning using program analysis techniques.

#BHAS @BlackHatEvents

## Slide 3

### Who Are We

###### **Lei Zhang**

- Assistant Professor at Fudan University @ Secsys Lab

- Focus on vulnerability detection, exploitation, and automatic fixes, etc.

###### **Xinyou Huang**

- Master student at Fudan University @ Secsys Lab

- Focus on dynamic and static program analysis, vulnerability exploitation.

###### **Yuan Zhang**

- Professor at Fudan University @ Secsys Lab (co-director)

- Focus on vulnerability research (e.g., Web, agents, kernel and firmware)

###### **Min Yang**

- Professor at Fudan University @ Secsys Lab (leader)

- Focus on vulnerability discovery, mitigation, and privacy protection, etc.

#BHAS @BlackHatEvents

## Slide 4

### Agenda

- **Introduction**

- **Technique Challenges**

- **JDD: Approach and Implementation**

- **Evaluation and New Findings**

- **Conclusion & Takeaways**

#BHAS @BlackHatEvents

## Slide 5

# Introduction

- **What is a Java deserialization vulnerability?**

- **Why is Java deserialization vulnerability worth researching?**

- **How to detect and exploit a Java deserialization vulnerability?**

- **Mitigation and discussion.**

#BHAS @BlackHatEvents

## Slide 6

##### Java Serialization and Deserialization

• Serialization and deserialization are inverse processes of each other. An object’s fields are preserved along with their assigned values.

Java  Stream of  Stream of  Java
Database
Object Bytes Bytes Object
field a field b Communication field a field b
… Data …

###### **Application Scenario**

- Communication

- Persistence

- Data Exchange Format

- Caching

• …

#BHAS @BlackHatEvents

## Slide 7

##### Java Deserialization Vulnerability

- Serialization and deserialization are inverse processes of each other. An object’s fields are preserved along with their assigned values.

è **By carefully manipulating the types and values of serialized data, an attacker can control the deserialization process** , potentially leading to remote code execution or other severe security impacts.

#BHAS @BlackHatEvents

## Slide 8

##### Why is Java Deserialization vulnerability worth researching?

- **High-impact security risks**

   - Can achieve attack consequences such as **_Remote Code Execution (RCE),_** data tampering, Denial of Service (DoS)…

#BHAS @BlackHatEvents

Log4Shell "nuclear bomb vulnerability" (CVE-2021-44228)#BHAS @BlackHatEvents

Java deserialization vulnerabilities rank among the Top 10 in OWASP

## Slide 9

Why is Java Deserialization vulnerability worth researching?

- **Widespread use of deserialization**

- The built-in serialization/deserialization mechanism in Java is widely integrated across multiple frameworks, libraries and features (e.g., RMI, HTTP sessions…).

- Thus, completely avoiding or replacing it can be highly challenging.

#BHAS @BlackHatEvents

## Slide 10

##### Java Deserialization Vulnerability

- 1 // Client Side

- 2   // For example, a request message

- 3 Object message = getRequestMessage();

- 4 // Serialize the Java object by Hessian protocol

- 5    byte[] serializedData = hessianSerialize(message)

- 6   // Send the serialized data to the server

- 7    Socket socket = new Socket(host_of_victim_server, port)

- 8    Socket.getOutputStream().write(serializedData).flush()

###### **Send the serialized data to the target server.**

#BHAS @BlackHatEvents

## Slide 11

##### Java Deserialization Vulnerability

- 1 // Client Side

- 2   // For example, a request message

- 3    Object message = getRequestMessage();

- 4 // Serialize the Java object by Hessian protocol

- 5    byte[] serializedData = hessianSerialize(message)

- 6   // Send the serialized data to the server

   - Reconstruct the original _Message_ object

- 7    Socket socket = new Socket(host_of_victim_server, port)

- 8    Socket.getOutputStream().write(serializedData).flush()

- 1 // Server Side

- 2   // Receive the serialized data from the client

   - Use the reconstructed object in the system’s business logic (e.g., message

   - handling, order processing).

- 3 ServerSocket serverSocket = new ServerSocket(port);

- 4 Socket socket = serverSocket.accept();

- 5 Hessian2Input hi = new Hessian2Input(socket.getInputStream()) 6   // Deserialize the received serialized data 7    Message deserMsg = (Message) hi.readObject();

**Receive the serialized data and deserialize it into a Java object**

#BHAS @BlackHatEvents

## Slide 12

##### Java Deserialization Vulnerability

- 1 // Client Side

- 2   // For example, a well-crafted HashMap instance

- 3    Object hashMap = getRequestMessage();

- 4 // Serialize the Java object by Hessian protocol

- 5    byte[] serializedData = hessianSerialize(hashMap)

- 6   // Send the serialized data to the server

- 7    Socket socket = new Socket(host_of_victim_server, port)

- 8    Socket.getOutputStream().write(serializedData).flush()

**E.g., a well-crafted** 1 // Server Side **HashMap instance**

- 2   // Receive the serialized data from the client

public class MapDeserializer { Object readMap(A…HessianInput in) {… Map map = new HashMap(); while(!in.isEnd()){ map.put(in.readObject(), …); // entry }} }

- 3 ServerSocket serverSocket = new ServerSocket(port);

- 4 Socket socket = serverSocket.accept();

- 5 Hessian2Input hi = new Hessian2Input(socket.getInputStream())

- 6   // Deserialize the received serialized data

7    Message deserMsg = (Message) hi.readObject();

###### **Receive the serialized data and deserialize it into a Java object**

#BHAS @BlackHatEvents

## Slide 13

##### Java Deserialization Vulnerability

- 1 // Client Side

- 2   // For example, a well-crafted HashMap instance

- 3    Object hashMap = getRequestMessage();

- 4 // Serialize the Java object by Hessian protocol

- 5    byte[] serializedData = hessianSerialize(hashMap)

- 6   // Send the serialized data to the server

- 7    Socket socket = new Socket(host_of_victim_server, port)

- 8    Socket.getOutputStream().write(serializedData).flush()

**E.g., a well-crafted** 1 // Server Side **HashMap instance**

- 2   // Receive the serialized data from the client

- 3 ServerSocket serverSocket = new ServerSocket(port); 4 Socket socket = serverSocket.accept();

- 5 Hessian2Input hi = new Hessian2Input(socket.getInputStream())

public class MapDeserializer { Object readMap(A…HessianInput in) {… Map map = new HashMap(); while(!in.isEnd()){ map.put(in.readObject(), …); // entry }} }

public class HashMap { Node<K,V>[] table; **// Entry method** public void put(K key, V value){… key.equals(value); … }}

- 6   // Deserialize the received serialized data

7    Message deserMsg = (Message) hi.readObject();

**Receive the serialized data and deserialize it into a Java object**

#BHAS @BlackHatEvents

## Slide 14

##### Java Deserialization Vulnerability

public class HashMap { Node<K,V>[] table; public void put(K key, V value){… key.equals(value); … }} public class EvilExample{ public String cmd; public boolean equals(Object o){… Runtime.getRuntime() .exec((EvilExample)o.cmd);}}

① Control the **type** of _key_ : control the deserialization process to execute the **EvilExample.equals** method.

#BHAS @BlackHatEvents

## Slide 15

##### Java Deserialization Vulnerability

public class HashMap { Node<K,V>[] table; public void put(K key, V value){… key.equals(value); … }} public class EvilExample{ public String cmd; public boolean equals(Object o){… Runtime.getRuntime() .exec((EvilExample)o.cmd);}}

① Control the **type** of _key_ : control the deserialization process to execute the **EvilExample.equals** method. ② Control the **value** of _o.cmd_ : control the executed code.

**Remote Code Execution**

#BHAS @BlackHatEvents

## Slide 16

How to detect and exploit a Java Deserialization vulnerability?

- **Gadget Chain** : A chain of **internal Java methods** (i.e., **gadgets** ) that can invoke securitysensitive method(s) capable of executing malicious code during the deserialization process.

- **Injection Object** : A **serialized object** that drives the execution of the gadget chain.

HashMap
table
EvilExample EvilExample
cmd

E.g., HashMap.put
-> EvilExample.equals
-> Runtime.exec

###### **Gadget Chain**

**Serialized => Injection Object**

#BHAS @BlackHatEvents

## Slide 17

##### Mitigation and Discussion

- **Commonly used defenses**

   - Setting a black/whitelist to restrict classes that can be deserialized to truncate the gadget chains

   - Restricted blocking options: to ensure that normal business functions are not affected.

WebLogic’s JOI vulnerabilities and the **reuse of their gadgets** , which lead to the **incomplete patch problem** .

#BHAS @BlackHatEvents

## Slide 18

##### Mitigation and Discussion

• An example of reusing partial gadgets to generate a new exploitable gadget chain.

- **1   // A part of code of the patch of CVE-2020-2883.**

- **2 // Rewriting** **_resolveClass_ method of** **_ObjectInputStream_ .**

- **3   Class<?> resolveClass(ObjectStreamClass desc) {**

- **4         String clzName = desc.getName();**

- **5         if (this.blackList.contains(clzName)) { 6               throw new  InvalidClassException();**

- **7         } 8         return super.resolveClass(desc);**

**9   }**

- **10 String[] blackList = {**

- **11 “com.tangosol.util.extractor.ReflectionExtractor”,**

- **12 “com.tangosol.util.extractor.MultiExtractor” ...**

**13 };**

- **1   PriorityQueue#readObject 2 PriorityQueue#heapify 3 PriorityQueue#siftDown 4 PriorityQueue#siftDownUsingComparator 5 AbstractExtractor#compare 6 MultiExtractor#extract 7 ReflectionExtractor#extract 8 Method#invoke**

**CVE-2020-14645**

- **1   ExtractorComparator#compare**

- **2 UniversalExtractor#extract**

- **3 UniversalExtractor#extractComplex**

#BHAS @BlackHatEvents

## Slide 19

##### Mitigation and Discussion

#### **Persistence of the threat**

- Attackers can find replaceable gadgets that **bypass defenses** (e.g., blacklist).

- **Java’s dynamic features**

- **Widespread use of third-party components**

- The fundamental design of Java deserialization allows for a large attack surface, and new classes with exploitable features may be introduced over time.

#BHAS @BlackHatEvents

## Slide 20

# Technical Challenges

- **How to detect gadget chains?**

- **How to generate the injection object?**

#BHAS @BlackHatEvents

## Slide 21

##### Quest ion I: Ho w to detect Gadget Chains in the real-world?

1 /* Gadget Fragment I: HashMap.put -> HashMap.putVal */
2 public class HashMap implements ...{
3   Node<K,V>[] table;
4     V put(K key, V value) {returen putVal(hash(key), key, value, …);}
5     V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ...
6         Node<K,V> p =  table[pre_inde x]; // p is an element in table
7 if (p.hashCode() == hash & p.key != key & key != null)
8 as 1 key.equals(p.key); } …}
9 } as2
10 /*  Gadget Frafment II: Simple Entry.equals ->…->Object.equals */
11 public static class SimpleEntry<K,V>{
Candidates: 2751
12     private final K k ey; private V valu e;
13 public int hashCode() {… return key.hashCode()^value.hashCode();}
14     public boolean equals(Object o) {
15 if (o instanceof Map.Entry)
16 return  eq (key, (Map.Entry)e.getKey())  &&  eq (value, e.getValue());}
17 }  xstrFSB j sonOb j

**An deserialization entry method (i.e., source)**

###### **…**

39 /* Gadget Fragment VI: ObjectWriter2.write -> FieldWritter.write */
40 public class ObjectWriter2<T> { Candidates: 87
41 public final FieldWriter fieldWriter;
42 void write(…, Object object, ...) { fieldWriter.write(…, object);}
43 }
44 /* Gadget Fragment VII: FieldWritterObject.write -> Method.invoke */
45 abstract class FieldWriterObject<T> {
Candidates: 55
46     // the method to g et the value of a  field. E.g. getter method
47 public final Method method;
48 public boolean write(…, T object) { ...getFieldValue(object);}
49 public Object getFieldValue(Object object)  {this.method.invoke(object);  ...}
50 } // Unsafe Reflection
jsonObj.map

**Part of the simplified exploitable Gadget Chain detected by JDD**

#BHAS @BlackHatEvents

## Slide 22

##### Quest ion I: Ho w to detect Gadget Chains in the real-world?

1 /* Gadget Fragment I: HashMap.put -> HashMap.putVal */
2 public class HashMap implements ...{
3   Node<K,V>[] table;
4     V put(K key, V value) {returen putVal(hash(key), key, value, …);}
5     V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ...
6         Node<K,V> p =  table[pre_inde x]; // p is an element in table
7 if (p.hashCode() == hash & p.key != key & key != null)
8 as 1 key.equals(p.key); } …}
9 } as2
10 /*  Gadget Frafment II: Simple Entry.equals ->…->Object.equals */
11 public static class SimpleEntry<K,V>{
Candidates: 2751
12     private final K k ey; private V valu e;
13 public int hashCode() {… return key.hashCode()^value.hashCode();}
14     public boolean equals(Object o) {
15 if (o instanceof Map.Entry)
16 return  eq (key, (Map.Entry)e.getKey())  &&  eq (value, e.getValue());}
17 }  xstrFSB j sonOb j

**An deserialization entry method (i.e., source) A controllable dynamic method call**

###### **…**

39 /* Gadget Fragment VI: ObjectWriter2.write -> FieldWritter.write */
40 public class ObjectWriter2<T> { Candidates: 87
41 public final FieldWriter fieldWriter;
42 void write(…, Object object, ...) { fieldWriter.write(…, object);}
43 }
44 /* Gadget Fragment VII: FieldWritterObject.write -> Method.invoke */
45 abstract class FieldWriterObject<T> {
Candidates: 55
46     // the method to g et the value of a  field. E.g. getter method
47 public final Method method;
48 public boolean write(…, T object) { ...getFieldValue(object);}
49 public Object getFieldValue(Object object)  {this.method.invoke(object);  ...}
50 } // Unsafe Reflection
jsonObj.map

**Part of the simplified exploitable Gadget Chain detected by JDD**

#BHAS @BlackHatEvents

## Slide 23

##### Quest ion I: Ho w to detect Gadget Chains in the real-world?

1 /* Gadget Fragment I: HashMap.put -> HashMap.putVal */
2 public class HashMap implements ...{
3   Node<K,V>[] table;
4     V put(K key, V value) {returen putVal(hash(key), key, value, …);}
5     V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ...
6         Node<K,V> p =  table[pre_inde x]; // p is an element in table
7 if (p.hashCode() == hash & p.key != key & key != null)
8 as 1 key.equals(p.key); } …}
9 } as2
10 /*  Gadget Frafment II: Simple Entry.equals ->…->Object.equals */
11 public static class SimpleEntry<K,V>{
Candidates: 2751
12     private final K k ey; private V valu e;
13 public int hashCode() {… return key.hashCode()^value.hashCode();}
14     public boolean equals(Object o) {
15 if (o instanceof Map.Entry)
16 return  eq (key, (Map.Entry)e.getKey())  &&  eq (value, e.getValue());}
17 }  xstrFSB j sonOb j

**An deserialization entry method (i.e., source) A controllable dynamic method call**

###### **…**

39 /* Gadget Fragment VI: ObjectWriter2.write -> FieldWritter.write */
40 public class ObjectWriter2<T> { Candidates: 87
41 public final FieldWriter fieldWriter;
42 void write(…, Object object, ...) { fieldWriter.write(…, object);}
43 }
44 /* Gadget Fragment VII: FieldWritterObject.write -> Method.invoke */
45 abstract class FieldWriterObject<T> {
Candidates: 55
46     // the method to g et the value of a  field. E.g. getter method
47 public final Method method;
48 public boolean write(…, T object) { ...getFieldValue(object);}
49 public Object getFieldValue(Object object)  {this.method.invoke(object);  ...}
50 } // Unsafe Reflection
jsonObj.map
unsafe
Reflection

**Part of the simplified exploitable Gadget Chain detected by JDD**

#BHAS @BlackHatEvents

## Slide 24

##### Quest ion I: Ho w to detect Gadget Chains in the real-world?

1 /* Gadget Fragment I: HashMap.put -> HashMap.putVal */
2 public class HashMap implements ...{
3   Node<K,V>[] table;
4     V put(K key, V value) {returen putVal(hash(key), key, value, …);}
5     V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ...
6         Node<K,V> p =  table[pre_inde x]; // p is an element in table
7 if (p.hashCode() == hash & p.key != key & key != null)
8 as 1 key.equals(p.key); } …}
9 } as2
10 /*  Gadget Frafment II: Simple Entry.equals ->…->Object.equals */
11 public static class SimpleEntry<K,V>{
Candidates: 2751
12     private final K k ey; private V valu e;
13 public int hashCode() {… return key.hashCode()^value.hashCode();}
14     public boolean equals(Object o) {
15 if (o instanceof Map.Entry)
16 return  eq (key, (Map.Entry)e.getKey())  &&  eq (value, e.getValue());}
17 }  xstrFSB j sonOb j
…
39 /* Gadget Fragment VI: ObjectWriter2.write -> FieldWritter.write */
40 public class ObjectWriter2<T> { Candidates: 87
41 public final FieldWriter fieldWriter;
42 void write(…, Object object, ...) { fieldWriter.write(…, object);}
43 }
44 /* Gadget Fragment VII: FieldWritterObject.write -> Method.invoke */
45 abstract class FieldWriterObject<T> {
Candidates: 55
46     // the method to g et the value of a  field. E.g. getter method
47 public final Method method;
48 public boolean write(…, T object) { ...getFieldValue(object);}
49 public Object getFieldValue(Object object)  {this.method.invoke(object);  ...}
50 } // Unsafe Reflection
jsonObj.map
unsafe
Reflection

**An deserialization entry method (i.e., source) A controllable dynamic method call**

**Command Injection Attack (i.e., sink)**

**Part of the simplified exploitable Gadget Chain detected by JDD**

#BHAS @BlackHatEvents

## Slide 25

##### Challenge I: Static Path Explosion

1 /* Gadget Fragment I: HashMap.put -> HashMap.putVal */
2 public class HashMap implements ...{
3   Node<K,V>[] table; # Fragment 1
4     V put(K key, V value) {returen putVal(hash(key), key, value, …);} HashMap.put (head)
5     V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ... HashMap.putVal
6         Node<K,V> p = table[pre_index]; // p is an element in table
7 if (p.hashCode() == hash & p.key != key & key != null)  Object.equals (end)
8 as 1 key.equals(p.key); } …} ①  Candidate: 2751
9 } as2 # Fragment 2
10 /* Gadget Frafment II: SimpleEntry.equals ->…->Object.equals */
11 public static class SimpleEntry<K,V>{ Abstract…Entry.equals (head)
12     private final K key; private V value; Candidates: 2751 AbstractMap.access$000
13 public int hashCode() {… return key.hashCode()^value.hashCode();} AbstractMap.eq
14     public boolean equals(Object o) { Object.equals (end)
15 if (o instanceof Map.Entry) Candidate: 2751
16 return  eq (key, (Map.Entry)e.getKey())  &&  eq (value, e.getValue());}
17 }  xstrFSB jsonObj # Fragment 3
18 public class AbstractMap implements …{ XStringForFSB.equals
19     private static boolean eq(Object o1, Object o2) { …
20         return o1 == null ?  o2  ==  null  :   o1.equals(o2); }} ②
21 /* Gadget Fragment III: XStringForFSB.equals -> Object.toString */ Candidate: 3129
22 public class XStringForFSB extends …{ # Fragment 4
23     protected Object m_obj; Candidates: 2751
24     public boolean equals(Object obj2){ JSONObject.toString
25         if (null != obj2 && !(obj2 instanceof XNumber)…) …
26 return equals (obj2.toString()) ;…}} Candidate: 3
③
27 jsonObj
28 /* Gadget Fragment IV: JSONObject.toString -> JSONWriter.write */ # Fragment 5
29 public abstract class JSONObject {
Candidates: 3129 JSONWriterUTF16.write
30  Node<String, Object> table;
Candidate: 87
31 public String toString() {
32          (JSONWriter) writer.write(this);  ...}} ④
33 /* Gadget Fragment V: JSONWriterUTF16.write ->ObjectWriter.write */ # Fragment 6
34 class JSONWriterUTF16 extends JSONWriter  { Candidates: 3 ObjectWriter2.write
35 public final void write(JSONObject jsonObject){ ...
36 for (Object value: jsonObject.map.values()){ … Candidate: 55
37             objectWriter. write(this, value, (Object)null, (Type)null, 0L); }} ⑤
38 } jsonObj.map # Fragment 7
39 /* Gadget Fragment VI: ObjectWriter2.write -> FieldWritter.write */
40 public class ObjectWriter2<T> { Candidates: 87 Field…ethod.write (head)
41 public final FieldWriter fieldWriter; Field…ethod.getFieldValue (head)
42 void write(…, Object object, ...) { fieldWriter.write(…, object);} ⑥  Method.invoke (end)
43 }
44 /* Gadget Fragment VII: FieldWritterObject.write -> Method.invoke */
4546 abstract class      // the method to get the value of a field. E.g. getter method FieldWriterObject<T> { Candidates: 55 # Fragment 8
47 public final Method method;      ServerM….getActiveServers (head)
48 public boolean write(…, T object) { ...getFieldValue(object);} ServerTableEntry.isValid
49 public Object getFieldValue(Object object)  {this.method.invoke(object);  ...}     ServerTableEntry.activate
50 } // Unsafe Reflection jsonObj.map Runtime.exec (sink)

**_Candidate: 2751 Candidate: 3129 Candidate: 3 Candidate: 87_**

**_# Fragment 8_** _ServerM….getActiveServers (head)_ ServerTableEntry.isValid ServerTableEntry.activate _Runtime.exec (sink)_

- During the search, it is easy to detect many dynamic method calls that the attacker can control.

- **Top-down** candidate search methods could grow exponentially with the search length.

25

#BHAS @BlackHatEvents

## Slide 26

##### Challenge II: Complex Object Field Relations

# Fragment 1
HashMap
HashMap.put Method.invoke
HashMap.putVal
Parallel and
# Fragment 8 table …
# Fragment 2 ServerManagerImpl.getActiveServers as1 as2
AbstractMap$SimpleEntry.equals Embedded Objects
ServerTableEntry.isValid
AbstractMap.access$000
ServerTableEntry.activate
AbstractMap$SimpleEntry AbstractMap$SimpleEntry
AbstractMap.eq Runtime.exec
# Fragment 3 smp
XStringForFSB.equals key value key value
ServerManagerI
mpl
xstrFSB jsonObj
# Fragment 4
JSONObject.toString XStringForFSB JSONObject JSONObject XStringForFSB
serverTable
# Fragment 5 Method.invoke
JSONWriterUTF16.write ServerTableEntry table Constraints Info
…
# Fragment 6 i.  as1 .hashCode() ==  as2 .hashCode()
ObjectWriter2.write state activateRetryCount activationCmd ServerManagerI smp ii.  smp .state == 2  (static field ACTIVATED)
mpl
iii.  smp .activateRetryCount < 5  (static field ActivationRetryMax)
# Fragment 7 getActiveServers() …
Inject malicious commands
FieldWriterObjectMethod.getFieldV
alue
Method.invoke
Challenge II: Complex object field relations

###### **Challenge II: Complex object field relations**

**_# Fragment 8_** ServerManagerImpl.getActiveServers ServerTableEntry.isValid ServerTableEntry.activate Runtime.exec

- Parallel and Embedded Injection Object Structure.

- Dependencies and constraints between fields.

#BHAS @BlackHatEvents

## Slide 27

## JDD: Approach and Implementation

- **Fragment-based Summary and Bottom-up Gadget Chain Search**

- • **Dataflow-aided Injection Object Construction**

#BHAS @BlackHatEvents

## Slide 28

##### Key Ideas

- **Path Explosion challenge** : **fragment-based summary** and **bottom-up** search approach.

   - _Key Observation: a bottom-up search reduces maximum static search time from exponential to polynomial, i.e., from O(_ 𝑒𝑀<sup>!</sup> _) to O(_ 𝑛<sup>"</sup> 𝑀<sup>#</sup> + 𝑒𝑛𝑀 _)._

- **Complex Object Field Relations:** use static taint analysis to **construct dataflow dependencies between possible injection objects’ fields** and use them to guide dynamic fuzzing to generate exploitable objects.

   - _Key Observation: different injection objects, e.g., their fields, are connected via dataflows._

#BHAS @BlackHatEvents

## Slide 29

##### Overall Architecture

- **Stage I: Gadget Chain Detection**

   - **Stage II: Injection Object Generation**

- Identify Entry Points

   - Generate IOCD

- Search Fragments

- Link Fragments via a bottom-up

- IOCD-enhanced directional Fuzzing to verify the exploitability of gadget chains

###### approach

1  Identify Entries 2  Identify Fragments 3  Link Fragments 4   Generate IOCD 5 Validate Exploitability
Entry Gadget  Gadget  Constrains Injection Object
Points Fragments  Fragments Gadget  Collection Generation & Mutation
Chains
Target  Identification Searching Linking Dominator
Application Injection  Constraints-based
Object
Feedback
Reusable
Fragment
Fragments  IOCD Fuzzing-based
Data Set IOCD
Extraction Generation Exploitability Validation
Exploits
New Exploitable Injection Object

**Stage II: Exploitable Injection Object Generation** 29

**Stage I: Gadget Chain Detection**

#BHAS @BlackHatEvents

## Slide 30

##### Fragment-based Summary

**Q: What is the biggest “culprit” that leads to path explosion in static analysis?**

**A: Dynamic method invocation**

#BHAS @BlackHatEvents

## Slide 31

##### Fragment-based Summary

**Q: What is the biggest “culprit” that leads to path explosion in static analysis?**

**A: Dynamic method invocation**

- **Break down the one-time search for a complete gadget chain into the search and chaining of multiple smaller and simpler segments based on dynamic method calls.**

- **Generate bottom-up summaries for each segment to minimize redundant analysis**

#BHAS @BlackHatEvents

## Slide 32

##### Fragment-based Summary

**Q: What is the biggest “culprit” that leads to path explosion in static analysis?**

**A: Dynamic method invocation**

- **Break down the one-time search for a complete gadget chain into the search and chaining of multiple smaller and simpler segments based on dynamic method calls.**

- - **Generate bottom-up summaries for each segment to minimize redundant analysis**

**Q: Why not generate detailed summaries for each method directly?**

**A: To balance path explosion** 32 **and state explosion.**

#BHAS @BlackHatEvents

## Slide 33

##### Component of Gadget Fragment

**_Head_** : entry method

- Source

- Exist some dynamic methods invocations that could jump to it

**_End_** : exist method

**_# Fragment 1 HashMap.put (head)_** HashMap.putVal **_Object.equals (end)_**

**_# Fragment 2 Abstract…Entry.equals (head)_** AbstractMap.access$000 AbstractMap.eq **_Object.equals (end)_**

**…**

- Dynamic method invocation or security-sensitive method.

**Other gadgets** : non-dynamic methods to connect the _head_ and _end_ .

**_# Fragment 6 ObjectWriter2.write (head) FieldWriter.write (end)_**

**_# Fragment 7 Field…ethod.write (head)_** Field…ethod.getFieldValue (head) **_Method.invoke (end)_**

#BHAS @BlackHatEvents

## Slide 34

##### Types of Gadget Fragment

###### **Source Fragment**

- whose head is a source method (e.g., readObject/ Map.put).

**_# Fragment 1 HashMap.put (head)_** HashMap.putVal **_Object.equals (end)_**

###### **Free-State Fragment**

- chains the execution sequence between two dynamic method invocations.

**_# Fragment 2 Abstract…Entry.equals (head)_** AbstractMap.access$000 AbstractMap.eq **_Object.equals (end)_**

###### **Sink Fragment**

- whose end is a sink.

**_# Fragment 7 Field…ethod.write (head)_** Field…ethod.getFieldValue (head) **_Method.invoke (end)_**

#BHAS @BlackHatEvents

## Slide 35

###### **F-I**

##### Summarized Information

**_Bottom-up taint behavior_** : dataflow reachability of the gadget chain

- Parameter taint relationships from _End_ (e.g., equals) to _Head_ (e.g., put)

**_Linking Condition_** : control flow reachability of the gadget chain

- The methods that the end gadget in this fragment

- can jump to. (Vary slightly for different types of dynamic invocations)

- E.g., _Head_ of F-II need to be the overridden method of _End_ of F-I

- **_Exploit Condition_** : the specific exploit condition for the sink gadget (in Sink Fragment)

**_Head1_**

Head1
gadget2
…
gadget_n
End1

_(a) Taint behavior: End pi => Head p[x,y,…]_

_(b) Link condition: E.g., Head2 is a overridden of Head1_

**F-II**

**_Head2_**

**_gadget2_**

**_gadget2_** _(c) Exploit Condition: E.g., in-coming_ **…** _parameters[1,2]_ of **_gadget_z_** _End2 need to be tainted_ **_End2 (sink)_**

**…**

**_End2 (sink)_**

#BHAS @BlackHatEvents

## Slide 36

#### STEP 1: Identify Entry Points

##### Step 1: Identify the entry points of deserialization (i.e., sources)

- Extract and filter deserialization entry methods ( **_i.e., sources_** )

- **A deserialization entry method (i.e., source)**

- 1 _/* Gadget Fragment I: HashMap.put -> HashMap.putVal */_

- 2 public class HashMap implements ...{

- 3 Node<K,V>[] table;

- 4 V put(K key, V value) {returen putVal(hash(key), key, value, …);}

- 5 V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ...

- 6 Node<K,V> p = table[pre_index]; // p is an element in table

- 7 if (p.hashCode() == hash & p.key != key & key != null)

- 8 as 1 key.equals(p.key); } ~~…}~~

- 9

   - } as2

- 10 _/* Gadget Frafment II: SimpleEntry.equals ->…->Object.equals */_

- 11 public static class SimpleEntry<K,V>{

   - Candidates: 2751

- 12 private final K key; private V value;

- 13 public int hashCode() {… return key.hashCode()^value.hashCode();}

- 14 public boolean equals(Object o) {

- 15 if (o instanceof Map.Entry)

- 16 return _eq_ (key, (Map.Entry)e.getKey()) && _eq_ (value, e.getValue());} 17 } xstrFSB jsonObj

#BHAS @BlackHatEvents

## Slide 37

#### STEP 2: Search Fragments

##### Step 2: Identify Gadget Fragments with Static Taint Analysis

- 1 _/* Gadget Fragment I: HashMap.put -> HashMap.putVal */_

- <u>2 public class HashMap implements ...{</u> ~~3~~ ~~N~~ ode<K,V>[] table; ① Fragment Summary: 4 V put(K key, V value) {returen putVal(hash(key), key, value, …);} 5 V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ... Taint analysis within a 6 Node<K,V> p = table[pre_index]; // p is an element in table 7 if (p.hashCode() == hash & p.key != key & key != null) fragment… ~~8~~ as 1 key.equals(p.key); } ~~…}~~ 9 } as2

- 10 _/* Gadget Frafment II: SimpleEntry.equals ->…->Object.equals */_ ❌

- 11 public static class SimpleEntry<K,V>{ Candidates: 2751

- 12 private final K key; private V value; 13 public int hashCode() {… return key.hashCode()^value.hashCode();} 14 public boolean equals(Object o) { 15 if (o instanceof Map.Entry) 16 return _eq_ (key, (Map.Entry)e.getKey()) && _eq_ (value, e.getValue());} 17 } xstrFSB jsonObj ② Search for subsequent 18 public class AbstractMap implements …{ 19 private static boolean eq(Object o1, Object o2) { gadget fragments 20 return o1 == null ?  o2  ==  null  : o1.equals(o2); }} 21 _/* Gadget Fragment III: XStringForFSB.equals -> Object.toString */_ 22 public class XStringForFSB extends …{ ❌ 23 protected Object m_obj; Candidates: 2751 24 public boolean equals(Object obj2){ 25 if (null != obj2 && !(obj2 instanceof XNumber)…) 26 return equals (obj2.toString()) ;…}} 27 jsonObj

**_# Fragment 1 HashMap.put (head)_** HashMap.putVal **_Object.equals (end)_**

**_# Fragment 2 Abstract…Entry.equals (head)_** AbstractMap.access$000 AbstractMap.eq **_Object.equals (end)_**

#BHAS @BlackHatEvents

## Slide 38

#### STEP 2: Search Fragments

##### Step 2: Identify Gadget Fragments with Static Taint Analysis

###### **_(1) Search Source: HashMap.put_**

HashMap.put **_(2) Generate_** HashMap.putVal **_Fragment_** Object.equals _a. Taint Summary b. Link condition Summary_

**_# Fragment_** _head: HashMap.put_ HashMap.putVal _end: Object.equals_

#BHAS @BlackHatEvents

## Slide 39

#### ~~<u>STEP 2 : Searc</u>~~ <u>h Fragments</u>

##### Step 2: Identify Ga <u>dget Fragments with Static Taint Analysis</u>

**_(_** **_~~2) Search Sources: methods overwritter~~ n `Object.equals`_**

AbstractMa p $SimpleEntry.equals ~~AbstractMap.access$000~~ AbstractMap.eq Object.equals

###### **_# Fragment_**

AbstractMap$SimpleEntry.equals AbstractMap.access$000 AbstractMap.eq

**_<u>…</u>_**

XStringForFSB.equals Object.toString

**_# Fragment_** XStringForFSB.equals

#### **_…_**

FieldWriterObjectMethod.getFieldValue Method.invoke

**_# Fragment 8# Fragment 7_** ServerManagerImpl.getActiveServersFieldWriterObjectMethod.getFieldV ServerTableEntry.isValidalue ServerTableEntry.activate Method.invoke i

**_…_**

#BHAS @BlackHatEvents

## Slide 40

#### STEP 2: Search ~~Fragments~~

Step 2: Identify Gadget Fra ~~<u>g</u>~~ ~~ments with S~~ tatic Taint Analysi s

**Source Fragm ents**

**Free-State Fragments**

**Sink Fragments**

**_# Fragment_** _head: HashMap.put_ HashMap.putVal _end: Object.equals_

**_# Fragment_** AbstractMap$SimpleEntry.equals Abstrac tMap.access$000 Abstra ~~c~~ ~~tMap.eq~~

###### **_# Fragment 7_**

FieldWriterObjectMethod.getFieldV alue Method.invoke

###### **_# Fragment 8_**

**_# Fra_** **_~~<u>g</u>~~_** **_~~<u>ment</u>~~_** XStringForFSB.equals

ServerManagerImpl.getActiveServers ServerTableEntry.isValid ServerTableEntry.activate Runtime.exec

**_…_**

**_…_**

**_…_**

#BHAS @BlackHatEvents

## Slide 41

##### STEP 3: Linking Fragments via a Bottom-up approach

Step 3: Linking Gadget Fragments to Construct Gadget Chains **_# Fragment 1_** Using a Bottom-up Approach HashMap.put

**_# Fragment 1_** HashMap.put HashMap.putVal

- **Chain gadget fragments from sink to source.**

- **-** Fully reuse existing sink knowledge to minimize repetitive analyses and reduce search complexity.

# Fragment 2
AbstractMap$SimpleEntry.equals
AbstractMap.access$000
AbstractMap.eq
# Fragment 3
XStringForFSB.equals

# Fragment 4
JSONObject.toString

Statically chained

Source
Dynamic Method Call
Sink
…
Gadget Chain
Search Path …
Single Search
Repeated Searches
…

**Top-Down Searching**

**Bottom-Up Searching**

**_# Fragment 5_** JSONWriterUTF16.write

# Fragment 6
ObjectWriter2.write

**_# Fragment 7_** FieldWriterObjectMethod.getFieldV alue Method.invoke

**_# Fragment 8_** ServerManagerImpl.getActiveServers ServerTableEntry.isValid ServerTableEntry.activate Runtime.exec

###### **Bottom-up Linking**

###### Dynamically chained

#BHAS @BlackHatEvents

## Slide 42

##### STEP 3: Linking Fragments via a Bottom-up approach

Step 3: Linking Gadget Fragments to Construct Gadget Chains Using a Bottom-up Approach

- **Chain gadget fragments from sink to source.**

- Based on the exploitation conditions of the sink, calculate the precise parameter contamination requirements, etc., for linking.

- Avoid linking calculations for dataflow-unreachable and control-flowunreachable fragments. Source

Source
[-1,0,1]
Fragment
Free-State  Free-State
[0,1] [0,2,3]
Fragment Fragment
… [0,3]
[0,2] [0,1,2]
… Sink
Fragment
Top-Down: Unpredictability  required tainted
to Sink Fragment  parameters of pre-
fragment:  #BHAS @BlackHatEvents[0,3]

Source
Dynamic Method Call
Sink
…
Gadget Chain
Search Path …
Single Search
Repeated Searches
…

Bottom-Up Searching

**Top-Down Searching**

## Slide 43

#### STEP 4: IOCD-enhanced Directed Fuzzing

**JDD follows the call sequence in the gadget chain to construct dataflow dependencies between possible injection objects’ fields as an IOCD ==> To facilitate dynamic fuzzing**

- Class hierarchy relationships between object and field instance

- Conditional branches related to fields

- Field dependency constraints

- Fields related to the attack payload

#BHAS @BlackHatEvents

## Slide 44

#### STEP 4: IOCD-enhanced Directed Fuzzing

##### v **Class Hierarchy Relationships**

- 1 _/* Gadget Fragment I: HashMap.put -> HashMap.putVal */_

- 2 public class HashMap implements ...{

3

Node<K,V>[] table;

4

V put(K key, V value) {returen putVal(hash(key), key, value, …);}

5 V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ... 6 Node<K,V> p = table[pre_index]; // p is an element in table 7 if (p.hashCode() == hash & p.key != key & key != null) 8 as 1 key.equals(p.key); } ~~…}~~ 9 } as2 **Class hierarchy Relationship** 10 _/* Gadget Frafment II: SimpleEntry.equals ->…->Object.equals */_ 11 public static class SimpleEntry<K,V>{SimpleEntry<K,V>{<K,V>{K,V>{,V>{V>{>{ **Field Type**

- public static class SimpleEntry<K,V>{SimpleEntry<K,V>{<K,V>{K,V>{,V>{V>{>{

**Field Type** Candidates: 2751

12 private final K key; private V value; 13 public int hashCode() {… return key.hashCode()^value.hashCode();} 14 public boolean equals(Object o) { 15 if (o instanceof Map.Entry) 16 return _eq_ (key, (Map.Entry)e.getKey()) && _eq_ (value, e.getValue());} 17 } xstrFSB jsonObj

• **Taint analysis: for each fragment, which of its fields is link to the next fragment?** - E.g., “table” field of the HashMap instance

(Fragment I) link to Fragment II.

#BHAS @BlackHatEvents

## Slide 45

#### STEP 4: IOCD-enhanced Directed Fuzzing

##### v **Class Hierarchy Relationships**

- 1 _/* Gadget Fragment I: HashMap.put -> HashMap.putVal */_ 2 public class HashMap implements ...{

3

Node<K,V>[] table;

4

V put(K key, V value) {returen putVal(hash(key), key, value, …);}

5 V putVal(int hash, K key, V value, boolean onlyIfAbsent, boolean evict) { ... 6 Node<K,V> p = table[pre_index]; // p is an element in table 7 if (p.hashCode() == hash & p.key != key & key != null) 8 as 1 key.equals(p.key); } ~~…}~~ 9 } as2 **Class hierarchy Relationship** 10 _/* Gadget Frafment II: SimpleEntry.equals ->…->Object.equals */_ 11 public static class SimpleEntry<K,V>{ **Field Type** Candidates: 2751

- 12 private final K key; private V value; 13 public int hashCode() {… return key.hashCode()^value.hashCode();} 14 public boolean equals(Object o) {

- 15 if (o instanceof Map.Entry)

- 16 return _eq_ (key, (Map.Entry)e.getKey()) && _eq_ (value, e.getValue());} 17 } xstrFSB jsonObj

• **Taint analysis: for each fragment, which of its fields is link to the next fragment?**

- E.g., “table” field of the HashMap instance

(Fragment I) link to Fragment II.

- Use the head of the subsequent fragment to determine the actual type of the field. E.g., The “table” field stores instances of the SimpleEntry type.

#BHAS @BlackHatEvents

## Slide 46

#### STEP 4: IOCD-enhanced Directed Fuzzing

##### v **Conditional Branch & Field Dependence**

57 public class ServerTableEntry{
58     private String activationCmd;
59     synchronized boolean isValid(){ Conditional Branch
60 if ((state ==  ACTIVATING ) || (state ==  HELD_DOWN )) r eturn true;
61 if (state ==  ACTIVATED ) {
62 if (activateRetryCount <  ActivationRetryMax ) {

- Extract conditional branches related to fields

- Constraint solving

#BHAS @BlackHatEvents

## Slide 47

#### STEP 4: IOCD-enhanced Directed Fuzzing

##### v **Dominator Constraints**

public V gadgetA(K key, V value){ Candidate Constraints 1
1    if (…) { // condition_branch_1
o
The constraints whose necessity CANOT be
        … determined by static analysis.
    }
    if (…) { // condition_branch_2
2
Dominator Constraints 2
        invoke_gadgetB(…)
o
The constraints that MUST be satisfied, as
    }
}  determined by static taint analysis.
Two types of constraints that categorized by JDD

`o` **For Candidate Constraints**

JDD would **_mutate_** the related fields during the exploration stage of fuzzing.

`o` **For Dominator Constraints**

JDD would use the **_constraints solver_** (e.g., Z3) to obtain its concrete value.

#BHAS @BlackHatEvents

## Slide 48

#### STEP 4: IOCD-enhanced Directed Fuzzing

##### v **<u>Injection Object Construct Diagram (IOCD)</u>**

<u>Definition</u>

`o` The data structure for describing the Injection Object

4

1
2
3 5

<u>Functionality</u>

`o` The Structure of Injection Object `o` The Constraints Info of specific fields of Injection Object

<u>Components</u>

`o` Class-Node 1 `o` Field-Node 2 3 `o` Directed-Edge

`o` Constraints Info (Candidate and Dominator Conditions) `o` Potential Exploitable Payloads Position

4

5

**Illustration of IOCD**

#BHAS @BlackHatEvents

## Slide 49

#### STEP5: IOCD-enhanced Directed Fuzzing

v **Workflow Overview of JDD's Directed Fuzzing**

**Workflow of JDD's Directed Fuzzing**

#BHAS @BlackHatEvents

## Slide 50

#### STEP5: IOCD-enhanced Directed Fuzzing

v **IOCD-based Seed (Injection Object) Generation**

1
2
3
5
4

**<u>1. Object Initialization</u>** : Initializing different types of parameter-less Java instance objects based on the _<u>Class-Node</u>_ . 1 **<u>2. Object Structure Recovery</u>** <u>: 1) Establish the class</u> hierarchy of these instances according to _<u>directed edges</u>_ <u>. 2) Set</u> 3 <u>.</u> the _<u>fields</u>_ related to attack _<u>payload construction</u>_

5

2

**<u>3. Dominator Constraints Configuration</u>** : Extract _<u>dominator</u>_

_<u>constraints</u>_ and invoke the constraint solver to generate 4 appropriate values, which are then assigned to the corresponding fields.

###### **Illustration of IOCD**

#BHAS @BlackHatEvents

## Slide 51

#### STEP5: IOCD-enhanced Directed Fuzzing

##### v **Dependency-aware Mutation**

###### **Mutation Strategy**

###### **<u>Runtime Feedback-based Mutation</u>**

- JDD collects **_runtime feedback (e.g., covered branches, thrown exceptions)_** and uses this information to set corresponding fields accordingly.

- **<u>Fixed Structure Mutation</u>**

- Based on IOCD, JDD **_fixes the structure of the Injection Object_** and only **_mutates fields that do not affect the overall structure_** .

- **<u>Field Dependency Mutation</u>**

- JDD considers the **_dependency relationships between fields_** to ensure that these dependencies are preserved during the mutation process

#BHAS @BlackHatEvents

## Slide 52

#### STEP5: IOCD-enhanced Directed Fuzzing

v **Sink Reachable and Exploitable Verification**

##### **Sink Reachable Verification**

`o` JDD **_instruments Sink methods_** such as `Runtime.exec` to help determining whether a Sink point has been reached.

##### **Sink Exploitable Verification**

- For regular Sinks (e.g., `Runtime.exec`), JDD **_directly injects malicious payloads into the relevant fields of the Injection Object_** .

- For reflection-based Sinks (e.g., Method.invoke), JDD continues to **_search for related Gadget Fragments and links them to the existing Gadget chain_** .

#BHAS @BlackHatEvents

## Slide 53

# Evaluation and New Findings

Open-source repos: https://github.com/fdu-sec/JDD <u>https://github.com/BofeiC/JDD-PocLearning</u>

#BHAS @BlackHatEvents

## Slide 54

##### Evaluation

###### **Effectiveness**

- ü JDD detects **91 unknown** gadget chains not detected by baselines

ü JDD reduces the static false positive rate from 91.5% to 0% on Benchmark.

**1362 (static detected)** à **116 (dynamic verified)**

#BHAS @BlackHatEvents

## Slide 55

##### Evaluation

JDD discovered **127 zero-day gadget chains** in six popular Java applications and notified affected developers to help them resolve the issues.

###### **The Detected Chains and Performance Evaluation Results of JDD on Real-World Java Apps.**

CVE-2023-29234 CVE-2023-35839 CVE-2023-39131 CVE-2023-48967 CVE-2024-23636 CVE-2023-41331 **Assigned CVEs**

#BHAS @BlackHatEvents

## Slide 56

##### New Findings - Gadget Chains

###### **Known Gadget Chain**

###### **Unknown Gadget Chain**

AnnotationInvocationHandler.readObject Proxy Map.entrySet ConversionHandler.invoke ConvertedClosure.invokeCustom Closure.call

ConcurrentHashMap.readObject GString.hashCode GString.toString GString.writeTo Closure.call

**_Expanding the range of protocols that can be attacked_** : the unknow gadget chain can be used to attack protocols that do not support dynamic proxy features, e.g. Hessian.

HashMap.put HashMap.putVal AbstractMap$SimpleEntry.equals java.util.AbstractMap.access$000 java.util.AbstractMap.eq XStringForFSB.equals QBindingEnumeration.toString ContextImpl.lookup

**_Can be used to attack a new protocol_** : the unknow gadget chain can be used to attack protocols outside the scope of JDD's predefined detection rules, e.g. Apache Fury.

#BHAS @BlackHatEvents

## Slide 57

##### New Findings - Gadget Chains

- **Case #1**

   - The exploitable gadget chain relies only on the JDK and a popular library (i.e., fastjson2).

   - Impacts many popular Java apps, e.g. Sofa, Solon…

**_However, it cannot be used to exploit Motan (fastjson is not introduced by default)_**

**Zero-day Exploitable Gadget Chains**

#BHAS @BlackHatEvents

## Slide 58

##### New Findings - Gadget Chains

- **Case #2**

   - An evolution of Case #1.

**We found that by replacing certain fragments 4a–7d in Case #1, we can generate new gadget chains to exploit other apps, e.g., Motan(weibo).**

**Zero-day Exploitable Gadget Chains**

#BHAS @BlackHatEvents

## Slide 59

Gadget fragments with high reuse value > **=> `Comparator.compare`**

**Known:** java.util.PriorityQueue: void readObject(java.io.ObjectInputStream) java.util.PriorityQueue: void heapify() java.util.PriorityQueue: void siftDown(int,java.lang.Object) java.util.PriorityQueue: void siftDownUsingComparator(int,java.lang.Object) java.util.Comparator: int compare(T o1, T o2)

**JDD discovered:** java.util.concurrent.ConcurrentHashMap: boolean equals(java.lang.Object) java.util.concurrent.ConcurrentSkipListMap: java.lang.Object get(java.lang.Object) java.util.concurrent.ConcurrentSkipListMap: java.lang.Object doGet(java.lang.Object) java...ConcurrentSkipListMap: int cpr(java.util.Comparator,...Object,...Object) java.util.Comparator: int compare(T o1, T o2)

#BHAS @BlackHatEvents

## Slide 60

Gadget fragments with high reuse value > **`Object.equals`(Can satisfy the hash collision condition) => `Object.equals`** org.springframework.aop.target.HotSwappableTargetSource: boolean equals(java.lang.Object) java.lang.Object: boolean equals(java.lang.Object)

java.util.AbstractMap$SimpleEntry: boolean equals(java.lang.Object) java.util.AbstractMap: boolean access$000(java.lang.Object,java.lang.Object) java.util.AbstractMap: boolean eq(java.lang.Object,java.lang.Object) java.lang.Object: boolean equals(java.lang.Object) java.util.AbstractMap$SimpleImmutableEntry: boolean equals(java.lang.Object) java.util.AbstractMap: boolean access$000(java.lang.Object,java.lang.Object) java.util.AbstractMap: boolean eq(java.lang.Object,java.lang.Object) java.lang.Object: boolean equals(java.lang.Object)

#BHAS @BlackHatEvents

## Slide 61

Gadget fragments with high reuse value > **=> `Object.toString`** com.sun.org.apache.xpath.internal.objects.XString: boolean equals(java.lang.Object) java.lang.Object: java.lang.String toString()

com.sun.org.apache.xpath.internal.objects.XStringForFSB: boolean equals(java.lang.Object) java.lang.Object: java.lang.String toString()

javax.sound.sampled.AudioFormat$Encoding: boolean equals(java.lang.Object) java.lang.Object: java.lang.String toString() javax.sound.sampled.AudioFileFormat$Type: boolean equals(java.lang.Object) java.lang.Object: java.lang.String toString()

javax.swing.UIDefaults$TextAndMnemonicHashMap: java.lang.Object get(java.lang.Object) java.lang.Object: java.lang.String toString()

#BHAS @BlackHatEvents

## Slide 62

Gadget fragments with high reuse value > **getter => Command/JNDI injection attack** E.g. Linked after unsafe reflection com.sun.corba.se.impl.activation.ServerManagerImpl: int[] getActiveServers() com.sun.corba.se.impl.activation.ServerTableEntry: boolean isValid() com.sun.corba.se.impl.activation.ServerTableEntry: void activate() java.lang.Runtime: java.lang.Process exec(java.lang.String) com.p6spy.engine.spy.P6DataSource: java.sql.Connection getConnection() com.p6spy.engine.spy.P6DataSource: void bindDataSource() javax.naming.InitialContext: java.lang.Object lookup(java.lang.String) com.zaxxer.hikari.hibernate.HikariConnectionProvider: java.sql.Connection getConnection() com.zaxxer.Hikari.HikariDataSource: java.sql.Connection getConnection() com.zaxxer.hikari.pool.HikariPool: HikariPool(com.zaxxer.Hikari.HikariConfig) com.zaxxer.hikari.pool.PoolBase: PoolBase(com.zaxxer.Hikari.HikariConfig) com.zaxxer.hikari.pool.PoolBase : void initializeDataSource() javax.naming.InitialContext: java.lang.Object lookup(java.lang.String)

#BHAS @BlackHatEvents

## Slide 63

# Conclusion & Takeaways

- We introduced a fragment-based summary and a bottom-up gadget chain search approach that effectively addresses the challenge of static path explosion.

- JDD uses a technical framework that leverages a lightweight static taint analysis engine to guide directed fuzzing, thereby enhancing precision and efficiency in vulnerability verification.

- We also shared several zero-day exploitable gadget chains and fragments.

#BHAS @BlackHatEvents
