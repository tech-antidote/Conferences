---
title: "RATs & Socks abusing Google Services"
speakers: ["Valerio 'MrSaighnal' Alessandroni"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - RATs & Socks abusing Google Services - Valerio 'MrSaighnal' Alessandroni.eng.txt"
sha256: "976f02ad0410a382ce4f1d7d80d29135fa8f99043a8ec8329c8c77f8d9e98e7b"
duration_seconds: 953
words: 1790
text_chars: 9102
redacted_secrets: 0
converted_at: "2026-08-12T06:24:14Z"
---

# RATs & Socks abusing Google Services

**Speakers:** Valerio 'MrSaighnal' Alessandroni  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (15 min, 1,790 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Hello everybody. Thanks to be here. Thanks Defcon. So um today uh we are gonna talk about uh some way to abuse uh Google cloud services. In order to perform uh um some action in a context of uh red teaming operations. Uh first of all uh let uh let me introduce myself. My name is Valerio Alessandroni. Uh currently I am an offensive security leader at UI Italy. Uh my background is uh based on uh pentesting and red teaming. So the first topic uh is uh um research I performed uh in 2023. Which is called the Google calendar rat. Uh that was uh that is a tool uh a post exploitation tool that abuses uh of uh uh Google calendar in order to use it as a command and control infrastructure. Why I I developed this tool? Uh first of all because I wanted to um reduce uh the time to set up uh command and control infrastructure. And uh in order to to save uh to save money. Uh I wanted to perform some creative way to bypass uh uh defenses mechanism.

And uh last but not least uh I wanted to have fun during the development. How it works? Pretty simple. Google calendar is the middle man inside this schema. Um you have uh uh an agent that you deploy on your target machine. Uh the the original uh POC has been developed in uh in Python. Uh with a polling mechanism um the agent uh and the attacker can communicate uh with the Google calendar in the middle. And then you can establish uh connections and commands and receive the the output of those commands. Uh I think it's stuck. Okay. So I released the tool in 2023. Uh a few months later uh the Google cyber security action team uh mentioned the tool uh uh within the threat horizon report. Uh um but the most important uh event that happened was about uh few months ago.


## [03:01]


Maybe on April of this year. Uh while um APD41 uh used uh a similar technique based on uh Google calendar. But we will talk about it later. So uh how it works? Pretty easy. Uh when you create uh an event on uh Google calendar you have uh two two fields that you can uh put your data on. The title field and the description field. Uh the title accept up to uh 1,024 characters. And the description more than 8,000 characters. So I ask myself why can't I use that in order to put data and create a communication channel uh exploiting Google uh Google calendar. So uh I developed the the tool uh and the um the requirements uh to use it are the creation of a service account which is basically um uh an account that can take uh the control of your Gmail account. Uh so you can use it inside uh a software for automation. And you you have to enable the the API. In this case the the Google calendar API. Once you create uh a Google calendar um and you share with your accounts, you are ready for establish the communication.

So this is uh um the the POC of the tool. On the uh left side there is the target machine. On the uh right side uh the attacker machine. So we are running the tool. And uh it uh communicates directly with Google calendar. For this example we will use the Google uh calendar web application interface uh in order to in order to send and receive the commands. Uh we can see in the description field of the event uh on the left side uh uh the input command and right after with a pipe as a separator, the output that is uh base 64 encoded. So you can see that uh it's pretty easy to use it and uh no direct connection between uh the attacker and the target uh uh is established. Some security consideration. You don't need an infrastructure. So you can set up uh uh your environment uh in uh in few minutes.


## [06:07]


You don't need to buy domain name. You don't need to buy VPS uh and that's because you exploit the Google trust. Uh as accounts uh Google is a single point of failure. Because uh if an organization doesn't allow the traffic to Google uh it will it will it won't work. Few months ago uh Google analyzed uh some APT 41 actions uh and they discovered that uh they were spreading a malware called tough progress. Um I thank their effort for this uh research uh but I think they missed uh um a point. When I released the GCR, the Google Calendar Router, I put an IOC inside the code. Which was uh um hard coded data of for the event creation. Which was set up on May 30, 2023. And on the left image you can see the GSR, GCR sorry. Uh events with that that date. And on the right image the Google report. So APT use the same the same data that's an in an indicator that uh tough progress uh is based on uh a Google Calendar Router.

Of course uh uh that is not the only tool that abuses uh Google Cloud. There are multiple tool. One of them uh is called GSR. Is uh a tool I developed uh um some few months uh later the later I released the Google Calendar Router. But all those tools has something in common. They are limited to a synchronous uh request response uh communication model. And uh you are not able to vehiculate to tunnel your own uh protocol. That's why today I'm gonna release a new tool uh which uh allow you to tunnel uh your your uh favorite protocol uh within a SOCKS5 proxy server uh by using uh Google uh Google Cloud. So the tool is called the GSSOCKS. Is a post uh exploitation tool. Uh this time I decided to use uh Go as a language. And uh and uh set up a uh a uh a uh a uh a uh a uh a SOCKS5 proxy in order to vehiculate to tunnel uh every protocol by using proxy chains for example.


## [09:20]


The mechanism is similar to Google Calendar Router. Uh we have 2 2 parts. 2 entities. The GSSOCKS client and the server. The client stays on the attacker machine and the server uh is the is the agent that must be deployed on the on the target machines. Uh this time I decided to use Google Sheets uh because it's the most similar uh service uh that functions as a database. Um the client uh uh open a listener on port uh on a local port. This case a 9191. You can set up uh a proxy chains in order to send uh all the traffic through this port. Uh traffic go over Google Sheets. On the other side the server the agent uh read those information and send them to a proxy server. And then you are able to reach uh every service uh that is uh reachable from the from the target machine. So uh this is the the the Sheets model. Uh we have uh some uh some columns. The socket ID. Uh a label to identify the client or the server.

Uh a time stamp and um and the payload. So uh there are some limitations. Uh for uh for the payload encoding uh I had to use base 64 which uh increase uh the overhead uh about of uh 33 percent. And uh Google Sheets has uh a limit for uh a single cell of 5,000 characters. So um the the first test of which is uh to uh to uh to uh to execute a command. So I was using uh some common tools. PSX sec. PSX sec and secret dumps. So common pen testing tools to uh for Windows exploitation. And uh before the optimization uh PSX sec required about 20 minutes to execute a command. While secret dump required uh 15 minutes to execute uh to to extract uh the the information. So I opted my uh the the software uh splitting uh the the payload the the byte stream uh considering the limitation of 5,000 characters. But the main improvement is uh uh the implementation of um uh rotational account system. So after those uh corrections uh PSX sec required 2 minutes.


## [12:27]


And secret dump uh just 1 minute. So it's pretty usable. Uh this is a demo of uh the execution of secret dump. So um the agent is uh already deployed on a target machine. Uh we won't see that uh here. Uh we set up uh on the uh um right side top uh top right uh uh our client. And we use the other virtual machine on the left uh uh running uh proxy chains uh and secret dump. Secret dump over proxy chains. And on the bottom right uh we can see the information transmitted through Google sheets. So in a few seconds uh it will be completely executed and we'll read all the secrets. For this uh example I used uh about uh 3 and 3 accounts on the client and 4 accounts uh on the on the server. Due to the API quota limits. So it works. Everything has been executed and no direct connection has been performed for this exploitation. If uh if you want to see the uh you try to analyze uh traffic of uh the agent of the server.

You'll see that only uh connection to Google infrastructure uh is established. So it means that uh even uh uh we even um traffic inspection uh won't work against that. Uh for the future I'm gonna analyze further um what can be done in terms of uh analysis but I will release on the uh repository page repository GitHub soon. Google mitigation. During testing uh I I encountered this message. So I was testing and uh some of my account uh has been disabled. So I say oh yeah uh Google catched me. Uh but there is a button right there. Start appeal. And I I started an appeal and uh I was surprised that in less than 1 hour uh my account were fully restored so I continued my test and they have not been blocked again.


## [15:38]


Thank you so much. If you have uh any questions I'll be right there. And uh for my friends, Italian friends uh for Sanaboly. Thank you so much.
