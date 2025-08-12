import numpy as np
#using numpty  for multiplication and addition of vectors

#from challenge: v = (2,6,3), w= (1,0,0), u = (7,7,2). Calculate 3 * (2 * v - w) * 2 * u
v = np.array([2, 6, 3])
w = np.array([1, 0, 0])
u = np.array([7, 7, 2])

#splitting the equation up, (2 * v - w)
middle = 2 * v - w

# 3 * (2 * v - w)
start = 3 * middle

# 2 * u
end = 2 * u

# 3 * (2 * v - w) * 2 * u
answer = np.dot(start, end)

print(answer)