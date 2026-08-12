---
title: "From Spoofing to Tunneling - New Red Team Networking Techniques for Initial Access and Evasion"
speakers: ["Shu-Hao", "Tung 123ojp"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_type: "transcript"
source_transcript: "DEF CON 33 - From Spoofing to Tunneling - New Red Team Networking Techniques for Initial Access and Evasion - Shu-Hao, Tung 123ojp.eng.txt"
sha256: "5dd9f600935e0220d07a276f28c98f5b24f73c808905fec2b6732f436e1325ca"
duration_seconds: 2539
words: 4655
text_chars: 26241
redacted_secrets: 0
converted_at: "2026-08-12T06:24:13Z"
---

# From Spoofing to Tunneling - New Red Team Networking Techniques for Initial Access and Evasion

**Speakers:** Shu-Hao, Tung 123ojp  
**Conference:** DEF CON 33  
**Source:** automatic speech-recognition transcript (42 min, 4,655 words). Wording follows the recording and may contain recognition errors; timestamps anchor each section back to the video.


## [00:00]


Okay, thank you everyone. So let's start the talk. Hi, I'm Su Hao from Taiwan. This is my first time to present at DEF CON, and also my first time at DEF CON, and also my first time at Lagos, and not my first time in US. Okay, so thank you all for joining my session. So I'm excited to share some practical Red Team networking techniques with you today. So I guess we can get started. Okay. So now let me take you into a typical day in my IT life, seeing my intranet LDAP server log. And there's a login from Frank. And there's a login from Bob. And then, wow, there's an invalid login from a public IP, 9.9.9.9. And how and why this can happen? This is an intranet server without no destination NAT. So, okay, as an IT, I'll ban that bad IP. But a second later, there's another IP attacking my server again. So how is that possible? That someone can use a public IP address to attack our intranet server.

This is a key point that we are going to discuss in this talk. This presentation will explore ways of lower-level network penetration through virus of internal protocol. This technique can be used for advanced Red Team exercise or can be blocked before they are abused by malicious attackers in your corporate networks. Before we dive into the details, let me briefly introduce myself. Hi, I'm Su Hao Tao from Taiwan. And I now is a Red Teamer Trade Researcher at Tremyco. And I graduated from Tsinghua University in Taiwan and a former HAC-SERC president. I love to play something with networks and network protocols. I started this research for fun and it turned out that it is of great importance to general network security. So I'm sharing my GitHub account here where you can find all the tools and materials of this research. So this is today's agenda. First, I will share some new Red Team techniques using IP spoofing and how we can use that for initial access.

Then, I will reveal the nightmare of VXLAN, including internal hijacking and how buggy routing protocols can lead to IP hijacking and even domain compromise.


## [03:05]


And finally, I will wrap up with some key takeaways before we move on to the Q&A. So first, I want to talk about some spoofing source IP in the public network, also known as WAN. We all know that even in recent years, package spoofing is still possible on public networks. Please know that all the IP addresses are example IP addresses, not any common or public IPs. An attacker with the IP address 2.2.2.2 can send a DNS request with a source IP of 3.3.3.3. That does not belong to itself. And WAN.1.1 will receive the package and it has no way to verify whether the package is a spoofed package or a valid one. And it will send a DNS response to the 3.3.3.3. So the 3.3.3.3 will receive the DNS response with our making a request. This is a typical DDoS, DNS amplification attack. And it still works nowadays. Next, I want to dive into the company network infrastructure. How IT will block a computer from accessing the public network for security purposes.

So, for the best practice, when a package is sent from a crucial server to a public IP, it will arrive to the firewall. And the firewall will drop the package. However, we see some IT just disabled the NAT mechanism on the router. So the package will still forward out to the wide area network. And the remote server will see and receive that package and see that source IP is not valid. So it will either drop that package or respond to an unknown address. And the client will not receive the message. So when your code is completed, it's a mess, but it still works. Because the client still does not receive any response. So the client is not connected to the internet. So, if we consider both situations together, what would happen if we spoofed a source IP address on the intranet? Imagine a rating scenario. The right attacker hacked a company's device, like .1, .3. It can create a tunnel between the C2 server and the compromised device.

After that, it can create a DNS request through the tunnel, which source IP is the attacker public IP, which is 9.9.9.9. When the package arrives the compromised device, it will forward the package to the company intranet router.


## [06:14]


After the router will receive the package, it will look up its routing table and forward the package to the second victim. As we know, if there is no firewall for the second victim, .1, .2, the response package will send back to the attacker through the public intranet. Then, the attacker will receive the package, when there is no evidence that the package comes from .1, .3. The entire TCP or UDB string only shows the IP source, IP is 9.9.9, and IP source 192.168.1.2. So, why IR is hard? In typical lateral movement attacks, the attacker used the IP address for previous compromised machine to target to the next system. This means, when the alarm being triggered, an IR team could simply use network log to trace the attacker path from one compromised machine to the previous one. The IR team could find the relevant log on the previous compromised machine and identify the initial access point.

And then, the IR team will shut down the entire attack chain step by step. However, when spoofing techniques are involved, the source IP in the log will not be the previous compromised machine. So, the IR team will not be able to find the attacker path. They could only see a public IP is attacking their domain controller. Thus, the previous compromised machine will not be caught even if the alarm has triggered and it can change to another public source IP to continue the attack chain if the source IP is banded. Overlooking the attack path, the malicious package source and destination IPs only shows 9.9.9.9 and private IP 192. Thus, no one will know the previous compromised machine is .1.3. On the other hand, the terminal IP is HTTP traffic with a source IP of 7.7.7.7. So, if the 9.9.9 is banded, the attacker can simply switch to another public IP and attack the same target or different target.

The IR team would need to check every router for layer 2 port locks in order to identify the compromised machine. Also, the source MAC address can also be forged at the first hop. So, what if the ISP filter package with a private source IP address?


## [09:18]


We can use H.323 NAT pathway to enable a temporary destination NAT. The attacker can send a special package to 9.9.9.9, which is its C2 server. The NAT router will then create a temporary destination NAT rule for a private IP 1.3.4.4.5 and open to its public IP port 4.4.5. This allows attackers to access private IP 1.3 on port 4.4.5 via 9.9.9.9. So, here's a quick demo. We can see that DAW 241 has a web server at 8080. Initially, the attacker DAW 142 could not access the intranet web server via the public IP. After we create a server and send a H.323 package from the compromised machine, we receive a package from the victim routers. And we know that the router gives me a NAT port to connect to the intranet web server. Also, we can see that the weblog source IP is from a public IP rather than a private IP. So, let's create a breakpoint for the attack chain. Another method discovered by Jimmy Cai involves spoofing a fake TCP sync package from the compromised device.

Using the next target IP as the source IP address, which is .1.3 for now, and sending it to the attacker's server. The SNAT mechanism can be abused as a destination NAT to connect an intranet service. So, this is a second quick demo. We can see that the device at .35 has a web server running at 8080. Initially, the attacker at .131 could not access the intranet web server via the public IP. After we spoof a sync, sync package from the compromised device, using the next target IP and the port as source, and send it to the attacker's server. The router will create a source destination NAT, but we can abuse this route as a de- uh, destination NAT. So, we can, the SNAT mechanism will allow us to connect to the intranet web server. Additionally, we can see that the web server log shows the source IP as a public IP, rather than the private one. So, this also creates a breakpoint in the attack chain.


## [12:26]


So, next, can we replace the tunnel with, uh, official VPN? The answer is yes, in some cases. There are many commercial SSL VPN solutions that can spoof the source IP from the client. As shown in the diagram, commercial SSL VPN like those discussed at CyberSec 2025 may allow this behavior. On the other hand, whether open source VPN solutions like WireGuard or OpenVPN are affected depends on their configuration. So, where's the initial access? Do we have a chance to do this without an initial foothold in intranet? Can we use any existing tunnel? The answer is yes. On the internet exchange, everyone is on the same layer 2 network. Attacker can set a private network range as the next hop to the router of the company you want to attack. Also, the second method, we can abuse an existing tunnel such as GRE, IPIP, or SIP tunnel. But again, a good firewall configuration could cause this fail. So, in the intranet exchange, if we compromise a router at an intranet exchange, or we can just rent an IXP VM to assess an intranet exchange.

We can force a private subnet as the next hop to the victim company router. And then, we can create a connection using our own public IP as the source IP and a private subnet as a destination. The victim router will forward the package to its intranet via its routing table and the intranet target will respond to the attacker to its public IP because the package source IP is a public one. On the other hand, we can abuse existing tunnel like GRE. So first, what is a GRE? GRE is a stateless layer 3 tunnel. This is widely used because it is easy to set up by only setting its protocol GRE public IP and GRE interface IP and its routing table, which is the next hop. Nowadays, there are still a lot of companies that use GRE. Like Cloudflare, Magic Transcend, and its customer. They can choose between IPsec or GRE, and IPsec is safer. And AWS Transit Gateway also supports GRE tunnel, but sadly, it's used for internal networking only.

Also, Security Week reports that APT groups like Salt Typhoon create GRE tunnels to collect traffic from compromised devices.


## [15:35]


Last, a lot of companies also use GRE tunnel, but we don't know. So how does GRE work? When a package wants to go through a GRE tunnel, the kernel will pack the packet with a GRE header and send it over the public internet. At the receiver side, the GRE packet is unpacked and the inner packet is forward according to its routing table. GRE is stateless and doesn't provide any encryption, which means it's possible for everyone can spoof a GRE packet via a public network. For example, a private IP 1.2 wants to send a packet to another site, .2.2. The packet will send to its default gateway. And because it is a GRE tunnel, the gateway router will add a GRE header to the packet and then send it through the public internet. After a GRE packet arrives at 2.2.2, it will remove the GRE header and forward the inner packet according to its routing table. And then the 2.2.2 receives the packet. And if it wants to respond to the packet, the vice versa.

The packet will send back to its default gateway and add the GRE header and send back to the 1.1.1 router and remove the GRE header and send it back to the 1.2. So, how do we find a GRE tunnel? We can use OSINT techniques. For example, we can search for a net floor dashboard like a photo on Google and filter for GRE traffic. This way we can obtain the IP address on both ends of the tunnel. Other OSINT techniques can also help too. Also, we can use GRE spoofing techniques to scan for existing GRE tunnels. First, we can create a GRE tunnel using the command provided above. Then we can craft a GRE packet with a spoofed source IP address that does not belong to us and send it over the public network to the victim. If the victim has a GRE peer conflict with the GRE packet source IP, for example, 1.1.1, it will decapsulate the inner packet and process it according to its routing table and forward to the inner packet.


## [18:38]


So, we can create and send many packets with different source IP addresses to proof of the correct victim peer. If the victim does not recognize the source IP as a known peer, it will drop the packet. On the other hand, if the source IP matches one of the victim known peers, the victim will accept the GRE packet and forward the inner packet according to its routing table. For scanning purpose, we set the destination of the inner packet to the victim itself. So, the victim will immediately reply the inner packet with an ICMP response and send it back to the attacker. Then, we can identify the victim GRE internal peer IP address by its ID finder and sequence. We can encode the information into ICMP ID finder and sequence field, which together can represent all 255 to the part of four possible IPv4 addresses. We also create a scanner script on GitHub. As you can see, when a GRE source address matches the remote GRE peer address, we can get an ICMP reply.

Then, we can put everything together to get an initial access. Let's imagine a scenario the victim 1.1.1 has a GRE internal with 2.2.2. An attacker can forge a GRE packet that appears to be sent from 2.2.2. The inner packet is a DNS request sent from the provider IP 3.3.3 to an internal network IP. When the packet arrives, the victim will trust and use the GRE packet because it can claim to come from 2.2.2.2. Then, the victim will unpack the GRE packet and discover that it contains a DNS request whose destination is a private network IP. The victim will then forward the packet to its company intranet based on its routing table. Then, when the internal DNS server receives the DNS packet, it will respond and send a reply through the public internet to the attacker server.


## [21:48]


Thus, the attacker can interact with services on the victim intranet, including those using the TCP protocol. We have created a demo lab. The architecture is illustrated in the diagram. We have a target router whose GRE peer is 1.1.1. And there is an intranet waste server whose public network is 1.2. The waste server is hosted on 1.2 and the server can access the public network via SNAT. On the other hand, the router has a GRE internal and it can directly access the intranet waste server. And also, he has a public IP and we can see that there is a GRE internal. The peer is 1.1.1.1. So, initially, the attacker at IP address .142 cannot access the private network 192.168.1.2. Then, the attacker can create a spoofed GRE internal via the command shown above to the victim router and directly send traffic to the private address 1.2 through the fake internal. Then, the attacker can direct access and interact with the internal waste server.

Similarly, if the layer 2 internal like GRE tab, also, if we can leak the victim MAC address, we can also exploit this in the same way. It is common to use the SNMP protocol to obtain this. For a short TLDR summary, when a company does not configure its firewall and use database on encrypted internal, even if it is a legacy configuration, an attacker can exploit this internal for initial access to the intranet. So, then, we will reveal a nightmare of default configuration of VXLAN. So, what is a VXLAN? VXLAN is a stateless and unencrypted layer 2 internal. It packs layer 2 Ethernet frame into a layer 4 UDP packet. Each subnet is uniquely identified by a name called VNI. We can configure VXLAN internal similar to the GRE by giving the remote IP, local IP, and destination port and VNI.


## [24:54]


However, this configuration is vulnerable. Based on the previous configuration, set up a standard VXLAN peer is easy as usual. How about hijacking a VXLAN internal? Yes, here's the only difference. The only thing you have to change is your local IP argument. So, why does this happen? Does the Linux kernel doesn't check the source IP for VXLAN packet? How does it accept VXLAN packet with a valid VNI import even if the source IP is not configured? After looking at the Linux memo, you will see that this is a feature but not a bug. But this feature is insecure and it turned on by default. Before reporting, router OS couldn't turn this feature down. Now, you can change the setting to off but it's still on by default. So, what happens when learning is enabled in VXLAN? Normally, when a configured peer sends a VXLAN packet, the kernel will add its MAC address to the FDB, also known as forwarding database table, shown at the bottom on the slide.

The next time a packet needed to be sent to the destination MAC address that is listed in the FDB table, the kernel will pack and send the packet to the remote location using the information from the FDB table. Similarly, when learning mode is enabled, any VXLAN packet with a valid VNI import will be added to the FDB table. Also, the remote IP could be any IP on the internet. Thus, an attacker 9.9.9.9 can create a VXLAN packet with a MAC address which is broadcast address FFFFF. And the Linux kernel will add this MAC address to the list. Then, when the kernel wants to send a broadcast package on the VXLAN interface, it will look up the FDB table and then send it to the attacker server, which is 9.9.9.9. So, we know how VXLAN works.


## [27:56]


How do we get the information that we can hijack a VXLAN? We know our own IP, but we don't know the victim's IP, or VNI, or VXLAN inner subnet. However, all this information can be obtained by a simple scan. An attacker can discover the victim IP port and VNI by sending numerous packets. So, let's focus on how to determine the VXLAN inner subnet range. We can gather information by sending a single VXLAN packet where both the source and destination MAC address are set to the broadcast address LAN. When an ARP request is sent from the VXLAN interface, they will also send a copy to the attacker. Another method involves sending a neighbor-discovered protocol packet. When a router always receives a broadcast neighbor-discovered protocol, NDP, message, it will respond to the broadcasting MAC address with its own IP and MAC address. Thus, we can send numerous VXLAN packets with different VNI and port configurations.

Each contains an inner NDP packet where both the source and destination MAC address are set to the broadcast address. When the VNI and port matches the victim configuration, the victim device will add the attacker's IP to its FDB table. Then, the victim unpacks the VXLAN package and sees that it is an NDP request. The victim router replies to the NDP packet and tries to send a response to the broadcast MAC address. It checks the FDB table and finds that the destination is 9.9.9.9, which is the attacker IP. So, the router will send the packet to the attacker. Then, the attacker has everything to hijack the terminal. We create a scanner. We can discover the victim IP port and VNI by sending numerous packets. VXLAN has default ports 4789 and 8472, and VNI is usually smaller than 100. Here's a scanner link. We have also created a lab for VXLAN scanner demonstration, which includes a router and a web server.


## [31:05]


So, for demo, we can see that the scanner aims to scan the target at .200. The scanner sends numerous packets with different default ports and different VNIs. Later, we can receive an NDP reply with VNI 42 and port 8472. The inerts are made in 10.0.0.1. Then, by simplifying, we can simply create a VXLAN with the information above. We can direct access the VXLAN intranet server. We also scan for insecure VXLAN configuration worldwide. Usually, using VNI equals one and default ports. We found that more than 900 VXLAN endpoints respond to the scanner. Additionally, there are 4,000 IPs inside the VXLAN subnet. Some of these are public IPs, which means we can hijack public IPs. Additionally, some endpoints reply to numerous broadcast packets. Combined with the IP spoofing, this can lead to DDoS attack. Lastly, we see some VXLAN packets have source IPs that are private addresses. This raises a question.

Why are the private addresses being used as a source IP on the VXLAN packet? So, if I use VXLAN in an encrypted terminal, am I safe? The answer is no. VXLAN still accepts packet traffic in different interfaces. So, if you have a public IP interface and also you create a VXLAN interface, it can be scanned and hijacked. For TLDR, we can hijack a VXLAN terminal using only 3 pieces of concept. The victim IP address, the VXLAN port, and the VNI. There is no need to know the peer IP and internal IP address. Furthermore, if your network is set up including a public IP address and VXLAN on any interface, it is highly vulnerable. So, what can hackers do after hijacking a VXLAN terminal? Not only can attackers gain initial access to the company intranet, but also they can hijack IP communication or perform a man-in-the-middle attack between the two sites. Additionally, attackers can target their two network services such as exporting RADVD to RCE vulnerabilities.


## [34:11]


Incident response is challenging because the source IP cannot be trusted. Moreover, these terminals often run routing protocols like BGP or OSPF. Attackers can hijack IPs that are even not transmissioning through that terminal, such as those of a domain controller or an EXXI server. So, what is a routing protocol? It is a protocol like a router can exchange routes and network information with other routers. Routing protocols help routers to directly learn about the networks around them and to determine the best path for forwarding the packet. For example, Router A has a subnet 192.168.1.0.24 and Router C could learn the routes from Router B by routing protocols. We often see companies use VXLAN terminals to connect to sites with routing protocols. But when we combine this with a learning feature, we can hijack router's AIP. Then, we can announce, we can connect to the routing protocols and announce domain controller's IP in the routing protocols.

With slash 72. Other routers will receive and trust the routing prefix and redirect their domain controller's traffic to the attacker because the route is more specific, more smaller than the subnet. We have summarized the potential impact of hijacking different service IP. If an attacker hijacks the IP of domain controller and NTLN is possible, meaning SMB signing is disabled or ADCS ESC 8 is present, they can take over the entire domain. If an attacker hijacks the IP of vSphere, Proxmox or any HTTPS service and the original SSL certificate is unsigned or not valid, user may not be noticed. And the attacker can then take over the account or the full server. In short, hijacking this service IP can lead to account takeover, denial of service, DNS hijack or even full domain compromise or server compromise. And here's a bonus.


## [37:11]


A bad configuration in the company's OSPF lead to IP hijacking. This attack factor has been published for years and we actually observed it during our rating scenario. Yet, very few people discuss it. Do you check and use a TCP dump after you get into an intranet? If you see this on the victim intranet, it might be vulnerable. Just like the exploitation method described in the previous slide, if you see a hello package, there is a highly possible that you can direct establish an OSPF connection with the router and hijack the routes. So, in short, we can, if we connect to the OSPF, we can hijack the domain controller again and get previous escalation. Next, there are some key takeaways. Here's the key takeaways for Blue Team. First, check all unencrypted tunnels in your company's network. If you find any, don't use them. This includes protocols like GRE, IPIP, SIT, GRE-TAP and DXLAN. These tunnels are not secure and can be abused by attackers.

Next, make sure you have secure firewall in place. Your firewall should filter outbound intranet traffic, especially SYN-ASDK packet with a response from server. Also, check for IP spoofing in your intranet. Ideally, OSPF should fill out spoofed IP address, but in reality, this is rarely possible. Check if OSPF is not enabled on ports between routers. It's only enabled on ports between routers. OSPF should not open on unnecessary port. Monitor your routing prefix for any anomalies. Unaccept change in router protocol can indicate an ongoing attack. Finally, set minimum accept prefix size in your routing protocol, for example, slash 24. In summary, avoid unencrypted tunnels, secure your firewall, filter for IP spoofing, restrict OSPF, monitor routing and enforce minimum prefix size. And here's the takeaway for writing. First, scan or use OSINT techniques to find victims on encrypted tunnels.


## [40:12]


These can be entry point into the network. Once you are inside the intranet, check the victim's network setup for spoofing. Use source IP spoofing techniques during high-risk scanning to avoid detection. Look for OSPF upload message to identify active routing protocols and potential attack path. Scan for misconfiguration via extended tunnel. If you find a vulnerable tunnel, hijack it to get initial access. Abuse routing protocols and hijack IP for lateral movement and privilege escalation. Automating can continue looking for more vulnerable protocols in future. Remember, scan, find, hack. And here are some takeaway for tool makers. First, implement intranet IP spoofing command control tools. Develop automated tools to test possible of IP spoofing within a target intranet. Create automation save times. Create automated correction mechanism for mismatch between IP destination and source address within the same TCP session.

Some routers still perform SNAT. Even the packet is a server response. Automate the process of sending H.323 package or new TCP packet to trigger a routing mechanism. Especially for ISP that filter private IP as a source IP address. Develop tools for automation OSPF IP hijacking attacks. And finally, implement a more efficient GIS scanner for global scanning. Similar to what MaxScan does for TCP. So, thank you everyone.
