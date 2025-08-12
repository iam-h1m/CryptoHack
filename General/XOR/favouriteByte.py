from pwn import xor


secret = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
#this shows me the result of xor with all 126 ascii characters. I then look in the results for the 'crypto' flag
for i in range(126):
  print(xor(secret, i))