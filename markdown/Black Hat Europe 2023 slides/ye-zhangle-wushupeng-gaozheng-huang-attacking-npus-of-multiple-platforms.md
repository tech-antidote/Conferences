---
title: "Attacking NPUs of Multiple Platforms"
speakers: ["Ye Zhang", "Le Wu", "Shupeng Gao", "Zheng Huang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Ye Zhang,Le Wu,Shupeng Gao,Zheng Huang_Attacking NPUs of Multiple Platforms.pdf"
pages: 113
sha256: "e11b9e28a48ae1ae4017eb5b70a69c4555f829d8bd717afaccd2d3f120ca9dc1"
text_chars: 52511
ocr_pages: 14
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:13:54Z"
---
# Attacking NPUs of Multiple Platforms

**Speakers:** Ye Zhang, Le Wu, Shupeng Gao, Zheng Huang  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Ye Zhang,Le Wu,Shupeng Gao,Zheng Huang_Attacking NPUs of Multiple Platforms.pdf` (113 pages)


## Slide 1

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
DECEMBER 4-7
EXCEL LONDON / UK
#BHEU
@BlackHatEvents
```

## Slide 2

### Attacking NPUs of Multiple Platforms

Baidu Security Lab X-Team Ye Zhang,  Le Wu,  Shupeng Gao,  Zheng Huang

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piiek hat
Attacking NPUs of Multiple
Platforms
Baidu Security Lab X-Team
Ye Zhang, Le Wu, Shupeng Gao, Zheng Huang
#BHEU @BlackHatEvents
```

## Slide 3

###### About US

###### Security Researchers from Baidu Security Lab X-Team

- Ye Zhang (@VAR10CK)

- Le Wu (@NVamous)

- Shupeng Gao

- Zheng Huang

#BHEU @BlackHatEvents

Information Classification: General

## Slide 4

##### Agenda

• Background & Basics • Samsung Exynos NPU • Apple Neural Engine • Qualcomm Snapdragon NPU • Conclusion & Future work

#BHEU @BlackHatEvents

Information Classification: General

## Slide 5

# Why NPU?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 6

###### Why NPU?

###### Neural Network

- Image classification

- • Self driving

- • Face recognition

- • Language processing

   - …

#BHEU @BlackHatEvents

Information Classification: General

## Slide 7

###### Why NPU?

Basic of CNN(Convolution Neural Network)

###### What an image looks like from Computer’s view ?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 8

###### Why NPU?

Basic of CNN(Convolution Neural Network)

equals?

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
5
=
Cg
O
e
COleS
AD
—
URAO
?
Why NPU
Basic of CNN(Convolution Neural Network)
(2
(Ss
oO
oO
oO
(S)
oO
(S
oO
0/0;0/;0}/0}0;0;0/;0
0;0;0/0}0/0|;0/0]0
0;0;0/0}0/0|;0/0]0
al
Information Classification: Gener:
```

## Slide 9

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
EUROPE @O25
Why NPU?
Basic of CNN(Convolution Neural Network)
cat face
cat paw
cat tail
=> it's a cat
Information Classification: General
```

## Slide 10

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
Why NPU?
Basic of CNN(Convolution Neural Network)
black hat
Information Classification: General
filter
Lo] of.
0 ij o
ojo Ry
~
wy \ s
WS 0/o}o]o]o]}0 0|0
‘\ °s. fo MiRoTololo 0
‘\ “So }o 0100 0] 0
‘ |) 0] 0 0 0/0
‘\ |0}0]0] 0, 0 0/0
‘\Jololo 0 o|0
‘olo ololo 0}0
OO} 0}0]0 0
o}o;olo}olo 0}0
input image
weight_1 = 1*1 + O*0 + O*0 + O*0 + 1*1 + O*0 + 0*0 + 0*0 + 1*1
weight_2
1*0 + O*O + O*1 + O*O + 1*1 + O*O + O*1 + O*O + 1*0
```

## Slide 11

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Why NPU?
Basic of CNN(Convolution Neural Network)
filter
0/;0]
weight *1*O + O*O + 0*0 + O*0 + O*1 + 1*1 + O*0 + O*0 + 1*1 = 2
0 0
0 0
10 0 2
0 0 ?|?
0 0 —) ? ?
0 0
0 0 2)? )2?)...)?
0 0 output featrue map
0 0
input featrue map
Information Classification: General
```

## Slide 12

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blckhat
Why NPU?
Basic of CNN(Convolution Neural Network)
filter
0/0}
0 .,
lo weight = T*Q + O*O + 0*0 + O*1 + 1*0 + 0*0 + 0*0 + O*1 + 1*0 = 0
. 0 0
0 0
~ ~O 0 2 0
0 0 ?|?
0 0 =) ? 2
0 0
0 0 2)? )2?)...)?
0 0 output featrue map
0 0
input featrue map
Information Classification: General
```

## Slide 13

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blckhat
Why NPU?
Basic of CNN(Convolution Neural Network)
Information Classification: General
filter
0 ss
weight = 1*O-«_0*0 + 0*0 + 0*0 + 1*0 + 0*0 + O*1 + 0*0 + 1*0 = 0
2|}0]0 ?
2?/2?|? ?
2121? ?
2)? )2?)...)?
COLO lSOlOyoloe};eo4yo}Se
’
O;JO;O;O;}O}O};O};O0;}O
input featrue map
output featrue map
```

## Slide 14

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Why NPU?
Basic of CNN(Convolution Neural Network)
filter 1 filter 2
ter 0 |
Lo] 0 S. i)
0 0 i 0 | Input Bias
single neuron model
o|olololojo|o
ci Ad
LY IVIVIVITVITVIYVY
oo Qty 4
\ Wk,
. ~ channels T2
0 04> Activation
0 0 0 Output
0 ° : y+ pl...) —> yz
filter 3 0 Sum
o[o] oto HS Win
0 0 Em
0 0 ; 0 Z
0 0
0 0
me
0
input feature map
Information Classification: General
```

