---
title: "SystemUI As EvilPiP The Hijacking Attacks on Modern Mobile Devices"
speakers: ["WeiMin Cheng", "Yue Liu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/WeiMin Cheng & Yue Liu-SystemUI As EvilPiP The Hijacking Attacks on Modern Mobile Devices.pdf"
pages: 79
sha256: "77165163a30cd8e35802825f0280fcf10950771e185ae5a72d3a8579b8c50266"
text_chars: 21070
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:52:59Z"
---
# SystemUI As EvilPiP The Hijacking Attacks on Modern Mobile Devices

**Speakers:** WeiMin Cheng, Yue Liu  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/WeiMin Cheng & Yue Liu-SystemUI As EvilPiP The Hijacking Attacks on Modern Mobile Devices.pdf` (79 pages)


## Slide 1

## SystemUI As EvilPiP **The Hijacking Attacks on Modern Mobile Device**

WeiMin Cheng(mgaldys4@gmail.com)

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ASIA i a
* I-18-19, 2024 Vi
a BRIEFINGS _
 ” SystemUI As EvilPiP
The Hijacking Attacks on Modern Mobile Device
WeiMin Cheng(mgaldys4@gmail.com)
#BHASIA @BlackHatEvents
```

## Slide 2

###### WhoAreWe

WeiMin Cheng QI-ANXIN Github: MG1937 Twitter: MGAldys4 Mobile&AOSP

Yue Liu QI-ANXIN Github: lieanu Binary Researcher

# BHASIA @BlackHatEvents

## Slide 3

##### Agenda

- **What is Activity Hijack Attack (AHA)**

- **Restrictions and Policies released by Google**

- **Bypass Security Policies**

   - BAL Restriction

   - Runtime State Leak

   - Strictly LMKD

- **Video Demo for Fullchain**

# BHASIA @BlackHatEvents

## Slide 4

###### What is AHA

- Activity Hijack Attack(AHA) almost zero cost and easy to exploit

- • Hijack target app for stealing sensitive data or runtime privilege

- Adware, BankBot, Ransomware, Rat…

# BHASIA @BlackHatEvents

## Slide 5

###### How AHA Work

- Take Android4.0 as an example

- Case of Simplocker, malware for Android4.0

- Essence is abuse NEW_TASK FLAG to seize FG Task

Code snippet of Simplocker

# BHASIA @BlackHatEvents

## Slide 6

###### How AHA Work

- Malicouse Activity enter FG Task

- Previous Task pushed to BG Task

- Now Malware can forge the trusted App, StrandHogg-like Hijack scheme

- **Why have to seize FG Task for hijack?**

# BHASIA @BlackHatEvents

## Slide 7

###### Task And Back-Stack

- Task Stack is a collection of activities

- User can only interact with ONE Front Task (in most case)

# BHASIA @BlackHatEvents

## Slide 8

###### Classic Attack Scheme

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Classic Attack Scheme
EBank \
, EBank
7 Splash Page
Leak Running State
ou A
Background Target Detecter
```

## Slide 9

###### Classic Attack Scheme

**Low cost, high return Almost affects all App in Old Device**

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Classic Attack Scheme
EBank \
Fake
| EBank Login
th
Low cost, high return
Almost affects all App in Old Device
startActivi a
Intent#FLAG_ACTIVITY_NEW_TASK
oo»
. Background Target Detecter
```

## Slide 10

###### Key Factors OF AHA

- Background Activity Launch (BAL)

- Target Running State Detect

- Background Persistent Processaaass

# BHASIA @BlackHatEvents

## Slide 11

#### Google will not allow this happen

# BHASIA @BlackHatEvents

## Slide 12

###### Restriction 0x1 No Leak State

- getRunningTasks || getRunningAppProcesses requires no permission

- • Leak runtime state of other app by special interface **before API22** • **Only Return Caller’s Data in API>=22**

Get all running Task and Process

# BHASIA @BlackHatEvents

## Slide 13

###### Restriction 0x1 No Leak State

- Still have side-channel way to bypass in **API<26**

- cat /proc/{target_pid}/oom_score_adj

- Work for non-privilege user!

# BHASIA @BlackHatEvents

## Slide 14

###### Restriction 0x1 No Leak State

- Google update SELinux Policy in 2017

- **Hidepid=2 like protections**

- **Restrict App access file in non-AppDomain**

hidepid in man7 Doc

# BHASIA @BlackHatEvents

## Slide 15

###### Compromise Scheme

- Case of MysteryBot

- Turn to UsageStatsManager for leak runtime state indirectly

- Dangerous Runtime Permission required

- Complex User Interaction

- **Some ROM force warn when grant!**

# BHASIA @BlackHatEvents

## Slide 16

###### Restriction 0x2 No BAL

API29+ App without privilege can’t start Activity from Background No BAL == can’t inject target from Background Most Adware && Hijackware disppeared due to this

https://developer.android.com/guide/components/activities/background-starts

# BHASIA @BlackHatEvents

## Slide 17

###### Compromise Scheme

- Turn to AccessibilityService||SystemServices||SAW permission

   - Complex User Interaction&&Dangerous Runtime Permission

- Satisfy BAL Restriction Exemptions in document • Requires System System Bind… • Requires Visible App Bind…

   - Requires Holds System Privilege…

   - Almost impossible…

# BHASIA @BlackHatEvents

## Slide 18

###### Restriction 0x3 BEL&&LMKD

- Background Service in **API26+** get **High OOM_ADJ&&Low Priority!**

- • BgProcess == IDLE Process, LMKD kill idle process first

- System Broadcast Trick BANNED in API24+!

https://developer.android.com/about/versions/oreo/background

# BHASIA @BlackHatEvents

## Slide 19

Compromise Scheme Compromise scheme provided by Google Start Foreground Service For Low OOM_ADJ

- Have to notify User, no silent process

- 3rd ROM even not allow FgService long time running

# BHASIA @BlackHatEvents

## Slide 20

###### But, Compromise Scheme Really Work?

- Grant dangerous permission → Complex User Interaction

- No Silent Running → Awared by user

- Case Of Xiaomi OS, even no persistently process

- High attack cost, highly user detectable → Attack failed

When #removeTask AOSP will call #isProcStateBackground MIUI directly call forceStop to all process.

framework.jar smali code of MIUI OS

# BHASIA @BlackHatEvents

## Slide 21

###### So, Any Way To Bypass?

- No Permission required

- • Undetectable

- Hijack precisely

• Attack High Version Device

# BHASIA @BlackHatEvents

## Slide 22

### 1<sup>st</sup> High Wall: BAL Restriction

# BHASIA @BlackHatEvents

## Slide 23

###### Analyse BAL Restriction

```
Activity#startActivity
```

Handled By ActivityManagerService(AMS)

```
ActivityStarter#executeRequest
```

API33

# BHASIA @BlackHatEvents

## Slide 24

Analyse BAL Restriction System try to start target component

restrictedBgActivity

**Decide whether to move Task to front**

```
ActivityStarter#setInitialState
```

determines

moveToFront Still needs to focus on check func and Bypass it.

```
ActivityStarter#startActivityInner
```

# BHASIA @BlackHatEvents

## Slide 25

###### Analyse BAL Restriction

**Developer Doc give some exemption for check func**

How to define ‘visible window’?

shouldAbortBackgroundActivityStart(shouldABAS)

# BHASIA @BlackHatEvents

## Slide 26

###### Analyse BAL Restriction

**Developer Doc give some exemption for check func**

How to define ‘visible window’?

hasActiviteVisibleWindow

# BHASIA @BlackHatEvents

## Slide 27

###### Analyse BAL Restriction

WindowState#onSurfaceShownChanged

mNumNonAppVisibleWindowMap

Inside hasNonAppVisibleWindow

# BHASIA @BlackHatEvents

## Slide 28

###### Window Type&&Z-Axis

WindowToken#addWindow

WindowState#<init>

WindowComparator compare BaseLayer value

Window Type decides mBaseLayer Which decides Z-axis indirectly **Higher BaseLayer, Higher Z-axis**

getWindowLayerFromTypeLw

# BHASIA @BlackHatEvents

## Slide 29

###### Visible Window

hasNonAppVisibleWindow

- Window Type > FIRST_SYSTEM_WINDOW && != TYPE_TOAST

Non-Privilege App usually gets BASE_APPLICATION window Almost invisible in most time

TYPE_APPLICATION_OVERLAY = FIRST_SYSTEM_WINDOW + 38 ;

Non-Privilege App can only get a “system” window with TYPE_APPLICATION_OVERLAY

**But requires SYSTEM_ALERT_WINDOW permission Which needs complex user interact!**

# BHASIA @BlackHatEvents

## Slide 30

###### What is Picture-in-Picture

- Non-SAW Permission float-window compromise scheme for developer

- Pinned Activity in PiP window at the top of screen

- Handled by SystemUI Component

- Window Type > FIRST_SYSTEM_WINDOW and Permission-less

# BHASIA @BlackHatEvents

## Slide 31

###### What is Picture-in-Picture

- Non-SAW Permission float-window compromise scheme for developer

- Pinned Activity in PiP window at the top of screen

- Handled by SystemUI Component

- Window Type > FIRST_SYSTEM_WINDOW and Permission-less

# BHASIA @BlackHatEvents

## Slide 32

###### What is Picture-in-Picture

Unable to abuse PiP directly

- Pip window can’t hide from screen

- Pinned Activity can be detected by User(Even use transparent theme)

- User can remove PiP window at any time

- PiP is highly detectable feature!

# BHASIA @BlackHatEvents

## Slide 33

CVE-2021-0485 By valsamaras Invalid Input for a abnormal PiP Window Visible for System, But Invisible for User

Abnormal 1 pixel PiP window Almost invisible

Sets abnormal height and width

# BHASIA @BlackHatEvents

## Slide 34

###### CVE-2021-0485 By valsamaras

PipBoundsAlgorithm Patch

###### <u>aad7fdc4f82ad56e332d3c23c5d07719e069b099</u>

# BHASIA @BlackHatEvents

## Slide 35

###### New Attack Surface

###### **Nice bug expanding Attack Surface**

- No need to bypass Window Visible Check(Abuse PiP)

- Create a legal System Window but User undetectable

- Abuse PiP API by abnormal input

# BHASIA @BlackHatEvents

## Slide 36

###### How PiP Work

ATMS#enterPictureInPictureMode

RootWindowContainer#moveActivityToPinnedRootTask

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
How PiP Work
ATMS#enterPicturelnPictureMode YJ
RootWindowContainer#moveActivity ToPinnedRootTask
rootTask. setwindowingMode(WINDOWING MODE PINNED);
ff Set the launch bounds tor launch-into-pip Activity on the root task.
if (r.getOptions() != null && r.getOptions(}).isLaunchIntoPip()) {
// Record the snapshot now, it will be later fetched for content-pip animation.
// We do this early in the process to make sure the right snapshot is used for
// entering content-pip animation.
mwindowManager .mTaskSnapshotController.recordTaskSnapshot(
task, false /* allowSnapshotHome */);
rootTask. setBounds(r.petOptions( ).getLaunchBounds( ));
t
rootTask. setDeferTaskAppear( false);
```

## Slide 37

###### How PiP Work

IPC

Task#sendTaskAppear

ShellTaskOrganizer#onTaskAppeared

**com.android.systemui** Pip rendered here

PipTaskOrganizer#onTaskAppeared

# BHASIA @BlackHatEvents

## Slide 38

###### How PiP Work

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
How PiP Work
AppLayer System_Server SystemUl
Activity ATMS RootWindowContainer Task PipTaskOrganizer
T
'
'
'
'
‘
'
‘
a
}-------4
T T T
' ' '
' ' '
' ' '
' ' '
‘ ‘ ‘
' ' '
‘ ‘ ‘
—_ a a
enterPicturelnPicture — >
moveActivity ToPinnedRootTask >
send TaskAppeared
rp —{(Pc }—+
onTaskAppeared
```

## Slide 39

###### Analyse Attack Vector

Prevent IPC!
Scheme 0x1 :
Attack PiP chain, make App task in ‘visible’ state
But no systemUI handle PiP window

# BHASIA @BlackHatEvents

## Slide 40

###### Analyse Attack Vector

Unfortunately, no trick could be exploited **Scheme 0x1** : User Space have no way to affect the code execute in System_Server Can’t prevent IPC

# BHASIA @BlackHatEvents

## Slide 41

###### Analyse Attack Vector

Scheme 0x2 :
Attack SystemUI side, create CVE-2021-0485-like vuln

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Analyse Attack Vector
AppLayer System_Server SystemUl
Activity ATMS RootWindowContainer Task PipTaskOrganizer
T
'
'
'
'
‘
'
‘
a
}-------4
T T T
' ' '
' ' '
' ' '
' ' '
‘ ‘ ‘
' ' '
‘ ‘ ‘
—_ a a
enierPicturelnPicture — >
moveActivity ToPinnedRootTask >
send TaskAppeared
onTaskAppeared
Scheme Ox2:
Attack SystemUI side, create CVE-2021-0485-like vuln
```

## Slide 42

###### Attack SourceRectHint

Auto scale and crop the Activity Window by passed-in Rect Abnormal Rect → Abnormal PiP Window??

Developer Doc of setSourceRectHint API

# BHASIA @BlackHatEvents

## Slide 43

###### Attack SourceRectHint

Enter PiP Mode with 1-pixel Rect, Run POC in Android13.0.0_r7 branch AVD We get a 1-pixel Window indeed, but recover to normal size within 0.5s

Around 0.5s

Any Trick to expands duration?

# BHASIA @BlackHatEvents

## Slide 44

###### Trace Rect

PipTaskOrganizer#onTaskAppeared

**This transition will resize PiP window** animateResizePip **into Rect defined size(1px) But what happen after resize???**

# BHASIA @BlackHatEvents

## Slide 45

###### Trace Rect

###### PipTransitionAnimator set a call back hander

onPipAnimationEnd interface called after Pip entered, within calls finishResize

# BHASIA @BlackHatEvents

## Slide 46

###### Trace Rect

finishResize creates a WindowContainerTransaction(WCT) instance Pass to prepareFinishResizeTransaction with **normal size Rect defined by System** Set a **SurfaceControl.Transaction and the Rect** for WCT inside function

# BHASIA @BlackHatEvents

## Slide 47

###### Trace Rect

###### applyFinishBoundsResize carry WCT to IPC with SystemServer

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biseichat x ——
ASIA 2024
Trace Rect
applyFinishBoundsResize carry WCT to IPC with SystemServer
void FinishResize{ mm) {
Rect preResizeBounds Fect(mPipBoundsState _getBounds{ });
boolean isPipTopLeft = isPipTopLeft(};
mPipBoundsState .setBounds(destinationBounds} ;
(direction TRANSITION DIRECTION MOVE STACK) { =} C(isInPipDirection(direction
HindowClontainerTransaction wet HindowlontainerTransaction( 3
prepareFinishResizeTransaction(destinationBounds, direction, tx, wet);
5Soolean mayAnimateFinishResize = direction
foolean animateCrossFadeResize nayAnimateFinishResize a
CanimateCrossFadeResize) { =} q
applyFinishBoundsResize(wet, direction, isPipTopLeft);
r
FinishResizeForHenu(destinationBounds) 5;
```

