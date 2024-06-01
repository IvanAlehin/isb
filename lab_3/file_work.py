import json
import logging

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

logging.basicConfig(level=logging.INFO)


class FileWork:
    """
    A class containing additional functions for reading and writing files, 
    serializing and deserializing keys.

    Attributes:
        None
    """
    def __init__(self, path: str) -> None:
        """
        Initialize FileWork object with path.
        :param path: Path to file.
        """
        self.path = path

    def serializer(self, key: bytes) -> None:
        """
        Serialize the key and save it to a file.
        :param key: The key to be serialized.
        """
        try:
            with open(self.path, 'wb') as key_file:
                key_file.write(key)
        except Exception as ex:
            logging.error(f"Incorrect path - {ex}")

    def deserializer(self) -> bytes:
        """
        Deserialize the key from a file.
        :return: The deserialized key.
        """
        try:
            with open(self.path, 'rb') as key_file:
                return key_file.read()
        except Exception as ex:
            logging.error(f"Incorrect path - {ex}")

    def txt_reader(self, mode: str, encoding=None) -> str:
        """
        Read text from a file.
        :param mode: The mode to open the file in.
        :param encoding: (str, optional) The encoding of the text file. Defaults to None .

        :return: The content of the text file.
        """
        try:
            with open(self.path, mode=mode, encoding=encoding) as file:
                return file.read()
        except Exception as ex:
            logging.error(f"Incorrect path - {ex}")

    def txt_writer(self, text: str) -> None:
        """
        Write text to a file.

        :param text: The text to write to the file.
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(text)
        except Exception as ex:
            logging.error(f"Incorrect path - {ex}")

    def json_reader(self) -> dict:
        """
        Reading json file with paths and returning dict
        :return: dict with data in json file
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                paths = json.load(f)
            return paths
        except Exception as ex:
            logging.error(f"Incorrect path - {ex}")
 
    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize the private key and save it to a file.

        :param private_key: The private key.
        """
        try:
            with open(self.path, 'wb') as key_file:
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
            with open(self.path, 'wb') as key_file:
                key_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                       format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as e:
            logging.error(f"Error in serializing public key - {e}")

    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """
        Deserialize the private key and return it.

        :return: The deserialized private key.
        """
        try:
            with open(self.path, 'rb') as key_file:
                return serialization.load_pem_private_key(key_file.read(), password=None)
        except Exception as e:
            logging.error(f"Error in deserializing private key - {e}")
 