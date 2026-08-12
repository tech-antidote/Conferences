---
title: "Thinking Outside the Sink How Tree-of-AST Redefines the Boundaries of Dataflow Analysis"
speakers: ["Sasha Zyuzin", "Ruikai Peng"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Sasha Zyuzin&Ruikai Peng_Thinking Outside the Sink How Tree-of-AST Redefines the Boundaries of Dataflow Analysis_Compressed.pdf"
pages: 53
sha256: "6ad480775ab6d77b913bac530f6fd2f172daa53b5dca14c5600da4fb4ea5a7a2"
text_chars: 19997
ocr_pages: 13
has_ocr: true
redacted_secrets: 0
ocr_confidence: 90.5
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:25:22Z"
---
# Thinking Outside the Sink How Tree-of-AST Redefines the Boundaries of Dataflow Analysis

**Speakers:** Sasha Zyuzin, Ruikai Peng  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Sasha Zyuzin&Ruikai Peng_Thinking Outside the Sink How Tree-of-AST Redefines the Boundaries of Dataflow Analysis_Compressed.pdf` (53 pages)


## Slide 1

### **Thinking Outside the Sink**

How Tree-of-AST Redefines the Boundaries of Dataflow Analysis

Alexander Zyuzin Ruikai Peng


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Thinking
Outside
the Sink
How Tree-of-AST
Redefines the Boundaries
of Dataflow Analysis
Alexander Zyuzin
Ruikai Peng _
```

## Slide 2

CONTENTS

01

02

ALGORITHMIC

TECHNICAL

#BHUSA   @BlackHatEvents

## Slide 3

1 PICTURE  WORTH 1000 WORDS…

My teacher

Me

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TPICTURE WORTH 1000 WORDS...
\ saylese 16.10.2024, 16:46 My teacher
‘» ihave a student who's very interested in security stuff and he's looking for a mentor for a
project he's working on (idk what i it is). https://retrO.blog/ would you be interested in
discussing with him? i don't think he would expect much time from you
RetrO's Register
RetrO's Threat Research
g greyroad 16.10.2024, 18:28 Me
«l've had the incredibleopportunity to identify 22 CVEs,»
Does he need a mentor for stealing nuclear codes?
| mean sure
```

## Slide 4

WHAT IS THE ALGORITHMIC
PART OF OUR SOLUTION?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WHAT IS THE ALGORITHMIC
PART OF OUR SOLUTION?
```

## Slide 5

THE PAPER I’VE
READ

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE PAPER I'V
READ
Tree of Thoughts: Deliberate Problem Solving
with Large Language Models
=
‘Shunyu Yao Jeffrey Zhao Izhak Shafran wor +
Princeton University 5 Google DeepMind Google DeepMind Output Output Output Output
‘Thomas L. Griffiths Yuan Cao Karthik Narasimhan Prompting 0) Prompting incor
Princeton University Google DeepMind Princeton University
(4) Tree of Thoughts (ToT)
Figure 1: Schematic illustrating various approaches to problem solving with LLMs. Each rectangle
box represents a thought, which is a coherent language sequence that serves as an intermediate
step toward problem solving. See concrete examples of how thoughts are generated, evaluated, and
Abstract searched in Figures 24]
choices instead of just picking one, and (2) evaluates its current status and actively looks ahead or
[cs.CL] 3D
.10601v
5
arXiv:230.
Language models are increasingly being deployed for general problem solving
across a wide range of tasks, but are still confined to token-level, left-to-right
decision-making processes during inference. This means they can fall short in
tasks that require exploration, strategic lookahead, or where initial decisions play
‘MpivOtalTOle. To surmount these challenges, we introduce a new framework for
language model inference, “Tree of Thoughts” (ToT), which generalizes over the
popular “Chain of Thought” approach to prompting language models, and enables
exploration over coherent units of text (“thoughts”) that serve as intermediate steps
toward problem solving. ToT allows LMs to perform deliberate decision making
by considering multiple different reasoning paths and self-evaluating choices to
decide the next course of action, as well as looking ahead or backtracking when
necessary to make global choices. Our experiments show that ToT significantly
enhances language models’ problem-solving abilities on three novel tasks requiring
non-trivial planning or search: Game of 24, Creative Writing, and Mini Crosswords.
For instance, in Game of 24, while GPT-4 with chain-of-thought prompting only
solved 4% of tasks, our method achieved a success rate of 74%. Code repo with all
prompts: https: //github.com/princeton-nlp/tree-of-thought-11m
1 Introduction
Originally designed to generate text, scaled-up versions of language models (LMs) such as GPT [25.
26, 1, 23] and PaLM [5] have been shown to be increasingly capable of performing an ever wider
range of tasks requiring mathematical, symbolic, commonsense, and knowledge reasoning. ~
pethaps surprising that underlying all this progress is still the original autoregressive mechanist*
generating text, which makes token-level decisions one by one and in a left-to-right fashion. Is suc
a simple mechanism sufficient for a LM to be built toward a general problem solver? If not, what
problems would challenge the current paradigm, and what should be alternative mechanisms?
‘The literature on human cognition provides some clues to answer these questions. Research on “dual
process” models suggests that people have two modes in which they engage with decisions — a fast,
automatic, unconscious mode (“System 1”) and a slow, deliberate, conscious mode (“System 2”)
[30, 31, 16, 15]. These two modes have previously been connected to a variety of mathematical
models used in machine learning. For example, research on reinforcement learning in humans and
other animals has explored the circumstances under which they engage in associative “model free”
learning or more deliberative “model based” planning [7]. The simple associative token-level choices
of LMs are also reminiscent of “System 1”, and thus might benefit from augmentation by a more
deliberate “System 2” planning process that (1) maintains and explores diverse alternatives for current
Conference on Neural Information Processing Systems (NeurIPS 2023),
backtracks to make more global decisions.
To design such a planning process, we return to the origins of artificial intelligence (and cog
drawing inspiration from the planning processes explored by Newell, Shaw, and Simon
starting in the 1950s [21, 22]. Newell and colleagues characterized problem solving (21] as search
through a combinatorial problem space, represented as a tree. We thus propose the Tree of Thoughts
(ToT) framework for general problem solving with language models. As Figure] illustrates, while
existing methods (detailed below) sample continuous language sequences for problem solving, ToT
actively maintains a tree of thoughts, where each #MOWghi is a coherent language sequence that serves
as an intermediate step toward problem solving (Table{I). Such a high-level semantic unit allows the
LM to Selfeevallate the progress different intermediate thoughts make towards solving the problem
through a deliberate reasoning process that is also instantiated in language (Figures 246). Thi
implementation of search heuristics via LM self-evaluation and deliberation is novel, as previous
search heuristics are either programmed or learned. Finally, we combine this language-based
capability to generate and evaluate diverse thoughts with search algorithms, such as breadth-first
search (BFS) or depth-first search (DFS), which allow systematic exploration of the tree of thoughts
with lookahead and backtracking,
Empirically, we propose three new problems that challenge existing LM inference methods even with
the state-of-the-art language model, GPT-4 [23]: Game of 24, Creative Writing, and Crosswords
(Table I). These tasks require deductive, mathematical, commonsense, lexical reasoning abilities,
and a way to incorporate systematic planning or search. We show ToT obtains superior results on
all three tasks by being general and flexible enough to support different levels of thoughts, different
ways to generate and evaluate thoughts, and different search algorithms that adapt to the nature of
different problems. We also analyze how such choices affect model performances via systematic
ablations and discuss future directions to better train and use LMs.
2 Background
We first formalize some existing methods that use large language models for problem-solving,
which our approach is inspired by and later compared with. We use pg to denote a pre-trained LM
with parameters 6, and lowerease letters ,y, =, s,--- to denote a language sequence, i.e. 2
({1],---,2{n]) where each zi) is a token, so that po(r) = IT" po( ). We use uppercase
letters $,:-- to denote a collection of language sequences.
Input-output (10) prompting is the most common way to turn a problem input x into output
y with LM: y ~ po(yiprompto(z)), where prompt jo (=r) wraps input « with task instruct
and/or few-shot input-output examples. For simplicity, let us denote p"°"*(output | input)
pe(output | prompt(input)), so that IO prompting can be formulated as y ~ pj
```

## Slide 6

TREEOFTHOUGHT

###### WHY IT’S SO CHALLENGING FOR AI?

**Goal:**

Make 24 using four given numbers and basic math operations

**Rules:**

Given: 4 numbers (e.g., 8, 3, 8, 3

Use:

+, −, ×, ÷ and parentheses

1. Huge search space of combinations

2. Early mistakes lead to dead ends

3. Requires strategic planning & backtracking

###### RESULTS

Must: Use each number exactly once

Final result = 24

Target:

4% Chain-ofThought

74% Tree-ofThought

#BHUSA   @BlackHatEvents

## Slide 7

HOW CAN
A GENERATIVE APPROACH,
BE A GAME CHANGER FOR TAINT
ANALYSIS FRAMEWORK?

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
HOW CAN
A GENERATIVE APPROACH,
BE A GAME CHANGER FOR TAINT
ANALYSIS FRAMEWORK?
```

