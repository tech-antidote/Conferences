---
title: "Making the DEF CON 33 Badge"
speakers: ["Mar"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Making the DEF CON 33 Badge - Mar.eng.txt"
sha256: "d06bd2658c9b7063520f01b124b6d7015cdb49d060c9e36eb2050c2fcd20b97c"
duration_seconds: 730
words: 1925
text_chars: 10221
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Making the DEF CON 33 Badge

**Speakers:** Mar  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (12 min, 1,925 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Hi, welcome. It's actually kind of nice to see not so many people out there in the audience. It's a little scary when it's full. Not as much drama on the stage as last year. Not electronic years are a little bit more mellow. Okay, so... oh, first off, I want to recognize that we stand on southern Paiute land. I'm a citizen of the Choctaw Nation of Oklahoma, but we should all be standing up for indigenous rights. All right. And... that's the button. Okay. All right. So, my name is Mar Williams. You've seen my art around Con for many years. My first art was DC-17. I've led development teams as a UX designer. I've chaired hackerspaces, and I've run a collaborative gallery, and I opened a new gallery in September called Feral. If you're in the Denver area, please come check us out. I did the design for the DC-31 badges and the DC-32 badges and ran the 32 badge team. You can find me in the vendor area or check out my Patreon, and I'll put up a slide later for that.

This year's contributors, Bonnie Finley, who did the 3D modeling of the badge, so transformed the designs into 3D that we could use for manufacturing. ICSN is our manufacturing partner and design support so that everything flows just right with injection molding. It can get really tricky. Amy Valentine and Bonnie Finley did a lot of work on the black badges, and I can't show you those just yet, but you'll see them, and they're super cool at closing ceremonies. Thanks to Will Tuttle, who's my best friend and gets to listen to me rant and pull my hair out throughout the year. So, thanks to him. And Sage, who is my monster up here for inspiration and testing every time a prototype comes off the 3D printer, and I hand it to them, and I'm like, hey, what do you think of this? So, all right. Okay. So, one thing I want to speak to you about design, and something that I want to speak to you about last year, and where this is hard to talk about, because I wrote this talk, like, 30 minutes ago.

So, bear with me here. So, design and art, design and usability in UX design, it's this whole enchilada. It's this huge zoomed out thing, right? So, it's not just, like, you put art on something and it's done. There's a whole lot of... one of my titles over the years was human factors engineer, which is super dorky title, but it really, like, encapsulates how much work goes into the badge experience.


## [03:05]


And so, that's kind of what I wanted to speak to you about badge design last year, and how, you know, we had a hardware contractor who was just one small part of that puzzle. And it wasn't a very small part. You know, it was significant. But that there's many layers of this. There was also an entire game development team making a custom game last year, and I just wanted them to get the credit that I couldn't speak to last year. You know, I put everybody's names up, but with the drama, everything got lost. So, I just wanted to touch on that and, like, thank those collaborators again for all the work that they put in last year. Okay, in design, in this whole enchilada design, the majority of this work is invisible. And you just kind of see the finished product. And sometimes just the problems that come up along the way is, like, this year we've got a screw instead of a rivet. And so, it's causing some problems with badges falling apart.

And these are last-minute design decisions that come with the timeline and having to choose parts very quickly when, you know, getting 28,000 of something, even just a screw or a rivet, is pretty challenging. I have endless respect for the badge designers before me. As the badge project has grown over the years to scale the conference itself, it's become more of an electronics project, right? It's a massive undertaking with so many moving parts, several different teams. Okay. So, just want to speak to that. Okay. So, this is kind of where I started out. I had this idea that was inspired by a jeweler's lens. If you've ever seen one of those where the little parts slide out. I had also taken some inspiration from the wings of a beetle, like a scarab beetle. So, you can kind of see your badge splays out like little wings. And I had some concept designs along the way that were more beetle look.

But I think it distilled down into this one. But still captures a little bit of that inspiration. I love color. And I love, like, color theory and how this all works. In 2016, I did a Denver Art Museum residency for four months. And there was a lot of exploration of additive versus subtractive color. And there's so much crazy making when you get down into the little details and weirdness of color. And so, some of the stuff that went into this badge was getting, like, the opacity just right. And getting just the right shade of magenta, you know? So, just lots of tweaking so that these so that this badge would work. So, if you notice around the con, there's art that interacts with the badge. And I have a cat. If you take the magenta and the yellow lens together and look at this cat, the skeleton is gonna pop out to the forefront. When it's up on the screen, you can also do blue, which in light, it's different than... Anyway.


## [06:05]


So, the blue and the red lens together can get you, like, a really nice dark blue. And then you'll just see circuitry on its face. And if not, you can just switch to the cyan lens. So, there's some tricks there that were fun to dig in. Yeah. I'm gonna go back a little bit here. Yeah. So, if you layer up the CMY lenses, then you get RGB, which is just... It's just really neat and fun. So, I really wanted to do something with that concept. So, you can do, where you have, like, the red decoder from, like, a cereal box. And 3D glasses. And there's some examples of that in the signage. Where you have the cyan lens. And then, again, you take the magenta and yellow, put them together, and you have the red lens for the other side. Part of the design was you have to be able to hold it up to your face. And so, kind of the size form factor is because I wanted people to be able to hold it up like this and do the... Oops.

Got the wrong lenses on here. Like this. Yeah. All right. And then, if you want to see a really cool example of this in video movement format that's actually done not with lenses, but with RGB lighting, I highly recommend checking out Jason Levesque as an artist. I really dig. And he did something in Norfolk called Transparent Seas. So, here's our first, like, 3D rendering of the badge. So, then how we got from sketches to this was a lot of back and forth with Bonnie Finley and 3D printing over and over and over again. Yeah. Okay. So, some of the challenges this year, literally right before we had to ship the badges, I'm sure you guys noticed that there was paper badges this year just for a minute before we got the rest of the shipment in. There was a typhoon in Vietnam. And it knocked out power to the factory for 11 hours. And that was during the period of time where the bulk of the badges were being made.

So, that caused significant delays for us. Tariffs. Tariffs were a crazy problem that we didn't know was going to happen. And Vietnam was hit hardest of a lot of places. And then that also impacted our timeline because people were, like, trying to book these shipments that were all happening at the same time because they were all trying to beat the new tariffs, right? So, we had to compete with all the people shipping around the first. So, that was tough. And that really impacted everything. And ICSN really came through with getting everything here as close to on time as we possibly could. Okay. Here's an important thing that I've been wanting to say for a minute.


## [09:09]


I think it's important that it's said. I don't want to romanticize the idea that the badge designer can overcome all the odds and bring this crazy project to completion in such a short time and that that's a good thing. This isn't a measure of my value. I take no pride in sacrificing sleep and well being. And I don't think that people out there should be doing that with their projects or companies or whatever either. Like, take care of yourselves. Any manufacturing project at this scale, whether it be electronic or non-electronic, is almost impossible in the timeline of one year. So, there's no room for errors, proper testing. There's manufacturer issues along the way that we can't address. Sourcing the right parts, that's also a challenge where we have to keep switching up what parts we're using. We have to switch up even just, like, the dyes that go into the plastics. Things like that. Because one manufacturer can't get them.

There's, yeah, so there's no room for error. And no room for real testing. Like, I was still drawing designs, like, right at the end there and trying to push them through before things had to get printed. You know, and much love to DEF CON and all of that. But I personally will be moving to a two-year badge cycle. So, next year I won't be doing the badges so that I have a whole two years to do this well. Because I just want to do hacker stuff with my friends. I put this slide up last year. And working with DEF CON, working for DEF CON, anybody who works with conferences knows that, like, at a certain point, you don't get to go play anymore. And so, I just really wanted to play. So, I squeezed in a little bit of time to do a badge challenge this year. So, you can find me near the arts and entertainment booth in the vendor area. And I have a big stupid pumpkin with buttons on it. And , yeah, come check it out.

And press some buttons. And I hope you can figure it out. Yokoki, please support me on Patreon. It's Patreon slash Spux. Follow my Instagram. It's Spuxo. Yeah. So, I post all my art there. Yeah. And come support me in the vendor booth area. I have shirts and stickers and all kinds of things. Yeah. So, if you have any questions, let's see if I can see pass this really bright light. All right. I guess that's it then. Thank you so much. I can't wait to see all your badge life stuff. This has been a great con. And we still got, you know, all this time today and tomorrow left.


## [12:10]


Thank you.
