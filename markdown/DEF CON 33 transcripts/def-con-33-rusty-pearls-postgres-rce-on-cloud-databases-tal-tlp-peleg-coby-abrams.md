---
title: "Rusty pearls - Postgres RCE on cloud databases"
speakers: ["Tal 'TLP' Peleg", "Coby Abrams"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - Rusty pearls - Postgres RCE on cloud databases - Tal 'TLP' Peleg, Coby Abrams.eng.txt"
sha256: "1936df1fd20eaf2f2ed9393c59328dfe89d2fe30907929088041122ff20f7dcb"
duration_seconds: 1093
words: 2637
text_chars: 14989
redacted_secrets: 0
converted_at: "2026-08-12T02:50:00Z"
---

# Rusty pearls - Postgres RCE on cloud databases

**Speakers:** Tal 'TLP' Peleg, Coby Abrams  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (18 min, 2,637 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Okay, so let's get started. Okay, so hi, I'm Tal Peleg. I'm a security research team lead at Varonis. I specialize on security currently, so AWS Azure, things like that. And I really like breaking things and fixing them again. I like making music and astrophysics. And I'm Colby Abrams, so I work with Tal at Varonis. As a cloud security researcher as well, I also do IS research. And I'm really passionate about teaching, so I like teaching a lot, and specifically teaching cybersecurity. So yeah, that's us. Let's talk about what's about to happen, what we're going to talk about. So we're going to start by talking just a little bit about how the vulnerability that we found works. Just kind of the basic details. And then later on in the talk, we're going to kind of talk a little bit more about how we found it, what our methodology was, what we found was interesting. And of course, we're going to share with you a little bit about what we found out along the way, and what we think needs to be done now.

If you want to take three things from this talk, first, we found a cool RC on Postgres. We even ran it a bit on the cloud. Two, you should be looking for RCs everywhere, not only in workloads, which are popular now, but any other managed service is now made of so many microservices. Something could go wrong. And three, collaborate before you're running a remote RC during vulnerability research. Okay, so before we start, we're also going to do a little bit of background on Postgres. So Postgres is a relational database. It's open source. It's extendable. It's a really strong database. It's really versatile. And because of these reasons, a lot of cloud providers have, or I think almost all the cloud providers have, an instance of managed Postgres, which is why we were kind of looking at it. So that's just a little bit about Postgres. So this story has two parts. The first one is using Perl to modify environment variables of a Postgres session process.

So... This isn't working. But Postgres has extensions. They allow adding functionality to the database. And one of these types of extensions are language extensions, which allow writing custom functions in programming languages such as SQL, C, Python, Rust, and Perl. And there are two types of languages. There are trusted languages and untrusted languages. So untrusted languages have access to the system. They can access the environment variables.


## [03:00]


They can access files, open sockets, create processes. And only a super user can run them for that reason. And trusted languages have a limited access to the system. Normal users that are not super users can only run trusted language functions. What we were able to do is break that assumption by using the trusted Perl language, PL Perl, in order to change environment variables. Something that should only be done by super users. How does that work? Perl has a magic hash map, a magic variable, the env hash map, and it allows managing environment variables. So you can use it in order to read and write environment variables for the current process. And we assume that something that's embedded so much inside of the Perl language wouldn't be overridden by PL Perl, and we were right. So we can use a function like the next one, like this, in order to modify the path environment variable of our current session process.

Okay, so at this point, we have a pretty strong primitive, right? We can change environment variables, and usually we can leverage that into code execution. The way we leveraged it this time into code execution is using another extension called PL Rust. So, a little bit about Rust. Rust is a compiled language, and what happens when you create a PL Rust function is that you're calling cargo. Cargo is the package manager for Rust, so cargo is going to download the different packages that you need and kind of set up the environment, and then it's going to call Rust C, which is the compiler for Rust. So again, we're going to be running cargo when we create the PL Rust function, and then cargo is going to call Rust C. And this is important because we can change environment variables, right? So, we can kind of control this process using environment variables. PL Rust does try to change and kind of sanitise the environment before running.

They were kind of aware of this, but you can see it's a denialist. So , we have various different environment variables that are moved just before we run cargo. Now, one of those environment variables is called Rusty Wrapper, right? So, Rusty Wrapper, what Rusty Wrapper does is, basically, instead of calling Rust C, once you've set Rusty Wrapper, cargo is going to call a different binary.


## [06:03]


Usually, it's meant to be a bash script that kind of... well, actually, it's supposed to be a wrapper for Rust C, as the name hints. So, they did remove that from the environment, and that would have been really nice for us because we can change the binary that's being run, but what they didn't remove is CargoBuildRustyWrapper, which is a similar environment variable that has the exact same effect. So, we were able to use CargoBuildRustyWrapper to change the binary that's being run when cargo is calling Rusty. Now, we can only change the binary, and with Postgres, we don't have a lot of control over what's happening, so we can't really change anything else. We can just run a binary, and we needed to find something that would be able to run kind of like a script that we want to run, or some kind of injection where we could inject shellcodes. So, we have the RustGDB script. It's going to be a script that's installed with Rust, and what it basically does is execute the RustGDB parameter.

So, another environment variable that we can set, and when we change CargoBuildRustyWrapper to actually call the RustGDB script, we're going to be able to inject bash commands into the RustGDB script with the RustGDB parameter, and we can see that right here. So, again, cargo runs Rusty, or we're going to change it with CargoBuildRustyWrapper, and at this point, we can't change the parameters that are passed, we can't inject commands, but we can change it when we run the RustGDB script, because we can change the RustGDB contents. So, let's see that in action, right? So, first, we're just going to create the extensions that we need to create in order for this to work, so we're going to create the PL Rust extension, and we're going to create the PL Perl extension, and then, right after that, we're going to create a PL Perl function that what it's going to do is it's going to edit the environment variable CargoBuildRustyWrapper to point to RustGDB, and then, after that, we can change the RustGDB parameter to kind of contain the Bash script, the Bash commands that we want to run, and then we're just going to create a PL Rust function.

We don't actually need to do anything in that function, we just need PL Rust to compile the function. So, once we've done that, we can run this Perl function, and as you'll see in a moment, at first, it looks like some kind of error, but we do get the STD out, and we have successfully run code on a Postgres instance. Okay, so what's going on?


## [09:04]


Well, you probably have some questions. How did we find this vulnerability? Why did we choose PL Perl and Rust? And also, we promised you a Cloud RC. So, the idea started after I disclosed a very impactful SQL injection on a database that was hosted on AWS RDS. And I wanted to see what impact a real malicious actor could have on Postgres in RDS. So, when you create a database in RDS, Amazon gives you an admin user, and while it can manage the schema and data, it's not a super user. So, we wanted to find a privileged escalation to gain super user access, or even better, try to run code on the underlying system. So, now we have our objective, running shell commands on Postgres as a non-super user. And this is especially interesting in the Cloud, since breaking that barrier of trust between the user and the Cloud provider, and running in areas that are under the Cloud provider's responsibility, may potentially allow exfiltrating Cloud credentials, or even moving laterally between Cloud customers.

So, we were looking for something like that. So, extensions are a common area to look for vulnerabilities. And we chose Perl, since it's part of the official Postgres repo. So, it comes built in with many installations. That means that it's a lot of impact. Also, Perl is from the 80s, so there's a lot of code written in it. And the 80s, security was much less common. There was much less awareness. And also, Perl has these built-in magic variables, and it's open source, so it's easier to look at. So, now we have the option to edit environment variables with Postgres. So, now what? So, I mentioned that usually it's pretty easy to run code when you're changing environment variables. Postgres actually creates some difficulties for us in this aspect, because there is an API to create background workers within Postgres. So, extensions, when they're creating another process, or doing anything like that, they're supposed to use the API that Postgres provides, which means that we're not creating the process directly.

And if we're not creating the process directly, it's not going to inherit the environment variables that we edited, which means that we can't actually execute code this way. So, what we needed to find was we needed to find an extension, or something in Postgres that was going to run code, or run a binary directly without using this API. And for this, we kind of used GitHub search and Copilot to kind of look through the open source extensions that exist, and find somewhere in the code where that's happening, and try to cause that to happen as a non-superuser.


## [12:04]


So, what we looked for was, you know, the system function, or the execv family of functions. And in Rust, we looked for the command function that creates new commands, and that's how we found out that Rust is actually running cargo directly. So, we promised CloudRCE. We did briefly run code on RDS, right? We were able to execute this on RDS, because they have both PLPerl and PLRust extensions available. Why would we attack our own cloud database? So, like we said earlier, we were interested to see if we could leverage it to access network, or if we could, you know, get in cross-tenant access, or see if there were any interesting tokens that we could have stolen. And what did we find? Well, it was a really locked-down environment, right? We weren't able to do a lot of things. We weren't able to access network. And the other thing that we found is that the AWS incident response team is really good.

So, within a very short time of us running code, we had, like, emails from our CEO and emails from AWS, and they found me on LinkedIn, and we had all different kinds of, like, people asking us what we were doing. And they were also able to shut down our database just in case we were a threat actor. So, really good response from them. Talk a little about how you ran code on RDS. So, yeah. So, we did run into some difficulties because of the limited environment. There were binaries that, like, the Rust GDB script needed that it didn't have, so it wouldn't run and get to the point where it was running the Rust GDB parameter. So, we had to find, like, different ways to kind of play with it a little bit more. So , we had to use the bash-env parameter, which is a really interesting environment parameter that bash actually expands before bash starts. So, that was really interesting. And so, we kind of had to tweak it a little bit just because this environment was so, so limited.

All right. So, we can't leave you without any takeaways. So, first of all, if you're managing a database, keep your database up to date. At least the minor version. So , Postgres patched all the versions since version 12. If you're using an older version than that, I don't know. It's not supported anymore. Do lease privileges. So, if you don't need users to create functions or to install extensions, don't give them that access. And limit the extensions that people can load by using the allowed extensions configuration parameter.


## [15:07]


Don't allow extensions that you're not using. So, if you're not using Perl or you're not using Rust, don't allow them, obviously. So, for cloud providers, I think, and for the community, these kind of vulnerabilities aren't rare. There's a Speckle umbrella story by Imran that you should look up that's really interesting where he did something similar on GCP. We also recently found a vulnerability in Azure Cosmos for Postgres that also allows us to run code on the backend. So, these vulnerabilities, they exist and they're not going away. So, what can we do about that? I think it's really important, right, to have community research. And in this case, it's important to have responsible community research because you're accessing systems and accessing, you know, proprietary code, maybe. But I really think it's important to create a framework where we can have this kind of research to make sure that even if somebody executes one of these vulnerabilities, we're able to test that they're not able to access network resources and not able to get cross-tenant access.

And I think that that's something that's really important. And , you know, some cloud providers do allow this in some way or another. But I think it should become more prevalent. Finally, some tips for ourselves, if you're a security researcher. First of all, environment variables are fun, so you should look for custom environment variables that might allow you to run code. Prepare before running code on sensitive systems. So, collaborate with a cloud provider if you're about to enter a cloud-managed territory. Remember to take pictures along the way. We forgot to take pictures of most of the exploit. Do give your database a good name. So, our database was called Kobe, and that helped AWS contact him via LinkedIn when they thought that our AWS account was being attacked. They also thought that we were researchers since it was research something. And also, collaborate. So, AWS, we're not too happy about having lots of unexpected alerts appearing right before the weekend.

And finally, set your goals before researching. So, make an assessment of potential risks and think what an attacker would want from attacking the system. So, to summarize, the three things that you should remember. We found a cool RSC on Postgres, and it worked for a bit on the cloud. Look for vulnerabilities anywhere, not only workloads. And don't exploit on a major cloud service without telling them beforehand, just before the weekend. Thank you very much. Thank you, guys.


## [18:09]


What happens now, questions? If we have time for questions, then if someone has a question, otherwise we'll be outside.
