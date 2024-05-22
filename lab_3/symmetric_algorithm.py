import logging
import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

logging.basicConfig(level=logging.INFO)


class SymmetricAlgorithm:
    """
    A class for symmetric cryptography operations.

    This class provides methods for generating symmetric keys,
    encrypting and decrypting data using symmetric encryption algorithms.

    Attributes:
        None
    """

    def __init__(self, key_len: int) -> None:
        """
        Initialize SymmetricCryptography object with key length.

        :param key_len: Length of the key.
        """
        self.key_len = key_len

    def generate_key(self) -> bytes:
        """
        Generate and return symmetric key.
        
        :param self: Length of the key.
        """
        return os.urandom(self.key_len // 8)

 