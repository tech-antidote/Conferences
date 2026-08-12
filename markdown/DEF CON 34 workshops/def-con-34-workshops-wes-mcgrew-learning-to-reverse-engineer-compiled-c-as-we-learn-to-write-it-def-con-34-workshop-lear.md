---
title: "Learning to Reverse Engineer Compiled C as We Learn to Write It"
speakers: ["Wes McGrew"]
conference: "DEF CON"
conference_full: "DEF CON 34"
year: 2026
source_type: "workshop-materials"
source_dir: "DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing"
files_included: 57
files_skipped: 140
text_chars: 80276
redacted_secrets: 0
sha256: "d02363dde2cfcb2f035aeadc441569d87a9cd8c8da12bfa9631649fc6346df22"
converted_at: "2026-08-12T02:54:56Z"
---

# Learning to Reverse Engineer Compiled C as We Learn to Write It

**Speakers:** Wes McGrew  
**Conference:** DEF CON 34 (workshop materials)  
**Contents:** 57 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Files not inlined

Binaries and oversized artefacts, listed for completeness:

- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/._dc34_workshop_learning_reversing_c` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/._.DS_Store` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/._windows_types.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._.DS_Store` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._bgc_source.zip` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._bgc_usl_c_1.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._dc33_x64_workshop` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._intel_manual_june_2026.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._modernC.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/._thecbook.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._manual.pdf` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_1_and_2` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_3` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_4` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_5` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_6` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/._module_7` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_1_and_2/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_1_and_2/._simple.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_1_and_2/._simple.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._hello.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._hello.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._write.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._write.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_4/._data.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_4/._data.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_4/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_5/._math.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_5/._math.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_5/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_6/._control.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_6/._control.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_6/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_7/._download.exe` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_7/._download.obj` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_7/._mllink$.lnk` — 0 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/.DS_Store` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/c_reversing_workshop.gar` — 3708 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_2dinit.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_2dinit.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_arrayptr.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_arrayptr.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_funcmod.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_funcmod.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_init.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_init.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fread.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fread.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fwrite.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fwrite.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/intro_hello.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/intro_hello.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/pointers2_qsort.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/pointers2_qsort.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/scope_global.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/scope_global.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/structs2_commoninitseq.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/structs2_commoninitseq.obj` — 4 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/types4_staticvar.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/types4_staticvar.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_if.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_if.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_print.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_print.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_do_while.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_do_while.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_passfunc.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_passfunc.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_ptrarith.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_ptrarith.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_switch.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_switch.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_while.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_while.obj` — 3 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_2dinit.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_2dinit.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_arrayptr.exe` — 10 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_arrayptr.obj` — 2 KB (binary)
- `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_funcmod.exe` — 10 KB (binary)
- …and 60 more

## Materials

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/._README.md`

```markdown
    Mac OS X            	   2   �      �                                      ATTR       �   �                     �     com.apple.lastuseddate#PS       �     com.apple.provenance 	Dj    �2     9��[g)]
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/._pi-session_windows_api_port.html`

```html
    Mac OS X            	   2   �      �                                      ATTR       �   �                     �     com.apple.lastuseddate#PS       �     com.apple.provenance �Dj    �}�0     ��У�Ly
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/._windows_types.md`

```markdown
    Mac OS X            	   2   �      �                                      ATTR       �   �                     �     com.apple.lastuseddate#PS       �     com.apple.provenance �Cj    S	p:     9��[g)]
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_1_and_2/._simple.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._hello.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/._write.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_4/._data.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_5/._math.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_6/._control.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/__MACOSX/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_7/._download.asm`

```asm
    Mac OS X            	   2   �      �                                      ATTR       �   �   =                  �   =  com.apple.quarantine q/0281;6a4401b2;Firefox;F889D3CC-5616-4FF3-BE65-A8C6E1FB8414 
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/README.md`

```markdown
# Learning to Reverse Engineer Compile C as We Learn to Write It

## Message to Students From the Instructor

Attendees:

Thank you so much for signing up for my DEF CON 33 workshop, "Learning 
to Reverse Engineer Compile C as We Learn to Write It". The purpose of 
this message is to give you the information you need to get yourself and 
your laptop ready for this workshop:

On your laptop, should you want to follow along step by step:

- Download the materials from 
  https://drive.google.com/drive/folders/1zG5dm20P3x-Q6BtpHlr74_D-qNzVhBfL?usp=sharing
- Ghidra (https://github.com/nationalsecurityagency/ghidra)
  - At a minimum, you'll need a Ghidra installation. We will be analyzing
    programs compiled within Windows, but you will be able to create and
    open the projects within Ghidra in any operating system.
- A text editor of your choice.
- If you want to be able to compile and run the programs yourself:
  - Windows 11 (10 is probably fine) - Either native or in a virtual
    machine.
  - Visual Studio Community

I will be demonstrating and discussing the use of locally-hosted AI. If
you have a locally hosted AI environment, or a subscription to a cloud 
service, you may be able to use it in the workshop. It is not required 
to get the full benefit of the workshop.

You:
- There is no programming or reverse engineering prerequisite for this
  workshop. You need to be able to download and navigate files on your 
  computer, and install software.
- You can follow along live, collaborate with a fellow student, or simply
  observe.
- Ask questions! I'd rather everyone understand the material that we can
  cover, rather than cover more material

If you trade or gift your EventBrite ticket to someone else, please give
them the text of this message as well.

I enjoy communicating with folk that sign up for my workshops! I have 
recently set up a Discord server for folks interested in following my 
DEF CON content (this workshop, my talk, and DJ sets), that also 
serves as a way for like-minded people to coordinate meeting at the 
conference and stay in touch before and after. There is a channel 
specifically for this workshop, where you're welcome to ask me 
questions and discuss the material with your fellow attendees:

Proper Villains Social Club: https://discord.gg/USbV3CFjVA

If you're the private sort, that's completely optional. If you have 
any questions leading up to the workshop, or would like to introduce 
yourself and talk a bit, you can get in touch with me directly:

Email: wesleymcgrew@gmail.com
X: @McGrewSecurity

## Abstract

Software reverse engineering is a fundamental skill: a prerequisite
to engaging with many fields of study in computer security that depend
on low-level knowledge. Malware analysis, vulnerability research,
offensive tool development, and digital forensics all involve the
analysis of code which has been compiled, obfuscated, or otherwise
stripped of useful names, data types, comments, and other
human-readable information. Without the ability to read disassembled
code, you will not be able to understand code that your computer will
happily execute.

In this workshop, I will guide you through learning to read
disassembled code *while* you learn C. We will progress through the C
programming language's constructs with as few assumptions as possible
about your background, and at each stage we will reverse engineer the
compiler's output in Ghidra and trace through with a debugger to
understand the generated code. You do not need any prior experience in
programming.

I will also be demonstrating useful techniques for using
locally-hosted large language models to aid in the learning process.
Use AI to improve your own skillset, rather than using it to do the
work for you.

## Contents of this Distribution

- Example code that we will be compiling and reversing
  - Taken and adapted from Beej's Guide to C Programming
    - https://beej.us/guide/bgc/
  - examples_crt/ - Examples for standard C libraries and runtime
  - examples_win/ - A port of the exercises to the Windows API and types
- c_reversing_workshop.gar - Archived copy of a Ghidra project
  containing processed copies of the examples
- windows_types.md and .pdf - A reference to data types used in the
  Windows API
- pi-session_windows_api_port.html - A transcript of the session where
  an LLM was used to create the Windows API version of the examples from
  the C runtime version, using a local AI model.
- Resources - Additional free reference material
  - Beej's Guide to C - PDF and example code
  - Intel X64 Manual
  - Material from my previous workshop on X64 assembly programming
  - Alternate C Books/Reference
    - Modern C - Jens Gustedt
    - The C Book - Banahan, Brady, Doran
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_2dinit.c`

```c
#include <stdio.h>

int main(void)
{
    int row, col;

    int a[2][5] = {      // Initialize a 2D array
        {0, 1, 2, 3, 4},
        {5, 6, 7, 8, 9}
    };

    for (row = 0; row < 2; row++) {
        for (col = 0; col < 5; col++) {
            printf("(%d,%d) = %d\n", row, col, a[row][col]);
        }
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_arrayptr.c`

```c
#include <stdio.h>

int main(void)
{
    int a[5] = {11, 22, 33, 44, 55};
    int *p;

    //p = &a[0];  // p points to the array
                  // Well, to the first element, actually

    p = a;      // p points to the array, but much nicer-looking!

    printf("%d\n", *p);  // Prints "11"
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_funcmod.c`

```c
#include <stdio.h>

void double_array(int *a, int len)
{
    // Multiple each element by 2
    //
    // This doubles the values in x in main() since x and a both point
    // to the same array in memory!

    for (int i = 0; i < len; i++)
        a[i] *= 2;
}

int main(void)
{
    int x[5] = {1, 2, 3, 4, 5};

    double_array(x, 5);

    for (int i = 0; i < 5; i++)
        printf("%d\n", x[i]);  // 2, 4, 6, 8, 10!
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/arrays_init.c`

```c
#include <stdio.h>

int main(void)
{
    int i;
    int a[5] = {22, 37, 3490, 18, 95};  // Initialize with these values

    for (i = 0; i < 5; i++) {
        printf("%d\n", a[i]);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/build_all.bat`

