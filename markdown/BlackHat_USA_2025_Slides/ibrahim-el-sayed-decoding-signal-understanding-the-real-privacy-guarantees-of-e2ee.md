---
title: "Decoding Signal Understanding the Real Privacy Guarantees of E2EE"
speakers: ["Ibrahim El-sayed"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Ibrahim El-sayed_Decoding Signal Understanding the Real Privacy Guarantees of E2EE.pdf"
pages: 86
sha256: "8eec24ff6a597133c7bd883b86e1812c3a4a1d008ca6e6d7da4023f808a34cbd"
text_chars: 24451
ocr_pages: 39
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.9
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:13:47Z"
---
# Decoding Signal Understanding the Real Privacy Guarantees of E2EE

**Speakers:** Ibrahim El-sayed  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Ibrahim El-sayed_Decoding Signal Understanding the Real Privacy Guarantees of E2EE.pdf` (86 pages)


## Slide 1

### Decoding Signal: Understanding the Real Privacy Guarantees of E2EE

###### Ibrahim M. ElSayed

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat
: BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Decoding Signal: Understanding the
Real Privacy Guarantees of E2EE
Ibrahim M. ElSayed
```

## Slide 2

## Agenda

●Setting the scene ●Attack surface

●1:1 Messages

●Linked devices

●Conclusion

#BHUSA   @BlackHatEvents

## Slide 3

## $whoami

- ●Ibrahim M. ElSayed  (@the_st0rm) ●Security Engineer

   - Meta

   - Signal

   - Lacework

- ●Focus on Static Analysis

- ●Messaging application enthuthiast

   - Whatsapp - 2018

   - NSO attacks

#BHUSA   @BlackHatEvents

## Slide 4

## Disclaimer

●Opinions shared are my own, not my employer ●The focus is purely technical

●Any app comparisons made are focused only technologybased and do not reference specific products by name

#BHUSA   @BlackHatEvents

## Slide 5

## What to expect?

●A security review (I’m not a crypto expert) ●Close collaboration with the Signal team ●Focus on Signal 1:1 Messaging (no groups/calls) ●Takeaways: how signal works, privacy guarantees and vulnz (all fixed)

#BHUSA   @BlackHatEvents

## Slide 6

## Methodology

●Design: What the system is supposed to do ●Intent: What the engineer understood ●Implementation: The actual code that was written. ●Execution:How the code behaves in practice

#BHUSA   @BlackHatEvents

## Slide 7

#### Methodology - Vulnerability classes

●Language-specific: Memory corruption in C++ ●Application-specific: SQL injection

●Logic-based: Broken authorization ●Product-specific: Unique to the app’s domain e.g., leaking if 2 users are communicating

#BHUSA   @BlackHatEvents

## Slide 8

##### Understanding Signal’s Architecture

#BHUSA   @BlackHatEvents

## Slide 9

## Sending a mail

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Sending a mail
Sender
Mail company
Recipient
```

## Slide 10

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Name: Alice \
About lorem ipsum
Phone number: Otxxxxx
Alice
Name: Bob
About: lorem ipsum
Phone number: O9?xxxx
Bob
Directory
look up
(as) Message Process Services
sends——> —routes>
Processing
|
Alice
xf
Bob
1
1
1
1
'
1
1
1
'
1
1
1
1
```

## Slide 11

## Attack Surface

●Backend Services

- Mostly Java and Rust

●Clients

- Library Rust

- Android: Kotlin + Java

- iOS: Swift + ObjC

- Desktop: Electron App

#BHUSA   @BlackHatEvents

## Slide 12

## Attack Surface

●Backend Services

- Chat server: ~230K

- Storage Server: ~40K

●Clients

- Signal Library: ~100K LoC Rust

- Android: ~300K

- Desktop: ~300K

○ iOS: ~500K (~90% Swift)

#BHUSA   @BlackHatEvents

## Slide 13

## Attack Surface

- ●Expectation of E2EE applications

   - Server is malicious

   - Network is hostile

- ●Protecting

   - Message Content

   - Metadata

      - Profile

      - Messages

#BHUSA   @BlackHatEvents

## Slide 14

## Profile Data

#BHUSA   @BlackHatEvents

## Slide 15

## Profile Data

●Account identifiers

   - ACI: Account Identifier

   - PNI: Phone Number Identifier

- ●Profile data ○ Name, Avatar, Bio, Badges, Device caps, …

#BHUSA   @BlackHatEvents

## Slide 16

## Profile Data

●Stored in Storage Service (Java) ●Encrypted in AES-256-GCM ●Key generation: Clients ●Key sharing: every message after conversation is accepted ●Key rotation: Blocking a user

#BHUSA   @BlackHatEvents

## Slide 17

## Profile Data Storage

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
| ald8c8de.. E1Q9x/L50Gb8v6mZq3KcHg== XaB2+Of j TwXVOMIHVXIPZg== | aqn4Z2s3ZnlmbHNqa3g@0A==
| 91ad7c55.. ZT lwT2xheHh@eG12ZDIzYw== YT11LbnU4KkJxd@g9Q2Zpbk4= | NkJubGlyZUdGejN@Y1IN1Yw==
| 839201 i . "Living the dream ¢ | https://cdn. random. net/u1.png
| 283932 . "Coffee @& > Everything" | https://cdn.mockcdn.io/bob. jpg
+
```

## Slide 18

## Messages

#BHUSA   @BlackHatEvents

## Slide 19

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 40/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
' &> Message Process Services
Alice Bob
```

## Slide 20

## Diffie-Hellman

#BHUSA   @BlackHatEvents

## Slide 21

## Diffie-Hellman

#BHUSA   @BlackHatEvents

## Slide 22

## Diffie-Hellman

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 52/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Alice
common paint
Public transport
```

## Slide 23

## Diffie-Hellman

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Diffie-Hellman
Bob
common paint =
+
Secret Colors ES
+
Secret Colors SS
common secret
```

## Slide 24

## Diffie-Hellman

●EC-DH

●Pre-keys are signed by Identity keys

●Identity keys are the most critical keys for Signal account

#BHUSA   @BlackHatEvents

## Slide 25

How it works - Messages

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sends,
° E>] Message Process Services
To: Bob P €ss! "Y
```

## Slide 26

## Backward Secrecy

●Compromised device shouldn’t compromise previous conversations

#BHUSA   @BlackHatEvents

## Slide 27

## Backward Secrecy

●Compromised device shouldn’t compromise previous conversations

●Design: Every message is encrypted with a unique key ●Symmetric key ratchet

#BHUSA   @BlackHatEvents

## Slide 28

## Backward Secrecy

●Chain key from DH agreement ●Message key for encryption ●Chain key to derive next message Key ●Intermediate chain-keys are deleted

#BHUSA   @BlackHatEvents

## Slide 29

## Backward Secrecy

●Chain key from DH agreement ●Message key for encryption ●Chain key to derive next message Key ●Intermediate chain-keys are deleted

#BHUSA   @BlackHatEvents

## Slide 30

## Future Secrecy

●Compromised key shouldn’t compromise future conversations

#BHUSA   @BlackHatEvents

## Slide 31

## Future Secrecy

●Compromised key shouldn’t compromise future conversations

●Design: Assume the secret channel is compromised. Establish Secret keys on an unsafe channel

●Diffie-Hellman Ratchet

#BHUSA   @BlackHatEvents

## Slide 32

## Diffie-Hellman ratchet

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Diffie-Hellman ratchet
Alice Bob
t
Private key Public key
```

