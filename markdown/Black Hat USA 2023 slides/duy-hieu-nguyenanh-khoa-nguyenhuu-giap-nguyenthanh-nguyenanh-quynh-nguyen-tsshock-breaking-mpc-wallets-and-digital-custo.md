---
title: "TSSHOCK Breaking MPC Wallets and Digital Custodians for $BILLION$ Profit"
speakers: ["Duy Hieu Nguyen", "Anh Khoa Nguyen", "Huu Giap Nguyen", "Thanh Nguyen", "Anh Quynh Nguyen"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Duy Hieu Nguyen,Anh Khoa Nguyen,Huu Giap Nguyen,Thanh Nguyen,Anh Quynh Nguyen_TSSHOCK Breaking MPC Wallets and Digital Custodians for $BILLION$ Profit_wp.pdf"
pages: 11
sha256: "a892cbbc863dccd205d3e9476b3ce6236d00efa4c701edba9e7c7360a3d3a7b6"
text_chars: 42695
ocr_pages: 0
has_ocr: false
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2"
converted_at: "2026-08-11T23:57:47Z"
---
# TSSHOCK Breaking MPC Wallets and Digital Custodians for $BILLION$ Profit

**Speakers:** Duy Hieu Nguyen, Anh Khoa Nguyen, Huu Giap Nguyen, Thanh Nguyen, Anh Quynh Nguyen  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Duy Hieu Nguyen,Anh Khoa Nguyen,Huu Giap Nguyen,Thanh Nguyen,Anh Quynh Nguyen_TSSHOCK Breaking MPC Wallets and Digital Custodians for $BILLION$ Profit_wp.pdf` (11 pages)

## Slide 1

# **New Key Extraction Attacks on Threshold ECDSA Implementations**

Duy Hieu Nguyen Anh Khoa Nguyen Huu Giap Nguyen _Verichains Verichains Verichains_

## Thanh Nguyen Anh Quynh Nguyen _VNSecurity & Verichains Nanyang Technological University_

## **Abstract**

Threshold ECDSA, a Threshold Signature Scheme based protocol for the widely used digital signature algorithm ECDSA, has gained much attention in the distributed ledger industry. The use of this protocol was introduced as a means to increase security in these systems, as many ledgers have a dependency on ECDSA. However, as with any novel cryptographic protocol, the security of Threshold ECDSA has not been thoroughly tested over time. In light of this, a survey was conducted to evaluate the security of various implementations of Threshold ECDSA.

The survey conducted on the security of Threshold ECDSA implementations yielded some unexpected results, revealing the persistence of implementation flaws that can leave systems vulnerable to various attack vectors. Our research has identified three potential attacks that have the potential to recover the private key of ECDSA, depending on the particular implementation flaw. As a result, this paper provides a comprehensive analysis of the security of Threshold ECDSA, starting with a review of the cryptographic primitives utilized in its implementation, followed by a detailed explanation of the attack process and how to mitigate them.

Our research highlights the need for ongoing security evaluations in the distributed ledger technology field, especially when it comes to new technologies like Threshold ECDSA. Through our analysis, we have identified several implementation flaws that could be exploited to trigger attacks on these systems. It is critical to understand the potential risks associated with the use of Threshold ECDSA and to take proactive measures to ensure the security of assets stored in these systems. By sharing our findings and attack instructions, we hope to raise awareness and encourage both the academic and practical communities to prioritize security in their implementations.

messages. For signing a message, at least _t_ (the threshold) out of _n_ (the number of parties participating in the generation ceremony of the key in use) parties are required. There is no trusted dealer as the TSS private key is never constructed (each party only keeps a private key share).

In the blockchain ecosystem, ECDSA is the most popular signature scheme as it is used by Bitcoin and Ethereum, to name a few. Designing a TSS for ECDSA is not straightforward, since it requires MPC (multi-party computation)unfriendly operations over shared secrets such as inversion or multiplication. To accomplish this, many cryptographic toolboxes (e.g., homomorphic encryption, zero-knowledge proof, ...) are involved, thus making the scheme complex and adding more attacking surface. Most open-source TSS implementations today follow the research line of Rosario Gennaro and Steven Goldfeder [1–3], which is also the only design of concern throughout this paper.

Section 2 presents an overview of the cryptographic techniques employed in the implementation of Threshold ECDSA. Section 3 details the various attack vectors that can exploit commonly observed implementation flaws in Threshold ECDSA. Specifically, we provide a comprehensive list of the triggering flaws, attack flow, and potential mitigation strategies for each of the three identified attacks. Finally, in Section 5, we summarize our contributions and highlight the significance of our findings for the security of Threshold ECDSA implementations in practical settings.

## **2 Background**

This section provides the necessary details to understand the attacks to be discussed. For complete specification of the Threshold ECDSA protocol, please refer to [1–3].

## **1 Introduction**

## **2.1 Fiat–Shamir heuristic**

Threshold Signature Scheme (TSS) is a cryptographic scheme allowing multiple parties to jointly generate keys and sign

Fiat-Shamir heuristic is a technique for removing interactivity from interactive, public-coin proof systems.

## Slide 2

In these systems, the verifier generates and sends to the prover some random values acting as challenges which can only be solved if the statement being proved is correct (the soundness property). Usually if these random values are known in advance, the prover will be able to forge proofs for incorrect statements.

Fiat-Shamir heuristic replaces random values with outputs from a cryptographic hash function, hashing the verifier context whenever randomness is needed. Public parameters, the statement being proved, previously exchanged messages, ... all contribute to this context. Since randomness is removed, the verifier becomes deterministic and simulatable, thus making the proof system non-interactive.

## **2.2 dlnproof**

dlnproof is used to verify, in zero-knowledge manner, that a prover knows log _g h_ modulo a composite number _N_ .

At the key generation ceremony, each party is required to generate and broadcast a triple _N_<sup>˜</sup> _, h_ 1 _, h_ 2, which is later used in subsequent signing ceremonies, together with a dlnproof proving that the party knows log _h_ 2 _h_ 1 mod _N_<sup>˜</sup> . Some implementations also require an additional dlnproof for log _h_ 1 _h_ 2 mod _N_<sup>˜</sup> .

Here is the interactive version of dlnproof:

1. Peggy (the prover) commits to a random value ρ _∈_ Zφ( _N_ ) (φ( _N_ ) known only to Peggy) by sending α = _g_<sup>ρ</sup> mod _N_ to Victor (the verifier).

2. Victor chooses and sends Peggy a random challenge bit _c ∈{_ 0 _,_ 1 _}_ .

3. Peggy computes and sends back τ = ρ + _c_ log _g h_ .

4. Victor accepts if and only if _g_<sup>τ</sup> = α _h_<sup>_c_</sup> modulo _N_ .

This protocol is sound since, given a successful prover, one can apply the rewind technique to extract the discrete logarithm value similar to proving soundness of the well-known Schnorr protocol. Note that knowing _c_ in advance allows an attacker Eve, who does not have knowledge of log _g h_ , to trick Victor into accepting by sending him α = _g_<sup>τ</sup> _h_<sup>_−c_</sup> for an arbitrary τ of Eve’s choice in round 1.

The interactive proof above is converted to non-interactive dlnproof by applying the Fiat-Shamir heuristic described earlier. The proof is also repeated λ times (usually λ _≥_ 80) to reduce the soundness error from<sup><u>1</u></sup> 2<sup>(the chance of making a</sup> correct guess for _c_ at the beginning of the protocol) to 2<sup><u>1λ</u>.</sup>

## **2.3 MtA sub-protocol**

MtA stands for multiplicative-to-additive, which is a subprotocol involving 2 parties Alice and Bob holding secret values _a, b_ respectively. At the end of MtA, Alice obtains α and Bob obtains β such that _ab_ = α + β mod _q_ in which _q_ is

|Iteration|Alice|_a_|Bob|_b_|
|---|---|---|---|---|
|1|_Pi_|_ki_|_Pj_|γ_j_|
|2|_Pj_|_kj_|_Pi_|γ_i_|
|3|_Pi_|_ki_|_Pj_|_wj_|
|4|_Pj_|_kj_|_Pi_|_wi_|

Table 1: The 4 iterations of MtA between 2 parties _Pi_ and _Pj_ .

the order of the ECDSA group in use. During a TSS signing ceremony, for each pair of 2 different parties _Pi, Pj_ , MtA is run four times (Table 1). The input secret values are:

- _ki_ : _Pi_ ’s private share of the nonce inverse. If all _ki_ are leaked, the nonce inverse _k_ could be reconstructed ( _k_ = ∑ _ki_ ) and combined with the message hash _m_ and the signature _r, s_ ( _m, r, s_ are public information) to recover the private key _d_ of the TSS group based on the ECDSA formula _s_ = _k_ ( _m_ + _rd_ ) mod _q_ .

- γ _i_ : _Pi_ ’s private share of γ, a temporary secret value used to calculate the shares of _k_<sup>_−_1</sup> mod _q_ . Since δ = _k_ γ is published, the leakage of all γ _i_ also allows _k_ to be reconstructed ( _k_ =<sup><u>δ</u></sup> γ<sup>=</sup> ∑γδ _i_<sup>mod</sup><sup>_q_).</sup>

- _wi_ : a value depends on _Pi_ ’s private key share _xi_ and which members of the TSS group are currently running the signing ceremony (requiring _t/n_ members). If all _wi_ are leaked, the TSS private key _d_ can be reconstructed by _d_ = ∑ _wi_ mod _q_ .

As a conclusion, leaking MtA input _a_ or _b_ both lead to TSS private key recovery.

In the MtA protocol, both parties need to exchange encrypted values with each other in order to perform the desired computations. However, since there is a lack of trust between the parties, it is difficult to ensure that the encrypted values being sent are valid. To mitigate this problem, the protocol requires both parties to also send a range proof of the encrypted values.

At first glance, the requirement for a range proof may seem unnecessary, but it has been shown in [4] that the absence of a range proof can lead to a major breakdown in the security of the protocol. The reason for this is that range proofs ensure that the encrypted values are within a specified range, and prevent attackers from tampering with the values or sending invalid data.

## **2.4 ˜N** _,_ **h1** _,_ **h2**

The triple _N_ ˜ _, h_ 1 _, h_ 2 is used in MtA range proofs. Let _N_ ˜ _A, h_ 1 _A, h_ 2 _A_ and _N_ ˜ _B, h_ 1 _B, h_ 2 _B_ denote Alice and Bob’s _N_ ˜ _, h_ 1 _, h_ 2

## Slide 3

Figure 1: This lattice (represented by black dots) in R<sup>2</sup> can be constructed from either _{u_ 1 _, u_ 2 _}_ or _{v_ 1 _, v_ 2 _}_ .

respectively. It turns out that the following values are revealed by the range proofs:

- _zA_ = _h_<sup>_a_</sup> 1 _B_<sup>_h_ρ</sup> 2 _B_<sup>_A_mod</sup><sup>_N_˜</sup><sup>_B_via Alice range proof for</sup><sup>_a_. ρ</sup><sup>_A_is a</sup> random value in Z _qN_ ˜ _B_ .

- _zB_ = _h_<sup>_b_</sup> 1 _A_<sup>_h_ρ</sup> 2 _A_<sup>_B_mod</sup><sup>_N_˜</sup><sup>_A_via Bob respondent range proof for</sup> _b_ . ρ _B_ is a random value in Z _qN_ ˜ _A_ .

It can be seen that if Bob is able to eliminate _h_<sup>ρ</sup> 2 _B_<sup>_A_and compute</sup> discrete logarithm modulo _N_<sup>˜</sup> _B_ , then he could learn Alice’s private input _a_ . A similar result can be obtained when the attacker plays on the side of Alice.

In many implementations of TSS protocols, the values of _h_ 1 and _h_ 2 are chosen in such a way that there exists a value _x_ that satisfies the equation _h_ 1 = _h_<sup>_x_</sup> 2<sup>mod</sup><sup>_N_˜.To ensure the</sup> other parties that their chosen values are generated as such, a dlnproof of log _h_ 2 _h_ 1 is appended when they broadcast these values. This serves as a means of verifying that the values of _h_ 1 and _h_ 2 were indeed generated as specified, and that there are no discrepancies or malicious alterations made by any of the parties.

## **2.5 Vector enumeration in lattice**

A lattice in R<sup>_n_</sup> is a set of linear combinations with integer coefficients of _n_ linearly independent vectors<sup>*</sup> :

These independent vectors are together called a lattice basis. Different bases may generate the same lattice as shown in Figure 1.

*Only full-dimensional lattices are considered.

A lattice basis is good if it consists of nearly orthogonal, short vectors (e.g., _{v_ 1 _, v_ 2 _}_ in Figure 1). To convert a bad basis (e.g., _{u_ 1 _, u_ 2 _}_ in Figure 1) to a good one, we need a lattice basis reduction technique such as the well-known LLL algorithm. LLL runs in polynomial time and guarantees some qualities on the output basis. It is widely implemented and has useful applications in many areas, especially cryptanalysis.

In practice, there are often times when we need to search or enumerate through all vectors of a lattice (its basis is given) inside a particular region (e.g., a hypersphere or box) until some certain condition is met. To solve this kind of problem, we may use the following approach:

1. Apply LLL to the given basis, obtain _B_ = _{b_ 1 _, b_ 2 _,..., bn}_ . The result vector _v_ can now be represented by ∑<sup>_n_</sup> _i_ =1<sup>_cibi_.</sup>

2. Determine the possible range [ _ci_ -min _, ci_ -max] for each _ci_ . This is done by first projecting each _bi_ and the searching region onto the orthogonal line of the subspace generated by _B \{bi}_ to obtain _b_<sup>_∗_</sup> _i_<sup>and a line segment. Then, only</sup> _ci_ such that _cib_<sup>_∗_</sup> _i_<sup>lies in that segment is considered valid.</sup> Note that the purpose of projection is to make sure that we are working on a subspace that is only affected by _bi_ . In other words, if _ci_ is out of range ( _cib_<sup>_∗_</sup> _i_<sup>falls out of the</sup> segment), then no combination of the remaining vectors _B \{bi}_ is able to fix that error.

3. Looping over all _ci_ to search for the desired vector _v_ . Specifically, the search space _S_ for _v_ is equivalent to the Cartesian product of the ranges [ _ci_ -min _, ci_ -max]. Hence, its size _|S|_ is equal to ∏<sup>_n_</sup> _i_ =1<sup>(</sup><sup>_ci_-max</sup><sup>_−ci_-min +1).</sup>

One may figure out that the enumeration approach above is not optimal since it does not make use of early-exit or pruning. For example, when _c_ 1 is determined, the actual range for _c_ 2 may be adaptively smaller than the generic range [ _c_ 2-min _, c_ 2-max] but this fact is ignored.

However, the approach allows for seamless integration of the meet-in-the-middle technique (MITM) to significantly improve its time complexity (possibly down to _O_ ( ~~�~~ _|S|_ )) when the required condition on _v_ can be converted into some form that allows separated working on 2 complementary subspaces _S_ 1 _, S_ 2 of _S_ . For example, if _v_ = _c_ 1 _b_ 1 + _c_ 2 _b_ 2 and the condition on _v_ can be expressed in _c_ 1 _, c_ 2 as _f_ 1( _c_ 1) = _f_ 2( _c_ 2), then _S_ 1 = [ _c_ 1-min _, c_ 1-max], _S_ 2 = [ _c_ 2-min _, c_ 2-max] and by applying MITM, the searching time will be reduced from _O_ ( _|S|_ ) to _O_ ( _|S_ 1 _|_ + _|S_ 2 _|_ ) at the cost of some memory<sup>†</sup> .

For some optimization, one may consider applying a more advanced lattice enumeration technique inside each of the subspaces _S_ 1 _, S_ 2 whenever possible.

> †Basically, by the technique, we loop over _S_ 1 and cache all _f_ 1( _c_ 1) to memory as a table (requiring _O_ ( _|S_ 1 _|_ ) time and space), then loop over _S_ 2 until an entry for _f_ 2( _c_ 2) is found (requiring _O_ ( _|S_ 2 _|_ ) time).

## Slide 4

Figure 2: Hashing ( _i_ 1 _, i_ 2) by simply concatenating their byte representations.

Figure 3: ( _i_ 1 _, i_ 2) and ( _i_<sup>_′_</sup> 1<sup>_,i′_</sup> 2<sup>) both produce the same hash out-</sup> put.

## **3 Attacks**

The Threshold ECDSA technology is a recent development in the field of cryptography. As with any new technology, there is a risk of implementation flaws that can lead to potential attacks. In sections 3.1 and 3.3, we will discuss some potential attack vectors that can arise in the context of Threshold ECDSA and their triggering conditions.

The focus of our attack will be on the leaking of secret shared values _x_ in _z_ = _h_<sup>_x_</sup> 1<sup>_h_ρ</sup> 2<sup>mod</sup><sup>_N_˜during the MtA rounds.</sup> This can be accomplished if a malicious party generates a triple _N_<sup>˜</sup> _, h_ 1 _, h_ 2, where _h_ 1 and _h_ 2 are chosen in such a way that it is possible to eliminate _h_<sup>ρ</sup> 2<sup>from</sup><sup>_z_and compute discrete</sup> logarithm to base _h_ 1 modulo _N_<sup>˜</sup> .

For eliminating _h_<sup>ρ</sup> 2<sup>, we let</sup><sup>_h_2 =</sup><sup>_h_</sup> 1<sup>_e_mod</sup><sup>_N_˜‡ in which</sup><sup>_e_is a</sup> divisor of ord( _h_ 1). Now, raising _z_ to the power of _f_ =<sup>ord</sup> _e_<sup><u>(</u></sup><sup>_h_</sup><sup><u>1)</u></sup> , we have _z_<sup>_f_</sup> = ( _h_ 1<sup>_f_)</sup><sup>_x_mod</sup><sup>_N_˜. Solving it (log</sup> _h_ 1<sup>_fzf_) yields</sup><sup>_x_mod</sup> _e_ . When _e_ is greater than _q_ (the ECDSA group order), _x_ is fully recovered. However, this approach will not work unless we can forge a dlnproof for the inexistent log _h_ 2 _h_ 1 =<sup><u>1</u></sup> _e_<sup>mod</sup> ord( _h_ 1). By utilizing some implementation flaws, we are able to do so!

To make discrete logarithm easy to compute, we choose _N_ ˜ to have one of the following properties, depending on the exploitation context (e.g., which checks are performed on _N_<sup>˜</sup> ):

- ( _square_ ) _N_<sup>˜</sup> = _p_<sup>2</sup> . Computing a discrete log is similar to how the Paillier cryptosystem decrypts a ciphertext, exploiting the fact that (1 + _kp_ )<sup>_x_</sup> = 1 + _kpx_ mod _p_<sup>2</sup> . Since

> ‡Currently, we consider working over Z _∗N_ ˜<sup>. However, as Z</sup> _N_<sup>_∗_</sup> ˜<sup>can be de-</sup> composed into a direct product of smaller subgroups, working over any of these subgroups is also fine. In that case, only the projections of _h_ 1 _, h_ 2 onto the working subgroup are of concern and it may not hold that _h_ 2 = _h_<sup>_e_</sup> 1 modulo _N_<sup>˜</sup> (it holds over the subgroup only). For example, let _N_<sup>˜</sup> = _p_ ˜ ˜ _q_ , then Z _N_<sup>_∗_</sup> ˜<sup>= Z</sup><sup>_∗_</sup> _p_ ˜<sup>_×_Z</sup><sup>_∗_</sup> _q_ ˜<sup>and one may consider working over Z</sup><sup>_∗_</sup> _p_ ˜<sup>instead of Z</sup><sup>_∗_</sup> _N_ ˜<sup>. In that</sup> case, _h_ 1 and _h_ 2 mod _q_ ˜ are ignored, only _h_ 2 = _h_<sup>_e_</sup> 1<sup>mod</sup><sup>_p_˜ holds.</sup>

the unknown _x_ has been moved out of the exponent position, solving for it becomes easy.

- ( _smooth_ ) φ( _N_<sup>˜</sup> ) is smooth. It is well-known that the hardness of the discrete logarithm problem depends on the size of the largest prime factor of the base’s order. When this order is a product of only small primes, computing discrete logarithm becomes easy.

- ( _unbalanced_ ) _N_<sup>˜</sup> = _p_ ˜ _q_ ˜ for just small _p_ ˜ (e.g., 256-bit _p_ ˜ compared to 2048-bit _N_<sup>˜</sup> ). Computing discrete logarithm over Z ˜ _p_ instead of Z ˜ _N_ drastically reduces the difficulty.

## **3.1** α **-shuffle Attack**

### **3.1.1 The Flaw**

In practical context, the dlnproof is carried out in a noninteractive manner by using the Fiat-Shamir heuristic, which requires hashing a list of integers including _N_ , _g_ , _h_ , α1, α2, ..., αλ (α _i_ is α at the _i_ -th iteration of the proof). To achieve this, some implementations just concatenate the byte representations of the integers with some delimiter before feeding to a Cryptographic hash function as shown in Figure 2.

Let bytes(), int() denote integer-to-bytes and bytes-tointeger conversion functions respectively. Let ’ _|_ ’ denote byte concatenation (should not be confused with ’ _|_ ’ as ’divides’ in the context of integers). Let rand() denote the function that returns a random element from an input set. Let _H_ () denote the vulnerable hashing implementation and _D_ denote the byte representation of the delimiter used by _H_ .

Recall that at the beginning of a dlnproof, Peggy (the prover) is required to commit to an α _i_ for each of the λ iterations of the corresponding interactive proof. The idea is, Peggy first commits to a stream of bytes in the format of _a|D|a|D|a|...|D|a_ . When _H_ is applied, the challenge bits _ci_ are determined and Peggy can then flexibly choose each α _i_ to be equal to int( _a_ ) or int( _a|D|a_ ), depending on which value causes Victor (the verifier) to output ’accept’ for that iteration. Figure 4 demonstrates this idea.

### **3.1.2 The Attack**

Algorithm 1 allows Peggy to forge a valid dlnproof for arbitrary _g, N_ of his choice. The algorithm outputs _h_ and a dlnproof for log _g h_ modulo _N_ consisting of λ pairs of α _i,_ τ _i_ .

Note that if the condition at step 4c of Algorithm 1 holds, subsequent modification of α _i_ will not affect the challenge bits _ci_ since _H_ ( _g, h, N,_ α1 _,_ α2 _,...,_ αλ) will be unaltered as long as the number of instances of _a_ remains the same (regardless of how they are interpreted). Moreover, it can be verified that _g_<sup>τ</sup><sup>_i_</sup> = α _ih_<sup>_ci_</sup> for all _i_ when the algorithm returns, hence the output dlnproof is correct. As the list of α _i_ (α _,_ α _,...,_ α _,_ β _,_ β _,...,_ β) is rearranged based on the challenge bits _ci_ , we name this technique α-shuffle.

## Slide 5

Figure 4: α _i_ are chosen after the challenge bits _ci_ are revealed.

### **Algorithm 1** α-shuffle dlnproof forging

Input: _g, N_ .

Output: _h_ , dlnproof for log _g h_ mod _N_ .

1. Let τ = rand(Zord( _g_ )). Let α = _g_<sup>τ</sup> mod _N._ Set all τ _i_ = τ.

2. Let _a_ = bytes(α) _._ Let β = int( _a|D|a_ ).

5. Go back to step 1.

Now, we know how to forge a dlnproof. Ideally, an attacker may execute the above algorithm with _g_ = _h_ 2 = 1<sup>§</sup> and a discrete-log-friendly _N_<sup>˜</sup> to obtain _h_ 1 and a malicious dlnproof for log _h_ 2 _h_ 1 that should be successfully verified by other TSS parties. Additionally, _h_ 1 is likely to have large order (it is just a virtually random element in Z ˜ _N_ ), allowing the full MtA secret input _x_ to be extracted from _z_ = _h_<sup>_x_</sup> 1<sup>_h_ρ</sup> 2<sup>mod</sup><sup>_N_˜. As</sup> explained in Section 2.3, this results in full recovery of the TSS private key.

### **P1: h2 must not equal 1** **_._**

If _h_ 2 can be wrapped around, then just let _h_ 2 = _N_<sup>˜</sup> + 1. Otherwise, let _h_ 2 = _N_<sup>˜</sup> _−_ 1 (need _z_ squared to eliminate _h_ 2).

### **P2: A dlnproof for** log **h1h2 is also required.**

Add an extra condition to ensure that Algorithm 1 will not return unless log _h g_ modulo _N_<sup>˜</sup> exists. Since _N_<sup>˜</sup> has already been chosen to be discrete-log-friendly, testing this condition should not be hard. As a result, it is feasible to compute and build an ordinary dlnproof for log _h_ 1 _h_ 2 after forging one for log _h_ 2 _h_ 1.

### **P3:** α **i must be smaller than N.**<sup>**˜**</sup>

Instead of picking a random τ and computing α = _g_<sup>τ</sup> mod _N_ as in step 1 of Algorithm 1, one can pick a suitable α first, then compute τ = log _g_ α mod _N_ . Here, ’suitable’ means that α is small enough (so that β _< N_ for _a_ = bytes(α), β = int( _a|D|a_ )) and τ can be successfully computed. For example, supposing that _N_<sup>˜</sup> = _p_ ˜ _q_ ˜ _, N_<sup>˜</sup> is 2048-bit, _p_ ˜ is 512-bit and _g_ = _h_ 2 = 1 mod _p_ ˜, we have 1 _, p_ + 1 _,_ 2 _p_ + 1 _,..._ are some candidates for α since they are small and α = 1 mod _p_ is the minimum requirement for the existence of log _g_ α.

### **P4: The dlnproof hashing context must include an auxiliary input which is only determined after N**<sup>**˜**</sup> _,_ **h1** _,_ **h2 are committed.**

The probability that Algorithm 1 succeeds in only one run is:

### **3.1.3** α **-shuffle in practice**

This part briefly describes how to bypass different checks or policies (P) applied to _N_<sup>˜</sup> _, h_ 1 _, h_ 2 encountered in practical Threshold ECDSA implementations.

> §One may consider incrementing α by _N_ (α = α + _N_ ) instead of picking another random τ in step 1 of Algorithm 1 to avoid an infinity loop in this case.

For λ = 80, _P ≈_ 0 _._ 6441, which is also the probability that Eve, an attacker, successfully applies α-shuffle in this situtation. This is because Eve has to execute Algorithm 1 without a complete definition of _H_ since it depends on an unkown input. To continue the attack, Eve has to break early (after step 3) and broadcast a commitment for a might-be-working triple of _N_ ˜ _, h_ 1 _, h_ 2. Later on when the unknown input is revealed, Eve resumes to step 4 of Algorithm 1 to check if a dlnproof can be successfully forged with respect to the committed triple. If

## Slide 6

Figure 5: _N_<sup>˜</sup> _, h_ 1 _, h_ 2 and _N_<sup>˜</sup> _, h_<sup>ˆ</sup> 1 _, h_<sup>ˆ</sup> 2 having the same commitment.

Eve is unlucky, the key-generation ceremony has to abort and other TSS parties might be able to identify Eve as the culprit.

However, it is likely that the commitment scheme is hashbased and also depends on the vulnerable hash implementation _H_ (module/function reuse is common in software development). If it is true, Eve will have a way to escape in case the dlnproof can not be forged. The idea is to reveal a different triple _N_<sup>˜</sup> _, h_<sup>ˆ</sup> 1 _, h_<sup>ˆ</sup> 2 such that it has the same commitment as _N_<sup>˜</sup> _, h_ 1 _, h_ 2 and log _h_ ˆ2 _h_<sup>ˆ</sup> 1 mod _N_<sup>˜</sup> exists, allowing a correct dlnproof to be built. Figure 5 demonstrates this idea. Note that the commit function is supposed to simply return _H_ ( _L_ ) in which _L_ is a list constructed from a secret decommitment and to-be-commited values.

Since the input _g_ = _h_ 2 can be freely chosen, putting a delimiter inside its byte representation is usually not a problem. However, if 0 _≤ h_ 1 _, h_ 2 _, h_<sup>ˆ</sup> 1 _, h_<sup>ˆ</sup> 2 _< N_<sup>˜</sup> is required, the uncontrolled output _h_ = _h_ 1 will also need to be small enough so that _h_<sup>ˆ</sup> 1 _< N_<sup>˜</sup> can be satisfied<sup>¶</sup> . This can be achieved by carefully choosing α _,_ β such that _b_ = bytes(β), α = int( _b|D|b_ ) and β _|_ α beforehand<sup>||</sup> . As a result, _h_ =<sup><u>α</u></sup> β<sup>is small regardless of</sup><sup>_N_˜.</sup>

To sum up, whenever Eve fails to complete an attack, she can safely fallback to the usual workflow for not being detected while trying to trigger (or simply wait for) another key generation or re-sharing ceremony to conduct another attack. Eve may keep repeating this process until success. The expected number of failures is:

For λ = 80 _, P_ = 0 _._ 6441, this value is approximately 0 _._ 5526.

### **3.1.4 Mitigation**

To mitigate α-shuffle attack, it is necessary to adopt a nonambiguous encoding scheme to construct the list-of-integer hashing function _H_ . There should not exist two different lists encoded into the same byte sequence. A rule of thumb is that if you do not have a deterministic way to decode the

> ¶Another workaround is to choose small input _g_ = _h_ 2, then brute-force the first 3 steps of Algorithm 1 until a delimiter appears in the byte representation of the output _h_ = _h_ 1. However, this approach is only suitable for short delimiters.

> ||The correctness of Algorithm 1 does not rely on whether β = int( _a|D|a_ ) (as in the original version) or α = int( _b|D|b_ ) (as in the version being described).

byte sequence (back to the original list of integers), you are likely doing it wrong. A simple fix is to always include the length of each integer. Other popular encoding schemes like Protocol Buffers (Protobuf [5]), Abstract Syntax Notation One (ASN.1 [6]) or Tag-Length-Value (TLV [7]) are also fine.

It is important to note that changing the way _H_ works requires an update to all existing systems and software in a TSS group. However, the potential security benefits that result from implementing such measures are substantial, and can help to protect against the risks associated with hash collision.

## **3.2 c-split Attack**

### **3.2.1 The Flaw**

The dlnproof requires repeatedly generating random challenge bit _c ∈{_ 0 _,_ 1 _}_ . However, instead of repeating the interactive proof with binary challenge _ci ∈{_ 0 _,_ 1 _}_ , the implementation decide to use a much larger challenge set (e.g., all possible outputs of SHA-256 or Z2256) in only one run. It turns out that a larger challenge set does not result in a better soundness error ( _<_<sup><u>1</u></sup> 2<sup>). Let</sup><sup>_g ∈_Z</sup> _N_<sup>_∗_,</sup><sup>_h_=</sup><sup>_g_2and 2</sup><sup>_|_ord(g).</sup> Since 2 has no inverse modulo ord(g), log _h g_ =<sup><u>1</u></sup> 2<sup>doesnot</sup> exist. However, when 2 _| c_ (probability<sup><u>1</u></sup> 2<sup>), Peggy is able to</sup> forge a correct dlnproof for it by having τ = ρ + 2<sup>_<u>c</u>_.</sup>

### **3.2.2 The Attack**

The attack is straightforward. Let _e_ be a small divisor of ord( _h_ 1) (recall that _h_ 2 = _h_<sup>_e_</sup> 1<sup>mod</sup><sup>_N_˜).Whenbuildinga</sup> dlnproof for log _h_ 2 _h_ 1, one can just keep brute-forcing ρ until _c_ is divisible by _e_ (probability<sup><u>1</u></sup> _e_<sup>).Thiswillnotbe</sup> hard if _e_ is, say, only 32-bit long. Consequently, (α _,_ τ) = ( _h_<sup>ρ</sup> 2<sup>mod</sup><sup>_N_˜</sup><sup>_,_ρ +</sup><sup>_<u>c</u>_</sup> _e_<sup>)isavaliddlnproofforthenonexistent</sup> log _h_ 2 _h_ 1. Since _e | c_ is required to forge the proof, we name the technique c-split.

However, it is not quite done yet since only _x_ mod _e_ for some secret MtA input _x_ ( _ki_ ,γ _i_ or _wi_ ) can be recovered during a signing ceremony while _e_ cannot be made arbitrarily large or the brute-forcing step above becomes infeasible. To fully recover the TSS private key, some extra work is needed.

Firstly, given a message-signature pair ( _m,_ ( _r, s_ )), one can leverage the leaked information ( _ki_ , γ _i_ , _wi_ mod _e_ for 1 _≤ i ≤ t_ , recall that _t_ is the number of TSS parties participating in the signing ceremony) to obtain the following equation:

In which solving for the small unknowns _w_ ¯ _,_ ¯γ (bounded by <u>�</u> _teq_ <u>�) would give the TSS private key</u><sup>**</sup> .

> **Deriving (1) from the ECDSA formula _s_ = _k_ ( _m_ + _rd_ ) mod _q_ requires some arithmetic:

1. Multiply both sides by γ to separate the product of 2 unknowns _kd_ (recall that δ = _k_ γ is a public value).

## Slide 7

And also:

For some elements _P, Q_ of the ECDSA group<sup>††</sup> .

Next, multiple pairs of message-signature must be collected. Supposing that _l_ pairs are given:

the right-hand side. To make the two subspaces balanced, one may consider splitting a single _ci_ , say _c_ 1 = _cam_ + _cb_ for a suitable _m_ , then repartitioning the set of _ci_ (has now become _{ca, cb, c_ 2 _, c_ 3 _,...cl_ +1 _}_ ) accordingly<sup>‡‡</sup> .

Note that all _w j_ need not be the same since each depends on the set of participating parties that may change for each signing ceremony. However, they all equal _d_ mod _q_ . Therefore, a single _w_ ¯ is used for all _j_ to reflect this fact.

Rewriting (3) as a vector equation, one obtains (4).

This is exactly an instance of the lattice enumeration problem described in Section 2.5. The left-hand side columns are basis vectors for a ( _l_ + 1)-dimensional lattice. The required condition on the result vector _v_ is that its first entry _w_ ¯ must satisfy (2). Since 0 _≤ w_ ¯ _,_ γ¯1 _,_ γ¯2 _,...,_ ¯γ _l ≤_ � _teq_ �, the searching region is in fact a hypercube. Its edge has a length of � _teq_ � and (0 _, b_ 1 _, b_ 2 _,..., bl_ ) is one of its vertices.

Note that the equation (2) makes it very straightforward to apply MITM in this case. After the lattice basis is reduced with LLL, let ω _i_ denote the first entry of the new basis’s _i_ -th vector, then _w_ ¯ = ∑ _ci_ ω _i_ . Let _Wi_ = ω _iP_ , from (2) we have ∑ _ciWi_ = _Q_ . Decomposing the search space is now as simple as shifting some _ciWi_ from the sum on the left-hand side to

The only remaining question is how many messagesignature pairs are required (i.e., the minimum value for _l_ ) to solve for _w_ ¯. The answer is that it depends on how much computational power an attacker has or is willing to pay for. With _t_ fixed to 32<sup>§§</sup> , Table 2 gives the search space size ( _|S|_ ) under various configuration for _e_ and _l_ . From the cell corresponding to ( _e, l_ ) = (2<sup>56</sup> _,_ 2), it can be understood that if the attacker is willing to construct 2<sup>56</sup> different dlnproof challenges and <u>104</u> _<u>.</u>_ <u>71</u> perform about 2 _×_ 2 <u>2</u> elliptic curve group additions, then the TSS private key can be recovered with only 2 signatures.

### **3.2.3 c-split in practice**

The c-split exploitation technique should work well in practice. One can even choose a small _e_ , say 32-bit long, since the required number of signatures is usually not a practical issue. The payload of the attack ( _N_<sup>˜</sup> _, h_ 1 _, h_ 2 and dlogproof for

> 2. Compute (γ˜ _, w_ ˜) = (γ _, w_ ) mod _e_ by summing up γ _i_ and _wi_ mod _e_ respectively.

> 3. Substitute γ = ¯γ _e_ + ˜γ and _d_ = _w_ = _we_ ¯ + _w_ ˜ mod _q_ into the formula. Note that _a, b_ are just aliases for<sup><u>δ</u></sup> _s_<sup>_<u>r</u>_and</sup><sup><u>γ˜</u></sup><sup>_s−_δ</sup><sup>_m_</sup> _es_<sup>_−_δ</sup><sup>_r_˜</sup><sup>_w_</sup> mod _q_ respectively. Since γ _, w < tq_ , γ¯ _, w_ ¯ _≤_ � _teq_ �. If _w_ ¯ is determined, the TSS private key _d_ = _we_ ¯ + _w_ ˜ mod _q_ can also be recovered.

> ††Let _G_ denote the group generator defined by the ECDSA signature scheme and _D_ = _dG_ denote the public key corresponding to _d_ , then ( ¯ _we_ + _w_ ˜) _G_ = _D_ . Therefore, _P_ and _Q_ are just aliases for _eG_ and _D − wG_ ˜ respectively. ‡‡This idea is similar to the baby-step-giant-step (BSGS) technique.

> §§There is a known scalability issue with the TSS design as it has time and communication complexity of _O_ ( _t_<sup>2</sup> ). _t_ = 32 is a quite high value in practice.

log _h_ 2 _h_ 1) looks statistically the same as a legit one.

However, there is a case in which Bob respondent range proof in MtA is omitted. As a result, an attacker no longer has access to γ _i_ and _wi_ mod _e_ for each signing ceremony. Note that omitting Bob respondent proof comes with its own issues such as unidentifiable abort, i.e., a malicious party may corrupt the signing ceremony without being detected.

In this situation, with enough malicious cooperating parties, it’s possible to recover the TSS private key with just one signature. The idea is to have a pairwise relatively prime set _{e_ 1 _, e_ 2 _,..., el}_ (the _e_ values from _l_ malicious parties) so that _ki_ mod _e_ π = _e_ 1 _e_ 2 _...el_ can be recovered by applying the Chinese remainder theorem (CRT) to _ki_ mod _e j_ for 1 _≤ j ≤ l_ . Now, the malicious parties need to solve for _k_ satisfying:

## Slide 8

|e _\l_|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|---|
|2<sup>32</sup>|202.48|177.24|151.26|126.03|100.40|76.13|51.57|27.56|
|2<sup>40</sup>|186.62|152.43|119.23|85.72|52.61|20.06|0.00|0.00|
|2<sup>48</sup>|171.01|128.52|87.74|46.29|1.58|0.00|0.00|0.00|
|2<sup>56</sup>|154.39|104.71|54.78|4.75|0.00|0.00|0.00|0.00|
|2<sup>64</sup>|138.40|80.74|22.96|0.00|0.00|0.00|0.00|0.00|

Table 2: The search space size on the log2 scale for different ( _e, l_ ). _t_ is always 32. The data are generated by simulating the signing and exploiting process with SageMath v9.5 [8]. Each test is repeated 1000 times for increased reliability.

λ is low enough with regards to the computational power of a malicious prover, the prover can then repeat the proof generation until a correct guess for all _ci_ is found, thus successfully forge a dlnproof.

Similar to Section 3.3, let _k_<sup>¯</sup> = � _ek_ π � ( _k_ = _ke_<sup>¯</sup> π + _k_<sup>˜</sup> ), _P_ = _e_ π _R_ and _Q_ = _G − kR_<sup>˜</sup> , then the rest of the attack is about searching for _k_<sup>¯</sup> _<_ � _etq_ π � such that _kP_<sup>¯</sup> = _Q_ . [9] is a very well-optimized tool to tackle this kind of problem. It has been used to crack a 114-bit secp256k1 private key for a reward of 1.15 BTC, so one can expect 1.15 BTC to be a reliable upper bound on the cost of solving for _k_<sup>¯</sup> when � _etq_ π � _≤_ 2<sup>114</sup> (assume that the curve in use is also secp256k1).

Again, the only remaining question is how many malicious parties are required. _l_ = 3 is quite practical, while _l_ = 2 is also possible but the attack will be costly. In practice, making a decision on _l_ should depend on many factors such as the benefit from a successful attack, the cost to become or corrupt a member of the targeted TSS group, ...

### **3.2.4 Mitigation**

In a proof system, the most important factor to determine the number of proof iterations is its soundness error. Deciding to not repeat a proof without proving that the proof has a negligible soundness error is like taking a crazy risk.

It is therefore highly advised that protocols are implemented in compliance with their specifications. Any attempt to optimize the implementation without a proper understanding of its security implications should be avoided, as this might create vulnerabilities exploitable by attackers.

## **3.3 c-guess Attack**

### **3.3.2 The Attack**

The attack is straightforward: the malicious prover chooses random challenge bits _ci_ and applies _H_ (a hash function according to the Fiat-Shamir transformation) to the corresponding payload prepared for those guessed _ci_ to check if the actual output challenge bits are the same as the guessed ones. If they are not, the prover simply makes another guess and retries until a correct one is made. The expected number of trials is 2<sup>λ</sup> .

### **3.3.3 Mitigation**

As discussed in 2.2, the dlnproof requires a minimum number of iterations to achieve a certain level of security. CGGMP21 recommends the number of iterations to be at least 80 which should be enforced by all implementations.

## **4 Impact Factors**

In this section, we will provide a comprehensive summary of our study’s key findings. We will begin by recapping the implementation flaws that enabled our attacks on the dlnproof protocol. We will then discuss the detrimental impact of our attacks. Finally, we will provide an estimate of the funds that were saved due to our swift actions in contacting product owners. By highlighting the critical importance of thorough testing and robust security measures in threshold cryptography, this section underscores the significance of our research.

### **3.3.1 The Flaw**

## **4.1 Weaknesses**

In dlnproof, each proof iteration requires the verifier to send a binary challenge _ci ∈{_ 0 _,_ 1 _}_ . The probability for a successful guess on all _ci_ is 2<sup><u>1λ</u>for λ iterations. It is important to note</sup> that applying Fiat-Shamir heuristic allows the prover to not be punished for making an incorrect guess. Therefore, when

During our research, we identified several implementation flaws of dlnproof that can be exploited, such as hash collisions resulting from concatenating hash values. To avoid this issue, we recommend using a non-ambiguous encoding

## Slide 9

scheme. Moreover, reducing the number of rounds in the protocol can significantly undermine its security. It is imperative to follow the protocol specifications and perform an adequate number of binary challenges, which is 80 as specified in CGGMP21.

## **4.2 Key Recovery**

The attacks we presented in this paper can rebuild the ECDSA private key, despite it not being computed in the Threshold ECDSA protocol. This is achievable because all private values that pass through the MtA protocol can be recovered through our attacks. These values play a significant role in the logic of computing ECDSA signatures. With a series of signatures and secret values, an attacker can quickly re-compute the private key.

This has significant implications for the security of Threshold ECDSA if implemented wrongly, as the reconstruction of the private key would allow an attacker to forge arbitrary signatures and gain complete control over the system. As such, it is critical to identify if the implementation are vulnerable to our attacks and take measures as we suggest to enhance the security of the library.

## **4.3 Impacts**

In our study, we developed proof-of-concept attacks on various open-source projects that implement Threshold ECDSA. Our PoCs demonstrated that, in most cases, a single malicious party and one signing ceremony are enough to recover the private key. The details of the affected implementations can be found in Table 3. In addition to the PoC attacks on opensource projects implementing Threshold ECDSA, we also created demonstrations that successfully withdraw all funds from a deployed development environment. These simulations serve to illustrate the potential impact that such attacks could have on a production level.

## **5 Conclusions**

This paper introduces new attack vectors leveraging common implementation flaws of Threshold ECDSA, a new cryptographic protocol. The paper warns of the dangers of relying on untested code and highlights the gap that often exists between design and implementation. It emphasizes that modifications made to the design to meet specific needs can lead to serious bugs and that the implementation may not always be a direct representation of the design. The paper stresses the importance of thorough testing of implementations to guarantee the security and stability of the technology in use. The findings of this paper have significant consequences for various vendors who use Threshold ECDSA, which is widely adopted in production environments. Our disclosure may have prevented a potential major hack in the blockchain industry.

## Slide 10

|Implementations|Attack Technique|PoC||Required number of||
|---|---|---|---|---|---|
||||Malicious parties|(Re)sharing ceremonies|Signing ceremonies|
|Axelar (tofn)|c-split|YES|1|1|2|
|Binance/BNBChain (tss-lib)|α-shuffle|YES|1|1|1|
|ING Bank (threshold-signatures)|c-split|YES|1|1|2|
|Keep Network/Threshold Network|α-shuffle|YES|1|1|1|
|Multichain (fastMPC)|α-shuffle|YES|1|1|1|
||c-guess|YES|1|1|1|
|Swingby (tss-lib)|α-shuffle|YES|1|1|1|
|Taurus (multi-party-sig)|α-shuffle|YES|1|1.5526|1|
|Thorchain (tss-lib)|α-shuffle|YES|1|1|1|
|ZenGo X (multi-party-ecdsa)|c-split|YES|2|1|1|

Table 3: Affected implementations.

The table above was calculated based on the assumption that the attacker could practically break 64-bit security. This table was last updated on March 2023. For the updated table, please visit verichains.io/tsshock.

## Slide 11

## **References**

- [1] Rosario Gennaro and Steven Goldfeder. Fast Multiparty Threshold ECDSA with Fast Trustless Setup. Cryptology ePrint Archive, Paper 2019/114, 2019. https://epri nt.iacr.org/2019/114.

- [2] Rosario Gennaro and Steven Goldfeder. One Round Threshold ECDSA with Identifiable Abort. Cryptology ePrint Archive, Paper 2020/540, 2020. https://epri nt.iacr.org/2020/540.

- [3] Ran Canetti, Rosario Gennaro, Steven Goldfeder, Nikolaos Makriyannis, and Udi Peled. UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts. Cryptology ePrint Archive, Paper 2021/060, 2021. http s://eprint.iacr.org/2021/060.

- [4] Dmytro Tymokhanov and Omer Shlomovits. Alpha-rays: Key extraction attacks on threshold ecdsa implementations. Cryptology ePrint Archive, Paper 2021/1621, 2021. https://eprint.iacr.org/2021/1621.

- [5] Protobuf. https://protobuf.dev/.

- [6] ASN.1. https://en.wikipedia.org/wiki/ASN.1.

- [7] TLV. https://en.wikipedia.org/wiki/Type%E2% 80%93length%E2%80%93value.

- [8] Sage Math. https://www.sagemath.org/.

- [9] Kangaroo. https://github.com/JeanLucPons/Kan garoo.
