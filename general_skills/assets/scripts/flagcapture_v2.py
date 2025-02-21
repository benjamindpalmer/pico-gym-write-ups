#### Written to solve challenge 'PW Crack 5' ####


import hashlib

### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
###############################################################################

# make sure flag_enc and correct_pw_hash are pointing to the right files
flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

#There is no list here, so we need to open dictionary.txt and use it to populate our list
pos_pw_list = open('dictionary.txt', 'r').read().splitlines()

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_5_pw_check():
    #Since the password is already in the script, we don't need to ask for user input. We can comment out the lines below: 

    # user_pw = input("Please enter correct password for flag: ")
    # user_pw_hash = hash_pw(user_pw)

    # We can copy in the loop written for the last few challenges:
    for user_pw in pos_pw_list:
        check_hash = hash_pw(user_pw)
        if( check_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        # print("That password is incorrect")


level_5_pw_check()