## Slide 48

###### Trace Rect

###### *** Before IPC**

**applyFinishBoundsResize**

Extra SurfaceControl.Transaction, IPC with System Pass SCT into setMainWindowSizeChangeTransaction

Task#setMainWindowSizeChangeTransaction SystemServer directly call merge to render SCT on screen Cause Pip Window resize to normal after merge, any way to **prevent merge???**

# BHASIA @BlackHatEvents

## Slide 49

###### Trace Rect

Block IPC for prevent merge

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Trace Rect
onPipAnimationEnd 4
SystemUl
PipTask Organizer
Block IF
al
=
finishResize
System_Sever
Window OrganizerController
apolyFinishBoundsResize
a pplyTra nsacti on
i
setMainWindowSizeChange Transaction
Task
|< —
IPC
C for prevent m
erg
le
apply Window ContainerChange
all
```

## Slide 50

###### Trace Rect

Almost no way to prevent merge

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2024
Trace Rect
SystemUl
System_Sever
PipTask Organizer
onPipAnimationEnd -4
Window OrganizerController Task
'
rho
|
Almost no way to prevent merge
| |
a pplyTra nsaction '
IPC
apply vvindow_ontainen_nange |
```

## Slide 51

###### Diff Analyse

**Compare different branch** API32 found code change

