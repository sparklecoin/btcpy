from .setup import SYMBOL
class Constants:
    global SYMBOL
    
    m_p2pkh = bytearray(b'\x37')
    t_p2pkh = bytearray(b'\x6f')
    m_p2sh  = bytearray(b'\x75')
    t_p2sh  = bytearray(b'\xc4')
    m_wif   = 0xb7
    t_wif   = 0xef

    if SYMBOL is 'btc':
        m_p2pkh = bytearray(b'\x00')
        t_p2pkh = bytearray(b'\x6f')
        m_p2sh  = bytearray(b'\x05')
        t_p2sh  = bytearray(b'\xc4')
        m_wif   = 0x80
        t_wif   = 0xef

    _lookup = {'base58.prefixes': {'1': ('p2pkh', 'mainnet'),
                                'm': ('p2pkh', 'testnet'),
                                'n': ('p2pkh', 'testnet'),
                                '3': ('p2sh', 'mainnet'),
                                '2': ('p2sh', 'testnet')},
            'base58.raw_prefixes': {('mainnet', 'p2pkh'): m_p2pkh,
                                    ('testnet', 'p2pkh'): t_p2pkh,
                                    ('mainnet', 'p2sh'): m_p2sh,
                                    ('testnet', 'p2sh'): t_p2sh},
            'bech32.net_to_hrp': {'mainnet': 'bc',
                                    'testnet': 'tb'},
            'bech32.hrp_to_net': {'bc': 'mainnet',
                                    'tb': 'testnet'},
            'xkeys.prefixes': {'mainnet': 'x', 'testnet': 't'},
            'xpub.version': {'mainnet': b'\x04\x88\xb2\x1e', 'testnet': b'\x04\x35\x87\xcf'},
            'xprv.version': {'mainnet': b'\x04\x88\xad\xe4', 'testnet': b'\x04\x35\x83\x94'},
            'wif.prefixes': {'mainnet': m_wif, 'testnet': t_wif}}

    @staticmethod
    def get(key):
        try:
            return Constants._lookup[key]
        except KeyError:
            raise ValueError('Unknown constant: {}'.format(key))
