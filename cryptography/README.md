<h1 align="center"> :closed_lock_with_key: CRYPTOGRAPHY :closed_lock_with_key:</h1>

* [Easy1](#easy1):pirate_flag:
* [13](#13):pirate_flag:
* [Mod 26](#mod-26):pirate_flag:
* [Caesar](#caesar):pirate_flag:
* [interencdec](#interencdec):pirate_flag:

:pirate_flag: Flags Captured: 5 / 5 :pirate_flag:

# Easy1
* **Difficulty:** Medium
* **Category:** Cryptography
* **Author:** Alex Fulton/Daniel Tunitis

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


### Solution

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
* **Difficulty:** Easy
* **Category:** Cryptography
* **Author:** Alex Fulton/Daniel Tunitis

### Description

> Cryptography can be easy, do you know what ROT13 is? 
>
> cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}

### Solution

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
# manually created some keys
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

### Description
> Cryptography can be easy, do you know what ROT13 is? 
> cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}

### Solution 

Like previous challenge, we have a ROT13 cipher where you take the 26 letter alphabet and replace each letter with the letter 13 places from that letter.
so "a" (1) becomes "n" (1+13)

This time, I used <a href="https://gchq.github.io/CyberChef/">CyberChef</a> to do the basic decryption. There is a "ROT13" recipe built right into it. 

[!cyberchef screenshot](#/cryptography/assets/screenshots/Mod26_144_1.png)

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



# interencdec
* **Difficulty:** Easy
* **Category:** CRYPTOGRAPHY
* **Tags:** Base64, Caesar
* **Author:** NGIRIMANA Schadrack

### Description
> Can you get the real meaning from this file. Download the file <a href="Can you get the real meaning from this file. Download the file here. ">here</a>. 

> **HINT:** Engaging in various decoding processes is of utmost importance

### Solution
The file provided contains one encrypted string:

`YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6YzRNalV3YUcxcWZRPT0nCg==` 

Based on the tags in the challenge and the little bit I know about Base64, I suspect this is probably a Base64 encoded string.

I using CyberChef's 'From Base64' recipe, the string is decoded to the following: 

`b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ=='` 

From here, I had a little bit of trouble. Based on the hint and tags provided with the challenge, I assumed that this would be a simple caesar decode. It was that, but I skipped a crucial step before running a rot13 decrypt and rot47 decrypt (rot47 rotates through more ascii character to include non-alphanumeric characters). This didn't get me anywhere until I removed the `b'` and `'` at the beginning and end of the decoded string. As soon as I recognized this as Python's byte string syntax, I realized I needed to do the decryption on just the text inside the byte string. 

Running another 'From Base64' decode on the byte string `d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrXzc4MjUwaG1qfQ==` gives us a string that looks like it's finally ready for simple caesar decryption:

`wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}`

[!NOTE]
> In Python binary strings are expressed this way `b'string'`
> Byte string syntax is used before encoding to base64 because the encoding is done on the binary data
> See the <a href ="/general_skills/README.MD#Bases">Bases</a> challenge for a high-level summary on how Base64 encoding works

I ran this string through the cute little brute-force caesar decryptor script I wrote. The flag was printed at rot-19. 

```
$ python3 brute_caesar.py 
 ________   ________   _________   _________
|   _____| |   __   | |   ___   | |   ___   | 
|   |____  |  |__|  | |  |   |  | |  |___|  |
|_____   | |   _____| |  |_\  \ | |   __   _|
 _____|  | |  |       |_____\  \| |  |  \  \
|________| |__| BRUTÉ CAESAR \__\ |__|   \__\ 

Enter the text you want to encrypt / decrypt
>
>wpjvJAM{jhlzhy_k3jy9wa3k_78250hmj}
>
rot-0:wpjvjam{jhlzhy_k3jy9wa3k_78250hmj}
rot-1:xqkwkbn{kimaiz_l3kz9xb3l_78250ink}
rot-2:yrlxlco{ljnbja_m3la9yc3m_78250jol}
rot-3:zsmymdp{mkockb_n3mb9zd3n_78250kpm}
rot-4:atnzneq{nlpdlc_o3nc9ae3o_78250lqn}
rot-5:buoaofr{omqemd_p3od9bf3p_78250mro}
rot-6:cvpbpgs{pnrfne_q3pe9cg3q_78250nsp}
rot-7:dwqcqht{qosgof_r3qf9dh3r_78250otq}
rot-8:exrdriu{rpthpg_s3rg9ei3s_78250pur}
rot-9:fysesjv{squiqh_t3sh9fj3t_78250qvs}
rot-10:gztftkw{trvjri_u3ti9gk3u_78250rwt}
rot-11:haugulx{uswksj_v3uj9hl3v_78250sxu}
rot-12:ibvhvmy{vtxltk_w3vk9im3w_78250tyv}
rot-13:jcwiwnz{wuymul_x3wl9jn3x_78250uzw}
rot-14:kdxjxoa{xvznvm_y3xm9ko3y_78250vax}
rot-15:leykypb{ywaown_z3yn9lp3z_78250wby}
rot-16:mfzlzqc{zxbpxo_a3zo9mq3a_78250xcz}
rot-17:ngamard{aycqyp_b3ap9nr3b_78250yda}
rot-18:ohbnbse{bzdrzq_c3bq9os3c_78250zeb}
rot-19:picoctf{caesar_d3cr9pt3d_78250afc}
rot-20:qjdpdug{dbftbs_e3ds9qu3e_78250bgd}
rot-21:rkeqevh{ecguct_f3et9rv3f_78250che}
rot-22:slfrfwi{fdhvdu_g3fu9sw3g_78250dif}
rot-23:tmgsgxj{geiwev_h3gv9tx3h_78250ejg}
rot-24:unhthyk{hfjxfw_i3hw9uy3i_78250fkh}
rot-25:voiuizl{igkygx_j3ix9vz3j_78250gli}
```

### flag
:pirate_flag:`picoctf{caesar_d3cr9pt3d_78250afc}`:pirate_flag:

<br>

---

<br>