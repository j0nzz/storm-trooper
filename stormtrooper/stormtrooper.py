from collections import namedtuple


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
    print('nice', position, troops)


if __name__ == '__main__':
    import argparse

    # parse arguments
    parser = argparse.ArgumentParser(
        description='Report trooper geolocation using homomorphic encryption'
    )
    subparsers = parser.add_subparsers()
    # create the parser for the "report" command
    parser_report = subparsers.add_parser('report')
    parser_report.add_argument('latitude', type=float)
    parser_report.add_argument('longitude', type=float)
    parser_report.add_argument('troops', type=int)
    parser_report.set_defaults(func=report)
    args = parser.parse_args()
    args.func(args)