## Slide 33

Diffie-Hellman ratchet
X

X

#BHUSA   @BlackHatEvents

## Slide 34

#BHUSA   @BlackHatEvents

## Slide 35

#### Unidentified Sender (UD Sender)

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Unidentified Sender (UD Sender)
To: Bob
From: Alice To: Bob To: Bob
```

## Slide 36

## Technology check

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Technology check
Encrypted Profile @ x x x x
Encrypted Messages LV Co al LV iv iV
Single ratchet © @ iV | iv | iv
double ratchet @ x x @ x
Sealed Sender @ x x x x
```

## Slide 37

# Implementation

#BHUSA   @BlackHatEvents

## Slide 38

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
message Envelope {
optional
reserved
optional
optional
optional
reserved
optional
reserved
optional
optional
optional
optional
optional
optional
Type type
/*sourceE164*/
string sourceServiceld
uint32 sourceDevice
string destinationServiceld =
/*relay*/
uint64 timestamp
bytes content
string serverGuid
uint64 serverTimestamp
bool urgent
bool story
bytes reportingToken
Contains encrypted Content
```

## Slide 39

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ message Envelope {
enum Type {
UNKNOWN
CIPHERTEXT
RECEIPT =
UNIDENTIFIED_SENDER =
reserved 7;
1
2
3
4
5
6
7
8
i)
```

## Slide 40

Plaintext Envelopes Design

<u>https://signal.org/docs/specifications/sesame/</u>

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Plaintext Envelopes
Design
When the recipient device receives anjundecryptable message] the recipient
device sends an|junencrypted retry request|message to the original sending
device's mailbox, containing the undecryptable message's MessagelD.
When the original sending device fetches a retry request along with the relevant
UserID and DevicelD of the device that sent the retry request, the original sending
device executes the following resending process:
```

## Slide 41

## Plaintext Envelopes Implementation

#BHUSA   @BlackHatEvents

## Slide 42

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
validatedEnvelope: ValidatedIncomingEnvelope,
cipherType: CiphertextMessage.Messagelype,
tx transaction: SDSAnyWriteTransaction
) throws -> DecryptedIncomingEnvelope {
1
2
4
5
7
let plaintext: [UInt8]
switch cipherType {
case .whisper:
case .preKey:
case .senderKey:
case .plaintext:
```

