import logging

from symmetric_algorithm import SymmetricAlgorithm
from asymmetric_algorithm import AsymmetricAlgorithm
from file_work import FileWork

logging.basicConfig(level=logging.INFO)


class HybridSystem:
    """
    A class for hybrid encryption using both symmetric and asymmetric keys.
    """

    def __init__(self, text_path: str, symmetric_key_path: str,
                 symmetric_obj: SymmetricAlgorithm, asymmetric_obj: AsymmetricAlgorithm) -> None:
        """
        Initialize HybridEncryption object with necessary paths and key length.

        :param text_path: Path to the text file.
        :param symmetric_key_path: Path to the symmetric key file.
        :param symmetric_obj: An instance of a class for working with symmetric cryptography.
        :param asymmetric_obj: An instance of a class for working with asymmetric cryptography.
        """
        self.text_path = text_path
        self.symmetric_key_path = symmetric_key_path
        self.symmetric_obj = symmetric_obj
        self.asymmetric_obj = asymmetric_obj

    def generate_keys(self) -> None:
        """
        Generate asymmetric and symmetric keys and write them to files.
        """
        try:
            symmetric_key = self.symmetric_obj.generate_key()
            private_key, public_key = self.asymmetric_obj.generate_key(2048)

            self.asymmetric_obj.serialize_private_key(private_key)
            self.asymmetric_obj.serialize_public_key(public_key)

            encrypted_symmetric_key = self.asymmetric_obj.encrypt_with_public_key(public_key, symmetric_key)
            key = FileWork(f"{self.symmetric_key_path[:-4]}_{self.symmetric_obj.key_len}_bit.txt")
            key.serializer(encrypted_symmetric_key)

            logging.info("Keys successfully generated and written to files.")
        except Exception as ex:
            logging.error(f"An error occurred while generating the keys: {ex}")
 