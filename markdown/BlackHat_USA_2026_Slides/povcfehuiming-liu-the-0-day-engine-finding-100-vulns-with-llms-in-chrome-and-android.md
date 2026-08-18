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
text_chars: 19954
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 95.2
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 30
vision_verified_pages: 47
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:41:39Z"
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

**Fuzz? Such As AFL**

AFL-Fuzz sends Input to the Fork Server, which runs the Target Binary; a Crash is reported back from the Target Binary to the Fork Server, and the loop returns to AFL-Fuzz.

The same pipeline is drawn twice, the lower copy highlighting the Crash feedback path in red.

## Slide 8

## **1.2 How Can We Scale Finding Logic Vulnerabilities On Large-scale Codebases?**

**Static Audit? Such As Codeql**

Source Code is turned into a Codeql DB by a Compiler wrapper; Vuln Rules become XXX.ql. Both feed Taint analysis, which produces the Result.

The same pipeline is drawn twice, the lower copy highlighting the Taint analysis path in red and adding two callouts.

Callout on Vuln Rules: Lack of many rules

Callout on the Taint analysis path:

1. Reflection calls

2. Function pointers

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

5. 2024: CVE-2024-0015

6. 2025: CVE-2025-0086 / CVE-2025-48537 / CVE-2025-48585

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

### **Does the historical vulnerability still exist?**

### **Do similar variants exist elsewhere?**

Patch Diff branches into two questions:

- Historical Vuln Still Exists?

- Similar Variant Discovery Elsewhere?

## Slide 16

## **How to model N-day patch primitives?**

### **Thousands of fixes become thousands of searchable vulnerability models.**

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Historical Vuln Still Exists? leads to Root Cause, which leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both converge on Variant Candidates.

## Slide 17

## **How to model N-day patch primitives?**

### **Thousands of fixes become thousands of searchable vulnerability models.**

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Historical Vuln Still Exists? leads to Root Cause, which leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both converge on Variant Candidates.

Two red callouts are added, each reading "How analyze large-scale codebases?" — one pointing at Root Cause, the other at the Role-driven / Variant Candidates path.

## Slide 18

## **How LLM Agents Analyze Large-scale Codebases?**

### **Init Task: Analyze all control-flow paths leading to system() calls.**

Large-scale Codebases and Init Task both feed Find Many Call Sites, which leads to Analyze All Control-Flow Paths.

## Slide 19

## **How LLM Agents Analyze Large-scale Codebases?**

### **Init Task: Analyze all control-flow paths leading to system() calls.**

Large-scale Codebases and Init Task both feed Find Many Call Sites, which leads to Analyze All Control-Flow Paths.

Three problems are called out in red over the diagram:

1. Limited LLM context window

2. Too many analysis targets, distracting the model’s attention

3. Deep function-call chains, making in-depth analysis difficult

## Slide 20

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis

Large-scale Codebases and Init Task both feed Find Many Call Sites, which fans out to Call Site 1, Call Site 2 and Call Site 3 inside a red dashed region labelled Decompose Tasks.

## Slide 21

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis

Large-scale Codebases and Init Task both feed Find Many Call Sites, which fans out to Call Site 1, Call Site 2 and Call Site 3.

Call Site 2 enters a red dashed region labelled Iterative Loop: Locate deep-dive points fans out to three Small-scope, precise analysis boxes, which feed Merge; Merge loops back to Locate deep-dive points.

Cycle_0(Control Flow)

```text
A -> B -> E
  -> C -> F
  -> D
```

None of the path is highlighted yet — every node is still white.

## Slide 22

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis

Large-scale Codebases and Init Task both feed Find Many Call Sites, which fans out to Call Site 1, Call Site 2 and Call Site 3.

Call Site 2 leads to Locate deep-dive points, which fans out to three Small-scope, precise analysis boxes; those feed Merge, and Merge loops back to Locate deep-dive points.

Cycle_1(Control Flow)

```text
A -> B -> E
  -> C -> F
  -> D
```

A, B, C and D are now highlighted in blue; E and F are still white.

## Slide 23

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Large-scale Codebases Analysis

Large-scale Codebases and Init Task both feed Find Many Call Sites, which fans out to Call Site 1, Call Site 2 and Call Site 3.

Call Site 2 leads to Locate deep-dive points, which fans out to three Small-scope, precise analysis boxes; those feed Merge, and Merge loops back to Locate deep-dive points.

Cycle_2(Control Flow)

```text
A -> B -> E
  -> C -> F
  -> D
```

The whole path is now highlighted in blue.

## Slide 24

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Left branch: Historical Vuln Still Exists? feeds a Large-scale Codebases Analysis step that yields the Root Cause; a second Large-scale Codebases Analysis step then yields the Fix Status.

