import random
import time
import sympy
import matplotlib.pyplot as plt

def set_keys(partner, n, g):
    """
    Sets the private and public key for the given partner (Alice or Bob)

    Parameters:
    partner (dict): the partner (Alice of Bob)
    n (int): a large prime for the modulus
    g (int): the shared public information
    """

    # create a random private key for the person
    partner["private_key"] = random.randint(2, n - 2)

    # performs modular exponentiation; signature is pow(base, exponent, mod)
    partner["public_key"] = pow(g, partner["private_key"], n)

def set_shared_key(partner1, partner2_public_key, n, g):
    """
    Sets the shared secret for one partner (Alice or Bob), given only public
    information

    Parameters:
    partner1 (dict): first partner
    partner2_public_key (int): second partner's public key
    n (int): a large prime for the modulus
    g (int): the shared public information
    """
    
    # adds the shared key to each person's dictionary
    partner1["shared_secret"] = pow(partner2_public_key, partner1["private_key"], n) # g^ab

def diffie_hellmann(n, g):
    """
    Performs the diffie_hellman to create the private key.

    Parameters:
    n (int): a large prime for the modulus
    g (int): the shared public information

    Returns:
    alice (dict): the private key of alice, the public key of alice, and the shared key
    bob (dict): the private key of bob, the public key of bob, and the shared key
    """
    #print(f"Alice and Bob decide on some public parameters, n is {n}, and g is {g}")

    # create the dictionaries
    alice = {}
    bob = {}
    
    # create the private and public keys for alice and bob
    set_keys(alice, n, g) # g^a
    set_keys(bob, n, g) # g^b
    
    # create variables to later use
    alice_public = alice['public_key'] 
    bob_public = bob['public_key']
    # print(f"Alice's public key: {alice_public}")
    # print(f"Bob's public key: {bob_public}")

    # create the shared key 
    set_shared_key(alice, bob_public, n, g) # g^ab mod n
    set_shared_key(bob, alice_public, n, g) # the keys should be the same
 
    return alice, bob

def brute_force_attack(n, g, alice_public_key, bob_public_key):
    """
    Brute force attack to solve the private key of a partner

    Parameters:
    alice_public_key (int): alice's public key (known)
    bob_public_key (int): bob's public key (known)
    n (int): a large prime for the modulus (known)
    g (int): shared public information (known)

    Returns:
    shared_secret (int): the secret key g^ab mod n
    end_time - start_time (int): total time required to solve key
    """
    #  -- g^b mod p -- public bob
    start_time = time.time()
    b_private = 0

    # iterate through every possible private key
    for i in range(2, n-1):
        if pow(g, i, n) != bob_public_key:
            i += 1
        else:
            b_private = i
            break
    shared_secret = pow(alice_public_key, b_private, n)
    end_time = time.time()
    return shared_secret, end_time - start_time

# create arrays for plotting
total_time = []
x_axis = []

for i in range(5,26):
    bitlength = i
    x_axis.append(i)
    # get a random prime of bitlength i
    prime = sympy.randprime(2**(bitlength-1), 2**bitlength - 1)
    diffie_hellmann1 = diffie_hellmann(prime, 5)
    alice_public = diffie_hellmann1[0]["public_key"]
    bob_public = diffie_hellmann1[1]["public_key"]
    # perform the bruteforceattack
    brute_force = brute_force_attack(prime,5,alice_public, bob_public)
    total_time.append(brute_force[1])

    # code for the average total time over 100 iterations
    # tot_time = 0
    # for i in range(100):
    #     tot_time += brute_force_attack(prime,5,alice_public, bob_public)[1]
    # print(tot_time/100)

# plot the graph of bit length of prime vs time (seconds)   
plt.plot(x_axis, total_time)
plt.xlabel("Bit length of prime")
plt.ylabel("Time(s)")
plt.title("Time Spent During brute_force_attack vs Bit Length of Prime")
plt.show()