---
title: "Quantum Cryptography (PQC) for Hackers"
speakers: ["Eric 'Eijah' Anderson-Post"]
conference: "DEF CON"
conference_full: "DEF CON 34"
year: 2026
source_type: "workshop-materials"
source_dir: "DEF CON 34 - Workshops - Eric - Eijah - Anderson-Post - Quantum Cryptography (PQC) for Hackers - Student Resources"
files_included: 3
files_skipped: 0
text_chars: 15820
redacted_secrets: 0
sha256: "2225a208f8ecfe0916b74122f1d43d9dfe5f7edd5f5302b13458789cd3601c52"
converted_at: "2026-08-12T07:17:47Z"
---

# Quantum Cryptography (PQC) for Hackers

**Speakers:** Eric 'Eijah' Anderson-Post  
**Conference:** DEF CON 34 (workshop materials)  
**Contents:** 3 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Materials

### `DEF CON 34 - Workshops - Eric - Eijah - Anderson-Post - Quantum Cryptography (PQC) for Hackers - Student Resources/Outline.txt`

```text

[ ABSTRACT ]
Secure communications are not a luxury — they are a foundational requirement for human dignity in the digital age. Our most meaningful conversations, transactions, and decisions demand end-to-end encryption, strong authentication, and verifiable integrity. The notion that "only those with something to hide need strong crypto" is not merely lazy; it is dangerously shortsighted. Privacy is the space where autonomy, intimacy, and authentic human experience thrive. When that space is violated, the damage ripples far beyond the individual.

For decades, classical public-key cryptography has quietly protected everything from online banking to private messaging. That era is ending. Quantum computers are advancing rapidly, and the break of today's asymmetric algorithms — often called the Quantum Apocalypse — is no longer a question of if, but when. The window to prepare is narrowing. Migration must begin now.

In this workshop, you'll implement PQC algorithms from the NSA's CNSA Suite 2.0. You'll use C++, OpenSSL and Linux to demonstrate the secure usage of ML-KEM, ML-DSA, AES-256, and SHA-512. You'll leave with clean, reusable code, deep implementation insight, and the practical skills needed to integrate PQC into real-world systems.

We might not all have something to hide, but we all have something worth protecting.


[ WORKSHOP GOALS ]
* Understand why PQC and CNSA 2.0 matter
* Implement all CNSA 2.0 algorithms using OpenSSL 4.0.0
* Discuss realistic threat scenarios (e.g., secure channel, code signing, hybrid TLS-like handshake) and how PQC algorithms help
* Leave the Workshop with working code knowledge, including the pro's/con's of the PQC algorithms (crypto agility, implementation complexity, large keys/signature sizes, performance overhead, and the novelty of Lattice-based algorithms)

[ OUTLINE ]
1) Introduction	
	a. Quick intro to the instructor 
	b. Workshop format
		1. Hands-on
		2. Minimal slides
		3. Coding lessons
		4. Scheduled breaks
2) Configuration
	a. Setting up our environment
	b. Configuring and running the C/C++ Makefiles
	c. Compiling, linking, and running the applications		
	d. During this workshop we'll use a variety of tools, including…
		1. Linux (Debian-based kernel preferred)
		2. C, C++ programming languages (C++ 20 or above)		
		3. The GNU Compiler (GCC 12.2.0 or above)
		4. CMake build system (3.18.4 or above)
		5. Boost C++ Libraries (1.86.0 or above)
		6. OpenSSL Cryptlib (4.0.0 or above)
	d. HANDS-ON LESSON: Verify that GCC, CMake, and OpenSSL are configured correctly: "Hello, Hacker PQC World"	
3) Motivation
	a. INTERACTIVE DISCUSSION
	b. What is the purpose of this workshop?
		1. Implement all of the PQC algorithms specified in the NSA's Commercial National Security Algorithm (CNSA) Suite 2.0 specification using OpenSSL 4.0.0
		2. Understand the pro's/con's of PQC algorithms: large keys/signature sizes, performance overhead, and the novelty of Lattice-based algorithms
		3. Leave with clean, reusable code, deep implementation insight, and the practical skills needed to integrate PQC into real-world systems	
	c. Why C++?
		1. Performance
		2. Control
		3. Interoperability with existing codebases
	d. Why OpenSSL?
		1. Open Source
		2. Tried and true
		3. The defacto standard in cryptographic libraries
		4. Early-adopter of PQC algorithms
		5. Multi-platform support	
4) Quantum Computing
	a. INTERACTIVE DISCUSSION
	b. What are Quantum Computers?
		1. Quantum Entanglement and the Speed of Light (“Spooky Action at a Distance” - Einstein)
		2. Utilize Qubits (with error correction) can exist in multiple states at once (0, 1, or both)
		3. Can explore multiple possibilities simultaneously (superposition)
		4. Harness quantum entanglement for interconnected processing
		5. Speed potential exponentially greater than classical computers.
	c. Quantum threats: 
		1. All modern-day encryption will be broken
		2. Shor's algorithm (quantum algorithm that finds prime factors of an integer)
		3. Grover's algorithm (quantum search algorithm that finds unique input to a black box function that produces a particular output)
		4. Harvest-now-decrypt-later (Store-not-decrypt-later)
		5. Consider this an Event Horizon from which the majority of humanity will never recover
	d. What is the Quantum Apocalypse?
		1. Quantum Computers (Quantum Entanglement, Qubits, error correction code)
		2. Our entire society uses traditional public-key encryption...
		3. What would happen if all of that was suddenly broken overnight?
	e. Modus Operandi of an adversary who achieved Quantum Enlightenment first?
		1. Burn it all down (fun but unlikely)
		2. Say nothing and decrypt whatever I want for years to come (boring but likely)			
5) PQC Overview
	a. INTERACTIVE DISCUSSION
	b. The development of algorithms that are thought to be secure against quantum computers
	c. PQC CNSA 2.0
		1. Symmetric: AES-256 in GCM mode
		2. Hash: SHA-384/512
		3. PQC Key Agreement: ML-KEM-1024 (FIPS 203)
		4. PQC Signatures: ML-DSA-87 (FIPS 204)
		5. Firmware/software signing: LMS/XMSS (NIST SP 800-208)
	d. Cryptographic Suite for Algebraic Lattices (CRYSTALS)
	e. Certifications
		1. NIST CAVP algorithms
		2. NIST CMVP 140-3 
	f. The bad news...
		1. Implementation difficulty
		2. Storage overheads (key, signature sizes)
		3. Performance overheads (keygen, keysig, keyver)
		4. Integration channels into existing apps
		5. Crypto agility and backwards compatibility (Lattice-based)
	g. HANDS-ON LESSON: Simple command-line interface app that parses switches
6) Base 16
	a. INTERACTIVE DISCUSSION
	b. Sometimes there's pre-code that we must create before we can start the real code
	c. We need a base16 class so that we can convert from octet-to-hex and hex-to-octet (optional)
	d. This will help us debug our code since we'll be able to print out any raw octet variables that we have, e.g. keys, signatures, etc.
	e. Let's create a C++ class that uses the new std::from_chars function (added in C++17) to convert raw octets into hexadecimal notation
	f. HANDS-ON LESSON: Create a program that converts raw octets passed into the cmd-line into hexadecimal format
7) Cryptographic Hash
	a. INTERACTIVE DISCUSSION
	b. We're going to implement the SHA512 hash using the OpenSSL EVP API
	c. SHA-512 is a one-way cryptographic hash function
	d. Used to verify 2 or more sets of data are the same (integrity checks of messages, files, packages)
	e. Let's create a C++ class that performs the SHA-512 hash operations of any length of data
	f. HANDS-ON LESSON: Create a program that performs a one-way SHA512 hash function on data passed in via the cmd-line
8) Ciphers
	a. INTERACTIVE DISCUSSION
	b. We're going to implement the AES cipher using the OpenSSL EVP API
	c. Ciphers are used to guarantee confidentiality in messages (encryption, decryption)
	d. Let's explore AES CBC and GCM modes, both using 256 bit keys
	e. AES-256 in CBC mode
		1. Initialization Vector (IV)
		2. Ciphertext padding
	f. AES-256 in GCM mode
		1. Initialization Vector (IV)
		2. Message Digest (TAG)
		3. Authenticated Encryption and Associated Data (AEAD)
	g. GCM mode is superior to CBC for a few reasons:
		1. Resulting ciphertext sizes are not limited to modulus 16 on GCM like they are on CBC (unless padding is disabled on CBC)
		2. GCM uses a tag to guarantee integrity of data, whereas CBC does not
	h. HANDS-ON LESSON: Create a program that encrypts and decrypts data passed in via the cmd-line
9) Break
10) Digital Signature Algorithm (DSA)
	a. INTERACTIVE DISCUSSION
	b. A private/public keypair that is used for signing and verifying messages
	c. Enforces authenticity and non-repudiation via known/trusted identities
	d. What are the different versions of ML-DSA?
		1. ML-DSA-44 (128-bit)
		2. ML-DSA-65 (192-bit)
		3. ML-DSA-87 (256-bit)
	e. One of the downsides of using PQC DSA is the massive sizes of all cryptographic primitives, including private/public keys and signatures
	f. HANDS-ON LESSON: Create a program that generates a ML-DSA-44 keypair, takes a message on the cmd-line, signs the message with the ML-DSA private key, and then verifies the message & signature with the ML-DSA public key 
11) Key Encapsulation Mechanism (KEM)
	a. INTERACTIVE DISCUSSION
	b. A KEM allows 2 parties to generate a the same secret key without having a MITM being able to also retrieve the secret key. A sender, who knows a public key of the other party, generates a short random secret key and an encapsulation/ciphertext of the secret key by the KEM's encapsulation algorithm. The receiver, who knows the private key corresponding to the public key used by the sender, is able to recover the same random secret key by using the KEM's decapsulation algorithm.
	c. The security goal of a KEM is to prevent anyone who does not know the private key from recovering any information about the encapsulated secret keys, even after eavesdropping or submitting other encapsulations to the receiver to study how the receiver reacts
	d. What are the different versions of ML-KEM?
		1. ML-KEM-512 (Level 1)
		2. ML-KEM-768 (Level 3)
		3. ML-KEM-1024 (Level 5)
	e. One of the downsides of using PQC KEM is the massive sizes of all cryptographic primitives, including private/public keys and ciphertexts (encapsulated secrets)
	f. HANDS-ON LESSON: Create a program that generates 2 ML-KEM-512 keypairs: one for the sender and another for the receiver. The sender will encpsulate a secret with the receivers public key, generating a ciphertext and shared key.  The sender will then forward the ciphertext to the receiver. The receiver will decap the ciphertext with the private key that matches the public key used by the sender, resulting in another shared key. Verify that the shared keys derived by both the sender and receiver are identical.
12) PQC Handshake
	a. INTERACTIVE DISCUSSION
	b. How would be design a protocol (request & response) for performing a PQC handshake for the purpose of shared key derivation?
	c. Which of the core security principles would be want to use for this protocol?
		1. Confidentiality
		2. Authenticity
		3. Integrity
		4. Non-repudiation
	d. We would need to use both ML-DSA and ML-KEM in the handshake, after which we could use AES-256 in GCM mode to secure message
	e. What are some of the components that we would want to include in the PQC handshake request?
		1. Datetime and/or sequence number to prevent replay attacks
		2. Sender's ML-DSA public key
		3. Sender's ML-KEM public key
		4. Sender's ML-DSA signature of all previous bytes
		5. What else?
	f. What are some of the components that we would want to include in the PQC handshake response?
		1. Datetime and/or sequence number to prevent replay attacks
		2. Receiver's ML-DSA public key
		3. Receiver's ML-KEM ciphertext (generated from  sender's ML-KEM public key)
		4. Receiver's ML-DSA signature of all previous bytes		
		5. What else?
	g. Let's combine all the PQC algorithms we've learned thus far into a single use-case
	h. HANDS-ON LESSON: Create a program that implements the PQC handshake request/response protocol for the purpose of shared key derivation
14) LMS/XMSS
	a. NOTE: This is an optional lesson if time permits
	b. What are LMS and XMSS?
	c. Why are there so many more requirements around firmware/software signing with LMS and XMSS? 
	d. What support does OpenSSL 4.0.0 have regarding both of these algorithms?
	e. HANDS-ON LESSON: Create a program that verifies an LMS message and signature contained within files
15) Summary
	a. What are the possible applications of this tech?
	b. Botnets, backdoors, or even the next great privacy app - the sky's the limit!
	c. Where do we go from here?
	d. Open source communities, online resources, books, etc.
	e. Thank you!
16) References
	a. Debian: https://www.debian.org/
	b. GCC: https://gcc.gnu.org/
	c. Boost: https://www.boost.org/
	d. CMake: https://cmake.org
	e. OpenSSL: https://openssl.org/
	f. NSA's CNSA Suite 2.0: https://media.defense.gov/2025/May/30/2003728741/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS.PDF
	g. Grover's algorithm: https://en.wikipedia.org/wiki/Grover%27s_algorithm
	h. Shor's algorithm: https://en.wikipedia.org/wiki/Shor%27s_algorithm
	i. DSA: https://en.wikipedia.org/wiki/Digital_Signature_Algorithm
	j. KEM: https://en.wikipedia.org/wiki/Key_encapsulation_mechanism
	k. AES: https://en.wikipedia.org/wiki/Advanced_Encryption_Standard
	l. SHA-2: https://en.wikipedia.org/wiki/SHA-2
```

