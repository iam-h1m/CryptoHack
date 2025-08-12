p = 29
ints = [14, 6, 11]
# checking if  a^2 ≡ x mod p is one of the integers in ints as it says in challenge 'We say that an integer x
# is a Quadratic Residue if there exists an a such that a^2 ≡ x mod p.' each residue added to
#residue array where the smallest result is then found after

def is_quadratic_residue(a, p):
    return pow(a, 2, p) in ints

residue = [a for a in range(p) if is_quadratic_residue(a, p)]

print(min(residue))