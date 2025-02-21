<h1 align="center"> :microscope: FORENSICS :microscope:</h1>

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

(svg_inspected.png)

But what if I wanted to actually zoom in on this SVG? It _is scalable_ right? It says so right in the name. I was able to do some successful web searching that pointed me to the `viewbox` element in the SVG file. The Viewbox pretty much does what it's namesake says, allows the view to set parameters around which parts of the SVG they're looking at by setting x y cooridnates for an anchorpoint and then box size in pixles width by heigh. Opening the file in a text editor, we can see the four values of the `viewbox`

(svg_viewbox.png)

The first two values are the x y coordinates and the last two determind the height and width of the view in pixels. I had a very hard time 'moving' the viewbox into the correct position with trial and error, so I grabbed the coordinates from lines 71 and 72 that set the coordinates of the elipse element that contained the flag. Adjusting the viewbox to display the flag was still finnicky and required somem trial and error but I was able to get a nice screenshot after a minute or two once I had the right coordinates. 

(svg_flag.png)

Also had some fun editing other parts of the file. Changing colors of the elements, changing the text color, etc. 

![Blade Runner Enchance Gif]()


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
> * To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.


### Solution 
We have access to to files and a directory called files that contains a bunch of files. Too many to sift through manually. I used `ls` to list the files and directories in the first directory, and then used `cd` to change to the files directory. From there I used `ls -la` to list all of the files. There were a lot of files. 

![Screenshot](verify_1.png)

The flag is somewhere in this group of files, but is encrypted. So doing somethign like

`$ grep 'picoCTF{' *` 

on the files directory won't work here. We ARE given the Sha256 hash though. We can return all of the sha256 sums on every file in the directry with `sha256sum *` and then grep for the checksum value provided in the challenge. We can combine these two commands with a |

`sha256sum * | grep 67a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02`

![Screenshot](verify_2.png)

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

![PNG file that contains a QR code](/assets/images/flag.png)

Although it's entirely safe in this case, scanning random QR codes with one's phone probably isn't best practice from a security standpoint. I used this online QR code scanner https://scanqr.org/#scan to print the scanned flag. 

### Flag
:pirate_flag:`picoCTF{p33k_@_b00_b5ce2572}`:pirate_flag:
