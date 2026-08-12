---
title: "Hacking OBD-II Emissions Testing"
speakers: ["Archwisp"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Hacking OBD-II Emissions Testing - Archwisp.eng.txt"
sha256: "616d339db44b3f8755aef0fdb4a7ca80d1b04d4c2975f929d8536ef83725f8cf"
duration_seconds: 810
words: 2457
text_chars: 12618
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Hacking OBD-II Emissions Testing

**Speakers:** Archwisp  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (13 min, 2,457 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Thank you all for coming. Thanks DEF CON for having me up here. As Juris mentioned, I've been involved here in a lot of different ways, but this is the first time I've actually been up on the stage, so it means a lot. Do we have any car enthusiasts in the audience? Yeah, okay. Any of you ever had problems with your emissions testing? Yeah, we're going to have some fun. So I assume you all can see something. I can't see shit. But we're going to talk about the ODB2 systems in cars and what we can have fun with. So this is a car I bought about ten years ago. It's a fun go-kart of a car. It has a little quirk about it. Anybody know what this car is? Anybody? Yeah, so we've got the Wankel rotary motor in it. And specifically, these things love to kill catalytic converters. But at the time, I was living in Kansas City, and they don't do emissions testing. Oh, by the way, did he mention SetKC? Yeah, so we'll wrap around to that.

So, you know, it's not there. We don't have to worry about it. So I enlisted my little helper, and we were like, fuck that, get it out of here. So life was good for about eight years. Then I decided, well, let's move to the West Coast. Turns out, they don't like that so much around here. However, as I was digging into the laws, they had this statute that got me kind of excited. It said for collectible vehicles, we don't do emissions testing. I'm thinking, well, this car is kind of unique. It's old. They don't make it anymore. It's the last time they made this type of motor. So I'm like, yeah, let's start digging into this. And then, you know, used infrequently, sign me up, right? This is how I'm going to get in. But then they had this last little thing at the end. It's like, every person must have, every person who's of a driving age in your house must also have another car. I've been working from home for like, ever.

And I drive this car less than 5,000 miles a year, maybe once a week, right? So not only do I have to have this car that I never drive, but I have to have another car registered to me that I never drive, right? And motorcycles don't count. Lots of other fun little things don't count. You have to have a car that you can drive every single day, regardless of the fact that my wife works from home, I work from home, we take the kids to school. That's it, right? So we're like, well, glad. I'm kind of a hoarder, so I still have the catalytic converter and all that kind of crap. Put it back in. A thing about that, if you don't ever have to do emissions testing, and it's never a concern of yours, if you just put the stuff back in there and you go and try and get it tested, there's this thing that happens in the computer that they don't really ever tell you about unless you have to deal with it.


## [03:02]


I was like, what the fuck does it mean to not be ready? And you dig into it, and I pull up the service manual, and sure enough, after you reinstall these parts, and it turns out any time you reset the battery, you're going to have to go through the cycle. Drive the car up to a certain speed, let it idle for so long, and meanwhile you have to have the air conditioner off and all that stuff. Did I mention I live in the desert? Driving a car around for 40 minutes to do this with the air conditioner off is not fun. But I tried for months doing this thing while in the time that I don't actually drive this car. And I just can't get rid of these goddamn readiness monitors. And so I'm like, what the hell? So let's throw back to DEF CON 26. Mentioned I was tech Casey. Anybody heard of the badge pirates here? So this was their first badge they made. As part of a tech Casey kind of let's have fun, we're going to be part of badge life, blah, blah, blah.

And as part of it, I made this little add-on to my badge and hooked it into the ECU and it could read the oil temperature and water temperature and stuff. So I was like, yeah, I've done this before. At the time it was a UART adapter, no problem. It's a little high-level, but really how hard can it be? So I start digging into the protocol. There's an authentication mechanism in the front. We're like, okay, I've got to bypass that at some point, right? There's something that's going to happen. Anybody who's familiar with Canvas right now is going, oh, yeah, okay, I know where this is going. A basic data frame. As I dug in to the next part, by the way, the references for all these are on there. I'm not going to go there. We only have 20 minutes. We're going to keep this moving. Zero to eight are the possible authentication IDs, okay? So when I saw that is the moment when I went, you know what, maybe I don't have to do this the right way.

I can just kind of tell the computer to do what I want it to do. So I did what any sane person would do and put together a thread board that let me hook up a logic analyzer. That's kind of what it looks like. You can buy these things off of Amazon for a couple of bucks and you hook them up. But then you plug in a logic analyzer and anybody who is familiar with Canvas knows this part, but anybody who's just kind of getting into analyzing hardware signals, you'll notice that the signal never goes near zero. So you have it's plus 2.5 up or down over 1.7 volts, I believe. And it's inverted together to cancel noise and all that stuff. So if you want to be able to use like a Salia logic analyzer or any of the cheaper stuff, you need to do a little bit of messing around. So this is what we call a DC filter or an AC coupling. And you're essentially just removing that low level DC voltage from the signal so that you can get something like this.


## [06:05]


And also I added a cap in there that rounds off the top so you get a nice square wave, but square being relative. So now we see data, right? At the top of the screen we can see it's actually starting to parse data. We're not going to dig into it too much, but at least we can confirm what we read in the document is what we're seeing, right? It's good. But what I really wanted to do was, hey, how can I respond to this thing in a programmatic way? So these things now, they don't even bother to separate them. I can't fucking see the screen. Sorry. You pay six bucks for six of these. They don't split them up. You just pop them off or whatever. But these are your transceivers. I have ESP32s laying around the house. Anybody who plays with these kind of things have them, right? It has a built-in CAN bus controller, but it doesn't have a transceiver. So you need one of these. They're a couple of bucks.

You get them off of Amazon, plug it in, and then you can start seeing this kind of stuff. It's actually acknowledging packets instead of just being able to listen to it. So as we dig in a little bit deeper, we see there's the identifier field, but just fixed, by the way. The zero is the ECU, so you just tell it you're the ECU. You tell it this is the received packet from the scanner. It's saying, well, there's a link, there's a service, there's a PID. Turns out there's this handy little thing called Wikipedia that you go in and you look it up, and it tells you exactly what it's looking for, and then you go back to the other page where they have this little decoder tool that says, oh, I can't, you know, if you receive this message, this is how you want to respond and construct the frame. So we have a response , right? So now you can see it's being sent on both. It's a response on both sides when you send a message.

So echo, I believe is what we call it. But then we have this error that happens right after we respond to the goddamn thing, and this is what happens. So this is a little cheap scanner you can buy anywhere that I just use for clearing messages and stuff, but the goal at first was, like, can I even fool this thing? That screen I looked at for probably two months. Turns out these kinds of things are pretty complicated. It's just so many different layers that you're worried about. Yeah, you just got to make sure you're keeping track of every little piece. And it didn't help that at this time I had lots of friends on Twitter going, AI coding agents are awesome, you should really look into these, blah, blah, blah. I'm thinking, great, I'm in this really, really complicated project, now's a great time for me to start exploring AI coding tools. Malicious ignorance is about the best word or phrase I can come up with to describe that experience.

Something it's really, really good at. The, like, writing registers, reading back registers, debugging information, all that kind of crap it was really, really great at. It thinks about hardware like a high school level kid who just read a book on hardware thinks, right?


## [09:15]


It had convinced me that I knew nothing about hardware at all. And the protocols were just garbage and everything that I thought I knew was just terrible. Don't listen to it, right? Half of what we're going to do with these things is figure out how to teach them. But in the process, I ended up actually abandoning the entire design of the original one, digging in a little bit deeper, I learned the canvas controller on this thing is actually kind of a pseudo copy of whatever the SDA 1000 proper one was, and there's some details that they don't expose that you really need to know when you're figuring out all the timing and all that kind of crap. So I went with an external spy controlled one, which has the secondary benefit of later on, I actually wanted to proxy on the same board without having to, like, chain two ESPs together. So I'm like, I know I can run multiple spy buses. I'm sorry if I'm high leveling some of this stuff.

You're just going to have to look it up later. We only have 20 minutes. But, yeah, faster, faster, faster. So we've gone through, we have it working, and sure enough, we have a working response to the scanner. This is very, very phase one, gone through all this, but within the end of the day, we have this thing reading out exactly what we want. So these are the same screens that we saw earlier where I was like, god damn, I just can't get it to do what I want. Now I've proven this concept of, like, okay, we can actually show that we can convince this little crappy scanner to do what we want. So, you know , I have an emulator working, and I had some working knowledge of the AI thing, and I forked it off and said, hey, turn it into a proxy for me, let's see what happens. It can't hurt, right? So it turns out, it actually didn't do a real bad job. But the ultimate incarnation of this thing is you've got the two breakout boards, one goes to your scanner side, one goes to your ECU side, and installed, it looks like this.

I mean, it looks, if you've ever crawled under the dashboard and looked at your ODB2 plug, you've got a legit-looking thing. That's part of the thing. And I should mention, too, in the state where I live, which I haven't said what it is, but the rule is, it doesn't matter, as long as there's no check engine light and they can plug the thing in and it reads what it wants to read and it gets an okay, then it says, yeah, it's going to work. So we have a video. So it starts off just, you've got to start the motor when you get up there. It gets it running, make sure the, come on, move it a little faster. So we can see the DAS is running, we have RPMs, it's all working the way you would expect it to. Then we get our ODB2 tester out. That one, we plug it in. This is your factory configuration. I know it feels like an eternity when I've been talking this fast, but really, it just, so you can see, it run the scan, it can't really see with the lights, huh ?


## [12:20]


But it's showing, like, there are two incomplete, or actually more than that in this case, because I had reset the motor. Running through them, doesn't work. So I reach under there and just kind of move the, pull that cable out, plug in the adapter and then tuck it back under the dashboard and I'll just skip forward in the video a second. There we are. It took about two minutes total to do this, if you can see the time stamp, but I'm impatient, so come on. Okay, there we are. We have it plugged in with the photo that you saw before and we can see we have zero codes, monitors, zero incomplete and 11 ready. So that's, we have it working. I chose specifically not to include any kind of active testing in this presentation. You can extrapolate from that what you want. But you can go to this website as of right after this talk and download the code for this and all the instructions on how to build it.

So have fun.
