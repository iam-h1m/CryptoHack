from Crypto.PublicKey import RSA

with open("privacy_enhanced_mail.pem", "r") as key_file:
    pem_data = key_file.read()

rsa_key = RSA.importKey(pem_data)

flag = rsa_key.d

print(flag)