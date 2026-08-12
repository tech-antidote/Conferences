---
title: "Gateways to Chaos - How We Proved Modems Are a Ticking Time Bomb"
speakers: ["Chiao-Lin 'Steven Meow' Yu"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Gateways to Chaos - How We Proved Modems Are a Ticking Time Bomb - Chiao-Lin 'Steven Meow' Yu.eng.txt"
sha256: "4ab2212f0b1449febe1fd456dfe5a5ea4ea27729e48ec7f162f70fe24b71d282"
duration_seconds: 2380
words: 5141
text_chars: 28915
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Gateways to Chaos - How We Proved Modems Are a Ticking Time Bomb

**Speakers:** Chiao-Lin 'Steven Meow' Yu  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (39 min, 5,141 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Imagine you have a gun and your home modem loaded and facing global security. Gateways to chaos, Stephen Miu. Give him a big hand, everybody. Hello, everyone. I'm very excited to share this topic with you today. Gateway to chaos. How we prove that the modems are the ticking time bomb that hacker chaos is everywhere. In this talk, we will share about many real-world vulnerability and cases. This weakness could be happening in your own home. Let me quickly introduce myself. My name is You Zhao-Lin, but you can call me Stephen Miu. I'm currently as a senior researcher at Trend Micro Rating in Taiwan. I have several certifications, including OSC-3. I have also received several CVE from a big company like the VMware and D-Link and Zycel. I have given talk at event like the B-Side Tokyo, Hikon Bunty House and the CyberSec conference in Taiwan. This year I'm also the Hikon training speaker. At this DEF CON, in fact, I have three talks.

One is this one in the main stage and the other are the car hacking village and the IOT village. Okay, so what do we find during the research? Yes, we report several CVE in this research. And more CVE and even more CVE still in the reporting process. Okay, last year we found some critical vulnerability in D-Link devices. Sadly, D-Link say these are end of life device and they will not patch or fix the issue. Also, in Taiwan, modem or the residential gateway are provided by ISP. User cannot change them by ourselves. At that time, there were about 60,000 of this device in the world. The vendor refused to patch and the ISP refused to replace that with the new one. Here's the something interesting. Even though we know the device is vulnerable, both the ISP and the vendor refuse to fix or replace it. Oh, you might think, maybe we can just disable some vulnerable service from the setting page, right?

But sadly, the control panel doesn't actually work. Even if we disable the service from the console, they are still available. The control panel is pretty much useless. Okay, also we found some hardcore password in the device. This device is widely used by ISP in the United States. For example, the Mark Twain communications.


## [03:01]


We also found a critical vulnerability that can let attacker control the device all over the world. For example, in Europe, Asia and the U.S. Okay, here is our agenda today. First, I will introduce the agenda and the six different methods about the devices. Our first story is about changing several vulnerabilities together to achieve the remote code execution about 60,000 devices. The second story starts from a free Wi-Fi network on a bus. We would find a vulnerability there and discover the same bug could be used on even a water company in the United States and many large ISP worldwide. We even found a backdoor in this product, which means attacker can use it to control the device around the world. The third story is about Zycel. Even though there are many problems with Zycel and CNA, they still not handle the problem well. Next, I will introduce a modern security scanner we developed. This tool can detect all the vulnerability we share with you today.

And finally, I will share a summary conclusion and the main takeaways. Okay, let's get started. Generally, how do we connect a device to the internet? First, our laptop connect to a wireless router. Then the router connect to a modem with maybe PPPoE and finally connect to the internet. So, how do we prevent the cyber threat? Most of time, we install the anti-virus or maybe some EDR to stop the virus, right? But almost no one care about the modem or the router. Usually, the router and the modem are the embedded system. It's hard to install the anti-virus software on them. So, besides home environment, what about the critical infrastructure? Things like the water planet, the smart city, and even the rocket system usually connect the internet through a router. The router is placed behind the firewall, then connect to a modem. And finally, to the internet. So, we can say that the every device behind the firewall is relative secure.

But any device in front of the firewall is at risk. Just like this, we secure all the device that we can control. We can use all kind of security method inside the intranet. But for the gateway or the modem, it's much harder to install these protections. So, what is a modem? A modem is like a bridge that connect you to the internet.


## [06:03]


There are many types like the cable, fiber, phone line, and even 4G LTE or 5G secure network. Modem are used in many place. At home, at business, and in the critical infrastructure. Basically, if you need to use the internet, you need a modem. During our research and the threat intelligence work, we found that many critical infrastructure are using the vulnerable devices. Hacker can directly break into their intranet and control these devices. For example, we saw this in a water planet in the U.S. and some smart grid, oil and gas system, and even the ATM network. We also found that some vehicle management system and using this kind of devices. If you want to know more about vehicle, I have another talk at the car hacking village just next 30 minutes after this talk. We have even found some government, military, and police system using these vulnerable devices. In February this year in Taiwan, a home modem was used by a scam group to commit fraud worth about 60,000 U.S.

dollar. This incident forced the ISP to replace the old modem with the latest one. So, we are just an ordinary people. Why do we the threat actor want to hack to our devices? It's because of the underground business called the residential proxy. For example, when we use the credit card to shop online, sometimes we will receive a verification OTP code, right? But sometimes we don't receive just to swap the card and it's okay. It's because the 3D secure verification system check for the abnormal user behavior. For example, if a user always shop online from New York, but suddenly the IP is from Las Vegas, it might trigger an alert. Hacker want to get more different IP address from the different place to bypass the 3D secure check. It called a residential proxy. Many ISP in different country force user to use modem and router that ISP provided. User cannot use their own devices. This is done to reduce the support cost and for the ISP business model.

They also say, maybe it's for the security reason, but they don't maintain it. It's ridiculous. Recently, Europe has start to promote the router freedom, which means user can bring their own device to connect to the ISP network. Okay, let's share some more technical detail for our first case. Last year, I moved to a new house and asked my ISP to install the internet service.


## [09:09]


And as a hacker, I always test all my device for the security before I using them. So, I test my modem provided by the ISP and discover more than 10 different vulnerable service in these devices. I believe it's a textbook level example for even an IOT penetration for a beginner. Okay, so when we get an IOT devices, the first step is to evaluate a possible attack path. For example, we can check the network access for both the WAN and the LAN side. We can also analyze the Wi-Fi signal. And we can try a physical intrusion by disassembling the casing. Okay, so here is a web logging page for our target devices. So first, what would you want to do? Admin, admin? No, it doesn't work. But we define some clue in the documentation. After analyzing the devices, we found a several predictable credential on it. Also, there is a WAN side password that is not shown in the user interface. This is an ISP defined it better for the maintenance purpose.

And interesting is that the password for both the Wi-Fi and the web console is created using the device MAC address. As we all know, we can get a MAC address from the Wi-Fi BSSID or connecting to the WAN LAN and checking the ARP packet, right? Also, we can access the physical device and maybe we can see the MAC address just on its label. Finally, if we can find a way to bypass the web authentication, we might also be able to retrieve the MAC address. Yes, we actually found a way to do this. And I will share more detail later. Also, we found some strange default setting . SSH and telnet are enabled from the WAN side and disabled from the LAN side. Why? Okay , is this reasonable? I don't think so. Maybe it's for the maintenance purpose. The web portal is also provide a remote access control wireless. This probably means to let only the certain ISP network segment to access the service. But sadly, as I mentioned before, this feature is broken.

Any user from the WAN side can access the, all the WAN service. Okay. And, sorry. There is a low privilege user account in the devices. The user name and the password is both user. This low privilege account can only change the Wi-Fi SSID, Wi-Fi password and their own password.


## [12:13]


The high privilege account is not for the normal user. It is only for the ISP engineer to set up the advanced function. When we change the low privilege user's password from the web console, we can see the request shown on before, above. In this example, we set the user 2 name to user. And the user 2's password to user. Okay. Yes, we can use the Burp suite to change the request. The low privilege user's ID is 2. We can change the ID to 1. And then use the low privilege station to change the high privilege user's password. In this way, you can achieve the privilege escalation. Okay. Next, we can check the SSH and the telnet service. Since we used the default low privilege account to get the high privilege password, now we can log in with the high privilege user. Yes, we found something interesting. The interesting function are things like the ping test, trace route test and other testing tool.

You guess that this feature are implemented using some simple string concatenation. This make them vulnerable to the command ingestion. Yeah. Yes, all of this function have the command ingestion vulnerability. And then we receive 5 different CVE for that. Yeah, very very easy, right? After getting the remote code execution, we can bring our own tool to extract the firmware. For example, we can use the like busy box, netcast or the TCP dump to do more analysis. We can also check the partition and dump data from the device. For the password issue, we also found that the plain text chip secret store in the devices. We can write a simple deep code function to get any password or secret from the devices. After dumping the firmware from the device, we can do more reverse engineering. For example, we found several XGI paths in the THTTP binary. One interesting path is config dot XGI. This path does not require any authentication.

Any user can use the config dot XGI to dump the device configuration. For example, we can get a MAC address from the device. And as we all know, the admin password is made from the MAC address. And one of the hard code password cannot be changed. So, we can use this function to get a root credential. We also found another path called DELT file dot XGI. This XGI path take a perimeter and is vulnerable to the path reversal. With the path reversal, we can read a system configuration file.


## [15:17]


For example, by using the path slash S Y S class net E T H zero address, this path, we can get a MAC address. Yeah. Once we have the MAC address, we can calculate the root password again. Okay, next is the interesting part. For the previous password change vulnerability, the key point is to changing the set S Y S user password perimeter from the MT underscore the admin dot XGI path. And for the previous authentication bypass, we all know that the DELT file dot XGI does not need any authentication. What if we change the perimeter set S Y S user password within the DELT file dot XGI? After testing, the answer is yes. We can use the DELT file function to send the change password perimeter and change the root password without any authentication. Okay, let's go back to the change password API. Now that we have the firmware, we can do reverse engineering and review the some code. To understand all the perimeter, for example, this does uh, EXE equal to CHT log.

What is it mean? After checking, the EXE perimeter will eventually be passed to a EXE shell function. And about CHT log, CHT stand for uh, Chung Hua Telecom, which is uh, ISP in Taiwan. CHT log is an executable script. Yes, we can also find another communication remote execution in the web portal again. Okay. We also found another interesting vulnerability. Insecure user station handling. If one user is logging, another person can just access the device without any authentication. I believe it's ridiculous. The station is stored on the server and no any user cookie is needed in these devices. Here's a summary of the attack path. Once we get a web access, we can use the authentication bypass to retrieve the password. And even change the root password and log in to the console. After logging, both the web portal and the SSH or telnet console is vulnerable to the communication so we can do the remote execution on it.

It's very easy to combine this vulnerability into a full attack chain. About this case report, it's very, very interesting. When we report this vulnerability to the Taiwan server, the TW server CC, we also mention that this is very, very, very critical because we found many vulnerable device in the Taiwan government networks.


## [18:28]


But the TW server CC replied that, oh this device is end of support so the vendor will not provide any help for this case. This report will be disclosed early. They did not work with the Taiwan government to handle the issue. Also the Taiwan ISP like the Chunghwa Telecom was not willing to replace the vulnerable devices for it. And in November last year, D-Link market value dropped by the 30 million USD in just one day because of this case. Yeah, maybe I should consider shutting the stock before reporting the vulnerability. Online news like the briefing computer report on this case. Okay. Three months later, we discover another modem model called DSL7740C. It's very similar to the previous mention, DSL6740C. And all the vulnerability are identical. It's very disappointing that the vendor does not disclose this existing of the twin model. By using the O-Sync tool, we found about 60,000 vulnerable device online when the vulnerability were disclosed.

And by July this year, about eight months later, there are still more than 20,000 vulnerable device in the world. Maybe today still there are 20,000 vulnerable devices. You can just use the payload and I'll see that. Okay, here's a quick summary of the issue. First, the device should not use the predictable password. The mask address is not a secret, right? For the privilege management, low privilege users should not be able to access the high privilege function. Also, the default setting on the website are not secure. For the management level, it is also a problem that the vendor is not willing to fix the vulnerability. They did not disclose the related device model. As a researcher, we do not have enough visibility to find and buy all the device to check the issue. ISP also have the responsibility for that. ISP refusing to replace a vulnerable device is a big problem. They provide the device but they do not have responsible for maintaining that.

Okay. Just drink of water. Okay. So, this is the first case . Next, let me to introduce our second case. This story is also quite expected. We start from a single bus and end up to reaching the entire transportation company. Here's how the story goes. One time I was taking a bus and connected to its free wifi.


## [21:32]


It just happened to be during the priority when I was researching the modem. So, I start to look into how the bus wifi system is designed. First, when we connect to a device, I always check the port which are open. What really caught my eyes in this time was the two strange port. Especially in the port 5555. Looking closer at the port 5555, it seems to be a running UPNP service. That's right. This device has a UPNP service enabled by default. Without any authentication, we can use UPNP to change device SSID, reboot the device or even restore it to the factory setting by sending the UPNP packet. For example, we could simply ask chat GPT to write a POC code that use the UPNP to change the device wifi SSID. Yeah. After checking out the UPNP port, let's take a look at the port 80. Actually, port 80 require a user name and password for the authentication. But if we take a closer look at the server header, we can see that it's running a BOA server.

So we try to searching any pass vulnerability in BOA. We found that in 2022, that was a authentication bypass vulnerability in BOA. Okay, let me try it. We decide to give it a try by sending just a HAT request with a curl. We were able to bypass the authentication restriction. Yeah, just it's simple. After the OS bypass, the next step was to look the interesting thing on the setting page. The change password feature caught my attention. We remove the type equal to password attribute from the HTML tag. And sure enough, we were able to directly see and get the password from the devices. Yes, we are F12 hacker. If you know how to use the F12, the device per tool, you can easily to get a user's password. Okay. We can also combine the authentication bypass and the password retrieval step. In this way, we can get a device password in one go. And then log into the system normally. Yeah. Yes, that's how we successfully get into the system.

Of course, the SSH is also enabled in this device. We could use the SSH to access the device console. And next, SSH console has a ping function.


## [24:33]


And yes, you get it. We found another, another communication vulnerability in the ping function. After getting a reverse shell, we notice something strange in the ETC password file. There was a user called Xin Dian. So what is Xin Dian? Xin Dian is a place in Taiwan which is also the vendor's headquarter are located. There's a strange to see a hidden account in the user name after this place. Unfortunately, we could not brute force the password using the word list like the Roku. So we try to find some code in the firmware instead. After analyzing the firmware, we actually found the plain text password for this account. Just use several if and the equal equal to concatenate that. Yes, we are able to use this password to SSH into the system. Within this account, we got the direct access to the shell. Not just a limited configuration console. After entering the system, we start to do further testing and research inside.

We found an interesting process called the MQTT sub running in the system. It will start from the command line with the certificate, IP address, and the credential all shown directly in the command. The CA related file are also stored directly in the system's temp folder. Next, we try to connect to the system using like the MQTT client. We found that we could subscribe all topic and see the status report from the device all over the world. It look like this MQTT feature also has the remote command execution capability. So we can control the device all over the world just by the MQTT. Also, some of these device even have the GPS tracking feature. By checking one of the GPS location, we were able to find a bus company's parking lot. Next, we analyze the data even further. We had found that the wind side and the land side open the same port. All the device can apply from the both side. We discovered that many important critical infrastructure were using this system.

Including the water panel in United States. Even more surprising, we found that the most of this router installed by ISP were still using the default password. This mean we could access this device either through the MQTT or by using the hard-coded password.


## [27:34]


We could also see the related impact list on the product's official website. For example, the SCADA and this also include a virus component of the smart city system. It also include a power transmission line and even more communication inside the operating room. And also virus the ATM systems. Finally, there were the energy sector. For example, the oil and the gas industry. Many factory automation device use this device as their router. Okay, let's quick sum up this case. We can abuse the UPNP to change device setting without any restriction. We also use the web authentication bypass to get the plan task password from the device. After getting the password, we can access the backdoor through the SSH or use the hard-code backdoor password to get a shell. We can even use the MQTT to control thousands of devices. As soon as I discover this vulnerability, I report them to the TW cert CC again.

This include the five different CVE number we collected. After this CVE was published, we saw that the vendor honestly disclosed the other related product and had the same issue. They also provide a fix for all of that, which is something we should encourage. But we also found something interesting . This product is actually passed the Taiwan IOT cyber security certification. This show us that we cannot fully trust this kind of certification, right? And after some time, a familiar story happen again. We found about main company in this case, BDN. And he has a BEC branch in the United States. It's a subordinary. This branch also has a many vulnerable model. But the vendor does not disclose this model in earlier CVE report. So we report this related vulnerability to the ZDI again. But this time, the vendor didn't respond at all. After waiting four months, this vulnerability were eventually disclosed public.

Let's quick sum up the key point of this case. First, they are insecure default setting. For example, the WAN access to the web and the SSH interface by default. And authentication user being able to use UPNP. Another serious issue was storing password in plain text and the backdoor password, right? And this system is also had outdated component, which made authentication bypass possible.


## [30:38]


There were hidden backdoor that were not disclosed. And all device share the same NQTT credential. Finally, the vendor did not fully disclose all the affected models. Next, let me to quick share our third case. Because of the previous case, I start to take the BOA authentication bypass issue even more seriously. Through the open source intelligence, we found that the Zycell device had this same problem. We report this to the TWCC right away. Since the Zycell is NCNA, which means they have their right to issue their own CVE. So, we forward our finding to the Zycell. Zycell only replied that, oh, this device is EOL end of life. Next, we forward this email to information to the MITRE. MITRE mentioned that sometimes CNA will refuse to provide a CVE like this. But MITRE can sometimes escalate to case to just remind them about it. Okay. And in this then, a month , we successfully receive a CVE number for this case.

This story show us that if CNA does not want to handle the EOL issue, we can just ask MITRE to help and put some pressure on them. There's a few example and also quite interesting. They include a product from like the Nokia, Dashan and the Hytron. This model are still very widely used in the home across Taiwan. First, we found a Nokia device that allow you to access the system log without any log, logging or the authentication. The syslog contain the MAC address. And the default password is just a combination of MAC address. Just like our first case. So if we get a MAC address, we can log into the root console. And what interesting is the Nokia P3's response. They say, we do not treat this weakness as a vulnerability. We kindly ask you not to disclose any information about this publicly. But if it's not a vulnerability, then why shouldn't we share it? The logic doesn't make sense at all, right?

And the fifth example is from the Dashan. Their product have the same UPNP problem. UPNP can be accessed directly from the website. And there is also an issue where the MAC address can be neglected. We also report this related case to both the VDI and MITRE. For the HITRON device, after connecting to the system using like the telnet, we saw a console management for the system setting.


## [33:44]


There was also an telnet function inside. And once again, we were able to find the command injection vulnerability through this feature. We also report this case to MITRE in the March of this year. Because of this, we realize there are so many of the overlooked vulnerability out there. So, I developed a modern vulnerability scanner. For user who don't need to know anything about the vulnerability or the device model. They just need to visit the website and click the scan. The idea behind this tool is actually very simple. We record the unique characteristic of all the vulnerability and we use the banner grabbing to quickly to find a possible threat. Now, let's take a quick look about a demo video. On this page, user just need to click a start scan. After that, simply wait a few second. Our system will check then check all the signature against the source IP and then you know if there is any vulnerabilities.

While running this tool, we also found some interesting result. Some device seems to match the vulnerable feature but they, their server hater shows like the Apache or the Python instead. It looks like someone is trying to research my research. Okay, finally let me, let's move on to the conclusion of this talk. Across more than ten different device model, we found over thirty vulnerability. This issue cover ADSL, GPON, ONU, and the 4G, 5G router. Not only the home user but also the business factory or the critical infrastructures are affected. We discover many pre-auth RCE and the hidden backdoor. Also, a lot of these product are the end of support but they are still widely used. Especially for the EOL end of support issue. We believe vendors should clearly define an EOS timeline instead of sadly marking the device as the end of support just because the vulnerability is reported. It's common for the user to keep using the EOS devices for a long time.

Vulnerability platform should not refuse to accept the report about the EOS, EOL product. This talk also show the most IOT vulnerability are inherent problem. Device often use the same code base. As a security researcher, we usually cannot fully find out all the affected model. For this, vendors should take more responsibility for that.


## [36:48]


For all that software service, like the BOHS, vendors should keep a complete recall of all the component they use. For example, they should manage and monitor with the BOA and to monitor with the like the SBOM, for example the software building material. Okay. Vendors should also evacuate the attack service of their product. Especially when it's come to insecure default setting. Unfortunately, many vendor don't even know the service they are running on their own product. For example, TP-Links customer service, once they form that, their product doesn't support the telnet service and it's just a channel for the app to communicate. However, no more user can actually connect to it directly. This is a really ridiculous example. Yeah. Next is the issue of the backdoor. There is more and more evidence shows that the vendor like to keep the backdoor in their product. Sometimes it's for the maintenance purpose.

And sometimes it's done on the purpose for the government or the company. We believe all of this backdoor should be disclosed. For ISP, we believe it's important to promote the router freedom. Users should be allowed to change their own devices. ISP should also closely monitor product and replace them before reach out the end of support. If there is a security incident, user must to be notified right away. For user, don't assume that the product from our ISP are always safe. Don't fully trust the cyber security certification either. Don't trust of the product from any brand and trade your modem or the router as a tier zero critical device. Here are some final action item and the takeaway. Try your best to identify your modem and the IOT device model. Check if there are already end of life EOL or have any known vulnerabilities. ISP will not tell you about this issue. So keep track all of your device and manage them careful.

Don't trust every setting. Always use the pulse scan to check or confirm. If possible, closely monitor all the network traffic to detect unknown trade. Okay, this is all my sharing today. Thank you everyone. And let me take a selfie. Thank you.