Functional Patch instead of Security Patch from commit detail **Still valuable to analyse API32**

**API32 DO NOT CALL merge!**

# BHASIA @BlackHatEvents

## Slide 52

###### API32 For 12.1.0_r27

Sets the SCT
Gets the SCT
HOOK FUNC!

Gets the SCT
HOOK FUNC!

WindowStateAnimator#setSurfaceBoundariesLocked

# BHASIA @BlackHatEvents

## Slide 53

###### Analyse CALL STACK

- ActivityRecord#prepareSurface in the call stack

- Related with Activity Launch/Rendering (Enter PiP Mode will relaunch Activity)

- • **User space can affect it indirectly!**

# BHASIA @BlackHatEvents

## Slide 54

###### Attack API32

###### • API33&&API32 SystemUI all finally call to setMainWindowSizeChangeTransaction • **API33**

1. setMWSCT call merge, no way prevent pip size back to normal

2. Whole chain handled by SystemUI

###### • **API32**

1. setMWSCT sets SCT to global member, wait for access **2. Activity reDraw will access SCT and call merge == frozen reDraw, merge will not be called**

# BHASIA @BlackHatEvents

## Slide 55

###### CVE-2023-40116

BAL Bypass API32

We want API33+ Bypass

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
CVE-2023-40116
PicturelnPictureParams .Builder builder = new PicturelInPictureParams .Builder();
builder .setSourceRecthHint(new Rect(6,6,5,53);
enterPicturel nPicturehode(builder .build(});
while (true);
C:\Users\Administrator>adb shell dumpsys activity activities
ACTIVITY MANAGER ACTIVITIES (dumpsys activity activities)
Displav #0 (activities from ton to bottom):
« Task{ecadbf8 #42 type=standard A=10149:com.pip.poc U=@ visible=true visi
bleRequested=true mode=pinned translucent=false sz=1}
isSleeping=false
* Hist #0: ActivityRecord{167769d u®@ com.pip.poc/.PipPoCActivity t42}
packageName=com.pip.poc processName=com.pip.poc
launchedFromUid=@ launchedFromPackage=com.android.shell launchedFromFe
ature=null userId=@
app=ProcessRecord{e@82ee3 3546: com.pip.poc/uBal49}
Intent { act=android.intent.action.MAIN cat=[android.intent.category.L
AUNCHER] f1lg=0x10000800 cmp=com.pip.poc/.PipPoCActivity }
rootOfTask=true task=Task{ecadbf8 #42 type=standard A=10149:com.pip.po
c U=8 visible=true visibleRequested=true mode=pinned translucent=false sz=1}
taskAffinity=10149:com.pip.poc
mActivityComponent=com.pip.poc/ .PipPoCActivity
baseDir=/data/app/” ~mP2?7jJYsNUeu6RN4 7TF9IQ==/com. pip. poc-gIHxRIgx0BHES
Tu33szESQ==/base. apk
dataDir=/data/user/@/com.pip.poc
stateNotNeeded=false componentSpecified=false mActivitylype=standard
compat={420dpi} labelRes=0x7f@e081b icon=0x/7fOcOB08 theme=Ox7fOFO183
mLastReportedConfigurations:
mGlobalConfig={1.8 310mcc260mnc [en_US] ldltr swl@8dp w192dp h108dp
42@dpi smll land finger qwerty/v/yv dpad/v winConfig={ mBounds=Rect(533, 1140
- 1038, 1424) mAppBounds=Rect(533, 1140 - 1038, 1424) mMaxBounds=Rect(®, @
- 1080, 1920) mWindowingMode=pinned mDisplayWindowingMode=fullscreen mActivi
tyType=undefined mAlwaysOnTop=undefined mRotation=ROTATION_@} as.5 s.290 fon
tWeightAdjustment=0}
BAL Bypass API32
We want API33+ Bypass
```

## Slide 56

###### ActivityOptions

**Api_diff list -> makeLaunchIntoPip** Return ActivityOptions object

Activity#startActivity(Intent, **Bundle** ) Additional options for Activity launch

https://developer.android.com/sdk/api_diff/33/changes

# BHASIA @BlackHatEvents

## Slide 57

###### ActivityOptions

Save received PipParam to AO packaged Bundle By LAUNCH_INTO_PIP_PARAMS Key Bundle used to set options for Activity start

ActivityOptions#toBundle

# BHASIA @BlackHatEvents

## Slide 58

###### Trace Bundle

startActivityInner call moveToFront if App pass BAL check What Bundle will do inside chain?

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
ASIA 2024
Trace Bundle
Bundle
—») Activity#startActivity
N
ActivityStarter#executeR equest
RWC#resumeF ocused Tasks lopActivities
S
N
Instrumentation#execStartActivity
Activity Starter#startActivityInner
Task#resume TopActivityUn checkedLocked
NS
ATMS#startActivityAsUser
N
Task#startActivityLocked
x
TaskFragment#resume lopActivity
startActivityInner call moveToFront if App pass BAL check
What Bundle will do inside chain?
```

## Slide 59

###### CVE-2023-21269

###### Check Bundle by isLaunchIntoPip()

• Where is BAL restriction check?????

Directly call moveActivityToPinnedRootTask without any check???

- **Set app to pinned state from background at any time for API33+**

# BHASIA @BlackHatEvents

## Slide 60

### 2<sup>nd</sup> High Wall: State Leaking

# BHASIA @BlackHatEvents

## Slide 61

###### Bug OR Trick?

###### Bug I met when I am developing an app…

- After merge code → throw Exception by startServiceCommon

- Before merge at bug position: bindService

- After merge at bug position: startService

# BHASIA @BlackHatEvents

## Slide 62

###### Side Channel Detector

###### Background Execution Limitation

- Throw exception when start background service

- • Background Process Detector!

- Bypass Limitation? Explote Limitation!

# BHASIA @BlackHatEvents

## Slide 63

###### A-254674510

###### ActiveServices#startServiceLocked

System return Abnormal ComponentName

**Throw exception in User Space**

**POC For side channel detect**

# BHASIA @BlackHatEvents

## Slide 64

###### Other Tricks?

Due to time reason, more side-channel trick of other Rom in WhitePaper.

# BHASIA @BlackHatEvents

## Slide 65

### 3<sup>rd</sup> High Wall: Breaking LMKD

# BHASIA @BlackHatEvents

## Slide 66

###### LMKD & OOM_ADJ Score

- Lower oom_adj → Higher priority

- Higher oom_adj → Lower priority

   - Fg Service usually gets score of 250

   - No silent process

- LMKD kills high oom score process first

- • Bg process always gets high oom score

Low-memory Killer Daemon

# BHASIA @BlackHatEvents

## Slide 67

###### OOM_ADJ Calc Trick

Service bound by 3<sup>rd</sup> Client with oom score < Bounder oom score

• Bounder may gets oom score **VISIBLE_APP_ADJ**

OomAdjuster#computeOomAdjLSP

# BHASIA @BlackHatEvents

## Slide 68

###### Attack Surface

Bound by System persistent process?

Non-privilege App operate Managers(AMS, WMS…) by correspond IBinder object.

Managers run as system(UID=1000)

Can abuse Managers???

# BHASIA @BlackHatEvents

## Slide 69

###### AccessibilityService

- Accessibility function handled by Accessibility **Manager** Service

- • Non-privilege App needs to declare specific Intent-Filter • Intent-Filter pointing a specific Service

# BHASIA @BlackHatEvents

## Slide 70

###### AccessibilityManagerService

- AccessibilityManagerService will find all Service with specific Intent-Filter

- Create AccessibilityServiceConnection by specific Intent-Filter

- Call **bindLocked**

AccessibilityManagerService#updateServiceLocked

# BHASIA @BlackHatEvents

## Slide 71

Bound by System! AccessibilityManagerService run as system_server(UID=1000) System_server gets oom score of -900 Non-privilege gets oom socre of **100** ! **But Accessibility requires dangerous runtime-permission!**

# BHASIA @BlackHatEvents

## Slide 72

###### AccountManager

AccountManager API added in API5(2009) Handled by privilege AccountManagerService For Developers:

- Declare Service with abstract Component “AccountAuthenticator”!

- • **Declare Intent-Filter with specific Action** !

- **No Need dangerous runtime permission** !

# BHASIA @BlackHatEvents

## Slide 73

###### AddAccount

Get AM by getSystemService Call addAccount

new Session().bind()

**Bind specific component as system_server!**

# BHASIA @BlackHatEvents

## Slide 74

A-263918277 High Priority Process elevate to Persistent Process! Make SystemServer keep binding target!

AccountManager$AmsTask$Response#onResult

POC

# BHASIA @BlackHatEvents

## Slide 75

### DEMO OF PERSISTENT POC

# BHASIA @BlackHatEvents

## Slide 76

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
C:\Users\Administrator>adb logcat -c
> | > <p
ASIA 2024 a nN
C:\Users\Administrator>adb logcat|findstr POC-TESTER
C:\Users\Administrator>
Settings POC
GOe0e
GE
```

## Slide 77

# Full Chain Of Hijack Exp

# BHASIA @BlackHatEvents

## Slide 78

# BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
C:\Users\Administrator>adb logcat|findstr POC-SERVICE
Settings
@@x
Telegram YouTube
06086906
GEEZ:
```

## Slide 79

## THANKS!

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ASIA 2 2a
IL 18-19, 2024
vA BRIEFINGS
#BHASIA @BlackHatEvents
```
