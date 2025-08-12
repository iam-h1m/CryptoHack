import socket

# i found 2 strings via https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value that are different but have the same md5 hash
message1 = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa200a8284bf36e8e4b55b35f427593d849676da0d1555d8360fb5f07fea2'
message2 = '4dc968ff0ee35c209572d4777b721587d36fa7b21bdc56b74a3dc0783e7b9518afbfa202a8284bf36e8e4b55b35f427593d849676da0d1d55d8360fb5f07fea2'

#i send to message 1 and then message 2 as json documents which the server adds to the sytems.
# This system leaks the flag as message 2 collides with the first message "return {"error": f"Document system crash, leaking flag: {FLAG}"}"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

 sock.connect(('socket.cryptohack.org', 13389))
 print(sock.recv(1024).decode())

 sock.sendall(f'{{"document": "{message1}"}}'.encode())
 print(sock.recv(1024).decode())

 sock.sendall(f'{{"document": "{message2}"}}'.encode())
 print(sock.recv(1024).decode())