#Crack
---

Crack is a simple hash md5 hash cracking tool.

##Technologies
---

Created with:
* Python 3.8
  * Click
  * Datetime
  * Hashlib
  * Time
  * Colorama
  * Multiprocessing

##Installation
--- 

clone the repo
```git clone https://github.com/Oxyn4/crack.git```

move into the crack directory
```cd crack```

install the dependencies and package 
```pip install -e .```

Follow the usage commands

##Usage
---

Before using understand i dont take responsibility for how you use this tool, 
it should only be used ethicaly and for research or testing security (with permission).

To use crack simply type:
```crack```

you will get an error after entering command as crack requires two arguments

* A text file containg one or more hashes seperated onto different lines with no blank lines

* A wordlist containing potential matches for the password

lets try it with these specified 

```crack example/path/to/hash.txt example/path/to/wordlist```

This repo contains a folder which has a hash.txt file and a wordlist.txt file for testing purposes










