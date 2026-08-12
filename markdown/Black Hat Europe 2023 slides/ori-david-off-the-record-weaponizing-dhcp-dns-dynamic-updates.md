---
title: "Off The Record - Weaponizing DHCP DNS Dynamic Updates"
speakers: ["Ori David"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Ori David_Off The Record - Weaponizing DHCP DNS Dynamic Updates.pdf"
pages: 53
sha256: "ce8ea99b35d72dccb547a57c287fd0b9927c7e6f07f8d05fc8d175e2467aef2c"
text_chars: 9748
ocr_pages: 7
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:12:57Z"
---
# Off The Record - Weaponizing DHCP DNS Dynamic Updates

**Speakers:** Ori David  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Ori David_Off The Record - Weaponizing DHCP DNS Dynamic Updates.pdf` (53 pages)


## Slide 1

#### **Off The Record: Weaponizing DHCP DNS Dynamic Updates**

###### **Ori David**

**1** © 2022 Akamai | Confidential

## Slide 2

##### **Agenda**

● Unfamiliar attack surface in Active Directory

● Series of attacks allowing **DNS records overwrite without authentication** ● Mitigations

## Slide 3

##### **_whoami_**

**Ori David** Security Researcher at Akamai Background in red teaming & threat hunting @oridavid123

## Slide 4

##### **It’s always DNS**

- DNS exposes a lot of attack opportunities

   - DNS Spoofing

   - DNS Tunneling

   - DNS Amplification

   - …

- Decided to look at DNS in Active Directory domains

## Slide 5

##### **ADI DNS**

Every domain requires an Active Directory Integrated DNS zone

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ADI DNS
Every domain requires an Active Directory Integrated DNS zone
es DNS
rward Lookup Zones
| omsdecs.aka.test
aka.test
Reverse Lookup Zones
Trust Points
Conditional Forwarders
Cached Lookups
Mame
Fe _msdes
fa | _sites
J tcp
| _udp
| DomainDnsZones
| ForestDnsZones
FF] (same as parent folder)
FE] (same as parent folder)
FE] (same as parent folder)
Start of Authority ($
Name Server (MS)
Host (4)
Host (4)
Host (4)
OA)
2,25,14,123
172.25.14.101
```

## Slide 6

##### **DNS Dynamic Updates**

Every Windows host manages its own DNS record

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DNS Dynamic Updates
Every Windows host manages its own DNS record
Domain Name System (query)
Length: 163
Transaction ID: @xd783
Flags: @x280@ Dynamic update
Zones: 1
Prerequisites: @
Updates: 1
Additional RRs:
Zone
Updates
Y PC.aka.test: type A, class IN, addr 172.25.14.102
Name: PC.aka.test
Type: A (Host Address) (1)
Class: IN (@x@@@1)
Time to live: 6@@ (10 minutes)
```

## Slide 7

##### **Secure Dynamic Updates**

By default, DNS updates are Kerberos authenticated

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Secure Dynamic Updates
By default, DNS updates are Kerberos authenticated
v Key Data: 6 67786062b0601050562a082066b30820667ab0d3G0b06892a8 #712010202a2...
~~ GSS-API Generic Security Service Application Program Interface
OID: 1.3.6.1.5.5.2 (SPNEGO - Simple Protected Negotiation)
w Simple Protected Negotiation
w negTokenInit
mechTypes:
mechToken: ; 8. 626637a003020105a180302010ea2...
~ krebS_ blob: 6 7a003020105a10302010ea2...
KRBS OID: 1.:
krb5S tok id:
~ Kerberos
Vv ap-reg
pyno: 5
msg-type: krb-ap-req (14)
Padding: @
ap-options: @G8B8B8BRE
ticket
```

## Slide 8

- **Secure Dynamic Updates** Updates are authorized based on ACLs ● Once created - every machine controls its own record

- Authenticated users can create records for non-existing names

## Slide 9

##### **DHCP & DNS**

**<u>DHCP</u>** provide a unique IP address and other network configuration for network clients

**<u>DHCP DNS Dynamic Update</u>** DHCP feature to create a DNS record on behalf of DHCP clients

## Slide 10

##### **DHCP DNS Dynamic Update**

2.DNS Update Request
Add PC.aka.test A
DHCP 10.0.0.1 DNS
Server Server
PC
10.0.0.1
PC

## Slide 11

**Performing Updates - Demo**

## Slide 12

##### **DHCP DNS Dynamic Update Potential Impact**

Unauthenticated Default Popular

Bypass ADI-DNS authentication requirement - any client can lease an IP address from the DHCP server Enabled by default on Microsoft DHCP

Microsoft DHCP server is very common

## Slide 13

##### **Microsoft DHCP server**

We saw Microsoft DHCP in 40% of the networks that we monitor

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft DHCP server
We saw Microsoft DHCP in 40% of the networks that we monitor
Environment: Prod 169.254.0.0/16
”
67 67
67—_
Environment: VPN
67 —>
Environment: Users Environment: DMZ-ENV
—67
=
Environment: Printers
67
@
a Internet destinations
10.0.0.0/8 192.168.0.0/16 172.16.0.0/12
```

## Slide 14

##### **Abusing DHCP DNS Dynamic Updates**

- How can we abuse the ability to create DNS records?

- Previous name resolution attacks:

   - LLMNR/NBNS Spoofing

   - ADI-DNS Spoofing

## Slide 15

##### **LLMNR/NBNS Spoofing**

DNS
Server
4.LLMNR Response
PC.aka.test - <Attacker IP>
Victim

## Slide 16

##### **LLMNR/NBNS Spoofing**

DNS
Server
Victim

## Slide 17

##### **LLMNR/NBNS Spoofing**

✔ Doesn’t require authentication

✘ Only works against targets in the same LAN

## Slide 18

##### **ADI-DNS Spoofing**

DNS
Server
4.DNS Update
PC.aka.test - <Attacker IP>
Victim

## Slide 19

##### **ADI-DNS Spoofing**

✔ Works against all targets in the domain

✘ Requires authentication

## Slide 20

# **DDSpoofing** DHCP DNS Spoofing

## Slide 21

##### **DHCP DNS Spoofing**

5.DNS Update
PC.aka.test - <Attacker IP>
DHCP  DNS
Server Server
4.DHCP Request
FQDN: PC.aka.test
Victim

## Slide 22

##### **Comparing to existing attacks**

Attack Works Without Works Across Subnets Credentials LLMNR/NBNS Spoofing ✔ ✘ ADI-DNS Spoofing ✘ ✔ DHCP DNS Spoofing ✔ ✔

## Slide 23

**Working Towards DNS Overwrites**

## Slide 24

##### **Working Towards Overwrites**

**2.DNS Update Request** Add PC.aka.test A 10.0.0.11 Authentication: DHCP$ DNS DHCP Server Server **3.DNS Update Response** Refused PC 10.0.0.1 **Owner: PC$**

## Slide 25

##### **Working Towards Overwrites**

● The DHCP server will send a DNS Dynamic Update even if the record exists

- ACLs are meant to stop overwrites

## Slide 26

##### **DNS Record Types**

- “Client Records” - records that were created by Windows hosts directly

- “Managed Records” - records that were created by the DHCP server

Main difference - record ownership

## Slide 27

DNS
Server
Managed Record:
PC1
A: 10.0.0.1
Owner: DHCP$
DHCP
Client Record: PC2
Server
PC2
A: 10.0.0.2
Owner: PC2$
PC1

## Slide 28

# **DDOverwrite** DHCP DNS Overwrite

## Slide 29

##### **Managed Record Overwrite**

DHCP server doesn’t verify the requested FQDN

DHCP server uses its own permissions to update records

DHCP server owns its managed records We can overwrite any managed record!

## Slide 30

##### **Managed Record Overwrite**

2.DNS Update Request
Add PC.aka.test A
10.0.0.11
Authentication: DHCP$
DNS
DHCP Server
Server
PC
10.0.0.1
Owner: DHCP$
PC
10.0.0.11
Owner: DHCP$

## Slide 31

##### **Managed Record Overwrite**

● By default, modern Windows hosts will not have a Managed Record

● The attack could be useful for:

Non-Windows clients

Legacy Windows hosts       Disabled client updates (<Windows 2K)

## Slide 32

##### **Overwriting Client Records**

● Owned by each individual client - DHCP server has no permissions

● But what about the DHCP server own client record?

## Slide 33

##### **DHCP Self-Overwrite**

DHCP server doesn’t verify the requested FQDN

DHCP server owns its own client record

DHCP server uses its own permissions to update records

We can make the DHCP server overwrite its own record!

## Slide 34

##### **DHCP Self-Overwrite**

2.DNS Update Request
Add DHCP.aka.test A
10.0.0.11
Authentication: DHCP$
DNS
DHCP Server
Server
DHCP
10.0.0.101
Owner: DHCP$
DHCP
10.0.0.11
Owner: DHCP$

## Slide 35

##### **DHCP Self-Overwrite**

- Intercept any communication destined for the DHCP server

- Impact depends on other services hosted on the server

## Slide 36

##### **Domain Controller Self-Overwrite**

- Overwrite the DC record if a DHCP server is installed on it

## Slide 37

##### **DC Arbitrary Overwrite**

DCs have write permissions on all the records in the zone **- arbitrary DNS record overwrite!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DC Arbitrary Overwrite
DCs have write permissions on all the
records in the zone - arbitrary DNS record
overwrite!
or ENTER PRISE DOMAIN
RS
Advanced
```

## Slide 38

##### **DC Arbitrary Overwrite**

**2.DNS Update Request** Add AnyServer.aka.test A 10.0.0.11 Authentication: DC$

10.0.0.11
Authentication: DC$
DHCP + DC

DNS
Server
AnyServer
10.0.0.2
Owner: AnyServer$
AnyServer
10.0.0.11
Owner: AnyServer$

## Slide 39

**Attack Demo**

## Slide 40

##### **DNS Spoofing Impact**

Capture  Block Access to
Relay
Sensitive  SIEM/EDR
Authentication
Information Servers

## Slide 41

##### **DC Arbitrary Overwrite**

Domain compromise from an **unauthenticated context**

Works with the **default configuration**

Seen in **57% of the networks** that used Microsoft DHCP

## Slide 42

## **Mitigations for DHCP DNS Attacks**

## Slide 43

##### **Name Protection**

- Prevent overwriting names that were already created by the DHCP server

- Associate each Managed Record with its original creator

- Implemented using DHCID records - DHCP client identifier

## Slide 44

##### **Name Protection**

2.DNS Update Request
Pre-req PC1.aka.test DHCID
BbCcDdEeFf…
Add PC1.aka.test A
10.0.0.10
DHCP  DNS
Server Server
3.DNS Update Response
PC1
Refused A: 10.0.0.1
DHCID: AaBbCcDd..
Owner: DHCP$

## Slide 45

##### **Name Protection Caveats**

- Only meant to protect Managed records - prevent Managed Record Overwrite

● Could be bypassed even in this case by spoofing a DHCP Release

## Slide 46

##### **DNS Credential**

● Specify an alternative credential to be used when sending updates

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DNS Credential
General DNS Filters Failover Advanced
e Specify an alternative credential to
be used when sending updates
DNS dynamic update credentials ? x
Type the credentials that the DHCP server supplies when registering names
using DNS dynamic updates.
User name dhep-sve
Domain
Password
Confirm password
```

## Slide 47

##### **DNS Credential Caveats**

- The credential used has to be weak

● Only meant to protect Client records - prevent DHCP Self-Overwrite & DC Arbitrary Overwrite

## Slide 48

##### **Attacks & Mitigations Summary**

- DHCP DNS Spoofing

   - **Can’t mitigate**

- Managed Record Overwrite

   - **Can’t mitigate**

   - Name Protection could make this harder to perform

   - Use static DNS records instead if possible

- DHCP Self-Overwrite & DC Arbitrary Overwrite

   - Mitigate by configuring a weak user as a DNS credential

   - Especially critical for Domain Controllers

## Slide 49

**Microsoft’s Response**

## Slide 50

## Slide 51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PS C:\Users\Administrator> Invoke-DHCPCheckup -domainName aka.test
PS C:\Users\Administrator> Import-Module .\Desktop\Invoke-DHCPCheckup.ps1
| _\I |/ ___|
| | | |
}l |] —~ Tt |
| | | |
| | | |_
/
|__)
IIdd |} tle
—/I_| I_I\N_
Microsoft DHCP Server Risk Assessment
By Ori David Of Akamai SIG
[*] Found 2 active DHCP servers:
* DC2022.AKA.TEST
* DHCP1.AKA. TEST
Checking DNS Credentials Settings
__/
\__
```

## Slide 52

##### **Black Hat Europe Sound Bytes**

●DHCP DNS Dynamic Updates provide a significant attack surface

●Avoid risky configuration

- Configure a weak user as the DNS credential on all DHCP servers

- Enable DHCP Name Protection

●Disable DHCP DNS Dynamic Updates if they aren’t required

## Slide 53

### **Thank you Questions?**

@oridavid123

© 2022 Akamai | Confidential

**53**
