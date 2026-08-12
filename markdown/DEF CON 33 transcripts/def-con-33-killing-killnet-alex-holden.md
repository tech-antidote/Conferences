---
title: "Killing Killnet"
speakers: ["Alex Holden"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Killing Killnet - Alex Holden.eng.txt"
sha256: "a32eba83f74ec9153d5bc458440fd2da3e87a7519ad258a644790cb951b83774"
duration_seconds: 1298
words: 3016
text_chars: 17308
redacted_secrets: 0
converted_at: "2026-08-12T06:24:14Z"
---

# Killing Killnet

**Speakers:** Alex Holden  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (21 min, 3,016 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Right now, this talk is called Killing Killnets with Alex Holden. And please give him a big round of applause. Here's Alex. Well, hello, everybody. It's a pleasure to be here speaking at DEF CON. This is an interesting personal story that I want to share with you guys. So it's going to be quick, technical, interesting. And rather adventurous. By the way of introductions, hi, my name is Alex. I was born a great many years ago in the wonderful city of Kiev, Ukraine. My family were refugees from former Soviet Union. And we came to Milwaukee, Wisconsin 36 years ago, where I spent the rest of my adult life. And professional career. I've been doing cybersecurity for my entire professional career. And the last 15 years, I spent tracking down the bad guys. Tracking down, figuring out what they're up next to. And I have a number of fun, interesting stories to tell. But definitely the highlight of my professional resume is this.

I've been making Vladimir Putin mad since 2014. Almost 11 years ago to the date. We were on the front page of New York Times showing what is still one of the biggest breaches in history. Perpetrated by Russian hackers. And Vladimir Putin was not very happy about this. Apparently he put me on his naughty list. And I probably shouldn't be going to Russia anytime soon. As a retaliation, I put him on my sanctions list as well. He's not allowed inside my house. He can wait in the garage while me and a couple of my friends from Ukraine will figure out what to do. But this story is not about him as much as we feel that we do a lot of good things. And we have some archnemesis. He's not one of them, but this is a story about a person, a group that consider me their archnemesis. And I want to introduce you today to Nikolai Nikolaevich Serafimov. This is a person that some people would think that just a normal guy from Russia looks normal.

He's a musician. He is a husband. He even will claim that he is a patriot of his country.


## [03:00]


He has actually served in Russian armed forces many years ago. And he would show himself as a patriot of that country. But the real face of Serafimov is not that. He is a bigot. He is a racist. He is a fascist, based on his statements. And he was also a leader and cheerleader of a group called Killnet. I'm going to tell you more about him under his nickname Killmilk. And also his group that he had named Killnet. The history of the group and their rise to power and infamy is really storied. They started their existence, their life in November of 2021 by running a distributed denial of service systems. And they would be attacking any target that they can hit. Their early targets were actually the Russian government. But just a day before the Russian invasion into Ukraine in 2022, Killnet actually declares its allegiance to the Russian government. And they are trying to push Russian propaganda and rhetoric through their actions as activists.

They have been attacking anybody who would be deemed enemies of Russia. And just imagine that before this time, four years ago, five years ago, ten years ago, it would be unthinkable if citizens of one country would engage in open cyber warfare against the other country. In fact, the Russian government, officials of Duma, which is the equivalent of our Congress, has been openly endorsing groups like Killnet, telling them that it's good to engage in cyber warfare against external enemies, including the United States. In fact, they also suggested that being a part of Killnet and similar groups is the equivalent of serving in the Russian armed forces. So Killnet is actually one of their claims to fame and infamy is about legitimizing activism and making it possible. They normalized cyber attacks from one nation to another, and we see this happening right now in the Middle East. We have seen it happening in other parts of the world, where the rulebook written by Killnet is actually being used in activists, malicious activists across the world.

They also did something highly unusual. They brought in activists, not from cyber criminal ranks, but actually from ranks of normal people. Imagine this, before the war in Ukraine, a lot of Russian citizens living in Russia were actually employed in companies in the West. In Europe, in the United States, there were just normal personnel, not only cybersecurity, but also IT. There were our developers, there were our system administrators. And with the war, Russia against Ukraine, most companies fired every single employee who resided in Russia.


## [06:09]


Meaning that a lot of these people became unemployed overnight, literally, and they have a grudge to pick, while still holding, some of them held keys to their old employers, technology and knowledge. So this was a movement that brought in IT personnel, people who never considered themselves cyber criminals or activists, but they have vendetta they wanted to pick. Also, there are some funny stories about being in Killnet. For example, one person wrote about his grandma, that she joined Killnet and in her spare time, maybe an hour a day, she sits behind her old computer in front of open Microsoft Edge and clicking reload button as quickly as possible, trying to create this DDoS attack. And while grandma can be really stopped by arthritis, the other cyber criminals were not as easy to stop. And this is really actually the new era of hacktivists. It also was based not only on technology, but also on propaganda.

On the left side of the screen, you can see the Telegram messages in Killnet's official channel on Telegram via Killnet, that had more than 100,000 individuals joining this channel, photoshopping members of Lockheed Martin executive team in caskets, showing what would happen to them and other employees of Lockheed Martin, Boeing and others because of their support of Ukraine. And you also see, and we heard on the news, that attacks of Killnet against our financial system, against our airports and other components were actually doing some damage, not only technology-wise, but propaganda. One of the most vile displays of their propaganda and attack vectors actually came in January of 2023 in this post. On the left side, the original, on the right side is a translation into English, where Killmilk, the leader of Killnet, actually called for attacks against the hospital systems in the United States, Great Britain, Germany and many other European countries.

The post scriptum in this call for actions, attacking hospitals around the world, were very simple. Kill them first. This is our enemy. This is a group of people, 100,000 strong, that were attacking not only our systems, but also the weak, the sick, disabled. This was an enemy that we, at Holt Security, my company, we actually formed a small group of nine people in 2022, trying to think of how to stop Killnet. And we figured out an interesting end, an interesting idea. In October of 2022, we saw an interview from a power-hungry and fame-infused Killmilk, leader of Killnet, in Russian state media called RT.


## [09:15]


He was doing an interview to one of the questions that he was asked about support from abroad. He named a group named Solaris from the dark web, and said that without this group, without their support, Killnet would not be able to move forward. So the way I read this is that if there is no Solaris, Killnet would not go forward. But there are a whole bunch of interesting things. Who is Solaris? Why are they tied to Killnet? And I know Solaris. I know Solaris really well. Solaris is a Russian dark web forum and sales system for illegal drugs trafficked in Russia. Designed by a guy named Zanzi in 2017, by the time we see this in 2022, it's one of the top three platforms on the Russian dark web to buy illegal drugs. And they operated over a thousand stores in hundreds of cities across Russia selling illegal drugs. Why would a hacktivist group be connected to this platform? This was an interesting question, but if you do a little bit of research, you find out that Killmilk is actually an ex-criminal who served time for his part in illegal drug operations in Russia.

Still, what can we do? And why would a cybersecurity company know much about Russian illegal drug trade? Well, really simple. Figuring out Solaris and other illegal drug trade platforms around the world actually gives you very interesting information. Illegal drug marketplaces are a great way to track malicious threat actors that are otherwise invisible on the dark web. Going out of this theory that cybercriminals in Russia often buy drugs, they use the same nicknames that they would on other places on the dark web, but we can actually figure out that they buy their drugs not that far from their home. They don't go into a different country or even a different city to buy their illegal drugs. So we can actually track their locations, and we've been doing this for many years. We also didn't have to hack Solaris. We wanted to, but we didn't have to. Because a great many years ago, about 2017-2018, Zanzi came to one of our alter egos on the dark web and said, Hey guys, I need help, because I'm having some issues with PHP code in one of my servers.

Can you help us fix it? And we said, of course we will take a look. So he gave us the root access to one of the servers. And we were very nice enough to say, well, you know, it's important we don't get locked out of the system just in case something happens. Can we install something to the failsafe switch? And he said, of course, go ahead, and we installed it backdoor. He said that we could.


## [12:16]


In case we get locked out. So, like vampires, we were invited inside, we were given the backdoor that we were using, and we've been monitoring Solaris for a great many years. Now, the Solaris system was not very simple, and it's actually a very complex ecosphere. Because in Russia, to buy illegal drugs, you can actually buy them from your credit card, or debit card. The only thing that you do within the Solaris system, you convert your bank account into bitcoins, which were, by the way, illegal in Russia at the time. But you can do this conversion and then put your money into the trade ecosphere. Whereas Solaris would be actually administering your money on that marketplace between the buyers of drugs, sellers of drugs, drug runners, drug dealers, shop operators. So, it was a big autonomous system that was operating there. And it was components of automation, it was components of monitoring, they actually had a store catalog, they had DDoS systems, because they helped with DDoS systems for Killnet, and a number of other communication tools there.

So, here's what we did. We only had access to one or two servers within their system. And it's extremely complex, very, very secure system, except that admins really love SSH authorization keys in .ssh files. So, we are able, using SSH session keys, to log into some of the servers. Those that we can't log into, we go to Ansible and use Ansible components automation to give us access. And those that we can't log into through Ansible or through SSH keys, we log in through Zumbix by running login scripts, because they would have to be monitored. So, before long, we come back and we take quite a bit of control over Solaris system. Still, we don't feel that we are empowered to do much, but we do one little thing. We let the drug dealers themselves push buttons to transfer funds within their systems to Ukrainian charity that helped elderly and sick in times of war. We were able to transfer nearly 50,000 U.S.

dollars from the Russian drug dealers to actually a worthy charity within Ukraine. And Forbes Magazine actually covered this story quite well. We also highlighted in that story the connection between Solaris and Killnet. This actually made us feel good, because the bad guys did everything themselves. We just created a situation for them to do this.


## [15:18]


Yet, this is not the main plot. Because Solaris replies quite quickly, and they actually make a statement saying that, hey, nothing could happen. Nobody hacked us, and we are still up and running. Then they said, well, don't read everything that you've seen on the Internet. Forbes Magazine was probably lying. And don't believe your lying eyes. It's provocation. It's manipulation. But just in case, just in case, they're taking the system down for maintenance to figure out what the heck is wrong. And after a week, they come back and they say, well, everything is fixed. There are no intruders in the system. Nobody can get into the system. So we go inside the system and try to see what they fixed, because they kicked everybody out. So we get into the GitLab server, take a look at what they actually changed. And they changed the onion address of one of their servers. They updated their logo and copyright, which is important.

And they changed their Bitcoin address as well. So they really secured the system from us. Three weeks after the Forbes story, we actually go on our site and we do one more post, now up-to-date, stating specifically our goal. To highlight the connection between illegal Russian drug trade and Killnet, a Russian hacktivist collective. And not only to say it in words, we actually published a lot of components, including components about the Tor nodes, monitoring components, their entire source code repository, including some of the database dumps and communication components, and some of their shops. So Solaris and their customers were surprised and confused, like this guy in the picture. But from the components, people started paying attention. Everybody was paying attention because this was real. And not only Solaris customers, but everybody around the world, including the Russian government.

So what happens afterwards? Solaris quickly gets taken over by another illegal Russian drug trade platform called Kraken. They actually use information about the Tor exit nodes and take over those for routing. Not much damage is done to Solaris except another vote to their reputation. Zanzi quickly hangs up his boots and leaves the project, and then Solaris fades to obscurity. They exist for a little bit in infamy, and longer than we expected. But about a year ago, Solaris finally calls its quits, and they no longer exist. So we took down the Russian illegal drug marketplace, which is okay, we're helping somebody. But the real goal was going after Kilnet, and guess what?


## [18:22]


In our research, we are seeing that this actually starts making sense. We are noticing that the Russian government withdraws its financial support of Kilnet. They are no longer supporting this organization financially. And this is also visible that the leader of Kilnet goes broke. Very quickly, he starts pawning his cars. In May of 2023, he actually files bankruptcy. And even his wife, we see from records, taking microloans to pay for her hair and for her nails, which is a real crisis. But in the public eye, Kilnet is in disarray. First, they say that they are now for profit. They are going to be charging people to do DDoS attacks against others. Which, I'm not sure how they are going to pay 100,000 people for this. They were in the chat all the time, so they abandoned that idea. Kilnet disbands. Kilnet says, I'm calling quits, everybody is fired, I will reform it again. But then he calls everybody in.

That time, they come back. Then KillMilk gives control of Kilnet to another hacker named BlackSide. And somebody says, hey, KillMilk, were you called BlackSide last year? Oh, he's like, never mind, it's just me, I was kidding. On October 6th of 2023, KillMilk and Kilnet call for peace. In the post on the Telegram channel, they actually asked to stop attacks against civilians and follow Red Cross guidelines. But that was October 6th of 2023. October 7th, after the Hamas attack against Israel, Killnet went back to war. And attacked everybody they could, including Israel and the United States. As of 2024, Killnet is no more. We are a Killnet channel on the dark web. Instead of having 100,000 followers, it only has 3,000 followers. And it's been sold by KillMilk, supposedly for about 10,000 US dollars, to a group called the Anon Club. And guess what the Anon Club does with this channel? You would never guess, they actually fight Russian illegal drug trade in that channel.

They dox drug dealers and stuff like that. Not sure where they got that example from, but that's what they do. Realistically, they're actually trying to get in good graces of Russian government. Or it's Russian government itself trying to do something to correct the mistakes they made. KillMilk himself gets doxed by the Russian media and very quickly fades to obscurity. He still considers me his enemy. Once in a while, he writes bad things, but that's okay. There's a story about winning. And winning is important. I'm not going to claim that we actually stopped Russian hacktivism. But we were able to find a kill-is-kill that took down a big 100,000 strong army of Russian threat actors.


## [21:29]


And while the hacktivism still continues, we feel that a small team of Ukrainian people actually made a difference. This is my story today, and thank you for your attention.
