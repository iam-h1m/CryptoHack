p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = (p-1)*(q-1)

#e=65537, what is the private key d≡e−1modϕ(N)d≡e −1 modϕ(N) /from the challenge details
d = pow(e, -1, N)

print(d)