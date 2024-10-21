import math
import random

# Function to check if a number is prime using trial division
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Pollard's Rho algorithm for integer factorization
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (pow(x, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        y = (pow(y, 2, n) + c + n) % n
        d = math.gcd(abs(x - y), n)
        if d == n:
            return pollards_rho(n)
    return d

# Main function to factorize a number
def prime_factors(n):
    factors = []
    
    # Check for small prime factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    
    # Use Pollard's Rho for larger factors
    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        factor = pollards_rho(n)
        while n % factor == 0:
            factors.append(factor)
            n //= factor
    
    return factors

# Example usage
n = 779824646737390614738439729
factors = prime_factors(n)
print(f"Prime factorization of {n}: {factors}")
