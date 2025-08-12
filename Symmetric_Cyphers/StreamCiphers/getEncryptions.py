import requests
# getting the encryptions and saving them to a text file to speed up the process

def getAndOrganise(num_requests=150):
    encryptions = []
    for i in range(num_requests):  
        site = "https://aes.cryptohack.org/stream_consciousness/encrypt/"
        response = requests.get(site) 
        data = response.json()  
        ciphertext = data['ciphertext'] 
        encryptions.append(ciphertext)  
        print(f"Getting Ciphers {i + 1}")

    encryptions = list(set(encryptions))
    encryptions = sorted(encryptions, key=lambda x: len(x))
    encryptions = [bytes.fromhex(ct) for ct in encryptions]

    return encryptions

encryptions = getAndOrganise()

with open("encryptions.txt", "w") as file:
    for enc in encryptions:
        file.write(enc.hex() + "\n")
    print("Encrypted data saved to encryptions.txt")