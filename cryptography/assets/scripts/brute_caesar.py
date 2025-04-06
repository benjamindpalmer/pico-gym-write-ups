# written to solve various pico ctf challenges that use basic caesar cipher encryption

import re

title = """\
 ________   ________   _________   _________
|   _____| |   __   | |   ___   | |   ___   | 
|   |____  |  |__|  | |  |   |  | |  |___|  |
|_____   | |   _____| |  |_\  \ | |   __   _|
 _____|  | |  |       |_____\  \| |  |  \  \\
|________| |__| BRUTÉ CAESAR \__\ |__|   \__\ """


# check to see if a letter is not a letter
def not_a_letter(string):
    return re.match('[^a-z,A-Z]', string)


# encode / decode a string based a single rot value
def decode_string(string, rot):
    decoded = []
    # loop through the string
    for letter in string:
        # check if actually a letter
        if not_a_letter(letter):
            # add to the output without encoding 
            decoded.append(letter)
        else:
            # get new ord based on the rot value
            ord_value = ord(letter) + rot
            if ord_value > 122:
                ord_value -= 26
            else:
                ord_value
            # get letter from new index value
            l = chr(ord_value)
            # add letter to decoded array
            decoded.append(l)
    # join and print
    decoded_text = "".join(decoded)
    print(f"rot-{rot}:{decoded_text}")


def run_program():
    print(f"{title}\n")
    while True:
        print("Enter the text you want to encrypt / decrypt")
        print(">")
        ciphertext = input(">")
        print(">")
        if ciphertext == "q":
            exit(0)
        else:
            my_string = ciphertext.lower()      
            for rot in range(0, 26):
                decode_string(my_string, rot)


run_program()
