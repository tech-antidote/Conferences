---
title: "My other ClassLoader is your ClassLoader Creating evil twin instances of a class"
speakers: ["Dimitrios Valsamaras"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Dimitrios Valsamaras_My other ClassLoader is your ClassLoader Creating evil twin instances of a class.pdf"
pages: 44
sha256: "7be22477666964ec9215509f84fcddea48926ba06e1dbf7d8f445ade3e192e1a"
text_chars: 26120
ocr_pages: 24
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:49:43Z"
---
# My other ClassLoader is your ClassLoader Creating evil twin instances of a class

**Speakers:** Dimitrios Valsamaras  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Dimitrios Valsamaras_My other ClassLoader is your ClassLoader Creating evil twin instances of a class.pdf` (44 pages)

## Slide 1

#### **My other ClassLoader Is Your ClassLoader**

**Dimitrios Valsamaras** Microsoft Threat Intelligence

#BHEU @BlackHatEvents

## Slide 2

###### About Me

❑ **Engaged in computer security since 2002**

- ❑ **Focus on Mobile Security for the last 6 years**

❑ **Senior Security Researcher @Microsoft**

**/Ch0pin**

**@Ch0pin​**

**/in/valsamaras**

#BHEU @BlackHatEvents

## Slide 3

###### Outline

❑ **Basic Concepts**

❑ **How it was going…**

❑ **Common security issues** ❑ **How it started …**

###### ❑ **How it ended**

- ❑ **Showcases**

❑ **Takeaways**

#BHEU @BlackHatEvents

## Slide 4

###### Basic Concepts

ClassLoader
Bootstrap
Concepts
Types
UD 0
UD 1 UD 1 UD 1
UD: User Defined

**ClassLoader Concepts**

Types

#BHEU @BlackHatEvents

## Slide 5

###### Basic Concepts

###### **Dalvik VM**

**ART**

**d8(.class)** → **.dex** → **.apk**

ClassLoader
BootClassLoader BaseDexClassLoader SecureClassLoader
PathClassLoader InMemoryDexClassLoader DexClassLoader

#BHEU @BlackHatEvents

## Slide 6

###### Parcelables & Serializables

- -
JVM  A JVM  B
Byte  Byte
stream stream
class A   ∈ class path
class A implements java.io.Serializable

###### **class A implements java.io.Serializable**

#BHEU @BlackHatEvents

## Slide 7

###### Parcelables & Serializables

Obtained
Recycled

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ari NN
pisekhat Parcelables & Serializables —
EUROPE 2024
public class MyParcelable| implements Parcelabld {
private int mData;
public int describeContents() {
return 6;
}
public void writeToParcel(Parcel out, int flags) {
out.writeInt(mData) ;
}
public static final Parcelable.Creator<MyParcelable> CREATOR
= new Parcelable.Creator<MyParcelable=() {
public MyParcelable |createFromParcel(Parcel in)| {
return new MyParcelable(in);
}
Recycled public MyParcelable[] newArray(int size) {
return new MyParcelable[size] ;
4
I
I
I
I
I
l
I
}
IPF
private MyParcelable(Parcel in) {
mData = in.readInt();
= 6
#BHEU @BlackHatEvents
```

## Slide 8

###### Known Issues

**Parcelables Serializables ?**

**CVE 2014 7911 (Jan Horn)**

**CVE 2021 0928 (M. Bednarski**

**android.os.BinderProxy**

**CVE 2015 3825 (Peles & Hay)**

**CVE 2017 0806 (M. Bednarski)**

**OpenSSLX509Certificate**

#BHEU @BlackHatEvents

## Slide 9

###### How it started

#BHEU @BlackHatEvents

## Slide 10

###### How it started

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EUROPE 2024
pisekhat How it started — \
a
tte 8
LL i—
HELLO?.
ra
Hello ?
@ Hey! I'm here. How can | help you further?
write a Frida script to intercept android intents
#BHEU @BlackHatEvents
```

## Slide 11

###### How it started

Parcelable

**https://<trusted host>**

**https://github.com/Ch0pin/medusa**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2 How it started
black hat
EUROPE 2024 7
RuActivity Chas extras) }
enter. fragments.
[+] New Intent: Intent { cmp=com
rActivity#portrait_Llockstrue, fragment_class=com.
\ getAction, name: , null
\ugetStringExtra, name: marked_as_dumped, null
\getExtras, name: , Bundle[{custom_transition=false, com.
g=ContactFlowArgs(requestMetadata=null, requestInput=null, requestFlowType=null, requestCallId=null, reserwationCode=null, sea
s7entry=GUEST_PROFILE_SAFETY&role=guest, entry=nul1)}], marked_as_dumped_internal=173150430273, navigat
ContactFlowFragment, fragment_args=Bundle[{mav
rchKey=nul1, roleOnEntry=GUEST, entryUri=https://waw.;
ion_instance=cZe17f95-f762-47c0-978f-@31c1391dd65, require_login=true}]
xActivity Chas extras) }
Intent { cmp=com.
Che intent is targeting a NON EXPORTED component)
\_Extras:
(Boolean) custom_transition = false
(Boolean) com. rActivity#portrait_lock = true
CString) marked_as_dumped internal = Lraloet 0273
¥
!
I
(Boolean) require_login = true
\_Flags: @x@
/  Parcelable
https ://github.com/ChOpin/medusa
https://<trusted-host>
#BHEU @BlackHatEvents
```

## Slide 12

###### How it was going…

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biseichat How it was going... =
EUROPE 2024
S £.
1
| SHALL CALL HIM MINI-ME
#BHEU @BlackHatEvents
```

## Slide 13

###### How it was going…

**Let’s reconstruct the class**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSekhat How it was going... Si
EUROPE 2024
package [com. .android. feat. payments. questwalLlet.nav;
/* loaded from: classes3.dex +/
public final class b implements android.os.Parcelable {
public static final android.os.Parcelable.Creator<com. android. feat. payments. questwallet.nav.b> CREATOR = new java. Lang.0
private final java. lang.foolean success;
public b(java.lang.Boolean bool) {
this.success = bool;
@Override // android.os.Parcelable
public final int describeContents(
return @;
}
Let’s reconstruct the class
#BHEU @BlackHatEvents
```

## Slide 14

###### How it was going…

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piSekhat How it was going... —
EUROPE 2024
package url;
loaded from: cla
public abstract class a implements android.os.Parcelable {
private final boolean broadcastShareChannellnfo;
private final url.d chinaSharingEntryInfo; public final class d {
private final 224.a deepLinkEntryPoint; public static final url.c [;
private final h14.a deeplinkItemType; public static final url.d 1;
private final j ig previewContent; public static final url.d vu;
private final j revi : public static final url.d
private final J public static final url.d 1!;
public static final url.d v;
public static final url.d 4;
public static final url.d cj
public static final /*
public final java. lang
public final hl4.a !1;
public final 224.a 11;
public final url.b 1!;
public final java. lang
package h14;
loaded from: ¢
public enum a {
Home (1),
Experience(2),
Story(3),
Guidebook(4),
Place(5)
Detour(6),
Itinerary(7),
WishList
Referral(
HostReferral(10),
#BHEU @BlackHatEvents
```

## Slide 15

###### How it was going…

###### ✓ **Get the dex/apk files**

✓ **Use dex 2 jar**

**Import the jar to the project**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat How it was going... =
EUROPE 2024
New
Add C++ to Module
ae |e v¥ Get the dex/apk files
Copy Path/Reference..
(=) Paste
{} gradie.properties Find Usages
Analyze
Refactor
a Bookmarks
tth External Libraries
=e Delete...
= Scratches and Consoles
Override File Type
wwane W UJse dex 2 jar
Debug ‘base-dex2jar jar’
© Run 'base-dex2jar.jar’ with Coverage
Modify Run Configuration.
(D Open in Right Split
Open In
Local History
Build Sync Build Output Bui
Git
&> TestAppp: finished Repair IDE on File :
+, Download info «> Reload from Disk
+ Compare With...
Compare File with Editor
— am Import the jar to the project
#BHEU @BlackHatEvents
```

## Slide 16

###### How it was going…

#BHEU @BlackHatEvents

## Slide 17

###### How it was going…

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Y @ Build TestAppp: failed At 11/11/2024, 19 sec, 209 ms
4, Download info
@ :app:checkDebugDuplicateClasses
234 ms
> @ :app:desugarDebugFileDependenc 16 sec, 119 ms
> &:app:compileDebugJavaWithJavac 5 sec, 239 ms
> @:app:dexBuilderDebug 10 errors
@ Duplicate class found
426 ms
Inplaiene
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
Duplicate
How it was go
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
class
/
j
android. support.v4.app.RemoteActionCompatParcelizer found in modules base-dex2jar.jar -> base- aes (base- iaaen. jar) and core-1.9.0.aar -> core-1.9.0-ru
android.support.v4.graphics.drawable.IconCompatParcelizer found in modules base-dex2jar.jar -> base-dex2jar (base-dex2jar.jar) and core-1.9.0.aar -> core-1.
androidx.annotation.Keep found in modules annotation-1.3.0.jar -> annotation-1.3.0 (androidx.annotation:annotation:1.3.0) and base-dex2jar.jar -> base-dex2j
androidx.
androidx.
androidx
androidx
androidx
androidx
androidx.
androidx.
androidx.
androidx.
androidx.
androidx
androidx
androidx
androidx
androidx.
androidx.
androidx.
androidx.
androidx.
androidx
androidx
androidx
appcompat.
appcompat.
-appcompat.view.menu.ActionMenuItemView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and bas
-appcompat.
-appcompat.
-appcompat.
appcompat .
appcompat.
appcompat.
appcompat.
appcompat.
-appcompat.
-appcompat.
.appcompat.
-appcompat.
appcompat.
appcompat.
appcompat.
appcompat.
appcompat .
-appcompat.
-appcompat.
app.AlertController found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2jar
app.AlertController$RecycleListView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1)
view.menu.ExpandedMenuView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-
view.menu.ListMenuItemView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-
widget.
widget.
widget.
widget.
widget.
-AlertDialogLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-de
widget
widget.
widget.
widget.
widget.
widget.
widget.
widget.
.SearchView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2jar.j
widget
widget.
widget.
widget.
.constraintlayout.
ActionBarContainer found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-d
ActionBarContextView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base
ActionBarOverlayLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and ba
ActionMenuView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2j
ActivityChooserView$InnerLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.
AppCompatImageView found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-d
ButtonBarLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2
ContentFrameLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-d
DialogTitle found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2jar
FitWindowsFrameLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and bas
FitWindowsLinearLayout found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and ba
LinearLayoutCompat found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-d
SearchView$SearchAutoComplete found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1)
Toolbar found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2jar.jar
ViewStubCompat found in modules appcompat-1.6.1.aar -> appcompat-1.6.1-runtime (androidx.appcompat:appcompat:1.6.1) and base-dex2j
helper.widget.Flow found in modules base-dex2jar.jar -> base-dex2jar (base-dex2jar.jar) and constraintlayout-2.1.4.aar -> constrai
#BHEU @BlackHatEvents
```

## Slide 18

###### How it was going…

# **Dynamic Code Loading ?**

#BHEU @BlackHatEvents

## Slide 19

###### How it was going…

**java.lang.Object**

**java.lang.Object**

↳ java.lang.ClassLoader

↳ java.lang.ClassLoader

- ↳ dalvik.system.BaseDexClassLoader

↳ dalvik.system.BaseDexClassLoader

↳ dalvik.system.DexClassLoader

↳ dalvik.system.PathClassLoader

**/data/app/…/base.apk**

#BHEU @BlackHatEvents

## Slide 20

###### How it was going…

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekchat How it was go
EUROPE 2024
PackageManager packageManager = getPackageManager();
try {
ApplicationInfo appInfo = packageManager.getApplicationInfo( s: "com.android.chrome", i: 0);
String codeDir = appInfo.sourceDir;
System.out.printin("Code directory: " + codeDir); a
PathClassLoader pathClassLoader = new PathClassLoader(codeDir, parent: null);
System.out.println(pathClassLoader) ;
} catch (PackageManager.NameNotFoundException e) {
throw new RuntimeException(e);
we LUIIVAOL ULlidllyt 1u bPopulrccu. 21u7Z040Z, Viv 1UZ0U, DSLaLtt. CINADLCU
Code directory: /data/app/~~bCnKLyrI5gIBbJTs1l45k0g==/com. android. chrome-ONVpflDvLIIOitUt1V8pog==/base.apk
ClassLoaderContext shared library size mismatch. Expected=1, found=0 (PCL[]{PCL[]} | PCLI[])
dalvik.system.PathClassLoader[DexPathList[[zip file "/data/app/~~bCnKLyrI5gIBbJTsSL45k0g==/com. android. chrome-ONVpfLDVLII0itUt1V8pog==/base.apk"]
#BHEU @BlackHatEvents
```

## Slide 21

###### How it ended

**createPackageContextAsUser()**

**setResources()**

###### **createPackageContext**

**Flags: CONTEXT_INCLUDE_CODE | CONTEXT_IGNORE_SECURITY | CONTEXT_RESTRICTED**

#BHEU @BlackHatEvents

## Slide 22

###### How it ended

###### **Package Visibility**

- **SDK 29 or lower**

• **SDK 30 or higher**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EUROPE 2024
Package Visibility
aw 4
piSekhat How it ended . a
<uses-permission android:name='android.permission.QUERY_ALL_PACKAGES'
tools: ignore="QueryAllPackagesPermission"/>
SDK 29 or lower
<queries>
<intent>
<action android:name="x"/>
</intent>
<package android:name="com.example.app"/>
</queries>
—_— =>
SDK 30 or higher
Pe
if your app targets Android 11 or higher and needs to interact with apps other than the ones that are visible
automatically, add the element in your app's manifest file. Within the element, specify the [+
other apps by package name, by intent signature, or by provider authority, as described in the following sections.
tL
#BHEU @BlackHatEvents
```

## Slide 23

###### How it ended

### **Reflection**

- **Class<T>**

- • **Field**

- **Method**

• **Constructor**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisekhat How it ended
EUROPE 2024
e Class<T>
e Field
e Method
Reflection
¢ Constructor
public Class<?> loadClass(String name) throws ClassNotFoundException {
return loadClass(name, false);
}
#BHEU
@BlackHatEvents
```

## Slide 24

###### How it ended

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
How it ended vs
Object = clu.getInstanceForClass( className: "com.example.app.Example",
new Class[]{String.class, String.class},
new Object[]{"Java", "Reflection"}
YF
public Object (String className,Class<?>[] parameterTypes, Object[] constructorArg
try {
Class<?> clazz = classLoader.loadClass(className) ;
Constructor<?> genericConstructor = clazz.getDeclaredConstructor(parameterTypes) ; _
genericConstructor.setAccessible(true) ; -
return genericConstructor.newInstance(constructorArgs) ;
} catch (NoSuchMethodException | InvocationTargetException | IllegalAccessException
InstantiationException | ClassNotFoundException e){
throw new RuntimeException(e);
IF
}
public T newInstance(java.lang.Object... initargs)
throws java.lang.IllegalAccessException, java.lang.IllegalArgumentException,
java.lang.InstantiationException, java.lang.reflect.InvocationTargetException {
throw new RuntimeException("Stub!");
) { nousag
#BHEU @BlackHatEvents
```

## Slide 25

###### So Far…

✓ **An application can access and use the class loader of another application, if both apps are installed on the same device**

- ✓ **This allows it to load classes defined in other apps and create instances of those classes with arbitrary data.**

- ✓ **If a class is parcelable or serializable it can be sent across apps.**

#BHEU @BlackHatEvents

## Slide 26

###### Impact

##### **Account Hijacking Intent Redirection Code Execution**

#BHEU @BlackHatEvents

## Slide 27

##### **What to look for ?**

**API Calls**

(Intent)     getParcelableExtra (Intent)     getSerializableExtra (Bundle)   getParcelable (Bundle)   getSerializable

#BHEU @BlackHatEvents

## Slide 28

###### Frequency

300  156
•
Account Hijacking Retail & eCommerce
14%
•
Travel & Hospitality
Not Vulnerable Vulnerable
Intent Redirection
69% 31%
3%
•
Media & entertainment
Other
14%
•
Financial services
Not Vulnerable Account Hijacking Intent Redirection Other

#BHEU @BlackHatEvents

## Slide 29

###### Showcases

###### **Intent redirection**

_Source: https://support.google.com/faqs/answer/9267555_

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EUROPE 2024
Intent redirection
After the deadlines shown in your Play Console, any apps that contain unfixed security
vulnerabilities will be removed from Google Play.
Source: https://support.google.com/faqs/answer/926 7555
#BHEU @BlackHatEvents
```

## Slide 30

###### Showcases

###### **Intent redirection**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EUROPE 2024
a”
bisckhat Showcases. <<: a
Intent redirection
if |(intent. hasExtra("extra_request"))| {
if (android.os.Build. VERSION. SDK_INT > 33) {
parcelableExtra = intent.getParcelableExtra("extra_request", com.example.acase. features. shared.nav. Request. class);
parcelable? = (android.os.Parcelable) parcelableExtra;
} else {
android.os.Parcelable parcelableExtra4 = intent.getParcelableExtra("extra_request");
if |(parcelableExtra4 instanceof com.example.acase.features.shared.nav.Request) {
parcelable3 = parcelableExtra4;
}
parcelable? = (com.example.acase. features. shared.nav.Request) parcelable3;
}
intent. removeExtra("extra_regquest");
setintent( intent);
geRequestHandler().handleRequest(this, (com.example.acase. features. shared.nav.Request) parcelable?) ;
return;
; 6
#BHEU @BlackHatEvents
```

## Slide 31

###### Showcases

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
od
EUROPE 2024
public final class IRequest extends] com.example.acase. features. shared.nav.Request| {
pistkhat Showcases. \
x
public static final android.os.Parcelable.Creator =< com.example.acase. features. shared.nav. [Request > CREATOR =
new com.example.acase. features. shared.nav. IRequest.Creator( );
private Tinal android.content.Intent intent;
public static final class Creator implements android.os.Parcelable.Creator < com.example.acase. features. shared.nav. [Request > {
}
/* JADX WARN: ‘super’ call moved to the top of the method (can break code semantics) »/
public IRequest(@org.jetbrains.annotations.NotNull android.content.Intent intent) {
super(mull);
kotlin. jvm. internal.Intrinsics. checkNotNullParameter(intent, “intent");
this.intent = intent;
}
#BHEU @BlackHatEvents
```

## Slide 32

###### Showcases

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©
— *
piscichat Showcases .
LO x
EUROPE 2024
if (lintent.hasExtra("extra request")) { |
android.os.Build.VERSION.SDK_INT > 33) {
parcelableExtra = intent. getParcelableExtra("extra_request", com.example.acase. features. shared. nav.Request. class);
parcelable? = (android.os.Parcelable) parcelableExtra;
android.os.Parcelable parcelableExtra4 = intent. getParcelableExtra("extra_request");
(parcelableExtra4 instanceof com. example.acase. features. shared.nav.Request)| {
parcelable3 = parcelableExtrad;
}
parcelable? = (com.example.acase. features.shared.nav.Request) parcelable3;
intent. removeExtra("extra_reguest");
setintent( intent);
geRequestHandler().handleRequest(this, (com.example.acase. features.shared.nav.Request) parcelable2); — 4
'
/fcom,examp le.acase. features. shared. nav. RequestHand ler
I
} else if (request instanceof com.example.acase. features. shared.nav.I[Request) {
navigator. getMainView( ).getContext().startActivity( ((com.example.acase. features. shared.nav.[Request) request).getIntent());
} else if (request instanceot com.example.acase. features. shared. nav.OtherRequest)
#BHEU @BlackHatEvents
```

## Slide 33

###### Showcases

> loader from createPackageContext

> loader.loadClass(“.IRequest”)

> Create Malicious intent_1

> Create IRequest Object > Create intent_2 with an extra_request extra

> startActivity(intent_2)

#BHEU @BlackHatEvents

## Slide 34

###### Showcases

###### **Account Hijacking**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
EUROPE 2024
Account
Hijacking
mm,
Showcases. ._ S.
@0verride
protected void onCreate(Bundle bundle) {
boolean 214;
String f14;
ArticleCollectionFragment articleCollectionFragment;
super.onCreate(bundle) ;
setContentView(R$layout. f57861a) ;
if (bundle == null) {
if (this. f45638c.e() != null && this. f45638c.e().get("follow_signup") != null) {
214 = true;
} else Ki
z14 = false;
iM
lif (getIntent().hasExtra("e_insider") ) k
jarticleCollectionFragment = articleCollectionFragment.yj((Insider) getIntent().getParcelableExtra("e_insider"), z14)}
} else {
if (getIntent().hasExtra("e_insider_id")) {
#14 = getIntent().getStringExtra("e_insider_id");
} else {
f14 = this. f45638c.f();
}
if (f14 != null) {
articleCollectionFragment
} else {
articleCollectionFragment = null;
articleCollectionFragment.Fj(f14, z14);
}
}
if (articleCollectionFragment != null) {
getSupportFragmentManager().q().u(R$id.f4424600, articleCollectionFragment, articleCollectionFragment.class.getName()).j();
}
#BHEU @BlackHatEvents
```

## Slide 35

###### Showcases

###### **Account Hijacking**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Be 4
piSeichat Showcases | SS
EUROPE 2024
A public class Insider implements Parcelable {
ccount public static final Parcelable.Creator<Insider> CREATOR = new a();
Hijacking @Json(name = “about")
private String about;
@Json(name = "a_collection_url")
private String aCollectionUrl;
Insider(Parcel parcel) {
this.about = parcel.readString();
this.aCollectionUrl = parcel. readString();
6
#BHEU @BlackHatEvents
```

## Slide 36

###### Showcases

###### **Account Hijacking**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
EUROPE 2024
e Article Collection QO
PNexerolUlalm@alit-(e.diare
GET //n/
11/04 / 2023 at 8:57:19 AM
94.63.170.172
order=id_desc&offset=0&limit=10
Cache-Allow
Client-Os
X-Forwarded-Proto
Device
User-Agent
Authorization
Accept-Encoding
Os-Version
Accept
Accept-Language
Host
true
Android
https
barbet
Bearer Qigjll2VhEqfSoRU3BghiCuWPuPmmuwRvbAug7W-9Y
mnV_65JM3abUzuD YK8dmv1 -BiO-GRymVkkkgVO8sgbiA2wwA
cdwEZy_iiVWKK2OTX2qvzaeswtzUIS1AvrKbAs1jOWWUiTphhw
R&fdnuoXAB3Xu_2J36/7Q0wd8vi4F4Nn8AqGSAFi0O3LwuR1T1
Es7tE-lyOF7uBSS5IFZbq7TRpaAXD3f7umU6TDW YeoH_auMRo
gzip, deflate, br
12
application/json
en
api.webhookinbox.com
#BHEU @BlackHatEvents
```

## Slide 37

###### Showcases

> loader from createPackageContext > loader.loadClass(“.Insider”) > Create .Insider Evil Twin (with malicious URL) > Create intent with an e_insider extra > startActivity(intent)

#BHEU @BlackHatEvents

## Slide 38

###### Showcases

###### **“Complementary Argument”**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
'*)
EUROPE 2024
7
A
y
blackhat Showcases~
“Complementary Argument’
Z
fragment
android: Label="VideoListFragment"
android: name="com.the.app. feed. videolist.VideoListFragment"
android: id="@+id/VideoListFragment”
a
rgument
android:name="url"
apprargType="string"
a
a
a
rgument
android:name="title"
android: defaultValue="anul1"
app:arglype="string”
app:nuLlable="true"
rgument
android: name="subtitle"
android: defaultValue="a@null"
appiarglype="string"
app:nuLlable="true"
rgument
android:name="symboL"
android: defaultValue="anul1"
app:arglype="string”
app:nuLlable="true"
a
rgument
android:name="appScreen"
appiarglype="com.app.core.analytics. Screens"
app:inuLllable="false"
Fragment
&
#BHEU @BlackHatEvents
```

## Slide 39

###### Showcases

**…Required argument appScreen is missing**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
10-1
10-81
10-@1
10-@1
10-@1
biSekchat
EUROPE 2024
14:
14:
14;
14:
735:
35:
35:
Bos
735:
335:
235:
Sas
35:
35:
35:
35:
35:
15.
15.
15
15.
15.
886
886
886
886
886
886
886
886
886
886
-886
886
886
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
beginning of crash
15.
15.
1S.
15.
15.
15.
15.
15.
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
12799
—_———, j
A Ne
Showcase \
AndroidRuntime; FATAL EXCEPTION: main
AndroidRuntime: Process: com. development, PID: 12799
AndroidRuntime: java.lang.RuntimeException: java.lang. reflect. InvocationTargetException
AndroidRuntime: at com.android.internal.os.RuntimeInit$MethodAndArgsCal ler. run(RuntimeInit. java: 504)
AndroidRuntime: at com.android.internal.os.ZygoteInit .main(ZygoteInit. java:965)
AndroidRuntime: Caused by: java.lang.reflect. InvocationTargetException
AndroidRuntime: at java.lang.reflect.Method.invoke(Native Method)
AndroidRuntime: at com.android.internal.os.RuntimeInit$MethodAndArgsCal ler. runCRuntimeInit. java:494)
AndroidRuntime ; aamore
AndroidRuntime:] Caused by: java.lang.IllegalArgumentException: Required argument “appScreen" is missing and does not have an android:defaultValue
AndroidRuntime at com. i$Companion. fromBundleCUnknown Source:135)
AndroidRuntime GC COM. pas d Sepp Fay fv Cel 6 cuaweal Sibdd te seeceur weuuin iv apmaiow yo. fromBundleCUnknown Source:2)
AndroidRuntime : . 28 more
#BHEU @BlackHatEvents
```

## Slide 40

###### Showcases

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EUROPE 2024
public abstract class Screens implements java. io.S5erializable
public static final int stable = @;
private final java.lang.String aName;
private final java.lang.String bName;
> *
pis hat Showcases. Ny
x
public static final class AScreen extends com.app.core.analytics.Screens implements java.io.Serializable {
public Static Tinal int $stable = @;
public static final com.app.core.analytics.Screens.AScreen INSTANCE = new com.app.core.analytics.Screens.AScreen()};
private AScreen() {
super({"Ascreen", null, 2, mull};
_ By
#BHEU @BlackHatEvents
```

## Slide 41

###### Showcases

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blaekhat Showcases Ss
EUROPE 2024
714 https://4x2gz5e0mifk5x7a012widnyvp 1gp6dv.oastify.com GET i 200 203 HTML
T1715) Atte /fetaninn-ani 017AN19SR AS 749 heallanihlie earn ET faranheearvineain intasFevimnhnls ui >nin TARY JASON
Request Response
Pretty Raw Hex ® S&S in = Pretty Raw Hex Render
1 GET / HITP/1.1 1 HITP/1.1 200 OK
? Host: 4x2gz5e0mifk5x/abl2wjdnyvplgp6dv.oastify.com ? | Server: Burp Collaborator https:/
3 X-App-Version: android—3.162.0-b33625 3 X=Collaborator-Version: 4
4 User-Agent: android—-3.162.0-b33625 4 Content-Type: text/html
5 | Authorization: Bearer 5 Content-Length: 55
ey] @eXAi01IJKV10iL¢ LYTQtY)]NiNy@l1 6
v0 7 | shtml>
; D1 <body>
#BHEU @BlackHatEvents
```

## Slide 42

###### Showcases

> loader from createPackageContext

> loader.loadClass(“.Screen”) > Create .Sreen Evil Twin

> Create intent with an appScreen + url extra > startActivity(intent)

#BHEU @BlackHatEvents

## Slide 43

###### Takeaways

###### ▪ **You don’t own your ClassLoader**

▪ **Avoid exposing Parcelable or Serializable objects in exported components**

▪ **Exploitation may be just an app away**

#BHEU @BlackHatEvents

## Slide 44

**_about: // this_briefing_**

## **Questions ?**

**_@_ ch0pin**

**/in/valsamaras**

**/ch0pin**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat a ~~
EUROPE 2024
Questions ?
/in/valsamaras y @chOpin
/chOpin
about: // this_briefing
#BHEU @BlackHatEvents
```
