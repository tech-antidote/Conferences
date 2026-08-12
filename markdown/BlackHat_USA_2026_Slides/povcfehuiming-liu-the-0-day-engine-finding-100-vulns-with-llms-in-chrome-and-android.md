---
title: "The 0-Day Engine Finding 100+ Vulns with LLMs in Chrome and Android"
speakers: ["Povcfe", "Huiming Liu"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Povcfe&Huiming Liu_The 0-Day Engine Finding 100+ Vulns with LLMs in Chrome and Android.pdf"
pages: 47
sha256: "b10737bf6a51719a8375cd986d9083ad28f3272521ec00d0a359e0154b147a35"
text_chars: 19869
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:14:48Z"
---
# The 0-Day Engine Finding 100+ Vulns with LLMs in Chrome and Android

**Speakers:** Povcfe, Huiming Liu  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Povcfe&Huiming Liu_The 0-Day Engine Finding 100+ Vulns with LLMs in Chrome and Android.pdf` (47 pages)


## Slide 1

**The 0-Day Engine: Finding 100+ Vulns with LLMs in Chrome and Android**

**Speaker: Fangang Bu & Huiming Liu**

## Slide 2

## **ABOUT US**

**腾讯安全玄武实验室 TENCENT SECURITY XUANWU LAB**

**Fangang Bu @povcfe Security Researcher**

**Huiming Liu @liuhm09 Security Researcher**

## Slide 3

**Question: Will large language models replace security researchers?**

## Slide 4

## **AGENDA**

- **THE MOTIVATION**

- **FROM N-DAY PATCHES TO VARIANTS**

- **DECONSTRUCTING THE ZERO-DAYS**

- **LIVE DEMO**

## Slide 5

**1. THE MOTIVATION**

## Slide 6

## **1.1 Logic Vulnerabilities Matter**

### **For Android: No code execution needed. The boundary break is the impact.**

1. Privilege Escalation & Permissions

- Permission Bypasses

- Special App Access

- While-In-Use (WIU) Abuse

2. UI, Activity, & Multi-User Security

- Activity & Intent Spoofing

- UI Obfuscation & Tapjacking

- Multi-User & Private Space

3. Device Management

- Enterprise Bypasses

## Slide 7

## **1.2 How Can We Scale Finding Logic Vulnerabilities On Large-scale Codebases?**

Fuzz? Such As AFL AFL-Fuzz Fork Server Target Binary
Input
Crash
AFL-Fuzz Fork Server Target Binary
Input
Crash

## Slide 8

## **1.2 How Can We Scale Finding Logic Vulnerabilities On Large-scale Codebases?**

**Static Audit? Such As Codeql**

Source Code Codeql DB
Taint analysis
Compiler wrapper
Result
Vuln Rules XXX.ql
Source Code Codeql DB
Taint analysis
Compiler wrapper
Result
Vuln Rules XXX.ql
1. Reflection calls
2. Function pointers
Lack of many rules
3. ...

## Slide 9

## **1.3 Think Another Way(N-Day)**

### **Too many bugs. Too many models to internalize**

1. 3000+ Android security vulnerabilities (2016 – Now)

2. No researcher can internalize every vulnerability model

## Slide 10

## **1.3 Think Another Way(N-Day)**

**The bug is fixed. The model repeats.**

One Repeating Model: Authorization Based on Forged Identity Fields

1. 2020: CVE-2020-0107 / CVE-2020-0246

2. 2021: CVE-2021-0319

3. 2022: CVE-2022-20223 / CVE-2022-20455

4. 2023: CVE-2023-21266 / CVE-2023-40105 / CVE-2023-40127

5. 2024: CVE-2024-0015 6. 2025: CVE-2025-0086 / CVE-2025-48537 / CVE-2025-48585

## Slide 11

## **1.4 How I Did It**

### **Generalization finds candidates. Verification makes them real.**

1. Scaling Model N-day Patch Primitives

2. Generalize them into 0-day variants

3. Verify each phase with agents and toolchains

## Slide 12

- **THE MOTIVATION**

- **FROM N-DAY PATCHES TO VARIANTS**

- **DECONSTRUCTING THE ZERO-DAYS**

- **LIVE DEMO**

## Slide 13

**2. FROM N-DAY PATCHES TO VARIANTS**

## Slide 14

## **2.1 The Question**

**The target question:**

**1. Does the historical vulnerability still exist?**

**2. Do similar variants exist elsewhere?**

**The technical question:**

**1. How to model N-day patch primitives?**

**2. How LLM Agents Analyze Large-scale Codebases?**

**3. How to ensure vulnerabilities are real?**

**4. How to find vulnerabilities at scale?**

## Slide 15

## **2.2 WorkFlow**

### **Does the historical vulnerability still exist? Do similar variants exist elsewhere?**

Patch Diff
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?

## Slide 16

## **How to model N-day patch primitives?**

### **Thousands of fixes become thousands of searchable vulnerability models.**

Patch Diff
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Root Cause Security Invariant
Searchable Pattern
Primitive-driven Role-driven
Variant Candidates

## Slide 17

## **How to model N-day patch primitives?**

### **Thousands of fixes become thousands of searchable vulnerability models.**

Patch Diff
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Root Cause Security Invariant
Searchable Pattern
How analyze large-scale
codebases?
Primitive-driven Role-driven
Variant Candidates How analyze large-scale
codebases?

## Slide 18

## **How LLM Agents Analyze Large-scale Codebases?**

### **Init Task: Analyze all control-flow paths leading to system() calls.**

Large-scale
Codebases
Find Many  Analyze All
Call Sites Control-Flow Paths
Init Task

## Slide 19

## **How LLM Agents Analyze Large-scale Codebases?**

### **Init Task: Analyze all control-flow paths leading to system() calls.**

1. Limited LLM context window Large-scale Codebases Find Many Analyze All Call Sites Control-Flow Paths Init Task 2. Too many analysis targets, distracting the model’s attention

3. Deep function-call chains, making in-depth analysis difficult

## Slide 20

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis
Decompose Tasks
Call Site 1
Large-scale
Codebases
Find Many
Call Site 2
Call Sites
Init Task
Call Site 3

## Slide 21

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis
Iterative Loop
Small-scope,
Call Site 1
precise analysis
Large-scale
Codebases
Find Many  Locate deep- Small-scope,
Call Site 2 Merge
Call Sites dive points precise analysis
Init Task
Small-scope,
Call Site 3
precise analysis
Cycle_0(Control Flow)
A -> B -> E
-> C -> F
-> D

## Slide 22

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis
Small-scope,
Call Site 1
precise analysis
Large-scale
Codebases
Find Many  Locate deep- Small-scope,
Call Site 2 Merge
Call Sites dive points precise analysis
Init Task
Small-scope,
Call Site 3
precise analysis
Cycle_1(Control Flow)
A -> B -> E
-> C -> F
-> D

## Slide 23

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis
Small-scope,
Call Site 1
precise analysis
Large-scale
Codebases
Find Many  Locate deep- Small-scope,
Call Site 2 Merge
Call Sites dive points precise analysis
Init Task
Small-scope,
Call Site 3
precise analysis
Cycle_2(Control Flow)
A -> B -> E
-> C -> F
-> D

## Slide 24

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Patch Diff

Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Large-scale  Security Invariant
Codebases Analysis
Searchable Pattern
Root Cause
Large-scale  Primitive-driven Role-driven
Codebases Analysis
Large-scale
Fix Status
Codebases Analysis
Variant Candidates

## Slide 25

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

One LLM session. One simple task. Patch Diff
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Large-scale  Security Invariant
Codebases Analysis
Searchable Pattern
Root Cause
Large-scale  Primitive-driven Role-driven
Codebases Analysis
Large-scale
Fix Status
Codebases Analysis
if the issue is real?
Variant Candidates
if the issue is real?

### **One LLM session. One simple task.**

## Slide 26

## **How to ensure vulnerabilities are real**

### **Step-by-Step Verification**

1. Build Tools  - compile test apps, framework modules, and PoCs.

2. ADB - deploy, trigger, reproduce.

3. Frida & System Monitoring - inspect dynamic behavior and verify runtime state.

## Slide 27

Patch Diff

## **How to ensure vulnerabilities are real**

Step-by-Step Verification
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Large Program  Security Invariant
Analysis Task
Searchable Pattern
Root Cause
Verify
Large Program  Primitive-driven Role-driven
Analysis Task
Large Program
Fix Status
Analysis Task
Variant Candidates
Verify
Verify

### **Step-by-Step Verification**

## Slide 28

***Android/Chrome/Firefox/Open Source Project***

Solve One Problem, Then Scale It Patch Diff  *Android/Chrome/Firefox/Open Source Project*
Historical Vuln Similar Variant
Still Exists? Discovery Elsewhere?
Large Program  Security Invariant
Analysis Task
Searchable Pattern
Root Cause
Verify
Large Program  Primitive-driven Role-driven
Analysis Task
Large Program
Fix Status
Analysis Task
Variant Candidates
Verify
Verify

## **Solve One Problem, Then Scale It**

## Slide 29

**2.6 Result**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2.6 Result
Ha og &
buganizer-sy... May 9
a
to b-system+1027... v
https://issuetracker.google.com/issues/495651377
Changed
nc...@google.com added comment #5:
Hello,
The Android security team has conducted an initial
severity assessment on this report. Based on our
published severity assessment matrix (1) it was rated
as Critical severity and High quality.
This issue has been assigned to the appropriate team
for remediation. We will provide an update on
remediation status as it becomes available. We ask
for your continued confidentiality as we proceed with
our standard investigation and remediation process.
Thank you,
Android Security Team
(1) Severity Matrix: https://source.android.com/
security/overview/updates-resources#severity
«6 he nn me a
En: ew ae 5 me
= = = =
r vent: 190951
status: Assigned
reporter: povcfe2sec@gmail.com
oeape>
OM 2S26
```

## Slide 30

- **THE MOTIVATION**

- **FROM N-DAY PATCHES TO VARIANTS**

- **DECONSTRUCTING THE ZERO-DAYS**

- **LIVE DEMO**

## Slide 31

# **3. DECONSTRUCTING THE ZERO-DAYS**

## Slide 32

## **3.1 Pin Lock Bypass(CVE)**

```
CVE-2025-48541
```

```
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
```

```
index 8270d50a..ce4fdd6 100644
```

- `--- a/src/com/android/settings/biometrics/face/FaceSettings.java`

```
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
```

## Slide 33

## **3.1 Pin Lock Bypass(CVE)**

#### **`CVE-2025-48541`**

```
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
```

```
index 8270d50a..ce4fdd6 100644
```

- `--- a/src/com/android/settings/biometrics/face/FaceSettings.java`

```
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
```

```
-
mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
```

```
+        if (callingPackage == null || !callingPackage.equals(activity.getPackageName())) {
```

```
+            // only allow these extras when called internally by Settings
```

```
+            mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
```

## Slide 34

## **3.1 Pin Lock Bypass(CVE)**

```
CVE-2025-48541
```

```
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
index 8270d50a..ce4fdd6 100644
```

```
---a/src/com/android/settings/biometrics/face/FaceSettings.java
```

```
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
```

```
-
mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
```

- `mSensorId = getIntent().getIntExtra(BiometricEnrollBase.EXTRA_KEY_SENSOR_ID, -1);`

- `mChallenge = getIntent().getLongExtra(BiometricEnrollBase.EXTRA_KEY_CHALLENGE, 0L);`

- `mUserId = getActivity().getIntent().getIntExtra(`

- `Intent.EXTRA_USER_ID, UserHandle.myUserId());`

```
+        if (callingPackage == null || !callingPackage.equals(activity.getPackageName())) {
```

```
+            mUserId = UserHandle.myUserId();
+        } else {
```

```
+            // only allow these extras when called internally by Settings
```

```
+            mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
```

```
+            mSensorId = getIntent().getIntExtra(BiometricEnrollBase.EXTRA_KEY_SENSOR_ID, -1);
```

```
+            mChallenge = getIntent().getLongExtra(BiometricEnrollBase.EXTRA_KEY_CHALLENGE, 0L);
```

## Slide 35

## **3.1 Pin Lock Bypass(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
---a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

## Slide 36

## **3.1 Pin Lock Bypass(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
---a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
+        mAllowInternalExtras = false;
```

```
+            if (TextUtils.equals(callingPackage, activity.getPackageName())) {
```

```
+                mAllowInternalExtras = true;
```

```
if (BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

```
-
if (BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
+        if (mAllowInternalExtras && BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

## Slide 37

## **3.1 Pin Lock Bypass(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
---a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

```
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

   - `public void onAttach(Context context) {`

- `mUserId = getActivity().getIntent().getIntExtra(Intent.EXTRA_USER_ID,`

- `UserHandle.myUserId());`

- `+        mUserId = UserHandle.myUserId();`

```
+        mAllowInternalExtras = false;
```

```
+
```

- `+        if (context instanceof SettingsActivity) {`

- `+            final SettingsActivity activity = (SettingsActivity) context;`

- `+            final String callingPackage = activity.getInitialCallingPackage();`

- `+            if (TextUtils.equals(callingPackage, activity.getPackageName())) {`

```
+                mAllowInternalExtras = true;
```

```
+                mUserId = activity.getIntent().getIntExtra(Intent.EXTRA_USER_ID, mUserId);
```

```
if (BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

```
+        if (mAllowInternalExtras && BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

## Slide 38

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
```

```
index 67219a5..45be472 100644
```

- `--- a/src/com/android/keychain/KeyChainActivity.java`

```
+++ b/src/com/android/keychain/KeyChainActivity.java
```

## Slide 39

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
```

```
index 67219a5..45be472 100644
```

- `--- a/src/com/android/keychain/KeyChainActivity.java`

```
+++ b/src/com/android/keychain/KeyChainActivity.java
```

```
String hostMessage = String.format(res.getString(R.string.requesting_server),
```

```
uri.getAuthority());
```

```
+                    Uri.encode(uri.getAuthority(), "$,;:@&=+"));
```

## Slide 40

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
index 67219a5..45be472 100644
```

- `--- a/src/com/android/keychain/KeyChainActivity.java`

```
+++ b/src/com/android/keychain/KeyChainActivity.java
```

```
@@ -533,7 +533,7 @@
```

```
Uri uri = getIntent().getParcelableExtra(KeyChain.EXTRA_URI);
if (uri != null) {
```

```
String hostMessage = String.format(res.getString(R.string.requesting_server),
```

```
uri.getAuthority());
```

```
+                    Uri.encode(uri.getAuthority(), "$,;:@&=+"));
```

```
if (contextMessage == null) {
```

```
contextMessage = hostMessage;
```

```
} else {
```

## Slide 41

## **3.2 UI Obfuscation(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
```

```
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
```

```
index 0000000..0000000 100644
```

```
---a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
```

```
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
```

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
```

- `--- a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java`

```
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
```

## Slide 42

## **3.2 UI Obfuscation(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
index 0000000..0000000 100644
```

```
---a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
-
applicationInfo.loadLabel(getPackageManager())));
+                    applicationInfo.loadSafeLabel(getPackageManager())));
```

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
```

```
---a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
```

```
-
applicationInfo.loadLabel(mPackageManager)));
+                        applicationInfo.loadSafeLabel(mPackageManager)));
```

## Slide 43

## **3.2 UI Obfuscation(Zero-Day)**

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
index 0000000..0000000 100644
```

```
---a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
@@ -243,11 +243,11 @@ private void loadHeader() {
```

```
-
applicationInfo.loadLabel(getPackageManager())));
+                    applicationInfo.loadSafeLabel(getPackageManager())));
```

```
diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
```

```
---a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
@@ -84,11 +84,11 @@ public class HeaderViewHolder extends RecyclerView.ViewHolder {
mAppIconView.setImageDrawable(mPackageManager.getApplicationIcon(applicationInfo));
```

```
-
applicationInfo.loadLabel(mPackageManager)));
```

```
+                        applicationInfo.loadSafeLabel(mPackageManager)));
```

## Slide 44

**4. LIVE DEMO**

## Slide 45

**Question: Will large language models replace security researchers? Answer:**

- The birth of AFL started a security technology revolution in the fuzzing era, and LLMs are now changing the way we do security research.

- The core value of security researchers has never changed: finding issues, verifying issues, and solving real-world security problems.

- **Tools will keep evolving, but security researchers will not be replaced.**

## Slide 46

## **Key Takeaways**

**1. N-Day Patches Turn Old Fixes into Reusable Models**

**2. Large-Codebase Analysis Becomes Scalable Through Task Decomposition**

**3. LLM Results Become Reliable Through Tool-Based Verification**

**4. One Concrete Vulnerability Problem Can Scale to Batch Discovery Across Projects**

**5. LLMs Change Vulnerability Research, but Security Researchers Still Drive It**

## Slide 47

**QA**

### **email: povcfe2sec+blackhat@gmail.com**
