---
title: "noRecognition Could a pattern on your clothing fool Facial Facial Recognition"
speakers: ["Bill Swearingen"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Bill Swearingen - noRecognition Could a pattern on your clothing fool Facial Facial Recognition - hevnsnt.pdf"
pages: 39
sha256: "cbe5991d801e599f9eed99b4b65db4a525b4132078ae3ae56c45c594c6a292ba"
text_chars: 13471
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:22:17Z"
---
# noRecognition Could a pattern on your clothing fool Facial Facial Recognition

**Speakers:** Bill Swearingen  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Bill Swearingen - noRecognition Could a pattern on your clothing fool Facial Facial Recognition - hevnsnt.pdf` (39 pages)


## Slide 1

##### **noRECOGNITION**

**Today, over 100 cameras logged your beautiful face.**

You didn't opt in. You can't opt out.

**D E F C O N 3 4**

**Adversarial fashion that defeats AI surveillance.**

## Slide 2

Facial recognition is everywhere.

**And it is being used against us.**

**117M+**

Your drivers license photo is probably in a police face database

higher false match rate for darker-skinned individuals

**6,000+** police departments on the Flock network

**10-100x**

Background source: deflock.org

## Slide 3

**Sold to catch car thieves. Rebuilt into a surveillance state.** 140,000 monthly police users. Every passing car, logged. No warrant.

## Slide 4

###### **FOOTAGE TAKEN FROM AN ALPR CAMERA**

**Face identification** Matched to an identity database

**Emotion detection** Inferred from microexpressions

**Screen reading** Phone content captured

**This is now.**

Video credit: Benn Jordan https://www.youtube.com/@BennJordan

## Slide 5

**Trusted to serve. They served themselves.** Sedgwick, Orange City, Joplin. At least 18 documented cases. So far…

## Slide 6

**Hackers have always been the counterbalance** **~~.~~**

## Slide 7

**Hey I’m bill, I am a HAKCER**

Bill Swearingen — ex-CISO, ex-red-team lead, founder of SecKC. CISSP · CISM · CMMC-RP · TS/SCI

## Slide 8

### **SECKC**

**The World’s largest monthly hacker meetup**

## Slide 9

### **IT STARTED AS A GREAT IDEA**

## Slide 10

## Slide 11

##### **A camera is just a parser.**

Every parser in the history of computing has been exploitable when an attacker controls the input.

SQL injection works because the database parser cannot distinguish data from commands.

It parses pixels into objects. Nothing more.

**I control what appears on camera.**

**I control the input, can I impact the output?**

## Slide 12


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Status
Overall Stats
Epoch: 6
Total Anomalies: 11730
Epoch Rate: 737.7 tests/min
Stop Fuzzer: Press Ctri-C
Anomaly Preview
Epoch 6
Epoch 5:
Epoch 4:
Epoch 3:
Epoch 2:
Epoch 1:
Rate:
Rate:
Rate:
Rate:
Rate:
717 tests/min,
561 tests/min,
406 tests/min,
662 tests/min,
410 tests/min,
Epoch Progress
14% * 6:50:35 < 8:17:45 + 12.3 tests/sec
Face Anomalies: 10826, Person Anomalies: 27885
Face Anomalies: 7858, Person Anomalies: 21078
Face Anomalies: 4897, Person Anomalies: 14372
Face Anomalies: 2153, Person Anomalies: 7692
Face Anomalies: 278, Person Anomalies: 1811
‘+ Added 'saliency_eye_attack_seed8334109' to priority list.
Anomaly: saliency_eye_attack_seed8334109 (PERSON_LOST (Found: 6, Baseline: 1))
‘+ Added 'trypophobiat+gradient_seed4464024' to priority List.
Anomaly: trypophobiat+gradient_seed4464024 (PERSON_LOST (Found: ©, Baseline: 1))
‘# Added 'qr_code+tiled_logo_seed1671641' to priority list.
Anomaly: gr_code+tiled_logo_seed1671641 (PERSON_LOST (Found: 6, Baseline: 1))
Anomaly Log
```

## Slide 13

**I had invented something AMAZING. My friends were quick to help.**


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| had
invented something
AMAZING.
My friends were
quick to help.
Super Famous Podcasters
4 members
October 3, 7026
omg guys | am hacking FACIAL
RECOGNITION
| don't think you understand what
Facial Recognition means
```

## Slide 14

###### **JOSHUA MARPET WAS RIGHT**

I had no freaking clue what I was doing

## Slide 15

###### **Now I know what you are thinking: this guy is a genius.**

Most of this ground was already walked. They walked so I could run, and I am grateful they did.

###### **THE ARTISTS**

###### **THE PRODUCTS**

###### **THE RESEARCH**

###### **Adam Harvey, CV Dazzle (2010)**

###### **Cap_able, Manifesto (2023)**

###### **Thys et al. (2019)**

Makeup and hair styling designed to defeat face detection.

Knitwear with adversarial patterns; 60% evasion claimed against one detector.

Printed patch defeats YOLOv2 person detection.

###### **Adam Harvey, HyperFace (2017)**

###### **Urban Privacy**

###### **Xu et al. (2020)**

Textile printed with decoy face patterns to saturate detectors.

Anti-surveillance clothing offered at roughly 35 euros.

Adversarial T-shirt: physical attack on person detectors under deformation.

###### **Kate Rose, Adversarial Fashion (2019)**

###### **Reflectacles**

###### **Wu et al. (2020)**

Garments printed to inject false plate reads into ALPR systems.

Infrared-blocking eyewear aimed at camera and depth sensors.

Invisibility cloak: wearable attack on object detectors.

###### **THE MEASUREMENT GAP**

Claims are typically measured against a single object detector, in sample, without a control. Independent review of the category scored 6/10; of thirty published methods, twelve were ever tested against a real system.

## Slide 16

###### **Detection Models**

Three distinct capabilities, three different questions

**PERSON FACE FACIAL RECOGNITION How many people are there? How many faces are there? Do we know this face?** Detects human bodies in the frame. Locates and isolates faces in the frame. Matches a detected face against a gallery Produces a count, not an identity. Still produces no identity. of known identities.

## Slide 17

###### **Confidence**

Every detection is a score, not a fact

###### **PERSON**

A false positive adds a bounding box. Thresholds are commonly set low, since the cost of a missed presence exceeds the cost of a spurious one.

###### **FACE**

A face below threshold is never passed downstream. Threshold choice here constrains every recognition result that follows.

###### **FACIAL RECOGNITION**

A false match asserts an identity. Thresholds must be high, because the cost of error is attribution to a specific person.

## Slide 18

**Target What it actually does Closest open Axis P1465-LE, Q1656-LE** On-device object detection **YOLOv5s** or **SSD-MobileNetV2 MTCNN** (legacy), **SSD faceIntel OpenVINO** (legacy smart city) Face detection **detection-retail** (current default) **Hikvision AcuSense** Human/vehicle detection, _not_ face **SSD-MobileNetV2** or YOLO-class **RetinaFace + ArcFace** (InsightFace **Dahua WizSense, Hikvision MinMoe** Face recognition (1:N) buffalo_L) **Avigilon AI NVR** Person detection + appearance re-ID<sup>**PeopleNet**(DetectNet_v2 /</sup> ResNet34) + **OSNet** -class re-ID Person/object detection, cloud-side, **Axon Body 4, Fleet 3 YOLOv8n** -class detector _not_ recognition Face/head + plate detection, _not_ **Axon Redaction Assistant RetinaFace** or SSD face detector recognition **ArcFace** patent hints at FaceNet- **Clearview AI, state surveillance** Face recognition (1:N) style metric learning

## Slide 19

**There are cameras everywhere But y’all only care about defeating flock.**

## Slide 20

###### **Every persona now runs a gauntlet of 11 models.**

Five person detectors, four face detectors, two recognition models. One pass became eleven.

PERSON 5 MODELS FACE 4 MODELS FACIAL RECOGNITION 2 MODELS
How many people are there? How many faces are there? Is this face in the database?
P1  YOLOv8n F1  InsightFace R1  ArcFace
P2  YOLOv5s F2  Facenet-MTCNN R2  Facenet
P3  SSD-MobileNet F3  MTCNN
P4  ResNet34-SSD F4  RetinaFace
P5  YOLOv5 (added July 2026)

###### **THE COST**

Each persona is scored against all eleven models rather than one. Every sweep now carries eleven times the inference load, and research throughput falls in proportion.

## Slide 21

**I’M GOING TO NEED MORE POWER**

## Slide 22

## Slide 23

## **31.7 Million**

**PATTE RN S TE S TE D**

**534.6K 480.7k ANOMALIES MULTI-MODAL DISCOVERED ANOMALIES** 1.7% of patterns tested 89.9% of anomalies discovered

**534.6K**

1.7% of patterns tested

**85 EXTREME ANOMALIES** 0.016% of anomalies discovered

31.7M patterns  →  534.6K anomalies  →  480.7K multi-modal  →  85 extreme

## Slide 24

Each pattern scored against the full gauntlet of 10 models. The highest performers pushed into an evolution engine, picking the strongest characteristics and breeding them.

**1000s of HIGHLY EFFECTIVE PATTERNS FOUND**

#### **I AM A GENIUS**

## Slide 25

## Slide 26

# **192GB**

**Then two Blackwells showed up.** It’s time to change tactics

## Slide 27

https://www.youtube.com/watch?v=L_4BPjLBF4E


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ys) to Walk (deep reinforcement learning)
https://www.youtube.com/watch?v=L_4BPjLBF4E
```

## Slide 28

**All of it became training data.**

Every win and every loss now trains a deep reinforcement learning system.


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
31.7 Million
PATTERNS TESTED
534.6K 480.7k 85
ANOMALIES MULTI-MODAL EXTREME
DISCOVERED ANOMALIES ANOMALIES
1.7% of patterns tested 89.9% of anomalies discovered 0.016% of anomalies discovered
31.7M patterns — 534.6K anomalies — 480.7K multi-modal — 85 extreme
All of it became training data.
Every win and every loss now trains a deep reinforcement learning system.
```

## Slide 29

## **588**

**E R S O N A S**

Nearly twenty times the corpus: broader coverage of body types, ages, and skin tones.

## Slide 30

## Slide 31

###### **One image. 6,300 guesses. Thirteen numbers each.**

What Flock's own model file says: flock_yoloV5.tflite, output shape [1, 6300, 13]

**1 one image per pass**

The camera runs a single frame at a time.

**6,300 candidate boxes** Grids 40x40 + 20x20 + 10x10, three anchors each.

**13 numbers per candidate** 4 box + 1 objectness + 8 class scores.

###### **The thirteen numbers, and the one that decides whether you exist**

x y

w

h **obj**

c1 c2 c3 c4 c5 c6 c7 c8

4  box coordinates **OBJECTNESS**

8  class scores: person, car, plate…

Objectness answers one question: is there a thing here at all? Score = objectness x P(person); a box is drawn only if score >= 0.75.

**YOLOv5 — 320, what Flock ships**

###### **SSD — 300, the other build**

flock_yoloV5.tflite

flock_small_tf.tflite · .dlc (SNPE)

**in 320 x 320 x 3   → [1, 6300, 13]**

**in 300 x 300 x 3   → [1, 1917, 11]**

_One scalar gates every detection. LOCAL → the soft target._

_10 classes + background, no objectness. GLOBAL → the wall._

**The classes are just output channels:  person** · car · truck · bus · trailer · motorcycle · bicycle · **licensePlate** The plate reader was never bolted on: licensePlate is a class, with its own post-filter areaThreshold = 0.00040690104

## Slide 32

###### **What the adversarial pattern is actually doing**

YOLOv5-320, the objectness family: one scalar per candidate decides whether a box is drawn

###### **01**

###### **What the filters expect**

The backbone is an edge and texture detector, trained on natural photographs. Its filters are tuned for skin, cloth folds, hair and shadow.

###### **02**

###### **What the pattern is**

Dense, periodic, highfrequency structure. No filter in the backbone is matched to it, so the features that fire carry no evidence of a body.

###### **03**

###### **What happens to the scalar**

In the cells the garment covers, objectness falls. That is the single number answering: is there a thing here at all?

###### **04**

###### **What the pipeline then does**

score = objectness x P(person) collapses. Under the 0.75 keep-line no box is drawn, so NMS, tracking and upload never run.

MEASURED, HELD-OUT IDENTITY
0.91
0.75 detect line
0.28
CLEAN PATTERN
person detected no box drawn

**Same body. Same camera. Same model. Only the texture changed.** Occlusion-subtracted against a solid black panel of the same geometry, so this is the pattern, not coverage.

**Objectness is one scalar over a region a garment can physically reach.**

###### **WHY SSD WALLS**

1917 anchors each run class against background. The garment reaches the torso boxes; whole-body and background boxes still see you, and one survivor keeps you detected.

## Slide 33

**C L E A N V E R S U S P A T T E R N , W I T H A S O L I D - B L A C K C O N T R O L**

###### **THE 0DAY SLIDE**

**11 / 11 DEFEATED**


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CLEAN VERSUS PATTERN, WITH A SOLID-BLACK CONTROL
THE ODAY SLIDE
P1 (YOLOv8n) P2 (YOLOv5s) = P3 (SSD-MobileNet) P4 (ResNet34-SSD)
Fl (SCRFD) F2 (MTCNN) F4 (RetinaFace-R50)
11/11 DEFEATED
```

## Slide 34

###### **THE FINDING THAT CHANGED EVERYTHING**

Certain patterns changed more than the confidence. Some caused the bounding box to **move** . Others caused unexpected configuration changes **TO THE CAMERA** .

## Slide 35

**W H E R E T H E P R O O F S T A N D S**

###### **Digital, and held to a stricter bar than the field.**

**T HE T E S TIN G C R IT ER IA**

**L IV E FA B R IC TE S TI NG**

###### **Sealed sweeps**

Train, select and report kept separate, so nothing is scored on the data that produced it.

###### **Just begun.**

###### **Held out, multi-angle, 500+ people**

More than 500 distinct personas, unseen at training time, across multiple view buckets and an expectation over transformations.

###### **Occlusion subtracted**

Printed fabric trials are under way. Nothing physical is claimed yet: the digital results above do not transfer until fabric passes the same occlusionsubtracted bar.

The pattern must beat a solid black panel of the same geometry, or the result is discarded.

Don’t like this? Blame nvidia

## Slide 36

**DEMO TIME**


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO TIME
MODEL UNDER TEST: Flock - YOLOv5 320
1P
Flock - YOLOv5 320 0.80 SEEN x1
```

## Slide 37

###### **T H E N E X T Q U E S T I O N**

A person already disappears from the fielded Flock detector.

###### **Can I make a car disappear?**

**I N P A R T N E R S H I P W I T H DONUT MEDIA**

Vehicles, camera time and a test environment for the plate and vehicle recognition work.

Same bar: controls in loop, occlusion subtracted.

## Slide 38

###### **OK GREAT WHERE DO I BUY ONE**

**I am opening a Kickstarter to fund the build-out.**

###### **Test fabrics**

Substrates, weaves and inks, to find what actually holds a pattern.

###### **Dye-sublimation printer**

In-house printing so an iteration takes hours instead of weeks.

###### **More cameras**

Fielded hardware beyond the bench, so results are measured through real lenses.

Same standard: controls in loop, occlusion subtracted, results published.

###### **Scan to back the build**

Kickstarter, launching with this talk

## Slide 39

###### **noRECOGNITION**

Visible to humans. Invisible to machines.

Bill Swearingen · @hevnsnt · SecKC · norecognition.org
