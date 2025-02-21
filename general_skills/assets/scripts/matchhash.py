#### Used to solve challenge 'PW Crack 3' ####

import hashlib

correct_pw_hash = open('level3.hash.bin', 'rb').read()
print(correct_pw_hash)

# array of possible correct passwords found in level3.py
pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

# pulled this function from level3.py 
# leveraging this to hash passwords from the possible password list 
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

# loop through pos_pw_list array
# check if matches correct_pw_hash from level3.hash.bin
for pw in pos_pw_list:
    check_hash = hash_pw(pw)
    if check_hash == correct_pw_hash:
        print(f'Matching hash: \n {check_hash}')
        print(f'The password is {pw}')
        quit()

