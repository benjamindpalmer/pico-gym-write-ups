<h1 align="center"> :closed_lock_with_key: CRYPTOGRAPHY :closed_lock_with_key:</h1>

* [Easy1](#easy1)
* [13](#13)
* [Mod 26](#mod-26)


# Easy1
* **Difficulty:** EASY
* **Category:** Cryptography
* **Author:** 

### Description
> The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? 
> We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. 
> Can you use this table to solve it?.
> 


```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
   +----------------------------------------------------
A | A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B | B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C | C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D | D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E | E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F | F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G | G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H | H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I | I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J | J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K | K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L | L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M | M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N | N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O | O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P | P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q | Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R | R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S | S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T | T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U | U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V | V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W | W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X | X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y | Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z | Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```


## Solution

This is called a <a href="https://www.youtube.com/watch?v=SkJcmCaHqS0">Vigenère Cipher</a>. You can use a key and the above table to encrypt/decrypt text.
The cipher text is just the letter by letter interseciton of the plaintext one axis of the table and the key on the other. 
So to decrypt, we start with key on one column and stop on the row with that contains the cipher text. 

Very easy to search for a site that does this automatically, even without knowing the key. But in the spirit of learning I decided to manually decipher (most) of the text. 

Key: `SOLVECRYPTO` <br>
Cipher Text: `UFJKXQZQUNB`

|Key|CT|PT|
|--|--|--|
|S|U|C| 
|O|F|R|
|L|J|Y|
|V|K|P| 
|E|X|T|
|C|Q|O| 
|R|Z|I| 
|Y|Q|S|
|P|U|F| 
|T|N|U|
|O|B|N|

Plain Text: `CRYPTOISFUN`

 :black_flag: **flag:**`picoCTF{CRYPTOISFUN}`


# 13
* **Points:** 100
* **Category:** Cryptography
* **Challenge Year:** 2019

## Description

> Cryptography can be easy, do you know what ROT13 is? 
>
> cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

## Solution

A ROT13 cipher substitues a letter of plaintext with a letter 13 places away from it in the A-Z alphabet. 
Because of this, it works the same both forwards and backwards. 

```
A + 13 = N
N + 13 = A 
```

A ROT26 Cipher would do nothing: 

```
A + 26 = A
```

This challenge can be solved easily by going here: 
- https://rot13.com/

But why do that we when can write some bad code that does the same thing? <br>
I'm using Python's maketrans method below to compare my rot0 string with my rot13 string. <br>
There is probably a much better way to do this. But it was more fun than just going to someone else's site to decipher. 

```python
rot0 = "abcdefghijklmnopqrstuvwxyz"
rot1 = "bcdefghijklmnopqrstuvwxyza"
rot13 = "nopqrstuvwxyzabcdefghijklm"

flag = []
ciphertext = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
string = ciphertext.lower()
print(string)

rot_table = ciphertext.maketrans(rot13, rot0)
print(rot_table)

no_decode = ["_","}","{"]

for letter in string:
    if letter in no_decode:
        flag.append(letter)
    else:
        letter = ord(letter)
        flag.append(chr(rot_table[letter]))

final_flag = "".join(flag)
print(final_flag)
```

:black_flag: **flag:**
`picoCTF{not_too_bad_of_a_problem}`



# Mod 26

* **Difficulty:** EASY
* **Category:** CRYPTOGRAPHY
* **Author:** PANDU

## Description
> Cryptography can be easy, do you know what ROT13 is? 
> cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}

## Solution
Oh! I know this! 

ROT13 is a cipher where you take the 26 letter alphabet and replace each letter with the letter 13 places from that letter.
so "a" (1) becomes "n" (1+13)

used this site instead of manually counting
https://rot13.com/

> [!NOTE]
> [<a href='https://gchq.github.io/CyberChef/'>Cyberchef</a> is a better resource for basic decryptions like this.]

### flag
:pirate_flag:`picoCTF{next_time_I'll_try_2_rounds_of_rot13_aFxtzQWR}`:pirate_flag:

'two rounds of rot13' would be rot26, so `a` would equal `a`. Very funny! 

<br>
---
<br>

# Caesar    
* **Difficulty:** Medium
* **Category:** Cryptography
* **Author:** Sanjay C/Daniel Tunitis

## Description
> Decrypt this <a href= "https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext">message</a>. 
>

## Solution
The file we downloaded from the link above contains the following ciphertext: 
PicoCTF{ynkooejcpdanqxeykjrbdofgkq}

Since the first part of the flag is not encrypted, we don't know how many places our ciphertext is shitfed by. Like the previous challenges, this one can be solved by just using an online tool. However, I wanted to refactor the script I wrote in the last challenge that brute forces through rot values 0 - 26. Also I wanted to practice making some ascii art for fun. 

```python
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
```

This script returned decoded cipher text 26 times (rot 0 - rot 25)

```
rot-0:ynkooejcpdanqxeykjrbdofgkq
rot-1:zolppfkdqeboryfzlkscepghlr
rot-2:apmqqglerfcpszgamltdfqhims
rot-3:bqnrrhmfsgdqtahbnmuegrijnt
rot-4:crossingtherubiconvfhsjkou
rot-5:dspttjohuifsvcjdpowgitklpv
rot-6:etquukpivjgtwdkeqpxhjulmqw
rot-7:furvvlqjwkhuxelfrqyikvmnrx
rot-8:gvswwmrkxlivyfmgsrzjlwnosy
rot-9:hwtxxnslymjwzgnhtsakmxoptz
rot-10:ixuyyotmznkxahoiutblnypqua
rot-11:jyvzzpunaolybipjvucmozqrvb
rot-12:kzwaaqvobpmzcjqkwvdnparswc
rot-13:laxbbrwpcqnadkrlxweoqbstxd
rot-14:mbyccsxqdrobelsmyxfprctuye
rot-15:nczddtyrespcfmtnzygqsduvzf
rot-16:odaeeuzsftqdgnuoazhrtevwag
rot-17:pebffvatgurehovpbaisufwxbh
rot-18:qfcggwbuhvsfipwqcbjtvgxyci
rot-19:rgdhhxcviwtgjqxrdckuwhyzdj
rot-20:sheiiydwjxuhkrysedlvxizaek
rot-21:tifjjzexkyvilsztfemwyjabfl
rot-22:ujgkkafylzwjmtaugfnxzkbcgm
rot-23:vkhllbgzmaxknubvhgoyalcdhn
rot-24:wlimmchanbylovcwihpzbmdeio
rot-25:xmjnndiboczmpwdxjiqacnefjp
```

From here, it was easy to grab the string that was actually human readable. *rot-4:crossingtherubiconvfhsjkou*
Again, easy to solve online but you can probably tell I had fun here :nerd-glases:


### Flag
:pirate_flag: **flag:**`picoCTF{crossingtherubiconvfhsjkou}`:pirate_flag:

# title
* **Difficulty:** 
* **Category:** CRYPTOGRAPHY
* **Author:** 

### Description
>

### Solution


### flag
:pirate_flag: :pirate_flag:

<br>
---
<br>