## Slide 8

INSPIRATION HUNTR STORY

51 report

18 CVEs

Transformers, Tensorflow, Llama.cpp…

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 39/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
INSPIRATION: HUNTR STORY
‘Command Injection Bypass via escaped \xa0 in inteVneural-compressor
```

## Slide 9

INSPIRATION HUNTR STORY

The first thing you do with a target, you run Bandit to see static point-of-interest: Code Search, SAST tell us where the sinks are

- There are tons of them!

- We spend hours tracking them to their sources.

_e.g., modelscope/agentscope:_

- 8 sinks identified per …4 of them SAST Bandit scan reachable

- … within only 2 of them exploitable

#BHUSA   @BlackHatEvents

## Slide 10

WHAT IS TAINT ANALYSIS.
SINK? SOURCE?

"Sink" _The place where meets usually indicate dangerous (e.g. eval, memcpy, pickle)_

"Source": _The input of data (e.g., endpoint, argv, file)_

#BHUSA   @BlackHatEvents

## Slide 11

**SOURCETOSINK**

##### **WH** AT IS TAINT ANALYSIS. ENYOU THINK IT SINK? SOURCE? UPSIDEDOWN,

###### Why?

- It’s too _easy_ to identify sinks

- Avoids False positive & prioritize

- _Context relevance_

   - Potential Context

   - State Recovery

      - Complexity of conditional flow (path explosion of executions)

**SINKTOSOURCE**

#BHUSA   @BlackHatEvents

## Slide 12

**TREEOF** **_STATES_ ?**

ESSENCE
OF THE TASKS
STATEFULNESS,
PRUNING?

- The Pruning Process: - Cut off unrelated / low-valued branches, to focus on the biggest fruit

Statefulness:

- dependency of relationship between each nodes (states). Directed acyclic graph)

###### State-Recovery

- Recovering future states with both past states and potential states as contextual information,

**SINKTOSOURCE?**

#BHUSA   @BlackHatEvents

## Slide 13

TREEOFAST

1. Diffuse taint graph from on the sink

2. Traverse _sink-to-source_

   - vote if current state is source

      - _vote & value next parrallel states for most possible source-leading node_

      - _depth, lookaheads_

      - _rewind, stateful-task_

#BHUSA   @BlackHatEvents

## Slide 14

PAYLOAD GENERATION

1. Reverse traverse _source-to-sink_ - Nested-restriction tags to semantically describe the constrains from the slice.

   - Make up for the part we deliberately neglacted

   - “ _Intuition_ ” for solvers in a _pruned-and-limited_ slice

2. Traverse _source-to-sink_ again - Constraints with _SMT_ Solvers for model-generations, linearly solving the constrains into payloads

#BHUSA   @BlackHatEvents

## Slide 15

# Technical side of our approach

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technical side
of our approach
```