## Slide 15

###### Why NPU?

###### Basic of CNN(Convolution Neural Network)

CONV layer:

convolution operations, input data + filter -> output

Pooling layer:

Downsample the spatial dimensions of the input volume

###### Activation layer:

non-linearity, learn complex relationships and patterns in the data

###### Fully connected layer:

connect every neuron in one layer to every neuron in the next layer

#BHEU @BlackHatEvents

Information Classification: General

## Slide 16

###### Model File

###### Training VS Prediction/Inference

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Model File
Training VS Prediction/Inference
—— ee i i a
ee
aes eee ae ee =
eee eee
/
Information Classification: General
```

## Slide 17

###### Hardware Design

###### Main problem to solve

large amounts of calculation for AI algorithm. Most of computing can be parallelized (matrix-vector multiplication).

CPU:

Fast in data processing; High frequency; Branch Prediction, etc.

Not good on parallel computing.

GPU:

Good at parallel computing; framework support(e.g. CUDA).

High power consumption; Not designed specifically for machine learning.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 18

###### Hardware Design

###### AI processors

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Hardware Design
Al processors
a-----------K~
7 N
(a a I Cambricon pee eee .
Baa  _ +6 ‘
I . I I i]
; BEYOND FAST ' i DEEPHi ;
! im = Bt
intel = '
I I I l I
' IRIS. i | rt AMDi¢1
| Ea 1 | , rt XILINX !
I ' I Ooms 1 I 1
I ! : . l I I
! RADEON Tensor Processing Unit ! A = D A ;
I I I I I
| t 4 FPGA ;
oe GPU / I I Swe eee ee eee 2
alain - ; ASIC ;
(Application-specific integrated circuit)
N 7
Information Classification: General
```

## Slide 19

###### Hardware Design

###### Cambricon DianNao chipset

- SRAM & DMA

NBin is for input neurons. NBout is for output neurons SB is for NN’s weight param. through DMA.

- CP & NFUs

NFU-1 is for multiplication, 16*16 multipliers. NFU-2 is for addition tree. NFU-3 is for activation. Control Processer

- Instruction Set Called DianNaoYu.

- SIMD.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 20

###### Hardware Design

###### Prediction module on edge devices

- Only for prediction and inference, not for training.

- Need pre-trained model file (for mobile).

- • Low power consumption, low latency, accuracy, enough TOPS …

- Vendor specific, different design.

We will mainly focus on these chips in this talk.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 21

