import random
import math

def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

def generate_prime():
    """
    Generate prime number between 6 and 9 digits by an odd number between 6 and 9 digits.
    """

    list_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    repeat_bool = False

    while repeat_bool == False:
        # Guess an odd number (except last digit 5) between 6 and 9 digits
        guess = random.randrange(1000000, 1000000000)
        if guess % 2 == 0:
            guess += 1
        if guess % 5 == 0:
            guess += 2
        
        repeat_bool = True

        # Write guess-1 as 2^r * d
        d = guess - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        for prime_num in list_primes:
            x = pow(prime_num, d, guess)
            if x == 1 or x == guess - 1:
                continue
            for idx in range(r - 1):
                x = pow(x, 2, guess)
                if x == guess - 1:
                    break
            else:
                repeat_bool = False
                continue
    return guess

def generate_keypair(p, q):
    """
    Generate a public/private key pair using the RSA algorithm.
    p and q are two prime numbers.
    Returns a tuple of two values: (public_key, private_key)
    """
    n = p * q
    phi = (p-1) * (q-1)
    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = pow(e, -1, phi)

    public_key = (n, e)
    private_key = (n, d)
    return (public_key, private_key)

def pre_encrypt(s):
    base = 38  # Base of the number system
    num = 0
    for c in s:
        if c.isalpha():
            digit = ord(c.upper()) - ord('A') + 10
        elif c.isdigit():
            digit = int(c)
        elif c == ' ':
            digit = 36
        elif c == '.':
            digit = 37
        else:
            raise ValueError("Invalid character: " + c)
        num = num * base + digit
    return num

def encrypt(public_key, plaintext):
    """
    Encrypts the plaintext using the public key.
    The plaintext must be an integer between 0 and n-1, where n is the modulus of the public key.
    Returns the ciphertext as an integer.
    """
    plaintext = str(plaintext)
    n, e = public_key
    block_size = (n.bit_length() + 7) // 8 - 1 # Calculate the block size based on the size of n
    blocks = [plaintext[i:i+block_size] for i in range(0, len(plaintext), block_size)] 
    ciphertext_blocks = []
    for block in blocks:
        m = int.from_bytes(block.encode(), 'big')
        c = pow(m, e, n)
        ciphertext_blocks.append(c)
    return ciphertext_blocks

def decrypt(private_key, ciphertext_blocks):
    """
    Decrypts the ciphertext using the private key.
    Returns the plaintext as an integer.
    """
    n, d = private_key
    message_blocks = []
    for ciphertext in ciphertext_blocks:
        m = pow(ciphertext, d, n)
        message_block = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()
        message_blocks.append(message_block)
    return ''.join(message_blocks)

def checker(number):
    mapping = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
        16: 'G',
        17: 'H',
        18: 'I',
        19: 'J',
        20: 'K',
        21: 'L',
        22: 'M',
        23: 'N',
        24: 'O',
        25: 'P',
        26: 'Q',
        27: 'R',
        28: 'S',
        29: 'T',
        30: 'U',
        31: 'V',
        32: 'W',
        33: 'X',
        34: 'Y',
        35: 'Z',
        36: ' ',
        37: '.'
    }
    digits = []
    while number > 0:
        digit = number % 38
        digits.append(digit)
        number //= 38
    digits.reverse()
    return ''.join([mapping[d] for d in digits])

# Generate key pair
p = generate_prime()
q = generate_prime()
public_key, private_key = generate_keypair(p, q)

message = "NAO SOU NADA. NUNCA SEREI NADA. NAO POSSO QUERER SER NADA. A PARTE ISSO TENHO EM MIM TODOS OS SONHOS DO MUNDO. ESTOU HOJE VENCIDO COMO SE SOUBESSE A VERDADE. ESTOU HOJE PERPLEXO COMO QUEM PENSOU E ACHOU E ESQUECEU."

# Encrypt message
plaintext = pre_encrypt(message)
print("Plaintext:", plaintext)
ciphertext_blocks = encrypt(public_key, plaintext)


print("")

# Decrypt message
verifiertext = decrypt(private_key, ciphertext_blocks)
print("Verifiertext:", verifiertext)

print("")

verifiertext = int(verifiertext)

if plaintext == verifiertext:
    print("Success!")

    print("")

    final_message = checker(verifiertext)
    print(final_message)