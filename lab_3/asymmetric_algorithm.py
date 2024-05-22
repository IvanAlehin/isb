import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

logging.basicConfig(level=logging.INFO)


class AsymmetricAlgorithm:
    """
    A class for asymmetric cryptography operations.

    This class provides methods for generating key pairs,
    encrypting and decrypting data using asymmetric encryption algorithms.

    Attributes:
        None
    """

    def __init__(self, private_key_path: str, public_key_path: str, key_size: int) -> None:
        """
        Initialize AsymmetricCryptography object with public and private key paths.

        :param private_key_path: Path to the private key file.
        :param public_key_path: Path to the public key file.
        :param key_size: The size of the RSA key in bits.
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    @staticmethod
    def generate_key(key_size: int) -> tuple:
        """
        Generate an RSA key pair.

        :return: A tuple containing the private and public keys.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key

    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize the private key and save it to a file.

        :param private_key: The private key.
        """
        try:
            with open(self.private_key_path, 'wb') as key_file:
                key_file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                         format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                         encryption_algorithm=serialization.NoEncryption()))
        except Exception as e:
            logging.error(f"Error in serializing private key - {e}")

    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """
        Serialize the public key and save it to a file.

        :param public_key: The public key.
        """
        try:
            with open(self.public_key_path, 'wb') as key_file:
                key_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                       format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as e:
            logging.error(f"Error in serializing public key - {e}")

    @staticmethod
    def encrypt_with_public_key(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        Encrypts ntext using the provided public key.

        :param public_key: The RSA public key used for encryption.
        :param text: The text to be encrypted.

        :return: The ciphertext produced by the encryption process.
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))
  