### `DEF CON 34 - Workshops - Eric - Eijah - Anderson-Post - Quantum Cryptography (PQC) for Hackers - Student Resources/Student Email.txt`

```text

Shall We Play A Game,

Thank you for registering for my DEF CON 34 Workshop, "Post-Quantum Cryptography (PQC) for Hackers". I'm excited to spend the day with you on Sunday, August 9th from 9:00 AM – 1:00 PM. Please read the following email so that you are adequately prepared for the workshop.

Critical Prep: What to Do Before You Arrive 
• Visit the official workshop page for complete setup instructions, system requirements, and download links: https://www.codesiren.com/defcon34. The webpage will be live on (or before) Monday, August 3rd.
• Bring your laptop to the workshop.
• Install the latest version of Oracle VirtualBox on your laptop before the workshop. You can download VirtualBox for free here: https://www.virtualbox.org/wiki/Downloads
• Download the "Post-Quantum Cryptography (PQC) for Hackers" workshop files prior to the workshop. The workshop files (Linux Virtual Machine and PDF presentation) will be available for download at https://www.codesiren.com/defcon34 starting Monday, August 3rd.

What to Expect
• This is an intermediate workshop and requires that you have some prior experience programming on a Linux environment with GCC and CMake, and C/C++. Basic knowledge of cryptography, OpenSSL and a familiarly with the Linux operating system is also helpful.
• The course material will be available in both raw (tar.gz) and VM formats. All materials including files, prerequisites and instructions will be available to download before the workshop on my website: https://www.codesiren.com/defcon34. A laptop with a multi-core 64-bit processor (4+ cores recommended). 8 GB of RAM (minimum). At least 20 GB of free disk space. VirtualBox (latest version) installed and running. Administrator rights are required to install and run VirtualBox. The VM must be run within an x86_64 host.
• You will need to bring an x64 laptop with either a Windows 10/11, Debian-based Linux distribution (e.g. Debian), or a VM environment in which you can run an instance of x86_64 Debian (e.g. Virtual Box). For those who choose the VM route (the preferred approach), you will be able to download the workshop VM files prior to the start of the workshop at my website: https://www.codesiren.com/defcon34.
• Although this is an intermediate workshop, it’s also designed to be flexible to meet the needs of as many students as possible.
• You can progress through the material in a variety of ways:
    o You can take a passive approach with a focus on listening, learning, and understanding the course material.  
    o You can compile and run the lesson solutions as opposed to writing the code yourself.
    o You can code all solutions yourself
    o Or any combination thereof
• All the code (3rd parties, engine, examples) will be available for you to take home and modify after the workshop
• If you have any other questions, I can be contacted at mailto:eric@codesiren.com.


Hack the Planet,

Eijah
```

### `DEF CON 34 - Workshops - Eric - Eijah - Anderson-Post - Quantum Cryptography (PQC) for Hackers - Student Resources/Workshop Goals.txt`

```text
[ WORKSHOP GOALS ]
* Understand why PQC and CNSA 2.0 matter
* Implement all CNSA 2.0 algorithms using OpenSSL 4.0.0
* Discuss realistic threat scenarios (e.g., secure channel, code signing, hybrid TLS-like handshake) and how PQC algorithms help
* Leave the Workshop with working code knowledge, including the pro's/con's of the PQC algorithms (crypto agility, implementation complexity, large keys/signature sizes, performance overhead, and the novelty of Lattice-based algorithms)
```
