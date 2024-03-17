from typing import Dict

from common_functions import *

INPUT_FILE = 'dec_inp.txt'
OUTPUT_FILE = 'dec_out.txt'


def read_table(table_string: str) -> dict[int, str]:
    pairs = table_string.strip().split(',')

    result = {}

    for pair in pairs:
        value, key = pair.split(':')
        key = int(key)
        result[key] = value

    return result


def find_file_data(text: str, needle: str) -> str:
    lines = text.split('\n')

    for line in lines:
        if line.strip('').startswith(needle):
            return line.lstrip(needle + ' ')

    return ''


def main() -> None:
    file_data = Path(INPUT_FILE).read_text()
    table = find_file_data(file_data, 'table')
    table = read_table(table)
    print(table)

    encrypted_data = find_file_data(file_data, 'processed')

    processed = map_to_chars(encrypted_data, table)

    shift = int(find_file_data(file_data, 'shift'))
    direction = find_file_data(file_data, 'direction')

    processed = caesar_decrypt(processed, shift, direction)

    print(processed)
    Path(OUTPUT_FILE).write_text(processed)



if __name__ == '__main__':
    main()