```bat
@echo off
REM Program 1: Hello World
cl /MD /O1 /Gy /DEBUG:NONE /nologo intro_hello.c

REM Program 2: Variables - int, float, and char*
cl /MD /O1 /Gy /DEBUG:NONE /nologo var_stat_print.c

REM Program 3: Pointer arithmetic
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_ptrarith.c

REM Program 4: Flow control: if
REM Try it again with "else"
cl /MD /O1 /Gy /DEBUG:NONE /nologo var_stat_if.c

REM Program 5: Flow control: while
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_while.c

REM Program 6: Flow control: do/while
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_do_while.c

REM Program 7: Flow control: for (as well as arrays)
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_init.c

REM Program 8: Flow control: Nested loops
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_2dinit.c

REM Program 9: Flow control: switch
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_switch.c

REM Program 10: Functions
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_passfunc.c

REM Program 11: Scope
cl /MD /O1 /Gy /DEBUG:NONE /nologo scope_global.c

REM Program 12: Static variables
cl /MD /O1 /Gy /DEBUG:NONE /nologo types4_staticvar.c

REM Program 13: Arrays and pointers
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_arrayptr.c

REM Program 14: Modification by reference
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_funcmod.c

REM Program 15: Structures
cl /MD /O1 /Gy /DEBUG:NONE /nologo pointers2_qsort.c
cl /MD /O1 /Gy /DEBUG:NONE /nologo structs2_commoninitseq.c

REM Program 16: File IO
cl /MD /O1 /Gy /DEBUG:NONE /nologo fileio_fwrite.c
cl /MD /O1 /Gy /DEBUG:NONE /nologo fileio_fread.c
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fread.c`

```c
#include <stdio.h>

int main(void)
{
    FILE *fp;
    unsigned char c;

    fp = fopen("output.bin", "rb"); // rb for "read binary"!

    while (fread(&c, sizeof(char), 1, fp) > 0)
        printf("%d\n", c);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/fileio_fwrite.c`

```c
#include <stdio.h>

int main(void)
{
    FILE *fp;
    unsigned char bytes[6] = {5, 37, 0, 88, 255, 12};

    fp = fopen("output.bin", "wb");  // wb mode for "write binary"!

    // In the call to fwrite, the arguments are:
    //
    // * Pointer to data to write
    // * Size of each "piece" of data
    // * Count of each "piece" of data
    // * FILE*

    fwrite(bytes, sizeof(char), 6, fp);

    fclose(fp);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/intro_hello.c`

```c
/* Hello world program */

#include <stdio.h>

int main(void)
{
    printf("Hello, World!\n");  // Actually do the work here
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/pointers2_qsort.c`

```c
#include <stdio.h>
#include <stdlib.h>

// The type of structure we're going to sort
struct animal {
    char *name;
    int leg_count;
};

// This is a comparison function called by qsort() to help it determine
// what exactly to sort by. We'll use it to sort an array of struct
// animals by leg_count.
int compar(const void *elem1, const void *elem2)
{
    // We know we're sorting struct animals, so let's make both
    // arguments pointers to struct animals
    const struct animal *animal1 = elem1;
    const struct animal *animal2 = elem2;

    // Return <0 =0 or >0 depending on whatever we want to sort by.

    // Let's sort ascending by leg_count, so we'll return the difference
    // in the leg_counts
    if (animal1->leg_count > animal2->leg_count)
        return 1;
    
    if (animal1->leg_count < animal2->leg_count)
        return -1;

    return 0;
}

int main(void)
{
    // Let's build an array of 4 struct animals with different
    // characteristics. This array is out of order by leg_count, but
    // we'll sort it in a second.
    struct animal a[4] = {
        {.name="Dog", .leg_count=4},
        {.name="Monkey", .leg_count=2},
        {.name="Antelope", .leg_count=4},
        {.name="Snake", .leg_count=0}
    };

    // Call qsort() to sort the array. qsort() needs to be told exactly
    // what to sort this data by, and we'll do that inside the compar()
    // function.
    //
    // This call is saying: qsort array a, which has 4 elements, and
    // each element is sizeof(struct animal) bytes big, and this is the
    // function that will compare any two elements.
    qsort(a, 4, sizeof(struct animal), compar);

    // Print them all out
    for (int i = 0; i < 4; i++) {
        printf("%d: %s\n", a[i].leg_count, a[i].name);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/scope_global.c`

```c
#include <stdio.h>

int shared = 10;    // File scope! Visible to the whole file after this!

void func1(void)
{
    shared += 100;  // Now shared holds 110
}

void func2(void)
{
    printf("%d\n", shared);  // Prints "110"
}

int main(void)
{
    func1();
    func2();
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/structs2_commoninitseq.c`

```c
#include <stdio.h>

struct common {
    int type;   // common initial sequence
};

struct antelope {
    int type;   // common initial sequence

    int loudness;
};

struct octopus {
    int type;   // common initial sequence

    int sea_creature;
    float intelligence;
};

union animal {
    struct common common;
    struct antelope antelope;
    struct octopus octopus;
};

#define ANTELOPE 1
#define OCTOPUS  2

void print_animal(union animal *x)
{
    switch (x->common.type) {
        case ANTELOPE:
            printf("Antelope: loudness=%d\n", x->antelope.loudness);
            break;

        case OCTOPUS:
            printf("Octopus : sea_creature=%d\n", x->octopus.sea_creature);
            printf("          intelligence=%f\n", x->octopus.intelligence);
            break;
        
        default:
            printf("Unknown animal type\n");
    }
}

int main(void)
{
    union animal a = {.antelope.type=ANTELOPE, .antelope.loudness=12};
    union animal b = {.octopus.type=OCTOPUS, .octopus.sea_creature=1,
                                       .octopus.intelligence=12.8};

    print_animal(&a);
    print_animal(&b);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/types4_staticvar.c`

