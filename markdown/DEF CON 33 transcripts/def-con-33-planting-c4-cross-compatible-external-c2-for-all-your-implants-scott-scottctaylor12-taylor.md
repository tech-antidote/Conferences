---
title: "Planting C4 - Cross-Compatible External C2 for All Your Implants"
speakers: ["Scott 'ScottCTaylor12' Taylor"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Planting C4 - Cross-Compatible External C2 for All Your Implants - Scott 'ScottCTaylor12' Taylor.eng.txt"
sha256: "ae96b6449b448b3c31ab7b50da8335a17b78d25f79097db3c1907b8348e60b45"
duration_seconds: 977
words: 2620
text_chars: 14700
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Planting C4 - Cross-Compatible External C2 for All Your Implants

**Speakers:** Scott 'ScottCTaylor12' Taylor  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (16 min, 2,620 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:04]


All right. Thank you so much for coming to my talk, everyone. Not only am I a first-time speaker, but it's also my first time attending DEF CON. So I'm really excited to be... yeah, that's right. Thank you. Yeah. So I'm excited to be here and give you my talk, C4. As a quick disclaimer, this is given on my personal behalf and does not reflect my current employer, Sony Corporation. All right. So like I said, I'm Scott Taylor, and I'm part of Sony's internal red team. Prior to Sony, I've done red team work with T. Rowe Price and the MITRE Corporation. But before all of the offensive security work, I started as a Linux system administrator, because you have to learn how to build before you break things. Additionally, I have a couple of certs and degrees. So for today, I'm going to be talking about a tool that I wrote called C4, the cross-compatible command and control. And this tool heavily relies on the commonly known technique in the red team world called external C2 or external command and control .

So in your typical red team operation, as usual, you're going to drop malware onto the blue team's monitor computers, and that malware is going to reach out to your red team command and control server. Now, some of the more advanced teams, instead of directly communicating from your malware to the team server, you're going to instead use a trusted third party website to perform your message communication. So there's been instances of using like GitHub and AWS, various trusted websites that typical users in your enterprise are going to browse to. But instead, as offensive security folks, we are going to send our malicious messages through these same trusted websites. So earlier this year, there was a really cool project that was released called the LOLC2 or living off the land C2. And this documented numerous websites that were compatible with external C2. So security researchers managed to figure out how to do this communication over very popular websites like Microsoft OneDrive, Google Calendar, and even some fun ones like over a counter strike server.

So security researchers are certainly using this in the wild and doing a lot of creative research in this space, but also threat actors or the bad guys are also getting in on this. So as you can see, I have a screen shot of the MITRE attack framework, because of course, as a former MITRE employee, I have to rep the attack framework. And you see there's a couple of examples like Google Drive, Dropbox, and all these trusted websites being used in the wild. Now one thing to note is in this attack framework, this technique was actually added all the way back in 2017. So it's certainly not a new development in the red team space.


## [03:05]


So you might be wondering, well, why are you coming to DEF CON and talking about it? Well, I started thinking about external C2, and I was like, well, there's all these C2 frameworks out there, but when you actually start using them, there's only a handful of external C2 options available for each one. So in Cobblestrike, you see a couple of the interesting C2 profiles. Personally, I'm a mythic C2 person, and there's a handful there, but in the previous screen shot, you saw loads of examples. So, you know, I started looking at it, and I'm like, well, yeah, it's challenging to take some of these really custom C2 profiles that are specific to a framework and port it to other frameworks. So today I'm going to talk about my tool C4, and how I aim to tackle this issue of portability of external C2. So, like I mentioned, I'm a mythic C2 fan, and with this framework, it's quite simple to develop your C2 profiles.

Mythic deploys in multiple docker containers, and the actual C2 portion of the framework runs in its own docker container. So what I did was I developed the server side in Python, and this is published on GitHub, and not, you know, granted I'm exploiting GitHub, but in this case, it's actually published on GitHub. And on the client side, this is where mythic is a little bit more unique. Commonly in C2 frameworks, you have one agent for one C2 framework, so you might have, for example, beacon for Cobalt Strike. In mythic, there's multiple agents that exist. So for myself, I decided to develop this for the Athena agent, which is an agent run by check commander, and this agent is written in the dot net framework. So with dot net, I was able to find a dot net library out there to very easily interact with GitHub, and this is quite specific developed for this agent. Now, the cool thing is, yeah, this worked great.

I was able to do my, you know, GitHub C2 using the Athena agent in the mythic C2 framework, but some of the other agent developers for this framework were like, well, I want to get in on the fun, but it's a little more challenging to take what I developed in dot net and port it to all these other languages . You know, all you malware developers out there, I'm sure you all have your preferred languages that you like to write in. You know, even in this case, I have a table of all the different agents, just some of them. There are more than this. And, you know, it ranges from all over the place. There's even like a JavaScript agent that acts as a malicious Visual Studio code extension. So, really cool stuff, but again, I wanted to find a way to take these external C2 profiles that I'm developing and make it more accessible for malware developers regardless of language of choice.


## [06:08]


So, this started my security research endeavor and I ended up stumbling upon WebAssembly. So, for WebAssembly, I went into this thinking, well, this is more of like a browser technology thing. And, you know, this is partly true. For WebAssembly, this is a compiled format, so you end up with a bunch of dot WASM files. And these WASM files, or WASM modules, I should say, they run at near native speed. So, for web developers, they love it. For example, the folks that develop Photoshop took that really intensive program, compiled it down to a WebAssembly module, loaded it in the browser, and now you can do Photoshop in the browser. So, really cool advancements. But the problem is, for WebAssembly, you know, this instance, this is all in the browser. But us red team operators, we're on the operating system. So, I needed to figure out how I could take all this really cool WebAssembly stuff and end up using it on the real host that we're trying to hack into.

Now, for WebAssembly, again, popular in the web browser, however, there are WASM, or WebAssembly run times, outside of the browser. And further down the rabbit hole, this led me to discovering WASI, the WebAssembly system interface. Now, this is exactly what I was looking for, because this allows your WebAssembly modules to actually interact directly with the operating system. This is the bridge for the WebAssembly modules to your computer. So, with WASI enabled, you're able to interact with the file system, so you can read, write, delete files, you can read the system time, and you can interact with sockets. So, you can start making network requests. So, for what I was trying to do, this is looking very promising. And WASI also advertises that it works in all kinds of places. So, you can run WebAssembly modules in the cloud, server side apps, embedded system developers really like this stuff, but what I was really interested in is the fact that it was advertised as a plug-in system.

So, for myself, because I wanted to develop external C2 plug-ins, this was looking really promising. So, this all sounds great in theory, but I needed to find an actual project that I could take and really make this happen, take the theory to the practical. So, this led me to discovering a project called Xtism, which is developed by Delipso. And aside from this wicked cool logo, it advertised exactly what I was looking for, a universal WebAssembly plug-in system. It supports multiple languages, so that's exactly what I was shooting for, and there's the idea of a plug-in kit and a host kit. For plug-ins, you can write your plug-ins in multiple different languages, compile it down to WebAssembly, and then take that WebAssembly module and run it in multiple languages.


## [09:11]


So, very, very ideal. Additionally, the WebAssembly runtime that Xtism produces has a couple of nice features, such as persistent memory, host-based control, so you can specify what HTTP endpoints your WebModules can reach out to, and a couple of execution guard rails , which helps keep the WebAssembly module secure. Here's a high-level overview of what this development pipeline looks like. So, for myself, I developed my plug-ins in Rust, and Rust can sometimes scare folks, so no need to fear, you can develop your plug-ins in multiple different languages. Regardless of the language you choose, compile it down to a WASM file, and then you take that and run it and load it inside of multiple languages, and this is where the malware developers get really excited, because you can take whatever language you're writing in, and start loading this WebAssembly module, and start running this shared code very seamlessly.

So, this all sounds great in theory, but it was time to actually put it to the test, and that's when I started developing my tool, C4, the cross-compatible command and control. So, in a typical crawl, walk, run fashion, we had to start with a basic hello world. Now, this is a very basic six-line Rust program to just return hello world, and then I went language by language and just tested this out. Sure enough, one by one, each of the programming languages returned my basic hello world message, so we're off to a good start. Next, we had to step it up a little bit, we had to really make sure that this thing could do reliable HTTP requests, so now my Rust program got a little bit more complex, but no need to worry, each programming language returned a status 200, indicating that your website is up and active. So, we're able to make, we're able to compile WebAssembly modules and make HTTP requests and interact with APIs and all that fun stuff.

Which then leads me to my first example of the AWS S3 plugin that I developed. Now, for those that aren't familiar, AWS S3 is a cloud-based service that's very popular for file sharing and file hosting. So, in this case, I developed two actions, and this is true across all of the plugins that I developed. There is a basic send and receive function. In the context of AWS S3, you're going to send a message by uploading a file to an AWS S3 bucket. Receiving a message, you're downloading a message from AWS S3, and then I also go ahead and delete the file after retrieving the message. You know, cleaning up after ourselves. Now, in a red team operation, there's a couple of things that you need to consider when developing an operationally ready external C2 channel. First thing, you need to be able to support multiple agents simultaneously calling back. In the red team world, two is one, one is none.


## [12:14]


You have to make sure you have a backup agent in case one of your other agents gets burned. So, in this case, I organized my messages into multiple folders, depending on which agent is sending and receiving messages. So, this ensures that multiple agents can simultaneously communicate with the C2. Additionally, we have to make sure the files that we're uploading don't overwrite each other. They can't have the same name. So, with WASI, I read the system time, and each of the files that are being uploaded are named after the time that it is. And additionally, you have to make sure that large messages are compatible. In this case, AWS S3 supports very large files, but this is really important when you go to exfiltrate or steal really large files off of a victim computer. So, with this, AWS S3 is a very good and viable option for external C2. In the plug-in, just as we talked about earlier, these are the two actions that are existing.

It's your send and receive commands, and I handle all of this with JSON. So, when you call your functions out of plug-ins, you're just sending a little JSON blob. So, in this case, because we're dealing with AWS S3, the parameters are going to include AWS specific details, like your access and secret key, the bucket name that you're creating and writing files to, and the region that that bucket is located in. So, here's an example of actually taking a plug-in and using it in Python. So, for Python, to actually get this WASM or WebAssembly run time, it's just as simple as pip install XSIM. You know, I'm sure the Python developers are familiar with that. You import your XSIM package, and then inside of a manifest configuration, you have to specify that this WebAssembly module is allowed to make network connections, and in this case, I just allow it to make connections anywhere, but if you want it to be more OPSEC safe, you could limit it to just AWS S3.

Then you have to enable WASI, because we're making network connections, we're reading the system time, all that fun stuff. So, we enable WASI, and then we have a loaded plug-in, and we can start actually calling it and making actions. So, here's an example of actually calling this loaded plug-in that we have in Python. So, we take our loaded plug-in, we build out our JSON message, and in this example, we're sending a message, just very basic test message. As you can see, we have some redacted access and secret keys, and some details about the S3 bucket that we're communicating with. And with that, we're very, it's very simple to continue to call these actions, and likewise with sending, you can receive just as easily. So, in the context of external C2, you know, this is all you really need, right?


## [15:18]


I look at a lot of agents on the open source side of things, and you just set up your infinite for loop, and you continue to call and receive, or send and receive messages to and from your C2 server. So, with that, hopefully you're walking away from this saying, well, external C2, it doesn't have to be that hard. With this, I have multiple plug-ins, I support AWS S3, Confluence, everyone's favorite documentation site, and GitHub Gist. So, with that, I have tons of plans for developing more external C2 channels. Additionally, WASM is a relatively new technology, I'd highly suggest checking it out. It's constantly being developed, and it's just a really cool tech to keep up with. So, with that, start downloading some C4 plug-ins and loading them up in your malware today. If you have any questions, reach out to me at scottctaylor12 across all the socials. Thank you so much for your time, everyone.
