---
title: "De-Virtualizing the Dragon - Automated Unpacking and Deobfuscation of Nested VM-Based Protectors"
speakers: ["Agostino 'Van1sh' Panico"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - De-Virtualizing the Dragon - Automated Unpacking and Deobfuscation of Nested VM-Based Protectors - Agostino 'Van1sh' Panico.eng.txt"
sha256: "1090b14c948b41d3956656b5ade554014a5dc47eaeaecce860e2560287045b71"
duration_seconds: 2318
words: 4001
text_chars: 23879
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# De-Virtualizing the Dragon - Automated Unpacking and Deobfuscation of Nested VM-Based Protectors

**Speakers:** Agostino 'Van1sh' Panico  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (38 min, 4,001 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Good afternoon DEF CON. I'm Agostino aka Vanish and I'm here to talk about slaying dragons. Not the mythical one so we are not talking about the orbit but we are talking about the one that got modern software through sophisticated virtualization based techniques. This is the agenda for the next 45 minutes. We are going to start with a brief introduction. We are going to see the VM protection evolution. I'm presenting the VM dragon slayer architecture and we do a deep dive. We do some live demos because it's cool. We do some, we analyze some performance and validation and we analyze the limitation, the future work and the community that I hope to build around the project after this talk. Let's set up the expectation. Why VM protection is winning the arm race? This is what we are going to analyze today. How VM dragon slayer, that is the framework that I'm presenting today, defeats this protection using hybrid analysis techniques.

We do some live demos as I said before and also after the talk the entire framework will be completely open source to everyone to use it. The talk is aimed for malware analyst, reverse engineer, instant response, instant responder, security researcher and frankly anyone who is tired of being defeated by obfuscated code or is trying to build better obfuscated code. So before we jump into the technical myth, let me introduce myself. I'm a security researcher with over 15 years in engineering. I'm the maintainer of the project that I'm presenting today. I'm also the maintainer of spider foot today, a fork of spider foot that is being revived. And the framework that is the framework for exploitation that I'm going to present tomorrow. My research focus is everything that's weaponizable. That's it. And when I'm not breaking things, I love scuba diving because I love the exploration. I'm also the owner, the proud owner of three cuts.

And while I'm speaking they are probably planning the world conquest. That's why they are looking at us. Now, how many of you have ever tried to reverse engineer software protected by VM protect for instance?


## [03:04]


Or encounter custom VM based malware that made you question your career choice? I know some of you have done, otherwise you would not be here doing this talk. We all have been there. Staring at the sample code that looks like it was written by an alien civilization having a particularly bad day. Let me show you what we are dealing with. This is what happens when a simple three line function gets the VM protect treatment. On the left, we have an elegant readable assembly. A basic function that any first year computer science student could understand. Three sections, easy. Load two values, add them, return the result. On the right, we have what I like to call the algorithmic nightmare fuel. Over 500 lines of deliberately obfuscated code that will make Lovecraft proud. This isn't just obfuscation. It's a complete architectural transformation. But there is what makes it truly nightmare-ish from a technical perspective.

Behind those 500 lines, we have a constraint satisfaction problem with over 1,200 pod constraints. More than 256 virtual registers. 64 custom VM handlers implementing a unique instruction set. Dynamic propagation across more than 47 execution pods. That's what we have. And if it was not enough, a symbolic execution, the challenge that will break traditional analysis engine. The original control flow, it's gone. It's been completely destroyed and it's been replaced by custom virtual machine. The data flow, hidden behind constraint satisfaction problems that require advanced symbolic reasoning. This isn't just a problem, an academic problem or something that affects a few security researchers. Let me share some statistics. We are living through an arm race that's fundamentally changing the landscape of software protection. I analyze almost 300, 400 samples over 2024 of advanced threat factors.

And the results are striking. 70 percent of them employ some form of virtualization-based protection. Think about the numbers for a moment. Seven out of ten advanced threats are using techniques that completely breaks our traditional analysis approach.


## [06:15]


The success rate of existing tools, less than 15 percent. This means that 85 percent of the time, your current tool chain is failing you. Manual analysis time has ballooned to two to six months per sample. And we are seeing over 200 thousand variation per day nowadays. The mathematics are unforgiving. We are losing this world through shared numbers. But let me trace the evolution that brought us to this special circle. Do you remember the good old days when you peaks was the hate of sophistication? These early protection protectors focused on compression and simple encryption. That's it. You could defeat most of them with generic or just setting the right break point. Life was simple back then. We didn't realize it, but it was simple. The typical analysis process was almost ritualistic. Set a break point. Run until you hit it. Fix the import. Celebrate with beer because you're done. And then in 2010, VM protect 1.6 came out and everything changed.

It was like going from child play to adult play to casino play. The introduction of 686 instructions were converted into custom VM byte codes. The protection wasn't just about adding code anymore. It was about a fundamental architecture transformation. But then we move on phase 3. It's like the MCU. We are going forward. And we got VM protect 3.X. We got VM. We got code visualizer. Those two raised the bar even higher. These weren't just protectors. They were more like code transformers engine. After that, we got to phase 4. We got to the next level. And perhaps the most concerning development is the proliferation nowadays of custom VM. We are no longer dealing with commercial protectors.


## [09:21]


That we can study. That we can analyze. We are dealing with malware family that now implement their own protection. APT groups deploy custom protection scheme that can be analyzed with commercial tool. So they fail us completely. I've seen nation state malware with VMs that will make commercial developer jealous. Honestly. To understand why this is such a critical problem, let's examine what makes VM protection so effective. I call it the three headed dragon. The original code isn't just hidden. It's completely transformed into a custom byte code. That exists nowhere else in the universe. That's frightening. We are dealing with custom instruction set that contain more than 200 opcodes with no documentation, no standards. We got polymorphic byte code generation, dynamic generation and context dependent semantics. Let me give you a concrete example. From VM protect. A simple instruction like the move is just one instruction representing one single memory load.

From one instruction we get 247 instruction in the protected binary. This means that we have a 247 to one ratio. The VM itself is designed as a fortress. These protectors deploy an anti-analysis arsenal with over 50 techniques. Debugging detection include is debugger present, that is the common one. Debug, flag monitor, debug point detection, time based detection and everything can be actually mapped to understand what's going on at the VM . And if the sample is running in a safe environment for them. We got dynamic countermeasure that includes self modification dispatcher, the changes you analyze them. Code flow integrity check and exception based control flow that require symbolic execution across exception handles. But even if you manage to identify individual VM instruction, understanding the overall program logic require mapping the VM internals to something that should be meaningful.


## [12:37]


There is where even experienced analysts just give up on a certain point. VM register don't correspond to CPU register. A VM may have more than 246 virtual registers versus the 16 that we have in the x86 architecture. Using custom segmentation scheme and VM specific implementation, that's a nightmare. That's the idea. So when we face this threat, what we do? We try to forge better weapon. And that's what I've done with VM Dragon Slayer. After years hiding these dragons with stone knives and bare skin, I decided that it was time to build a proper dragon slaying weapon. VM Dragon Slayer represents a fundamental shift in how we approach VM. The core innovation lies in the analysis approach. We use dynamic team tracking plus symbolic execution plus machine learning. And we got an automated VM defecation. Here are some key insights on how this works and why this works. VM must read byte codes.

That's our team source. VMs must dispatch the handler. And that's our control flow target. Handlers have semantic patterns. That's where symbolic analysis shines. Patterns are universal across protectors. And that's where machine learning does its job best. VM Dragon Slayer is built as a research framework, honestly. But it's built with enterprise in mind. So it has a modular architecture. Let me walk you through the system completely. We have a multi -platform plug-in suite supporting Ghidra. That is the one available today. We have the alpha release of IDA Pro. And we plan to do the same for Binary Ninja. This integrates with the REST API that is built on the server side. The core analysis engine includes the dynamic tracking using Intel pin. A symbolic execution with a Python implementation using Z3 and Angular. And a machine learning engine for pattern classification and confidence scoring.

We also got some ZPU acceleration support for CUDA and OpenCL. But it's in alpha release.


## [15:37]


And you can make it work, but it's not really stable. The system includes some benchmarking and validation. But also it's CICD compliant. Means that you can use the framework in your pipeline without any issue. Because it's just an API. Let's deep dive into some of those models. The DTT implementation is built on Intel pin. With a custom Python wrapper. Let me show you how this works. The pin configuration use the custom DLL that is available in the source code. We are not going to cover it in detail because we are needing more than an hour just to go over there. With 300 second timeout. We define 10 source as VM by 10 second timeout. And we have a white code section. Typically for VM protect, we go for 4010 to 4050 in the other. The point is this is the only input that you have to take. We have to put into the framework. It's the only input that you have to get. Because if you put it too wide, this is going to run forever.

Some features that we have in the DTT includes instruction level precision for memory reads. Automatic discovery via control flow analysis. Multithreaded propagation tracking. And real time confidence scoring. And this is just the DTT. This is how it works in practice. Everything is a library. So you can call the entire framework or you can call part of it. If you run it, you have just the output. And then the Python process it and produce the summary statistics. In this case for this sample, we have 47 VM discovered in 2.3 seconds. 2,847 instruction. 156 propagation chains identified. And we have a 100 percent accuracy rate for entry points. Our symbolic execution engine is completely implemented in Python supporting Z3. The configuration uses symbolic execution with a maximum depth of 100. Up to 1,000 concurrent paths. We have a timeout of 300 seconds. And the state merging is usually enabled.

But you can disable it. It's just from configuration perspective. VM context modeling include program counter tracking. Symbolic values for registry and memory. And machine learning guided path prioritization.


## [18:40]


Path exploration because you can explore the binary that you have. Use machine learning guidance. With VM pattern weights, priority scoring for an intelligent exploration. Let me show you how it's implemented. The symbolic execution is implemented. The core class initialized with a path prioritizer. Execution queue management and configuration from the VM configuration. The main execution loop runs asynchronously. So it means that it just runs without you needing to pull it. Processing the execution queue. For each context, we get the highest priority path. Execute one symbolic step. And process result by adding terminal states to completed path and non-terminal states back to the queue. The path prioritizer use machine learning guided path exploration with VM pattern weights. We define the dispatcher access with a weight of 2.5. The handler entry gets a 2. The VM registry access gets a 1.8.

The byte code fetch gets a 2.2. And the anti-analysis checks gets a 3. Our pattern classifier implements a multi-method approach with automatic method selection. The system supports rule-based classification, similarity matching, machine learning classification, and hybrid approach. The auto-classification logic tries rule-based first because it's fastest. If confidence of the rule base is below 0.8, it tries similarity matching. If that's below 0.7, it falls back to machine learning exploratory mode. The pattern database user is back to SQLite. The full pattern that had been added to the platform are, for instance, VM add stack, VM conditional branch, and so on. But that's just part of the framework. We also have the Guider plugin. Let's have a quick view of the Guider plugin. The Guider plugin just shows how you can interact with the framework. So you can define which kind of engine you want to use, which kind of confidence you can set from the framework.

You can get the result view. So you have all the path, all the VM discovered, all the path, everything. And you have statistics over the engines that are running.


## [21:47]


But let's begin the hunt. Let's see how it works. Let's start with a real VM protect 3.6 sample. This is a commercial license validation function that contained initially 47 instructions. After VM protect, it became 2,847 instructions. A 60 to 1 ratio. Protection feature includes virtual machine byte code, anti debugging and so on. The manual analysis estimated for this sample is from three to four weeks. As you can see, the VM layer initialized the dynamic team tracking and launched the Intel pin with our custom DLL. Within seconds it detects the VM entry point with high confidence. The ender table is discovered and contains 51 entries. The symbolic execution phase starts from there. And ender analysis complete with 47 ender discovered and 43 analyzed. We have a roughly 90 percent success rate. The semantic operation discovered include VM load license, string compare, conditional jump and return value.

And everything is done in roughly three minutes. The transformation that comes from this process is actually pretty dramatic. The version shows thousands online of unreadable assembly. The version reveals the true algorithm. Load license key, decrypt XOR using the key, compare with the expected value and jump if invalid, return success. Clear algorithm after the process. Just three weeks reduced to three minutes plus the analyst enrichment time. That's it. Let's analyze the second sample. It targets a real world bank in Trojan from an instant response case. This sample used completely custom VM architecture and three teams completely failed to analyze it over six months. VM layer in exploratory mode handles also unknown architecture. Automatically if it doesn't find any signature it goes. The custom VM implementation is discovered with a 64 entry ender table using ash base dispatch.


## [24:56]


It's 4K of XOR encrypted content and VM context 256 bytes and roughly 60 bit opcodes. Everything is being done in roughly 18 minutes. But there is more. The actual framework automatically identifies VM operation and their purpose. This is part of the report that the framework gave you. We have VM load URL that loads the URL from an encrypted config. We have VM hook browser that install browser API hooks using set windows hook X and plus DLL injection. We have VM capture creds that extract credentials from browser, chrome, firefox and ash in this case. And we have VM custom crypto that implements a custom CRC 32 variant that it was never seen before. So it was a good attribution part, technical attribution IOC. The intelligence value from this report is actually immense. The complete behavior profile extracted automatically. The attribution markers in custom crypto algorithm and we have the TTP that can be easily mapped to the attack framework.

Everything being done in less than 20 minutes. Plus the time that the analyst needs to read the report and then reach it. But now let's see some more dynamic demo. Let me show you what happened if we load multiple samples to the platform and how we handle it. In this case we have three samples that are loaded through API. Those three samples are VM protect base and the custom VM. We have the first one that is actually analyzed in almost three minutes. And we get the actual handler number and the handler type. Then we have the second sample that is the one.


## [27:59]


It's a little bit more difficult to analyze. So we got some details from it. And some of those details are also regarding the handler and all the address of the handler and how it has been used. So we have DTT, a symbolic execution. Everything is guided through machine learning. The third sample is just custom VM. So we don't have anything. We don't have documentation. We don't have standards. And also in this case we got some handlers to lift the sample and try to decrypt it. And try to deobfuscate it. But let's see how it works from a statistical perspective. We have performed a complete evaluation and we use roughly 300 samples over 12 months. Those 300 samples were de-obfuscated and then we divided between 15 protected families and almost 50 malware families. Among those we have 25 nested samples. It means VM inside the VM. And this is the success rate of the platform. So we got from roughly 60 percent of manual success rate for VM protect 2.X to 84.

And we got an overall 70 percent of success rate from different families. But that's not the point. The real improvement comes from the time. Because we went from two to six months in analyst time to roughly one hour. That's the key point. So we are saving analyst time. In this way the analyst can focus on something that is truly important for the organization. For instance, for example, we went from roughly $40,000 of analyst time to 50. That's a huge drawing. Let's see some case study in which we used VM Dragon Slayer. The case study involves a financial institution facing a bank in Troia. The sample used custom VM plus VM protect 3.6. The traditional analysis took over three months. Showed complete failure. We have a partial analysis using IDA pro and x-ray the compiler failed completely. We required six senior reverse engineers on the case.


## [31:03]


Means roughly $200,000 in analyst time. For four months. The VM Dragon Slayer took the sample and the results after three hours of analysis were 73 VM endless, 91 percent of endless classification. We identified seven novel evasion methods and provided full integration with a documented binary. Total cost, $150 roughly. Plus the computational resource. The technical breakthrough of this implementation includes the finding of a novel browser certificate bypass never been documented before. A polymorphic VM handler with a four hour mutation cycle. And a complete attack chain reconstruction for defensive development. That's the second case study. In which we analyze a batch of state sponsor generated malware that contain almost 47 implants. Developed all with VM protection technology. Traditional approach will require six analysts, mostly, 12 to 18 months to analyze everything. Means almost $1 million in analyst time.

We take it in one weekend. So we batch it, we give them to the platform and in 48 hours we go back to the platform and we analyze the data . And we got 70 percent success rate across all the samples. The intelligence breakthrough of this analysis include infrastructure, the campaign infrastructure completely mapped. The code reuse pattern we find across the samples. And also, and this is important, the development timeline was reconstructed from VM evolution over time. Because we see how they change over time, the implementation of the VM. And this is actually a unique IOC for the specific architecture. But the platform is good. I developed it so I can say that. But it's imperfect. We have a 30 percent failure rate across challenge scenario. We have complex control flow that accounts for roughly 13 percent of failure. In some cases it's really because the sample is too complex or is too unneeded.


## [34:10]


And other things that cause failure is actually the resource constraint. Because sometimes we have individual ender that exceeding 10,000 instruction. Deeply nested obfuscation with more than five layer obfuscation. In those cases it's really difficult to have the resource to handle this kind of computational capability. That's why we are moving over the GPU acceleration part. But also some novel techniques produce some failure. And including a generated or quantum resistant technology that can generate some failure in the analysis process. But what's the future? The first thing that I would like to develop from year to the end of the year and I hope that someone will join me. It's a machine learning advancement. That includes transformer based classification, anomaly detection for techniques using unsupervised learning. Probably the idea is with three sigma deviation threshold. Transfer learning for cross protectors that require this knowledge, this knowledge I hope is going to require 70 percent less training data.

The other thing that I want to develop, it's an enhancement of the plugin to be more integrated with the platform. In which we have a real time ender notation that is not there now, you need to do it manually unfortunately. Automated function naming based on semantic analysis. And detailed commenting with confidence score. But even a cooler feature. The cooler feature is binary rewriting. So you took the binary and you rewrite it in clean code. That's the idea. I think it's doable. I didn't have a lot of success with it I have to be honest. But I think it's doable in an automated way. In which we provide a complete pipeline with full VM structure discovery and semantic analytics, control for reconstruction and clean code generation. So to conclude, to wrap up what we have seen today, the VM protection actually dominates the modern malware. We have a lot of modern malware that use that. Manual analysis cannot scale.


## [37:14]


That's why we need automation. And it's not just possible, it's needed. It's essential. Hybrid approach works if you choose the right tool to do the right thing. Not like LLM, you use LLM for everything. Open source I hope is going to accelerate the process. Having more research on board that can help develop this kind of technology. Because the defender advantage is achievable. If you have the right tool, if you have the right techniques and if you have the right community behind it. VM Dragon Slayer is going to be available on github after the talk. Just the time to go back to the hotel. Add this address. It's going to be available on github . This is open source because I firmly believe in democratizing these capabilities. And just remember, every dragon can be slayed with the right sword. And the right community welding it together. Thank you for your time. I hope you enjoyed the talk.

I'm going to stick around if you want to ask some questions. So I'll be around. Thank you.
