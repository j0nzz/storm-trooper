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


def generate(args):
    """Generate ElGamal key pair"""
    key = elgamal.key_gen()
    scopes = {'pub': ['p', 'g', 'y', 'x'], 'priv': ['x']}
    for scope, components in scopes.items():
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
    parser_key_gen.set_defaults(func=generate)
    # parse
    args = parser.parse_args()

    if args.verbose:
        config_logging()

    try:
        args.func(args)
    except:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
