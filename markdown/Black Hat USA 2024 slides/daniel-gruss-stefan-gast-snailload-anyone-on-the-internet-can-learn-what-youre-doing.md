---
title: "SnailLoad Anyone on the Internet Can Learn What You're Doing"
speakers: ["Daniel Gruss", "Stefan Gast"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Daniel Gruss & Stefan Gast_SnailLoad Anyone on the Internet Can Learn What You're Doing.pdf"
pages: 82
sha256: "df3660c157b2d845803a91bde6bdeb057c4c1b4fa0e9383d1999490fccaa107e"
text_chars: 16873
ocr_pages: 0
has_ocr: false
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T21:30:04Z"
---
# SnailLoad Anyone on the Internet Can Learn What You're Doing

**Speakers:** Daniel Gruss, Stefan Gast  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Daniel Gruss & Stefan Gast_SnailLoad Anyone on the Internet Can Learn What You're Doing.pdf` (82 pages)


## Slide 1

# SnailLoad

Anyone on the Internet Can Learn What You’re Doing

**Stefan Gast, Daniel Gruss**

2024-08-07

Graz University of Technology

1

Stefan Gast, Daniel Gruss

## Slide 2

## **Who are we?**

### **Stefan Gast**

PhD Student Graz University of Technology

- @notbobbytables@infosec.exchange

- @notbobbytables

- https://stefangast.eu/

2

Stefan Gast, Daniel Gruss

## Slide 3

## **Who are we?**

### **Stefan Gast**

PhD Student Graz University of Technology

- @notbobbytables@infosec.exchange

- @notbobbytables

- https://stefangast.eu/

### **Daniel Gruss**

### Professor

Graz University of Technology

- @lavados@infosec.exchange

- @lavados

- https://gruss.cc/

2

Stefan Gast, Daniel Gruss

## Slide 4

## **SnailLoad**

### We can tell which website you visit, without running anything on your system:

≥ 50
10
20 40
30
40 30
50
60 20
70
80 10
90
100 0
10 20 30 40 50 60 70 80 90 100
Website

Prediction

3

Stefan Gast, Daniel Gruss

## Slide 5

**What are Side Channels?**

Stefan Gast, Daniel Gruss

4

## Slide 6

**What are Side Channels?**

Obtain meta-data and derive data from it

Stefan Gast, Daniel Gruss

4

## Slide 7

**Side Channel Example**

Stefan Gast, Daniel Gruss

5

## Slide 8

**Timing Side Channels**

6

Stefan Gast, Daniel Gruss

## Slide 9

**Local Timing Attack**

10 7
10 4
10 1
ofNumberaccesses

Stefan Gast, Daniel Gruss

7

## Slide 10

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

Stefan Gast, Daniel Gruss

7

## Slide 11

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

Stefan Gast, Daniel Gruss

7

## Slide 12

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

• Local → code execution

Stefan Gast, Daniel Gruss

7

## Slide 13

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

- Local _→_ code execution

- • code to use secrets

Stefan Gast, Daniel Gruss

7

## Slide 14

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

- Local _→_ code execution

- • code to use secrets • code to measure time

Stefan Gast, Daniel Gruss

7

## Slide 15

## **Local Timing Attack**

Cache Hits Cache Misses

10 7
10 4
10 1
100 200 300 400
Access time [CPU cycles]
ofNumberaccesses

- Local _→_ code execution

- code to use secrets

- code to measure time

- code to exfiltrate data

Stefan Gast, Daniel Gruss

7

## Slide 16

## **Remote Timing**

Remote in “remote adversary” can mean different things

8

Stefan Gast, Daniel Gruss

## Slide 17

## **Remote Timing**

Remote in “remote adversary” can mean different things

- attack from a different chip?

8

Stefan Gast, Daniel Gruss

## Slide 18

## **Remote Timing**

Remote in “remote adversary” can mean different things

- attack from a different chip?

- JavaScript?

8

Stefan Gast, Daniel Gruss

## Slide 19

## **Remote Timing**

Remote in “remote adversary” can mean different things

- attack from a different chip?

- JavaScript?

- network-exposed API?

8

Stefan Gast, Daniel Gruss

## Slide 20

## **Remote Timing**

Remote in “remote adversary” can mean different things

- attack from a different chip?

- JavaScript?

- network-exposed API?

- local WiFi?

8

Stefan Gast, Daniel Gruss

## Slide 21

## **State of the Art**

- local code execution _→_ fingerprint videos

9

Stefan Gast, Daniel Gruss

## Slide 22

## **State of the Art**

- local code execution _→_ fingerprint videos

- • control local gateway _→_ precisely monitor network traffic

9

Stefan Gast, Daniel Gruss

## Slide 23

## **State of the Art**

- local code execution _→_ fingerprint videos

- control local gateway _→_ precisely monitor network traffic

- Tor gateway _→_ estimate network traffic

9

Stefan Gast, Daniel Gruss

## Slide 24

## **State of the Art**

- local code execution _→_ fingerprint videos

- control local gateway _→_ precisely monitor network traffic

- Tor gateway _→_ estimate network traffic

- _→_ application fingerprinting

9

Stefan Gast, Daniel Gruss

## Slide 25

## **State of the Art**

- local code execution _→_ fingerprint videos

- control local gateway _→_ precisely monitor network traffic

- Tor gateway _→_ estimate network traffic

- _→_ application fingerprinting

- _→_ website fingerprinting

9

Stefan Gast, Daniel Gruss

## Slide 26

## **State of the Art**

- local code execution _→_ fingerprint videos

- control local gateway _→_ precisely monitor network traffic

- Tor gateway _→_ estimate network traffic

- _→_ application fingerprinting

- _→_ website fingerprinting

- _→_ video fingerprinting

9

Stefan Gast, Daniel Gruss

## Slide 27

**Internet Access Technologies**

- DSL, Fiber, LTE, 5G: different throughput

10

Stefan Gast, Daniel Gruss

## Slide 28

**Internet Access Technologies**

- DSL, Fiber, LTE, 5G: different throughput

- backbone connection **has orders of magnitude higher throughput**

10

Stefan Gast, Daniel Gruss

## Slide 29

## **Internet Access Technologies**

- DSL, Fiber, LTE, 5G: different throughput

- backbone connection **has orders of magnitude higher throughput**

- _→_ buffering before last mile is necessary!

10

Stefan Gast, Daniel Gruss

## Slide 30

## Slide 31

## Slide 32

## Slide 33

**Packet Buffering**

...
Figure 1: Connection idle Figure 2: Connection busy Figure 3:

11

Stefan Gast, Daniel Gruss

## Slide 34

## **Packet Buffering**

...
Figure 2: Connection busy Figure 3:

#### **Figure 1:** Connection idle

11

Stefan Gast, Daniel Gruss

## Slide 35

**Packet Buffering**

...
Figure 3:

Figure 1: Connection idle

**Figure 2:** Connection busy

11

Stefan Gast, Daniel Gruss

## Slide 36

**Packet Buffering**

...
Figure 1: Connection idle Figure 2: Connection busy Figure 3: Bufferbloat

11

Stefan Gast, Daniel Gruss

## Slide 37

## **Network Activity Causes Latency Spikes**

Figure

60
amazon.com
40
google.com
20
0 s 5 s 10 s 15 s 20 s
Figure 4: Same machine pinging 8.8.8.8
[ms]RTT

12

Stefan Gast, Daniel Gruss

## Slide 38

## **Network Activity Causes Latency Spikes**

60
amazon.com
40
google.com
20
0 s 5 s 10 s 15 s 20 s
Figure 4: Same machine pinging 8.8.8.8
60
amazon.com
40
google.com
20
0 s 5 s 10 s 15 s 20 s
Figure 5: Different machine sharing the same internet connection pinging 8.8.8.8
[ms]RTT
[ms]RTT

12

Stefan Gast, Daniel Gruss

## Slide 39

**Idle and Busy Round-Trip-Times**

with download
2,000 2,000
0 0
0 200 400 600 0 200
Figure 6: RTT [ms], ADSL-1, 50 Mbit / s Figure 7: RTT [ms],
4,000 idle 4,000
with download
2,000 2,000
0 0
20 30 40 50 20 30
Figure 8: RTT [ms], FTTH-1, 80 Mbit / s Figure 9: RTT [ms],
Cases# Cases#
Cases# Cases#

13

Stefan Gast, Daniel Gruss

## Slide 40

## **Idle and Busy Round-Trip-Times**

2,000
0
0 200
Figure 7: RTT [ms],
4,000 idle 4,000
with download
2,000 2,000
0 0
20 30 40 50 20 30
Figure 8: RTT [ms], FTTH-1, 80 Mbit / s Figure 9: RTT [ms],
Cases#
Cases# Cases#

4,000 idle
with download
2,000
0
0 200 400 600
Figure 6: RTT [ms], ADSL-1, 50 Mbit / s
Cases#

13

Stefan Gast, Daniel Gruss

## Slide 41

## **Idle and Busy Round-Trip-Times**

with download
2,000 2,000
0 0
20 30 40 50 20 30
Figure 8: RTT [ms], FTTH-1, 80 Mbit / s Figure 9: RTT [ms],
Cases# Cases#

4,000 idle 4,000 idle
with download with download
2,000 2,000
0 0
0 200 400 600 0 200 400 600
Figure 6: RTT [ms], ADSL-1, 50 Mbit / s Figure 7: RTT [ms], LTE, 75 Mbit / s
Cases# Cases#

13

Stefan Gast, Daniel Gruss

## Slide 42

## **Idle and Busy Round-Trip-Times**

2,000
0
20 30
Figure 9: RTT [ms],
Cases#

4,000 idle 4,000 idle
with download with download
2,000 2,000
0 0
0 200 400 600 0 200 400 600
Figure 6: RTT [ms], ADSL-1, 50 Mbit / s Figure 7: RTT [ms], LTE, 75 Mbit / s
4,000 idle
with download
2,000
0
20 30 40 50
Cases# Cases#
Cases#

Figure 8: RTT [ms], FTTH-1, 80 Mbit / s

13

Stefan Gast, Daniel Gruss

## Slide 43

## **Idle and Busy Round-Trip-Times**

4,000 idle 4,000 idle
with download with download
2,000 2,000
0 0
0 200 400 600 0 200 400 600
Figure 6: RTT [ms], ADSL-1, 50 Mbit / s Figure 7: RTT [ms], LTE, 75 Mbit / s
4,000 idle 4,000 idle
with download with download
2,000 2,000
0 0
20 30 40 50 20 30 40 50
Cases# Cases#
Cases# Cases#

Figure 8: RTT [ms], FTTH-1, 80 Mbit / s

Figure 9: RTT [ms], Cable, 80 Mbit / s

13

Stefan Gast, Daniel Gruss

## Slide 44

## **Attack Setups**

YouTube
ISP Victim’s Victim’s
Endpoint Gateway Computer
fast

14

Stefan Gast, Daniel Gruss

## Slide 45

## **Attack Setups**

Bottleneck
YouTube
slow!
ISP Victim’s Victim’s
Endpoint Gateway Computer
fast

14

Stefan Gast, Daniel Gruss

## Slide 46

## **Attack Setups**

Bottleneck
YouTube
slow!
ISP Victim’s Victim’s
Attacker’s Endpoint Gateway Computer
HTTP Server
fast
fast

14

Stefan Gast, Daniel Gruss

## Slide 47

## **Attack Setups**

Bottleneck
YouTube
slow!
ISP Victim’s Victim’s
Attacker’s Endpoint Gateway Computer
HTTP Server
fast
fast

- Various scenarios: Compromised websites, malicious ads, emails, and more

14

Stefan Gast, Daniel Gruss

## Slide 48

## **Attack Setups**

Bottleneck
YouTube
slow!
ISP Victim’s Victim’s
Attacker’s Endpoint Gateway Computer
HTTP Server
fast
fast

- Various scenarios: Compromised websites, malicious ads, emails, and more

- Different ways attackers can exploit network traffic to perform attacks

14

Stefan Gast, Daniel Gruss

## Slide 49

## Slide 50

**Polling the Server’s Send Buffer To Measure RTTs**

**begin** acked _←_ **false** ; start _←_ get ~~c~~ urrent ~~t~~ ime(); send( _sock, b, 1, 0_ ); **repeat if** ioctl( _sock,_ **SIOCOUTQ** ) = 0 **then** acked _←_ **true** ; **end until** acked; end _←_ get ~~c~~ urrent ~~t~~ ime(); **return** end _−_ start; **end**

15

Stefan Gast, Daniel Gruss

## Slide 51

**Polling the Server’s Send Buffer To Measure RTTs**

**begin** acked _←_ **false** ; start _←_ get ~~c~~ urrent ~~t~~ ime(); send( _sock, b, 1, 0_ ); **repeat if** ioctl( _sock,_ **SIOCOUTQ** ) = 0 **then** acked _←_ **true** ; **end until** acked; end _←_ get ~~c~~ urrent ~~t~~ ime(); **return** end _−_ start; **end**

15

Stefan Gast, Daniel Gruss

## Slide 52

**Polling the Server’s Send Buffer To Measure RTTs**

**begin** acked _←_ **false** ; start _←_ get ~~c~~ urrent ~~t~~ ime(); send( _sock, b, 1, 0_ ); **repeat if** ioctl( _sock,_ **SIOCOUTQ** ) = 0 **then** acked _←_ **true** ; **end until** acked; end _←_ get ~~c~~ urrent ~~t~~ ime(); **return** end _−_ start; **end**

15

Stefan Gast, Daniel Gruss

## Slide 53

**Polling the Server’s Send Buffer To Measure RTTs**

**begin** acked _←_ **false** ; start _←_ get ~~c~~ urrent ~~t~~ ime(); send( _sock, b, 1, 0_ ); **repeat if** ioctl( _sock,_ **SIOCOUTQ** ) = 0 **then** acked _←_ **true** ; **end until** acked; end _←_ get ~~c~~ urrent ~~t~~ ime(); **return** end _−_ start; **end**

15

Stefan Gast, Daniel Gruss

## Slide 54

**Polling the Server’s Send Buffer To Measure RTTs**

**begin** acked _←_ **false** ; start _←_ get ~~c~~ urrent ~~t~~ ime(); send( _sock, b, 1, 0_ ); **repeat if** ioctl( _sock,_ **SIOCOUTQ** ) = 0 **then** acked _←_ **true** ; **end until** acked; end _←_ get ~~c~~ urrent ~~t~~ ime(); **return** end _−_ start; **end**

15

Stefan Gast, Daniel Gruss

## Slide 55

## Slide 56

**Fingerprinting with Machine Learning**

16

Stefan Gast, Daniel Gruss

## Slide 57

**Fingerprinting with Machine Learning**

16

Stefan Gast, Daniel Gruss

## Slide 58

**Fingerprinting with Machine Learning**

- use machine learning to analyze network traffic and infer user actions

16

Stefan Gast, Daniel Gruss

## Slide 59

**Fingerprinting with Machine Learning**

- use machine learning to analyze network traffic and infer user actions

- pre-process traces with an STFT

16

Stefan Gast, Daniel Gruss

## Slide 60

**Fingerprinting with Machine Learning**

- use machine learning to analyze network traffic and infer user actions

- pre-process traces with an STFT

- KERAS (Tensorflow)

16

Stefan Gast, Daniel Gruss

## Slide 61

## **Fingerprinting with Machine Learning**

- use machine learning to analyze network traffic and infer user actions

- pre-process traces with an STFT

- KERAS (Tensorflow)

- closed-world vs. open-world

16

Stefan Gast, Daniel Gruss

## Slide 62

## **Fingerprinting with Machine Learning**

#### **Table 1:** CNN Parameters

- use machine learning to analyze network traffic and infer user actions

- pre-process traces with an STFT

- KERAS (Tensorflow)

- closed-world vs. open-world

Type Parameters Activation
Conv2D filters=32, ker- ReLU
nel size=[5,5],
strides=[1,1]
MaxPooling2D pool size=[2,2], -
strides=[2,2]
Conv2D filters=64, ker- ReLU
nel size=[3,3],
strides=[1,1]
MaxPooling2D pool size=[2,2], -
strides=[2,2]
Conv2D filters=128, ker- ReLU
nel size=[3,3],
strides=[1,1]
MaxPooling2D pool size=[2,2], -
strides=[2,2]
Flatten - -
Dense output size=1024 ReLU
Dense output size=512 ReLU
Dense output size=10 Softmax

16

Stefan Gast, Daniel Gruss

## Slide 63

**Video Fingerprinting**

30 30
0 20 40 60 0 20
34 34
32 32
30 30
0 20 40 60 0 20
Figure 10: Video A, Time in seconds on x Figure 11: Video B,
axis axis
[ms]RTT [ms]RTT

17

Stefan Gast, Daniel Gruss

## Slide 64

## **Video Fingerprinting**

30
0 20
34
32
30
0 20
Figure 11: Video B,
axis
[ms]RTT

34
32
30
0 20 40 60
34
32
30
0 20 40 60
[ms]RTT
[ms]RTT

**Figure 10:** Video A, Time in seconds on x axis

17

Stefan Gast, Daniel Gruss

## Slide 65

## **Video Fingerprinting**

34
32
30
0 20 40 60
34
32
30
0 20 40 60
Figure 10: Video A, Time in seconds on x
axis
[ms]RTT
[ms]RTT

34
32
30
0 20 40 60
34
32
30
0 20 40 60
[ms]RTT
[ms]RTT

**Figure 11:** Video B, Time in seconds on x axis

17

Stefan Gast, Daniel Gruss

## Slide 66

## **How large does the website have to be?**

128 KiB 0 0 0 0 0 0 0 0 0 0
256 KiB 0 0 0 0 0 2 0 0 0 0
512 KiB 8 7 6 8 7 9 8 8 6 2
1 MiB 10 7 8 8 7 9 8 8 7 8
2 MiB 10 10 9 10 10 10 10 10 9 10
4 MiB 10 10 9 10 10 9 9 9 10 8
8 MiB 10 10 9 9 9 10 10 10 9 10
Sample Rate (µs)
100 200 400 800160032006400128002560051200
Download Size

18

Stefan Gast, Daniel Gruss

## Slide 67

## **Video Fingerprinting on 10 different connections**

10 10 10 10 10
5 5 5 5 5
0 0 0 0 0
Prediction Prediction Prediction Prediction Prediction
10 10 10 10 10
5 5 5 5 5
0 0 0 0 0
Prediction Prediction Prediction Prediction Prediction
Video Video Video Video Video
Video Video Video Video Video

19

Stefan Gast, Daniel Gruss

## Slide 68

## **Top-100 Open-World Website Fingerprinting**

≥ 50
10
20 40
30
40 30
50
60 20
70
80 10
90
100 0
10 20 30 40 50 60 70 80 90 100
Prediction
Website

20

Stefan Gast, Daniel Gruss

## Slide 69

**Cross-Connection Website Fingerprinting**

10
5
0
Prediction
Website

21

Stefan Gast, Daniel Gruss

## Slide 70

**Live Demo**

## Slide 71

## **Video Call Detection**

60
Person A: 75 Mbit/s LTE
Person B: 200 Mbit/s LTE+
50 Video Start / Stop
40
0 50 100 150 200
Time [s]
RTT [ms]

22

Stefan Gast, Daniel Gruss

## Slide 72

## **Impact of Noise on Website Fingerprinting**

10 10 10
5 5 5
0 0 0
Prediction Prediction Prediction
Website Website Website

23

Stefan Gast, Daniel Gruss

## Slide 73

**Context, Impact, Disclosure**

- SnailLoad is a generic problem of heterogenous networks (with different throughputs)

24

Stefan Gast, Daniel Gruss

## Slide 74

**Context, Impact, Disclosure**

- SnailLoad is a generic problem of heterogenous networks (with different throughputs)

- Many “remote” attacks can now be transformed to truly remote attacks

24

Stefan Gast, Daniel Gruss

## Slide 75

## **Context, Impact, Disclosure**

- SnailLoad is a generic problem of heterogenous networks (with different throughputs)

- Many “remote” attacks can now be transformed to truly remote attacks

- We disclosed to Google / YouTube

24

Stefan Gast, Daniel Gruss

## Slide 76

## **Context, Impact, Disclosure**

- SnailLoad is a generic problem of heterogenous networks (with different throughputs)

- Many “remote” attacks can now be transformed to truly remote attacks

- We disclosed to Google / YouTube

   - they investigated the issue for several weeks

24

Stefan Gast, Daniel Gruss

## Slide 77

## **Context, Impact, Disclosure**

- SnailLoad is a generic problem of heterogenous networks (with different throughputs)

- Many “remote” attacks can now be transformed to truly remote attacks

- We disclosed to Google / YouTube

   - they investigated the issue for several weeks

   - concluded that it is a generic problem

24

Stefan Gast, Daniel Gruss

## Slide 78

**Take Aways (Black Hat Sound Bytes)**

- Any connection to a remote server can obtain high-resolution traces of your activity

25

Stefan Gast, Daniel Gruss

## Slide 79

**Take Aways (Black Hat Sound Bytes)**

- Any connection to a remote server can obtain high-resolution traces of your activity

- Traces can leak websites and videos watched

25

Stefan Gast, Daniel Gruss

## Slide 80

**Take Aways (Black Hat Sound Bytes)**

- Any connection to a remote server can obtain high-resolution traces of your activity

- Traces can leak websites and videos watched

- Throughput difference is the root cause _→_ not trivial to fix

25

Stefan Gast, Daniel Gruss

## Slide 81

## **Acknowledgments**

This research was made possible by generous funding from:

Supported in part by the European Research Council (ERC project FSSec 101076409) and the Austrian Science Fund (FWF SFB project SPyCoDe 10.55776/F85 and FWF project NeRAM I6054). Additional funding was provided by generous gifts from Red Hat, Google, and Intel. Any opinions, findings, and conclusions or recommendations expressed in this paper are those of the authors and do not necessarily reflect the views of the funding parties.

26

Stefan Gast, Daniel Gruss

## Slide 82

# SnailLoad

Anyone on the Internet Can Learn What You’re Doing

**Stefan Gast, Daniel Gruss** 2024-08-07 Graz University of Technology

27

Stefan Gast, Daniel Gruss
