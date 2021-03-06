from collections import namedtuple
from decimal import Decimal


Constants = namedtuple('Constants', [
    'name',
    'base58_prefixes',
    'base58_raw_prefixes',
    'bech32_hrp',
    'bech32_net',
    'xkeys_prefix',
    'xpub_version',
    'xprv_version',
    'wif_prefix',
    'from_unit',
    'to_unit'
])


BitcoinMainnet = Constants(
    name='BitcoinMainnet',
    base58_prefixes={
        '1': 'p2pkh',
        '3': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x00'),
        'p2sh': bytearray(b'\x05'),
    },
    bech32_hrp='bc',
    bech32_net='mainnet',
    xkeys_prefix='x',
    xpub_version=b'\x04\x88\xb2\x1e',
    xprv_version=b'\x04\x88\xad\xe4',
    wif_prefix=0x80,
    from_unit=Decimal('1e-8'),
    to_unit=Decimal('1e8')
)


BitcoinTestnet = Constants(
    name='BitcoinTestnet',
    base58_prefixes={
        'm': 'p2pkh',
        'n': 'p2pkh',
        '2': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x6f'),
        'p2sh': bytearray(b'\xc4'),
    },
    bech32_hrp='tb',
    bech32_net='testnet',
    xkeys_prefix='t',
    xpub_version=b'\x04\x35\x87\xcf',
    xprv_version=b'\x04\x35\x83\x94',
    wif_prefix=0xef,
    from_unit=Decimal('1e-8'),
    to_unit=Decimal('1e8')
)


PeercoinMainnet = Constants(
    name='PeercoinMainnet',
    base58_prefixes={
        'P': 'p2pkh',
        'p': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x37'),
        'p2sh': bytearray(b'\x75'),
    },
    bech32_hrp='bc',
    bech32_net='mainnet',
    xkeys_prefix='x',
    xpub_version=b'\x04\x88\xb2\x1e',
    xprv_version=b'\x04\x88\xad\xe4',
    wif_prefix=0xb7,
    from_unit=Decimal('1e-6'),
    to_unit=Decimal('1e6')
)


PeercoinTestnet = Constants(
    name='PeercoinTestnet',
    base58_prefixes={
        'm': 'p2pkh',
        'n': 'p2pkh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x6f'),
        'p2sh': bytearray(b'\xc4'),
    },
    bech32_hrp='tb',
    bech32_net='testnet',
    xkeys_prefix='t',
    xpub_version=b'\x04\x35\x87\xcf',
    xprv_version=b'\x04\x35\x83\x94',
    wif_prefix=0xef,
    from_unit=Decimal('1e-6'),
    to_unit=Decimal('1e6')
)


SparklecoinMainnet = Constants(
    name='SparklecoinMainnet',
    base58_prefixes={
        'S': 'p2pkh',
        's': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x3f'),
        'p2sh': bytearray(b'\x7d'),
    },
    bech32_hrp='bc',
    bech32_net='mainnet',
    xkeys_prefix='x',
    xpub_version=b'\x04\x88\xb2\x1e',
    xprv_version=b'\x04\x88\xad\xe4',
    wif_prefix=0xbf,
    from_unit=Decimal('1e-6'),
    to_unit=Decimal('1e6')
)


SparklecoinTestnet = Constants(
    name='SparklecoinTestnet',
    base58_prefixes={
        't': 'p2pkh',
        '2': 'p2sh',
    },
    base58_raw_prefixes={
        'p2pkh': bytearray(b'\x7f'),
        'p2sh': bytearray(b'\xc4'),
    },
    bech32_hrp='tb',
    bech32_net='testnet',
    xkeys_prefix='t',
    xpub_version=b'\x04\x35\x87\xcf',
    xprv_version=b'\x04\x35\x83\x94',
    wif_prefix=0xff,
    from_unit=Decimal('1e-6'),
    to_unit=Decimal('1e6')
)
