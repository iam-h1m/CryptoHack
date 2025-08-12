from Crypto.PublicKey import RSA

pem_file = open('transparency.pem','r')

rsa_key = RSA.import_key(pem_file.read())

#.n will return the modulus of the rsa key
#i actually found the key using crt.sh which displays certs for different web domains. I have screenshots of the answer. See directory
modulus = rsa_key.n
print(modulus)