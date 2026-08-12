---
title: "Physical Attacks Against Smartphones"
speakers: ["Christopher Wade"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Christopher Wade_Physical Attacks Against Smartphones.pdf"
pages: 69
sha256: "c61694c61ec56879c61f1de7c3d5d969dc3b674d80f0a40c92b2635dcfb0fd98"
text_chars: 18117
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:14:35Z"
---
# Physical Attacks Against Smartphones

**Speakers:** Christopher Wade  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Christopher Wade_Physical Attacks Against Smartphones.pdf` (69 pages)


## Slide 1

# Physical Attacks Against Smartphones

Christopher Wade @Iskuri1

## Slide 2

## Introduction

Modern smartphones employ a high number of measures to protect their security

Despite this, simple techniques can still be used to break physical security

In this talk, we will discuss two case studies:

- Gaining root access to a smartphone with no bootloader unlocking capability

- Gaining code execution in the bootloader of a Samsung smartphone

## Slide 3

Case Study 1 - Rooting On A Locked Bootloader

I wanted to root my old smartphone to test mobile applications

On most Android devices, this has a standard approach: bootloader unlocking While some OEMs place restrictions on this feature, this phone had it disabled completely

## Slide 4

## Target Device

A Smartphone From A Chinese OEM

Released in 2019

Uses an OEM-developed fork of Android

## Slide 5

## Disabled Bootloader Unlock

The device used a special engineering app to permit unlocking

This used a signature stored in a special partition, inaccessible to standard users

It was not publicly available, and required an approved user account

## Slide 6

## Disabled Bootloader Unlock

When bootloader unlocking isn’t available, an exploit is generally required to escalate privileges

With no direct access to the bootloader USB interface, a vulnerability was needed in the Android fork

The Android fork contained a high number of custom System-level apps and Rootlevel services which could potentially be exploited

## Slide 7

## Finding An Exploit

The Android fork had a service running as root, which could be called by Systemlevel applications

The purpose of the service was to facilitate archiving of App data on a remote server

Brief analysis of the service binary found a command injection vulnerability, which would provide immediate root access

This could be exploited by archiving a file with backticks in the name

## Slide 8

## SELinux Protection

Android uses SELinux to control access between software components

This can be used to prevent a process with root access from accessing other components of the Operating System

The root command injection vulnerability was extremely locked down, only allowing access to all application data, but nothing else on the device

## Slide 9

## Alternative Attack Vectors

SELinux was well configured throughout the OS

Most vulnerabilities would be limited to the SELinux context, and useless without a Kernel exploit

As the bootloader was locked down, and any OS exploits would be useless on their own, focus was placed on the next most available target: Recovery Mode

## Slide 10

## Custom Recovery Mode

Recovery mode in Android uses a standard architecture to full-fledged Android, and often uses the same Kernel built for the main OS

Recovery mode is usually basic, covering a few menu options controlled by the phone’s volume buttons

In the OEM’s Android fork, this had been replaced with a fully-featured interface

## Slide 11

## Finding An Update Image

In order to find a vulnerability in Recovery mode, the firmware image would be useful

Downloading an update .zip for the device found that it didn’t contain the recovery image at all

Several iterations of updates were downloaded, and Recovery was not in any of them

## Slide 12

## Recovery Mode Menu

With no recovery image to reverse engineer, basic attacks were attempted

The menu included the option to load encrypted firmware updates from external storage A vulnerability in this feature would be the easiest to exploit

## Slide 13

## Finding An Exploit

Due to the command injection vulnerability in the Android fork, a similar attack was attempted

A legitimate encrypted update file was renamed to contain a command:

```
`sleep 30000`.zip
```

This caused the update process to hang, demonstrating that it was vulnerable to command injection somewhere

## Slide 14

## Disclosure

Both command injection vulnerabilities were disclosed to the OEM

They were swiftly remediated, and new versions of the software were released As the Recovery Mode command injection was likely to run as root, and have no restrictions, this would be the basis for gaining root access to Android

## Slide 15

## Root Cause Analysis

By checking the running processes, the injection point could be identified

A sha1sum command was in use by the Recovery process

In the /sbin/recovery binary, the command was present

## Slide 16

## Exploiting Command Injection

As there was a command injection vulnerability in the filename, this could be used to execute a more complex script

By altering the name to include a base64 encoded command, piped into /system/bin/sh, a shell script could be read from the filesystem and executed:

```
`echo Y2F0IC9kYXRhL21lZGlhLzAvYmFja2Rvb3Iuc2ggfCBzaAo= | busybox base64 -d
- | sh`.zip
```

## Slide 17

## Exploiting Command Injection

The filesystem used by Android’s userdata does not support all special characters Due to this, a MicroSD Card was formatted to EXT4, allowing for extra characters

Android does not typically support EXT4, but the custom Recovery Mode did

## Slide 18

## Getting A Shell

To gather more information, a script was used which wrote key information about the OS to a file

This included the fact that the recovery process was running as root, and that SELinux could be disabled completely

With the capability to run a shell script from Recovery Mode, ADB was also reenabled

## Slide 19

## Switching To Android

Root access in Recovery mode gave full access to the device This would allow for modification of some data, but not control over the core Android OS upon a reboot

A method would be required for switching from Recovery to Android without rebooting

## Slide 20

## Kexec

Kexec is a part of the Linux Kernel which allows for booting a new Kernel from the current one

While this would be the perfect solution, it is not typically compiled into Android, and could not be loaded as a Kernel module due to signature verification

A userspace-only solution was required

## Slide 21

## Ptrace

Ptrace is a system call allowing a process to observe and control another

Typically, this is used for debugging purposes, but is extremely useful for exploitation

Even W^X memory can be overwritten and executed

Ptrace could be used to override and replace the “init” process, restarting it in a new context

## Slide 22

## Overriding Init

Ptrace can be configured to immediately pause the process

The subsequent operations can then be altered to execute execve to run commands

Using execve will cause the PID to remain as 1

## Slide 23

## switch_root

switch_root is used to switch to a new root filesystem

This is a common feature on Linux-based devices, to switch from the RAMDisk to the main root filesystem

We could use this to switch from the Recovery RAMDisk to Android’s

## Slide 24

Init Process

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Init Process
!
init selinux_setup
t
init second stage
```

## Slide 25

Init Process

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Init Process
init selinux_setup
t
init second_stage
’
switch_root /boot_rd/ /init
’
|
init selinux_setup
'
init second_stage
```

## Slide 26

## Shared Mounts

A core component of switch_root is the remounting of mounted folders Remounting does not work on folders mounted as “shared”, including standard Android partitions

This could trivially be resolved by switching all folders to “private”

## Slide 27

## Patching out SELinux Checks

The init binary checks /proc/cmdline for whether the image requires SELinux If it does, and it is disabled, init forcibly reenables it

Ptrace could be used to override the “read” syscall, removing the parameter

## Slide 28

## Fixing Kernel Panics

Init also executes all of  the .rc scripts

This included initialising hardware which Recovery had already initialised

The second initialisation caused a Kernel panic in many cases, crashing the device This could be trivially remediated by using Ptrace to return an empty script for all hardware initialisation .rc files

## Slide 29

## Reinitialising Services

Once Android had started, services were still running in the Recovery context

This prevented PIN unlocking from operating This could be trivially resolved by killing the processes before the new version of init started

## Slide 30

## Replacing Read-Only Files

The System partition of the Android OS uses dm-verity to ensure it cannot be modified

Despite this, system files can be overlayed using the “mount –bind” command

This can allow for modification of System services, as well as other core files By replacing core apps and frameworks, bloatware and root-access checks can be removed

## Slide 31

Demo

## Slide 32

## Hidden RAMDisk

For debugging purposes, a Busybox Telnetd server was started within Recovery, but after Android had started, the server was still running Logging into it found that the Recovery RAMDisk was still in place, but empty

Using Busybox, the standard tools could be repopulated

## Slide 33

## Hidden RAMDisk

The Recovery RAMDisk was hidden from Android

CDing/Chrooting to the directory /proc/1/root from Recovery would access the Android rootfs as root

The same hidden context could be used to add a Debian chroot, independent of Android, with access to all hardware and hidden control over Android

## Slide 34

## Conclusion

Root access via this method was found to work consistently

The tool manipulating init via Ptrace continued to operate in the background, with no impact to the device

Rebooting the phone had no ill effects, and it could operate normally, without persistent root access

Ptrace should never be required on a standard Android device, and only serves to assist attackers

## Slide 35

Case Study 2 – Exploiting An Exynos Secondary Bootloader Exynos-based devices have had significant research performed on Download mode in their secondary bootloader

This all focused on the high-level Download protocol, and not on the USB stack itself

I wanted to find a vulnerability in the core USB stack

## Slide 36

## Target Device

Samsung Galaxy A04S

Released In August 2022 Exynos 850 Chipset

## Slide 37

## Sboot

The Exynos secondary bootloader has multiple features: Standard boot Download mode Fastboot mode Upload mode

All of this is encompassed in a single firmware binary: sboot.bin This meant the USB protocol of the three modes would likely use the same core USB stack

## Slide 38

## USB Control Transfers

Control Transfers are used to send and receive information about a USB device

Use standard parameters:

bmRequestType bRequest wValue wIndex Buffer

Buffer Size

## Slide 39

## Fuzzing USB Control Transfers

Control Transfers are mostly stateless

Basic fuzzing can be achieved just by randomising all parameters

Unsuccessful requests can be easily filtered out

## Slide 40

Initial Fuzzing Attempts Sending purely random data caused the device to reboot into a failure mode

This occurred when an 0xf6 value was in the bRequest parameter

The failure mode was recoverable using Download mode tools, and 0xf6 values were filtered out

## Slide 41

## Causing A Crash

Continued fuzzing found that the device would crash and reboot after a certain set of transfers

Transfers in the sequence were removed until the root cause was identified One transfer was a malformed GET_DESCRIPTOR request, transferring in the wrong direction, and the second was a valid GET_DESCRIPTOR request

## Slide 42

## Descriptor Overwrite

GET_DESCRIPTOR is a core Control Transfer that retrieves descriptors about the device

This data should always be transmitted to the host, and never received from it

The first byte of the data is always the size of the buffer If this can be overwritten, usually the buffer size can be extended to cover out of bounds memory, as well as alter the data at that location

## Slide 43

## Descriptor Overwrite

Most USB stacks do not check the Control Transfer Direction

They are usually protected by how they handle USB transactions If they don’t verify the direction, but do specify a response direction, they are not vulnerable

STM32 USBD Stack:

## Slide 44

## Exploiting Descriptor Overwrite

The size byte of the buffer was overwritten

This was ineffective, and didn’t alter the size of data received

Luckily, there was also a buffer overflow in the Control Transfer buffer

Data next to the buffer could be overwritten, regardless of the size parameter

## Slide 45

## Brute Forcing Memory

Sending a large buffer caused the device to crash and reboot

Buffers of increasing byte values and sizes were sent, until several valid pointers were generated

These were found to be pointers to other Descriptors Modifying these pointers facilitated arbitrary memory read/write

## Slide 46

## Dumping Memory

The pointers in the brute-forced memory were between 0xf9000000 and 0xfa000000 A memory dump was created of data from 0xf8000000 onwards

This included the entire running bootloader and RAM contents, starting at 0xf8800000

## Slide 47

## DEP Misconfiguration

As the running bootloader was in RAM, attempts were made to override its opcodes

This caused the device to hang, implying DEP was configured

Attempts to execute code written into unused RAM were successful

## Slide 48

## Patching In New Functions

C functions can be compiled to object using “gcc –static –nostdlib”

Using the objcopy command, this can be converted to a raw binary Directly writing these into memory was sufficient to execute them, due to the DEP misconfiguration

## Slide 49

## Basic Code Execution

Fastboot mode was used as a base for the exploit

Fastboot uses string-based commands which usually keep function pointers in a table, simplifying code execution

Modifying this table would allow for easy code execution, without modifying the stack The getvar: command was chosen for calling other functions

## Slide 50

Basic Code Execution

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Basic Code Execution
f8931bf0 48
f8
00
f8931bf8
8931c00
8931c08
PTR_s_reboot_f8931bf0
addr s_reboot_f88e6948
PTR_reboot_command_f8931bf8
addr reboot_command
PTR_s_getvar:_f8931c00
addr s_getvar:_f88e6950
getvar_command
```

## Slide 51

## Reimplementing Boot

Code execution in the bootloader meant that secure boot bypass would be possible No USB-based mode had the capability to boot directly to Android

Directly calling the standard boot function crashed the phone

## Slide 52

## Reimplementing Boot

There were two options for reimplementing the boot process:

Copy the entirety of sboot to writeable memory, and call the required functions

Reimplement the boot functionality from scratch

The latter choice was chosen, due to a lack of writeable memory available

## Slide 53

Reimplementing Boot Functions in the bootloader can be trivially called by absolute addresses in C

These could be used to replicate the entire boot function call flow

Functions could be removed that weren’t necessary for booting

## Slide 54

## Boot Debugging

The bootloader contained a huge number of debug strings

These were written into RAM at address 0xf0000000

By comparing my boot implementation’s output to a legitimate boot process, debugging would be possible

## Slide 55

## Kernel Execution

The boot process ended with calling directly into the Kernel

This included KASLR, with the Kernel base address being stored in memory

Standard debugging of errors would be impossible after execution

## Slide 56

## Boot Failure

After patching in all of the appropriate functions, a Kernel loaded into memory could be executed

This hung, and never started Android

The Kernel code could be modified after loading, so each step was altered to return back to the bootloader, so the function causing the crash could be identified

## Slide 57

## Boot Failure

The device froze after the Kernel reinitialised the MMU

This implied that parts of the bootloader were still executing

The most likely reason was the bootloader potentially using threads

## Slide 58

## Bootloader Threads

Most Android bootloaders use a single thread for all functionality

Sboot was found to implement an RTOS to handle all management features As the Kernel altered the MMU page tables, they were attempting to execute unmapped memory

## Slide 59

## Bootloader Threads

Three threads were identified on the device: Background Tasks USB Control Transfers High Level USB Communication

Each one was constantly running, and had no trivial way to disable them individually

## Slide 60

## Disabling Threads

A simple solution was required to disable all threads

Throwing an exception would achieve this Recovering from the exception would not be required

The Kernel bootstrapping code could be executed from an exception

## Slide 61

## Aarch64 Exceptions

The VBAR_EL1 register points to the exception vector table for Sboot

Every 128 bytes is a different exception type By pointing VBAR_EL1 to a table with NOPs, followed by the boot code, any exception would execute the payload

## Slide 62

## Additional Errors

Even with the Kernel booting, Android still failed to start, reverting to Recovery mode

The error was within the fs_mgr_mount_all function

This error message suggested that the userdata partition could not be decrypted

This strongly implied that key storage was not enabling properly

## Slide 63

## Additional Errors

Analysing the logs prior to boot found that multiple hardware initialisations were being performed twice, including keystorage

This was due to Fastboot requiring them for other purposes

The second initialisation would fail, and break the rest of the process

## Slide 64

## Additional Errors

Both keystorage and TEE functions were enabled by a large, complex function

This was fully reimplemented, with the functions removed

With the errors removed, the phone could complete booting to Android

## Slide 65

Demo

## Slide 66

## Android Modification

It was possible to modify the Android image at any point prior to Kernel execution With the arbitrary memory read/write vulnerability, this would be trivial

The Kernel could be modified without triggering protection mechanisms

## Slide 67

## Final Notes

As the exploit could now be triggered using an exception, any boot mode could be used

This meant even vulnerable Samsung devices without Fastboot could be exploited While code execution was possible in the Kernel, there was still a risk of triggering KNOX

## Slide 68

## Disclosure

The initial vulnerability was disclosed to Samsung in December 2022 Samsung provided constant updates on progress, and patched the finding within three months

The target device was updated, and found to no longer be vulnerable to the Descriptor Overwrite vulnerability

Tools will be released demonstrating the outlined exploit

## Slide 69

## Conclusion

Most devices will still have exploitable vulnerabilities, despite the resources used to mitigate against them

Even with basic vulnerabilities, the effort required to go from a proof-of-concept to a full exploit can be extremely rewarding

Even on targets which have had a huge amount of research performed on them, there will still be a vector no one else has tried
