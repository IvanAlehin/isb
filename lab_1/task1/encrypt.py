import logging
import os

from sys import argv
from constants import ALPHABET, PATHS
from file_work import json_reader, txt_reader, txt_writer, json_writer

SHIFT_NUMBER = int(argv[1])
logging.basicConfig(level=logging.INFO)


def encryption(shift: int, path: str) -> str:
    """
    Encrypt text using Caesar algorithm
    :param shift:
    :param path:
    :return:
    """

    encrypted = ""

    try:
        input_text = txt_reader(path)

        for letter in input_text:
            encrypted += ''.join((symbol for symbol, code in ALPHABET.items()
                                  if code == (ALPHABET[letter] + shift) % 33))
        return encrypted
    except Exception as ex:
        logging.error(f"Error in encryption or file can't be open or was not found: {ex}\n")


def write_result(input_text: str, shift: int, path_encrypt: str, path_key: str, path_input: str) -> None:
    """
    Write encrypted text and keyword in file
    :param input_text:
    :param shift:
    :param path_input:
    :param path_key:
    :param path_encrypt:
    :return:
    """
    try:
        txt_writer(path_encrypt, encryption(shift, path_input))
        dict_result = {key: letter for (key, letter) in zip(input_text, encryption(shift, path_input))}
        json_writer(path_key, dict_result)
    except Exception as ex:
        logging.error(f"Error in encryption or file can't be open or was not found: {ex}\n")


if __name__ == "__main__":
    paths = json_reader(PATHS)
    try:
        write_result(txt_reader(os.path.join(paths["folder"], paths["input"])), SHIFT_NUMBER,
                     os.path.join(paths["folder"], paths["encrypt"]), os.path.join(paths["folder"], paths["key"]),
                     os.path.join(paths["folder"], paths["input"]))
        logging.info(f"Text successfully encrypted and saved to file")
    except Exception as ex:
        logging.error(f"Error in encryption or file can't be open or was not found: {ex}\n")