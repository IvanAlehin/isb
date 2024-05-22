import argparse
import logging
import os

from dotenv import load_dotenv

from asymmetric_algorithm import AsymmetricAlgorithm
from symmetric_algorithm import SymmetricAlgorithm
from hybrid_system import HybridSystem
from file_work import FileWork

load_dotenv()
logging.basicConfig(level=logging.INFO)

PATHS_DEFAULT = os.environ.get('PATHS_DEFAULT')


def main():
    parser = argparse.ArgumentParser(description="Entry point of the program")
    paths_default = FileWork(PATHS_DEFAULT)
    paths_dict = paths_default.json_reader()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-generate_key', '--generation_keys',
                       action='store_true',
                       help='Run key generation mode.')

    parser.add_argument('-len', '--key_length',
                        type=int,
                        default=128,
                        help='Length of the symmetric key in bits (default: 128).')

    parser.add_argument('-text_file', '--input_text_file',
                        type=str,
                        default=paths_dict["text_file"],
                        help='Path of the input txt file with text(default: paths_dict["text_file"]')

    parser.add_argument('-public_key', '--public_key_path',
                        type=str,
                        default=paths_dict["public_key"],
                        help='Path of the public pem file with key(default: paths_dict["public_key"]')

    parser.add_argument('-private_key', '--private_key_path',
                        type=str,
                        default=paths_dict["private_key"],
                        help='Path of the private pem file with key(default: paths_dict["private_key"]')

    parser.add_argument('-symmetric_key', '--symmetric_key_path',
                        type=str,
                        default=paths_dict["symmetric_key_file"],
                        help='Path of the symmetric txt file with key(default: paths_dict["symmetric_key_file"]')

    

    try:
        args = parser.parse_args()
        if args.key_length != 128 and args.key_length != 192 and args.key_length != 256:
            raise argparse.ArgumentTypeError
        symmetric_crypto = SymmetricAlgorithm(args.key_length)
        asymmetric_crypto = AsymmetricAlgorithm(args.private_key_path, args.public_key_path, args.key_length)
        hybrid_system = HybridSystem(args.input_text_file,
                                     args.symmetric_key_path, symmetric_crypto, asymmetric_crypto)
        match args:
            case args if args.generation_keys:
                hybrid_system.generate_keys()

    except argparse.ArgumentTypeError:
        logging.error(f"Error in arguments, key_length must be equal 128 or 192 or 256 bits")


if __name__ == "__main__":
    main()