Right branch: Root Cause leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both feed a Large-scale Codebases Analysis step that produces Variant Candidates.

## Slide 25

## **How LLM Agents Analyze Large-scale Codebases: Task Decomposition**

### **One LLM session. One simple task.**

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Left branch: Historical Vuln Still Exists? feeds a Large-scale Codebases Analysis step that yields the Root Cause; a second Large-scale Codebases Analysis step then yields the Fix Status.

Right branch: Root Cause leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both feed a Large-scale Codebases Analysis step that produces Variant Candidates.

Two red callouts are added, each reading "if the issue is real?" — one pointing at Fix Status, the other at Variant Candidates.

## Slide 26

## **How to ensure vulnerabilities are real**

### **Step-by-Step Verification**

1. Build Tools  - compile test apps, framework modules, and PoCs.

2. ADB - deploy, trigger, reproduce.

3. Frida & System Monitoring - inspect dynamic behavior and verify runtime state.

## Slide 27

## **How to ensure vulnerabilities are real**

### **Step-by-Step Verification**

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Left branch: Historical Vuln Still Exists? feeds a Large Program Analysis Task that yields the Root Cause; a second Large Program Analysis Task then yields the Fix Status, which feeds a Verify step; that Verify loops back to the first Large Program Analysis Task.

Right branch: Root Cause leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both feed a Large Program Analysis Task that produces Variant Candidates, which feed a Verify step; that Verify loops back to Security Invariant.

A red dotted region labelled Verify encloses the analysis steps of both branches.

## Slide 28

## **Solve One Problem, Then Scale It**

\*Android/Chrome/Firefox/Open Source Project\*

Patch Diff branches into Historical Vuln Still Exists? (left) and Similar Variant Discovery Elsewhere? (right).

Left branch: Historical Vuln Still Exists? feeds a Large Program Analysis Task that yields the Root Cause; a second Large Program Analysis Task then yields the Fix Status, which feeds a Verify step; that Verify loops back to the first Large Program Analysis Task.

Right branch: Root Cause leads to Security Invariant, then Searchable Pattern, which splits into Primitive-driven and Role-driven; both feed a Large Program Analysis Task that produces Variant Candidates, which feed a Verify step; that Verify loops back to Security Invariant.

A red dotted region labelled Verify encloses the analysis steps of both branches.

## Slide 29

## **2.6 Result**

Phone screenshot of a Gmail thread: message from `buganizer-sy…`, May 9, to `b-system+1027…`.

```text
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
(1) Severity Matrix: https://source.android.com/security/overview/updates-resources#severity

________________________________

component:  190951
status:  Assigned
reporter:  povcfe2sec@gmail.com
```

Three lines above `component:` are blurred out in the screenshot and cannot be read.

The sentence "published severity assessment matrix (1) it was rated as Critical severity and High quality." is boxed in red on the slide.

## Slide 30

- **THE MOTIVATION**

- **FROM N-DAY PATCHES TO VARIANTS**

- **DECONSTRUCTING THE ZERO-DAYS**

- **LIVE DEMO**

## Slide 31

# **3. DECONSTRUCTING THE ZERO-DAYS**

## Slide 32

## **3.1 Pin Lock Bypass(CVE)**

#### **`CVE-2025-48541`**

```text
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
index 8270d50a..ce4fdd6 100644
--- a/src/com/android/settings/biometrics/face/FaceSettings.java
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
```

## Slide 33

## **3.1 Pin Lock Bypass(CVE)**

#### **`CVE-2025-48541`**

```text
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
index 8270d50a..ce4fdd6 100644
--- a/src/com/android/settings/biometrics/face/FaceSettings.java
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
...
-        mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
+        if (callingPackage == null || !callingPackage.equals(activity.getPackageName())) {
+            // only allow these extras when called internally by Settings
+            mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
```

## Slide 34

## **3.1 Pin Lock Bypass(CVE)**

#### **`CVE-2025-48541`**

```text
diff --git a/src/com/android/settings/biometrics/face/FaceSettings.java b/src/com/android/settings/biometrics/face/FaceSettings.java
index 8270d50a..ce4fdd6 100644
--- a/src/com/android/settings/biometrics/face/FaceSettings.java
+++ b/src/com/android/settings/biometrics/face/FaceSettings.java
...
-        mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
-        mSensorId = getIntent().getIntExtra(BiometricEnrollBase.EXTRA_KEY_SENSOR_ID, -1);
-        mChallenge = getIntent().getLongExtra(BiometricEnrollBase.EXTRA_KEY_CHALLENGE, 0L);

-        mUserId = getActivity().getIntent().getIntExtra(
-                Intent.EXTRA_USER_ID, UserHandle.myUserId());
+        if (callingPackage == null || !callingPackage.equals(activity.getPackageName())) {
+            mUserId = UserHandle.myUserId();
+        } else {
+            // only allow these extras when called internally by Settings
+            mToken = getIntent().getByteArrayExtra(KEY_TOKEN);
+            mSensorId = getIntent().getIntExtra(BiometricEnrollBase.EXTRA_KEY_SENSOR_ID, -1);
+            mChallenge = getIntent().getLongExtra(BiometricEnrollBase.EXTRA_KEY_CHALLENGE, 0L);
```

