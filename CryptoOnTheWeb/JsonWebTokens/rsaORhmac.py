import jwt
from requests import get

#was able to alter the key but i had to go to algorithm.py and remove the part of the prepare key function that checks matched
# expected type. This was done after i downgraded my version of pyjwt to version 17 from 2.1
pubkey = get("https://web.cryptohack.org/rsa-or-hmac/get_pubkey/").json()["pubkey"]
token = jwt.encode({"username": "master", "admin": True}, pubkey, algorithm="HS256")
print(token)