import random
import math

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1+max_divisor, 2):
        if n % d == 0:
            return False
    return True

def generate_prime():
    """
    Generate prime number between 6 and 9 digits by an odd number between 6 and 9 digits.
    """
    temp_number = random.randrange(1000000, 1000000000)
    if temp_number % 2 == 0:
        temp_number += 1
    odd_number = temp_number
    return odd_number

def generate_keypair(p, q):
    """
    Generate a public/private key pair using the RSA algorithm.
    p and q are two prime numbers.
    Returns a tuple of two values: (public_key, private_key)
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")
    # Compute n = p*q
    n = p * q
    # Compute phi(m) = (p-1) * (q-1)
    phi = (p-1) * (q-1)
    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    # Compute the modular inverse of e, modulo phi
    d = pow(e, -1, phi)
    # Return public and private keys
    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)

def encrypt(public_key, plaintext):
    """
    Encrypts the plaintext using the public key.
    The plaintext must be an integer between 0 and n-1, where n is the modulus of the public key.
    Returns the ciphertext as an integer.
    """
    n, e = public_key
    if plaintext >= n:
        raise ValueError("Plaintext is too large.")
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    """
    Decrypts the ciphertext using the private key.
    Returns the plaintext as an integer.
    """
    n, d = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Generate key pair
p = 61
q = 53
public_key, private_key = generate_keypair(p, q)

# Encrypt message
plaintext = 1234
ciphertext = encrypt(public_key, plaintext)
print("Ciphertext:", ciphertext)

# Decrypt message
verifiertext = decrypt(private_key, ciphertext)
print("Verifiertext:", verifiertext)

if plaintext == verifiertext:
    print("Success!")

# Poema de Fernando Pessoa a ser decodificado:

    """
    Não sou nada.
    Nunca serei nada.
    Não posso querer ser nada.
    À parte isso, tenho em mim todos os sonhos do mundo.
    Estou hoje vencido, como se soubesse a verdade.
    Estou hoje perplexo, como quem pensou e achou e esqueceu.
    """

# Código do poema em ASCII:

    """
    23102436282430362310131037
    """

# Código do poema: 
# 23102436282430362310131037