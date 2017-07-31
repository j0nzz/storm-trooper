from collections import namedtuple
from stormtrooper import elgamal
from os import path
import logging
import json


class Geolocation(namedtuple('Geolocation', ['latitude', 'longitude'])):
    pass


def split_into_integers(coordinate):
    """Get individual parts of a float and transform into integers

    :coordinate: float value
    :returns: list of integers

    """
    return list(map(int, str(coordinate).split('.')))


def report(args):
    """Report a troop position for a configured server"""
    position = Geolocation(args.latitude, args.longitude)
    troops = args.troops
    logging.info(position, troops)


def encrypt(args):
    """Encrypt data using ElGamal

    :args: parsed args
    :returns: tuple with 2 items

    """
    with open(args.public_key_path, 'r', encoding='utf8') as f_pub:
        public_dict = json.load(f_pub)
    with open(args.private_key_path, 'r', encoding='utf8') as f_priv:
        private_dict = json.load(f_priv)
    key = elgamal.construct(public_dict, private_dict)
    enc_geo = elgamal.encrypt(args.latitude, args.longitude, key)
    print(enc_geo)

    print('>', elgamal.decrypt(enc_geo, enc_geo, key))


class Key(object):

    """Key args handler"""

    def generate(self, args):
        """Generate ElGamal key pair"""
        key = elgamal.key_gen()
        for scope, components in elgamal.SCOPES.items():
            component_dict = {k: getattr(key, k) for k in components}
            with open('.'.join([args.output, scope]), 'w', encoding='utf8') as of:
                json.dump(component_dict, of)


def config_logging():
    logging.basicConfig(level=logging.DEBUG)


def main():
    import argparse
    import sys

    # parse arguments
    parser = argparse.ArgumentParser(
        description='Report trooper geolocation using homomorphic encryption'
    )
    # logging
    parser.add_argument('-v', '--verbose', help='Verbose mode',
                        action='store_true')
    subparsers = parser.add_subparsers()
    # parser for "report" command
    parser_report = subparsers.add_parser('report',
                                          help='Report troop position')
    parser_report.add_argument('latitude', type=float)
    parser_report.add_argument('longitude', type=float)
    parser_report.add_argument('troops', type=int)
    parser_report.set_defaults(func=report)
    # parser for "key" command
    parser_key = subparsers.add_parser('key',
                                       help='Manage key')
    subparsers_key = parser_key.add_subparsers()
    parser_key_gen = subparsers_key.add_parser('gen',
                                               help='Generate a new key')
    parser_key_gen.add_argument('-o', '--output', default='id_elgamal')
    parser_key_gen.set_defaults(func=Key.generate)
    # parser for "encrypt" command
    parser_encrypt = subparsers.add_parser('encrypt',
                                       help='Encrypt message')
    parser_encrypt.add_argument('latitude', help='Latitude to be encrypted',
                                type=int)
    parser_encrypt.add_argument('longitude', help='Longitude to be encrypted',
                                type=int)
    parser_encrypt.add_argument('public_key_path',
                                help='ElGamal path to public key')
    parser_encrypt.add_argument('private_key_path',
                                help='ElGamal path to private key')
    parser_encrypt.set_defaults(func=encrypt)
    # parse
    args = parser.parse_args()

    if args.verbose:
        config_logging()

    #try:
    args.func(args)
    #except:
    #    parser.print_help()
    #    sys.exit(0)


if __name__ == "__main__":
    main()
