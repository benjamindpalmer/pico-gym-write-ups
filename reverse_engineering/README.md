<h1 align="center"> :gear: REVERSE ENGINEERING :gear:</h1>

- [asm1](#asm1)
- [Bit-O-Asm-1](#bit-o-asm-1) :pirate_flag:
- [Bit-O-Asm-1](#bit-o-asm-2) :pirate_flag:
- [Bit-O-Asm-1](#bit-o-asm-3) :pirate_flag:
- [Bit-O-Asm-1](#bit-o-asm-4) :pirate_flag:
- [asm2](#asm2)
- [Picker 1](#picker-1) :pirate_flag:
- [keygenme-py](#keygenme-py) 
- [vault-door-training](#vault-door-training) :pirate_flag:
- [vault-door-1](#vault-door-1) :pirate_flag:
- [vault-door-3](#vault-door-3) :pirate_flag:
- [vault-door-4](#vault-door-4) :pirate_flag:
- [vault-door-5](#vault-door-5) :pirate_flag:
- [vault-door-6](#vault-door-6)
- [Safe Opener](#safe-opener) :pirate_flag:
- [Safe Opener 2](#safe-opener-2) :pirate_flag:

# asm1
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** SANJAY C

### Description
> What does asm1(0x2e0) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. 
> <a href="https://jupiter.challenges.picoctf.org/static/f1c2358ff7d1e9386e41552c549cf2f6/test.S">Source</a>
>
> HINT: assembly <a href="https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm">conditions</a>

### Solution 

```x86 assembly
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb
	<+10>:	jg     0x512 <asm1+37>
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x280
	<+19>:	jne    0x50a <asm1+29>
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0xa
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0xa
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x559
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0xa
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0xa
	<+60>:	pop    ebp
	<+61>:	ret    
```

<p>This is my first time looking at anything assembly language related. I spent about a week every night opening this file and muttering "where the f*** do I even begin with this one?" On Friday night I opened the provided `test.S` file with some determination, knowing that I'd probably have to learn some assembly language. The assembly conditions hint was helpful, as it touches on what many of the assembly intructions in `test.S` actually do.</p>
<p>So I knew there were instructions in the file. I knew assembly needed to be read line by line. But I like a little context. What is actually happening here? What is an assembly language? I found this <a href="https://www.youtube.com/watch?v=75gBFiFtAb8">x86 Assembly Crash Course</a> video that breaks everything down in ten minutes. I still don't know assembly language, but I have a little bit of context as to what all of the different assembly intructions are actually doing in this challenge.</p>

```
asm1:
	<+0>:	push   ebp							;0x2e0 to base pointer												
	<+1>:	mov    ebp,esp										
```
We know that asm1 starting with 0x2e0 per the challenge description. 0x2e0 is 736 in decimal. This is important because will be adding, subtracting, and comparing this value with other hex values as we move line by line through asm1.

```
    <+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb	;0x2e0(736), 0x3FB(1019)
    <+10>:	jg     0x512 <asm1+37>				;jg - jump if greater than
```
`cmp` "compares" two values, the one at ebp + 8bits(?) and hex value 0x3FB which is 1019 in decimal. The value at ebp is 0x2e0 or 736. 736 is less than 1019. We know that compare instructions are always followed by a "jump", depending on the type of jump, we'll move to a different line of asm1 (or not). `jg` is jump if greater. Because the `cmp` above does not resolve to 'greater than', we don't jump here and instead move on the to the next line.

```
    <+12>:	cmp    DWORD PTR [ebp+0x8],0x280	;736 =! 640
    <+19>:	jne    0x50a <asm1+29>				;jne - jump if NOT equal
```
On the next line we have another `cmp` instruction, followed by `jne` or 'jump if NOT equal'. Because the values in our compare are not equal, we can jump to `<asm1+29>`.

```
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]		;set 0x2e0 to eax register
	<+32>:	sub    eax,0xa						;subtract 0xa (10) from 0x2e0, eax register updated to value 726						
	<+35>:	jmp    0x529 <asm1+60>				;jmp - non conditional jump to go <+60>
```

Down here at `asm1+29` we start with a `mov` instruction. This sets the value at ebp to a different register at eax. The value is still 0x2e0. 
Next, we have a `sub` or 'subtract' instruction to subtract 10 from the value at eax (736). This gives us 726.
Our next 'jump' instruction is `jmp` which is a non-conditional jump. We just get to jump all the way down to `<asm1+60>`

```
	<+60>:	pop    ebp							;pop ebp out of the stack 
	<+61>:	ret    
```
My understanding is that here `ret` transfers program control to a retrun address on the top of the stack. For the purposes of this challenge however, the most important thing about this line is that it is the end of asm1. We're left with decimal value 726 which in hex is 0x2d6!

![Hansel gif](https://c.tenor.com/iEFPkqaIeXIAAAAC/do-i-know-what-im-doing.gif)

### Flag
:pirate_flag:`0x2d6`:pirate_flag:

<br>

---

<br>


# Bit-O-Asm-1
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** LT 'syreal' Jones

### Description
> Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the `eax` register in the decimal number base. If the answer was `0x11` your flag would be `picoCTF{17}`. 
> Download the assembly dump <a href="https://artifacts.picoctf.net/c/509/disassembler-dump0_a.txt">here<a>.


### Solution
Taking a look at the provided assembly dump, we can see the hexidecimal value `0x30` is in the `eax` register. 

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

Using an <a href="https://www.asciitable.com/">ASCII table</a>, we can see that `0x30` in hexidecimal is `48` in decimal. 

[!NOTE]
> A CPU register refers to an actual physical location on a CPU


### flag
:pirate_flag:`picoCTF{48}`:pirate_flag:

<br>

---

<br>

# Bit-O-Asm-2
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** LT 'syreal' Jones

### Description
> Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be `picoCTF{17}`. 
> Download the assembly dump <a href="https://artifacts.picoctf.net/c/510/disassembler-dump0_b.txt">here</a>.


### Solution

For this challenge, we're asked download another disassembly dump and find what is the `eax` register again. This challenge introduces pointers: `PTR`. 

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
<+25>:    pop    rbp
<+26>:    ret
```

At instruction `<+22>` we see the line `mov    eax,DWORD PTR [rbp-0x4]`. This is loading the value at `[rbp-0x4]` to `eax`. At instruction `<+15>` we see that location `[rbp-0x4]` is set to `0x9fe1a`.  This means `0x9fe1a` is the value in `eax` register. Now we just convert to decimal. 

Interestingly, converting to decimal was the hardest part here. I was using Cyberchef's 'From Hex' recipe which was converting `0x9fe1a` as three separate hex bytes: `159 225 10`

What I really wanted here was a base16 to decimal conversion. Treated as a Base16 number, `0x9fe1a` is `654874` in decimal. 

https://gchq.github.io/CyberChef/#recipe=From_Base(16)&input=MHg5ZmUxYQ


### flag
:pirate_flag:`picoCTF{654874}`:pirate_flag:

<br>

---

<br>

# Bit-O-Asm-3
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** LT 'syreal' Jones

### Description
> Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be `picoCTF{17}`. 
> Download the assembly dump <a href="https://artifacts.picoctf.net/c/530/disassembler-dump0_c.txt">here</a>.


### Solution

This assembly challenge introduces two arithematic operators: `add` which adds, and `imul` which multiplies. 
The assembly dump is copied below, and I've added some comments to break down the solution. 

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a ; store 0x9fe1a at [rbp-0xc]
<+22>:    mov    DWORD PTR [rbp-0x8],0x4 ; store 0x4 at [rbp-0x8]
<+29>:    mov    eax,DWORD PTR [rbp-0xc] ; set eax to equal 0x9fe1a
<+32>:    imul   eax,DWORD PTR [rbp-0x8] ; multiply 0x9fe1a * 0x4, eax = 0x27fa5d
<+36>:    add    eax,0x1f5 ; add 0x1f5 + 0x27fa5d, eax = 0x27f868
<+41>:    mov    DWORD PTR [rbp-0x4],eax; store 0x27f868 at [[rbp-0x4]]
<+44>:    mov    eax,DWORD PTR [rbp-0x4] ; eax = 0x27f868
<+47>:    pop    rbp
<+48>:    ret
```

* At instruction `<+29>` there is an `eax` pointer to location `[rbp-0xc]`. That location is set to `0x9fe1a` (a familiar value from the last challenge.)
* The value at `eax` is `0x9fe1a`
* At instruction `<+32>` the `imul` operator appears with a `PTR` to location `[rbp-0x8]`. Multiplying the value at `[rbp-0x8]` (`0x4`) returns a product of `0x27f868` (654874<sub>10</sub> *<sub>10</sub> 4 = 2619496<sub>10</sub> = 0x27f868<sub>16</sub>
* The value at `eax` is `0x27f868`
* At instruction `<+36>` the `add` operator adds `0x1f5`  to `eax`. `0x27f868` + `0x1f5` = `0x27fa5d`. (2619496<sub>10</sub> + 501<sub>10</sub> = 2619997<sub>10</sub> = 0x27f868<sub>16</sub>)
* Finally, instruction `<+44>` just has the the current value of `eax` which is `0x27f868` or `2619997` in decimal. 

Cyberchef was used to convert all of the results of the operations to Decimal and then back to Base16. This was unnecessary since the answer needed to be in Decimal anyway. 


### flag`
:pirate_flag:`picoCTF{2619997}`:pirate_flag:

<br>

---

<br>

# Bit-O-Asm-4
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** LT 'syreal' Jones

### Description
> Can you figure out what is in the `eax` register? Put your answer in the picoCTF flag format: `picoCTF{n}` where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be `picoCTF{17}`. 
> Download the assembly dump <a href="https://artifacts.picoctf.net/c/511/disassembler-dump0_d.txt">here</a>.


### Solution

In this challenge, we're introduced to compares (`cmp`) and jumps (`jmp` and `jle` for this challenge). Also present is is a subtract `sub` operator.
I found PicoCTF's brief summary of '<a href="https://play.picoctf.org/playlists/2?m=22">Assembly Branching</a>' absolutely necessary to solve this.  

Once again I copied the provided assembly dump and went straight into commenting what each line relevant to the challenge does. 

```
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x14],edi
<+11>:    mov    QWORD PTR [rbp-0x20],rsi
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a ; store 0x9fe1a at [rbp-0x4]
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710 ; compare 0x9fe1a > 0x2710
<+29>:    jle    0x55555555514e <main+37> ; conditional jump to location +37 if 0x9fe1a <= 0x2710. This is false. No jump. 
<+31>:    sub    DWORD PTR [rbp-0x4],0x65 ; subtract 0x9fe1a - 0x65 = 0x9FDB5
<+35>:    jmp    0x555555555152 <main+41> ; jump to location <+41>
<+37>:    add    DWORD PTR [rbp-0x4],0x65 ; 
<+41>:    mov    eax,DWORD PTR [rbp-0x4] ; eax = 0x9FDB5
<+44>:    pop    rbp
<+45>:    ret
```

Detailed breakdown of the relevant lines: 

* At instruction `<+15>` the value 0x9fe1a<sub>16</sub> is stored at address `[rbp-0x4]`
* At instruction `<+22>` 0x9fe1a is compared to 0x2710 with `cmp`. It is worth noting that 0x9fe1a is greater than 0x2710
* At instruction `<+29>` There is a conditional jump to location `<+37>` with `jle` "jump if less than or equal to". This condition is false, so there is no jump. 
* At instruction `<+31>` 0x65<sub>16</sub> (101<sub>10</sub>) is substracted from 0x9fe1a<sub>16</sub> at location `[rbp-0x4]`. The difference is 654773<sub>10</sub>. 
* At instruction `<+35>` there is a non-conditional jump `jmp` to instruction `<+41>` 
* At instruction `<+41>` eax = the value at location `[rbp-0x4]`, which is 0x9FDB5<sub>16</sub> or  654773<sub>10</sub> in decimal.


### flag
:pirate_flag:`picoCTF{654773}`:pirate_flag:

<br>

---

<br>

# Picker 1
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** LT 'syreal' Jones

### Description
> This service can provide you with a random number, but can it do anything else?
> Connect to the program with netcat: `$ nc saturn.picoctf.net 58051` 
> The program's source code can be downloaded <a href="https://artifacts.picoctf.net/c/513/picker-I.py">here</a>.


### Solution
When we use netcat to connect, we're prompted to enter 'getRandomNumber' which always returns '4'. 

```
$ nc saturn.picoctf.net 58051
Try entering "getRandomNumber" without the double quotes...
==> getRandomNumber
4
```

This is because what we are really doing is calling a function in python. We can throw a very common python error when entering anything that isn't a function name the python script.  

```
$ nc saturn.picoctf.net 63749
Try entering "getRandomNumber" without the double quotes...
==> iTestInProduction
name 'iTestInProduction' is not defined
```

"is not defined" is thrown when trying to invoke a function name that doesn't exist. Like "iTestInProduction"

If we look at the included copy of the source code, there is a function named `getRandomNumber` that just prints the number 4. 

```python
def getRandomNumber():
  print(4)  # Chosen by fair die roll.
            # Guaranteed to be random.
            # (See XKCD)
```
This is a reference to the famous web comic: 
![Famous XKCD Random Number Comic](https://imgs.xkcd.com/comics/random_number.png)


There are a few more functions in the source code that are interesting, especially the `win` function. It looks like this function opens and reads a filee called `flag.txt`, and then prints it in hexidecimal. 

```python
def win():
  # This line will not work locally unless you create your own 'flag.txt' in
  #   the same directory as this script
  flag = open('flag.txt', 'r').read()
  #flag = flag[:-1]
  flag = flag.strip()
  str_flag = ''
  for c in flag:
    str_flag += str(hex(ord(c))) + ' '
  print(str_flag)
```

Instead of calling "getRandomNumber", we can call "win" and get this function to execute. 

```
Try entering "getRandomNumber" without the double quotes...
==> win
0x70 0x69 0x63 0x6f 0x43 0x54 0x46 0x7b 0x34 0x5f 0x64 0x31 0x34 0x6d 0x30 0x6e 0x64 0x5f 0x31 0x6e 0x5f 0x37 0x68 0x33 0x5f 0x72 0x30 0x75 0x67 0x68 0x5f 0x62 0x35 0x32 0x33 0x62 0x32 0x61 0x31 0x7d 
```

This time, the python script printed out some stuff in hexidecimal. This is definitely the flag. It starts to "pico" magic bytes `0x70 0x69 0x63 0x6f`. Using <a href="https://cyberchef.org/#recipe=From_Hex('Auto')">Cyberchef</a> we can convert this from hex to a plaintext string. 


### flag
:pirate_flag:`picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}`:pirate_flag:

<br>


---


<br>


# keygenme-py
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** SYREAL

### Description
> <a href="https://mercury.picoctf.net/static/a6d9cac3bfa4935ceb50c145d3ff5586/keygenme-trial.py">keygenme-trial.py</a>
>

### Solution 
No helpful description or hints here. Just a link to download a python script. Taking a look at the script, we can

### Flag
:pirate_flag:``:pirate_flag:

<br>

---

<br>

# asm2
* **Difficulty:** Hard
* **Category:** Reverse Engineering
* **Author:** SANJAY C

### Description
> What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). <br>
> NOTE: Your submission for this question will NOT be in the normal flag format. <a href="https://jupiter.challenges.picoctf.org/static/ceac75672637589213b952abe32c84b3/test.S">Source</a><br>
> *HINT:* assembly <a href="https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm">conditions</a>


### Solution 
<p>Oh, what's this? More assembly language? Why do I feel like a child being thrown in the deep end of a pool? I can't swim! Help. </p>

<p>We know ASM is a low level language. We're actually giving instructions to the CPU at this level and that's pretty exciting and cool. That said, let's take a deep breath and take a look at these lovely and not intimidating at all assembly instructions and see if we can find a the flag.</p>

```
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] ; 
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    
```

### Flag
:pirate_flag:``:pirate_flag:

<br>

---

<br>

# vault-door-training
* **Difficulty:** Easy
* **Category:** Reverse Engineering
* **Author:** MARK E. HAASE

### Description
> Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: <a href="https://jupiter.challenges.picoctf.org/static/a4a1ca9c54d8fac9404f9cbc50d9751a/VaultDoorTraining.java">VaultDoorTraining.java</a>

### Solution

This is a cautionary tale against putting the key in source code. At the bottom of the file provided, we see flag in plaintext. 

```java
    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_be8d9806f18");
    }
```

### Flag
:pirate_flag:`w4rm1ng_Up_w1tH_jAv4_be8d9806f18`:pirate_flag:

<br>
---
<br>

# vault-door-1
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** MARK E. HAASE

### Description
> This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: <a href="https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java">VaultDoor1.java</a> 


### SolutionChecking the provided java source code we find: 

```java
    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
```

.charAt() will return a letter in a string with the index value as an argument. There's probably something in Java that will let me rebuild the password by joining everything. But let's use python and then we can come back and see if anyone else approached this a differnet way. Manually going through lists like this reminds me too much of data entry work and I'd much rather get in the habit of using scripts. 

Using a little `ctrl+shift+l` and `opt_shift+i` magic in VScode, I created this little python dictionary based on the source code above. 

```python
letters = {
0:'d',
29:'9',
4:'r',
2:'5',
23:'r',
3:'c',
17:'4',
1:'3',
7:'b',
10:'_',
5:'4',
9:'3',
11:'t',
15:'c',
8:'l',
12:'H',
20:'c',
14:'_',
6:'m',
24:'5',
18:'r',
13:'3',
19:'4',
21:'T',
16:'H',
27:'5',
30:'2',
25:'_',
22:'3',
28:'0',
26:'7',
31:'e'
}
```   
Now we just have to loop through the dictionary in the correct order to build a list of letters. Then use `.join` to print out the flag just like we did in the first cryptography challenge. 

```python
# array of flag letters in the right order
sorted_letters = []

# range 
for i in range(32):
    #print(letters[i])
    sorted_letters.append(letters[i])

# join and print flag
flag = "".join(sorted_letters)
print(flag)
```

### Flag
:pirate_flag:`picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}`:pirate_flag:

<br>
---
<br>

# vault-door-3
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** MARK E. HASSE

### Description
> This vault uses for-loops and byte arrays. The source code for this vault is here: <a href="https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java">VaultDoor3.java</a>
>
> **HINT:** Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

### Solution 
The java file provided contains a string that looks a little like a flag, but isn't a flag: `jU5t_a_sna_3lpm18g947_u_4_m9r54f`. The script is scrambling this string based on rules that change every 8 characters. 
}
```
I added some comments to the provided Java file to break down what each set of rules does. The first 8 characters iterate sequentially. They aren't scrambled at all. 

```Java
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);  // the first eight characters are the same as the starting string
```

| Buffer index | password |  
| ---------    | ----------- | 
| 0 | j
| 1 | U 
| 2 | 5
| 3 | t
| 4 | _
| 5 | a
| 6 | _
| 7 | s

The subsequent parts of the script follow different rules. I manually whent though and created tables to index them. This took a lot of time and I actually ended up writing a pythong script to automate this anyway. 

```Java 
for (; i<16; i++) {
            buffer[i] = password.charAt(23-i); // subtract i from 23 and get the character at that index
```
| Buffer index | password |  
| ----------- | -------| 
| 23 - 8 | 1
| 23 - 9 | m 
| 23 - 10 | p
| 23 - 11 | l
| 23 - 12 | 3
| 23 - 13 | _
| 23 - 14 | a
| 23 - 15 | n

<p>This was going well as a manual 'one character at time' processs up to this point . But I ran into a ton of problems as I continued. I wasn't thinking about assigning the values I got to the right index, and instead was just listing them in the order that I found them. Again, this took forever because I used these tables to figure this out manually.</p>

```Java
        for (; i<32; i+=2) {                      //i is interating by two here, which means the values I'm picking up for the password are at every other index
            buffer[i] = password.charAt(46-i);
```
| Buffer index | password |  
| ----------- | -------| 
| 46 - 16 | 4
| 46 - 18 | r 
| 46 - 20 | m
| 46 - 22 | 4
| 46 - 24 | u
| 46 - 26 | 7
| 46 - 28 | 9
| 46 - 30 | 8


```python vault3.py
password = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"

# I need to buffer this list to 32 characters so I can assign values to any index between 0 - 31
# appending to a list won't work, because we're not building this list in sequence, so a bunch of while loops will have to hack it. 
flag_list = [""]*32
i = 0

while i < 8:
    flag_list[i] = password[i]
    i = i + 1

while i < 16:
    flag_list[i] = password[23-i]
    i = i + 1

while i < 32:
    flag_list[i] = password[46-i]
    i = i + 2

# The algorithm in the original script was ADDING two index values to my flag. To reverse it, i need to start at i=31 and interate backwards.

i = 31
while i >= 17:
    flag_list[i] = password[i]
    i = i - 2

flag = ''.join(flag_list)
print(flag)
```

Could have saved a ton of time here if I had just written the little python script to start

### Flag
:pirate_flag:`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}`:pirate_flag:

<br>

---

<br>

# vault-door-4
* **Difficulty:** 
* **Category:** 
* **Author:** 

### Description
> This vault uses ASCII encoding for the password. The source code for this vault is here: <br>
> <a href="https://jupiter.challenges.picoctf.org/static/c695ee23309d453a3ef369c34cc1bccb/VaultDoor4.java">VaultDoor4.java</a>
><br><br>
>**HINT1:** Use a search engine to find an "ASCII table".<br>
>**HINT2:** You will also need to know the difference between octal, decimal, and hexadecimal numbers.

### Solution 
<p>Reading the comments in the source code gives us another hint. The flag has just been converted into different bases. Lucky for us, we it's easy to use python to convert from any base back into ASCII. I modified a basic python script from an <a href="https://raw.githubusercontent.com/QPalmer/Pico-Gym-Write-Ups/master/general_skills/based">eariler challenge</a> to reverse the flag back into ascii</p>

</p>Looking at line 32 of VaultDoor.java we can see the flag has just been converted into separate bases one letter at time</p>

```java
    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
```

<p>I wrote a python script to convert each line based on its base, join, and print the flag</p>

```python
# arrange 'my_bytes' into lists based on base

flag_decimal = [106 , 85  , 53  , 116 , 95  , 52  , 95  , 98] 
flag_hex = [55, "6e", 43, 68, "5f", 30, 66, "5f"]
flag_octal = [142, 131, 164, 63 , 163, 137, 70 , 146]
flag_plain = ['4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ]

# convert each list to ascii plaintext 
# join and print flag 

flag = []

def all_your_base(list, base):
    text = []
    for letter in list:

        # convert letter to string
        letter = str(letter)

        # convert to decimal using python int
        decimal = (int(letter, base))

        # convert to ascii using chr
        text.append(chr(decimal))

    #join
    converted = "".join(text)  
    flag.append(converted)

all_your_base(flag_decimal, 10)
all_your_base(flag_hex, 16)
all_your_base(flag_octal, 8)

ascii = "".join(flag_plain)
flag.append(ascii)

flag = "".join(flag)
print(f"picoCTF{{{flag}}}")
```

### Flag
:pirate_flag:`picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}`:pirate_flag:

<br>

---

<br>

# vault-door-5

* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** MARK E. HAASE 

### Description
> In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: 
> <a href="https://jupiter.challenges.picoctf.org/static/d31ce4356bdfd15d33a9af7e35ab4d0a/VaultDoor5.java"> VaultDoor5.java</a>
><br><br>
>**Hint 1:** You may find an encoder/decoder tool helpful, such as https://encoding.tools/ <br>
>**Hint 2:** Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

### Solution 
<p>The encoder tool in the hint was very helpful here. Basically, all that needed to be done was the following:</p>

1. Join the string from `VaultDoor5.java`

```Java
    public boolean checkPassword(String password) {
        String urlEncoded = urlEncode(password.getBytes());
        String base64Encoded = base64Encode(urlEncoded.getBytes());
        String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                        + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                        + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
        return base64Encoded.equals(expected);
    }
}
```

Now I have a very long ugly string that looks like this: `"JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0"`

2. Convert the string from base64 to Ascii 
3. Covert the encoded URL to plaintext

We can use our friend :chef: <a href="https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)URL_Decode()&input=SlRZekpUTXdKVFpsSlRjMkpUTXpKVGN5SlRjMEpUTXhKVFpsSlRZM0pUVm1KVFkySlRjeUpUTXdKVFprSlRWbUpUWXlKVFl4SlRNMUpUWTFKVFZtSlRNMkpUTTBKVFZtSlRZMUpUTXpKVE14SlRNMUpUTXlKVFl5SlRZMkpUTTA">CyberChef</a> for these steps! 


<p> In a previous challenge, <a href=https://github.com/benjamindpalmer/Pico-Gym-Write-Ups/tree/master/general_skills/#bases>I wrote a quick synopsis on the how and why of base64 encoding.</a> The conversion is really interesting. Like all character encoding, base 64 encoding relies on a table that assigns a letter to a numeric value. </p>

<p>URL encoding works the same way, and exists for many of the same reasons at base64 encoding. The ASCII's 127 characters work great for the english language, but characters that fall outside of it are disallowed in URLs. To support these characters, URL % percent encoding is used.</p>

</p>https://www.urlencoder.io/learn/</p>


### Flag
:pirate_flag:`picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}`:pirate_flag:

<br>

---

<br>

# vault-door-6
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** MARK E. HAASE

### Description
> This vault uses an XOR encryption scheme. The source code for this vault is here: <a href="https://jupiter.challenges.picoctf.org/static/cdb33ffba609e2521797aac66320ec65/VaultDoor6.java">VaultDoor6.java</a>

> **HINT1:** If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.

### Solution 

We have another 32 characters to decrypt here. This time it looks like they're 

```Java
    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x60, 0x37, 0x30, 0x60, 0x31, 0x36,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}
```

### Flag
:pirate_flag:``:pirate_flag:

<br>

---

<br>

# Safe Opener
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** Mubarak Mikail

### Description
> Can you open this safe? 
> I forgot the key to my safe but this <a href="https://artifacts.picoctf.net/c/83/SafeOpener.java">program</a> is supposed to help me with retrieving the lost key. Can you help me unlock my safe? 
> Put the password you recover into the picoCTF flag format like: 
> picoCTF{password}


### Solution
Downloaded and opened the <a href="https://artifacts.picoctf.net/c/83/SafeOpener.java">SafeOpener.java</a> program, and found an interesting variable called 'encodedkey'

```java
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
```


`encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";`

The 'encodedkey' variable is set to 'cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz'. This is a base64 string. I'm getting good at recognizing Base64 encoding. 

Use CyberChef to convert to plaintext 

`cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`
`pl3as3_l3t_m3_1nt0_th3_saf3`


### flag
:pirate_flag:`picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`:pirate_flag:

<br>

---

<br>

# Safe Opener 2
* **Difficulty:** Medium
* **Category:** Reverse Engineering
* **Author:** Mubarak Mikail

### Description
> What can you do with this file? 
> I forgot the key to my safe but this <a href="https://artifacts.picoctf.net/c/287/SafeOpener.class">file</a> is supposed to help me with retrieving the lost key. Can you help me unlock my safe?


### Solution
Downloaded the SafeOpener.class binary. First used `xxd` to take a look in hexidecimal. I was able to manually find part of the flag that way. 

```
00000310: 2920 6c65 6674 0c00 7d00 7401 002c 7069  ) left..}.t..,pi
00000320: 636f 4354 467b 5341 6633 5f30 7033 6e33  coCTF{SAf3_0p3n3
00000330: 7272 5f79 3075 5f73 6f6c 7633 645f 6974  rr_y0u_solv3d_it
00000340: 5f62 3432 3739 3432 627d 0c00 7e00 7f01  _b427942b}..~...
00000350: 000b 5365 7361 6d65 206f 7065 6e01 0016  ..Sesame open...
```

So the flag is there at offset `0000310`, but I wanted a more elegant solution. 

Using `grep` with `-a` tells grep to treat the binary file as text and return the pattern. 

```
$ grep -a "picoCTF" SafeOpener.class
You have  
          z{
            z| attempt(s) left
                              }t,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}
                                                                             ~
                                                                              Sesame openPassword is incorrect
```



### flag
:pirate_flag:`picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}`:pirate_flag:

<br>

---

<br>
