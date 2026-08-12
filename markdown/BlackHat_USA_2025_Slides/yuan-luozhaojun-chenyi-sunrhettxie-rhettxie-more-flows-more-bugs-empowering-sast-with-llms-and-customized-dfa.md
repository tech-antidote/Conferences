---
title: "More Flows, More Bugs Empowering SAST with LLMs and Customized DFA"
speakers: ["Yuan Luo", "Zhaojun Chen", "Yi Sun", "Rhettxie Rhettxie"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Yuan Luo&Zhaojun Chen&Yi Sun&Rhettxie Rhettxie_More Flows, More Bugs Empowering SAST with LLMs and Customized DFA.pdf"
pages: 47
sha256: "a954eb15e47c0d8a2ea00252a8595f5433cf305ef381853fa6cb224fbee3da87"
text_chars: 25117
ocr_pages: 4
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:04:16Z"
---
# More Flows, More Bugs Empowering SAST with LLMs and Customized DFA

**Speakers:** Yuan Luo, Zhaojun Chen, Yi Sun, Rhettxie Rhettxie  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Yuan Luo&Zhaojun Chen&Yi Sun&Rhettxie Rhettxie_More Flows, More Bugs Empowering SAST with LLMs and Customized DFA.pdf` (47 pages)


## Slide 1

## More Flows, More Bugs: Empowering SAST with LLMs and Customized DFA

Yuan Luo & Zhaojun Chen & Yi Sun & Rhettxie @Tencent Security YunDing Lab

#BHUSA @BlackHatEvents

## Slide 2

### Outline

- ➢ Introduction to SAST

- ➢ How to use LLM to recognize Sources & Sinks

- ➢ DFA (Data Flow Analysis) Enhancement

- ➢ Results

#BHUSA @BlackHatEvents

## Slide 3

#### What is SAST?

- ⚫ Static Application Security Testing (SAST)

   - Analyze source code without execution

- ⚫ Scans code for bugs

   - Such as SQL injection or XSS, acting like an X-ray

- ⚫ Essential part of DevSecOps

   - Integrated into CI/CD pipelines

- ⚫ Popular tools

###### DevSecOps Lifecycle Diagram

- CodeQL/Fortify/SonarQube/Checkmarx/...

Source: https://www.mend.io/blog/sast-static-application-security-testing/

#BHUSA @BlackHatEvents

## Slide 4

#### What is CodeQL?

###### **Background**

- ⚫ Founded in 2006, GitHub acquired CodeQL in 2019

- ⚫ Queries and libraries are open-source

- ⚫ The core CodeQL engine is proprietary

###### Source code

###### Build database

###### **Workflow**

- ⚫ Preparing the code

- ⚫ Creating a CodeQL database

- ⚫ Running CodeQL queries against the database

- ⚫ Interpreting the query results

###### Query Results

###### QL query

#BHUSA @BlackHatEvents

Source: https://codeql.github.com/

## Slide 5

#### No bugs anymore?

Many vulnerabilities found…

Periodically perform code scanning on the default branch and pull requests

#BHUSA @BlackHatEvents

## Slide 6

#### However, SAST tools may overlook …

Our attempts to detect recent critical RCE vulnerabilities using CodeQL revealed two main causes for **false negatives** :

1. Incomplete **source and sink** coverage in built-in propagation rules.

2. Disruptions in data flow due to insufficient support for certain **language features** .

|**CVE**|**Description**|**Root causes for**
**missed detection**|
|---|---|---|
|CVE-2024-47552
CVE-2024-56180
CNVD-2023-45001|Apache Seata, Apache EventMesh, Alibaba Nacos JRaft
vulnerability; other affected applications include Apache Ignite and
Apache HugeGraph.|Missing source rule|
|CVE-2024-37084|Spring Cloud Data Flow Remote Code Execution Vulnerability|Missing summary rule|
|CVE-2024-22263|Spring Cloud Data Flow Arbitrary File Write Vulnerability|Missing summary rule|
|CVE-2023-52251|Kafka UI Background Messages Groovy Code Execution
Vulnerability|Code pre-generation|
|CVE-2023-34050|Spring AMQP Deserialization Vulnerability|Asynchronous
Method Reference|
|CVE-2023-37582|Apache RocketMQ NameServer Remote Code Execution
Vulnerability|Reflection
Cross-Thread|
|CVE-2023-33246|Apache RocketMQ Remote Code Execution Vulnerability|Reflection
Cross-Thread|
|CVE-2023-46604|Apache ActiveMQ Remote Code Execution Vulnerability|Cross-Thread
Missing sink rule|
|CVE-2023-25194
…|Apache Kafka JAAS JNDI Injection Vulnerability
…|Missing source rule
Missing summary rule
Missing sink rule
…|

#BHUSA @BlackHatEvents

## Slide 7

How to use LLM to recognize Sources & Sinks

## Slide 8

#### Current Methods Depend on Human Effort

Manual Definition

###### Community Contributions

Labor-intensive. Any automated methods?

#BHUSA @BlackHatEvents

## Slide 9

Where to find Sources and Sinks?

Developers implement functionality using third-party frameworks (using APIs).

The API implementation is included in the framework's open-source code

Scan open-source frameworks and detect Sources and Sinks

#BHUSA @BlackHatEvents

## Slide 10

#### How LLMs can help?

- ⚫ Discover Agent

   - Discover possible functions from frameworks

- ⚫ Judge Agent

   - Use expert rules to verify

- ⚫ Validation Agent

   - Verify sources/sinks are used in real-world repos

The workflow of our method

#BHUSA @BlackHatEvents

## Slide 11

#### Discover Agent – How to find source/sink functions?

##### ◼ File-Level Coarse-Grained Filtering

###### Source code file

###### LLM prompt. The prompts vary depending on different LLMs.

You are a cybersecurity expert. You are given a source code file written in the Go programming language. Identify functions in the source code that send HTTP requests. Such functions could be labeled as potential HTTP sinks for taint analysis. If no such functions exist, answer "None" directly. If such functions exist, return the function name, concrete code context, and confidence score as a JSON in the following format:

- { "method": <method name>, "code": <code context that send HTTP requests>, "score": <confidence score>}.

Do not provide explanations or comments; just output the JSON. If there are multiple functions, list all functions.

- [start of Go source code]

- {source code}

- [end of Go source code]

###### Tencent HunYuan

###### Functions list

- { "method": "Get”}

- { "method": ”Post”}

###### Score filter

You can change the threshold to get more or fewer functions.

###### LLM results

- { "method": "Get", "code": "func (r *Request) Get(url string) (*Response, error) { return r.Execute(MethodGet, url) }", "score": 0.9 }

- { "method": "AddRetryConditions", "code": "func (r *Request) AddRetryConditions(conditions ...RetryConditionFunc) *Request { r.retryConditions = append(r.retryConditions, conditions...) return r}", "score": 0.1 }

#BHUSA @BlackHatEvents

## Slide 12

Discover Agent – How to remove false positives? ◼ Function-Level Filtering

###### Function name and body

###### LLM prompt for SSRF Sink detection

You are a cybersecurity expert. Determine if the following function is a sink for SSRF vulnerabilities by checking if it sends HTTP requests. If it does, answer "YES". If not, answer "NO". Do not explain or comment.

###### Source/Sink functions for each framework

Discard, if it does not meet standards

#BHUSA @BlackHatEvents

## Slide 13

#### Judge Agent

   - We need to combine expert experience

- ⚫ The function should be publicly accessible. (Source/Sink)

- ⚫ The function should not read authentication credentials and key information. (Source/Sink)

###### Function body

- ⚫ The function should have return values that propagate tainted data. (Source)

- ⚫ The return value of the function should not be of the Bool type. (Source)

- **+**

- ⚫ The function should accept inputs from untrusted sources. For example, user input (web forms,

cookies, URL parameters), external files, network data, environment variables, etc. (Source)

- ⚫ The function should create or execute a SQL query. (Sink-SQL)

- ⚫ The function should send HTTP requests. (Sink-SSRF)

⚫

###### Conduct expert rule checks on functions using LLMs

#BHUSA @BlackHatEvents

## Slide 14

Validation Agent - How to ensure functions are used in real-world repos? ◼ Run queries on real-world repos

###### Retrieve the framework's dependent repositories

###### Get the source code of these repositories

- ⚫ Incorporate identified sources and sinks into SAST tools (e.g., CodeQL)

- ⚫ Verify the presence of these sources and sinks

Finally, we get new sources and sinks!

#BHUSA @BlackHatEvents

## Slide 15

DFA (Data Flow Analysis) Enhancement

## Slide 16

#### CodeQL DFA Implementation Mechanism

◼ What is the execution principle of DFA (Data flow analysis) queries?

Data Flow Example

?

DFA Result
Taint
Data PathNode
Edge
Flow
(Node & AccessPath)
Graph
AccessPath
Node

In the following examples, note that:

1. CodeQL version is 2.17.2.

2. We define that the arguments to the main method serve as the **_source_** , and the arguments to the System.out.println method serve as the **_sink_** .

#BHUSA @BlackHatEvents

## Slide 17

#### CodeQL DFA Implementation Mechanism

PathNodeImpl Stage4/3/2 Utils
• isSource • revFlow • revFlow
• isSink • fwdFlow • fwdFlow
• pathSuccPlus • revFlow • sourceNode
• flowPath
• directReach • fwdFlow • sinkNode
• … • pathStep • viableCallable
• …
User Interface Stage5 Stage1

- ⚫ The user implements taint analysis by inheriting the **_DataFlow::ConfigSig_** interface and then calling the **_flowPath_** interface.

- ⚫ The **_fwdFlow_** begins at the source to identify potential data flow propagation points, while **_revFlow_** starts from the sink to trace back the origins of propagation points. They target the **_Node_** , and together they form the complete **_source-to-sink_** path.

- ⚫ From Stage 5 to Stage 1, the logic is similar, differing only in context, with the ultimate goal of obtaining the **_AccessPath_** .

#BHUSA @BlackHatEvents

## Slide 18

#### CodeQL DFA Implementation Mechanism

◼ How to calculate the Node?

|**Step**|**Demo**|**Description**|
|---|---|---|
|**Source**||Taint analysis source node.|
|**Local Flow**|mid = "taint";
node = mid;|Intra-procedural analysis, if a mid-node exists and can propagate to a node within the
program, then that node is also considered a point in the flow.|
|**Jump**||Custom extension methods provided for users can be implemented through
**_AdditionalValueStep_**.|
|**Store**|node.filed = mid;
node[x] = mid;|Assign values to fields, arrays, collections, maps, etc.|
|**Load**|node = mid.filed;
node = mid[x];|Retrieve values from fields, arrays, collections, maps, and so on.|
|**Call In**|public void m(param){
this.f=param;
}
o.m(arg);|Inter-procedural analysis, propagation during method invocation:
1. Propagation from actual argument**_arg_**to formal parameter**_param_**.
2. Propagation from the method call qualifier (**_o_**) to the**_this_**parameter of the method.|
|**Call Out**|public Object m(param){
ret=source;
return ret;
};
r=o.m(arg);|Specifically, the return value ret is not propagated from parameters, but from sources such
as source points. In this case:
1.**_ret_**propagates to the expression**_o.m(arg)_**.|
|**Call Through**|public Object m(param, o){
ret=param;
o.field=param;
return ret;
};
r=o.m(arg, obj);|Specifically, the return value ret is propagated from the parameters. In this example:
1.**_ret_**propagates to the expression**_o.m(arg, obj)._**
2.**_o[post update][field]_**propagates to**_obj[post update][field]._**|

#BHUSA @BlackHatEvents

## Slide 19

CodeQL DFA Implementation Mechanism ◼ What is AccessPath?

###### **_Content_**

###### **_AccessPath_**

- Content is a description of the way data may be stored inside an object.

- Different object type has different content, as follows:

- AccessPath records the **_content_** propagation relationships for the four types of nodes (Field, Array, Collection, and Map) in Store/Load propagation. It consists of **_a content list_** and **_a type_** .

|**Object Type**|**Demo Code**|**Content**|
|---|---|---|
|**Field**|Person p = new Person();
p.name =taint;|name|
|**Array**|String[] ts = new String[1];
ts[0] =taint;|[]|
|**Collection**|ArrayList<String> ts = new ArrayList<>();
ts.add(taint);|<element>|
|**MapKey**|HashMap<String, int> ts = new HashMap<String, int>();
ts.put(taint,1);|<map.key>|
|**MapValue**|HashMap<int, String> ts = new HashMap<int, String>();
ts.put(1,taint);|<map.value>|

|**Object Type**|**Demo Code**|**AccessPath**|
|---|---|---|
|**Field**|Person p = new Person();
p.name = taint;|[name] : String|
|**Array**|String[] ts = new String[1];
ts[0] = taint;|[[]] : String|
|**Collection**|ArrayList<String> ts = new ArrayList<>();
ts.add(taint);|[<element>]: String|
|**MapKey**|HashMap<String, int> ts = new HashMap<String, int>();
ts.put(taint,1);|[<map.key>] : String|
|**MapValue**|HashMap<int, String> ts = new HashMap<int, String>();
ts.put(1, taint);|[<map.value>] :
String|

###### ⚫ Assuming that **_taint_** is a taint **_Node_** , type String.

###### ⚫ The red mark indicates the corresponding **_Node_** .

#BHUSA @BlackHatEvents

## Slide 20

#### CodeQL DFA Implementation Mechanism

◼ How to calculate the AccessPath?

|**Stage**|**AP**|**Description**|**Demo**|
|---|---|---|---|
|**Stage1**|Unit|No explicit access paths; tracks candidate content operations
(storeStepCand, readStepCand) that will form access paths.|-|
|**Stage2**|Boolean|Boolean access paths (true for non-empty, false for empty), introducing
coarse pruning based on whether any dereference exists.|true|
|**Stage3**|ApproxAccessPath
Front|Single-content approximation (ApproxAccessPathFront), tracking the first
content operation to refine pruning.|[]
<element>
<map.key>
<map.value>
approximated field a to approximated field z|
|**Stage4**|AccessPathFront|Precise single-content tracking (AccessPathFront), with content clearing
to eliminate invalid paths.|[]
<element>
<map.key>
<map.value>
ps1
ps2
ps3
ps4|
|**Stage5**|AccessPathApprox|Type-safe access paths (AccessPathApprox), tracking up to two
contents or an approximated tail, with type checking and cost-based
pruning.|[ps1, [], …(3)]
[ps2, <element>, …(3)]
[ps3, <map.value>, …(3)]
[ps4, <map.key>, …(3)]|
|**PathNodeIm**
**pl**|AccessPath|Precise access paths (AccessPath), representing full sequences of
contents (or approximations for expensive cases), integrated into the
final path graph for accurate data flow paths.|[ps1, [], name] : String
[ps2, <element>, name] : String
[ps3, <map.value>, name] : String
[ps4, <map.key>, name] : String|

#BHUSA @BlackHatEvents

## Slide 21

#### Language-specific Limitations

◼ Java as an example

Cross Thread

Reflection

Value Passing

…

#BHUSA @BlackHatEvents

## Slide 22

#### Java Cross-Thread

In the following examples, we agree that:

1. The parameters of the static main method serve as **_source_** . 2. The parameters of the System.out.println method serve as **_sink_** .

###### Runnable Instance Constructor Call

sink
jump
source

- ⚫ When the taint node ( **_tt_** ) is positioned in the constructor call of a Runnable subclass.

- ⚫ Jump from the **_constructor call expression_** of a Runnable subclass to the instance parameter ( **_this_** ) of **_run_** method.

#BHUSA @BlackHatEvents

## Slide 23

#### Java Cross-Thread

◼ How to jump?

Jump API: **AdditionalValueStep**

/** Value step from the constructor call of a `Runnable` to the instance parameter (this) of `run`. * * Class MyRunnable implements Runnable{ * public void run(){} * } * MyRunnable m = new MyRunnable(xxx) * additional step: * from: new MyRunnable(xxx) * to: MyRunnable#run#this */ private class RunnableConstructorCallToRunStep extends AdditionalValueStep { override predicate step(Node pred, Node succ) { exists(ConstructorCall cc, Method m | m.getDeclaringType() = cc.getConstructedType().getSourceDeclaration() and cc.getConstructedType().getAnAncestor().hasQualifiedName("java.lang", "Runnable") and m.hasName("run") | pred.asExpr() = cc and succ.(InstanceParameterNode).getEnclosingCallable() = m ) } }

#BHUSA @BlackHatEvents

## Slide 24

#### Java Cross-Thread

Thread start

jump

- ⚫ When the taint node ( **_tt_** ) is positioned after the constructor call of a Thread subclass and before the start method.

- ⚫ Jump from the Thread instance ( **_T1_** ) initiating the start() call to the **_this_** reference within the run method's execution context.

#BHUSA @BlackHatEvents

## Slide 25

#### Java Cross-Thread

Field Update
jump

- ⚫ When the taint node( **_tt_** ) is positioned after the constructor call and the start method.

- ⚫ Jump from the Runnable instance PostUpdateNode parameter ( **_this[post update]_** ) of a store operation to the instance parameter ( **_this_** ) of the run method.

#BHUSA @BlackHatEvents

## Slide 26

#### Java Reflection

###### Invoke Call

To enable Java reflection analysis in CodeQL, including operations like method invocation, we face the following difficulties:

Call Through

1. How to locate method invoked.

Call In

2. The previous propagation flow rules for **_Call In/Call Through_** in Data Flow are no longer applicable and require patching.

#BHUSA @BlackHatEvents

## Slide 27

#### Java Reflection

◼ Challenge1: How to locate method invoked ?

###### Trace Class instance

obj.Class Trace Method instance obj.getClass() Class.forName(className) class.getMethod(name, …) ClassLoader.loadClass(name, …) class.getMethods() class.getDeclaredMethod(name, …) class.getDeclaredMethods()

###### Trace invoke call

method.invoke(obj, args…)

Positioning method Method(…)

   - Through **_Class instance tracking_** , **_Method instance tracking_** , and **_Invoke call tracking_** , the location of the invoked method can be pinpointed.

   - Every trace requires global DataFlow.

- Solid line indicates confirmed transmission links.

- Dashed line indicates potential transmission links.

#BHUSA @BlackHatEvents

## Slide 28

#### Java Reflection

◼ Challenge2: How to Patch CodeQL data flow analysis (DFA)?

**_AdditionalValueStep_** does not work because

of **_Non-monotonic recursion_** .

1. To achieve reflection analysis, we need to

   - use the global DataFlow.

2. And then connect the Call In/Call Through rules with AdditionalValueStep.

3. But the global DataFlow depends on AdditionalValueStep.

user defined
AdditionalValueStep
AdditionalValueStep
user uses the
DataFlow interface
DataFlowCommonImpl
to locate the
reflection methods
DataFlowImp DataFlow

#BHUSA @BlackHatEvents

## Slide 29

#### Java Reflection

◼ Challenge2: Patch CodeQL data flow analysis (DFA).

Patched DataFlow
Module
DataFlowImpl DataFlow
DataFlowCommonImpl
DataFlow
Reflection Patches
DataFlowCommonImpl DataFlow
DataFlow Module
DataFlowImp
Replica

Invoke reflection data propagation policy

r = method.invoke(obj, arg1, …)
Method(param1, …){ this …; return ret;}

Step Demo Policy
1.  arg  propagates to the  param.
Call In
2.  obj  propagates to  parameter this.
public object m(param,…){
…
return ret; 1. ret  propagates to the method call expression
} (m.invoke(obj, arg, …))
Call
r = m.invoke(obj, arg, …); 2. If there is a  PostUpdateNode  in the method,
Through
it should also be propagated to the
corresponding  obj/arg[post update] .

#BHUSA @BlackHatEvents

## Slide 30

#### Java Reflection

Invoke Call
3
4
2
1

⚫ As can be seen from the results, by supporting Java reflection, taint node **_s_** can propagate to **_obj[name]._**

#BHUSA @BlackHatEvents

## Slide 31

#### Java Value Passing

- What is Java Value Passing?

In Java, the way to pass actual parameters to methods is

###### **_pass-by-value_** :

- ⚫ If the parameter is a primitive type, it's straightforward; what is passed is a copy of the literal value of the primitive type, and a copy is created.

- ⚫ If the parameter is not a primitive type, what is passed is a copy of the address value in the heap of the object

referenced by the actual parameter, and similarly, a copy is created.

#BHUSA @BlackHatEvents

## Slide 32

#### Java Value Passing

- What is the problem?

However, the CodeQL Java parameter passing model may miss some instances when multiple copies of non-primitive type parameters exist.

- ⚫ Both **_p_** and **_d.a_** are instances of the Person class, pointing to the same object, which is a copy of the heap address of that object.

- ⚫ In the CodeQL analysis flow, the analysis considers that **_d.a_** has changed but cannot track **_pn_** .

- ⚫ Actually, the final **_pn_** is also tainted.

#BHUSA @BlackHatEvents

## Slide 33

#### Java Value Passing

- How to support multiple copies of non-primitive type parameters value passing?

###### Taking the copy stored in a **_Field_** as an example.

1. Locate the **_field_** that is **_non-primitive_** .

2. For this field, find its **_store_** operations, identifying both **_nonPostUpdateNode_** and _PostUpdateNode_ nodes.

3. For **_non-PostUpdateNode store_** operations, use **_global data flow_** to locate the parameter **_param_** and the actual argument **_arg_** .

4. For another **_store_** operation of **_PostUpdateNode_** , add a mapping from this node to **_arg_** .

Tips:

- ⚫ Implementation may lead to **non-monotonic recursion,** as

   - shown in the Java Reflection Solution.

#BHUSA @BlackHatEvents

## Slide 34

#### Java Value Passing

◼ Why must use global data flow ？

###### Inter-procedural Call

###### Array Store & Read

###### Map Store & Read

#BHUSA @BlackHatEvents

## Slide 35

Results of research

## Slide 36

#### Newly discovered sources/sinks

###### Statistics on Newly Discovered Sources and Sinks for Popular Golang Frameworks

###### Scanned 5,000+ repositories, detecting a >15% increase in data flows

#BHUSA @BlackHatEvents

## Slide 37

#### Case study - CVE-2024-45387

SQL injection vulnerability in Traffic Ops in Apache Traffic Control

Automated Vulnerability Scanning with CodeQL

#BHUSA @BlackHatEvents

## Slide 38

#### CVE-2024-45387 – Data flow

###### Read parameters from user input

###### Process parameters from HTTP requests

###### Validate request parameters

###### Insert comments into the database

###### QueryRowx

#BHUSA @BlackHatEvents

## Slide 39

#### The sink function was omitted…

###### The _QueryRowx_ function in the _sqlx_ framework was omitted in CodeQL

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€Q
black hat
BRIEFINGS
The sink function was omitted...
The QueryRowx function in the sq/x framework was omitted in CodeQL
- addsTo:
pack: codeql/go-all
extensible: sinkModel
data:
- ["github.com/jmoiron/sqlx", "DB", True, "Get", "",
- ["github.com/jmoiron/sqlx", "DB", True, "MustExec", "", "", "“Argument[@]", “sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "DB", True, "NamedExec", "", "", "“Argument[@]", "sql-injection", “manual"]
- ["github.com/jmoiron/sqlx", "DB", True, "NamedQuery", , , "Argument[0]", "sql-injection", “manual"]
- ["github.com/jmoiron/sqlx", "DB", True, "“Queryx", "", "", “Argument[@]", "“sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "DB", True, "Select", "", "", "Argument[1]", “sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "Get", "", "", “Argument[1]", "sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "MustExec", , » "Argument[0]", "sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "NamedExec", , » "Argument[@]", "sql-injection", “manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "“NamedQuery", "", "", “Argument[@]", “sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "“Queryx", "", "", "Argument[@]", “sql-injection", "manual"]
- ["github.com/jmoiron/sqlx", "Tx", True, "Select", "", "", "Argument[1]", “sql-injection", "manual"]
» “Argument[1]", "sql-injection", "“manual"]
```

## Slide 40

#### Our method found this sink and thus the vulnerability

Our method reported the sink function

Vulnerable code snippet

err := inf.Tx.QueryRowx(selectQuery() + `WHERE dsrc.id=` + inf.Params["id"]).StructScan(&current)

#BHUSA @BlackHatEvents

## Slide 41

#### Reproduced historical CVEs

CVE-2024-47552 Apache Seata, Apache EventMesh, Alibaba Nacos JRaft vulnerability; other affected applications CVE-2024-56180 Missing source rule include Apache Ignite and Apache HugeGraph. CNVD-2023-45001

source
sink
#BHUSA @BlackHatEvents

## Slide 42

#### Reproduced historical CVEs

CVE-2023-46604

Apache ActiveMQ Remote Code Execution Vulnerability

Cross-Thread Missing sink rule

source

socket.getInputStream TcpTransport#initializeStreams 1 TcpTransport#connect TcpTransport#doStart TransportThreadSupport#doStart

2

sink

5

Cross-Thread Jump

3

TcpTransport#run TcpTransport#doRun TcpTransport#readCommand OpenWireFormat#unmarshal OpenWireFormat#doUnmarshal BaseDataStreamMarshaller#tightUnmarsalThrowable BaseDataStreamMarshaller#createThrowable

4

#BHUSA @BlackHatEvents

## Slide 43

#### Reproduced historical CVEs

CVE-2023-37582 Apache RocketMQ NameServer Remote Code Execution Vulnerability

Reflection Cross-Thread

⚫ Just explain the Java reflection analysis in it

#BHUSA @BlackHatEvents

## Slide 44

#### CVEs we discovered

- 5 new disclosed vulnerabilities, some cases below

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
CVEs we discovered
JEKCVE-2024-45387 Detail
Description AKCVE-2024-45794 Detail
An SQL injection vulnerability in Traffic O
"operations", "portal", or "steering" to ex Descri ption
recommended to upgrade to version Apa deviron is an open source tool int AKCVE-2024-43406 Deta il
could utilize and exploit SQL Injec
Metrics CVSS Version 4.0 been addressed in version 0.7.2 a
NVD enrichment efforts reference publicly ava
CVSS 3.x Severity and Vector String
Description
LF Edge eKuiper is a lightweight loT data analytics and stream processing engine running on resource-constraint edge devices. A user could
utilize and exploit SQL Injection to allow the execution of malicious SQL query via Get method in sqlKvStore. This vulnerability is fixed in
1.14.2.
Metrics [| cvss versi
\ \ NIST: NVD Bz NVDenrichment efforts reference pui
CVSS 3.x Severity and Vecta
Ya CNA: Apache Bi \ NIST: NVD
Software Foundation
Metrics | cvssversion4.0 (RASSNGEERER@N CVSS Version 2.0
Va CNA: GitHub, Inc. NVD enrichment efforts reference publicly available information to associate vector strings. CVSS information contributed by other sources is also displayed.
CVSS 3.x Severity and Vector Strings:
Ww CNA: GitHub, Inc. Base Score: [BBHIGHy Vector: CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
```

## Slide 45

### Takeaways

➢ Semantic analysis of code in SAST is particularly suitable for LLMassisted analysis, and their combination is a research direction.

➢ CodeQL's data flow analysis mechanism is highly representative, serving as a good start for learning data flow analysis.

➢ CodeQL's data flow analysis is not perfect and can be studied, modified, and improved.

#BHUSA @BlackHatEvents

## Slide 46

# **Q & A**

leonyuanluo@tencent.com zzzzjchen@tencent.com landonsun@tencent.com jitxie@tencent.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘black hat
RIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
eonyuanluo@tencent.com
zzzzjchen@tencent.com FHSS Fee
jixie@tencent.com
#BHUSA @BlackHatEvents
```

## Slide 47

# **Thank you!**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
~ biaekhat
RIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Thank you!
```
