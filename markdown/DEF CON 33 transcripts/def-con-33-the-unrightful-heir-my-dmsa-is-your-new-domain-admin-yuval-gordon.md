---
title: "The (Un)Rightful Heir - My dMSA Is Your New Domain Admin"
speakers: ["Yuval Gordon"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - The (Un)Rightful Heir - My dMSA Is Your New Domain Admin - Yuval Gordon.eng.txt"
sha256: "08a42d565374cc64f262d9b95745a24ca3a2ecbc3b84a146987d00edefcb37b0"
duration_seconds: 2009
words: 4509
text_chars: 24185
redacted_secrets: 0
converted_at: "2026-08-12T06:24:14Z"
---

# The (Un)Rightful Heir - My dMSA Is Your New Domain Admin

**Speakers:** Yuval Gordon  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (33 min, 4,509 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Okay. So Tote is going to be talking about Active Directory and something. So let's give him a welcome . Yeah . Wow. Hello, everyone. Welcome. Thank you so much for joining. So this is actually my first time talking. I mean, this is actually my first time actually being in an international conference. So talking in DEF CON feels like a dream. So anyway, today I'm going to talk about a vulnerability I found in Active Directory. And before we actually get to the vulnerability, let me start with some background. So I found this vulnerability while doing a research about DMSA. And three years ago I also did a research on GMSA. Now, there is just one thing that I couldn't figure out about MSA. Because I can, like, I mean, after I did research on both of them, I can say that I have a grasp of how they work. But the thing that I just couldn't figure out was why the D in DMSA and the G in GMSA are lower case.

And the at first I thought this is just because I'm not an English speaker. So when I worked on GMSA, I asked like a ton of people why the G is lower case. And so I'm telling you this story just so you know that if at some point during the presentation you will ask yourself why it is written that way, I have no clue. And yeah, so I'm Yuval Gordon. I'm a security researcher at Akamai Technologies. And in the past decade or so, I've been working on different roles in cyber security. But the one domain that I keep coming back to is identity research and active directory. And so in Akamai, I'm now doing an offensive research. So that's how I got to this research. And that's my X handle over somewhere. So feel free to follow me or reach out to me. And okay, so let's get started. So we're going to start by with a quick introduction of service accounts. So this is just to make sure that everyone has some understanding of what service account is.

And then I'm going to do a deep dive to GMSA. I'm going to explain exactly how they work and where I found the vulnerability. And after that, I will be talking about that successor, which is the name of the technique that we use to exploit this vulnerability. Okay, so in order to explain what a service account is, I'm going to use a story by Elad Shamir.


## [03:07]


So Elad Shamir is, I think, the VP research of Specter Ops. And he has some talks related to Kerberos. And in his talks, he has this concept to explain about Kerberos and different things in Kerberos. And I just really love his story. So I really recommend you guys to watch his talks. But for now, I will just summarize the relevant parts for us. So in his story, Elad is talking about this amusement park. And in this amusement park, there are, you know, visitors. And when a visitor enters the park, they get a daily ticket. So the daily ticket, it's like a TGT in Kerberos. And so in the park, we have a lot of different rides. So every ride, it's like a different service. And service, for example, can be a web application. So when the visitor wants to get on a ride, they need a ticket for that ride. So actually, the daily ticket that they got is not enough to get on a ride. Each ride requires a different ticket.

So what the visitor has to do, they go to the ticket office once again, and they now ask for a ticket for the specific ride they want to get on. And so when they get the ticket, they will go to the ride operator. And this will be the main focus of our talk today. So they will go to the ride operator with this ticket, and they will hand it the ticket. So the ride operator will validate the ticket. They will, so the ticket has some information about the user. So it will include the age of the visitor and the height of the visitor and maybe the different membership, like maybe this is a premium user and the ride operator will validate it and decide whether the visitor should be allowed to get on the ride or not. So maybe it's like a premium ride and the visitor can't actually access it. So that's the purpose of service account, kind of. So there are different types of service accounts. We have the legacy type of service account, the unmanaged type, and we have the managed type.

So actually the legacy service account, they had like a lot, they have a lot of security risks involved with them and the most major one is that they are a target for an attack called Kerberos thing.


## [06:08]


So this is a widely used attack, very common today. Attackers love it. And in 2008 and 2012, Microsoft introduced MSA and then GMSA and we will refer to both of them as MSA because for the sake of our talk, we don't really care about the differences between them. So MSA actually solved the security risks that were related to the legacy service account. But if that's the case, you might think that it's pretty weird that I'm still talking about legacy service accounts more than a decade after MSA were introduced. So the reason for that is that unfortunately, GMSA just didn't take over. So let's talk about why that is the case. So the first and I think most major problem with MSA is that they are just not fully supported. So for us to configure a service , to configure an MSA for a service, the service has to support MSA. And if the service doesn't support MSA, well, we can't just do it and then we have to use a legacy service account.

And so the other problem is that even if the service does support MSA, so say we have an existing service that is running with a legacy service account because we have our environment for like decades. So it makes sense. We couldn't done anything before. So now we want to have this service that uses the legacy service account use MSA. Well, that's a pretty difficult task. It will require a lot of time and work from the IT team. And if they will have some mistake, if they will get something wrong, the results can be down time for the service. And some services are too critical to risk with this kind of risk. So that's a problem . But luckily for us, just recently in 2025, Microsoft introduced a new kind of MSA , DMSA. So DMSA is delegated managed service account. It's a new type of MSA that has all of the advantages that the previous types of MSA had. But this time, the IT team can just lay back and relax.

Because there is a really new cool migration process that let IT teams take an existing legacy service account and migrate it into a DMSA. And every service that uses the legacy service account will now use the DMSA. And it doesn't matter if the service supports MSA or not, it will work. And it doesn't require much work from the IT team.


## [09:10]


It's pretty straightforward. So they can't make any mistake there. So it's pretty amazing process. And one more thing about DMSA, Microsoft documentation says, I'm not sure if you can read the quote, but DMSA secret can be retrieved or found anywhere other than on the DC. So when I saw this sentence, it was pretty weird for me. And we will get to this sentence back later because I think that we can debate on if this statement is actually true or not. But that's for later. So let's talk about the migration process. So we can actually divide the migration process into three phases. At first we start the migration. Then we have to wait. And then we complete the migration. So before actually talking about each of those phases, let's start with how authentication looks like before we even start the migration. So we have a server on our left, an SQL server. And that server is running an SQL service.

And we have configured a legacy service account for that service. So the name of the legacy service account is SBC SQL. And when the service will ‑‑ so the service needs to authenticate and for that it will request to authenticate as SBC SQL. And the DC will respond with a TGT. Okay. So that's nice. So now let's start the migration. So when we start the migration, what happens is we have now a new DMSA. I have created a DMSA. I called it DMSA dollar. And we started the migration. So what happens is the two accounts get automatically linked. So each account is pointing to the other. And also the legacy service account is granted the right permissions on a certain attribute on the DMSA. So this attribute is a pretty critical one. It controls who can authenticate as the DMSA. And I will explain why the legacy service accounts need these permissions in the next slide. So, okay, we have started the migration process and now we are entering the waiting phase.

So what happens during this phase, so when the server is authenticating now, when the service will try to authenticate as SBC SQL, it will get a TGT in response once again. This time, however, the response will include some additional information. So the additional information will have a message saying that this user will be soon superseded by DMSA dollar.


## [12:15]


So when the Kerberos client, which actually handles all of the authentication for the SQL service, so when the Kerberos client will see this message, it will automatically send an LDAP modification request to the DC requesting to allow SQL server, which is the server we are currently running on, to be able to authenticate as the DMSA. So we are, so the Kerberos client is doing that to make sure that the server will be able to use the DMSA after the migration will be completed. And this is why the waiting phase is actually there. So we want every server that is currently using this service, this service account, sorry, to authenticate with the service account and get the permissions to actually access the DMSA for the moment that we will complete the migration. So at this point, we need to wait. So, okay, we are waiting for about a week. Then we complete the migration. And when we complete the migration, we have the legacy service account.

And it gets automatically disabled. And some Kerberos configurations are being copied to the DMSA. Okay, so let's look at what happens during authentication now. So once again, the service is configured to run with SVC SQL. So it will try to authenticate as SVC SQL, but this time the DC will respond with an error because, and then the error will have some additional information. So the error was because the user is disabled, but the additional information will say that this user is superseded by DMSA dollar. So when the Kerberos client sees this message, it will just try to authenticate automatically as DMSA dollar. And because we allowed SQLSRV to authenticate as the DMSA, it will work and the DC will reply with a TGT. So that's great. And almost everything I just showed is from Microsoft documentation about DMSA. But there was this one thing that they didn't mention at all. So it really bothered me because it's a really critical thing.

So this thing is privileges. So we have a legacy service account and we have a DMSA and I said that there is a really cool new migration process that, you know, migrate the service account to the DMSA. But I expected the permissions of DMSA to be the same as the legacy service account. But the process was pretty weird. So in order to understand what happens, let's talk a bit about Kerberos privileges.


## [15:21]


So in Kerberos, in Kerberos TKET, we have a structure that is called the pack and our privileges in the domain are determined by the pack when we authenticate with Kerberos. So in the pack, we have some information about the user and also a list of every group that the user is a member of. So we had the legacy service account and they were a member of several groups. And so that was like their privileges in the domain. And now I've created a new DMSA. I completed the migration process and I checked whether the DMSA is a member of the same groups. And well, the DMSA is not a member of any group. So by this logic, I can expect the pack of the DMSA to look like this. But if that's the case, that's a huge problem because it means that those two users don't have the same privileges in the domain and therefore the service wouldn't work as expected. So I guess Microsoft engineers have watched Dragon Ball, same as me, because they too knew that when a problem is just too big, there is only one solution, which is fusion.

So the pack of the DMSA actually looks like this. So what this is doing, when we authenticate as a DMSA, it will build a pack for the DMSA just as we can expect. But then it will also check if the DMSA is linked to another account. If so, the DC will also generate a pack for the other account and will just merge the two together and that way we will have a pack that has, I mean, that way the DMSA will have the privileges of SVC, SQL and the exact same privileges. Okay, so when we saw that, we thought that this is like really interesting because I have never heard of any mechanism in Active Directory that just let you copy the privileges of one user, give it to another and without changing any group membership or something like that. So I thought this was really cool and I wanted to know whether I can abuse it or not. So, spoiler alert, I did abuse it. But before actually talking about how I abused it, let's talk about how the migration process, like how we start the migration process.

So, Microsoft documentation says that in order to start a migration process, we need to execute this partial commandlet. Now, if you will try to execute this partial commandlet as a non-domain admin, well, it will fail because Microsoft probably thought about it.


## [18:23]


They don't want regular users to just migrate a legacy service to DMSA. It's problematic. Okay, that makes sense. So, let's understand like why it is failing. What is happening when we execute this command? So, apparently this command is just a wrapper for an LDAP operation. So this is just basically a request that we send to the DC to invoke some functionality. And, well, if you will try to manually send this LDAP operation, this request to the DC as a non-domain admin, it will fail. Yeah, sorry, forgot the animation. So, what happens is that on the DC side, there is a verification and the DC checks if the color of this LDAP operation is a domain admin or not. And if we're not a domain admin, it will just fail. So, again, it makes sense. Microsoft don't want us to just migrate services, service accounts. So, at this point, let's understand what the DC is doing when this functionality gets invoked.

So, what the DC is doing is actually just changing some attributes. So, it changes attributes on both the DMSA and the superseded user. So, at this point, what we want to check if, like, if we have control over the DMSA, maybe even if we don't have domain admin rights, maybe we can just write to the same attributes and, like, you know, mimic the migration process and apparently that just worked. So, if we change an attribute on the DMSA, that DMSA is now linked to whatever account we want. There is no protection from that. So, even if the account is in the protected users group or, like, I don't know, there is the account sensitive and, like, cannot be configured for delegation. So, that won't work as well. I mean, I can link the DMSA to any account I want and just copy the privileges of that account to my DMSA. So, that leads us to bad success. Okay. So, let's go over the attack flow. So, we have an attacker and that attacker has a control over a DMSA and their goal is to achieve domain admin privileges.

So, what the attacker will do is they will just simulate the DMSA migration. So, they will link the DMSA to another user, a domain admin, and then what they have to do is to authenticate as a DMSA and the DC will just grant them the privileges.


## [21:27]


So, okay, that's nice. The attacker achieved their goals and that's pretty bad. But, actually, I mean, the starting point, that's not trivial at all because, I mean, first of all, DMSA is a brand new feature. So, I mean, most organizations don't use it. So, gaining control over an existing DMSA is a pretty difficult task. But, also, the DMSA by default are being created in a container called a managed service account container. So, this container is highly restrictive and if we're not like tier zero accounts, we probably don't have control over this container or any object inside which includes the DMSA. So, okay, that's not like a really strong attack. But then we figured that while DMSA by default are being created in the managed account, in the managed service account container, they don't have to be created there. So, apparently, we can create DMSA in any OU. So, OU is organizational unit and basically this is like a folder in active directory.

And so, some folders may be considered like as, you know, less important because maybe they don't have any important object inside and maybe there is a team that consistently annoys the IT team in requesting to do stuff in that OU. So, the IT team will just grant this team permissions over the OU. I mean, it's their OU so they can just manage it and what's the worst that can happen, right? So, that's the worst that can happen. So, now the attacker has control over an OU and they will just create a DMSA there and the rest of the attack flow will be the exact same. So, now let's see a demo of this attack. Okay. So, we are running as a weak user and we will try to add ourselves to the managed meals but we fail because we don't have permissions. So, now we see that we have privileges to create an object inside of the temp OU and we will create a DMSA in that OU. And now we will link this DMSA to the administrator account.

Okay. So, the DMSA is linked and now we need to authenticate as the DMSA. We will use Rubius for that. So, now we can see that we are authenticated as the DMSA. We will try to add ourselves to the managed meals once again. This time we succeed as we are running with administrator privileges.


## [24:33]


Right. That was a great time for drinking water. Okay. So, we have reported this vulnerability to Microsoft and they agreed with us that this is actually a vulnerability. And so, they said that if we have an attacker and that attacker has a control over an OU and from that they can just gain the privileges of any account in the domain and basically just own the domain. This is a moderate severity vulnerability. And because of that, it does not meet the bar for immediate servicing . But, however, they did say that they will fix it in the future. So, yeah. But that's actually not the end of it. So, when I started with the research, I saw this structure. So, this structure is a structure that, okay. So, the TGTs for DMSA includes this structure and this structure holds two very important fields. It holds the current keys and previous keys of the DMSA. So, in the current keys and previous keys, there are the Kerberos keys for the DMSA, which are basically credentials.

So, we can think about it as the password hash of the DMSA. And when I saw it at first, I thought it makes, I mean, I thought this is, I mean, it makes sense. The machine actually needs the credentials of the DMSA to do different stuff. And I didn't give it any attention until I saw this response. So, I hope you guys can actually see it. But what happens here is we have a decoded response. So, this is the Kerb DMSA key package structure. And we have the current keys and previous keys. So, in the current keys, we have the existing Kerberos keys of the DMSA. I have just created and simulated the migration linked to the administrator account. And we also have the previous keys. So, that's pretty weird because this account is, I have just created it. It doesn't suppose to have a previous password. So, that's weird, but I actually didn't notice that. What I did notice is that the value in the previous keys, and again, maybe you can't actually see it, but that's okay.

It's just an NTLM hash. And usually I wouldn't recognize a specific NTLM hash, but I did recognize this specific NTLM hash because that's the NTLM hash of that password.


## [27:36]


And this is the password that I always use. I mean, in my lab environment, yeah? So, when I saw the NTLM hash of that password, I immediately recognized it and I thought it's, it was like really weird. Why the DMSA that I have just created and DMSA is this, you know, it's so secure and it has like randomly generated password. So, why does it have a previous password that is AA126, my default password? So, apparently what happens is when we link a DMSA to another account, we are not only stealing their privileges, we are also getting their credentials as well. So, that's pretty cool, I think. And that, of course, was the password that I configured for the administrator account. As again, I always use it. So, I created a tweet about it and in this tweet I show a video and I'm running this script and it will just dump the credentials of every user and computer in the domain. And we also have here the credentials of which is, I think, the most critical account in the domain.

If you have it, you can craft golden tickets. Yeah, so, I'm showing this because there was this one comment that I think summarized this whole thing perfectly. So, it seems quite moderate. Yeah. Okay. So, that's about it. That's the attack. And now, let's talk about detection. So, I will talk just about detection and not mitigation at all because we will wait for Microsoft to patch it for the mitigation. But, yeah. So, for detection, when we execute the successor, there are a couple of logs that will be logged. So, we have a log for creation but for this log we have to configure a cycle. Cycle is system ACL. So, you need to configure a cycle to actually log every time that a new DMSA will be created. The next one is DMSA linkage. So, again, configure a cycle and then every time that the attribute that controls the link will be, every time that it will be modified, the log will be generated.

And the next one, I think it's pretty interesting. So, this is actually a log for DMSA. And so, this log is for when you fetch a password for the DMSA, this log will be logged. So, and you will have the caller seed and caller IP and they will hold the seed that actually fetched the password and IP that the request was originating from.


## [30:48]


But when I authenticated as a DMSA, this log and this exact log has been generated and the weird thing about it is that in the caller seed, instead of like, I'm not sure what because I'm just authenticated as a DMSA, but the caller seed that we can see here is the seed of anonymous log on. So, that's pretty weird and I think that it might be, like, it might be worth to take another look at it, but I haven't got the chance to do it yet. So, maybe later. But it will also include a blank in the caller IP. So, that's pretty interesting, I think. And anyway, I, MSRC were great to work with. I mean, we did disagree on the vulnerability severity, but other than that, they were great. So, I sent them the presentation before this talk. I asked if they want to include any official statement and so they said that this is their official statement. We are aware of this report and we'll be addressing it in an upcoming update.

So, stay tuned. So, let's talk about conclusions. So, first of all, DMSA is like a new security feature. It was designed with security in mind. It actually solves a lot of problems. And it doesn't mean that the feature itself is necessarily secured just because they made it with, like, security in mind. And so, the second point is to never skip the obvious because when I saw the whole pack merging thing and I talked with my manager about it and he said, well, maybe you can just try to change the attribute that control the link. And I was like, no, that would be, like, way too easy. But it apparently just worked and it was that easy. So, yeah. Next point is to log in the layer on DMSA links and creation. Yeah. And the final one is that DMSA is a great new feature. I really love DMSA. When Microsoft will patch it, I think it will be really worth for organizations to actually use this feature.

And, yeah. So, that was it. And hope you enjoyed. Thank you so much.
