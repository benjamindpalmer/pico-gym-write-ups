# written to solve the 'tapping' picoCTF challenge

mc = {
'A':'.-',
'B':'-...',
'C':'-.-.',
'D':'-..',
'E':'.',
'F':'..-.',
'G':'--.',
'H':'....',
'I':'..',
'J':'.---',
'K':'-.-',
'L':'.-..',
'M':'--',
'N':'-.',
'O':'---',
'P':'.--.',
'Q':'--.-',
'R':'.-.',
'S':'...',
'T':'-',
'U':'..-',
'V':'...-',
'W':'.--',
'X':'-..-',
'Y':'-.--',
'Z':'--..',
'1':'.----',
'2':'..---',
'3':'...--',
'4':'....-',
'5':'.....',
'6':'-....',
'7':'--...',
'8':'---..',
'9':'----.',
'0':'-----'
}

# get dots and dashes on input
ddin = input(f"Enter Morse Code Here: \n")

ddinsplit = ddin.split()
decoded = []
    
def decode_morse(d):
    # loop though the mc items directionary   
    for l, c in mc.items():
        # if the coded string matches the input string
        if d == c:
        # append the cooresponding letter to the output array
            decoded.append(l)

for d in ddinsplit:
    # loop through the inputted morse code strings
    # run the decode method on each
    decode_morse(d)

decoded_string = ''.join(decoded)
print(decoded_string)

        