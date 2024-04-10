import logging
import os

from collections import Counter

from constants import arr_encrypt_letters, PATHS
from file_work import json_reader, json_writer, txt_reader, txt_writer

logging.basicConfig(level=logging.INFO)


def frequency(enc_text: str) -> list[str]:
    """
    Returns list of counts of letters in descending order

    :param enc_text:
    :return:
    """
    c = Counter(enc_text)
    dict_pairs = c.most_common()

    return [tup[0] for tup in dict_pairs]


def decrypt_text(text_for_decrypt: str, arr_decrypt_letters: list[str]) -> str:
    """
    Decrypt text using frequency analysis algorithm

    :param text_for_decrypt:
    :param arr_decrypt_letters:
    :return:
    """
    arr_encrypt_text = []

    dictionary = dict(zip(arr_decrypt_letters, arr_encrypt_letters))
    for symb in text_for_decrypt:
        arr_encrypt_text.append(dictionary[symb])
    text_for_decrypt = ''.join(arr_encrypt_text)
    return text_for_decrypt


def write_result(path_decrypt: str, path_key: str, path_input: str) -> None:
    """
    Write decrypted text and keys in file
    :param path_input:
    :param path_key:
    :param path_decrypt:
    :return:
    """
    try:
        txt_writer(path_decrypt, decrypt_text(txt_reader(path_input), frequency(txt_reader(path_input))))

        keys = dict(zip(list(frequency(txt_reader(path_input))), arr_encrypt_letters))

        json_writer(path_key, keys)
    except Exception as ex:
        logging.error(f"Error in decryption or file can't be open or was not found: {ex}\n")


if __name__ == "__main__":
    paths = json_reader(PATHS)
    try:
        write_result(os.path.join(paths["folder"], paths["decrypt"]),
                     os.path.join(paths["folder"], paths["key"]), os.path.join(paths["folder"], paths["input"]))
        logging.info(f"Text successfully decrypted and saved to file")
    except Exception as ex:
        logging.error(f"Error in decryption or file can't be open or was not found: {ex}\n")
