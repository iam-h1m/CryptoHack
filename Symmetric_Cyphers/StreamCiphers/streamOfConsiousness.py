import requests
import json

# first thing is to get the encryptions from the api. Then remove the duplicates via the use of a set. Then sort the encryptions by length. 
# Then convert the hex to bytes. Done 150 to get a lot of encryptions to work with.
# To speed things up to remove waiting time of recieving a set of encryptions each time, I moved getAndOrganise() to a separate file (getEncryptions.py) and saved the encryptions to a text file.
# This way I can just load the encryptions from the file and work with them.

encryptions = []

with open("encryptions.txt", "r") as file:
    for line in file:
        hex_string = line.strip()
        encryption = bytes.fromhex(hex_string)
        encryptions.append(encryption)

print("Encryptions have been loaded into the variable.")

# function used to perform XOR operation on two byte sequences and return the result
def bytewiseXor(message1, message2):
    xorlen = min(len(message1), len(message2))
    result = bytearray(xorlen)
    
    for i in range(xorlen):
        result[i] = message1[i] ^ message2[i]
    
    return bytes(result)

# this function to be used to print decrypted message by applying the crib and XORing the ciphertexts at the given line/index
def printDecryptions(lineOfCipher, crib):
    for i, encryption in enumerate(encryptions):
        decrypted_message = bytewiseXor(crib, bytewiseXor(encryption, encryptions[lineOfCipher]))
        print(decryptions[i] + decrypted_message)

# function to be used to truncate the encryptions by removing the portion corresponding to the length of the given crib
def truncate_encryptions(encryptions, crib):
    for i in range(len(encryptions)):
        encryptions[i] = encryptions[i][len(crib):]
    return encryptions

# function to be used to update the decryptions list for all encryptions except the one at the given 'line' index,
def update_decryptions(line, crib, encryptions, decryptions):
    for i in range(len(encryptions)):
        if i != line:
            decryptions[i] += bytewiseXor(crib, bytewiseXor(encryptions[i], encryptions[line]))

    return decryptions


# starting with the first crib which is 'crypto{. This is from the know flag paramaeters of the flag format.
crib = b'crypto{'
print('Next crib to be used is ' + crib.decode())

# We are trying to find which encryption in the list gives readable text
# when we XOR it with all other encryptions and a known piece of text (the 'crib').

for index in range(len(encryptions)):
    all_printable = True
    for i in range(len(encryptions)):
        if not bytewiseXor(crib, bytewiseXor(encryptions[index], encryptions[i])).decode().isprintable():
            all_printable = False
            break
    
    if all_printable:
        line = i
        break
    
decryptions = [b'' for i in range(len(encryptions))]
decryptions[line] += crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

for i in decryptions:
  print(i)

# guessing the next crib. Says 'I'm unh' which im assuming is 'I'm unhappy' so lets try 'appy' and located on line 17.
crib = b'appy'
print('Next crib to be used is ' + crib.decode())
line = 17
printDecryptions(line,crib)

decryptions[line] += crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

# key appearing now is now crypto{k3y5
# next crib is 'bly' and text number 18 as 'proba' is the next word i notice.
line = 18
crib = b'bly'
print('Next crib to be used is ' + crib.decode())
printDecryptions(line, crib)

decryptions[line]+=crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

# key is now crypto{k3y57r3
# next crib is 'ning ' and text number 5. It says 'Three boys run' so im assuming 'ning' and text number 5
line = 8
crib = b'ning'
print('Next crib to be used is ' + crib.decode())
printDecryptions(line, crib)

decryptions[line] += crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

# key is now crypto{k3y57r34m_r
# next crib is 'ved '. Line 15 says 'What a lot of thin' so im assuming 'king' and located on line 15
line=15
crib=b'ved '
print('Next crib to be used is ' + crib.decode())
printDecryptions(line, crib)

decryptions[line] += crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

# key is now crypto{k3y57r34m_r3u53
# next crib is 'rything '. Line 21 says 'I shall, I'll lose eve' so im assuming 'rything' in line 21
crib=b'rything '
print('Next crib to be used is ' + crib.decode())
line = 13
printDecryptions(line,crib)

decryptions[line] += crib
decryptions = update_decryptions(line,crib,encryptions,decryptions)
encryptions = truncate_encryptions(encryptions,crib)

# at this point the key is crypto{k3y57r34m_r3u53_15_f474. The obvious end would be f474l}. So before i cribbed again i tried that flag
# into cryptohack, i.e. crypto{k3y57r34m_r3u53_15_f474l}, and it was correct. 