from sympy import isprime

# integers given from challenge and all 3 digit primes generated past 851 as this is the greatest number, so cycle ended
# near here
powers = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]
primeNumbers = [p for p in range(851, 1000) if isprime(p)]

# looping across 3 digit prime numbers. nested loop testing every base in range 1->p. and another nested loop that iterates
# through the given powers while keeping track of index and power of each item in ints. If 'i' equals the last index meaning its matched
#  all powers then the prime and the base are printed i.e. flag
for p in primeNumbers:
    # Test every possible base x (1 ≤ x < p)
    for x in range(1, p):
        # Compute successive powers of x modulo p
        for i, power in enumerate(powers):
            calculated_value = (x * power) % p
            if i == len(powers) - 1:
                print(f"{p} {x}")
#checks if calculated value matches the corresponding item in powers.
            elif calculated_value != powers[i + 1]:
                break

