<h1 align="center"> :microscope: FORENSICS :microscope:</h1>

- [Enhance](#enhance!):pirate_flag:
- [Verify](#verify) :pirate_flag:
- [Scan Surprise](#scan-surprise) :pirate_flag: 
- [extensions](#extensions) :pirate_flag:
- [Glory of the Garden](#glory-of-the-garden) :pirate_flag:
- [information](#information) :pirate_flag:
- [CanYouSee](#canyousee) :pirate_flag:
- [Sleuthkit Intro](#sleuthkit-intro) :pirate_flag:
- [Disk, disk, sleuth!](#disk-disk-sleuth) :pirate_flag:
- [Disk, disk, sleuth! II](#disk-disk-sleuth-ii) :pirate_flag:
- [Sleuthkit Apprentice](#sleuthkit-apprentice) :pirate_flag:
- [Secret of the Polyglot](#secret-of-the-polyglot) :pirate_flag:

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

![screenshot of svg file](/forensics/assets/screenshots/svg_inspected.png)

But what if I wanted to actually zoom in on this SVG? It _is scalable_ right? It says so right in the name. I was able to do some successful web searching that pointed me to the `viewbox` element in the SVG file. The Viewbox pretty much does what it's namesake says, allows the view to set parameters around which parts of the SVG they're looking at by setting x y cooridnates for an anchorpoint and then box size in pixles width by heigh. Opening the file in a text editor, we can see the four values of the `viewbox`

![screenshot of svg viewbox](/forensics/assets/screenshots/svg_viewbox.png)

The first two values are the x y coordinates and the last two determind the height and width of the view in pixels. I had a very hard time 'moving' the viewbox into the correct position with trial and error, so I grabbed the coordinates from lines 71 and 72 that set the coordinates of the elipse element that contained the flag. Adjusting the viewbox to display the flag was still finnicky and required somem trial and error but I was able to get a nice screenshot after a minute or two once I had the right coordinates. 

![screenshot of svg displaying flag](/forensics/assets/screenshots/svg_flag.png)

Also had some fun editing other parts of the file. Changing colors of the elements, changing the text color, etc. 

![screenshot of some unnessary but fun edits to the svg file](/forensics/assets/screenshots/svg_flag_fun.png)

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
* **Category:** FORENSICS
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
> - `xxd filename` - display file in hexidecimal
> - `xxd -b filename` - display file in binary
> - `od filename` - display file in octal


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

# information
* **Difficulty:** Easy
* **Category:** Forensics
* **Author:** Susie

### Description
> Files can always be changed in a secret way. Can you find the flag? <a href="https://mercury.picoctf.net/static/b4d62f6e431dc8e563309ea8c33a06b3/cat.jpg">cat.jpg</a>

### Solution
Downloading cat.jpg gives a picture of a kitten sitting on a laptop keyboard. Very cool. 

I first opened the image in a hex editor using `xxd` from the terminal, but that didn't yield anything. I took a look at the image metadata using `exiftool` and noticed something strange about the license value. 

```
$ exiftool cat.jpg 
ExifTool Version Number         : 13.25
File Name                       : cat.jpg
Directory                       : .
File Size                       : 878 kB
File Modification Date/Time     : 2025:04:20 16:31:24-07:00
File Access Date/Time           : 2025:04:22 14:36:40-07:00
File Inode Change Date/Time     : 2025:04:22 01:15:27-07:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Current IPTC Digest             : 7a78f3d9cfb1ce42ab5a3aa30573d617
Copyright Notice                : PicoCTF
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 10.80
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
Rights                          : PicoCTF
Image Width                     : 2560
Image Height                    : 1598
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 2560x1598
Megapixels                      : 4.1
```

This looks familiar. A lot of these challenges encode the flag in Base64. I've seen Base64 encoded strings in the <a href="/general_skills/README.MD#Bases">Bases</a> and <a href="/web_exploitation/README.md#webdecode">WebDecode</a> challenges. These are getting easier to recognize. The combinations of upper and lower cased letters and numbers indicate a Base64 encoding. 

```
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

From here, I copied `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` into CyberChef's "From Base64" recipe which returned the flag. 

### flag
:pirate_flag:picoCTF{the_m3tadata_1s_modified}:pirate_flag:

<br>

---

<br>

# CanYouSee
* **Difficulty:** Easy
* **Category:** Forensics
* **Author:** Mubarak Mikail

### Description
> How about some hide and seek? 
> Download this file <a href="https://artifacts.picoctf.net/c_titan/130/unknown.zip">here</a>. 


### Solution
Hide and seek is easy when the hiding spot is the same every time. Like the above challenge, there is a Base64 string hiding in the image metadata. 

I downloaded and unzipped the included file `ukn_reality.jpg` and used `exiftool` to view the image metadata. 

```
$ exiftool ukn_reality.jpg 
ExifTool Version Number         : 13.25
File Name                       : ukn_reality.jpg
Directory                       : .
File Size                       : 2.3 MB
File Modification Date/Time     : 2024:03:11 17:05:55-07:00
File Access Date/Time           : 2025:04:27 15:17:19-07:00
File Inode Change Date/Time     : 2025:04:27 15:11:39-07:00
File Permissions                : -rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
XMP Toolkit                     : Image::ExifTool 11.88
Attribution URL                 : cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==
Image Width                     : 4308
Image Height                    : 2875
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4308x2875
Megapixels                      : 12.4
```

These Base64 strings are *really* starting to pop out at me now, especially since `cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==` doesn't look like an 'Attribution URL'. I copied the Base64 string into Cyberchef to decode from Base64. 

Base64: `cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==`
Plaintext: `picoCTF{ME74D47A_HIDD3N_6a9f5ac4}`


### flag
:pirate_flag:`picoCTF{ME74D47A_HIDD3N_6a9f5ac4}`:pirate_flag:

<br>

---

<br>

# Sleuthkit Intro
* **Difficulty:** Medium
* **Category:** Forensics
* **Author:** LT 'syreal' Jones

### Description
> Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory. 
> <a href="https://artifacts.picoctf.net/c/164/disk.img.gz">Download disk image</a>
> Access checker program: nc saturn.picoctf.net 51212

### Solution

I downloaded and unzipped the linked disk image after installing Sleuthkit. I opted to start with the non-gui version of Sleuthkit for now, and we'll see how far that gets me. It worked fine for this challenge, but based on what I'm reading about 'autopsy' (the GUI for Sleuthkit) it's probably worth using moving forward. 

`mmls` is a sleuthkit tool that runs on the MultiMedia layer of the disk image. This tool prints out the partition table, which will be helpful to finding the size of the linux partition. 

```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```

The Linux partition has a Lenght of 202752 sectors. Connecting with net cat and answering the question gives us the flag. 

```
$ nc saturn.picoctf.net 59875
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```


### flag
:pirate_flag:picoCTF{mm15_f7w!}:pirate_flag:

<br>

---

<br>

# Disk, disk, sleuth!
* **Difficulty:** Medium
* **Category:** Forensics
* **Author:** Syreal

### Description
> Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: <a href="https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz">dds1-alpine.flag.img.gz</a>

### Solution

After downloading and uncompressing the disk image `dds1-alpine.flag.img.gz`, I did as instructed and used the Sleuthkit tool `srch_strings`. 

According to this wiki of Sleuthkit commands https://wiki.sleuthkit.org/index.php?title=The_Sleuth_Kit_commands, `srch_strings` does exactly what I thought it did. It finds printable strings in files. 

However, running `srch_strings` returns **all** of the strings. So many. Like thousands probably. I didn't count theme all. There were too many. To get around this, I justed piped the result of `srch_strings` to a `grep` on "picoCTF". It took a few seconds to actually complete, but this worked to print just the flag. 

```
$ srch_strings dds1-alpine.flag.img | grep "picoCTF"
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}
```

### flag
:pirate_flag:picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}:pirate_flag:

<br>

---

<br>

# Disk, disk, sleuth! II
* **Difficulty:** Medium
* **Category:** Forensics
* **Author:** Syreal

### Description
> All we know is the file with the flag is named `down-at-the-bottom.txt`... 
> Disk image: <a href="https://mercury.picoctf.net/static/6cd5ca45d75250451931cea538fb38c0/dds2-alpine.flag.img.gz">dds2-alpine.flag.img.gz</a>

> **HINT:** Sleuthkit docs here are so helpful: <a href=https://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview>TSK Tool Overview</a>

### Solution

Alright, no more hand-holding with this one. We're given a file name a link to some Sleuthkit Documentation in a hint. 

https://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview

`fls` popped out at me right away as a contender for useful tools in this challenge. The file-system layer seemed like a good place to start looking for a file, and `fls` "lists allocated and deleted file names" which seemed like a great place to start. However, I kept getting 'cannot determine file system type' when using this and other commands. 

```
$ fls dds2-alpine.flag.img
Cannot determine file system type
```

This was happening because there are a few different partitions in the image, and I needed to tell fls which partition to look in. We can do this with `-o` for 'imgoffset'. 

I ran `mmls` to determine where I should be telling `fls` to look. It looks like our Linux partition starts at sector 2048. 

```
$ mmls dds2-alpine.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

Knowing this, I was able to run `fls` with an offset argument which allowed me to see a list of directories. After some trial and error, I also passed `-r` to make fls recursive. 


```
$ fls -r -o 2048 dds2-alpine.flag.img
```

This returned a lot of (too much) stuff, but we're probably getting somewhere. Piping all of this to a grep for the file name 'bottom-of-the-page.txt' to the end of this `fls` command hopefully gets us somewhere. 

```
$ fls -r -o 2048 dds2-alpine.flag.img | grep "down-at-the-bottom.txt"
+ r/r 18291:	down-at-the-bottom.txt
```

This did get us somewhere. We have found the file that contains the flag and we know the inode number. In the Sleuthkit documentation, I remember seeing a command that let's us `cat` out a file if we know the inode number. 

```
ICAT(1)                                                                                                                           General Commands Manual                                                                                                                          ICAT(1)

NAME
       icat - Output the contents of a file based on its inode number.

SYNOPSIS
       icat [-hrsvV] [-f fstype ] [-i imgtype ] [-o imgoffset ] [-b dev_sector_size] image [images] inode
```

Now we just have to `icat` on the `dds2-alpine.flag.img` image starting in sector 2048 for inode number 18291. 

```
$ icat -o 2048 dds2-alpine.flag.img 18291
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
   _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( 3 ) ( _ ) ( f ) ( f ) ( 2 ) ( 7 ) ( f ) ( 1 ) ( 3 ) ( 9 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
```


### flag
:pirate_flag:`picoCTF{f0r3ns1c4t0r_n0v1c3_ff27f139}`:pirate_flag:

<br>

---

<br>

# Sleuthkit Apprentice
* **Difficulty:** Medium
* **Category:** Forensics
* **Author:** LT 'syreal' Jones

### Description
> Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

> - <a href="https://artifacts.picoctf.net/c/137/disk.flag.img.gz">Download compressed disk image</a>



### Solution

No hints or file names or Sleuthkit tools to try this time. We're on our own. After downloading and uncompressing the disk image, I ran `mmls` to look at the partition table. 

```
$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)
```

We have some more partitions this time. I did a quick `fls` at each offset to take glance. The second linux partition that starts at `360448` looked the most promising. 

```
 fls -o 360448 disk.flag.img 
d/d 451:	home
d/d 11:	lost+found
d/d 12:	boot
d/d 1985:	etc
d/d 1986:	proc
d/d 1987:	dev
d/d 1988:	tmp
d/d 1989:	lib
d/d 1990:	var
d/d 3969:	usr
d/d 3970:	bin
d/d 1991:	sbin
d/d 1992:	media
d/d 1993:	mnt
d/d 1994:	opt
d/d 1995:	root
d/d 1996:	run
d/d 1997:	srv
d/d 1998:	sys
d/d 2358:	swap
V/V 31745:	$OrphanFiles
```

I didn't feel like looking in each of these directories manually. So I decided to use our recursive `fls` piped to a `grep` for "flag" to see if that could narrow down the search a little. I figured I might ass well check all partitions this way. 

```
$ fls -r -o 2048 disk.flag.img | grep "flag"
$
```

Nothing in the first `Linux (0x83P)` partition... 

```
$ fls -r -o 360448 disk.flag.img | grep "flag"
++ r/r * 2082(realloc):	flag.txt
++ r/r 2371:	flag.uni.txt
```

But we have a hit in the second partition that starts in sector 360448. There is a 'flag.txt' and a 'flag.uni.txt'. I was unable to `icat` the 'flag.txt'. My understanding is that a 'realloc' means the file might have been moved or deleted. 

I was able to successfully use the icat tool to open 'flag.uni.text' by passing the inode number `2371`. 

```
$ icat -o 360448 disk.flag.img 2371
picoCTF{by73_5urf3r_adac6cb4}
```

### flag
:pirate_flag:`picoCTF{by73_5urf3r_adac6cb4}`:pirate_flag:

<br>

---

<br>

# Secret of the Polyglot
* **Difficulty:** Easy
* **Category:** Forensics
* **Author:** Syreal

### Description
> The Network Operations Center (NOC) of your local institution picked up a suspicious file, they're getting conflicting information on what type of file it is. They've brought you in as an external expert to examine the file. Can you extract all the information from this strange file? 
> Download the suspicious file <a href="https://artifacts.picoctf.net/c_titan/98/flag2of2-final.pdf">here</a>. 


### Solution

In this challenge, I downloaded the provided file named `'flag2of2-final.pdf'`. This file has a PDF extension. I was able to open in on my machine's PDF reader and see what looks like the second half of a flag. 

![Screenshot of PDF reader which displays part of a flag](/forensics/assets/screenshots/polyglot_1.png)

Next, I took a look at the file with the `xxd` hex reader and noticed the PNG file signature (`89 50 4E 47 0D 0A 1A 0A`)

```
$ xxd flag2of2-final.pdf 
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 0032 0000 0032 0806 0000 001e 3f88  ...2...2......?.
00000020: b100 0001 8569 4343 5049 4343 2070 726f  .....iCCPICC pro
00000030: 6669 6c65 0000 2891 7d91 3d48 c340 1cc5  file..(.}.=H.@..
00000040: 5f53 a5a2 1511 3b88 0866 a80e 6241 54c4  _S....;..f..bAT.
00000050: 51ab 5084 0aa1 5668 d5c1 e4d2 2f68 d290  Q.P...Vh..../h..
00000060: a4b8 380a ae05 073f 16ab 0e2e ceba 3ab8  ..8....?......:.
00000070: 0a82 e007 88ab 8b93 a28b 94f8 bfa4 d022  ..............."
```

This is curious, because I was able to open this as a PDF. I changed the file extension to `.png` and opened `'flag2of2-final.png'` and was able to the native photos app. This displayed(albeit in very low resolution) the first half of the flag. 

![screenshot of photo containing low res text of flag](/forensics/assets/screenshots/polyglot_2.png)

What's happening here? This file is BOTH a PNG and a PDF. Depending on which applications read it, the 'code' of the file is interpreted differently. With my PDF reader noticing the PDF parts and the photo app (after changing the file extension) noticing the PNG parts. 

The PNG file signature is at the very top of the file. But I was curious on where the PDF signature lived. There has to be a PDF signature in the file as well, right? To check this, I piped `xxd` to `grep` and searched for PDF. 

```
$ xxd flag2of2-final.pdf | grep PDF
00000390: 6082 2550 4446 2d31 2e34 0a25 c7ec 8fa2  `.%PDF-1.4.%....
00000550: 6353 6574 5b2f 5044 4620 2f54 6578 745d  cSet[/PDF /Text]
```
Confirmed, at offset `00000390` we have a PDF file signature. 

I knew exactly what was going on here because earlier today a friend sent me this LiveOverFlow video which covers this exact concept. 
https://www.youtube.com/watch?v=VVdmmN0su6E 


### flag
:pirate_flag:`picoCTF{f1u3n7_1n_pn9_&_pdf_1f991f77}`:pirate_flag:
<br>

---

<br>



