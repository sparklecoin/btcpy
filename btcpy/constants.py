from decimal import Decimal


class Constants(object):

    _lookup = {'base58.prefixes': {'S': ('p2pkh', 'mainnet'),
                                   't': ('p2pkh', 'testnet'),
                                   's': ('p2sh', 'mainnet'),
                                   '2': ('p2sh', 'testnet')},
               'base58.raw_prefixes': {('mainnet', 'p2pkh'): bytearray(b'\x3f'),
                                       ('testnet', 'p2pkh'): bytearray(b'\x7f'),
                                       ('mainnet', 'p2sh'): bytearray(b'\x7d'),
                                       ('testnet', 'p2sh'): bytearray(b'\xc4')},
               'bech32.net_to_hrp': {'mainnet': 'bc',
                                     'testnet': 'tb'},
               'bech32.hrp_to_net': {'bc': 'mainnet',
                                     'tb': 'testnet'},
               'xkeys.prefixes': {'mainnet': 'x', 'testnet': 't'},
               'xpub.version': {'mainnet': b'\x04\x88\xb2\x1e', 'testnet': b'\x04\x35\x87\xcf'},
               'xprv.version': {'mainnet': b'\x04\x88\xad\xe4', 'testnet': b'\x04\x35\x83\x94'},
               'wif.prefixes': {'mainnet': 0xbf, 'testnet': 0xff},
               'decimals': Decimal('1e6')
               }

    @staticmethod
    def get(key):
        try:
            return Constants._lookup[key]
        except KeyError:
            raise ValueError('Unknown constant: {}'.format(key))