## Slide 35

## **3.1 Pin Lock Bypass(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
--- a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
```

## Slide 36

## **3.1 Pin Lock Bypass(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
--- a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
+        mAllowInternalExtras = false;
+            if (TextUtils.equals(callingPackage, activity.getPackageName())) {
+                mAllowInternalExtras = true;
-        if (BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
+        if (mAllowInternalExtras && BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

## Slide 37

## **3.1 Pin Lock Bypass(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
--- a/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
+++ b/packages/apps/Settings/src/com/android/settings/biometrics/combination/BiometricsSettingsBase.java
     public void onAttach(Context context) {
-        mUserId = getActivity().getIntent().getIntExtra(Intent.EXTRA_USER_ID,
-                UserHandle.myUserId());
+        mUserId = UserHandle.myUserId();
+        mAllowInternalExtras = false;
+
+        if (context instanceof SettingsActivity) {
+            final SettingsActivity activity = (SettingsActivity) context;
+            final String callingPackage = activity.getInitialCallingPackage();
+            if (TextUtils.equals(callingPackage, activity.getPackageName())) {
+                mAllowInternalExtras = true;
+                mUserId = activity.getIntent().getIntExtra(Intent.EXTRA_USER_ID, mUserId);
...
-        if (BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
+        if (mAllowInternalExtras && BiometricUtils.containsGatekeeperPasswordHandle(getIntent())) {
```

## Slide 38

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```text
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
index 67219a5..45be472 100644
--- a/src/com/android/keychain/KeyChainActivity.java
+++ b/src/com/android/keychain/KeyChainActivity.java
```

## Slide 39

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```text
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
index 67219a5..45be472 100644
--- a/src/com/android/keychain/KeyChainActivity.java
+++ b/src/com/android/keychain/KeyChainActivity.java
             String hostMessage = String.format(res.getString(R.string.requesting_server),
-                                               uri.getAuthority());
+                    Uri.encode(uri.getAuthority(), "$,;:@&=+"));
```

## Slide 40

## **3.2 UI Obfuscation(CVE)**

#### **`CVE-2022-20230`**

```text
diff --git a/src/com/android/keychain/KeyChainActivity.java b/src/com/android/keychain/KeyChainActivity.java
index 67219a5..45be472 100644
--- a/src/com/android/keychain/KeyChainActivity.java
+++ b/src/com/android/keychain/KeyChainActivity.java
@@ -533,7 +533,7 @@
         Uri uri = getIntent().getParcelableExtra(KeyChain.EXTRA_URI);
         if (uri != null) {
             String hostMessage = String.format(res.getString(R.string.requesting_server),
-                                               uri.getAuthority());
+                    Uri.encode(uri.getAuthority(), "$,;:@&=+"));
             if (contextMessage == null) {
                 contextMessage = hostMessage;
             } else {
```

## Slide 41

## **3.2 UI Obfuscation(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java

diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
```

## Slide 42

## **3.2 UI Obfuscation(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java

-                    applicationInfo.loadLabel(getPackageManager())));
+                    applicationInfo.loadSafeLabel(getPackageManager())));
...
diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java

-                        applicationInfo.loadLabel(mPackageManager)));
+                        applicationInfo.loadSafeLabel(mPackageManager)));
```

## Slide 43

## **3.2 UI Obfuscation(Zero-Day)**

```text
diff --git a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
+++ b/packages/apps/Settings/src/com/android/settings/security/RequestManageCredentials.java
@@ -243,11 +243,11 @@ private void loadHeader() {
...
-                    applicationInfo.loadLabel(getPackageManager())));
+                    applicationInfo.loadSafeLabel(getPackageManager())));
...
diff --git a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
index 0000000..0000000 100644
--- a/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
+++ b/packages/apps/Settings/src/com/android/settings/security/CredentialManagementAppAdapter.java
@@ -84,11 +84,11 @@ public class HeaderViewHolder extends RecyclerView.ViewHolder {
mAppIconView.setImageDrawable(mPackageManager.getApplicationIcon(applicationInfo));
-                        applicationInfo.loadLabel(mPackageManager)));
+                        applicationInfo.loadSafeLabel(mPackageManager)));
```

## Slide 44

**4. LIVE DEMO**

## Slide 45

**Question: Will large language models replace security researchers?**

**Answer:**

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
