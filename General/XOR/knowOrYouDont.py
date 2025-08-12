from pwn import xor

secret = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
secretBytes = bytes.fromhex(secret)

#reverse engineer using the know flags e.g crypto{}. This gives us a key which is then xor'ed with the secret message
key = xor(secretBytes[:7], 'crypto{'.encode()) + xor(secretBytes[len(secretBytes) - 1], '}'.encode())

print(xor(secretBytes, key))