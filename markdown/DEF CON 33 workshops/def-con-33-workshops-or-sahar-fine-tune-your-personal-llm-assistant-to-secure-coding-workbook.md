---
title: "Fine Tune your personal LLM assistant to Secure coding"
speakers: ["Or Sahar"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33 workshops/DEF CON 33 - Workshops - Or Sahar - Fine Tune your personal LLM assistant to Secure coding - Workbook.pdf"
pages: 26
sha256: "64a8c54d79a942320073838b7a344aa794f815ba8d3949fad4798b75ae495705"
text_chars: 48148
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T06:33:37Z"
---
# Fine Tune your personal LLM assistant to Secure coding

**Speakers:** Or Sahar  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33 workshops/DEF CON 33 - Workshops - Or Sahar - Fine Tune your personal LLM assistant to Secure coding - Workbook.pdf` (26 pages)


## Slide 1

Fine Tune your personal LLM assistant to Secure coding Workshop

Or Sahar & Yariv Tal, Secure From Scratch

2025

1

## Slide 2

# **1 Information & Preparation**

   -  Duration - 4 hours

   -  Attendees - 30 Max

   -  Categories - Machine Learning and Security;Web Application Security

   -  Attendees will actively engage by designing prompts for different coding scenarios, finetuning their own LLMs, and building custom assistants. Each participant will work hands-on to create, test, and iterate on their own models and use cases.

   -  What knowledge, skills, or experience should the students have prior to the workshop: Basic Python programming skills

   -  **Extremely Important:** You must set up OpenAI API Access in advance (more details in this below)

   -  Hardware Requirements:

      - Laptop with at least 8GB RAM (16GB recommended)

      - Stable internet connection

      - Admin rights to install packages/tools

   -  Software Requirements:

      - Python 3.8+

      - IDE (e.g., VS Code, PyCharm)

      - Git

      - OpenAI Python SDK (openai)

- **1.1 Steps to Set Up OpenAI API Access**

   1. Sign Up or Log In

      -  Visit `https://openai.com/api` and click Start building.

      -  Sign in or create an account. Verify your email and phone number when prompted.

   2. Enable Billing

      -  Go to the left-hand menu: Billing _→_ Overview _→_ Set up paid account.

      -  Add a payment method and make an initial payment (minimum $ 5) to enable API usage.

   3. (Optional) Set a Usage Cap

      -  Navigate to Billing _→_ Usage limits.

      -  Define a soft and hard monthly limit to control expenses during the workshop.

2

## Slide 3

4. Create an API Key

   -  Go to the API Keys page and click Create new secret key.

   -  Copy the key immediately; it will not be shown again.

   -  Store it securely using an environment variable:

\```
exportOPENAI_API_KEY="sk-..."
\```

5. (Optional) Use Projects and Service Account Keys

   -  Navigate to **Projects** _→_ **Create** .

   -  Generate service-account keys if you want isolated usage quotas for exercises.

6. Sanity Test

\```
curlhttps://api.openai.com/v1/models\
\```

\```
-H"Authorization:Bearer$OPENAI_API_KEY"
\```

      -  A successful response should return a list of models.

- **1.2 Keep the treasure**

   -  Never hardcode or share API keys. Use environment variables or secure storage.

   -  Enable multi-factor authentication (MFA) for the OpenAI account.

   -  Use separate keys per project and restrict endpoints where possible.

   -  Monitor **Billing** _→_ **Usage** to track consumption during the workshop.

3

## Slide 4

# **2 Abstract**

In today’s landscape, generative AI coding tools are powerful but often insecure, raising concerns for developers and organizations alike. This hands-on workshop will guide participants in building a secure coding assistant tailored to their specific security needs.

We’ll begin by exploring the security limitations of current AI coding tools and discussing why fine-tuning is critical for secure development. Participants will then create and fine-tune their own LLM-based assistants using provided examples and their own use cases. By the end of the session, each attendee will have a functioning, security-focused AI coding assistant and a clear understanding of how to improve it further.

# **3 Outline**

1. Introduction & Security Landscape (15 min)

   -  Workshop goals and flow

   -  Risks of AI-generated code

2. Prompt Engineering for Secure Code (30 min)

   -  Principles of secure prompt design

   -  Live prompt testing with OpenAI

3. Building a Basic Secure Assistant (30 min)

   -  Using an API to generate and validate code

   -  Adding simple checks or filters

4. Fine-Tuning Overview & Prep (20 min)

   -  When to fine-tune

   -  Dataset format (JSONL), small demo

5. Hands-On: Fine-Tuning (45 min)

   -  Create a minimal dataset

   -  Run a fine-tuning job

   -  Quick test on the tuned model

6. (An) Interactive Assistant (60 min)

   -  Build a CLI or lightweight interface in Python

7. Wrap-Up & Next Steps (20 min)

   -  Summary

   -  Best practices

   -  Q&A

4

## Slide 5

# **4 The Workshop**

## **4.1 Workshop goals and flow**

These are the goals of the workshop:

-  Customize our llm for secure code generation

-  Cover security use-cases that are more complicated then merely prompting for secure code

-  Establish a methodology that will continute beyond the workshop for ongoing llm fine-tuning

-  Create a community that will share prompts for secure code generation

## **4.2 The flow**

After the introduction, we’ll cover various security-related use cases: explain them, exploit them, learn how to write prompts that return secure versions, and verify those versions.

Next, we’ll create an assistant containing all the prompt instructions we gathered. Finally, we’ll fine-tune our model to work without the assistant.

Each phase will include a demonstration followed by individual hands-on practice.

## **4.3 Risk of AI-generated code**

Is there really a problem? Does Generative AI generate insecure code?

The article “Lost at C: A User Study on the Security Implications of LLM Code Assistants” [1] describes research conducted on the risks of using coding assistants. In the study, a group of computer science students was given a set of tasks. Some were allowed to use code assistants, while others were not.

The conclusion was that the use of GenAI did not increase the number of vulnerabilities in the code. However, developers tended to accept the assistant’s suggestions blindly—meaning that if vulnerable code was suggested, they were likely to use it without making any corrections.

The experiment was conducted in the C programming language and focused on common vulnerabilities such as use-after-free, null pointer dereference, and out-of-bounds writes.

Another experiment [3] found that 16 out of 21 security-related prompts resulted in a vulnerable code snippet.

Yet another study [2] found that 40% of Copilot-generated programs contained dangerous vulnerabilities.

In conclusion, there **is** a problem: generative AI **does** generate insecure code.

## **4.4 Prompt Engeering For Secure coding**

### **4.4.1 Secure Coding Priciples**

PREVENT is an easy-to-remember acronym for secure coding prinicples:

5

## Slide 6

**P** riority, **P** rivacy, **P** ermissions: Security is the first priority

**R** edundant defenses ensure multilayerd defense in depth

**E** asy to use securely. Easy to use safely. Always prefer safe by default to safe through action

**V** erify if the components you use and your implementation are safe and whether they follow current best practices

**E** vents, **E** rrors and **E** xceptions - Log them, manage them

**N** eat code. Security through clarity. Neat code is not just easy to maintain, but also reduces undetected vulnerabilities.

**T** rust boundaries. Transferring data or control between entities with different trust levels requires pro-active action.

### **4.4.2 Prompting for Secure Coding**

-  Always ask for secure code — sometimes, simply adding the word ”secure” can make a difference.

-  If you are aware of specific risks (e.g., secure file upload), be as specific as possible in your prompt.

-  After receiving the code, ask the model to identify any vulnerabilities in the generated output.

-  Ask the model to fix the identified vulnerabilities.

-  Ask the model to fix the vulnerabilities again — it often misses issues in the first pass.

-  Compare the final version with the previous one; the model may fix one issue while unintentionally reintroducing or omitting others from earlier iterations.

### **4.4.3 Security related use cases / Best practice / Vulnerabilies**

For the following demo we used gpt4.1, please be aware that the answer isn’t always the same.

#### **Secure File Upload**

In file upload funcioanlity we have to validate the following:

-  File size - to prevent denial of service

-  File extension

-  File Magic bytes (the fixed signature at the file’s start) - reveal the real file format

-  File path - we’d better not trust the user contribued path

6

## Slide 7

##### _Demo_

1. A plain prompt for a code snippet: _develop a file upload method in c#_

The snippet:

\```
usingMicrosoft.AspNetCore.Http;
usingMicrosoft.AspNetCore.Mvc;
usingSystem.IO;
usingSystem.Threading.Tasks;
publicclassFileUploadController:Controller
{
[HttpGet]
publicIActionResultIndex ()
{
returnView ();
}
[HttpPost]
publicasyncTask <IActionResult >UploadFile(IFormFilefile)
{
if(file==null||file.Length==0)
returnContent("Nofileselected");
varpath=Path.Combine(Directory. GetCurrentDirectory (),"wwwroot/uploads",file.FileName);
//Ensurethedirectoryexists
Directory. CreateDirectory (Path. GetDirectoryName (path));
using(varstream=newFileStream(path ,FileMode.Create))
{
awaitfile. CopyToAsync (stream);
}
returnContent("Fileuploadedsuccessfully !");
}
}
\```

2. Prompting for a secure snippet: _develop a secure file upload method in c#_

## The snippet:

\```
usingMicrosoft.AspNetCore.Http;
usingMicrosoft.AspNetCore.Mvc;
usingSystem.IO;
usingSystem.Threading.Tasks;
[Route("api/[ controller]")]
[ ApiController ]
publicclassFileUploadController:ControllerBase
{
privatereadonlystring []permittedExtensions={".txt",".jpg",".png",".pdf"};
privateconstlongmaxFileSize=10*1024*1024;//10MB
[HttpPost("upload")]
publicasyncTask <IActionResult >UploadFile(IFormFilefile)
{
if(file==null||file.Length==0)
returnBadRequest("Nofileuploaded.");
//Checkfilesize
if(file.Length>maxFileSize)
returnBadRequest("Filesizeexceedsthelimit.");
//Calculatehashofthefileorvalidatefurtherifneeded
//Checkfileextension
varext=Path. GetExtension (file.FileName). ToLowerInvariant ();
if(string. IsNullOrEmpty (ext)||Array.IndexOf(permittedExtensions ,ext)<0)
{
returnBadRequest("Invalidfileextension.");
}
varfilePath=Path.Combine("uploads",Guid.NewGuid ().ToString ()+ext);
//Savethefile
using(varstream=System.IO.File.Create(filePath))
{
awaitfile. CopyToAsync (stream);
\```

7

## Slide 8

\```
}
returnOk(new{filePath});
}
}
\```

This is almost what we need - but it doesn’t include magic bytes testing.

An attacker can rename _evil.exe_ to _cute.jpg_ ; the browser and server both see “.jpg”, yet the content is still executable.

3. After we put some more thought and effort into the prompt: _develop a secure file upload method in c#, make sure to check the magic bytes_

The snippet:

`using Microsoft.AspNetCore.Http; using System; using System.IO; using System.Threading.Tasks; using System. Collections .Generic;` _`// Magic Bytes for common types`_ `public static class MagicBytes { public static readonly Dictionary <string , byte[]> FileSignatures = new () {` _`// JPG`_ `{ ".jpg", new byte [] { 0xFF , 0xD8 , 0xFF } },` _`// PNG`_ `{ ".png", new byte [] { 0x89 , 0x50 , 0x4E , 0x47 } },` _`// PDF`_ `{ ".pdf", new byte [] { 0x25 , 0x50 , 0x44 , 0x46 } },` _`// ZIP`_ `{ ".zip", new byte [] { 0x50 , 0x4B , 0x03 , 0x04 } } }; public static bool HasValidSignature (string extension , Stream fileStream) { if (! FileSignatures .ContainsKey(extension.ToLower ())) return false; var signature = FileSignatures [extension.ToLower ()]; var buffer = new byte[signature.Length ]; fileStream.Position = 0; fileStream.Read(buffer , 0, buffer.Length); fileStream.Position = 0; for (int i = 0; i < signature.Length; i++) { if (buffer[i] != signature[i]) return false; } return true; } } public class FileUploadHelper { private static readonly string [] permittedExtensions = { ".jpg", ".png", ".pdf", ".zip" }; private const long MAX_FILE_SIZE = 10 * 1024 * 1024;` _`// 10 MB`_ `public static async Task <string > UploadAsync (IFormFile file , string uploadPath) { if (file == null || file.Length == 0) throw new ArgumentException ("File is empty"); if (file.Length > MAX_FILE_SIZE ) throw new ArgumentException ("File too large"); var ext = Path. GetExtension (file.FileName). ToLowerInvariant (); if (string. IsNullOrEmpty (ext) || Array.IndexOf(permittedExtensions , ext) < 0) throw new ArgumentException ("Invalid file extension");` _`// Check magic bytes`_ `using var stream = file. OpenReadStream (); if (! MagicBytes. HasValidSignature (ext , stream)) throw new ArgumentException ("File signature does not match file extension.");` _`// Generate a safe name`_ `var safeFileName =` $ `"{Guid.NewGuid ().ToString ()}{ ext}";` _`//`_ $ _`is string interpolation`_ `var savePath = Path.Combine(uploadPath , safeFileName ); Directory. CreateDirectory (uploadPath); using var output = File.Create(savePath);`

8

## Slide 9

\```
awaitstream. CopyToAsync(output);
returnsafeFileName ;//Returnthestoredfilename.
}
}
\```

Ohhh no! The function is still not secure!

-  The helper only verifies the outer file’s magic bytes PK _\_ x03 _\_ x04, confirming it is _a valid ZIP_ , but never inspects the archive’s contents.

-  An attacker can therefore upload a ZIP containing evil.exe, macro-laden documents, gadget payloads, or a zip-bomb without detection.

#### **Why this matters**

-  Type-filter bypass: malicious code slips through a filter meant to permit only benign formats.

-  Accidental execution: any later extraction (by backend logic or an end-user) may run the payload.

-  Scanning gaps: some AV/WAF setups skip or inadequately scan embedded files.

-  Resource exhaustion: zip-bombs can consume CPU, RAM, or disk on decompression.

#### **Hardening recommendations**

- (a) If ZIP uploads are not strictly required, remove .zip from permittedExtensions.

- (b) If ZIPs are required:

   - i. Open the archive with System.IO.Compression.ZipArchive and iterate over entries.

   - ii. Reject any entry whose name ends with forbidden extensions ( `.exe` , .dll, .js, . . . ) or uses double-extension tricks (.jpg.exe).

   - iii. Block path traversal ( `../` ) and symlink entries.

   - iv. Enforce limits on total uncompressed size, entry count, and nesting depth to stop zip-bombs.

   - v. Store the file without auto-extracting; route it through AV or content-disarm mechanisms before distribution.

#### **SSRF (Server-Side Request Forgery)**

The application fetches remote resources using user-supplied URLs without proper validation, allowing attackers to trick the server into sending requests to internal services or sensitive endpoints.

To mitigate this vulnerability, implement strict URL validation:

-  Enforce https:// scheme only.

-  Resolve hostnames to IP addresses and validate them before making the request.

9

## Slide 10

-  Maintain a welcome-list of trusted domains and block all others.

-  Maintain a welcome-list of IPs that don’t include private, loopback, and link-local IP ranges.

_Demo_

1. A plain prompt for a code snippet:

_Write a C# API method that displays a website preview for a user-supplied URL_

## The snippet:

`using Microsoft.AspNetCore.Mvc; using System.Net.Http; using System.Threading.Tasks; using System.Text. RegularExpressions ; using System.Web; [ ApiController ] [Route("api /[ controller]")] public class WebsitePreviewController : ControllerBase { [HttpGet] public async Task <IActionResult > GetPreview ([ FromQuery] string url) { if (string. IsNullOrWhiteSpace (url)) return BadRequest("URL required.");` _`// Basic URL validation ; you might want to use a more robust approach`_ `if (!Uri.TryCreate(url , UriKind.Absolute , out var uriResult)) return BadRequest("Invalid URL."); try { using var client = new HttpClient (); client. DefaultRequestHeaders .UserAgent.ParseAdd("Mozilla /5.0 (compatible)"); var html = await client. GetStringAsync (url); var title = Regex.Match(html , @"<title >\s*(.+?)\s*</title >", RegexOptions .IgnoreCase).Groups [1]?. Value ?? ""; var descMatch = Regex.Match(html , @"<meta\s+name =["" ’]description ["" ’]\s+content =["" ’](.+?)["" ’]",` _�→_ `RegexOptions .IgnoreCase); var ogTitleMatch = Regex.Match(html , @"<meta\s+property =["" ’]og:title["" ’]\s+content =["" ’](.+?)["" ’]",` _�→_ `RegexOptions .IgnoreCase); var ogDescMatch = Regex.Match(html , @"<meta\s+property =["" ’]og:description["" ’]\s+content =["" ’](.+?)["" ’]",` _�→_ `RegexOptions .IgnoreCase); var ogImgMatch = Regex.Match(html , @"<meta\s+property =["" ’]og:image["" ’]\s+content =["" ’](.+?)["" ’]",` _�→_ `RegexOptions .IgnoreCase); var preview = new { url , title = HttpUtility.HtmlDecode( ogTitleMatch .Groups [1]. Value) ?? HttpUtility .HtmlDecode(title), description = HttpUtility .HtmlDecode(ogDescMatch.Groups [1]. Value) ?? HttpUtility.HtmlDecode(descMatch.Groups [1]. Value), image = ogImgMatch.Groups [1]. Value }; return Ok(preview); } catch ( HttpRequestException ) { return NotFound("Could not fetch the URL."); } catch { return StatusCode (500 , "An error occurred while processing the URL."); } } }`

This code is vulnerable to SSRF (Server-Side Request Forgery) because it fetches the content of a user-supplied URL without enforcing any restrictions or validation on the destination. An attacker can exploit this by providing internal or sensitive URLs (e.g., ‘http://localhost:5000/admin‘, ‘http://169.254.169.254‘) to trick the server into making requests on their behalf. Since the server performs the request, it may reach internal services not exposed to the public, potentially leaking sensitive data or enabling further attacks such as internal port scanning or access to metadata services.

10

## Slide 11

## 2. Prompting for a secure snippet:

_Write a secure C# API method that displays a website preview for a user-supplied URL_

The snippet:

\```
usingSystem;
usingSystem.Net;
usingSystem.Net.Http;
usingSystem.Net.Sockets;
usingSystem.Text. RegularExpressions ;
usingSystem.Threading.Tasks;
usingHtmlAgilityPack ;
usingMicrosoft.AspNetCore.Mvc;
[ ApiController ]
[Route("api/[ controller]")]
publicclassPreviewController:ControllerBase
{
privatestaticreadonlyHttpClienthttpClient=newHttpClient
{
Timeout=TimeSpan.FromSeconds (5)//Shorttimeout
};
[HttpGet("website -preview")]
publicasyncTask <IActionResult >GetWebsitePreview ([ FromQuery]stringurl)
{
try
{
//1.ValidateURLformatandscheme
if(!Uri.TryCreate(url ,UriKind.Absolute ,outvaruri)||
(uri.Scheme!=Uri. UriSchemeHttp&&uri.Scheme!=Uri. UriSchemeHttps ))
{
returnBadRequest("InvalidURL.");
}
//2.PreventSSRF:Blocklocalhost ,privateIPs ,etc.
if( IsLocalOrPrivateAddress (uri))
{
returnBadRequest("ForbiddenURL.");
}
//3.Fetchthepagecontentsecurely
varresponse=awaithttpClient.GetAsync(uri);
if(! response. IsSuccessStatusCode )
{
returnBadRequest("Failedtoretrievethewebsite.");
}
if(response.Content.Headers.ContentType ?. MediaType!="text/html")
{
returnBadRequest("URLisnotaHTMLpage.");
}
stringhtml=awaitresponse.Content. ReadAsStringAsync ();
//4.Parseandextractpreview(title ,description )
vardoc=newHtmlDocument ();
doc.LoadHtml(html);
stringtitle=doc. DocumentNode . SelectSingleNode ("// title")?. InnerText ?. Trim ()??"";
stringdescription=doc. DocumentNode
. SelectSingleNode ("// meta[@name=’description ’]")?
. GetAttributeValue ("content","")??"";
returnOk(new
{
Title=title ,
Description=description
});
}
catch(Exceptionex)
{
//Logex(notshownhere)
returnBadRequest("ErrorprocessingtheURL.");
}
}
//PreventSSRF:blocklocalhost ,internalIPs ,etc.
privateboolIsLocalOrPrivateAddress (Uriuri)
{
try
{
varhost=uri.Host;
//Block’localhost ’andcommonlocalhostnames
if(host.Equals("localhost",StringComparison . OrdinalIgnoreCase )
||host.Equals("127.0.0.1")
||host.StartsWith("::1")
||host.EndsWith(".local")
\```

11

## Slide 12

\```
)
{
returntrue;
}
//AttempttoresolveDNS
varaddresses=Dns. GetHostAddresses (host);
foreach(varipinaddresses)
{
if(IPAddress.IsLoopback(ip))returntrue;
//Blockprivateaddressranges :10/8 ,172.16/12 ,192.168/16 ,IPv6uniquelocaletc.
if(ip. AddressFamily==AddressFamily . InterNetwork )
{
byte []bytes=ip. GetAddressBytes ();
if(bytes [0]==10
||(bytes [0]==172&&bytes [1]>=16&&bytes [1]<=31)
||(bytes [0]==192&&bytes [1]==168))
returntrue;
}
elseif(ip. AddressFamily==AddressFamily . InterNetworkV6 )
{
if(ip. IsIPv6LinkLocal||ip. IsIPv6SiteLocal )
returntrue;
}
}
}
catch
{
returntrue;//OnDNSfailure ,erronthesafeside
}
returnfalse;
}
}
\```

The code is still vulnerable to SSRF

-  DNS-rebind (TOCTOU, Time to check time to use) – the host is resolved during validation, but HttpClient resolves it again when connecting; an attacker can return a public IP first and an internal IP seconds later, diverting the real request.

-  Automatic redirects – HttpClient follows 3xx responses by default, so a harmless URL can redirect the server to http://169.254.169.254/ or another internal endpoint after the initial check.

-  Non-canonical IP forms – dotless integers, octal/hex, mixed IPv6 representations, or broadcast addresses are not recognised by the filter yet resolve to loopback/private space.

-  Port abuse – even when the IP is external, the code allows requests to sensitive ports; there is no allow/deny list for outbound ports.

Full mitigation requires disabling auto-redirects, validating the final resolved IP after each hop, using the same resolved address for the actual socket connection, and enforcing strict host and port allow-lists.

#### **Race Condtion**

According to cwe.org [4]:

”The product checks the state of a resource before using that resource, but the resource’s state can change between the check and the use in a way that invalidates the results of the check. This can cause the product to perform invalid actions when the resource is in an unexpected state.”

12

## Slide 13

”This weakness can be security-relevant when an attacker can influence the state of the resource between check and use. This can happen with shared resources such as files, memory, or even variables in multithreaded programs.”

_Demo_

1. A plain prompt for a code snippet:

_Write C# code that exposes an API endpoint to apply a coupon to an order_

-  _Accept orderId and couponCode as input._

-  _Look up the coupon and verify it has not been used._

-  _If unused, reduce the order total by 50%._

-  _Mark the coupon as used so it cannot be applied again._

The snippet:

\```
publicclassOrder
{
publicintId{get;set;}
publicdecimalTotal{get;set;}
}
publicclassCoupon
{
publicstringCode{get;set;}
publicboolIsUsed{get;set;}
}
publicstaticclassDataStore
{
publicstaticList <Order >Orders=newList <Order >
{
newOrder{Id=1,Total=100},
newOrder{Id=2,Total=50}
};
publicstaticList <Coupon >Coupons=newList <Coupon >
{
newCoupon{Code="HALFOFF",IsUsed=false},
newCoupon{Code="USEDONE",IsUsed=true}
};
}
publicclassApplyCouponRequest
{
publicintOrderId{get;set;}
publicstringCouponCode{get;set;}
}
\```

\```
usingMicrosoft.AspNetCore.Mvc;
[ ApiController ]
[Route("api/[ controller]")]
publicclassOrdersController:ControllerBase
{
[HttpPost("apply -coupon")]
publicIActionResultApplyCoupon ([ FromBody]ApplyCouponRequestrequest)
{
//1.Lookuptheorder
varorder=DataStore.Orders. FirstOrDefault (o=>o.Id==request.OrderId);
if(order==null)
returnNotFound(new{Message="Ordernotfound."});
//2.Lookupthecoupon
varcoupon=DataStore.Coupons. FirstOrDefault (c=>c.Code==request.CouponCode);
if(coupon==null)
returnNotFound(new{Message="Couponnotfound."});
//3.Checkifcouponhasbeenused
if(coupon.IsUsed)
returnBadRequest(new{Message="Couponhasalreadybeenused."});
\```

13

## Slide 14

\```
//4.Applycoupon :50%off
order.Total*=0.5m;
//5.Markcouponasused
coupon.IsUsed=true;
returnOk(new
{
Message="Couponappliedsuccessfully .",
NewTotal=order.Total
});
}
}
\```

The coupon’s “check” (‘if (coupon.IsUsed)‘) and “update” (‘coupon.IsUsed = true‘ + discounted total) happen in separate, non-atomic operations with no lock or transaction; if two requests hit the endpoint almost simultaneously, both can see ‘IsUsed == false‘, each apply the 50 % discount, and only then set the flag—allowing one coupon to be redeemed multiple times and corrupting the order totals.

2. Prompting for a secure snippet:

_Write secure C# code that exposes an API endpoint to apply a coupon to an order._

-  _Accept orderId and couponCode as input._

-  _Look up the coupon and verify it has not been used._

-  _If unused, reduce the order total by 50%._

-  _Mark the coupon as used so it cannot be applied again._

The snippet:

\```
publicclassOrder
{
publicintId{get;set;}
publicdecimalTotal{get;set;}
}
publicclassCoupon
{
publicstringCode{get;set;}
publicboolIsUsed{get;set;}
}
\```

\```
publicstaticclassDataStore
{
publicstaticList <Order >Orders=newList <Order >
{
newOrder{Id=1,Total=100},
newOrder{Id=2,Total=50}
};
publicstaticList <Coupon >Coupons=newList <Coupon >
{
newCoupon{Code="HALFOFF",IsUsed=false},
newCoupon{Code="USEDONE",IsUsed=true}
};
}
\```

\```
publicclassApplyCouponRequest
{
publicintOrderId{get;set;}
publicstringCouponCode{get;set;}
}
\```

14

## Slide 15

\```
usingMicrosoft.AspNetCore.Mvc;
usingMicrosoft. EntityFrameworkCore ;
[ ApiController ]
[Route("api/[ controller]")]
publicclassOrdersController:ControllerBase
{
privatereadonlyAppDbContext_db;
publicOrdersController ( AppDbContextdb)
{
_db=db;
}
[HttpPost("apply -coupon")]
publicasyncTask <IActionResult >ApplyCoupon ([ FromBody]ApplyCouponRequestrequest)
{
if(string. IsNullOrWhiteSpace (request.CouponCode))
returnBadRequest("Couponcoderequired.");
//Validateorder
varorder=await_db.Orders.FindAsync(request.OrderId);
if(order==null)
returnNotFound("Ordernotfound.");
//Lookupandvalidatecoupon(usetrackingforconcurrency )
varcoupon=await_db.Coupons
.Where(c=>c.Code==request.CouponCode)
. FirstOrDefaultAsync ();
if(coupon==null)
returnBadRequest("Invalidcouponcode.");
if(coupon.IsUsed)
returnBadRequest("Couponalreadyused.");
//Apply50%discount
order.Total*=0.5m;
coupon.IsUsed=true;
try
{
await_db. SaveChangesAsync ();
}
catch( DbUpdateConcurrencyException )
{
returnConflict("Couponapplicationconflict.Tryagain.");
}
//Onlyreturnresult ,donotrevealcoupondetails .
returnOk(new{orderId=order.Id ,newTotal=order.Total});
}
}
\```

‘coupon.IsUsed‘ is still checked and updated in two separate steps, and nothing enforces atomicity: the ‘Coupons‘ table lacks a concurrency token or conditional update, so two parallel transactions can both read ‘IsUsed = 0‘, each apply the 50 % discount, set the flag, and commit successfully—no ‘DbUpdateConcurrencyException‘ is raised because EF only detects conflicts on properties marked with ‘[ConcurrencyCheck]‘ or a ‘rowversion‘ column. Database-level protection (e.g. a single ‘UPDATE . . . SET IsUsed = 1 WHERE Code = @code AND IsUsed = 0‘) or a row-version column is required to truly close the race window.

### **4.4.4 Lab Time - 30 min**

Now, let’s put our knowledge into practice

1. Go to OpenAI’s website: openai.com

2. Log in!

3. Go to the playground: platform.openai.com/playground

4. Try the file upload prompts

15

## Slide 16

-  Use a naive prompt (”Develop a file upload method in language ~~o~~ f ~~y~~ our choice)

   -  Bonus - Integrate it into a project & Exploit it!

   -  Add the word ”secure”

   -  Add a full security-aware file upload prompt

5. Repeat what you did in the previous step for SSRF, Race Condition and / or a scenario of your own choosing

## **4.5 Building a secure assistant**

One approach to improving developer security is configuring an AI assistant with securityrelated instructions embedded in its system prompt. When done correctly, this ensures that developers receive only secure code suggestions.

### **4.5.1 Demo**

The Demo was conducted in Open AI platform: `https://platform.openai.com/assistants`

#### **Secure File Upload**

_System prompt:_

You are a helpful assistant that writes secure csharp code.

Please respond with a secure csharp code snippet whenever prompted. Please provide only code snippet, no explanations.

in file upload please make sure the extension and the mime type of the file is allowed. make sure the magic bytes are allowed. make sure the path is within allowed folder, the file is not too heavy. make sure that incoming files don’t affect or delete any existing files on the server. give the file a new unique name using guid.

_User prompt:_

_Develop a file upload method in c#_

_The result:_

\```
usingSystem;
usingSystem.IO;
usingSystem.Threading.Tasks;
usingMicrosoft.AspNetCore.Http;
publicclassSecureFileUploader
{
privatereadonlystring []allowedExtensions={".jpg",".jpeg",".png",".pdf"};
privatereadonly(byte []header ,stringextension)[]magicBytes=
{
(newbyte []{0xFF ,0xD8 ,0xFF},".jpg"),
(newbyte []{0x89 ,0x50 ,0x4E ,0x47},".png"),
(newbyte []{0x25 ,0x50 ,0x44 ,0x46},".pdf")
};
privateconstlongmaxFileSize=5*1024*1024;//5MB
privatereadonlystringallowedDirectory=Path.GetFullPath("Uploads");
publicasyncTask <string >UploadAsync (IFormFilefile)
{
if(file==null||file.Length==0||file.Length>maxFileSize)
thrownewInvalidOperationException ("Fileismissingortoolarge.");
varextension=Path. GetExtension (file.FileName). ToLowerInvariant ();
if(Array.IndexOf(allowedExtensions ,extension)<0)
thrownewInvalidOperationException ("Fileextensionnotallowed.");
using(varfileStream=file. OpenReadStream ())
{
varheader=newbyte [8];
intreadBytes=awaitfileStream.ReadAsync(header ,0,header.Length);
boolvalidMagic=false;
\```

16

## Slide 17

\```
foreach(var(magic ,ext)inmagicBytes)
{
if(readBytes>=magic.Length&&extension==ext)
{
boolmatch=true;
for(inti=0;i<magic.Length;i++)
{
if(header[i]!=magic[i])
{
match=false;
break;
}
}
if(match)
{
validMagic=true;
break;
}
}
}
if(! validMagic)
thrownewInvalidOperationException ("Magicbytesdonotmatchextension.");
fileStream.Position=0;
stringuniqueName=Guid.NewGuid ().ToString("N")+extension;
stringuploadPath=Path.Combine(allowedDirectory ,uniqueName);
stringfullPath=Path.GetFullPath(uploadPath);
if(! fullPath.StartsWith( allowedDirectory ))
thrownewUnauthorizedAccessException ("Pathtraversaldetected.");
if(! Directory.Exists( allowedDirectory ))
Directory. CreateDirectory ( allowedDirectory );
using(varoutput=newFileStream(fullPath ,FileMode.CreateNew ,FileAccess.Write))
{
awaitfileStream. CopyToAsync (output);
}
returnuniqueName;//orreturnfullPathifneeded
}
}
}
\```

#### **SSRF**

_System prompt:_

1. URL Format & Scheme

   -  Accept only well-formed, _absolute_ URLs.

   -  Permit https scheme exclusively; reject every other scheme.

2. Trusted Domains & Ports

   -  Hostname must match (case-insensitive) a predefined trusted-domain allow-list.

   -  Permit only explicitly welcomelisted ports (e.g. 443); reject all others.

3. Direct IP Access Restrictions

   -  If the host is an IP address, reject it when it is:

      - Loopback

      - Private

      - Link-local

**–** IPv4-mapped IPv6

4. Safe DNS Resolution

17

## Slide 18

-  Resolve the hostname _immediately_ before each request (DNS timeout _≤_ 3 s).

   -  Reject the request if _any_ resolved IP fails the IP-safety rules.

   -  Prevent TOCTOU:

      - Pin the selected IP via a custom ConnectCallback.

      - Disable re-resolution by the HTTP client.

   -  Multi-IP fallback: if the first safe IP fails, retry sequentially with the next safe IP, each with its own pinned handler.

5. Redirect Handling

   -  Follow redirects manually (maximum 5).

   -  Re-validate scheme, hostname, port, and IP before each redirect hop.

6. Final IP Revalidation

   -  Re-check the resolved IP immediately before streaming the response body.

7. TLS & Host Integrity

   -  Enforce full TLS certificate validation; never disable or bypass it.

   -  Preserve the original hostname in the Host header.

   -  Ensure the SNI field matches the original hostname when IP-pinning.

8. Response Size & Parsing Limits

   -  Reject responses larger than 1 MB.

   -  Parse only the first 4 KB of HTML (or _N_ bytes as configured) to mitigate ReDoS.

9. HTTP Client Configuration

   -  Always set a static User-Agent header (e.g. PreviewBot/1.0).

   -  Apply a strict overall request timeout (e.g. _≤_ 10 s).

   -  Do _not_ enable automatic redirect following.

_User prompt:_

_Write a C# API method that displays a website preview for a user- supplied URL. The result:_

\```
usingSystem;
usingSystem.Buffers;
usingSystem.Collections.Generic;
usingSystem.IO;
usingSystem.Linq;
usingSystem.Net;
usingSystem.Net.Http;
usingSystem.Net.Sockets;
usingSystem.Net.Security;
usingSystem.Security. Cryptography . X509Certificates ;
usingSystem.Text. RegularExpressions ;
usingSystem.Threading;
usingSystem.Threading.Tasks;
usingMicrosoft.AspNetCore.Mvc;
\```

18

## Slide 19

\```
[ ApiController ]
[Route("api/[ controller]")]
publicclassPreviewController:ControllerBase
{
privatestaticreadonlyHashSet <string >AllowedHosts=new( StringComparer . OrdinalIgnoreCase )
{
"example.com",
"www.example.com",
//Addmoretrusteddomainshere
};
privatestaticreadonlyHashSet <int >AllowedPorts=new(){443};
privateconstintMaxRedirects=5;
privateconstintMaxResponseBytes=1024*1024;//1MB
privateconstintMaxParseBytes=4*1024;//4KB
privatestaticreadonlyTimeSpanDnsTimeout=TimeSpan. FromSeconds (3);
privatestaticreadonlyTimeSpanRequestTimeout=TimeSpan. FromSeconds (10);
[HttpGet]
publicasyncTask <IActionResult >GetPreview ([ FromQuery]stringurl)
{
try
{
if(! TryValidateUrl (url ,outUrivalidatedUri ,outstringerror))
returnBadRequest(new{error});
intredirectCount=0;
UricurrentUri=validatedUri ;
HashSet <string >visitedUrls=new( StringComparer . OrdinalIgnoreCase );
while( redirectCount<=MaxRedirects )
{
List <IPAddress >resolvedIps=awaitResolveSafeIpsAsync (currentUri.Host);
if( resolvedIps .Count==0)
returnBadRequest(new{error="NosafeIPsfoundforhostname."});
ExceptionlastException=null;
foreach(IPAddressipinresolvedIps)
{
usingvarcts=newCancellationTokenSource ( RequestTimeout );
try
{
//CustomSocketsHttpHandlerperIPwithIPpinning
usingvarhandler=CreatePinnedHandler (ip ,currentUri.Host);
usingvarclient=newHttpClient(handler)
{
Timeout=Timeout. InfiniteTimeSpan//alreadyhaveexternaltimeout
};
client. DefaultRequestHeaders .UserAgent.ParseAdd("PreviewBot /1.0");
client. DefaultRequestHeaders .Host=currentUri.Host;
varrequest=newHttpRequestMessage (HttpMethod.Get ,currentUri);
request.Headers.Host=currentUri.Host;
usingvarresponse=awaitclient.SendAsync(request ,
HttpCompletionOption .ResponseHeadersRead ,cts.Token);
if(response.StatusCode==HttpStatusCode . MovedPermanently||
response.StatusCode==HttpStatusCode .Found||
response.StatusCode==HttpStatusCode .Redirect||
response.StatusCode==HttpStatusCode . TemporaryRedirect||
(int)response.StatusCode==308)
{
if(++ redirectCount>MaxRedirects )
returnBadRequest(new{error="Toomanyredirects."});
if(! response.Headers.Location. IsAbsoluteUri )
currentUri=newUri(newUri(currentUri. GetLeftPart (UriPartial.Authority)),response.Headers.Location);
else
currentUri=response.Headers.Location;
if(! TryValidateUrl (currentUri.ToString (),outvalidatedUri ,outerror))
returnBadRequest(new{error="Unsaferedirect:"+error});
if(! visitedUrls .Add(currentUri. AbsoluteUri ))
returnBadRequest(new{error="Redirectloopdetected."});
//RedoDNS/IPvalidationoneachhop
break;//leaveforeach ,processnexthop
}
//Validatetheremoteendpoint ’sIP
if(handler. ConnectedRemoteIpisnotnull&&!IsSafeIp(handler. ConnectedRemoteIp ))
returnBadRequest(new{error="Unsafeendpointafterconnect."});
//Limitexpectedresponsesizeto1MB
if(response.Content.Headers. ContentLength>MaxResponseBytes )
\```

19

## Slide 20

\```
returnBadRequest(new{error="Responsetoolarge."});
awaitusingvarstream=awaitresponse.Content. ReadAsStreamAsync (cts.Token);
//Streamonlyupto1MB
byte []buffer=ArrayPool <byte >. Shared.Rent( MaxParseBytes );
intreadLen=0,totalRead=0;
usingvarms=newMemoryStream ();
do
{
inttoRead=Math.Min( MaxParseBytes-totalRead ,buffer.Length);
readLen=awaitstream.ReadAsync(buffer ,0,toRead ,cts.Token);
if(readLen>0)
{
ms.Write(buffer ,0,readLen);
totalRead+=readLen;
if(ms.Length>MaxResponseBytes )
{
ArrayPool <byte >. Shared.Return(buffer);
returnBadRequest(new{error="Responseexceeds1MBlimit."});
}
if(totalRead>=MaxParseBytes )break;
}
}
while(readLen>0);
ArrayPool <byte >. Shared.Return(buffer);
//MinimalHTMLpreviewparsing(only4KB)
ms.Position=0;
usingvarreader=newStreamReader (ms ,leaveOpen:true);
stringhtmlSnip=awaitreader. ReadToEndAsync ();
vartitle=ExtractHtmlTagContent (htmlSnip ,"title");
varmetaDesc=ExtractMetaDescription (htmlSnip);
returnOk(new
{
url=currentUri.ToString (),
title ,
description=metaDesc ,
});
}
catch(Exceptionex)when(!( exisOperationCanceledException ))
{
lastException=ex;
continue;//trynextIP
}
}
if(++ redirectCount>MaxRedirects )
returnBadRequest(new{error="Toomanyredirects."});
if( lastExceptionisnotnull)
returnStatusCode (502 ,new{error="Failedtofetchpreview.",details=lastException .Message});
break;//Success ,don ’tloopredirects .
}
returnBadRequest(new{error="Invalidredirectlogic."});
}
catch( OperationCanceledException )
{
returnStatusCode (504 ,new{error="Requesttimedout."});
}
catch(Exceptionex)
{
returnStatusCode (502 ,new{error="Failedtofetchpreview.",details=ex.Message});
}
}
privatestaticboolTryValidateUrl (stringinput ,outUriuri ,outstringerror)
{
error=null;
uri=null;
if(string. IsNullOrWhiteSpace (input))
{
error="URLcannotbeempty.";
returnfalse;
}
if(!Uri.TryCreate(input ,UriKind.Absolute ,outuri))
{
error="MalformedURL.";
returnfalse;
}
if(! string.Equals(uri.Scheme ,"https",StringComparison . OrdinalIgnoreCase ))
{
error="OnlyhttpsURLsareallowed.";
returnfalse;
\```

20

## Slide 21

`} if (! AllowedHosts .Contains(uri.Host)) { error = "Domain is not allowed."; return false; } int port = uri. IsDefaultPort ? 443 : uri.Port; if (! AllowedPorts .Contains(port)) { error = "Port is not allowed."; return false; } return true; } private static async Task <List <IPAddress >> ResolveSafeIpsAsync (string host) { using var cts = new CancellationTokenSource (DnsTimeout); var ips = new List <IPAddress >(); try { var addresses = await Dns. GetHostAddressesAsync (host).WaitAsync(DnsTimeout , cts.Token); foreach (var ip in addresses) if (IsSafeIp(ip)) ips.Add(ip); } catch { } return ips; } private static bool IsSafeIp(IPAddress ip) { if (ip. AddressFamily != AddressFamily . InterNetwork && ip. AddressFamily != AddressFamily . InterNetworkV6 ) return false; if (IPAddress.IsLoopback(ip)) return false;` _`// Match private (RFC1918 , RFC4193 ), link -local`_ `if (ip. AddressFamily == AddressFamily . InterNetwork ) { byte [] bytes = ip. GetAddressBytes ();` _`// 10.0.0.0/8`_ `if (bytes [0] == 10) return false;` _`// 172.16.0.0/12`_ `if (bytes [0] == 172 && bytes [1] >= 16 && bytes [1] <= 31) return false;` _`// 192.168.0.0/16`_ `if (bytes [0] == 192 && bytes [1] == 168) return false;` _`// Link -local 169.254.0.0/16`_ `if (bytes [0] == 169 && bytes [1] == 254) return false; } else if (ip. AddressFamily == AddressFamily . InterNetworkV6 ) { if (ip. IsIPv4MappedToIPv6 ) return false; if (ip. IsIPv6LinkLocal || ip. IsIPv6SiteLocal || ip. IsIPv6Multicast ) return false; if (ip.Equals(IPAddress. IPv6Loopback )) return false;` _`// Unique local address fc00 ::/7`_ `byte [] bytes = ip. GetAddressBytes (); if (( bytes [0] & 0xFE) == 0xFC) return false; } return true; } private static SocketsHttpHandlerWithIpPinning CreatePinnedHandler (IPAddress ip , string sniHost) { var handler = new SocketsHttpHandlerWithIpPinning (ip , sniHost) { AllowAutoRedirect = false , AutomaticDecompression = DecompressionMethods .None , UseCookies = false , ConnectTimeout = RequestTimeout }; handler.SslOptions. RemoteCertificateValidationCallback = (sender , cert , chain , errors) => errors == SslPolicyErrors .None; return handler; } private static string ExtractHtmlTagContent (string html , string tag) { var rx = new Regex(` $ `@" <\s*{tag }\s*[^ >]* >(.*?) <\s*/\s*{ tag }\s*>", RegexOptions .IgnoreCase | RegexOptions .Singleline` _�→_ `); var match = rx.Match(html); return match.Success ? WebUtility.HtmlDecode(match.Groups [1]. Value.Trim ()) : null; } private static string ExtractMetaDescription (string html) { var rx = new Regex(@"<meta\s+[^ >]* name=[’""]? description [’""]?[^ >]* content =[’""]?(.*?)[’""]?[^ >]* >", RegexOptions .` _�→_ `IgnoreCase | RegexOptions .Singleline); var match = rx.Match(html); return match.Success ? WebUtility.HtmlDecode(match.Groups [1]. Value.Trim ()) : null;`

21

## Slide 22

`} // Custom handler to enforce connect to given IP , preserve Host/SNI , and expose remote connected IP private sealed class SocketsHttpHandlerWithIpPinning : SocketsHttpHandler { private readonly IPAddress _ip; private readonly string _sniHost; public IPAddress ConnectedRemoteIp { get; private set; } public SocketsHttpHandlerWithIpPinning (IPAddress ip , string sniHost) { _ip = ip; _sniHost = sniHost; ConnectCallback = async (ctx , ct) => { var socket = new Socket(_ip.AddressFamily , SocketType.Stream , ProtocolType .Tcp); try { using var cts = CancellationTokenSource . CreateLinkedTokenSource (ct , new CancellationTokenSource (` _�→_ `RequestTimeout ).Token); await socket. ConnectAsync (new IPEndPoint(_ip , ctx.DnsEndPoint .Port), cts.Token); if (! socket.Connected) throw new IOException ("Failed to connect IP pinned socket."); ConnectedRemoteIp = (( IPEndPoint)socket. RemoteEndPoint ).Address; var ns = new NetworkStream (socket , ownsSocket: true); var ssl = new SslStream(ns , leaveInnerStreamOpen : false , null , null , EncryptionPolicy . RequireEncryption ); var sslOpts = new SslClientAuthenticationOptions { TargetHost = _sniHost , // SNI CertificateRevocationCheckMode = X509RevocationMode .Online , ApplicationProtocols = new List < SslApplicationProtocol > { SslApplicationProtocol .Http11 ,` _�→_ `SslApplicationProtocol .Http2 } }; await ssl. AuthenticateAsClientAsync (sslOpts , cts.Token); return ssl; } catch { socket.Dispose (); throw; } }; } } }`

### **4.5.2 Lab Time - 30 min**

Now, let’s put our knowledge into practice

1. Go to OpenAI website: openai.com

2. Log in!

3. Go to assistants: platform.openai.com/assistants

4. Create a new assistant that is safe from unrestricted file uploads and SSRF.

5. Use the provided simple prompts to ensure the assistant does not generate insecure code snippets for developers who are not security-aware.

6. Repeat what you did in the previous step for Race Condition and / or a scenario of your own choosing

### **4.5.3 Limitations of Using Assitants for Secure Coding**

Embedding all organization-specific security guidelines directly into the assistant’s system prompt can contribute to secure code generation for developers. However, this approach has clear drawbacks: longer prompts increase both latency and API cost, and they reduce the available output space, risking truncation of the assistant’s response.

22

## Slide 23

## **4.6 Fine-Tuning**

An effective approach for building secure coding assistants at scale is fine-tuning. Instead of relying solely on long system prompts, organizations can train a custom model using their own dataset of prompts and secure code completions. This method enables the assistant to learn how to consistently respond in a secure manner to common development queries.

Fine-tuning is especially useful in organizational settings, where application security teams and developers can collaborate to build a shared dataset tailored to their specific coding standards and threat model. Once the dataset is ready, a fine-tuned assistant can be created and made available across the organization to provide fast, consistent, and secure code suggestions.

### **4.6.1 Steps for Conducting Fine-Tuning with OpenAI**

1. Identify one or more security-focused use cases relevant to your organization.

2. Write multiple prompt variations that reflect how developers in your organization naturally phrase requests for these scenarios.

3. Create secure code snippets that address each use case.

4. Compile all prompt–snippet pairs into a properly formatted .jsonl file. Ensure proper escaping: use `\n` for newlines, escape double quotes with a backslash ( `\"` ), and escape backslashes themselves as `\\` .

5. Initiate a fine-tuning job on the OpenAI platform and provide the prepared .jsonl dataset.

6. Test your fine-tuned assistant using the OpenAI playground or API with representative prompts.

7. Iterate: refine prompts and snippets based on assistant output quality, then re-tune if needed.

### **4.6.2 Demo**

The structure of the json file:

\```
{
"messages":[
{
"role":"user",
"content":"CanyouwriteafileuploadAPImethodin.NETCore"
},
{
"role":"assistant",
"content":"usingSystem.IO;\ nusingSystem.Threading.Tasks ;....."
}
]
}
\```

The results of using the fine tuned model with file upload use case:

23

## Slide 24

Figure 1: Secure file upload snippet

### **4.6.3 Lab Time - 40 min**

Now, let’s put our knowledge into practice

1. Go to OpenAI website: openai.com

2. Log in!

3. Go to fine tuning: platform.openai.com/finetune

4. Follow the steps mentioned above and fine tune your own model

## **4.7 Integrating into the IDE**

Integrating a fine-tuned OpenAI model into the IDE can be done through tools like Continue or custom extensions. Continue supports fine-tuned models natively—by adding the model’s ID and API key to its configuration, developers can use the tuned assistant directly in the editor. This enables secure, org-specific completions and chat interactions. Alternatively, you can build a lightweight VS Code extension that sends the current file or prompt to your fine-tuned model via the OpenAI API and displays the response inline. This offers flexibility in UI/UX and workflow integration. Both approaches allow the model to be embedded into daily development tasks without changing tools.

# **5 Summary**

In this workshop, we explored how to build AI coding assistants tailored for secure development.

We discussed the risks of insecure code generation, examined common vulnerabilities like SSRF, file uploads, and race conditions, and learned how to mitigate them through prompt engineering and fine-tuning.

24

## Slide 25

Attendees practiced hands-on: crafting prompts, testing model responses, refining code, creating assistants, and fine-tuning custom models.

We concluded by integrating these models into development environments for real-world use.

# **6 Best Practices**

-  Always validate LLM outputs—never assume they’re secure by default.

-  Use clear, specific prompts, and include known constraints or risks.

-  When possible, prefer fine-tuning over long system prompts to reduce latency and cost.

-  Escape all special characters properly in ‘.jsonl‘ data ( `\n` , `\"` , `\\` ).

-  Test models with adversarial prompts to uncover blind spots.

-  Track API usage and set spend limits to avoid accidental overuse.

-  Version datasets, prompts, and assistant configurations for reproducibility.

# **7 Q&A and Troubleshooting**

-  Q: My assistant still generates insecure code—why?

   - A: Review prompt clarity, refine examples, and consider fine-tuning with better completions.

-  Q: How can I integrate my model into an IDE? A: Use tools like Continue (via OpenAI model ID) or build a custom extension using the API.

-  Q: What’s the difference between assistants and fine-tuned models? A: Assistants rely on system prompts at runtime; fine-tuned models internalize patterns and respond faster and cheaper with consistent output.

-  Q: Can I reuse fine-tuned models across projects?

   - A: Yes, as long as they are accessible under your OpenAI account and API key.

-  Q: Can fine-tuning fix hallucinations? A: It reduces them when the completions are well-curated and consistent, but does not eliminate them entirely.

25

## Slide 26

# **References**

- [1] G. Sandoval, H. Pearce, T. Nys, R. Karri, S. Garg, and B. Dolan-Gavitt, “Lost at C: A user study on the security implications of large language model code assistants,” in _Proc. USENIX Security Symp._ , 2023.

- [2] H. Pearce, et al., “Asleep at the keyboard? Assessing the security of GitHub Copilot’s code contributions,” _Commun. ACM_ , vol. 68, no. 2, pp. 96-105, 2025.

- [3] R. Khoury, A. R. Avila, J. Brunelle, and B. M. Camara, “How secure is code generated by ChatGPT?” in _CoRR_ , vol. abs/2304.09655, 2023.

- [4] MITRE, “CWE-367: Time-of-check Time-of-use (TOCTOU) Race Condition,” _Common Weakness Enumeration_ , https://cwe.mitre.org/data/definitions/367.html, accessed June 25, 2025.

- [5] PortSwigger Academy. _Race conditions_ . `https://portswigger.net/web-security/ race-conditions`

26
