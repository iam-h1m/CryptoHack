p = 28151
g = 2

#check if a number is a primitive root % p (g^n mod p as stated in challenge). will return
#false if equation equals 1 as primitive root generates all numbers from range before returning
#to 1. So if it equals 1 before the end of the range it means it hasnt generated
#all of the numbers from 1 to p-1. While loops uses is_primitive function until primitive
#root found starting at g (2) going up once each loop
def is_primitive(g):
    for i in range(1, p - 1):
        if pow(g, i, p) == 1:
            return False
    return True

while True:
    if is_primitive(g):
        break
    g = g + 1

print(g)