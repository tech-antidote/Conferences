---
title: "Time for ACKrobatics Abusing TCP Timestamps to Improve Remote Timing Attacks"
speakers: ["Vik Vanderlinden", "Tom Van Goethem", "Mathy Vanhoef"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Vik Vanderlinden&Tom Van Goethem&Mathy Vanhoef_Time for ACKrobatics Abusing TCP Timestamps to Improve Remote Timing Attacks.pdf"
pages: 56
sha256: "f4dbea1b0f5d9c9d925ed679ae8a4a6ee491bf17d0335105151877d4b415927c"
text_chars: 8494
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:16:53Z"
---
# Time for ACKrobatics Abusing TCP Timestamps to Improve Remote Timing Attacks

**Speakers:** Vik Vanderlinden, Tom Van Goethem, Mathy Vanhoef  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Vik Vanderlinden&Tom Van Goethem&Mathy Vanhoef_Time for ACKrobatics Abusing TCP Timestamps to Improve Remote Timing Attacks.pdf` (56 pages)

## Slide 1

Time for A C Krobatics

Leveraging TCP Timestamps to Improve Remote Timing Attacks

## Slide 2

## Slide 3

Lucky 13

## Slide 4

MtE

padding

4

## Slide 5

MtE

padding
jitter
~ 1 µs

5

## Slide 6

6

## Slide 7

7

## Slide 8

8

## Slide 9

##### The ACKrobats

**<u>Vik Vanderlinden</u>** PhD @ KU Leuven

**Tom Van Goethem** SWE @ Google PhD @ KU Leuven

**Mathy Vanhoef** Prof. @ KU Leuven

## Slide 10

Building Blocks

## Slide 11

##### **Timing** Attacks

**1.** Measure execution time

**2.** Infer secret based on time

11

## Slide 12

##### **Remote** Timing Attacks

   **1.** Send request

**2.** Cry because of jitter

**3.** Measure response time

12

## Slide 13

##### **Example** Remote Timing Attacks<sup>[2]</sup>

1

2

13

## Slide 14

##### **Example** Remote Timing Attacks

1

2

Joins private group Infers group membership Reports security vulnerability Leaks contents of report

…

…

14

## Slide 15

##### **Improving** Remote Timing Attacks

Date Header<sup>[5]</sup> (HTTP)

Server-Timing Header<sup>[4]</sup> (HTTP) Timeless Timing Attack<sup>[1]</sup> (TCP)

15

## Slide 16

#### Enter: TCP Timestamps

16

## Slide 17

##### **What** are TCP Timestamps

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What are TCP Timestamps
Client Server
TSval=x, TSecr=0
ia
[ Sit
TSval=y, TSecr=x
a
——
SYN/ACK
TSval=x+8., TSecr=y
nn,
ACK——___
v Vv
17
```

## Slide 18

##### **Why** TCP Timestamps Exist

**Improve RTTM**<sup>[12]</sup> Congestion Control

**LEDBAT**<sup>[14]</sup>

**PAWS**<sup>[12]</sup> High-bandwidth applications (DC)

**Reducing Time-Wait state**<sup>[13]</sup>

18

## Slide 19

##### **Evolution** of TCP Timestamps

2021, 2020 - µs timestamp accuracy proposals<sup>[8, 9]</sup>

2023 - µs timestamps implemented in kernel<sup>[10]</sup>

2023 - µs timestamps can be enabled using ip route option<sup>[10]</sup>

19

## Slide 20

# Attack Detail s

## Slide 21

##### Timing Attacks **Leveraging** TCP Timestamps

Basic Attack

21

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Timing Attacks Leveraging TCP Timestamps
Client Server
3WHS
Basic iat.
Attack 5 i
ee
FIN/RST
21
```

## Slide 22

##### Timing Attacks **Leveraging** TCP Timestamps

Runtime Multiplication Enhancement

22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Timing Attacks Leveraging TCP Timestamps
Client Server
Runtime <——_
Multiplication
Enhancement ./
FIN/RST
22
```

## Slide 23

##### Attack **Preconditions**

**>880k**

Servers tested

23

## Slide 24

##### Attack **Preconditions**

## **>88%**

TCP Timestamps enabled

24

## Slide 25

##### Attack **Preconditions**

## **>99%**

Immediate ACKnowledgement

25

## Slide 26

##### Attack **Preconditions**

## **>95%**

Persistent connections

26

## Slide 27

### **HTTP** Specif i cs

27

## Slide 28

##### Attack **Preconditions**

Support for non-concurrency (e.g. HTTP/1.1)

28

## Slide 29

Coalescing **Practicalities** or: how to get all those requests to the server?

29

## Slide 30

Coalescing **Practicalities** or: how to get all those requests to the server?

TCP segment

30

## Slide 31

31

## Slide 32

Coalescing **Practicalities** or: how to get all those requests to the server?

TCP segment size (1,5KB; MSS)

32

## Slide 33

Coalescing **Practicalities** or: how to get all those requests to the server?

###### TLS frame size (16KB)

33

## Slide 34

Coalescing **Practicalities** or: how to get all those requests to the server?

Out-of-order TCP segments (6 MiB default @ AWS ubuntu)

34

## Slide 35

##### **Distributed** Attack

35

## Slide 36

##### Attack **Performance**

ms timestamps

25 µs → 5 µs 25 µs: >10k requests → 200 requests

µs timestamps

25 µs → 750 ns

36

## Slide 37

Case Studies

## Slide 38

38

## Slide 39

39

## Slide 40

##### Case Studies: **Lucky 13**

MtE

padding
jitter
~ 1 µs

40

## Slide 41

##### Case Studies: **Lucky 13**

**transatlantic**

Client: **UK** Server: **USA** Timestamps: **µs** Target: **Embedded Linux Library CVE-2025-32998** assigned

41

## Slide 42

##### Case Studies: **Lucky 13**

Distinguish 0x00 and 0x01 byte **150ns** with 50k requests

Responsibly disclosed

**no response** received

42

## Slide 43

##### Case Studies: **OpenSSH**

User enumeration OpenSSHd pre 7.3

decryption<sup>[19]</sup>

bcrypt

sha512

43

## Slide 44

##### Case Studies: **OpenSSH**

###### Multiple Clients Timestamps: **ms Distributed** evaluation

44

## Slide 45

##### Case Studies: **OpenSSH**

Artificial load: **>900 req/s** Results: **Unchanged**

45

## Slide 46

Defense
s

## Slide 47

##### Defenses

Send TCP Timestamps **less often** (e.g. [11]) Only hinders the attack slightly

47

## Slide 48

##### Defenses

**Disable** TCP Timestamps RTTM and PAWS stop working

48

## Slide 49

##### Defenses

**Obfuscate** TCP Timestamps Requires kernel support & Potential middlebox impact

49

## Slide 50

##### Defenses

###### Limited overhead: 20 entries → 95% of connections

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Defenses
r
ro)
B fo.) fo)
Proportion of TCP connections
fo}
N
10° 10? 10? 10
Estimated max unACKed packets in TCP connection
Limited overhead: 20 entries » 95% of connections
50
```

## Slide 51

Conclusion

## Slide 52

##### Takeaway

Timing Attacks are getting more performant This attack can be performed fully distributed Be careful when exposing time(-related) info

52

## Slide 53

High time to check your servers: use our scripts

53

## Slide 54

Time for A C Krobatics

Leveraging TCP Timestamps to Improve Remote Timing Attacks

## Slide 55

##### Refs

[1] T. Van Goethem, C. Popper, W. Joosen, and M. Vanhoef, “Timeless ¨ timing attacks: Exploiting concurrency to leak secrets over remote connections,” in 29th USENIX Security Symposium (USENIX Security 20), 2020, pp. 1985–2002.

[2] A. Bortz and D. Boneh, “Exposing private information by timing web applications,” in Proceedings of the 16th international conference on World Wide Web, 2007, pp. 621–628.

[3] B. B. Brumley and N. Tuveri, “Remote timing attacks are still practical,” in European Symposium on Research in Computer Security. Springer, 2011, pp. 355–371.

[4] V. Vanderlinden, W. Joosen, and M. Vanhoef, “Can you tell me the time? security implications of the server-timing header,” in Proceedings 2023 Workshop on Measurements, Attacks, and Defenses for the Web. No. March, Internet Society, 2023

[5] V. Vanderlinden, T. Van Goethem, and M. Vanhoef, “Time will tell: Exploiting timing leaks using http response headers,” in Computer Security – ESORICS 2023, G. Tsudik, M. Conti, K. Liang, and G. Smaragdakis, Eds. Cham: Springer Nature Switzerland, 2024, pp. 3–22.

[7] nginx contributors, “nginx module ngx http core module directives,” accessed: 06 sept 2024. [Online]. Available: https://nginx.org/en/ docs/http/ngx http core module.html#keepalive requests

[8] W. Wang, N. Cardwell, Y. Cheng, and E. Dumazet, “TCP Low Latency Option,” Internet Engineering Task Force, Internet-Draft draft-wang-tcpm-low-latency-opt-00, Jun. 2017, work in Progress. [Online]. Available: https://datatracker.ietf.org/doc/ draft-wang-tcpm-low-latency-opt/00/

[9] K. Y. Yang, N. Cardwell, Y. Cheng, and E. Dumazet, “TCP ETS: Extensible Timestamp Options,” Internet Engineering Task Force, Internet-Draft draft-yang-tcpm-ets-00, Nov. 2020, work in Progress. [Online]. Available: https://datatracker.ietf.org/doc/ draft-yang-tcpm-ets/00/

[10] <u>https://github.com/torvalds/linux/commit/93be6ce0e91b6</u> - <u>https://github.com/torvalds/linux/commit/614e8316aa4ca</u> -

<u>https://github.com/iproute2/iproute2/commit/a043bea750026</u>

55

## Slide 56

##### Refs 2

[11] Y. Nishida, “Disabling PAWS When Other Protections Are Available,” Internet Engineering Task Force, Internet-Draft draft-nishida-tcpmdisabling-paws-00, Jun. 2018, work in Progress. [Online]. Available: https://datatracker.ietf.org/doc/draft-nishida-tcpm-disabling-paws/00/

[12] D. Borman, R. T. Braden, V. Jacobson, and R. Scheffenegger, “TCP Extensions for High Performance,” RFC 7323, Sep. 2014. [Online]. Available: https://www.rfc-editor.org/info/rfc7323

- [13] F. Gont, “Reducing the TIME-WAIT State Using TCP Timestamps,” RFC 6191, Apr. 2011. [Online]. Available: https://www.rfc-editor. org/info/rfc6191

- [14] S. Shalunov, G. Hazel, J. Iyengar, and M. Kuhlewind, “Low Extra ¨ Delay Background Transport (LEDBAT),” RFC 6817, Dec. 2012. [Online]. Available: https://www.rfc-editor.org/info/rfc6817

- [15] B. McDanel, “TCP Timestamping and Remotely gathering uptime information,” Mar. 2001, accessed: 06 sept 2024. [Online]. Available: https://seclists.org/bugtraq/2001/Mar/182

[16] E. Bursztein, “TCP Timestamp to count hosts behind NAT,” Jan. 2005, accessed: 06 sept 2024. [Online]. Available: http://phrack.org/issues/63/3.html#:∼:text=[%20TCP% 20Timestamp%20To%20count%20Hosts%20behind%20NAT%20]

- [17] G. Wicherski, F. Weingarten, and U. Meyer, “Ip agnostic real-time traffic filtering and host identification using tcp timestamps,” in 38th Annual IEEE Conference on Local Computer Networks, Oct 2013, pp. 647–654

- [18] J. Giffin, R. Greenstadt, P. Litwack, and R. Tibbetts, “Covert messaging through tcp timestamps,” in Privacy Enhancing Technologies, R. Dingledine and P. Syverson, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2003, pp. 194–208.

- [19] <u>https://github.com/openssh/openssh-portable/commit/9286875a73b2de7736b5e50692739d314cd8d9dc</u>

Icons used on slides: FontAwesome, <u>https://fontawesome.com/</u>

56
