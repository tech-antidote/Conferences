---
title: "A Run a Day Wont Keep the Hacker Away"
speakers: ["Dhondt"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Dhondt-A-Run-a-Day-Wont-Keep-the-Hacker-Away.pdf"
pages: 33
sha256: "b977350cb67e85fd814b02f7266202779e3105f65bd6eca4462758424af38cc9"
text_chars: 10379
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.4
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:48:23Z"
---
# A Run a Day Wont Keep the Hacker Away

**Speakers:** Dhondt  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Dhondt-A-Run-a-Day-Wont-Keep-the-Hacker-Away.pdf` (33 pages)


## Slide 1

_A run a day won't keep the hacker away_ : Inference Attacks on Endpoint Privacy Zones in Fitness Tracking Social Networks

**Karel Dhondt, Victor Le Pochat** , Alexios Voulimeneas, Wouter Joosen, Stijn Volckaert

## Slide 2

2

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Running is enjoying a boom REUTERS
pandemic Exclusive: Brits on bikes as fitness app data
shows pandemic boom
Updated 0953 GMT psa) IKT) April 25, 2020 vases oe ‘ °
Bloomberg ECONOM Ic
The Pandemic Bike Boom —
Hits in Some Unexpected Fitness apps grew by nearly
American Cities 50% during the first half of
2020, study finds
Los Angeles and Houston are hardly cycling capitals.
But both saw surges in biking after Covid-19 began,
according to new data from the fitness app Strava.
Carmen Ang
By Laura Bliss
September 23, 2020, 3:00 PM GMT+2
```

## Slide 3

3

> Text below was recovered by OCR (confidence 96/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Fitness app Strava lights up staff at
military bases
© 29 Januar y 2018
Garmin is slowly coming back online after a massive
ransomware hack
By Oliver Effron, CNN Business
Updated 1937 GMT (0337 HKT) July 27, 2020
The Washington Post
Democracy Dies in Darkness
Fitness app Polar revealed not
only where U.S. military
personnel worked, but where
they lived
By Rebecca Tan
July 18, 2018 at 10:00 a.m. UTC
Strava removes automatic
flybys after safety concerns
The ride-tracking app has now made the comparison
feature opt-in
BY ALEX BALLINGER OCTOBER 15, 2020
```

## Slide 4

# Fitness Tracking Social Networks: Activities

4

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Fitness Tracking Social Networks: Activities
Strava User — Ride Givekudos (70 [Elo 4
Thursday, May 20, 2021 - Ghent, Flanders .
— 1.87km 5:55 Om
Evenin Ride Distance Moving Time Elevation
Avg Max
Speed 19.0km/h 20.9km/h
Elapsed Time 5:55
ay 8
& SLUIZEKEN
rstraat
BRUGHUIZEKEN Groenevalleipark
Riserva park © Mapbox © OpenStreetMap Improve this map
5:05
Dist: 1.6 km
Grade: 0.1%
4 Om
: 0.4km 0.6 km 0.8 km 1.0 km 1.2km 1.4km 1.6 km
```

## Slide 5

# Endpoint Privacy Zones

##### View of owner of activity

##### View of user that doesn’t own activity

> [1] Hassan et al. Analysis of Privacy Protections in Fitness Tracking Social Networks -or- You can run, but can you hide? In USENIX (2018)

> [2] GRUTESER et al. Anonymous usage of location-based services through spatial and temporal cloaking. In Proceedings of the 1st international conference on Mobile systems, applications and services (2003)

5

## Slide 6

# Attack

### › Threat model

   - → capabilities of _regular_ user

   - → only based on _public_ (meta)data

- › Two subproblems:

   1. Discovering EPZs

   2. Finding protected location inside EPZ

6

## Slide 7

## Attack: Discovering EPZs

#### Adaptation of K-Means

**repeat**

assign each endpoint to closest fitted circle of cluster lsq fit new circle for cluster

**until** convergence criterium is met

7

## Slide 8

# Attack: Protected Location Inside EPZ

› Two scenarios:

1. **Inner** Distance

2. **Total** Distance

8

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Attack: Protected Location Inside EPZ
» Two scenarios:
1. Inner Distance
2. Total Distance
Activity metadata Total activity distance
total_distance: 1.86, | 1.66 km 1.86 km ,
visible_distances: o> | |
is: =" Cloaked distances Visible distance
Available distances: Inner distance scenario: 0.16 km + 1.50 km + 0.20 km = 1.86 km
~~“ Total distance scenario: 0.36 km + 1.50 km = 1.86 km
```

## Slide 9

# Inner Distance Scenario

**Inner distance scenario** Distance covered inside EPZ leaked

9

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Inner Distance Scenario
Strava User - Ride
Give Kudos
Thursday, Me 20/202 Ghent, Flanders 1.87 km 5:55 Om
Evening Ride Distance Moving Time Elevation
Speed 19.0km/h 20.9km/h
Elapsed Time 5:55
ROOIGEM
+]
wv {latlng: Array(31), grade_smooth: Array(31), distance: Array(31), altitude: Array(31), time: Array(31)}
>altitude: (31) [8.7, 8.7, 8.7, 8.7, 8.4, 8.1, 8.1, 8.1, 7.7, 7.5, 8, 8.2, 8.3, 8.5, 9, 9.2, 9, 9, 8.6, 8.6, 9, 9.1, 9.2, 9.3, 9.1, 9.2, 9.2, 9.3, 9.3, 9.3, 9.4]
>distance: (31) [211.8, 294.2, 296.5, 302.6, 318.4, 337.6, 425.7, 440.5, 496.2, 551.9, 607.3, 645.8, 699.2, 737.4, 780.4, 797.7, 844.3, 851.1, 901.8, 982.4, 1063
> lating: (31) [Array(2), (2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(J
>time: (31) [41, 56, 57, 58, 64, 81, 84, 94, 105, 115, 123, 133, 140, 148, 151, 160, 162, 171, 186, 202, 208, 226, 244, 263, 272, 280, 292, 305, 307, 309]
Ovievaarstraat
prongensest© ST. JACOBS
BRUGHUIZEKEN Groe
Dist: 1.6 km
Elev: 9m
Grade: 0.1%
a Inner distance scenario
Segments
oe Distance covered inside EPZ leaked
0.42km
```

## Slide 10

# Total Distance Scenario

› distance covered inside EPZ = total distance – track distance

10

## Slide 11

# Attack

› Two scenarios:

**Total Inner Distance Distance** 1. **Inner** Distance **Attack Attack** 2. **Total** Distance **Strava** ✔ ✔ **Garmin Connect** ✔ **Komoot** ✔ **Map My tracks** ✔ ✔ **Map My Run** ✔ **Ride With GPS** ✔ ✔

11

## Slide 12

# Attack: Finding Protected Locations Inside EPZ Intuition of attack

12

## Slide 13

# Attack: Finding Protected Locations Inside EPZ Intuition of attack

13

## Slide 14

# Attack: Finding Protected Locations Inside EPZ Preprocessing

Downloaded road graph

Node resolution increased through chaining

14

## Slide 15

# Attack: Finding Protected Locations Inside EPZ Identifying Entry Gates

15

## Slide 16

# Attack: Finding Protected Locations Inside EPZ Filtering outliers

######

|**activity_id **|**entry_gate **|**type**|**inner_distance**|
|---|---|---|---|
|1|EG0|START|184.8|
|1|EG1|END|293.2|
|2|EG2|START|236.4|
|~~2~~|~~EG0~~|~~END~~|~~199.1~~|
|~~3~~|~~EG0~~|~~START~~|~~152.3~~|
|3|EG1|END|289.7|
|...|…|…|…|
|N|EG0|START|186.9|

16

## Slide 17

# Attack: Finding Protected Locations Inside EPZ Predicting Location

› For each node of interpolated road graph:

**LAD fit** of _N_ observed distances and _M_ theoretical distances

|**activity_id**|**entry_gate**|**type**|**EPZ_distance**|
|---|---|---|---|
|**1**|EG0|START|184.8|
|**1**|EG1|END|293.2|
|**2**|EG2|START|236.4|
|**3**|EG1|END|289.7|
|**...**|…|…|…|
|**N**|EG0|START|186.9|

|**node_id**|**EG_0**|**EG_1**|**EG_2**|
|---|---|---|---|
|**0**|𝑑0,0|𝑑0,1|𝑑0,2|
|**1**|𝑑1,0|𝑑1,1|𝑑1,2|
|**2**|𝑑2,0|𝑑2,1|𝑑2,2|
|**3**|𝑑3,0|𝑑3,1|𝑑3,2|
|**...**|…|…|…|
|**M**|𝑑𝑀,0|𝑑𝑀,1|𝑑𝑀,2|

Theoretical Distances

Observed Activity Distances

17

## Slide 18

# Attack: Finding Protected Locations Inside EPZ Predicting Location

18

## Slide 19

# Constructing Confidence Intervals

activity_id entry_gate type inner_distance
1 EG0 START 184.8
1 EG1 END 293.2
2 EG2 START 236.4
3 EG1 END 289.7
... … … …
N EG0 START 186.9

##### Observed Activities

activity_id entry_gate type inner_distance
1 EG0 START 184.8
1 EG1 END 293.2
2 EG2 START 236.4
2 EG2 START 236.4
... … … …
N EG0 START 186.9
activity_id entry_gate type inner_distance
1 EG0 START 184.8
1 EG1 END 293.2
1 EG1 END 293.2
1 EG0 START 184.8
... … … …
N EG0 START 186.9
…
activity_id entry_gate type inner_distance
1 EG0 START 184.8
2 EG2 START 236.4
2 EG2 START 236.4
3 EG1 END 289.7
... … … … Confidence Interval
N-1 EG0 START 185.3

Resamples

19

## Slide 20

# Privacy Metrics

› **Success:** prediction within threshold of GT

› **Accuracy:** # unique predicted locations › **Reduction:** Accuracy / # locations inside EPZ

- › **Correctness:** avg distance between predictions and GT

- › **Uncertainty region:** joint area around predictions

20

## Slide 21

# Results

›

›

›

›

›

**Success:** prediction within threshold of GT

**Accuracy:** # unique predicted locations

**Reduction:** Accuracy / # locations inside EPZ

**Correctness:** avg distance between predictions and GT

**Uncertainty region:** joint area around predictions

21

## Slide 22

# Recommendations

### › Data minimization

_"What you don't have, you can't leak"_ (On-device) Generalization

Truncation

Rounding (m)

- Trade-off with usability: activity gets shorter

Reflect on data minimization at design time

22

## Slide 23

# Recommendations

› Data leak prevention Avoid inner distance scenario

0, 82.4, 84.7, 90.8, ….

23

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
» Data leak prevention +
Recommendations 320 + —
Correctness (m) 7
» Avoid inner distance scenario EPZ Radius (m) == Total distance
Strava User - Ride
© Evening Ride
Speed
=== |nner distance
pageView. streams.streamData.data
v {latlng: Array(31), grade_smooth: Array(31), distance: Array(31), altitude: Array(31), time: Array(.
p altitude: (31) [8.7, 8.7, 8.7, 8.7, 8.4, 8.1, 8.1, 8.1, 7.7, 7.5, 8, 8.2, 8.3, 8.5, 9, 9.2, 9, 9,
> distance: (31) | 0, 82.4, 84.7, 90.8, ...
> grade smooth: (31) [@, 0, -0.3, -1.4, -@.5, -@.4, -@.4, -0.3, -@.1, 0, 0.3, 0.5, 0.6, 0.7, 0.5, @.
> lating: (31) [Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Array(2), Arra
>time: (31) [41, 56, 57, 58, 61, 64, 81, 84, 94, 105, 115, 123, 133, 140, 148, 151, 160, 162, 171,
Dist: 1.6 km
Elev: 9m
Grade: 0.1%
23
```

## Slide 24

# Recommendations

- › Data leak prevention

Avoid inner distance scenario Fixing API leaks

Matching data precision API / UI

Thoroughly test API implementations for leaks

24

## Slide 25

# Recommendations

› Reduce the possibility of inferences

Figure
circle
lines

25

## Slide 26

# Recommendations

› Reduce the possibility of inferences

Metadata leaks may enable inferences! Model and mitigate possible inferences during design

May require some out-of-the-box thinking

Figure
circle
lines

Consider inferences during algorithm design

26

## Slide 27

# Recommendations

› Noisy distances?

Random noise distributions average out!

› Shifting distances?

No influence on total distance scenario!

- › Regenerating EPZs yields more diverse data

- › Smoothing tracks makes regression more accurate

Apparent solutions might not work!

27

## Slide 28

# Recommendations

› Nudge and support users towards privacy-friendly options

Enable privacy zones by default

Suggest EPZ radius based on street density _Requires effective solutions_

_that do not violate user privacy perception_

Provide users with clear privacy options

28

## Slide 29

## Proof-of-concept Service

### › 'Sanitize' sports activities

Create privacy zone based on street density

Avoiding the "inner distance" scenario

Applying generalization

Upload sanitized activity to service

<u>https://priva.distrinet-research.be/</u>

29

## Slide 30

# Disclosure to Networks

› All affected networks were contacted

› 3 out of 6 acknowledged our report

› Strava has engaged in a substantial discussion

30

## Slide 31

# Conclusion

› We develop a novel **inference attack** on privacy zones › Intuition: distance metadata + street grid = protected location

31

## Slide 32

## Black Hat Sound Bytes

### 1. Thoroughly test API implementations for leaks

### 2. Consider inferences during algorithm design

3. Provide users with clear privacy options

32

## Slide 33

Thank you!

karel.dhondt@kuleuven.be     victor.lepochat@kuleuven.be https://distrinet.cs.kuleuven.be/
