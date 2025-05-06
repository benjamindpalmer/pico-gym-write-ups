<h1 align="center"> :closed_lock_with_key: CRYPTOGRAPHY :closed_lock_with_key:</h1>

* [Easy1](#easy1):pirate_flag:
* [13](#13):pirate_flag:
* [Mod 26](#mod-26):pirate_flag:
* [Caesar](#caesar):pirate_flag:
* [interencdec](#interencdec):pirate_flag:
* [la cifra de](#la-cifra-de) :pirate_flag:
* [Mr Worldwide](#mr-worldwide) :pirate_flag: 
* [substitution0]
* [substitution1]
* [substitution2]


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

# la cifra de
* **Difficulty:** Medium
* **Category:** CRYPTOGRAPHY
* **Author:** Alex Fulton/Daniel Tunitis

### Description
> I found this cipher in an old book. Can you figure out what it says? <br>
> Connect with nc jupiter.challenges.picoctf.org 58295.

> **Hint:** There are tools that make this easy.
### Solution

```
nc jupiter.challenges.picoctf.org 58295
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}

Tnj qixxe wkqw-duhfmkseej ipsiwtpznzn uk l puqjarusahjeii htpnjc hubpvkw, hay rldk fcoaso 1467 be Qpot Gltzndtg Fwbkwei.

Zmp Volpnèxj Nivmpr ox ehkwpfuwp surptorps ifwlki ehk Fwbkwei Jndc uw Llhjcto Htpnjc.

It 1508, Ozhgsyey Ycizmpmozd itapnzjo tnj do-ifwlki eahzwa xjntg (f xazwtx uk dhokeej fwpnfmezx) ehgy hoaqo lgypr hj l cxneiifw curaotjyt uk ehk Atgksèce Inahkw.

Merqlsu’x deityd htzkrje avupaxjo it 1555 fd a itytosfaznzn uk ehk ktryy. Ehk qzwkw saraps uk ehk fwpnfmezx lrk szw ymtfzjo rklflgwwy, hze tnj llvmlbkyd ati ehk nydkc wezypry fce sniej gj mkfys uk l mtjxotnn kkd ahxfde, cmtcn hln hj oilkprkse woys eghs cuwceyuznjjyt.
```

We are given quite a bit of text to decode. That's good. I wasn't sure which cipher was being used here, so I dumped the first couple strings into my favorite LLM and was told I was likely looking at was encrpyted using a Vigenère Cipher. In order to decrypt, a key is needed. What IS a Vigenère Cipher? 

Unlike a Caesar Cipher, where all the text is transposed by X number of letters, a Vigenere Cipher encrypts text using a key. Each letter in the key encryptes one letter in the plaintext by that many spaces. E.g. If the first letter in my plaintext is "A" and the first letter in my key is "L", I'm transposing "A" by "L" spaces and getting "L" for the first letter of my encrypted text. This is a lot easier to visualize for most people as a table of letters as explained in this video: https://www.youtube.com/watch?v=SkJcmCaHqS0&t=13s 

Without using an online tool, where would I begin to make an attempt to find the flag here? Let's look at the part of the text that is in the same format as the flag: hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xf966878l}. We found what is probably the flag here, but it is encrypted.

Knowing "pohzCZK{" = "picoCTF{", we might be able to extrapolate what the key is and use it to decrypt the rest of the flag. The first thing I noticed is that a few letters haven't been transposed at all. For instance, the "C" in "pohzCZK{" lines up perfectly with the "C" in "picoCTF{". This is true for the letter "p" as well. 

**p**ohz**C**ZK{
**p**ico**C**TF{

So we know part of the key is "A" because p + ("a" spaces) = "p". 

I used a <a href="https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table.jpg">vingenere matrix</a>, to the other  encrypted characters to each decrypted character and find the rest of the key.</p>

![Vingenere Matrix](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table.jpg)

| plaintext | encrypted text |  key |
| ---- | ---- | ---- | 
|P | P | A |
|I | O | G |
|C | H | F |
|O | Z | L |
|C | C | A | 
|T | Z | G | 
|F | K | F | 


It looks like the the key is 'FLAG'. How appropriate. From here, I used CyberChef's built in Vingenere Matrix decode to decrypt the text, and it worked. I confirmed 'FLAG' is the right key. However, I couldn't pass up an opportunity to write a bit of python. 

I wrote <a href="/cryptography/assets/scripts/vigenere.py">vingenere.py"</a> which will decrypt any alpha vingenere encoded text provided you have the key handy. 

```
vigenere.py 
Enter Key: 
FLAG
Decrypted Text: IT IS INTERESTING HOW IN HISTORY PEOPLE OFTEN RECEIVE CREDIT FOR THINGS THEY DID NOT CREATE

DURING THE COURSE OF HISTORY, THE VIGENÈRE CIPHER HAS BEEN REINVENTED MANY TIMES

IT WAS FALSELY ATTRIBUTED TO BLAISE DE VIGENÈRE AS IT WAS ORIGINALLY DESCRIBED IN 1553 BY GIOVAN BATTISTA BELLASO IN HIS BOOK LA CIFRA DEL. SIG. GIOVAN BATTISTA BELLASO 

FOR THE IMPLEMENTATION OF THIS CIPHER A TABLE IS FORMED BY SLIDING THE LOWER HALF OF AN ORDINARY ALPHABET FOR AN APPARENTLY RANDOM NUMBER OF PLACES WITH RESPECT TO THE UPPER HALFPICOCTF{B311A50_0R_V1GN3R3_C1PH3RA966878A}

THE FIRST WELL-DOCUMENTED DESCRIPTION OF A POLYALPHABETIC CIPHER HOWEVER, WAS MADE AROUND 1467 BY LEON BATTISTA ALBERTI.

THE VIGENÈRE CIPHER IS THEREFORE SOMETIMES CALLED THE ALBERTI DISC OR ALBERTI CIPHER.

IN 1508, JOHANNES TRITHEMIUS INVENTED THE SO-CALLED TABULA RECTA (A MATRIX OF SHIFTED ALPHABETS) THAT WOULD LATER BE A CRITICAL COMPONENT OF THE VIGENÈRE CIPHER.

BELLASO’S SECOND BOOKLET APPEARED IN 1555 AS A CONTINUATION OF THE FIRST. THE LOWER HALVES OF THE ALPHABETS ARE NOW SHIFTED REGULARLY, BUT THE ALPHABETS AND THE INDEX LETTERS ARE MIXED BY MEANS OF A MNEMONIC KEY PHRASE, WHICH CAN BE DIFFERENT WITH EACH CORRESPONDENT.
```

### flag
:pirate_flag:`picoCTF{B311A50_0R_V1GN3R3_C1PH3RA966878A}`:pirate_flag:

<br>

---

<br>

# Mr-WorldWide
* **Difficulty:** Medium
* **Category:** CRYPTOGRAPHY
* **Author:** Danny

### Description
> A musician left us a <a href="https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt">message</a>. What's it mean?
>

### Solution
<p>message.text looks like it has a list of gps coordinates inside of the 'picoCTF' flag format string. Punching these gps coordinates into google maps will take us to these places. I did two of these before I got bored and started looking at random places in Egypt. 

```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

As fun as it would be copy and paste all of these into google maps, it would be more fun to use a script to just give us the location names. I found this script in a forum <a href="/cryptography/assets/scripts/locations.py">locations.py"</a> and leveraged it to work with the coords in this challenge. Here's what it returned when I fed `locations.py` the list of coordinates.

```
$ python3 locations.py 
(35.028309, 135.753082) : セブン-イレブン, 元誓願寺通, 鷹司町, 東町, 上京区, 京都市, 京都府, 602-0953, 日本
(46.469391, 30.740883) : Лев, Привокзальна площа, Центр, Приморський район, Одеса, Одеська міська громада, Одеський район, Одеська область, 65011, Україна
(39.758949, -84.191605) : Fusion, 20, South Main Street, East Second Street Historic District, Dayton, Montgomery County, Ohio, 45402, United States
(41.015137, 28.97953) : 1, Istasyon Arkası Sokağı, Hocapaşa Mahallesi, Cankurtaran Mahallesi, Fatih, İstanbul, Marmara Bölgesi, 34110, Türkiye
(24.466667, 54.366669) : شارع هزاع بن زايد الأول, الكرامة, المنهل, أبو ظبي, المَنهَل, أبوظبي, أبو ظبي, 109595, الإمارات العربية المتحدة
(3.140853, 101.693207) : Bulatan KTM, Brickfields, Kuala Lumpur, 50000, Malaysia
(9.005401, 38.763611) : ኦሎምፒያ, Addis Ababa / አዲስ አበባ, Kirkos, አዲስ አበባ / Addis Ababa, 111, ኢትዮጵያ
(-3.989038, -79.20356) : Avenida Nueva Loja, Paris, Loja, 110105, Ecuador
(52.377956, 4.89707) : Art'Otel, 33, Prins Hendrikkade, Centrum, Amsterdam, Noord-Holland, Nederland, 1012TM, Nederland
(41.085651, -73.858467) : 276, North Broadway, Sleepy Hollow, Town of Mount Pleasant, Westchester County, New York, 10591, United States
(57.790001, -152.407227) : Rezanof Drive West, Kodiak, Kodiak Island, Alaska, 99615, United States
(31.205753, 29.924526) : كلية الهندسة ، جامعة الإسكندرية, شارع جمال عبد الناصر, كامب شيزار, الشاطبى, الإسكندرية, 21561, مص
```

This is neat but not super helpful, some of the results aren't in English. I ended up just manually googling most of these and copying the city and state next to the GPS coordinates. If you take the first letter of every city name, it spells out `KODIAK_ALASKA`

```
message.txt
-----------

picoCTF{
(35.028309, 135.753082)  - KYOTO JAPAN
(46.469391, 30.740883)   - ODESSA UKRAINE
(41.015137, 28.979530)   - DAYTON OHIO
(39.758949, -84.191605)  - ISTABUL TURKEY
(24.466667, 54.366669)   - ABU DHABI UAE
(3.140853, 101.693207)   - KUALA LUMPUR MALAYSIA
_
(9.005401, 38.763611)    - ADDIS ABABA ኢትዮጵያ
(-3.989038, -79.203560)  - LOJA ECUADOR
(52.377956, 4.897070)    - AMSTERDAM NEDERLAND
(41.085651, -73.858467)  - SLEEPY HOLLOW NEW YORK
(57.790001, -152.407227) - KODIAK ALASKA
(31.205753, 29.924526)}  - ALEXANDRIA EGYPT
```

<p>I learned a little about google APIs in researching ways to get addresses from GPS coordinates before discovering <a href="https://geopy.readthedocs.io/en/stable/index.html#module-geopy.geocoders">GeoPy</a>. GeoPy just leverages the Nominatim API - https://nominatim.org/ It probably would have been less of a headache in this case to manually google search each GPS coordinates. However, even when it's terrible code copied from forums, PYTHON IS FUN.</p> 

### flag
:pirate_flag:picoCTF{KODIAK_ALASKA}`:pirate_flag:

<br>

---

<br>

# Substitution0
* **Difficulty:** Medium
* **Category:** Cryptography
* **Author:** Will Hong

### Description
> A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher? 
> Download the message <a href="https://artifacts.picoctf.net/c/152/message.txt">here</a>.

> **HINT:** Try a frequency attack. An online tool might help.

### Solution

At the bottom of <a href="https://artifacts.picoctf.net/c/152/message.txt">message.txt</a> there is a string that looks just like the flag. 

`Bif mwdy qa: xqcpCBM{5UE5717U710Z_3S0WU710Z_59533D2F}`

Let's start by mapping 'picoCTF{'to part of this string that definitely decrypts to 'picoCTF'. Four lowercase letters, three caps, followed by more text surrounded by curly brackets is definitley our flag. 

| x | q | c | p | C | B | M |
|---|---|---|---|---|---|---|
| p | i | c | o | C | T | F | 


This is interesting, but I doesn't really crack our substitution cipher outside of these letters. This is where frequeny analysis comes in. 

<!NOTE>
- Frequency Analyis involves comparing the relative frequency distribution of letters in ciphertext with the expected frequency distribution of letters in the target language of the plaintext. For instance, in English, we can expect the letter 'e' to make up 12.2% of all letters in plaintext. It follows that any character in our ciphertext (assuming a substitution cipher is being used) that also occurs ~12.2% of the time, likely maps to an 'e'. 
- Frequency Analysis best works when there is a large amount of encrypted data. Small samples of text will break 'normal' frequency distribution rules. 

I found a frequency analysis tool online that shows a graph of the average frequency of letters in English:
![Graph with letters A-Z](https://www.101computing.net/wp/wp-content/uploads/frequency-analysis-english-language.png)


I copied the body of text found in message.txt to that frequency analysis tool and was able to start mapping the letters 'picoCTF' to the letters in the ciphertext. 


![Frequency analysis tool filled out partially](/cryptography/assets/screenshots/substitution0_1.png)

This only got me so far. However, in this challenge we ARE provided with a key at the start of the ciphertext. The Key is *exactly* 26 letters which lead me to try mapping `DECKFMYIQJRWTZPXGNABUSOLVH` to `ABCDEFGHIJKLMNOPQRSTUVWXYZ`. 

|D|E|C|K|F|M|Y|I|Q|J|R|W|T|Z|P|X|G|N|A|B|U|S|O|L|V|H|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---| 
|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|


With the key, it was easy to just fill out the proper substitutions for each letter in the alphabet. I knew I had everything filled out correctly when my key was decrypted to `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

![Frequency analysis tool filled out completely](/cryptography/assets/screenshots/substitution0_2.png)

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ 

HEREUPON LEGRAND AROSE, WITH A GRAVE AND STATELY AIR, AND BROUGHT ME THE BEETLE
FROM A GLASS CASE IN WHICH IT WAS ENCLOSED. IT WAS A BEAUTIFUL SCARABAEUS, AND, AT
THAT TIME, UNKNOWN TO NATURALISTS—OF COURSE A GREAT PRIZE IN A SCIENTIFIC POINT
OF VIEW. THERE WERE TWO ROUND BLACK SPOTS NEAR ONE EXTREMITY OF THE BACK, AND A
LONG ONE NEAR THE OTHER. THE SCALES WERE EXCEEDINGLY HARD AND GLOSSY, WITH ALL THE
APPEARANCE OF BURNISHED GOLD. THE WEIGHT OF THE INSECT WAS VERY REMARKABLE, AND,
TAKING ALL THINGS INTO CONSIDERATION, I COULD HARDLY BLAME JUPITER FOR HIS OPINION
RESPECTING IT.

THE FLAG IS: PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}
```

### flag
:pirate_flag:`PICOCTF{5UB5717U710N_3V0LU710N_59533A2E}`:pirate_flag:

<br>

---

<br>