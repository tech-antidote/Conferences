---
title: "Help Linux in my Webcam (• •)"
speakers: ["Mickey Shkatov", "Jesse Michael"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Help Linux in my Webcam (• •) - Mickey Shkatov, Jesse Michael.eng.txt"
sha256: "a9024287f0ca83e6cab68dbd58c743ca70eb056d8335280db3cb316ba34f60a3"
duration_seconds: 2476
words: 5638
text_chars: 29512
redacted_secrets: 0
converted_at: "2026-08-12T06:24:14Z"
---

# Help Linux in my Webcam (• •)

**Speakers:** Mickey Shkatov, Jesse Michael  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (41 min, 5,638 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Quick intro. I'm Mickey. That's Jesse. We hack things. We give talks. That's who we are. There's a lot of stuff online. We work for a company called Eclipsium. We want to mention them because they help us fund all of this stuff. Quick terminology, for those unaware, UART is a serial communication protocol. Wow, it's really distracting, that noise from the other place. Don't tempt me. Okay, so UART is a serial communication protocol, usually in IoT devices, OTA over the air, UVC, basically read it yourselves. One thing I want to be clear about that I do want some participation. If anyone has a question, shout because I can't see anything. I have a light in my eyes. So either come to the microphones and ask us a question or interrupt, yell, everything's cool as long as you do it, you know, with taste. Another thing I want to be clear about, there's multiple ways to hack a thing. We did it one way.

I'm sure there's at least 12 people here that can do it better. I'll start with a story. Back in the COVID days, we did a lot of e-meetings, you know, video calls, all that stuff. And I needed a good webcam. So I found one that did 60 frames per second. I'm like, yeah, I buy it. I plug it into my computer. And then a year goes by and it starts to be flaky in meetings. And I'm like, okay, it's been on the market for two years. There must be a firmware update that I haven't applied yet. I should go and apply that. So I find the firmware update tool. I go on their website. I download it. That's the URL for the web archive for the original tool. I recommend that you save it because it's no longer on the internet. So I download the tool and I install it, right? Run the installer. Get the GUI for the installer. It automatically opens it up. It shows the camera, the firmware version. But did you see it?

It extracts into a folder. Me, being an inquisitive mind, I'm like, okay, something's sus here. I open and look at the files. You see it? I take a closer look and I say to myself, like, what the fuck?


## [03:03]


Why does a webcam need almost an 8 meg firmware update? So take a look at it again. There's a .sh script. Keep in mind this is a Windows updater. U-boot, a USB update binary. Some weird ass looking file, OTA. And an auto update TXT. Okay, something is off here. I like to hack IOT, so bin walk. I don't know why I'm doing this. I swear, this is one of the most beautiful bin walks I've ever gotten in my life. If you ever run bin walk, you see a lot of sometimes noise. This is the whole dump. This is how the firmware for the camera looks. Now I really have to open this. Open this device. And it's like hard. The front panel is glued in. I rip it apart. I open it up. I look at the back. I see an SOC. You see this stuff. You go like, okay, I'd expect to see a chip on a webcam. USB to the chip. The chip does its, you know, conversion of the image. Passes on the USB. Normal stuff. What you'd normally expect from a Linux running target or a system or a device is to have the trifecta.

The CPU, the memory and the storage. I didn't see memory, so I'm like, okay, weird. Look at the back. I see a spy and then I see these pads. I call them sus pads. It's three pads on the middle of a PCB. I'm like, okay. Turns out, there you are. So maybe I can hotwire this thing. So I hotwire it. And this is what I see. Okay? So at this point, um, I'm a bit processing. I'm like, okay, what did I see? I see Linux on a CPU. What Linux version? Firmware version. And this is the exact process of emotions that I've had at the time. Then it turned into this. And then it came into that. Okay. I'm going to hand it off to Jesse now. So we've already seen some kind of suspicious things already. So we started to dive into what the firmware update process actually does and how that works. So the way their package arrives, you have this firmware tool executable and then a couple DLLs. There's this HD 510 SDK DLL that has most of the update code itself.


## [06:06]


And then it has a helper function that's AIT UBC extension API. It's basically just used for, there's something in UBC or USB video class, it's called extension units. And those are used for configuring different things about the camera. This really, most of the update code runs in that HD SDK. It only calls three of the functions through this helper. There's a lot of other stuff in this extension unit helper library that is used for other types of devices. So they just pulled this in for a few small commands. And then together, those will take instructions from the auto update.txt which will then basically parse commands from the OTA and send commands and the firmware file to the device itself. And if you look at that auto update, it just has this E star command and then the name of the other file to parse and then reset. If we look in the OTA, these are even more suspicious because it's just SF probe.

It's like spy flash probe and we're probing chip select zero. And then spy flash erase. This particular region offset, this particular size and then it's TFTP transfer. That doesn't really make sense over this USB interface for how they're doing it. But we'll go with that and then write that region to that offset that they just erased. This is literally the full update script that it runs. We take a closer look at how this actually works in the internals. I mentioned the UVC extension units . They're only doing one call to get a property for this specific vendor extension extension unit to get the firmware version and then also switch the camera into firmware update mode. Extension units are used for a bunch of other things for different cameras like if you have like a pan, tilt, zoom, all of that, those are configured using extension units. But when you send this specific vendor, specific set property, it reboots the device and comes up as a mass storage device which is kind of interesting.

And then from then on, it's sent, it's using SCSI commands, basically SCSI direct, SCSI pass through commands in order to use vendor specific SCSI op codes to continue sending command and data to the device. And then it also sends this interesting USB updater op bin and uboot.bin for the camera to run during that update process, which is also something that we're concerned and suspicious about. But here's some of the code. It's just doing the open device by path using that helper library and then sending this extension set with a specific GUID and then a specific control selector to say what specific request I'm doing within this extension unit.


## [09:12]


Once it does this, it just starts waiting and looks to see, has a new mass storage device popped up? Can I find the specific device I'm looking for? So at that point it starts sending SCSI commands. If you look at the bottom, there's this device IO control. The specific IOCTL number is OX4D004. That's the specific IOCTL for SCSI pass through. And it's used for other mass storage devices. But in this case we're just sending an inquiry request where we get information back from the device about the specific device from this inquiry request. In this case they're using this in order to determine what mode the camera is operating in. So after it reboots, it comes up in what's called ROM mode. And by doing this inquiry command they can determine if it's in ROM mode based on inside of the buffer it will have a G or a C at a specific offset. If it has a UPD at a different offset, it's in update mode.

And if it's in UBO, it's in UBOOT mode. And the way that this works is that it will transition the camera into update by sending that UVC extension unit request. And then it will send an inquiry. Once it's in ROM mode, it will send the updater. And then once it's in updater mode, it will send UBOOT. And then once it's in UBOOT mode, it will just literally send UBOOT commands over that mass storage channel that it's still using, which is kind of an interesting way to do this. So they are using vendor specific SCSI op codes to transfer data. The TFT command instead of doing network operations, they have special handling to convert that into there's a load info command that they send which says here's the address to load this at in memory. Here's the size. And then the update tool itself will then calculate an MD5 hash, pass that over and then start sending chunks of that buffer in multiple different SCSI write requests using that specific vendor op code with a sub op code to say these are the chunks and then the last chunk has a different sub op code.

But all the other commands are just sent as literal strings to run and by the camera to interpret in this UBOOT that's running for you now. So when you're looking at the camera UART itself, it basically looks like this. And you can see the camera is running and then it switches into UBOOT mode and waits a little bit while it's doing things. And you start seeing things like this run command at the end. Those are literal commands that are being run by this, that are being sent from the updater tool to be run by UBOOT in the camera. So it will do the run commands and then it will do this operation of erase, transfer the data and then write. And we can look at this and these basically map to our commands that were in that auto update TXT or the OTA TXT.


## [12:20]


One interesting thing that we noticed is if you look at the order for here, they're erasing the spy region and in this case they are erasing only the root file system and the kernel. So they erase the file system and then they transfer the new image to update. So if you look at the bottom there, there's an MD5 pass. What happens if that fails? If there's like an integrity ‑‑ if there's an integrity problem while they're transferring that file, maybe it was a file that isn't going to work. They've already erased the image and there isn't really any retry and send the copy, send the firmware file again if that fails. So that's another thing to take a look at. But at this point, it's a pretty straightforward method of how we can do the updates. I'll pass that back to Becky. Spoiler alert, it breaks the camera. That was easy. So we've seen their GUI and their tool and everything. Can we just simplify and make our own tool?

Because we know they're using the third party API from some SOC vendor. Short answer is yes. And it's in C sharp. And the simplest thing is because we got lucky and the firmware update tool is in C sharp, we threw it in our IL disassembler and got the assembly and hacked it together. And you can convert it to PowerShell if you'd like. It's fun. And it works the same, calls the DLLs and fun. So a quick topic change. Why the fuck would you put Linux in a webcam? The quick answer is basically money. If there's a company that sells you an SOC that has all this integrated already in it and it works and you just got to rebrand it and maintain a, a small workforce of people to maintain the updates over a couple of years that already do other things, it's cheaper to do it that way but it's not always secure. The way it looks is like this. The SOC vendor is called Sigma Star. They make this chip. You go on the website, they sell all these kinds of SKUs of it, they do for webcams, IOT, all kinds of stuff.

They are a subsidiary of a company called M-Star Semiconductor that doesn't appear to be alive, it's only on paper and that is a subsidiary of Mediatek. Out of Sigma Star's SOCs we've identified so far, we've seen, um, in TP-Link, which credit to TP-Link, they do publish their GPL code, which is great.


## [15:23]


Nexigo and OBSBot. Never heard of these before this, uh, this research. But we'll get to that in a second. Uh, when you go to their website, the fun, the, the good thing about these companies when they, when they want to sell their product, they build a full vertical stack of everything you need. So, the SDK, the code, the documentation, the data sheets, the examples, everything. You go to the website and you get all the data you need. That's, that's the link to go there. You do need, uh, to create a credential. Supposedly it will get you access to the source and the SDK. I have tried, I think it's been two months with two different accounts. Uh, one is Gmail, one is a cor, Gmail didn't work so I went with my corporate email to see maybe they filter. No, they just don't give a shit. Um, there's no data, there's no, nothing. It is like pulling teeth. It's terrible. So, what can you do? So, do it yourself.

You go Google things, GitHub things, look in the forums. Surprise, you can go through LinkedIn and you can go through Twitter. Why? In a second. Um, so the process is like this, you Google for the files, you find them on GitHub, you find them on Google and you repeat this over and over and over and over again. And if you can go into the Russian forums, you get bonus points. There's a GitHub repo with four, sorry, GitHub user with four repos. One of them is the actual USB tool from Sigma Star. It's a bit of an older version but it, they keep things the same way over generations because people are lazy. Um, and if it works they just keep it moving over the years, the technology. You get the U-Boot, you get the Linux, you get the, their SDK. Um, the next two are open directories. So, you just find random stuff in open directories. And the last one is an open IPC kinda sorta, um, implementation.

Open IPC if you don't know. It's, um, it's for internet cameras that you can open, you can use open source code to do it. And it supports Sigma Star's chipsets. So, they do have a kernel for that. But like I said, no help from them. I thought maybe there's a chance. Nothing. Forget about it. Um, the only other thing we could do is reach out to Lenovo and say, can you give us the GPL code? And this is how it went. We asked for the GPL code, Lenovo asks Sigma Star for GPL code.


## [18:24]


Sigma Star's, Sigma Star gives Lenovo the code, Lenovo gives us the code. We build it, it fails. We go to Lenovo and we go back to Lenovo and say, we need more, uh, it's not complete. Again, cycle. We get the code, it works. We build all our demos for the talk and then we're like, you know what, we want to take the extra step, do something, we did something crazy, let's do something even more crazy. Uh, we requested the GPL again and nothing yet. Um, hopefully we'll get it. So, we do have the U-Boot, we have the kernel, we don't have the latest SDK. We have a bunch of stuff from GitHub, what can we do? We do know the structure of how it looks. They do have, for the same SOC you can build either for, uh, Spynor or Spynand. In our case it's a NOR. This is how the, the partition looks like. We're going to focus on these two because it's easier, it's the easiest way for anyone to get into this world.

Uh, just build a kernel or modify a file system and that's what we know. We know, this is what we know. We know the camera runs Linux, we know how to build a Linux, we know we can flash it, we know how to flash it. So, here comes the fun part. Can we turn the camera into a camera? We have a laptop, we have a camera, this one. We plug the USB in. Uh, I opened the camera app on the, on the background just to show, I disabled the, the built-in camera. The camera shoots out a text and then it reboots into normal, regular code. Take a picture of him too. Okay, cool. And that's it. So, we, we took the kernel, we built it, we added the hit stack, USB gadgets, cool. The camera boots up, it's a hit, it's a keyboard, it types in stuff, it's cool, it's funny. Um, what? There's more. So, um, so this is the, this is the, this is the, this is the how do we do that? The, the file system is read only, right?

It's, it's a spy chip, it loads it to memory and then runs it and every change you do doesn't persist across reboots. Um, so it turns out there's a, there's a section in memory called environment variables, every system usually has it. Um, in this case we just added our own variable called implant and the camera just, the, our code in the camera checks if implant is one, run the hit payload, change it to zero.


## [21:24]


Next time the camera reboots, implant is zero, if, if, if the code is, if the implant is zero, boot into the normal Lenovo flow. That's it. This is how it looks from the camera side. The camera boots, you see implant equals one, means run the payload, start sending key strokes, this opens an admin command prompt and starts saying, psst, I'm your camera, this is an admin command prompt, I'm going to become a camera now. It reboots, implant is now zero and it just follows the normal Lenovo boot flow and it's a regular camera. Okay, let's, uh, change gears. Uh, for some god awful reason, uh, the RCS script in the camera has Telnet D starting in it. So can we have a network gadget on the camera? Let's try it. So we plug in a camera , I don't know if it's playing. Yeah, it's playing now. So we plug in a camera, integrated camera is off, just to be sure. I'm going to show that there's an, there's an RNDIS gadget, once it's plugged in, it flashed, means the USB event happened, USB Ethernet means the camera's connected.

As you can see, it's connected alongside a keyboard from the same composite device. Here we, uh, open Teraterm, Telnet to it, AI Scion, no password, we drop, drop into a shell, I go to my folder, I run the script, it issues the usual I am evil keyboard script, and then I go and I reboot the camera, I don't, I type reboot, it's wrong, I need to type, no, I do, I type reboot, it works, it's fine, I open the, uh, the camera app in Windows and then I wait. And that's it, it's a normal camera. Uh, so, what else can we do? We got to this point. Um, better buckle up for this one. This is a PowerShell script that all it does is share the Internet connection from the host Wi-Fi to the gadget. I see you're getting the, where we're going with this. So, on the left top is the webcam UI, on the bottom left is a Kali machine that we have in Microsoft's cloud, and on the right is the laptop.


## [24:39]


We start hosting a payload, we start Metasploit listening on the 443, and then you have Metasploit running and listening. Um, yeah, listening. The moment, the moment the text starts running on the top left, the camera's plugged in. Uh, Wi-Fi is connected to a, uh, network called local host, sorry for the confusion. That's it, it's connected to a Wi-Fi, nothing says shared, nothing there, just normal Wi-Fi. Camera plugged in, you are scrolling, the camera now goes to and fetches that PowerShell script. The, the camera has now enabled Internet connection sharing between the Wi-Fi and the RNDIS gadget. The camera now has Internet, but the camera wants to show you, so here we go, there's the gadget, the camera opens the properties for the Wi-Fi controller, tabs over, Internet connection sharing, hits enter, and we have the Wi-Fi controller . And we have a, an interpreter session open on the camera.

I open a shell to the camera from the cloud, I just reboot it, because the flag tells it to run as normal camera now. Usual Windows camera app to show you there's no camera found, but it's connected, it will pop it up. Yay! To be honest, this whole demo is structured around this GIF, so I'm not going to show it . That's it. So, um, go have fun. You can buy this camera on Amazon right now, 45 bucks, uh, even cheaper on eBay. Uh, if you're, uh, if you, uh, if you're afraid, if you want to go deeper and you want to play with it, get two. Always get two. Uh, pro tip. And get a flash tool. I recommend, if you have money, buy, uh, Dirty Prog. If you don't, if you have 50 bucks, buy the, uh, the Tigard by Joe Fitz, also known the Tigard King. Um, or any other spy flashing tool. Let's go rent a little bit of the other vendors. So, um, quick question, anyone here from Lenovo?


## [27:42]


Raise your hand. Don't be shy, I'm not going to do anything bad. No one here from Lenovo? Okay. I'm not offended. Um, so we looked at other cameras, and it turns out there's a bunch of other cameras running Linux. Uh, the Opal Tadpole is running Linux on an Ambarella SOC. Uh, there's a story behind that, I think I'm going to tell that in a second, I don't remember if it's in the slides, but they published the, the, the GPL code yesterday. Next to go is Sigma Star SOC, crickets, nothing. Uh, TP-Link, love it. They already burn, they already got burned by GPL, so they publish it, they don't argue with that. Uh, and OBS Bot is another unknown, uh, brand. OBS is Open Broadcasting Studio, if you're not familiar with it, that's a very popular tool, open source tool to do a lot of video capturing. So, some companies rebranded it, and is selling cameras. Sigma Star SOCs, but newer kernel, ask for GPL, no answer.

So, we're going to drop an O there. Um, this is how the Opal Tadpole motherboard looks like. Remember I said, in the beginning, the trifecta, you get the SOC, the RAM, and the storage, it's right there, you can see it, it's three chips. Easiest to recognize, you know, you see this, you get a wide attack surface. OBS Bot, um, Sigma Star SOC, they were kind enough, to mark on the board, T and R, which is TX and RX. So, you connect it, and this is what you get. So, this is going to be an O day, real quick, I'm going to run you through it. Um, you boot, you hold enter, you get into the boot loader, you print the environment variables, remember print env, you see in the environment variables, it mounts the UBI file system as, um, sorry, I'm going faster than my explanation in the video. RO, so it's mounting the NAND as read only, and it in it's, into the Linux RC executable. So, we're going to change those.

We're going to set env, RW, and in it to bin SH, and save env. Don't ever forget to save env. So, we're going to reboot , because that doesn't work, so type reset.


## [30:43]


The camera resets and falls into bin SH, you fall into a root shell, you just change the password, root, root, it's too short, but it will change it anyway. You reboot, you go back into your boot, and then you have to revert your changes. So, you change it back to RW, because you don't want anyone messing with your changes, and Linux RC, the usual stack, and it boots into the normal vertical, the normal code, normal camera code. At the end, it's OBS Linux, OBS boot Linux, you just type root, root, and you have a root shell. Okay, so, I can't believe I'm saying this. There's Linux and webcams now, so, go look at that stuff. There's a whole, like, we've done this 10 years ago, we're going to do this thing again, where you have to do a root of trust, verify firmware signatures, do all that stuff, but now we have to do it in webcams and everything else that runs Linux. Basically, all the stuff that we have to deal with IoT, move that, move that mindset into USB.

So, think of every USB device also as an IoT device. Now, GPL compliance. I've done a lot of, of, of complaining to people for GPL code for this project for a while. Basically, any device that runs GPL code, you can ask for the source. They don't usually do that, especially if they're in China. But, you can, you can harass them into compliance. Okay, so, there's, there's a way to do this. You can track people down on LinkedIn and Twitter and social media, which I did in a second. And you can also contact the Software Freedom Conservancy, and they can help as well. What I did, I have no shame, so I just contact Opal co-founders on LinkedIn. I counted the OBS bot CEO on LinkedIn. The next to go co-founder, I just contacted the co-founders. I just went, give me code. And I, pro tip, use GPT to word legal sounding messages. I got a response on Twitter from one of the co-founders of Opal.


## [33:43]


Any, give me a chance , anyone from Opal here? Ah, thank you for coming. So, good job. Get GPL code. Cool story about Opal, they do firmware updates over web USB. And because they were good, I'm not going to say more about that. Um, so, a, a little bit of experience of how to work with PSIRTs as a security, a security researcher. When you talk to product security response teams, there's a lot of communication that goes on in the background between what the PSIRT team does that face you when you, when you contact Lenovo or any other big OEM. They have to go talk to their product team. So there's a lot of sometimes miscommunications. At first we were told that these devices are end of development and turns out it was not the case. So we have to, we have to change things. Anyway, if you've seen the movie, you know how I feel. This is the Lenovo statement, we're going to skip that. Updates, links, firmware updates over that link.

Um, this is the disclosure for them. They, they published it yesterday. Uh, arbitrary code execution as a medium. Someone needs to help me math this. Um, physical access, I don't know, I can have software execution on the host if it's connected to the camera, then I can flash the camera. I guess you can word it as physical access, I don't know. Bottom line, this is not a camera . Uh, I want to thank Rainforest Puppy for, uh, GPL advice and, uh, Case for helping us battling the, the kernel. There is a bunch of shit on this mega link, um, including an OVA VMware image for you to take, download and install and build your own Sigma Star Kernel and other stuff in the GitHub. Questions? Okay, you can clap now, sorry. We were, we were rushing it a little bit. We have five minutes, I know. We, we were stressed out that we won't have enough time. Okay, now we're open for questions. Just yell them out if you have them.

Or run to the next talk, it's fine too. Either yell it louder or... How long did it take us to reverse the camera? Minutes. It's, it's basically building blocks that you know exist.


## [36:44]


Linux, you look at it, it's like hacking classic IOT but over USB. Thank you. More questions, give me more questions. Yes, yell it out. Anybody, anybody can buy one of these, flash it and resell it. Yes. I have a, I have a question. Yeah. I, uh, I bought a, a very similar generic Chinese webcam, uh, about two years ago and a couple of weeks ago I was doing some ADB debugging on my Android phone and when I ran ADB list devices, the camera showed up. Yeah, that, that'll be it. Yeah, have fun. Yeah. We do that too. Android's a Linux too. Yeah, go ahead. How many times did Linux fail to build? Oh God. Um, so Linux failed to build a couple of times but maybe mainly because we got incomplete source. Oh. There, there was a bug in... Oh, there, there was a bug in, uh, the HID gadget that we had to patch for getting the, to get the HID stack to work but in the second iteration of GPL code they already gave us the fixed version.

Oh, okay. So it works . Yeah, building the kernel is fun. Just take a deep breath before you do it. Go ahead. I think it, you sounded surprised to see Linux in these. I've, I've been an embedded developer for a long time myself. What was it you expected to see, like Wind River, FreeRTOS, something like that? Uh , simple, like it's, it's a freaking convert a CMOS image to USB. That's it. It just takes an image and put it on. Why? Well, it looked like a... Wait, wait, hold on. The AIs, I get it. There's a lot of, you expand things, facial recognition, Windows hello, all that stuff, I get it. But I was surprised to see it because I wasn't expecting it, I was expecting the host to handle most of the processing versus the camera to do all that. Do you feel like that's a trend you see accelerating, just shoveling more horsepower into those things? I'd say over the past ten years there would be a trend of just shoving Linux into things.

How's that affecting like the prototyping cycle for these guys? Are they kicking stuff out even faster, figuring they can just patch it? It's, it's a low, it's a, it's a more convenient learning curve. And it, it helps handle your attrition of staff. Because all you need to do is bring in people that know Linux and they can pick up where the other left off and just maintain the stack. I guess it's cheaper. So by attrition of staff you mean you're seeing kind of the same education fall off in everything that isn't Windows or Linux in China as here?


## [39:47]


When I, when I say education of staff I mean learning curve. If you have a custom SOC with your own custom stack with not, with complicated proprietary code, learning curve is wild. But if you have Linux it's simple. Just bring someone who knows the basics, ramp them up fast. So you mentioned that you were able to get internet access over USB. Is it possible that you could use this method to implement something like say an IP webcam or like functionally upgrade the camera to do something it didn't do before? So funny you mention that. We, we, we were missing files at the end of the, of the cycle of the GPL. Let's call it that way. And some, a couple of those files, not you guys, I'm pointing at Opal, not, not you guys, the, the Sigma Star people. They had kernel modules specifically for the IR SOC, the IR chip and the, the CMOS chip. So we were hoping we can get those kernel modules and just use an interpreter and just webcam, snapshot, go wild.

But we didn't get that in time. So, yeah. You can do, you can do crazy stuff with this. It's a computer on a USB. It's a bash bunny basically with a camera. More questions? We got no time, so catch me in the hallway.
