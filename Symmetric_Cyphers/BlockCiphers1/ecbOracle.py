import requests, string
# help received with the logic here https://yidaotus.medium.com/breaking-ecb-by-prepending-your-own-message-b7b376d5efbb
url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"

# this function sends the input string to the challenge endpoints via the url above. The returned ciphertext
#is split into 16 byte blocks (AES operates with 128 bits)
def cipher_blocks(input):
    block = input.encode().hex()
    response = requests.get(url + block).json()
    ciphertext = response["ciphertext"]
    return [ciphertext[i:i + 32] for i in range(0, len(ciphertext), 32)]

# the function below finds the index for the block to be targeted. This was done using test payload to determine
# number of blocks in ciphertext as the ciphertext was split in the above function. The while loop re-iterates
# until last part of the flag is found. within this loop we add a padding as in the source code encryption via the challenge
# interaction page. block gets the ciphertext block corresponding to the padding state. The for loop guesses each
# byte of the flag adding characters from printable characters. if the newly added word doesn't change the trial
# block this means the word is correct. This is because in ECB identical plaintext blocks = identical ciphertext blocks meaning
# no change in ciphertext block has resulted in the same output
def decrypt_flag():
    flag = ""
    block_index = len(cipher_blocks("MARLONMARLONMARL")) - 1

    while "}" not in flag:
        pad = "M" * (16 * block_index - 1 - len(flag))
        block = cipher_blocks(pad)[block_index - 1]

        for char in string.printable:
            input = pad + flag + char
            trial_block = cipher_blocks(input)[block_index - 1]

            if trial_block == block:
                flag += char
                print(flag)
                break

    return flag

if __name__ == "__main__":
    flag = decrypt_flag()
    print(flag)