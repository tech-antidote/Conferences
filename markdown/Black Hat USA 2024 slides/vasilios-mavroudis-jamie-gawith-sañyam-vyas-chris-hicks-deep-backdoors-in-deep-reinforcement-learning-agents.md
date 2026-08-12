---
title: "Deep Backdoors in Deep Reinforcement Learning Agents"
speakers: ["Vasilios Mavroudis", "Jamie Gawith", "Sañyam Vyas", "Chris Hicks"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Vasilios Mavroudis & Jamie Gawith & Sañyam Vyas & Chris Hicks_Deep Backdoors in Deep Reinforcement Learning Agents.pdf"
pages: 38
sha256: "0d08be5b6d30611049c434f514e43168ba209bfe62201236bd6569db47b6d4e3"
text_chars: 5640
ocr_pages: 14
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:39:53Z"
---
# Deep Backdoors in Deep Reinforcement Learning Agents

**Speakers:** Vasilios Mavroudis, Jamie Gawith, Sañyam Vyas, Chris Hicks  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Vasilios Mavroudis & Jamie Gawith & Sañyam Vyas & Chris Hicks_Deep Backdoors in Deep Reinforcement Learning Agents.pdf` (38 pages)


## Slide 1

# **Deep Backdoors in Deep RL**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The
Alan Turing
Institute
Deep Backdoc
inDeep RL —
UNIVERSITY OF
©» BATH
ORE HORRORS EAS
ACAMwWS SB wWEAE wee
TOR RHE R BOOM OM
<~OnwWasOOCNeceun
#OP—-“VErOunNKRep
ween Sab oba0——
Ome 316 00000006
Se ®® O3990000 8". <8 FA
@S2@ @ DD ODOd Op’ FRE
&
```

## Slide 2

**Reinforcement Learning**

## Slide 3

**Reinforcement Learning**

## Slide 4

**Reinforcement Learning**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
— Beeblt Sal sxtsasesttcesis: RENENSIE] —— SelBileall -
ee a
```

## Slide 5

## Slide 6

**Reinforcement Learning**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a Drone racing: human versus autonomous
mann nee eS OSE REESE i ,
se . ”
#
_» Autonomous drone (ours)
```

## Slide 7

## **The Anatomy of a RL Backdoor**

Backdoor’ed
Neurons
Malicious
Trigger

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Anatomy of a RL Backdoor
STATE (si) Backdoor’ed
Neurons
St+1
Malicious eer
Trigger POLICY (n)
ENVIRONMENT AGENT
i) ACTION (a)
```

## Slide 8

## **Software Supply Chain Attacks**

Code Build

Deploy

Update

## Slide 9

## **Software Supply Chain Attacks**

Code Build

Deploy

Update

Compromise source code

## Slide 10

## **Software Supply Chain Attacks**

Code Build

Deploy

Update

Inject malicious code in build

## Slide 11

## **Software Supply Chain Attacks**

Code Build Deploy Update

#### Exploit deployment pipelines

## Slide 12

## **Software Supply Chain Attacks**

Code Build Update
Deploy

#### Tamper with updates

## Slide 13

## **ML Supply Chain Attacks**

**Data Training Model**

Deployment

Update

## Slide 14

## **ML Supply Chain Attacks**

Data **Training Model**

**Deployment**

Update

#### Poison training data

## Slide 15

## **Backdoor’ed Agent**

With Backdoor Trigger

## Slide 16

## **In-Distribution Trigger Demo**

Backdoor defence against indistribution triggers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
In-Distribution Trigger Demo
Backdoor defence against simple triggers
ad
Backdoor defence against in-
distribution triggers
```

## Slide 17

## **ML Supply Chain Attacks**

Data **Training** Model

**Deployment**

Update

Architectural Backdoors

## Slide 18

## **ML Supply Chain Attacks**

Data Training Model

Deployment

Update

Introduce backdoors in training

## Slide 19

## **ML Supply Chain Attacks**

Data Training Model

Deployment

Update

Compromise deployment pipelines

## Slide 20

## **ML Supply Chain Attacks**

Data Training Model

Deployment

Update

#### Poison the model update

## Slide 21

**Reinforcement Learning**

## Slide 22

## **~~Nuclear Fusion Reactors~~**

Fusion fuel must be kept “ **Dense** enough and **Hot** enough for **Long** enough”

