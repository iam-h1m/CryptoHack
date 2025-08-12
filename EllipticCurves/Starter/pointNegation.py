# finite field and coordinates of P given in the challenge
p = 9739  
Px, Py = 8045, 6936

# trying to combine P and Q to = 0. Px stays same for Qx. y bit though needs to be flipped and modularized.
Qx = Px
Qy = (-Py) % p

print("Q =", (Qx, Qy))