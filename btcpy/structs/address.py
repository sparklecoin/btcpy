# Copyright (C) 2017 chainside srl
#
# This file is part of the btcpy package.
#
# It is subject to the license terms in the LICENSE.md file found in the top-level
# directory of this distribution.
#
# No part of btcpy, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE.md file.

from abc import ABCMeta, abstractmethod


class BaseAddress(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def get_codec():
        raise NotImplemented
    
    @classmethod
    def from_string(cls, string, check_network=True):
        return cls.get_codec().decode(string, check_network)

    def __str__(self):
        return self.__class__.get_codec().encode(self)


class Address(BaseAddress):

    @staticmethod
    def get_codec():
        from ..lib.codecs import Base58Codec
        return Base58Codec

    def __init__(self, addr_type, hashed_data, network):

        self.network = network
        self.type = addr_type
        self.hash = hashed_data
    
    def __eq__(self, other):
        return (self.type, self.network, self.hash) == (other.type, other.network, other.hash)


class SegWitAddress(Address):

    @staticmethod
    def get_codec():
        from ..lib.codecs import Bech32Codec
        return Bech32Codec

    def __init__(self, addr_type: str, hashed_data: bytes, version: int, network: str):
        super().__init__(addr_type, hashed_data, network)
        self.version = version

    def to_address(self):

        return Address(self.hash, self.network, addr_type='p2wpkh')

    def __eq__(self, other):
        return super().__eq__(other) and self.version == other.version
