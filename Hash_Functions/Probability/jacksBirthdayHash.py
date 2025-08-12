# jack11 designed with 11bir array length. n is the total amount of values (2048)
n = 2 ** 11

# setting the probability of no collision to one because trials havent started (100%)
no_collision = 1

# starting from 1 trial until probability is 50%. each trial calculates probability of no collision and collision and then checks if probability has exceeded 50%
for i in range(1, n):
    no_collision *= (1 - 1 / n)

    collision = 1 - no_collision

    if collision > 0.5:
        print(i)
        break