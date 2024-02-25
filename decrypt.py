from common_functions import *

INPUT_FILE = 'dec_inp.txt'
OUTPUT_FILE = 'dec_out.txt'


def main():
    handle_io(INPUT_FILE, OUTPUT_FILE, caesar_decrypt)


if __name__ == '__main__':
    main()
