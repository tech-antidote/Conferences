---
title: "Browser Extension Clickjacking - One Click and Your Credit Card Is Stolen"
speakers: ["Marek Tóth"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Browser Extension Clickjacking - One Click and Your Credit Card Is Stolen - Marek Tóth.eng.txt"
sha256: "8f81d449094cc7ad87a4537fc33aaf3c9567139209b1ca64f6f4992cc3921c39"
duration_seconds: 2996
words: 4859
text_chars: 27104
redacted_secrets: 0
converted_at: "2026-08-12T06:24:13Z"
---

# Browser Extension Clickjacking - One Click and Your Credit Card Is Stolen

**Speakers:** Marek Tóth  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (49 min, 4,859 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Hello and welcome to my talk. My topic is about browser extension click checking and one click and your credit card is stolen. This is me. I have about seven years experience in cyber security. During a day I do penetration tester but in my free time I do security research. This is the reason why I am here as independent security researcher and I am from Czech Republic and my focus is web application security. As you probably know, that click checking vulnerability is out of scope on many programs and if it is accepted, it is not a problem. Then it doesn't mean if it has some severity or give you some rewards. And the reason is that the click checking vulnerability, the click checking vulnerability in these days is very, very protected and can be ‑‑ and it cannot be exploitable when someone is using it. Or the developers set headers like extreme options, content security policy and could be used, for example, some side cookies likes and strict.

In my research, I just want to say that click checking is not that because in my research, when I reported click checking vulnerability, it has still security impact on users and I received some bounties and someone I received, let's say, nice bounty. I will start with very, very basic introduction to the topic. The first will be about intrusive web elements. The intrusive web elements, that is the annoying element what everyone we see on the Internet and it could be, for example, cookies banner and you need to click for accepting or declining cookies or there could be some newsletter pop‑ups or log‑in dialogues and other clicks from the user. For example, this is website or this is the Instagram with DEF CON and you can see if you are logged out, then you will see that you need to accept the cookies or decline cookies.


## [03:00]


After that, it's showing you another window for closing or log‑in and then you will see the content and if you want to see the comments, you need to click again. So the user, users usually clicking and needs to, for closing some dialogues and it could be web push notifications and other clicks could be. Or CloudFlare challenge page, the CAPTCHA page, what everyone hates it, but there is another click that you need to click on the check box to verify that you are human. And so basically, one, two, three clicks are from the user commonly required before accessing the content. And the reason, the reason why I am telling you that I will use this web element for forcing user to click somewhere. Another is about the click‑checking web applications. And that's vulnerability where the malicious page loads target site in the transparent iframe and use opacity zero and the result is that users unknowingly clicks on invisible target site in iframe.

And it could be used with basic iframe elements where is the source, there is the target site and there is used opacity zero in style. But how I mentioned in the beginning, the web click‑checking vulnerability is mostly without impact because the user is not locked in the cross‑site iframe. Another what you should know that just very basic that browser extension has some parts like background scripts which is scripts that are running in the background and if you just switch or change domain and switch the top, you will be still locked to the extension. There is the content scripts which modifying and reading web content of the page. There is the configuration file, manifest.json and their developer definitions, background scripts, content scripts could be loaded from the browser if you know extension ID or it could be accessible from the local device in your profile.


## [06:05]


The manifest could look like this, this is for example from manifest.json and you can see that there is like background scripts loading, there is some content scripts, permissions and for example web accessible resources that is files that are ‑‑ that could be loaded across domain. For browser extension it's important that authentication persists across browser session. And developer has more responsibility for security than web application developer because in web applications some security can provide browser, he can check same origin policy, course request, cookies, but in extension needs to developer set the rules. And the last one for introduction is password managers and for my research I select references from the PC mark where is article about the best password managers for 2025, it was updated in April and there was these password managers and I used ‑‑ I tested this password managers on my new technique.

So for example, one password and not only this, I selected another one and this is iCloud passwords and the reason is a lot of users use this browser extension. And I just want to mention that I just test browser extension, not the system application what is in Mac and what is integrated in Safari. So I mean the browser extension what can be used in Google Chrome, Microsoft Edge and Firefox and others. Password managers have autofill feature and could be two types. Automatic autofill where the credentials are automatically filled in, that means that it's zero click. And another type is manual autofill where the user interaction is required to fill in credentials. That means that he selecting the user name from the drop down menu. And because my talk is about click checking, I will focus on the second type, the manual autofill.


## [09:14]


So browser extension click checking can be separate to two types. The first type is iFrame based. And before I start, I have some demo, let's say video, and you can just guess what's happened there. So now from the beginning, you can see that the user just clicking to verify that he is human, refreshing the capture, solve the puzzle, and then just click on to verify. And he is verified. So you can just guess what happened there. And I will continue and after a few minutes I will tell you what happened. So iFrame based is publicly known click checking technique, and it's used misconfiguration in manifest.json. And that was what I showed you a few minutes ago, and this part sets files that could be loaded across domain. There is the file that I showed you, the file that I showed you, the file that I showed you, the file that I showed you, and the file that I showed you . So the difference between manifest, v2 and v3, in the oldest, there was missing the matches, and in the new one, in the matches, you can set for which domain can be accessible, the file that you want to access .

In v3, it's again used iFrame, there is a source with the extension ID and file which is in web accessible resources. And after that, user just set opacity zero if he wants to make transparent the file. In December 2023, I found that NordPass has in web accessible resources has HTML, and this HTML was, or it is still, it's interface of the NordPass, so I was able to load interface in different domain. And you can see that there is manifest version 2, that means that here missing matches, so I was able to load in different. And this is the proof that I was really able to load interface on my domain.


## [12:26]


And I have second demo, and now with the results. So now you will see what will be. So clicking verifying was selecting all items. After that, refreshing was share button. The puzzle contains attackers email address, and if you drop there, there will be for sharing, and verify is share. And you can see that attacker received notification that account's victim shared items with him, and you can see that it was very, account's victim, and he can just accept, he has access to plain text passwords with full rights to his NordPass manager account. So with four clicks, the user, all NordPass items could be shared with attacker, and could be shared credit cards, personal data, logins, pass keys, but very important that victim didn't receive notification. And for this vulnerability, I received $10,000. Mitigation for iframe based is that developer needs to set only necessary files in web accessible resources.

He needs to whitelist domain in the matches, and after that, set X frame options or content security policy for HTML files. And that was iframe based, and it wasn't my primary scope in our research. My primary scope was on DOM based. And DOM based extension click checking is vulnerability where malicious script manipulates UI elements that browser extensions injected into DOM. And you can see in the bottom that there is elements which, for example, password managers injected into DOM and can be somehow manipulated. In this category, iframe is not used, and it will be used that browser extension adds elements to the DOM, and the user changes the element's visibility using JavaScript.


## [15:33]


You can see in the bottom again that, for example, the screen with proton pass, that first screen is opacity one, then opacity zero five, and opacity zero. So user cannot see what is there. The opacity or using this type of vulnerability can be used with setting changing opacity or overlaying UI. I used manual autofill feature for increasing impact in password managers. I used this feature in the DOM . And now this is just basic case how it could be used for password managers, how it should be the steps in exploit script. So the first one is that it's great, the intrusive element like cookie content, the cloud fire capture, and others. After that, it's great, it is used for example, for the form input. Then it sets transparency for the form with changing opacity. Then it's used for the form input, that means that autofill drop down menu will appear. The user, the script then make UI invisible with the user's own UI.

So the user can see what is Dom-based extension, so the user will not see the menu. And when the user just accepts reject cookies, that means that he clicks on invisible UI and data will be filled into the created form and the attacker just gets data from the form values. The Dom-based extension can be separated to some categories, to some types. The first type is extension element and root element. In this type, it's a goal to just change opacity for the root element. You can see there is the root. So in this category, it's needed to change opacity for them. So I used just very, very basic selector for the root element and set opacity for them. And in this moment, I was successful and the user could set opacity for them.


## [18:33]


And if I set zero, it will be invisible for the user. Another subcategory is child element. It's very similar to the first one. And you can see that, again, a proton pass with a different version. And I wasn't able to set opacity for the root element. And they used a day changing suffix for the root element. So I needed to find it for first. And after, I was able to set opacity for the child. So I firstly find the root element and set opacity for the child. And this mostly the case where developer used shadow root open. And you can see after that, it's set opacity zero and user cannot see nothing. And, yeah. Another type is parent element. And first type is first subcategory is body. So now I cannot change opacity for the root element, for the extension element. So I need to move up. And there is body. Because the element is in body. So for my case, for the quick checking, I will change opacity for the body.

And if I set, for example, 2.2 or 0.2, then it will be a little bit transparent. And if I set zero, it will be completely transparent for the user. And now what? I have transparent body, but there is element which can be used. And it's HTML. HTML is not used for frontend developing, but in my case, it could help. Because for the HTML, I will set background image with the same picture what is website looks like. And after that, you will not see body, but you will still see the website, but it's only the image. And you can see that if I increase opacity, then if you just click on the cookies, you will click on the autofill menu. And I have demo. Just for the beginning.


## [21:42]


Right now, you can see that I set opacity 0.5 with background image, and you can see that I can click on the autofill menu. And I just prepared terminal with attacker, and when I changed where is the opacity is 0, you can see that. And when it clicks, attacker receives card number, expiry date, and security code. Another subcategory is HTML. It's, again, very similar, but it's very complicated to exploit it because everything is transparent. It's less practical because user just will see blank page. For exploitation, that should be used some clicking game for like reaction game that user needs to click on the whiteboard or something like that, and after that, the web page tells the user the reaction game on the white color. Another is overlay. And the first type is partial overlay. The extensions elements has mostly has the Z index, Z index is with highest level, highest value, so you cannot easily overlay with that you will have highest Z index value.

So you need to put your element behind the extension. And because it's not full type of overlay, it's just partial overlay, then I will just put elements around the UI. So I will create div 1, div 2, div 3, div 4, and in the middle will be still auto fill menu and still will be clickable and can be used for the attack. And for the divs, I can set again some background image or code and then it should look like this. So the user, when he clicks for closing, he clicks on the auto fill menu and I am able to steal his data.


## [24:46]


The last type is full overlay. And again, I put element behind, behind extensions elements, and right now, I have elements which I cannot, I cannot click on extension, auto fill extension, because there is overlaying and for this case, it could be used pointer events now. It makes me, that makes the element is clickable through and if user just click on the div 1, he is not clicking on div 1, but is clicking through, this means he clicks on extensions element. This is first one that it should be behind, but another type could be that will be used, will be created element that used pop over API and pop over API makes my elements as the top layer and I again can set pointer events now, so my elements will be every time on top and everything under could be clickable. So, I create element to this part and you can see that the top layer is used, my new elements and is used pointer events now. And the extension UI is under and if I just change the opacity, we can see that it's still there, oh, sorry, it's under and can be again clickable.

And I have another demo with the proof that again it works. So, this is with using opacity 0.5 and you can see that the user still can see that it's something there and I use the top layer on the top and you can see that if I move the mouse, I can click on the auto fill menu and when I change the side for opacity 0, then user will see that and just clicking and I receive the data.


## [27:48]


So, this is complete, all categories of the DOM based extension click jacking. This is how, kind of looks like the exploit code what I used in the last video for full overlay. You can see that in the beginning is cookie banner what I used and I set pop over API for them and it's used and after one second, after showing the cookies banner, it's creating personal data form with the use of the focus function on the name and the personal form has on change event get data and get data just I'm receiving data from the form values and when password managers fillings the data then starting from the beginning so I just only check the last one and if I receive the last one, after that I just send it to my server. When I receive it, I just make hidden the personal form and the cookies banner. The position could be two types. The first one is fix it click position. That means that you can put the auto fill menu under like for clicking like accept the client cookies for the check box for verifying we are human or for closing dialogue.

Another type is under mouse cursor. That means that it will follow your cursor and could be set for extension element that you can override the position and it will be follows your mouse or for the form will be used position of the mouse and every 100 milliseconds will be used focused on the input. That means that UI will follow the form. And for imaging, I have another demo for them for that. I just... yeah, and you can see it's every time under my mouse and when I click, I every time click on the auto fill menu.


## [30:49]


So basically just one click anywhere on the website, it could lead to data leak. And now it's time of the truth. This is just a table with how many or who was vulnerable on this type of attack and the results are that all of them. And if I have the specific type that you can see, the only... the basic extension element was protected only for a few but the others categories were vulnerable. The impact could be that could be used on the attacker's website and the attacker can receive information like credit card, that means that credit card number, expiration date and security code and personal data like name, email, phone and address. And the reason is that these data are not domain specific and can be auto filled anywhere. And what's about the results? Six out of nine that supports this function or this manual auto fill for credit cards, so six out of nine were vulnerable and you can see for example, it's not supported because right now it doesn't have the manual auto fill feature.

You can just copy paste from the password manager but it doesn't have the auto fill feature. For personal data, it was like that. So only if I count, one is not supported so I have ten and two was let's say protected so eight of the ten were vulnerable on this type of attack. And I have another demo and I have demo when you just visited attacker's website and you will see if it works or not. So this is, I use the robot form for this attack and you can see user just click the verifying then it's showing cookies banner, another click, another data.


## [34:14]


And I have to prove that it was really from the robot form password manager. So that was about credit card and personal data on attacker's website. Another type could be website with vulnerability like cross-site scripting, subdomain takeover, web cache poisoning and others and others. And for this could be leaked login credentials like username, password and second factor code, because the two-factor code could be used in password manager and if you just visited login form then it will be automatically filled to your form. There is one limitation that only credentials for vulnerable domain can be stealed. But on the other hand, there is advantage that all password managers allowed autofill on different subdomain by default. And what doesn't mean that this is screen from one password and you can see the default behavior that it will fill anywhere on the website. And if I change the behavior, you can see that never on subdomain or parent's domain.

But default behavior is filled anywhere on the website. That means if I saved credentials like on the just main domain, that could be autofilled anywhere on subdomain or subdomain another types. Or if I just saved credential on subdomain, it could be autofilled on the main domain. And this behavior was for all password managers. So that means if you use for example Google, account on Google, then your credentials could be saved or will be saved on account.google.com. For the attacker, that means that he can find, for example, cross-site scripting vulnerability on this domain and can use this technique and steal your credentials. So let's say that cross-site scripting is not remote code execution and it could be easily find if someone really want.


## [37:15]


I can do results. And for the login, only one was protected and that was Dashlane. But I need to mention that Dashlane has automatic autofill by default. So for them, if you visit some trusted domain, it will be autofilled just without clicking. For TOTP, it was very, very similar. Let's say now that I want to just use, let's say that I found cross-site scripting vulnerability on trusted domain and I will use, let's say I want all data what user have in his password manager. So I can combine several dialogues and each clicks give me data from his password manager. I have another demo and that will be just example. When someone find cross-site scripting vulnerability and just share link, for example, on Twitter and you just click and you will see how it can look like. So again, the terminal which is empty and post. You can see that credentials for accounts.google. Password is password and verification code is ending 1, 4, 2.

Right now. And here is some post on X and it's issuetracker.google.com. If user just open it, I'm on the domain. So the first click. Second. And third. Yeah. And you can see that the password TOTP was what I showed to you and the data will be exactly the same what I have in password manager. You can see the card number, expiry date and security code and, of course, my address and my birthday.


## [40:15]


Another impact could be for passkeys and there could be authentication flow hijacking but, unfortunately, I needed to remove this part because it's needed to remove this part because of time and you can see that the flow hijacking on my research but, basically, it's very same that for the dialogue can be set opacity that user not see the dialogue for passkeys and when accepted and when passkeys implementation doesn't have oh, sorry, yeah, it's very, it's a strict domain limitation for that and there is problematic when session is not bound to the challenge then the sign it assertion, the challenge request can be used without cookie. That means that with cross-site scripting could be stolen just the sign it assertion request from the attacker and can use this request on the server. When I tested the federal alliance certified solutions so I tested seven solutions and four of them were vulnerable on this type that means that the challenge wasn't bound to the session and the impact could be that one click, one user click and attacker could be locked as the victim with the new session and attacker can add new passkey device that means that he received the persistent access to the account and for the passkeys was results like this so free was protected and at this moment the dashlane was the part where was vulnerable on the DOM based extension click checking and now about the fixed status that's from I think last week And I want to mention that everything I reported in April this year, and I told them that I will share results in July, and it's August, so this is results.

And today's morning I checked one password, Bitwarden, and I called password, and it's still vulnerable. So I'm not sure if I will click anywhere, but this is the results.


## [43:20]


And about users at risk, it's very complicated to count it, but when I reported the vulnerabilities, then it was active about 40 million installations when I reported the vulnerability. The attacker can detect all password managers just in one script. He just used the new form, and for the new form just used focus for password input. And after that, he just checked what is dumb and used the correct method for them. So he just can see that there is one password element, and so he will use the, for example, the opacity type, the parent elements type. There is the limitation. One of them is the auto logout feature for inactivity time, and it's by default enabled for one password and pass. For others, too, but it's less than one day, what I found. The auto log is for iCloud password, but autofill feature can be used, even application is locked. So you can see that autofill still can be used, and if I click even the application is locked, I can use it.

Another limitation is closing the browser. For example, has this functionality, so this is another limitation which could be. Another user has to have the stored credentials for the domain, and the attacker needs to find the vulnerability, and click is needed from the user. About the mitigation, so for extension element, their styles cannot be changed and could be used, for example, mutation observer API, could be used closed shadow root. For parent element, there could be detection for the body and HTML opacity, and you can use, for example, the DOM element, and for extension overlay, you need to detect the last DOM element, and you can just listing of all popover elements and check if your is last. It could be used, for example, elements from points for partial overlay, but there is problematic that pointer events now will be ignored.


## [46:22]


So you cannot use for full overlay attack. And doesn't exist for this vulnerability, doesn't exist simple protection, and probably new browser API should be created, because right now it's very complicated and needs to be checked a lot of parts in the DOM. Recommendation for users, you can, for example, disable manual autofill and just use copy-paste, but I know that it could be inconvenient for someone. Another type could be that you set only exact URL for autofill credentials, but still can be exploitable for credit cards or personal data. Some hybrid solution could be that for Chromium-based browser, that you will set site access, and you will set site access only on click. That means that if you set this settings, that on the left you can see if you have enabled on click, and every time you need just click on your extension, click on the reload, and after that, on your request will be autofilled the data.

So just the summary, all browsers password managers in the research were vulnerable. Fixit are NordPass, ProtonPass, RoboForm, Dashlane, and Keeper, and still vulnerable are Bitwarden, 1Password, and others, but for Bitwarden and 1Password could be used, for example, the attacker's website, and I think a lot of users use these password managers. So for takeaway, that the click checking is not bad. Browser extensions are vulnerable, could be vulnerable on iFrame-based, and especially to the DOM-based. Malicious script can be anywhere, so the cross-site scripting, it can be found very, very easily, so just only one click and attacker gets your credentials, including the second factor, and no vulnerability is needed to leak your credit card personal data. And this research was only 11 password managers, so that means others' DOM-manipulating extension could be vulnerable, so like others' password managers, crypto-wallets, nodes, extensions, and others.


## [49:26]


The research and presentation is now available on my website, and you can just type the short URL, and you can see that, and here is some references. Thank you for attention. Thank you very much. I think that I have a little bit over than five minutes, so I will be there for some questions if you want, so thank you very much.
