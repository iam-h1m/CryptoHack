from Crypto.PublicKey import RSA

with open("2048b-rsa-example-cert.der", "rb") as der_file:
    der_data = der_file.read()

rsa_key = RSA.importKey(der_data)

#.n will return the modulus of the rsa key
modulus = rsa_key.n

print(modulus)