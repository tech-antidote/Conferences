---
title: "Client or Server- The Hidden Sword of Damocles in Kafka"
speakers: ["Ji'an 'azraelxuemo' Zhou", "Ying Zhu", "ZiYang 'lz2y' Li"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Client or Server- The Hidden Sword of Damocles in Kafka - Ji'an 'azraelxuemo' Zhou, Ying Zhu, ZiYang 'lz2y' Li.eng.txt"
sha256: "069202ff871e7c8b78182a2d83c31fad392da7f6722e90f1489a9b78e9f4189a"
duration_seconds: 2039
words: 4073
text_chars: 23801
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Client or Server- The Hidden Sword of Damocles in Kafka

**Speakers:** Ji'an 'azraelxuemo' Zhou, Ying Zhu, ZiYang 'lz2y' Li  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (33 min, 4,073 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Hello everyone, thanks for coming. I am very honored to be here to give a presentation. So today, our topic is... First of all, let me introduce my team. We are security engineers from Alibaba County, and I am Ziyang Lin. Then, let me introduce the agenda. First, I will introduce something about Kafka. Then, we will compare previous research with our new findings. Next, we will discuss the journey of hunting bugs in Kafka Ecology. After that, we will uncover the hidden vulnerabilities in Kafka broker. And finally, explore the insights and differences. Okay, let's officially begin our presentation. So, what is Kafka? According to the official documentation, Apache Kafka is an open-source distributed event streaming platform widely adapted by the enterprises for building high performance data pipelines, real-time analysis, data integration systems, and critical application architectures. At its core, Kafka has three main parts, producers, consumers, and the Kafka cluster.

Consumers are like the data sources. They send messages into the system. Consumers read those messages and add on them, like analyzing or storing data. And the Kafka cluster is a backbone. It handles messages, storage, reputations, and ensures everything runs smoothly at scale. Inside the Kafka cluster, the functions are stripped into two main parts, the data prime and the control prime. The control prime is in charge of chain managing all the metadata, like topics, brokers, and reputations. Meanwhile, the data prime is where the real action happens. It's handled by the brokers, which are responsible for reading from and writing to Kafka topics. In the control prime of Kafka, there are two different implementations of the kiss-and-save protocol. The older one, based on Kafka, and the newer one, known as kraft-control. As for the data prime, current requests fall into two categories, producer requests and flash requests.

A producer request is used to write a data to a specific topic. A flash request, on the other hand, is used to write data from Kafka topics. These operations are all limited with the topic, making it the central component in Kafka's architecture. In addition, Kafka has a powerful ecology. The Kafka ecology is built around several core components.


## [03:03]


Kafka core, Kafka systems, Kafka connect, rest procedure, schema registry, and case code. So, are there any security risks? That's a good question. Let's now look at the known findings and see how certain protections might be bypassed in repetition. There is a remote code execution ability in Kafka clients, identified at CVE-2023-25194, which can be supported in components such as Red and Kafka Connect. The key issue is that if an attacker can control the connection string used to connect to Kafka, they might be able to trigger gmdata injection, and that will lead all the way to remote code execution. Here is the proof of concept. The program acts as a Kafka client and uses an attacker-controlled connection string to connect the Kafka server. The payload contains an LDAP which is the key component in this export. As the program ends, it ends up triggering a gmdata lookup. Here on the right, you can clearly see the code stack leading to the injection point.

This is the cover of the vulnerability. Let's focus on the context logging process. It's essential to understand how the export works. It will initialize, subject, and construct gmdl logging model and analyze with subject, callback handler options, and finally, we'll call the logging method. gmdl logging model logging calls the attempt authentication method. Then the lookup method of the initial method is called. Before we move on to the next slide, I would like to briefly introduce the lookup method here. It's a common thing like runtime.exec, and it will look up an untransitive address and leads to RCE. You can use a diagram to show how the attack process. First, the attacker set up an evil gmdl server. Second, the attacker constructs the evil connection stream and passes it to the Kafka client. Third, the Kafka client passes the connection stream, constructs the evil logging config, passes it to the logging context, and calls the logging method of the logging context.

Then, the logging context analyzes the gmdl logging model to authenticate the user.


## [06:09]


Next, the gmdl logging model loads our evil gmdl server, and the server returns something evil payload. Finally, the server is taken over. The key point is the controllable logging config. Kafka client allows the users to control the logging config, so the user can use an evil logging config to achieve RCE. In version 3.4.1, the rector introduces a backlist mechanism, and by default, it includes the gmdl logging module. In other words, the gmdl logging module is disabled out of the box. If we run the poke again, we will see the program now slower and exception. The error message clearly says that the gmdl logging module is not allowed. We can use a diagram to show how the patch was. When the attacker constructs evil connection stream and passes it to the Kafka client, the Kafka client will check the logging config. If the logging config contains an evil logging module, memory-level gmdl logging module, the Kafka client will raise an exception.

And can we bypass? After understanding both the vulnerability and how the patch was, we came up with an idea. What if we find another logging module that can be abused in the similar way? If we can identify a new malicious logging module, such as some much-liked gmdl logging module, we might be able to achieve RCE once again. So, what are the registrations on the logging modules that we are looking for? First, improvement logging module. Second, it exists in popular javalibs. Third, can trigger RCE attribute flywrite, attribute flyread. Thanks to this idea, we found several interesting logging modules. The first one is a proxy logging module provided by JBoss. As the name suggests, it delegates an authentication request to another agent or module. Specifically, in its analyze method, it constructs an agent based on the specified logging module name and then analyzes it. During the logging phase, the proxy logging module passes the authentication process to the agent.

Now, you might have already guessed where I am going with this. Yes, we can use proxy logging module to bypass the backlist.


## [09:13]


Here is the prologue. We configure the proxy logging module and set its logging name to gmdl logging method. Even though it is on the backlist, when we run the prologue, you can see that the logging method of a gmdl logging module is actually invoked. If we check the EVO gmdl server, we can find that we have bypassed the backlist and achieved RCE again. Here is how the bypass was. Proxy logging module delegates to gmdl logging module, allowing us to bypass the backlist and tickle gmdl injection, leading to RCE. Another interesting state of logging modules is provided by WebSphere. Due to time constraints, I won't go into full details, but here is the proof of concept. Imagine a web server deployed on WebSphere that allows users to control Kafka connection stream. Could we take over? Of course we can. The idea is simple. We prepare a consumer login configuration file. Then we send the first payload to instruct the web server to use our login config.

After that, we send a second payload, which will trigger an error. As a result, the server writes the error message now containing malicious content to the file we specified. Finally, we will get a web shell and achieve RCE again. In addition, there's an interesting logging module named the LDAP logging module. It's built into the JDK. This logging method calls a timer authentication method. When authenticating the user, the logging module will first obtain name and password via a callback handler. Then it will check whether the password is blank. If not blank, it will initialize the GMDI LDAP logged context, which is a trigger GMDI injection. Briefly, if we can find a callback handler that can provide a password, we can trigger GMDI injection and achieve RCE. So our goal is to find a callback handler for the LDAP logging module. There are three registrations on the callback handlers that we are looking for.

First, you should be able to handle name callback and password callback.


## [12:15]


Otherwise, you will receive unsupportive callback exception. Second, you should be able to obtain a password which is not blank. Most importantly, it should be in permanent authenticated callback handler, which is an interface provided by Kafka. Otherwise, you will receive a cluster exception. To be honest, it is really hard to share all three requirements at the same time, especially the last one, which greatly limited the range. So which vendors implement the interfaces of Kafka? After some registration, we found that Confluent is a great candidate. Confluent is the creators of Kafka and the custodians of Kafka. And Confluent has their released versions. Confluent primarily offers two versions, the community versions of Kafka, known as cp-kafka, and the commercial version called cp-server. As shown here, the availability exists in cp-server but not in cp-kafka. We tested this on November 2024 on version 7.7.1 and it was confirmed to be support flow.

These issues have been fixed in the newer versions. We discovered a callback handler named filebase-dynamic-blank-callback-handler in Confluent Kafka, which reads the username and password from the local file. Here is a simplified code of a file callback handler. We can control the file name, the keys of name, and password. For example, if there is a file named user.conf, the file contains one or more username, password, pairs, separative, private, and password. This callback handler means almost a resistance. But the file named user.conf is created by us. Can we find one more common one? Of course, the etc password file fits our needs perfectly. This means we no longer need to upload a consumer user.conf. We just need to set the file name to etc password and keep to m the existing user.


## [15:17]


For example, root. Here is the poke. In the end, we can use this callback handler to trigger jmdi injection and achieve RCE. As shown in the diagram, it shows how the entire attack processed. In the third step, we can use the file-based dynamic blanker callback handler to bypass the login config track. And this callback handler will obtain the username and password to the LDAP login module. And finally, the LDAP login module will recover an evil jmdi server and finally will be taken over. As you can see on this slide, we are now entering a new phase of our research. Not just exploiting a single vulnerability, but hunting for bugs around the entire Kafka ecologic. In the previous chapter, we successfully triggered the jmdi injection in the Kafka client of the conventional version of Kafka. Can this be implemented in the real system as CVE-2023-25194? Let's take it step by step. First, can Kafka Connect be exported?

After our testing, the answer is yes, it can be exported. We can follow the official Confluent Kafka documentation to install and set up a Confluent platform. This proof-of-concept is exploitable CVE-2023-25194, operative in Apache Kafka Connect. This is our new plug from Confluent Kafka Connect. We just need to convert it into appropriate format and then we replace it with the previously mentioned bypass payload. And you will finally trigger jmdi injection and achieve RCE again. Something else? Yes, let's start a journey to take over Confluent ksqlDB server. When we deploy the Confluent platform, there are many components. In the website, we can see three of those components. When I try to use it, I find the ksqlDB is something like DBMS.


## [18:19]


Since DBMS also has a lot of features, just choose this to analyze. And then I read documents to learn about this. And when I read the documents, I find an interesting issue in the GitHub. It says the producer is closed firstly. Wait a moment, why does the producer exist here? And I just try to try it out in our local environment. We can see the producer configured in logs. What does this mean? Through the insert operation, ksqlDB can produce data. Can we modify the producer config? We can see that the configuration is obtained from the session config. So what is the session config? Since there is no other place to set here, let's try, let's give a simple try. Unexpectedly, we successfully modified the configuration. And then we modify it to use our POC. And we finally achieve an answer each year. Let's watch the video demo. Okay, let's do a brief summary. Using the bypass technology, we successfully bypass confluent Kafka broker and achieve RCE on ksqlDB.

We have taken over the confluent products of multiple cloud vendors. So if we can, we can attack, control Kafka client's configuration, and using the bypass tactics, we can achieve RCE. So next, let's uncover hidden vulnerabilities in Kafka broker. And in previous section, we already have a basic understanding of the Kafka ecosystem. And it is clear that the Kafka broker is the core component of the Kafka ecosystem.


## [21:19]


And also, prior to this, Kafka broker had no RCE vulnerability. And so if someone can find a vulnerability in such a critical and unbreakable system, and it is definitely something worth celebrating. And so you may be curious about how I found this vulnerability. And to be honest, just by accident. So initially, I didn't ever think that I could achieve RCE in Kafka broker. And as mentioned earlier, I was actually focusing on finding other issues or potential bypass method in the Kafka client. And at that time, I was reading the official document, looking for some suspicious configuration. And when I read the document, I found a very interesting feature, and that is the listeners can be added or removed dynamically. And also, what's more, the JS configuration of the listener can also be set dynamically. So this means that the Kafka broker also supports JS. And here, let's take some time to introduce this interesting feature.

So first, this is a very normal request. And the user just sends an add listener request to the Kafka broker, and the broker receives the request and adds a new listener. And after that, the other Kafka client can connect to this new listener for producing or consuming message. But if there is a hacker, and he can just send an evil request, and the broker will receive the add listener request and try to add a new listener. However, the server will also trigger the JS process, and will send the gender request to the evil gender server, and finally achieve RSE. So first, let's set up the exploit environment. And we can download the binary from the official website, and then run below command to start the Kafka server. And now, let's explore it step by step. So first, we can use the Kafka config tool to retrieve the broker's configuration. As you can see here, there are a lot of configurations.

And here, we should pay special attention to the broker ID. And here it is one. And here, we only need to focus on the configurations related to listener. So we use grab command, and you can see that now it has two ports. The one is the standard 9092 port, and the protocol is blantest. And the other is managed by craft, and called controller listener. And the port is 9093. And then, we can use nested command to check the locally listener ports, and confirm the existence of these two ports. And so now, we will try to add a new listener, and we just copy the previous configuration, and add a new listener. Listen on the 9094 port. And as you can see that after we send this request, and the Kafka server will receive the request, and update its configuration.


## [24:24]


And we can use the nested command to check the newly added ports. And you may have noticed that the newly added listener configuration is SASL blantest. So what is that? And it is essentially the communication protocol for brokers. And there are different types, such as blantest, and it is encrypted, and SASL, and it is authenticate, and also SASL. SASL is the encrypted protocol. But in fact, after we execute the command to add a new listener, essentially when we specify the new listener, use the SASL protocol, and it will throw an exception on the broker side. And if we look carefully, the error message, we can see that it indicates that exists the absence of JAS related configuration. And this is because that Kafka's authentication mechanism is based on JAS. And therefore, when we add listeners that requires authentication, and the system will look for corresponding JAS configuration. And if we properly configure and we can trigger the JAS process and finally achieve RCE.

But the question is, how can we set the evil JAS configuration? And after reviewing the Kafka document again, and I just found the answer. We can configure it through the configuration key, and you can see the key is listener name, listener name, and .saslmechanism.sasl.js.config. And so now, we need to set the corresponding configuration. And since by default, the SASL mechanism is JASS API, so we can name it in this way, listener.name.sasl.planetize, this is our listener name, and .gssapi, this is our SASL mechanism, and .sas.js.config. And so we re-succeed in one shoot. But it didn't work, and it's through a new exception. But not bad, since we at least successfully configured our JAS. But set not equal solution and code equal clues, and I just reviewed the code, and you can see that this is our error message. And so here, you can see we need to set either the JSS server name or the config service name.

And here, I choose to set this config service name, and you can see that it get from our configuration, SASL Kerberos service name. So here, we need to add this parameter. So now, you can see that we just added this configuration key, and we can add a test. And finally, you can see that we receive the LDAP request. So yeah, we finally made it. And there exists another solution. So we can simply change our SASL mechanism to plan and don't forget to modify the name.


## [27:26]


And we can also receive the LDAP request. And since now, we can just utilize the server, send the GNDI request, and the only thing we need to do is deploying an evil GNDI server, and then waiting for the shell. So now, I have discovered the first-ever RCE vulnerability in CapCapBroker, and no one has thought of it in this way. And if you look carefully, and we just exploit it in our old version of CapCap. And so, at that time, I just wondered that this exploit also works in the latest version. And then, I just choose to exploit in the version 3.4.0, and the exact version fits the CVE-2023 and 25194. And but when I try to exploit, and but unfortunately, it just threw an exception, and just the same exception as the CapCap plan. And I was very confused. I don't know why the patch method related to the CapCap plan also affects CapCap server. And I reviewed the source code, and finally, I got the answer.

And the reason is that you can say the CapCap plan uses the loadClientContext function to load the GIS configuration. And it will finally call the load function, which specifies we are client. And however, our CapCap server will also use the loadServerContext function, it will also call the load function in the end, and it will specify our type is server. But our CapCap patch method is adding a restriction in the load function. So this means that it will influence both the server side and the client side. So CapCap just accidentally fixed a crucial unknown server side vulnerability. So what the hell? But since the fixed way is the same as the client, and if you remember in the previous section, and we have a bypass method in the Confluent version. And so this means that we can bypass and achieve RSA in the latest version of Confluent CapCap broker. And so first, we also need to set up the environment and just follow the guide.

And now we need to add a port mapping to help with our testing. And then we can use the CapCapConfig tool to quickly verify if our server runs normally. And here, we first just want to test with our previous code, just want to verify whether the CapCap, the Confluent broker has patched the vulnerability. And we started by fetching the current listener configuration, and this is now slightly different with the previous one, and then slightly modify the port. But however, it shows an exception, indicating the absence of the security protocol not defined. And I just find the reason, and the reason is that we missed this configuration. And you can see that the security protocol of each listeners must be defined in this configuration. And in our previous CapCap broker vulnerability, and since by default, it has already defined this map, and you can see it has the SASL plan test.


## [30:37]


So now, we will not encounter this error. But however, here, this is our now map, and you can see it only has controller, plan test, plan test holds, don't have the SASL plan test. So this is why we failed. So we need to add this parameter. And now you can see that we just modified the listener security protocol map, and we add this mapping. And now we can use the listeners SASL plan test. You can see that yes, and we just trigger the patch logic. So now, we need to just bypass it using our previous method. And just looking back at our previous method, and you can see that the key of the bypass method is the SASL.login.callback.handle.class parameter. But now, here is the question, how can we set the callback handler on the broker side? So after reviewing the official document again, and I discovered that it can also be configured dynamically. And the format of the key is similar to the key format used by the listener, and called listener.name.listener.name, listener .SASL.login.callback.handle.class.

And now, we can just add in the callback handler, and the name is listener.name.SASL.plan test.plan.SASL.login.callback.handle.class. And we modify the JS configuration to our previous bypass method. And finally, we can also receive the GenDI request. So this means we successfully bypassed it. And now, here comes to the video. And so first, we can run our Evo GenDI server, and we get the listener's configuration, and we can run our... first we start the listening port, waiting for the share, and we run our exploit payload, and update the configuration, update configuration, and finally, we receive the share. And you can see that we are inside our container, and this is the Confluent Kafka broker. So after that, we promptly reported our findings to the Kafka official team, and finally, Kafka has acknowledged this vulnerability, and this is the first-ever RCE vulnerability affecting Kafka broker.

And we also reported this vulnerability to Confluent, and we were rewarded the highest-ever bug bounty in Confluent. And also, here is the patch, and it is very easy to understand, and it just disabled GenDI login module and LDAP login module by default. And finally, it's some defense recommendation. So first, if you still use the affected version of Kafka, please update now. And then, authentication and authorization must be enabled to prevent unauthorized sites.


## [33:43]


And what's more, the components in the Kafka ecosystem are very important, and usually don't need to be exposed to public internet, and therefore, it is best not to expose them publicly. So, are there any questions? And thanks again for your listening, and if you have any questions, please feel free to contact us.
