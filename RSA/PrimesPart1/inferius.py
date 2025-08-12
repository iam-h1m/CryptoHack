from Crypto.Util.number import long_to_bytes
#output file variables
n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

#factorized n into 2 primes using factorDB
p = 848445505077945374527983649411
q = 1160939713152385063689030212503

N = (p-1)*(q-1)
d = pow(e, -1, N)


plaintext = pow(ct, d, n)
flag = long_to_bytes(plaintext)

print(flag)