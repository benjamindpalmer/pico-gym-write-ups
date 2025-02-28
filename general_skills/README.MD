<h1 align="center"> :computer: GENERAL SKILLS :computer:</h1>

:pirate_flag: Flags Captured: 20 / 51 :pirate_flag:

- [Obedient Cat](#obedient-cat) :pirate_flag: 
- [Super SSH](#super-ssh) :pirate_flag: 
- [what's a net cat?](#whats-a-net-cat) :pirate_flag:
- [Lets Warm Up](#lets-warm-up):pirate_flag:
- [Warmed Up](#warmed-up) :pirate_flag: 
- [2 Warm](#2warm) :pirate_flag: 
- [Bases](#bases) :pirate_flag: 
- [Wave a flag](#wave-a-flag) :pirate_flag: 
- [Tab, Tab, Attack](#tab-tab-attack) :pirate_flag: 
- [First grep](#first-grep) :pirate_flag: 
- [strings it](#strings-it) :pirate_flag: 
- [Python Wragling](#python-wrangling) :pirate_flag:
- [PW Crack 1](#pw-crack-1) :pirate_flag:
- [PW Crack 2](#pw-crack-2) :pirate_flag:
- [PW Crack 3](#pw-crack-3) :pirate_flag:
- [PW Crack 4](#pw-crack-4) :pirate_flag:
- [PW Crack 5](#pw-crack-5) :pirate_flag:
- [Nice netcat...](#Nice-netcat...) :pirate_flag:
- [Binary Search](#binary-search) :pirate_flag:
- [Codebook](#codebook) :pirate_flag:
- [Convertme.py](#convertme.py) :pirate_flag:
- [runme.py](#runme.py) :pirate_flag:
- [HashingJobApp](#hasingjobapp) :pirate_flag:
- [Serpentine](#serpentine) :pirate_flag:
- [Plumbing](#plumbing):pirate_flag:
- [Time Machine](#time-machine) :pirate_flag:
- [Commitment Issues](#commitment-issues):pirate_flag:
- [Collaborative Development](#collaborative-developement) :pirate_flag:
- [Blame Game](#blame-game) :pirate_flag:
- [First Find](#first-find) :pirate_flag:
- [Big Zip](#big-zip) :pirate_flag:
- [Glitch Cat](#glitch-cat) :pirate_flag:
- [fixme1.py](#fixme1) 
- [fixme2.py](#fixme2) 
- [Magikarp Ground Mission](#magikarp-ground-mission)
- [Static ain't always noise](#static-ain't-always-noise)
- [useless](#useless)
- [Based](#based)



# Obedient Cat 

* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
>This file has a flag in plain sight (aka "in-the-clear"). <a href="https://mercury.picoctf.net/static/2d24d50b4ebed90c704575627f1f57b2/flag">Download flag.</a>

### Solution
Clicked on the 'Download flag' link in the challenge description. This downloaded a text file called 'flag' which contained the flag: 
`picoCTF{s4n1ty_v3r1f13d_f28ac910}`

Learned how to add this stuff to Github so I can document more interesting challenges. Created a Repo called PicoCTF-write-ups and am starting to add solved challenges here. I want to write from the perspective of someone who is new to all of these concepts (because it most cases, I suspect most of the concepts in these challenges will be new to me) to track my own personal growth and encourage others who are starting at a similar place. 

**Quick Git Cheat Sheet:**
* `git add 'file'` - stage a specific file to commit
* `git add -u` adds all modifed files changes to the stage
* `git add *` adds all modified and any new files that aren't gitignored')
* `git commit 'file' -m "commit message"` - commit with message
* `git push origin master` - push changes to master

### Flag
:pirate_flag:`picoCTF{s4n1ty_v3r1f13d_f28ac910}`:pirate_flag:

<br>

---

<br>

# Super SSH
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** JEFFERY JOHN

### Description
>Using a Secure Shell (SSH) is going to be pretty important. Can you ssh as ctf-player to titan.picoctf.net at port 62323 to get the flag? You'll also need the password 6dd28e9b. If asked, accept the fingerprint with yes. If your device doesn't have a shell, you can use: https://webshell.picoctf.org If you're not sure what a shell is, check out our Primer: https://primer.picoctf.com/#_the_shell

### Solution

SSH or 'Secure Shell' is a protocol that allows you to access another machine and share data. In this challenge, you're simply asked to use SSH to call a specific webhost.

Syntax is important here. I'm command line proficient but I can never remember ssh syntax. 

> [!NOTE]
> [SSH Syntax: `ssh {user}@{webhost} -p {port}`]

The challenge wants us to ssh to webhost 'titan.picoctf.net' at port '62323' as user 'ctf-player'. After a quick syntax refresh (after a failed attempt or two at remembering the syntax) I opened my terminal and entered the following to get the flag. 

```
~ % ssh ctf-player@titan.picoctf.net -p 62323
ctf-player@titan.picoctf.net's password: 
Welcome ctf-player, here's your flag: picoCTF{s3cur3_c0nn3ct10n_5d09a462}
Connection to titan.picoctf.net closed.
```

### flag
:pirate_flag:`picoCTF{s3cur3_c0nn3ct10n_5d09a462}`:pirate_flag:

<br>
---
<br>

# whats a net cat
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 25103 to get the flag?

### Solution
Here you you can just open up your shell or pico's webshell and use `nc` to call the url and port to get the flag.

```
s0ren-picoctf@webshell:~$ nc jupiter.challenges.picoctf.org 25103
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_d0c64587}
```

I have a lot of questions about what net cat is actually used for. Most of the tutorials I've run into sofar online present this tool in a nefarious context as a means to set up a <a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md">reverse shell</a>. However, this security company blog outlines use by network admins and has a handy 'cheat sheet' that I'll likely need to reference in future challenges. 

https://www.varonis.com/blog/netcat-commands/

### flag
:pirate_flag:`picoCTF{nEtCat_Mast3ry_d0c64587}`:pirate_flag:

<br>
---
<br>

# Lets warm up
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

### Solution: 
We can solve this one quickly by using Cyberchef's 'From Hex Recipe' to get the character value of 0x70. Inputting `70` gives us a charcter value `p`
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NzA

|Hex|Decimal|ASCII Char|
|---|---|---|
|70|112|p|

### Flag
:pirate_flag:`picoCTF{p}`:pirate_flag:


<br>


# Warmed Up
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> What is 0x3D (base 16) in decimal (base 10)?

### Solution
There are a lot of conversion calculators online and I was able to use one of these to convert '3D' in base 16 to '61'

But what does this mean? 

A Base 10 model would look like this:

`0 1 2 3 4 5 6 7 8 9`

A Base 16 model looks like this: 

`0 1 2 3 4 5 6 7 8 9 A B C D E F `

So "Base 16" and "Hexidecimal" mean the same thing. 

Hexidecimal is easier to convert into Binary than decimal. There is a good line from this wikipedia article that explains this: 

> For example, a single byte can have values ranging from 00000000 to 11111111 in binary form, which can be conveniently represented as 00 to FF in hexadecimal.
> - https://en.wikipedia.org/wiki/Hexadecimal


Referred to this chart to confirm "Base 16" 0x3D is "61" in decimal.
* https://www.asciitable.com/

### flag
:pirate_flag:`picoCTF{61}`:pirate_flag:

<br>
---
<br>

# 2Warm
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> Can you convert the number 42 (base 10) to binary (base 2)? 

### Solution
As previously discovered, it's much easier to convert to binary from hexidecimal (base 16) rather than decimal (base 10).

Using our handy (but ugly) table at https://www.asciitable.com/ we can convert 42 to '2A' in base 16. 

Again, we're in a situation where I *could* just use an online tool to convert '2A' to binary, but I want to understand a little more about how this conversion actually happens.  

https://owlcation.com/stem/How-to-Convert-Hex-to-Binary-and-Binary-to-Hexadecimal

|Hex|Binary|
|--|--|
|0|0|
|1|0|
|2|10|
|3|11|
|4|100|
|5|101|
|6|110|
|7|111|
|8|1000|
|9|1001|
|A|1010|
|B|1011|
|C|1100|
|D|1101|
|E|1110|
|F|1111|

> Hex is very easy to convert to binary.

> 1. Write down the hex number and represent each hex digit by its binary equivalent number from the table above.
> 2. Use 4 digits and add insignificant leading zeros if the binary number has less than 4 digits. E.g. Write 102 (2 decimal) as 00102.
> 3. Then concatenate or string all the digits together.
> 4. Discard any leading zeros at the left of the binary number.

So using the table 
2 = 10
A = 1010

|Base 10|Base 16|Base 2|
|------|-----|-----|
|42|2A|101010|

> [!NOTE]
> [PicoCTF recommends the <a href="https://gchq.github.io/CyberChef/">CyberChef</a> tool for simple conversions like this.]

### flag
:pirate_flag:`picoCTF{101010}`:pirate_flag:

<br>
---
<br>

# Bases
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

### Solution
You can run `bDNhcm5fdGgzX3IwcDM1` through an online Base64 decoder <a href="https://www.base64decode.org/">like this one</a> to get the flag easily. 

But that leaves us with a lot of questions. What *is* Base 64? How is Base 64 encoded / encoded? What is Base 64 used for? 

These questions took me down a little rabbit hole of internet history that I'll *attempt* to summarize here.  

Email was first developed in the early days of the internet and only 7bit characters (0-128) could be sent over it. 128 characters isn't a lot. A-Z,a-z,0-9 uses 62 characters alone, and when you consider languages that aren't english you start to run out of 7bit characters really fast. A bigger problem was that if I wanted to send an 8-bit file over email (which only takes 7 bits) there wasn't a way to do that. This is where base 64 comes in. You get an extra character with base64, but it's 7 bit compatable. 

Base64 takes 8bits of data and encodes it into a 7bit compatible format with the following process. 
1. Takes the Ascii values of three characters and converts them into 8 bit bytes
2. Concatenates those bits into a 24 bit string. 
3. Takes that 24 bit string and breaks it into four 6 bit "bytes" (6^2 = 64)
4. Takes the decimal values of those 6 bit bytes returns a character based on the Base64 index table. 

![Image of Base64 Index Table](/general_skills/assets/images/Base64_index.png) 

Using the Base 64 index table let's manually decode the first four characters into the first three ascii characters of the flag (`bDNh`). 

#### **1. Find the index value of each character and then convert that into the 6 bit value.**

|base64 char|index value|6 bit value| 
|------|-----|-----|
|b|27|011011|
D|3|000011
N|13|001101
h|33|100001

#### **2. Concatenate into those four 6 bit strings a 24 bit string:**
<br>011011000011001101100001

#### **3. Convert back into 8 bit bytes:**
01101100 
00110011 
01100001

#### **4. Convert those bytes into their decimal values and then user our <a href="https://www.asciitable.com/">handy ascii table</a> to find the letter:**

|Byte|Decimal Value|Decoded ASCII|
|----|----|----|
|01101100|108|l|
|00110011|51|3|
|01100001|97|a|

So we've successfully converted the base64 string `bDHn` into the ASCII string `l3a`, which is the first part of the flag.

Knowing that I *could* continue this process, I'm more comfortable with using an existing decoder to finish the rest of the process. 

Sources: 
<ul>
<li>https://www.base64decode.org/</li>
<li>https://www.youtube.com/watch?v=8qkxeZmKmOY</li>
<li>https://allthewebtools.com/base64-encode#base64_index_table</li>
</ul>


### flag
:pirate_flag:`picoCTF{l3arn_th3_r0p35}`:pirate_flag:

<br>
---
<br>

# Wave a flag
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
> Can you invoke help flags for a tool or binary? <a href="https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm">This program</a> has extraordinarily helpful information...

> HINT: This program will only work in the webshell or another Linux computer.

### Solution
Header of the file starts with 'ELF' 'executable and linkable format'. 

Tried running the file in the terminal but 'Permission denied' was returned

```
$ ./warm
-bash: ./warm: Permission denied
```

Looks like I just need to change the permissions of `warm` so that it can be executed. This can be done by running the `chmod` command. 

```
$ chmod +x warm
$ ./warm
-bash: ./warm: cannot execute binary file
```

cannot execute binary file? What does this mean?! I did a little digging and it looks like the file is ONLY for GNU/Linux. 
I thought all unix operating systems (Mac OS) could generally run the same files, but the `warm` binary is specifically for GNU/Linux. 

```
$ file warm
warm: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=b11c22752c901adc13ba1ce86eda9d5516f22763, with debug_info, not stripped
```

> [!NOTE]
> [Different processors and OS software need different binaries. This challenge can only be completed on a linux box or in the PicoCTF webshell. Refer to Hint 1 in the challenge]

Using the webshell made this easy. Give the file execute permissions. Run it with a `-h` argument. 

```
s0ren-picoctf@webshell:~$ chmod +x warm
s0ren-picoctf@webshell:~$ ./warm
Hello user! Pass me a -h to learn what I can do!
s0ren-picoctf@webshell:~$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: <br> picoCTF{b1scu1ts_4nd_gr4vy_d6969390}
```

### flag
:pirate_flag:`picoCTF{b1scu1ts_4nd_gr4vy_d6969390}`:pirate_flag:

<br>
---
<br>

# Tab, Tab, Attack
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
>Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: <a href="https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip">Addadshashanammu.zip</a>

### Solution

Use CD to change directories and keep hitting tab hit tab to see all of the sub directories

```
s0ren-picoctf@webshell:~$ cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
```

There no more subdirectories inside `Ularradallaku` so let's run `ls` to see what's in there. 

```
s0ren-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/As
surnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ls
fang-of-haynekhtnamet
s0ren-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/As
surnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ file fang-of-haynekhtnamet 
fang-of-haynekhtnamet: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=55548d0314fdf7999b966728d19712cdf8a52e58, not stripped
```

Cool! Another executable. Let's run it to get the flag. 

```
s0ren-picoctf@webshell:~/Addadshashanammu/Almurbalarammi/Ashalmimilkala/As
surnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku$ ./fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}
```


### flag
:pirate_flag:picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}:pirate_flag:

<br>
---
<br>

# First Grep
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** ALEX FULTON/DANNY TUNITIS

### Description
> Can you find the flag in <a href="https://jupiter.challenges.picoctf.org/static/315d3325dc668ab7f1af9194f2de7e7a/file">file</a>? This would be really tedious to look through manually, something tells me there is a better way.

### Solution
If you just open this file and look at it, you should be able to find the flag visually. But this is supposed to be a lesson on grep, which I've found extremely useful in my working career. So let's use grep here.  What **is** grep? <br>

Grep is a great way to find things within files and across multiple files at once. <br>
I like to think of it as a `ctrl+f` that doesn't require you to even open the file that you're searching in. <br>
The genesis of GREP has to do with early text editors using regular expressions with those text editors. <br>

The GREP origin story. This is an interesting video:<br>
https://www.youtube.com/watch?v=NTfOnGZUZDk

* g/re/p
* $\color{Green}{global}$/$\color{yellow}{regex}$/$\color{red}{print}$

Was able to solve this challenge by downloading the file and "grepping?" for the beginning of the flag. Since all flags start with `picoCTF` I figured that would be a good string to use. 

```
s0ren$ grep picoCTF file
picoCTF{grep_is_good_to_find_things_f77e0797}
```

### flag
:pirate_flag:picoCTF{grep_is_good_to_find_things_f77e0797}:pirate_flag:

<br>
---
<br>

# strings it
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SANJAY C/DANNY TUNITIS

### Description
> Can you find the <a href="https://jupiter.challenges.picoctf.org/static/94d00153b0057d37da225ee79a846c62/strings">flag</a> in file without running it?

> HINT: <a href="https://linux.die.net/man/1/strings">strings</a>

### Solution
The file is super ugly. 

![screenshot of strings file](/general_skills/assets/images/strings.png)

grep is a neat way to find things in files. Let's try it here. 

```
$ grep picoCTF strings
Binary file strings matches
```

Huh. So that wasn't completely useless. Grep did *something* and returned 'Binary file strings matches'. So that means we know that the string "picoCTF" exists in the file right? 
I greped for different text and nothing was returned. Looks like "Binary file strings matches" is a common grep error when a file begins with non-text data. 

https://unix.stackexchange.com/questions/335716/grep-returns-binary-file-standard-input-matches-when-trying-to-find-a-string


Let's take a look at the HINT provided, which links to a linux man page on the 'strings' function It looks like strings will "*print the strings of printable characters in files.*" Let's try it! 

```
s0ren-picoctf@webshell:~$ strings strings
```

This returned a TON of strings. Too many strings. Let's save the output of the `strings` function to a file and then use `grep` to search that file for the string that contains `'picoCTF'`


```
s0ren-picoctf@webshell:~$ strings strings >> mystrings.txt
s0ren-picoctf@webshell:~$ grep picoCTF mystrings.txt 
picoCTF{5tRIng5_1T_d66c7bb7}
```

> [!NOTE]
> [Using the >> operator allows you redirect all output and append it to a file. In this case I wanted to append all of the output from the strings function to a file called mystrings.txt]

And there's our flag. There's probably some parameters to use the `strings` function to narrow down what it returns, but this way works too. 

### flag
:pirate_flag:`picoCTF{5tRIng5_1T_d66c7bb7`:pirate_flag:

<br>
---
<br>

# Python Wrangling
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
> Python scripts are invoked kind of like programs in the Terminal... Can you run this <a href="https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py">Python script</a> using this <a href="https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/pw.txt">password</a> to get <a href="https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/flag.txt.en">the flag</a>?

### Solution

This challenge is just mean to walk you through how to run python scripts. We're given three files. A password file, a flag file, and the python script. 

Let's use the command `cat` to take a look at the `pw.txt` file. 

```
s0ren-picoctf@webshell:~$ cat pw.txt
6008014f6008014f6008014f6008014f
```

Next let's take a look at the `flag.txt.en` file to see what's in there. Looks encrypted. 

```
s0ren-picoctf@webshell:~$ cat flag.txt.en 
gAAAAABgUAIVI-r3OTKrDSgUJ8i3N9OzjacXZ1w4Hua00I_-Bg7gZu9Fld-TFYRiUiZlkLkChceqqpL9XnGOMO-W2-lRXpFhTkrqk9fHAvDfNkZHuZcjGPpG4xaR4mPnagzSNIrtL9tKs0ren-pi
```

When we try to run the python script, we get a useful message printed. It looks like this program takes two arguments: `e` or `d` and should be pointed at a file. 

```
$ python ende.py 
Usage: ende.py (-e/-d) [file]
```
With that in mind, we can run the program again with an argument, pointed at the `flag.txt.en` file. 

```
s0ren-picoctf@webshell:~$ python ende.py -d flag.txt.en
Please enter the password:6008014f6008014f6008014f6008014f
picoCTF{4p0110_1n_7h3_h0us3_6008014f}
```

After entering the password we got from the `pw.txt` file. The flag is returned.


### flag
:pirate_flag:`4p0110_1n_7h3_h0us3_6008014f`:pirate_flag:

<br>
---
<br>


# PW Crack 1
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Can you crack the password to get the flag?<br>
> Download the password checker <a href="https://artifacts.picoctf.net/c/52/level1.py">here</a> and you'll need the encrypted <a href="https://artifacts.picoctf.net/c/52/level1.flag.txt.enc">flag</a> in the same directory too.

### Solution
<p>With both the  pulled down locally, run the python file. It asks for a password. We know the password is `1e1a` because it is written in plaintext in the python file `level1.py`</p>

```
$ python3 level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
```

<p>If we open up `level1.py`in a text editor, we can see the password in plaintext in the `level_1_pw_check` method.</p>


```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "1e1a"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```


### Flag
:pirate_flag:`picoCTF{545h_r1ng1ng_fa343060}`:pirate_flag:

<br>
---
<br>

# PW Crack 2
* **Difficulty:** $\color{Green}{EASY}$
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Can you crack the password to get the flag? <br>
> Download the password checker <a href="https://artifacts.picoctf.net/c/18/level2.py">here</a> and you'll need the encrypted <a href="https://artifacts.picoctf.net/c/18/level2.flag.txt.enc">flag</a> in the same directory too.

### Solution
Opened the `level2.py` file in a text editor. This time instead of a plaintext password, the user_pw value is endoded in decimal format. 

```
def level_2_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), user_pw)
        print(decryption)
        return
    print("That password is incorrect")
```

`if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):`We can print this out in the python interpreter to get the plaintext password: `39ce`

```
$ python3
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))
39ce
```
With the password `39ce` now we just run the python script and enter the password to get the flag. 

```
$ python3 level2.py
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
```

### Flag
:pirate_flag:`picoCTF{tr45h_51ng1ng_502ec42e}`:pirate_flag:

<br>
---
<br>


# PW Crack 3
* **Difficulty:** $\color{Yellow}{MEDIUM}$
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Can you crack the password to get the flag? <br>
> Download the password checker <a href="https://artifacts.picoctf.net/c/23/level3.py">here</a> and you'll need the encrypted <a href="https://artifacts.picoctf.net/c/23/level3.flag.txt.enc">flag</a> and the <a href="https://artifacts.picoctf.net/c/23/level3.hash.bin">hash</a> in the same directory too. <br>
> There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.

### Solution
<p>The level3.py script has most of the pieces we need to solve this:</p>

<p>1. We have a list of all the possible passwords. We could just manually try each potential password from the array of potential passwords in the script, but that isn't sexy at all. Doing things manually is not fun.</p>

```python
# The strings below are 7 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]
```

<p>2. We have a nice function provided that just hashes input from the user. We can use this to take possible passwords from `pos_pw_list` array instead.</p>

```
def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()
```

<p>3. We were given a file called level3.hash.bin. The code to open it is also in the level3.py script. Convenient!</p>
correct_pw_hash = open('level3.hash.bin', 'rb').read()

<p>Originally I started writing a script from scratch, but had difficulty getting hashes in a format that would match level3.hash.bin. Luckly we are given everything we need to write a script that does the following:</p>

1. Loop through each possible password
2. Hash the possible password
3. Compare that hash with the hash from `level3.hash.bin`

Wrote `matchhash.py` with all of the above elements, plus a little loop that ties everything together. Ran the script to get the password.

```python
import hashlib


correct_pw_hash = open('level3.hash.bin', 'rb').read()
print(correct_pw_hash)


pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]


# pulled this function from the provided level3.py file
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

```

<p>Looks alright! let's run it!</p>

```
$ python3 returnhash.py 
b'\x03\x07\x81y\xea>\x83\x07V \xb5\xed\x18\xf9X\x94'
Matching hash: 
 b'\x03\x07\x81y\xea>\x83\x07V \xb5\xed\x18\xf9X\x94'
The password is 4b17
```

<p>We have our password: `4b17`! Now we can run the level3.py script and enter the password to get the flag!</p>

```
$ python3 level3.py
Please enter correct password for flag: 4b17
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_2b072a90}
```


### Flag
:pirate_flag:`picoCTF{m45h_fl1ng1ng_2b072a90}`:pirate_flag:

<br>
---
<br>

# PW Crack 4
* **Difficulty:** $\color{YELLOW}{MEDIUM}$
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Can you crack the password to get the flag? <br>
> Download the password checker <a href="https://artifacts.picoctf.net/c/59/level4.py">here</a> and you'll need the encrypted <a href="https://artifacts.picoctf.net/c/59/level4.flag.txt.enc">flag</a> and the <a href="https://artifacts.picoctf.net/c/59/level4.hash.bin">hash</a> in the same directory too. <br>
> There are 100 potential passwords with 1 being correct. You can find these by examining the password checker script.<br>
>
>Hint: A for loop can help you do many things very quickly

### Solution
<p>Because we didn't cut any corners in the previous challenge, we can apply the same exact strategy here. All of the work is already done! The only difference is that this time the pos_pw_list has 100 potential passwords. We're forced to automate or be extremely lame.</p>

```
# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]
```

<p>We could just update the pos_pw_list list in matchhash.py (from the previous challenge) to include all 100 potential passwords. But that script only gives us the password. We want the **flag**. So why not just own the entire script so that when we run it gives us the flag?</p>


<p>To do *that* we just need to add a loop that loops through the entire pos_pw_list and comment out the lines that ask for user input</p>


```
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

flag_enc = open('level4.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level4.hash.bin', 'rb').read()

# The strings below are 100 possibilities for the correct password. 
#   (Only 1 is correct)
pos_pw_list = ["158f", "1655", "d21e", "4966", "ed69", "1010", "dded", "844c", "40ab", "a948", "156c", "ab7f", "4a5f", "e38c", "ba12", "f7fd", "d780", "4f4d", "5ba1", "96c5", "55b9", "8a67", "d32b", "aa7a", "514b", "e4e1", "1230", "cd19", "d6dd", "b01f", "fd2f", "7587", "86c2", "d7b8", "55a2", "b77c", "7ffe", "4420", "e0ee", "d8fb", "d748", "b0fe", "2a37", "a638", "52db", "51b7", "5526", "40ed", "5356", "6ad4", "2ddd", "177d", "84ae", "cf88", "97a3", "17ad", "7124", "eff2", "e373", "c974", "7689", "b8b2", "e899", "d042", "47d9", "cca9", "ab2a", "de77", "4654", "9ecb", "ab6e", "bb8e", "b76b", "d661", "63f8", "7095", "567e", "b837", "2b80", "ad4f", "c514", "ffa4", "fc37", "7254", "b48b", "d38b", "a02b", "ec6c", "eacc", "8b70", "b03e", "1b36", "81ff", "77e4", "dbe6", "59d9", "fd6a", "5653", "8b95", "d0e5"]

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def level_4_pw_check():
    '''Since the password is already in the script, we don't need to ask for user input. 
    We can comment out the lines below: 
    '''
    # user_pw = input("Please enter correct password for flag: ")
    # user_pw_hash = hash_pw(user_pw)

    '''We can copy in our loop from the last challenge:'''
    for user_pw in pos_pw_list:
        check_hash = hash_pw(user_pw)
        if( check_hash == correct_pw_hash ):
            print("Welcome back... your flag, user:")
            decryption = str_xor(flag_enc.decode(), user_pw)
            print(decryption)
            return
        print("That password is incorrect")



level_4_pw_check()
```

<p>Running the modified version of level4.py script, the flag is just printed out!</p>


```
$ python3 flagcapture.py 
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
That password is incorrect
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_cf341ff1}
```

### Flag
:pirate_flag:`picoCTF{fl45h_5pr1ng1ng_cf341ff1}`:pirate_flag:

<br>
---
<br>

# PW Crack 5
* **Difficulty:** $\color{Yellow}{MEDIUM}$
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Can you crack the password to get the flag? 
> Download the password checker <a href="https://artifacts.picoctf.net/c/32/level5.py">here></a> and you'll need the encrypted <a href="https://artifacts.picoctf.net/c/32/level5.flag.txt.enc">flag</a> and the <a href="https://artifacts.picoctf.net/c/32/level5.hash.bin">hash</a> in the same directory too. Here's a dictionary with all possible passwords based on the password conventions we've seen so far.

### Solution
<p>We can do the same thing we did in the previous two challenges. The only difference is that the list of possible passwords has gone up from 100 to 65,000. Automation is a must. The `pos_pw_list` list has been replaced by a file, `dictionary.txt`, that contains all of the passwords we need to loop through to get the flag.</p>

<p>So to replace the list with the dictionary.txt file, we just use python read and assign the contents of that file to a list called `pos_pw_list`. 

```python
# make sure flag_enc and correct_pw_hash are pointing to the right files
flag_enc = open('level5.flag.txt.enc', 'rb').read()
correct_pw_hash = open('level5.hash.bin', 'rb').read()

#There is no list here, so we need to open dictionary.txt and use it to populate our list
pos_pw_list = open('dictionary.txt', 'r').read().splitlines()
```
leveraged the loop I wrote for the previous two challenge to include in `flagcapture_v2.py`.

```
$ python3 flagcapture_v2.py 
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81}
```

### Flag
:pirate_flag:`picoCTF{h45h_sl1ng1ng_40f26f81}`:pirate_flag:

<br>
---
<br>

# Nice netcat...
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
> There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 7449`, but it doesn't speak English...

### Solution

Used net cat to go to the provided url and port. A list of numbers was returned: 

```
s0ren-picoctf@webshell:~$ nc mercury.picoctf.net 7449
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
102 
50 
100 
55 
99 
97 
102 
97 
125 
10
```

Recognized it as probably decimal and tested that theory by looking up a decimal to ascii table. Here's a decent one: http://www.asciitable.com/


First Dec charater is 122 (p), 105 is "i". Ok this looks like the beginning of the flag, decimal it is. I don't want to use the table to manually convert the decimal values into characters one by one, we need a little script. 

Moved the decimals into a list and looped through

    for num in decimals:
        print(chr(num))

This did the job but returned the flag in a horizontal line in the terminal. 

After some stack overflow searching, landed on this syntax to print out in a copy / pastable format. 

    flag = "".join([chr(num) for num in decimals])
        print(flag)   

This returned the flag! 

```
$ python3 convertdecimal.py 
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
```

### Solution 

### Flag
:pirate_flag:`picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}`:pirate_flag:

<br>
---
<br>

# Binary Search
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** Jeffery John

### Description
> Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.
Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!
You can download the challenge files here:
<a href="https://artifacts.picoctf.net/c_atlas/18/challenge.zip">challenge.zip</a>
> Additional details will be available after launching your challenge instance.

### Solution 
<p>The "Binary search" algorithm is simple. With each guess, you want to narrow the range of valid guesses as much as possible.
Beacause we are giving a response of 'higher' or 'lower' after each guess, we can cut our range of valid guesses in half each time
by guessing in the middle of each valid range.</p>

<p> Our first valid range is 1-1000. By guessing in the middle of valid range every time, we eliminate half of the possible answers. Starting 
with a guess of 500, we know the number is lower. Our new valid range is 1 - 499. We'll split this range in half by guessing 250. In just two guesses,
we've eliminated 75 of possible numbers. Rinse and repeat until we narrow down on our answer.</p> 

```
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Lower! Try again.
Enter your guess: 125
Higher! Try again.
Enter your guess: 186
Higher! Try again.
Enter your guess: 220
Lower! Try again.
Enter your guess: 200
Lower! Try again.
Enter your guess: 192
Higher! Try again.
Enter your guess: 196
Lower! Try again.
Enter your guess: 194
Congratulations! You guessed the correct number: 194
Here's your flag: picoCTF{g00d_gu355_2e90d29b}
```

### Flag
:pirate_flag:`picoCTF{g00d_gu355_2e90d29b}`:pirate_flag:

<br>
---
<br>

# Codebook
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'SYREAL' JONES

### Description
> Run the Python script code.py in the same directory as codebook.txt.
<ul>
<li><a href="https://artifacts.picoctf.net/c/102/code.py">Download code.py</a></li>
<li><a href=https://artifacts.picoctf.net/c/102/codebook.txt>codebook.txt</a></li>
</ul>


### Solution 
This looks like another warm-up / environment set up to make sure you can run programs from the shell

1. Just make sure the two files are in the same directory on your local machine
2. Run the python file from terminal and the flag will print to the console

<p>Familiarize yourself with <a href = "https://primer.picoctf.com/#_what_the_shell">The Shell</a></p>

'''
python3 code.py
picoCTF{c0d3b00k_455157_197a982c}
'''

### Flag
:pirate_flag:`picoCTF{c0d3b00k_455157_197a982c}`:pirate_flag:

<br>
---
<br>

# Convertme.py
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Run the Python script and convert the given number from decimal to binary to get the flag.<br>
> <a href="https://artifacts.picoctf.net/c/31/convertme.py">Download Python script</a>

### Solution 
<p>Run the python script. It asks you to convert the decimal number 60 to binary.</p>

```
$ python3 convertme.py 
If 60 is in decimal base, what is it in binary base?
Answer:
```

<p> Python has a built in function that can convert any integer to binary. Using `bin()` in a python shell gives us the answer</p>

```
$ python3
Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bin(60)
'0b111100'
>>> 
```

<p>We have our answer and the flag is returned! 4ll_y0ur_b4535!</p>

![ALL YOUR BASE ARE BELONG TO US](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExem9jZWJqcGF6cjEzZ2E5bmdvaGt1cGhxY3NqZTcwZ3FkZW81cm02OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/spmJ2CMMcf1fSR7DRS/giphy.gif)

```
$ python3 convertme.py 
If 60 is in decimal base, what is it in binary base?
Answer: 111100
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_9c3b7d4d}
```

### Flag
:pirate_flag:`4ll_y0ur_b4535_9c3b7d4d}`:pirate_flag:

<br>
---
<br>

# runme.py
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** Sujeet Kumar

### Description
> Run the runme.py script to get the flag. Download the script with your browser or with wget in the webshell. 
> <a href="https://artifacts.picoctf.net/c/34/runme.py">Download runme.py Python script</a>

### Solution
This is just an sanity check to make sure you can run python scripts. Succesfully running the script will print the flag. It's redundant in the context of this write up, but consider that many of these challenges were published over different challenge years and are aimed at absolute beginners. 

```
$ python3 runme.py 
picoCTF{run_s4n1ty_run}
```
You could also just open `runme.py` in a text editor and look at the flag in plaintext within the script. 

### Flag
:pirate_flag:`picoCTF{run_s4n1ty_run}`:pirate_flag: 


# HashingJobApp
* **Difficulty:** Easy
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> If you want to hash with the best, beat this test! 
> nc saturn.picoctf.net 61000

### Solution 

In this challenge, you're asked to provide the md5 hash value of a bunch of different strings. I found the most straightforward way to do this was to open another terminal window and use the build in `md5` command with the option `-s` to print the checksum of a given string. 

<table border="0">
<tr>
<td>

```            
$ md5 -s caffeine
MD5 ("caffeine") = e724f8b8a8349afb5beaeaa300323933
$ $ md5 -s Casablanca
MD5 ("Casablanca") = adf20488d00fb576b16546b1c93611b4
$ md5 -s armed robbery
MD5 ("armed") = 6e0c631e86ef2402cfa1ca3608a5123e
md5: robbery: No such file or directory
$ md5 -s 'armed robbery'
MD5 ("armed robbery") = 986ad0db60b8d3d46281880f693a5926
```        

</td> 
<td>    

```
$ nc saturn.picoctf.net 61000
Please md5 hash the text between quotes, excluding the quotes: 'caffeine'
Answer: 
e724f8b8a8349afb5beaeaa300323933
e724f8b8a8349afb5beaeaa300323933
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'Casablanca'
Answer: 
adf20488d00fb576b16546b1c93611b4
adf20488d00fb576b16546b1c93611b4
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'armed robbery'
Answer: 
986ad0db60b8d3d46281880f693a5926
986ad0db60b8d3d46281880f693a5926
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}
```
                        
</td>   
</tr>
</table>


### Flag
:pirate_flag:`picoCTF{4ppl1c4710n_r3c31v3d_674c1de2}`:pirate_flag:

<br>
---
<br>


# Serpentine
* **Difficulty:** Medium
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Find the flag in the Python script! <br>
> <a href="https://artifacts.picoctf.net/c/93/serpentine.py">Download Python script</a>

### Solution 
<p>When we run serpentine.py, we can select option 'b' to print the flag.</p>

```
Welcome to the serpentine encourager!


a) Print encouragement
b) Print flag
c) Quit

What would you like to do? (a/b/c) b

Oops! I must have misplaced the print_flag function! Check my source code!
```

<p>Only option 'b' doesn't print the flag! We can comment out message and replace it with the `print_flag()` function to get the flag to print on option 'b'.</p>

```
# The 'print_flag' function is the function that actually decrypts and prints the flag. 
# Let's call this function in the if / else statements below
def print_flag():
  flag = str_xor(flag_enc, 'enkidu')
  print(flag)
```
```
    elif choice == 'b':
      # calling the function here will allow the flag to actually be printed on option 'b'.
      print_flag()

      # print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```

<p>With the `print_flag()` function in the 'right' place, we can just run serpentine.py to print the flag.</p>

```
What would you like to do? (a/b/c) b
picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
```

### Flag
:pirate_flag:`picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}`:pirate_flag:

<br>
---
<br>

# Plumbing
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** Alex Fulton/Danny Tunitis

### Description
> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.


### Solution 

<p>Pipes allow you to run processes on the output of another process. In this example, the program we're pointing to just spits out a ridiculous amount of garbage when we connect to it (including the flag).</p>

```
$ nc jupiter.challenges.picoctf.org07489
Not a flag either
This is defintely not a flag
Not a flag either
Not a flag either
I don't think this is a flag either
Again, I really don't think this is a flag
I don't think this is a flag either
...
```

<p>We want to find the flag in this sea of garbage output. A pipe will allow us to run another process on the garbage. In this case, we can just grep for the string 'picoCTF{' This effectively filters out everything else and shows us only the strings that contain 'picoCTF{' which is where we find the flag.</p>

```
$ nc jupiter.challenges.picoctf.org 14291 | grep picoCTF{
picoCTF{digital_plumb3r_ea8bfec7}
```

### Flag
:pirate_flag:`picoCTF{digital_plumb3r_ea8bfec7}`:pirate_flag:

<br>
---
<br>


# Time Machine
![https://play.picoctf.org/practice/challenge/411](/assets/images/challengescreenshots/Time Machine)


### Solution
I'm going to use the webshell for these git related challenges so I don't have to deal with a mess of local files. I can `wget` for the right file with `s0ren-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/66/challenge.zip` and then unzip the file with `unzip`

This gives me a folder called `drop-in` with a file called `message.txt`.

```
s0ren-picoctf@webshell:~/drop-in$ cat message.txt 
This is what I was working on, but I'd need to look at my commit history to know why...
```

The flag isn't in there, but there is a hint about commit history. We can look at the commit history with the `git log` command. 

```
commit 3339c144a0c78dc2fbd3403d2fb37d3830be5d94 (HEAD -> master)
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:10:22 2024 +0000

    picoCTF{t1m3m@ch1n3_d3161c0f}
```

### Flag
:pirate_flag:`picoCTF{t1m3m@ch1n3_d3161c0f}}`:pirate_flag:

<br>
---
<br>



# Commitment Issues
![Screenshot of challenge instead of copy and pasting info](/assets/images/challengescreenshots/Commitment_Issues_411.png)

### Solution 
In this challenge we're given access to another `git` folder with some history. I used the webshell to solve this one by first using `wget` to grab right file from the challenge. 

`s0ren-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/139/challenge.zip`

I unzipped the file using `unzip` and was able to CD into the directory `/drop-in`. Ran `git status` to confirm this is a git folder. 

```
s0ren-picoctf@webshell:~/drop-in$ git status
On branch master
nothing to commit, working tree clean
```

The only thing in this folder is a file called message.txt. Let's see what's in there. 

```
s0ren-picoctf@webshell:~/drop-in$ cat message.txt 
TOP SECRET
```

We need to see what the file looked like *before* the last commit. To do this, I can run `git reset --hard HEAD^` to revert the last commit. Then we can `cat message.txt` to see what was written in that file previously. 

```
s0ren-picoctf@webshell:~/drop-in$ git reset --hard HEAD^
HEAD is now at 7d3aa55 create flag
s0ren-picoctf@webshell:~/drop-in$ cat message.txt 
picoCTF{s@n1t1z3_be3dd3da}
```

Nice. We've reverted to a commit with the message 'create flag'. This is promising. If we look at the contents of message.txt, we can see it has been reverted and contains the flag. 

### Flag
:pirate_flag:`picoCTF{s@n1t1z3_be3dd3da}`:pirate_flag:

<br>
---
<br>

# Collaborative Development
![Another screenshot of a challenge that I'll probably take down because I won't like how it looks or I'll link to it incorrectly](https://github.com/benjamindpalmer/pico-gym-write-ups/blob/main/general_skills/assets/images/challengescreenshots/Collaborative_Development_410.png)

### Solution

We have another git challenge here. We'll start the same way by grabbing the file and unzipping it and then moving into the 'drop-in' directory to see our status. 

```
s0ren-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c_titan/71/challenge.zip
```

This time, we have a python file called `flag.py`. The copy on MAIN only contains the text 'Printing the flag...'

```
s0ren-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")
```

We can use `git branch -a` to see the different branches in this git repo. It looks like there are three. 


```
  feature/part-1
  feature/part-2
  feature/part-3
* main
```

We can move through each of these branches with `git checkout`. Each branch contains a `flag.py` file that is printing out a different part of the flag. 


```
s0ren-picoctf@webshell:~/drop-in$ git checkout feature/part-1
Switched to branch 'feature/part-1'
s0ren-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')s0ren-picoctf@webshell:~/drop-in$
s0ren-picoctf@webshell:~/drop-in$ git checkout feature/part-2
Switched to branch 'feature/part-2'
s0ren-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')s0ren-picoctf@webshell:~/drop-in$ 
s0ren-picoctf@webshell:~/drop-in$ git checkout feature/part-3
Switched to branch 'feature/part-3'
s0ren-picoctf@webshell:~/drop-in$ cat flag.py 
print("Printing the flag...")

print("w0rk_4c24302f}")
```

How do I merge all of these together? First, I need to move back to MAIN with `git checkout main` and start merging in the different features with starting with `git merge feature/part-1`. 

I ran into conflicts that I had to use nano to correct. 

[!screenshot of editing a merge conflicts in nano](/assets/images/screenshots/collaborative_development_nano.png)


```
s0ren-picoctf@webshell:~/drop-in$ python flag.py 
Printing the flag...
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}
```

### Flag
:pirate_flag:`picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_4c24302f}`:pirate_flag:

<br>
---
<br>


# Blame Game
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** Jeffery John

### Description
> Someone's commits seems to be preventing the program from working. Who is it? You can download the challenge files here:
> * <a href="https://artifacts.picoctf.net/c_titan/157/challenge.zip">challenge.zip</a>

### Solution 
In this git related challenge,  we're given another git repo with a bunch of different commits. The directory contains one python file. If we run the python script,  we get a syntax error.  

```
s0ren-picoctf@webshell:~/drop-in$ python message.py 
  File "/home/s0ren-picoctf/drop-in/message.py", line 1
    print("Hello, World!"
         ^
SyntaxError: '(' was never closed
```

Let's look at the git log with `git log` to see a list of commits and see if anything pops out.  

Running `git  log` returned a LOT of commits. Too many to look through manually. Let's pipe a grep search for flag to the end of the log and see if that returns anything.  

```
$ git log |  grep "picoCTF{"
Author: picoCTF{@sk_th3_1nt3rn_cfca95b2} <ops@picoctf.com>
```

It  worked! The  commit  that  contains the flag was returned. We could have also created a text file and of the log and searched through that by using the `>` command to print the output to a file. `git log > log.txt`

### Flag
:pirate_flag:`picoCTF{@sk_th3_1nt3rn_cfca95b2}`:pirate_flag:

---

# First Find
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Unzip this archive and find the file named 'uber-secret.txt'
> * <a  href = "https://artifacts.picoctf.net/c/501/files.zip">Download zip file</a>

### Solution 
The unzipped directory contains a ton of subdirectories, and we're trying to find the folder that contains  `uber-secret.txt`

Looking at some of the documentation for `find` and it is very powerful and takes a lot of paramenters. In this case, we're given the full name of the file so we just need to use `-name` along with `find` to look for that file. Initially, I used `find ~\` which looks through your *entire* home directory.  That worked, but was very unecessary. I founed out we can use `.` to tell find to only look in the directory that I unzipped from the challenge. 

``` 
$ find .  -name "uber-secret.txt"
./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
```

Great! We successfully used `find` to locate the target file. Now we know that `uber-secret.txt` can be found in `/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt` From there, I copied the file path and used it with the `cat` command to print out the contents of `uber-secret.txt` Our flag is in this file. 

```
$ cat ./adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
picoCTF{f1nd_15_f457_ab443fd1}
```

It's good to know `man find` from the terminal and https://man7.org/linux/man-pages/man1/find.1.html exist. Will keep them handy to reference later when 


### Flag
:pirate_flag:`picoCTF{f1nd_15_f457_ab443fd1}`:pirate_flag:

---

# Big Zip
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Unzip this archive and find the flag.
> * <a href="https://artifacts.picoctf.net/c/503/big-zip-files.zip">Download zip file</a>

### Solution 
In this challenge, we download and unzip a giant folder called `big-zip-files` which contains hundreds of files and subdirectories. Our flag is hidden in this mess, and this time we don't even know which file to look for. 

![add screenhot](#path-to-screenshot)

We do know the flag will contain the string `'picoCTF{'` so we can use a recursive grep (`grep -r`) to search all directories and their children inside the 'big-zip-files' folder. 

```
$ grep -r "picoCTF"
./folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

### Flag
:pirate_flag:`picoCTF{gr3p_15_m4g1c_ef8790dc}`:pirate_flag:


# Glitch Cat
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Our flag printing service has started glitching!
> Additional details will be available after launching your challenge instance.
> $ nc saturn.picoctf.net 57717

### Solution 

```
s0ren-picoctf@webshell:~$  nc saturn.picoctf.net 53869
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```

The environment we're in has part of the flag printed in plaintext and the rest is encoded in hexidecimal. In Python,  the `chr()` function should return charater based on its encoding value.  e.g. `chr(0x39)`returns "9" in python.  Rather than look up the encoding values for every character and create the flag manually, I'd rather just save what we have as a python file see if it will run. Let's use `touch` to create a new python file called `flag.py` and the use `nano` to open it from the shell. 

```
s0ren-picoctf@webshell:~$ touch flag.py
s0ren-picoctf@webshell:~$ nano flag.py 
```

With nano open, I copy/pasted our bit of python into flag.py and wrapped it in a `print()`
```python
print('picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}')
```

Now running flag.py will should print our flag. 

```
s0ren-picoctf@webshell:~$ python3 flag.py
picoCTF{gl17ch_m3_n07_9c42a45d}
```

### Flag
:pirate_flag:`picoCTF{gl17ch_m3_n07_9c42a45d}`:pirate_flag:

---

# fixme1
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Fix the syntax error in this Python script to print the flag.
> <a href="https://artifacts.picoctf.net/c/26/fixme1.py">Download Python script</a>

### Solution 
Error messages can be extremely helpful sometimes. After downloading `fixme1.py` I decided to run it first and it returned an indentation error on line 20.  

```
s0ren-picoctf@webshell:~$ python3 fixme1.py 
  File "/home/s0ren-picoctf/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

Python cares about indents. In this case, we just have to remove the indent from line 20 where the flag is printed. I did this and the script ran without errors and printed the flag. 

```
s0ren-picoctf@webshell:~$ python3 fixme1.py 
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
```

### Flag
:pirate_flag:`picoCTF{1nd3nt1ty_cr1515_09ee727a}`:pirate_flag:

---

# fixme2
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** LT 'syreal' Jones

### Description
> Fix the syntax error in the Python script to print the flag. 
> <a href="https://artifacts.picoctf.net/c/5/fixme2.py">Download Python script</a>


### Solution 

Let's try running the script again to see what kind of error we get. 

```
s0ren-picoctf@webshell:~$ python3  fixme2.py 
  File "/home/s0ren-picoctf/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```
In this case, it looks like a single equal operator is being used for an `if` statement, which is incorrect syntax in many languages. 

> [!TIP]
> Python (and other languages) Comparison Operator 
> - == comparison operator used to compare two values. If the values are the same then `True` is returned
> - =! Inverse comparison returns `True` if the values are not the same.
> - = assignment operator used to assign a value to a variable. 

Put the comparison operator in the correct place and re-ran the script.

```
s0ren-picoctf@webshell:~$ python3 fixme2.py 
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```


### Flag
:pirate_flag:`{3qu4l1ty_n0t_4551gnm3nt_4863e11b}`:pirate_flag:

---

# Magikarp Ground Mission
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** SYREAL

### Description
> Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`
>

### Solution 

### Flag
:pirate_flag:``:pirate_flag:

---

# Static ain't always noise
* **Difficulty:** 
* **Category:** GENERAL SKILLS
* **Author:** 

### Description
> Can you look at the data in this binary: <a href = "https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static">static</a>? This <a href="https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh"><BASH script></a> might help!
>

### Solution 

### Flag
:pirate_flag:``:pirate_flag:

---

# useless
* **Difficulty:** MEDIUM
* **Category:** GENERAL SKILLS
* **Author:** Loic Shema

### Description
> There's an interesting script in the user's home directory The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
>

### Solution 

### Flag
:pirate_flag:``:pirate_flag:

---

# Based
* **Difficulty:** MEDIUM
* **Category:** GENERAL SKILLS
* **Author:** Alex Fulton/Daniel Tunitis

### Description
> To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc jupiter.challenges.picoctf.org 15130.
>

### Solution 

### Flag
:pirate_flag:``:pirate_flag:

---



