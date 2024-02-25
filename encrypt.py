from common_functions import *

INPUT_FILE = 'enc_inp.txt'
OUTPUT_FILE = 'enc_out.txt'


def main():
    handle_io(INPUT_FILE, OUTPUT_FILE, caesar_encrypt)


if __name__ == '__main__':
    main()
