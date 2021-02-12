#Crack
---

Crack is a simple hash md5 hash cracking tool.

##Technologies
---

Created with:
* Python 3.8
  * Argparse
  * Datetime
  * Hashlib

Be sure to install these technologies and libaries before following usage.

##Usage
---

Run using python:

`python crack.py`

You will get an error, as two positional arguments need to be specified:
  * File containing the hash
  * File containing the wordlist
  
Specify them by placing the filepaths after Crack.py like so:

`python crack.py example/path/to/hash.txt example/path/to/wordlist.txt`

Because of this I recomend simplifying this progress by placing both files in the crack folder.

**Note: they must be placed in this order 1: hashfile 2: wordlist**

**Note: the hash in hash file should be placed on line 1 with no spaces**
