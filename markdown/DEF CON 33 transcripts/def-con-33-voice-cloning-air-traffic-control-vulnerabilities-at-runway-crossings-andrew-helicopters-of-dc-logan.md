---
title: "Voice Cloning Air Traffic Control - Vulnerabilities at Runway Crossings"
speakers: ["Andrew 'Helicopters of DC' Logan"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Voice Cloning Air Traffic Control - Vulnerabilities at Runway Crossings - Andrew 'Helicopters of DC' Logan.eng.txt"
sha256: "ac6b5ee0050e69fb75a3515c103731720274e38a373cd50f37587b1113f0cc4b"
duration_seconds: 1355
words: 3321
text_chars: 18657
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Voice Cloning Air Traffic Control - Vulnerabilities at Runway Crossings

**Speakers:** Andrew 'Helicopters of DC' Logan  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (22 min, 3,321 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Please help me welcome Andrew Logan doing talks on voice cloning air traffic control. Woo! Thank you. Very excited to be at my 33rd DEF CON. No, this is my 4th DEF CON. And I want to start by saying my name is Andrew Logan. I am not a pilot, an air traffic controller or really even an aviation professional. But now that we're letting comedians make recommendations about how to fix airline safety, I figure I'll give it a shot. I am an audio engineer like Rob in the back. Give it up for Rob. And I was up here two years ago talking about tracking the military ghost helicopters of DC. That project relied heavily on Twitter. Let's take a moment of silence to remember Twitter. Now we're at copterspotter.com, but in that talk I was critical of the military's use of ADSB exemptions. Essentially turning off a safety feature to obscure their location with no national security benefit. And since a Black Hawk struck flight 5342 on January 29th, killing 67 people, lawmakers have become more receptive to critique on this issue.

And if this is important to you, I encourage you to take a photo of this slide, contact your member, and encourage them to support bills that broaden the use of ADSB. There are currently two in the Senate. But that is not what this talk is about. This talk is about my nightmare. And my nightmare is that a sophisticated attacker might use AI voice cloning technology to impersonate air traffic controllers and intermittently give false clearances to cross runways, particularly in adverse weather conditions. I think this could cause crashes or more broadly undermine the legitimacy of air traffic control. And if you haven't picked up on it already, when I was preparing this presentation, stories about FAA's dated systems were trending. So this whole presentation is themed VHS movie. So see if you can recognize all the VHS movies. And with that, we'll start with an FCC warning. Federal law prohibits transmitting on air band frequencies.

Do not do that. Couple disclosures, I've been in touch with the U.S. Senate Committee on Transportation, the National Air Traffic Controllers Association, that's the union for air traffic controllers, and via web form I submitted this to ICAO, that's the International Civil Aviation Organization, as well as CISA, FAA and FCC, who have not gotten back to me. So to begin with AM radio, I believe the reason this is used in air band is largely for interoperability.


## [03:05]


Countries from the 193 member countries of the ICAO have been using AM radio to communicate since even before its official specification in 1947. But I believe there are two features of AM radio that make it uniquely well suited for air band and uniquely vulnerable to this threat. The first is that AM allows for the heterodyning of carriers. What this means is that if you have two stations that are talking at the same time, let's say a plane and a controller, and they talk at the same time, they either hear each other, they hear a garbled mess, or they hear a tone. And any one of these three indicates that someone, both of them need to retransmit. So it's essentially like error correction for this analog system. Similarly, AM has a weak capture effect. And what this means is that you can hear the plane that's right next to you as well as the one that's way off in the distance and it may be well down in the dirt of the radio signal.

And crucially to this vulnerability, I want to note that AM radio is unencrypted and can be received by anyone within an expensive radio or an internet rebroadcast. And there are legitimate use cases for AM transceivers. That includes transmitting. And this might include aircraft that didn't originally have electrical systems, or perhaps pilots want backups, or maybe people on the ground are coordinating traffic with helicopters at a hospital helipad or a small airfield. And these sub-600 dollar transceivers put out about 1.8 watts. So you kind of need line of sight to make that work. However, as we know that the FAA is trolling eBay for parts, you too can be the owner of a defunct tower transmitter, really for under $200. It's pretty scary how cheap these things go. And when paired with an appropriate antenna, it offers an order of magnitude more power, 25 to 45 watts. And my fear is that an adversary with that power could transmit much further away from the airfield.

Now I talked to two manufacturers of this type of equipment at the air traffic controller conference, and interestingly the one that is based in Europe is subject to strict import controls and has to verify who they sell to, while the one that is based domestically in the U.S. does not have to verify who they sell to at all. So I believe there may be room for additional regulation on that front. A couple other modes that are worth talking about as potential fallbacks in this loss of trust situation that we might run into. HF radio has been used for a long time for transatlantic and transpacific flights.


## [06:09]


It's lower in the frequency spectrum so has better propagation characteristics. Though I don't really see controllers switching over to this in an emergency. ACARS is a digital text based system that... you're going to give me that much love, right? ACARS is a digital text based... you really get the full experience here. Thank you, thank you. I appreciate that, appreciate that. ACARS is a text based digital system that was originally specified for air crews to send hours back to their airlines. But now it is used for various messages from TFRs, which is temporary flight restrictions. Notams, which is notices to airmen. And automated diagnostic messages from the planes. These are now transmitted on a more modern kind of like backhaul system called VDL mode 2. This is a series of ground stations that connect on the aviation telecommunications network or ATN. They call this the Internet of Civil Aviation Authorities.

And it is 30 kilobytes per second, guys. This thing is fast. They did... the FAA had proposed a VDL mode 3 that would include voice, but it was never adopted. So these are text based systems that are on this backhaul as well as controller pilot data link communications, which is CPDLC. This is a very modern text based either preformatted text or free text that is exchanged between controllers and pilots. And probably our most practical emergency backup should VHF radio go down. But what we're really trying to get to, the solution to this problem is L band digital aeronautical communication system or LDACS. This is currently being tested in Europe. We don't think we're going to see it here until 2030 at the earliest. It is... has a lot more data throughput, embedded navigation capability. It works on a series of ground stations as well as satellites when you're overseas. But it's encrypted.

So, if a lot of this went over your head, I will make you an analogy. The VHF radio that we controllers use now, if that's a telephone call, then HF radio is like a long distance call. ACARS is like a fax machine. VHF VDL mode 2 is like the cellular network that's a modernization . It carries CPDLC. That's like a text message. But what we're really trying to get to is signal. And we all know why we want to get to signal. It's encrypted. All right. So there are some interpersonal elements of ATC that are worth noting here. At first I thought that ATC might be a single factor trust system. But there are a couple things you have to meet to be trusted on the airwaves.


## [09:10]


First you have to transmit on the right channel. And bigger airports have several channels for different phases of flight or regions of the airport. You may need the right voice. Although in talking to pilots, I found that controllers actually switch out between shifts without any warning. So it's likely if you met all the other criteria, you may be trusted even with a new voice. As long as you have the correct syntax, that's basically that you talk like an air traffic controller and format your calls the correct way and meet the expectation or timing that you say things at the right phase of flight or response to a prior request perhaps. So there are a couple FCC enforcement techniques that we know about. The first is they employ direction finding vehicles to find people who are misusing the airwaves. In problematic areas, they've been known to use fixed direction finding stations. But at the end of the day, it requires a field agent coming within a few hundred feet of a problematic transmitter.

And we know that in cases where there have been malicious actors on air band, that results in an apprehension. While lower things may result in a sternly worded letter that is published and public. And I read a lot of these. And it tends to be people who have 5 gigahertz access points outside that are interfering with weather radio. But it also can include amateur radio and pirate radio stations that are either on the wrong frequency or have spurious emissions, which is basically resonant frequencies that are interfering with air band. I mentioned intermittent interference. And the reason I believe this is important is because we all know this trope of tracing the call in horror movies. And we know that doesn't really, that's not how it works on the telephone system. But it is kind of how it works on the radio system. Because the longer you stay on the line, the better chance you're giving FCC to find, I say you, a bad actor in this case.

And so my real worry is that someone could operate intermittently and only transmit once or twice a day. And that would be quite a challenge to track down I believe. So voice cloning. Many of you are probably already familiar with this already and the threats that it poses to industries like banking or defrauding my parents. It is a three part process from a technical side. First an encoder finds the unique characteristics of the voice you're cloning. A synthesizer takes the input text or prompt and applies that voice to it before a vocoder converts that spectrogram that's generated in part two back into an audible waveform.


## [12:14]


But I don't believe that an adversary would need to have this level of technical knowledge, use an open source technology or roll their own because there is such a plethora of free or low cost voice cloning technology available at the moment and many of it does not have the necessary safeguards. I used 11 labs for this upcoming example and I did find that they have one guard rail which is that they verify your identity before you clone a celebrity or a public figure. And I find this encouraging because they have the ability to use guard rails and I would encourage AI companies to install guard rails for either voices that sound like they're coming off a radio or prompts that are in the format of air traffic control or a combination of the two. I'll also note on this slide that Sam Allman recently gave a talk in front of bankers where he acknowledged the threat that AI voice cloning poses to the banking industry but stopped short of recommending a legislative fix.

So I really think that industry is going to have to take the first move on installing guard rails in this situation. So now I want to talk about why I believe runway crossings are most at risk and we're going to have a little history lesson. We start by going back to 1977 to the Tenerife disaster. This is the deadliest disaster in aviation history and kind of a wild example of the butterfly effect. It all started when separatists detonated a bomb in the terminal of Grand Canaria Airport which is in the Canary Islands, part of Spain. And this resulted in eight fatalities but the diversion of all these flights from a major airport to a single runway airport, Los Rodeos in Tenerife. As a result, controllers had to park flights on the taxiways and taxi flights one at a time on the single runway, which I'll note is not incredibly unusual for a single runway airport, but under this condition and the rush that pilots were in to get back to Grand Canaria when it reopened, and a thick fog that had descended on the runway, obscuring the visibility of controllers, kind of set the stage for the situation where a KLM flight misheard their takeoff clearance.

And instead of clarifying, they also ignored a heterodyning artifact of a Pan Am flight saying that they were still on the runway and they began their takeoff and collided with that Pan Am flight in a real tragedy that was created from really a single miscommunication and some adverse weather. Ironically, at the end of the day, the separatists who set off the bomb at the beginning of this story denied responsibility for this incident.


## [15:21]


So a more modern example is in 2024 where at Haneda Airport, which is near Tokyo, and this was JAL flight 516 that was coming into land and collided with a Japanese Coast Guard airplane that was crossing the runway, believing that they had received takeoff clearance again. And there were a couple things that could have, that went wrong here. First, the JAL flight and the controllers failed to visually identify the runway incursion despite clear conditions. Second, investigators found that an audible tone, an alarm was heard in the tower for over a minute that was the radar that detected the runway incursion. And third, there are stop bars installed on the runways at Haneda Airport. Stop bars are embedded runway lighting that serve as a stop sign to pilots that is taught to be observed above any clearance given by air traffic control. However, they were unserviceable on the runway that the Coast Guard was using that day.

So in aviation, they frequently use the Swiss cheese model, which is when you put up various fail safes to stop all the eventual hazards. But unfortunately, in this example, we found out what happens when one of those safeguards isn't in place and a hazard manages to make it through those Swiss cheese holes and a real tragedy occurs. Now, the silver lining is that 367 passengers and 12 crew were able to evacuate this plane before it burned to the ground, but the Coast Guard flight sadly did not fare as well. So I want to introduce a simulation here that I created at JFK Airport. In this example, you're going to hear Speedbird, which is a call sign for British Airways, really one of the best call signs, and they are holding short of 22 right. There's traffic landing in front of them, but they're being coordinated on a different channel, so we don't hear them. Second, you will hear the flight being told to land behind them.

That's jet blue. And then you will hear a beep and you will hear the audio that I cloned. So what I want you to listen to in this example is the characteristics of the controller's voice. Here we go. Speedbird 173, Juliet, hold short runway 22 right. Roger, roger, 22 right, Speedbird 173, outbound. Jet blue 1436, go ahead and call in heavy Boeing 777, runway 22 left, call in. Left, left, jet blue 1436. Speedbird 173, Alpha Heavy, cross runway 22 right without delay.


## [18:24]


So that third, after the beep, was a voice clone that I created using only the ten seconds of the previous two calls that you heard. So it only gets better the more you feed it and it is trivially easy to create a convincing voice clone, particularly when you're about to transmit it over a radio that's going to obscure it further. Just to give you another chance, I'm going to play this example again, but I'm only going to play the first call from the controller and the cloned audio. And in this example, I want you to imagine that you are Speedbird waiting to cross this runway and you have no visibility of what's in front of you. And think to yourself if you would trust the voice after the beep. Speedbird 173, Alpha Heavy, Juliet, hold short runway 22 right. Speedbird 173, Alpha Heavy, cross runway 22 right without delay. So again, pretty scary. Radio, the air band radio is a simplex system which means everything is heard on a single channel.

And so controllers would hear their own voice being played back to them and that would be disconcerting. And we don't know how controllers would react to that, but I think we can take some example from this incident that happened at Cincinnati airport where a man on a helicopter heard the words go around one time and that created this audio. So how are we to verify instructions when the voice that we hear is that of the air traffic controller? It's really difficult. And this brings us to mitigation and I think that the first thing we can do is get this information in front of as many pilots and controllers as possible and I hope that's what I'm doing here today. From a technology perspective, I think that the FCC could do some threat modeling about airports that have the most adverse weather. This is just some data I pulled of the ones with the most weather delays. And then looking at rental properties like hotels and apartments that have balconies that face the runway because I could imagine a scenario where an adversary is operating equipment remotely from another country from a rental property.

We talked about stop bars in the Haneda example. Again, it's a stop sign. It's to be observed over any clearance that they receive so this would be a very effective mitigation and we have them at 26 U.S. airports and we're trying to get to 75 by 2026 but we are behind schedule. I'll also note about this in my research I found that these are radio controlled so there's another problem.


## [21:24]


And I know some of you are thinking in your head, but we have TCAS, man. TCAS is the traffic collision avoidance system and it is possible for it to detect a collision of two aircraft and automatically divert them but it is inactive under a thousand feet so it plays no role in takeoff and landing. What would help is enhanced flight vision systems which are installed on many cargo aircraft because they operate frequently at night and this includes forward facing cameras, infrared cameras and radar that would really help with situational awareness during those critical phases of takeoff and landing. So in conclusion, I really hope that this brings this problem to the attention of pilots, controllers and regulators. I want to thank the DEF CON CFP board for having me again. I want to thank my colleagues at the aerospace village for their kind of validating this idea last year and I really want to thank all of you for coming out on 530 at 5.30 p.m.

It is really great to see all of you and I look forward to connecting with you out here. Thank you.
