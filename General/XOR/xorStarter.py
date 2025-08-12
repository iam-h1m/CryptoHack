from pwn import xor

label = "label"

def xor_(label):
    new_string = xor(label.encode(), 13).decode('utf-8')
    return f"crypto{{{new_string}}}"

print(xor_(label))