# Plumbing
* **Points:** 100
* **Category:** General Skills
* **Challenge Year:** 2019

## Description
> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 14291
>
>

## Solution
<p>Pipes are neat-o!</p>

<p>You've probably used these when copying answers from stack overflow (I know I have) for questions like "how do I grep for such and such?". Pipes allow you to run processes on the output of another process. In this example, the program we're poing to just spits out a ridiculous amount of garbage (including the flag).</p>

```
$ nc jupiter.challenges.picoctf.org 14291
Not a flag either
This is defintely not a flag
Not a flag either
Not a flag either
I don't think this is a flag either
Again, I really don't think this is a flag
I don't think this is a flag either
...
```

<p>We want to find the flag in this sea of garbage output. A pipe will allow us to run another process on the garbage. In this case, we can just grep for the string 'picoCTF{'</p>

```
$ nc jupiter.challenges.picoctf.org 14291 | grep picoCTF{
picoCTF{digital_plumb3r_ea8bfec7}
```

:black_flag: **flag:**`picoCTF{digital_plumb3r_ea8bfec7}`