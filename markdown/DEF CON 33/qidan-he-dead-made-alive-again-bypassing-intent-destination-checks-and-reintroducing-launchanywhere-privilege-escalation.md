---
title: "Dead Made Alive Again Bypassing Intent Destination Checks and Reintroducing LaunchAnyWhere Privilege Escalation"
speakers: ["Qidan He"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Qidan He - Dead Made Alive Again Bypassing Intent Destination Checks and Reintroducing LaunchAnyWhere Privilege Escalation.pdf"
pages: 59
sha256: "2ef71d038802bc91b0b88526e0d8eab619ace0657c51ecb44b80c0370748dc25"
text_chars: 28759
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.4
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:11:23Z"
---
# Dead Made Alive Again Bypassing Intent Destination Checks and Reintroducing LaunchAnyWhere Privilege Escalation

**Speakers:** Qidan He  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Qidan He - Dead Made Alive Again Bypassing Intent Destination Checks and Reintroducing LaunchAnyWhere Privilege Escalation.pdf` (59 pages)


## Slide 1

Dead Made Alive Again: Bypassing Intent Destination Checks and Reintroducing LaunchAnyWhere Privilege Escalation

Qidan He DEFCON 33 Las Vegas, USA

## Slide 2

# About me

- Senior Director and Chief Security Researcher at JD.com

- Leading the Dawn Security Lab

   - Focusing on anti-fraud, client security, security research etc

- Winner of

   - Pwn2Own, Mobile Pwn2Own

   - Pwnie Award

- Speaker at

   - Black Hat, DEFCON, CanSecWest, RECon, PoC, HITB

## Slide 3

# Agenda

- Related Android Security Background

- Recap of LaunchAnyWhere Stories and Mitigations

- BadResolve: Make LaunchAnyWhere Great Again

- Unleashing the Power of LLM and MCP

- Summary

- QA

## Slide 4

Background Knowledge about Intents in Android

## Slide 5

# What is Intent

- Intents are the core of IPC mechanism in Android

   - Abstraction for messages sent within and between apps containing embedded data

   - Apps communicate with each other using (largely) Intents

## Slide 6

# Android App Components

- Components can be started by Intent (except Application) and receive input from it

- Components can declare Intent-filters in Manifest about expected Intents

   - Except dynamic broadcast-receiver – out of scope for this talk

   - *expected* means it’s not always enforced – only when in implicit intent resolving

## Slide 7

# Intent composition

- Intent objects use Bundle to store key-value pairs, including

   - Primitive data types, Arrays: intent.putExtra("defcon", "2025")

   - Objects implementing Serializable or Parcelable

- Object can define custom serialization scheme

- Intent itself implements Parcelable – which means intent can contains intent that contains intent that ….

   - So as Bundle

## Slide 8

# Intent Resolution

- Intents can be explicit or implicit

- Explicit intent’s target is deduced from the component set within it

- Implicit intent goes through resolution process, if no component is specified

• Currently in _com.android.server.pm.ResolveIntentHelper .resolveIntentInternal_

- Considers Intent-filter, permission, privilege, preferred options

   - Lots of details, we will go back to it later on

- Security Restrictions

startActivity(new Intent("android.intent.action.CALL_PRIVILEGED", Uri.parse("tel:911")));

<activity-alias android:name="PrivilegedCallActivity" android:targetActivity=".components.UserCallActivity" android:permission="android.permission.CALL_PRIVILEGED " android:exported="true" android:process=":ui"> <intent-filter android:priority="1000"> <action

android:name="android.intent.action.CALL_PRIVILEGED"/> <category android:name="android.intent.category.DEFAULT"/> <data android:scheme="tel"/> </intent-filter> ... </activity-alias>

public class UserCallActivity extends Activity implements TelecomSystem.Component {

@Override protected void onCreate(Bundle bundle) { //... Intent intent = getIntent(); verifyCallAction(intent);

## Slide 9

Recap of LaunchAnyWhere Stories of LaunchAnyWhere vulnerabilities

## Slide 10

# What is LaunchAnyWhere?

- Activity that can perform sensitive actions like install package, perform call or even execute command are usually protected with permission or is unexported – cannot be accessed by attacker

- Recall that Intent can contain nested Intent – which leads to _Intent Redirection/Injection_

Attacking App

Vulnerable App/Code

Victim App/Component

(usually protected)

Intent my_benign_attack_intent = new Intent(SECRET_PACKAGE, SECRET_PROTECTED_ACTIVITY); intent.putExtra("extra_intent", my_benign_attack_intent); startActivity(intent);

Intent whatABenignIntent = getIntent().getParcelableExtra("extra_intent"); startActivity(whatABenignIntent);

Intent intent = getIntent(); String secretCmdToRun = intent.getStringExtra("secret_cmd_to_run"); Runtime.getRuntime().exec(secretCmdToRun);

## Slide 11

# What is LaunchAnyWhere?

- System-uid applications are juicy targets

   - As it can be used to start arbitrary protected activity, regardless of permission, export status

- The primary goal is Settings (com.android.settings)

#### /** @hide

- Determines whether the given UID can access unexported components

- @param uid the calling UID

- @return true if the calling UID is ROOT or SYSTEM

- */

- public static boolean canAccessUnexportedComponents(int uid) { final int appId = UserHandle.getAppId(uid);

   - return (appId == Process.ROOT_UID || appId == Process.SYSTEM_UID);

}

//Called by resolveIntentInternal

## Slide 12

# Bug 7699048: where all the stories begin

public Bundle addAccount(AccountAuthenticatorResponse response, String accountType, String authTokenType, String[] requiredFeatures, Bundle options) { Intent intent = new Intent(); intent.setComponent(new ComponentName(

"com.trick.trick ", " com.trick.

trick.AnyWhereActivity"));

intent.setAction(Intent.ACTION_RUN); intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK); final Bundle bundle = new Bundle(); bundle.putParcelable(AccountManager.KEY_INTENT,

intent);

return bundle;

}

/** Handles the responses from the AccountManager */ private class Response extends IAccountManagerResponse.Stub {

public void onResult(Bundle bundle) {

Intent intent =

bundle.getParcelable(KEY_INTENT);

if (intent != null && mActivity != null) {

// since the user provided an Activity we will silently start intents

// that we see mActivity.startActivity(intent);

// leave the Future running to wait for the real response to this request

- } else if (bundle.getBoolean("retry")) {

## Slide 13

# Bug 7699048: the first round of fix

+ @Override public void onResult(Bundle result) { mNumResults++; - if (result != null && !TextUtils.isEmpty(result.getString(AccountManager.KEY_AUTHTOKEN))) { + Intent intent = null; + if (result != null + && (intent = result.getParcelable(AccountManager.KEY_INTENT)) != null) { + /* + * The Authenticator API allows third party authenticators to + * supply arbitrary intents to other apps that they can run, + * this can be very bad when those apps are in the system like + * the System Settings. + */ + PackageManager pm = mContext.getPackageManager(); + ResolveInfo resolveInfo = pm.resolveActivity(intent, 0); + int targetUid = resolveInfo.activityInfo.applicationInfo.uid; + int authenticatorUid = Binder.getCallingUid(); + if (PackageManager.SIGNATURE_MATCH != + pm.checkSignatures(authenticatorUid, targetUid)) { + throw new SecurityException( + "Activity to be started with KEY_INTENT must " + + "share Authenticator's signatures"); + } + } + if (result != null + && !TextUtils.isEmpty(result.getString(AccountManager.KEY_AUTHTOKEN))) {

Perform a resolve on the incoming Intent to make sure the target Activity this Intent will resolve to is in the same Application as calling Application (i.e. attacker application)

## Slide 14

# Bug 7699048: the first round of fix

AccountManagerService (system_server) Settings (com.android.settings)
checkKeyIntent startActivity
Bundle (contains a malicious Intent)
Attacker Application (Calling Application)
addAccount

## Slide 15

# … and now transformed into

/**

- Checks Intents, supplied via KEY_INTENT, to make sure that they don't violate our * security policy.

*

- In particular we want to make sure that the Authenticator doesn't try to trick users

- into launching arbitrary intents on the device via by tricking to click authenticator

* supplied entries in the system Settings app. */

protected boolean checkKeyIntent(int authUid, Bundle bundle) { //... Intent intent = bundle.getParcelable(AccountManager.KEY_INTENT, Intent.class); try { PackageManager pm = mContext.getPackageManager(); ResolveInfo resolveInfo = pm.resolveActivityAsUser(intent, 0, mAccounts.userId); //...

ActivityInfo targetActivityInfo = resolveInfo.activityInfo; int targetUid = targetActivityInfo.applicationInfo.uid;

PackageManagerInternal pmi = LocalServices.getService(PackageManagerInternal.class); if (!isExportedSystemActivity(targetActivityInfo)

&& !pmi.hasSignatureCapability(targetUid, authUid, CertCapabilities.AUTH)) { String pkgName = targetActivityInfo.packageName; String activityName = targetActivityInfo.name; String tmpl = "KEY_INTENT resolved to an Activity (%s) in a package (%s) that " + "does not share a signature with the supplying authenticator (%s)."; Log.e(TAG, String.format(tmpl, activityName, pkgName, mAccountType)); return false; }

//...

## Slide 16

# Round 1 finished?

• Round 2!

## Slide 17

What if AccountManagerService (system_server) sees different Intent as Settings?

## Slide 18

# Round 2: Parcel Mismatch

- Recall that Bundle can contain Parcelable objects

   - And it’s developers’ responsibility to write pack & unpack code

   - Things usually go wrong here: e.g. com.samsung.android.knox.ucm.configurator.CACertificateInfo

**private void** readFromParcel( **Parcel** in) { this.bundle = (Bundle)in.readParcelable(Bundle.class.getCl assLoader()); **int** v0 = in.readInt(); this.certLength = v0; if(v0 > 0) { **byte** [] v0_1 = new **byte** [v0]; this.certificate = v0_1; in.readByteArray(v0_1); }

}

@ **Override** _// android.os.Parcelable_ **public void** writeToParcel( **Parcel** dest, **int** flag) { if(dest != null) { dest.writeParcelable(this.bundle, flag); dest.writeInt(this.certLength); if(this.certLength != 0) { dest.writeByteArray(this.certifi cate); } } }

## Slide 19

# Parcel mismatch: the nightmare of 100+ vulnerabilities

- Given a certLength=-1, mismatch will occur when Parcel is written and then read

- Bundle contains different object after deserialize and serialize and then deserialize again

   - Which bypasses the _checkKeyIntent_ check

   - System_server and Settings actually see different Intent! Which of course will lead to different resolve result

- The detail is quite complex – will not elaborate here due to not quite relevant to today’s talk

   - For anyone who’s interested, the next slide gives an overview

   - Largely exploited in the wild

## Slide 20

*Taken from Hao Ke’s BH EU22 slide


> Recovered by OCR — confidence 92/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bundle “FengShu
- Self changing Bundle: Exploits
system_server
AccountManagerService
4. Serializes account Bundle
includes a {KEY_INTENT:good_intent} entry
5. "Sure, here is my account": return Bundle
*Taken from Hao Ke’s BH EU22 slide
Deserialization: Bundle {KEY_INTENT: good_intent} <
Settings App
6. "Let me check this Bundle"
checkKeyintent(bundle)
Found: KEY_INTENT - Good Intent, check passed
7. "Here is the Bundle for adding an account"
onResult(bundle)
system_server
AccountManagerService
Diffe
rent!
```

## Slide 21

BadResolve(s) What if AccountManagerService (system_server) and Settings see same Intent, but the intent resolve to different target Activities? Make LaunchAnyWhere Great Again

## Slide 22

# Looking back into the fix

protected boolean checkKeyIntent(int authUid, Bundle bundle) { if (!checkKeyIntentParceledCorrectly(bundle)) { EventLog.writeEvent(0x534e4554, "250588548", authUid, ""); return false; }

Intent intent = bundle.getParcelable(AccountManager.KEY_INTENT, Intent.class); //... PackageManager pm = mContext.getPackageManager(); ResolveInfo resolveInfo = pm.resolveActivityAsUser(intent, 0, mAccounts.userId); //... ActivityInfo targetActivityInfo = resolveInfo.activityInfo; int targetUid = targetActivityInfo.applicationInfo.uid; PackageManagerInternal pmi = LocalServices.getService(PackageManagerInternal.class); if (!isExportedSystemActivity(targetActivityInfo)

&& !pmi.hasSignatureCapability(targetUid, authUid, CertCapabilities.AUTH)) { String pkgName = targetActivityInfo.packageName; String activityName = targetActivityInfo.name; String tmpl = "KEY_INTENT resolved to an Activity (%s) in a package (%s) that " + "does not share a signature with the supplying authenticator (%s)."; Log.e(TAG, String.format(tmpl, activityName, pkgName, mAccountType)); return false;

}

bundle.putParcelable(AccountManager.KEY_INTENT, intent);

## Slide 23

# TOCTOU comes to rescue

- The core idea is check the target using _resolveActivity_ in system_server, and send it to Settings if check passed then start

- _startActivity_ implicitly calls _resolveActivity_ internally

- What if the result changed between these resolves? Possible for race?

- Inspect the source to figure out anything to manipulate

AccountManagerService (system_server) Settings (com.android.settings)
checkKeyIntent startActivity
resolveActivity resolveActivity
Activity Activity Protected or Privileged Activity Attacker wants to start
(of calling App which passes check)

Activity
(of calling App which passes check)

## Slide 24

# TOCTOU: changing component state

- Primitive: Application is allowed to use

_PackageManager.setComponentEnabledSetting_ to enable or disable its own component (activity etc) in runtime. A disabled component is considered to be vanished (as if does not exist)

- Idea: can we utilize this primitive to manipulate results? For example, can we disable the result component in former resolve (the check round) to force the latter resolve point to different result?

AccountManagerService (system_server) Settings (com.android.settings)
checkKeyIntent startActivity
resolveActivity resolveActivity
Activity (of calling App which passes check) Activity Protected or Privileged Activity Attacker wants to start

(of calling App which passes check)

## Slide 25

# TOCTOU: feasibility check

- Intent may resolve to a single target or multiple targets – Activity can declare similar Intent-filters

- When intent resolves to single target, if the target is disabled, the process fails and exception is thrown

   - Explicit intent always resolve to single target (explicit means component/class set)

   - Implicit intent may resolve to single target (if only one fit)

AccountManagerService (system_server) Settings (com.android.settings)
checkKeyIntent startActivity
resolveActivity resolveActivity
Activity
(of calling App which passes check)

## Slide 26

TOCTOU: feasibility check

Clicking on chooser item and click Always will mark an Activity as Preferred


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOCTOU: feasibility check
a Single result >| Return
Intent starts resolving Ne Return the highest priority target
Do targets have different
Ny multiple found /Excluding out Disabled Ones—> 9 am Return the Preferred target
priorities with one highest?
—~No—> Is there a Preferred target?
Return the ChooserActivity
from Resolver, let user decide
r >
Complete action using we
No—>
<x) Settings
TestContentBug Clicking on chooser item and click Always
AttackActivity will mark an Activity as Preferred
```

## Slide 27

# TOCTOU: feasibility check

- When Intent resolves to multiple targets (only implicit intents will)

   - Disabled targets won’t be taken into consideration

   - ~~Try to choose one with Largest Priority, and return it~~

   - Try to choose a Preferred One, and return it

   - ~~If neither satisfied, a Chooser Dialog (ChooserActivity) is poped up for user confirmation (ChooserActivity is returned)~~

      - ~~If Always is clicked for a target, that target is marked as Preferred (survives app update)~~

- checkKeyIntent is not happy with Chooser

- Priority is ignored for non-system app

- Make           a preferred one!Activity

## Slide 28

# TOCTOU: Feasible!

Do Disable
AccountManagerService (system_server) Settings (com.android.settings)
checkKeyIntent startActivity
resolveActivity resolveActivity
Activity Activity Activity
(of calling App which passes check)
Preferred

## Slide 29

# Perfetto View

checkKeyIntent call 1 checkKeyIntent call 2

startActivity

*Note actually two calls to checkKeyIntent are performed

## Slide 30

Just race within this time window and we are good to go


> Recovered by OCR — confidence 93/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
resolvelntent unbindService resolvelntent
Y
Just race within this time window and we are good to go
```

## Slide 31


> Recovered by OCR — confidence 74/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
30:00:02 00:00:02 00:00:02 0:00 00:0 00:00:0 10:00
169 000 001 9 500 ( 000 000 150 (
resolvelntent unbindService
queryintentActiv... unbindServiceLocke...
updateOomA..
quer..
launchingActivity#2
470 500 OO 471 000 OO! 471 500 Of
1ms 331us 960ns
\2 00:00:02
) OOF 469 500 000
531us |
queryintentActiv...
```

## Slide 32

# Need to get a larger window… which direction?

Slow down _resolveIntent_ ? And disable component in this time frame? However, if the disable is instantly reflected in resolve result, we still fail

Slow down IPC between _system_server_ & Settings And disable component in this time frame?

## Slide 33

# TOCTOU: diving deeper into resolveIntent

- Component information query is fulfilled by _ComponentResolver_ in _PackageManagerService_

   - Maintains mappings of {Activity, Service, BroadcastReceiver, ContentProvider}s and intent-filters, etc

      - Stores information in fields -> _ActivityIntentResolver, ProviderIntentResolver, ReceiverIntentResolver, ServiceIntentResolver_

- _ComputerEngine.mComponentResolver_ is snapshot of _ComponentResolver_ , fetched/updated when _PackageManagerInternalBase.resolveIntent_ is called

ResolveIntentHelper.resolveIntentInternal

ComputerEngine.queryIn ResolveIntentHelper.cho
tentActivitiesInternal oseBestActivity

ComponentResolver(Api).queryActivities

- Queries are performed on _ComponentResolverSnapshot_ (snapshot actually creates copies of the big 4)

## Slide 34

# Snapshot in PackageManagerService

- _Snapshot_ creates a read-only current state copy of Package infos

- Queries are done on a *frozen* component mappings and states

- • Any changes during the time frame of _resolveIntent_ will not be taken into consideration

## Slide 35

# TOCTOU: extending race window

- An idea is to figure out ways to extend time spend on search

   - Play with manifests

      - Lots of components?

      - Lots of attributes?

      - Lots of intent-filters?

         - Lots of elements?

## Slide 36

# TOCTOU: extending race window

## • FLAG_DEBUG_LOG_RESOLUTION and large number of categories

final boolean debug = localLOGV || ((intent.getFlags() & Intent.FLAG_DEBUG_LOG_RESOLUTION) != 0);

match = intentFilter.match(action, resolvedType, scheme, data, categories, TAG); if (match >= 0) {

if (debug) Slog.v(TAG, " Filter matched! match=0x" + Integer.toHexString(match) + " hasDefault="

//..

if (oneResult != null) { dest.add(oneResult); if (debug) { dumpFilter(logPrintWriter, " ", filter); logPrintWriter.flush(); intentFilter.dump(logPrinter, " "); }

}

} else { hasNonDefaults = true; }

IntentFilter:

public void dump(Printer du, String prefix) { StringBuilder sb = new StringBuilder(256); if (mActions.size() > 0) { Iterator<String> it = mActions.iterator(); while (it.hasNext()) { sb.setLength(0); sb.append(prefix); sb.append("Action: \""); sb.append(it.next()); sb.append("\""); du.println(sb.toString());

}

} if (mCategories != null) { Iterator<String> it = mCategories.iterator(); while (it.hasNext()) { sb.setLength(0); sb.append(prefix); sb.append("Category: \""); sb.append(it.next()); sb.append("\""); du.println(sb.toString());

}

}

## Slide 37

# TOCTOU: extending race window

- Declare intent-filters with large number of categories

• The upper bound is limited by the timeout restriction of _PackageManager.packageVerification_ and AndroidManifest XML format • Anyway 10499-39999 is small enough to make both happy

- And slows down resolveIntent to (50, 400+) ms

<activity android:name=".MainActivity3" android:label="AttackActivity" android:exported="true"> <intent-filter>

<action android:name="android.settings.TRAMPOLINE" />

- <category android:name="android.intent.category.DEFAULT" />

<category android:name="android.intent.category.DEFAULT.1" />

- <category android:name="android.intent.category.DEFAULT.29999" />

- </intent-filter>

</activity>

## Slide 38

# Final outcome

thread to disable comp
Trigger AddAccount
Attacker App
System_serverSettings
First check Second
Check
Settings

Actual Use


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Final outcome
|
Trigger AddAccount
thread to disable comp
03:22:09 + 00:00:01 00:00:01 00:00:01 00:00:01 00:00:02
696 309 266 200 000 000 400 000 000 600 000 000 800 000 000 000 000 000
x = Y Default Workspace vi v
Thread 16228 (main thread)
Thread 1538 x | | resolvelntent resolvelntent | |
| |
A
aunchingActivity#77 . Check
launchingActivity#78 settings,
Actual Use
```

## Slide 39

# TOCTOU: Unhappy SystemUI

- _SystemUI_ crashes on clicking ResolveActivity’s dialog

   - Due to too large body of Intent-filter (> 10499)

- Reinstall the application can bypass this restriction (installing update to application will not clear _PreferredActivity_ preference)

   - Install normal version exploit application, trigger Resolve and made Attacker’s Activity PreferredActivity

   - Install an update to the exploit application with large number of categories

   - Trigger the vulnerability

- Actually not mandatory

## Slide 40

# Bridging via SearchTrampolineActivity

\```
@Override
\```

- This vulnerability

   - Require target component to have intent-filter with category default and an action string

   - Need a gadget to extend it

- We are allowed to call _SearchTrampolineActivity_ , with controllable intent parameter

   - Phone call, install package, etc..

\```
protectedvoidonCreate(BundlesavedInstanceState) {
finalStringcallerPackage=getLaunchedFromPackage();
// First make sure caller has privilege to launch a
search result page.
FeatureFactory.getFeatureFactory()
.getSearchFeatureProvider()
.verifyLaunchSearchResultPageCaller(this,
callerPackage);
\```

\```
Intentintent=getIntent();
//...
\```

\```
} else{
\```

\```
// Direct link case
\```

\```
finalStringintentUriString=intent.getStringExtra(
Settings.EXTRA_SETTINGS_EMBEDDED_DEEP_LINK_INTENT_URI);
//...
\```

\```
intent =Intent.parseUri(intentUriString,
Intent.URI_INTENT_SCHEME);
intent.setData(data);
//...
\```

\```
intent.addFlags(Intent.FLAG_ACTIVITY_FORWARD_RESULT);
startActivity(intent);
\```

## Slide 41

# TOCTOU: FIX

• Make implicit intent an explicit one

• setComponent or setPackage


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TOCTOU: FIX
¢ Make implicit intent an explicit one
* setComponent or setPackage
@@ -5062,6 +5062,8 @@
Log.e(TAG, String.format(tmpl, activityName, pkgName, mAccountType) );
return false;
}
+ intent.setComponent (targetActivityInfo. getComponentName () ) ;
+ bundle. putParcelable(AccountManager.KEY_INTENT, intent) ;
return true;
} finally {
```

## Slide 42

# TOCTOU: digging further

- Any code snippet that calls _startActivity_ on Intent after checking resolve result can be vulnerable

- The previously discussed issue is already fixed, with 4 other code snippets in AOSP are found to have similar vulnerability and reported to Google

   - CVE-2025-32321, CVE-2025-8192

## Slide 43

# Exploitation Technique

- Key parameter here is the timeout before disabling component

   - Varies on high-end and low-end devices, e.g. on Pixel 7Pro it’s ~390ms, Galaxy S21 is 1 second

- We can continuously retry until succeed

## Slide 44

# DEMO

(for modifying lock password)


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DEMO
(for modifying lock password)
55090 0
Trigger Resolve
Trigger AddAccount Step 1
Trigger AddAccount Step 2
Disable/Enable AttackActivity
Disable/Enable PlaceHolderActivity
```

## Slide 45

### DEMO

Android 16 Beta3 For calling arbitrary number


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
submission2-3 python3 test_exp.py ) ( Pixel 7 Pro
pinitializing environment...
eaning up restricted users...
rrent users: Users: 1088 © OS 4 -
UserInfo{@:Owner:4c13} running
bund restricted user with ID: 27
iccessfully removed user with ID 27
Android version
Android version
16
Android security update
April 5, 2025
DEMO Google Play system update
Android 16 Beta3 May 1, 2025
For calling arbitrary Baseband version
g5300q-2503. 0402-B-13303902,g5300q-250320-
number 250402-B-13303902
Kernel version
6.1.124-android14-11-g8d713f9e8e7b-ab13202960
#1 Wed Mar 3:40:07 UTC 2025
Build number
BP22.250325.007
```

## Slide 46

# Going even further

- Problem with _SearchTrampolineActivity_

   - _parseUri_ does not support parcelable inside

   - Code modified/removed on some vendors

- _ChooserActivity_ comes to rescue!

   - Who draws a parcelable from Intent and starts it

**public class** SearchResultTrampoline **extends** k { @Override // android.app.Activity **protected void** onCreate(Bundle bundle0) { Intent intent0 = **this** .getIntent();

**try** {

String s =

intent0.getStringExtra( **":settings:fragment_args_key"** ); Bundle bundle1 = **new** Bundle();

bundle1.putString( **":settings:fragment_args_key"** , s); intent0.putExtra( **":settings:show_fragment_args"** , bundle1); }

intent0.setClass( **this** , SubSettings. _class_ ).addFlags( **0x2000000** ); AmsUtils.startActivity( **this** , intent0);

## Slide 47

# Going even further

- _ChooserActivity_ takes an _EXTRA_INTENT_ from input and launches it (using _startActivityAsCaller_ )

- AOSP version of _ChooserActivity_ has a priority of 500, which is not applicable as BadResolve’s target

- Vendor tends to implement their own version of XXChoooser

   - Mimic the official ChooserActivity

   - With no priority specified!

|**VENDOR**|**Trampoline**
**Gadget**|**Custom**
**Gadget**|
|---|---|---|
||**Available?**|**Available?**|
|AOSP|YES|NO|
|HONOR|NO|YES|
|SAMSUNG|YES|NO|
|HXXWEI|NO|YES|
|XIAOMI|YES|YES|

- Question: does XXChooser verify its targets?

   - Yes, but not enough

## Slide 48

# Chaining startActivityAsCaller

Attacker App’s
Attacker App ChooserActivi
ResolverActivity/ChooserActivity
ty
BadResolve
Verifies caller has permission
ResolverListController
to start target
MixxChoo
Settings
serActivity
startActivity
filterIneligibleActivities
startActivity
EXTRA_INTENT
AsCaller
checkComponentPermission
Victim
Activity

## Slide 49

# Different XXChooser Implementations

- Some vendors’ _XXChooserActivity (subclass of XXResolverActivity)_ verifies _mLaunchedFromUid(caller)_ has permission to start the target and the target needs to be exported

- Additional hop is needed

getParcelableExtra
"android.intent.extra.INTENT"
startActivityAsCaller
getInfoFromIntents filterOrigResolveInfos startActivityOrPrivacy
filterNoPermissionReso
filterNoExportedInfos
lveInfos

## Slide 50

# Chaining startActivityAsCaller

Attacker App’s Attacker App ChooserActivi ty Verifies caller has permission BadResolve to start target XXChooser ChooserAc Victim Settings Activity tivity Activity startActivity startActivity startActivityAsCaller AsCaller • Verifies caller has permission to start target • Verifies target is exported

## Slide 51

Unleashing LLM How LLM can be used for finding these kind of bugs

## Slide 52

# Working with LLM

Prompt for fetching possibly vulnerable code

Manager Agent Prompt for checking if code is vulnerable Vote Vote

Prompt for checking if code is vulnerable

Auditor Agent

Auditor Agent Double check prompt

Reviewer Agent

AOSP MCP Codebase

CodeQL, Filesystem Search for API, decompile/retrieve code, retrieve caller/callee

Vendor
MCP Codebase
JEB, Filesystem

JEB, Filesystem

_https://github.com/flankerhqd/jebmcp_

## Slide 53

# Working with MCP

- LLM of course cannot directly consume all the AOSP code base

- Search for APIs

_resolveActivity,resolveActivityAsUser,queryIntentActivities,queryIntent ActivitiesAsUser_

   - Feed function and enclosing classes into LLM

- Different MCPs are used

   - CodeQL for AOSP

   - JEB for closed-source vendor code

## Slide 54

# Prompt

Background: You are required to determine whether the provided source code contains a specific type of vulnerability, based on a given vulnerability description, and explain the reason.

Input Format: The input is in JSON format, structured as follows: {"inputId": "1", "inputSource": "source code"}

Output Format: Your output must be returned in JSON format as: …, provide your reason in `reason` field Task: You are now an Android code security auditing expert. In the following conversations, I will provide Java or Kotlin code. Your task is to audit the code and determine whether it contains an Intent Resolve TOCTOU vulnerability.

## Slide 55

# Prompt

Vulnerability Example: A Time-of-Check to Time-of-Use vulnerability may occur when the resolved component of an Intent is checked for security, but the actual start of the activity is delayed, allowing an attacker to tamper with the target. For example, the following code snippet is considered vulnerable: ResolveInfo ri = pm.resolveActivityAsUser(intent, ...);

if (isSafe(ri)) {

context.startActivity(intent); // <-- TOCTOU window

}

Also, consider the following real-world vulnerability example of same kind. //…

To avoid false positives, DO NOT consider it vulnerable if:

The intent explicitly sets a target component using setPackage, setComponent, or setClass – even if there's a time window between resolve and start

The intent is constructed with or sets an explicit action (via constructor or setAction) The resolved Intent is not passed to startActivity, startActivityForResult, etc.

## Slide 56

# Observations

- Tested on Deepseek-(v3,r1) and GPT-(4o,o1-mini,o1)

   - Low false-negatives, but a few false positives

      - Hallucination on whether the intent is used to startActivity

      - Lack of knowledge for some tricky details of Android Security (Intent internals)

      - Lazy on querying call graph

- Reasoning model gives less false-positive

- Found 1 additional bug (precision 4/20, recall 4/5)

- Additional work needed

## Slide 57

Conclusion

## Slide 58

# QA

- Refs & Credits

   - https://i.blackhat.com/EU-22/Wednesday-Briefings/EU-22-Ke-AndroidParcels-Introducing-Android-Safer-Parcel.pdf

   - <u>https://blog.canyie.top/2024/11/07/self-changing-data-type/</u>

   - Moyu from Dawn Security Lab (@bin_20000s)

- Follow future research at

   - @flanker_hqd, https://blog.flanker017.me

   - @dawnseclab, https://dawnslab.jd.com

## Slide 59

Thanks
