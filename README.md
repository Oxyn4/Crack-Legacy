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

Be sure to install these technologies and libaries before following usage.

##Usage
---

Run using python:

`python3 crack.py`

You will get an error, as two positional arguments need to be specified:
  * File containing the hash
  * File containing the wordlist
  
Specify them by placing the filepaths after Crack.py like so:

`python crack.py example/path/to/hash.txt example/path/to/wordlist.txt`