## Slide 43

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
func decryptIdentifiedEnvelope(
validatedEnvelope: ValidatedIncomingEnvelope,
cipherType: CiphertextMessage 9
localIdentifiers: LocalIdentifiers,
tx transaction: SDSAnyWriteTransaction
) throws -> DecryptedIncomingEnvelope {
let plaintext: [
switch cipherType {
case g
let message = try SignalMessage(bytes: encryptedData)
plaintext = try signalDecrypt(
message: message,
from: protocolAddress,
sessionStore: signalProtocolStore
identityStore: identityManager
localIdentity, tx: transaction No
context: transaction
)
sendReactiveProfileKeyIfNecessary(to: sourceAci, tx:
```

## Slide 44

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
validatedEnvelope: ValidatedIncomingEnvelope,
cipherType: CiphertextMessage.MessageType,
tx transaction: SDSAnyWriteTransaction
) throws -> DecryptedIncomingEnvelope {
let plaintext: [UInt8]
switch cipherType {
case .whisper:
case .preKey:
case .senderKey:
case .plaintext:
let plaintextMessage = try PlaintextContent(bytes: encryptedData
plaintext = plaintextMessage. body
1
2
3}
4
5
6
7
(0)
Ne
1
1
1
1
1
1
1
```

## Slide 45

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 message Content {
1
2
3
4
5
6
7
8
optional
optional
optional
optional
optional
optional
optional
DataMessage
SyncMessage
CallMessage
NullMessage
ReceiptMessage
TypingMessage
bytes
dataMessage
syncMessage
callMessage
nullMessage
receiptMessage
typingMessage =
senderKeyDistributionMessage =
optional
bytes
decryptionErrorMessage
optional
optional
optional
StoryMessage
PniSignatureMessage
EditMessage
storyMessage
pniSignatureMessage
editMessage
```

## Slide 46

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
func handleRequest(
request: MessageReceiverRequest,
context: DeliveryReceiptContext,
localIdentifiers: LocalIdentifiers,
tx: SDSAnyWriteTransaction
let protoContent = request
switch request {
case (let syncMessage):
case (let dataMessage):
case (let callMessage):
case (let typingMessage):
case 5
case (let receiptMessage):
case (let decryptionErrorMessage):
case (let storyMessage):
case (let editMessage):
case 8
case
("Ignoring envelope with unknown type.")
```

## Slide 47

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
func handleRequest(
request: MessageReceiverRequest,
context: DeliveryReceiptContext,
localIdentifiers: LocalIdentifiers,
tx: SDSAnyWriteTransaction
let protoContent = request
switch request {
case (let syncMessage):
case (let dataMessage):
handleIncomingEnvelope( request: request, dataMessage:
dataMessage, localIdentifiers: localIdentifiers, tx: tx)
case (let callMessage):
case (let typingMessage):
case 8
case (let receiptMessage):
case (let decryptionErrorMessage):
case (let storyMessage):
case (let editMessage):
case 8
case
Logger ("Ignoring envelope with unknown type.")
```

## Slide 48

#### Plain-Text envelope vulnerability

●iOS Clients process plain-text envelopes ○ ex: DataMessage, Edit Message ●Requires a malicious server

#BHUSA   @BlackHatEvents

## Slide 49

## Impact

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Impact
plain-text envelope with
any content
a) Message Process Services
=)
@
Bob
```

## Slide 50

<u>https://github.com/signalapp/Signal-iOS/commit/6bdf97ae88a72e2c7e843d7e4937647fcfbbf339#diff-79ca5c51f765f3b6fc3d184a8fb115d7b21bbbdbb1a5eec225cd33d914fd2f5d</u>

#BHUSA   @BlackHatEvents

## Slide 51

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 private Plaintext decryptInternal(
Envelope envelope,
long serverDeliveredTimestamp) {
if (envelope.type == Envelope. Type.PREKEY_BUNDLE) {
} else if (envelope.type == Envelope.Type.CIPHERTEXT) {
} else if (envelope.type Envelope. Type.PLAINTEXT_CONTENT) {
} else if (envelope.type Envelope. Type.UNIDENTIFIED_SENDER) {
} else {
throw new InvalidMetadataMessageException( "Unknown type: " +
envelope.type);
9 }
1
2
3}
4
5
6
7
8
```

## Slide 52

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private Plaintext decryptInternal(Envelope envelope, long serverDeliveredTimestamp) {
if (envelope.type == Envelope.Type.PREKEY BUNDLE) {
} else if (envelope.type == Envelope.Type.CIPHERTEXT) {
SignalProtocolAddress sourceAddress = new SignalProtocolAddress
envelope.sourceServiceld,
SignalSessionCipher sessionCipher = new SignalSessionCipher(
sessionLock,
new SessionCipher(signalProtocolStore,
sourceAddress) );
metadata = new SignalServiceMetadata
getSourceAddress(envelope),
envelope.sourceDevice,
envelope. serverTimestamp
serverDeliveredTimestamp,
Optional.empty(),
envelope.destinationServiceld);
} else if (envelope.type == Envelope. Type.PLAINTEXT_CONTENT) {
} else if (envelope.type == Envelope. Type.UNIDENTIFIED_SENDER) {
} else {
throw new InvalidMetadataMessageException("Unknown type:
}
+ envelope.type);
```

## Slide 53

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 private Plaintext decryptInternal(Envelope envelope, long serverDeliveredTimestamp) {
1 if (envelope.type == Envelope.Type.PREKEY_BUNDLE) {
3 |} else if (envelope.type == Envelope. Type.PLAINTEXT_CONTENT) {
4 paddedMessage = new PlaintextContent(envelope. content. toByteArray()).getBody( );
5 metadata = new SignalServiceMetadata(
getSourceAddress(envelope),
envelope.timestamp,
envelope.serverTimestamp,
serverDeliveredTimestamp,
6
7
Q
8
oo
envelope.serverGuid,
Optional.empty(),
} else {
throw new InvalidMetadataMessageException( "Unknown type: " + envelope.type);
}
NO
```

## Slide 54

DataMessage Check is missing!

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private fun createPlaintextResultIfInvalid(content: Content): Result? {
val errors: MutableList<String> = mutableListOf( )
if (content.decryptionErrorMessage == ){
errors += "Missing DecryptionErrorMessage"
if (content.storyMessage != ){
errors += "Unexpected StoryMessage"
}
if (content.senderKeyDistributionMessage != ){
errors += "Unexpected SenderKeyDistributionMessage"
}
if (content.editMessage != ){
errors += "Unexpected EditMessage"
}
return if (errors.isNotEmpty()) {
} else {
}
```

## Slide 55

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private fun handleMessage(
senderRecipient: Recipient,
envelope: Envelope,
content: Content,
metadata: EnvelopeMetadata,
serverDeliveredTimestamp: Long,
processingEarlyContent: Boolean,
localMetric: SignalLocalMetrics.MessageReceive?
when {
content.dataMessage != -> {
content.syncMessage != —> {
content.callMessage != -> {
content.receiptMessage !=
content.typingMessage !=
content.storyMessage != -> {
content.decryptionErrorMessage != -> {
content.editMessage != —-> {... }
content.senderKeyDistributionMessage !=
|| content.pniSignatureMessage != -> {
else -> {
warn(envelope.timestamp!!, "Got unrecognized message!")
```

## Slide 56

#### Plain-Text envelope vulnerability

●Android Clients process plain-text envelopes with DataMessage

●Required a malicious server

#BHUSA   @BlackHatEvents

## Slide 57

#BHUSA   @BlackHatEvents

<u>https://github.com/signalapp/Signal-Android/commit/8d8c21f2286d2449aaaf63669ea6e06e47ec076a</u>


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private fun validatePlaintextContent(content: Content): Result?
{
val errors:
if (content
errors +=
if (content
errors +=
if (content.
errors +=
}
if (content.
errors +=
}
.decryptionErrorMessage ==
.dataMessage !=
"Unexpected
MutableList<String> = mutableListOf( )
"Missing DecryptionErrorMessage"
){
DataMessage"
SyncMessage"
syncMessage !=
"Unexpected
CallMessage"
callMessage !=
"Unexpected
```

## Slide 58

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private async innerDecrypt(
stores: LockedStores,
envelope: UnsealedEnvelope,
ciphertext: Uint8Array,
servicelIdKind: ServiceIdKind
): Promise<InnerDecryptResultType | undefined> {
const { sourceDevice } = envelope;
const { destinationServiceId } = envelope;
const address = new QualifiedAddress(
destinationServiceld,
if (
serviceIdKind === ServiceIdKind.PNI &
envelope.type !== envelopeTypeEnum.PREKEY_BUNDLE
if (envelope.type envelopeTypeEnum.PLAINTEXT_CONTENT) {
if (envelope. type envelopeTypeEnum.CIPHERTEXT) { ... }
if (envelope.type envelopeTypeEnum.PREKEY_BUNDLE) { ... }
if (envelope.type envelopeTypeEnum.UNIDENTIFIED_SENDER) {
throw new Error( ‘Unknown message type’);
```

## Slide 59

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
if (
servicelIdKind === ServiceIdKind.PNI &&
envelope.type !== envelopeTypeEnum. PREKEY_BUNDLE
if (envelope.type === envelopeTypeEnum.PLAINTEXT_CONTENT) {
log. info( decrypt/${logId}: plaintext message );
const buffer = Buffer.from(ciphertext );
const plaintextContent = PlaintextContent.deserialize( buffer);
return {
plaintext: this.unpad(plaintextContent.body()),
wasEncrypted: ;
if (envelope.type === envelopelTypeEnum.CIPHERTEXT) { ... }
if (envelope.type === envelopeTypeEnum.PREKEY_BUNDLE) { ... }
if (envelope.type === envelopeTypeEnum.UNIDENTIFIED_SENDER) {
throw new Error('Unknown message type' );
```

## Slide 60

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private async decryptEnvelope(
stores: LockedStores,
envelope: UnsealedEnvelope,
serviceIdKind: ServiceIdKind
): Promise<DecryptResult> {
const content = Proto.Content.decode(plaintext);
if (!wasEncrypted && Bytes.isEmpty(content.decryptionErrorMessage)) {
${logId}: dropping plaintext envelope without decryption error message
const { sourceServiceId: senderAci } = envelope;
strictAssert(isAciString(senderAci), ‘Sender uuid must be an ACI');
const event = new InvalidPlaintextEvent({
senderDevice: envelope.sourceDevice ?? 1,
senderAci,
timestamp: envelope.timestamp,
return { plaintext: undefined, envelope };
return { plaintext, envelope };
}
```

## Slide 61

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
private async innerHandleContentMessage(
incomingEnvelope: UnsealedEnvelope,
plaintext: Uint8Array
): Promise<void> {
const content = Proto.Content.decode(plaintext);
const envelope = await this.maybeUpdateTimestamp( incomingEnvelope) ;
if (
content.decryptionErrorMessage &
Bytes.isNotEmpty(content.decryptionErrorMessage)
if (content.syncMessage) { ... }
if (content.dataMessage) { ... }
if (content.nullMessage) { ... }
if (content.callingMessage) { ... }
if (content.receiptMessage) { ... }
if (content.typingMessage) { ... }
if (content.storyMessage) { ... }
if (content.editMessage) { ... }
if (Bytes.isEmpty(content.senderKeyDistributionMessage)) {
throw new Error('Unsupported content message' );
}
}
```

## Slide 62

## Recap of the vulnerabilities

●Signal allows plain-text messages only for specific error reporting cases

●However, **some clients failed to enforce this, accepting actual text messages** via this fallback path ●This opened the door for a malicious server to inject messages (relevant to SIM swap scenarios too)

#BHUSA   @BlackHatEvents

## Slide 63

#### Linked Device

<u>https://signal.org/blog/a-synchronized-start-for-linked-devices/</u>

#BHUSA   @BlackHatEvents

## Slide 64

#BHUSA   @BlackHatEvents

<u>https://signal.org/blog/a-synchronized-start-for-linked-devices/</u>

## Slide 65

#BHUSA   @BlackHatEvents

<u>https://signal.org/blog/a-synchronized-start-for-linked-devices/</u>

## Slide 66

#BHUSA   @BlackHatEvents

## Slide 67

Linked Device - Synchronization

●E2EE between the 2 devices using Signal Protocol

●Same path as 1:1 message ●Protobuf Sync Messages

#BHUSA   @BlackHatEvents

## Slide 68

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 message Content {
optional
DataMessage
dataMessage
optional
SyncMessage
syncMessage
1
2
3
4
5
6
7
8
optional
optional
optional
optional
optional
optional
optional
optional
optional
CallMessage
NullMessage
ReceiptMessage
TypingMessage
bytes
bytes
StoryMessage
PniSignatureMessage
EditMessage
callMessage
nullMessage
receiptMessage
typingMessage =
senderKeyDistributionMessage =
decryptionErrorMessage
storyMessage
pniSignatureMessage
editMessage
```

## Slide 69

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
message SyncMessage {
optional Sent sent
optional Contacts contacts
reserved /* groups */ 3;
optional Request request
repeated Read read
optional Blocked blocked
optional Verified verified
optional Configuration configuration
optional bytes padding
repeated StickerPackOperation stickerPackOperation
optional FetchLatest fetchLatest
optional Keys keys
optional MessageRequestResponse messageRequestResponse
reserved
repeated Viewed viewed
reserved
optional PniChangeNumber pniChangeNumber
optional CallEvent callEvent
optional CallLinkUpdate callLinkUpdate
optional CallLogEvent callLogEvent
optional DeleteForMe deleteForMe
```

## Slide 70

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 message SyncMessage {
1 [optional Sent sent
2 optional Contacts contacts
3. reserved /* groups */ 3;
3
4 optional DataMessage message a geRequestResponse messageRequestResponse
read
eco blocked
verified
configuration
© message Sent { padding
1 optional string destination =1; erPackOperation stickerPackOperation
2 optional string destinationServiceld =7; Pitecelpsir WAUSHLaTNTEeYSIN
3 optional uint64 timestamp = 2; pore
5 optional uint64 expirationStartTimestamp = 4;
6 repeated UnidentifiedDeliveryStatus unidentifiedStatus Ss 59 g Weta
7 optional bool isRecipientUpdate = angeNumber pniChangeNumber
8 optional StoryMessage storyMessage = 8; vent callEvent
repeated StoryMessageRecipient storyMessageRecipients = 9; inkUpdate callLinkUpdate
optional EditMessage editMessage = 10; a cat ooeven
```

## Slide 71

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 message Read {
optional string sender =
optional string senderAci
optional uint64 timestamp
we
we
1
0 message SyncMessage {
optional
optional
reserved
optional
repeated
optional
optional
optional
optional
repeated
optional
optional
optional
optional
reserved
repeated
reserved
optional
optional
optional
optional
optional
Sent
Contacts
/* groups */ 3;
Request
Read
Blocked
Verified
Configuration
bytes
StickerPackOperation
FetchLatest
Keys
MessageRequestResponse
Viewed
PniChangeNumber
CallEvent
CallLinkUpdate
CallLogEvent
DeleteForMe
sent
contacts
request
read
blocked
verified
configuration
padding
stickerPackOperation
viewOnceOpen
fetchLatest
keys
messageRequestResponse
viewed
pniChangeNumber
callEvent
callLinkUpdate
callLogEvent
deleteForMe
```

## Slide 72

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
message Configuration {
optional bool readReceipts =1;
optional bool unidentifiedDeliveryIndicators = 2;
optional bool typingIndicators = 3;
reserved /* LinkPreviews */ 3
optional uint32 provisioningVersion =5;
optional bool LinkPreviews = 6;
message SyncMessage {
optional
optional
reserved
optional
repeated
optional
optional
optional
optional
repeated
optional
optional
optional
optional
reserved
repeated
reserved
optional
optional
optional
optional
optional
Sent
Contacts
/* groups */ 3;
Request
Read
Blocked
Verified
Configuration
bytes
StickerPackOperation
ViewOnceOpen
FetchLatest
Keys
MessageRequestResponse
Viewed
PniChangeNumber
CallEvent
CallLinkUpdate
CallLogEvent
DeleteForMe
sent
contacts
request
read
blocked
verified
configuration
padding
stickerPackOperation
viewOnceOpen
fetchLatest
keys
messageRequestResponse
viewed
pniChangeNumber
callEvent
callLinkUpdate
callLogEvent
deleteForMe
```

## Slide 73

## Processing SyncMessages

●Decrypt using Signal protocol ●Validate sender is self

●Process

#BHUSA   @BlackHatEvents

## Slide 74

<u>https://github.com/signalapp/Signal-iOS/blob/4f272777f6e7c1de0f9f025b23e789fac99036e2/SignalServiceKit/Messages/MessageReceiver.swift#L366</u> #BHUSA   @BlackHatEvents

## Slide 75

<u>https://github.com/signalapp/Signal-Desktop/blob/2a55bfbef93f75f8b40f32a002e06827b15ffe91/ts/textsecure/MessageReceiver.ts#L3041</u>

#BHUSA   @BlackHatEvents

## Slide 76

#BHUSA   @BlackHatEvents

<u>https://github.com/signalapp/Signal-Android/blob/d84612ebf41a2f9c45f54217219db21960605c98/libsignal-service/src/main/java/org/whispersystems/signalservice/api/</u>

<u>messages/EnvelopeContentValidator.kt#L148</u>

## Slide 77

## Forging SyncMessages

- ●Missing sender validation on SyncMessages

- ●Android-only vulnerability

- ●Impact

   - Attackers can send Sync messages to Android clients (0click)

   - Actions possible: send, delete, mark as read, update settings

- ●Reading message content was **not** possible

- ●Patched immediately, fixed in September 2024

#BHUSA   @BlackHatEvents

## Slide 78

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Envelope with SyncMessage
&> Message Process Services
Processing
Mallory
```

## Slide 79

## Demo

#BHUSA   @BlackHatEvents

## Slide 80

#BHUSA   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
message SyncMessage {
optional Sent sent
optional Contacts contacts
reserved /* groups */ 3;
optional Request request
repeated Read read
optional Blocked blocked
optional Verified verified
optional Configuration configuration
optional bytes padding
repeated StickerPackOperation stickerPackOperation
optional FetchLatest fetchLatest
optional Keys keys
optional MessageRequestResponse messageRequestResponse
reserved
repeated Viewed viewed
reserved
optional PniChangeNumber pniChangeNumber
optional CallEvent callEvent
optional CallLinkUpdate callLinkUpdate
optional CallLogEvent callLogEvent
optional DeleteForMe deleteForMe
```

## Slide 81

#BHUSA   @BlackHatEvents

Fix commit: <u>https://github.com/signalapp/Signal-Android/commit/ac10ff4cbe1312ce4932337278d3c4a2c69954cc</u>


> Recovered by OCR — confidence 89/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
0 private fun validateSyncMessage(envelope: Envelope, syncMessage: SyncMessage, localAci:
if (sourceServicelId != localAci) {
return Result.Invalid("[SyncMessage] Source was not our own account!")
}
if (syncMessage.read.any { it.senderAci.isNullOrInvalidAci() }) {
Fix commit:
```

## Slide 82

## Vulnerability Recap

●When you have a linked devices, your devices synchronize the state via an invisible E2EE “conversation” between them

●This conversation use special message type “SyncMessages”

●The vulnerability was that Android clients accepted SyncMessages not just from linked devices but **from anyone** (even if you had no linked devices)

#BHUSA   @BlackHatEvents

## Slide 83

## Forging SyncMessages

● <u>CVE-2025-24903: Whisperfish an unofficial signal clients</u> on top of Signal library ●CVSS score: 8.5

#BHUSA   @BlackHatEvents

## Slide 84

## What Else Did I Review?

●Language specific

●Application-specific

●Logic-based

●Product-specific

#BHUSA   @BlackHatEvents

## Slide 85

## Wrapping up

●A security engineer review on Signal ●Close collaboration with the Signal team ●Takeaways:

- How signal works?

- ○ Privacy guarantees

- ○ Vulnz (all fixed)

#BHUSA   @BlackHatEvents

## Slide 86

## Big thanks to the team

●Jim O’Leary (Signal VP of engineering) ●Ehren Kret (Signal CTO) ●Signal engineering and comms teams ●Otto Ebeling

●Edoardo Nava

#BHUSA   @BlackHatEvents
