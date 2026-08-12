---
title: "QUACK Hindering Deserialization Attacks via Static Duck Typing"
speakers: ["Neophytos Christou", "Andreas Kellas"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Neophytos Christou&Andreas Kellas_QUACK Hindering Deserialization Attacks via Static Duck Typing.pdf"
pages: 117
sha256: "2db1290ad0d07f7a6e53ca01f80d505fc65c0fff78038fde5f9a188bc57a37cb"
text_chars: 37183
ocr_pages: 25
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:58:36Z"
---
# QUACK Hindering Deserialization Attacks via Static Duck Typing

**Speakers:** Neophytos Christou, Andreas Kellas  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Neophytos Christou&Andreas Kellas_QUACK Hindering Deserialization Attacks via Static Duck Typing.pdf` (117 pages)


## Slide 1

# QUACK: Hindering Deserialization Attacks via Static Duck Typing

Speakers: Andreas Kellas, Neophytos Christou

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
BRIEFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
QUACK: Hindering Deserialization
Attacks via Static Duck Typing
Speakers: Andreas Kellas, Neophytos Christou
```

## Slide 2

### **whoarewe**

Neophytos Christou PhD student, Brown University

Andreas Kellas PhD student, Columbia University

Collaborators: Yaniv David<sup>1</sup> , Vasileios Kemerlis<sup>2</sup> , Junfeng Yang<sup>1</sup> Columbia University<sup>1</sup> , Brown University<sup>2</sup>

#BHUSA   @BlackHatEvents

## Slide 3

**We know that deserialization is dangerous …**

#BHUSA   @BlackHatEvents

## Slide 4

**We know that deserialization is dangerous …**

**2010: “Utilizing Code Reuse/ROP in PHP Application Exploits” Stefan Esser @ BHUSA**

**2015: “Marshalling Pickles: how deserializing objects will ruin your day” Frohoff and Lawrence @ AppSecCali 2018: “Automated Discovery of Deserialization Gadget Chains” Ian Haken @ BHUSA**

#BHUSA   @BlackHatEvents

## Slide 5

**We know that deserialization is dangerous … … so we set out to mitigate the risks**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
We know that deserialization is dangerous...
... So We Set out to mitigate the risks
QUACK: Hindering Deserialization Attacks
via Static Duck Typing
Yaniv David*, Neophytos Christou', Andreas D. Kellas*, Vasileios P. Kemerlis', and Junfeng Yang*
*Columbia University 'Brown University
```

## Slide 6

#### **Goals**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifikhat Sa gk f
BRIEFINGS
QUACK: Hindering Deserialization Attacks
via Static Duck Typing
Yaniv David*, Neophytos Christou', Andreas D. Kellas*, Vasileios P. Kemerlis', and Junfeng Yang*
*Columbia University 'Brown University
Artifact
Evaluated
&npss
Available
Functional
Reproduced
```

## Slide 7

#### **Goals**

#### **1. Introduce QUACK to the security community**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifikhat Sa gk f
BRIEFINGS . Y
Goals
1. Introduce QUACK to the security community
QUACK: Hindering Deserialization Attacks
via Static Duck Typing
Yaniv David*, Neophytos Christou', Andreas D. Kellas*, Vasileios P. Kemerlis', and Junfeng Yang*
*Columbia University 'Brown University
```

## Slide 8

#### **Goals**

#### **1. Introduce QUACK to the security community**

**2.   Raise awareness for the risks of deserialization**

#BHUSA   @BlackHatEvents

## Slide 9

### **Roadmap**

Background QUACK Takeaways
PHP Mitigating  The future of
deserialization  deserialization  QUACK and
exploits exploits with  deserialization
static duck typing exploits

#BHUSA   @BlackHatEvents

## Slide 10

### **Roadmap**

Background
PHP
deserialization
exploits

QUACK Takeaways
Mitigating  The future of
deserialization  QUACK and
exploits with  deserialization
static duck typing exploits

#BHUSA   @BlackHatEvents

## Slide 11

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 12

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 13

### **We Know Deserialization is Dangerous**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
We Know Deserialization is Dangerous
InvoiceShelf <= 1.3.0 - PHP CVE-2093-30534: Insecure
+ ae . Deserialization in Cacti prior to 1.2.95
Deserialization P
CVE-2024-55556 7. —“ - ork Soa ASN
THREAT INTELLIGENCE
UNPATCHED PHP DESERIALIZATION VULNERABILITY IN
ARTICA PROXY
Description
ClipBucket V5 provides open source video hosting with PHP. ClipBucket-v5 Version 2.0 to Version 5.5.1 Revision 199 are vulnerable to PHP
Deserialization vulnerability. The vulnerability exists in upload/photo_upload.php within the decode_key function. User inputs were supplied
PHP deserialization attacks and a new gadget chain in Laravel
Posted) Tue 13 February 2024
Author) Viathieu Farrel
```

## Slide 14

### **We Know Deserialization is Dangerous**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat AS - tee | ;
BRIEFINGS 4 \ ~% j ,
We Know Deserialization is Dangerous
unserialize(string $data, array $options = []): mixed
unserialize() takes a single serialized variable and converts it back into a PHP value.
Warning -—“—
and a malicious user may be able to exploit this.
```

## Slide 15

### **PHP Object Injection (POI)**

#BHUSA   @BlackHatEvents

## Slide 16

### **PHP Object Injection (POI)**

**Programmer expects $obj to be an App…**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
PHP Object Injection (POl)
Programmer expects $obj Ke)
class App { be an App...
public $name;
public function run() { }
}
$obj = unserialize( );
$objrun();
```

## Slide 17

### **PHP Object Injection (POI)**

O:3:”App”:1:{s:4:”name”;s:8:”MyWebApp”;}

**Programmer expects $obj to be an App…**

App Object
(
  [name] => MyWebApp
)

#BHUSA   @BlackHatEvents

## Slide 18

### **PHP Object Injection (POI)**

O:3:”App”:1:{s:4:”name”;s:8: ”MyWebAppB lackHat”;}

**Programmer expects $obj to be an App…**

**… but the attacker controls its** **_properties…_**

App Object
(
  [name] => BlackHat
)

#BHUSA   @BlackHatEvents

## Slide 19

### **PHP Object Injection (POI)**

O:3: ”AppF oo”:1:{s:3:” nameb ar”;s:3: ”MyWebAppB AZ”;}

**Programmer expects $obj to be an App…**

**… but the attacker controls its** **_properties…_**

**… and its whole** **_type_**

Foo Object
(
  [bar] => BAZ
)

#BHUSA   @BlackHatEvents

## Slide 20

### **PHP Object Injection (POI)**

O:3: ”AppF oo”:1:{s:3:”name”;O:3:”Bar”:1:{...}};

Foo Object
(
  [name] => Bar Object
   (...)
)

**Programmer expects $obj to be an App…**

**… but the attacker controls its** **_properties…_**

- **… and its whole** **_type_**

**They can create** **_nested_ objects of** **_any loaded class_**

#BHUSA   @BlackHatEvents

## Slide 21

### **PHP Object Injection (POI)**

O:3: ”AppF oo”:1:{s:3:”name”;O:3:”Bar”:1:{...}};

**Programmer expects $obj to be an App…**

**… but the attacker controls its** **_properties…_**

**… and its whole** **_type_**

**Attacker’s goal: Change the control flow to execute malicious functionality**

**They can create** **_nested_ objects of** **_any loaded class_**

#BHUSA   @BlackHatEvents

## Slide 22

### **Manipulating Control Flow**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Manipulating Control Flow
class CommandExecutor {
public $command;
public function run() { system($this—command); }
$obj = unserialize( )
¢objrun();
```

## Slide 23

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

#BHUSA   @BlackHatEvents

## Slide 24

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

O:15:”CommandExecutor”:1:{s:7:”command”;s:13:”echo “pwned!””;}

#BHUSA   @BlackHatEvents

## Slide 25

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

#BHUSA   @BlackHatEvents

## Slide 26

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

**_Magic methods_ execute** **_automatically_ in certain circumstances**

#BHUSA   @BlackHatEvents

## Slide 27

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

O:15:”CommandExecutor”:1:{s:7:”command”;s:13:”echo “pwned!””;}

**_Magic methods_ execute** **_automatically_ in certain circumstances**

#BHUSA   @BlackHatEvents

## Slide 28

### **Manipulating Control Flow**

**Attacker’s goal:** **_Change the control flow_ to** **_execute malicious functionality_**

**What if the attacker can’t find one method that achieves both?**

#BHUSA   @BlackHatEvents

## Slide 29

### **Property Oriented Programming (POP)**

**Exploit Idea:**

**1. Change initial control flow by creating a top-level object with an appropriate magic method 2. Execute malicious functionality by chaining method calls - Recursively set object properties to other objects**

#BHUSA   @BlackHatEvents

## Slide 30

### **Property Oriented Programming (POP)**

**Exploit Idea:**

**1. Change initial control flow by creating a top-level object with an appropriate magic method**

**2. Execute malicious functionality by chaining method calls - Recursively set object properties to other objects**

#BHUSA   @BlackHatEvents

## Slide 31

### **Property Oriented Programming (POP)**

**Exploit Idea:**

**1. Change initial control flow by creating a top-level object with an appropriate magic method**

**2. Execute malicious functionality by chaining method calls - Recursively set object properties to other objects**

#BHUSA   @BlackHatEvents

## Slide 32

### **Property Oriented Programming (POP)**

**Exploit Idea:**

**1. Change initial control flow by creating a top-level object with an appropriate magic method**

**2. Execute malicious functionality by chaining method calls - Recursively set object properties to other objects**

**“Utilizing Code Reuse/ROP in PHP Application Exploits” Stefan Esser @ BHUSA 2010**

#BHUSA   @BlackHatEvents

## Slide 33

### **Property Oriented Programming**

class graph {
function init( ) {...}
class qtype_ddwtos { }
function import($input)
{
    unserialize($input);
class tree {
  }
  public $children;
} function __toString( ) {
   foreach ($this->children){...}
  }
}
class lock {
public $key;
function __destruct( ) {
    echo “Key: $this->key”;
class student_enrollment {
  }
function get_samples( ) {... }
}
}

class filter_data {
function filter( ) {...}
}

class qtype_ddwtos_choice { function choice_group( ) {...} } class recordset_walk { public $callback; public $record; function current( ) { call_user_func($this->callback, $this->record); } }

#BHUSA   @BlackHatEvents

## Slide 34

### **Property Oriented Programming**

class graph {
  function init( ) {...}
class qtype_ddwtos { }
function import($input)
{
    unserialize($input);
class tree {
  }
  public $children;
}   function __toString( ) {
   foreach ($this->children){...}
  }
}
class lock {
  public $key;
  function __destruct( ) {
    echo “Key: $this->key”;
class student_enrollment {
  }
  function get_samples( ) {... }
}
}

class filter_data { function filter( ) {...} }

class qtype_ddwtos_choice { function choice_group( ) {...} } class recordset_walk { public $callback; public $record; function current( ) { call_user_func($this->callback, $this->record); } }

#BHUSA   @BlackHatEvents

## Slide 35

### **Property Oriented Programming**

class graph { class filter_data { function init( ) {...} function filter( ) {...} class qtype_ddwtos { } } function import($input) { unserialize($input); class qtype_ddwtos_choice { class tree { } function choice_group( ) {...} public $children; } function __toString( ) { } foreach ($this->children){...} } } class recordset_walk { {

class recordset_walk { {
public $callback;
  public $record;
function current( ) {
    call_user_func($this->callback,
$this->record);
  }
}

class lock {
  public $key;
  function __destruct( ) {
    echo “Key: $this->key”;
class student_enrollment {
  }
  function get_samples( ) {... }
}
}

#BHUSA   @BlackHatEvents

## Slide 36

### **Property Oriented Programming**

class graph { class filter_data {
  function init( ) {...}   function filter( ) {...}
} }
class qtype_ddwtos_choice {
class tree {
  function choice_group( ) {...}
  public $children;
}
function __toString( ) {
   foreach ($this->children){...}
  }
} class recordset_walk {
public $callback;
  public $record;
function current( ) {
    call_user_func($this->callback,
$this->record);
class student_enrollment {
  }
  function get_samples( ) {... }
}
}

class qtype_ddwtos {
function import($input)
{
    unserialize($input);
  }
}

class lock {
public $key;
function __destruct( ) {
    echo “Key: $this->key”;
class student_enrollment {
  }
  function get_samples( ) {... }
}
}

#BHUSA   @BlackHatEvents

## Slide 37

### **Property Oriented Programming**

class qtype_ddwtos {
function import($input)
{
    unserialize($input);
  }
}
class recordset_walk {
public $callback;
class tree {
class lock {   public $children;   public $record;
public $key; function __toString( ) { function current( ) {
function __destruct( ) {    foreach ($this->children){...}     call_user_func($this->callback,
    echo “Key: $this->key”;   } $this->record);
  } }   }
} }

#BHUSA   @BlackHatEvents

## Slide 38

### **Property Orient** **ed Progr amming**

class qtype_ddwtos {
function import($input)
{
    unserialize($input);
  }
}
class recordset_walk {
public $callback;
class tree {
class lock {   public $children;   public $record;
public $key; function __toString( ) { function current( ) {
function __destruct( ) {    foreach ($this->children){...}     call_user_func($this->callback,
    echo “Key: $this->key”;   } $this->record);
  } }   }
} }

#BHUSA   @BlackHatEvents

## Slide 39

### **Property Oriented Programming**

class qtype_ddwtos {
function import($input)
{
    unserialize($input);
  }
}
class recordset_walk {
public $callback;
class tree {
class lock {   public $children;   public $record;
public $key; function __toString( ) { function current( ) {
function __destruct( ) {    foreach ($this->children){...}     call_user_func($this->callback,
    echo “Key: $this->key”;   } $this->record);
  } }   }
} }

#BHUSA   @BlackHatEvents

## Slide 40

### **Property Oriented Programming**

class qtype_ddwtos { function import($input) { unserialize($input); } } class recordset_walk { public $callback; class tree { class lock { public $children; public $record; public $key; function __toString( ) { function current( ) { function __destruct( ) { foreach ($this->children){...} call_user_func($this->callback, echo “Key: $this->key”; } $this->record); } } } } }

#BHUSA   @BlackHatEvents

## Slide 41

### **Property Oriented Programming**

class qtype_ddwtos {
function import($input)
{
    unserialize($input);
  }
}
class recordset_walk {
public $callback;
class tree {
class lock {   public $children;   public $record;
public $key; function __toString( ) { function current( ) {
function __destruct( ) {    foreach ($this->children){...}     call_user_func($this->callback,
    echo “Key: $this->key”;   } $this->record);
  } }   }
} }

#BHUSA   @BlackHatEvents

## Slide 42

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 43

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 44

### **Moodle POI Vulnerability**

https://sec-consult.com/vulnerability-lab/advisory/remote-code-execution-php-unserialize-moodle-open-source-learning- platform-cve-2018-14630

#BHUSA   @BlackHatEvents

## Slide 45

### **Moodle POI Vulnerability**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Moodle POI Vulnerability
foreach ($data['#']['answer'] as $answerxml) {
$ans = $format—import_answer($answerxml);
$options = unserialize($ans—feedback[ 'text']);
$question>choices[] = array(
‘answer' => $ans—ar
wer,
‘choicegroup' => $options—dra
sroun
sroup,
‘infinite' => $options—infinite
);
```

## Slide 46

### **Moodle POI Vulnerability**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Moodle POI Vulnerability
foreach ($data['#']['answer'] as $answerxml) {
$ans = $format—import_answer($answerxml);
$options =
unserialize($ans— feedback['text']);
$question->choices[] = array(
‘answer' = $ans—answer,
‘choicegroup' => $options—draggroup,
‘infinite' > $options—infinite,
);
```

## Slide 47

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 48

### **Roadmap**

**Background PHP deserialization exploits**

**How do PHP deserialization exploits work? Deserialization exploit demo How do existing defenses work?**

#BHUSA   @BlackHatEvents

## Slide 49

## **POI Mitigations**

**Simple(r) representations:** Works only for simple data structures, not complex objects

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
POI Mitigations
Simple(r) representations: Use a safe, standard data interchange
Works only for simple data format such as JSON (via json_decode() and
structures, not complex json_encode()) if you need to pass serialized
objects data to the user.
```

## Slide 50

## **POI Mitigations**

**HMACs:** Works only if the serialized object was produced by the application

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
POI Mitigations
HMACs: Works only if the If you need to unserialize externally-stored
serialized object was serialized data, consider using hash_hmac()
produced by the application for data validation. Make sure data is not
modified by anyone but you.
```

## Slide 51

## **POI Mitigations**

**allowed_classes** option to unserialize: **works!**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
POI Mitigations
unserialize(string $data, array $options = [])
Description
Either an array of class names which should be
a 1 lowed _C lasses ; accepted, false to accept no classes, or true to
option to Uunseria lize: accept all classes. If this option is defined and
works! unserialize() encounters an object of a class that
isn't to be accepted, then the object will be
instantiated as __PHP_Incomplete_Class instead.
Omitting this option is the same as defining it as
true: PHP will attempt to instantiate objects of any
class.
```

## Slide 52

### **Restricting Allowed Classes**

O:15:”CommandExecutor”:1:{s:7:”command”;s:13:”echo “pwned!””;}

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
":1:{s:7:"command” ;s:13:”echo “pwned! ”";}
PHP Fatal error: Uncaught Error: The script tried to call a method
on an incomplete object. Please ensure that the class definition "Co
mmandExecutor" of the object you are trying to operate on was loaded
```

## Slide 53

### **Restricting Allowed Classes**

- **allowed_classes** is barely used

   - ~0.1% of PHP deserialization invocations in Github use it

- Why?

   - Developers are not aware of the dangers of deserialization

   - ○ Tedious to manually deduce allowed classes for each deserialization call

#BHUSA   @BlackHatEvents

## Slide 54

### **Key Takeaways**

**Background PHP deserialization exploits**

**Deserialization vulnerabilities are exploitable because attackers have access to more classes than the developer intended**

#BHUSA   @BlackHatEvents

## Slide 55

### **Key Takeaways**

**Background PHP deserialization exploits**

**Deserialization vulnerabilities are exploitable because attackers have access to more classes than the developer intended**

**Existing mitigations help, but not fully**

#BHUSA   @BlackHatEvents

## Slide 56

### **Roadmap**

Background
PHP
deserialization
exploits

QUACK Takeaways
Mitigating  The future of
deserialization  QUACK and
exploits with  deserialization
static duck typing exploits

#BHUSA   @BlackHatEvents

## Slide 57

### **Roadmap**

Background QUACK
PHP Mitigating
deserialization  deserialization
exploits exploits with
static duck typing

Takeaways
The future of
QUACK and
deserialization
exploits

#BHUSA   @BlackHatEvents

## Slide 58

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 59

### **QUACK’s Objective**

**Automatically restrict each unserialize call to create** **_only programmer-intended classes_**

#BHUSA   @BlackHatEvents

## Slide 60

### **QUACK: High-level Approach**

class graph { function init( ) {...} }

class course { function filter( ) {...} }

class qtype_ddwtos { function import($input) { unserialize($input); } }

class lock { function __destruct( ) { echo “Key: $this->key”; } }

class base_setting { function get_name( ) {...} }

class tree { function __toString( ) { foreach ($this->children){...} } }

class student_enrollment { function get_samples( ) {... } }

class filter_data { function filter( ) {...} }

class qtype_ddwtos_choice { function choice_group( ) {...} }

class recordset_walk { function current( ) { call_user_func($this->callback, $this->record); } }

#BHUSA   @BlackHatEvents

## Slide 61

### **QUACK: High-level Approach**

**1. Determine set of** class graph { **_available classes_** function init( ) {...} **loaded at deserialization point** } class

class base_setting { function get_name( ) {...} }

class course { function filter( ) {...}

}

class tree { function __toString( ) { foreach ($this->children){...} } }

class qtype_ddwtos { function import($input) { unserialize($input); }

}

class lock { function __destruct( ) { echo “Key: $this->key”; } }

class student_enrollment { function get_samples( ) {... } }

class filter_data { function filter( ) {...} }

class qtype_ddwtos_choice { function choice_group( ) {...} }

class recordset_walk { function current( ) { call_user_func($this->callback, $this->record); } }

#BHUSA   @BlackHatEvents

## Slide 62

### **QUACK: High-level Approach**

class graph { function init( ) {...} }

class base_setting { function get_name( ) {...} }

class course { function filter( ) {...} }

class tree { function __toString( ) { foreach ($this->children){...} }

class qtype_ddwtos { function import($input) { unserialize($input); }

- }

}

**2. Infer the set of** classfunctionlock {__destruct( ) { **_possible classes_ based on** echo “Key: $this->key”; class student_enrollment { **how deserialized object is used** } function get_samples( ) {... } } } **(static duck typing)**

class filter_data { function filter( ) {...} }

class qtype_ddwtos_choice { function choice_group( ) {...} }

class recordset_walk { function current( ) { call_user_func($this->callback, $this->record); }

}

#BHUSA   @BlackHatEvents

## Slide 63

### **QUACK: High-level Approach**

class graph { function init( ) {...} }

class base_setting { function get_name( ) {...} }

class course { function filter( ) {...} }

class tree { function __toString( ) { foreach ($this->children){...} }

class qtype_ddwtos { function import($input) { unserialize($input); }

   - }

- }

**3. Restrict the** class lock { **unserialize call to allow** function __destruct( ) {

echo “Key: $this->key”; class student_enrollment {

**classes that are both** } **_available_ and** **_possible_** function get_samples( ) {... }

} }

**(leaves only the likely intended classes)**

class filter_data { function filter( ) {...} }

class qtype_ddwtos_choice { function choice_group( ) {...} }

class recordset_walk { function current( ) { call_user_func($this->callback, $this->record);

- }

}

#BHUSA   @BlackHatEvents

## Slide 64

QUACK
Identify available
classes at
Available
unserialize call
Classes
PHP
Allowed
application
Classes
source code
Infer possible types
Inferred
of unserialized
Classes
object with type
evidence
#BHUSA   @BlackHatEvents

## Slide 65

Static analysis
QUACK
using Joern
framework
Identify available
classes at
Available
unserialize call
Classes
PHP
Allowed
application
Classes
source code
Infer possible types
Inferred
of unserialized
Classes
object with type
evidence
#BHUSA   @BlackHatEvents

## Slide 66

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 67

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 68

## **Inferring Available Classes**

class qtype_ddwtos_choice {...} include qtype_ddwtos.php class course {...} class graph {...} **Available Classes** qtype_ddwtos include tree.php class qtype_ddwtos { function import($input) { include qtype_ddwtos_choice.php unserialize($input); include recordset_walk.php } class tree {...} } class filter_data {...} include qtype_ddwtos.php class lock {...} class recordset_walk {...}

#BHUSA   @BlackHatEvents

## Slide 69

## **Inferring Available Classes**

class qtype_ddwtos_choice {...} include qtype_ddwtos.php class course {...} class graph {...}

include tree.php
class qtype_ddwtos {
function import($input) {
include qtype_ddwtos_choice.php
unserialize($input);
include recordset_walk.php
  }
class tree {...}
}
class filter_data {...}
include qtype_ddwtos.php
class lock {...}
class recordset_walk {...}

**Available Classes** qtype_ddwtos tree

#BHUSA   @BlackHatEvents

## Slide 70

## **Inferring Available Classes**

class qtype_ddwtos_choice {...}
include qtype_ddwtos.php
class course {...}
class graph {...} Available Classes
qtype_ddwtos
include tree.php
tree
class qtype_ddwtos {
function import($input) { qtype_ddwtos_choice
include qtype_ddwtos_choice.php
unserialize($input); recordset_walk
include recordset_walk.php
  }
class tree {...}
}
class filter_data {...}
include qtype_ddwtos.php
class lock {...}
class recordset_walk {...}

#BHUSA   @BlackHatEvents

## Slide 71

## **Inferring Available Classes**

class qtype_ddwtos_choice {...}
include qtype_ddwtos.php
class course {...}
class graph {...} Available Classes
qtype_ddwtos
include tree.php
tree
class qtype_ddwtos {
function import($input) { qtype_ddwtos_choice
include qtype_ddwtos_choice.php
unserialize($input); recordset_walk
include recordset_walk.php
  }
class tree {...}
}
class filter_data {...}
include qtype_ddwtos.php
class lock {...}
class recordset_walk {...}

#BHUSA   @BlackHatEvents

## Slide 72

## **Inferring Available Classes**

class qtype_ddwtos_choice {...}
include qtype_ddwtos.php
class course {...}
class graph {...} Available Classes
qtype_ddwtos
include tree.php
tree
class qtype_ddwtos {
function import($input) { qtype_ddwtos_choice
include qtype_ddwtos_choice.php
unserialize($input); recordset_walk
include recordset_walk.php
  } class tree {...} course
}
lock
class filter_data {...}
include qtype_ddwtos.php
class lock {...}
class recordset_walk {...}

#BHUSA   @BlackHatEvents

## Slide 73

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 74

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 75

### **Duck Typing**

Dynamic languages: An object is of a given type if it has the methods/properties required by that type

#BHUSA   @BlackHatEvents

## Slide 76

### **Duck Typing**

Dynamic languages: An object is of a given type if it has the methods/properties required by that type

QUACK: _static_ duck-typing-based _type inference rules_

#BHUSA   @BlackHatEvents

## Slide 77

### **Type Inference Rules: Class Methods**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Type Inference Rules: Class Methods
class Duck {
public function swim() {}
public function fly() {}
}
class Whale {
public function swim() {}
}
$animal = unserialize($input);
$animal>swim();
$animal>fly();
```

## Slide 78

### **Type Inference Rules: Class Methods**

Type: **Duck** | **Whale**

- Reason: **swim** method

- ● Node: **$animal**

#BHUSA   @BlackHatEvents

## Slide 79

### **Type Inference Rules: Class Methods**

Type: **Duck** | **Whale**

- Reason: **swim** method

- ● Node: **$animal**

Type: **Duck**

- Reason: **fly** method

- Node: **$animal**

#BHUSA   @BlackHatEvents

## Slide 80

### **Type Inference Rules: Class Methods**

Type:  Duck  |  Whale
● Reason:  swim  method
●
Node:  $animal
Type:  Duck

- Reason: **fly** method

- ● Node: **$animal**

Possible classes: **Duck**

#BHUSA   @BlackHatEvents

## Slide 81

### **Type Inference Rules: Class Properties**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Type Inference Rules: Class Properties
class Duck {
public $feather_color;
}
class Whale {
public $flippers;
}
$animal = unserialize($object);
echo "This duck's feathers are $animal—>feather_color";
```

## Slide 82

### **Type Inference Rules: Class Properties**

Type: **Duck**

● Reason: **feather_color** property

● Node: **$animal**

#BHUSA   @BlackHatEvents

## Slide 83

### **Type Inference Rules: Class Properties**

Type: **Duck**

● Reason: **feather_color** property ● Node: **$animal**

Possible classes: **Duck**

#BHUSA   @BlackHatEvents

## Slide 84

**Type Inference Rules: Argument Type**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Type Inference Rules: Argument Type
class Duck {}
class Whale {}
function somefunc(Duck $duck) {}
$animal = unserialize($object);
somefunc($animal);
```

## Slide 85

### **Type Inference Rules: Argument Type**

Type: **Duck**

●
Reason: 1st argument to
somefunc

● Node: **$animal**

#BHUSA   @BlackHatEvents

## Slide 86

### **Type Inference Rules: Argument Type**

Type: **Duck**

●
Reason: 1st argument to
somefunc

● Node: **$animal**

Possible classes: **Duck**

#BHUSA   @BlackHatEvents

## Slide 87

### **Type Inference Rules: Known Operators**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
BRIEFINGS
Type Inference Rules: Known Operators
class Duck {}
class Whale {}
function is_it_duck() {
$animal = unserialize($object);
if ($animal instanceof Duck) {
echo "It's a duck!\n"
}
```

## Slide 88

### **Type Inference Rules: Known Operators**

Type:  Duck
● Reason:  instanceof
●
Node:  $animal

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Type Inference Rules: Known Operators
class Duck {}
Type: Duck
class Whale {} e Reason: instanceof
e Node: $animal
function is_it_duck() {
¢$animal = unserialize($object);
Lf {$animal instanceof Duck) {
echo "It's a duck! \n"
i
```

## Slide 89

### **Type Inference Rules: Known Operators**

Type: **Duck**

● Reason:  instanceof
●
Node:  $animal

Possible classes:  Duck

#BHUSA   @BlackHatEvents

## Slide 90

### **Nested Classes**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Nested Classes
class Human {
public $best_friend;
public function sing() {
echo "Human singing\n";
}
class Cat {
public function meow() {
echo "Cat meowing\n";
class Dog {
public function bark() {
echo "Dog barking\n";
}
}
¢hacker = unserialize($object);
$hacker> ();
$hacker> = QO;
```

## Slide 91

### **Nested Classes**

Type:  Human
●
Reason:  sing  method
●
Node:  $hacker

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Nested Classes
class Human {
Type: Human
public $best_friend; e Reason: sing method
Me eis ined ea: e Node: $hacker
}
}
class Cat {
public function meow() {
echo "Cat meowing\n";
t
}
class Dog {
public function bark() {
echo "Dog barking\n";
t
t
ghackor = wnsorialize($object);
Khackersing();
$hacker—> t end—bark();
```

## Slide 92

### **Nested Classes**

Type: **Human**

●
Reason:  sing  method
●
Node:  $hacker
Type:  Human
● Reason:  best_friend
property
●
Node:  $hacker

#BHUSA   @BlackHatEvents

## Slide 93

### **Nested Classes**

Type: **Human**

- Reason: **sing** method

- ● Node: **$hacker**

- Type: **Human** ● Reason: **best_friend** property

- ● Node: **$hacker**

- Type: **Dog** ● Reason: **bark** method ● Node: **$hacker->best_friend**

#BHUSA   @BlackHatEvents

## Slide 94

### **Nested Classes**

Type: **Human**

- Reason: **sing** method

- ● Node: **$hacker**

- Type: **Human** ● Reason: **best_friend** property

- ● Node: **$hacker**

- Type: **Dog** ● Reason: **bark** method ● Node: **$hacker->best_friend**

Possible classes: **Human, Dog**

#BHUSA   @BlackHatEvents

## Slide 95

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 96

### **Roadmap**

**QUACK Mitigating deserialization exploits with** **_static duck typing_**

**QUACK design goals**

**Identifying available classes**

**Restricting classes with static duck typing Putting it all together**

#BHUSA   @BlackHatEvents

## Slide 97

### **Setting allowed_classes** Available classes

Possible classes

#BHUSA   @BlackHatEvents

## Slide 98

### **Setting allowed_classes**

Available classes

allowed_classes Possible classes

#BHUSA   @BlackHatEvents

## Slide 99

### **Setting allowed_classes**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Setting allowed_classes
foreach ($data['#']['answer'] as $answerxml) {
$ans = $format—import_answer($answerxml);
$options = unserialize($ans—feedback[ 'text']);
$question>choices[] = array(
‘answer' => $ans—ar
wer,
‘choicegroup' => $options—dra
sroun
sroup,
‘infinite' => $options—infinite
);
```

## Slide 100

### **Setting allowed_classes**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Setting allowed_classes
foreach ($data['#']['answer'] as $answerxml) {
ormat—import_answer($answerxml);
= unserialize($ans—feedback['text']);
$options
question—choices[] = array(
‘answer' = $ans—answer,
‘choicegroup' =>] $options—draggroup
‘infinite' > L$options infinite,
);
```

## Slide 101

### **Setting allowed_classes**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Setting allowed_classes
"conditions": [
{
"condType": "Duck",
"field": "infinite",
"reason": "HasField",
"type":
ddimageortext drag
aflow_SourceMetadata
"Google
_ddmarker_drag_item|
_ddwtos_choice",
Trode ra
},
{
"condType":
"field": "d
"reasop
"type"
"nodeld
"avail_classes": [
"Google_Service_SQLAdmin_User",
"HTMLPurifier_AttrDef_CSS_ListStyle",
service AdeychangeSeller_Report",
"Google
"qtype_ddwtos_choice",
ADODB
"Google_Service_YouTube_Watermarks_Resource",
_mssqlnative’,
"moodle1_mod_data_handler",
```

## Slide 102

### **Setting allowed_classes**

#BHUSA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
Setting allowed_classes
foreach ($data['#']['answer'] as $answerxml) {
$ans = $format—import_answer($answerxml);
$options = unserialize(tans—feedbacl ['te £" |.
['allowed_classes' = [qtype_ddwtos_choice::class]]);
$ USSTIOMNSCHOICEST T= array
'answer' => $ans—answer,
'‘choicegroup' => $options—draggroup,
'infinite' => $options—infinite,
yy
```

## Slide 103

## **Demo**

#BHUSA   @BlackHatEvents

## Slide 104

### **Roadmap**

Background QUACK
PHP Mitigating
deserialization  deserialization
exploits exploits with
static duck typing

Takeaways
The future of
QUACK and
deserialization
exploits

#BHUSA   @BlackHatEvents

## Slide 105

### **Roadmap**

Background QUACK Takeaways
PHP Mitigating  The future of
deserialization  deserialization  QUACK and
exploits exploits with  deserialization
static duck typing exploits

#BHUSA   @BlackHatEvents

## Slide 106

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 107

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 108

### **QUACK’s Effectiveness**

**Test setup: Identified 11 applications with CVEs**

**● 15 vulnerable unserialize calls**

**● Automated exploit generation tools automatically generate exploits for 5 CVEs**

**Results:**

**● QUACK blocked** **_all methods_ for 12/15 vulnerable calls ○ Blocked 97% of methods overall**

**● No exploits can be generated**

#BHUSA   @BlackHatEvents

## Slide 109

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 110

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 111

### **QUACK’s Future**

**Battle testing: we want to know where QUACK can help! ● We welcome new users – please raise GitHub issues ● Contributing to Joern’s PHP support helps QUACK, too**

**Improved usability ● Imagine: IDE integration with immediate suggestions for allowed_classes**

#BHUSA   @BlackHatEvents

## Slide 112

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 113

### **Is the Deserialization Problem Solved?**

**QUACK** **_cannot_ prevent “data-only” attacks Always ask: do I** **_need_ this deserialization call? What other mitigations apply to my use case? Other languages? - Java and C# have similar considerations - Python’s pickle is more challenging**

#BHUSA   @BlackHatEvents

## Slide 114

### **Is the Deserialization Problem Solved?**

**QUACK** **_cannot_ prevent “data-only” attacks Always ask: do I** **_need_ this deserialization call? Zhang et al. “Automatic Policy Synthesis and Enforcement What other mitigations apply to my use case? for Protecting Untrusted Deserialization” NDSS ‘24 Other languages? - Java and C# have similar considerations - Python’s pickle is more challenging**

#BHUSA   @BlackHatEvents

## Slide 115

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 116

### **Roadmap**

**Takeaways**

**How well does QUACK work?**

**The future of QUACK and deserialization exploits**

**How can QUACK be improved?**

**Is the deserialization security problem solved? Parting thoughts**

#BHUSA   @BlackHatEvents

## Slide 117

### **BlackHat Sound Bites**

**Attackers exploit deserialization vulns by chaining together object types that the programmer never intended to instantiate**

**QUACK prevents exploits by observing how objects are used to infer and restrict the intended types**

**Developers: only use unserialize calls when needed, and use allowed_classes when you do. QUACK can help :)**

<u>github.com/columbia/quack</u>

Paper: <u>bit.ly/4eInLri</u>

#BHUSA   @BlackHatEvents
