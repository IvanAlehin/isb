import logging
import math
import mpmath

from constants import MAX_LENGTH_BLOCK, PI, SEQUENCE_PATH, TEST_RESULTS
from file_work import json_reader, txt_writer

logging.basicConfig(level=logging.DEBUG, filemode='w')


def frequency_bitwise_test(sequence: str) -> float:
    """
    Perform the frequency bitwise test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:
        
        n = len(sequence)
        count_ones = sequence.count('1')
        count_zeroes = n - count_ones

        s = abs(count_ones - count_zeroes) / math.sqrt(n)

        p_value = math.erfc(s / math.sqrt(2))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def consecutive_bits_test(sequence: str) -> float:
    """
    Perform the same consecutive bits test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:

        size_seq = len(sequence)
        s = sequence.count('1') / size_seq
        if not (abs(s - 0.5) < (2 / math.sqrt(size_seq))):
            return 0.0
        
        v = len([i for i in range(size_seq - 1)
                   if sequence[i] != sequence[i + 1]])
        p_value = mpmath.erfc(abs(v - 2 * size_seq * s * (1 - s)) /
                           (2 * math.sqrt(2 * size_seq) * s * (1 - s)))
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


def longest_sequence_in_block_test(sequence: str) -> float:
    """
    Perform the longest run of ones in a block test and return the p-value.
    :param sequence: str binary sequence
    :return: float p-value of the test
    """
    try:

        i_seq = list(map(int, sequence))
        blocks = [i_seq[i:i + MAX_LENGTH_BLOCK] for i in range(0, len(i_seq), MAX_LENGTH_BLOCK)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_seq = 0
            temp_max = 0
            for bit in block:
                temp_max = (temp_max + 1) if bit == 1 else 0
                max_seq = max(max_seq, temp_max)
            match max_seq:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case 4 | 5 | 6 | 7 | 8:
                    v[4] += 1

        x_square = 0
        for i in range(4):
            x_square += math.pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        p_value = mpmath.gammainc(3 / 2, x_square / 2)
        return p_value
    except Exception as ex:
        logging.error(f"Error during the test execution: {ex}\n")


if __name__ == "__main__":
    sequences = json_reader(SEQUENCE_PATH)
    print(sequences)
    test_cpp = sequences["cpp"]
    test_java = sequences["java"]

    txt_writer(TEST_RESULTS, f'C++\n\nfrequency_bitwise_test: {frequency_bitwise_test(test_cpp)}\n'
                             f'consecutive_bits_test: {consecutive_bits_test(test_cpp)}\n'
                             f'longest_sequence_in_block_test: {longest_sequence_in_block_test(test_cpp)}\n\n'
                             f'Java\n\nfrequency_bitwise_test: {frequency_bitwise_test(test_java)}\n'
                             f'consecutive_bits_test: {consecutive_bits_test(test_java)}\n'
                             f'longest_sequence_in_block_test: {longest_sequence_in_block_test(test_java)}')
 