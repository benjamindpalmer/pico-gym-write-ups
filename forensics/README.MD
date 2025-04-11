<h1 align="center"> :microscope: FORENSICS :microscope:</h1>

- [Enhance](#enhance!):pirate_flag:
- [Verify](#verify) :pirate_flag:
- [Scan Surprise](#scan-surprise) :pirate_flag: 
- [extensions](#extensions) :pirate_flag:
- [Glory of the Garden](#glory-of-the-garden) :pirate_flag:


# Enhance!
* **Difficulty:** $\color{Yellow}{MEDIUM}$
* **Category:** FORENSICS
* **Author:** Author: LT 'syreal' Jones

### Description
> Download this image file and find the flag.
> * <a href="https://artifacts.picoctf.net/c/101/drawing.flag.svg">Download image file</a>

### Solution 

SVG stands for Scalable Vector Graphics, and in this challenge we want to scale the SVG file provided to see the tiny flag in the middle.  I hadn't encountered  an SVG file before, so I went down a couple of little rabbit holes and had fun editing the file a little bit. 

I was able to open the provided file in the web browser and zoom in enough to see a little black speck inside a small white circle, surrounded by a large black circle. Opening the inspector revealed what was going on. There was indeed a very small elipse element in the center of the white circle. There was also a text element that listed out letters of the flag separately. So one way to get the flag is just to look at the text element and piece the flag together manually. 

[screenshot of svg file](/forensics/assets/screenshots/svg_inspected.png)

But what if I wanted to actually zoom in on this SVG? It _is scalable_ right? It says so right in the name. I was able to do some successful web searching that pointed me to the `viewbox` element in the SVG file. The Viewbox pretty much does what it's namesake says, allows the view to set parameters around which parts of the SVG they're looking at by setting x y cooridnates for an anchorpoint and then box size in pixles width by heigh. Opening the file in a text editor, we can see the four values of the `viewbox`

[screenshot of svg viewbox](/forensics/assets/screenshots/svg_viewbox.png)

The first two values are the x y coordinates and the last two determind the height and width of the view in pixels. I had a very hard time 'moving' the viewbox into the correct position with trial and error, so I grabbed the coordinates from lines 71 and 72 that set the coordinates of the elipse element that contained the flag. Adjusting the viewbox to display the flag was still finnicky and required somem trial and error but I was able to get a nice screenshot after a minute or two once I had the right coordinates. 

[screenshot of svg displaying flag](/forensics/assets/screenshots/svg_flag.png)

Also had some fun editing other parts of the file. Changing colors of the elements, changing the text color, etc. 

[screenshot of some unnessary but fun edits to the svg file](/forensics/assets/screenshots/svg_flag_fun.png)

![Blade Runner Enchance Gif](https://i.gifer.com/9XO3.gif)


### Flag
:pirate_flag:`picoCTF{3nh4nc3d_24374675}`:pirate_flag:

<br>

---

<br>

# Verify
* **Difficulty:** Easy
* **Category:** FORENSICS
* **Author:** Jeffery John

### Description
> People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. 
> ssh -p 49657 ctf-player@rhea.picoctf.net Using the password 83dcefb7. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

> * Checksum: 467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02
> * To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

### Solution 
We have access to to files and a directory called files that contains a bunch of files. Too many to sift through manually. I used `ls` to list the files and directories in the first directory, and then used `cd` to change to the files directory. From there I used `ls -la` to list all of the files. There were a lot of files. 

![Screenshot](/forensics/assets/screenshots/verify_1.png)

The flag is somewhere in this group of files, but is encrypted. I tried running a quick grep but that doesn't work here. 

`$ grep 'picoCTF{' *` 

We ARE given the Sha256 hash though. We can return all of the sha256 sums on every file in the directry with `sha256sum *` and then grep for the checksum value provided in the challenge. We can combine these two commands with a | (pipe). 

`sha256sum * | grep 67a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02`

![Screenshot](/forensics/assets/screenshots/verify_2.png)

This returns the file that matches the sha256 value we're lookinig for! Which is `c6c8b911`. Now we just run the `decrypt.sh` script on that file to return the flag. For some reason, you have to be outside of the `files` directory to run the script. I believe it is expecting to look in a directory first (files) and then at a specific file. 

### Flag
:pirate_flag:`picoCTF{trust_but_verify_c6c8b911}`:pirate_flag:

<br>

---

<br>

# Scan Surprise
* **Difficulty:** EASY
* **Category:** GENERAL SKILLS
* **Author:** Jeffery John

### Description
> I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? You can download the challenge files here:
> <a href="https://artifacts.picoctf.net/c_atlas/2/challenge.zip">challenge.zip</a>

### Solution 
After downloading and unzipping <<a href="https://artifacts.picoctf.net/c_atlas/2/challenge.zip">challenge.zip</a>, we find a file called flag.png buried in a few other directories. It is a .png that displays a QR code. 

![PNG file that contains a QR code](/forensics/assets/images/flag.png)

Although it's entirely safe in this case, scanning random QR codes with one's phone probably isn't best practice from a security standpoint. I used this online QR code scanner https://scanqr.org/#scan to print the scanned flag. 

### Flag
:pirate_flag:`picoCTF{p33k_@_b00_b5ce2572}`:pirate_flag:

<br>

---

<br>

# extensions
* **Difficulty:** Medium
* **Category:** Forensics
* **Author:** Sanjay C/Danny

### Description
> This is a really weird text file <a href="https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt">TXT</a>? Can you find the flag?
>
> **Hint 1:** How do operating systems know what kind of file it is? (It's not just the ending!)
> 

### Solution 

Running the `file` command shows us the that the downloaded "flag.txt" is really a PNG file. 

```
$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```

We can also open the file. The .txt extension is causing my OS to treat it like a txt file. In a text editor, a 'PNG' header is visible. 

![screenshot of png file in text editor](/forensics/assets/screenshots/png_header.png)


I changed the extenstion of the .txt file to .png to see if that would get it to open as an image. It's amazing when stuff 'just works'. Basically I'm just telling my OS to 'treat this like a PNG' because a PNG is what it is. The flag is displayed on the png file.

![screenshot of png file displaying as an image](/forensics/assets/screenshots/flag_extensions.png)


### Flag
:pirate_flag:`picoCTF{now_you_know_about_extensions}`:pirate_flag:

<br>

---

<br>

# Glory of the Garden
* **Difficulty:** Easy
* **Category:** Forensics
* **Author:** Jedavis/Danny

### Description
> This <a href="https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg">garden</a>contains more than it seems.
>
> **Hint:** What is a hex editor?

### Solution

We are provided with this photo of a path winding through a green garden. 

![photo of a path winding through a green garden](/forensics/assets/images/garden.jpg)

```
$ file garden.jpg 
garden.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, baseline, precision 8, 2999x2249, components 3
```

This is definitely a jpg. Opening in a text editor was not helpful. I don't have a hex editor installed on this machine currently, and sometimes rather than install software first, I want to see what can actually be done with the tools that I currently have. After a little searching I found out there ARE ways to view binaries in different formats from the terminal. 

I ended up running `xxd garden.jpg` which printed out the file in hexidecimal and the ASCII representaton of the bytes. 

> [!TIP]
> Hex Dumps
> `xxd filename` - display file in hexidecimal
> `xxd -b filename` - display file in binary
> `od filename` - display file in octal


```
00230550: a2bb bdac 9687 98e4 d3b2 e87f ffd9 4865  ..............He
00230560: 7265 2069 7320 6120 666c 6167 2022 7069  re is a flag "pi
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3365 4264  m33ts_the_3y3eBd
00230590: 4264 3263 637d 220a                      Bd2cc}".
```

At the bottom of the hex dump, we can see the ASCII characters "Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"


### Flag
:pirate_flag:`picoCTF{more_than_m33ts_the_3y3eBdBd2cc}`:pirate_flag:

<br>

---

<br>