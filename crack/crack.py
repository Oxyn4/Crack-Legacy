try:
    from colorama.ansi import Back, Fore
    from datetime import datetime
    import multiprocessing
    import colorama
    import hashlib
    import click 
    import time
except ImportError:
    print("Install required modules listed in README.md or upgrade python.")

# TODO: Add suport for multiple hashes in hash file | add optional param for hash type

colorama.init()

# ! intro text

click.echo("Welcome to...")

time.sleep(1)

click.echo(Fore.GREEN +'''
__________________________________________________________________
|     ______     ______     ______     ______     __  __          |
|    /\  ___\   /\  == \   /\  __ \   /\  ___\   /\ \/ /          |
|    \ \ \____  \ \  __<   \ \  __ \  \ \ \____  \ \  _"-.        |
|     \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\       |
|      \/_____/   \/_/ /_/   \/_/\/_/   \/_____/   \/_/\/_/       |
|_________________________________________________________________|
                                                                    ''')

time.sleep(1)

@click.command()
@click.argument('hash')
@click.argument('wordlist')
def crack(hash, wordlist):
    
    hashfile = open(hash, "r")

    click.echo("By Oxyn4" + " - " + Fore.RED + "use ethically")
    click.echo("")
    click.echo(Fore.WHITE + "Cracking " + Fore.RED + hash + Fore.WHITE + " with " + Fore.RED + wordlist + Fore.WHITE)
    click.echo("")

    time.sleep(1)

    def runhash(hash, wordlist):

        wordlist = open(wordlist, 'r')

        getdate = datetime.today().strftime("%b-%d-%Y")
        gettime = datetime.now().strftime("%H:%M:%S")
        click.echo(f'started cracking: {hash} on  {getdate} at {gettime}:')

        for line in wordlist: # ! Iterate through wordlist convert to hash and compare to desired hash

            hashedline = hashlib.md5(line.encode('utf-8')).hexdigest()

            if str(hashedline) == str(hash): # ! if the hashes are the same print the password
                click.echo("password " + "for " + hash + " is " + line + "finished on " + getdate + " at " + gettime) # ! prints password date and time

                click.echo("")
            
        wordlist.close()
        

    for hashline in hashfile:

        hash = hashline

        wordlist = wordlist

        p = multiprocessing.Process(target=lambda: runhash(hash, wordlist))

        p.start()

    p.join()

    colorama.deinit()

    hashfile.close()

if __name__ == "__main__":
    crack()