2H
3H

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nuclear Fusion Reactors
Fusion fuel must be kept “Dense enough and Hot enough for Long enough”
Stellarators/Heliotro.. Laser/Inertial Altern. Concepts
17 11 40
Neutron
ry Q \S pS ee
6)- =<) Energy
Fusion _ ; 4 Republic of K..
Costa Rica
r Czech Republic
He én,
¢ ye
European jee
Kazakhstan
Libya
Operating Under construction Public i Public-Private Portu:
99 13 111 1
Germany
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Nuclear Fusion Reactors - Tokamaks
. bel se F coil current outer poloidal
toroidal . BneLIC Tleld coils magnetic field coils
magnetic field coils
```

## Slide 24

## Slide 25

**Plasma Control**

## Slide 26

## **Plasma Control**

Flux loop sensors
Magnetic probes

## Slide 27

## **Plasma Control**

Flux loop sensors
Magnetic probes

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Plasma Control
O Flux loop sensors
—> Magnetic probes
MN, Signal cables Thermocouple
\
15 2.0 25
Rim) Nest for the
metrology
Tangential
antimony
Hall sensor
Bottom coated vee
alumina
Normal antimony Attachment
Hall sensor to the vacuum vessel
```

## Slide 28

## **Plasma Control**

Flux loop sensors
Magnetic probes
Sensor Feedback
Controller
Target values

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Plasma Control
15 2.0 25
Bottom coated with
Sensor Feedback alumina af
O Flux loop sensors
—> Magnetic probes
NN Signal cables
\
Thermocouple
Tangential
antimony
Hall sensor
Nest for the
metrology
4
Controller <
Target values
Normal antimony Attachment
Hall sensor to the vacuum vessel
```

## Slide 29

## **Plasma Control**

Flux loop sensors
Magnetic probes
Actuator commands Sensor Feedback
Controller
Target values

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Plasma Control
+
| Actuator commands
15 2.0 25
Bottom coated with
Sensor Feedback alumina af
O Flux loop sensors
—> Magnetic probes
™.
Signal cables
\
Thermocouple
Tangential
antimony
Hall sensor
Nest for the
metrology
4
Controller <
Target values
Normal antimony Attachment
Hall sensor to the vacuum vessel
```

## Slide 30

## **Plasma Control**

Flux loop sensors
Magnetic probes
Sensor Feedback
Target values

Actuator commands

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Plasma Control
+
| Actuator commands
15 2.0 25
ay <
Bottom coated with
Sensor Feedback alumina af
O Flux loop sensors
—> Magnetic probes
MN, Signal cables Thermocouple
\
Tangential
antimony
Hall sensor
Nest for the
metrology
4
Target values
Normal antimony Attachment
Hall sensor to the vacuum vessel
```

## Slide 31

**Loss of Plasma Control – "Disruption"**

https://tds-scidac.github.io/gallery/

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Loss of Plasma Control - “Disruption”
gnitude
oO oO
Lb a
U Magnitude
4
O22
NA &
5
=
—
Pas
lu
fa
e
=)
O
°o
Time: 0.00000e+00
—|_phi (plasma) ug
| =Lphi (wall)
~ |—=T_max -O.
600 800 1000 1200 1400
bi
y
Relative_Densit
phi Magnitude
TEMPERATURE
J
https://tds-scidac.github.io/gallery/
```

## Slide 32

**Consequences**

## Slide 33

## **Threat Model**

Actuator
commands
Sensor Feedback

##### **Backdoor’ed Neurons**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Threat Model
Actuator
commands
r 7")
JET vessel: Re-deposited molten beryllium —
consequence of runaway beam hit
Neelele
ve
Wel
YAP XN \
.
\) Po 1M,
Hann
tty.
Backdoor’ed
Neu ro n Ss ease metal cover
was deformed during disruption
```

## Slide 34

## **Neural Activation Watchdog**

Normal activation patterns.

## Slide 35

## **Neural Activation Watchdog**

### Normal activation patterns.

Malicious Trigger observed!

## Slide 36

## **Neural Activation Watchdog**

### Normal activation patterns.

Malicious Trigger observed!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Neural Activation Watchdog
Episode 0 and Move 15
Normal activation patterns.
Malicious Trigger observed!
```

## Slide 37

Thanks!

# **Takeaways**

- ❖ RL agents show great promise for controlling complex and critical systems.

- ❖ ML is prone to supply chain attacks and neural network harder to audit.

- ❖ Check out our detection tool and let’s collaborate if you’re worried about ml supply chain attacks!

## Slide 38

Thanks!

# **Questions?**
