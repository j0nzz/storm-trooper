from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
import logging


def key_construct(components):
    """Construct ElGamal object key based on given components

    :components: tuple ElGamal components usually p, g, y and x. Where x is
                 the secret key and it is optional.
    :returns: Crypto.PublicKey.ElGamal.ElGamalobj

    """
    return ElGamal.construct(components)


def key_gen(size=1024):
    """Generate ElGamal key
    :returns: Crypto.PublicKey.ElGamal.ElGamalobj key

    """
    return ElGamal.generate(size, Random.new().read, logging.info)


def sign(plaintext, key):
    """Encrypt a message

    :plaintext: byte string or long - data to encrypt
    :key: Crypto.PublicKey.ElGamal.ElGamalobj - ElGamel object key
    :returns: A tuple with two items. Each item is of the same type as the
              plaintext (string or long)

    """
    h = SHA.new(message).digest()
    while True:
        k = random.StrongRandom().randint(1, key.p - 1)
        if GCD(k, key.p - 1) == 1:
            break
    return key.sign(h, k)
