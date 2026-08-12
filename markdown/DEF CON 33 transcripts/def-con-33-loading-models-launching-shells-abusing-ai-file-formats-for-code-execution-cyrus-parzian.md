---
title: "Loading Models, Launching Shells - Abusing AI File Formats for Code Execution"
speakers: ["Cyrus Parzian"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Loading Models, Launching Shells - Abusing AI File Formats for Code Execution - Cyrus Parzian.eng.txt"
sha256: "b9decddc49bdc178ec43ee523534d701bded5c7b3d86291f7dc01c317e7e4a85"
duration_seconds: 1118
words: 3057
text_chars: 16377
redacted_secrets: 0
converted_at: "2026-08-12T06:24:14Z"
---

# Loading Models, Launching Shells - Abusing AI File Formats for Code Execution

**Speakers:** Cyrus Parzian  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (18 min, 3,057 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Okay, hello everyone. Thank you for being here. My name is Cyrus Parzian and I am an AI retimer at one of the largest U.S. healthcare companies. Okay, can you hear me better? Okay, my name is Cyrus Parzian. I'm an AI retimer at one of the largest U.S. healthcare companies. Just a disclaimer, what I will be sharing today is my personal view and opinion and does not reflect my employer. So I've been in offensive security, especially in the areas of phishing, creating and modifying payloads, and finding new ways to bypass an AV and EDR for the last 10 years or so. And about last year, we actually started our own dedicated AI retiming. And I've been focusing a lot on prompt injection and different ways to bypass healthcare chatbots or different type of chatbots. But one area I think that might not get enough attention is the supply chain risk attacks in AI and large language models. So today we're gonna talk about that.

Also, as part of my presentation, I will be mentioning a few well-known and top-tier tools and platforms, but the main goal is to stay vigilant and raise awareness. So first, I'm not the first person to actually talk about Pickle Falls and the danger of them. Back in Black Hat 2011, Marco first talked about Pickle Falls and highlighted the security issues with Pickle Falls. And then in DEF CON Theory, Jonathan talked about how you could actually backdoor Pickle Falls. And today we're gonna talk about the dangers of Pickle Falls in the age of AI. So in this demo, I just show you real quick how you can actually turn an object into a Pickle file. It's a very simple method. And then next, we're gonna look into how you can actually create a malicious Pickle, which is, again, very simple. In this example, we're just gonna basically pop up a calculator and then we have our load.pickle, which is just gonna load our Pickle Fall and then just gonna pop up a calculator.

So that really what the demo is. But really what Pickle is, Pickle is a way or usually default way in Python to serialize and deserialize objects. Think of it as a way that Python, Pickle turns objects into byte stream and then when we load it, it turns it back into objects. And one of the main issues with it is that it can execute code when it's loaded. And Pickle Falls usually have the extension Pickle or .pkl, but not every, but some files could actually not have the extension Pickle or .pkl and they still be a Pickle Fall because what really matters is the content of the file, not what really is the extension.


## [03:01]


And that's one of the security issues is that you can't really rely on the extension to actually run that. So let's think about how an attacker would go and actually try to use this vulnerability. So they may go and download a model file from a website such as Hugging Face or GitHub, and they could go and create a model or a chatbot themselves as well, but we attackers like to use name camouflage so whenever we can use the popularity and the familiarity of people with another model or chatbot, we're gonna focus on that. And then after we downloaded that chatbot, for example, we're gonna try to insert our malicious code inside that chatbot. And then we're gonna republish the model file to a website such as Hugging Face or GitHub. And then we're gonna, at that point, we really have two options. We could just sit back and relax and see who's gonna download our model or chatbot and run it. Or if you're trying to actually go after a specific environment or target, we might make a very enticing phishing ruse and send that to them and entice that, in this case, probably most likely a developer to download our chatbot and run it.

So when I wanted to do that, I really didn't trust a lot of chatbots that were on Hugging Face. So I just decided to create my own chatbot. This is not a Rack chatbot. Rack chatbots are chatbots that you have a data set, you have basically some data that you go create embedding of it, you set in a vector database. This chatbot just relies on Flan-T5 small model, which is a model that you can run in most CPUs. And that's why I actually chose that. And there's another thing as well, is the Pickle Fall. The Pickle Falls have a set of questions and answers that we're relying on in here to help our chatbot to answer it. So I might go ask a question, what are the symptoms of the flu? And you see the answers, because our Flan-T5 small model is so small that it actually repeats the word fever. Another note here is that if you look at, in the Hugging Face, next to our Pickle Fall, there's a white square that says Pickle, and if you click on that, it says that Hugging Face scanners didn't find any issues with the Pickle Fall.

So there's no problematic problem with this chatbot, but here is the modification version of it. And in this version, we went and made two changes. First to the Python Fall, which is the main fall we have here, and also to our Pickle Fall. And if you notice here, there is a change to our white square, and now it has turned into orange. And if you actually click on it, you see that Hugging Face mentioning that the reverse shell fix function that we're mentioning here might be the issue. But one note is, I think when I actually uploaded this, it took a week or two weeks for Hugging Face scanners to have enough time to actually load that. And when they did, you have to actually go and click on that orange square to see the problem.


## [06:09]


Now let's take a look at what we changed about our Python Healthcare chatbot. We added the function, reverse shell fix function, which is a very simple function. I call back to a server and port address. Now if you want, you can set up a content delivery network or a CDN. And in our Pickle Fall, which I said, we have a set of questions and answers. At the end, we have a callback to war zero, which is our reverse shell fix function. So what really happens here, when the chatbot loads the Pickle Fall, it actually calls back to that reverse shell fix function, which gives us a shell. One of the greatest tools out there is Fickling for basically analyzing, creating Pickle Falls, and also check the safety of Pickle Falls. So in here, I used Fickling first in the above screenshot to analyze the, this keeps going, to analyze the Pickle Fall and the modified version of the Pickle Fall. So as you can see here, in the previous version of the Pickle Fall, we only have the set of questions and answers, but in the modified version of the Pickle Fall, we have added a new question and answer, which is the stealth payload, and also the war zero, which calls back to reverse shell fix function.

In the bottom screenshot, you see that I actually check the safety of the modified Pickle Fall using Fickling, and as you notice, it exactly points out the issue with the Pickle Fall, which is the war zero and reverse shell fix function, and says this fall could maybe malicious. But not every open source or actually commercial tool is gonna point that out. So on the right side of the screen, I have two very well-known open source tools for scanning Pickle Falls. I use them, and as you notice, they actually not point out any problems with that Pickle Fall. And I actually created this chatbot in February of this year, and when I ran it against most AV and EDRs, they did not detect any issues with it, and one of the very well-known commercial tools for scanning Pickle Falls said, this attack may be a little bit complex because it's using the Pickle Fall and also Python together, so they hope that they can actually detect it in the future.

After I created this chatbot, I notified Microsoft about it, so starting April this year, if you try to actually download this... Sorry, this keeps going to the next slide. But starting this April, if you try to actually download the healthcare chatbot, you notice that it would say virus detected, and if somehow you had an option to actually try to run the chatbot, it would say this is a reversal Trojan and would not allow you to do that. Now let's take a look at a different demo. In this demo, I'm gonna put all the reversal fix function and also the call to that function in a single Pickle Fall, and we're gonna just try to run it as an example to see if you're actually able to bypass Microsoft Defender Endpoint.


## [09:20]


And I bring up Microsoft Defender Endpoint EDR because it's one of the greatest EDRs out there. And as you can see here, using our one-liner, we can actually bypass Microsoft Defender Endpoint and it does not raise any flags or issues. And I was able actually to install Microsoft Defender Endpoint trial in here without any issues. Next, we're gonna look at ONNX. ONNX is a deep learning model that's used for actually converting a framework to another framework. So you might have a PyTorch model that you're trying to change it to TensorFlow. You're doing the same thing that we did in Pickle Fall, but we're just gonna use a one-liner to see if we're actually, in this time, we can actually bypass Microsoft Defender Endpoint. And as you can see here as well, we get a callback to our command and control, which is just a very simple Python server, but I was just curious if that would actually bypass Microsoft Defender Endpoint as well.

And if we go to the protection history, we don't see any signs of our malware being detected. And in the virus and protection settings, everything is good as well. So now let's take a look at the code. In our Pickle version, we just go define the reverse shell payload, we encode it in a Base64, we create a malicious class for that, and then we just dump the Pickle Fall. And very similar in the ONNX version, we define the reverse shell payload, we encode it with Base64, and we create a ONNX model, and then we embed our payload and we save it. So that's a very easy way that we could actually compare those two together. Now let's put everything together. We've gone to the ONNX, now we want to take a look at what happens if we actually try to inset that ONNX as part of our healthcare chatbot. Because what I want you to think about at this point, that healthcare chatbot is just a loader that we try to load various Python modules that may allow us to run code.

So in here, we're just going to try to create our ONNX malicious file, and then using ONNX.load in our healthcare chatbot, we're going to load that malicious ONNX, and we're going to use Flan-T5 model, similar as before, to run that code. Sorry, it seems we are running at issue, okay. Okay, in here, as you can see, we're going to run the Flan-T5, we're going to run our healthcare chatbot using Stemlet, and, apologies for some reason, and then in here, as you can see, we are running the healthcare chatbot, we are waiting to load our ONNX model in the background. I have to load this. Yeah, we're waiting for it here.


## [12:20]


And as you can see, we get a callback to our command and control, and now chatbot is functional, the developer or whoever is using the chatbot may just click on it, they get answers to their questions without any issues, and we as attackers got an access to their machine without them knowing that. So, this was just some theories of, we're doing it in a lab, but does this attack actually happens in real world? And there are multiple cases of that over this year and last year that has happened. One case was in February, Hugging Face found multiple malicious pickle falls on their website. Another developer in Disney actually gave access to their machine voluntarily because of AI Trojan horse, and the hackers were actually able to download 1.1 terabyte of data, and there was a malicious case of PyPy when they actually put some pickle falls there as well. So, still a big issue. So I talked about healthcare chatbot and how we could actually use that to make it a loader for various Python modules.

In here, I created four other different versions as well and uploaded to Hugging Face. In the case of Egg, Egg is a, think of it like a zip file for Python packages. So I went and created a version that only specifically focuses on egg files. Then I created a Cloud Pickle version. Cloud Pickle, think of it still pickle, but it has extended functionality for other type of file types that you may wanna do. Joblib is another one that you only use to save models, but under the hood it actually has pickle. And then lastly is Feather, which I call it Fast CSV. So those are like all of the four type of healthcare chatbot I created. And as you notice, two of those are actually being detected by Hugging Face, but two of them are not being detected. And that really, the issue is that some of them could easily bypass Hugging Face security. In the next two slides, what I really wanna point out here is that there are a lot of Python modules that some of them are being used in LLMs.

So Pickle is one that being used in LLMs, Cloud Pickle is another one, and we mentioned ONNX. But because of the prevalence of Python in large language models and in the AI workflow and pipeline, attackers don't necessarily need to go and use them. They could go and choose to use other Python modules such as Egg, such as Feather that we mentioned. So those are some of the notes that we wanna look into because we may go and just focus on the AI pipeline and just the modules that being used in AI pipeline, but we may miss the other important ones as well.


## [15:23]


Lastly, this is our last demo. In all of the previous demos I showed you, you actually needed to have Python installed on the machine. But using PyInstaller, you actually can turn your ONNX file into an EXE. So in here, I just turn our ONNX file that I showed you into an EXE, and we are able to get a callback to our command and control center here without any issues. And I'm actually, I'm gonna go as far as trying to scan this EXE with Microsoft Defender Endpoint, which usually they don't suggest you do that. But as you can see, we were able to actually bypass Microsoft Defender Endpoint without any issues using the ONNX EXE. Next, let's take a look at the Microsoft console and see what's the artifact look like for the EXE that we just ran. As you can see, VirusTotal gives our EXE a score of zero out of zero. And if you look, there is no sign of malicious activity as part of our EXE. So there are a lot of other models, there are other Python modules that you can go and try to turn them into EXE using PyInstaller.

And that would absolutely bypass a lot of AV and EDRs. And that's one of the issues I had when I was doing full-time red teaming is that we had to spend days, weeks, or months trying to find a new payload that would bypass AV and EDR. But apparently, if you actually focus on a lot of these Python modules, you're able to do that. Okay, what is the mitigation or recommendations? Well, probably the main thing is do not run untrusted code. So if you don't trust it, do not run it. And if you want to think about from the developer's side of view, they trust the websites that they're downloading that to detect this type of activity. And after they download it, they trust the AV and EDR to actually basically detect any type of malicious activity. But in this case, it doesn't happen. So another thing that you might want to focus on is restricting access to websites such as GitHub and Hugging Face for most of the users in the environment because it is so easy to actually download the type of, this type of healthcare chatbots that in the background, they may actually give access to the machine, to the attacker.

And why traditional security fails? Well, traditional security fails because the reality is a lot of AV and EDRs are not looking into the supply chain risk attacks with AI and ML file formats. And it is not an easy job to actually try to, you know, go and patch the issues and the securities with those. So in a, for example, an example for a HTA file or a JavaScript file, it is very easy to go and block or detect a .HTA or JavaScript. But as we showed, a Pico file, if it doesn't have the .pko pickle, still could be a secure risk but we wouldn't know that.


## [18:28]


So those are some of the things that I think could be great to implement. With that, thank you for your attention and I hope you found this informative. Thank you.
