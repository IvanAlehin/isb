import logging
import os

from collections import Counter

from constants import ARR_ENCRYPTED_LETTERS, PATHS
from file_work import json_reader, json_writer, txt_reader, txt_writer

logging.basicConfig(level=logging.INFO)


def count_letter(enc_text: str) -> list[str]:
    """
    Count number of letters in input string

    :param enc_text: input encrypted text
    :return: list of letters in descending order of frequency in encrypted text
    """
    c = Counter(enc_text)
    dict_pairs = c.most_common()

    return [tup[0] for tup in dict_pairs]


def decrypt_text(text_for_decrypt: str, arr_decrypt_letters: list[str]) -> str:
    """
    Decrypt text using frequency analysis algorithm

    :param text_for_decrypt:  input encrypted text
    :param arr_decrypt_letters: list of letters in descending order of frequency in encrypted text
    :return: decrypted text using algorithm frequency analysis
    """
    arr_encrypt_text = []

    dictionary = dict(zip(arr_decrypt_letters, ARR_ENCRYPTED_LETTERS))
    for symb in text_for_decrypt:
        arr_encrypt_text.append(dictionary[symb])
    text_for_decrypt = ''.join(arr_encrypt_text)
    return text_for_decrypt


def write_result(path_decrypt: str, path_key: str, path_input: str) -> None:
    """
    Write decrypted text and keys in file
    :param path_input: path of file with input encrypted text
    :param path_key: path of file with key
    :param path_decrypt: path of file with decrypted text
    :return: None
    """
    try:
        txt_writer(path_decrypt, decrypt_text(txt_reader(path_input), count_letter(txt_reader(path_input))))

        keys = dict(zip(list(count_letter(txt_reader(path_input))), ARR_ENCRYPTED_LETTERS))

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
