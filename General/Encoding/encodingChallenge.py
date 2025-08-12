import codecs, json
from urllib.parse import to_bytes
from pwn import *  # pip install pwntools
from Crypto.Util.number import long_to_bytes as to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#i am creating a map to each encoding type e.g. base64, hex etc... for each type i have a different function
#i use lambda so i dont have to def every decoding...
def decoding_message(encoding_type, encoding):
    decode_key = {
        "base64": lambda d: base64.b64decode(d).decode('utf-8'),
        "hex": lambda d: bytes.fromhex(d).decode('utf-8'),
        "rot13": lambda d: codecs.decode(d, 'rot_13'),
        "bigint": lambda d: to_bytes(int(d, 16)).decode('utf-8'),
        "utf-8": lambda d: ''.join(chr(b) for b in d),
    }
    return decode_key[encoding_type](encoding)

#i then use the function below to repeat until 'flag' is received which is known to be in the response carrying
#the flag from the 13377.py file.
def find_the_flag():
    received = json_recv()

    if "flag" in received:
        print(f"Flag received: {received['flag']}")
    else:
        to_send = {
            "decoded": decoding_message(received["type"], received["encoded"])
        }
        json_send(to_send)
        find_the_flag()

find_the_flag()