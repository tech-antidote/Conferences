---
title: "OverLAPS - Overriding LAPS Logic"
speakers: ["Antoine Goichot"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - OverLAPS - Overriding LAPS Logic - Antoine Goichot.eng.txt"
sha256: "dc0be439e6867cb0e4d2d5959ffb44263a56d386d5a4e6a4999c8832284854bb"
duration_seconds: 1275
words: 2911
text_chars: 16193
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# OverLAPS - Overriding LAPS Logic

**Speakers:** Antoine Goichot  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (21 min, 2,911 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


All right. Good evening, DEF CON Track 4. Welcome. Welcome back. We have one more speaker for you guys. It is my absolute pleasure to introduce Antoine. The title of his talk is Overlaps, Overriding Lapsed Logic. Let's give it up for Antoine. Okay. So, hello. Thank you very much. So this is my second DEF CON but first time as a speaker. And I will present some subject about lapsed and in particular its internal logic. So, quick introduction. I am Antoine, working at Pederasi Luxembourg. I spent the last 10 years breaking things to help our clients improving their security. And yes, I am from Dijon, the capital of the mustard. A quick agenda. So we will start with a quick refresher about lapsed. We will cover the background and scope of this talk. And the core of the talk will be how lapsed works and how we can mess with it. And we will finish with a conclusion. So let's start with some definitions.

So lapsed stands for Local Administrator Password Solution. It's a Microsoft product to manage local admin password by setting unique random password that will change regularly. There is two versions of lapsed. First one, Microsoft Lapse, that we will call V1 in this talk, that was released 10 years ago. It's Active Directory only and passwords are stored in clear text, in AD. And we have Windows Lapse, that we will call V2, or the current version, that was released 2 years ago. It's built-in into Windows and supports both Active Directory and Enter ID setup. And passwords are encrypted and it supports extra features. Now, let's have a quick overview about lapsed. So both versions, V1 and V2, follow the same high-level process during each password rotation cycle. So if the password needs to be changed, first we will generate a new password on the local system. Then we will send the password to the directory, so either Enter ID or Active Directory, depending on the config.

After that, we set the password locally on the system. And there is also an additional step for device match via Entra. There is an update in the registry on the local system that we will cover later. And basically, on Active Directory, resetting the lapsed password equals to setting the expiration time to now and wait for a new cycle. So just a quick word on Lapse V1 for completeness. So it runs as a group policy extension on domain-joined machines. On the device, there is one DLL called admpwd.dll in charge of the core logic of Lapse.


## [03:00]


Password and expiration time are stored in Active Directory on the computer object and in clear text. The password is only protected by ACLs, meaning that only authorized users can access the password, but the expiration time is visible to anyone. And we have now Lapse V2. So first difference, managed device can be either domain-joined or Entra-joined. It's not a GPO extension anymore, but it still reacts to policy changes. You can also manually use PowerShell complex with admin privileges to force a refresh cycle. The polling cycle is hard-coded to once per hour. On the managed devices, we have three main DLLs. And the passwords are now stored both with encryption and ACL on Active Directory. And for Entra-ID, it's in the cloud, but it's written in the documentation that passwords are further encrypted at rest. And there is also protection against password tampering on the local system. So moving on, we'll start about the motivation and goals behind this research.

So Lapse V1 and V2 have been widely analyzed. There is a lot of tools, a lot of paper on this subject. But most of the attacks focus on the server side of Lapse, so meaning abusing authorized accounts to read the password. On the other hand, client-side remains not so explored in public tooling and research, but it's not a new observation. Actually, we studied the client-side of Lapse V1 eight years ago with my colleague Max Clements, who is in this room with me. And just to summarize our previous talk, Lapse V1 is based on an open source project called ADMPWD, and it's backward compatible. So basically, you recompile ADMPWD with your extra features, and you put it on the device, and you will override Lapse. Eight years later, a lot of things changed. There is a new feature, and it's not based on an open source component anymore. So we have the support of EnterID with Active Directory, so making things a bit more complex.

Passwords are stored with encryption, and there is this password tampering protection mechanism. In this context, we would like to explore three different questions. Can we capture the password? Can we desynchronize the password from the local system to the directory? And can we trigger a password change on demand? So for this research, we have defined a scope, so we will focus exclusively on Lapse V2. We will enable encryption, but I will not take into the details of cryptographic internals. For that, you can check XPN blog that is really great on this subject.


## [06:05]


And our testing lab will include two small infrastructures, one with Active Directory, with one client, and the other with a client that is domain joined. In both cases, we will use Windows 11, and Lapse will be used to manage the built-in local admin account. And an important note, so now Lapse runs inside LSAS process, so we will disable run as PPL just to ease our research. Bypassing run as PPL is a different topic, and we assume local, temporary administrator access on the client device. So, time to dig into the guts of Windows Lapse. So, as I mentioned earlier, the client side relies on three main DLLs, but we will focus only on Lapse.dll, which contains the core logic of Lapse. And luckily for us, Microsoft provides with the PDB files, which makes the understanding of the logic easier, and gives us as well internal function names. Here we have a simplified code tree of some of the Lapse functions inside Lapse.dll, and we can see three main zones in this diagram.

So first, on the left, we have functions that are for active directory setup only. On the other side, we have functions only for intra-join setup. And on the middle, we have shared functions that are used for password generation, and password changes. We will use Frida just to ease our research, and to hook some functions that we will see in a minute. Actually, in a second. To start with our objective, we will try to capture the password every time it changes. So we can have a look at this function, that is an undocumented function exposed by some server DLL, and is used by Lapse to change the manager account password. And by doing some instrumentation, we can find that two parameters are quite interesting, and are pointers to Unicode string structure. And just by applying an offset, we can have the actual string that is stored in these pointers. And you can see on the slide, for instance, a password.

But we will have a demo to ease the understanding. So before we start, on the left, we have a domain controller. On the right, our client. On the machine, you will see two command prompts. The one on the top will run with admin privileges, and we will use it to attach to Lsas and to hook our function. And below, we will use it just to run a GP update, just to have a refresh of the GPO easier.


## [09:07]


So let's start the video. So first, we check the password is not expired. We launch our hook. Now we expire the password, and we launch a GP update. It's just to force, to ease the setup, and to avoid waiting for a real expiration. And you can see that we have already captured the password. And I will just test the password on the local system, just to prove that the password that I captured is really the LAPS password. And here we are. We are administrator. Now, same on the EnterID setup. So exact same code. And again, we will force an expiration just to ease, but the process is the same when the password expires for real. We just wait a couple of seconds that the password will be changed. Yes, it is. And same, we can see that the password on Entra is the same that the one that we have captured. Here, another example to achieve the same result. We can hook internal function with Frida. So for instance, if we look at reset local admin account password, we just need to find the offset of this function, and then to find interesting parameters.

And again, by doing some instrumentation, we can find that there is a parameter that contains the password. So again, we just hook this function and we can capture the password in cleartext. And it works exactly the same on EntraID setup. So basically, we have achieved our first objective, and we will move to our second objective. So can we try to desynchronize the LAPS password? So for this, we have two options. So either we modify the password on the local system, so we have a control on the local password, but the password on the directory remains random. Or we do the opposite. We don't modify the local password, but we modify the one on the directory. But the impact is quite limited used alone, because the actual password will be random and you don't have it. Both options can be useful for a kind of denial of service, because LAPS will not be usable by administrator, because the password they will see on the directory is not the one that is actually set.

I didn't record a video for this one, but just a screenshot to demonstrate this. So on top, you have the Active Directory setup.


## [12:08]


So the actual password is a random password, while the one that admin will see on the domain controller is really random. And on the bottom, it's the opposite. So we have changed the password that is sent to the directory without changing the real one. So second objective achieved. So we will move on to the third one. So can we trigger a password change on demand? So our goal now is to hook the password expiration check and force it to return that the password is expired, even when it's not. And to do this, it's quite easy. So we can use these two functions. So one for Active Directory setup and the other for Enter ID setup. And we will just basically modify one parameter before the function returns. So you can see on the screenshot, we just modify the args5 in parameter and we change the value to 1 to force the reset. So we'll have a quick video on this. Again, same setup. We attach our hook.

And now, each and every time a GP update or a GPO refresh will happen, the password will be changed. So here, we just check. So the password that we have captured is the same as the one on the directory. And now, I will do it a couple of times, but each and every time there will be a GPO update, the password will be changed. And in this case, synchronized with the Active Directory. And it works the same on Enter ID setup. It's just less convenient to force a refresh cycle, except using the PowerShell samelet. But for Enter ID, we have another approach. In this introduction, I briefly mentioned that for Enter ID setups, there is the expiration time that is stored locally on the register. And I didn't really explain how the password expire block works in that case. If you look at Microsoft documentation, you will see basically the same diagram as mine, but they are separated in two parts. One for Active Directory and one for Enter ID.

But functions are basically the same. And if we zoom a bit on the top of the diagram, there is this block. Query local registry password for current password expiration time. So maybe you have the same idea as mine. What if we change it? So on the registry, there is two values that are interesting. One called Azure Password Expiry Time and the other Last Password Update Time.


## [15:11]


The purpose is pretty self-explanatory. Azure Password Expiry Time will be used to have the expiration of the password. Both values are stored as Windows file time. And here you can see readable functions for humans. So question now, what if we change the Azure Password Expiry Time key? Let's have a quick video. So I will just run the simulate function and check the logs to see if the password is expired. The answer is not. The password is not expired at this time. Now we'll go on the registry and edit the key just for convenience. And because the format is quite complex, I will just copy the value from the other key in this one. And now I will force a cycle with the PowerShell commandlet. And now if we check the logs, the local admin account was updated with a new password. And the reason, the current password was considered expired. So basically we managed to force a reset of the password.

If you are wondering what if we put a password in the future, basically it will break LAPS because on the directory it's written that the password is expired, but on the local system it says that it's not expired. So LAPS is in a weird state. So basically we have achieved our three objectives. But with Frida, maybe Frida is not installed on the victims. So we can use, for instance, Microsoft Detour library. So it's an open source looking library from Microsoft. And the diagram shows the principle. We place our own function between the original call and destination call. And we will do something in between. So for instance, capturing the LAPS password. So, quick video for this. First we will hook some asset password for an user to, from some server DLL. So again, I will force the expiration time, run gpupdate. And here we have a txt file that has been created in the background. And if we look, it contains the password.

So we managed to capture it. And now I will do exactly the same but using an internal function. So reset local admin account password. Again. And again, a new txt file is created.


## [18:11]


And if we look, it contains the password. So basically we can just do like this. So now it will be time to conclude this talk. So, if you are wondering, can we hook other functions for similar results? The quick answer is yes. Here on this screenshot, for instance, I captured the LAPS password on six different functions on active directory setup. And there is probably other functions that can be hooked for similar results. In the introduction, I mentioned the password tampering. It's written in the documentation that LAPS protects accounts from accidental or careless tampering. So, for instance, if you use a net user command, it won't work. But with this approach, it will work. So, in other words, intentional tampering is still possible if you know what you are doing. So, did we accomplish our mission? Yes, we managed to achieve our three objectives. So, capturing the password, desynchronizing the password from the directory, and trigger a password change on demand.

But let's be clear. For, let's say, a real scenario, you will need to bypass RANAS PPL, you will need to fight against ADR, and so on. And we are touching ELSA, so it's always a tricky question. But my objective was to, let's say, lay the foundation. And I hope some of you will have some ideas and will build on this research to go further and to develop other scenarios. Some key takeaways. So , for our Red Team friends, in two words, be creative. Think beyond the spoke. You can retrieve the password via the network or other scenarios. As I mentioned, other functions can be hooked or abused. The logic of LAPS might change with updates, so we need to check basically each and every patch Tuesday if there is a new version of LAPS. For Blue Teamers, watch for unexpected LAPS reset. Because if you are not using LAPS evilly, the reset of the LAPS password should more or less match the rotation period that you have configured.

Of course, limit privilege escalation vector, because we assume that we have compromised already a system. And ensure that your technical controls are working, such as RANAS PPL, ADR, and so on. So, thank you all for your attention. So, all the talks that I showed and additional words are available on this GitHub repository. There is also some scripts to help finding the offset automatically once a new LAPS version is released.


## [21:11]


So, feel free to check them out and reach out if you have any questions. Thank you.