```c
#include <stdio.h>

void counter(void)
{
    static int count = 1;  // This is initialized one time

    printf("This has been called %d time(s)\n", count);

    count++;
}

int main(void)
{
    counter();  // "This has been called 1 time(s)"
    counter();  // "This has been called 2 time(s)"
    counter();  // "This has been called 3 time(s)"
    counter();  // "This has been called 4 time(s)"
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_if.c`

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    bool x = true;

    if (x) {
        printf("x is true!\n");
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/var_stat_print.c`

```c
#include <stdio.h>

int main(void)
{
    int i = 2;
    float f = 3.14;
    char *s = "Hello, world!";  // char * ("char pointer") is the string type

    printf("%s  i = %d and f = %f!\n", s, i, f);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_do_while.c`

```c
#include <stdio.h>

int main(void)
{
    int r;
	
	do {
		r = rand() % 100;
		printf("%d\n",r);
	} while(r!=37);
	
	printf("All done!\n");
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_passfunc.c`

```c
#include <stdio.h>

int sum(int count, int *v)
{
    int total = 0;

    for (int i = 0; i < count; i++)
        total += v[i];

    return total;
}

int main(void)
{
    int x[5];   // Standard array
	int y[5];
	
    for (int i = 0; i < 5; i++)
        x[i] = y[i] = i + 1;

    printf("%d\n", sum(5, x));
    printf("%d\n", sum(5, y));
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_ptrarith.c`

```c
#include <stdio.h>

int main(void)
{
    int v[5];

    int *p = v;

    *(p+2) = 12;
    printf("%d\n", v[2]);  // 12

    p[3] = 34;
    printf("%d\n", v[3]);  // 34
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_switch.c`

```c
#include <stdio.h>

int main(void)
{
	int goat_count = 2;
	
	switch(goat_count) {
		case 0:
			printf("You have no goats.\n");
			break;
		case 1:
			printf("You have a singular goat.\n");
			break;
		case 2:
			printf("You have a brace of goats.\n");
			break;
		default:
			printf("You have a bona fide plethora of goats!\n");
			break;
	}
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_crt/wes_while.c`

```c
#include <stdio.h>

int main(void)
{
    int i = 0;
	
	while(i < 10) {
		printf("i is now %d!\n",i);
		i++;
	}
	
	printf("All done!\n");
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_2dinit.c`

```c
/* Nested loops with 2D arrays - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[128];
    int row, col;

    int a[2][5] = {      /* Initialize a 2D array */
        {0, 1, 2, 3, 4},
        {5, 6, 7, 8, 9}
    };

    for (row = 0; row < 2; row++) {
        for (col = 0; col < 5; col++) {
            wsprintfA(buf, "(%d,%d) = %d\n", row, col, a[row][col]);
            WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
        }
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_arrayptr.c`

```c
/* Arrays and pointers - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int a[5] = {11, 22, 33, 44, 55};
    int *p;

    /* p = &a[0];  // p points to the array
                  // Well, to the first element, actually */

    p = a;      /* p points to the array, but much nicer-looking!
                 * In C, an array name decays to a pointer to its first element */

    wsprintfA(buf, "%d\n", *p);   // Prints "11"
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_funcmod.c`

```c
/* Modification by reference - Windows API version */

#include <windows.h>

void double_array(int *a, int len)
{
    /* Multiple each element by 2.
     * This doubles the values in x in main() since x and a both point
     * to the same array in memory! */

    for (int i = 0; i < len; i++)
        a[i] *= 2;
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int x[5] = {1, 2, 3, 4, 5};

    double_array(x, 5);

    for (int i = 0; i < 5; i++) {
        wsprintfA(buf, "%d\n", x[i]);   // 2, 4, 6, 8, 10!
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/arrays_init.c`

```c
/* Flow control: for loop with arrays - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int i;
    int a[5] = {22, 37, 3490, 18, 95};   /* Initialize with these values */

    for (i = 0; i < 5; i++) {
        wsprintfA(buf, "%d\n", a[i]);
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/build_all.bat`

```bat
@echo off
REM ================================================================
REM Build script for Windows API reverse engineering workshop
REM Each program demonstrates replacing CRT functions with Win32 API
REM ================================================================

echo Building Windows API examples...
echo.

REM Program 1: Hello World - WriteConsoleA replaces printf
cl /MD /O1 /Gy /DEBUG:NONE /nologo intro_hello.c /link user32.lib

REM Program 2: Variables - int, float, and char* with wsprintfA
cl /MD /O1 /Gy /DEBUG:NONE /nologo var_stat_print.c /link user32.lib

REM Program 3: Pointer arithmetic
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_ptrarith.c /link user32.lib

REM Program 4: Flow control: if (BOOL/TRUE/FALSE instead of bool)
cl /MD /O1 /Gy /DEBUG:NONE /nologo var_stat_if.c /link user32.lib

REM Program 5: Flow control: while
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_while.c /link user32.lib

REM Program 6: Flow control: do/while (GetTickCount for pseudo-random)
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_do_while.c /link user32.lib

REM Program 7: For loop with arrays
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_init.c /link user32.lib

REM Program 8: Nested loops with 2D arrays
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_2dinit.c /link user32.lib

REM Program 9: Switch statement
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_switch.c /link user32.lib

REM Program 10: Functions (passing arrays by pointer)
cl /MD /O1 /Gy /DEBUG:NONE /nologo wes_passfunc.c /link user32.lib

REM Program 11: Global scope
cl /MD /O1 /Gy /DEBUG:NONE /nologo scope_global.c /link user32.lib

REM Program 12: Static variables
cl /MD /O1 /Gy /DEBUG:NONE /nologo types4_staticvar.c /link user32.lib

REM Program 13: Arrays and pointers
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_arrayptr.c /link user32.lib

REM Program 14: Modification by reference
cl /MD /O1 /Gy /DEBUG:NONE /nologo arrays_funcmod.c /link user32.lib

REM Program 15: Structures and sorting (bubble sort replaces qsort)
cl /MD /O1 /Gy /DEBUG:NONE /nologo pointers2_qsort.c /link user32.lib
cl /MD /O1 /Gy /DEBUG:NONE /nologo structs2_commoninitseq.c /link user32.lib

REM Program 16: File IO - CreateFile/WriteFile/ReadFile/CloseHandle
cl /MD /O1 /Gy /DEBUG:NONE /nologo fileio_fwrite.c /link user32.lib
cl /MD /O1 /Gy /DEBUG:NONE /nologo fileio_fread.c /link user32.lib

echo.
echo All done!
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/fileio_fread.c`

```c
/* File IO: reading binary data - Windows API version */
/* Replaces fopen/fread/fclose with CreateFile/ReadFile/CloseHandle */

#include <windows.h>

int main(void)
{
    HANDLE hFile;           /* Handle to the file */
    DWORD bytesRead;        /* Number of bytes actually read */
    unsigned char c;        /* Single byte buffer */

    /* CreateFileA opens the file for reading.
     * GENERIC_READ = we want read access
     * OPEN_EXISTING = file must already exist */
    hFile = CreateFileA("output.bin",
                        GENERIC_READ,       /* Desired access: read */
                        0,                  /* Share mode: exclusive */
                        NULL,               /* Security attributes */
                        OPEN_EXISTING,      /* Creation disposition: open existing file */
                        FILE_ATTRIBUTE_NORMAL,
                        NULL);

    if (hFile == INVALID_HANDLE_VALUE) {
        /* File not found or can't be opened - return error code */
        return 1;
    }

    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[16];

    /* ReadFile reads from the file. Returns FALSE when it reaches EOF.
     * We read one byte at a time (like fread with count=1). */
    while (ReadFile(hFile,        /* File handle */
                    &c,           /* Buffer to receive data */
                    sizeof(char), /* Number of bytes to read */
                    &bytesRead,   /* Receives actual bytes read */
                    NULL))        /* No overlapped I/O */
    {
        /* bytesRead > 0 means we got data; FALSE from ReadFile means EOF/error */
        wsprintfA(buf, "%d\n", c);
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
    }

    CloseHandle(hFile);   /* Close the file */
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/fileio_fwrite.c`

```c
/* File IO: writing binary data - Windows API version */
/* Replaces fopen/fwrite/fclose with CreateFile/WriteFile/CloseHandle */

#include <windows.h>

int main(void)
{
    HANDLE hFile;           /* Handle to the file (Win32 equivalent of FILE*) */
    DWORD bytesWritten;     /* Number of bytes actually written */
    unsigned char bytes[6] = {5, 37, 0, 88, 255, 12};

    /* CreateFileA is the Win32 equivalent of fopen.
     * On Windows, files are opened in binary mode by default (no "b" needed).
     * GENERIC_WRITE = we want to write to this file
     * CREATE_ALWAYS = create new file or overwrite existing one */
    hFile = CreateFileA("output.bin",
                        GENERIC_WRITE,      /* Desired access: write */
                        0,                  /* Share mode: 0 = exclusive (no other opens) */
                        NULL,               /* Security attributes: use defaults */
                        CREATE_ALWAYS,      /* Creation disposition: always create/overwrite */
                        FILE_ATTRIBUTE_NORMAL, /* File flags/attributes */
                        NULL);              /* Template file: none */

    if (hFile == INVALID_HANDLE_VALUE) {
        /* CreateFileA failed - return error code */
        return 1;
    }

    /* WriteFile is the Win32 equivalent of fwrite.
     * Arguments: handle, pointer to data, number of bytes to write,
     *            pointer to receive count written, OVERLAPPED (NULL for sync) */
    WriteFile(hFile,              /* File handle */
              bytes,              /* Pointer to data buffer */
              6,                  /* Number of bytes to write */
              &bytesWritten,      /* Receives actual bytes written */
              NULL);              /* No overlapped I/O */

    CloseHandle(hFile);   /* Close the file - equivalent of fclose() */
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/intro_hello.c`

```c
/* Hello world program - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);  // Get console output handle
    DWORD written;                                   // Bytes actually written
    char msg[] = "Hello, World!\n";                  // Null-terminated string

    /* WriteConsoleA writes a string to the console.
     * Arguments: handle, pointer to string, length in bytes,
     *            pointer to receive count written, reserved (NULL) */
    WriteConsoleA(hOut, msg, (DWORD)lstrlenA(msg), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/pointers2_qsort.c`

```c
/* Structures and sorting - Windows API version */
/* Note: qsort() is a CRT function with no direct Win32 equivalent.
 * We implement a simple bubble sort to demonstrate the concept without
 * relying on library functions. This is what you'd actually do in
 * kernel-mode or highly constrained Windows code. */

#include <windows.h>

// The type of structure we're going to sort
struct animal {
    const char *name;
    int leg_count;
};

/* Comparison function: returns <0, 0, or >0 for sorting order.
 * Same concept as the qsort compar() function, but we call it ourselves. */
int compar(const struct animal *animal1, const struct animal *animal2)
{
    if (animal1->leg_count > animal2->leg_count)
        return 1;

    if (animal1->leg_count < animal2->leg_count)
        return -1;

    return 0;
}

/* Bubble sort implementation - no library dependency */
void bubble_sort(struct animal *arr, int count)
{
    int i, j;
    struct animal temp;

    for (i = 0; i < count - 1; i++) {
        for (j = 0; j < count - i - 1; j++) {
            if (compar(&arr[j], &arr[j + 1]) > 0) {
                /* Swap arr[j] and arr[j+1] */
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[128];

    // Build an array of 4 struct animals with different characteristics.
    // This array is out of order by leg_count, but we'll sort it next.
    struct animal a[4] = {
        {"Dog", 4},
        {"Monkey", 2},
        {"Antelope", 4},
        {"Snake", 0}
    };

    // Sort the array using our bubble_sort() instead of qsort()
    bubble_sort(a, 4);

    // Print them all out
    for (int i = 0; i < 4; i++) {
        wsprintfA(buf, "%d: %s\n", a[i].leg_count, a[i].name);
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/scope_global.c`

```c
/* Global scope - Windows API version */

#include <windows.h>

int shared = 10;    /* File scope! Visible to the whole file after this! */

void func1(void)
{
    shared += 100;  /* Now shared holds 110 */
}

void func2(HANDLE hOut, DWORD *written)
{
    char buf[64];
    wsprintfA(buf, "%d\n", shared);   // Prints "110"
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), written, NULL);
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;

    func1();
    func2(hOut, &written);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/structs2_commoninitseq.c`

```c
/* Structures: common initial sequence in unions - Windows API version */

#include <windows.h>

struct common {
    int type;   /* common initial sequence */
};

struct antelope {
    int type;   /* common initial sequence */

    int loudness;
};

struct octopus {
    int type;   /* common initial sequence */

    int sea_creature;
    float intelligence;
};

union animal {
    struct common common;
    struct antelope antelope;
    struct octopus octopus;
};

#define ANTELOPE 1
#define OCTOPUS  2

void print_animal(union animal *x, HANDLE hOut, DWORD *written)
{
    char buf[256];

    switch (x->common.type) {
        case ANTELOPE:
            wsprintfA(buf, "Antelope: loudness=%d\n", x->antelope.loudness);
            WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), written, NULL);
            break;

        case OCTOPUS:
            wsprintfA(buf, "Octopus : sea_creature=%d\n", x->octopus.sea_creature);
            WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), written, NULL);
            wsprintfA(buf, "          intelligence=%f\n", x->octopus.intelligence);
            WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), written, NULL);
            break;

        default:
            WriteConsoleA(hOut, "Unknown animal type\n", 21, written, NULL);
    }
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;

    union animal a = {.antelope.type = ANTELOPE, .antelope.loudness = 12};
    union animal b = {.octopus.type = OCTOPUS, .octopus.sea_creature = 1,
                                      .octopus.intelligence = 12.8f};

    print_animal(&a, hOut, &written);
    print_animal(&b, hOut, &written);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/types4_staticvar.c`

```c
/* Static variables - Windows API version */

#include <windows.h>

void counter(HANDLE hOut, DWORD *written)
{
    static int count = 1;   /* Initialized only once, persists across calls */

    char buf[128];
    wsprintfA(buf, "This has been called %d time(s)\n", count);
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), written, NULL);

    count++;
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;

    counter(hOut, &written);  // "This has been called 1 time(s)"
    counter(hOut, &written);  // "This has been called 2 time(s)"
    counter(hOut, &written);  // "This has been called 3 time(s)"
    counter(hOut, &written);  // "This has been called 4 time(s)"
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/var_stat_if.c`

```c
/* Flow control: if - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    BOOL x = TRUE;   /* BOOL is Win32's boolean type (int, 0 or non-zero) */

    if (x) {
        char msg[] = "x is true!\n";
        WriteConsoleA(hOut, msg, (DWORD)lstrlenA(msg), &written, NULL);
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/var_stat_print.c`

```c
/* Variables - int, float, and char* - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[256];

    int i = 2;
    float f = 3.14f;
    const char *s = "Hello, world!";   // char* is the string type on Windows too

    /* wsprintfA is the Win32 equivalent of sprintf - formats into a buffer */
    wsprintfA(buf, "%s  i = %d and f = %f!\n", s, i, f);

    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/wes_do_while.c`

```c
/* Flow control: do/while - Windows API version */
/* Note: rand() is replaced with GetTickCount() % 100 as a pseudo-random source.
 * There is no simple Win32 API equivalent to the CRT's rand().
 * GetTickCount() returns milliseconds since system start - useful for rough randomness. */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int r;

    do {
        r = (int)(GetTickCount() % 100);   /* Pseudo-random using system tick count */
        wsprintfA(buf, "%d\n", r);
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
    } while (r != 37);

    char msg[] = "All done!\n";
    WriteConsoleA(hOut, msg, (DWORD)lstrlenA(msg), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/wes_passfunc.c`

```c
/* Functions - passing arrays by pointer - Windows API version */

#include <windows.h>

int sum(int count, int *v)
{
    int total = 0;

    for (int i = 0; i < count; i++)
        total += v[i];

    return total;
}

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int x[5];
    int y[5];

    for (int i = 0; i < 5; i++)
        x[i] = y[i] = i + 1;

    wsprintfA(buf, "%d\n", sum(5, x));
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);

    wsprintfA(buf, "%d\n", sum(5, y));
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/wes_ptrarith.c`

```c
/* Pointer arithmetic - Windows API version */

#include <windows.h>

int main(void)
{
    DWORD v[5];     /* DWORD = 32-bit unsigned int, standard Win32 type */

    DWORD *p = v;   /* p points to the start of array v */

    *(p + 2) = 12;  /* Dereference p+2 and store 12.
                     * Pointer arithmetic: p+2 advances by 2*sizeof(DWORD) bytes */
    char buf[64];
    wsprintfA(buf, "%d\n", v[2]);   // Prints "12"

    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);

    p[3] = 34;  /* Array-style dereference: same as *(p + 3) */
    wsprintfA(buf, "%d\n", v[3]);   // Prints "34"
    WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/wes_switch.c`

```c
/* Flow control: switch - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    int goat_count = 2;

    switch (goat_count) {
        case 0:
            WriteConsoleA(hOut, "You have no goats.\n", 21, &written, NULL);
            break;
        case 1:
            WriteConsoleA(hOut, "You have a singular goat.\n", 25, &written, NULL);
            break;
        case 2:
            WriteConsoleA(hOut, "You have a brace of goats.\n", 26, &written, NULL);
            break;
        default:
            WriteConsoleA(hOut, "You have a bona fide plethora of goats!\n", 41, &written, NULL);
            break;
    }
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/examples_win/wes_while.c`

```c
/* Flow control: while - Windows API version */

#include <windows.h>

int main(void)
{
    HANDLE hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    DWORD written;
    char buf[64];
    int i = 0;

    while (i < 10) {
        wsprintfA(buf, "i is now %d!\n", i);
        WriteConsoleA(hOut, buf, (DWORD)lstrlenA(buf), &written, NULL);
        i++;
    }

    char msg[] = "All done!\n";
    WriteConsoleA(hOut, msg, (DWORD)lstrlenA(msg), &written, NULL);
}
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_1_and_2/simple.asm`

```asm
; Module 1
;
; ml64 simple.asm /link /subsystem:windows

.data

; Placing some arbitrary values into memory, so we can view them in
; x64dbg and manipulate them

bytes		db	23, -40, 0a3h, 01100110b, 'a', 'deadbeef', 0
words		dw	0, -40, 0d3adh
dwords	dd 0deadbeefh, 40, -40
qwords   dq 0c000f000bbbb1234h, -40

.data?

temp_byte	db 	?
temp_word	dw		?
temp_dword	dd		?
temp_qword	dq		?

.code

WinMainCRTStartup proc
	; Move the data into rax. we'll patch the addresses and move RIP
	; around live to demonstrate x64dbg while we're at it.
	mov al, bytes[0]
	; mov temp_byte, bytes[0] <-- can't do this, not one of the valid
	;                             forms of mov!
	mov temp_byte, al
	mov ax, words[0]
	mov temp_word, ax
	mov eax, dwords[0]
	mov temp_dword, eax
	mov rax, qwords[0]
	mov temp_qword, rax	

	; Register-to-register movement
	mov rbx, rax
	
	ret
WinMainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/hello.asm`

```asm
; Module 3 - Hello World
;
; ml64 hello.asm /link /subsystem:windows
;----------------------------------------------------------------------

includelib kernel32.lib
includelib user32.lib

extern ExitProcess: PROC
extern MessageBoxA: PROC

HWND_DESKTOP	equ	0
MB_OK				equ	0

;----------------------------------------------------------------------
.data

helloworld	db	'hello cruel world',00h

;----------------------------------------------------------------------
.code

WinMainCRTStartup proc
	push 	rbp							; Save the old base pointer
	mov 	rbp,rsp						; Set a new base pointer
		
	mov	rcx, HWND_DESKTOP		
	mov	rdx, OFFSET helloworld	; lpText
	mov	r8, OFFSET helloworld	; lpCaption
	mov	r9d, MB_OK
	sub	rsp, 20h						; shadow space
	call	MessageBoxA				 
		
	mov	rcx, rax						; use MessageBox return value
	call	ExitProcess
	mov	rsp, rbp
	pop	rbp
	ret
WinMainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_3/write.asm`

```asm
; Module 3 - Hello World (Console)
;
; ml64 write.asm /link /subsystem:console
;---------------------------------------------------------------------

includelib kernel32.lib

extern ExitProcess:		PROC
extern GetStdHandle: 	PROC
extern WriteConsoleA:	PROC

STD_OUTPUT_HANDLE	equ -11
NULL					equ 0

;----------------------------------------------------------------------
.data

helloworld	db	'hello cruel world',0Ah,00h

;----------------------------------------------------------------------
.code

mainCRTStartup proc
	push 	rbp							; Save the old base pointer
	mov 	rbp, rsp						; Set a new base pointer
		
	push	0								; Allocate local space to get 
											; number of characters written
	mov	rbx, rsp
	and 	rsp, -10h

	mov	rcx, STD_OUTPUT_HANDLE
	sub	rsp, 20h
	call	GetStdHandle
	add	rsp, 20h
	
	push	NULL
	and 	rsp, -10h
	mov	r9, rbx
	mov	r8, 18
	mov	rdx, OFFSET helloworld
	mov	rcx, rax
	sub	rsp, 20h
	call	WriteConsoleA
	add	rsp, 30h
	
	mov	ecx,eax						; use MessageBox return value
	sub	rsp, 20h
	call	ExitProcess
	mov	rsp, rbp
	pop	rbp
	ret
mainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_4/data.asm`

```asm
; Module 4 - Data
;
; ml64 data.asm /link /subsystem:windows
;----------------------------------------------------------------------

includelib kernel32.lib

extern ExitProcess: PROC

;----------------------------------------------------------------------
.const

port			dw		31377

;----------------------------------------------------------------------
.data

global_var	dq		0h
bytes			db		011h, 022h, 033h, 044h, 055h, 066h, 077h, 088h
n				dq		-3289,-2883,22214,-758324

;----------------------------------------------------------------------

.data?

p				dw		6000 dup(?)

;----------------------------------------------------------------------
.code

WinMainCRTStartup proc 
	local a:qword      ; MASM inserts a function prologue and epilogue
	local k:word
	local b[4]:byte
	
	; Register and immediate addressing
	mov	rax, 42
	
	; RIP-Relative (check the instruction decoding in the debugger)
	mov	global_var, rax
	
	; Register indirect
	lea	rax, global_var
	mov	rbx, 420
	mov	[rax], rbx
	
	; Offset (Base + Displacement)
	lea	rbx, bytes
	mov	rax, [rbx+3]
	
	; Offset (Base + (Index * Scale))
	lea	rbx, n
	mov	rcx, 3
	mov	rax, [rbx + rcx * 8]
	
	; Offset (Base + (Index * Scale) + Displacement)
	mov	rax, 0h
	mov	ax, [rbx + rcx * 8 + 2]
	
	; Local and uninitialized (note file size)
	mov	ax, port
	mov	k, ax
	mov	bx, k
	mov	p[0], bx
	mov   p[5999], bx
	
	mov	rcx, 0						
	call	ExitProcess
	ret
WinMainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_5/math.asm`

```asm
; Module 5 - Integer Math and Bitwise Operations
;
; ml64 math.asm /link /subsystem:windows
;----------------------------------------------------------------------

includelib kernel32.lib

extern ExitProcess: PROC

;----------------------------------------------------------------------
.data


;----------------------------------------------------------------------
.code

WinMainCRTStartup proc
	push 	rbp
	mov 	rbp,rsp
	
	; Simple arithmetic
	
	; Addition
	mov	rax, 20
	mov	rbx, 30
	add	rax, rbx
	
	; Subtraction
	mov	rax, 40
	mov	rbx, 35
	sub	rax, rbx
	
	; Multiplication
	mov	rdx, -1
	mov	rax, -849
	mov	rbx, 7
	imul	rbx
	
	; Division/Modulo
	mov	rdx, 0
	mov	rax, 100
	mov	rbx, 31
	div	rbx
	
	; Logic operations
	
	; AND
	mov	rax, 0F0F0h
	and	rax, 00FF0h
	
	; OR
	mov	rax, 0FFF0h
	or		rax, 00F0Fh
	
	; XOR
	mov	rax, 12345678h
	xor	rax, 9ABCDEF0h
	xor	rax, rax
	
	; Shift Left
	mov	rax, 16
	shl	rax, 4
	
	; Shift Right
	mov	rax, 64
	shr	rax, 3
		
	mov	rcx, rax	
	call	ExitProcess
	mov	rsp, rbp
	pop	rbp
	ret
WinMainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_6/control.asm`

```asm
; Module 6 - Control Structures
;
; ml64 control.asm /link /subsystem:windows
;----------------------------------------------------------------------

includelib kernel32.lib

extern ExitProcess: PROC

;----------------------------------------------------------------------
.data


;----------------------------------------------------------------------
.code

WinMainCRTStartup proc
				push 	rbp
				mov 	rbp,rsp
	
				; If/Else
	
				mov	rax, 12
				cmp	rax, 30
				jnl	_else
				; Execute this if rax < 30
				mov	rbx, 1
				jmp	_endif
_else:		; Else if !(rax < 30)
				mov	rbx, 2
_endif:
			
				; While
beginwhile:	cmp	rax, 30
				jl		endwhile	  ; Test
				; body
				add	rax, 3
				; end body
				jmp 	beginwhile ; Loop
endwhile:	

				; Exercise for reader: Make a do-while loop
				
				; For loop
				mov	rcx, 0	  ; Initialize
f_test:		cmp	rcx, 30	  ; Test
				jnl	f_end		  ;
				; body
				nop
				; end body
				inc	rcx		  ; Iterate
				jmp	f_test	  ; Loop
f_end:
	
				mov	rcx, rax	
				call	ExitProcess
				mov	rsp, rbp
				pop	rbp
				ret
WinMainCRTStartup endp

END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/resources/dc33_x64_workshop/module_7/download.asm`

```asm
; Module 7 - Capstone: Downloader
;
; ml64 download.asm /link /subsystem:windows
;----------------------------------------------------------------------
includelib kernel32.lib

extern	LoadLibraryA:		PROC
extern	GetProcAddress:	PROC
extern	ExitProcess:		PROC

NULL	equ	0

;----------------------------------------------------------------------
.data

; Our obfuscation (XOR with 0AAh repeating) is commutative, so we
; can use our obfuscation function to get the correct obfuscated bytes
; to store in the working version of the program.\						

;s_urlmon_dll				db "urlmon.dll",0
s_urlmon_dll				db 0DFh,0D8h,0C6h,0C7h,0C5h,0C4h,084h,0CEh
								db 0C6h,0C6h,0
;s_URLDownloadToFileA	db	"URLDownloadToFileA",0
s_URLDownloadToFileA		db 0FFh,0F8h,0E6h,0EEh,0C5h,0DDh,0C4h,0C6h
								db 0C5h,0CBh,0CEh,0FEh,0C5h,0ECh,0C3h,0C6h
								db 0CFh,0EBh,0
;url							db "https://wttr.in/las%20vegas?ATF",0
url							db 0C2h,0DEh,0DEh,0DAh,0D9h,090h,085h,085h
								db 0DDh,0DEh,0DEh,0D8h,084h,0C3h,0C4h,085h
								db 0C6h,0CBh,0D9h,08Fh,098h,09Ah,0DCh,0CFh
								db 0CDh,0CBh,0D9h,095h,0EBh,0FEh,0ECh,0
;filename					db	"vegas_wx.txt",0
filename						db	0DCh,0CFh,0D9h,0F5h,0DDh,0D2h,084h,0DEh
								db 0D2h,0DEh,0

;----------------------------------------------------------------------
.data?

; Populated from GetProcAddress
URLDownloadToFileA		dq	?

;----------------------------------------------------------------------
.code

; deobfuscate: XOR's a null-terminated string (provided in RCX as the
; first argument) in-place in memory.
deobfuscate	proc
		push	rbp
		mov	rbp,rsp
		push	rdi				; These are non-volatile in the calling 
		push	rbx				; convention, so we save them
			
		mov	rdi, rcx			; RDI - Base address of the string
		xor	rcx, rcx			; ECX - Position in the string = 0
		xor	rbx, rbx			; We'll store individual chars here
	
L1:	mov	bl, [rdi+rcx]	; Load a character into BL
		test	bl, bl			; If bl == 0, exit the loop
		jz		L2
		xor	bl, 0AAh			; XOR BL with 0AAh
		mov	[rdi+rcx], bl  ; Store the character back
		inc	rcx
		jmp	L1
			
L2:	xor	rax, rax			; We'll only ever return NULL 
		pop 	rbx				; Restoring these two registers
		pop	rdi				;  in the opposite order
		mov	rsp, rbp
		pop	rbp
		ret
deobfuscate	endp

; Here we deobfuscate all in one place, but if you'd like to
; be clever, you could do it right before you use each of them
; (and even re-obfuscate them after use with the same function)
deobfuscate_strings	proc
		push	rbp
		mov	rbp,rsp
		sub	rsp, 20h
			
		lea	rcx, s_urlmon_dll
		call	deobfuscate
		lea	rcx, s_URLDownloadToFileA
		call	deobfuscate
		lea	rcx, url
		call	deobfuscate
		lea	rcx, filename
		call	deobfuscate
			
		mov	rsp, rbp
		pop	rbp
		ret
deobfuscate_strings	endp

resolve_functions	proc
		push	rbp
		mov	rbp,rsp
		push	NULL ; Alignment
		push	rbx
		
		lea	rcx, s_urlmon_dll
		sub	rsp, 20h
		call	LoadLibraryA
		mov	rbx, rax
			
		lea	rdx, s_URLDownloadToFileA
		mov	rcx, rbx						
		call	GetProcAddress
		mov	URLDownloadToFileA, rax
			
		pop 	rbx
		mov	rsp, rbp
		pop	rbp
		ret
resolve_functions	endp

download_data proc
		push	rbp
		mov	rbp,rsp		

		push  NULL ; Alignment
		push	NULL
		mov	r9, 0
		lea	r8, filename
		lea	rdx, url
		mov	rcx, NULL
		sub	rsp, 20h
		call 	URLDownloadToFileA
			
		mov	rsp, rbp
		pop	rbp
		ret
download_data endp


WinMainCRTStartup proc
		push 	rbp
		mov 	rbp, rsp
		sub	rsp, 20h
			
		call	deobfuscate_strings
		call	resolve_functions
		call	download_data
			
		xor	eax, eax
		call	ExitProcess
			
		mov	rsp, rbp
		pop	rbp
		ret
WinMainCRTStartup endp
END
```

### `DEF CON 34 - Workshops - Wes McGrew - Learning to Reverse Engineer Compiled C as We Learn to Write It - DEF CON 34 workshop learning reversing/dc34_workshop_learning_reversing_c/windows_types.md`

````markdown
---
layout: Conceptual
title: Windows Data Types (BaseTsd.h) - Win32 apps | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/windows/win32/winprog/windows-data-types
breadcrumb_path: /windows/desktop/breadcrumb/toc.json
uhfHeaderId: MSDocsHeader-WinDevCenter
recommendations: true
adobe-target: true
ms.service: windows-api-desktop-tech
ms.subservice: get-started
ms.author: stwhi
author: stevewhims
feedback_system: Standard
feedback_product_url: https://www.microsoft.com/en-us/windowsinsider/feedbackhub/fb
feedback_help_link_url: https://learn.microsoft.com/answers/tags/224/windows-api-win32/
feedback_help_link_type: get-help-at-qna
description: The data types supported by Windows are used to define function return values, function and message parameters, and structure members.
ms.assetid: 4553cafc-450e-4493-a4d4-cb6e2f274d46
keywords:
- data types
- data types,Windows
- Windows API
- Windows API,data types
- APIENTRY
- ATOM
- BOOL
- BOOLEAN
- BYTE
- CALLBACK
- CCHAR
- CHAR
- COLORREF
- CONST
- DWORD
- DWORDLONG
- DWORD_PTR
- DWORD32
- DWORD64
- FLOAT
- HACCEL
- HALF_PTR
- HANDLE
- HBITMAP
- HBRUSH
- HCOLORSPACE
- HCONV
- HCONVLIST
- HCURSOR
- HDC
- HDDEDATA
- HDESK
- HDROP
- HDWP
- HENHMETAFILE
- HFILE
- HFONT
- HGDIOBJ
- HGLOBAL
- HHOOK
- HICON
- HINSTANCE
- HKEY
- HKL
- HLOCAL
- HMENU
- HMETAFILE
- HMODULE
- HMONITOR
- HPALETTE
- HPEN
- HRESULT
- HRGN
- HRSRC
- HSZ
- HWINSTA
- HWND
- INT
- INT_PTR
- INT8
- INT16
- INT32
- INT64
- LANGID
- LCID
- LCTYPE
- LGRPID
- LONG
- LONGLONG
- LONG_PTR
- LONG32
- LONG64
- LPARAM
- LPBOOL
- LPBYTE
- LPCOLORREF
- LPCSTR
- LPCTSTR
- LPCVOID
- LPCWSTR
- LPDWORD
- LPHANDLE
- LPINT
- LPLONG
- LPSTR
- LPTSTR
- LPVOID
- LPWORD
- LPWSTR
- LRESULT
- PBOOL
- PBOOLEAN
- PBYTE
- PCHAR
- PCSTR
- PCTSTR
- PCWSTR
- PDWORD
- PDWORDLONG
- PDWORD_PTR
- PDWORD32
- PDWORD64
- PFLOAT
- PHALF_PTR
- PHANDLE
- PHKEY
- PINT
- PINT_PTR
- PINT8
- PINT16
- PINT32
- PINT64
- PLCID
- PLONG
- PLONGLONG
- PLONG_PTR
- PLONG32
- PLONG64
- POINTER_32
- POINTER_64
- POINTER_SIGNED
- POINTER_UNSIGNED
- PSHORT
- PSIZE_T
- PSSIZE_T
- PSTR
- PTBYTE
- PTCHAR
- PTSTR
- PUCHAR
- PUHALF_PTR
- PUINT
- PUINT_PTR
- PUINT8
- PUINT16
- PUINT32
- PUINT64
- PULONG
- PULONGLONG
- PULONG_PTR
- PULONG32
- PULONG64
- PUSHORT
- PVOID
- PWCHAR
- PWORD
- PWSTR
- QWORD
- SC_HANDLE
- SC_LOCK
- SERVICE_STATUS_HANDLE
- SHORT
- SIZE_T
- SSIZE_T
- TBYTE
- TCHAR
- UCHAR
- UHALF_PTR
- UINT
- UINT_PTR
- UINT8
- UINT16
- UINT32
- UINT64
- ULONG
- ULONGLONG
- ULONG_PTR
- ULONG32
- ULONG64
- UNICODE_STRING
- USHORT
- USN
- VOID
- WCHAR
- WINAPI
- WORD
- WPARAM
ms.topic: reference
ms.date: 2024-11-07T00:00:00.0000000Z
locale: en-us
document_id: d2d19b47-898d-b607-6181-70078bfa7f2f
document_version_independent_id: cf2919a4-c2a4-ca34-3dbc-67c7e1334b3e
updated_at: 2024-12-05T09:27:00.0000000Z
original_content_git_url: https://github.com/MicrosoftDocs/win32-pr/blob/live/desktop-src/WinProg/windows-data-types.md
gitcommit: https://github.com/MicrosoftDocs/win32-pr/blob/92ebc38efa0c9b01a1979100de70801891c0162f/desktop-src/WinProg/windows-data-types.md
git_commit_id: 92ebc38efa0c9b01a1979100de70801891c0162f
site_name: Docs
depot_name: MSDN.win32
page_type: conceptual
toc_rel: toc.json
pdf_url_template: https://learn.microsoft.com/pdfstore/en-us/MSDN.win32/{branchName}{pdfName}
word_count: 3967
asset_id: winprog/windows-data-types
moniker_range_name: 
monikers: []
item_type: Content
source_path: desktop-src/WinProg/windows-data-types.md
cmProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/bcbcbad5-4208-4783-8035-8481272c98b8
- https://authoring-docs-microsoft.poolparty.biz/devrel/540ac133-a371-4dbb-8f94-28d6cc77a70b
spProducts:
- https://authoring-docs-microsoft.poolparty.biz/devrel/43b2e5aa-8a6d-4de2-a252-692232e5edc8
- https://authoring-docs-microsoft.poolparty.biz/devrel/60bfc045-f127-4841-9d00-ea35495a5800
platformId: 41176de5-97f8-9485-e49f-a1eb64a939dc
---

# Windows Data Types (BaseTsd.h) - Win32 apps | Microsoft Learn

The data types supported by Windows are used to define function return values, function and message parameters, and structure members. They define the size and meaning of these elements. For more information about the underlying C/C++ data types, see [Data Type Ranges](/en-us/cpp/cpp/data-type-ranges).

The following table contains the following types: character, integer, Boolean, pointer, and handle. The character, integer, and Boolean types are common to most C compilers. Most of the pointer-type names begin with a prefix of P or LP. Handles refer to a resource that has been loaded into memory.

For more information about handling 64-bit integers, see [Large Integers](large-integers).

| Data type | Description |
| --- | --- |
| `APIENTRY` | The calling convention for system functions. This type is declared in WinDef.h as follows:`#define APIENTRY WINAPI` |
| `ATOM` | An atom. For more information, see [About Atom Tables](/en-us/windows/desktop/dataxchg/about-atom-tables). This type is declared in WinDef.h as follows:`typedef WORD ATOM;` |
| `BOOL` | A Boolean variable (should be **TRUE** or **FALSE**). This type is declared in WinDef.h as follows:`typedef int BOOL;` |
| `BOOLEAN` | A Boolean variable (should be **TRUE** or **FALSE**). This type is declared in WinNT.h as follows:`typedef BYTE BOOLEAN;` |
| `BYTE` | A byte (8 bits). This type is declared in WinDef.h as follows:`typedef unsigned char BYTE;` |
| `CALLBACK` | The calling convention for callback functions. This type is declared in WinDef.h as follows:`#define CALLBACK __stdcall`**CALLBACK**, **WINAPI**, and **APIENTRY** are all used to define functions with the \_\_stdcall calling convention. Most functions in the Windows API are declared using **WINAPI**. You may wish to use **CALLBACK** for the callback functions that you implement to help identify the function as a callback function. |
| `CCHAR` | An 8-bit Windows (ANSI) character. This type is declared in WinNT.h as follows:`typedef char CCHAR;` |
| `CHAR` | An 8-bit Windows (ANSI) character. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts). This type is declared in WinNT.h as follows:`typedef char CHAR;` |
| `COLORREF` | The red, green, blue (RGB) color value (32 bits). See [**COLORREF**](/en-us/windows/desktop/gdi/colorref) for information on this type. This type is declared in WinDef.h as follows:`typedef DWORD COLORREF;` |
| `CONST` | A variable whose value is to remain constant during execution.  This type is declared in WinDef.h as follows:`#define CONST const` |
| `DWORD` | A 32-bit unsigned integer. The range is 0 through 4294967295 decimal. This type is declared in IntSafe.h as follows:`typedef unsigned long DWORD;` |
| `DWORDLONG` | A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal. This type is declared in IntSafe.h as follows:`typedef unsigned __int64 DWORDLONG;` |
| `DWORD_PTR` | An unsigned long type for pointer precision. Use when casting a pointer to a long type to perform pointer arithmetic. (Also commonly used for general 32-bit parameters that have been extended to 64 bits in 64-bit Windows.) This type is declared in BaseTsd.h as follows:`typedef ULONG_PTR DWORD_PTR;` |
| `DWORD32` | A 32-bit unsigned integer. This type is declared in BaseTsd.h as follows:`typedef unsigned int DWORD32;` |
| `DWORD64` | A 64-bit unsigned integer. This type is declared in BaseTsd.h as follows:`typedef unsigned __int64 DWORD64;` |
| `FLOAT` | A floating-point variable. This type is declared in WinDef.h as follows:`typedef float FLOAT;` |
| `HACCEL` | A handle to an [accelerator table](/en-us/windows/desktop/menurc/keyboard-accelerators). This type is declared in WinDef.h as follows:`typedef HANDLE HACCEL;` |
| `HALF_PTR` | Half the size of a pointer. Use within a structure that contains a pointer and two small fields. This type is declared in BaseTsd.h as follows:<br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef _WIN64<br> typedef int HALF_PTR;<br>#else<br> typedef short HALF_PTR;<br>#endif<br>``` | |
| --- | --- |
| `HANDLE` | A handle to an object.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef PVOID HANDLE;` |
| `HBITMAP` | A handle to a [bitmap](/en-us/windows/desktop/gdi/bitmaps).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HBITMAP;` |
| `HBRUSH` | A handle to a [brush](/en-us/windows/desktop/gdi/brushes).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HBRUSH;` |
| `HCOLORSPACE` | A handle to a [color space](/en-us/previous-versions//dd316799%28v=vs.85%29).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HCOLORSPACE;` |
| `HCONV` | A handle to a dynamic data exchange (DDE) conversation.<br><br>This type is declared in Ddeml.h as follows:<br><br>`typedef HANDLE HCONV;` |
| `HCONVLIST` | A handle to a DDE conversation list.<br><br>This type is declared in Ddeml.h as follows:<br><br>`typedef HANDLE HCONVLIST;` |
| `HCURSOR` | A handle to a [cursor](/en-us/windows/desktop/menurc/cursors).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HICON HCURSOR;` |
| `HDC` | A handle to a [device context](/en-us/windows/desktop/gdi/device-context-types) (DC).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HDC;` |
| `HDDEDATA` | A handle to DDE data.<br><br>This type is declared in Ddeml.h as follows:<br><br>`typedef HANDLE HDDEDATA;` |
| `HDESK` | A handle to a [desktop](/en-us/windows/desktop/winstation/desktops).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HDESK;` |
| `HDROP` | A handle to an internal drop structure.<br><br>This type is declared in ShellApi.h as follows:<br><br>`typedef HANDLE HDROP;` |
| `HDWP` | A handle to a deferred window position structure.<br><br>This type is declared in WinUser.h as follows:<br><br>`typedef HANDLE HDWP;` |
| `HENHMETAFILE` | A handle to an [enhanced metafile](/en-us/windows/desktop/gdi/metafiles).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HENHMETAFILE;` |
| `HFILE` | A handle to a file opened by [**OpenFile**](/en-us/windows/desktop/api/winbase/nf-winbase-openfile), not [**CreateFile**](/en-us/windows/desktop/api/fileapi/nf-fileapi-createfilea).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef int HFILE;` |
| `HFONT` | A handle to a [font](/en-us/windows/desktop/gdi/about-fonts).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HFONT;` |
| `HGDIOBJ` | A handle to a GDI object.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HGDIOBJ;` |
| `HGLOBAL` | A handle to a global memory block.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HGLOBAL;` |
| `HHOOK` | A handle to a [hook](/en-us/windows/desktop/winmsg/hooks).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HHOOK;` |
| `HICON` | A handle to an [icon](/en-us/windows/desktop/menurc/icons).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HICON;` |
| `HINSTANCE` | A handle to an instance. This is the base address of the module in memory.<br><br>**HMODULE** and **HINSTANCE** are the same today, but represented different things in 16-bit Windows.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HINSTANCE;` |
| `HKEY` | A handle to a registry key.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HKEY;` |
| `HKL` | An input locale identifier.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HKL;` |
| `HLOCAL` | A handle to a local memory block.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HLOCAL;` |
| `HMENU` | A handle to a [menu](/en-us/windows/desktop/menurc/menus).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HMENU;` |
| `HMETAFILE` | A handle to a [metafile](/en-us/windows/desktop/gdi/metafiles).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HMETAFILE;` |
| `HMODULE` | A handle to a module. This is the base address of the module in memory.<br><br>**HMODULE** and **HINSTANCE** are the same in current versions of Windows, but represented different things in 16-bit Windows.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HINSTANCE HMODULE;` |
| `HMONITOR` | A handle to a display monitor.<br><br>This type is declared in WinDef.h as follows:<br><br>`if(WINVER >= 0x0500) typedef HANDLE HMONITOR;` |
| `HPALETTE` | A handle to a palette.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HPALETTE;` |
| `HPEN` | A handle to a [pen](/en-us/windows/desktop/gdi/pens).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HPEN;` |
| `HRESULT` | The return codes used by COM interfaces. For more information, see [Structure of the COM Error Codes](/en-us/windows/desktop/com/structure-of-com-error-codes). To test an **HRESULT** value, use the [**FAILED**](/en-us/windows/desktop/api/winerror/nf-winerror-failed) and [**SUCCEEDED**](/en-us/windows/desktop/api/winerror/nf-winerror-succeeded) macros.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef LONG HRESULT;` |
| `HRGN` | A handle to a [region](/en-us/windows/desktop/gdi/regions).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HRGN;` |
| `HRSRC` | A handle to a resource.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HRSRC;` |
| `HSZ` | A handle to a DDE string.<br><br>This type is declared in Ddeml.h as follows:<br><br>`typedef HANDLE HSZ;` |
| `HWINSTA` | A handle to a [window station](/en-us/windows/desktop/winstation/window-stations).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE WINSTA;` |
| `HWND` | A handle to a [window](/en-us/windows/desktop/winmsg/windows).<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE HWND;` |
| `INT` | A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef int INT;` |
| `INT_PTR` | A signed integer type for pointer precision. Use when casting a pointer to an integer to perform pointer arithmetic.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if defined(_WIN64) <br> typedef __int64 INT_PTR; <br>#else <br> typedef int INT_PTR;<br>#endif<br>``` | |
| --- | --- |
| `INT8` | An 8-bit signed integer.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef signed char INT8;` |
| `INT16` | A 16-bit signed integer.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef signed short INT16;` |
| `INT32` | A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef signed int INT32;` |
| `INT64` | A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef signed __int64 INT64;` |
| `LANGID` | A language identifier. For more information, see [Language Identifiers](/en-us/windows/desktop/Intl/language-identifiers).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef WORD LANGID;` |
| `LCID` | A locale identifier. For more information, see [Locale Identifiers](/en-us/windows/desktop/Intl/locale-identifiers).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef DWORD LCID;` |
| `LCTYPE` | A locale information type. For a list, see [Locale Information Constants](/en-us/windows/desktop/Intl/locale-information-constants).<br><br>This type is declared in WinNls.h as follows:<br><br>`typedef DWORD LCTYPE;` |
| `LGRPID` | A language group identifier. For a list, see [**EnumLanguageGroupLocales**](/en-us/windows/desktop/api/winnls/nf-winnls-enumlanguagegrouplocalesa).<br><br>This type is declared in WinNls.h as follows:<br><br>`typedef DWORD LGRPID;` |
| `LONG` | A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef long LONG;` |
| `LONGLONG` | A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if !defined(_M_IX86)<br> typedef __int64 LONGLONG; <br>#else<br> typedef double LONGLONG;<br>#endif<br>``` | |
| --- | --- |
| `LONG_PTR` | A signed long type for pointer precision. Use when casting a pointer to a long to perform pointer arithmetic.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if defined(_WIN64)<br> typedef __int64 LONG_PTR; <br>#else<br> typedef long LONG_PTR;<br>#endif<br>``` | |
| --- | --- |
| `LONG32` | A 32-bit signed integer. The range is -2147483648 through 2147483647 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef signed int LONG32;` |
| `LONG64` | A 64-bit signed integer. The range is -9223372036854775808 through 9223372036854775807 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef __int64 LONG64;` |
| `LPARAM` | A message parameter.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef LONG_PTR LPARAM;` |
| `LPBOOL` | A pointer to a **BOOL**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef BOOL far *LPBOOL;` |
| `LPBYTE` | A pointer to a **BYTE**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef BYTE far *LPBYTE;` |
| `LPCOLORREF` | A pointer to a [**COLORREF**](/en-us/windows/desktop/gdi/colorref) value.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef DWORD *LPCOLORREF;` |
| `LPCSTR` | A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef __nullterminated CONST CHAR *LPCSTR;` |
| `LPCTSTR` | An **LPCWSTR** if **UNICODE** is defined, an **LPCSTR** otherwise. For more information, see [Windows Data Types for Strings](/en-us/windows/desktop/Intl/windows-data-types-for-strings).<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef LPCWSTR LPCTSTR; <br>#else<br> typedef LPCSTR LPCTSTR;<br>#endif<br>``` | |
| --- | --- |
| `LPCVOID` | A pointer to a constant of any type.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef CONST void *LPCVOID;` |
| `LPCWSTR` | A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CONST WCHAR *LPCWSTR;` |
| `LPDWORD` | A pointer to a **DWORD**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef DWORD *LPDWORD;` |
| `LPHANDLE` | A pointer to a **HANDLE**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HANDLE *LPHANDLE;` |
| `LPINT` | A pointer to an **INT**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef int *LPINT;` |
| `LPLONG` | A pointer to a **LONG**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef long *LPLONG;` |
| `LPSTR` | A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CHAR *LPSTR;` |
| `LPTSTR` | An **LPWSTR** if **UNICODE** is defined, an **LPSTR** otherwise. For more information, see [Windows Data Types for Strings](/en-us/windows/desktop/Intl/windows-data-types-for-strings).<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef LPWSTR LPTSTR;<br>#else<br> typedef LPSTR LPTSTR;<br>#endif<br>``` | |
| --- | --- |
| `LPVOID` | A pointer to any type.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef void *LPVOID;` |
| `LPWORD` | A pointer to a **WORD**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef WORD *LPWORD;` |
| `LPWSTR` | A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef WCHAR *LPWSTR;` |
| `LRESULT` | Signed result of message processing.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef LONG_PTR LRESULT;` |
| `PBOOL` | A pointer to a **BOOL**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef BOOL *PBOOL;` |
| `PBOOLEAN` | A pointer to a **BOOLEAN**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef BOOLEAN *PBOOLEAN;` |
| `PBYTE` | A pointer to a **BYTE**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef BYTE *PBYTE;` |
| `PCHAR` | A pointer to a **CHAR**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CHAR *PCHAR;` |
| `PCSTR` | A pointer to a constant null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CONST CHAR *PCSTR;` |
| `PCTSTR` | A **PCWSTR** if **UNICODE** is defined, a **PCSTR** otherwise. For more information, see [Windows Data Types for Strings](/en-us/windows/desktop/Intl/windows-data-types-for-strings).<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef LPCWSTR PCTSTR;<br>#else<br> typedef LPCSTR PCTSTR;<br>#endif<br>``` | |
| --- | --- |
| `PCWSTR` | A pointer to a constant null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CONST WCHAR *PCWSTR;` |
| `PDWORD` | A pointer to a **DWORD**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef DWORD *PDWORD;` |
| `PDWORDLONG` | A pointer to a **DWORDLONG**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef DWORDLONG *PDWORDLONG;` |
| `PDWORD_PTR` | A pointer to a **DWORD\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef DWORD_PTR *PDWORD_PTR;` |
| `PDWORD32` | A pointer to a **DWORD32**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef DWORD32 *PDWORD32;` |
| `PDWORD64` | A pointer to a **DWORD64**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef DWORD64 *PDWORD64;` |
| `PFLOAT` | A pointer to a **FLOAT**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef FLOAT *PFLOAT;` |
| `PHALF_PTR` | A pointer to a **HALF\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef _WIN64<br> typedef HALF_PTR *PHALF_PTR;<br>#else<br> typedef HALF_PTR *PHALF_PTR;<br>#endif<br>``` | |
| --- | --- |
| `PHANDLE` | A pointer to a **HANDLE**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef HANDLE *PHANDLE;` |
| `PHKEY` | A pointer to an **HKEY**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef HKEY *PHKEY;` |
| `PINT` | A pointer to an **INT**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef int *PINT;` |
| `PINT_PTR` | A pointer to an **INT\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef INT_PTR *PINT_PTR;` |
| `PINT8` | A pointer to an **INT8**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef INT8 *PINT8;` |
| `PINT16` | A pointer to an **INT16**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef INT16 *PINT16;` |
| `PINT32` | A pointer to an **INT32**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef INT32 *PINT32;` |
| `PINT64` | A pointer to an **INT64**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef INT64 *PINT64;` |
| `PLCID` | A pointer to an **LCID**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef PDWORD PLCID;` |
| `PLONG` | A pointer to a **LONG**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef LONG *PLONG;` |
| `PLONGLONG` | A pointer to a **LONGLONG**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef LONGLONG *PLONGLONG;` |
| `PLONG_PTR` | A pointer to a **LONG\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef LONG_PTR *PLONG_PTR;` |
| `PLONG32` | A pointer to a **LONG32**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef LONG32 *PLONG32;` |
| `PLONG64` | A pointer to a **LONG64**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef LONG64 *PLONG64;` |
| `POINTER_32` | A 32-bit pointer. On a 32-bit system, this is a native pointer. On a 64-bit system, this is a truncated 64-bit pointer.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if defined(_WIN64)<br>#define POINTER_32 __ptr32<br>#else<br>#define POINTER_32<br>#endif<br>``` | |
| --- | --- |
| `POINTER_64` | A 64-bit pointer. On a 64-bit system, this is a native pointer. On a 32-bit system, this is a sign-extended 32-bit pointer.<br><br>Note that it is not safe to assume the state of the high pointer bit.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if (_MSC_VER >= 1300)<br>#define POINTER_64 __ptr64<br>#else<br>#define POINTER_64<br>#endif<br>``` | |
| --- | --- |
| `POINTER_SIGNED` | A signed pointer.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`#define POINTER_SIGNED __sptr` |
| `POINTER_UNSIGNED` | An unsigned pointer.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`#define POINTER_UNSIGNED __uptr` |
| `PSHORT` | A pointer to a **SHORT**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef SHORT *PSHORT;` |
| `PSIZE_T` | A pointer to a **SIZE\_T**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef SIZE_T *PSIZE_T;` |
| `PSSIZE_T` | A pointer to a **SSIZE\_T**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef SSIZE_T *PSSIZE_T;` |
| `PSTR` | A pointer to a null-terminated string of 8-bit Windows (ANSI) characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef CHAR *PSTR;` |
| `PTBYTE` | A pointer to a **TBYTE**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef TBYTE *PTBYTE;` |
| `PTCHAR` | A pointer to a **TCHAR**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef TCHAR *PTCHAR;` |
| `PTSTR` | A **PWSTR** if **UNICODE** is defined, a **PSTR** otherwise. For more information, see [Windows Data Types for Strings](/en-us/windows/desktop/Intl/windows-data-types-for-strings).<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef LPWSTR PTSTR;<br>#else typedef LPSTR PTSTR;<br>#endif<br>``` | |
| --- | --- |
| `PUCHAR` | A pointer to a **UCHAR**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef UCHAR *PUCHAR;` |
| `PUHALF_PTR` | A pointer to a **UHALF\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef _WIN64<br> typedef UHALF_PTR *PUHALF_PTR;<br>#else<br> typedef UHALF_PTR *PUHALF_PTR;<br>#endif<br>``` | |
| --- | --- |
| `PUINT` | A pointer to a **UINT**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef UINT *PUINT;` |
| `PUINT_PTR` | A pointer to a **UINT\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef UINT_PTR *PUINT_PTR;` |
| `PUINT8` | A pointer to a **UINT8**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef UINT8 *PUINT8;` |
| `PUINT16` | A pointer to a **UINT16**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef UINT16 *PUINT16;` |
| `PUINT32` | A pointer to a **UINT32**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef UINT32 *PUINT32;` |
| `PUINT64` | A pointer to a **UINT64**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef UINT64 *PUINT64;` |
| `PULONG` | A pointer to a **ULONG**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef ULONG *PULONG;` |
| `PULONGLONG` | A pointer to a **ULONGLONG**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef ULONGLONG *PULONGLONG;` |
| `PULONG_PTR` | A pointer to a **ULONG\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef ULONG_PTR *PULONG_PTR;` |
| `PULONG32` | A pointer to a **ULONG32**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef ULONG32 *PULONG32;` |
| `PULONG64` | A pointer to a **ULONG64**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef ULONG64 *PULONG64;` |
| `PUSHORT` | A pointer to a **USHORT**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef USHORT *PUSHORT;` |
| `PVOID` | A pointer to any type.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef void *PVOID;` |
| `PWCHAR` | A pointer to a **WCHAR**.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef WCHAR *PWCHAR;` |
| `PWORD` | A pointer to a **WORD**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef WORD *PWORD;` |
| `PWSTR` | A pointer to a null-terminated string of 16-bit Unicode characters. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef WCHAR *PWSTR;` |
| `QWORD` | A 64-bit unsigned integer.<br><br>This type is declared as follows:<br><br>`typedef unsigned __int64 QWORD;` |
| `SC_HANDLE` | A handle to a service control manager database. For more information, see [SCM Handles](/en-us/windows/desktop/Services/scm-handles).<br><br>This type is declared in WinSvc.h as follows:<br><br>`typedef HANDLE SC_HANDLE;` |
| `SC_LOCK` | A lock to a service control manager database. For more information, see [SCM Handles](/en-us/windows/desktop/Services/scm-handles).<br><br>This type is declared in WinSvc.h as follows:<br><br>`typedef LPVOID SC_LOCK;` |
| `SERVICE_STATUS_HANDLE` | A handle to a service status value. For more information, see [SCM Handles](/en-us/windows/desktop/Services/scm-handles).<br><br>This type is declared in WinSvc.h as follows:<br><br>`typedef HANDLE SERVICE_STATUS_HANDLE;` |
| `SHORT` | A 16-bit integer. The range is -32768 through 32767 decimal.<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef short SHORT;` |
| `SIZE_T` | The maximum number of bytes to which a pointer can point. Use for a count that must span the full range of a pointer.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef ULONG_PTR SIZE_T;` |
| `SSIZE_T` | A signed version of **SIZE\_T**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef LONG_PTR SSIZE_T;` |
| `TBYTE` | A **WCHAR** if **UNICODE** is defined, a **CHAR** otherwise.<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef WCHAR TBYTE;<br>#else<br> typedef unsigned char TBYTE;<br>#endif<br>``` | |
| --- | --- |
| `TCHAR` | A **WCHAR** if **UNICODE** is defined, a **CHAR** otherwise.<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef UNICODE<br> typedef WCHAR TCHAR;<br>#else<br> typedef char TCHAR;<br>#endif<br>``` | |
| --- | --- |
| `UCHAR` | An unsigned **CHAR**.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef unsigned char UCHAR;` |
| `UHALF_PTR` | An unsigned **HALF\_PTR**. Use within a structure that contains a pointer and two small fields.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#ifdef _WIN64<br> typedef unsigned int UHALF_PTR;<br>#else<br> typedef unsigned short UHALF_PTR;<br>#endif<br>``` | |
| --- | --- |
| `UINT` | An unsigned **INT**. The range is 0 through 4294967295 decimal.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef unsigned int UINT;` |
| `UINT_PTR` | An unsigned **INT\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if defined(_WIN64)<br> typedef unsigned __int64 UINT_PTR;<br>#else<br> typedef unsigned int UINT_PTR;<br>#endif<br>``` | |
| --- | --- |
| `UINT8` | An unsigned **INT8**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned  char UINT8;` |
| `UINT16` | An unsigned **INT16**.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned  short UINT16;` |
| `UINT32` | An unsigned **INT32**. The range is 0 through 4294967295 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned int UINT32;` |
| `UINT64` | An unsigned **INT64**. The range is 0 through 18446744073709551615 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned __int64 UINT64;` |
| `ULONG` | An unsigned **LONG**. The range is 0 through 4294967295 decimal.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef unsigned long ULONG;` |
| `ULONGLONG` | A 64-bit unsigned integer. The range is 0 through 18446744073709551615 decimal.<br><br>This type is declared in WinNT.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if !defined(_M_IX86)<br> typedef unsigned __int64 ULONGLONG;<br>#else<br> typedef double ULONGLONG;<br>#endif<br>``` | |
| --- | --- |
| `ULONG_PTR` | An unsigned **LONG\_PTR**.<br><br>This type is declared in BaseTsd.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>#if defined(_WIN64)<br> typedef unsigned __int64 ULONG_PTR;<br>#else<br> typedef unsigned long ULONG_PTR;<br>#endif<br>``` | |
| --- | --- |
| `ULONG32` | An unsigned **LONG32**. The range is 0 through 4294967295 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned int ULONG32;` |
| `ULONG64` | An unsigned **LONG64**. The range is 0 through 18446744073709551615 decimal.<br><br>This type is declared in BaseTsd.h as follows:<br><br>`typedef unsigned __int64 ULONG64;` |
| `UNICODE_STRING` | A Unicode string.<br><br>This type is declared in Winternl.h as follows:<br><br><br>| C++ |<br>| --- |<br>| ```<br>typedef struct _UNICODE_STRING {<br>  USHORT  Length;<br>  USHORT  MaximumLength;<br>  PWSTR  Buffer;<br>} UNICODE_STRING;<br>typedef UNICODE_STRING *PUNICODE_STRING;<br>typedef const UNICODE_STRING *PCUNICODE_STRING;<br>``` | |
| --- | --- |
| `USHORT` | An unsigned **SHORT**. The range is 0 through 65535 decimal.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef unsigned short USHORT;` |
| `USN` | An update sequence number (USN).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef LONGLONG USN;` |
| `VOID` | Any type.<br><br>This type is declared in WinNT.h as follows:<br><br>`#define VOID void` |
| `WCHAR` | A 16-bit Unicode character. For more information, see [Character Sets Used By Fonts](/en-us/windows/desktop/gdi/character-sets-used-by-fonts).<br><br>This type is declared in WinNT.h as follows:<br><br>`typedef wchar_t WCHAR;` |
| `WINAPI` | The calling convention for system functions.<br><br>This type is declared in WinDef.h as follows:<br><br>`#define WINAPI __stdcall`<br><br>**CALLBACK**, **WINAPI**, and **APIENTRY** are all used to define functions with the \_\_stdcall calling convention. Most functions in the Windows API are declared using **WINAPI**. You may wish to use **CALLBACK** for the callback functions that you implement to help identify the function as a callback function. |
| `WORD` | A 16-bit unsigned integer. The range is 0 through 65535 decimal.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef unsigned short WORD;` |
| `WPARAM` | A message parameter.<br><br>This type is declared in WinDef.h as follows:<br><br>`typedef UINT_PTR WPARAM;` |

## Requirements

| Requirement | Value |
| --- | --- |
| Minimum supported client | Windows XP [desktop apps only] |
| Minimum supported server | Windows Server 2003 [desktop apps only] |
| Header | - BaseTsd.h;<br>- WinDef.h;<br>- WinNT.h |
````
