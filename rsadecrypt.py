"""
Author: Aaron Huang
Last Modified: 10/14/2024
Description:
    RSA Encryption and Decryption for Homework
"""
import random
import math
from math import gcd

n = 708779824646737390614738439729
def modular_multiply(a, b, mod):
    result = 0
    a = a % mod

    while b > 0:
        if b % 2 == 1:  # If b is odd, add a to result
            result = (result + a) % mod
        a = (a * 2) % mod  # Double a and reduce modulo mod
        b //= 2  # Divide b by 2

    return result

def pollards_rho(n):

    x = random.randint(2, n-1)
    y = x 
    c = random.randint(1, n-1)
    d = 1

    def f(x, n, c):
        return (modular_multiply(x,x,n)+c) % n

    while d == 1:
        x = f(x, n, c)
        y = f(f(y,n,c),n,c)
        d = gcd(abs(x-y), n)

        if d == n:
            return pollards_rho(n)

    return d    

pollards_rho(100000000)
# do I need to create code to find the prime factorization of n?
n = 689343651926443*1028195186342803 # from Wolfram Alpha
phi_n = (689343651926443-1)*(1028195186342803-1) # by definition 

e = 1292107475330115076780889

# private key
d = pow(e, -1, phi_n)

# decrypt a text file's message
with open('message.txt', 'r') as file:
    # read text by lines
    lines_c_text = file.readlines()
    for line in lines_c_text:
        message = pow(int(line), d, n)
        # convert the decrypted integers into their respective unicode characters
        print(chr(message), end = "")

# encrypt a message into numbers written on a text file
with open("encrypted.txt", 'w') as file:
    # message to encrypt
    message_back = "My name is Aaron Huang and my hometown is Andover, MA."
    for char in message_back:
        # convert back to the int representation
        unicode_message = ord(char)
        cipher_text = pow(unicode_message, e, n)
        # make the encrypted text file look like the original
        file.writelines(str(cipher_text) + '\n')
        





