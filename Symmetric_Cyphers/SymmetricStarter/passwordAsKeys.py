from Crypto.Cipher import AES

ciphertext_hex = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
ciphertext = bytes.fromhex(ciphertext_hex)

#I hashed the words to a text file called hashed words. Was taking too long when all on one script
with open("hashed_words.txt", "r") as hashfile:
    hashed_passwords = [line.strip() for line in hashfile.readlines()]

#trying decryption with each hashed password. First convert hash to bytes. Then try decrypt
#using the hash as the AES key. From there i check if the decrypted text starts with 'crypto{
# and otherwise skips on to next word'
for hashed_password_hex in hashed_passwords:
    hashed_password_bytes = bytes.fromhex(hashed_password_hex)
    cipher = AES.new(hashed_password_bytes, AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(ciphertext)
    try:
        decrypted_text = decrypted_bytes.decode('utf-8').strip()
        if decrypted_text.startswith("crypto{"):
            print("Flag=", decrypted_text)
            break
    except UnicodeDecodeError:
        continue