# written to solve 'hashcrack' picoCTF challenge
# check provided hashes against known passwords 

import hashlib

wordlist = "/users/palm/Downloads/rockyou.txt"
userhash = input("Enter hash to decode:")


# determine hash algorithm based on length of hash
if len(userhash) == 32:
    hash_algo = 'md5'
elif len(userhash) == 40:
    hash_algo = 'sha1'
elif len(userhash) == 64:
    hash_algo = 'sha256'
elif len(userhash) == 128:
    hash_algo = 'sha512'
else:
    print(f"could not find hash algorithm for {userhash}")

# loop through all passwords, get the hash for each, compare with known hash
with open(wordlist, 'r', encoding='ISO-8859-1') as file:
    for word in file:
        word = word.strip() 
        hash = hashlib.new(hash_algo)
        hash.update(word.encode())
        hash_hex = hash.hexdigest()
        print(word)
        print(hash_hex)
        if hash_hex == userhash:
            print(f"the password for hash {userhash} is: \n {word}")
            break
            
    