###### Attack Surface

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blckhat
Attack Surface
[ Raw Input |
Y
Apps/Framework e{ Model file |
User Space Runtime Lib ]
kernel NPU Driver |
NPU | NPU Firmware }
Processor Hardware
Information Classification: General
```

## Slide 22

## Samsung Exynos NPU

#BHEU @BlackHatEvents

Information Classification: General

## Slide 23

###### Samsung Exynos NPU

###### Hardware Overview

###### Control processor + NPU Cores

Exynos 9820

#BHEU @BlackHatEvents

Information Classification: General

## Slide 24

###### Samsung Exynos NPU

###### Hardware Overview

###### Control processor + NPU Cores

###### **32bit ARM core, running firmware, communicate with kernel, control NPU cores**

Exynos 9820

#BHEU @BlackHatEvents

Information Classification: General

## Slide 25

###### Samsung Exynos NPU Driver

###### NPU device

- Device

- Selinux (Galaxy A series)

- ENN (Exynos Neural Network) framework

#BHEU @BlackHatEvents

Information Classification: General

## Slide 26

###### Samsung Exynos NPU Driver

###### Device probing

###### • Consistent DMA mapping **npu_device_probe -> npu_system_probe -> npu_system_soc_probe -> npu_init_iomem_area -> npu_memory_alloc_from_heap**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 27

###### Samsung Exynos NPU Driver

###### Device probing

• Consistent DMA mapping

**npu_device_probe -> npu_system_probe -> npu_system_soc_probe -> npu_init_iomem_area -> npu_memory_alloc_from_heap**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 28

###### Samsung Exynos NPU Driver

###### Address mapping

||||•IOMEM Sace|
|---|---|---|---|
|**IOMEM name**|**IOMEM addr / IOVA**|**Size**|p|
|**SFR_DNC**|**0x16200000**|**0x200000**||
|**SFR_NPUC0**|**0x16500000**|**0x100000**||
|**TCUSRAM**|**0x16700000**|**0x20000**||
|**SFR_NPU0**|**0x10a00000**|**0x100000**||
|**SFR_NPU1**|**0x10b00000**|**0x100000**||
|**MAILBOX0**|**0x165c0000**|**0x10000**||
|**IDPSRAM**|**0x16100000**|**0x100000**||
|**FW_DRAM**|**0x50000000**|**0xe0000**||
|**FW_UNITTEST**|**0x50100000**|**0x200000**||
|**FW_LOG**|**0x50300000**|**0x200000**||

Exynos 9630

#BHEU @BlackHatEvents

Information Classification: General

## Slide 29

###### Samsung Exynos NPU Driver

###### Address mapping

|**IOMEM name**|**IOMEM addr / IOVA**|**Size**|•
FW_DRAM
|
|---|---|---|---|
|**SFR_DNC**|**0x16200000**|**0x200000**|Firmware binary
Mailbox Ring buffer|
|**SFR_NPUC0**|**0x16500000**|**0x100000**||
|**TCUSRAM**|**0x16700000**|**0x20000**|• FW_UNITTEST|
|**SFR_NPU0**|**0x10a00000**|**0x100000**||
|**SFR_NPU1**|**0x10b00000**|**0x100000**|• FW_LOG|
|**MAILBOX0**|**0x165c0000**|**0x10000**|•Other DMA sac|
|**IDPSRAM**|**0x16100000**|**0x100000**|p|
|**FW_DRAM**|**0x50000000**|**0xe0000**||
|**FW_UNITTEST**|**0x50100000**|**0x200000**||
|**FW_LOG**|**0x50300000**|**0x200000**||
||Exynos 9630|||

- Other DMA space:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 30

###### Samsung Exynos NPU Driver

###### Device open

###### • Load Firmware binary

###### **open(”/dev/vertex10”) -> npu_vertex_open -> npu_device_open -…> npu_system_resume**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 31

###### Samsung Exynos NPU Driver

###### Device open

###### • NPU power on

**open(”/dev/vertex10”) -> npu_vertex_open -> npu_device_open -…> npu_system_resume -…> npu_cpu_on**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 32

###### Samsung Exynos NPU Driver

Device open

- Kernel worker to handle the data on DMA buffer

**npu_vertex_open -> npu_device_open -…> proto_drv_open -…> auto_sleep_thread_create(…, proto_drv_do_task, …)**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 33

###### Samsung Exynos NPU Driver

- Finish address mapping while device probe. DMA buffer alloc & IOMMU configuration, from DTS. Create address mapping to IOMEM address and IOVA.

- Load Firmware & NPU power on when device open. Firmware image is on file system or in kernel image, no signature checking yet. NPU device power on , control processor start running the RTOS. AP side start worker task to handle the data transfer.

- Data transfer (userspace --- kernel --- firmware) AP and NPU communicate through DMA buffer.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 34

###### Samsung Exynos NPU Driver

- Finish address mapping while device probe. DMA buffer alloc & IOMMU configuration, from DTS. Create address mapping to IOMEM address and IOVA.

- Load Firmware & NPU power on when device open. Firmware image is on file system or in kernel image, no signature checking yet. NPU device power on , control processor start running the RTOS. AP side start worker task to handle the data transfer.

- Data transfer (userspace --- kernel --- firmware) AP and NPU communicate through DMA buffer. What data is on the DMA buffer actually?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 35

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Mailbox initialized while NPU power on

###### **npu_vertex_open -…> npu_system_resume**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 36

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Mailbox initialized while NPU power on

###### **npu_vertex_open -…> npu_system_resume**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 37

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Mailbox initialized while NPU power on

###### **npu_vertex_open -…> npu_system_resume -> npu_interface_open -> mailbox_init**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 38

###### Samsung Exynos NPU Driver

###### Mailbox

- Ring buffer init

**npu_vertex_open -…> npu_system_resume -> npu_interface_open -> mailbox_init**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 39

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Host to Firmware (network request)

###### **ioctl (…) -…> vertex_ioctl -…> npu_session_put_nw_req**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 40

###### Samsung Exynos NPU Driver

###### Mailbox

• Host to Firmware (network request) **kernel thread proto_drv_do_task -> npu_protodrv_handler_nw_free**

Later function npu_protodrv_handler_nw_requested handles the REQEUSTED network request.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 41

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Host to Firmware (network request) **npu_protodrv_handler_nw_requested -> __mbox_nw_ops_put -…> nw_req_manager -> mbx_ipc_put**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 42

###### Samsung Exynos NPU Driver

###### Mailbox

###### • Host to Firmware (network request) **npu_protodrv_handler_nw_requested -> __mbox_nw_ops_put -…> nw_req_manager -> mbx_ipc_put**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 43

###### Samsung Exynos NPU Driver

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blckhat
FW_DRAM DMA buffer
! 0
0x0 ee H 0x80000
-ox4oo0-—" -0x2000 -0x1800  -0x1400 —-0x1000 ;
f2h[1] f2h[0] padding
ee cmd.payload ‘
msg cmd msg cmd
¢ /
ION DMA buffer
|
ION DMA buffer, init by userspace, IOVA dynamically allocated with “dma-window" field in DTS }
Information Classification: General
```

## Slide 44

###### Samsung Exynos NPU Driver ION/DMA-buf heaps data

###### e.g. COMMAND_LOAD

memory_vector.type = { IN_FMAP, OT_FMAP, IM_FMAP, WEIGHT }

address_vector.m_addr : IOVA of feature map, weight…

#BHEU @BlackHatEvents

Information Classification: General

## Slide 45

###### Samsung Exynos NPU Driver COMMAND_PROCESS

**vertex_ioctl → npu_vertex_qbuf(VS4L_VERTEXIOC_QBUF) → npu_session_queue**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 46

###### Samsung Exynos NPU Driver

###### Summary

- kernel thread enqueues NCP requests and serializes them on Mailbox’s ring buffer.

- AP or NPU  side updates W/R ptr on Ring buffer, when new request/response arrives.

- Data on Ring buffer are message+command, the real payload data is on other ION DMA buffer.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 47

###### Samsung Exynos NPU Firmware

• Firmware image Loaded to DMA buffer while device open. No signature checking.

- RTOS

Running on NPU control core, 32bit ARMv7 Communicate with AP, get request & send result.

• Feature Basic subsystems: task, heap, events, etc. No modern OS mitigation.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 48

###### Samsung Exynos NPU Firmware

• Firmware boot up

Init heap, events, etc. Start native tasks for schedule.

How does it handle HOST’s requests? e.g. from LOW priority ring buffer

#BHEU @BlackHatEvents

Information Classification: General

## Slide 49

###### Samsung Exynos NPU Firmware

###### • TASK_mailbox_lowpriority

