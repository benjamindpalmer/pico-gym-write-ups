# used to solve 'la cifra de' challenge even though it wasn't necessary. I just wanted to write some pythhon. 

# let's write a little script that can decode vigenere when we know the key. 


with open('encrypted.txt') as f:
    encrypted = f.readlines()

encrypted_text = '' 
encrypted_text = encrypted_text.join(encrypted).upper()
key = input(f"Enter Key: \n")
key = key.upper()

# parse the key into its value on the Vigenere Tableau
# e.g A = 0
parsed_key = []
for letter in key: 
    # find the ord value of the key
    ord_value = ord(letter)
    # subtract the ord value of 'A'
    parsed_key.append(ord_value - 65)

# check to see if a letter is not a letter
def not_a_letter(l):
    if ord(l) < 65:
        return True
    elif ord(l) > 90:
        return True
    else: 
        return False

def decode_string(string, parsed_key):
    decoded = []
    for letter in string:
        if not_a_letter(letter):
            decoded.append(letter)
        else:
            decrypt_value = ord(letter) - parsed_key[0]
            parsed_key.append(parsed_key.pop(parsed_key.index(parsed_key[0])))
            if decrypt_value < 65:
                decrypt_value = decrypt_value + 26
            # get letter from new index value
            l = chr(decrypt_value)
            # add letter to decoded array
            decoded.append(l)
    # join and print
    decoded_text = "".join(decoded)
    print(f"Decrypted Text: {decoded_text}")

decode_string(encrypted_text, parsed_key)