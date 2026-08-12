---
title: "Silent Leaks - Harvesting Secrets from Shared Linux Environments"
speakers: ["Cernica Ionut Cosmin"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Silent Leaks - Harvesting Secrets from Shared Linux Environments - Cernica Ionut Cosmin.eng.txt"
sha256: "20eeb46c37c0c981ce065ee1a751d03bd68437f919ebe673bd0d6ac60d8f6079"
duration_seconds: 1187
words: 2570
text_chars: 13691
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Silent Leaks - Harvesting Secrets from Shared Linux Environments

**Speakers:** Cernica Ionut Cosmin  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (19 min, 2,570 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


It is my absolute pleasure to introduce Jonas Cernica, who will be talking about Silent Leaks, Harvesting Secrets from Shared Linux Environments. Take it away. Thank you. So, welcome to my presentation, Silent Leaks, Harvesting Secrets from Shared Linux Environments. My name is Jonas Cernica. So, for today, so I'm... Okay, I was thinking I did an update, but it's okay. I'm an application security engineer for UiPath, and also I'm an AI security researcher, bug bounty hunter, former CTF player, and former entrepreneur. For today, I'll have a short introduction about multi-user Linux environments, how the process arguments are leaked through commands in Linux. Then I'll speak about jailing and isolation systems, temporary file leaks, and a demo, and closing remarks, the conclusion. So, multi-user Linux environments is where you have multiple users with unprivileged... you are not privileged... you haven't... you don't have privilege...

privileges, and mostly you find in hosting panels, dev servers, education labs, providers, and CTF infrastructure, maybe. The assumption you have no root privileges, and you don't have to do the local privilege escalation, you just have a basic user with maybe an SSH shell, access, or a web shell. You can do both ways. So, as an attacker goal, you have to discover secrets like database secrets, API keys, passwords, and other kinds of secrets. Then you can fingerprint, you have to fingerprint the users or domain if you can do that, and then prepare for the lateral movement. Process arguments leaks most of the time are leaked through this command, ps, which is a default... is default for each Linux installation. Sometimes I found that I can cut in the prox prox directory any bid, but in some situations, not all the situations, and you can use the big rep in the shared Linux environments, like web hosting providers and so on.

Why is this default behavior like you can use the command ps? Legacy of transparency, so the Linux was designed to trust multi-user environments for university or shared labs, and it was a good debugging and monitor way to do it for tools, and in this case, just in this case, it wasn't a security, it was a priority of the security, so it's about a backward compatibility changing this behavior would break many tools, as I said earlier.


## [03:07]


I will not name affected providers in this presentation, because, yeah, I reported these issues in early of April this year, and I want to give them more time. One of the providers did a very quick fix in a few days, and it was very proactive. They told me not to put their name on the slides, but I can do the demo with them. To act responsibly, so I choose not to give names about the providers, but most of them have problems. You'll see in the examples, and then you'll see in the demo. So let's run the command in Linux ps au xww. It's au xww to take the full command and all the arguments. That's why I choose this. You have to run it in a loop to take each, I don't know, you can put, you can make a loop, which at 100 milliseconds you run this command and take the output. And let's see some data. In one of the hosting providers, when you run this from one of your users, so you have just to register as a user, you have your web access, your website, you have web access shell or you have SSH shell, I don't know, they can provide this to you.

Maybe most of you know about the web hosting providers, how it works and you get some SSH shell. If not, there are ways to get to run system commands on the Linux. So from another user I run the command that the ps au xww and I took this kind of information. Another user like test one here, he was installing his newly website, it was about WordPress and in the command it was linked the user name of the newly WordPress install and the password here as you can see. So it's easy to wait for new users and take their passwords. On another web hosting provider, this command was run by root, I redacted the first part of the output of the command ps because you figure out which provider it would be. But it was running by root and as you can see, the root is installing the new user test two and his password, this is the Linux user as you can see. And he is creating the home directory, public HTML and so on.

So I can find his password on the leaked command arguments. So you figure out already that most of them they put passwords and important data in the arguments of newly installed websites and so on.


## [06:09]


Okay. Here another case, another web hosting provider, he's running as root, this will be the demo at the end. They run as root and they created the ‑‑ when I tried to ‑‑ to come back, the other two cases was about to wait for other users to come on the website and register. This case, you can trigger this exploit by your own. So you have to create a database backup. We'll create this temporary directory which I will show you in another slide that you can leak this one because it's readable by any user. You have to wait in the temporary directory and grab anything from there that is coming because this will be deleted in seconds, in milliseconds. And as well you can see in the process arguments that you have the root MySQL and the password of the root user. And you can grab all the databases from the hosting provider. So he was doing a backup restore with the user root just to don't have any problems.

And he used the root user name to do the restoration. In another case, I know that all these cases have similarities, but they do in a way or another they do differently. So here he chose to run as root and put the database name, database user and the database password and you can leak it through other user. As well in another case, again the root is installing the new database for a newly user from the web hosting panel. He put here the database name, database user, database password and you can grab it very easy with your user. Okay. Now solutions for this would be to, I don't know, to install a new, to remount the proc directory so with high speed too, but it may break some tools and monitor debugging tools. Also a lot of hosting providers they are using containers or like docker, but not a lot. You can use the containerization, but I think it will cost a lot to do that, but most of the hosting providers they are using cage FS with cloud Linux.

But you'll see that you can break that too. Okay. Jailing and installation systems, most of the hosting providers they are using this first two, cage FS and cage root. The others I didn't see, I did bug bounty on these problems and I found a lot of things, but most of the hosting providers which gives you the ability to look on their stuff and they have a public bug bounty program for their web hosting, they use cage FS or cage root.


## [09:09]


So now bug bounty time, I used to have to use this information and make some money. So escape, I used to escape the cage FS in a major hosting panel, but after I used that on their panel, I figured out that that escaping solution was working on all other hosting panels because it was a general problem. So I cannot speak about this one because I sent this problem to the vendor, but he didn't give me any clue when this problem will be fixed. I told them that I will speak at DEF CON about this problem, but maybe that's why they delayed the fix, I'm not sure. So I was able to find the binary in the cage FS that was executing in the ‑‑ not in the isolation environment, in the Linux itself. So outside the cage FS. So I was able to read any file from most of the users, but I combined with another exploit for that. Another way to create isolation was with chroot, and most of the chroot isolation they are using the file browser, which is a software written in Go.

Let me go back. I'm not sure it's not ‑‑ okay. It's a software written in Go and it's a UI interface for the file system, so the user that has a website can access their files through this file browser. So I find an undocumented command on file browser to run commands, system commands, and that's how I escaped the chroot from one of the hosting panels. Another problem was credential exposure via light speed. Light speed is an optimization software for ‑‑ so when you create isolation environments, you have problems with ‑‑ I don't know. You have problems that your websites can run much slower and so on. So they created light speed for caching. It's a caching technique for isolated systems for web hosting. And the major hosting providers are using light speed because they have thousands of users. And in a lot of bug bounties programs, I found that if you execute a script and then read the proc ‑‑ I'm not sure why it doesn't work anymore.

Okay. If you read the proc self file descriptor number 2, you will read the STD error log file which is from all the users.


## [12:14]


And I reported this on 31 March and they on 3 April light speed already fixed this. That's why I can speak about this right now. So what I found in bug bounty programs with this kind of problem, so I read that file and I find it was the full request like the response and the request that was sent to the server. So there you can find user name, password, when cookie was set for web servers, you can grab the cookie and the domain where you have to use that cookie or the authorization tokens from PayPal or other websites domain. So there were a lot of information in those files or gigabytes of files. I just look for a few kinds of information and just to prove that it is a big problem. Now I'll speak about temporary file leaks and poor file permission because when you install a new website or you are doing something on the disk, sometimes they create new files on temporary directories and those files are readable by anyone.

So here it's an example of hosting provider which when you install that software, you have in temporary file directory, a directory then a log where you can find all these passwords and you can take control over the hosting panel. I report this it's already fixed. They fix it in a few days but I didn't speak with them because they didn't want to show to speak their name to a conference. Another example and this one will be in my demo, is when you are trying to create, to restore a database, you first create the restoration data, you first create the backup, then the backup will be named, will be placed on your space, on your public user. But firstly when it's created, it will be sent in temporary directory then deleted from them and it will be sent, I don't know, via e-mail or something like this. But if you, from another user, if you want to grab all these files, you can do it easily and you can read all the databases that are backup from the system.

In another bug bounty program, it was about not web hosting necessary but they didn't have, I didn't have access to the proc directory, the PS command as well. It was very easily, it was very good, and it was very good isolated. But I found that they were installed scripts for each user with their passwords and so on. It was in a temporary directory under a random name and then main.php.


## [15:18]


So it was exposing credentials like WordPress passwords and other kind of credentials, not just WordPress. Okay. Let me go on the first demonstration. Oh no, this is not mine. There are multiple, I think it's this, yeah. So in this demo it's about our panel which is a web hosting software, which right now I create a backup copy here. I already, here, I already created the backup copy. And after that, when the backup is created, now I'm going to my shell, I'm on the user A, there is the user B, and I run this command, the PS AAUXWW in a loop, and I grab the content at 100 milliseconds. So now I'll restore the database and let's see what I took from the output of the PS command. So here is the whole output and now I look for the root password from my shell. So here is the root password of my shell. Let me show you here. As you can see, I trigger a backup copy of my database, then I try a restoration of the database and when I read the output of the command PS, I find the root password of my shell and I can take all the databases from that web hosting software.

Here is it. And as you can see, it has the temporary file with random name and you can grab it from another user, it's readable and so on. Another example, it is for file leak, the second video. So here, here is just when you install a new website, you create a new website, you'll do the, let's see, I'll cut everything that starts with temporary A, A, W, B, C, E, I and every file that starts with that name, I'll cut and redirect to another file, to a dump file. So let's see what's happening. Right now I'm under the user A, so I try to hack the user B, which is the newly user created.


## [18:28]


Okay, the dump file which was under the user A and let's see what's in there. So we have data about the user B, the user password, the user B account and so on. So you can easily take this kind of data. Now, going back to my presentation, yeah, as closing remarks, so multi-user environments are full of unexpected leaks and maybe sometimes are devastating and can take everything from your, you have to give like databases and passwords. So security is not just about exploits, it's about assumptions, so don't make wrong assumptions about your system. So tools like PS or PGREP are trusted because they are standard, but in shared environments you can see that are not so, they can have a lot of problems, you can have a lot of problems with them. That's all, thank you.
