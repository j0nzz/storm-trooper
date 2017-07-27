import collections

class Geolocation (collections.namedtuple('Geolocation', ['lat', 'lon'])): pass

def split_into_integers(coordinate):
    """Get individual parts of a float and transform into integers

    :coordinate: float value
    :returns: list of integers

    """
    return list(map(int, str(coordinate).split('.')))
