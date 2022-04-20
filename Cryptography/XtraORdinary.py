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


