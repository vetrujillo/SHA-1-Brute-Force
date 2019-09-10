#!/usr/bin/python3.6

#Simple SHA-1 Brute Force program. Tutorial used: https://null-byte.wonderhowto.com/how-to/use-beginner-python-build-brute-force-tool-for-sha-1-hashes-0185455/

from urllib.request import urlopen, hashlib
#Creates variable set to user input
sha1hash = input("Input hash to crack.\n>")
#Uses urlopen to read provided url containing common passwords. The data from the url is first encoded as utf-8, then stringified using str()
common_pw_list = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#Creates new variable using for loop and the common_pw_list variable. Since the data in common_pw_list are separated by new lines, split('\n') is used to ensure the for loop correctly assigns guess a new value after each line.
for guess in common_pw_list.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print('Password guess ' + str(guess) + ' does not match. Trying next in list')
print("Password not in database")