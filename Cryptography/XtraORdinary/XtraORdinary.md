# Challenge 

Check out my new, never-before-seen method of encryption! I totally invented it myself. I added so many for loops that I don't even know what it does. It's extraordinarily secure!

We are also provided with two files:

1. The output text file containing the encrypted flag - 57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637

2. A python script which shows how the flag is encrypted

# Solution 

Let's first examine the *encrypt* function in the python script.

```python
def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt
```    

We observe that this function takes in the plaintext and a key and XORs the two byte arrays together. It then returns the ciphertext, the plaintext which has been encrypted by the key.

```python
random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

for random_str in random_strs:
    for i in range(randint(0, pow(2, 8))):
        for j in range(randint(0, pow(2, 6))):
            for k in range(randint(0, pow(2, 4))):
                for l in range(randint(0, pow(2, 2))):
                    for m in range(randint(0, pow(2, 0))):
                        ctxt = encrypt(ctxt, random_str) 
```
                        
In the next segment of the encryption script, we see a **BIG CHUNK** of nested for loops, and although this appears cryptic at first, all the for loops are essentially useless (an even number of XORs undoes the encryption process). Thus, we need only look at the last for loop - which tells us that each random_str is either XOR'ed with ptxt, or it is **NOT**.   

# Implementation 

```python
import sys 
from random import randint

encrypted_string = "57657535570c1e1c612b3468106a18492140662d2f5967442a2960684d28017931617b1f3637"

c = bytes.fromhex(encrypted_string)

rand_strings = [
	b"my encryption method", 
	b"is absolutely impenetrable", 
	b"and you will never", 
	b"ever",
	b"break it",
]

def repeating_key_xor(ct, key):
    repetitions = 1 + (len(ct) // len(key))
    key = key * repetitions
    key = key[:len(ct)]

    return bytes([b ^ k for b, k in zip(ct, key)])

def find_key(ctxt, key):
	ptxt = b""
	i = 0 
	for i in range(len(key)):
		ptxt += bytes([ctxt[i] ^ key[i]])
	return ptxt	

def obtain_key(ctxt, key):
	pt = b''

	for i in range(len(ctxt)):
		a = ctxt[i]
		b = key[i % len(key)]
		pt += bytes([a ^ b])

	return pt

while True:
	for rand_str in rand_strings:
		for i in range(randint(0 ,pow(2,0))):
			c = obtain_key(c, rand_str)	

	partial_flag = b"picoCTF{"

	key = find_key(c, partial_flag)

	# brute force all iterations of ciphertext to find key
	# if key.decode().isprintable():
	# 	print(key)
	# 	sys.exit()

	key = b"Africa!"

	flag = repeating_key_xor(c, key)

	if flag.startswith(b"picoCTF"):
		print(flag.decode())
		sys.exit()
```