#BHEU @BlackHatEvents

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Samsung Exynos NPU Firmware
37 [2] = ;
° ° °
38 [3] = ;
¢ TASK_mailbox_lowpriority - 8) = viens
_ _ = msg->data;
40 [4] = msg->self; .
. - 41 [5] i call handler with msg.command.
42 [Oxc] = param_4; .
2 void my_TASK_mailbox_towpriority void) re [ovd] = param 3, for network LOAD request, handler is
; ; 44 [0x19] = *(undefined4 *)(param_1 + 0xd90); ncp_manager_load
5 | uint 45 enableIRQinterrupts(); ~ ~
6 int ; 46 = (**(code **)(param_1 + msg->command * 4 + Oxd60)) ( + Oxd);
7) uint * ; 47 = param_4;
8 uint * : =| 48 if ( '= 0) {
9 | undefined [4]; 49 = 3
10} undefined4 ; 50 my_printk(s_[ERR]%s:%d>cmd_handler_table[%d]_0000fae8,PTR_s_mbx_msghub_req_0000f9e4, 0x7
11) undefined4 ; 51 ,msg->command, 3
12) undefined4 [2]; 52 }
te 53 goto LAB_0000f894;
14 = *DAT_00010054; 54 } -
re uN. 00003be(1 ) 55 my_printk(s_[ERR]%s:%d>mid_%d_is_not_free_st_0000fa80,PTR_s_mbx_msghub_req_0000f9e4, 0x69,
7 = *DAT_O 54: 56 »param_4) ;
18) } 57 = 0x103;
19) my_printk( tart )1005c,PTR TASK mailbo pr ty_00010058); =l 58 enableIROinterrupts();
20 = DAT_00010054 + 2; =
21 = DAT_00010054 + Oxc5; loop to get network request From DMA buffer, l| ¢ Decompile: my_ncp_manager_load - (NPU.bin) % |x] i
22) dot ay mbx drward 7 according to the read/write ptr in mailbox_hdr 52 | *(undefinedd *) ( + * Oxddd + 0x1040) = 0x226;
Pit (ive ae a — se : : i 53 | *(undefined4 *) ( + * Qxdd4 + Ox103c) = 0;
25 my_printk(s_[ERR]%s:%d>mbx_dnward_get_is_fai_00010068,PTR_s TASK_mailbox_lowpriority 00010058, 54 | FUN_00020aac(*(undefined4 *) ( + * Oxdd4 + 0x1044) ,0x898) ;
26 ( ); 55 FUN_00020aac(*(undefined4 *) ( + * Qx4d4 + 0x1048) ,0x898);
27 my_printk(s_[ERR]%s:%d>BUG! !_0000ff68,PTR_s_TASK_mailbox_lowpriority_00010058, Ox5b) ; 56 | *(undefined4 *) ( + * Ox4d4 + Ox104c) = 0;
28 /* WARNING: Subroutine does not return */ 57 = (**(code **) (PTR DAT 00014760 + *(int *) ( + * Ox4d4 + Qxc94) * 0x20 + 0x24))
29 my_assert(); 58 ( 3 param ;
a] oy printk(s MSG(L). +. (dl parse & handle the request 59 = PTR_s_ncp_manager_load_00014710; . ..
y_P s_MSG(L)_+_[%d]_%t_ , rlocat_18); 60 | if ( == 0) calling another handler accoriding to cmd.
32 = my_mbx_msghub_req( , : (ol, i + { . .
33) } while ( == 0); 61 = 0; for LOAD is ncp_object_load
34| my_printk(s_[ERR]%s:%d>mk ub_req_is_fai_000100a4,PTR TASK_mailt Lowpriori 0010058,99, 62 = 0; _ _
35 ds; 63 = 0;
36) my_printk(s_[ERR] 1>BUG! !_0000Ff68,PTR ASK_mailt l rity_00010058, 100) ; 64 do {
37 /* WARNING: Subroutine does not return */ 65 _ +1:
38) my_assert(); ~ "
39}
an
Information Classification: General
```

## Slide 50

###### Samsung Exynos NPU Firmware

• TASK_mailbox_lowpriority

After process the payload, function mbx_msghub_req send response and set event. Later task TASK_mailbox_response will copy result to DMA buffer and notify host side.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 51

###### Samsung Exynos NPU Vulnerabilities

###### **CVE-2022-22265**

• double free，In-the-wild exploited

**vertex_ioctl → npu_vertex_s_format(VS4L_VERTEXIOC_S_FORMAT) → npu_queue_s_format → vb_queue_s_format**

**vertex_ioctl → npu_vertex_streamoff (VS4L_VERTEXIOC_STREAM_OFF) → npu_queue_stop → vb_queue_stop → __vb_queue_stop**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 52

###### Samsung Exynos NPU Vulnerabilities

###### **CVE-2022-22265**

• double free，In-the-wild exploited

**vertex_ioctl → npu_vertex_s_format(VS4L_VERTEXIOC_S_FORMAT) → npu_queue_s_format → vb_queue_s_format**

**vertex_ioctl → npu_vertex_streamoff (VS4L_VERTEXIOC_STREAM_OFF) → npu_queue_stop → vb_queue_stop → __vb_queue_stop**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 53

###### Samsung Exynos NPU Vulnerabilities

###### **CVE-2020-28343**

- TOCTOU issue between userspace & kernel

**vertex_ioctl → npu_vertex_s_graph(VS4L_VERTEXIOC_S_GRAPH) → npu_session_s_graph → __config_session_info**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 54

###### Samsung Exynos NPU Vulnerabilities

###### **CVE-2020-28343**

• TOCTOU issue between userspace & kernel **vertex_ioctl → npu_vertex_s_graph(VS4L_VERTEXIOC_S_GRAPH) → npu_session_s_graph → __config_session_info → __second_parsing_ncp**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 55

###### Samsung Exynos NPU Vulnerabilities

**CVE-2020-28343** • TOCTOU issue between userspace & kernel **vertex_ioctl → npu_vertex_s_graph(VS4L_VERTEXIOC_S_GRAPH) → npu_session_s_graph → __config_session_info → __second_parsing_ncp**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 56

###### Samsung Exynos NPU Vulnerabilities

###### **SVE-2021-20204**

###### • Multiple OOB access

###### **TASK_mailbox_lowpriority → mbx_msghub_req → ncp_manager_load → ncp_object_load → parser_init**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 57

###### Samsung Exynos NPU Vulnerabilities

###### **SVE-2021-20204**

- Multiple OOB access

**TASK_mailbox_lowpriority → mbx_msghub_req → ncp_manager_load → ncp_object_load → parser_init**

Add multiple range check to prevent OOB. Now kernel side and firmware side all have range check.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 58

###### Samsung Exynos NPU Vulnerabilities

###### **SVE-2021-20204**

- Multiple OOB access

**TASK_mailbox_lowpriority → mbx_msghub_req → ncp_manager_load → ncp_object_load → parser_init**

But Wait …

#BHEU @BlackHatEvents

Information Classification: General

## Slide 59

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

###### • Let’s look at the patch more closely

###### Kernel driver

Firmware

#BHEU @BlackHatEvents

Information Classification: General

## Slide 60

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

- The issue

here address_vector_index is on DMA buffer, the access to this address between AP with firmware may have latency.

So, here’s a TOCTOU issue(checked in kernel but used in firmware), leads to OOB access.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 61

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

- The issue

We can start another thread to race, in order to change the address_vector_index to a wrong value, after kernel’s check, but before firmware’s use.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 62

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

- Exploit

ivar14 is user controllable, though it has to be 0x10 aligned(*0x10), ivar15 is calculated from user input (width, height, stride),which is also under control.

So yes, we get an AAW primitive.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 63

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

###### • Exploit

###### Tips: function hook

So audit firmware with this bug pattern , I think should find more bugs,

#BHEU @BlackHatEvents

Information Classification: General

## Slide 64

###### Samsung Exynos NPU Exploit

###### **CVE-2023-42483**

- Exploit

We can put our shellcode on NPU’s heap, since all heap area are mapped executable. Putting shellcode behind the NCP object, firmware will copy them to heap space later. Shellcode are all hard coded, again, no ASLR J.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 65

###### Samsung Exynos NPU Exploit

###### **Same pattern, more bugs**

- **CVE-2023-45864**

###### There’re some other bugs with the same pattern in Exynos NPU firmware.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 66

###### Samsung Exynos NPU Exploit

###### **Same pattern, more bugs**

- **CVE-2023-45864**

###### There’re some other bugs with the same pattern in Exynos NPU firmware.

###### More?

#BHEU @BlackHatEvents

Information Classification: General

## Slide 67

### Apple Neural Engine

#BHEU @BlackHatEvents

Information Classification: General

## Slide 68

###### Apple Neural Engine

###### Overview

**https://github.com/0x36/weightBufs/blob/main/attacking_ane_poc2022.pdf**

**https://i.blackhat.com/asia-21/Friday-Handouts/as21-Wu-Apple-Neural_Engine.pdf**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 69

###### Apple Neural Engine

###### • **CVE-2022-32948 : index OOB**

**ZinComputeProgramUpdateMutables -> DeCxt::ProcessInitInfo -> DeCxt::ParseScaleBiasWeightFileInfo -> DeCxt::GetFileInfo -> DeCxt::FileIndexToWeight**

Bug:

Patch:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 70

###### Apple Neural Engine

- **CVE-2022-32899 : integer overflow leads to OOBW**

###### **DeCxt::RasterizeScaleBiasData**

Bug:

Patch:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 71

###### Apple Neural Engine

• **CVE-2022-32932 : Double Fetch**

###### **ZinComputeProgramUpdateMutables**

###### Bug:

###### Patch:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 72

###### Apple Neural Engine

• **CVE-2022-32840 : OOBW**

###### **H11ANEIn::ANE_ProgramSendRequest_gated**

Bug:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 73

###### Apple Neural Engine

- **CVE-2023-40409: OOB leads to type confusion**

When I audited the patch for CVE-2022-32948, I found the “H11ANEProgramRequestArgsStruct” structure has changed to this format:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 74

###### Apple Neural Engine

**https://github.com/0x36/weightBufs/blob/main/attacking_ane_poc2022.pdf**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 75

### Qualcomm Snapdragon NPU

#BHEU @BlackHatEvents

Information Classification: General

## Slide 76

###### Qualcomm Snapdragon NPU Driver

/dev/msm_npu

IOCTL:

**MSM_NPU_MAP_BUF MSM_NPU_UNMAP_BUF**

**User Space APPs, including untrusted APPs**

**_MSM_NPU_LOAD_NETWORK_V2 MSM_NPU_UNLOAD_NETWORK_ MSM_NPU_EXEC_NETWORK_V2** ……

npu_network_cmd

NPU Firmware

#BHEU @BlackHatEvents

Information Classification: General

## Slide 77

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 78

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

###### **struct npu_network network:**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock); npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 79

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**static struct npu_network_cmd *npu_alloc_network_cmd(struct npu_host_ctx *ctx, uint32_t stats_buf_size)**

**{ struct npu_network_cmd *cmd = NULL;**

**cmd = kmem_cache_zalloc(ctx->network_cmd_cache, GFP_KERNEL);**

**…**

**init_completion(&cmd->cmd_done); if (stats_buf_size == 0) return cmd; cmd->stats_buf = kmem_cache_zalloc(ctx->stats_buf_cache, GFP_KERNEL);**

**…**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**}**

**cmd->stats_buf_size = stats_buf_size; return cmd;**

**struct npu_network_cmd load_cmd:**

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_LOAD_V2; struct completion cmd_done; void *stats_buf;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 80

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

**static void npu_queue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)**

**{**

**INIT_LIST_HEAD(&cmd->list); list_add_tail(&cmd->list, &network->cmd_list);**

**}**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT);**

**mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

###### **struct npu_network network:**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**struct npu_network_cmd load_cmd:**

struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_LOAD_V2; struct completion cmd_done; void *stats_buf;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 81

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

NPU Firmware

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 82

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

###### **static void npu_dequeue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)**

**{ list_del(&cmd->list); }**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT);**

**mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

###### **struct npu_network network:**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**struct npu_network_cmd load_cmd:**

struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_LOAD_V2; struct completion cmd_done; void *stats_buf;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 83

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_LOAD_NETWORK_V2

**mutex_lock(&host_ctx->lock);**

**network = alloc_network(host_ctx, client);**

**load_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, load_cmd);**

**static void npu_free_network_cmd(struct npu_host_ctx *ctx, struct npu_network_cmd *cmd) { if (cmd->stats_buf) kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf); kmem_cache_free(ctx->network_cmd_cache, cmd);**

**}**

**npu_send_network_cmd(npu_dev, network, load_packet, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&load_cmd->cmd_done,NW_CMD_TIMEOUT);**

**mutex_lock(&host_ctx->lock);**

###### **struct npu_network network:**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**npu_dequeue_network_cmd(network, load_cmd);**

**npu_free_network_cmd(host_ctx, load_cmd);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 84

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 85

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

###### **struct npu_network network:**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl);**

**unload_cmd = npu_alloc_network_cmd(host_ctx, 0);**

**npu_queue_network_cmd(network, unload_cmd);**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 86

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd = npu_alloc_network_cmd(host_ctx, 0);**

**npu_queue_network_cmd(network, unload_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id);**

**mutex_unlock(&host_ctx->lock);**

**static struct npu_network_cmd *npu_alloc_network_cmd(struct npu_host_ctx *ctx, uint32_t stats_buf_size)**

**{**

**struct npu_network_cmd *cmd = NULL; cmd = kmem_cache_zalloc(ctx->network_cmd_cache, GFP_KERNEL); …**

**init_completion(&cmd->cmd_done); if (stats_buf_size == 0) return cmd; cmd->stats_buf = kmem_cache_zalloc(ctx->stats_buf_cache, GFP_KERNEL);**

**… cmd->stats_buf_size = stats_buf_size; return cmd;**

**}**

**struct npu_network_cmd unload_cmd:**

struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_ UNLOAD; struct completion cmd_done; void *stats_buf;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 87

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd);**

###### **static void npu_queue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)**

**{**

**INIT_LIST_HEAD(&cmd->list); list_add_tail(&cmd->list, &network->cmd_list); }**

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

###### **struct npu_network network:**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id);**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**struct npu_network_cmd unload_cmd:**

struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_ UNLOAD; struct completion cmd_done; void *stats_buf;

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 88

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

NPU Firmware

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 89

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd); npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**static void npu_dequeue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)**

**{ list_del(&cmd->list); }**

###### **struct npu_network network:**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd); npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

uint64_t id; **struct npu_network_cmd unload_cmd:** uint32_t network_hdl; struct list_head cmd_list; struct list_head list; uint32_t cmd_type = NPU_IPC_CMD_ UNLOAD; struct completion cmd_done; void *stats_buf;

**struct npu_network_cmd unload_cmd:**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 90

###### Qualcomm Snapdragon NPU Driver

###### • MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl);**

**unload_cmd = npu_alloc_network_cmd(host_ctx, 0);**

**npu_queue_network_cmd(network, unload_cmd);**

**npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**static void npu_free_network_cmd(struct npu_host_ctx *ctx, struct npu_network_cmd *cmd) { if (cmd->stats_buf) kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf); kmem_cache_free(ctx->network_cmd_cache, cmd); }**

###### **struct npu_network network:**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

**npu_dequeue_network_cmd(network, unload_cmd);**

**npu_free_network_cmd(host_ctx, unload_cmd);**

**free_network(host_ctx, client, network->id);**

**mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 91

###### Qualcomm Snapdragon NPU Driver

• MSM_NPU_UNLOAD_NETWORK

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl);**

**static void free_network(struct npu_host_ctx *ctx, struct npu_client *client, int64_t id) {**

**struct npu_network *network = NULL; struct npu_network_cmd *cmd;**

**…**

**unload_cmd = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd); npu_send_network_cmd(npu_dev, network, load_packet, unload_cmd); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd); npu_free_network_cmd(host_ctx, unload_cmd); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

**}**

**network = get_network_by_id(ctx, client, id); if (network) {**

**… while (!list_empty(&network->cmd_list)) { cmd = list_first_entry(&network->cmd_list, struct npu_network_cmd, list); npu_dequeue_network_cmd(network, cmd); npu_free_network_cmd(ctx, cmd);**

**}**

**… } Release all the cmd in the cmd_list!**

**struct npu_network network:**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 92

###### Qualcomm Snapdragon NPU Driver

The bug(CVE-2023-33114)

If we try to unload a network concurrently, what would happen?

###### **struct npu_network network:**

uint64_t id; uint32_t network_hdl; struct list_head cmd_list;

#BHEU @BlackHatEvents

Information Classification: General

## Slide 93

###### Qualcomm Snapdragon NPU Driver

Ø CVE-2023-33114

**Task A (on cpu1)**

**mutex_lock(&host_ctx->lock); network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd1 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd1); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd1->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 94

###### Qualcomm Snapdragon NPU Driver

###### Ø CVE-2023-33114

**Task A (on cpu1)**

**Task B (on cpu2)**

**mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd1 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd1); mutex_unlock(&host_ctx->lock);**

###### **mutex_lock(&host_ctx->lock);**

**network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd2 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd2); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd2->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd2); npu_free_network_cmd(host_ctx, unload_cmd2); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

**wait_for_completion_timeout(&unload_cmd1->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 95

###### Qualcomm Snapdragon NPU Driver

Ø CVE-2023-33114

**Task A (on cpu1)**

**Task B (on cpu2)**

**mutex_lock(&host_ctx->lock); network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd1 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd1); mutex_unlock(&host_ctx->lock);**

**mutex_lock(&host_ctx->lock); network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd2 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd2); mutex_unlock(&host_ctx->lock); wait_for_completion_timeout(&unload_cmd2->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock); npu_dequeue_network_cmd(network, unload_cmd2); npu_free_network_cmd(host_ctx, unload_cmd2); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock); unload_cmd1 gets released here!**

**wait_for_completion_timeout(&unload_cmd1->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

**UAF or Double free happens!**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 96

###### Qualcomm Snapdragon NPU Driver

###### With the bug, we can:

**wait_for_completion_timeout(&unload_cmd1->cmd_done, …); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

**static void npu_dequeue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd) { list_del(&cmd->list); list_del() primitive }**

**static void npu_free_network_cmd(struct npu_host_ctx *ctx, struct npu_network_cmd *cmd) {**

**if (cmd->stats_buf)** **_Arbitrary free() primitive_ kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf); kmem_cache_free(ctx->network_cmd_cache, cmd); } Double free primitive**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 97

###### Qualcomm Snapdragon NPU Driver

###### A large enough time window:

**Task A (on cpu1)**

**Task B (on cpu2)**

**mutex_lock(&host_ctx->lock); network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd1 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd1); mutex_unlock(&host_ctx->lock);**

**mutex_lock(&host_ctx->lock); network = get_network_by_hdl(host_ctx, …,unload->network_hdl); unload_cmd2 = npu_alloc_network_cmd(host_ctx, 0); npu_queue_network_cmd(network, unload_cmd2); mutex_unlock(&host_ctx->lock); wait_for_completion_timeout(&unload_cmd2->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock); npu_dequeue_network_cmd(network, unload_cmd2);** 20s **npu_free_network_cmd(host_ctx, unload_cmd2); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock); unload_cmd1 gets released here!**

**wait_for_completion_timeout(&unload_cmd1->cmd_done,NW_CMD_TIMEOUT); mutex_lock(&host_ctx->lock);**

**UAF or Double free happens!**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 98

###### Qualcomm Snapdragon NPU Driver

###### Limitations when exploiting

Ø A dedicated kmem_cache

**host_ctx->network_cmd_cache = kmem_cache_create("** **_network_cmd_cache_ ", sizeof(struct npu_network_cmd), 0, 0, NULL);**

**Occupy with the same object: struct npu_network_cmd** No exploitable routines found L

**Perform cross cache attack**

- By manipulating the npu_network_cmd objects npu_network_cmd object gets allocated and then released immediately L

- By manipulating kernel objects on the same kmem_cache (SLAB Merging )

#BHEU @BlackHatEvents

Information Classification: General

## Slide 99

###### Qualcomm Snapdragon NPU Driver

###### Limitations when exploiting Ø Misaligned object size

**struct npu_network_cmd { struct list_head list; uint32_t cmd_type; uint32_t cmd_id; uint32_t trans_id;** （104=13*8） **bool async; struct completion cmd_done; /* stats buf info */ uint32_t stats_buf_size; void __user *stats_buf_u; void *stats_buf; int ret_status; };**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 100

###### Qualcomm Snapdragon NPU Driver

###### Limitations when exploiting

Ø Misaligned object size

###### • **Heap spray with common struct objects** à **illegal memory access** L

**static void npu_dequeue_network_cmd(struct npu_network *network, struct npu_network_cmd *cmd)**

**wait_for_completion_timeout(&unload_cmd1->cmd_done, …); mutex_lock(&host_ctx->lock);**

**npu_dequeue_network_cmd(network, unload_cmd1); npu_free_network_cmd(host_ctx, unload_cmd1); free_network(host_ctx, client, network->id); mutex_unlock(&host_ctx->lock);**

**{ list_del(&cmd->list); list_del() primitive** panic **}**

**static void npu_free_network_cmd(struct npu_host_ctx *ctx, struct npu_network_cmd *cmd)** panic **{ if (cmd->stats_buf)** **_Arbitrary free() primitive_ kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf);**

> **kmem_cache_free(ctx->network_cmd_cache, cmd);** panic **} Double free primitive**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 101

###### Qualcomm Snapdragon NPU Driver

###### Limitations when exploiting

Ø Misaligned object size

- **Heap spray with array** J

   - Page table

   - Page pointer array

- file array

……

###### array slab

#BHEU @BlackHatEvents

Information Classification: General

## Slide 102

###### Qualcomm Snapdragon NPU Driver Limitations when exploiting ü **Advantage of file array**

- Corrupt the first 16bytes of struct file has no side effect

**struct file { union { struct llist_node fu_llist; struct rcu_head fu_rcuhead; } f_u; … }**

- Every element of file array can be set to valid file pointer or zero individually

- Corrupt any element won’t cause panic directly

#BHEU @BlackHatEvents

Information Classification: General

## Slide 103

###### Qualcomm Snapdragon NPU Driver

###### Occupy npu_network_cmd with file array

struct npu_network_cmd file array
struct list_head list; struct list_head *next; struct file * file;
struct list_head *prev; struct file * file;
+16 +16
uint32_t cmd_type; 0
uint32_t cmd_id;
uint32_t trans_id; 0
bool async;
+32 +32
struct completion cmd_done; 0
0
+48
0
0
+64
0
uint32_t stats_buf_size; 0
padding
+80 +80
void __user *stats_buf_u; 0
void *stats_buf; struct file *file;
+96 +96
int ret_status; 0
#BHEU @BlackHatEvents
+104 +104

Information Classification: General

## Slide 104

###### Qualcomm Snapdragon NPU Driver

###### Occupy npu_network_cmd with file array

static void npu_free_network_cmd(struct npu_host_ctx *ctx,
struct npu_network_cmd *cmd)
{
if (cmd->stats_buf)
kmem_cache_free(ctx->stats_buf_cache, cmd->stats_buf);
kmem_cache_free(ctx->network_cmd_cache, cmd);
}
struct npu_network_cmd file array
struct list_head list; struct list_head *next; struct file * file;
struct list_head *prev; struct file * file;
…… ……
void __user *stats_buf_u; 0
void *stats_buf; struct file *file;
File UAF  happens!
int ret_status; 0

#BHEU @BlackHatEvents

Information Classification: General

## Slide 105

###### Qualcomm Snapdragon NPU Driver

File UAF —— A very popular kind of vulnerability in recent years!

- 《 <u>Exploiting race conditions on [ancient] Linux 》</u> by Jann Horn

- 《 <u>Linux kernel: erroneous error handling after fd_install() 》</u> by Mathias Krause

- 《 <u>Cautious! A New Exploitation Method! No Pipe but as Nasty as Dirty Pipe 》</u> by Zhenpeng Lin, Yuhang Wu, Xinyu Xing

- • 《 <u>Devils Are in the File Descriptors: It Is Time To Catch Them All 》</u> by Le Wu

- 《 <u>Monitoring Surveillance Vendors: A Deep Dive into In-the-Wild Android Full Chains in 2021 》</u> by Xingyu Jin, Christian Resell, Clement Lecigne, Richard Neal

- 《 <u>Canary in the Kernel Mine: Exploiting and Defending Against Same-Type Object Reuse 》</u> by Mathias Krause

- 《 <u>Ret2page-The-Art-of-Exploiting-Use-After-Free-Vulnerabilities-in-the-Dedicated-Cache》</u> by Yong Wang

- 《 <u>A Very Powerful Clipboard: Analysis of a Samsung in-the-wild exploit chain 》</u> by Maddie Stone

- ……

**<u>《Dirty Pagetable: A Novel Exploitation Technique To Rule Linux Kernel》by Le Wu and Ye Zhang</u>**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 106

###### Qualcomm Snapdragon NPU Driver

Exploit file UAF with Dirty Pagetable

- **Occupy released victim file object with user page table:**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 107

###### Qualcomm Snapdragon NPU Driver

Exploit file UAF with Dirty Pagetable

- **Perform the increment primitive of file object:**

//victim_pte += 0x1000 for(int i = 0; i < 0x1000; i++) { dup(victim_fd); }

#BHEU @BlackHatEvents

Information Classification: General

## Slide 108

###### Qualcomm Snapdragon NPU Driver

Exploit file UAF with Dirty Pagetable

- **Get AARW by manipulating the pipe buffer !**

#BHEU @BlackHatEvents

Information Classification: General

## Slide 109

###### Qualcomm Snapdragon NPU Driver

ROOT on Samsung S20 5G:

#BHEU @BlackHatEvents

Information Classification: General

## Slide 110

#### Conclusion & Future work

#BHEU @BlackHatEvents

Information Classification: General

## Slide 111

###### Conclusion / Future work

###### Conclusion:

- User space -- kernel -- firmware, TOCTOU / Double Fetch bug pattern.

- Old bugs -> new bugs, patch analysis.

- Vendors should correctly enhance SELinux policy.

- Some code lack of review, more bugs to be found.

###### TODO:

- More firmware reverse / driver audit.

- Vendor’s specific model file parsing issues.

- Lower level hardware issues.

#BHEU @BlackHatEvents

Information Classification: General

## Slide 112

###### Reference

- https://blog.impalabs.com/2103_reversing-samsung-npu.html

- https://blog.impalabs.com/2110_exploiting-samsung-npu.html

- https://i.blackhat.com/asia-21/Friday-Handouts/as21-Wu-Apple-Neural_Engine.pdf

- https://github.com/0x36/weightBufs/blob/main/attacking_ane_poc2022.pdf

- https://securitylab.github.com/research/qualcomm_npu/

- https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2022/CVE-2022-22265.html

- https://bugs.chromium.org/p/project-zero/issues/detail?id=2073

- https://github.com/antgroup-arclab/ANETools

- https://static.sched.com/hosted_files/lsseu2019/04/LSSEU2019%20-%20Exploiting%20race%20conditions%20on%20Linux.pdf

- https://seclists.org/oss-sec/2022/q1/99

- https://i.blackhat.com/USA-22/Thursday/US-22-Lin-Cautious-A-New-Exploitation-Method.pdf

- https://i.blackhat.com/USA-22/Wednesday/US-22-Wu-Devils-Are-in-the-File.pdf

- https://i.blackhat.com/USA-22/Wednesday/US-22-Jin-Monitoring-Surveillance-Vendors.pdf

- https://github.com/opensrcsec/same_type_object_reuse_exploits

- https://i.blackhat.com/USA-22/Thursday/US-22-WANG-Ret2page-The-Art-of-Exploiting-Use-After-Free-Vulnerabilities-in-the-Dedicated-Cache.pdf

- • https://googleprojectzero.blogspot.com/2022/11/a-very-powerful-clipboard-samsung-in-the-wild-exploit-chain.html

- https://machinethink.net/blog/mobile-architectures

#BHEU @BlackHatEvents

Information Classification: General

## Slide 113

### Thank you!

#BHEU @BlackHatEvents

Information Classification: General
