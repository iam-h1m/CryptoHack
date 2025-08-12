# jack11 designed with 11bir array length. n is the total amount of values (2048)
n = 2 ** 11

# setting the probability of no collision to one because trials havent started (100%)
no_collision = 1

# starting from 1 trial until probability is 75%. each trial calculates probability of collision and then checks if probability has equals or exceeded 75%
for i in range(1, n):
    collision = 1 - no_collision

    if collision >= 0.75:
        print(i)
        break

    # update the probability of no collision
    no_collision *= (1 - (i / n))