## Slide 16

THE PROBLEM WE NEED TO SOLVE

INTERNAL PROGRAM
REPRESENTATION

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
THE PROBLEM WE NEED TO SOLVE:
INTERNAL PROGRAM
REPRESENTATION
```

## Slide 17

STAGES OF PROBLEM ACCEPTANCE

###### DENIAL

#BHUSA   @BlackHatEvents

## Slide 18

FIRST STEP AST

###### An Abstract Syntax Tree

###### **Steps in processing of source code**

- Code Structure as Data

- Foundation for Security Analysis

- Steps in processing of source code

Lexical analysis

Tokens

Syntactic analysis

AST

#BHUSA   @BlackHatEvents

## Slide 19

AST OR NO AST?

###### Intuitively (as simple result):

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AST ORNO AST? a
Intuitively (as simple result):
>>> print(ast.dump(ast.parse('a if b else c', mode='eval'), indent=4) )
Expression(
test=Name(id='b', ctx=Load()),
body=Name(id='a', ctx=Load()),
orelse=Name(id='c', ctx=Load())))
```

## Slide 20

AST OR NO AST?

Intuitively (as simple result):

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
AST ORNO AST? a
Intuitively (as simple result):
‘a if b else c'
test=Name(id='b',
body=Name(id='a',
orelse=Name(id='c'
```

## Slide 21

STAGES OF PROBLEM ACCEPTANCE

###### DENIAL

AST

#BHUSA   @BlackHatEvents

## Slide 22

PROBLEMS OF ASTS

Note: ASTs remain useful for static analysis despite these challenges

Must implement custom parser for each language

#BHUSA   @BlackHatEvents

## Slide 23

PROBLEMS OF ASTS

Note: ASTs remain useful for static analysis despite these challenges

Tracking definitions and usage across files (e.g., function in a.py used in b.py)

#BHUSA   @BlackHatEvents

## Slide 24

PROBLEMS OF ASTS

Note: ASTs remain useful for static analysis despite these challenges

LANGUAGE CROSSFILE
SPECIFIC PARSING ANALYSIS
IMPORT  COMPLEXITY VS.
HANDLING BENEFIT

Managing variable shadowing and name conflicts

#BHUSA   @BlackHatEvents

## Slide 25

PROBLEMS OF ASTS

Note: ASTs remain useful for static analysis despite these challenges

Resolving module dependencies and import paths

#BHUSA   @BlackHatEvents

## Slide 26

PROBLEMS OF ASTS

Note: ASTs remain useful for static analysis despite these challenges

High implementation effort for basic static analysis tasks

#BHUSA   @BlackHatEvents

## Slide 27

STAGES OF PROBLEM ACCEPTANCE

DENIAL ANGER
AST
Resolving
imports
with AST

#BHUSA   @BlackHatEvents

## Slide 28

THE SOLUTION? STACK GRAPHS!

## Stack graphs are an open source framework

#BHUSA   @BlackHatEvents

## Slide 29

THE SOLUTION? STACK GRAPHS!

## for precise

## code navigation

#BHUSA   @BlackHatEvents

## Slide 30

THE SOLUTION? STACK GRAPHS!

, which allows to represent how symbols flow through a program.

#BHUSA   @BlackHatEvents

## Slide 31

WHAT IS SYMBOL RESOLUTION?

**community.py conference.py def share() from community import * pass def enjoy() pass**

###### **community.py**

blackhat.py

from conference import enjoy

**enjoy()**

**def network pass() pass**

#BHUSA   @BlackHatEvents

## Slide 32

STAGES OF PROBLEM ACCEPTANCE

DENIAL ANGER BARGAIN
Happy
for a second…
AST
Found a
promising
framework
Resolving
imports
with AST

#BHUSA   @BlackHatEvents

## Slide 33

HOW DO THEY WORK? SIMPLIFIED

###### Tree-sitter

Tells you "there's a function called foo here and a call to foo there"

1. Builds CST

2. Consistent API across languages

3. Understands the grammar but not the meaning

## Slide 34

HOW DO THEY WORK? SIMPLIFIED

Tell you "this specific call to foo resolves to that specific definition of foo based on the language's scoping rules"

1. Apply language-specific rules TSGs to understand how names resolve 3. Understand imports, scope rules, and visibility modifiers

4. Resolve references across files based on actual language semantics 3. Build a graph structure that represents all possible name resolution paths

## Slide 35

HOW DO THEY WORK? ACTUAL

###### Phase I. Index-Time Per File)

###### Phase II. Query-Time Cross-File)

Create scope nodes
Parse code with tree-sitter →  for lexical scopes Load partial paths
Concrete Syntax Tree from relevant files
Symbol stack:
⟨referenced_symbol⟩
Create push nodes
(↓) for references Apply TSG rules → Transform CST  Create virtual edges  Start node:
reference location
Create pop nodes  nodes to stack graph nodes between file root nodes
(↑) for definitions
Build isolated file subgraph   Create root  Initialize path search
node for file
with nodes and edges from reference node
entry
Continue until
empty symbol
stack at
Record preconditions/ definition
Calculate all partial   postconditions with  Execute partial
paths within the file variables (ψ) path stitching Find compatible paths
(postcondition matches precondition)
Track symbol/ Concatenate
scope stack  Start from  Store partial paths with precondi- Unify stack  paths Return resolved definitions
changes tions/postconditions in database variables with precedence ranking
important nodes
(refs, defs, root)
#BHUSA   @BlackHatEvents

## Slide 36

STAGES OF PROBLEM ACCEPTANCE

ANGER BARGAIN DEPRESSION **Happy Includes the for a second… Frustration stage**

###### DENIAL

Attempted to create own version of stack graphs for our Found a needs promising framework

AST Resolving imports with AST

#BHUSA   @BlackHatEvents

## Slide 37

SO WHAT ARE WE
EVENTUALLY
USING?

After quite some time, we’ve found a working Stack Graphs library, and it all simplified to…

#BHUSA   @BlackHatEvents

## Slide 38

STAGES OF PROBLEM ACCEPTANCE

DENIAL ANGER BARGAIN DEPRESSION ACCEPTANCE **Happy Includes the Integration for a second… Frustration stage** Attempted to create own version of AST stack graphs for our Found a Found needs promising ready framework library Resolving imports with AST

###### DENIAL

#BHUSA   @BlackHatEvents

## Slide 39

MORE INTERESTING STUFF
OUR SOLUTIONS, APPROACHES & OTHER OBSERVATIONS

#BHUSA   @BlackHatEvents

## Slide 40

TRIED AND TRUE, YET OFTEN OVERLOOKED

###### Instead of asking this…

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisek hat
TRIED AND TRUE, YET OFTEN OVERLOOKED nee
Instead of asking this...
Does the sink directly receive tainted data?
```

## Slide 41

TRIED AND TRUE, YET OFTEN OVERLOOKED

###### Try asking this

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bisek hat
TRIED AND TRUE, YET OFTEN OVERLOOKE aa
Can tainted data reach the sink through any path, including via callee functions?
+ 2 Tools Q i)
t
Try asking this
```

## Slide 42

THREE REPRESENTATIVE CASES

|Code Pattern|Description|Argument
Tracking|Parameter-
Based Tainting|Traditional
Sink Trace|
|---|---|---|---|---|
|sink(caller.param)|Direct taint flow from
caller parameter|Yes|Yes|Yes|
|sink(callee())|Taint originates from
callee function|No|Yes|No|
|sink(callee(caller.param))|Tainted parameter
passed through callee|Yes|Yes|No|

#BHUSA   @BlackHatEvents

## Slide 43

THREE REPRESENTATIVE CASES

|Code Pattern|Description|Argument
Tracking|Parameter-
Based Tainting|Traditional
Sink Trace|
|---|---|---|---|---|
|sink(caller.param)|Direct taint flow from
caller parameter|Yes|Yes|Yes|
|sink(callee())|Taint originates from
callee function|No|Yes|No|
|sink(callee(caller.param))|Tainted parameter
passed through callee|Yes|Yes|No|

#BHUSA   @BlackHatEvents

## Slide 44

HOW TO AVOID
FREEZES
ON LARGE
PROJECTS?

MODULE 1

Might call the sink

SINK
Calls to the sink function are likely here

MODULE 2

Functions here likely don't call the sink

## Slide 45

HOW DO WE USE LMS?

#### We use LangChain

**01**

LLM makes decisions on 1 Input Source Detection, 2 Path Selection, and 3 Backtracking

**02** Implements chain lookahead analysis

**03** Voting algorithms are implemented

**04** Similar voting results are getting re-weighted with smarter models.

#BHUSA   @BlackHatEvents

## Slide 46

WHAT ARE
THE RESULTS?

#BHUSA   @BlackHatEvents

## Slide 47

HOW IS OUR APPROACH DIFFERENT
AS A DATAFLOW ENGINE?

It doesn’t require the entry point specification to analyze the program.

**01**

It uses LMs, but doesn’t just send the code over and ask “Is there a vulnerability?”

**02**

Designed specifically for large projects that span across many files, modules, repositories.

**03**

#BHUSA   @BlackHatEvents

## Slide 48

WHAT HAVE WE RE DISCOVERED?

CVE202229216 TENSORFLOW

CVE202340581 YTDLP

Code injection via eval

Command injection via subprocess.call

190k stars on Github

119k stars on Github

CVE201914904 ANSIBLE

Code injection via os.system

63k stars on Github

#BHUSA   @BlackHatEvents

## Slide 49

WHAT IS THE
PROBLEM WITH
MEASURING THE
PERFORMANCE?

#BHUSA   @BlackHatEvents

## Slide 50

CONCLUSIONS AKA BLACK HAT SOUND BYTES

Replacing traditional Rethinking Automating security analysis problems from strategic decisions (fuzzing, static/ first principles with LLMs to dynamic) with AIrather than optimize human powered iterating on work automation approaches existing solutions

#BHUSA   @BlackHatEvents

## Slide 51

The sink is just the end. What matters is how we got there.

azyuzin@terpmail.umd.edu

retr0@retr0.blog

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The sink is just the end.
What matters is how we got there.
azyuzin@terpmail.umd.edu retrO@retr0.blog
```

## Slide 52

RESOURCES

https://github.blog/open-source/introducing-stack-graphs/

https://pypi.org/project/stack-graphs-python-bindings/

https://arxiv.org/pdf/2305.10601

https://apps.apple.com/us/app/wheres-my-water/id449735650

#BHUSA   @BlackHatEvents

## Slide 53

INTERESTING FACTS ABOUT OUR PROJECT

We are called Tree-of-AST, but we don’t actually use AST that much…

We re-wrote the project from 0 at least 3 times

**01**

**02**

Different versions of the project have different codebase sizes, varying from 1000 to 12 000+ lines of code

**03**

#BHUSA   @BlackHatEvents
