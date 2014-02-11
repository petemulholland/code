def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_divisor = int(n ** 0.5) # square root of n
    divisor = 5
    while divisor <= max_divisor:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6
    return True

# key generation



#    Choose two distinct prime numbers p and q.
#        For security purposes, the integers p and q should be chosen at random, and should be of similar bit-length. Prime integers can be efficiently found using a primality test.
        # PM: maybe limit the size of these for testing this code
# http://en.wikipedia.org/wiki/Primality_test
# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#    Compute n = pq.
#        n is used as the modulus for both the public and private keys. Its length, usually expressed in bits, is the key length.
#    Compute ?(n) = ?(p)?(q) = (p ? 1)(q ? 1), where ? is Euler's totient function.
    # PM need to figure out Euler's totient
    # http://en.wikipedia.org/wiki/Euler%27s_totient_function
#    Choose an integer e such that 1 < e < ?(n) and gcd(e, ?(n)) = 1; i.e., e and ?(n) are coprime.
#        e is released as the public key exponent.
#        e having a short bit-length and small Hamming weight results in more efficient encryption – most commonly 216 + 1 = 65,537. However, much smaller values of e (such as 3) have been shown to be less secure in some settings.[5]
#    Determine d as d ? e?1 (mod ?(n)); i.e., d is the multiplicative inverse of e (modulo ?(n)).#

#            This is more clearly stated as: solve for d given d?e ? 1 (mod ?(n))
#            This is often computed using the extended Euclidean algorithm. Using the pseudocode in the Modular integers section, inputs a and n correspond to e and ?(n), respectively.
#            d is kept as the private key exponent.



# Encryption

# Alice transmits her public key (n, e) to Bob and keeps the private key secret. Bob then wishes to send message M to Alice.
# He first turns M into an integer m, such that 0 ? m < n by using an agreed-upon reversible protocol known as a padding scheme. He then computes the ciphertext c corresponding to
#     c\equiv m^{e}{\pmod {n}}
# This can be done quickly using the method of exponentiation by squaring. Bob then transmits c to Alice.
# http://en.wikipedia.org/wiki/Exponentiation_by_squaring
# Note that at least nine values of m will yield a ciphertext c equal to m,[note 1] but this is very unlikely to occur in practice.


# Decryption

# Alice can recover m from c by using her private key exponent d via computing
#     m\equiv c^{d}{\pmod {n}}
# Given m, she can recover the original message M by reversing the padding scheme.
# (In practice, there are more efficient methods of calculating cd using the precomputed values below.)