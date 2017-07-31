from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Hash import SHA
import logging


SCOPES = {'pub': ['p', 'g', 'y'], 'priv': ['x']}


def construct(pub_dict, priv_dict):
    """Construct ElGamal object key based on given components

    :components: tuple ElGamal components usually p, g, y and x. Where x is
                 the secret key and it is optional.
    :returns: Crypto.PublicKey.ElGamal.ElGamalobj

    """
    return ElGamal.construct((pub_dict['p'],
                          pub_dict['g'],
                          pub_dict['y'],
                          priv_dict['x']))


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


def encrypt(lat, lon, key):
    """TODO: Docstring for encrypt.

    :arg1: TODO
    :returns: TODO

    """
    while True:
        k = random.StrongRandom().randint(1, key.p-1)
        if GCD(k, key.p-1) == 1:
            break
    return key.encrypt(lat, k)


def decrypt(enc_lat, enc_lon, key):
    """TODO: Docstring for decrypt.

    :enc_lat: TODO
    :enc_lon: TODO
    :key: TODO
    :returns: TODO

    """
    return key.decrypt(enc_lat)
