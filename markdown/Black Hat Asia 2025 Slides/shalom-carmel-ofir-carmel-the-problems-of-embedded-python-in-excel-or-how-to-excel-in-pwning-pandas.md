---
title: "The Problems of Embedded Python in Excel, or How to Excel in Pwning Pandas"
speakers: ["Shalom Carmel", "Ofir Carmel"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Shalom Carmel & Ofir Carmel_The Problems of Embedded Python in Excel, or How to Excel in Pwning Pandas.pdf"
pages: 37
sha256: "e9824611a1e1e0b98988e8d2958c645e9328e57772d0f51c8c8fc6f9ad6fcae6"
text_chars: 13123
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 94.8
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:57:42Z"
---
# The Problems of Embedded Python in Excel, or How to Excel in Pwning Pandas

**Speakers:** Shalom Carmel, Ofir Carmel  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Shalom Carmel & Ofir Carmel_The Problems of Embedded Python in Excel, or How to Excel in Pwning Pandas.pdf` (37 pages)


## Slide 1

The Problems of Embedded Python in Excel

( How to excel in pwning pandas )

#BHAS @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ASIA 2025
APRIL 3-4, 2025
BRIEFINGS
The Problems of
Embedded Python
In Excel
( How to excel in
pwning pandas )
#BHAS @BlackHatEvents
```

## Slide 2

#### Who are we?

##### **Shalom Carmel**

##### **Ofir Carmel**

##### **CIO @ GlobalDots.com**

##### **CS Student**

#BHAS @BlackHatEvents

## Slide 3

### TL;DR

###### **The facts**

- Excel 365 runs python which refers to spreadsheet data

- The python code and the data are sent over to Microsoft for processing

###### **I found out that**

- We can play with and modify the PY cloud runtime environment

- PY cloud runtime environments seem to be shared between sessions<sup>1</sup>

_1 See March 27, 2025 update_

#BHAS @BlackHatEvents

## Slide 4

### Work In Progress / Proof Of Concept

**https://github.com/shalomc/bhasia2025**

#BHAS @BlackHatEvents

## Slide 5

#### Thank you, GlobalDots HR

HR made me take PTO near the end of the year. My wife told me to fix the shed.

I pleaded for a couple of hours to look at some new productivity stuff.

This is the result, some days and nights later

#BHAS @BlackHatEvents

## Slide 6

#### Timeline

- Introduction

- The PY environment

- Execution of remote server code

- Shared user sessions (??)

- Uploading of custom binary files

- Live demo

- Summary

- Q&A

#BHAS @BlackHatEvents

## Slide 7

#### Introduction

- Excel is used by millions worldwide, and Excel 365 supports python

- The Python environment is geared at heavy data processing business and academia users

- It is expected to be a secure and private environment

- Prevalence of VB macros & automation in the finance sector

#BHAS @BlackHatEvents

## Slide 8

#### Excel-specific embedded Python extensions

- =PY() Excel formula

- The xl() python function refers to Excel cells and ranges

- CTRL+Enter sends the code to execution

- Input options: cells, ranges, named ranges, tables

- Output options: pandas dataframes, lists, discrete values, python objects

#BHAS @BlackHatEvents

## Slide 9

#### How it works?

https://support.microsoft.com/en-us/office/get-started-with-python-in-excel-a33fbcbe-065b-41d3-82cf-23d05397f53d

#BHAS @BlackHatEvents

## Slide 10

#### How it works?

#BHAS @BlackHatEvents

## Slide 11

#### Architecture

Data + py Code
Results
365
Entitlement

#BHAS @BlackHatEvents

## Slide 12

Python in Excel Security **https://support.microsoft.com/en-gb/office/data-security-and-python-in-excel-33cc88a4-4a87-485e-9ff9-f35958278327**

- The container has Python and a curated set of secured libraries provided by Anaconda.

- The Python code doesn't have access to your computer, devices, or account.

- The Python code doesn't have network access.

- The Python code doesn't have access to a user token.

- Python formulas have access to read cell values within the workbook, based on the cell reference, or values from external data sources, through the Power Query connection name.

- Python functions cannot return other object types like macros, VBA code, or other formulas.

- The Python code doesn’t have access to other properties in the workbook, such as formulas, charts, PivotTables, macros, or VBA code.

- The containers stay online as long as the workbook is open or until a timeout occurs.

- Data isn't persisted in the Microsoft Cloud.

- Python code runs within the compliance boundary of your organization.

#BHAS @BlackHatEvents

## Slide 13

#### Jupyter in Excel

- The spreadsheet becomes a Jupyter notebook

- Every Excel cell is a Jupyter cell. Evaluation order:

   - sheets → rows ↓ columns →

- Jupyter magic commands supported

#BHAS @BlackHatEvents

## Slide 14

#### Jupyter magic commands

Executed on the host (Azure container)

**Command Action** %system  %sx !! _Execute a shell command_ %env _Returns a dictionary of environment variables_ %%bash _Execute an entire bash script_ %lsmagic _Lists available magic commands_

#BHAS @BlackHatEvents

## Slide 15

OFFICEPY_OUTBOUND_BROKER_HOSTNAME fs.officepy.microsoftusercontent.com OFFICEPY_OUTBOUND_BROKER_IP_ADDRESS 10.0.1.250 OFFICEPY_OUTBOUND_BROKER_PORT 5050 Fabric_NET-0-[Delegated] 10.32.0.99 Fabric_NodeIPOrFQDN 10.92.0.12

Interesting environment variables **`list(os.environ.items()) sorted(os.environ.items(), key=lambda y: y[0].lower())`**

|list(os.environ.items())
**Variable**|**Value**|
|---|---|
|OFFICEPY_OUTBOUND_BROKER_IP_ADDRESS|_10.0.1.250_|
|OFFICEPY_OUTBOUND_BROKER_PORT|_5050_|
|Fabric_NET-0-[Delegated]|_10.32.0.99_|
|Fabric_NodeIPOrFQDN|_10.92.0.12_|
|JUPYTER_TOKEN|_F57431********9cc9_|
|JPY_SESSION_NAME|_A5e*******38c6.py_|

#BHAS @BlackHatEvents

## Slide 16

#### Python standard libraries

\```
def list_installed_packages():
try:
import importlib.metadata
installed_packages= importlib.metadata.distributions()
except ImportError:
installed_packages= []
packages_list= [(package.metadata['Name'],
str(package.version),
str(package.metadata['Summary']),
str(package._path)
)
for package in installed_packages]
packages_list_sorted= [(p00, p01, p02, p03 ) for p00, p01, p02, p03
in sorted(packages_list, key=lambda y: y[0].lower())]
return packages_list_sorted
list_installed_packages()
\```

#BHAS @BlackHatEvents

## Slide 17

#### User writable file system

\```
import os
def find_writable_directories(start_dir='/'):
writable_dirs= []
# Walk through the directory tree
for root, dirs, files in os.walk(start_dir, onerror=lambda e: None):
try:
# Check if the directory is writable
if os.access(root, os.W_OK):
writable_dirs.append(root)
\```

\```
except Exception as e:
\```

\```
continue
\```

\```
return writable_dirs
\```

\```
find_writable_directories()
\```

#BHAS @BlackHatEvents

## Slide 18

#### User writable file system

**Directory Note** /app/officepy/* /app/officepy/lib/python3.12/* _All of the python modules_ /app/officepy/share/jupyter/* /proc/[pid]/fd/ /home/jovyan/.ipython/profile_default/startup/ _This is the IPython startup directory_ /home/jovyan/.local/share/jupyter/runtime/ _Jupyter connections and session files_

#BHAS @BlackHatEvents

## Slide 19

#### Some system commands

**Command Action** <u>ping -c 3 4.4.4.4</u> _/bin/bash: line 1: ping: command not found_ dig www.blackhat.com _/bin/bash: line 1: dig: command not found_ nmap localhost _/bin/bash: line 1: nmap: command not found /bin/bash: line 1: nc: command not found_ nc --v which curl _/bin/bash: line 1: which: command not found_ curl --help _Usage: curl [options...] <url> -d, --data <data>           HTTP POST data ….._ pip --version _pip 24.0 from /app/officepy/lib/python3.12/site-_ _<u>packages/pip (python 3.12)</u>_ rpm --version _RPM version 4.18.0_

#BHAS @BlackHatEvents

## Slide 20

#### Install custom python module

\```
%%bash
\```

\```
cd $HOME
mkdirfubar
cd fubar
mkdirexcelpypwn
echo "fubar = 42" > excelpypwn/__init__.py
echo "from setuptoolsimport setup, find_packages" > setup.py
echo "setup(" >> setup.py
echo "    name='excelpypwn'," >> setup.py
echo "    version='0.666.0'" >> setup.py
echo ")" >> setup.py
pip install .  > ../fubar.log
cd ..
\```

#BHAS @BlackHatEvents

## Slide 21

#### Install custom python module

\```
Processing /home/jovyan/fubar
\```

\```
Preparing metadata (setup.py): started
Preparing metadata (setup.py): finished with status 'done'
Building wheels for collected packages: excelpypwn
Building wheel for excelpypwn(setup.py): started
Building wheel for excelpypwn(setup.py): finished with status 'done'
\```

\```
Created wheel for excelpypwn: filename=excelpypwn-0.666.0-py3-none-any.whl size=1168
sha256=2372634cb81cd91ce0ca431965ae4e43245049313f036aefd22528fc63077ad0
\```

\```
Stored in directory: /tmp/pip-ephem-wheel-cache-
lnir11ew/wheels/d5/aa/24/40817f0f8c7b89493c6ccba31edcbc4c495be26e4987f7be54
Successfully built excelpypwn
Installing collected packages: excelpypwn
Successfully installed excelpypwn-0.666.0
\```

#BHAS @BlackHatEvents

## Slide 22

#### Install custom python module

\```
# verify installation of custom module
import excelpypwn
excelpypwn.fubar
\```

#BHAS @BlackHatEvents

## Slide 23

## Jupyter Sessions

#BHAS @BlackHatEvents

## Slide 24

#### March 27, 2025 Update

**In a call with Microsoft security, we were informed that as of February 2025 there is a tightening of session management security, and there will be a session per open file instead of a session per user According to Microsoft**

- **Containers are spun up pre-emptively to improve performance**

- **When there are not a lot of users, a container could be in the hotpool for a few hours.**

- **Before February, different documents from the same user could share the same container. If a user opened multiple workbook, or open/close a workbook multiple times, or clicked the Reset Runtime from Excel UI, there will be multiple Jupyter sessions created within a single container.**

- **After February, we changed to use one container per document per user. So different documents from the same users will not share the same container. There could still be multiple Jupyter sessions in a single container if a user open/close the same workbook multiple times, or clicked Reset Runtime from Excel UI.**

#BHAS @BlackHatEvents

## Slide 25

#### How to find Jupyter sessions

\```
%sxjupyter–paths
\```

\```
config:
/home/jovyan/.jupyter
/home/jovyan/.local/etc/jupyter
/app/officepy/etc/jupyter
/usr/local/etc/jupyter
/etc/jupyter
\```

\```
data:
\```

\```
/home/jovyan/.local/share/jupyter
/app/officepy/share/jupyter
/usr/local/share/jupyter
/usr/share/jupyter
\```

\```
runtime:
\```

\```
/home/jovyan/.local/share/jupyter/runtime
\```

#BHAS @BlackHatEvents

## Slide 26

#### How to find Jupyter sessions

\```
%sxls -al $(jupyter--runtime-dir)
\```

\```
total28
\```

\```
drwx-----T 2 jovyanusers4096 Mar 29 22:09 .
drwxr-xr-x 3 jovyanusers4096 Mar 29 19:44 ..
-rw-r--r--1 jovyanusers510 Mar 29 19:44 jpserver-71-open.html
-rw-------1 jovyanusers293 Mar 29 19:44 jpserver-71.json
-rw-------1 jovyanusers45 Mar 29 19:44 jupyter_cookie_secret
-rw-------1 jovyanusers334 Mar 2919:45kernel-1bc54bd1-b96d-4b6a-b00f-f976054faa3f.json
-rw-------1 jovyanusers334 Mar 2922:09kernel-81d23646-a712-4199-bf1f-14c8a95dd90e.json
\```

#BHAS @BlackHatEvents

## Slide 27

#### How to find Jupyter sessions

\```
%sxjupyterserver list
\```

\```
Currently running servers:
\```

\```
http://SandboxHost-638789305605774754:8888/?token=a8c9a32b-fef8-4926-a45f-4889b9afd71a :: /mnt/file_upload
\```

\```
%sxcat /home/jovyan/.local/share/jupyter/runtime/jpserver*json| grep token
\```

\```
"token": "a8c9a32b-fef8-4926-a45f-4889b9afd71a",
\```

\```
%envJUPYTER_TOKEN
\```

\```
a8c9a32b-fef8-4926-a45f-4889b9afd71a
\```

\```
os.environ["JUPYTER_TOKEN"]
\```

\```
a8c9a32b-fef8-4926-a45f-4889b9afd71a
\```

#BHAS @BlackHatEvents

## Slide 28

#### How to find Jupyter sessions

\```
%sxcurl -s http://${HOSTNAME}:8888/api/sessions?token=${token}
\```

[ { "id": "f3cddf3b-5cf3-45de-9145-2a7e54c5dde0", "path": "3872d4e5-564f-4c2b-aee9-a522473559de.py", "name": null, "type": "notebook", "kernel": { "id": "859fdaa0-7703-4881-af62-18fe3130bdfc", "name": "python3", "last_activity": "2025 -03 -30T11:55:21.642558Z", "execution_state": "busy", "connections": 1 }, "notebook": { "path": "3872d4e5-564f-4c2b-aee9-a522473559de.py", "name": null

}

},

{ "id": "7192eeb7-c201-447b-9b4c-ff21e89325f2", "path": "f5ead0be-35b4-418a-9d25-eafc30b6a99f.py", "name": null, "type": "notebook", "kernel": { "id": "d877ba13-961d-4df1-b109-0d87faf0d5a8", "name": "python3", "last_activity": "2025 -03 -30T11:38:40.905620Z", "execution_state": "idle", "connections": 1 }, "notebook": { "path": "f5ead0be-35b4-418a-9d25-eafc30b6a99f.py", "name": null }

}

]

#BHAS @BlackHatEvents

## Slide 29

#### Upload binary files

- Unincluded python modules

- Overwrite anaconda curated modules with custom code

- Network analysis tools

- Container breakout attempts

- Useful Linux utilities

#BHAS @BlackHatEvents

## Slide 30

#### Upload binary files – practical steps

1. Create a base64 file from the binary

2. Don’t copy/paste

3. Using Excel PowerQuery, import the file to a named range

4. In your code, refer to **xl(“named_range”)**

5. In code, save the text to remote disk

6. Restore binary from base64 representation

7. Run rpm / tar / pip / chmod as necessary

8. Add the binaries to PATH, LD_LIBRARY_PATH, PYTHONPATH

#BHAS @BlackHatEvents

## Slide 31

#### Upload binary files tips

- Binaries from WSL work just fine

- Use the ldd command to find dependencies

   - Handy script on github

- Use VBA to automate process

#BHAS @BlackHatEvents

## Slide 32

# Summary

#BHAS @BlackHatEvents

## Slide 33

#### Controlling python via registry

- Block python

\```
regaddHKCU\software\policies\microsoft\office\16.0\excel\security/v
PythonFunctionWarnings/t REG_DWORD /d 2 /f
\```

Value Meaning
0 Allow all (default)
1 Warn
2 Block

#BHAS @BlackHatEvents

## Slide 34

#### Venues of research

- Jupyter is a code execution platform

   - https://www.youtube.com/watch?v=8vwo6gDANiY

- Is container breakout possible?

- Are sessions really limited?

- Exfiltration of data by custom pandas

- DOS by long-running containers

#BHAS @BlackHatEvents

## Slide 35

#### Attributions and thanks

- Jupyter logo By Cameron Oelsen - https://commons.wikimedia.org/w/index.php?curid=68763478

- <u>www.globaldots.com</u>

#BHAS @BlackHatEvents

## Slide 36

Black Hat Asia Sound Bytes • Python in Excel is a remote code execution platform • All new technology has bugs and security issues

• I am having fun, are you?

#BHAS @BlackHatEvents

## Slide 37

Q&A

#BHAS @BlackHatEvents
