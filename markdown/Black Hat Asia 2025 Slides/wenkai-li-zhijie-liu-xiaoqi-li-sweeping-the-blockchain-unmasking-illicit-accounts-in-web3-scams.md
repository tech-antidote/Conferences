---
title: "Sweeping the Blockchain Unmasking Illicit Accounts in Web3 Scams"
speakers: ["Wenkai Li", "Zhijie Liu", "Xiaoqi Li"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Wenkai Li & Zhijie Liu & Xiaoqi Li_Sweeping the Blockchain Unmasking Illicit Accounts in Web3 Scams.pdf"
pages: 27
sha256: "9f56de63d3e9a963d8dd449e45ba8ba37dda6d5b357441a2320be4d235246409"
text_chars: 10376
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
ocr_confidence: null
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-12T03:58:21Z"
---
# Sweeping the Blockchain Unmasking Illicit Accounts in Web3 Scams

**Speakers:** Wenkai Li, Zhijie Liu, Xiaoqi Li  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Wenkai Li & Zhijie Liu & Xiaoqi Li_Sweeping the Blockchain Unmasking Illicit Accounts in Web3 Scams.pdf` (27 pages)


## Slide 1

## Sweeping the Blockchain: Unmasking Illicit Accounts in Web3 Scams **<u>Speaker: Wenkai Li</u>** <u>Hainan University, China</u>

Collaborators: Zhijie Liu (ShanghaiTech University), Xiaoqi Li* (Hainan University)

*Corresponding author: csxqli@ieee.org

#BHAS @BlackHatEvents

## Slide 2

#### The Team

### About Us

###### **Li Wenkai**

##### Security Research

- PhD Student, Hainan University, China

   - 9 year-experience (since 2016) of Ethereum (Born in 2015) Blockchain Security.

- cswkli@hainanu.edu.cn

- https://cswkli.github.io/

- Blockchain/Software/System Security and Privacy, Ethereum/Smart Contract, Malware Detection, and etc.

###### **Liu Zhijie**

   - 40+ papers including ASE、INFOCOM、ICSE、 WWW、AAAI、TSE, etc. within 5 years

- Msc Student, ShanghaiTech University, China

- liuzhj2022@shanghaitech.edu.cn

   - 30+ CVE/CNVD Vulnerabilities identified within 5 years

- https://rroscha.github.io/

- 3700+ citations within 5 years

###### **Li Xiaoqi**

   - Best Paper from INFOCOM、ISPEC、CCF, etc.

- Associate Professor, Hainan University, China

   - SV Insight Annual Global Top-50 Blockchain Research Paper

- csxqli@ieee.org

- https://csxqli.github.io/

- ESI Hot (Top 0.1%)、Highly Cited Paper (Top 1%)

#BHAS @BlackHatEvents

## Slide 3

#### Overview

### Agenda

**Introduction**

**Motivation**

**ScamSweeper**

**Experiments**

**Case Study**

#BHAS @BlackHatEvents

## Slide 4

# Introduction

#BHAS @BlackHatEvents

## Slide 5

#### The 3<sup>rd</sup> Generation Internet – Web 3.0

- Many ways for crypto users to engage with Web3.0:

NFT

Decentraland

Horizon Worlds

meta

- The most used Web3.0 Services:

DEX

CEX

Crypto Gaming

#BHAS @BlackHatEvents

## Slide 6

#### The 3<sup>rd</sup> Generation Internet – Web 3.0

- What is the scale of Web3.0 tech market?

   - ➢ A growing trend.

   - ➢ The accelerating growth rate.

   - ➢ USD 3.17 billion in 2024.

3.5
3.17
Grand View Research
3
2.5
2.23
2
1.73
1.5 1.36
1.06
1
2020 2021 2022 2023 2024
Year
Web3 Market Size

- Web3.0 applications

   - ➢ DApp, DeFi protocol, DID, and etc. based on blockchain.

   - ➢ The blockchain node network follows a power-law distribution.

Ethereum

- ➢ A minority of accounts appear at majority of Txs.

The Web3 environment comes with scam risks **…**

#BHAS @BlackHatEvents

## Slide 7

# Motivation

#BHAS @BlackHatEvents

## Slide 8

#### Motivation: Web3 Scams

- The situation of Web3 scams:

   - ➢ Phishing, Rug Pulls, Harmful Airdrops, Giveaway Scams…

   - ➢ Crypto Drainer, Pig Butchering, Address Poisoning Scams…

**<u>www.infosecurity-magazine.com</u>**

- The scams on Web3 ecosystem can be catastrophic

**ScamSniffer**

#BHAS @BlackHatEvents

## Slide 9

#### Motivation: Web3 Scams

• What do the **Web3 Scams** on blockchain look like?

➢ e.g., crypto drainers often masquerade as web3 projects, enticing victims into the drainer and getting the control access.

Initiating from broadcast phishing address Return tokens Phishing Scams on Blockchain

Attacker

Victim

Website
Building
Initiation
Message
Profit
Scam as
Attacker service provider Victim
NFT

sensitive information stolen

Crypto Drainer Scams

#BHAS @BlackHatEvents

## Slide 10

#### Motivation: previous research

- Graph Learning Methods

- ➢ Intuitive to represent interactions of the topology structure.

- ➢ Account as node, transaction as edge.

- ➢ Top-k algorithm.

- ➢ Power-law distribution leads lots of noise.

EOA
Top-k neighbor
Representation Space
Transaction Network
Top-k Algorithm

Random Walk

- [1] Li, Shucheng and et al. "SIEGE: Self-Supervised Incremental Deep Graph Learning for Ethereum Phishing Scam Detection." in _Proc. of MM_ . 2023.

- [2] Wu, Zhiying and et al. "TRacer: Scalable graph-based transaction tracing for account-based blockchain trading systems. " _TIFS_ . 2023.

- [3] Li, Sijia and et al. "TTAGN: Temporal transaction aggregation graph network for Ethereum phishing scams detection." in _Proc. of WWW_ . 2022.

#BHAS @BlackHatEvents

## Slide 11

#### Motivation: previous research

- Sequence Learning Methods

   - ➢ Transductive to learn the logic of account behavior feature.

   - ➢ Analyzing an account is related to its length.

   - ➢ Large-scale transactions, e.g., **2.7 billion txs** on Ethereum.

**Tab.1 –** The statistical information of some accounts on Ethereum.

S

Account

Transaction sequence

#BHAS @BlackHatEvents

[4] Hu, Sihao and et al. "BERT4ETH: A Pre-trained Transformer for Ethereum Fraud Detection." in _Proc. of WWW_ . 2023.

## Slide 12

#### Motivation: previous research

- Graph Learning Methods

   - ➢ Not suitable to capture dynamic information.

      - Merging multiple edges into one for graph computation e.g., graph convolution or random walk

   - ➢ Not suitable for power law distribution.

EOA
Top-k neighbor
Representation Space

**Transaction Network**

Introducing noise when multi-hop convolution,

In GRU, Model capability is limited (# of GNN layers = # of hop)

- Sequence Learning Methods

S

Account Transaction sequence

- ➢ Not suitable to large - scale transactions.

Analyzing an account is related to the length of its transaction sequence .

#BHAS @BlackHatEvents

[4] Hu, Sihao and et al. "BERT4ETH: A Pre-trained Transformer for Ethereum Fraud Detection." in _Proc. of WWW_ . 2023.

## Slide 13

# ScamSweeper

#BHAS @BlackHatEvents

## Slide 14

#### ScamSweeper

- Learning the dynamic evolution of transaction graph, and applying to account detection ➢ Sequence learning from the graph structure.

#BHAS @BlackHatEvents

## Slide 15

#### ScamSweeper (1)

- (a) Graph Construction

   - ➢ Most previous works used the **random walk** to sample the transaction network.

！

- ➢ Random walk is like a dice game **！**

**Motivation:**

To lower the computing consumption, and learn features from temporal sequence and topology structure. We designed a new walk-sampling method:

###### Struct-Temporal Random walk (STRWalk)

#BHAS @BlackHatEvents

## Slide 16

#### ScamSweeper (1)

##### • (a) Graph Construction

➢ current node is 𝑣𝑖 , next node is 𝑣𝑖+1,

➢ the edge is 𝑒𝑖

➢ 𝜇 ( 𝑇 ( 𝑒𝑖 ))= 𝑇 ( 𝑒𝑖 )− 𝑚𝑖𝑛𝑇𝑖𝑚𝑒 ,

With 𝑷𝒊 and 𝒑𝒎 , Struct-Temporal Random walk (STRWalk) With 𝑷𝒊 , Temporal Random Walk (TRWalk)

➢ 𝛿 ( 𝑣 ) represents the number of nodes that are in the same interval with 𝑣

- account - 1st sampled account - transaction - 2nd sampled account 𝑇 - time 𝑝 - probability

- account - 1st sampled account

The 1st sampled node selected by the alias sample algorithm with the **probability** 𝒑𝒊 . The 2nd sampled node selected by the alias sample algorithm with the **probability** 𝒑𝒎 .

#BHAS @BlackHatEvents

## Slide 17

#### ScamSweeper (1)

- (a) Graph Construction

   - ➢ Walk length: 20, the window size: 4, and the embedding dimension: 128

   - ➢ Phishing dataset, 1165 **malicious** nodes and 636 **normal** nodes.

➢ T-SNE Visualization

Random Walk

Deep Walk

TRWalk

STRWalk

#BHAS @BlackHatEvents

## Slide 18

#### ScamSweeper (2)

• (b) Directed Graph Encoder

- ➢ Split the whole graph according to the interval, generating several sub-graphs

➢ Learning the feature of each subgraph in time sequence

Nodes and Txs Representation
Source node set N F
 Collect
Directed
Transaction Set
Target node set N T
Transaction Graph
 Feature Align
Feature Extract
Graph Neural Network

Arrange TXs in order of Execution
Source Node N 1 ⤍ Target Node N 2
① Sort
… …
Source Node N 4 ⤍ Target Node N 1
④
Directed Graph Feature

**Transaction Graph Data**

④ Transaction Graph
Feature Extract

#BHAS @BlackHatEvents

## Slide 19

#### ScamSweeper (2)

• (b) Directed Graph Encoder

𝑉= {𝑋𝑓; 𝑋𝑡| (𝑋𝑓1; 𝑋𝑡1, 𝑋𝑓2; 𝑋𝑡2, . . . , 𝑋𝑓𝑛; 𝑋𝑡𝑛)} 𝐸= {𝑋𝑓 →𝑋𝑡|(𝑒1, 𝑒2, … , 𝑒𝑛)} 𝛩- linear transformation layer ℎ- hidden feature of nodes

ො𝑣= 𝐿𝑒𝑎𝑘𝑦𝑅𝑒𝑙𝑢(Θ𝑣 ⋅[𝑣| 𝑒]) (1) 𝑒𝑖𝑗 = 𝐿𝑒𝑎𝑘𝑦𝑅𝑒𝑙𝑢(Θ𝑛 ⋅ ℎ𝑖 ℎ𝑗]) (2) 𝑒𝑥𝑝(𝑒𝑖𝑗) (3) 𝛼𝑖𝑗 = σ𝑥∈𝑁 𝑖<sup>𝑒𝑥𝑝</sup> 𝑒𝑖𝑥 ℎ𝑔 = 𝐸𝑙𝑢(𝛼𝑖𝑗 ⋅Θ ⋅ℎ𝑖 + σ𝑥∈𝑁 𝑖<sup>𝛼</sup> 𝑖𝑥<sup>⋅Θ ⋅ℎ</sup> 𝑥<sup>)</sup> (4)

#BHAS @BlackHatEvents

## Slide 20

#### ScamSweeper (3)

- (c) Temporal Feature Learning

   - ➢ Leveraging the ability of Transformer

𝐻<sup>(𝑙+1)</sup> = 𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝐻 𝑙<sup>𝑇</sup> Θ𝑄, 𝐻 𝑙<sup>𝑇</sup> Θ𝐾, 𝐻 𝑙<sup>𝑇</sup> Θ𝑉) <u>𝑄𝐾</u><sup>𝑇</sup> ℎ= 𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛 𝑄, 𝐾, 𝑉= 𝑠𝑜𝑓𝑡𝑚𝑎𝑥 ~~(~~ 𝑑𝑘<sup>𝑉)</sup> 𝐻<sup>(𝑙+1)</sup> = 𝐹𝐹𝑁 ℎ (𝑙) 𝐹𝐹𝑁 𝑥= 𝑆𝑖𝑔𝑚𝑖𝑜𝑑 𝑥𝑊1(𝑙) + 𝑏1(𝑙) 𝑊2(𝑙) + 𝑏2

(5) (6) (7) (8)

#BHAS @BlackHatEvents

## Slide 21

# Experiments

#BHAS @BlackHatEvents

## Slide 22

#### Experiments: large-scale data

- Data & distribution

   - ➢ Crawling the first 18 million block height on Ethereum

   - ➢ Phishing labels from Etherscan

###### **Tab.2 –** The statistical information of dataset.

- ➢ Web3 scams from [5]

- ➢ Normal nodes contains 4 types: exchange, mining, ICO wallet, and gambling.

#BHAS @BlackHatEvents

[5] https://github.com/scamsniffer/scam-database..“, 2024.

## Slide 23

#### Experiments: Ablation

- How well do the components work?

   - ➢ the importance of graph encoder and T-Transformer

**ScamSweeper** with all components, **ScamSweeper-t** without the T-Transformer, **ScamSweeper-g** without the graph encoder.

**ScamSweeper > Graph encoder > T-Transformer**

#BHAS @BlackHatEvents

## Slide 24

#### Experiments: Comparison

- How well do the ScamSweeper work?

   - ➢ Compared with Graph methods and Transformer

   - ➢ Structure window: {5,10,15}, Adam weight decay rate: 5 𝑒 − 4.

   - ➢ Training: 70%, Validation: 20%, Test:10%

#BHAS @BlackHatEvents

## Slide 25

# Case Study

#BHAS @BlackHatEvents

## Slide 26

#### Case Study: Web3 Scam

##### • Dynamic Evolution

###### ➢ 𝜏 is a time interval.

Malicious Obfuscation
(a) (0, 𝝉 ) (b) ( 𝝉 , 𝟐𝝉 ) (c) ( 𝟐𝝉 , 𝟑𝝉 ) (d) ( 𝟓𝝉 , 𝟔𝝉 )
Transaction Graph
(e) ( 𝟔𝝉 , 𝟕𝝉 ) (f) ( 𝟗𝝉 , 𝟏𝟎𝝉 ) (g) ( 𝟏𝟎𝝉 , 𝟏𝟏𝝉 )
Transaction Pattern

#BHAS @BlackHatEvents

## Slide 27

#### Takeaways

- Summary & key takeaways

➢ **Web3 Scams Proliferation:** Web3 applications are increasingly targeted by scammers who mimic legitimate transactions to deceive users, highlighting a critical gap in current detection methods.

- ➢ **Research Gap:** Prior studies focus on de-anonymization and phishing nodes, neglecting the unique temporal and structural patterns of web3 scams, while existing detection tools struggle with power-law distributed transaction networks.

➢ **ScamSweeper Framework:** A novel approach that combines structure-temporal random walks for efficient transaction network sampling and variational transformers for dynamic pattern analysis, capturing both temporal and structural evolution of scams.

➢ **​Practical Insights:** Large-scale dataset collection, cost-effective data sampling, and dynamic evolution analysis, enabling real-world application in Ethereum transaction monitoring.

#BHAS @BlackHatEvents
