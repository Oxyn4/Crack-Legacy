try:
    import argparse as ap
    from datetime import datetime
    import hashlib
    import multiprocessing # ? potetnially use this for multiple hash cracking at once
except ImportError:
    print("Install required modules listed in README.md or upgrade python.")

# TODO: Add suport for multiple hashes in hash file | add optional param for hash type

parser = ap.ArgumentParser(description="A simple password cracker", epilog="After inputing both arguments then run")

parser.add_argument('hashfile', help="Text file containing hash to be cracked.")

parser.add_argument('wordlist', help="Path to the desired wordlist")

# ? implement optional param for hash type here

args = parser.parse_args()

def crackpassword(hash, wordlist):
    hashfile = open(hash, "r") # ! open hash file

    hash = hashfile.readline() # ! get hash and save as variable
    print(f"found {hash} hash")

    hashfile.close()

    wordlist = open(wordlist, "r") # ! open wordlist 

    count = 0

    getdate = datetime.today().strftime("%b-%d-%Y")
    gettime = datetime.now().strftime("%H:%M:%S")
    print(f'started on {getdate} at {gettime}:')

    for line in wordlist: # ! Iterate through wordlist convert to hash and compare to desired hash
        count += 1

        hashedline = hashlib.md5(line.encode()).hexdigest()

        if str(hashedline) == str(hash): # ! if the hashes are the same print the password
            print("password is" + line + "finished on " + getdate + " at " + gettime) # ! prints password date and time 

    return ""

    wordlist.close()

if __name__ == '__main__': # ! runs this when program stars
    crackpassword(args.hashfile, args.wordlist)

# ? Basic usage: python3 crack.py testingtools/hash.txt testingtools/wordlist.txt

