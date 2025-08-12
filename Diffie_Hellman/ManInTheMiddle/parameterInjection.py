from pwn import *
import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

#using same functions given from Deriving Symmetric Keys
def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

io = remote('socket.cryptohack.org', 13371)

alice_receive = io.recvline().strip().decode().split("e: ")[1]
alice_receive = json.loads(alice_receive)

#manipulating public keys. made (Alices Public Key ) A = g which Bob uses to make his public key making it easier to find shared secret.
#this makes each of their shared secrets the same value. B^a % p == g^(b * a) % p and A^b % p == g^(a * b) % p.
alice_bob = {
    'p': alice_receive['p'],
    'g': alice_receive['g'],
    'A': alice_receive['g']
}

io.sendline(json.dumps(alice_bob).encode())

bob_recv = io.recvline().strip().decode().split("b: ")[2]
bob_recv = json.loads(bob_recv)

bob_alice = {'B': alice_receive['g']}


io.sendline(json.dumps(bob_alice).encode())

#hex changed to int so can be entered into function as parameter
shared_secret = int(alice_receive['A'], 16)

_flag = io.recvline().strip().decode().split("e: ")[2]
_flag = json.loads(_flag)
#iv and flag pulled using parameters from source code of deriving symmetric keys
iv = _flag["iv"]
flag = _flag["encrypted_flag"]
print(decrypt_flag(shared_secret, iv, flag))
io.close()
